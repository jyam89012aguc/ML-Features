"""atr_expansion_dynamics base features 376-450 — Pipeline 1b-technical extension batch 3 cont.

75 NEW fine-grained ATR/range signals. Focus: realized intraday vol (range/close ratios),
TR pattern signatures (monotonic runs, oscillation, step-events), ATR-MACD-style derivatives,
range-vs-return coupling, ATR-cone diagonals, range autocorrelation structure (PACF), post-
peak ATR regime features, range conditional on close-position (bullish vs bearish close TR),
time-of-cycle ATR (since last peak / trough), final misc fine-grained signals.

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


def _ema(s, n):
    return s.ewm(span=n, min_periods=n, adjust=False).mean()


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


# ============================================================
# Bucket A — Realized intraday vol (376-381)
# ============================================================

def f40_atxd_376_hl_over_close_mean_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean (high - low) / close over 21d (intraday range as fraction of price)."""
    return _safe_div(high - low, close).rolling(MDAYS, min_periods=WDAYS).mean()


def f40_atxd_377_hl_over_open_mean_21d(open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean (high - low) / open over 21d."""
    return _safe_div(high - low, open).rolling(MDAYS, min_periods=WDAYS).mean()


def f40_atxd_378_hl_variance_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Variance of (high - low) over 21d (intraday range variability)."""
    return (high - low).rolling(MDAYS, min_periods=WDAYS).var()


def f40_atxd_379_hl_skew_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Skew of (high - low) over 21d."""
    return (high - low).rolling(MDAYS, min_periods=WDAYS).skew()


def f40_atxd_380_hl_minus_ema21_deviation(high: pd.Series, low: pd.Series) -> pd.Series:
    """(high - low) − EMA-21 of (high - low) — deviation from intraday-range trend."""
    rng = high - low
    return rng - _ema(rng, MDAYS)


def f40_atxd_381_hl_zscore_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of (high - low) over trailing 252d."""
    return _rolling_zscore(high - low, YDAYS)


# ============================================================
# Bucket B — Specific TR pattern signatures (382-389)
# ============================================================

def f40_atxd_382_tr_monotonic_rise_streak_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Longest streak of TR_t > TR_{t-1} > TR_{t-2} (monotonic rise) within 63d."""
    tr = _true_range(high, low, close)
    monoup = ((tr > tr.shift(1)) & (tr.shift(1) > tr.shift(2))).astype(float).fillna(0.0)

    def _run(w):
        m = 0; c = 0
        for v in w:
            if v > 0.5: c += 1; m = c if c > m else m
            else: c = 0
        return float(m)
    return monoup.rolling(QDAYS, min_periods=MDAYS).apply(_run, raw=True)


def f40_atxd_383_tr_monotonic_fall_streak_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Longest streak of TR_t < TR_{t-1} < TR_{t-2} (monotonic fall) within 63d."""
    tr = _true_range(high, low, close)
    monodn = ((tr < tr.shift(1)) & (tr.shift(1) < tr.shift(2))).astype(float).fillna(0.0)

    def _run(w):
        m = 0; c = 0
        for v in w:
            if v > 0.5: c += 1; m = c if c > m else m
            else: c = 0
        return float(m)
    return monodn.rolling(QDAYS, min_periods=MDAYS).apply(_run, raw=True)


def f40_atxd_384_tr_alternating_count_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of alternating TR patterns (TR_t > TR_{t-1} AND TR_{t-1} < TR_{t-2}) over 63d."""
    tr = _true_range(high, low, close)
    alt = ((tr > tr.shift(1)) & (tr.shift(1) < tr.shift(2))).astype(float)
    return alt.rolling(QDAYS, min_periods=MDAYS).sum()


def f40_atxd_385_tr_alternation_frequency_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Frequency of TR-direction alternations (ΔTR sign-changes per bar) over 252d."""
    tr = _true_range(high, low, close)
    return np.sign(tr.diff()).diff().abs().rolling(YDAYS, min_periods=QDAYS).mean()


def f40_atxd_386_tr_oscillation_count_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of ΔTR sign-changes over 21d (short-horizon range oscillation)."""
    tr = _true_range(high, low, close)
    return np.sign(tr.diff()).diff().abs().rolling(MDAYS, min_periods=WDAYS).sum()


def f40_atxd_387_tr_mean_reversion_rate_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of bars where ΔTR sign reverts within 1 bar (mean-reversion frequency)."""
    tr = _true_range(high, low, close)
    sign = np.sign(tr.diff())
    reverts = (sign != sign.shift(1)).astype(float)
    return reverts.rolling(YDAYS, min_periods=QDAYS).mean()


def f40_atxd_388_tr_step_event_count_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of |ΔTR| > 1·std-of-ΔTR over 252d (TR-step events)."""
    tr = _true_range(high, low, close)
    sigma_dtr = tr.diff().rolling(MDAYS, min_periods=WDAYS).std()
    return (tr.diff().abs() > sigma_dtr).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f40_atxd_389_tr_step_signed_sum_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Σ signed ΔTR over 63d (net TR-shift)."""
    return _true_range(high, low, close).diff().rolling(QDAYS, min_periods=MDAYS).sum()


# ============================================================
# Bucket C — ATR-MACD-style derivatives (390-394)
# ============================================================

def f40_atxd_390_atr_macd_12_26(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-MACD: ATR(12) - ATR(26) — bullish-vol vs bearish-vol oscillator."""
    return _atr(high, low, close, 12) - _atr(high, low, close, 26)


def f40_atxd_391_atr_macd_hist_9_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-MACD histogram: (ATR(12)-ATR(26)) − EMA-9 of itself."""
    macd = _atr(high, low, close, 12) - _atr(high, low, close, 26)
    return macd - _ema(macd, 9)


def f40_atxd_392_atr_macd_50_200(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-MACD long: ATR(50) - ATR(200) — long-term vol-regime oscillator."""
    return _atr(high, low, close, 50) - _atr(high, low, close, 200)


def f40_atxd_393_atr_macd_crossings_count_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of ATR-MACD line crossings of zero over 252d."""
    macd = _atr(high, low, close, 12) - _atr(high, low, close, 26)
    above = (macd > 0).astype(float)
    return above.diff().abs().rolling(YDAYS, min_periods=QDAYS).sum()


def f40_atxd_394_atr_macd_signal_crossings_count_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of ATR-MACD line crossings of its 9d signal line over 252d."""
    macd = _atr(high, low, close, 12) - _atr(high, low, close, 26)
    sig = _ema(macd, 9)
    above = (macd > sig).astype(float)
    return above.diff().abs().rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket D — Range alignment with returns (395-400)
# ============================================================

def f40_atxd_395_mean_tr_over_abs_r_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean TR / |r| ratio over 21d (range-to-return scaling)."""
    return _safe_div(_true_range(high, low, close), close.diff().abs()).rolling(MDAYS, min_periods=WDAYS).mean()


def f40_atxd_396_large_tr_small_r_count_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars where TR > 5·|r| over 252d (large-range small-net-move = choppy bar)."""
    tr = _true_range(high, low, close)
    return (tr > 5 * close.diff().abs()).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f40_atxd_397_decisive_bar_count_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars where TR < 1.5·|r| over 252d (decisive bars: move = range)."""
    tr = _true_range(high, low, close)
    return (tr < 1.5 * close.diff().abs()).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f40_atxd_398_tr_r_ratio_pctrank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Pct-rank of current TR/|r| ratio within trailing 252d distribution."""
    ratio = _safe_div(_true_range(high, low, close), close.diff().abs())
    return ratio.rolling(YDAYS, min_periods=QDAYS).apply(
        lambda w: float((w[-1] >= w).sum() / len(w)) if not np.isnan(w[-1]) else np.nan, raw=True)


def f40_atxd_399_tr_abs_r_corr_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 252d corr(TR, |r|) — coordination of bar range with bar return magnitude."""
    return _true_range(high, low, close).rolling(YDAYS, min_periods=QDAYS).corr(close.diff().abs())


def f40_atxd_400_tr_signal_noise_ratio_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """|Σ r| / Σ TR over 63d — signal-to-noise ratio (Kaufman-style efficiency)."""
    return _safe_div(close.diff().rolling(QDAYS, min_periods=MDAYS).sum().abs(),
                     _true_range(high, low, close).rolling(QDAYS, min_periods=MDAYS).sum())


# ============================================================
# Bucket E — ATR-cone diagonals (401-405)
# ============================================================

def f40_atxd_401_diag_p10_252d_minus_p90_504d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Diagonal: p10(ATR(21), 252d) − p90(ATR(21), 504d) — long-term-vs-short-term cone contraction."""
    a = _atr(high, low, close, MDAYS)
    return a.rolling(YDAYS, min_periods=QDAYS).quantile(0.10) - a.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.90)


def f40_atxd_402_diag_p90_252d_minus_p10_504d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Diagonal: p90(ATR(21), 252d) − p10(ATR(21), 504d) — long-vs-short cone expansion."""
    a = _atr(high, low, close, MDAYS)
    return a.rolling(YDAYS, min_periods=QDAYS).quantile(0.90) - a.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.10)


def f40_atxd_403_atr_cone_p50_slope_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 21d slope of p50(ATR(21), 252d) — median-vol-cone trend."""
    a = _atr(high, low, close, MDAYS)
    p50 = a.rolling(YDAYS, min_periods=QDAYS).quantile(0.50)
    return _rolling_slope(p50, MDAYS)


def f40_atxd_404_atr_cone_aperture_roc_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rate-of-change of ATR-cone aperture: (p90-p10)_t − (p90-p10)_t-21."""
    a = _atr(high, low, close, MDAYS)
    aperture = a.rolling(YDAYS, min_periods=QDAYS).quantile(0.90) - a.rolling(YDAYS, min_periods=QDAYS).quantile(0.10)
    return aperture - aperture.shift(MDAYS)


def f40_atxd_405_atr_cone_position_change_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-percentile position change: pct-rank(ATR21, 252d)_t − same 21d ago."""
    a = _atr(high, low, close, MDAYS)
    rk = a.rolling(YDAYS, min_periods=QDAYS).apply(
        lambda w: float((w[-1] >= w).sum() / len(w)) if not np.isnan(w[-1]) else np.nan, raw=True)
    return rk - rk.shift(MDAYS)


# ============================================================
# Bucket F — Range autocorrelation structure (406-410)
# ============================================================

def f40_atxd_406_tr_acf_lag5_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Corr(TR, TR.shift(5)) over 252d (TR autocorr at lag 5)."""
    tr = _true_range(high, low, close)
    return tr.rolling(YDAYS, min_periods=QDAYS).corr(tr.shift(WDAYS))


def f40_atxd_407_tr_acf_lag10_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Corr(TR, TR.shift(10)) over 252d."""
    tr = _true_range(high, low, close)
    return tr.rolling(YDAYS, min_periods=QDAYS).corr(tr.shift(10))


def f40_atxd_408_tr_acf_decay_rate_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """TR autocorrelation decay: |corr(TR, TR.shift(1))| − |corr(TR, TR.shift(21))| over 252d."""
    tr = _true_range(high, low, close)
    c1 = tr.rolling(YDAYS, min_periods=QDAYS).corr(tr.shift(1)).abs()
    c21 = tr.rolling(YDAYS, min_periods=QDAYS).corr(tr.shift(MDAYS)).abs()
    return c1 - c21


def f40_atxd_409_tr_pacf_lag1_proxy_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Partial autocorr lag-1 of TR over 252d (= simple corr lag-1)."""
    tr = _true_range(high, low, close)
    return tr.rolling(YDAYS, min_periods=QDAYS).corr(tr.shift(1))


def f40_atxd_410_tr_pacf_lag5_proxy_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Partial autocorr lag-5 of TR: residual corr controlling for lags 1..4 (simplified via Yule-Walker step)."""
    tr = _true_range(high, low, close)
    # Approximate: subtract OLS fit of TR on lags 1..4, then corr residuals with shift(5)
    lags = [tr.shift(k) for k in range(1, 5)]
    combined = pd.concat([tr] + lags + [tr.shift(WDAYS)], axis=1).values

    def _pacf(arr):
        if arr.shape[0] < QDAYS: return np.nan
        y = arr[:, 0]; X14 = arr[:, 1:5]; lag5 = arr[:, 5]
        m = ~np.isnan(y) & ~np.any(np.isnan(X14), axis=1) & ~np.isnan(lag5)
        if m.sum() < QDAYS: return np.nan
        try:
            X = np.column_stack([np.ones(m.sum()), X14[m]])
            beta = np.linalg.lstsq(X, y[m], rcond=None)[0]
            res = y[m] - X @ beta
            c = np.corrcoef(res, lag5[m])[0, 1]
            return float(c) if np.isfinite(c) else np.nan
        except Exception:
            return np.nan
    out = pd.Series(np.nan, index=close.index)
    for i in range(YDAYS, len(combined)):
        out.iloc[i] = _pacf(combined[i - YDAYS + 1:i + 1])
    return out


# ============================================================
# Bucket G — Post-event ATR features (411-418)
# ============================================================

def f40_atxd_411_mean_atr21_21d_after_252d_high(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean ATR(21) in 21d after a 252d-high event (post-peak ATR regime), mean over 252d."""
    a = _atr(high, low, close, MDAYS)
    new_high_lag = (close.shift(MDAYS) >= close.shift(MDAYS).rolling(YDAYS, min_periods=QDAYS).max())
    return a.where(new_high_lag, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f40_atxd_412_mean_atr21_63d_after_252d_high(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean ATR(21) in 63d after a 252d-high event, mean over 252d."""
    a = _atr(high, low, close, MDAYS)
    new_high_lag = (close.shift(QDAYS) >= close.shift(QDAYS).rolling(YDAYS, min_periods=QDAYS).max())
    return a.where(new_high_lag, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f40_atxd_413_atr_expansion_ratio_21d_after_peak(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR(21) 21d after peak / ATR(21) at peak, mean over 252d."""
    a = _atr(high, low, close, MDAYS)
    new_high_lag = (close.shift(MDAYS) >= close.shift(MDAYS).rolling(YDAYS, min_periods=QDAYS).max())
    return _safe_div(a, a.shift(MDAYS)).where(new_high_lag, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f40_atxd_414_atr_mean_reversion_test_post_peak(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: ATR(21) reverts toward mean post-peak: ATR_t < ATR_t-21 on bars 21d after 252d-high."""
    a = _atr(high, low, close, MDAYS)
    new_high_lag = (close.shift(MDAYS) >= close.shift(MDAYS).rolling(YDAYS, min_periods=QDAYS).max())
    reverted = a < a.shift(MDAYS)
    return (new_high_lag & reverted).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f40_atxd_415_atr5_vol_post_peak_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Std of ATR(5) in 21 bars after 252d-high events, mean over 252d."""
    a5 = _atr(high, low, close, WDAYS)
    new_high_lag = (close.shift(MDAYS) >= close.shift(MDAYS).rolling(YDAYS, min_periods=QDAYS).max())
    a5_post_std = a5.rolling(MDAYS, min_periods=WDAYS).std()
    return a5_post_std.where(new_high_lag, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f40_atxd_416_natr_mean_after_vs_before_peak(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean NATR(21) 21d-after vs 21d-before 252d-high events, mean of difference over 252d."""
    natr = _safe_div(_atr(high, low, close, MDAYS), close)
    new_high = (close >= close.rolling(YDAYS, min_periods=QDAYS).max())
    pre_mean = natr.rolling(MDAYS, min_periods=WDAYS).mean().shift(1)
    new_high_lag = new_high.shift(MDAYS)
    post_mean = natr.rolling(MDAYS, min_periods=WDAYS).mean()
    diff = post_mean - pre_mean.shift(-MDAYS - 1)
    # Restate causally: use new_high_lag (already past), post_mean at current bar, pre_mean from before lag
    causal_pre = natr.rolling(MDAYS, min_periods=WDAYS).mean().shift(MDAYS + 1)
    return (post_mean - causal_pre).where(new_high_lag, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f40_atxd_417_atr_pctrank_shift_after_peak(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-pct-rank shift post-peak: pct-rank now − pct-rank 21d ago, restricted to post-peak bars."""
    a = _atr(high, low, close, MDAYS)
    rk = a.rolling(YDAYS, min_periods=QDAYS).apply(
        lambda w: float((w[-1] >= w).sum() / len(w)) if not np.isnan(w[-1]) else np.nan, raw=True)
    new_high_lag = (close.shift(MDAYS) >= close.shift(MDAYS).rolling(YDAYS, min_periods=QDAYS).max())
    return (rk - rk.shift(MDAYS)).where(new_high_lag, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f40_atxd_418_mean_tr_over_atr_post_peak_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean TR/ATR(21) on bars 21d after 252d-high events, mean over 252d."""
    tr = _true_range(high, low, close)
    atr = _atr(high, low, close, MDAYS)
    new_high_lag = (close.shift(MDAYS) >= close.shift(MDAYS).rolling(YDAYS, min_periods=QDAYS).max())
    return _safe_div(tr, atr).where(new_high_lag, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


# ============================================================
# Bucket H — Range conditional on close-position (419-423)
# ============================================================

def f40_atxd_419_tr_when_close_top_quartile_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean TR on bars where close in top 25% of bar's range, over 252d (bullish-close TR)."""
    tr = _true_range(high, low, close)
    pos = _safe_div(close - low, high - low)
    return tr.where(pos > 0.75, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f40_atxd_420_tr_when_close_bottom_quartile_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean TR on bars where close in bottom 25% of bar's range, over 252d (bearish-close TR)."""
    tr = _true_range(high, low, close)
    pos = _safe_div(close - low, high - low)
    return tr.where(pos < 0.25, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f40_atxd_421_asym_tr_bull_vs_bear_close_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio: bullish-close-TR / bearish-close-TR over 252d (asymmetric range distribution)."""
    tr = _true_range(high, low, close)
    pos = _safe_div(close - low, high - low)
    bull_tr = tr.where(pos > 0.75, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    bear_tr = tr.where(pos < 0.25, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(bull_tr, bear_tr)


def f40_atxd_422_mean_close_pos_on_big_range_bars_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean close-position-in-bar on TR > 2·ATR bars over 252d."""
    tr = _true_range(high, low, close)
    atr_lag = _atr(high, low, close, MDAYS).shift(1)
    pos = _safe_div(close - low, high - low)
    return pos.where(tr > 2 * atr_lag, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f40_atxd_423_tr_conditional_outside_bar_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean TR on outside-bars (engulfs prior bar) over 252d."""
    tr = _true_range(high, low, close)
    outside = (high > high.shift(1)) & (low < low.shift(1))
    return tr.where(outside, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


# ============================================================
# Bucket I — Time-of-cycle ATR (424-428)
# ============================================================

def f40_atxd_424_atr_at_recent_63d_peak_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean ATR(21) on the bar where close hit its 63d-high, over 252d."""
    a = _atr(high, low, close, MDAYS)
    is_peak = (close >= close.rolling(QDAYS, min_periods=MDAYS).max())
    return a.where(is_peak, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f40_atxd_425_atr_at_recent_63d_trough_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean ATR(21) on the bar where close hit its 63d-low, over 252d."""
    a = _atr(high, low, close, MDAYS)
    is_trough = (close <= close.rolling(QDAYS, min_periods=MDAYS).min())
    return a.where(is_trough, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f40_atxd_426_atr_change_since_63d_low(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR(21) / ATR(21) at last 63d-low (causal: shift the low event forward)."""
    a = _atr(high, low, close, MDAYS)
    is_low = (close <= close.rolling(QDAYS, min_periods=MDAYS).min())
    a_at_low = a.where(is_low).ffill()
    return _safe_div(a, a_at_low)


def f40_atxd_427_atr_change_since_63d_high(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR(21) / ATR(21) at last 63d-high (causal)."""
    a = _atr(high, low, close, MDAYS)
    is_high = (close >= close.rolling(QDAYS, min_periods=MDAYS).max())
    a_at_high = a.where(is_high).ffill()
    return _safe_div(a, a_at_high)


def f40_atxd_428_atr_multi_lag_changes(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of normalized ATR changes vs 21d, 63d, 252d ago — composite multi-lag ATR delta."""
    a = _atr(high, low, close, MDAYS)
    chg21 = _safe_div(a - a.shift(MDAYS), a.shift(MDAYS))
    chg63 = _safe_div(a - a.shift(QDAYS), a.shift(QDAYS))
    chg252 = _safe_div(a - a.shift(YDAYS), a.shift(YDAYS))
    return chg21 + chg63 + chg252


# ============================================================
# Bucket J — Final misc (429-450)
# ============================================================

def f40_atxd_429_natr5_pctrank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of NATR(5) within trailing 252d."""
    n = _safe_div(_atr(high, low, close, WDAYS), close)
    return n.rolling(YDAYS, min_periods=QDAYS).apply(
        lambda w: float((w[-1] >= w).sum() / len(w)) if not np.isnan(w[-1]) else np.nan, raw=True)


def f40_atxd_430_natr63_pctrank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of NATR(63) within trailing 252d."""
    n = _safe_div(_atr(high, low, close, QDAYS), close)
    return n.rolling(YDAYS, min_periods=QDAYS).apply(
        lambda w: float((w[-1] >= w).sum() / len(w)) if not np.isnan(w[-1]) else np.nan, raw=True)


def f40_atxd_431_natr5_minus_natr63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """NATR(5) − NATR(63) — short-vs-intermediate normalized vol gap."""
    return _safe_div(_atr(high, low, close, WDAYS), close) - _safe_div(_atr(high, low, close, QDAYS), close)


def f40_atxd_432_natr21_minus_natr63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """NATR(21) − NATR(63) — medium-vs-intermediate gap."""
    return _safe_div(_atr(high, low, close, MDAYS), close) - _safe_div(_atr(high, low, close, QDAYS), close)


def f40_atxd_433_cv_tr_over_abs_r_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Std of (TR/|r|) over 21d — coefficient of variation of range-return ratio."""
    ratio = _safe_div(_true_range(high, low, close), close.diff().abs())
    return ratio.rolling(MDAYS, min_periods=WDAYS).std()


def f40_atxd_434_median_tr_over_abs_r_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Median TR/|r| ratio over 252d (robust range-return scaling)."""
    return _safe_div(_true_range(high, low, close), close.diff().abs()).rolling(YDAYS, min_periods=QDAYS).median()


def f40_atxd_435_atr_jump_count_10pct_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR(21) jump count: |ΔATR| / ATR.shift(1) > 0.10, summed 252d."""
    a = _atr(high, low, close, MDAYS)
    return (_safe_div(a.diff().abs(), a.shift(1)) > 0.10).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f40_atxd_436_atr_sticky_days_count_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR(21) sticky-day count: |ΔATR| / ATR.shift(1) < 0.01, summed 252d."""
    a = _atr(high, low, close, MDAYS)
    return (_safe_div(a.diff().abs(), a.shift(1)) < 0.01).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f40_atxd_437_mean_upper_pressure_21d(high: pd.Series, close: pd.Series) -> pd.Series:
    """Mean (high - close) over 21d — intraday selling pressure proxy."""
    return (high - close).rolling(MDAYS, min_periods=WDAYS).mean()


def f40_atxd_438_mean_lower_buying_21d(low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean (close - low) over 21d — intraday buying pressure proxy."""
    return (close - low).rolling(MDAYS, min_periods=WDAYS).mean()


def f40_atxd_439_selling_pressure_days_count_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Days where (high-close) > (close-low) — more selling pressure intraday — count over 252d."""
    return ((high - close) > (close - low)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f40_atxd_440_range_power_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean TR² over 21d — range power."""
    return (_true_range(high, low, close) ** 2).rolling(MDAYS, min_periods=WDAYS).mean()


def f40_atxd_441_range_geomean_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Geometric mean of TR over 21d (log-space mean)."""
    return np.exp(_safe_log(_true_range(high, low, close)).rolling(MDAYS, min_periods=WDAYS).mean())


def f40_atxd_442_range_harmonic_mean_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Harmonic mean of TR over 21d (sensitive to small values)."""
    return _safe_div(pd.Series(1.0, index=close.index),
                     _safe_div(pd.Series(1.0, index=close.index), _true_range(high, low, close)).rolling(MDAYS, min_periods=WDAYS).mean())


def f40_atxd_443_range_right_tail_top_decile_mean_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean TR restricted to top-decile-TR bars over 252d (right-tail mean)."""
    tr = _true_range(high, low, close)
    p90 = tr.rolling(YDAYS, min_periods=QDAYS).quantile(0.90).shift(1)
    return tr.where(tr > p90, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f40_atxd_444_range_left_tail_bot_decile_mean_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean TR restricted to bottom-decile-TR bars over 252d (left-tail mean)."""
    tr = _true_range(high, low, close)
    p10 = tr.rolling(YDAYS, min_periods=QDAYS).quantile(0.10).shift(1)
    return tr.where(tr < p10, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f40_atxd_445_tr_top_minus_bot_decile_gap_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Top-decile-TR-mean − bottom-decile-TR-mean over 252d (tail-gap)."""
    tr = _true_range(high, low, close)
    p90 = tr.rolling(YDAYS, min_periods=QDAYS).quantile(0.90).shift(1)
    p10 = tr.rolling(YDAYS, min_periods=QDAYS).quantile(0.10).shift(1)
    top = tr.where(tr > p90, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    bot = tr.where(tr < p10, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    return top - bot


def f40_atxd_446_tr_top_decile_over_median_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Top-decile TR mean / median TR over 252d (right-tail extremity)."""
    tr = _true_range(high, low, close)
    p90 = tr.rolling(YDAYS, min_periods=QDAYS).quantile(0.90).shift(1)
    med = tr.rolling(YDAYS, min_periods=QDAYS).median()
    top = tr.where(tr > p90, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(top, med)


def f40_atxd_447_tr_median_over_bot_decile_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Median TR / bottom-decile TR mean over 252d (left-tail extremity)."""
    tr = _true_range(high, low, close)
    p10 = tr.rolling(YDAYS, min_periods=QDAYS).quantile(0.10).shift(1)
    med = tr.rolling(YDAYS, min_periods=QDAYS).median()
    bot = tr.where(tr < p10, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(med, bot)


def f40_atxd_448_range_vol_volume_triplet_z_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Combined z-score: TR-z + |r|-z + volume-z, mean over 21d."""
    tr_z = _rolling_zscore(_true_range(high, low, close), YDAYS)
    r_z = _rolling_zscore(close.diff().abs(), YDAYS)
    v_z = _rolling_zscore(volume, YDAYS)
    return (tr_z + r_z + v_z).rolling(MDAYS, min_periods=WDAYS).mean()


def f40_atxd_449_atr_breakout_from_compression_count_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR(21) breakout: ATR > 1.5 · rolling 21d-min-ATR(21), count over 63d."""
    a = _atr(high, low, close, MDAYS)
    min21 = a.rolling(MDAYS, min_periods=WDAYS).min().shift(1)
    return (a > 1.5 * min21).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f40_atxd_450_multi_bar_range_expansion_count_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """3 consecutive bars all with TR > ATR(21).shift(1), count over 63d."""
    tr = _true_range(high, low, close)
    atr_lag = _atr(high, low, close, MDAYS).shift(1)
    flag = tr > atr_lag
    three = (flag & flag.shift(1) & flag.shift(2)).astype(float)
    return three.rolling(QDAYS, min_periods=MDAYS).sum()


# ============================================================
#                         REGISTRY 376-450
# ============================================================

ATR_EXPANSION_DYNAMICS_BASE_REGISTRY_376_450 = {
    "f40_atxd_376_hl_over_close_mean_21d": {"inputs": ["high", "low", "close"], "func": f40_atxd_376_hl_over_close_mean_21d},
    "f40_atxd_377_hl_over_open_mean_21d": {"inputs": ["open", "high", "low"], "func": f40_atxd_377_hl_over_open_mean_21d},
    "f40_atxd_378_hl_variance_21d": {"inputs": ["high", "low"], "func": f40_atxd_378_hl_variance_21d},
    "f40_atxd_379_hl_skew_21d": {"inputs": ["high", "low"], "func": f40_atxd_379_hl_skew_21d},
    "f40_atxd_380_hl_minus_ema21_deviation": {"inputs": ["high", "low"], "func": f40_atxd_380_hl_minus_ema21_deviation},
    "f40_atxd_381_hl_zscore_252d": {"inputs": ["high", "low"], "func": f40_atxd_381_hl_zscore_252d},
    "f40_atxd_382_tr_monotonic_rise_streak_63d": {"inputs": ["high", "low", "close"], "func": f40_atxd_382_tr_monotonic_rise_streak_63d},
    "f40_atxd_383_tr_monotonic_fall_streak_63d": {"inputs": ["high", "low", "close"], "func": f40_atxd_383_tr_monotonic_fall_streak_63d},
    "f40_atxd_384_tr_alternating_count_63d": {"inputs": ["high", "low", "close"], "func": f40_atxd_384_tr_alternating_count_63d},
    "f40_atxd_385_tr_alternation_frequency_252d": {"inputs": ["high", "low", "close"], "func": f40_atxd_385_tr_alternation_frequency_252d},
    "f40_atxd_386_tr_oscillation_count_21d": {"inputs": ["high", "low", "close"], "func": f40_atxd_386_tr_oscillation_count_21d},
    "f40_atxd_387_tr_mean_reversion_rate_252d": {"inputs": ["high", "low", "close"], "func": f40_atxd_387_tr_mean_reversion_rate_252d},
    "f40_atxd_388_tr_step_event_count_252d": {"inputs": ["high", "low", "close"], "func": f40_atxd_388_tr_step_event_count_252d},
    "f40_atxd_389_tr_step_signed_sum_63d": {"inputs": ["high", "low", "close"], "func": f40_atxd_389_tr_step_signed_sum_63d},
    "f40_atxd_390_atr_macd_12_26": {"inputs": ["high", "low", "close"], "func": f40_atxd_390_atr_macd_12_26},
    "f40_atxd_391_atr_macd_hist_9_signal": {"inputs": ["high", "low", "close"], "func": f40_atxd_391_atr_macd_hist_9_signal},
    "f40_atxd_392_atr_macd_50_200": {"inputs": ["high", "low", "close"], "func": f40_atxd_392_atr_macd_50_200},
    "f40_atxd_393_atr_macd_crossings_count_252d": {"inputs": ["high", "low", "close"], "func": f40_atxd_393_atr_macd_crossings_count_252d},
    "f40_atxd_394_atr_macd_signal_crossings_count_252d": {"inputs": ["high", "low", "close"], "func": f40_atxd_394_atr_macd_signal_crossings_count_252d},
    "f40_atxd_395_mean_tr_over_abs_r_21d": {"inputs": ["high", "low", "close"], "func": f40_atxd_395_mean_tr_over_abs_r_21d},
    "f40_atxd_396_large_tr_small_r_count_252d": {"inputs": ["high", "low", "close"], "func": f40_atxd_396_large_tr_small_r_count_252d},
    "f40_atxd_397_decisive_bar_count_252d": {"inputs": ["high", "low", "close"], "func": f40_atxd_397_decisive_bar_count_252d},
    "f40_atxd_398_tr_r_ratio_pctrank_252d": {"inputs": ["high", "low", "close"], "func": f40_atxd_398_tr_r_ratio_pctrank_252d},
    "f40_atxd_399_tr_abs_r_corr_252d": {"inputs": ["high", "low", "close"], "func": f40_atxd_399_tr_abs_r_corr_252d},
    "f40_atxd_400_tr_signal_noise_ratio_63d": {"inputs": ["high", "low", "close"], "func": f40_atxd_400_tr_signal_noise_ratio_63d},
    "f40_atxd_401_diag_p10_252d_minus_p90_504d": {"inputs": ["high", "low", "close"], "func": f40_atxd_401_diag_p10_252d_minus_p90_504d},
    "f40_atxd_402_diag_p90_252d_minus_p10_504d": {"inputs": ["high", "low", "close"], "func": f40_atxd_402_diag_p90_252d_minus_p10_504d},
    "f40_atxd_403_atr_cone_p50_slope_252d": {"inputs": ["high", "low", "close"], "func": f40_atxd_403_atr_cone_p50_slope_252d},
    "f40_atxd_404_atr_cone_aperture_roc_21d": {"inputs": ["high", "low", "close"], "func": f40_atxd_404_atr_cone_aperture_roc_21d},
    "f40_atxd_405_atr_cone_position_change_21d": {"inputs": ["high", "low", "close"], "func": f40_atxd_405_atr_cone_position_change_21d},
    "f40_atxd_406_tr_acf_lag5_252d": {"inputs": ["high", "low", "close"], "func": f40_atxd_406_tr_acf_lag5_252d},
    "f40_atxd_407_tr_acf_lag10_252d": {"inputs": ["high", "low", "close"], "func": f40_atxd_407_tr_acf_lag10_252d},
    "f40_atxd_408_tr_acf_decay_rate_252d": {"inputs": ["high", "low", "close"], "func": f40_atxd_408_tr_acf_decay_rate_252d},
    "f40_atxd_409_tr_pacf_lag1_proxy_252d": {"inputs": ["high", "low", "close"], "func": f40_atxd_409_tr_pacf_lag1_proxy_252d},
    "f40_atxd_410_tr_pacf_lag5_proxy_252d": {"inputs": ["high", "low", "close"], "func": f40_atxd_410_tr_pacf_lag5_proxy_252d},
    "f40_atxd_411_mean_atr21_21d_after_252d_high": {"inputs": ["high", "low", "close"], "func": f40_atxd_411_mean_atr21_21d_after_252d_high},
    "f40_atxd_412_mean_atr21_63d_after_252d_high": {"inputs": ["high", "low", "close"], "func": f40_atxd_412_mean_atr21_63d_after_252d_high},
    "f40_atxd_413_atr_expansion_ratio_21d_after_peak": {"inputs": ["high", "low", "close"], "func": f40_atxd_413_atr_expansion_ratio_21d_after_peak},
    "f40_atxd_414_atr_mean_reversion_test_post_peak": {"inputs": ["high", "low", "close"], "func": f40_atxd_414_atr_mean_reversion_test_post_peak},
    "f40_atxd_415_atr5_vol_post_peak_252d": {"inputs": ["high", "low", "close"], "func": f40_atxd_415_atr5_vol_post_peak_252d},
    "f40_atxd_416_natr_mean_after_vs_before_peak": {"inputs": ["high", "low", "close"], "func": f40_atxd_416_natr_mean_after_vs_before_peak},
    "f40_atxd_417_atr_pctrank_shift_after_peak": {"inputs": ["high", "low", "close"], "func": f40_atxd_417_atr_pctrank_shift_after_peak},
    "f40_atxd_418_mean_tr_over_atr_post_peak_252d": {"inputs": ["high", "low", "close"], "func": f40_atxd_418_mean_tr_over_atr_post_peak_252d},
    "f40_atxd_419_tr_when_close_top_quartile_252d": {"inputs": ["high", "low", "close"], "func": f40_atxd_419_tr_when_close_top_quartile_252d},
    "f40_atxd_420_tr_when_close_bottom_quartile_252d": {"inputs": ["high", "low", "close"], "func": f40_atxd_420_tr_when_close_bottom_quartile_252d},
    "f40_atxd_421_asym_tr_bull_vs_bear_close_252d": {"inputs": ["high", "low", "close"], "func": f40_atxd_421_asym_tr_bull_vs_bear_close_252d},
    "f40_atxd_422_mean_close_pos_on_big_range_bars_252d": {"inputs": ["high", "low", "close"], "func": f40_atxd_422_mean_close_pos_on_big_range_bars_252d},
    "f40_atxd_423_tr_conditional_outside_bar_252d": {"inputs": ["high", "low", "close"], "func": f40_atxd_423_tr_conditional_outside_bar_252d},
    "f40_atxd_424_atr_at_recent_63d_peak_252d": {"inputs": ["high", "low", "close"], "func": f40_atxd_424_atr_at_recent_63d_peak_252d},
    "f40_atxd_425_atr_at_recent_63d_trough_252d": {"inputs": ["high", "low", "close"], "func": f40_atxd_425_atr_at_recent_63d_trough_252d},
    "f40_atxd_426_atr_change_since_63d_low": {"inputs": ["high", "low", "close"], "func": f40_atxd_426_atr_change_since_63d_low},
    "f40_atxd_427_atr_change_since_63d_high": {"inputs": ["high", "low", "close"], "func": f40_atxd_427_atr_change_since_63d_high},
    "f40_atxd_428_atr_multi_lag_changes": {"inputs": ["high", "low", "close"], "func": f40_atxd_428_atr_multi_lag_changes},
    "f40_atxd_429_natr5_pctrank_252d": {"inputs": ["high", "low", "close"], "func": f40_atxd_429_natr5_pctrank_252d},
    "f40_atxd_430_natr63_pctrank_252d": {"inputs": ["high", "low", "close"], "func": f40_atxd_430_natr63_pctrank_252d},
    "f40_atxd_431_natr5_minus_natr63": {"inputs": ["high", "low", "close"], "func": f40_atxd_431_natr5_minus_natr63},
    "f40_atxd_432_natr21_minus_natr63": {"inputs": ["high", "low", "close"], "func": f40_atxd_432_natr21_minus_natr63},
    "f40_atxd_433_cv_tr_over_abs_r_21d": {"inputs": ["high", "low", "close"], "func": f40_atxd_433_cv_tr_over_abs_r_21d},
    "f40_atxd_434_median_tr_over_abs_r_252d": {"inputs": ["high", "low", "close"], "func": f40_atxd_434_median_tr_over_abs_r_252d},
    "f40_atxd_435_atr_jump_count_10pct_252d": {"inputs": ["high", "low", "close"], "func": f40_atxd_435_atr_jump_count_10pct_252d},
    "f40_atxd_436_atr_sticky_days_count_252d": {"inputs": ["high", "low", "close"], "func": f40_atxd_436_atr_sticky_days_count_252d},
    "f40_atxd_437_mean_upper_pressure_21d": {"inputs": ["high", "close"], "func": f40_atxd_437_mean_upper_pressure_21d},
    "f40_atxd_438_mean_lower_buying_21d": {"inputs": ["low", "close"], "func": f40_atxd_438_mean_lower_buying_21d},
    "f40_atxd_439_selling_pressure_days_count_252d": {"inputs": ["high", "low", "close"], "func": f40_atxd_439_selling_pressure_days_count_252d},
    "f40_atxd_440_range_power_21d": {"inputs": ["high", "low", "close"], "func": f40_atxd_440_range_power_21d},
    "f40_atxd_441_range_geomean_21d": {"inputs": ["high", "low", "close"], "func": f40_atxd_441_range_geomean_21d},
    "f40_atxd_442_range_harmonic_mean_21d": {"inputs": ["high", "low", "close"], "func": f40_atxd_442_range_harmonic_mean_21d},
    "f40_atxd_443_range_right_tail_top_decile_mean_252d": {"inputs": ["high", "low", "close"], "func": f40_atxd_443_range_right_tail_top_decile_mean_252d},
    "f40_atxd_444_range_left_tail_bot_decile_mean_252d": {"inputs": ["high", "low", "close"], "func": f40_atxd_444_range_left_tail_bot_decile_mean_252d},
    "f40_atxd_445_tr_top_minus_bot_decile_gap_252d": {"inputs": ["high", "low", "close"], "func": f40_atxd_445_tr_top_minus_bot_decile_gap_252d},
    "f40_atxd_446_tr_top_decile_over_median_252d": {"inputs": ["high", "low", "close"], "func": f40_atxd_446_tr_top_decile_over_median_252d},
    "f40_atxd_447_tr_median_over_bot_decile_252d": {"inputs": ["high", "low", "close"], "func": f40_atxd_447_tr_median_over_bot_decile_252d},
    "f40_atxd_448_range_vol_volume_triplet_z_252d": {"inputs": ["high", "low", "close", "volume"], "func": f40_atxd_448_range_vol_volume_triplet_z_252d},
    "f40_atxd_449_atr_breakout_from_compression_count_63d": {"inputs": ["high", "low", "close"], "func": f40_atxd_449_atr_breakout_from_compression_count_63d},
    "f40_atxd_450_multi_bar_range_expansion_count_63d": {"inputs": ["high", "low", "close"], "func": f40_atxd_450_multi_bar_range_expansion_count_63d},
}
