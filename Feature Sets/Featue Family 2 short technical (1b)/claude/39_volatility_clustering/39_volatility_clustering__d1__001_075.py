"""volatility_clustering d1 features 001-075 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __base__076_150.py. Each feature
encodes a *different concept* in the vol-clustering / GARCH-style theme:
ARCH(1) autocorr of r², EWMA-GARCH memory regimes, vol-of-vol at multiple
timescales, AR(1) persistence of σ and |r|, GARCH long-run anchoring, range-
based clustering, vol-regime indicators, |r| long-memory, vol-entropy, mixed-
frequency vol term-structure, vol-spike-vs-baseline regime.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Where σ̂ is used inside an AR(1)/regression,
σ_t and σ_{t-1} are both observable at t so the regression is causal. Self-
contained helpers — no cross-family imports.
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


def _log_ret(close):
    return _safe_log(close).diff()


def _rolling_sigma(r, n):
    return r.rolling(n, min_periods=max(n // 3, 2)).std()


def _ewma_vol(r, lam):
    """RiskMetrics-style EWMA sigma using decay λ → α = 1−λ."""
    return np.sqrt((r ** 2).ewm(alpha=1.0 - lam, min_periods=21).mean())


# ============================================================
# Bucket A — ARCH(1)-style autocorr of squared returns (001-008)
# ============================================================

def f39_vclu_001_autocorr_rsq_lag1_21d(close: pd.Series) -> pd.Series:
    """Rolling 21d corr(r²_t, r²_{t-1}) — short-horizon ARCH(1) effect."""
    r2 = _log_ret(close) ** 2
    return r2.rolling(MDAYS, min_periods=WDAYS).corr(r2.shift(1))


def f39_vclu_002_autocorr_rsq_lag1_63d(close: pd.Series) -> pd.Series:
    """Rolling 63d corr(r²_t, r²_{t-1}) — intermediate ARCH(1) effect."""
    r2 = _log_ret(close) ** 2
    return r2.rolling(QDAYS, min_periods=MDAYS).corr(r2.shift(1))


def f39_vclu_003_autocorr_rsq_lag1_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d corr(r²_t, r²_{t-1}) — annual ARCH(1) effect."""
    r2 = _log_ret(close) ** 2
    return r2.rolling(YDAYS, min_periods=QDAYS).corr(r2.shift(1))


def f39_vclu_004_autocorr_rsq_lag2_63d(close: pd.Series) -> pd.Series:
    """Rolling 63d corr(r²_t, r²_{t-2}) — short-decay clustering check."""
    r2 = _log_ret(close) ** 2
    return r2.rolling(QDAYS, min_periods=MDAYS).corr(r2.shift(2))


def f39_vclu_005_autocorr_rsq_lag5_63d(close: pd.Series) -> pd.Series:
    """Rolling 63d corr(r²_t, r²_{t-5}) — weekly-lag clustering."""
    r2 = _log_ret(close) ** 2
    return r2.rolling(QDAYS, min_periods=MDAYS).corr(r2.shift(WDAYS))


def f39_vclu_006_autocorr_rsq_lag21_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d corr(r²_t, r²_{t-21}) — monthly-lag long-memory clustering."""
    r2 = _log_ret(close) ** 2
    return r2.rolling(YDAYS, min_periods=QDAYS).corr(r2.shift(MDAYS))


def f39_vclu_007_ljung_box_rsq_lags5_63d(close: pd.Series) -> pd.Series:
    """Rolling 63d Ljung-Box-on-r² statistic summed over lags 1..5."""
    r2 = _log_ret(close) ** 2
    out = pd.Series(0.0, index=close.index)
    for k in range(1, WDAYS + 1):
        c = r2.rolling(QDAYS, min_periods=MDAYS).corr(r2.shift(k))
        out = out + (c ** 2) / (QDAYS - k)
    return QDAYS * (QDAYS + 2) * out


def f39_vclu_008_ljung_box_rsq_lags10_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d Ljung-Box-on-r² statistic summed over lags 1..10."""
    r2 = _log_ret(close) ** 2
    out = pd.Series(0.0, index=close.index)
    for k in range(1, 11):
        c = r2.rolling(YDAYS, min_periods=QDAYS).corr(r2.shift(k))
        out = out + (c ** 2) / (YDAYS - k)
    return YDAYS * (YDAYS + 2) * out


# ============================================================
# Bucket B — GARCH(1,1) proxies via EWMA volatility (009-016)
# ============================================================

def f39_vclu_009_ewma_vol_lambda094(close: pd.Series) -> pd.Series:
    """RiskMetrics EWMA σ with λ=0.94 (≈ short-memory ~25-day half-life)."""
    return _ewma_vol(_log_ret(close), 0.94)


def f39_vclu_010_ewma_vol_lambda097(close: pd.Series) -> pd.Series:
    """RiskMetrics EWMA σ with λ=0.97 (medium-memory ~50-day half-life)."""
    return _ewma_vol(_log_ret(close), 0.97)


def f39_vclu_011_ewma_vol_lambda099(close: pd.Series) -> pd.Series:
    """RiskMetrics EWMA σ with λ=0.99 (long-memory ~150-day half-life)."""
    return _ewma_vol(_log_ret(close), 0.99)


def f39_vclu_012_ewma_fast_minus_slow_vol(close: pd.Series) -> pd.Series:
    """Fast-vs-slow regime: EWMA σ(0.94) − EWMA σ(0.99) — regime-shift detector."""
    r = _log_ret(close)
    return _ewma_vol(r, 0.94) - _ewma_vol(r, 0.99)


def f39_vclu_013_ewma_fast_over_slow_vol_ratio(close: pd.Series) -> pd.Series:
    """Regime ratio: EWMA σ(0.94) / EWMA σ(0.99)."""
    r = _log_ret(close)
    return _safe_div(_ewma_vol(r, 0.94), _ewma_vol(r, 0.99))


def f39_vclu_014_log_ewma_fast_minus_log_slow(close: pd.Series) -> pd.Series:
    """log(EWMA σ_fast) − log(EWMA σ_slow): log-scale regime delta."""
    r = _log_ret(close)
    return _safe_log(_ewma_vol(r, 0.94)) - _safe_log(_ewma_vol(r, 0.99))


def f39_vclu_015_ewma_fast_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of EWMA σ(0.94) within own past 252d → vol-regime anomaly."""
    return _rolling_zscore(_ewma_vol(_log_ret(close), 0.94), YDAYS)


def f39_vclu_016_ewma_fast_anchor_deviation_252d(close: pd.Series) -> pd.Series:
    """Vol anchoring: |EWMA σ(0.94) − rolling 252d mean of EWMA σ(0.94)|."""
    e = _ewma_vol(_log_ret(close), 0.94)
    return (e - e.rolling(YDAYS, min_periods=QDAYS).mean()).abs()


# ============================================================
# Bucket C — Vol-of-vol at multiple horizons (017-026)
# ============================================================

def f39_vclu_017_vol_of_sigma21_63d(close: pd.Series) -> pd.Series:
    """Rolling 63d std of σ_21d — short-horizon vol-of-vol."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return s.rolling(QDAYS, min_periods=MDAYS).std()


def f39_vclu_018_vol_of_sigma5_21d(close: pd.Series) -> pd.Series:
    """Rolling 21d std of σ_5d — very-short-horizon vol-of-vol."""
    s = _rolling_sigma(_log_ret(close), WDAYS)
    return s.rolling(MDAYS, min_periods=WDAYS).std()


def f39_vclu_019_vol_of_sigma63_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d std of σ_63d — long-horizon vol-of-vol."""
    s = _rolling_sigma(_log_ret(close), QDAYS)
    return s.rolling(YDAYS, min_periods=QDAYS).std()


def f39_vclu_020_vol_of_ewma_fast_63d(close: pd.Series) -> pd.Series:
    """Rolling 63d std of EWMA σ(0.94) — vol-of-vol of the fast EWMA."""
    e = _ewma_vol(_log_ret(close), 0.94)
    return e.rolling(QDAYS, min_periods=MDAYS).std()


def f39_vclu_021_log_vol_of_sigma21_21d(close: pd.Series) -> pd.Series:
    """Log of σ-of-σ_21d over 21d — log-scale short vol-of-vol."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return _safe_log(s.rolling(MDAYS, min_periods=WDAYS).std())


def f39_vclu_022_log_vol_of_sigma21_252d(close: pd.Series) -> pd.Series:
    """Log of σ-of-σ_21d over 252d — log-scale annual vol-of-vol."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return _safe_log(s.rolling(YDAYS, min_periods=QDAYS).std())


def f39_vclu_023_vol_of_vol_of_vol_63d_252d(close: pd.Series) -> pd.Series:
    """Vol of (σ-of-σ_21d, 63d) over 252d — third-order vol curvature."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    vov = s.rolling(QDAYS, min_periods=MDAYS).std()
    return vov.rolling(YDAYS, min_periods=QDAYS).std()


def f39_vclu_024_vov63_over_vov252(close: pd.Series) -> pd.Series:
    """Temporal vov regime: vol-of-vol(63d) / vol-of-vol(252d) of σ_21d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    short = s.rolling(QDAYS, min_periods=MDAYS).std()
    long_ = s.rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_div(short, long_)


def f39_vclu_025_skew_sigma21_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d skew of σ_21d → asymmetry of vol process."""
    return _rolling_sigma(_log_ret(close), MDAYS).rolling(YDAYS, min_periods=QDAYS).skew()


def f39_vclu_026_kurt_sigma21_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d kurtosis of σ_21d → tail-heaviness of vol process."""
    return _rolling_sigma(_log_ret(close), MDAYS).rolling(YDAYS, min_periods=QDAYS).kurt()


# ============================================================
# Bucket D — Vol persistence (AR(1) of σ) (027-034)
# ============================================================

def f39_vclu_027_ar1_sigma21_252d(close: pd.Series) -> pd.Series:
    """AR(1) coef of σ_21d over 252d via rolling corr(σ_t, σ_{t-1})."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return s.rolling(YDAYS, min_periods=QDAYS).corr(s.shift(1))


def f39_vclu_028_ar1_sigma5_63d(close: pd.Series) -> pd.Series:
    """AR(1) coef of σ_5d over 63d."""
    s = _rolling_sigma(_log_ret(close), WDAYS)
    return s.rolling(QDAYS, min_periods=MDAYS).corr(s.shift(1))


def f39_vclu_029_ar1_sigma63_504d(close: pd.Series) -> pd.Series:
    """AR(1) coef of σ_63d over 504d — long-horizon vol persistence."""
    s = _rolling_sigma(_log_ret(close), QDAYS)
    return s.rolling(DDAYS_2Y, min_periods=YDAYS).corr(s.shift(1))


def f39_vclu_030_ar1_absret_252d(close: pd.Series) -> pd.Series:
    """AR(1) coef of |log-ret| over 252d → long-memory absolute-returns proxy."""
    a = _log_ret(close).abs()
    return a.rolling(YDAYS, min_periods=QDAYS).corr(a.shift(1))


def f39_vclu_031_ar1_rsq_252d(close: pd.Series) -> pd.Series:
    """AR(1) coef of r² over 252d → squared-return clustering."""
    r2 = _log_ret(close) ** 2
    return r2.rolling(YDAYS, min_periods=QDAYS).corr(r2.shift(1))


def f39_vclu_032_halflife_from_ar1_sigma21_252d(close: pd.Series) -> pd.Series:
    """Half-life of vol shock implied by AR(1) coef of σ_21d (clipped 0..200)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    rho = s.rolling(YDAYS, min_periods=QDAYS).corr(s.shift(1))
    abs_rho = rho.abs().clip(upper=0.99, lower=1e-3)
    hl = -np.log(2.0) / np.log(abs_rho)
    return hl.clip(upper=200.0)


def f39_vclu_033_slope_sigma_on_lag_sigma_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d OLS slope of σ_21d on its lag-1 — explicit regression form of AR(1)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    cov = s.rolling(YDAYS, min_periods=QDAYS).cov(s.shift(1))
    var = s.shift(1).rolling(YDAYS, min_periods=QDAYS).var()
    return _safe_div(cov, var)


def f39_vclu_034_ar1_truerange_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """AR(1) coef of true-range over 252d — Parkinson-style vol persistence."""
    tr = _true_range(high, low, close)
    return tr.rolling(YDAYS, min_periods=QDAYS).corr(tr.shift(1))


# ============================================================
# Bucket E — GARCH long-run vol convergence (035-040)
# ============================================================

def f39_vclu_035_sigma21_minus_rollmean_252d(close: pd.Series) -> pd.Series:
    """Deviation from long-run vol: σ_21d − rolling 252d mean of σ_21d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return s - s.rolling(YDAYS, min_periods=QDAYS).mean()


def f39_vclu_036_sigma5_minus_rollmean_252d(close: pd.Series) -> pd.Series:
    """Deviation from long-run vol: σ_5d − rolling 252d mean of σ_5d."""
    s = _rolling_sigma(_log_ret(close), WDAYS)
    return s - s.rolling(YDAYS, min_periods=QDAYS).mean()


def f39_vclu_037_log_sigma21_over_rollmean_252d(close: pd.Series) -> pd.Series:
    """Log-anchoring deviation: log(σ_21d / rolling 252d mean σ_21d)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return _safe_log(s) - _safe_log(s.rolling(YDAYS, min_periods=QDAYS).mean())


def f39_vclu_038_deviation_zscore_sigma21_252d(close: pd.Series) -> pd.Series:
    """Z-score of σ_21d within its own past 252d distribution."""
    return _rolling_zscore(_rolling_sigma(_log_ret(close), MDAYS), YDAYS)


def f39_vclu_039_reversion_speed_sigma21_63d(close: pd.Series) -> pd.Series:
    """Reversion speed: −rolling 63d slope of Δσ_21d on level σ_21d (mean-reversion β)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    ds = s.diff()
    cov = ds.rolling(QDAYS, min_periods=MDAYS).cov(s.shift(1))
    var = s.shift(1).rolling(QDAYS, min_periods=MDAYS).var()
    return -_safe_div(cov, var)


def f39_vclu_040_frac_time_sigma21_above_mean_252d(close: pd.Series) -> pd.Series:
    """Fraction of bars where σ_21d > rolling 252d mean of σ_21d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    m = s.rolling(YDAYS, min_periods=QDAYS).mean()
    return (s > m).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


# ============================================================
# Bucket F — Range-based vol clustering (041-046)
# ============================================================

def f39_vclu_041_ar1_parkinson_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """AR(1) coef of Parkinson range-vol estimator over 252d."""
    pk = (_safe_log(high) - _safe_log(low)) ** 2 / (4.0 * np.log(2.0))
    return pk.rolling(YDAYS, min_periods=QDAYS).corr(pk.shift(1))


def f39_vclu_042_ar1_loghl_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """AR(1) coef of log(H/L) over 63d — short-horizon range-clustering."""
    hl = _safe_log(high) - _safe_log(low)
    return hl.rolling(QDAYS, min_periods=MDAYS).corr(hl.shift(1))


def f39_vclu_043_autocorr_tr_lag5_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 252d corr(TR_t, TR_{t-5}) — weekly-lag range clustering."""
    tr = _true_range(high, low, close)
    return tr.rolling(YDAYS, min_periods=QDAYS).corr(tr.shift(WDAYS))


def f39_vclu_044_autocorr_loghl_lag10_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Rolling 252d corr(log(H/L)_t, log(H/L)_{t-10})."""
    hl = _safe_log(high) - _safe_log(low)
    return hl.rolling(YDAYS, min_periods=QDAYS).corr(hl.shift(10))


def f39_vclu_045_rs_hurst_truerange_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 252d R/S Hurst exponent of true-range — long-memory of range process."""
    tr = _true_range(high, low, close).dropna()

    def _rs(w):
        x = w[~np.isnan(w)]
        n = len(x)
        if n < 30:
            return np.nan
        m = x.mean()
        y = (x - m).cumsum()
        r = y.max() - y.min()
        s = x.std()
        if s == 0:
            return np.nan
        return float(np.log(r / s) / np.log(n))
    return tr.rolling(YDAYS, min_periods=QDAYS).apply(_rs, raw=True)


def f39_vclu_046_ljung_box_tr_lags5_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63d Ljung-Box statistic on true-range, lags 1..5."""
    tr = _true_range(high, low, close)
    out = pd.Series(0.0, index=close.index)
    for k in range(1, WDAYS + 1):
        c = tr.rolling(QDAYS, min_periods=MDAYS).corr(tr.shift(k))
        out = out + (c ** 2) / (QDAYS - k)
    return QDAYS * (QDAYS + 2) * out


# ============================================================
# Bucket G — Vol-regime indicators (047-054)
# ============================================================

def f39_vclu_047_frac_time_sigma21_above_p75_252d(close: pd.Series) -> pd.Series:
    """Fraction of time σ_21d > rolling 252d 75th-pct of σ_21d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p75 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    return (s > p75).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def _bars_since_event(ind: pd.Series) -> pd.Series:
    arr = ind.fillna(0).astype(int).values
    out = np.full(len(arr), np.nan)
    bars = np.nan
    for i, x in enumerate(arr):
        if x:
            bars = 0
        elif np.isfinite(bars):
            bars = bars + 1
        out[i] = bars
    return pd.Series(out, index=ind.index)


def f39_vclu_048_bars_since_high_vol_regime(close: pd.Series) -> pd.Series:
    """Bars since σ_21d last exceeded its trailing-252d 75th percentile."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p75 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    return _bars_since_event((s > p75).astype(float))


def f39_vclu_049_bars_since_low_vol_regime(close: pd.Series) -> pd.Series:
    """Bars since σ_21d last fell below its trailing-252d 25th percentile."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p25 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    return _bars_since_event((s < p25).astype(float))


def f39_vclu_050_count_median_crossings_sigma21_63d(close: pd.Series) -> pd.Series:
    """Number of σ_21d crossings of its trailing-252d median, summed over 63d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    med = s.rolling(YDAYS, min_periods=QDAYS).median()
    above = (s > med).astype(float)
    crossings = above.diff().abs().fillna(0.0)
    return crossings.rolling(QDAYS, min_periods=MDAYS).sum()


def f39_vclu_051_longest_high_vol_run_252d(close: pd.Series) -> pd.Series:
    """Longest run of σ_21d > trailing-252d 75th-pct within 252d window."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p75 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    hi = (s > p75).astype(float).fillna(0.0)

    def _run(w):
        m = 0; c = 0
        for v in w:
            if v > 0.5:
                c += 1; m = c if c > m else m
            else:
                c = 0
        return m
    return hi.rolling(YDAYS, min_periods=QDAYS).apply(_run, raw=True)


def f39_vclu_052_longest_low_vol_run_252d(close: pd.Series) -> pd.Series:
    """Longest run of σ_21d < trailing-252d 25th-pct within 252d window."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p25 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    lo = (s < p25).astype(float).fillna(0.0)

    def _run(w):
        m = 0; c = 0
        for v in w:
            if v > 0.5:
                c += 1; m = c if c > m else m
            else:
                c = 0
        return m
    return lo.rolling(YDAYS, min_periods=QDAYS).apply(_run, raw=True)


def f39_vclu_053_time_top_decile_sigma21_252d(close: pd.Series) -> pd.Series:
    """Fraction of time σ_21d in top decile of its own past 252d distribution."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p90 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    return (s > p90).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f39_vclu_054_time_bottom_decile_sigma21_252d(close: pd.Series) -> pd.Series:
    """Fraction of time σ_21d in bottom decile of its own past 252d distribution."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p10 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.10)
    return (s < p10).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


# ============================================================
# Bucket H — |r| long-memory (Ding-Granger-Engle) (055-059)
# ============================================================

def f39_vclu_055_autocorr_absret_lag1_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d corr(|log-ret|_t, |log-ret|_{t-1})."""
    a = _log_ret(close).abs()
    return a.rolling(YDAYS, min_periods=QDAYS).corr(a.shift(1))


def f39_vclu_056_autocorr_absret_lag5_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d corr(|log-ret|_t, |log-ret|_{t-5})."""
    a = _log_ret(close).abs()
    return a.rolling(YDAYS, min_periods=QDAYS).corr(a.shift(WDAYS))


def f39_vclu_057_autocorr_absret_lag21_504d(close: pd.Series) -> pd.Series:
    """Rolling 504d corr(|log-ret|_t, |log-ret|_{t-21}) — long-memory test."""
    a = _log_ret(close).abs()
    return a.rolling(DDAYS_2Y, min_periods=YDAYS).corr(a.shift(MDAYS))


def f39_vclu_058_sum_autocorr_absret_lags1to21_252d(close: pd.Series) -> pd.Series:
    """Sum of autocorr_|r| at lags 1..21 over 252d (long-memory aggregate)."""
    a = _log_ret(close).abs()
    out = pd.Series(0.0, index=close.index)
    for k in range(1, MDAYS + 1):
        out = out + a.rolling(YDAYS, min_periods=QDAYS).corr(a.shift(k))
    return out


def f39_vclu_059_gph_loglog_slope_absret_252d(close: pd.Series) -> pd.Series:
    """GPH-style log-log slope of |autocorr_|r|(k)| vs lag k over 252d (lags 1..10)."""
    a = _log_ret(close).abs()

    def _gph(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < QDAYS:
            return np.nan
        ks = np.arange(1, 11)
        rs = []
        m = ww.mean()
        var = ((ww - m) ** 2).sum()
        if var == 0:
            return np.nan
        for k in ks:
            c = ((ww[k:] - m) * (ww[:-k] - m)).sum() / var
            rs.append(abs(c) + 1e-9)
        x = np.log(ks); y = np.log(rs)
        xm = x.mean(); ym = y.mean()
        d = ((x - xm) ** 2).sum()
        return float(((x - xm) * (y - ym)).sum() / d) if d > 0 else np.nan
    return a.rolling(YDAYS, min_periods=QDAYS).apply(_gph, raw=True)


# ============================================================
# Bucket I — Vol entropy & complexity (060-065)
# ============================================================

def f39_vclu_060_shannon_entropy_sigma21_bins_252d(close: pd.Series) -> pd.Series:
    """Shannon entropy of σ_21d binned distribution (10 bins) over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)

    def _ent(w):
        ww = w[~np.isnan(w)]
        if len(ww) < QDAYS:
            return np.nan
        h, _ = np.histogram(ww, bins=10)
        p = h.astype(float) / h.sum()
        p = p[p > 0]
        return float(-(p * np.log(p)).sum())
    return s.rolling(YDAYS, min_periods=QDAYS).apply(_ent, raw=True)


def f39_vclu_061_sample_entropy_absret_252d(close: pd.Series) -> pd.Series:
    """Sample entropy (m=2, r=0.2·std) of |log-ret| over 252d."""
    a = _log_ret(close).abs()

    def _samp(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < QDAYS:
            return np.nan
        r = 0.2 * ww.std()
        if r == 0:
            return np.nan
        m = 2

        def _phi(mm):
            xs = np.array([ww[i:i + mm] for i in range(n - mm + 1)])
            cnt = 0
            for i in range(len(xs)):
                d = np.max(np.abs(xs - xs[i]), axis=1)
                cnt += (d <= r).sum() - 1
            return cnt
        bm = _phi(m); bm1 = _phi(m + 1)
        if bm == 0 or bm1 == 0:
            return np.nan
        return float(-np.log(bm1 / bm))
    return a.rolling(YDAYS, min_periods=QDAYS).apply(_samp, raw=True)


def f39_vclu_062_approx_entropy_sigma21_252d(close: pd.Series) -> pd.Series:
    """Approximate entropy (m=2, r=0.2·std) of σ_21d over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)

    def _ap(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < QDAYS:
            return np.nan
        r = 0.2 * ww.std()
        if r == 0:
            return np.nan

        def _phi(mm):
            xs = np.array([ww[i:i + mm] for i in range(n - mm + 1)])
            c = np.zeros(len(xs))
            for i in range(len(xs)):
                d = np.max(np.abs(xs - xs[i]), axis=1)
                c[i] = (d <= r).sum() / len(xs)
            return np.mean(np.log(c[c > 0])) if (c > 0).any() else np.nan
        p1 = _phi(2); p2 = _phi(3)
        return float(p1 - p2) if np.isfinite(p1) and np.isfinite(p2) else np.nan
    return s.rolling(YDAYS, min_periods=QDAYS).apply(_ap, raw=True)


def f39_vclu_063_permutation_entropy_sigma21_252d(close: pd.Series) -> pd.Series:
    """Permutation entropy (order 3) of σ_21d over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    from math import log

    def _perm(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < QDAYS:
            return np.nan
        cnt = {}
        for i in range(n - 2):
            pat = tuple(np.argsort(ww[i:i + 3]))
            cnt[pat] = cnt.get(pat, 0) + 1
        tot = sum(cnt.values())
        ent = 0.0
        for v in cnt.values():
            p = v / tot
            ent -= p * log(p)
        return float(ent / log(6.0))
    return s.rolling(YDAYS, min_periods=QDAYS).apply(_perm, raw=True)


def f39_vclu_064_shannon_entropy_tr_bins_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Shannon entropy of TR binned distribution (10 bins) over 252d."""
    tr = _true_range(high, low, close)

    def _ent(w):
        ww = w[~np.isnan(w)]
        if len(ww) < QDAYS:
            return np.nan
        h, _ = np.histogram(ww, bins=10)
        p = h.astype(float) / h.sum()
        p = p[p > 0]
        return float(-(p * np.log(p)).sum())
    return tr.rolling(YDAYS, min_periods=QDAYS).apply(_ent, raw=True)


def f39_vclu_065_variance_ratio_sigma63_sigma21_252d(close: pd.Series) -> pd.Series:
    """Variance ratio: var(σ_63d, 252d) / var(σ_21d, 252d) — entropy/scaling proxy."""
    s21 = _rolling_sigma(_log_ret(close), MDAYS)
    s63 = _rolling_sigma(_log_ret(close), QDAYS)
    return _safe_div(s63.rolling(YDAYS, min_periods=QDAYS).var(),
                     s21.rolling(YDAYS, min_periods=QDAYS).var())


# ============================================================
# Bucket J — Mixed-frequency vol / term-structure (066-071)
# ============================================================

def f39_vclu_066_ratio_sigma5_over_sigma21(close: pd.Series) -> pd.Series:
    """Short-vs-medium term-structure slope: σ_5d / σ_21d."""
    r = _log_ret(close)
    return _safe_div(_rolling_sigma(r, WDAYS), _rolling_sigma(r, MDAYS))


def f39_vclu_067_ratio_sigma21_over_sigma63(close: pd.Series) -> pd.Series:
    """Medium-vs-intermediate term-structure slope: σ_21d / σ_63d."""
    r = _log_ret(close)
    return _safe_div(_rolling_sigma(r, MDAYS), _rolling_sigma(r, QDAYS))


def f39_vclu_068_ratio_sigma63_over_sigma252(close: pd.Series) -> pd.Series:
    """Intermediate-vs-annual term-structure slope: σ_63d / σ_252d."""
    r = _log_ret(close)
    return _safe_div(_rolling_sigma(r, QDAYS), _rolling_sigma(r, YDAYS))


def f39_vclu_069_ratio_sigma5_over_sigma252(close: pd.Series) -> pd.Series:
    """Short-vs-annual term-structure slope: σ_5d / σ_252d."""
    r = _log_ret(close)
    return _safe_div(_rolling_sigma(r, WDAYS), _rolling_sigma(r, YDAYS))


def f39_vclu_070_log_term_structure_slope_5_252(close: pd.Series) -> pd.Series:
    """Log term-structure slope: log(σ_5d / σ_252d)."""
    r = _log_ret(close)
    return _safe_log(_rolling_sigma(r, WDAYS)) - _safe_log(_rolling_sigma(r, YDAYS))


def f39_vclu_071_term_structure_curvature_4pt(close: pd.Series) -> pd.Series:
    """Term-structure curvature: σ_5 − 2σ_21 + σ_63 — 3-point second-difference of σ-horizons."""
    r = _log_ret(close)
    return _rolling_sigma(r, WDAYS) - 2 * _rolling_sigma(r, MDAYS) + _rolling_sigma(r, QDAYS)


# ============================================================
# Bucket K — Vol jump risk / cross-horizon spike (072-075)
# ============================================================

def f39_vclu_072_max_sigma5_over_sigma63_21d(close: pd.Series) -> pd.Series:
    """Max σ_5d / σ_63d ratio within trailing 21d — short-term spike-vs-baseline peak."""
    r = _log_ret(close)
    return _safe_div(_rolling_sigma(r, WDAYS), _rolling_sigma(r, QDAYS)).rolling(MDAYS, min_periods=WDAYS).max()


def f39_vclu_073_count_sigma5_above_2x_sigma63_63d(close: pd.Series) -> pd.Series:
    """Count of bars where σ_5d > 2·σ_63d within 63d — vol-spike event count."""
    r = _log_ret(close)
    spike = (_rolling_sigma(r, WDAYS) > 2 * _rolling_sigma(r, QDAYS)).astype(float)
    return spike.rolling(QDAYS, min_periods=MDAYS).sum()


def f39_vclu_074_zscore_sigma21_minus_sigma63_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d z-score of (σ_21d − σ_63d) — short-vs-intermediate anomaly."""
    r = _log_ret(close)
    return _rolling_zscore(_rolling_sigma(r, MDAYS) - _rolling_sigma(r, QDAYS), YDAYS)


def f39_vclu_075_max_sigma5_over_sigma252_21d(close: pd.Series) -> pd.Series:
    """Max σ_5d / σ_252d within trailing 21d — extreme intra-period spike."""
    r = _log_ret(close)
    return _safe_div(_rolling_sigma(r, WDAYS), _rolling_sigma(r, YDAYS)).rolling(MDAYS, min_periods=WDAYS).max()


# ============================================================
#                         REGISTRY 001-075
# ============================================================



def f39_vclu_001_autocorr_rsq_lag1_21d_d1(close):
    return f39_vclu_001_autocorr_rsq_lag1_21d(close).diff()


def f39_vclu_002_autocorr_rsq_lag1_63d_d1(close):
    return f39_vclu_002_autocorr_rsq_lag1_63d(close).diff()


def f39_vclu_003_autocorr_rsq_lag1_252d_d1(close):
    return f39_vclu_003_autocorr_rsq_lag1_252d(close).diff()


def f39_vclu_004_autocorr_rsq_lag2_63d_d1(close):
    return f39_vclu_004_autocorr_rsq_lag2_63d(close).diff()


def f39_vclu_005_autocorr_rsq_lag5_63d_d1(close):
    return f39_vclu_005_autocorr_rsq_lag5_63d(close).diff()


def f39_vclu_006_autocorr_rsq_lag21_252d_d1(close):
    return f39_vclu_006_autocorr_rsq_lag21_252d(close).diff()


def f39_vclu_007_ljung_box_rsq_lags5_63d_d1(close):
    return f39_vclu_007_ljung_box_rsq_lags5_63d(close).diff()


def f39_vclu_008_ljung_box_rsq_lags10_252d_d1(close):
    return f39_vclu_008_ljung_box_rsq_lags10_252d(close).diff()


def f39_vclu_009_ewma_vol_lambda094_d1(close):
    return f39_vclu_009_ewma_vol_lambda094(close).diff()


def f39_vclu_010_ewma_vol_lambda097_d1(close):
    return f39_vclu_010_ewma_vol_lambda097(close).diff()


def f39_vclu_011_ewma_vol_lambda099_d1(close):
    return f39_vclu_011_ewma_vol_lambda099(close).diff()


def f39_vclu_012_ewma_fast_minus_slow_vol_d1(close):
    return f39_vclu_012_ewma_fast_minus_slow_vol(close).diff()


def f39_vclu_013_ewma_fast_over_slow_vol_ratio_d1(close):
    return f39_vclu_013_ewma_fast_over_slow_vol_ratio(close).diff()


def f39_vclu_014_log_ewma_fast_minus_log_slow_d1(close):
    return f39_vclu_014_log_ewma_fast_minus_log_slow(close).diff()


def f39_vclu_015_ewma_fast_zscore_252d_d1(close):
    return f39_vclu_015_ewma_fast_zscore_252d(close).diff()


def f39_vclu_016_ewma_fast_anchor_deviation_252d_d1(close):
    return f39_vclu_016_ewma_fast_anchor_deviation_252d(close).diff()


def f39_vclu_017_vol_of_sigma21_63d_d1(close):
    return f39_vclu_017_vol_of_sigma21_63d(close).diff()


def f39_vclu_018_vol_of_sigma5_21d_d1(close):
    return f39_vclu_018_vol_of_sigma5_21d(close).diff()


def f39_vclu_019_vol_of_sigma63_252d_d1(close):
    return f39_vclu_019_vol_of_sigma63_252d(close).diff()


def f39_vclu_020_vol_of_ewma_fast_63d_d1(close):
    return f39_vclu_020_vol_of_ewma_fast_63d(close).diff()


def f39_vclu_021_log_vol_of_sigma21_21d_d1(close):
    return f39_vclu_021_log_vol_of_sigma21_21d(close).diff()


def f39_vclu_022_log_vol_of_sigma21_252d_d1(close):
    return f39_vclu_022_log_vol_of_sigma21_252d(close).diff()


def f39_vclu_023_vol_of_vol_of_vol_63d_252d_d1(close):
    return f39_vclu_023_vol_of_vol_of_vol_63d_252d(close).diff()


def f39_vclu_024_vov63_over_vov252_d1(close):
    return f39_vclu_024_vov63_over_vov252(close).diff()


def f39_vclu_025_skew_sigma21_252d_d1(close):
    return f39_vclu_025_skew_sigma21_252d(close).diff()


def f39_vclu_026_kurt_sigma21_252d_d1(close):
    return f39_vclu_026_kurt_sigma21_252d(close).diff()


def f39_vclu_027_ar1_sigma21_252d_d1(close):
    return f39_vclu_027_ar1_sigma21_252d(close).diff()


def f39_vclu_028_ar1_sigma5_63d_d1(close):
    return f39_vclu_028_ar1_sigma5_63d(close).diff()


def f39_vclu_029_ar1_sigma63_504d_d1(close):
    return f39_vclu_029_ar1_sigma63_504d(close).diff()


def f39_vclu_030_ar1_absret_252d_d1(close):
    return f39_vclu_030_ar1_absret_252d(close).diff()


def f39_vclu_031_ar1_rsq_252d_d1(close):
    return f39_vclu_031_ar1_rsq_252d(close).diff()


def f39_vclu_032_halflife_from_ar1_sigma21_252d_d1(close):
    return f39_vclu_032_halflife_from_ar1_sigma21_252d(close).diff()


def f39_vclu_033_slope_sigma_on_lag_sigma_252d_d1(close):
    return f39_vclu_033_slope_sigma_on_lag_sigma_252d(close).diff()


def f39_vclu_034_ar1_truerange_252d_d1(high, low, close):
    return f39_vclu_034_ar1_truerange_252d(high, low, close).diff()


def f39_vclu_035_sigma21_minus_rollmean_252d_d1(close):
    return f39_vclu_035_sigma21_minus_rollmean_252d(close).diff()


def f39_vclu_036_sigma5_minus_rollmean_252d_d1(close):
    return f39_vclu_036_sigma5_minus_rollmean_252d(close).diff()


def f39_vclu_037_log_sigma21_over_rollmean_252d_d1(close):
    return f39_vclu_037_log_sigma21_over_rollmean_252d(close).diff()


def f39_vclu_038_deviation_zscore_sigma21_252d_d1(close):
    return f39_vclu_038_deviation_zscore_sigma21_252d(close).diff()


def f39_vclu_039_reversion_speed_sigma21_63d_d1(close):
    return f39_vclu_039_reversion_speed_sigma21_63d(close).diff()


def f39_vclu_040_frac_time_sigma21_above_mean_252d_d1(close):
    return f39_vclu_040_frac_time_sigma21_above_mean_252d(close).diff()


def f39_vclu_041_ar1_parkinson_252d_d1(high, low):
    return f39_vclu_041_ar1_parkinson_252d(high, low).diff()


def f39_vclu_042_ar1_loghl_63d_d1(high, low):
    return f39_vclu_042_ar1_loghl_63d(high, low).diff()


def f39_vclu_043_autocorr_tr_lag5_252d_d1(high, low, close):
    return f39_vclu_043_autocorr_tr_lag5_252d(high, low, close).diff()


def f39_vclu_044_autocorr_loghl_lag10_252d_d1(high, low):
    return f39_vclu_044_autocorr_loghl_lag10_252d(high, low).diff()


def f39_vclu_045_rs_hurst_truerange_252d_d1(high, low, close):
    return f39_vclu_045_rs_hurst_truerange_252d(high, low, close).diff()


def f39_vclu_046_ljung_box_tr_lags5_63d_d1(high, low, close):
    return f39_vclu_046_ljung_box_tr_lags5_63d(high, low, close).diff()


def f39_vclu_047_frac_time_sigma21_above_p75_252d_d1(close):
    return f39_vclu_047_frac_time_sigma21_above_p75_252d(close).diff()


def f39_vclu_048_bars_since_high_vol_regime_d1(close):
    return f39_vclu_048_bars_since_high_vol_regime(close).diff()


def f39_vclu_049_bars_since_low_vol_regime_d1(close):
    return f39_vclu_049_bars_since_low_vol_regime(close).diff()


def f39_vclu_050_count_median_crossings_sigma21_63d_d1(close):
    return f39_vclu_050_count_median_crossings_sigma21_63d(close).diff()


def f39_vclu_051_longest_high_vol_run_252d_d1(close):
    return f39_vclu_051_longest_high_vol_run_252d(close).diff()


def f39_vclu_052_longest_low_vol_run_252d_d1(close):
    return f39_vclu_052_longest_low_vol_run_252d(close).diff()


def f39_vclu_053_time_top_decile_sigma21_252d_d1(close):
    return f39_vclu_053_time_top_decile_sigma21_252d(close).diff()


def f39_vclu_054_time_bottom_decile_sigma21_252d_d1(close):
    return f39_vclu_054_time_bottom_decile_sigma21_252d(close).diff()


def f39_vclu_055_autocorr_absret_lag1_252d_d1(close):
    return f39_vclu_055_autocorr_absret_lag1_252d(close).diff()


def f39_vclu_056_autocorr_absret_lag5_252d_d1(close):
    return f39_vclu_056_autocorr_absret_lag5_252d(close).diff()


def f39_vclu_057_autocorr_absret_lag21_504d_d1(close):
    return f39_vclu_057_autocorr_absret_lag21_504d(close).diff()


def f39_vclu_058_sum_autocorr_absret_lags1to21_252d_d1(close):
    return f39_vclu_058_sum_autocorr_absret_lags1to21_252d(close).diff()


def f39_vclu_059_gph_loglog_slope_absret_252d_d1(close):
    return f39_vclu_059_gph_loglog_slope_absret_252d(close).diff()


def f39_vclu_060_shannon_entropy_sigma21_bins_252d_d1(close):
    return f39_vclu_060_shannon_entropy_sigma21_bins_252d(close).diff()


def f39_vclu_061_sample_entropy_absret_252d_d1(close):
    return f39_vclu_061_sample_entropy_absret_252d(close).diff()


def f39_vclu_062_approx_entropy_sigma21_252d_d1(close):
    return f39_vclu_062_approx_entropy_sigma21_252d(close).diff()


def f39_vclu_063_permutation_entropy_sigma21_252d_d1(close):
    return f39_vclu_063_permutation_entropy_sigma21_252d(close).diff()


def f39_vclu_064_shannon_entropy_tr_bins_252d_d1(high, low, close):
    return f39_vclu_064_shannon_entropy_tr_bins_252d(high, low, close).diff()


def f39_vclu_065_variance_ratio_sigma63_sigma21_252d_d1(close):
    return f39_vclu_065_variance_ratio_sigma63_sigma21_252d(close).diff()


def f39_vclu_066_ratio_sigma5_over_sigma21_d1(close):
    return f39_vclu_066_ratio_sigma5_over_sigma21(close).diff()


def f39_vclu_067_ratio_sigma21_over_sigma63_d1(close):
    return f39_vclu_067_ratio_sigma21_over_sigma63(close).diff()


def f39_vclu_068_ratio_sigma63_over_sigma252_d1(close):
    return f39_vclu_068_ratio_sigma63_over_sigma252(close).diff()


def f39_vclu_069_ratio_sigma5_over_sigma252_d1(close):
    return f39_vclu_069_ratio_sigma5_over_sigma252(close).diff()


def f39_vclu_070_log_term_structure_slope_5_252_d1(close):
    return f39_vclu_070_log_term_structure_slope_5_252(close).diff()


def f39_vclu_071_term_structure_curvature_4pt_d1(close):
    return f39_vclu_071_term_structure_curvature_4pt(close).diff()


def f39_vclu_072_max_sigma5_over_sigma63_21d_d1(close):
    return f39_vclu_072_max_sigma5_over_sigma63_21d(close).diff()


def f39_vclu_073_count_sigma5_above_2x_sigma63_63d_d1(close):
    return f39_vclu_073_count_sigma5_above_2x_sigma63_63d(close).diff()


def f39_vclu_074_zscore_sigma21_minus_sigma63_252d_d1(close):
    return f39_vclu_074_zscore_sigma21_minus_sigma63_252d(close).diff()


def f39_vclu_075_max_sigma5_over_sigma252_21d_d1(close):
    return f39_vclu_075_max_sigma5_over_sigma252_21d(close).diff()


VOLATILITY_CLUSTERING_D1_REGISTRY_001_075 = {
    "f39_vclu_001_autocorr_rsq_lag1_21d_d1": {"inputs": ["close"], "func": f39_vclu_001_autocorr_rsq_lag1_21d_d1},
    "f39_vclu_002_autocorr_rsq_lag1_63d_d1": {"inputs": ["close"], "func": f39_vclu_002_autocorr_rsq_lag1_63d_d1},
    "f39_vclu_003_autocorr_rsq_lag1_252d_d1": {"inputs": ["close"], "func": f39_vclu_003_autocorr_rsq_lag1_252d_d1},
    "f39_vclu_004_autocorr_rsq_lag2_63d_d1": {"inputs": ["close"], "func": f39_vclu_004_autocorr_rsq_lag2_63d_d1},
    "f39_vclu_005_autocorr_rsq_lag5_63d_d1": {"inputs": ["close"], "func": f39_vclu_005_autocorr_rsq_lag5_63d_d1},
    "f39_vclu_006_autocorr_rsq_lag21_252d_d1": {"inputs": ["close"], "func": f39_vclu_006_autocorr_rsq_lag21_252d_d1},
    "f39_vclu_007_ljung_box_rsq_lags5_63d_d1": {"inputs": ["close"], "func": f39_vclu_007_ljung_box_rsq_lags5_63d_d1},
    "f39_vclu_008_ljung_box_rsq_lags10_252d_d1": {"inputs": ["close"], "func": f39_vclu_008_ljung_box_rsq_lags10_252d_d1},
    "f39_vclu_009_ewma_vol_lambda094_d1": {"inputs": ["close"], "func": f39_vclu_009_ewma_vol_lambda094_d1},
    "f39_vclu_010_ewma_vol_lambda097_d1": {"inputs": ["close"], "func": f39_vclu_010_ewma_vol_lambda097_d1},
    "f39_vclu_011_ewma_vol_lambda099_d1": {"inputs": ["close"], "func": f39_vclu_011_ewma_vol_lambda099_d1},
    "f39_vclu_012_ewma_fast_minus_slow_vol_d1": {"inputs": ["close"], "func": f39_vclu_012_ewma_fast_minus_slow_vol_d1},
    "f39_vclu_013_ewma_fast_over_slow_vol_ratio_d1": {"inputs": ["close"], "func": f39_vclu_013_ewma_fast_over_slow_vol_ratio_d1},
    "f39_vclu_014_log_ewma_fast_minus_log_slow_d1": {"inputs": ["close"], "func": f39_vclu_014_log_ewma_fast_minus_log_slow_d1},
    "f39_vclu_015_ewma_fast_zscore_252d_d1": {"inputs": ["close"], "func": f39_vclu_015_ewma_fast_zscore_252d_d1},
    "f39_vclu_016_ewma_fast_anchor_deviation_252d_d1": {"inputs": ["close"], "func": f39_vclu_016_ewma_fast_anchor_deviation_252d_d1},
    "f39_vclu_017_vol_of_sigma21_63d_d1": {"inputs": ["close"], "func": f39_vclu_017_vol_of_sigma21_63d_d1},
    "f39_vclu_018_vol_of_sigma5_21d_d1": {"inputs": ["close"], "func": f39_vclu_018_vol_of_sigma5_21d_d1},
    "f39_vclu_019_vol_of_sigma63_252d_d1": {"inputs": ["close"], "func": f39_vclu_019_vol_of_sigma63_252d_d1},
    "f39_vclu_020_vol_of_ewma_fast_63d_d1": {"inputs": ["close"], "func": f39_vclu_020_vol_of_ewma_fast_63d_d1},
    "f39_vclu_021_log_vol_of_sigma21_21d_d1": {"inputs": ["close"], "func": f39_vclu_021_log_vol_of_sigma21_21d_d1},
    "f39_vclu_022_log_vol_of_sigma21_252d_d1": {"inputs": ["close"], "func": f39_vclu_022_log_vol_of_sigma21_252d_d1},
    "f39_vclu_023_vol_of_vol_of_vol_63d_252d_d1": {"inputs": ["close"], "func": f39_vclu_023_vol_of_vol_of_vol_63d_252d_d1},
    "f39_vclu_024_vov63_over_vov252_d1": {"inputs": ["close"], "func": f39_vclu_024_vov63_over_vov252_d1},
    "f39_vclu_025_skew_sigma21_252d_d1": {"inputs": ["close"], "func": f39_vclu_025_skew_sigma21_252d_d1},
    "f39_vclu_026_kurt_sigma21_252d_d1": {"inputs": ["close"], "func": f39_vclu_026_kurt_sigma21_252d_d1},
    "f39_vclu_027_ar1_sigma21_252d_d1": {"inputs": ["close"], "func": f39_vclu_027_ar1_sigma21_252d_d1},
    "f39_vclu_028_ar1_sigma5_63d_d1": {"inputs": ["close"], "func": f39_vclu_028_ar1_sigma5_63d_d1},
    "f39_vclu_029_ar1_sigma63_504d_d1": {"inputs": ["close"], "func": f39_vclu_029_ar1_sigma63_504d_d1},
    "f39_vclu_030_ar1_absret_252d_d1": {"inputs": ["close"], "func": f39_vclu_030_ar1_absret_252d_d1},
    "f39_vclu_031_ar1_rsq_252d_d1": {"inputs": ["close"], "func": f39_vclu_031_ar1_rsq_252d_d1},
    "f39_vclu_032_halflife_from_ar1_sigma21_252d_d1": {"inputs": ["close"], "func": f39_vclu_032_halflife_from_ar1_sigma21_252d_d1},
    "f39_vclu_033_slope_sigma_on_lag_sigma_252d_d1": {"inputs": ["close"], "func": f39_vclu_033_slope_sigma_on_lag_sigma_252d_d1},
    "f39_vclu_034_ar1_truerange_252d_d1": {"inputs": ["high", "low", "close"], "func": f39_vclu_034_ar1_truerange_252d_d1},
    "f39_vclu_035_sigma21_minus_rollmean_252d_d1": {"inputs": ["close"], "func": f39_vclu_035_sigma21_minus_rollmean_252d_d1},
    "f39_vclu_036_sigma5_minus_rollmean_252d_d1": {"inputs": ["close"], "func": f39_vclu_036_sigma5_minus_rollmean_252d_d1},
    "f39_vclu_037_log_sigma21_over_rollmean_252d_d1": {"inputs": ["close"], "func": f39_vclu_037_log_sigma21_over_rollmean_252d_d1},
    "f39_vclu_038_deviation_zscore_sigma21_252d_d1": {"inputs": ["close"], "func": f39_vclu_038_deviation_zscore_sigma21_252d_d1},
    "f39_vclu_039_reversion_speed_sigma21_63d_d1": {"inputs": ["close"], "func": f39_vclu_039_reversion_speed_sigma21_63d_d1},
    "f39_vclu_040_frac_time_sigma21_above_mean_252d_d1": {"inputs": ["close"], "func": f39_vclu_040_frac_time_sigma21_above_mean_252d_d1},
    "f39_vclu_041_ar1_parkinson_252d_d1": {"inputs": ["high", "low"], "func": f39_vclu_041_ar1_parkinson_252d_d1},
    "f39_vclu_042_ar1_loghl_63d_d1": {"inputs": ["high", "low"], "func": f39_vclu_042_ar1_loghl_63d_d1},
    "f39_vclu_043_autocorr_tr_lag5_252d_d1": {"inputs": ["high", "low", "close"], "func": f39_vclu_043_autocorr_tr_lag5_252d_d1},
    "f39_vclu_044_autocorr_loghl_lag10_252d_d1": {"inputs": ["high", "low"], "func": f39_vclu_044_autocorr_loghl_lag10_252d_d1},
    "f39_vclu_045_rs_hurst_truerange_252d_d1": {"inputs": ["high", "low", "close"], "func": f39_vclu_045_rs_hurst_truerange_252d_d1},
    "f39_vclu_046_ljung_box_tr_lags5_63d_d1": {"inputs": ["high", "low", "close"], "func": f39_vclu_046_ljung_box_tr_lags5_63d_d1},
    "f39_vclu_047_frac_time_sigma21_above_p75_252d_d1": {"inputs": ["close"], "func": f39_vclu_047_frac_time_sigma21_above_p75_252d_d1},
    "f39_vclu_048_bars_since_high_vol_regime_d1": {"inputs": ["close"], "func": f39_vclu_048_bars_since_high_vol_regime_d1},
    "f39_vclu_049_bars_since_low_vol_regime_d1": {"inputs": ["close"], "func": f39_vclu_049_bars_since_low_vol_regime_d1},
    "f39_vclu_050_count_median_crossings_sigma21_63d_d1": {"inputs": ["close"], "func": f39_vclu_050_count_median_crossings_sigma21_63d_d1},
    "f39_vclu_051_longest_high_vol_run_252d_d1": {"inputs": ["close"], "func": f39_vclu_051_longest_high_vol_run_252d_d1},
    "f39_vclu_052_longest_low_vol_run_252d_d1": {"inputs": ["close"], "func": f39_vclu_052_longest_low_vol_run_252d_d1},
    "f39_vclu_053_time_top_decile_sigma21_252d_d1": {"inputs": ["close"], "func": f39_vclu_053_time_top_decile_sigma21_252d_d1},
    "f39_vclu_054_time_bottom_decile_sigma21_252d_d1": {"inputs": ["close"], "func": f39_vclu_054_time_bottom_decile_sigma21_252d_d1},
    "f39_vclu_055_autocorr_absret_lag1_252d_d1": {"inputs": ["close"], "func": f39_vclu_055_autocorr_absret_lag1_252d_d1},
    "f39_vclu_056_autocorr_absret_lag5_252d_d1": {"inputs": ["close"], "func": f39_vclu_056_autocorr_absret_lag5_252d_d1},
    "f39_vclu_057_autocorr_absret_lag21_504d_d1": {"inputs": ["close"], "func": f39_vclu_057_autocorr_absret_lag21_504d_d1},
    "f39_vclu_058_sum_autocorr_absret_lags1to21_252d_d1": {"inputs": ["close"], "func": f39_vclu_058_sum_autocorr_absret_lags1to21_252d_d1},
    "f39_vclu_059_gph_loglog_slope_absret_252d_d1": {"inputs": ["close"], "func": f39_vclu_059_gph_loglog_slope_absret_252d_d1},
    "f39_vclu_060_shannon_entropy_sigma21_bins_252d_d1": {"inputs": ["close"], "func": f39_vclu_060_shannon_entropy_sigma21_bins_252d_d1},
    "f39_vclu_061_sample_entropy_absret_252d_d1": {"inputs": ["close"], "func": f39_vclu_061_sample_entropy_absret_252d_d1},
    "f39_vclu_062_approx_entropy_sigma21_252d_d1": {"inputs": ["close"], "func": f39_vclu_062_approx_entropy_sigma21_252d_d1},
    "f39_vclu_063_permutation_entropy_sigma21_252d_d1": {"inputs": ["close"], "func": f39_vclu_063_permutation_entropy_sigma21_252d_d1},
    "f39_vclu_064_shannon_entropy_tr_bins_252d_d1": {"inputs": ["high", "low", "close"], "func": f39_vclu_064_shannon_entropy_tr_bins_252d_d1},
    "f39_vclu_065_variance_ratio_sigma63_sigma21_252d_d1": {"inputs": ["close"], "func": f39_vclu_065_variance_ratio_sigma63_sigma21_252d_d1},
    "f39_vclu_066_ratio_sigma5_over_sigma21_d1": {"inputs": ["close"], "func": f39_vclu_066_ratio_sigma5_over_sigma21_d1},
    "f39_vclu_067_ratio_sigma21_over_sigma63_d1": {"inputs": ["close"], "func": f39_vclu_067_ratio_sigma21_over_sigma63_d1},
    "f39_vclu_068_ratio_sigma63_over_sigma252_d1": {"inputs": ["close"], "func": f39_vclu_068_ratio_sigma63_over_sigma252_d1},
    "f39_vclu_069_ratio_sigma5_over_sigma252_d1": {"inputs": ["close"], "func": f39_vclu_069_ratio_sigma5_over_sigma252_d1},
    "f39_vclu_070_log_term_structure_slope_5_252_d1": {"inputs": ["close"], "func": f39_vclu_070_log_term_structure_slope_5_252_d1},
    "f39_vclu_071_term_structure_curvature_4pt_d1": {"inputs": ["close"], "func": f39_vclu_071_term_structure_curvature_4pt_d1},
    "f39_vclu_072_max_sigma5_over_sigma63_21d_d1": {"inputs": ["close"], "func": f39_vclu_072_max_sigma5_over_sigma63_21d_d1},
    "f39_vclu_073_count_sigma5_above_2x_sigma63_63d_d1": {"inputs": ["close"], "func": f39_vclu_073_count_sigma5_above_2x_sigma63_63d_d1},
    "f39_vclu_074_zscore_sigma21_minus_sigma63_252d_d1": {"inputs": ["close"], "func": f39_vclu_074_zscore_sigma21_minus_sigma63_252d_d1},
    "f39_vclu_075_max_sigma5_over_sigma252_21d_d1": {"inputs": ["close"], "func": f39_vclu_075_max_sigma5_over_sigma252_21d_d1},
}
