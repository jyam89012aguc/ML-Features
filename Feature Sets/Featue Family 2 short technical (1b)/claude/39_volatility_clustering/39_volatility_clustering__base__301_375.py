"""volatility_clustering base features 301-375 — Pipeline 1b-technical extension batch 3.

75 NEW fine-grained vol-clustering signals for ML precision. Focus: vol-regime
durations and persistence, vol-rise vs vol-fall asymmetry, vol-of-vol-of-vol,
convergence-rate to long-run mean (Ornstein-Uhlenbeck-style), state-dependent
autocorrelation, memory-loss diagnostics, AR(3)/AR(5) higher-order persistence,
forecast-error variance, vol-cascading lead-lag, σ-spike-then-collapse counts,
HMM-style regime probability, σ-step-event counts.

Inputs: SEP OHLCV only. PIT-clean. Self-contained — no cross-family imports.
"""
import math
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


def _bars_since(ind: pd.Series) -> pd.Series:
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


def _longest_run(w: np.ndarray) -> float:
    m = 0; c = 0
    for v in w:
        if v > 0.5:
            c += 1; m = c if c > m else m
        else:
            c = 0
    return float(m)


# ============================================================
# Bucket A — Vol-regime duration features (301-308)
# ============================================================

def f39_vclu_301_mean_high_vol_regime_duration_252d(close: pd.Series) -> pd.Series:
    """Mean duration of σ_21 > 252d-p75 runs over 252d window."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p75 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    hi = (s > p75).astype(float).fillna(0.0)

    def _mean_dur(w):
        runs = []; cur = 0
        for v in w:
            if v > 0.5: cur += 1
            elif cur > 0: runs.append(cur); cur = 0
        if cur > 0: runs.append(cur)
        return float(np.mean(runs)) if runs else np.nan
    return hi.rolling(YDAYS, min_periods=QDAYS).apply(_mean_dur, raw=True)


def f39_vclu_302_mean_low_vol_regime_duration_252d(close: pd.Series) -> pd.Series:
    """Mean duration of σ_21 < 252d-p25 runs over 252d window."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p25 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    lo = (s < p25).astype(float).fillna(0.0)

    def _mean_dur(w):
        runs = []; cur = 0
        for v in w:
            if v > 0.5: cur += 1
            elif cur > 0: runs.append(cur); cur = 0
        if cur > 0: runs.append(cur)
        return float(np.mean(runs)) if runs else np.nan
    return lo.rolling(YDAYS, min_periods=QDAYS).apply(_mean_dur, raw=True)


def f39_vclu_303_total_high_vol_time_504d(close: pd.Series) -> pd.Series:
    """Total bars in σ_21 > 504d-p75 regime over 504d (multi-year high-vol exposure)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p75 = s.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.75)
    return (s > p75).astype(float).rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f39_vclu_304_total_low_vol_time_504d(close: pd.Series) -> pd.Series:
    """Total bars in σ_21 < 504d-p25 regime over 504d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p25 = s.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.25)
    return (s < p25).astype(float).rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f39_vclu_305_days_since_regime_change(close: pd.Series) -> pd.Series:
    """Bars since σ_21 last crossed its 252d median (regime change recency)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    med = s.rolling(YDAYS, min_periods=QDAYS).median()
    above = (s > med).astype(int)
    crossing = (above.diff().abs() > 0).astype(float).fillna(0.0)
    return _bars_since(crossing)


def f39_vclu_306_high_vol_regime_persistence_252d(close: pd.Series) -> pd.Series:
    """High-vol persistence: P(σ>p75 next bar | σ>p75 this bar) over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p75 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    hi = (s > p75).astype(float)
    next_hi = hi.shift(1).fillna(0)  # this looks ahead — restate causally
    # Causal: estimate P(hi_t | hi_{t-1}): count (hi_lag=1 AND hi=1) / count(hi_lag=1)
    hi_lag = hi.shift(1)
    both = ((hi_lag > 0.5) & (hi > 0.5)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    lag_total = (hi_lag > 0.5).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(both, lag_total)


def f39_vclu_307_low_vol_regime_persistence_252d(close: pd.Series) -> pd.Series:
    """Low-vol persistence: P(σ<p25 next | σ<p25 this) over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p25 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    lo = (s < p25).astype(float)
    lo_lag = lo.shift(1)
    both = ((lo_lag > 0.5) & (lo > 0.5)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    lag_total = (lo_lag > 0.5).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(both, lag_total)


def f39_vclu_308_regime_shift_recency_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of bars-since-last-regime-change within 252d distribution."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    med = s.rolling(YDAYS, min_periods=QDAYS).median()
    above = (s > med).astype(int)
    crossing = (above.diff().abs() > 0).astype(float).fillna(0.0)
    bars_since = _bars_since(crossing)
    return _rolling_zscore(bars_since, YDAYS)


# ============================================================
# Bucket B — Vol persistence asymmetry (309-316)
# ============================================================

def f39_vclu_309_rise_vs_fall_duration_ratio_252d(close: pd.Series) -> pd.Series:
    """Mean σ-rising-run duration / mean σ-falling-run duration over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    rising = (s.diff() > 0).astype(float).fillna(0.0)
    falling = (s.diff() < 0).astype(float).fillna(0.0)

    def _mean_dur(w):
        runs = []; cur = 0
        for v in w:
            if v > 0.5: cur += 1
            elif cur > 0: runs.append(cur); cur = 0
        if cur > 0: runs.append(cur)
        return float(np.mean(runs)) if runs else np.nan
    rise_d = rising.rolling(YDAYS, min_periods=QDAYS).apply(_mean_dur, raw=True)
    fall_d = falling.rolling(YDAYS, min_periods=QDAYS).apply(_mean_dur, raw=True)
    return _safe_div(rise_d, fall_d)


def f39_vclu_310_rise_vs_fall_magnitude_ratio_252d(close: pd.Series) -> pd.Series:
    """Mean |Δσ| on rising-σ days / falling-σ days over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    ds = s.diff()
    rise = ds.where(ds > 0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    fall = (-ds).where(ds < 0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(rise, fall)


def f39_vclu_311_sigma_rise_5d_rate_252d(close: pd.Series) -> pd.Series:
    """Mean (σ_t - σ_t-5) / σ_t-5 on rising days, over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    pct = _safe_div(s - s.shift(WDAYS), s.shift(WDAYS))
    rise = (s.diff() > 0)
    return pct.where(rise, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f39_vclu_312_sigma_acceleration_up_days_252d(close: pd.Series) -> pd.Series:
    """Mean Δ²σ on rising-σ days over 252d (acceleration when σ is rising)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    accel = s.diff().diff()
    rise = (s.diff() > 0)
    return accel.where(rise, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f39_vclu_313_sigma_acceleration_down_days_252d(close: pd.Series) -> pd.Series:
    """Mean Δ²σ on falling-σ days over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    accel = s.diff().diff()
    fall = (s.diff() < 0)
    return accel.where(fall, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f39_vclu_314_sigma_momentum_asymmetry_252d(close: pd.Series) -> pd.Series:
    """Corr(Δσ_t, Δσ_{t-1}) restricted to bars where Δσ_{t-1} > 0 minus same for < 0."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    ds = s.diff()
    pos_lag = (ds.shift(1) > 0)
    neg_lag = (ds.shift(1) < 0)
    pos_corr = ds.where(pos_lag, np.nan).rolling(YDAYS, min_periods=QDAYS).corr(ds.shift(1).where(pos_lag, np.nan))
    neg_corr = ds.where(neg_lag, np.nan).rolling(YDAYS, min_periods=QDAYS).corr(ds.shift(1).where(neg_lag, np.nan))
    return pos_corr - neg_corr


def f39_vclu_315_vov_in_rising_sigma_252d(close: pd.Series) -> pd.Series:
    """Std of σ_21 restricted to rising-σ bars over 252d (vol-of-vol in rising regime)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    rising = (s.diff() > 0)
    return s.where(rising, np.nan).rolling(YDAYS, min_periods=QDAYS).std()


def f39_vclu_316_vov_in_falling_sigma_252d(close: pd.Series) -> pd.Series:
    """Std of σ_21 restricted to falling-σ bars over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    falling = (s.diff() < 0)
    return s.where(falling, np.nan).rolling(YDAYS, min_periods=QDAYS).std()


# ============================================================
# Bucket C — Vol-of-vol-of-vol (317-319)
# ============================================================

def f39_vclu_317_vovov_63d(close: pd.Series) -> pd.Series:
    """Variance of (vol-of-σ_21 over 21d) over 63d — third-order vol curvature."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    vov = s.rolling(MDAYS, min_periods=WDAYS).std()
    return vov.rolling(QDAYS, min_periods=MDAYS).var()


def f39_vclu_318_skew_vov_63d(close: pd.Series) -> pd.Series:
    """Skew of vol-of-σ_21 (computed over 21d) over 63d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    vov = s.rolling(MDAYS, min_periods=WDAYS).std()
    return vov.rolling(QDAYS, min_periods=MDAYS).skew()


def f39_vclu_319_kurt_vov_63d(close: pd.Series) -> pd.Series:
    """Kurt of vol-of-σ_21 over 63d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    vov = s.rolling(MDAYS, min_periods=WDAYS).std()
    return vov.rolling(QDAYS, min_periods=MDAYS).kurt()


# ============================================================
# Bucket D — Convergence rate / OU features (320-325)
# ============================================================

def f39_vclu_320_relative_deviation_sigma_long_run(close: pd.Series) -> pd.Series:
    """(σ_21 - σ_252) / σ_252 — relative deviation from long-run vol."""
    r = _log_ret(close)
    s21 = _rolling_sigma(r, MDAYS); s252 = _rolling_sigma(r, YDAYS)
    return _safe_div(s21 - s252, s252)


def f39_vclu_321_convergence_halflife_to_sigma_mean_252d(close: pd.Series) -> pd.Series:
    """Convergence half-life: |log(deviation_t / deviation_t-21)| → -log(2)/log(decay)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    mu = s.rolling(YDAYS, min_periods=QDAYS).mean()
    dev = (s - mu).abs()
    decay = _safe_div(dev, dev.shift(MDAYS)).clip(upper=0.99, lower=1e-3)
    hl = -np.log(2.0) / np.log(decay)
    return hl.clip(upper=500.0)


def f39_vclu_322_sigma_deviation_in_long_run_units_252d(close: pd.Series) -> pd.Series:
    """Z-score of σ_21 within long-run σ_252 distribution over 252d."""
    r = _log_ret(close)
    s21 = _rolling_sigma(r, MDAYS); s252 = _rolling_sigma(r, YDAYS)
    return _safe_div(s21 - s252.rolling(YDAYS, min_periods=QDAYS).mean(),
                     s252.rolling(YDAYS, min_periods=QDAYS).std())


def f39_vclu_323_long_run_vol_stability_504d(close: pd.Series) -> pd.Series:
    """Variance of σ_252 over 504d (stability of long-run vol estimate)."""
    return _rolling_sigma(_log_ret(close), YDAYS).rolling(DDAYS_2Y, min_periods=YDAYS).var()


def f39_vclu_324_ou_reversion_coef_sigma_252d(close: pd.Series) -> pd.Series:
    """OU mean-reversion coef: slope of Δσ on (μ-σ) regression over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    mu = s.rolling(YDAYS, min_periods=QDAYS).mean()
    diff_s = s.diff()
    ou_dev = (mu - s).shift(1)
    cov = diff_s.rolling(YDAYS, min_periods=QDAYS).cov(ou_dev)
    var = ou_dev.rolling(YDAYS, min_periods=QDAYS).var()
    return _safe_div(cov, var)


def f39_vclu_325_ou_long_run_mean_sigma_252d(close: pd.Series) -> pd.Series:
    """OU long-run mean: intercept from regression of Δσ on σ over 252d (= θ in Ornstein-Uhlenbeck)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    diff_s = s.diff()
    s_lag = s.shift(1)
    combined = pd.concat([diff_s, s_lag], axis=1).values

    def _theta(arr):
        if arr.shape[0] < QDAYS:
            return np.nan
        y, x = arr[:, 0], arr[:, 1]
        m = ~(np.isnan(y) | np.isnan(x))
        if m.sum() < QDAYS:
            return np.nan
        X = np.column_stack([np.ones(m.sum()), x[m]])
        try:
            beta = np.linalg.lstsq(X, y[m], rcond=None)[0]
            # Δσ = α + β·σ → in OU form Δσ = κ·(θ-σ), so β = -κ, α = κ·θ → θ = -α/β
            if beta[1] == 0: return np.nan
            return float(-beta[0] / beta[1])
        except Exception:
            return np.nan
    out = pd.Series(np.nan, index=close.index)
    for i in range(YDAYS, len(combined)):
        out.iloc[i] = _theta(combined[i - YDAYS + 1:i + 1])
    return out


# ============================================================
# Bucket E — State-dependent autocorrelation (326-331)
# ============================================================

def f39_vclu_326_autocorr_rsq_lag1_high_vol_252d(close: pd.Series) -> pd.Series:
    """Corr(r²_t, r²_{t-1}) restricted to high-vol regime (σ_21>p75) over 252d."""
    r2 = _log_ret(close) ** 2
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p75 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    hi = (s > p75)
    return r2.where(hi, np.nan).rolling(YDAYS, min_periods=QDAYS).corr(r2.shift(1).where(hi, np.nan))


def f39_vclu_327_autocorr_rsq_lag1_low_vol_252d(close: pd.Series) -> pd.Series:
    """Corr(r²_t, r²_{t-1}) restricted to low-vol regime over 252d."""
    r2 = _log_ret(close) ** 2
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p25 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    lo = (s < p25)
    return r2.where(lo, np.nan).rolling(YDAYS, min_periods=QDAYS).corr(r2.shift(1).where(lo, np.nan))


def f39_vclu_328_autocorr_absr_lag1_high_vol_252d(close: pd.Series) -> pd.Series:
    """Corr(|r|_t, |r|_{t-1}) restricted to high-vol regime over 252d."""
    a = _log_ret(close).abs()
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p75 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    hi = (s > p75)
    return a.where(hi, np.nan).rolling(YDAYS, min_periods=QDAYS).corr(a.shift(1).where(hi, np.nan))


def f39_vclu_329_autocorr_absr_lag1_low_vol_252d(close: pd.Series) -> pd.Series:
    """Corr(|r|_t, |r|_{t-1}) restricted to low-vol regime over 252d."""
    a = _log_ret(close).abs()
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p25 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    lo = (s < p25)
    return a.where(lo, np.nan).rolling(YDAYS, min_periods=QDAYS).corr(a.shift(1).where(lo, np.nan))


def f39_vclu_330_autocorr_sigma_lag1_rising_252d(close: pd.Series) -> pd.Series:
    """AR(1) of σ_21 restricted to rising-σ days over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    rising = (s.diff() > 0)
    return s.where(rising, np.nan).rolling(YDAYS, min_periods=QDAYS).corr(s.shift(1).where(rising, np.nan))


def f39_vclu_331_autocorr_sigma_lag1_falling_252d(close: pd.Series) -> pd.Series:
    """AR(1) of σ_21 restricted to falling-σ days over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    falling = (s.diff() < 0)
    return s.where(falling, np.nan).rolling(YDAYS, min_periods=QDAYS).corr(s.shift(1).where(falling, np.nan))


# ============================================================
# Bucket F — Memory-loss diagnostics (332-336)
# ============================================================

def f39_vclu_332_sigma_memory_lag63_504d(close: pd.Series) -> pd.Series:
    """Corr(σ_21_t, σ_21_{t-63}) over 504d — quarterly-lag memory."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return s.rolling(DDAYS_2Y, min_periods=YDAYS).corr(s.shift(QDAYS))


def f39_vclu_333_sigma_memory_lag126_504d(close: pd.Series) -> pd.Series:
    """Corr(σ_21_t, σ_21_{t-126}) over 504d — half-year-lag memory."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return s.rolling(DDAYS_2Y, min_periods=YDAYS).corr(s.shift(126))


def f39_vclu_334_sigma_memory_loss_rate_252d(close: pd.Series) -> pd.Series:
    """Memory loss: |corr at lag-1| − |corr at lag-21| over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    c1 = s.rolling(YDAYS, min_periods=QDAYS).corr(s.shift(1))
    c21 = s.rolling(YDAYS, min_periods=QDAYS).corr(s.shift(MDAYS))
    return c1.abs() - c21.abs()


def f39_vclu_335_sigma_memory_completeness_252d(close: pd.Series) -> pd.Series:
    """Sum of |corr(σ_21, σ_21.shift(k))| for k=1..21 over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    total = pd.Series(0.0, index=close.index)
    for k in range(1, MDAYS + 1):
        c = s.rolling(YDAYS, min_periods=QDAYS).corr(s.shift(k))
        total = total + c.abs()
    return total


def f39_vclu_336_sigma_long_memory_ratio_252d(close: pd.Series) -> pd.Series:
    """Σ|corr| at lags 1..21 / Σ|corr| at lags 1..63 over 252d (longer-horizon memory share)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    short = pd.Series(0.0, index=close.index)
    long_ = pd.Series(0.0, index=close.index)
    for k in range(1, MDAYS + 1):
        short = short + s.rolling(YDAYS, min_periods=QDAYS).corr(s.shift(k)).abs()
    for k in range(1, QDAYS + 1):
        long_ = long_ + s.rolling(YDAYS, min_periods=QDAYS).corr(s.shift(k)).abs()
    return _safe_div(short, long_)


# ============================================================
# Bucket G — Higher-order persistence (337-341)
# ============================================================

def f39_vclu_337_ar3_phi3_sigma21_252d(close: pd.Series) -> pd.Series:
    """AR(3) coefficient φ_3 of σ_21 via rolling OLS over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    combined = pd.concat([s, s.shift(1), s.shift(2), s.shift(3)], axis=1).values

    def _phi3(arr):
        if arr.shape[0] < QDAYS:
            return np.nan
        y, x1, x2, x3 = arr[:, 0], arr[:, 1], arr[:, 2], arr[:, 3]
        m = ~(np.isnan(y) | np.isnan(x1) | np.isnan(x2) | np.isnan(x3))
        if m.sum() < QDAYS:
            return np.nan
        X = np.column_stack([np.ones(m.sum()), x1[m], x2[m], x3[m]])
        try:
            beta = np.linalg.lstsq(X, y[m], rcond=None)[0]
            return float(beta[3])
        except Exception:
            return np.nan
    out = pd.Series(np.nan, index=close.index)
    for i in range(YDAYS, len(combined)):
        out.iloc[i] = _phi3(combined[i - YDAYS + 1:i + 1])
    return out


def f39_vclu_338_ar5_phi5_sigma21_252d(close: pd.Series) -> pd.Series:
    """AR(5) coefficient φ_5 of σ_21 over 252d (deeper memory)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    lags = [s.shift(k) for k in range(1, 6)]
    combined = pd.concat([s] + lags, axis=1).values

    def _phi5(arr):
        if arr.shape[0] < QDAYS:
            return np.nan
        y = arr[:, 0]
        Xcols = arr[:, 1:]
        m = ~np.isnan(y) & ~np.any(np.isnan(Xcols), axis=1)
        if m.sum() < QDAYS:
            return np.nan
        X = np.column_stack([np.ones(m.sum()), Xcols[m]])
        try:
            beta = np.linalg.lstsq(X, y[m], rcond=None)[0]
            return float(beta[5])
        except Exception:
            return np.nan
    out = pd.Series(np.nan, index=close.index)
    for i in range(YDAYS, len(combined)):
        out.iloc[i] = _phi5(combined[i - YDAYS + 1:i + 1])
    return out


def f39_vclu_339_ar1_sigma5_252d(close: pd.Series) -> pd.Series:
    """AR(1) of σ_5 over 252d (very-short-horizon vol persistence)."""
    s = _rolling_sigma(_log_ret(close), WDAYS)
    return s.rolling(YDAYS, min_periods=QDAYS).corr(s.shift(1))


def f39_vclu_340_ar1_sigma252_504d(close: pd.Series) -> pd.Series:
    """AR(1) of σ_252 over 504d (very-long-horizon vol persistence)."""
    s = _rolling_sigma(_log_ret(close), YDAYS)
    return s.rolling(DDAYS_2Y, min_periods=YDAYS).corr(s.shift(1))


def f39_vclu_341_pp_stationarity_proxy_sigma_252d(close: pd.Series) -> pd.Series:
    """Phillips-Perron-style stationarity proxy: Δσ / σ_lag regression slope over 252d (negative = stationary)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    ds = s.diff(); s_lag = s.shift(1)
    cov = ds.rolling(YDAYS, min_periods=QDAYS).cov(s_lag)
    var = s_lag.rolling(YDAYS, min_periods=QDAYS).var()
    return _safe_div(cov, var)


# ============================================================
# Bucket H — Forecast-error / model-fit (342-347)
# ============================================================

def f39_vclu_342_ewma_forecast_error_var_21d(close: pd.Series) -> pd.Series:
    """Variance of (r²_t − EWMA(r², λ=0.94)_{t-1}) forecast errors over 21d."""
    r = _log_ret(close)
    ewma_pred = (r ** 2).ewm(alpha=0.06, min_periods=MDAYS).mean().shift(1)
    err = (r ** 2) - ewma_pred
    return err.rolling(MDAYS, min_periods=WDAYS).var()


def f39_vclu_343_garch_forecast_error_var_252d(close: pd.Series) -> pd.Series:
    """Variance of GARCH-style forecast errors over 252d (using simple EWMA forecast)."""
    r = _log_ret(close)
    ewma_pred = (r ** 2).ewm(alpha=0.06, min_periods=MDAYS).mean().shift(1)
    err = (r ** 2) - ewma_pred
    return err.rolling(YDAYS, min_periods=QDAYS).var()


def f39_vclu_344_mean_abs_forecast_error_21d(close: pd.Series) -> pd.Series:
    """Mean |forecast error| over 21d (forecast = EWMA σ²)."""
    r = _log_ret(close)
    ewma_pred = (r ** 2).ewm(alpha=0.06, min_periods=MDAYS).mean().shift(1)
    return ((r ** 2) - ewma_pred).abs().rolling(MDAYS, min_periods=WDAYS).mean()


def f39_vclu_345_forecast_bias_252d(close: pd.Series) -> pd.Series:
    """Mean signed forecast error over 252d: positive = underforecasting realized vol."""
    r = _log_ret(close)
    ewma_pred = (r ** 2).ewm(alpha=0.06, min_periods=MDAYS).mean().shift(1)
    return ((r ** 2) - ewma_pred).rolling(YDAYS, min_periods=QDAYS).mean()


def f39_vclu_346_forecast_error_skew_252d(close: pd.Series) -> pd.Series:
    """Skew of forecast errors over 252d."""
    r = _log_ret(close)
    ewma_pred = (r ** 2).ewm(alpha=0.06, min_periods=MDAYS).mean().shift(1)
    return ((r ** 2) - ewma_pred).rolling(YDAYS, min_periods=QDAYS).skew()


def f39_vclu_347_forecast_error_kurt_252d(close: pd.Series) -> pd.Series:
    """Kurt of forecast errors over 252d."""
    r = _log_ret(close)
    ewma_pred = (r ** 2).ewm(alpha=0.06, min_periods=MDAYS).mean().shift(1)
    return ((r ** 2) - ewma_pred).rolling(YDAYS, min_periods=QDAYS).kurt()


# ============================================================
# Bucket I — Vol cascading lead-lag (348-352)
# ============================================================

def f39_vclu_348_corr_sigma5_lead_sigma21_5d_252d(close: pd.Series) -> pd.Series:
    """Corr(σ_5_t-5, σ_21_t) over 252d — σ_5 leading σ_21 by 5 days."""
    r = _log_ret(close)
    s5 = _rolling_sigma(r, WDAYS); s21 = _rolling_sigma(r, MDAYS)
    return s21.rolling(YDAYS, min_periods=QDAYS).corr(s5.shift(WDAYS))


def f39_vclu_349_corr_sigma21_lead_sigma63_21d_252d(close: pd.Series) -> pd.Series:
    """Corr(σ_21_t-21, σ_63_t) over 252d — σ_21 leading σ_63 by 21 days."""
    r = _log_ret(close)
    s21 = _rolling_sigma(r, MDAYS); s63 = _rolling_sigma(r, QDAYS)
    return s63.rolling(YDAYS, min_periods=QDAYS).corr(s21.shift(MDAYS))


def f39_vclu_350_granger_sigma5_to_sigma21_252d(close: pd.Series) -> pd.Series:
    """Granger-causality proxy: ΔR² from adding σ_5.shift(1) to AR(1) of σ_21 over 252d."""
    r = _log_ret(close)
    s5 = _rolling_sigma(r, WDAYS); s21 = _rolling_sigma(r, MDAYS)
    combined = pd.concat([s21, s21.shift(1), s5.shift(1)], axis=1).values

    def _gc(arr):
        if arr.shape[0] < QDAYS:
            return np.nan
        y, x1, x2 = arr[:, 0], arr[:, 1], arr[:, 2]
        m = ~(np.isnan(y) | np.isnan(x1) | np.isnan(x2))
        if m.sum() < QDAYS:
            return np.nan
        # Restricted: y on x1
        Xr = np.column_stack([np.ones(m.sum()), x1[m]])
        # Unrestricted: y on x1, x2
        Xu = np.column_stack([np.ones(m.sum()), x1[m], x2[m]])
        try:
            br = np.linalg.lstsq(Xr, y[m], rcond=None)[0]
            bu = np.linalg.lstsq(Xu, y[m], rcond=None)[0]
            rss_r = ((y[m] - Xr @ br) ** 2).sum()
            rss_u = ((y[m] - Xu @ bu) ** 2).sum()
            return float((rss_r - rss_u) / rss_r) if rss_r > 0 else np.nan
        except Exception:
            return np.nan
    out = pd.Series(np.nan, index=close.index)
    for i in range(YDAYS, len(combined)):
        out.iloc[i] = _gc(combined[i - YDAYS + 1:i + 1])
    return out


def f39_vclu_351_lead_lag_max_lag_sigma5_sigma21_252d(close: pd.Series) -> pd.Series:
    """Lag at which corr(σ_5, σ_21.shift(k)) is maximum, for k∈{-5..5}, over 252d."""
    r = _log_ret(close)
    s5 = _rolling_sigma(r, WDAYS); s21 = _rolling_sigma(r, MDAYS)

    def _ll(arr):
        if arr.shape[0] < YDAYS:
            return np.nan
        a = arr[:, 0]; b = arr[:, 1]
        m = ~(np.isnan(a) | np.isnan(b))
        if m.sum() < QDAYS:
            return np.nan
        a, b = a[m], b[m]
        best_lag = 0; best_corr = -np.inf
        for k in range(-WDAYS, WDAYS + 1):
            if k == 0:
                c = np.corrcoef(a, b)[0, 1]
            elif k > 0:
                if len(a) <= k: continue
                c = np.corrcoef(a[k:], b[:-k])[0, 1]
            else:
                if len(a) <= -k: continue
                c = np.corrcoef(a[:k], b[-k:])[0, 1]
            if np.isfinite(c) and c > best_corr:
                best_corr = c; best_lag = k
        return float(best_lag)
    combined = pd.concat([s5, s21], axis=1).values
    out = pd.Series(np.nan, index=close.index)
    for i in range(YDAYS, len(combined)):
        out.iloc[i] = _ll(combined[i - YDAYS + 1:i + 1])
    return out


def f39_vclu_352_corr_sigma5_lead_sigma252_21d_252d(close: pd.Series) -> pd.Series:
    """Corr(σ_5_t-21, σ_252_t) over 252d — σ_5 leading σ_252 by 21 days."""
    r = _log_ret(close)
    s5 = _rolling_sigma(r, WDAYS); s252 = _rolling_sigma(r, YDAYS)
    return s252.rolling(YDAYS, min_periods=QDAYS).corr(s5.shift(MDAYS))


# ============================================================
# Bucket J — Specific vol-event signatures (353-360)
# ============================================================

def f39_vclu_353_spike_then_collapse_count_252d(close: pd.Series) -> pd.Series:
    """σ-spike (>p95) followed within 10d by σ-collapse (<p25), count over 252d (lag form)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p95 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    p25 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    spike_lag = (s.shift(10) > p95.shift(10))
    collapse_now = (s < p25)
    return (spike_lag & collapse_now).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f39_vclu_354_spike_without_revert_count_252d(close: pd.Series) -> pd.Series:
    """σ>p95 events where σ stays > median for 10 days, count over 252d (persistent spike)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p95 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    med = s.rolling(YDAYS, min_periods=QDAYS).median()
    spike_lag = (s.shift(10) > p95.shift(10))
    above_med_persistent = (s > med).rolling(10, min_periods=5).min().astype(bool)
    return (spike_lag & above_med_persistent).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f39_vclu_355_mean_sigma_decay_after_spike_252d(close: pd.Series) -> pd.Series:
    """Mean (σ_now − σ_lag1) on bars 1-10 after σ_21 > p95 events, over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p95 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    spike_anywhere_recent = (s.shift(1).rolling(10, min_periods=1).max() > p95.shift(1).rolling(10, min_periods=1).max())
    decay = s.diff().where(spike_anywhere_recent, np.nan)
    return decay.rolling(YDAYS, min_periods=QDAYS).mean()


def f39_vclu_356_sigma_step_event_count_252d(close: pd.Series) -> pd.Series:
    """σ-step event count: |Δσ_21| > p99 of |Δσ_21| over trailing 252d, summed 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    ds_abs = s.diff().abs()
    p99 = ds_abs.rolling(YDAYS, min_periods=QDAYS).quantile(0.99).shift(1)
    return (ds_abs > p99).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f39_vclu_357_sigma_step_down_count_252d(close: pd.Series) -> pd.Series:
    """σ-step-down events: Δσ_21 < −p99 of |Δσ_21|, summed 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    ds = s.diff()
    p99 = ds.abs().rolling(YDAYS, min_periods=QDAYS).quantile(0.99).shift(1)
    return (ds < -p99).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f39_vclu_358_sigma_step_up_count_252d(close: pd.Series) -> pd.Series:
    """σ-step-up events: Δσ_21 > +p99 of |Δσ_21|, summed 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    ds = s.diff()
    p99 = ds.abs().rolling(YDAYS, min_periods=QDAYS).quantile(0.99).shift(1)
    return (ds > p99).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f39_vclu_359_vov_spike_count_252d(close: pd.Series) -> pd.Series:
    """Vol-of-vol spike count: vol-of-σ_21 over 21d > 252d-p95, summed 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    vov = s.rolling(MDAYS, min_periods=WDAYS).std()
    p95 = vov.rolling(YDAYS, min_periods=QDAYS).quantile(0.95).shift(1)
    return (vov > p95).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f39_vclu_360_coincident_sigma5_sigma21_spike_count_252d(close: pd.Series) -> pd.Series:
    """Co-spike: σ_5 > 252d-p95 AND σ_21 > 252d-p95 same day, over 252d."""
    r = _log_ret(close)
    s5 = _rolling_sigma(r, WDAYS); s21 = _rolling_sigma(r, MDAYS)
    p95_5 = s5.rolling(YDAYS, min_periods=QDAYS).quantile(0.95).shift(1)
    p95_21 = s21.rolling(YDAYS, min_periods=QDAYS).quantile(0.95).shift(1)
    return ((s5 > p95_5) & (s21 > p95_21)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket K — HMM-style regime dynamics (361-365)
# ============================================================

def f39_vclu_361_hmm_high_vol_prob_252d(close: pd.Series) -> pd.Series:
    """HMM-style high-vol regime probability via 2-state EM on log σ²_21 over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    ls2 = _safe_log(s ** 2 + 1e-12)

    def _hmm(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < QDAYS:
            return np.nan
        med = np.median(ww)
        mu0 = ww[ww <= med].mean(); mu1 = ww[ww > med].mean()
        var0 = ww[ww <= med].var(); var1 = ww[ww > med].var()
        if var0 == 0 or var1 == 0:
            return np.nan
        for _ in range(5):
            p0 = np.exp(-0.5 * (ww - mu0) ** 2 / var0) / np.sqrt(2 * np.pi * var0)
            p1 = np.exp(-0.5 * (ww - mu1) ** 2 / var1) / np.sqrt(2 * np.pi * var1)
            w0 = p0 / (p0 + p1 + 1e-12); w1 = 1.0 - w0
            if w0.sum() <= 0 or w1.sum() <= 0:
                break
            mu0 = (w0 * ww).sum() / w0.sum(); mu1 = (w1 * ww).sum() / w1.sum()
            var0 = (w0 * (ww - mu0) ** 2).sum() / w0.sum(); var1 = (w1 * (ww - mu1) ** 2).sum() / w1.sum()
        if mu1 < mu0:
            mu0, mu1 = mu1, mu0; var0, var1 = var1, var0
        x = ww[-1]
        p0 = np.exp(-0.5 * (x - mu0) ** 2 / var0) / np.sqrt(2 * np.pi * var0)
        p1 = np.exp(-0.5 * (x - mu1) ** 2 / var1) / np.sqrt(2 * np.pi * var1)
        return float(p1 / (p0 + p1 + 1e-12))
    return ls2.rolling(YDAYS, min_periods=QDAYS).apply(_hmm, raw=True)


def f39_vclu_362_hmm_high_to_low_transition_estimate_252d(close: pd.Series) -> pd.Series:
    """HMM transition P(low | high): freq of σ-decrease from high regime to low over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    med = s.rolling(YDAYS, min_periods=QDAYS).median()
    above = (s > med).astype(int)
    hi_to_lo = ((above.shift(1) == 1) & (above == 0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    in_hi = (above.shift(1) == 1).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(hi_to_lo, in_hi)


def f39_vclu_363_hmm_low_to_high_transition_estimate_252d(close: pd.Series) -> pd.Series:
    """HMM transition P(high | low) over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    med = s.rolling(YDAYS, min_periods=QDAYS).median()
    above = (s > med).astype(int)
    lo_to_hi = ((above.shift(1) == 0) & (above == 1)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    in_lo = (above.shift(1) == 0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(lo_to_hi, in_lo)


def f39_vclu_364_hmm_steady_state_high_prob_252d(close: pd.Series) -> pd.Series:
    """Steady-state P(high) from 2-state transition matrix: π_h = P(h|l) / (P(h|l) + P(l|h))."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    med = s.rolling(YDAYS, min_periods=QDAYS).median()
    above = (s > med).astype(int)
    hi_to_lo = ((above.shift(1) == 1) & (above == 0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    in_hi = (above.shift(1) == 1).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    lo_to_hi = ((above.shift(1) == 0) & (above == 1)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    in_lo = (above.shift(1) == 0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    p_l_h = _safe_div(hi_to_lo, in_hi)
    p_h_l = _safe_div(lo_to_hi, in_lo)
    return _safe_div(p_h_l, p_h_l + p_l_h)


def f39_vclu_365_regime_shift_rate_252d(close: pd.Series) -> pd.Series:
    """Total regime shifts per bar: count of σ-crossings of median / 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    med = s.rolling(YDAYS, min_periods=QDAYS).median()
    above = (s > med).astype(float)
    return above.diff().abs().rolling(YDAYS, min_periods=QDAYS).sum() / YDAYS


# ============================================================
# Bucket L — Final misc (366-375)
# ============================================================

def f39_vclu_366_sigma_trend_expected_vs_realized_252d(close: pd.Series) -> pd.Series:
    """σ-trend reversal events: count of bars where sign(σ-slope_t) ≠ sign(σ-slope_{t-21}) over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    sl = _rolling_slope(s, MDAYS)
    rev = (np.sign(sl) != np.sign(sl.shift(MDAYS))) & (np.sign(sl) != 0)
    return rev.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f39_vclu_367_sigma_acceleration_d2_21d(close: pd.Series) -> pd.Series:
    """Δ²σ_21 (σ-acceleration) — 21d rolling mean."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return s.diff().diff().rolling(MDAYS, min_periods=WDAYS).mean()


def f39_vclu_368_vov_in_mean_reverting_state_252d(close: pd.Series) -> pd.Series:
    """σ-of-σ_21 in bars where σ has reverted toward 252d mean (current |dev| < lag1 |dev|), over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    mu = s.rolling(YDAYS, min_periods=QDAYS).mean()
    dev = (s - mu).abs()
    reverting = (dev < dev.shift(1))
    return s.where(reverting, np.nan).rolling(YDAYS, min_periods=QDAYS).std()


def f39_vclu_369_sigma_time_to_half_decay_252d(close: pd.Series) -> pd.Series:
    """Sigma time-to-half: bars for σ_21 to reach halfway to 252d median (from current deviation)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    med = s.rolling(YDAYS, min_periods=QDAYS).median()
    dev = s - med
    arr_s = s.values; arr_med = med.values; arr_dev = dev.values
    out = np.full(len(arr_s), np.nan)
    for i in range(YDAYS, len(arr_s) - MDAYS):
        if np.isnan(arr_dev[i]) or arr_dev[i] == 0:
            continue
        target = arr_med[i] + 0.5 * arr_dev[i]
        for j in range(i + 1, min(i + MDAYS, len(arr_s))):
            if np.isnan(arr_s[j]):
                continue
            if (arr_dev[i] > 0 and arr_s[j] <= target) or (arr_dev[i] < 0 and arr_s[j] >= target):
                out[i] = float(j - i)
                break
        else:
            out[i] = float(MDAYS)
    return pd.Series(out, index=close.index)


def f39_vclu_370_gjr_asymmetry_504d(close: pd.Series) -> pd.Series:
    """GJR-like asymmetry coefficient: rolling 504d OLS β on r²_{t-1}·1{r_{t-1}<0} controlling r²_{t-1}."""
    r = _log_ret(close)
    r2 = r ** 2
    y = r2; x1 = r2.shift(1); x2 = r2.shift(1) * (r.shift(1) < 0).astype(float)
    combined = pd.concat([y, x1, x2], axis=1).values

    def _gam(arr):
        if arr.shape[0] < YDAYS:
            return np.nan
        y_, x1_, x2_ = arr[:, 0], arr[:, 1], arr[:, 2]
        m = ~(np.isnan(y_) | np.isnan(x1_) | np.isnan(x2_))
        if m.sum() < YDAYS:
            return np.nan
        X = np.column_stack([np.ones(m.sum()), x1_[m], x2_[m]])
        try:
            beta = np.linalg.lstsq(X, y_[m], rcond=None)[0]
            return float(beta[2])
        except Exception:
            return np.nan
    out = pd.Series(np.nan, index=close.index)
    for i in range(DDAYS_2Y, len(combined)):
        out.iloc[i] = _gam(combined[i - DDAYS_2Y + 1:i + 1])
    return out


def f39_vclu_371_rv_5_minus_21_gap(close: pd.Series) -> pd.Series:
    """Realized variance at horizon 5 minus 21 (gap, annualized): RV5/5 − RV21/21."""
    r2 = _log_ret(close) ** 2
    return (r2.rolling(WDAYS, min_periods=2).sum() / WDAYS) - (r2.rolling(MDAYS, min_periods=WDAYS).sum() / MDAYS)


def f39_vclu_372_sigma21_iqr_252d(close: pd.Series) -> pd.Series:
    """IQR of σ_21 over 252d (p75 − p25)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return s.rolling(YDAYS, min_periods=QDAYS).quantile(0.75) - s.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)


def f39_vclu_373_quasi_garch_omega_intercept_252d(close: pd.Series) -> pd.Series:
    """Quasi-MLE GARCH ω̂: long-run-variance intercept proxy via mean r²·(1-persistence) over 252d."""
    r2 = _log_ret(close) ** 2
    rho = r2.rolling(YDAYS, min_periods=QDAYS).corr(r2.shift(1)).clip(upper=0.99, lower=-0.99)
    return r2.rolling(YDAYS, min_periods=QDAYS).mean() * (1.0 - rho.abs())


def f39_vclu_374_sigma_stable_alpha_proxy_252d(close: pd.Series) -> pd.Series:
    """Stable distribution α-tail proxy of σ_21 (McCulloch quantile estimator) over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)

    def _alpha(w):
        ww = w[~np.isnan(w)]
        if len(ww) < QDAYS:
            return np.nan
        q5, q25, q75, q95 = np.quantile(ww, [0.05, 0.25, 0.75, 0.95])
        denom = q75 - q25
        if denom <= 0:
            return np.nan
        v = (q95 - q5) / denom
        return float(np.interp(v, [2.439, 3.073, 4.451, 11.62], [2.0, 1.5, 1.0, 0.5]))
    return s.rolling(YDAYS, min_periods=QDAYS).apply(_alpha, raw=True)


def f39_vclu_375_sigma_short_residual_vs_long_252d(close: pd.Series) -> pd.Series:
    """Short-term residual std: std(σ_5 − rolling-252d-mean) over 252d."""
    r = _log_ret(close)
    s5 = _rolling_sigma(r, WDAYS)
    long_mean = s5.rolling(YDAYS, min_periods=QDAYS).mean()
    return (s5 - long_mean).rolling(YDAYS, min_periods=QDAYS).std()


# ============================================================
#                         REGISTRY 301-375
# ============================================================

VOLATILITY_CLUSTERING_BASE_REGISTRY_301_375 = {
    "f39_vclu_301_mean_high_vol_regime_duration_252d": {"inputs": ["close"], "func": f39_vclu_301_mean_high_vol_regime_duration_252d},
    "f39_vclu_302_mean_low_vol_regime_duration_252d": {"inputs": ["close"], "func": f39_vclu_302_mean_low_vol_regime_duration_252d},
    "f39_vclu_303_total_high_vol_time_504d": {"inputs": ["close"], "func": f39_vclu_303_total_high_vol_time_504d},
    "f39_vclu_304_total_low_vol_time_504d": {"inputs": ["close"], "func": f39_vclu_304_total_low_vol_time_504d},
    "f39_vclu_305_days_since_regime_change": {"inputs": ["close"], "func": f39_vclu_305_days_since_regime_change},
    "f39_vclu_306_high_vol_regime_persistence_252d": {"inputs": ["close"], "func": f39_vclu_306_high_vol_regime_persistence_252d},
    "f39_vclu_307_low_vol_regime_persistence_252d": {"inputs": ["close"], "func": f39_vclu_307_low_vol_regime_persistence_252d},
    "f39_vclu_308_regime_shift_recency_zscore_252d": {"inputs": ["close"], "func": f39_vclu_308_regime_shift_recency_zscore_252d},
    "f39_vclu_309_rise_vs_fall_duration_ratio_252d": {"inputs": ["close"], "func": f39_vclu_309_rise_vs_fall_duration_ratio_252d},
    "f39_vclu_310_rise_vs_fall_magnitude_ratio_252d": {"inputs": ["close"], "func": f39_vclu_310_rise_vs_fall_magnitude_ratio_252d},
    "f39_vclu_311_sigma_rise_5d_rate_252d": {"inputs": ["close"], "func": f39_vclu_311_sigma_rise_5d_rate_252d},
    "f39_vclu_312_sigma_acceleration_up_days_252d": {"inputs": ["close"], "func": f39_vclu_312_sigma_acceleration_up_days_252d},
    "f39_vclu_313_sigma_acceleration_down_days_252d": {"inputs": ["close"], "func": f39_vclu_313_sigma_acceleration_down_days_252d},
    "f39_vclu_314_sigma_momentum_asymmetry_252d": {"inputs": ["close"], "func": f39_vclu_314_sigma_momentum_asymmetry_252d},
    "f39_vclu_315_vov_in_rising_sigma_252d": {"inputs": ["close"], "func": f39_vclu_315_vov_in_rising_sigma_252d},
    "f39_vclu_316_vov_in_falling_sigma_252d": {"inputs": ["close"], "func": f39_vclu_316_vov_in_falling_sigma_252d},
    "f39_vclu_317_vovov_63d": {"inputs": ["close"], "func": f39_vclu_317_vovov_63d},
    "f39_vclu_318_skew_vov_63d": {"inputs": ["close"], "func": f39_vclu_318_skew_vov_63d},
    "f39_vclu_319_kurt_vov_63d": {"inputs": ["close"], "func": f39_vclu_319_kurt_vov_63d},
    "f39_vclu_320_relative_deviation_sigma_long_run": {"inputs": ["close"], "func": f39_vclu_320_relative_deviation_sigma_long_run},
    "f39_vclu_321_convergence_halflife_to_sigma_mean_252d": {"inputs": ["close"], "func": f39_vclu_321_convergence_halflife_to_sigma_mean_252d},
    "f39_vclu_322_sigma_deviation_in_long_run_units_252d": {"inputs": ["close"], "func": f39_vclu_322_sigma_deviation_in_long_run_units_252d},
    "f39_vclu_323_long_run_vol_stability_504d": {"inputs": ["close"], "func": f39_vclu_323_long_run_vol_stability_504d},
    "f39_vclu_324_ou_reversion_coef_sigma_252d": {"inputs": ["close"], "func": f39_vclu_324_ou_reversion_coef_sigma_252d},
    "f39_vclu_325_ou_long_run_mean_sigma_252d": {"inputs": ["close"], "func": f39_vclu_325_ou_long_run_mean_sigma_252d},
    "f39_vclu_326_autocorr_rsq_lag1_high_vol_252d": {"inputs": ["close"], "func": f39_vclu_326_autocorr_rsq_lag1_high_vol_252d},
    "f39_vclu_327_autocorr_rsq_lag1_low_vol_252d": {"inputs": ["close"], "func": f39_vclu_327_autocorr_rsq_lag1_low_vol_252d},
    "f39_vclu_328_autocorr_absr_lag1_high_vol_252d": {"inputs": ["close"], "func": f39_vclu_328_autocorr_absr_lag1_high_vol_252d},
    "f39_vclu_329_autocorr_absr_lag1_low_vol_252d": {"inputs": ["close"], "func": f39_vclu_329_autocorr_absr_lag1_low_vol_252d},
    "f39_vclu_330_autocorr_sigma_lag1_rising_252d": {"inputs": ["close"], "func": f39_vclu_330_autocorr_sigma_lag1_rising_252d},
    "f39_vclu_331_autocorr_sigma_lag1_falling_252d": {"inputs": ["close"], "func": f39_vclu_331_autocorr_sigma_lag1_falling_252d},
    "f39_vclu_332_sigma_memory_lag63_504d": {"inputs": ["close"], "func": f39_vclu_332_sigma_memory_lag63_504d},
    "f39_vclu_333_sigma_memory_lag126_504d": {"inputs": ["close"], "func": f39_vclu_333_sigma_memory_lag126_504d},
    "f39_vclu_334_sigma_memory_loss_rate_252d": {"inputs": ["close"], "func": f39_vclu_334_sigma_memory_loss_rate_252d},
    "f39_vclu_335_sigma_memory_completeness_252d": {"inputs": ["close"], "func": f39_vclu_335_sigma_memory_completeness_252d},
    "f39_vclu_336_sigma_long_memory_ratio_252d": {"inputs": ["close"], "func": f39_vclu_336_sigma_long_memory_ratio_252d},
    "f39_vclu_337_ar3_phi3_sigma21_252d": {"inputs": ["close"], "func": f39_vclu_337_ar3_phi3_sigma21_252d},
    "f39_vclu_338_ar5_phi5_sigma21_252d": {"inputs": ["close"], "func": f39_vclu_338_ar5_phi5_sigma21_252d},
    "f39_vclu_339_ar1_sigma5_252d": {"inputs": ["close"], "func": f39_vclu_339_ar1_sigma5_252d},
    "f39_vclu_340_ar1_sigma252_504d": {"inputs": ["close"], "func": f39_vclu_340_ar1_sigma252_504d},
    "f39_vclu_341_pp_stationarity_proxy_sigma_252d": {"inputs": ["close"], "func": f39_vclu_341_pp_stationarity_proxy_sigma_252d},
    "f39_vclu_342_ewma_forecast_error_var_21d": {"inputs": ["close"], "func": f39_vclu_342_ewma_forecast_error_var_21d},
    "f39_vclu_343_garch_forecast_error_var_252d": {"inputs": ["close"], "func": f39_vclu_343_garch_forecast_error_var_252d},
    "f39_vclu_344_mean_abs_forecast_error_21d": {"inputs": ["close"], "func": f39_vclu_344_mean_abs_forecast_error_21d},
    "f39_vclu_345_forecast_bias_252d": {"inputs": ["close"], "func": f39_vclu_345_forecast_bias_252d},
    "f39_vclu_346_forecast_error_skew_252d": {"inputs": ["close"], "func": f39_vclu_346_forecast_error_skew_252d},
    "f39_vclu_347_forecast_error_kurt_252d": {"inputs": ["close"], "func": f39_vclu_347_forecast_error_kurt_252d},
    "f39_vclu_348_corr_sigma5_lead_sigma21_5d_252d": {"inputs": ["close"], "func": f39_vclu_348_corr_sigma5_lead_sigma21_5d_252d},
    "f39_vclu_349_corr_sigma21_lead_sigma63_21d_252d": {"inputs": ["close"], "func": f39_vclu_349_corr_sigma21_lead_sigma63_21d_252d},
    "f39_vclu_350_granger_sigma5_to_sigma21_252d": {"inputs": ["close"], "func": f39_vclu_350_granger_sigma5_to_sigma21_252d},
    "f39_vclu_351_lead_lag_max_lag_sigma5_sigma21_252d": {"inputs": ["close"], "func": f39_vclu_351_lead_lag_max_lag_sigma5_sigma21_252d},
    "f39_vclu_352_corr_sigma5_lead_sigma252_21d_252d": {"inputs": ["close"], "func": f39_vclu_352_corr_sigma5_lead_sigma252_21d_252d},
    "f39_vclu_353_spike_then_collapse_count_252d": {"inputs": ["close"], "func": f39_vclu_353_spike_then_collapse_count_252d},
    "f39_vclu_354_spike_without_revert_count_252d": {"inputs": ["close"], "func": f39_vclu_354_spike_without_revert_count_252d},
    "f39_vclu_355_mean_sigma_decay_after_spike_252d": {"inputs": ["close"], "func": f39_vclu_355_mean_sigma_decay_after_spike_252d},
    "f39_vclu_356_sigma_step_event_count_252d": {"inputs": ["close"], "func": f39_vclu_356_sigma_step_event_count_252d},
    "f39_vclu_357_sigma_step_down_count_252d": {"inputs": ["close"], "func": f39_vclu_357_sigma_step_down_count_252d},
    "f39_vclu_358_sigma_step_up_count_252d": {"inputs": ["close"], "func": f39_vclu_358_sigma_step_up_count_252d},
    "f39_vclu_359_vov_spike_count_252d": {"inputs": ["close"], "func": f39_vclu_359_vov_spike_count_252d},
    "f39_vclu_360_coincident_sigma5_sigma21_spike_count_252d": {"inputs": ["close"], "func": f39_vclu_360_coincident_sigma5_sigma21_spike_count_252d},
    "f39_vclu_361_hmm_high_vol_prob_252d": {"inputs": ["close"], "func": f39_vclu_361_hmm_high_vol_prob_252d},
    "f39_vclu_362_hmm_high_to_low_transition_estimate_252d": {"inputs": ["close"], "func": f39_vclu_362_hmm_high_to_low_transition_estimate_252d},
    "f39_vclu_363_hmm_low_to_high_transition_estimate_252d": {"inputs": ["close"], "func": f39_vclu_363_hmm_low_to_high_transition_estimate_252d},
    "f39_vclu_364_hmm_steady_state_high_prob_252d": {"inputs": ["close"], "func": f39_vclu_364_hmm_steady_state_high_prob_252d},
    "f39_vclu_365_regime_shift_rate_252d": {"inputs": ["close"], "func": f39_vclu_365_regime_shift_rate_252d},
    "f39_vclu_366_sigma_trend_expected_vs_realized_252d": {"inputs": ["close"], "func": f39_vclu_366_sigma_trend_expected_vs_realized_252d},
    "f39_vclu_367_sigma_acceleration_d2_21d": {"inputs": ["close"], "func": f39_vclu_367_sigma_acceleration_d2_21d},
    "f39_vclu_368_vov_in_mean_reverting_state_252d": {"inputs": ["close"], "func": f39_vclu_368_vov_in_mean_reverting_state_252d},
    "f39_vclu_369_sigma_time_to_half_decay_252d": {"inputs": ["close"], "func": f39_vclu_369_sigma_time_to_half_decay_252d},
    "f39_vclu_370_gjr_asymmetry_504d": {"inputs": ["close"], "func": f39_vclu_370_gjr_asymmetry_504d},
    "f39_vclu_371_rv_5_minus_21_gap": {"inputs": ["close"], "func": f39_vclu_371_rv_5_minus_21_gap},
    "f39_vclu_372_sigma21_iqr_252d": {"inputs": ["close"], "func": f39_vclu_372_sigma21_iqr_252d},
    "f39_vclu_373_quasi_garch_omega_intercept_252d": {"inputs": ["close"], "func": f39_vclu_373_quasi_garch_omega_intercept_252d},
    "f39_vclu_374_sigma_stable_alpha_proxy_252d": {"inputs": ["close"], "func": f39_vclu_374_sigma_stable_alpha_proxy_252d},
    "f39_vclu_375_sigma_short_residual_vs_long_252d": {"inputs": ["close"], "func": f39_vclu_375_sigma_short_residual_vs_long_252d},
}
