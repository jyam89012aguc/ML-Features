"""macd_topping_dynamics d1 features 226-300 — Pipeline 1b-technical.

Extends 151-225 with cross-MACD volatility/regime variants, MACD on synthetic-smoothed
prices, multi-timeframe MACD, MACD information-theory measures, MACD ML feature engineering,
MACD regime modeling, and master composites / terminal signals.

Inputs: SEP OHLCV. PIT-clean. Self-contained helpers.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504


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


def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=max(n // 2, 2)).mean()


def _macd(close, fast=12, slow=26, signal=9):
    macd = _ema(close, fast) - _ema(close, slow)
    sig = _ema(macd, signal)
    histo = macd - sig
    return macd, sig, histo


def _ppo(close, fast=12, slow=26, signal=9):
    ef = _ema(close, fast)
    es = _ema(close, slow)
    ppo = 100.0 * _safe_div(ef - es, es)
    sig = _ema(ppo, signal)
    histo = ppo - sig
    return ppo, sig, histo


def _bars_since_true(mask: pd.Series) -> pd.Series:
    arr = mask.astype(bool).to_numpy()
    out = np.full(arr.shape, np.nan)
    last = -1
    for i in range(arr.size):
        if arr[i]:
            last = i
            out[i] = 0.0
        elif last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=mask.index)


def _streak_true(mask: pd.Series) -> pd.Series:
    arr = mask.astype(bool).to_numpy()
    out = np.zeros(arr.shape, dtype=float)
    c = 0
    for i in range(arr.size):
        c = c + 1 if arr[i] else 0
        out[i] = float(c)
    return pd.Series(out, index=mask.index)


def _kalman_simple(close, q=1e-4, r=1e-2):
    """1D Kalman smoothing of price (constant-state model). Simplified: scalar Kalman with
    process noise q and measurement noise r."""
    x = close.to_numpy(dtype=float)
    out = np.full(x.shape, np.nan)
    P = 1.0
    xhat = np.nan
    for i in range(len(x)):
        if np.isnan(x[i]):
            out[i] = xhat
            continue
        if np.isnan(xhat):
            xhat = x[i]; P = 1.0
        else:
            P = P + q
            K = P / (P + r)
            xhat = xhat + K * (x[i] - xhat)
            P = (1.0 - K) * P
        out[i] = xhat
    return pd.Series(out, index=close.index)


def _hp_filter_proxy(close, lam=1600):
    """HP-filter proxy via right-anchored centered-EMA approximation.
    Use double-EMA smoothing as a simplified trend extractor."""
    n_eff = int(max(5, np.sqrt(lam) / 4))
    e1 = _ema(close, n_eff)
    e2 = _ema(e1, n_eff)
    return e2


def _savgol_right_proxy(close, n=21):
    """Right-anchored Savitzky-Golay proxy: rolling-mean of last 'n' values weighted
    by a triangular weight (simulates low-pass smoother without forward-looking center)."""
    def _f(x):
        m = len(x)
        ww = np.arange(1, m + 1, dtype=float)
        v = ~np.isnan(x)
        if v.sum() < max(n // 2, 2):
            return np.nan
        if v.all():
            return float((x * ww).sum() / ww.sum())
        xx = x[v]; w2 = ww[v]
        return float((xx * w2).sum() / w2.sum())
    return close.rolling(n, min_periods=max(n // 2, 2)).apply(_f, raw=True)


def _median_filter(close, n=7):
    return close.rolling(n, min_periods=max(n // 2, 2)).median()


def _mad_smoother(close, n=21):
    """MAD-based robust smoother: rolling median (already robust)."""
    return close.rolling(n, min_periods=max(n // 3, 2)).median()


def _lowpass(close, n=5):
    """Simple low-pass: rolling mean of length n."""
    return close.rolling(n, min_periods=max(n // 2, 2)).mean()


def _wma(s, n):
    def _f(x):
        m = len(x)
        ww = np.arange(1, m + 1, dtype=float)
        v = ~np.isnan(x)
        if v.sum() < max(n // 2, 2):
            return np.nan
        if v.all():
            return float((x * ww).sum() / ww.sum())
        xx = x[v]; w2 = ww[v]
        return float((xx * w2).sum() / w2.sum())
    return s.rolling(n, min_periods=max(n // 2, 2)).apply(_f, raw=True)


def _hma_local(s, n):
    half = max(int(n / 2), 2)
    sq = max(int(np.sqrt(n)), 2)
    return _wma(2 * _wma(s, half) - _wma(s, n), sq)


def _dema_local(s, n):
    e1 = _ema(s, n)
    e2 = _ema(e1, n)
    return 2.0 * e1 - e2


def _entropy_window(w):
    v = w[~np.isnan(w)]
    if v.size < MDAYS:
        return np.nan
    q = np.quantile(v, [0.2, 0.4, 0.6, 0.8])
    bins = np.digitize(v, q)
    p = np.array([(bins == k).sum() for k in range(5)], dtype=float) / v.size
    p = p[p > 0]
    if p.size == 0:
        return np.nan
    return float(-(p * np.log(p)).sum())


def _hurst_window(w):
    v = w[~np.isnan(w)]
    if v.size < 32:
        return np.nan
    m0 = v.mean()
    y = np.cumsum(v - m0)
    R = y.max() - y.min()
    S = v.std()
    if S <= 0 or R <= 0:
        return np.nan
    return float(np.log(R / S) / np.log(v.size))


def _recurrence_window(w):
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < MDAYS:
        return np.nan
    s = v.std()
    if s <= 0:
        return np.nan
    diff = v[:, None] - v[None, :]
    rec = (np.abs(diff) < 0.1 * s).sum() - nn
    return float(rec) / float(nn * (nn - 1))


def _dwell_above_zero_252(x):
    return (x > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


# ============================================================
# Vol-adjusted MACD variants (226-235)
# ============================================================


def f27_mcdt_226_macd_realized_vol_normalized_21_d1(close: pd.Series) -> pd.Series:
    """MACD line / 21d std of log-returns — vol-normalized MACD."""
    m, _, _ = _macd(close)
    rv = _safe_log(close).diff().rolling(MDAYS, min_periods=WDAYS).std()
    return (_safe_div(m, rv * close)).diff()


def f27_mcdt_227_macd_garch_proxy_normalized_d1(close: pd.Series) -> pd.Series:
    """MACD normalized by GARCH(1,1)-proxy vol: EWMA of squared returns (lambda=0.94)."""
    r = _safe_log(close).diff()
    var = (r * r).ewm(alpha=1 - 0.94, adjust=False, min_periods=MDAYS).mean()
    sd = np.sqrt(var)
    m, _, _ = _macd(close)
    return (_safe_div(m, sd * close)).diff()


def f27_mcdt_228_macd_during_high_vol_regime_state_d1(close: pd.Series) -> pd.Series:
    """1 if MACD > 0 AND 21d vol z-score (252d) > 1.5 — bullish-momentum in high-vol regime."""
    m, _, _ = _macd(close)
    rv = _safe_log(close).diff().rolling(MDAYS, min_periods=WDAYS).std()
    z = _rolling_zscore(rv, YDAYS, min_periods=QDAYS)
    return (((m > 0) & (z > 1.5)).astype(float).where(m.notna() & z.notna(), np.nan)).diff()


def f27_mcdt_229_macd_during_low_vol_regime_state_d1(close: pd.Series) -> pd.Series:
    """1 if MACD > 0 AND 21d vol z-score (252d) < -1.0 — bullish-momentum in low-vol regime."""
    m, _, _ = _macd(close)
    rv = _safe_log(close).diff().rolling(MDAYS, min_periods=WDAYS).std()
    z = _rolling_zscore(rv, YDAYS, min_periods=QDAYS)
    return (((m > 0) & (z < -1.0)).astype(float).where(m.notna() & z.notna(), np.nan)).diff()


def f27_mcdt_230_macd_vol_adjusted_bearish_cross_d1(close: pd.Series) -> pd.Series:
    """Bearish MACD/signal cross fired AND 21d-vol > its 252d mean — vol-confirmed bearish cross."""
    m, s, _ = _macd(close)
    d = m - s
    cross = (d.shift(1) > 0) & (d <= 0)
    rv = _safe_log(close).diff().rolling(MDAYS, min_periods=WDAYS).std()
    rv_mean = rv.rolling(YDAYS, min_periods=QDAYS).mean()
    high_vol = rv > rv_mean
    return ((cross & high_vol).astype(float).where(d.notna() & rv.notna(), np.nan)).diff()


def f27_mcdt_231_macd_vol_adjusted_div_63_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish MACD divergence (63d) AND vol z-score > 1 — vol-confirmed divergence."""
    m, _, _ = _macd(close)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    prior_max = m.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    div = p_new & (m < prior_max)
    rv = _safe_log(close).diff().rolling(MDAYS, min_periods=WDAYS).std()
    z = _rolling_zscore(rv, YDAYS, min_periods=QDAYS)
    return ((div & (z > 1.0)).astype(float).where(m.notna() & z.notna(), np.nan)).diff()


def f27_mcdt_232_ppo_garch_normalized_d1(close: pd.Series) -> pd.Series:
    """PPO normalized by GARCH(1,1) proxy vol (EWMA of squared returns)."""
    r = _safe_log(close).diff()
    var = (r * r).ewm(alpha=1 - 0.94, adjust=False, min_periods=MDAYS).mean()
    sd = np.sqrt(var) * 100.0
    p, _, _ = _ppo(close)
    return (_safe_div(p, sd)).diff()


def f27_mcdt_233_macd_vol_expansion_ratio_63_d1(close: pd.Series) -> pd.Series:
    """63d std of MACD / 252d std of MACD — MACD-vol expansion vs annual baseline."""
    m, _, _ = _macd(close)
    sd63 = m.rolling(QDAYS, min_periods=MDAYS).std()
    sd252 = m.rolling(YDAYS, min_periods=QDAYS).std()
    return (_safe_div(sd63, sd252)).diff()


def f27_mcdt_234_macd_vol_contraction_ratio_63_d1(close: pd.Series) -> pd.Series:
    """21d std of MACD / 63d std of MACD — short-horizon MACD-vol contraction (squeeze)."""
    m, _, _ = _macd(close)
    sd21 = m.rolling(MDAYS, min_periods=WDAYS).std()
    sd63 = m.rolling(QDAYS, min_periods=MDAYS).std()
    return (_safe_div(sd21, sd63)).diff()


def f27_mcdt_235_macd_vol_regime_shift_indicator_252_d1(close: pd.Series) -> pd.Series:
    """1 if recent 21d MACD-vol > 2 * trailing 252d median of 21d MACD-vol — vol-regime shift up."""
    m, _, _ = _macd(close)
    sd21 = m.rolling(MDAYS, min_periods=WDAYS).std()
    med = sd21.rolling(YDAYS, min_periods=QDAYS).median()
    return ((sd21 > 2.0 * med).astype(float).where(med.notna(), np.nan)).diff()


def f27_mcdt_236_macd_on_kalman_filtered_close_d1(close: pd.Series) -> pd.Series:
    """MACD on Kalman-smoothed close (simplified scalar Kalman, q=1e-4, r=1e-2)."""
    k = _kalman_simple(close)
    return (_ema(k, 12) - _ema(k, 26)).diff()


def f27_mcdt_237_macd_on_kalman_above_zero_d1(close: pd.Series) -> pd.Series:
    """1 if MACD-on-Kalman-close > 0 — smoothed-bullish state."""
    k = _kalman_simple(close)
    m = _ema(k, 12) - _ema(k, 26)
    return ((m > 0).astype(float).where(m.notna(), np.nan)).diff()


def f27_mcdt_238_macd_on_robust_smoother_d1(close: pd.Series) -> pd.Series:
    """MACD on MAD-robust smoothed close (rolling 21d median)."""
    rsm = _mad_smoother(close, 21)
    return (_ema(rsm, 12) - _ema(rsm, 26)).diff()


def f27_mcdt_239_macd_on_hp_filter_smooth_d1(close: pd.Series) -> pd.Series:
    """MACD on HP-filter-proxy smoothed close (double-EMA trend extractor)."""
    hp = _hp_filter_proxy(close, lam=1600)
    return (_ema(hp, 12) - _ema(hp, 26)).diff()


def f27_mcdt_240_macd_on_savgol_smooth_d1(close: pd.Series) -> pd.Series:
    """MACD on right-anchored Savitzky-Golay-proxy smoothed close (triangular weighting, n=21)."""
    sg = _savgol_right_proxy(close, n=21)
    return (_ema(sg, 12) - _ema(sg, 26)).diff()


def f27_mcdt_241_macd_on_lowpass_filter_5_d1(close: pd.Series) -> pd.Series:
    """MACD on 5d-mean low-pass-smoothed close."""
    lp = _lowpass(close, 5)
    return (_ema(lp, 12) - _ema(lp, 26)).diff()


def f27_mcdt_242_macd_on_median_filter_7_d1(close: pd.Series) -> pd.Series:
    """MACD on 7d-median-filtered close — outlier-robust trend signal."""
    mf = _median_filter(close, 7)
    return (_ema(mf, 12) - _ema(mf, 26)).diff()


def f27_mcdt_243_macd_on_robust_smoother_above_zero_state_d1(close: pd.Series) -> pd.Series:
    """1 if MACD on MAD-robust-smoothed close > 0."""
    rsm = _mad_smoother(close, 21)
    m = _ema(rsm, 12) - _ema(rsm, 26)
    return ((m > 0).astype(float).where(m.notna(), np.nan)).diff()


def f27_mcdt_244_macd_on_kalman_div_vs_price_63_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish divergence using MACD-on-Kalman-smoothed close vs high (63d)."""
    k = _kalman_simple(close)
    m = _ema(k, 12) - _ema(k, 26)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    m_below = m < m.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return ((p_new & m_below).astype(float).where(m.notna(), np.nan)).diff()


def f27_mcdt_245_macd_on_synthetic_smooth_zscore_252_d1(close: pd.Series) -> pd.Series:
    """252d z-score of MACD on Savgol-smoothed close — distribution-position of smoothed-MACD."""
    sg = _savgol_right_proxy(close, n=21)
    m = _ema(sg, 12) - _ema(sg, 26)
    return (_rolling_zscore(m, YDAYS, min_periods=QDAYS)).diff()


def f27_mcdt_246_weekly_macd_resampled_5d_above_zero_d1(close: pd.Series) -> pd.Series:
    """Weekly-MACD proxy via 5d-spaced subsample: MACD on every-5th close (12,26,9), state."""
    w = close.shift(WDAYS - 1).rolling(WDAYS, min_periods=WDAYS).mean()
    m = _ema(w, 12) - _ema(w, 26)
    return ((m > 0).astype(float).where(m.notna(), np.nan)).diff()


def f27_mcdt_247_monthly_macd_resampled_21d_above_zero_d1(close: pd.Series) -> pd.Series:
    """Monthly-MACD proxy via 21d-spaced subsample: state."""
    w = close.shift(MDAYS - 1).rolling(MDAYS, min_periods=MDAYS).mean()
    m = _ema(w, 12) - _ema(w, 26)
    return ((m > 0).astype(float).where(m.notna(), np.nan)).diff()


def f27_mcdt_248_multi_tf_macd_alignment_state_d1(close: pd.Series) -> pd.Series:
    """1 if MACD > 0 on daily AND weekly AND monthly proxies — all-TF bullish alignment."""
    md, _, _ = _macd(close, 12, 26, 9)
    w = close.rolling(WDAYS, min_periods=WDAYS).mean()
    mw = _ema(w, 12) - _ema(w, 26)
    mo = close.rolling(MDAYS, min_periods=MDAYS).mean()
    mm = _ema(mo, 12) - _ema(mo, 26)
    return (((md > 0) & (mw > 0) & (mm > 0)).astype(float).where(md.notna() & mw.notna() & mm.notna(), np.nan)).diff()


def f27_mcdt_249_multi_tf_macd_dispersion_d1(close: pd.Series) -> pd.Series:
    """Std across z-scored daily/weekly/monthly MACDs — TF dispersion."""
    md, _, _ = _macd(close, 12, 26, 9)
    zd = _rolling_zscore(md, YDAYS, min_periods=QDAYS)
    w = close.rolling(WDAYS, min_periods=WDAYS).mean()
    mw = _ema(w, 12) - _ema(w, 26)
    zw = _rolling_zscore(mw, YDAYS, min_periods=QDAYS)
    mo = close.rolling(MDAYS, min_periods=MDAYS).mean()
    mm = _ema(mo, 12) - _ema(mo, 26)
    zm = _rolling_zscore(mm, YDAYS, min_periods=QDAYS)
    return (pd.concat([zd.rename("d"), zw.rename("w"), zm.rename("m")], axis=1).std(axis=1)).diff()


def f27_mcdt_250_weekly_macd_bearish_cross_d1(close: pd.Series) -> pd.Series:
    """1 if weekly-MACD proxy crossed below its 9-EMA signal."""
    w = close.rolling(WDAYS, min_periods=WDAYS).mean()
    m = _ema(w, 12) - _ema(w, 26)
    s = _ema(m, 9)
    d = m - s
    return (((d.shift(1) > 0) & (d <= 0)).astype(float).where(d.notna(), np.nan)).diff()


def f27_mcdt_251_monthly_macd_bearish_cross_d1(close: pd.Series) -> pd.Series:
    """1 if monthly-MACD proxy crossed below its 9-EMA signal."""
    o = close.rolling(MDAYS, min_periods=MDAYS).mean()
    m = _ema(o, 12) - _ema(o, 26)
    s = _ema(m, 9)
    d = m - s
    return (((d.shift(1) > 0) & (d <= 0)).astype(float).where(d.notna(), np.nan)).diff()


def f27_mcdt_252_cross_tf_macd_divergence_count_d1(close: pd.Series) -> pd.Series:
    """Count of TF pairs (D/W, D/M, W/M) where signs disagree — TF disagreement count."""
    md, _, _ = _macd(close, 12, 26, 9)
    w = close.rolling(WDAYS, min_periods=WDAYS).mean()
    mw = _ema(w, 12) - _ema(w, 26)
    o = close.rolling(MDAYS, min_periods=MDAYS).mean()
    mm = _ema(o, 12) - _ema(o, 26)
    dw = (md * mw < 0).astype(float)
    dm = (md * mm < 0).astype(float)
    wm = (mw * mm < 0).astype(float)
    return ((dw.fillna(0) + dm.fillna(0) + wm.fillna(0)).where(md.notna() & mw.notna() & mm.notna(), np.nan)).diff()


def f27_mcdt_253_weekly_macd_dwell_above_zero_252_d1(close: pd.Series) -> pd.Series:
    """Fraction of past 252 bars with weekly-MACD-proxy > 0 — weekly bullish dwell."""
    w = close.rolling(WDAYS, min_periods=WDAYS).mean()
    m = _ema(w, 12) - _ema(w, 26)
    return ((m > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(m.notna(), np.nan)).diff()


def f27_mcdt_254_multi_tf_macd_consensus_score_d1(close: pd.Series) -> pd.Series:
    """Sum of signs of daily, weekly, monthly MACDs (-3 to +3) — TF consensus score."""
    md, _, _ = _macd(close, 12, 26, 9)
    w = close.rolling(WDAYS, min_periods=WDAYS).mean()
    mw = _ema(w, 12) - _ema(w, 26)
    o = close.rolling(MDAYS, min_periods=MDAYS).mean()
    mm = _ema(o, 12) - _ema(o, 26)
    return ((np.sign(md).fillna(0) + np.sign(mw).fillna(0) + np.sign(mm).fillna(0)).where(

        md.notna() & mw.notna() & mm.notna(), np.nan)).diff()


def f27_mcdt_255_tf_macd_lead_lag_difference_21_d1(close: pd.Series) -> pd.Series:
    """21d slope of weekly-MACD-proxy minus 21d slope of monthly-MACD-proxy —
    which TF is leading the trend change."""
    w = close.rolling(WDAYS, min_periods=WDAYS).mean()
    mw = _ema(w, 12) - _ema(w, 26)
    o = close.rolling(MDAYS, min_periods=MDAYS).mean()
    mm = _ema(o, 12) - _ema(o, 26)
    return (_rolling_slope(mw, MDAYS) - _rolling_slope(mm, MDAYS)).diff()


def f27_mcdt_256_macd_information_ratio_with_returns_63_d1(close: pd.Series) -> pd.Series:
    """63d corr(MACD, fwd-1 log-return) using only PIT data — actually
    use lag(1) MACD vs current log-return (so MACD predicts current return)."""
    m, _, _ = _macd(close)
    r = _safe_log(close).diff()
    return (m.shift(1).rolling(QDAYS, min_periods=MDAYS).corr(r)).diff()


def f27_mcdt_257_macd_autocorrelation_lag_5_63_d1(close: pd.Series) -> pd.Series:
    """63d lag-5 autocorrelation of MACD line."""
    m, _, _ = _macd(close)
    return (m.rolling(QDAYS, min_periods=MDAYS).corr(m.shift(WDAYS))).diff()


def f27_mcdt_258_macd_kalman_innovation_residual_zscore_d1(close: pd.Series) -> pd.Series:
    """Z-score (63d) of (MACD - MACD-on-Kalman-close) — innovation residual of MACD vs filtered."""
    m, _, _ = _macd(close)
    k = _kalman_simple(close)
    mk = _ema(k, 12) - _ema(k, 26)
    return (_rolling_zscore(m - mk, QDAYS, min_periods=MDAYS)).diff()


def f27_mcdt_259_macd_signal_to_noise_ratio_63_d1(close: pd.Series) -> pd.Series:
    """|mean(MACD over 63)| / std(MACD over 63) — signal-to-noise of MACD."""
    m, _, _ = _macd(close)
    return (_safe_div(m.rolling(QDAYS, min_periods=MDAYS).mean().abs(),

                     m.rolling(QDAYS, min_periods=MDAYS).std())).diff()


def f27_mcdt_260_macd_predictability_zscore_252_d1(close: pd.Series) -> pd.Series:
    """Z-score (252d) of |lag-1 autocorr of MACD| over 63d — distribution-rel predictability."""
    m, _, _ = _macd(close)
    ac1 = m.rolling(QDAYS, min_periods=MDAYS).corr(m.shift(1)).abs()
    return (_rolling_zscore(ac1, YDAYS, min_periods=QDAYS)).diff()


def f27_mcdt_261_macd_entropy_discretized_63_d1(close: pd.Series) -> pd.Series:
    """Shannon entropy of MACD discretized into 5 quantile-bins over rolling 63d."""
    m, _, _ = _macd(close)
    return (m.rolling(QDAYS, min_periods=MDAYS).apply(_entropy_window, raw=True)).diff()


def f27_mcdt_262_macd_persistence_correlation_63_d1(close: pd.Series) -> pd.Series:
    """63d corr(MACD, MACD.shift(21)) — monthly-lag persistence of MACD."""
    m, _, _ = _macd(close)
    return (m.rolling(QDAYS, min_periods=MDAYS).corr(m.shift(MDAYS))).diff()


def f27_mcdt_263_macd_long_memory_hurst_proxy_63_d1(close: pd.Series) -> pd.Series:
    """Hurst-exponent proxy of MACD over 63d via log(R/S). Simplified per-window estimate."""
    m, _, _ = _macd(close)
    return (m.rolling(QDAYS, min_periods=MDAYS).apply(_hurst_window, raw=True)).diff()


def f27_mcdt_264_macd_chaos_lyapunov_proxy_63_d1(close: pd.Series) -> pd.Series:
    """Lyapunov-exponent proxy: mean(log|MACD[t] - MACD[t-1]|) over 63d.
    Higher = more sensitive to initial conditions (chaotic)."""
    m, _, _ = _macd(close)
    delta = (m - m.shift(1)).abs()
    return (np.log(delta.replace(0, np.nan)).rolling(QDAYS, min_periods=MDAYS).mean()).diff()


def f27_mcdt_265_macd_recurrence_quantification_proxy_63_d1(close: pd.Series) -> pd.Series:
    """Recurrence proxy: fraction of pairs (i,j) in 63d window where |MACD_i - MACD_j| < 0.1*std.
    High = MACD revisits same values often (regime-like)."""
    m, _, _ = _macd(close)
    return (m.rolling(QDAYS, min_periods=MDAYS).apply(_recurrence_window, raw=True)).diff()


def f27_mcdt_266_macd_rolling_min_63_zscore_d1(close: pd.Series) -> pd.Series:
    """Z-score (252d) of 63d-rolling-min of MACD — distribution position of recent floor."""
    m, _, _ = _macd(close)
    return (_rolling_zscore(m.rolling(QDAYS, min_periods=MDAYS).min(), YDAYS, min_periods=QDAYS)).diff()


def f27_mcdt_267_macd_rolling_max_63_zscore_d1(close: pd.Series) -> pd.Series:
    """Z-score (252d) of 63d-rolling-max of MACD — distribution position of recent ceiling."""
    m, _, _ = _macd(close)
    return (_rolling_zscore(m.rolling(QDAYS, min_periods=MDAYS).max(), YDAYS, min_periods=QDAYS)).diff()


def f27_mcdt_268_macd_rolling_iqr_63_d1(close: pd.Series) -> pd.Series:
    """63d IQR of MACD (Q75 - Q25) — robust dispersion measure."""
    m, _, _ = _macd(close)
    q75 = m.rolling(QDAYS, min_periods=MDAYS).quantile(0.75)
    q25 = m.rolling(QDAYS, min_periods=MDAYS).quantile(0.25)
    return (q75 - q25).diff()


def f27_mcdt_269_macd_rolling_skew_63_zscore_d1(close: pd.Series) -> pd.Series:
    """Z-score (252d) of 63d-skew of MACD — extreme asymmetry detection."""
    m, _, _ = _macd(close)
    return (_rolling_zscore(m.rolling(QDAYS, min_periods=MDAYS).skew(), YDAYS, min_periods=QDAYS)).diff()


def f27_mcdt_270_macd_rolling_kurt_63_zscore_d1(close: pd.Series) -> pd.Series:
    """Z-score (252d) of 63d-kurtosis of MACD — extreme-tail detection."""
    m, _, _ = _macd(close)
    return (_rolling_zscore(m.rolling(QDAYS, min_periods=MDAYS).kurt(), YDAYS, min_periods=QDAYS)).diff()


def f27_mcdt_271_macd_drawdown_from_max_63_d1(close: pd.Series) -> pd.Series:
    """(MACD - 63d rolling MACD-max) / |63d MACD-max| — relative drawdown of MACD from recent peak."""
    m, _, _ = _macd(close)
    rmax = m.rolling(QDAYS, min_periods=MDAYS).max()
    return (_safe_div(m - rmax, rmax.abs())).diff()


def f27_mcdt_272_macd_running_drawdown_from_max_252_d1(close: pd.Series) -> pd.Series:
    """(MACD - 252d running MACD-max) — annual drawdown of MACD."""
    m, _, _ = _macd(close)
    rmax = m.rolling(YDAYS, min_periods=QDAYS).max()
    return (m - rmax).diff()


def f27_mcdt_273_macd_drawdown_recovery_rate_63_d1(close: pd.Series) -> pd.Series:
    """5d slope of (MACD - 63d rolling-max) / |63d rolling-max| — recovery rate from MACD drawdown."""
    m, _, _ = _macd(close)
    rmax = m.rolling(QDAYS, min_periods=MDAYS).max()
    dd = _safe_div(m - rmax, rmax.abs())
    return (_rolling_slope(dd, WDAYS)).diff()


def f27_mcdt_274_macd_rolling_sharpe_ratio_proxy_63_d1(close: pd.Series) -> pd.Series:
    """mean(MACD)/std(MACD) over 63d — proxy Sharpe of MACD."""
    m, _, _ = _macd(close)
    return (_safe_div(m.rolling(QDAYS, min_periods=MDAYS).mean(),

                     m.rolling(QDAYS, min_periods=MDAYS).std())).diff()


def f27_mcdt_275_macd_rolling_sortino_proxy_63_d1(close: pd.Series) -> pd.Series:
    """mean(MACD)/downside-std(MACD) over 63d — proxy Sortino."""
    m, _, _ = _macd(close)
    neg = m.where(m < 0, 0.0)
    ds = neg.rolling(QDAYS, min_periods=MDAYS).std()
    return (_safe_div(m.rolling(QDAYS, min_periods=MDAYS).mean(), ds)).diff()


def f27_mcdt_276_macd_regime_above_zero_persistence_d1(close: pd.Series) -> pd.Series:
    """P(MACD>0 in next bar | MACD>0 now), estimated over 252d — regime persistence."""
    m, _, _ = _macd(close)
    pos = (m > 0).astype(float)
    pos_now = pos.shift(1)
    pos_next = pos
    both = (pos_now * pos_next).rolling(YDAYS, min_periods=QDAYS).sum()
    base = pos_now.rolling(YDAYS, min_periods=QDAYS).sum()
    return (_safe_div(both, base)).diff()


def f27_mcdt_277_macd_regime_below_zero_persistence_d1(close: pd.Series) -> pd.Series:
    """P(MACD<0 in next bar | MACD<0 now), 252d — bearish-regime persistence."""
    m, _, _ = _macd(close)
    neg = (m < 0).astype(float)
    neg_now = neg.shift(1)
    neg_next = neg
    both = (neg_now * neg_next).rolling(YDAYS, min_periods=QDAYS).sum()
    base = neg_now.rolling(YDAYS, min_periods=QDAYS).sum()
    return (_safe_div(both, base)).diff()


def f27_mcdt_278_macd_regime_change_count_252_d1(close: pd.Series) -> pd.Series:
    """Total count of MACD sign changes (both directions) in past 252d — regime instability."""
    m, _, _ = _macd(close)
    flip = (np.sign(m) != np.sign(m.shift(1))).astype(float)
    return (flip.rolling(YDAYS, min_periods=QDAYS).sum().where(m.notna(), np.nan)).diff()


def f27_mcdt_279_macd_regime_duration_252_zscore_d1(close: pd.Series) -> pd.Series:
    """252d z-score of current MACD-regime duration (current sign streak)."""
    m, _, _ = _macd(close)
    pos = (m > 0).astype(int)
    block = (pos != pos.shift(1)).fillna(False).cumsum()
    streak = pos.groupby(block).cumcount() + 1
    streak = streak.where(m.notna(), np.nan).astype(float)
    return (_rolling_zscore(streak, YDAYS, min_periods=QDAYS)).diff()


def f27_mcdt_280_macd_regime_age_current_d1(close: pd.Series) -> pd.Series:
    """Current age of MACD-sign regime (consecutive bars of same sign)."""
    m, _, _ = _macd(close)
    sg = np.sign(m).fillna(0).astype(int)
    block = (sg != sg.shift(1)).fillna(False).cumsum()
    age = sg.groupby(block).cumcount() + 1
    return (age.where(m.notna(), np.nan).astype(float)).diff()


def f27_mcdt_281_macd_avg_regime_duration_252_d1(close: pd.Series) -> pd.Series:
    """Average length of MACD-sign segments over past 252d."""
    m, _, _ = _macd(close)
    sg = np.sign(m).fillna(0).astype(int)
    flip = (sg != sg.shift(1)).fillna(False).astype(float)
    n_flips = flip.rolling(YDAYS, min_periods=QDAYS).sum()
    return (_safe_div(float(YDAYS), n_flips).where(m.notna(), np.nan)).diff()


def f27_mcdt_282_macd_regime_transition_velocity_d1(close: pd.Series) -> pd.Series:
    """|MACD - MACD at last regime-change| — magnitude of move since regime started."""
    m, _, _ = _macd(close)
    sg = np.sign(m).fillna(0).astype(int)
    flipped = (sg != sg.shift(1))
    last_m_at_flip = m.where(flipped, np.nan).ffill()
    return ((m - last_m_at_flip).abs()).diff()


def f27_mcdt_283_macd_regime_volatility_within_d1(close: pd.Series) -> pd.Series:
    """63d rolling std of MACD computed only within the current regime (same sign)."""
    m, _, _ = _macd(close)
    pos = (m > 0).astype(int)
    mask = pos == pos.shift(0)  # always True per-bar; the real grouping uses block
    block = (pos != pos.shift(1)).fillna(False).cumsum()
    # std over current contiguous segment, capped at QDAYS
    grp = m.groupby(block)
    out = grp.transform(lambda x: x.expanding(min_periods=2).std())
    return (out).diff()


def f27_mcdt_284_macd_regime_age_to_avg_ratio_d1(close: pd.Series) -> pd.Series:
    """Current regime-age / average regime-duration (252d) — overdue indicator."""
    m, _, _ = _macd(close)
    sg = np.sign(m).fillna(0).astype(int)
    block = (sg != sg.shift(1)).fillna(False).cumsum()
    age = (sg.groupby(block).cumcount() + 1).where(m.notna(), np.nan).astype(float)
    flip = (sg != sg.shift(1)).fillna(False).astype(float)
    n_flips = flip.rolling(YDAYS, min_periods=QDAYS).sum()
    avg = _safe_div(float(YDAYS), n_flips)
    return (_safe_div(age, avg)).diff()


def f27_mcdt_285_macd_regime_terminal_indicator_d1(close: pd.Series) -> pd.Series:
    """1 if regime age > 2x average regime duration AND 21d MACD slope opposing current sign — terminal regime."""
    m, _, _ = _macd(close)
    sg = np.sign(m).fillna(0).astype(int)
    block = (sg != sg.shift(1)).fillna(False).cumsum()
    age = (sg.groupby(block).cumcount() + 1).where(m.notna(), np.nan).astype(float)
    flip = (sg != sg.shift(1)).fillna(False).astype(float)
    avg = _safe_div(float(YDAYS), flip.rolling(YDAYS, min_periods=QDAYS).sum())
    sl = _rolling_slope(m, MDAYS)
    overdue = age > 2.0 * avg
    weakening = (sg * np.sign(sl)) < 0
    return ((overdue & weakening).astype(float).where(m.notna() & sl.notna(), np.nan)).diff()


def f27_mcdt_286_extended_macd_universe_count_above_zero_d1(close: pd.Series) -> pd.Series:
    """Count of MACD-universe variants currently > 0:
    classical(12,26), fast(5,35), slow(19,39), long(50,200), STC>50, hull(12,26),
    dema(12,26), tema(12,26), zlema(12,26)."""
    c, _, _ = _macd(close, 12, 26, 9)
    f = _ema(close, 5) - _ema(close, 35)
    s = _ema(close, 19) - _ema(close, 39)
    lg = _ema(close, 50) - _ema(close, 200)
    # quick HMA/DEMA/TEMA/ZLEMA inline
    e12_2 = _ema(close, 12); e12_3 = _ema(e12_2, 12)
    de12 = 2.0 * e12_2 - e12_3
    e26_2 = _ema(close, 26); e26_3 = _ema(e26_2, 26)
    de26 = 2.0 * e26_2 - e26_3
    dema_m = de12 - de26
    e12_4 = _ema(e12_3, 12)
    te12 = 3.0 * e12_2 - 3.0 * e12_3 + e12_4
    e26_4 = _ema(e26_3, 26)
    te26 = 3.0 * e26_2 - 3.0 * e26_3 + e26_4
    tema_m = te12 - te26
    z12 = _ema(2.0 * close - close.shift(5), 12)
    z26 = _ema(2.0 * close - close.shift(12), 26)
    zl_m = z12 - z26
    # STC > 50 indicator
    lo = (f).rolling(10, min_periods=4).min(); hi = (f).rolling(10, min_periods=4).max()
    k1 = 100.0 * _safe_div(f - lo, hi - lo)
    k1s = k1.ewm(alpha=0.5, adjust=False, min_periods=5).mean()
    lo2 = k1s.rolling(10, min_periods=4).min(); hi2 = k1s.rolling(10, min_periods=4).max()
    k2 = 100.0 * _safe_div(k1s - lo2, hi2 - lo2)
    stc = k2.ewm(alpha=0.5, adjust=False, min_periods=5).mean()
    return (((c > 0).astype(float).fillna(0) + (f > 0).astype(float).fillna(0)
            + (s > 0).astype(float).fillna(0) + (lg > 0).astype(float).fillna(0)
            + (stc > 50).astype(float).fillna(0) + (dema_m > 0).astype(float).fillna(0)
            + (tema_m > 0).astype(float).fillna(0) + (zl_m > 0).astype(float).fillna(0)
            + (dema_m > 0).astype(float).fillna(0)).where(c.notna(), np.nan)).diff()


def f27_mcdt_287_extended_macd_universe_extreme_z_count_252_d1(close: pd.Series) -> pd.Series:
    """Count of MACD-universe variants with 252d z-score > 2."""
    c, _, _ = _macd(close, 12, 26, 9)
    z1 = _rolling_zscore(c, YDAYS, min_periods=QDAYS)
    z2 = _rolling_zscore(_ema(close, 5) - _ema(close, 35), YDAYS, min_periods=QDAYS)
    z3 = _rolling_zscore(_ema(close, 19) - _ema(close, 39), YDAYS, min_periods=QDAYS)
    z4 = _rolling_zscore(_ema(close, 50) - _ema(close, 200), YDAYS, min_periods=QDAYS)
    return (((z1 > 2).astype(float).fillna(0) + (z2 > 2).astype(float).fillna(0)

            + (z3 > 2).astype(float).fillna(0) + (z4 > 2).astype(float).fillna(0)).where(c.notna(), np.nan)).diff()


def f27_mcdt_288_extended_macd_universe_bearish_cross_count_21d_d1(close: pd.Series) -> pd.Series:
    """Count of MACD-universe variants with a bearish cross in past 21 bars."""
    cnt = pd.Series(0.0, index=close.index)
    for f, sl, sg in [(5, 35, 5), (12, 26, 9), (19, 39, 9), (50, 200, 30)]:
        m, s, _ = _macd(close, f, sl, sg)
        d = m - s
        ev = ((d.shift(1) > 0) & (d <= 0)).astype(float)
        cnt = cnt + (ev.rolling(MDAYS, min_periods=1).sum() > 0).astype(float).fillna(0)
    return (cnt.where(close.notna(), np.nan)).diff()


def f27_mcdt_289_extended_macd_universe_div_count_63_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """Count of MACD-universe variants with a current bearish divergence (63d)."""
    cnt = pd.Series(0.0, index=close.index)
    variants = {
        "classical": _ema(close, 12) - _ema(close, 26),
        "fast": _ema(close, 5) - _ema(close, 35),
        "slow": _ema(close, 19) - _ema(close, 39),
        "long": _ema(close, 50) - _ema(close, 200),
    }
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    for name, m in variants.items():
        prior_max = m.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
        div = (p_new & (m < prior_max)).astype(float)
        cnt = cnt + div.fillna(0)
    return (cnt.where(close.notna(), np.nan)).diff()


def f27_mcdt_290_extended_macd_universe_avg_zscore_252_d1(close: pd.Series) -> pd.Series:
    """Mean 252d z-score across MACD-universe variants — basket average extension."""
    c, _, _ = _macd(close, 12, 26, 9)
    z1 = _rolling_zscore(c, YDAYS, min_periods=QDAYS)
    z2 = _rolling_zscore(_ema(close, 5) - _ema(close, 35), YDAYS, min_periods=QDAYS)
    z3 = _rolling_zscore(_ema(close, 19) - _ema(close, 39), YDAYS, min_periods=QDAYS)
    z4 = _rolling_zscore(_ema(close, 50) - _ema(close, 200), YDAYS, min_periods=QDAYS)
    return ((z1 + z2 + z3 + z4) / 4.0).diff()


def f27_mcdt_291_extended_macd_universe_correlation_break_63_d1(close: pd.Series) -> pd.Series:
    """Average pairwise 63d correlation among {fast, classical, slow, long} MACDs minus same from 21 bars ago."""
    f = _ema(close, 5) - _ema(close, 35)
    c, _, _ = _macd(close, 12, 26, 9)
    s = _ema(close, 19) - _ema(close, 39)
    lg = _ema(close, 50) - _ema(close, 200)
    pairs = [
        f.rolling(QDAYS, min_periods=MDAYS).corr(c),
        f.rolling(QDAYS, min_periods=MDAYS).corr(s),
        f.rolling(QDAYS, min_periods=MDAYS).corr(lg),
        c.rolling(QDAYS, min_periods=MDAYS).corr(s),
        c.rolling(QDAYS, min_periods=MDAYS).corr(lg),
        s.rolling(QDAYS, min_periods=MDAYS).corr(lg),
    ]
    avg = sum(pairs) / float(len(pairs))
    return (avg - avg.shift(MDAYS)).diff()


def f27_mcdt_292_extended_macd_universe_persistence_score_252_d1(close: pd.Series) -> pd.Series:
    """Sum of bullish-dwell (frac of past 252 bars > 0) across MACD-universe variants."""
    c, _, _ = _macd(close, 12, 26, 9)
    f = _ema(close, 5) - _ema(close, 35)
    s = _ema(close, 19) - _ema(close, 39)
    lg = _ema(close, 50) - _ema(close, 200)
    return ((_dwell_above_zero_252(c).fillna(0) + _dwell_above_zero_252(f).fillna(0)

            + _dwell_above_zero_252(s).fillna(0) + _dwell_above_zero_252(lg).fillna(0)).diff())


def f27_mcdt_293_macd_terminal_distribution_score_at_top_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """At bars where close = 252d max: sum of {MACD<0, slope<0, bearish-cross<21d, regime-overdue>2x avg}.
    Else NaN — terminal-distribution composite score at price peak."""
    m, s, _ = _macd(close)
    at_max = close == close.rolling(YDAYS, min_periods=QDAYS).max()
    a = (m < 0).astype(float).fillna(0)
    sl = _rolling_slope(m, MDAYS)
    b = (sl < 0).astype(float).fillna(0)
    d = m - s
    be = ((d.shift(1) > 0) & (d <= 0)).astype(float)
    c = (be.rolling(MDAYS, min_periods=1).sum() > 0).astype(float).fillna(0)
    sg = np.sign(m).fillna(0).astype(int)
    block = (sg != sg.shift(1)).fillna(False).cumsum()
    age = (sg.groupby(block).cumcount() + 1).where(m.notna(), np.nan).astype(float)
    flip = (sg != sg.shift(1)).fillna(False).astype(float)
    avg = _safe_div(float(YDAYS), flip.rolling(YDAYS, min_periods=QDAYS).sum())
    e = (age > 2.0 * avg).astype(float).fillna(0)
    return ((a + b + c + e).where(at_max, np.nan)).diff()


def f27_mcdt_294_macd_blowoff_collapse_universe_count_d1(close: pd.Series) -> pd.Series:
    """Count of MACD-universe variants in blowoff-then-collapse state:
    hit 252d max within last 63d AND has dropped > 50% of that peak's magnitude since."""
    cnt = pd.Series(0.0, index=close.index)
    variants = [
        _ema(close, 5) - _ema(close, 35),
        _ema(close, 12) - _ema(close, 26),
        _ema(close, 19) - _ema(close, 39),
        _ema(close, 50) - _ema(close, 200),
    ]
    for m in variants:
        rmax = m.rolling(YDAYS, min_periods=QDAYS).max()
        bs = _bars_since_true(m == rmax)
        drop = (rmax - m) > 0.5 * rmax.abs()
        ind = ((bs <= QDAYS) & drop).astype(float).fillna(0)
        cnt = cnt + ind
    return (cnt.where(close.notna(), np.nan)).diff()


def f27_mcdt_295_macd_post_peak_decay_velocity_universe_d1(close: pd.Series) -> pd.Series:
    """Average (rolling 63d max - current value) across MACD-universe variants — basket decay magnitude."""
    variants = [
        _ema(close, 5) - _ema(close, 35),
        _ema(close, 12) - _ema(close, 26),
        _ema(close, 19) - _ema(close, 39),
        _ema(close, 50) - _ema(close, 200),
    ]
    decays = [(m.rolling(QDAYS, min_periods=MDAYS).max() - m) for m in variants]
    return (sum(decays) / float(len(decays))).diff()


def f27_mcdt_296_macd_combined_classical_alternative_consensus_d1(close: pd.Series) -> pd.Series:
    """Sign-agreement score: count of {classical MACD, hull-MACD, dema-MACD, kama-MACD-proxy}
    that share the same sign as classical MACD."""
    c, _, _ = _macd(close, 12, 26, 9)
    hm = _hma_local(close, 12) - _hma_local(close, 26)
    dema = _dema_local(close, 12) - _dema_local(close, 26)
    er = _safe_div(close.diff(10).abs(), close.diff().abs().rolling(10, min_periods=5).sum()).clip(0, 1).fillna(0)
    kama_alpha = (er * (2.0 / 3.0 - 2.0 / 31.0) + 2.0 / 31.0) ** 2
    alpha_scalar = float(kama_alpha.mean()) if kama_alpha.notna().any() else 0.1
    kama_smooth = close.ewm(alpha=max(alpha_scalar, 1e-3), adjust=False, min_periods=5).mean()
    km = kama_smooth - _ema(close, 26)
    sc = np.sign(c)
    return ((((np.sign(hm) == sc).astype(float).fillna(0)
            + (np.sign(dema) == sc).astype(float).fillna(0)
            + (np.sign(km) == sc).astype(float).fillna(0)
            + 1.0).where(c.notna(), np.nan)).diff())


def f27_mcdt_297_macd_modern_basket_alignment_score_d1(close: pd.Series) -> pd.Series:
    """Alignment score across modern MACD variants {STC>50, hull-MACD>0, ZLEMA-MACD>0, classical>0}."""
    f = _ema(close, 23) - _ema(close, 50)
    lo = f.rolling(10, min_periods=4).min(); hi = f.rolling(10, min_periods=4).max()
    k1 = 100.0 * _safe_div(f - lo, hi - lo)
    k1s = k1.ewm(alpha=0.5, adjust=False, min_periods=5).mean()
    lo2 = k1s.rolling(10, min_periods=4).min(); hi2 = k1s.rolling(10, min_periods=4).max()
    k2 = 100.0 * _safe_div(k1s - lo2, hi2 - lo2)
    stc = k2.ewm(alpha=0.5, adjust=False, min_periods=5).mean()
    hm = _hma_local(close, 12) - _hma_local(close, 26)
    zlm = _ema(2 * close - close.shift(5), 12) - _ema(2 * close - close.shift(12), 26)
    c, _, _ = _macd(close, 12, 26, 9)
    return ((((stc > 50).astype(float).fillna(0)
            + (hm > 0).astype(float).fillna(0)
            + (zlm > 0).astype(float).fillna(0)
            + (c > 0).astype(float).fillna(0)).where(c.notna(), np.nan)).diff())


def f27_mcdt_298_macd_modern_basket_dispersion_zscore_d1(close: pd.Series) -> pd.Series:
    """Std across z-scored modern MACD variants {classical, hull, zlema, dema}, then z-score (252d)."""
    c, _, _ = _macd(close, 12, 26, 9)
    z1 = _rolling_zscore(c, YDAYS, min_periods=QDAYS)
    hm = _hma_local(close, 12) - _hma_local(close, 26)
    z2 = _rolling_zscore(hm, YDAYS, min_periods=QDAYS)
    zlm = _ema(2 * close - close.shift(5), 12) - _ema(2 * close - close.shift(12), 26)
    z3 = _rolling_zscore(zlm, YDAYS, min_periods=QDAYS)
    dema = _dema_local(close, 12) - _dema_local(close, 26)
    z4 = _rolling_zscore(dema, YDAYS, min_periods=QDAYS)
    disp = pd.concat([z1.rename("a"), z2.rename("b"), z3.rename("c"), z4.rename("d")], axis=1).std(axis=1)
    return (_rolling_zscore(disp, YDAYS, min_periods=QDAYS)).diff()


def f27_mcdt_299_macd_terminal_aggregate_v2_score_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """Aggregate terminal score v2: sum of {basket bearish-cross>=2 in 21d, basket div>=2 in 63d,
    regime overdue>2x avg, MACD<0, basket decay>50% from 63d peak}."""
    a_cnt = pd.Series(0.0, index=close.index)
    for f, sl, sg in [(5, 35, 5), (12, 26, 9), (19, 39, 9), (50, 200, 30)]:
        m, s, _ = _macd(close, f, sl, sg)
        d = m - s
        ev = ((d.shift(1) > 0) & (d <= 0)).astype(float)
        a_cnt = a_cnt + (ev.rolling(MDAYS, min_periods=1).sum() > 0).astype(float).fillna(0)
    a = (a_cnt >= 2).astype(float).fillna(0)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    div_cnt = pd.Series(0.0, index=close.index)
    for f, sl in [(5, 35), (12, 26), (19, 39), (50, 200)]:
        mv = _ema(close, f) - _ema(close, sl)
        pm = mv.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
        div_cnt = div_cnt + (p_new & (mv < pm)).astype(float).fillna(0)
    b = (div_cnt >= 2).astype(float).fillna(0)
    m, _, _ = _macd(close)
    sg2 = np.sign(m).fillna(0).astype(int)
    block = (sg2 != sg2.shift(1)).fillna(False).cumsum()
    age = (sg2.groupby(block).cumcount() + 1).where(m.notna(), np.nan).astype(float)
    flip = (sg2 != sg2.shift(1)).fillna(False).astype(float)
    avg = _safe_div(float(YDAYS), flip.rolling(YDAYS, min_periods=QDAYS).sum())
    c = (age > 2.0 * avg).astype(float).fillna(0)
    d_ind = (m < 0).astype(float).fillna(0)
    decay_cnt = pd.Series(0.0, index=close.index)
    for f, sl in [(5, 35), (12, 26), (19, 39), (50, 200)]:
        mv = _ema(close, f) - _ema(close, sl)
        rmax = mv.rolling(YDAYS, min_periods=QDAYS).max()
        bs = _bars_since_true(mv == rmax)
        drop = (rmax - mv) > 0.5 * rmax.abs()
        decay_cnt = decay_cnt + ((bs <= QDAYS) & drop).astype(float).fillna(0)
    e = (decay_cnt >= 2).astype(float).fillna(0)
    return ((a + b + c + d_ind + e).where(m.notna(), np.nan)).diff()


def f27_mcdt_300_macd_extended_topping_master_score_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """Master extended-topping score: aggregate of {terminal v2, basket-univ-count-above-zero<2,
    extended-univ extreme-z>=1, multi-TF disagreement>=2}. Each contributes 1; sum is 0-4."""
    # 1) terminal v2 >= 3
    a_cnt = pd.Series(0.0, index=close.index)
    for f, sl, sg in [(5, 35, 5), (12, 26, 9), (19, 39, 9), (50, 200, 30)]:
        m, s, _ = _macd(close, f, sl, sg)
        d = m - s
        ev = ((d.shift(1) > 0) & (d <= 0)).astype(float)
        a_cnt = a_cnt + (ev.rolling(MDAYS, min_periods=1).sum() > 0).astype(float).fillna(0)
    a_terminal = (a_cnt >= 2).astype(float).fillna(0)
    # 2) basket count above zero < 2 (most variants negative)
    c, _, _ = _macd(close, 12, 26, 9)
    f = _ema(close, 5) - _ema(close, 35)
    s = _ema(close, 19) - _ema(close, 39)
    lg = _ema(close, 50) - _ema(close, 200)
    cnt_above = ((c > 0).astype(float).fillna(0) + (f > 0).astype(float).fillna(0)
                 + (s > 0).astype(float).fillna(0) + (lg > 0).astype(float).fillna(0))
    b_bear = (cnt_above < 2).astype(float).fillna(0)
    # 3) extended-univ extreme-z >=1 (any config z>2)
    z1 = _rolling_zscore(c, YDAYS, min_periods=QDAYS)
    z2 = _rolling_zscore(f, YDAYS, min_periods=QDAYS)
    z3 = _rolling_zscore(s, YDAYS, min_periods=QDAYS)
    z4 = _rolling_zscore(lg, YDAYS, min_periods=QDAYS)
    z_cnt = ((z1 > 2).astype(float).fillna(0) + (z2 > 2).astype(float).fillna(0)
             + (z3 > 2).astype(float).fillna(0) + (z4 > 2).astype(float).fillna(0))
    d_extreme = (z_cnt >= 1).astype(float).fillna(0)
    # 4) multi-TF disagreement >= 2 pairs disagree
    w = close.rolling(WDAYS, min_periods=WDAYS).mean()
    mw = _ema(w, 12) - _ema(w, 26)
    o = close.rolling(MDAYS, min_periods=MDAYS).mean()
    mm = _ema(o, 12) - _ema(o, 26)
    dis = ((c * mw < 0).astype(float).fillna(0)
           + (c * mm < 0).astype(float).fillna(0)
           + (mw * mm < 0).astype(float).fillna(0))
    e_tf = (dis >= 2).astype(float).fillna(0)
    return ((a_terminal + b_bear + d_extreme + e_tf).where(c.notna(), np.nan)).diff()


# ============================================================
#                         REGISTRY 226-300 (d1)
# ============================================================

MACD_TOPPING_DYNAMICS_D1_REGISTRY_226_300 = {
    "f27_mcdt_226_macd_realized_vol_normalized_21_d1": {"inputs": ["close"], "func": f27_mcdt_226_macd_realized_vol_normalized_21_d1},
    "f27_mcdt_227_macd_garch_proxy_normalized_d1": {"inputs": ["close"], "func": f27_mcdt_227_macd_garch_proxy_normalized_d1},
    "f27_mcdt_228_macd_during_high_vol_regime_state_d1": {"inputs": ["close"], "func": f27_mcdt_228_macd_during_high_vol_regime_state_d1},
    "f27_mcdt_229_macd_during_low_vol_regime_state_d1": {"inputs": ["close"], "func": f27_mcdt_229_macd_during_low_vol_regime_state_d1},
    "f27_mcdt_230_macd_vol_adjusted_bearish_cross_d1": {"inputs": ["close"], "func": f27_mcdt_230_macd_vol_adjusted_bearish_cross_d1},
    "f27_mcdt_231_macd_vol_adjusted_div_63_d1": {"inputs": ["high", "close"], "func": f27_mcdt_231_macd_vol_adjusted_div_63_d1},
    "f27_mcdt_232_ppo_garch_normalized_d1": {"inputs": ["close"], "func": f27_mcdt_232_ppo_garch_normalized_d1},
    "f27_mcdt_233_macd_vol_expansion_ratio_63_d1": {"inputs": ["close"], "func": f27_mcdt_233_macd_vol_expansion_ratio_63_d1},
    "f27_mcdt_234_macd_vol_contraction_ratio_63_d1": {"inputs": ["close"], "func": f27_mcdt_234_macd_vol_contraction_ratio_63_d1},
    "f27_mcdt_235_macd_vol_regime_shift_indicator_252_d1": {"inputs": ["close"], "func": f27_mcdt_235_macd_vol_regime_shift_indicator_252_d1},
    "f27_mcdt_236_macd_on_kalman_filtered_close_d1": {"inputs": ["close"], "func": f27_mcdt_236_macd_on_kalman_filtered_close_d1},
    "f27_mcdt_237_macd_on_kalman_above_zero_d1": {"inputs": ["close"], "func": f27_mcdt_237_macd_on_kalman_above_zero_d1},
    "f27_mcdt_238_macd_on_robust_smoother_d1": {"inputs": ["close"], "func": f27_mcdt_238_macd_on_robust_smoother_d1},
    "f27_mcdt_239_macd_on_hp_filter_smooth_d1": {"inputs": ["close"], "func": f27_mcdt_239_macd_on_hp_filter_smooth_d1},
    "f27_mcdt_240_macd_on_savgol_smooth_d1": {"inputs": ["close"], "func": f27_mcdt_240_macd_on_savgol_smooth_d1},
    "f27_mcdt_241_macd_on_lowpass_filter_5_d1": {"inputs": ["close"], "func": f27_mcdt_241_macd_on_lowpass_filter_5_d1},
    "f27_mcdt_242_macd_on_median_filter_7_d1": {"inputs": ["close"], "func": f27_mcdt_242_macd_on_median_filter_7_d1},
    "f27_mcdt_243_macd_on_robust_smoother_above_zero_state_d1": {"inputs": ["close"], "func": f27_mcdt_243_macd_on_robust_smoother_above_zero_state_d1},
    "f27_mcdt_244_macd_on_kalman_div_vs_price_63_d1": {"inputs": ["high", "close"], "func": f27_mcdt_244_macd_on_kalman_div_vs_price_63_d1},
    "f27_mcdt_245_macd_on_synthetic_smooth_zscore_252_d1": {"inputs": ["close"], "func": f27_mcdt_245_macd_on_synthetic_smooth_zscore_252_d1},
    "f27_mcdt_246_weekly_macd_resampled_5d_above_zero_d1": {"inputs": ["close"], "func": f27_mcdt_246_weekly_macd_resampled_5d_above_zero_d1},
    "f27_mcdt_247_monthly_macd_resampled_21d_above_zero_d1": {"inputs": ["close"], "func": f27_mcdt_247_monthly_macd_resampled_21d_above_zero_d1},
    "f27_mcdt_248_multi_tf_macd_alignment_state_d1": {"inputs": ["close"], "func": f27_mcdt_248_multi_tf_macd_alignment_state_d1},
    "f27_mcdt_249_multi_tf_macd_dispersion_d1": {"inputs": ["close"], "func": f27_mcdt_249_multi_tf_macd_dispersion_d1},
    "f27_mcdt_250_weekly_macd_bearish_cross_d1": {"inputs": ["close"], "func": f27_mcdt_250_weekly_macd_bearish_cross_d1},
    "f27_mcdt_251_monthly_macd_bearish_cross_d1": {"inputs": ["close"], "func": f27_mcdt_251_monthly_macd_bearish_cross_d1},
    "f27_mcdt_252_cross_tf_macd_divergence_count_d1": {"inputs": ["close"], "func": f27_mcdt_252_cross_tf_macd_divergence_count_d1},
    "f27_mcdt_253_weekly_macd_dwell_above_zero_252_d1": {"inputs": ["close"], "func": f27_mcdt_253_weekly_macd_dwell_above_zero_252_d1},
    "f27_mcdt_254_multi_tf_macd_consensus_score_d1": {"inputs": ["close"], "func": f27_mcdt_254_multi_tf_macd_consensus_score_d1},
    "f27_mcdt_255_tf_macd_lead_lag_difference_21_d1": {"inputs": ["close"], "func": f27_mcdt_255_tf_macd_lead_lag_difference_21_d1},
    "f27_mcdt_256_macd_information_ratio_with_returns_63_d1": {"inputs": ["close"], "func": f27_mcdt_256_macd_information_ratio_with_returns_63_d1},
    "f27_mcdt_257_macd_autocorrelation_lag_5_63_d1": {"inputs": ["close"], "func": f27_mcdt_257_macd_autocorrelation_lag_5_63_d1},
    "f27_mcdt_258_macd_kalman_innovation_residual_zscore_d1": {"inputs": ["close"], "func": f27_mcdt_258_macd_kalman_innovation_residual_zscore_d1},
    "f27_mcdt_259_macd_signal_to_noise_ratio_63_d1": {"inputs": ["close"], "func": f27_mcdt_259_macd_signal_to_noise_ratio_63_d1},
    "f27_mcdt_260_macd_predictability_zscore_252_d1": {"inputs": ["close"], "func": f27_mcdt_260_macd_predictability_zscore_252_d1},
    "f27_mcdt_261_macd_entropy_discretized_63_d1": {"inputs": ["close"], "func": f27_mcdt_261_macd_entropy_discretized_63_d1},
    "f27_mcdt_262_macd_persistence_correlation_63_d1": {"inputs": ["close"], "func": f27_mcdt_262_macd_persistence_correlation_63_d1},
    "f27_mcdt_263_macd_long_memory_hurst_proxy_63_d1": {"inputs": ["close"], "func": f27_mcdt_263_macd_long_memory_hurst_proxy_63_d1},
    "f27_mcdt_264_macd_chaos_lyapunov_proxy_63_d1": {"inputs": ["close"], "func": f27_mcdt_264_macd_chaos_lyapunov_proxy_63_d1},
    "f27_mcdt_265_macd_recurrence_quantification_proxy_63_d1": {"inputs": ["close"], "func": f27_mcdt_265_macd_recurrence_quantification_proxy_63_d1},
    "f27_mcdt_266_macd_rolling_min_63_zscore_d1": {"inputs": ["close"], "func": f27_mcdt_266_macd_rolling_min_63_zscore_d1},
    "f27_mcdt_267_macd_rolling_max_63_zscore_d1": {"inputs": ["close"], "func": f27_mcdt_267_macd_rolling_max_63_zscore_d1},
    "f27_mcdt_268_macd_rolling_iqr_63_d1": {"inputs": ["close"], "func": f27_mcdt_268_macd_rolling_iqr_63_d1},
    "f27_mcdt_269_macd_rolling_skew_63_zscore_d1": {"inputs": ["close"], "func": f27_mcdt_269_macd_rolling_skew_63_zscore_d1},
    "f27_mcdt_270_macd_rolling_kurt_63_zscore_d1": {"inputs": ["close"], "func": f27_mcdt_270_macd_rolling_kurt_63_zscore_d1},
    "f27_mcdt_271_macd_drawdown_from_max_63_d1": {"inputs": ["close"], "func": f27_mcdt_271_macd_drawdown_from_max_63_d1},
    "f27_mcdt_272_macd_running_drawdown_from_max_252_d1": {"inputs": ["close"], "func": f27_mcdt_272_macd_running_drawdown_from_max_252_d1},
    "f27_mcdt_273_macd_drawdown_recovery_rate_63_d1": {"inputs": ["close"], "func": f27_mcdt_273_macd_drawdown_recovery_rate_63_d1},
    "f27_mcdt_274_macd_rolling_sharpe_ratio_proxy_63_d1": {"inputs": ["close"], "func": f27_mcdt_274_macd_rolling_sharpe_ratio_proxy_63_d1},
    "f27_mcdt_275_macd_rolling_sortino_proxy_63_d1": {"inputs": ["close"], "func": f27_mcdt_275_macd_rolling_sortino_proxy_63_d1},
    "f27_mcdt_276_macd_regime_above_zero_persistence_d1": {"inputs": ["close"], "func": f27_mcdt_276_macd_regime_above_zero_persistence_d1},
    "f27_mcdt_277_macd_regime_below_zero_persistence_d1": {"inputs": ["close"], "func": f27_mcdt_277_macd_regime_below_zero_persistence_d1},
    "f27_mcdt_278_macd_regime_change_count_252_d1": {"inputs": ["close"], "func": f27_mcdt_278_macd_regime_change_count_252_d1},
    "f27_mcdt_279_macd_regime_duration_252_zscore_d1": {"inputs": ["close"], "func": f27_mcdt_279_macd_regime_duration_252_zscore_d1},
    "f27_mcdt_280_macd_regime_age_current_d1": {"inputs": ["close"], "func": f27_mcdt_280_macd_regime_age_current_d1},
    "f27_mcdt_281_macd_avg_regime_duration_252_d1": {"inputs": ["close"], "func": f27_mcdt_281_macd_avg_regime_duration_252_d1},
    "f27_mcdt_282_macd_regime_transition_velocity_d1": {"inputs": ["close"], "func": f27_mcdt_282_macd_regime_transition_velocity_d1},
    "f27_mcdt_283_macd_regime_volatility_within_d1": {"inputs": ["close"], "func": f27_mcdt_283_macd_regime_volatility_within_d1},
    "f27_mcdt_284_macd_regime_age_to_avg_ratio_d1": {"inputs": ["close"], "func": f27_mcdt_284_macd_regime_age_to_avg_ratio_d1},
    "f27_mcdt_285_macd_regime_terminal_indicator_d1": {"inputs": ["close"], "func": f27_mcdt_285_macd_regime_terminal_indicator_d1},
    "f27_mcdt_286_extended_macd_universe_count_above_zero_d1": {"inputs": ["close"], "func": f27_mcdt_286_extended_macd_universe_count_above_zero_d1},
    "f27_mcdt_287_extended_macd_universe_extreme_z_count_252_d1": {"inputs": ["close"], "func": f27_mcdt_287_extended_macd_universe_extreme_z_count_252_d1},
    "f27_mcdt_288_extended_macd_universe_bearish_cross_count_21d_d1": {"inputs": ["close"], "func": f27_mcdt_288_extended_macd_universe_bearish_cross_count_21d_d1},
    "f27_mcdt_289_extended_macd_universe_div_count_63_d1": {"inputs": ["high", "close"], "func": f27_mcdt_289_extended_macd_universe_div_count_63_d1},
    "f27_mcdt_290_extended_macd_universe_avg_zscore_252_d1": {"inputs": ["close"], "func": f27_mcdt_290_extended_macd_universe_avg_zscore_252_d1},
    "f27_mcdt_291_extended_macd_universe_correlation_break_63_d1": {"inputs": ["close"], "func": f27_mcdt_291_extended_macd_universe_correlation_break_63_d1},
    "f27_mcdt_292_extended_macd_universe_persistence_score_252_d1": {"inputs": ["close"], "func": f27_mcdt_292_extended_macd_universe_persistence_score_252_d1},
    "f27_mcdt_293_macd_terminal_distribution_score_at_top_d1": {"inputs": ["high", "close"], "func": f27_mcdt_293_macd_terminal_distribution_score_at_top_d1},
    "f27_mcdt_294_macd_blowoff_collapse_universe_count_d1": {"inputs": ["close"], "func": f27_mcdt_294_macd_blowoff_collapse_universe_count_d1},
    "f27_mcdt_295_macd_post_peak_decay_velocity_universe_d1": {"inputs": ["close"], "func": f27_mcdt_295_macd_post_peak_decay_velocity_universe_d1},
    "f27_mcdt_296_macd_combined_classical_alternative_consensus_d1": {"inputs": ["close"], "func": f27_mcdt_296_macd_combined_classical_alternative_consensus_d1},
    "f27_mcdt_297_macd_modern_basket_alignment_score_d1": {"inputs": ["close"], "func": f27_mcdt_297_macd_modern_basket_alignment_score_d1},
    "f27_mcdt_298_macd_modern_basket_dispersion_zscore_d1": {"inputs": ["close"], "func": f27_mcdt_298_macd_modern_basket_dispersion_zscore_d1},
    "f27_mcdt_299_macd_terminal_aggregate_v2_score_d1": {"inputs": ["high", "close"], "func": f27_mcdt_299_macd_terminal_aggregate_v2_score_d1},
    "f27_mcdt_300_macd_extended_topping_master_score_d1": {"inputs": ["high", "close"], "func": f27_mcdt_300_macd_extended_topping_master_score_d1},
}
