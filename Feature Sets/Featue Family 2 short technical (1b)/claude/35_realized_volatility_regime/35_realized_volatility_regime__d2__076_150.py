"""realized_volatility_regime d2 features 076-150 — Pipeline 1b-technical.

Continuation of __base__001_075.py — see that file's header for the full
hypothesis split across buckets. This file covers:
sign-symmetric vol, vol term-structure slope, vol entropy / dispersion,
vol break / structural-shift detectors, annualized normalizations,
volume-weighted vol, multi-frequency vol (non-overlap), vol-distribution
moments, vol clustering / run length, cumulative variance, overnight +
intraday RV split.

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
# Bucket I — Sign-symmetric vol 076-081
# Use |r|, r^2, RMS — symmetric measures only (asymmetry owned by family 36)
# ============================================================

def f35_rvre_076_mean_abs_return_21d(close: pd.Series) -> pd.Series:
    """Mean of |log returns| over 21d — first absolute moment, monthly."""
    r = _log_returns(close).abs()
    return r.rolling(MDAYS, min_periods=WDAYS).mean()


def f35_rvre_077_mean_abs_return_252d(close: pd.Series) -> pd.Series:
    """Mean of |log returns| over 252d — first absolute moment, annual."""
    r = _log_returns(close).abs()
    return r.rolling(YDAYS, min_periods=QDAYS).mean()


def f35_rvre_078_rms_return_21d(close: pd.Series) -> pd.Series:
    """Root-mean-square log return over 21d — uncentered second moment."""
    r = _log_returns(close)
    return np.sqrt((r ** 2).rolling(MDAYS, min_periods=WDAYS).mean())


def f35_rvre_079_rms_return_252d(close: pd.Series) -> pd.Series:
    """RMS log return over 252d — uncentered annual second moment."""
    r = _log_returns(close)
    return np.sqrt((r ** 2).rolling(YDAYS, min_periods=QDAYS).mean())


def f35_rvre_080_geom_mean_abs_return_63d(close: pd.Series) -> pd.Series:
    """Geometric mean of |log returns| over 63d — log-scale central tendency."""
    r = _log_returns(close).abs()
    lr = _safe_log(r)
    return np.exp(lr.rolling(QDAYS, min_periods=MDAYS).mean())


def f35_rvre_081_sum_abs_return_252d(close: pd.Series) -> pd.Series:
    """Sum of |log returns| over 252d — total absolute travel (vol-points)."""
    r = _log_returns(close).abs()
    return r.rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket J — Vol term-structure 082-087
# Slope / curvature / R^2 / intercept of log(RV) vs log(horizon)
# ============================================================

def _term_struct_slope(close: pd.Series, horizons: list) -> pd.Series:
    """For each bar t, regress log(RV_h(t)) on log(h) across given horizons; return slope."""
    r = _log_returns(close)
    rvs = []
    for h in horizons:
        mp = max(h // 3, 2)
        rv = r.rolling(h, min_periods=mp).std()
        rvs.append(_safe_log(rv).rename(f"h{h}"))
    df = pd.concat(rvs, axis=1)
    logh = np.log(np.array(horizons, dtype=float))
    xm = logh.mean()
    xc = logh - xm
    xss = (xc ** 2).sum()
    arr = df.values
    n = arr.shape[0]
    out = np.full(n, np.nan)
    for i in range(n):
        y = arr[i]
        mask = ~np.isnan(y)
        if mask.sum() < 2:
            continue
        x = xc[mask]
        yv = y[mask]
        ym = yv.mean()
        denom = (x ** 2).sum()
        if denom <= 0:
            continue
        out[i] = float(((x) * (yv - ym)).sum() / denom)
    return pd.Series(out, index=close.index)


def _term_struct_curvature(close: pd.Series, horizons: list) -> pd.Series:
    """Second difference of log(RV) across sorted horizons (proxy for curvature)."""
    r = _log_returns(close)
    rvs = []
    for h in horizons:
        mp = max(h // 3, 2)
        rv = r.rolling(h, min_periods=mp).std()
        rvs.append(_safe_log(rv).rename(f"h{h}"))
    df = pd.concat(rvs, axis=1)
    arr = df.values
    n, k = arr.shape
    if k < 3:
        return pd.Series(np.nan, index=close.index)
    out = np.full(n, np.nan)
    for i in range(n):
        y = arr[i]
        if np.isnan(y).any():
            continue
        # average second differences across log-horizon spacings
        out[i] = float((y[2:] - 2.0 * y[1:-1] + y[:-2]).mean())
    return pd.Series(out, index=close.index)


def _term_struct_r2(close: pd.Series, horizons: list) -> pd.Series:
    """R-squared of regression log(RV) ~ log(horizon) — quality of term-structure fit."""
    r = _log_returns(close)
    rvs = []
    for h in horizons:
        mp = max(h // 3, 2)
        rv = r.rolling(h, min_periods=mp).std()
        rvs.append(_safe_log(rv).rename(f"h{h}"))
    df = pd.concat(rvs, axis=1)
    logh = np.log(np.array(horizons, dtype=float))
    arr = df.values
    n = arr.shape[0]
    out = np.full(n, np.nan)
    for i in range(n):
        y = arr[i]
        mask = ~np.isnan(y)
        if mask.sum() < 3:
            continue
        x = logh[mask]
        yv = y[mask]
        xm = x.mean(); ym = yv.mean()
        xc = x - xm; yc = yv - ym
        sxx = (xc ** 2).sum()
        syy = (yc ** 2).sum()
        sxy = (xc * yc).sum()
        if sxx <= 0 or syy <= 0:
            continue
        out[i] = float((sxy ** 2) / (sxx * syy))
    return pd.Series(out, index=close.index)


def _term_struct_intercept(close: pd.Series, horizons: list) -> pd.Series:
    """Intercept of regression log(RV) on log(horizon)."""
    r = _log_returns(close)
    rvs = []
    for h in horizons:
        mp = max(h // 3, 2)
        rv = r.rolling(h, min_periods=mp).std()
        rvs.append(_safe_log(rv).rename(f"h{h}"))
    df = pd.concat(rvs, axis=1)
    logh = np.log(np.array(horizons, dtype=float))
    arr = df.values
    n = arr.shape[0]
    out = np.full(n, np.nan)
    for i in range(n):
        y = arr[i]
        mask = ~np.isnan(y)
        if mask.sum() < 2:
            continue
        x = logh[mask]
        yv = y[mask]
        xm = x.mean(); ym = yv.mean()
        xc = x - xm
        denom = (xc ** 2).sum()
        if denom <= 0:
            continue
        slope = float(((xc) * (yv - ym)).sum() / denom)
        out[i] = float(ym - slope * xm)
    return pd.Series(out, index=close.index)


def f35_rvre_082_term_struct_slope_5_21_63_252(close: pd.Series) -> pd.Series:
    """Slope of log(RV) vs log(horizon) over {5,21,63,252} — vol term-structure tilt."""
    return _term_struct_slope(close, [WDAYS, MDAYS, QDAYS, YDAYS])


def f35_rvre_083_term_struct_slope_21_63_252_504(close: pd.Series) -> pd.Series:
    """Slope of log(RV) vs log(horizon) over {21,63,252,504} — long-end vol tilt."""
    return _term_struct_slope(close, [MDAYS, QDAYS, YDAYS, DDAYS_2Y])


def f35_rvre_084_term_struct_slope_5_21_63(close: pd.Series) -> pd.Series:
    """Slope of log(RV) vs log(horizon) over {5,21,63} — short-end vol tilt."""
    return _term_struct_slope(close, [WDAYS, MDAYS, QDAYS])


def f35_rvre_085_term_struct_curvature_5_21_63_252(close: pd.Series) -> pd.Series:
    """Mean second-difference of log(RV) across {5,21,63,252} — concavity of vol curve."""
    return _term_struct_curvature(close, [WDAYS, MDAYS, QDAYS, YDAYS])


def f35_rvre_086_term_struct_r2_5_21_63_252(close: pd.Series) -> pd.Series:
    """R^2 of log(RV) vs log(horizon) over {5,21,63,252} — term-structure fit quality."""
    return _term_struct_r2(close, [WDAYS, MDAYS, QDAYS, YDAYS])


def f35_rvre_087_term_struct_intercept_5_21_63_252(close: pd.Series) -> pd.Series:
    """Intercept of log(RV) vs log(horizon) over {5,21,63,252} — baseline (h=1) vol."""
    return _term_struct_intercept(close, [WDAYS, MDAYS, QDAYS, YDAYS])


# ============================================================
# Bucket K — Vol entropy / vol dispersion across sub-windows 088-093
# ============================================================

def f35_rvre_088_entropy_abs_r_252d(close: pd.Series) -> pd.Series:
    """Shannon entropy (base 2) of |log returns| binned into 8 equal-width bins over 252d."""
    r = _log_returns(close).abs()
    def _ent(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        lo = v.min(); hi = v.max()
        if hi <= lo:
            return 0.0
        bins = np.linspace(lo, hi, 9)
        cnt, _ = np.histogram(v, bins=bins)
        cnt = cnt[cnt > 0]
        if cnt.size == 0:
            return np.nan
        p = cnt.astype(float) / cnt.sum()
        return float(-(p * np.log2(p)).sum())
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_ent, raw=True)


def f35_rvre_089_entropy_abs_r_504d(close: pd.Series) -> pd.Series:
    """Shannon entropy of |log returns| in 8 equal-width bins over 504d."""
    r = _log_returns(close).abs()
    def _ent(w):
        v = w[~np.isnan(w)]
        if v.size < 60:
            return np.nan
        lo = v.min(); hi = v.max()
        if hi <= lo:
            return 0.0
        bins = np.linspace(lo, hi, 9)
        cnt, _ = np.histogram(v, bins=bins)
        cnt = cnt[cnt > 0]
        if cnt.size == 0:
            return np.nan
        p = cnt.astype(float) / cnt.sum()
        return float(-(p * np.log2(p)).sum())
    return r.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_ent, raw=True)


def f35_rvre_090_gini_abs_r_252d(close: pd.Series) -> pd.Series:
    """Gini coefficient of |log returns| over 252d — concentration of return magnitude."""
    r = _log_returns(close).abs()
    def _gini(w):
        v = w[~np.isnan(w)]
        v = v[v >= 0]
        if v.size < 10:
            return np.nan
        v = np.sort(v)
        n = v.size
        s = v.sum()
        if s <= 0:
            return np.nan
        idx = np.arange(1, n + 1)
        return float((2.0 * (idx * v).sum() - (n + 1) * s) / (n * s))
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_gini, raw=True)


def f35_rvre_091_dispersion_ratio_rv21_in_252d(close: pd.Series) -> pd.Series:
    """std/mean of 21d-RV series over trailing 252d — distinct from CV by normalization context."""
    r = _log_returns(close)
    rv21 = r.rolling(MDAYS, min_periods=WDAYS).std()
    m = rv21.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = rv21.rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_div(sd, m)


def f35_rvre_092_subwindow_vol_dispersion_252d(close: pd.Series) -> pd.Series:
    """Std of 4 non-overlapping 63d-RVs covering trailing 252d — dispersion of sub-window vols."""
    r = _log_returns(close)
    def _disp(w):
        v = w[~np.isnan(w)]
        if v.size < 200:
            return np.nan
        n = v.size
        seg = n // 4
        if seg < 5:
            return np.nan
        sds = np.empty(4)
        for k in range(4):
            chunk = v[k * seg:(k + 1) * seg]
            if chunk.size < 5:
                return np.nan
            sds[k] = chunk.std(ddof=1)
        return float(np.std(sds, ddof=1))
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_disp, raw=True)


def f35_rvre_093_subwindow_vol_dispersion_504d(close: pd.Series) -> pd.Series:
    """Std of 8 non-overlapping 63d-RVs covering trailing 504d — broader-base sub-window dispersion."""
    r = _log_returns(close)
    def _disp(w):
        v = w[~np.isnan(w)]
        if v.size < 400:
            return np.nan
        n = v.size
        seg = n // 8
        if seg < 5:
            return np.nan
        sds = np.empty(8)
        for k in range(8):
            chunk = v[k * seg:(k + 1) * seg]
            if chunk.size < 5:
                return np.nan
            sds[k] = chunk.std(ddof=1)
        return float(np.std(sds, ddof=1))
    return r.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_disp, raw=True)


# ============================================================
# Bucket L — Vol break / structural-shift detectors 094-103
# ============================================================

def f35_rvre_094_cusum_rsq_max_abs_252d(close: pd.Series) -> pd.Series:
    """Max |CUSUM| of centered r^2 over trailing 252d — structural-break magnitude."""
    r = _log_returns(close)
    rsq = r ** 2
    def _cusum(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        x = v - v.mean()
        cs = np.cumsum(x)
        return float(np.max(np.abs(cs)))
    return rsq.rolling(YDAYS, min_periods=QDAYS).apply(_cusum, raw=True)


def f35_rvre_095_cusum_abs_r_max_abs_504d(close: pd.Series) -> pd.Series:
    """Max |CUSUM| of centered |r| over trailing 504d — magnitude-level structural break."""
    r = _log_returns(close).abs()
    def _cusum(w):
        v = w[~np.isnan(w)]
        if v.size < 60:
            return np.nan
        x = v - v.mean()
        cs = np.cumsum(x)
        return float(np.max(np.abs(cs)))
    return r.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_cusum, raw=True)


def f35_rvre_096_jump_ratio_max_to_median_abs_r_21d(close: pd.Series) -> pd.Series:
    """max(|r|) / median(|r|) over 21d — single-bar jump indicator."""
    r = _log_returns(close).abs()
    mx = r.rolling(MDAYS, min_periods=WDAYS).max()
    md = r.rolling(MDAYS, min_periods=WDAYS).median()
    return _safe_div(mx, md)


def f35_rvre_097_rv_ratio_test_21_vs_252(close: pd.Series) -> pd.Series:
    """Log-ratio (var_21d / var_252d) — variance-equality test statistic, log space."""
    r = _log_returns(close)
    v21 = (r.rolling(MDAYS, min_periods=WDAYS).std()) ** 2
    v252 = (r.rolling(YDAYS, min_periods=QDAYS).std()) ** 2
    return _safe_log(_safe_div(v21, v252))


def f35_rvre_098_welch_rv_ratio_63_vs_504(close: pd.Series) -> pd.Series:
    """Welch-style log-ratio var_63 / var_504 — long-horizon variance shift."""
    r = _log_returns(close)
    v63 = (r.rolling(QDAYS, min_periods=MDAYS).std()) ** 2
    v504 = (r.rolling(DDAYS_2Y, min_periods=YDAYS).std()) ** 2
    return _safe_log(_safe_div(v63, v504))


def f35_rvre_099_max_diff_rv21_vs_rv252_over_21d(close: pd.Series) -> pd.Series:
    """Max |RV21 - RV252| over trailing 21d — local vol-break magnitude."""
    r = _log_returns(close)
    rv21 = r.rolling(MDAYS, min_periods=WDAYS).std()
    rv252 = r.rolling(YDAYS, min_periods=QDAYS).std()
    return (rv21 - rv252).abs().rolling(MDAYS, min_periods=WDAYS).max()


def f35_rvre_100_max_zscore_abs_r_in_21d(close: pd.Series) -> pd.Series:
    """Max z-score of |r| (vs 252d distribution) over trailing 21d — extreme-bar detector."""
    r = _log_returns(close).abs()
    z = _rolling_zscore(r, YDAYS, min_periods=QDAYS)
    return z.rolling(MDAYS, min_periods=WDAYS).max()


def f35_rvre_101_fraction_bars_above_3mad_in_63d(close: pd.Series) -> pd.Series:
    """Fraction of bars in trailing 63d with |r-median| > 3*MAD of 63d distribution — tail-share."""
    r = _log_returns(close)
    med = r.rolling(QDAYS, min_periods=MDAYS).median()
    mad = (r - med).abs().rolling(QDAYS, min_periods=MDAYS).median()
    z = (r - med).abs() / (1.4826 * mad).replace(0, np.nan)
    flag = (z > 3.0).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).mean()


def f35_rvre_102_largest_jump_rv21_change_in_252d(close: pd.Series) -> pd.Series:
    """Largest single-bar change in 21d-RV over trailing 252d — vol-jump magnitude."""
    r = _log_returns(close)
    rv21 = r.rolling(MDAYS, min_periods=WDAYS).std()
    return rv21.diff().abs().rolling(YDAYS, min_periods=QDAYS).max()


def f35_rvre_103_count_vol_jumps_abs_r_above_4sigma_in_252d(close: pd.Series) -> pd.Series:
    """Count of bars in trailing 252d where |r| > 4 * 252d-RV — extreme-jump count."""
    r = _log_returns(close)
    sigma = r.rolling(YDAYS, min_periods=QDAYS).std()
    flag = (r.abs() > 4.0 * sigma).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket M — Annualized normalizations & scale-invariant ratios 104-111
# ============================================================

def f35_rvre_104_ann_rv_21d(close: pd.Series) -> pd.Series:
    """Annualized 21d RV: sqrt(252) * std(log returns, 21d)."""
    r = _log_returns(close)
    return r.rolling(MDAYS, min_periods=WDAYS).std() * np.sqrt(float(YDAYS))


def f35_rvre_105_ann_rv_63d(close: pd.Series) -> pd.Series:
    """Annualized 63d RV: sqrt(252) * std(log returns, 63d)."""
    r = _log_returns(close)
    return r.rolling(QDAYS, min_periods=MDAYS).std() * np.sqrt(float(YDAYS))


def f35_rvre_106_ann_rv_252d(close: pd.Series) -> pd.Series:
    """Annualized 252d RV — direct annual realized volatility."""
    r = _log_returns(close)
    return r.rolling(YDAYS, min_periods=QDAYS).std() * np.sqrt(float(YDAYS))


def f35_rvre_107_ratio_ann_rv21_to_ann_rv252(close: pd.Series) -> pd.Series:
    """Ratio of annualized 21d-RV to annualized 252d-RV (sqrt-252 cancels — pure scale-invariant ratio)."""
    r = _log_returns(close)
    a = r.rolling(MDAYS, min_periods=WDAYS).std() * np.sqrt(float(YDAYS))
    b = r.rolling(YDAYS, min_periods=QDAYS).std() * np.sqrt(float(YDAYS))
    return _safe_div(a, b)


def f35_rvre_108_ratio_ann_rv5_to_ann_rv21(close: pd.Series) -> pd.Series:
    """Ratio of annualized 5d-RV to annualized 21d-RV — intra-month annualized vol shift."""
    r = _log_returns(close)
    a = r.rolling(WDAYS, min_periods=2).std() * np.sqrt(float(YDAYS))
    b = r.rolling(MDAYS, min_periods=WDAYS).std() * np.sqrt(float(YDAYS))
    return _safe_div(a, b)


def f35_rvre_109_min_to_max_rv21_in_252d(close: pd.Series) -> pd.Series:
    """min(21d-RV)/max(21d-RV) in trailing 252d — vol-range compression ratio."""
    r = _log_returns(close)
    rv21 = r.rolling(MDAYS, min_periods=WDAYS).std()
    mn = rv21.rolling(YDAYS, min_periods=QDAYS).min()
    mx = rv21.rolling(YDAYS, min_periods=QDAYS).max()
    return _safe_div(mn, mx)


def f35_rvre_110_rv21_over_median_rv21_in_504d(close: pd.Series) -> pd.Series:
    """Current 21d-RV / median(21d-RV) over trailing 504d — vol level vs typical."""
    r = _log_returns(close)
    rv21 = r.rolling(MDAYS, min_periods=WDAYS).std()
    med = rv21.rolling(DDAYS_2Y, min_periods=YDAYS).median()
    return _safe_div(rv21, med)


def f35_rvre_111_rv63_over_mean_rv63_in_1260d(close: pd.Series) -> pd.Series:
    """Current 63d-RV / mean(63d-RV) over trailing 1260d — 5y-baseline normalized vol."""
    r = _log_returns(close)
    rv63 = r.rolling(QDAYS, min_periods=MDAYS).std()
    m = rv63.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    return _safe_div(rv63, m)


# ============================================================
# Bucket N — Volume-weighted vol 112-117
# ============================================================

def _weighted_var(rsq: pd.Series, weights: pd.Series, window: int, min_periods: int) -> pd.Series:
    """Rolling weighted variance: sum(w*r^2)/sum(w)."""
    num = (weights * rsq).rolling(window, min_periods=min_periods).sum()
    den = weights.rolling(window, min_periods=min_periods).sum()
    return _safe_div(num, den)


def f35_rvre_112_volume_weighted_rvar_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted realized variance over 21d (heavy-volume bars dominate)."""
    r = _log_returns(close)
    rsq = r ** 2
    return _weighted_var(rsq, volume, MDAYS, WDAYS)


def f35_rvre_113_volume_weighted_rvar_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted realized variance over 63d."""
    r = _log_returns(close)
    rsq = r ** 2
    return _weighted_var(rsq, volume, QDAYS, MDAYS)


def f35_rvre_114_dollar_volume_weighted_rvar_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar-volume-weighted realized variance over 63d (weight = close * volume)."""
    r = _log_returns(close)
    rsq = r ** 2
    dv = close * volume
    return _weighted_var(rsq, dv, QDAYS, MDAYS)


def f35_rvre_115_ratio_vwrv_to_eqrv_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio: volume-weighted variance to equal-weighted variance over 21d.
    >1 ⇒ vol concentrated on high-volume days (driven by participation)."""
    r = _log_returns(close)
    rsq = r ** 2
    vw = _weighted_var(rsq, volume, MDAYS, WDAYS)
    eq = rsq.rolling(MDAYS, min_periods=WDAYS).mean()
    return _safe_div(vw, eq)


def f35_rvre_116_ratio_vwrv_to_eqrv_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of volume-weighted to equal-weighted variance over 252d."""
    r = _log_returns(close)
    rsq = r ** 2
    vw = _weighted_var(rsq, volume, YDAYS, QDAYS)
    eq = rsq.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(vw, eq)


def f35_rvre_117_dollar_volume_weighted_rvar_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar-volume-weighted realized variance over 21d."""
    r = _log_returns(close)
    rsq = r ** 2
    dv = close * volume
    return _weighted_var(rsq, dv, MDAYS, WDAYS)


# ============================================================
# Bucket O — Multi-frequency vol via non-overlapping returns 118-123
# Different sampling frequency = different hypothesis
# ============================================================

def _nonoverlap_kday_returns(close: pd.Series, k: int) -> pd.Series:
    """k-day log returns sampled non-overlapping (anchored by absolute bar index modulo k)."""
    lr = _safe_log(close)
    # Build k-day non-overlap return for every bar t as: log(close_t) - log(close_{t-k}) BUT only
    # for bars whose absolute index is a multiple of k (and forward-fill NaNs to bars in between).
    diff_k = lr.diff(k)
    pos = np.arange(len(close))
    mask = (pos % k == 0)
    out = diff_k.where(mask, np.nan)
    return out


def f35_rvre_118_sigma_1d_log_returns_252d(close: pd.Series) -> pd.Series:
    """Std of 1d log returns over 252d — baseline daily-frequency vol."""
    r = _log_returns(close)
    return r.rolling(YDAYS, min_periods=QDAYS).std()


def f35_rvre_119_sigma_nonoverlap_5d_returns_252d(close: pd.Series) -> pd.Series:
    """Std of non-overlapping 5d log returns sampled over a trailing 252d window."""
    r5 = _nonoverlap_kday_returns(close, 5)
    def _std_nonan(w):
        v = w[~np.isnan(w)]
        if v.size < 5:
            return np.nan
        return float(v.std(ddof=1))
    return r5.rolling(YDAYS, min_periods=QDAYS).apply(_std_nonan, raw=True)


def f35_rvre_120_sigma_nonoverlap_21d_returns_504d(close: pd.Series) -> pd.Series:
    """Std of non-overlapping 21d log returns sampled over trailing 504d."""
    r21 = _nonoverlap_kday_returns(close, 21)
    def _std_nonan(w):
        v = w[~np.isnan(w)]
        if v.size < 4:
            return np.nan
        return float(v.std(ddof=1))
    return r21.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_std_nonan, raw=True)


def f35_rvre_121_sigma_nonoverlap_5d_returns_1260d(close: pd.Series) -> pd.Series:
    """Std of non-overlapping 5d log returns sampled over trailing 1260d (5y)."""
    r5 = _nonoverlap_kday_returns(close, 5)
    def _std_nonan(w):
        v = w[~np.isnan(w)]
        if v.size < 10:
            return np.nan
        return float(v.std(ddof=1))
    return r5.rolling(DDAYS_5Y, min_periods=YDAYS).apply(_std_nonan, raw=True)


def f35_rvre_122_sigma_nonoverlap_21d_returns_1260d(close: pd.Series) -> pd.Series:
    """Std of non-overlapping 21d log returns sampled over trailing 1260d."""
    r21 = _nonoverlap_kday_returns(close, 21)
    def _std_nonan(w):
        v = w[~np.isnan(w)]
        if v.size < 8:
            return np.nan
        return float(v.std(ddof=1))
    return r21.rolling(DDAYS_5Y, min_periods=YDAYS).apply(_std_nonan, raw=True)


def f35_rvre_123_variance_ratio_nonoverlap_5d_vs_1d_252d(close: pd.Series) -> pd.Series:
    """Variance ratio: var(non-overlap 5d returns) / (5 * var(1d returns)) over 252d.
    1 under random-walk; >1 ⇒ trending; <1 ⇒ mean-reverting."""
    r1 = _log_returns(close)
    r5 = _nonoverlap_kday_returns(close, 5)
    def _vr(w_combined):
        # w_combined: not used — we instead compute via two passes outside via concat
        return np.nan
    # implement with concat — apply needs to see both series jointly. Use rolling on a frame.
    df = pd.concat([r1.rename("r1"), r5.rename("r5")], axis=1)
    out = np.full(len(close), np.nan)
    arr = df.values
    win = YDAYS
    mp = QDAYS
    for i in range(len(close)):
        lo = max(0, i - win + 1)
        sub = arr[lo:i + 1]
        if sub.shape[0] < mp:
            continue
        v1 = sub[:, 0]
        v1 = v1[~np.isnan(v1)]
        v5 = sub[:, 1]
        v5 = v5[~np.isnan(v5)]
        if v1.size < 30 or v5.size < 5:
            continue
        var1 = v1.var(ddof=1)
        var5 = v5.var(ddof=1)
        if var1 <= 0:
            continue
        out[i] = float(var5 / (5.0 * var1))
    return pd.Series(out, index=close.index)


# ============================================================
# Bucket P — Vol-distribution moments other than mean/std 124-129, 148-150
# ============================================================

def f35_rvre_124_median_rv21_in_252d(close: pd.Series) -> pd.Series:
    """Median of 21d-RV across trailing 252d — typical monthly vol level."""
    r = _log_returns(close)
    rv21 = r.rolling(MDAYS, min_periods=WDAYS).std()
    return rv21.rolling(YDAYS, min_periods=QDAYS).median()


def f35_rvre_125_max_rv21_in_252d(close: pd.Series) -> pd.Series:
    """Max of 21d-RV across trailing 252d — peak monthly vol attained."""
    r = _log_returns(close)
    rv21 = r.rolling(MDAYS, min_periods=WDAYS).std()
    return rv21.rolling(YDAYS, min_periods=QDAYS).max()


def f35_rvre_126_min_rv21_in_252d(close: pd.Series) -> pd.Series:
    """Min of 21d-RV across trailing 252d — quietest monthly vol attained."""
    r = _log_returns(close)
    rv21 = r.rolling(MDAYS, min_periods=WDAYS).std()
    return rv21.rolling(YDAYS, min_periods=QDAYS).min()


def f35_rvre_127_median_rv63_in_504d(close: pd.Series) -> pd.Series:
    """Median of 63d-RV across trailing 504d — typical quarterly vol level."""
    r = _log_returns(close)
    rv63 = r.rolling(QDAYS, min_periods=MDAYS).std()
    return rv63.rolling(DDAYS_2Y, min_periods=YDAYS).median()


def f35_rvre_128_max_rv63_in_504d(close: pd.Series) -> pd.Series:
    """Max of 63d-RV across trailing 504d — biennial peak quarterly vol."""
    r = _log_returns(close)
    rv63 = r.rolling(QDAYS, min_periods=MDAYS).std()
    return rv63.rolling(DDAYS_2Y, min_periods=YDAYS).max()


def f35_rvre_129_min_rv63_in_504d(close: pd.Series) -> pd.Series:
    """Min of 63d-RV across trailing 504d — biennial trough quarterly vol."""
    r = _log_returns(close)
    rv63 = r.rolling(QDAYS, min_periods=MDAYS).std()
    return rv63.rolling(DDAYS_2Y, min_periods=YDAYS).min()


# ============================================================
# Bucket Q — Vol clustering / run length 130-137
# ============================================================

def f35_rvre_130_consecutive_streak_abs_r_above_p80_252d(close: pd.Series) -> pd.Series:
    """Current consecutive-bar streak where |r| > p80(|r|, 252d)."""
    r = _log_returns(close).abs()
    p80 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.80)
    in_state = (r > p80).astype(float).values
    n = len(in_state)
    out = np.full(n, np.nan, dtype=float)
    streak = 0
    for i in range(n):
        v = in_state[i]
        if np.isnan(v):
            streak = 0
            out[i] = np.nan
        else:
            streak = streak + 1 if v > 0 else 0
            out[i] = float(streak)
    return pd.Series(out, index=close.index)


def f35_rvre_131_longest_run_abs_r_above_p80_in_252d(close: pd.Series) -> pd.Series:
    """Longest run-length of consecutive bars with |r| > p80(|r|, 252d) inside 252d window."""
    r = _log_returns(close).abs()
    p80 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.80)
    flag = (r > p80).astype(float)
    def _longest(w):
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        best = 0
        cur = 0
        for x in v:
            if x > 0:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return float(best)
    return flag.rolling(YDAYS, min_periods=QDAYS).apply(_longest, raw=True)


def f35_rvre_132_serial_corr_rsq_lag1_504d(close: pd.Series) -> pd.Series:
    """Serial correlation lag-1 of squared log returns over 504d (long-window vol clustering)."""
    r = _log_returns(close)
    rsq = r ** 2
    a = rsq
    b = rsq.shift(1)
    ma = a.rolling(DDAYS_2Y, min_periods=YDAYS).mean()
    mb = b.rolling(DDAYS_2Y, min_periods=YDAYS).mean()
    sa = a.rolling(DDAYS_2Y, min_periods=YDAYS).std()
    sb = b.rolling(DDAYS_2Y, min_periods=YDAYS).std()
    cov = ((a - ma) * (b - mb)).rolling(DDAYS_2Y, min_periods=YDAYS).mean()
    return _safe_div(cov, sa * sb)


def f35_rvre_133_serial_corr_rsq_lag5_504d(close: pd.Series) -> pd.Series:
    """Serial correlation lag-5 of squared log returns over 504d — weekly vol echo (long window)."""
    r = _log_returns(close)
    rsq = r ** 2
    a = rsq
    b = rsq.shift(5)
    ma = a.rolling(DDAYS_2Y, min_periods=YDAYS).mean()
    mb = b.rolling(DDAYS_2Y, min_periods=YDAYS).mean()
    sa = a.rolling(DDAYS_2Y, min_periods=YDAYS).std()
    sb = b.rolling(DDAYS_2Y, min_periods=YDAYS).std()
    cov = ((a - ma) * (b - mb)).rolling(DDAYS_2Y, min_periods=YDAYS).mean()
    return _safe_div(cov, sa * sb)


def f35_rvre_134_count_abs_r_above_p80_in_21d(close: pd.Series) -> pd.Series:
    """Count of bars in trailing 21d where |r| > p80(|r|, 252d)."""
    r = _log_returns(close).abs()
    p80 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.80)
    flag = (r > p80).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum()


def f35_rvre_135_count_abs_r_above_p80_in_63d(close: pd.Series) -> pd.Series:
    """Count of bars in trailing 63d where |r| > p80(|r|, 252d)."""
    r = _log_returns(close).abs()
    p80 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.80)
    flag = (r > p80).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f35_rvre_136_run_length_entropy_vol_regime_252d(close: pd.Series) -> pd.Series:
    """Shannon entropy (base 2) of run-lengths of the high-vol state (|r|>p80) over 252d."""
    r = _log_returns(close).abs()
    p80 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.80)
    flag = (r > p80).astype(float)
    def _rl_ent(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        runs = []
        cur = 0
        for x in v:
            if x > 0:
                cur += 1
            else:
                if cur > 0:
                    runs.append(cur)
                    cur = 0
        if cur > 0:
            runs.append(cur)
        if len(runs) < 2:
            return np.nan
        arr = np.array(runs, dtype=float)
        _, cnts = np.unique(arr, return_counts=True)
        p = cnts / cnts.sum()
        return float(-(p * np.log2(p)).sum())
    return flag.rolling(YDAYS, min_periods=QDAYS).apply(_rl_ent, raw=True)


def f35_rvre_137_fraction_in_high_vol_clusters_252d(close: pd.Series) -> pd.Series:
    """Fraction of bars in trailing 252d that belong to a high-vol cluster (run of length>=3 of |r|>p80)."""
    r = _log_returns(close).abs()
    p80 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.80)
    flag = (r > p80).astype(float)
    def _frac(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        total_in = 0
        cur = 0
        for x in v:
            if x > 0:
                cur += 1
            else:
                if cur >= 3:
                    total_in += cur
                cur = 0
        if cur >= 3:
            total_in += cur
        return float(total_in) / float(v.size)
    return flag.rolling(YDAYS, min_periods=QDAYS).apply(_frac, raw=True)


# ============================================================
# Bucket R — Cumulative variance / cumulative absolute returns 138-142
# ============================================================

def f35_rvre_138_cumulative_variance_252d(close: pd.Series) -> pd.Series:
    """Sum of squared log returns over trailing 252d — cumulative variance (annual)."""
    r = _log_returns(close)
    return (r ** 2).rolling(YDAYS, min_periods=QDAYS).sum()


def f35_rvre_139_cumulative_abs_return_21d(close: pd.Series) -> pd.Series:
    """Cumulative sum of |log returns| over trailing 21d — monthly cumulative travel."""
    r = _log_returns(close).abs()
    return r.rolling(MDAYS, min_periods=WDAYS).sum()


def f35_rvre_140_cumulative_variance_1260d(close: pd.Series) -> pd.Series:
    """Sum of squared log returns over trailing 1260d (5y) — long-horizon cumulative variance."""
    r = _log_returns(close)
    return (r ** 2).rolling(DDAYS_5Y, min_periods=YDAYS).sum()


def f35_rvre_141_ratio_cum_variance_252_to_1260(close: pd.Series) -> pd.Series:
    """Cumulative variance 252d / cumulative variance 1260d — recent share of 5y total variance."""
    r = _log_returns(close)
    v252 = (r ** 2).rolling(YDAYS, min_periods=QDAYS).sum()
    v1260 = (r ** 2).rolling(DDAYS_5Y, min_periods=YDAYS).sum()
    return _safe_div(v252, v1260)


def f35_rvre_142_cumulative_abs_return_504d(close: pd.Series) -> pd.Series:
    """Cumulative sum of |log returns| over trailing 504d — biennial cumulative travel."""
    r = _log_returns(close).abs()
    return r.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


# ============================================================
# Bucket S — Overnight + intraday RV split 143-147 (uses open and close)
# ============================================================

def f35_rvre_143_overnight_rv_21d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Overnight RV: std of log(open_t / close_{t-1}) over trailing 21d."""
    on = _safe_log(open_) - _safe_log(close.shift(1))
    return on.rolling(MDAYS, min_periods=WDAYS).std()


def f35_rvre_144_intraday_rv_21d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Intraday RV: std of log(close_t / open_t) over trailing 21d."""
    intra = _safe_log(close) - _safe_log(open_)
    return intra.rolling(MDAYS, min_periods=WDAYS).std()


def f35_rvre_145_overnight_rv_252d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Overnight RV: std of log(open/prev-close) over trailing 252d — annual overnight regime."""
    on = _safe_log(open_) - _safe_log(close.shift(1))
    return on.rolling(YDAYS, min_periods=QDAYS).std()


def f35_rvre_146_intraday_rv_252d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Intraday RV: std of log(close/open) over trailing 252d — annual intraday regime."""
    intra = _safe_log(close) - _safe_log(open_)
    return intra.rolling(YDAYS, min_periods=QDAYS).std()


def f35_rvre_147_ratio_overnight_to_intraday_rv_63d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of overnight-RV to intraday-RV over 63d — session-share of vol."""
    on = _safe_log(open_) - _safe_log(close.shift(1))
    intra = _safe_log(close) - _safe_log(open_)
    on_rv = on.rolling(QDAYS, min_periods=MDAYS).std()
    in_rv = intra.rolling(QDAYS, min_periods=MDAYS).std()
    return _safe_div(on_rv, in_rv)


# ============================================================
# Bucket P (continued) — three more vol-moment hypotheses 148-150
# ============================================================

def f35_rvre_148_max_rv5_in_63d(close: pd.Series) -> pd.Series:
    """Max of 5d-RV across trailing 63d — peak weekly vol within quarter."""
    r = _log_returns(close)
    rv5 = r.rolling(WDAYS, min_periods=2).std()
    return rv5.rolling(QDAYS, min_periods=MDAYS).max()


def f35_rvre_149_min_rv5_in_63d(close: pd.Series) -> pd.Series:
    """Min of 5d-RV across trailing 63d — quietest weekly vol within quarter."""
    r = _log_returns(close)
    rv5 = r.rolling(WDAYS, min_periods=2).std()
    return rv5.rolling(QDAYS, min_periods=MDAYS).min()


def f35_rvre_150_median_rv5_in_252d(close: pd.Series) -> pd.Series:
    """Median of 5d-RV across trailing 252d — typical weekly vol annually."""
    r = _log_returns(close)
    rv5 = r.rolling(WDAYS, min_periods=2).std()
    return rv5.rolling(YDAYS, min_periods=QDAYS).median()


# ============================================================
#                         REGISTRY 076-150
# ============================================================



def f35_rvre_076_mean_abs_return_21d_d2(close):
    return f35_rvre_076_mean_abs_return_21d(close).diff().diff()


def f35_rvre_077_mean_abs_return_252d_d2(close):
    return f35_rvre_077_mean_abs_return_252d(close).diff().diff()


def f35_rvre_078_rms_return_21d_d2(close):
    return f35_rvre_078_rms_return_21d(close).diff().diff()


def f35_rvre_079_rms_return_252d_d2(close):
    return f35_rvre_079_rms_return_252d(close).diff().diff()


def f35_rvre_080_geom_mean_abs_return_63d_d2(close):
    return f35_rvre_080_geom_mean_abs_return_63d(close).diff().diff()


def f35_rvre_081_sum_abs_return_252d_d2(close):
    return f35_rvre_081_sum_abs_return_252d(close).diff().diff()


def f35_rvre_082_term_struct_slope_5_21_63_252_d2(close):
    return f35_rvre_082_term_struct_slope_5_21_63_252(close).diff().diff()


def f35_rvre_083_term_struct_slope_21_63_252_504_d2(close):
    return f35_rvre_083_term_struct_slope_21_63_252_504(close).diff().diff()


def f35_rvre_084_term_struct_slope_5_21_63_d2(close):
    return f35_rvre_084_term_struct_slope_5_21_63(close).diff().diff()


def f35_rvre_085_term_struct_curvature_5_21_63_252_d2(close):
    return f35_rvre_085_term_struct_curvature_5_21_63_252(close).diff().diff()


def f35_rvre_086_term_struct_r2_5_21_63_252_d2(close):
    return f35_rvre_086_term_struct_r2_5_21_63_252(close).diff().diff()


def f35_rvre_087_term_struct_intercept_5_21_63_252_d2(close):
    return f35_rvre_087_term_struct_intercept_5_21_63_252(close).diff().diff()


def f35_rvre_088_entropy_abs_r_252d_d2(close):
    return f35_rvre_088_entropy_abs_r_252d(close).diff().diff()


def f35_rvre_089_entropy_abs_r_504d_d2(close):
    return f35_rvre_089_entropy_abs_r_504d(close).diff().diff()


def f35_rvre_090_gini_abs_r_252d_d2(close):
    return f35_rvre_090_gini_abs_r_252d(close).diff().diff()


def f35_rvre_091_dispersion_ratio_rv21_in_252d_d2(close):
    return f35_rvre_091_dispersion_ratio_rv21_in_252d(close).diff().diff()


def f35_rvre_092_subwindow_vol_dispersion_252d_d2(close):
    return f35_rvre_092_subwindow_vol_dispersion_252d(close).diff().diff()


def f35_rvre_093_subwindow_vol_dispersion_504d_d2(close):
    return f35_rvre_093_subwindow_vol_dispersion_504d(close).diff().diff()


def f35_rvre_094_cusum_rsq_max_abs_252d_d2(close):
    return f35_rvre_094_cusum_rsq_max_abs_252d(close).diff().diff()


def f35_rvre_095_cusum_abs_r_max_abs_504d_d2(close):
    return f35_rvre_095_cusum_abs_r_max_abs_504d(close).diff().diff()


def f35_rvre_096_jump_ratio_max_to_median_abs_r_21d_d2(close):
    return f35_rvre_096_jump_ratio_max_to_median_abs_r_21d(close).diff().diff()


def f35_rvre_097_rv_ratio_test_21_vs_252_d2(close):
    return f35_rvre_097_rv_ratio_test_21_vs_252(close).diff().diff()


def f35_rvre_098_welch_rv_ratio_63_vs_504_d2(close):
    return f35_rvre_098_welch_rv_ratio_63_vs_504(close).diff().diff()


def f35_rvre_099_max_diff_rv21_vs_rv252_over_21d_d2(close):
    return f35_rvre_099_max_diff_rv21_vs_rv252_over_21d(close).diff().diff()


def f35_rvre_100_max_zscore_abs_r_in_21d_d2(close):
    return f35_rvre_100_max_zscore_abs_r_in_21d(close).diff().diff()


def f35_rvre_101_fraction_bars_above_3mad_in_63d_d2(close):
    return f35_rvre_101_fraction_bars_above_3mad_in_63d(close).diff().diff()


def f35_rvre_102_largest_jump_rv21_change_in_252d_d2(close):
    return f35_rvre_102_largest_jump_rv21_change_in_252d(close).diff().diff()


def f35_rvre_103_count_vol_jumps_abs_r_above_4sigma_in_252d_d2(close):
    return f35_rvre_103_count_vol_jumps_abs_r_above_4sigma_in_252d(close).diff().diff()


def f35_rvre_104_ann_rv_21d_d2(close):
    return f35_rvre_104_ann_rv_21d(close).diff().diff()


def f35_rvre_105_ann_rv_63d_d2(close):
    return f35_rvre_105_ann_rv_63d(close).diff().diff()


def f35_rvre_106_ann_rv_252d_d2(close):
    return f35_rvre_106_ann_rv_252d(close).diff().diff()


def f35_rvre_107_ratio_ann_rv21_to_ann_rv252_d2(close):
    return f35_rvre_107_ratio_ann_rv21_to_ann_rv252(close).diff().diff()


def f35_rvre_108_ratio_ann_rv5_to_ann_rv21_d2(close):
    return f35_rvre_108_ratio_ann_rv5_to_ann_rv21(close).diff().diff()


def f35_rvre_109_min_to_max_rv21_in_252d_d2(close):
    return f35_rvre_109_min_to_max_rv21_in_252d(close).diff().diff()


def f35_rvre_110_rv21_over_median_rv21_in_504d_d2(close):
    return f35_rvre_110_rv21_over_median_rv21_in_504d(close).diff().diff()


def f35_rvre_111_rv63_over_mean_rv63_in_1260d_d2(close):
    return f35_rvre_111_rv63_over_mean_rv63_in_1260d(close).diff().diff()


def f35_rvre_112_volume_weighted_rvar_21d_d2(close, volume):
    return f35_rvre_112_volume_weighted_rvar_21d(close, volume).diff().diff()


def f35_rvre_113_volume_weighted_rvar_63d_d2(close, volume):
    return f35_rvre_113_volume_weighted_rvar_63d(close, volume).diff().diff()


def f35_rvre_114_dollar_volume_weighted_rvar_63d_d2(close, volume):
    return f35_rvre_114_dollar_volume_weighted_rvar_63d(close, volume).diff().diff()


def f35_rvre_115_ratio_vwrv_to_eqrv_21d_d2(close, volume):
    return f35_rvre_115_ratio_vwrv_to_eqrv_21d(close, volume).diff().diff()


def f35_rvre_116_ratio_vwrv_to_eqrv_252d_d2(close, volume):
    return f35_rvre_116_ratio_vwrv_to_eqrv_252d(close, volume).diff().diff()


def f35_rvre_117_dollar_volume_weighted_rvar_21d_d2(close, volume):
    return f35_rvre_117_dollar_volume_weighted_rvar_21d(close, volume).diff().diff()


def f35_rvre_118_sigma_1d_log_returns_252d_d2(close):
    return f35_rvre_118_sigma_1d_log_returns_252d(close).diff().diff()


def f35_rvre_119_sigma_nonoverlap_5d_returns_252d_d2(close):
    return f35_rvre_119_sigma_nonoverlap_5d_returns_252d(close).diff().diff()


def f35_rvre_120_sigma_nonoverlap_21d_returns_504d_d2(close):
    return f35_rvre_120_sigma_nonoverlap_21d_returns_504d(close).diff().diff()


def f35_rvre_121_sigma_nonoverlap_5d_returns_1260d_d2(close):
    return f35_rvre_121_sigma_nonoverlap_5d_returns_1260d(close).diff().diff()


def f35_rvre_122_sigma_nonoverlap_21d_returns_1260d_d2(close):
    return f35_rvre_122_sigma_nonoverlap_21d_returns_1260d(close).diff().diff()


def f35_rvre_123_variance_ratio_nonoverlap_5d_vs_1d_252d_d2(close):
    return f35_rvre_123_variance_ratio_nonoverlap_5d_vs_1d_252d(close).diff().diff()


def f35_rvre_124_median_rv21_in_252d_d2(close):
    return f35_rvre_124_median_rv21_in_252d(close).diff().diff()


def f35_rvre_125_max_rv21_in_252d_d2(close):
    return f35_rvre_125_max_rv21_in_252d(close).diff().diff()


def f35_rvre_126_min_rv21_in_252d_d2(close):
    return f35_rvre_126_min_rv21_in_252d(close).diff().diff()


def f35_rvre_127_median_rv63_in_504d_d2(close):
    return f35_rvre_127_median_rv63_in_504d(close).diff().diff()


def f35_rvre_128_max_rv63_in_504d_d2(close):
    return f35_rvre_128_max_rv63_in_504d(close).diff().diff()


def f35_rvre_129_min_rv63_in_504d_d2(close):
    return f35_rvre_129_min_rv63_in_504d(close).diff().diff()


def f35_rvre_130_consecutive_streak_abs_r_above_p80_252d_d2(close):
    return f35_rvre_130_consecutive_streak_abs_r_above_p80_252d(close).diff().diff()


def f35_rvre_131_longest_run_abs_r_above_p80_in_252d_d2(close):
    return f35_rvre_131_longest_run_abs_r_above_p80_in_252d(close).diff().diff()


def f35_rvre_132_serial_corr_rsq_lag1_504d_d2(close):
    return f35_rvre_132_serial_corr_rsq_lag1_504d(close).diff().diff()


def f35_rvre_133_serial_corr_rsq_lag5_504d_d2(close):
    return f35_rvre_133_serial_corr_rsq_lag5_504d(close).diff().diff()


def f35_rvre_134_count_abs_r_above_p80_in_21d_d2(close):
    return f35_rvre_134_count_abs_r_above_p80_in_21d(close).diff().diff()


def f35_rvre_135_count_abs_r_above_p80_in_63d_d2(close):
    return f35_rvre_135_count_abs_r_above_p80_in_63d(close).diff().diff()


def f35_rvre_136_run_length_entropy_vol_regime_252d_d2(close):
    return f35_rvre_136_run_length_entropy_vol_regime_252d(close).diff().diff()


def f35_rvre_137_fraction_in_high_vol_clusters_252d_d2(close):
    return f35_rvre_137_fraction_in_high_vol_clusters_252d(close).diff().diff()


def f35_rvre_138_cumulative_variance_252d_d2(close):
    return f35_rvre_138_cumulative_variance_252d(close).diff().diff()


def f35_rvre_139_cumulative_abs_return_21d_d2(close):
    return f35_rvre_139_cumulative_abs_return_21d(close).diff().diff()


def f35_rvre_140_cumulative_variance_1260d_d2(close):
    return f35_rvre_140_cumulative_variance_1260d(close).diff().diff()


def f35_rvre_141_ratio_cum_variance_252_to_1260_d2(close):
    return f35_rvre_141_ratio_cum_variance_252_to_1260(close).diff().diff()


def f35_rvre_142_cumulative_abs_return_504d_d2(close):
    return f35_rvre_142_cumulative_abs_return_504d(close).diff().diff()


def f35_rvre_143_overnight_rv_21d_d2(open_, close):
    return f35_rvre_143_overnight_rv_21d(open_, close).diff().diff()


def f35_rvre_144_intraday_rv_21d_d2(open_, close):
    return f35_rvre_144_intraday_rv_21d(open_, close).diff().diff()


def f35_rvre_145_overnight_rv_252d_d2(open_, close):
    return f35_rvre_145_overnight_rv_252d(open_, close).diff().diff()


def f35_rvre_146_intraday_rv_252d_d2(open_, close):
    return f35_rvre_146_intraday_rv_252d(open_, close).diff().diff()


def f35_rvre_147_ratio_overnight_to_intraday_rv_63d_d2(open_, close):
    return f35_rvre_147_ratio_overnight_to_intraday_rv_63d(open_, close).diff().diff()


def f35_rvre_148_max_rv5_in_63d_d2(close):
    return f35_rvre_148_max_rv5_in_63d(close).diff().diff()


def f35_rvre_149_min_rv5_in_63d_d2(close):
    return f35_rvre_149_min_rv5_in_63d(close).diff().diff()


def f35_rvre_150_median_rv5_in_252d_d2(close):
    return f35_rvre_150_median_rv5_in_252d(close).diff().diff()


REALIZED_VOLATILITY_REGIME_D2_REGISTRY_076_150 = {
    "f35_rvre_076_mean_abs_return_21d_d2": {"inputs": ["close"], "func": f35_rvre_076_mean_abs_return_21d_d2},
    "f35_rvre_077_mean_abs_return_252d_d2": {"inputs": ["close"], "func": f35_rvre_077_mean_abs_return_252d_d2},
    "f35_rvre_078_rms_return_21d_d2": {"inputs": ["close"], "func": f35_rvre_078_rms_return_21d_d2},
    "f35_rvre_079_rms_return_252d_d2": {"inputs": ["close"], "func": f35_rvre_079_rms_return_252d_d2},
    "f35_rvre_080_geom_mean_abs_return_63d_d2": {"inputs": ["close"], "func": f35_rvre_080_geom_mean_abs_return_63d_d2},
    "f35_rvre_081_sum_abs_return_252d_d2": {"inputs": ["close"], "func": f35_rvre_081_sum_abs_return_252d_d2},
    "f35_rvre_082_term_struct_slope_5_21_63_252_d2": {"inputs": ["close"], "func": f35_rvre_082_term_struct_slope_5_21_63_252_d2},
    "f35_rvre_083_term_struct_slope_21_63_252_504_d2": {"inputs": ["close"], "func": f35_rvre_083_term_struct_slope_21_63_252_504_d2},
    "f35_rvre_084_term_struct_slope_5_21_63_d2": {"inputs": ["close"], "func": f35_rvre_084_term_struct_slope_5_21_63_d2},
    "f35_rvre_085_term_struct_curvature_5_21_63_252_d2": {"inputs": ["close"], "func": f35_rvre_085_term_struct_curvature_5_21_63_252_d2},
    "f35_rvre_086_term_struct_r2_5_21_63_252_d2": {"inputs": ["close"], "func": f35_rvre_086_term_struct_r2_5_21_63_252_d2},
    "f35_rvre_087_term_struct_intercept_5_21_63_252_d2": {"inputs": ["close"], "func": f35_rvre_087_term_struct_intercept_5_21_63_252_d2},
    "f35_rvre_088_entropy_abs_r_252d_d2": {"inputs": ["close"], "func": f35_rvre_088_entropy_abs_r_252d_d2},
    "f35_rvre_089_entropy_abs_r_504d_d2": {"inputs": ["close"], "func": f35_rvre_089_entropy_abs_r_504d_d2},
    "f35_rvre_090_gini_abs_r_252d_d2": {"inputs": ["close"], "func": f35_rvre_090_gini_abs_r_252d_d2},
    "f35_rvre_091_dispersion_ratio_rv21_in_252d_d2": {"inputs": ["close"], "func": f35_rvre_091_dispersion_ratio_rv21_in_252d_d2},
    "f35_rvre_092_subwindow_vol_dispersion_252d_d2": {"inputs": ["close"], "func": f35_rvre_092_subwindow_vol_dispersion_252d_d2},
    "f35_rvre_093_subwindow_vol_dispersion_504d_d2": {"inputs": ["close"], "func": f35_rvre_093_subwindow_vol_dispersion_504d_d2},
    "f35_rvre_094_cusum_rsq_max_abs_252d_d2": {"inputs": ["close"], "func": f35_rvre_094_cusum_rsq_max_abs_252d_d2},
    "f35_rvre_095_cusum_abs_r_max_abs_504d_d2": {"inputs": ["close"], "func": f35_rvre_095_cusum_abs_r_max_abs_504d_d2},
    "f35_rvre_096_jump_ratio_max_to_median_abs_r_21d_d2": {"inputs": ["close"], "func": f35_rvre_096_jump_ratio_max_to_median_abs_r_21d_d2},
    "f35_rvre_097_rv_ratio_test_21_vs_252_d2": {"inputs": ["close"], "func": f35_rvre_097_rv_ratio_test_21_vs_252_d2},
    "f35_rvre_098_welch_rv_ratio_63_vs_504_d2": {"inputs": ["close"], "func": f35_rvre_098_welch_rv_ratio_63_vs_504_d2},
    "f35_rvre_099_max_diff_rv21_vs_rv252_over_21d_d2": {"inputs": ["close"], "func": f35_rvre_099_max_diff_rv21_vs_rv252_over_21d_d2},
    "f35_rvre_100_max_zscore_abs_r_in_21d_d2": {"inputs": ["close"], "func": f35_rvre_100_max_zscore_abs_r_in_21d_d2},
    "f35_rvre_101_fraction_bars_above_3mad_in_63d_d2": {"inputs": ["close"], "func": f35_rvre_101_fraction_bars_above_3mad_in_63d_d2},
    "f35_rvre_102_largest_jump_rv21_change_in_252d_d2": {"inputs": ["close"], "func": f35_rvre_102_largest_jump_rv21_change_in_252d_d2},
    "f35_rvre_103_count_vol_jumps_abs_r_above_4sigma_in_252d_d2": {"inputs": ["close"], "func": f35_rvre_103_count_vol_jumps_abs_r_above_4sigma_in_252d_d2},
    "f35_rvre_104_ann_rv_21d_d2": {"inputs": ["close"], "func": f35_rvre_104_ann_rv_21d_d2},
    "f35_rvre_105_ann_rv_63d_d2": {"inputs": ["close"], "func": f35_rvre_105_ann_rv_63d_d2},
    "f35_rvre_106_ann_rv_252d_d2": {"inputs": ["close"], "func": f35_rvre_106_ann_rv_252d_d2},
    "f35_rvre_107_ratio_ann_rv21_to_ann_rv252_d2": {"inputs": ["close"], "func": f35_rvre_107_ratio_ann_rv21_to_ann_rv252_d2},
    "f35_rvre_108_ratio_ann_rv5_to_ann_rv21_d2": {"inputs": ["close"], "func": f35_rvre_108_ratio_ann_rv5_to_ann_rv21_d2},
    "f35_rvre_109_min_to_max_rv21_in_252d_d2": {"inputs": ["close"], "func": f35_rvre_109_min_to_max_rv21_in_252d_d2},
    "f35_rvre_110_rv21_over_median_rv21_in_504d_d2": {"inputs": ["close"], "func": f35_rvre_110_rv21_over_median_rv21_in_504d_d2},
    "f35_rvre_111_rv63_over_mean_rv63_in_1260d_d2": {"inputs": ["close"], "func": f35_rvre_111_rv63_over_mean_rv63_in_1260d_d2},
    "f35_rvre_112_volume_weighted_rvar_21d_d2": {"inputs": ["close", "volume"], "func": f35_rvre_112_volume_weighted_rvar_21d_d2},
    "f35_rvre_113_volume_weighted_rvar_63d_d2": {"inputs": ["close", "volume"], "func": f35_rvre_113_volume_weighted_rvar_63d_d2},
    "f35_rvre_114_dollar_volume_weighted_rvar_63d_d2": {"inputs": ["close", "volume"], "func": f35_rvre_114_dollar_volume_weighted_rvar_63d_d2},
    "f35_rvre_115_ratio_vwrv_to_eqrv_21d_d2": {"inputs": ["close", "volume"], "func": f35_rvre_115_ratio_vwrv_to_eqrv_21d_d2},
    "f35_rvre_116_ratio_vwrv_to_eqrv_252d_d2": {"inputs": ["close", "volume"], "func": f35_rvre_116_ratio_vwrv_to_eqrv_252d_d2},
    "f35_rvre_117_dollar_volume_weighted_rvar_21d_d2": {"inputs": ["close", "volume"], "func": f35_rvre_117_dollar_volume_weighted_rvar_21d_d2},
    "f35_rvre_118_sigma_1d_log_returns_252d_d2": {"inputs": ["close"], "func": f35_rvre_118_sigma_1d_log_returns_252d_d2},
    "f35_rvre_119_sigma_nonoverlap_5d_returns_252d_d2": {"inputs": ["close"], "func": f35_rvre_119_sigma_nonoverlap_5d_returns_252d_d2},
    "f35_rvre_120_sigma_nonoverlap_21d_returns_504d_d2": {"inputs": ["close"], "func": f35_rvre_120_sigma_nonoverlap_21d_returns_504d_d2},
    "f35_rvre_121_sigma_nonoverlap_5d_returns_1260d_d2": {"inputs": ["close"], "func": f35_rvre_121_sigma_nonoverlap_5d_returns_1260d_d2},
    "f35_rvre_122_sigma_nonoverlap_21d_returns_1260d_d2": {"inputs": ["close"], "func": f35_rvre_122_sigma_nonoverlap_21d_returns_1260d_d2},
    "f35_rvre_123_variance_ratio_nonoverlap_5d_vs_1d_252d_d2": {"inputs": ["close"], "func": f35_rvre_123_variance_ratio_nonoverlap_5d_vs_1d_252d_d2},
    "f35_rvre_124_median_rv21_in_252d_d2": {"inputs": ["close"], "func": f35_rvre_124_median_rv21_in_252d_d2},
    "f35_rvre_125_max_rv21_in_252d_d2": {"inputs": ["close"], "func": f35_rvre_125_max_rv21_in_252d_d2},
    "f35_rvre_126_min_rv21_in_252d_d2": {"inputs": ["close"], "func": f35_rvre_126_min_rv21_in_252d_d2},
    "f35_rvre_127_median_rv63_in_504d_d2": {"inputs": ["close"], "func": f35_rvre_127_median_rv63_in_504d_d2},
    "f35_rvre_128_max_rv63_in_504d_d2": {"inputs": ["close"], "func": f35_rvre_128_max_rv63_in_504d_d2},
    "f35_rvre_129_min_rv63_in_504d_d2": {"inputs": ["close"], "func": f35_rvre_129_min_rv63_in_504d_d2},
    "f35_rvre_130_consecutive_streak_abs_r_above_p80_252d_d2": {"inputs": ["close"], "func": f35_rvre_130_consecutive_streak_abs_r_above_p80_252d_d2},
    "f35_rvre_131_longest_run_abs_r_above_p80_in_252d_d2": {"inputs": ["close"], "func": f35_rvre_131_longest_run_abs_r_above_p80_in_252d_d2},
    "f35_rvre_132_serial_corr_rsq_lag1_504d_d2": {"inputs": ["close"], "func": f35_rvre_132_serial_corr_rsq_lag1_504d_d2},
    "f35_rvre_133_serial_corr_rsq_lag5_504d_d2": {"inputs": ["close"], "func": f35_rvre_133_serial_corr_rsq_lag5_504d_d2},
    "f35_rvre_134_count_abs_r_above_p80_in_21d_d2": {"inputs": ["close"], "func": f35_rvre_134_count_abs_r_above_p80_in_21d_d2},
    "f35_rvre_135_count_abs_r_above_p80_in_63d_d2": {"inputs": ["close"], "func": f35_rvre_135_count_abs_r_above_p80_in_63d_d2},
    "f35_rvre_136_run_length_entropy_vol_regime_252d_d2": {"inputs": ["close"], "func": f35_rvre_136_run_length_entropy_vol_regime_252d_d2},
    "f35_rvre_137_fraction_in_high_vol_clusters_252d_d2": {"inputs": ["close"], "func": f35_rvre_137_fraction_in_high_vol_clusters_252d_d2},
    "f35_rvre_138_cumulative_variance_252d_d2": {"inputs": ["close"], "func": f35_rvre_138_cumulative_variance_252d_d2},
    "f35_rvre_139_cumulative_abs_return_21d_d2": {"inputs": ["close"], "func": f35_rvre_139_cumulative_abs_return_21d_d2},
    "f35_rvre_140_cumulative_variance_1260d_d2": {"inputs": ["close"], "func": f35_rvre_140_cumulative_variance_1260d_d2},
    "f35_rvre_141_ratio_cum_variance_252_to_1260_d2": {"inputs": ["close"], "func": f35_rvre_141_ratio_cum_variance_252_to_1260_d2},
    "f35_rvre_142_cumulative_abs_return_504d_d2": {"inputs": ["close"], "func": f35_rvre_142_cumulative_abs_return_504d_d2},
    "f35_rvre_143_overnight_rv_21d_d2": {"inputs": ["open", "close"], "func": f35_rvre_143_overnight_rv_21d_d2},
    "f35_rvre_144_intraday_rv_21d_d2": {"inputs": ["open", "close"], "func": f35_rvre_144_intraday_rv_21d_d2},
    "f35_rvre_145_overnight_rv_252d_d2": {"inputs": ["open", "close"], "func": f35_rvre_145_overnight_rv_252d_d2},
    "f35_rvre_146_intraday_rv_252d_d2": {"inputs": ["open", "close"], "func": f35_rvre_146_intraday_rv_252d_d2},
    "f35_rvre_147_ratio_overnight_to_intraday_rv_63d_d2": {"inputs": ["open", "close"], "func": f35_rvre_147_ratio_overnight_to_intraday_rv_63d_d2},
    "f35_rvre_148_max_rv5_in_63d_d2": {"inputs": ["close"], "func": f35_rvre_148_max_rv5_in_63d_d2},
    "f35_rvre_149_min_rv5_in_63d_d2": {"inputs": ["close"], "func": f35_rvre_149_min_rv5_in_63d_d2},
    "f35_rvre_150_median_rv5_in_252d_d2": {"inputs": ["close"], "func": f35_rvre_150_median_rv5_in_252d_d2},
}
