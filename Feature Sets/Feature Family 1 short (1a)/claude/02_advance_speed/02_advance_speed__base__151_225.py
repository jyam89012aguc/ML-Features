"""advance_speed base features 151-225 — Pipeline 1a-inverse short-side blowup family (gap-fill extension).

Extension beyond the original 150 — fills audit-identified gaps for advance-speed / velocity detection.
This file carries indices 151-157 (7 distinct hypotheses). Reserved range up to 225.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(-N). Self-contained — no imports across families.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5


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


def _true_range(high, low, close):
    pc = close.shift(1)
    return pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)


def _atr(high, low, close, n=21):
    return _true_range(high, low, close).rolling(n, min_periods=max(n // 3, 2)).mean()


# ============================================================
#                    FEATURES 151-157
# ============================================================


def f02_advs_151_anchored_vwap_from_trough_velocity(close: pd.Series, volume: pd.Series, low: pd.Series) -> pd.Series:
    """Log distance of close above anchored VWAP starting from the 252d trough bar.

    PIT-clean: trough anchor is the bar where rolling-252d-low is set (right-anchored argmin
    on the trailing 252d window). Cumulative (close*volume)/volume is summed FROM that anchor
    forward up to the current bar t (inclusive).
    """
    c = close.to_numpy(dtype=float)
    v = volume.to_numpy(dtype=float)
    lo = low.to_numpy(dtype=float)
    n = len(c)
    out = np.full(n, np.nan, dtype=float)
    if n == 0:
        return pd.Series(out, index=close.index)
    pv = c * v
    cum_pv = np.concatenate(([0.0], np.nancumsum(pv)))
    cum_v = np.concatenate(([0.0], np.nancumsum(v)))
    for t in range(n):
        start = max(0, t - YDAYS + 1)
        win = lo[start:t + 1]
        valid = ~np.isnan(win)
        if valid.sum() < QDAYS:
            continue
        masked = np.where(valid, win, np.inf)
        anchor_local = int(np.argmin(masked))
        anchor = start + anchor_local
        v_sum = cum_v[t + 1] - cum_v[anchor]
        pv_sum = cum_pv[t + 1] - cum_pv[anchor]
        if not np.isfinite(v_sum) or v_sum <= 0 or not np.isfinite(pv_sum):
            continue
        avwap = pv_sum / v_sum
        if not np.isfinite(avwap) or avwap <= 0 or not np.isfinite(c[t]) or c[t] <= 0:
            continue
        out[t] = float(np.log(c[t] / avwap))
    return pd.Series(out, index=close.index)


def f02_advs_152_days_to_double_from_252d_low(close: pd.Series, low: pd.Series) -> pd.Series:
    """Bars between the 252d-low date and first close >= 2 * (252d low). NaN if never reached."""
    c = close.to_numpy(dtype=float)
    lo = low.to_numpy(dtype=float)
    n = len(c)
    out = np.full(n, np.nan, dtype=float)
    for t in range(n):
        start = max(0, t - YDAYS + 1)
        win = lo[start:t + 1]
        valid = ~np.isnan(win)
        if valid.sum() < QDAYS:
            continue
        masked = np.where(valid, win, np.inf)
        anchor_local = int(np.argmin(masked))
        trough_val = win[anchor_local]
        if not np.isfinite(trough_val) or trough_val <= 0:
            continue
        anchor = start + anchor_local
        target = 2.0 * trough_val
        post = c[anchor:t + 1]
        hits = np.where(np.isfinite(post) & (post >= target))[0]
        if len(hits) == 0:
            continue
        out[t] = float(hits[0])
    return pd.Series(out, index=close.index)


def f02_advs_153_days_to_triple_from_252d_low(close: pd.Series, low: pd.Series) -> pd.Series:
    """Bars between the 252d-low date and first close >= 3 * (252d low). NaN if never reached."""
    c = close.to_numpy(dtype=float)
    lo = low.to_numpy(dtype=float)
    n = len(c)
    out = np.full(n, np.nan, dtype=float)
    for t in range(n):
        start = max(0, t - YDAYS + 1)
        win = lo[start:t + 1]
        valid = ~np.isnan(win)
        if valid.sum() < QDAYS:
            continue
        masked = np.where(valid, win, np.inf)
        anchor_local = int(np.argmin(masked))
        trough_val = win[anchor_local]
        if not np.isfinite(trough_val) or trough_val <= 0:
            continue
        anchor = start + anchor_local
        target = 3.0 * trough_val
        post = c[anchor:t + 1]
        hits = np.where(np.isfinite(post) & (post >= target))[0]
        if len(hits) == 0:
            continue
        out[t] = float(hits[0])
    return pd.Series(out, index=close.index)


def f02_advs_154_cornish_fisher_var_velocity_63d(close: pd.Series) -> pd.Series:
    """Cornish-Fisher adjusted 5% VaR of log returns over 63d.

    z0 = -1.6449; CF_z = z0 + (z0^2 - 1)*S/6 + (z0^3 - 3*z0)*K/24 - (2*z0^3 - 5*z0)*S^2/36.
    Returns mu + sigma * CF_z (sample skewness S, excess kurtosis K from rolling 63d).
    """
    r = _safe_log(close).diff()

    def _cf(w):
        valid = ~np.isnan(w)
        x = w[valid]
        n = len(x)
        if n < MDAYS:
            return np.nan
        mu = float(x.mean())
        sd = float(x.std(ddof=1))
        if sd == 0 or not np.isfinite(sd):
            return np.nan
        z = (x - mu) / sd
        m3 = float((z ** 3).mean())
        m4 = float((z ** 4).mean())
        S = m3
        K = m4 - 3.0
        z0 = -1.6449
        cf_z = (z0
                + (z0 ** 2 - 1.0) * S / 6.0
                + (z0 ** 3 - 3.0 * z0) * K / 24.0
                - (2.0 * z0 ** 3 - 5.0 * z0) * (S ** 2) / 36.0)
        return mu + sd * cf_z

    return r.rolling(QDAYS, min_periods=MDAYS).apply(_cf, raw=True)


def f02_advs_155_sortino_ratio_252d(close: pd.Series) -> pd.Series:
    """Sortino: mean(r) / sqrt(mean(min(r,0)^2)) over 252d, r = log(close).diff()."""
    r = _safe_log(close).diff()
    neg_sq = np.minimum(r, 0.0) ** 2
    mu = r.rolling(YDAYS, min_periods=QDAYS).mean()
    dnvar = neg_sq.rolling(YDAYS, min_periods=QDAYS).mean()
    dnstd = np.sqrt(dnvar)
    return _safe_div(mu, dnstd)


def f02_advs_156_calmar_ratio_252d(close: pd.Series) -> pd.Series:
    """Calmar: 252d log return / |max drawdown over 252d|."""
    lc = _safe_log(close)
    log_ret_252 = lc - lc.shift(YDAYS)

    def _mdd(w):
        valid = ~np.isnan(w)
        x = w[valid]
        if len(x) < QDAYS:
            return np.nan
        cummax = np.maximum.accumulate(x)
        dd = (x - cummax) / cummax
        return float(dd.min())

    mdd = close.rolling(YDAYS, min_periods=QDAYS).apply(_mdd, raw=True)
    return _safe_div(log_ret_252, mdd.abs())


def f02_advs_157_speed_in_low_vs_high_vol_regime_ratio_252d(close: pd.Series) -> pd.Series:
    """Ratio of mean log-return in low-vol regime vs high-vol regime over 252d.

    rvol_21d = rolling std of log returns over 21d. Threshold = median(rvol_21d) within 252d window.
    Returns mean(r | rvol_21d < thresh) / mean(r | rvol_21d >= thresh) over the 252d window.
    """
    r = _safe_log(close).diff()
    rvol = r.rolling(MDAYS, min_periods=WDAYS).std(ddof=1)
    arr = np.column_stack([r.to_numpy(dtype=float), rvol.to_numpy(dtype=float)])
    n = arr.shape[0]
    out = np.full(n, np.nan, dtype=float)
    for t in range(n):
        start = max(0, t - YDAYS + 1)
        win = arr[start:t + 1]
        rv = win[:, 1]
        rr = win[:, 0]
        valid = np.isfinite(rv) & np.isfinite(rr)
        if valid.sum() < QDAYS:
            continue
        rv_v = rv[valid]
        rr_v = rr[valid]
        thresh = float(np.median(rv_v))
        if not np.isfinite(thresh):
            continue
        lo_mask = rv_v < thresh
        hi_mask = rv_v >= thresh
        if lo_mask.sum() < WDAYS or hi_mask.sum() < WDAYS:
            continue
        mu_lo = float(rr_v[lo_mask].mean())
        mu_hi = float(rr_v[hi_mask].mean())
        if mu_hi == 0 or not np.isfinite(mu_hi):
            continue
        out[t] = mu_lo / mu_hi
    return pd.Series(out, index=close.index).replace([np.inf, -np.inf], np.nan)


# ============================================================
#                    REGISTRY
# ============================================================

ADVANCE_SPEED_BASE_REGISTRY_151_225 = {
    "f02_advs_151_anchored_vwap_from_trough_velocity": {"inputs": ["close", "volume", "low"], "func": f02_advs_151_anchored_vwap_from_trough_velocity},
    "f02_advs_152_days_to_double_from_252d_low": {"inputs": ["close", "low"], "func": f02_advs_152_days_to_double_from_252d_low},
    "f02_advs_153_days_to_triple_from_252d_low": {"inputs": ["close", "low"], "func": f02_advs_153_days_to_triple_from_252d_low},
    "f02_advs_154_cornish_fisher_var_velocity_63d": {"inputs": ["close"], "func": f02_advs_154_cornish_fisher_var_velocity_63d},
    "f02_advs_155_sortino_ratio_252d": {"inputs": ["close"], "func": f02_advs_155_sortino_ratio_252d},
    "f02_advs_156_calmar_ratio_252d": {"inputs": ["close"], "func": f02_advs_156_calmar_ratio_252d},
    "f02_advs_157_speed_in_low_vs_high_vol_regime_ratio_252d": {"inputs": ["close"], "func": f02_advs_157_speed_in_low_vs_high_vol_regime_ratio_252d},
}
