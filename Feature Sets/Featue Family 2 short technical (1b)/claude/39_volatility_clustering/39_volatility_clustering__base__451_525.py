"""volatility_clustering base features 451-525 — Pipeline 1b-technical batch 4.

75 NEW fine-grained vol-clustering signals. Focus: σ-roof/floor tests, regime
transition magnitudes, forecast-accuracy features, drawdown-conditional σ,
recovery-conditional σ, σ-pattern signatures, σ-correlated-with-price, σ-vs-
trend relationships.

Inputs: SEP OHLCV only. PIT-clean. Self-contained.
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


def _bars_since(ind):
    arr = ind.fillna(0).astype(int).values
    out = np.full(len(arr), np.nan); bars = np.nan
    for i, x in enumerate(arr):
        if x: bars = 0
        elif np.isfinite(bars): bars = bars + 1
        out[i] = bars
    return pd.Series(out, index=ind.index)


# ============================================================
# Bucket A — σ-roof / σ-floor tests (451-460)
# ============================================================

def f39_vclu_451_sigma21_tests_504d_max_count_252d(close: pd.Series) -> pd.Series:
    """Count of bars where σ_21 within 5% of its trailing 504d-max (σ-roof tests), over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    mx = s.rolling(DDAYS_2Y, min_periods=YDAYS).max()
    return (s >= 0.95 * mx).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f39_vclu_452_sigma21_tests_504d_min_count_252d(close: pd.Series) -> pd.Series:
    """Count of bars where σ_21 within 5% of its trailing 504d-min (σ-floor tests), over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    mn = s.rolling(DDAYS_2Y, min_periods=YDAYS).min()
    return (s <= 1.05 * mn).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f39_vclu_453_sigma21_max_test_count_252d(close: pd.Series) -> pd.Series:
    """Count of σ_21 making a new 252d-max within 252d window."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    new_max = s >= s.rolling(YDAYS, min_periods=QDAYS).max()
    return new_max.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f39_vclu_454_sigma21_min_test_count_252d(close: pd.Series) -> pd.Series:
    """Count of σ_21 making a new 252d-min within 252d window."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    new_min = s <= s.rolling(YDAYS, min_periods=QDAYS).min()
    return new_min.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f39_vclu_455_sigma21_breakout_above_roof_count_252d(close: pd.Series) -> pd.Series:
    """Bars where σ_21 > 1.05·trailing-504d-p90 (vol-roof breakout) count over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p90_long = s.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.90)
    return (s > 1.05 * p90_long).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f39_vclu_456_sigma21_breakdown_below_floor_count_252d(close: pd.Series) -> pd.Series:
    """Bars where σ_21 < 0.95·trailing-504d-p10 (vol-floor breakdown) count over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p10_long = s.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.10)
    return (s < 0.95 * p10_long).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f39_vclu_457_bars_since_sigma21_roof_breach_252d(close: pd.Series) -> pd.Series:
    """Bars since σ_21 last exceeded 504d-p90."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p90 = s.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.90)
    return _bars_since((s > p90).astype(float))


def f39_vclu_458_bars_since_sigma21_floor_breach_252d(close: pd.Series) -> pd.Series:
    """Bars since σ_21 last fell below 504d-p10."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p10 = s.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.10)
    return _bars_since((s < p10).astype(float))


def f39_vclu_459_sigma21_distance_from_roof_252d(close: pd.Series) -> pd.Series:
    """1 − σ_21 / trailing 504d-max(σ_21) — distance from σ-roof, 0=at-roof."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return 1.0 - _safe_div(s, s.rolling(DDAYS_2Y, min_periods=YDAYS).max())


def f39_vclu_460_sigma21_distance_from_floor_252d(close: pd.Series) -> pd.Series:
    """σ_21 / trailing 504d-min(σ_21) − 1 — distance from σ-floor."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return _safe_div(s, s.rolling(DDAYS_2Y, min_periods=YDAYS).min()) - 1.0


# ============================================================
# Bucket B — Regime transition magnitudes (461-470)
# ============================================================

def f39_vclu_461_mean_sigma_jump_size_on_regime_change_252d(close: pd.Series) -> pd.Series:
    """Mean |Δσ_21| on bars where regime (above/below median) changes, over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    med = s.rolling(YDAYS, min_periods=QDAYS).median()
    above = (s > med)
    change = above != above.shift(1)
    return s.diff().abs().where(change, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f39_vclu_462_max_sigma_jump_size_on_regime_change_252d(close: pd.Series) -> pd.Series:
    """Max |Δσ_21| on regime-change bars over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    med = s.rolling(YDAYS, min_periods=QDAYS).median()
    above = (s > med)
    change = above != above.shift(1)
    return s.diff().abs().where(change, np.nan).rolling(YDAYS, min_periods=QDAYS).max()


def f39_vclu_463_sigma_magnitude_into_high_regime_252d(close: pd.Series) -> pd.Series:
    """Mean σ_21 on bars where σ entered high regime (from below to above median) over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    med = s.rolling(YDAYS, min_periods=QDAYS).median()
    above = (s > med).astype(int)
    enter_high = (above == 1) & (above.shift(1) == 0)
    return s.where(enter_high, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f39_vclu_464_sigma_magnitude_into_low_regime_252d(close: pd.Series) -> pd.Series:
    """Mean σ_21 on bars where σ entered low regime over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    med = s.rolling(YDAYS, min_periods=QDAYS).median()
    above = (s > med).astype(int)
    enter_low = (above == 0) & (above.shift(1) == 1)
    return s.where(enter_low, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f39_vclu_465_avg_high_regime_dwell_252d(close: pd.Series) -> pd.Series:
    """Mean duration of σ-high (above-median) regimes within 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    med = s.rolling(YDAYS, min_periods=QDAYS).median()
    hi = (s > med).astype(float).fillna(0.0)

    def _mean_dur(w):
        runs = []; cur = 0
        for v in w:
            if v > 0.5: cur += 1
            elif cur > 0: runs.append(cur); cur = 0
        if cur > 0: runs.append(cur)
        return float(np.mean(runs)) if runs else np.nan
    return hi.rolling(YDAYS, min_periods=QDAYS).apply(_mean_dur, raw=True)


def f39_vclu_466_avg_low_regime_dwell_252d(close: pd.Series) -> pd.Series:
    """Mean duration of σ-low (below-median) regimes within 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    med = s.rolling(YDAYS, min_periods=QDAYS).median()
    lo = (s < med).astype(float).fillna(0.0)

    def _mean_dur(w):
        runs = []; cur = 0
        for v in w:
            if v > 0.5: cur += 1
            elif cur > 0: runs.append(cur); cur = 0
        if cur > 0: runs.append(cur)
        return float(np.mean(runs)) if runs else np.nan
    return lo.rolling(YDAYS, min_periods=QDAYS).apply(_mean_dur, raw=True)


def f39_vclu_467_sigma_jump_252d_max_change(close: pd.Series) -> pd.Series:
    """Max |σ_21_t − σ_21_t-5| within 252d window — biggest 5d σ-shift."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return (s - s.shift(WDAYS)).abs().rolling(YDAYS, min_periods=QDAYS).max()


def f39_vclu_468_sigma_max_pct_change_252d(close: pd.Series) -> pd.Series:
    """Max |σ_21_t / σ_21_t-5 − 1| within 252d window — biggest 5d % σ-shift."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return _safe_div(s - s.shift(WDAYS), s.shift(WDAYS)).abs().rolling(YDAYS, min_periods=QDAYS).max()


def f39_vclu_469_sigma_transition_count_to_extreme_252d(close: pd.Series) -> pd.Series:
    """Transitions from inside [p25,p75] to outside (extreme regime entries) over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p25 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    p75 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    inside = (s >= p25) & (s <= p75)
    outside = ~inside
    transition = inside.shift(1).fillna(False) & outside
    return transition.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f39_vclu_470_sigma_transition_count_to_central_252d(close: pd.Series) -> pd.Series:
    """Transitions from outside [p25,p75] to inside (return-to-normal) over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p25 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    p75 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    inside = (s >= p25) & (s <= p75)
    outside = ~inside
    transition = outside.shift(1).fillna(False) & inside
    return transition.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket C — Forecast-accuracy features (471-480)
# ============================================================

def f39_vclu_471_ewma_forecast_mse_21d(close: pd.Series) -> pd.Series:
    """Mean squared forecast error: (r²_t − EWMA(r²,0.94)_{t-1})² over 21d."""
    r = _log_ret(close)
    pred = (r ** 2).ewm(alpha=0.06, min_periods=MDAYS).mean().shift(1)
    err = (r ** 2) - pred
    return (err ** 2).rolling(MDAYS, min_periods=WDAYS).mean()


def f39_vclu_472_ewma_forecast_mse_63d(close: pd.Series) -> pd.Series:
    """Mean squared forecast error over 63d."""
    r = _log_ret(close)
    pred = (r ** 2).ewm(alpha=0.06, min_periods=MDAYS).mean().shift(1)
    err = (r ** 2) - pred
    return (err ** 2).rolling(QDAYS, min_periods=MDAYS).mean()


def f39_vclu_473_ewma_forecast_relative_error_21d(close: pd.Series) -> pd.Series:
    """Mean |(r² − pred)| / pred over 21d (relative forecast error)."""
    r = _log_ret(close)
    pred = (r ** 2).ewm(alpha=0.06, min_periods=MDAYS).mean().shift(1)
    return _safe_div((r ** 2 - pred).abs(), pred).rolling(MDAYS, min_periods=WDAYS).mean()


def f39_vclu_474_sigma_underpredict_count_252d(close: pd.Series) -> pd.Series:
    """Count of bars where r² > 2·EWMA(r²)_{t-1} (vol underpredicted), over 252d."""
    r = _log_ret(close)
    pred = (r ** 2).ewm(alpha=0.06, min_periods=MDAYS).mean().shift(1)
    return (r ** 2 > 2 * pred).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f39_vclu_475_sigma_overpredict_count_252d(close: pd.Series) -> pd.Series:
    """Count of bars where r² < 0.25·EWMA(r²)_{t-1} (vol overpredicted), over 252d."""
    r = _log_ret(close)
    pred = (r ** 2).ewm(alpha=0.06, min_periods=MDAYS).mean().shift(1)
    return (r ** 2 < 0.25 * pred).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f39_vclu_476_forecast_directional_accuracy_252d(close: pd.Series) -> pd.Series:
    """Fraction of bars where sign(σ_t - σ_t-1) matches sign(σ_t-1 - σ_t-2) over 252d (trend-direction-accuracy)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    pred_dir = np.sign(s.shift(1) - s.shift(2))
    actual_dir = np.sign(s - s.shift(1))
    correct = (pred_dir == actual_dir) & (pred_dir != 0)
    return correct.astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f39_vclu_477_forecast_log_likelihood_252d(close: pd.Series) -> pd.Series:
    """Mean log-likelihood of r_t under N(0, EWMA_σ̂_{t-1}) over 252d."""
    r = _log_ret(close)
    sig_pred = np.sqrt((r ** 2).ewm(alpha=0.06, min_periods=MDAYS).mean().shift(1) + 1e-12)
    ll = -0.5 * (_safe_div(r ** 2, sig_pred ** 2) + 2 * _safe_log(sig_pred) + np.log(2 * np.pi))
    return ll.rolling(YDAYS, min_periods=QDAYS).mean()


def f39_vclu_478_forecast_residual_kurt_252d(close: pd.Series) -> pd.Series:
    """Kurt of standardized residuals z = r / σ̂_{t-1} over 252d (residual-tail-heaviness)."""
    r = _log_ret(close)
    sig_pred = np.sqrt((r ** 2).ewm(alpha=0.06, min_periods=MDAYS).mean().shift(1) + 1e-12)
    z = _safe_div(r, sig_pred)
    return z.rolling(YDAYS, min_periods=QDAYS).kurt()


def f39_vclu_479_forecast_residual_skew_252d(close: pd.Series) -> pd.Series:
    """Skew of standardized residuals over 252d."""
    r = _log_ret(close)
    sig_pred = np.sqrt((r ** 2).ewm(alpha=0.06, min_periods=MDAYS).mean().shift(1) + 1e-12)
    z = _safe_div(r, sig_pred)
    return z.rolling(YDAYS, min_periods=QDAYS).skew()


def f39_vclu_480_forecast_residual_autocorr_252d(close: pd.Series) -> pd.Series:
    """Autocorr(lag=1) of squared standardized residuals over 252d (remaining ARCH effect)."""
    r = _log_ret(close)
    sig_pred = np.sqrt((r ** 2).ewm(alpha=0.06, min_periods=MDAYS).mean().shift(1) + 1e-12)
    z2 = _safe_div(r ** 2, sig_pred ** 2)
    return z2.rolling(YDAYS, min_periods=QDAYS).corr(z2.shift(1))


# ============================================================
# Bucket D — Drawdown-conditional σ (481-490)
# ============================================================

def f39_vclu_481_sigma_in_drawdown_252d(close: pd.Series) -> pd.Series:
    """Mean σ_21 restricted to bars currently in drawdown (close < running 63d max) over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    rmax = close.rolling(QDAYS, min_periods=MDAYS).max()
    in_dd = close < rmax
    return s.where(in_dd, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f39_vclu_482_sigma_in_uptrend_252d(close: pd.Series) -> pd.Series:
    """Mean σ_21 restricted to bars at running 63d-max (uptrend) over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    rmax = close.rolling(QDAYS, min_periods=MDAYS).max()
    at_max = close >= rmax * 0.999
    return s.where(at_max, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f39_vclu_483_sigma_in_deep_dd_252d(close: pd.Series) -> pd.Series:
    """Mean σ_21 restricted to bars in >10% drawdown (close < 0.9 × 252d-max) over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    deep_dd = close < 0.9 * rmax
    return s.where(deep_dd, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f39_vclu_484_sigma_in_shallow_dd_252d(close: pd.Series) -> pd.Series:
    """Mean σ_21 in shallow drawdown (close in [0.95, 1.0]·252d-max) over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    shallow = (close >= 0.95 * rmax) & (close < rmax)
    return s.where(shallow, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f39_vclu_485_sigma_dd_depth_corr_252d(close: pd.Series) -> pd.Series:
    """Corr(σ_21, drawdown depth from 252d-max) over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd = 1.0 - _safe_div(close, rmax)
    return s.rolling(YDAYS, min_periods=QDAYS).corr(dd)


def f39_vclu_486_sigma_at_dd_start_252d(close: pd.Series) -> pd.Series:
    """Mean σ_21 on bars where drawdown begins (close < prior 63d-max for the first time in 21d) over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    rmax = close.rolling(QDAYS, min_periods=MDAYS).max()
    in_dd = (close < rmax)
    just_started = in_dd & ~in_dd.shift(1).fillna(False)
    return s.where(just_started, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f39_vclu_487_sigma_at_dd_trough_252d(close: pd.Series) -> pd.Series:
    """Mean σ_21 on bars where close hits a 63d-low (drawdown trough) over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    at_trough = (close <= close.rolling(QDAYS, min_periods=MDAYS).min())
    return s.where(at_trough, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f39_vclu_488_sigma_during_recovery_252d(close: pd.Series) -> pd.Series:
    """Mean σ_21 on bars during recovery: drawdown narrowing (close higher than 5d-prior)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    rmax = close.rolling(QDAYS, min_periods=MDAYS).max()
    in_dd = (close < rmax)
    recovering = in_dd & (close > close.shift(WDAYS))
    return s.where(recovering, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f39_vclu_489_sigma_at_recovery_complete_252d(close: pd.Series) -> pd.Series:
    """Mean σ_21 on bars where close recovers to new 63d-high after a drawdown."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    new_high_63d = (close >= close.rolling(QDAYS, min_periods=MDAYS).max() * 0.999)
    was_in_dd = (close.shift(WDAYS) < close.shift(WDAYS).rolling(QDAYS, min_periods=MDAYS).max() * 0.99)
    recovery = new_high_63d & was_in_dd
    return s.where(recovery, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f39_vclu_490_sigma_dd_velocity_corr_252d(close: pd.Series) -> pd.Series:
    """Corr(σ_21, daily change in drawdown depth) over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    rmax = close.rolling(QDAYS, min_periods=MDAYS).max()
    dd = 1.0 - _safe_div(close, rmax)
    return s.rolling(YDAYS, min_periods=QDAYS).corr(dd.diff())


# ============================================================
# Bucket E — σ-pattern signatures (491-500)
# ============================================================

def f39_vclu_491_sigma21_double_top_count_504d(close: pd.Series) -> pd.Series:
    """Count of σ_21 "double-top" patterns: 2 peaks within 0.95-1.05 ratio within 63d, over 504d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)

    def _dtops(w):
        ww = w[~np.isnan(w)]
        if len(ww) < QDAYS: return np.nan
        # find local maxima
        peaks = []
        for i in range(1, len(ww) - 1):
            if ww[i] > ww[i-1] and ww[i] > ww[i+1]:
                peaks.append((i, ww[i]))
        cnt = 0
        for i in range(len(peaks) - 1):
            for j in range(i + 1, len(peaks)):
                if peaks[j][0] - peaks[i][0] > QDAYS: break
                ratio = peaks[j][1] / peaks[i][1] if peaks[i][1] != 0 else 0
                if 0.95 <= ratio <= 1.05:
                    cnt += 1
        return float(cnt)
    return s.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_dtops, raw=True)


def f39_vclu_492_sigma21_compression_to_expansion_count_252d(close: pd.Series) -> pd.Series:
    """σ-compression → σ-expansion: σ_21 below p10 followed within 21d by σ_21 above p90, count 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p10 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.10)
    p90 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    compressed_lag = (s.shift(MDAYS) < p10.shift(MDAYS))
    expanded_now = (s > p90)
    return (compressed_lag & expanded_now).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f39_vclu_493_sigma21_long_stable_run_252d(close: pd.Series) -> pd.Series:
    """Max run length of σ_21 inside [p40, p60] over 252d (long stable σ regime)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p40 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.40)
    p60 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.60)
    stable = ((s >= p40) & (s <= p60)).astype(float).fillna(0.0)

    def _run(w):
        m = 0; c = 0
        for v in w:
            if v > 0.5: c += 1; m = c if c > m else m
            else: c = 0
        return float(m)
    return stable.rolling(YDAYS, min_periods=QDAYS).apply(_run, raw=True)


def f39_vclu_494_sigma21_zigzag_count_63d(close: pd.Series) -> pd.Series:
    """Count of σ_21 "zigzag" reversals (sign(Δσ) changes) over 63d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    sign_chg = np.sign(s.diff()).diff().abs() > 0
    return sign_chg.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f39_vclu_495_sigma21_volatility_explosion_count_63d(close: pd.Series) -> pd.Series:
    """Count of bars where σ_21 > 2·σ_21.shift(21) over 63d (σ-explosion events)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return (s > 2 * s.shift(MDAYS)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f39_vclu_496_sigma21_implosion_count_63d(close: pd.Series) -> pd.Series:
    """Count of bars where σ_21 < 0.5·σ_21.shift(21) over 63d (σ-implosion events)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return (s < 0.5 * s.shift(MDAYS)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f39_vclu_497_sigma21_smooth_rise_count_252d(close: pd.Series) -> pd.Series:
    """Count of bars where σ_21 has been rising for 10+ consecutive days, over 252d (smooth-rise persistence)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    rising = (s.diff() > 0).fillna(False)
    ten_in_row = rising
    for k in range(1, 10):
        ten_in_row = ten_in_row & rising.shift(k).fillna(False)
    return ten_in_row.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f39_vclu_498_sigma21_smooth_fall_count_252d(close: pd.Series) -> pd.Series:
    """Count of bars where σ_21 has been falling for 10+ consecutive days, over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    falling = (s.diff() < 0).fillna(False)
    ten_in_row = falling
    for k in range(1, 10):
        ten_in_row = ten_in_row & falling.shift(k).fillna(False)
    return ten_in_row.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f39_vclu_499_sigma21_v_pattern_count_252d(close: pd.Series) -> pd.Series:
    """V-pattern: σ falling for 5+ days, then rising for 5+ days; count over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    falling = (s.diff() < 0).rolling(WDAYS, min_periods=2).min().astype(bool)  # all falling in last 5
    rising_lag = (s.shift(WDAYS).diff() > 0).rolling(WDAYS, min_periods=2).min().astype(bool)
    # Restate causally: bars where past 5d were rising AND prior 5d were falling
    rising_now = (s.diff() > 0).rolling(WDAYS, min_periods=2).min().astype(bool)
    falling_prior = (s.shift(WDAYS).diff() < 0).rolling(WDAYS, min_periods=2).min().astype(bool)
    return (rising_now & falling_prior).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f39_vclu_500_sigma21_inverted_v_count_252d(close: pd.Series) -> pd.Series:
    """Inverted-V: σ rising 5d then falling 5d, over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    falling_now = (s.diff() < 0).rolling(WDAYS, min_periods=2).min().astype(bool)
    rising_prior = (s.shift(WDAYS).diff() > 0).rolling(WDAYS, min_periods=2).min().astype(bool)
    return (falling_now & rising_prior).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket F — σ-correlated-with-price (501-510)
# ============================================================

def f39_vclu_501_corr_sigma21_price_63d(close: pd.Series) -> pd.Series:
    """Rolling 63d corr(σ_21, close)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return s.rolling(QDAYS, min_periods=MDAYS).corr(close)


def f39_vclu_502_corr_sigma21_price_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d corr(σ_21, close)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return s.rolling(YDAYS, min_periods=QDAYS).corr(close)


def f39_vclu_503_corr_sigma21_log_price_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d corr(σ_21, log(close))."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return s.rolling(YDAYS, min_periods=QDAYS).corr(_safe_log(close))


def f39_vclu_504_corr_sigma21_21d_return_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d corr(σ_21, 21d trailing log-return)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    r21 = _safe_log(close) - _safe_log(close.shift(MDAYS))
    return s.rolling(YDAYS, min_periods=QDAYS).corr(r21)


def f39_vclu_505_corr_dsigma_dprice_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d corr(Δσ_21, Δclose) — vol-price-change coupling."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return s.diff().rolling(YDAYS, min_periods=QDAYS).corr(close.diff())


def f39_vclu_506_corr_sigma21_drawdown_depth_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d corr(σ_21, drawdown depth from 252d-max)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd = 1.0 - _safe_div(close, rmax)
    return s.rolling(YDAYS, min_periods=QDAYS).corr(dd)


def f39_vclu_507_corr_sigma21_close_range_pos_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Rolling 252d corr(σ_21, close-position-in-252d-range)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    h252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    l252 = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - l252, h252 - l252)
    return s.rolling(YDAYS, min_periods=QDAYS).corr(pos)


def f39_vclu_508_sigma_rises_with_price_count_252d(close: pd.Series) -> pd.Series:
    """Bars where σ_21 AND close both increase, count over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return ((s.diff() > 0) & (close.diff() > 0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f39_vclu_509_sigma_rises_price_falls_count_252d(close: pd.Series) -> pd.Series:
    """Bars where σ_21 rises AND close falls, count over 252d (leverage effect)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return ((s.diff() > 0) & (close.diff() < 0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f39_vclu_510_corr_sigma_price_at_252d_high_252d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Mean σ_21 on bars within 5% of 252d-high (vol at peak)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    h252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    near_high = close >= 0.95 * h252
    return s.where(near_high, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


# ============================================================
# Bucket G — Recovery-conditional σ (511-520)
# ============================================================

def f39_vclu_511_sigma_post_5pct_decline_252d(close: pd.Series) -> pd.Series:
    """Mean σ_21 in 21 bars after a 5% decline (5d return < -5%), over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    r5_lag = (_safe_log(close).shift(MDAYS) - _safe_log(close.shift(MDAYS + WDAYS)))
    decline_lag = r5_lag < -0.05
    return s.where(decline_lag, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f39_vclu_512_sigma_post_10pct_decline_252d(close: pd.Series) -> pd.Series:
    """Mean σ_21 in 21 bars after a 10% decline, over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    r5_lag = (_safe_log(close).shift(MDAYS) - _safe_log(close.shift(MDAYS + WDAYS)))
    decline_lag = r5_lag < -0.10
    return s.where(decline_lag, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f39_vclu_513_sigma_post_5pct_rally_252d(close: pd.Series) -> pd.Series:
    """Mean σ_21 in 21 bars after a 5% rally, over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    r5_lag = (_safe_log(close).shift(MDAYS) - _safe_log(close.shift(MDAYS + WDAYS)))
    rally_lag = r5_lag > 0.05
    return s.where(rally_lag, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f39_vclu_514_sigma_post_10pct_rally_252d(close: pd.Series) -> pd.Series:
    """Mean σ_21 in 21 bars after a 10% rally, over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    r5_lag = (_safe_log(close).shift(MDAYS) - _safe_log(close.shift(MDAYS + WDAYS)))
    rally_lag = r5_lag > 0.10
    return s.where(rally_lag, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f39_vclu_515_sigma_ratio_post_decline_vs_pre(close: pd.Series) -> pd.Series:
    """Mean (σ_21_post5d / σ_21_pre5d) where prior 5d had >5% decline, over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    r5_lag = (_safe_log(close).shift(MDAYS) - _safe_log(close.shift(MDAYS + WDAYS)))
    decline_lag = r5_lag < -0.05
    ratio = _safe_div(s, s.shift(MDAYS + WDAYS))
    return ratio.where(decline_lag, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f39_vclu_516_sigma_5d_after_recovery_to_high_252d(close: pd.Series) -> pd.Series:
    """Mean σ_21 5d after close hits 252d-high (recovery completion), over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    was_at_high = (close.shift(WDAYS) >= close.shift(WDAYS).rolling(YDAYS, min_periods=QDAYS).max() * 0.999)
    return s.where(was_at_high, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f39_vclu_517_sigma_during_consolidation_252d(close: pd.Series) -> pd.Series:
    """Mean σ_21 during 21d-consolidation (21d range < 5% of mean close), over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    range21 = close.rolling(MDAYS, min_periods=WDAYS).max() - close.rolling(MDAYS, min_periods=WDAYS).min()
    mean21 = close.rolling(MDAYS, min_periods=WDAYS).mean()
    consolidation = _safe_div(range21, mean21) < 0.05
    return s.where(consolidation, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f39_vclu_518_sigma_during_trending_252d(close: pd.Series) -> pd.Series:
    """Mean σ_21 during trending periods (|21d return| > 10%), over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    r21 = (_safe_log(close) - _safe_log(close.shift(MDAYS)))
    trending = r21.abs() > 0.10
    return s.where(trending, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f39_vclu_519_sigma_during_choppy_252d(close: pd.Series) -> pd.Series:
    """Mean σ_21 during choppy periods (|21d return| < 2%), over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    r21 = (_safe_log(close) - _safe_log(close.shift(MDAYS)))
    choppy = r21.abs() < 0.02
    return s.where(choppy, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f39_vclu_520_sigma_during_high_close_pos_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean σ_21 when close in top quartile of 21d range, over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    h21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    l21 = low.rolling(MDAYS, min_periods=WDAYS).min()
    pos = _safe_div(close - l21, h21 - l21)
    in_top = pos > 0.75
    return s.where(in_top, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


# ============================================================
# Bucket H — Final misc (521-525)
# ============================================================

def f39_vclu_521_sigma21_above_p90_consecutive_252d(close: pd.Series) -> pd.Series:
    """Longest consecutive run of σ_21 > 252d-p90 within 252d window."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p90 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    above = (s > p90).astype(float).fillna(0.0)

    def _run(w):
        m = 0; c = 0
        for v in w:
            if v > 0.5: c += 1; m = c if c > m else m
            else: c = 0
        return float(m)
    return above.rolling(YDAYS, min_periods=QDAYS).apply(_run, raw=True)


def f39_vclu_522_sigma21_below_p10_consecutive_252d(close: pd.Series) -> pd.Series:
    """Longest consecutive run of σ_21 < 252d-p10 within 252d window."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p10 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.10)
    below = (s < p10).astype(float).fillna(0.0)

    def _run(w):
        m = 0; c = 0
        for v in w:
            if v > 0.5: c += 1; m = c if c > m else m
            else: c = 0
        return float(m)
    return below.rolling(YDAYS, min_periods=QDAYS).apply(_run, raw=True)


def f39_vclu_523_sigma_above_mean_pct_504d(close: pd.Series) -> pd.Series:
    """Fraction of bars where σ_21 > rolling 504d mean over 504d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    mu504 = s.rolling(DDAYS_2Y, min_periods=YDAYS).mean()
    return (s > mu504).astype(float).rolling(DDAYS_2Y, min_periods=YDAYS).mean()


def f39_vclu_524_sigma21_change_skew_252d(close: pd.Series) -> pd.Series:
    """Skew of Δσ_21 over 252d (sigma-change asymmetry)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return s.diff().rolling(YDAYS, min_periods=QDAYS).skew()


def f39_vclu_525_sigma_realized_minus_implied_via_pred_252d(close: pd.Series) -> pd.Series:
    """Mean (σ_21 − EWMA σ̂) over 252d — realized vs implied (forecast) gap."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    r = _log_ret(close)
    sig_pred = np.sqrt((r ** 2).ewm(alpha=0.06, min_periods=MDAYS).mean().shift(1) + 1e-12)
    return (s - sig_pred).rolling(YDAYS, min_periods=QDAYS).mean()


# ============================================================
#                         REGISTRY 451-525
# ============================================================

VOLATILITY_CLUSTERING_BASE_REGISTRY_451_525 = {
    "f39_vclu_451_sigma21_tests_504d_max_count_252d": {"inputs": ["close"], "func": f39_vclu_451_sigma21_tests_504d_max_count_252d},
    "f39_vclu_452_sigma21_tests_504d_min_count_252d": {"inputs": ["close"], "func": f39_vclu_452_sigma21_tests_504d_min_count_252d},
    "f39_vclu_453_sigma21_max_test_count_252d": {"inputs": ["close"], "func": f39_vclu_453_sigma21_max_test_count_252d},
    "f39_vclu_454_sigma21_min_test_count_252d": {"inputs": ["close"], "func": f39_vclu_454_sigma21_min_test_count_252d},
    "f39_vclu_455_sigma21_breakout_above_roof_count_252d": {"inputs": ["close"], "func": f39_vclu_455_sigma21_breakout_above_roof_count_252d},
    "f39_vclu_456_sigma21_breakdown_below_floor_count_252d": {"inputs": ["close"], "func": f39_vclu_456_sigma21_breakdown_below_floor_count_252d},
    "f39_vclu_457_bars_since_sigma21_roof_breach_252d": {"inputs": ["close"], "func": f39_vclu_457_bars_since_sigma21_roof_breach_252d},
    "f39_vclu_458_bars_since_sigma21_floor_breach_252d": {"inputs": ["close"], "func": f39_vclu_458_bars_since_sigma21_floor_breach_252d},
    "f39_vclu_459_sigma21_distance_from_roof_252d": {"inputs": ["close"], "func": f39_vclu_459_sigma21_distance_from_roof_252d},
    "f39_vclu_460_sigma21_distance_from_floor_252d": {"inputs": ["close"], "func": f39_vclu_460_sigma21_distance_from_floor_252d},
    "f39_vclu_461_mean_sigma_jump_size_on_regime_change_252d": {"inputs": ["close"], "func": f39_vclu_461_mean_sigma_jump_size_on_regime_change_252d},
    "f39_vclu_462_max_sigma_jump_size_on_regime_change_252d": {"inputs": ["close"], "func": f39_vclu_462_max_sigma_jump_size_on_regime_change_252d},
    "f39_vclu_463_sigma_magnitude_into_high_regime_252d": {"inputs": ["close"], "func": f39_vclu_463_sigma_magnitude_into_high_regime_252d},
    "f39_vclu_464_sigma_magnitude_into_low_regime_252d": {"inputs": ["close"], "func": f39_vclu_464_sigma_magnitude_into_low_regime_252d},
    "f39_vclu_465_avg_high_regime_dwell_252d": {"inputs": ["close"], "func": f39_vclu_465_avg_high_regime_dwell_252d},
    "f39_vclu_466_avg_low_regime_dwell_252d": {"inputs": ["close"], "func": f39_vclu_466_avg_low_regime_dwell_252d},
    "f39_vclu_467_sigma_jump_252d_max_change": {"inputs": ["close"], "func": f39_vclu_467_sigma_jump_252d_max_change},
    "f39_vclu_468_sigma_max_pct_change_252d": {"inputs": ["close"], "func": f39_vclu_468_sigma_max_pct_change_252d},
    "f39_vclu_469_sigma_transition_count_to_extreme_252d": {"inputs": ["close"], "func": f39_vclu_469_sigma_transition_count_to_extreme_252d},
    "f39_vclu_470_sigma_transition_count_to_central_252d": {"inputs": ["close"], "func": f39_vclu_470_sigma_transition_count_to_central_252d},
    "f39_vclu_471_ewma_forecast_mse_21d": {"inputs": ["close"], "func": f39_vclu_471_ewma_forecast_mse_21d},
    "f39_vclu_472_ewma_forecast_mse_63d": {"inputs": ["close"], "func": f39_vclu_472_ewma_forecast_mse_63d},
    "f39_vclu_473_ewma_forecast_relative_error_21d": {"inputs": ["close"], "func": f39_vclu_473_ewma_forecast_relative_error_21d},
    "f39_vclu_474_sigma_underpredict_count_252d": {"inputs": ["close"], "func": f39_vclu_474_sigma_underpredict_count_252d},
    "f39_vclu_475_sigma_overpredict_count_252d": {"inputs": ["close"], "func": f39_vclu_475_sigma_overpredict_count_252d},
    "f39_vclu_476_forecast_directional_accuracy_252d": {"inputs": ["close"], "func": f39_vclu_476_forecast_directional_accuracy_252d},
    "f39_vclu_477_forecast_log_likelihood_252d": {"inputs": ["close"], "func": f39_vclu_477_forecast_log_likelihood_252d},
    "f39_vclu_478_forecast_residual_kurt_252d": {"inputs": ["close"], "func": f39_vclu_478_forecast_residual_kurt_252d},
    "f39_vclu_479_forecast_residual_skew_252d": {"inputs": ["close"], "func": f39_vclu_479_forecast_residual_skew_252d},
    "f39_vclu_480_forecast_residual_autocorr_252d": {"inputs": ["close"], "func": f39_vclu_480_forecast_residual_autocorr_252d},
    "f39_vclu_481_sigma_in_drawdown_252d": {"inputs": ["close"], "func": f39_vclu_481_sigma_in_drawdown_252d},
    "f39_vclu_482_sigma_in_uptrend_252d": {"inputs": ["close"], "func": f39_vclu_482_sigma_in_uptrend_252d},
    "f39_vclu_483_sigma_in_deep_dd_252d": {"inputs": ["close"], "func": f39_vclu_483_sigma_in_deep_dd_252d},
    "f39_vclu_484_sigma_in_shallow_dd_252d": {"inputs": ["close"], "func": f39_vclu_484_sigma_in_shallow_dd_252d},
    "f39_vclu_485_sigma_dd_depth_corr_252d": {"inputs": ["close"], "func": f39_vclu_485_sigma_dd_depth_corr_252d},
    "f39_vclu_486_sigma_at_dd_start_252d": {"inputs": ["close"], "func": f39_vclu_486_sigma_at_dd_start_252d},
    "f39_vclu_487_sigma_at_dd_trough_252d": {"inputs": ["close"], "func": f39_vclu_487_sigma_at_dd_trough_252d},
    "f39_vclu_488_sigma_during_recovery_252d": {"inputs": ["close"], "func": f39_vclu_488_sigma_during_recovery_252d},
    "f39_vclu_489_sigma_at_recovery_complete_252d": {"inputs": ["close"], "func": f39_vclu_489_sigma_at_recovery_complete_252d},
    "f39_vclu_490_sigma_dd_velocity_corr_252d": {"inputs": ["close"], "func": f39_vclu_490_sigma_dd_velocity_corr_252d},
    "f39_vclu_491_sigma21_double_top_count_504d": {"inputs": ["close"], "func": f39_vclu_491_sigma21_double_top_count_504d},
    "f39_vclu_492_sigma21_compression_to_expansion_count_252d": {"inputs": ["close"], "func": f39_vclu_492_sigma21_compression_to_expansion_count_252d},
    "f39_vclu_493_sigma21_long_stable_run_252d": {"inputs": ["close"], "func": f39_vclu_493_sigma21_long_stable_run_252d},
    "f39_vclu_494_sigma21_zigzag_count_63d": {"inputs": ["close"], "func": f39_vclu_494_sigma21_zigzag_count_63d},
    "f39_vclu_495_sigma21_volatility_explosion_count_63d": {"inputs": ["close"], "func": f39_vclu_495_sigma21_volatility_explosion_count_63d},
    "f39_vclu_496_sigma21_implosion_count_63d": {"inputs": ["close"], "func": f39_vclu_496_sigma21_implosion_count_63d},
    "f39_vclu_497_sigma21_smooth_rise_count_252d": {"inputs": ["close"], "func": f39_vclu_497_sigma21_smooth_rise_count_252d},
    "f39_vclu_498_sigma21_smooth_fall_count_252d": {"inputs": ["close"], "func": f39_vclu_498_sigma21_smooth_fall_count_252d},
    "f39_vclu_499_sigma21_v_pattern_count_252d": {"inputs": ["close"], "func": f39_vclu_499_sigma21_v_pattern_count_252d},
    "f39_vclu_500_sigma21_inverted_v_count_252d": {"inputs": ["close"], "func": f39_vclu_500_sigma21_inverted_v_count_252d},
    "f39_vclu_501_corr_sigma21_price_63d": {"inputs": ["close"], "func": f39_vclu_501_corr_sigma21_price_63d},
    "f39_vclu_502_corr_sigma21_price_252d": {"inputs": ["close"], "func": f39_vclu_502_corr_sigma21_price_252d},
    "f39_vclu_503_corr_sigma21_log_price_252d": {"inputs": ["close"], "func": f39_vclu_503_corr_sigma21_log_price_252d},
    "f39_vclu_504_corr_sigma21_21d_return_252d": {"inputs": ["close"], "func": f39_vclu_504_corr_sigma21_21d_return_252d},
    "f39_vclu_505_corr_dsigma_dprice_252d": {"inputs": ["close"], "func": f39_vclu_505_corr_dsigma_dprice_252d},
    "f39_vclu_506_corr_sigma21_drawdown_depth_252d": {"inputs": ["close"], "func": f39_vclu_506_corr_sigma21_drawdown_depth_252d},
    "f39_vclu_507_corr_sigma21_close_range_pos_252d": {"inputs": ["close", "high", "low"], "func": f39_vclu_507_corr_sigma21_close_range_pos_252d},
    "f39_vclu_508_sigma_rises_with_price_count_252d": {"inputs": ["close"], "func": f39_vclu_508_sigma_rises_with_price_count_252d},
    "f39_vclu_509_sigma_rises_price_falls_count_252d": {"inputs": ["close"], "func": f39_vclu_509_sigma_rises_price_falls_count_252d},
    "f39_vclu_510_corr_sigma_price_at_252d_high_252d": {"inputs": ["close", "high"], "func": f39_vclu_510_corr_sigma_price_at_252d_high_252d},
    "f39_vclu_511_sigma_post_5pct_decline_252d": {"inputs": ["close"], "func": f39_vclu_511_sigma_post_5pct_decline_252d},
    "f39_vclu_512_sigma_post_10pct_decline_252d": {"inputs": ["close"], "func": f39_vclu_512_sigma_post_10pct_decline_252d},
    "f39_vclu_513_sigma_post_5pct_rally_252d": {"inputs": ["close"], "func": f39_vclu_513_sigma_post_5pct_rally_252d},
    "f39_vclu_514_sigma_post_10pct_rally_252d": {"inputs": ["close"], "func": f39_vclu_514_sigma_post_10pct_rally_252d},
    "f39_vclu_515_sigma_ratio_post_decline_vs_pre": {"inputs": ["close"], "func": f39_vclu_515_sigma_ratio_post_decline_vs_pre},
    "f39_vclu_516_sigma_5d_after_recovery_to_high_252d": {"inputs": ["close"], "func": f39_vclu_516_sigma_5d_after_recovery_to_high_252d},
    "f39_vclu_517_sigma_during_consolidation_252d": {"inputs": ["close"], "func": f39_vclu_517_sigma_during_consolidation_252d},
    "f39_vclu_518_sigma_during_trending_252d": {"inputs": ["close"], "func": f39_vclu_518_sigma_during_trending_252d},
    "f39_vclu_519_sigma_during_choppy_252d": {"inputs": ["close"], "func": f39_vclu_519_sigma_during_choppy_252d},
    "f39_vclu_520_sigma_during_high_close_pos_252d": {"inputs": ["close", "high", "low"], "func": f39_vclu_520_sigma_during_high_close_pos_252d},
    "f39_vclu_521_sigma21_above_p90_consecutive_252d": {"inputs": ["close"], "func": f39_vclu_521_sigma21_above_p90_consecutive_252d},
    "f39_vclu_522_sigma21_below_p10_consecutive_252d": {"inputs": ["close"], "func": f39_vclu_522_sigma21_below_p10_consecutive_252d},
    "f39_vclu_523_sigma_above_mean_pct_504d": {"inputs": ["close"], "func": f39_vclu_523_sigma_above_mean_pct_504d},
    "f39_vclu_524_sigma21_change_skew_252d": {"inputs": ["close"], "func": f39_vclu_524_sigma21_change_skew_252d},
    "f39_vclu_525_sigma_realized_minus_implied_via_pred_252d": {"inputs": ["close"], "func": f39_vclu_525_sigma_realized_minus_implied_via_pred_252d},
}
