"""dollar_volume_intensity d3 features 226-300 — Pipeline 1b-technical (extension).

Continuation of the gap-fill extension. New buckets:
- Distribution-day $-vol variant (O'Neil + $-vol gate)
- $-vol drawdown process (academic-style liquidity drawdown)
- Multi-resolution / wavelet decomposition of $-vol
- $-vol mutual information with price-change at various lags
- Cross-horizon $-vol extremes + persistence contrasts
- Liquidity-risk premium proxies
- $-vol concentration: top-K share dynamics, Lorenz-curve-derived
- Composite intensity / exhaustion scores

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers — no cross-family imports.
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


# ---------------------------- family helpers ----------------------------

def _dollar_vol(close: pd.Series, volume: pd.Series) -> pd.Series:
    return (close * volume).astype(float)


def _rolling_pct_rank(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    def _rk(w):
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    return s.rolling(window, min_periods=min_periods).apply(_rk, raw=True)


def _rolling_quantile(s, window, q, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    return s.rolling(window, min_periods=min_periods).quantile(q)


def _consecutive_true_streak(b: pd.Series) -> pd.Series:
    grp = (~b.fillna(False)).cumsum()
    return b.fillna(False).astype(int).groupby(grp).cumsum()


def _mutual_info_binned(x, y, bins=8):
    mask = (~np.isnan(x)) & (~np.isnan(y))
    if mask.sum() < 4 * bins:
        return np.nan
    x = x[mask]; y = y[mask]
    if x.size == 0 or x.max() == x.min() or y.max() == y.min():
        return np.nan
    xe = np.linspace(x.min(), x.max(), bins + 1)
    ye = np.linspace(y.min(), y.max(), bins + 1)
    hxy, _, _ = np.histogram2d(x, y, bins=[xe, ye])
    pxy = hxy / hxy.sum()
    px = pxy.sum(axis=1)
    py = pxy.sum(axis=0)
    def H(p):
        p = p[p > 0]
        return float(-(p * np.log(p)).sum()) if p.size > 0 else 0.0
    return float(H(px) + H(py) - H(pxy.ravel()))


# ============================================================
# Bucket T — Distribution-day $-vol variant (O'Neil + $-vol gate) (226-235)
# ============================================================

def f21_dvit_226_dv_distribution_day_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """$-vol distribution day: close down >0.2% AND log-$-vol z(252d) > 0 (above-baseline $-flow on a down day)."""
    pc = close.pct_change()
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return ((pc < -0.002) & (z > 0)).astype(float)


def f21_dvit_227_dv_distribution_day_count_25d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 25-bar count of $-vol distribution days."""
    pc = close.pct_change()
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    flag = ((pc < -0.002) & (z > 0)).astype(float)
    return flag.rolling(25, min_periods=10).sum()


def f21_dvit_228_dv_distribution_day_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 63d count of $-vol distribution days."""
    pc = close.pct_change()
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    flag = ((pc < -0.002) & (z > 0)).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f21_dvit_229_dv_distribution_severity_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d sum of |return| × log-$-vol z(252d) on $-vol distribution days only — magnitude-weighted."""
    pc = close.pct_change()
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    sev = pc.abs() * z
    flag = (pc < -0.002) & (z > 0)
    return sev.where(flag, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_230_dv_accumulation_day_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """$-vol accumulation day: close up >0.2% AND log-$-vol z(252d) > 0."""
    pc = close.pct_change()
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return ((pc > 0.002) & (z > 0)).astype(float)


def f21_dvit_231_dv_distribution_to_accumulation_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(63d $-vol distribution count) / (63d $-vol accumulation count) — net distribution intensity."""
    pc = close.pct_change()
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    dd = ((pc < -0.002) & (z > 0)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    ad = ((pc > 0.002) & (z > 0)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(dd, ad + 1.0)


def f21_dvit_232_dv_distribution_days_cluster_5d_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when >=4 $-vol distribution days in trailing 25 bars — warning cluster."""
    pc = close.pct_change()
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    flag = ((pc < -0.002) & (z > 0)).astype(float)
    return (flag.rolling(25, min_periods=10).sum() >= 4).astype(float)


def f21_dvit_233_dv_distribution_strict_high_dv_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Strict: close down >1% AND log-$-vol z(252d) > 2."""
    pc = close.pct_change()
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return ((pc < -0.01) & (z > 2.0)).astype(float)


def f21_dvit_234_dv_distribution_strict_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of strict $-vol distribution days."""
    pc = close.pct_change()
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return ((pc < -0.01) & (z > 2.0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_235_consec_dv_distribution_days_streak(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current consecutive-bar streak of $-vol distribution days."""
    pc = close.pct_change()
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    cond = (pc < -0.002) & (z > 0)
    return _consecutive_true_streak(cond).astype(float)


# ============================================================
# Bucket U — $-vol drawdown process (academic style) (236-245)
# ============================================================

def f21_dvit_236_dv_running_drawdown_pct_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current dv / 252d-trailing-max dv minus 1 — drawdown as pct of recent peak."""
    dv = _dollar_vol(close, volume)
    return _safe_div(dv, dv.rolling(YDAYS, min_periods=QDAYS).max()) - 1.0


def f21_dvit_237_dv_running_drawdown_log_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """log(dv) - log(252d trailing max dv) — log-space drawdown."""
    ldv = _safe_log(_dollar_vol(close, volume))
    return ldv - ldv.rolling(YDAYS, min_periods=QDAYS).max()


def f21_dvit_238_dv_drawdown_severity_252d_mean(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean over 252d of |dv drawdown|. Measures sustained deficit."""
    dv = _dollar_vol(close, volume)
    dd = _safe_div(dv, dv.rolling(YDAYS, min_periods=QDAYS).max()) - 1.0
    return dd.abs().rolling(YDAYS, min_periods=QDAYS).mean()


def f21_dvit_239_dv_drawdown_time_below_minus50pct_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where dv has fallen >50% from its trailing 252d peak."""
    dv = _dollar_vol(close, volume)
    dd = _safe_div(dv, dv.rolling(YDAYS, min_periods=QDAYS).max()) - 1.0
    return (dd < -0.50).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_240_dv_drawdown_time_below_minus80pct_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where dv has fallen >80% from its trailing 252d peak (extreme dryup)."""
    dv = _dollar_vol(close, volume)
    dd = _safe_div(dv, dv.rolling(YDAYS, min_periods=QDAYS).max()) - 1.0
    return (dd < -0.80).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_241_dv_drawdown_recovery_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when dv has recovered to within 10% of trailing 252d peak after being below it, else 0."""
    dv = _dollar_vol(close, volume)
    rmax = dv.rolling(YDAYS, min_periods=QDAYS).max()
    return ((dv / rmax >= 0.90) & (dv.shift(1) / rmax.shift(1) < 0.90)).astype(float)


def f21_dvit_242_dv_drawdown_recovery_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of dv-drawdown recovery events."""
    dv = _dollar_vol(close, volume)
    rmax = dv.rolling(YDAYS, min_periods=QDAYS).max()
    rec = ((dv / rmax >= 0.90) & (dv.shift(1) / rmax.shift(1) < 0.90)).astype(float)
    return rec.rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_243_dv_max_drawdown_in_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max drawdown (most negative dv/peak - 1) observed in trailing 252d window."""
    dv = _dollar_vol(close, volume)
    def _mdd(w):
        v = w[~np.isnan(w)]
        if v.size < 20:
            return np.nan
        peak = np.maximum.accumulate(v)
        dd = v / np.where(peak > 0, peak, np.nan) - 1.0
        return float(np.nanmin(dd))
    return dv.rolling(YDAYS, min_periods=QDAYS).apply(_mdd, raw=True)


def f21_dvit_244_dv_drawdown_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling skewness of daily dv drawdowns over trailing 252d — left-skewed means heavy down-days."""
    dv = _dollar_vol(close, volume)
    dd = _safe_div(dv, dv.rolling(YDAYS, min_periods=QDAYS).max()) - 1.0
    return dd.rolling(YDAYS, min_periods=QDAYS).skew()


def f21_dvit_245_dv_drawdown_dwell_below_zero_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d fraction of bars with dv drawdown < 0 (i.e., not at peak)."""
    dv = _dollar_vol(close, volume)
    dd = _safe_div(dv, dv.rolling(YDAYS, min_periods=QDAYS).max()) - 1.0
    return (dd < 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


# ============================================================
# Bucket V — Multi-resolution / wavelet decomposition of $-vol (246-255)
# ============================================================

def f21_dvit_246_haar_wavelet_level1_logdv_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Haar-wavelet level-1 detail of log-$-vol — high-freq noise magnitude (252d std)."""
    ldv = _safe_log(_dollar_vol(close, volume))
    detail = (ldv - ldv.shift(1)) / np.sqrt(2.0)
    return detail.rolling(YDAYS, min_periods=QDAYS).std()


def f21_dvit_247_haar_wavelet_level2_logdv_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Haar-wavelet level-2 detail of log-$-vol — 2-bar-scale fluctuations."""
    ldv = _safe_log(_dollar_vol(close, volume))
    s1 = (ldv + ldv.shift(1)) / np.sqrt(2.0)
    detail2 = (s1 - s1.shift(2)) / np.sqrt(2.0)
    return detail2.rolling(YDAYS, min_periods=QDAYS).std()


def f21_dvit_248_haar_wavelet_level3_logdv_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Haar-wavelet level-3 detail of log-$-vol — 4-bar-scale fluctuations."""
    ldv = _safe_log(_dollar_vol(close, volume))
    s1 = (ldv + ldv.shift(1)) / np.sqrt(2.0)
    s2 = (s1 + s1.shift(2)) / np.sqrt(2.0)
    detail3 = (s2 - s2.shift(4)) / np.sqrt(2.0)
    return detail3.rolling(YDAYS, min_periods=QDAYS).std()


def f21_dvit_249_dv_wavelet_low_to_high_ratio_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """log-$-vol wavelet level-3 std / level-1 std — > 1 = low-freq dominated."""
    ldv = _safe_log(_dollar_vol(close, volume))
    d1 = (ldv - ldv.shift(1)) / np.sqrt(2.0)
    s1 = (ldv + ldv.shift(1)) / np.sqrt(2.0)
    s2 = (s1 + s1.shift(2)) / np.sqrt(2.0)
    d3 = (s2 - s2.shift(4)) / np.sqrt(2.0)
    return _safe_div(d3.rolling(YDAYS, min_periods=QDAYS).std(), d1.rolling(YDAYS, min_periods=QDAYS).std())


def f21_dvit_250_dv_smooth_minus_raw_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of (EMA21 log-$-vol minus raw log-$-vol) — shock vs smoothed."""
    ldv = _safe_log(_dollar_vol(close, volume))
    return _rolling_zscore(ldv.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean() - ldv, YDAYS)


def f21_dvit_251_dv_ema_diff_21_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """EMA21(log-$-vol) minus EMA63(log-$-vol) — short-vs-medium $-vol momentum."""
    ldv = _safe_log(_dollar_vol(close, volume))
    return ldv.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean() - ldv.ewm(span=QDAYS, min_periods=MDAYS, adjust=False).mean()


def f21_dvit_252_dv_ema_diff_63_252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """EMA63(log-$-vol) minus EMA252(log-$-vol) — medium-vs-long $-vol drift."""
    ldv = _safe_log(_dollar_vol(close, volume))
    return ldv.ewm(span=QDAYS, min_periods=MDAYS, adjust=False).mean() - ldv.ewm(span=YDAYS, min_periods=QDAYS, adjust=False).mean()


def f21_dvit_253_dv_multi_horizon_zscore_aggregate(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(z(log_dv, 21) + z(log_dv, 63) + z(log_dv, 252)) / 3 — aggregate multi-horizon $-vol z."""
    ldv = _safe_log(_dollar_vol(close, volume))
    return (_rolling_zscore(ldv, MDAYS) + _rolling_zscore(ldv, QDAYS) + _rolling_zscore(ldv, YDAYS)) / 3.0


def f21_dvit_254_dv_multi_horizon_zscore_dispersion(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Std across (z(log_dv,21), z(log_dv,63), z(log_dv,252)) at each bar — multi-horizon disagreement."""
    ldv = _safe_log(_dollar_vol(close, volume))
    z21 = _rolling_zscore(ldv, MDAYS); z63 = _rolling_zscore(ldv, QDAYS); z252 = _rolling_zscore(ldv, YDAYS)
    return pd.concat([z21, z63, z252], axis=1).std(axis=1)


def f21_dvit_255_dv_hp_filter_residual_std_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """HP-filter proxy: 252d std of (log-$-vol - EMA126(log_dv)) — residual magnitude."""
    ldv = _safe_log(_dollar_vol(close, volume))
    trend = ldv.ewm(span=QDAYS * 2, min_periods=QDAYS, adjust=False).mean()
    return (ldv - trend).rolling(YDAYS, min_periods=QDAYS).std()


# ============================================================
# Bucket W — $-vol mutual information with price-change (256-265)
# ============================================================

def f21_dvit_256_mi_logdv_logreturn_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mutual information between log-$-vol and log-return over 63d."""
    ldv = _safe_log(_dollar_vol(close, volume))
    r = _safe_log(close).diff()
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(QDAYS - 1, n):
        out.iloc[i] = _mutual_info_binned(ldv.iloc[i - QDAYS + 1 : i + 1].values, r.iloc[i - QDAYS + 1 : i + 1].values, bins=6)
    return out


def f21_dvit_257_mi_logdv_logreturn_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mutual information between log-$-vol and log-return over 252d."""
    ldv = _safe_log(_dollar_vol(close, volume))
    r = _safe_log(close).diff()
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        out.iloc[i] = _mutual_info_binned(ldv.iloc[i - YDAYS + 1 : i + 1].values, r.iloc[i - YDAYS + 1 : i + 1].values, bins=8)
    return out


def f21_dvit_258_mi_logdv_lagged_logreturn_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mutual information between log-$-vol and 1-bar-lagged |log-return| over 63d (PIT-safe; uses past)."""
    ldv_lag = _safe_log(_dollar_vol(close, volume)).shift(1)
    ar = _safe_log(close).diff().abs()
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(QDAYS, n):
        out.iloc[i] = _mutual_info_binned(ldv_lag.iloc[i - QDAYS + 1 : i + 1].values, ar.iloc[i - QDAYS + 1 : i + 1].values, bins=6)
    return out


def f21_dvit_259_mi_change_63_minus_252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """MI(log_dv, log_ret, 63) minus MI(log_dv, log_ret, 252) — coupling-shift."""
    ldv = _safe_log(_dollar_vol(close, volume))
    r = _safe_log(close).diff()
    out63 = pd.Series(np.nan, index=close.index, dtype=float)
    out252 = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        out63.iloc[i] = _mutual_info_binned(ldv.iloc[i - QDAYS + 1 : i + 1].values, r.iloc[i - QDAYS + 1 : i + 1].values, bins=6)
        out252.iloc[i] = _mutual_info_binned(ldv.iloc[i - YDAYS + 1 : i + 1].values, r.iloc[i - YDAYS + 1 : i + 1].values, bins=8)
    return out63 - out252


def f21_dvit_260_conditional_entropy_dv_given_return_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """H(log_dv | binned log-return) over trailing 252d — uncertainty of dv given return state."""
    ldv = _safe_log(_dollar_vol(close, volume))
    r = _safe_log(close).diff()
    bins = 6
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        x = r.iloc[i - YDAYS + 1 : i + 1].values
        y = ldv.iloc[i - YDAYS + 1 : i + 1].values
        mask = (~np.isnan(x)) & (~np.isnan(y))
        if mask.sum() < 50:
            continue
        x = x[mask]; y = y[mask]
        if x.max() == x.min() or y.max() == y.min():
            continue
        xe = np.linspace(x.min(), x.max(), bins + 1)
        ye = np.linspace(y.min(), y.max(), bins + 1)
        hxy, _, _ = np.histogram2d(x, y, bins=[xe, ye])
        pxy = hxy / hxy.sum()
        px = pxy.sum(axis=1)
        nz = px > 0
        h_y_given_x = 0.0
        for j in np.where(nz)[0]:
            cond = pxy[j, :] / px[j]
            cond = cond[cond > 0]
            h_y_given_x += px[j] * float(-(cond * np.log(cond)).sum())
        out.iloc[i] = h_y_given_x
    return out


def f21_dvit_261_dv_information_share_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Information share proxy: MI(log_dv, |log_ret|) / H(|log_ret|) over 252d — fraction of return-vol explained by dv."""
    ldv = _safe_log(_dollar_vol(close, volume))
    ar = _safe_log(close).diff().abs()
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    bins = 8
    for i in range(YDAYS - 1, n):
        x = ldv.iloc[i - YDAYS + 1 : i + 1].values
        y = ar.iloc[i - YDAYS + 1 : i + 1].values
        mi = _mutual_info_binned(x, y, bins=bins)
        if np.isnan(mi):
            continue
        ymask = ~np.isnan(y)
        if ymask.sum() < 50:
            continue
        yv = y[ymask]
        if yv.max() == yv.min():
            continue
        ye = np.linspace(yv.min(), yv.max(), bins + 1)
        hy, _ = np.histogram(yv, bins=ye)
        py = hy.astype(float) / hy.sum()
        py = py[py > 0]
        Hy = float(-(py * np.log(py)).sum()) if py.size > 0 else np.nan
        if Hy and Hy > 0:
            out.iloc[i] = mi / Hy
    return out


def f21_dvit_262_mi_logdv_abs_open_close_63d(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """MI between log-$-vol and |log(close/open)| (intraday-magnitude) over 63d."""
    ldv = _safe_log(_dollar_vol(close, volume))
    intra = (_safe_log(close) - _safe_log(open)).abs()
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(QDAYS - 1, n):
        out.iloc[i] = _mutual_info_binned(ldv.iloc[i - QDAYS + 1 : i + 1].values, intra.iloc[i - QDAYS + 1 : i + 1].values, bins=6)
    return out


def f21_dvit_263_dv_kl_divergence_recent_vs_baseline_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """KL divergence between trailing 21d log-$-vol distribution and trailing 252d baseline."""
    ldv = _safe_log(_dollar_vol(close, volume))
    bins = 8
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        x252 = ldv.iloc[i - YDAYS + 1 : i + 1].dropna().values
        x21 = ldv.iloc[i - MDAYS + 1 : i + 1].dropna().values
        if x252.size < 50 or x21.size < 10 or x252.max() == x252.min():
            continue
        edges = np.linspace(x252.min(), x252.max(), bins + 1)
        q, _ = np.histogram(x252, bins=edges)
        q = q.astype(float) / max(q.sum(), 1)
        p, _ = np.histogram(x21, bins=edges)
        p = p.astype(float) / max(p.sum(), 1)
        q = np.where(q == 0, 1e-9, q)
        p_pos = p > 0
        out.iloc[i] = float((p[p_pos] * np.log(p[p_pos] / q[p_pos])).sum())
    return out


def f21_dvit_264_dv_joint_entropy_logdv_logret_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Joint Shannon entropy(252d) of binned (log_dv, log_return) — state diversity of flow-return pair."""
    ldv = _safe_log(_dollar_vol(close, volume))
    r = _safe_log(close).diff()
    bins = 6
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        x = ldv.iloc[i - YDAYS + 1 : i + 1].values
        y = r.iloc[i - YDAYS + 1 : i + 1].values
        mask = (~np.isnan(x)) & (~np.isnan(y))
        if mask.sum() < 50:
            continue
        x = x[mask]; y = y[mask]
        if x.max() == x.min() or y.max() == y.min():
            continue
        xe = np.linspace(x.min(), x.max(), bins + 1)
        ye = np.linspace(y.min(), y.max(), bins + 1)
        h, _, _ = np.histogram2d(x, y, bins=[xe, ye])
        p = h.ravel() / max(h.sum(), 1)
        p = p[p > 0]
        out.iloc[i] = float(-(p * np.log(p)).sum())
    return out


def f21_dvit_265_dv_shannon_entropy_signed_dv_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Shannon entropy(252d) of binned signed-$-vol = sign(close.diff()) × dv — flow concentration in $-units."""
    dv = _dollar_vol(close, volume)
    sgn = np.sign(close.diff()).fillna(0.0)
    sdv = sgn * dv
    bins = 10
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        v = sdv.iloc[i - YDAYS + 1 : i + 1].dropna().values
        if v.size < 50 or v.max() == v.min():
            continue
        edges = np.linspace(v.min(), v.max(), bins + 1)
        h, _ = np.histogram(v, bins=edges)
        p = h.astype(float) / max(h.sum(), 1)
        p = p[p > 0]
        out.iloc[i] = float(-(p * np.log(p)).sum())
    return out


# ============================================================
# Bucket X — Liquidity-risk premium proxies (266-275)
# ============================================================

def f21_dvit_266_amihud_proxy_252d_mean(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Amihud-style: mean over 252d of (|log-return| / dollar_vol). High = illiquid."""
    dv = _dollar_vol(close, volume)
    ar = _safe_log(close).diff().abs()
    return _safe_div(ar, dv).rolling(YDAYS, min_periods=QDAYS).mean()


def f21_dvit_267_amihud_proxy_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of daily Amihud-style |log-return| / dollar_vol."""
    dv = _dollar_vol(close, volume)
    ar = _safe_log(close).diff().abs()
    return _rolling_zscore(_safe_div(ar, dv), YDAYS)


def f21_dvit_268_dv_per_atr_zscore_252d_v2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of (1 / (dv/ATR21)) — inverse capacity proxy."""
    dv = _dollar_vol(close, volume)
    atr = _atr(high, low, close, n=MDAYS)
    return _rolling_zscore(_safe_div(atr, dv), YDAYS)


def f21_dvit_269_kyle_lambda_proxy_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Kyle's lambda proxy: 252d regression slope of |return| on log_dv. Negative beta = liquid stock; positive = illiquid."""
    ldv = _safe_log(_dollar_vol(close, volume))
    ar = _safe_log(close).diff().abs()
    def _b(idx):
        x = ldv.iloc[idx].values; y = ar.iloc[idx].values
        mask = (~np.isnan(x)) & (~np.isnan(y))
        if mask.sum() < 30:
            return np.nan
        xv = x[mask]; yv = y[mask]
        xm = xv.mean(); ym = yv.mean()
        sxx = ((xv - xm) ** 2).sum()
        if sxx <= 0:
            return np.nan
        return float(((xv - xm) * (yv - ym)).sum() / sxx)
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        out.iloc[i] = _b(range(i - YDAYS + 1, i + 1))
    return out


def f21_dvit_270_dv_per_volatility_252d_mean(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean(252d) of (log_dv / std(log_ret, 21d)) — flow per unit short-vol."""
    ldv = _safe_log(_dollar_vol(close, volume))
    r = _safe_log(close).diff()
    s21 = r.rolling(MDAYS, min_periods=WDAYS).std()
    return _safe_div(ldv, s21).rolling(YDAYS, min_periods=QDAYS).mean()


def f21_dvit_271_dv_capacity_residual_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS residual: log_dv - (a + b*log(ATR)) using HL spread proxy — flow that can't be explained by volatility."""
    ldv = _safe_log(_dollar_vol(close, volume))
    sp = _safe_log(close).diff().abs()
    def _res(idx):
        x = sp.iloc[idx].values; y = ldv.iloc[idx].values
        mask = (~np.isnan(x)) & (~np.isnan(y))
        if mask.sum() < 30:
            return np.nan
        xv = x[mask]; yv = y[mask]
        xm = xv.mean(); ym = yv.mean()
        sxx = ((xv - xm) ** 2).sum()
        if sxx <= 0:
            return np.nan
        b = ((xv - xm) * (yv - ym)).sum() / sxx
        a = ym - b * xm
        last_x = x[-1]; last_y = y[-1]
        if np.isnan(last_x) or np.isnan(last_y):
            return np.nan
        return float(last_y - (a + b * last_x))
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        out.iloc[i] = _res(range(i - YDAYS + 1, i + 1))
    return out


def f21_dvit_272_dv_per_corwin_schultz_spread_252d_mean(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean over 252d of (dv / Corwin-Schultz spread proxy) — flow per unit illiquidity."""
    lh = _safe_log(high) - _safe_log(low)
    beta_pit = (lh.shift(1) ** 2) + (lh ** 2)
    pair_high = pd.concat([high.shift(1), high], axis=1).max(axis=1)
    pair_low = pd.concat([low.shift(1), low], axis=1).min(axis=1)
    gamma = (_safe_log(pair_high) - _safe_log(pair_low)) ** 2
    denom_a = 3.0 - 2.0 * np.sqrt(2.0)
    alpha_num = np.sqrt(2.0 * beta_pit) - np.sqrt(beta_pit)
    alpha = (alpha_num / denom_a) - np.sqrt(gamma / denom_a)
    spread = (2.0 * (np.exp(alpha) - 1.0) / (1.0 + np.exp(alpha))).clip(lower=1e-9)
    dv = _dollar_vol(close, volume)
    return _safe_div(dv, spread).rolling(YDAYS, min_periods=QDAYS).mean()


def f21_dvit_273_liquidity_premium_proxy_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(Mean Amihud, 252d) × (mean HL spread, 252d) — combined illiquidity premium proxy."""
    dv = _dollar_vol(close, volume)
    ar = _safe_log(close).diff().abs()
    amihud_mean = _safe_div(ar, dv).rolling(YDAYS, min_periods=QDAYS).mean()
    hl_spread_mean = ((high - low) / close).rolling(YDAYS, min_periods=QDAYS).mean()
    return amihud_mean * hl_spread_mean


def f21_dvit_274_dv_capacity_shrinkage_indicator_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when (current dv / 252d-mean dv) < 0.5 AND mean Amihud is in top decile of trailing 252d distribution."""
    dv = _dollar_vol(close, volume)
    mean252 = dv.rolling(YDAYS, min_periods=QDAYS).mean()
    cap_shrunk = (dv / mean252) < 0.5
    ar = _safe_log(close).diff().abs()
    amihud = _safe_div(ar, dv)
    am_q90 = _rolling_quantile(amihud, YDAYS, 0.90)
    illiquid = amihud > am_q90
    return (cap_shrunk & illiquid).astype(float)


def f21_dvit_275_dv_capacity_shrinkage_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 63d count of dv-capacity-shrinkage events."""
    dv = _dollar_vol(close, volume)
    mean252 = dv.rolling(YDAYS, min_periods=QDAYS).mean()
    cap_shrunk = (dv / mean252) < 0.5
    ar = _safe_log(close).diff().abs()
    amihud = _safe_div(ar, dv)
    am_q90 = _rolling_quantile(amihud, YDAYS, 0.90)
    illiquid = amihud > am_q90
    flag = (cap_shrunk & illiquid).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


# ============================================================
# Bucket Y — $-vol concentration: Lorenz / top-K dynamics (276-285)
# ============================================================

def f21_dvit_276_dv_top_decile_threshold_change_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(252d top-decile dv threshold) / (504d top-decile dv threshold) — recent threshold vs longer baseline."""
    dv = _dollar_vol(close, volume)
    q90_252 = _rolling_quantile(dv, YDAYS, 0.90)
    q90_504 = _rolling_quantile(dv, DDAYS_2Y, 0.90)
    return _safe_div(q90_252, q90_504)


def f21_dvit_277_dv_top_decile_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars in top decile of 252d dv (should be ~25 by construction; deviations are interesting)."""
    dv = _dollar_vol(close, volume)
    q90 = _rolling_quantile(dv, YDAYS, 0.90)
    return (dv >= q90).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_278_dv_concentration_in_top_decile_share_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of dv on top-decile-dv bars / total dv (252d) — what fraction of activity occurs on top-10% of days."""
    dv = _dollar_vol(close, volume)
    q90 = _rolling_quantile(dv, YDAYS, 0.90)
    top_v = dv.where(dv >= q90, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()
    tot = dv.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(top_v, tot)


def f21_dvit_279_dv_concentration_in_top_percentile_share_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of dv on top-1% bars / total dv (252d) — extreme concentration share."""
    dv = _dollar_vol(close, volume)
    q99 = _rolling_quantile(dv, YDAYS, 0.99)
    top_v = dv.where(dv >= q99, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()
    tot = dv.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(top_v, tot)


def f21_dvit_280_dv_concentration_change_252d_vs_504d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Top-decile share(252d) minus top-decile share(504d) — concentration drift."""
    dv = _dollar_vol(close, volume)
    def _share(window, q):
        qv = _rolling_quantile(dv, window, q)
        top_v = dv.where(dv >= qv, 0.0).rolling(window, min_periods=max(window // 3, 5)).sum()
        tot = dv.rolling(window, min_periods=max(window // 3, 5)).sum()
        return _safe_div(top_v, tot)
    return _share(YDAYS, 0.90) - _share(DDAYS_2Y, 0.90)


def f21_dvit_281_dv_lorenz_area_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Lorenz curve area (above the diagonal) for dv distribution over trailing 252d. Range 0 (equal) to 0.5 (concentrated)."""
    dv = _dollar_vol(close, volume)
    def _l(w):
        v = w[~np.isnan(w)]
        if v.size < 30 or v.sum() <= 0:
            return np.nan
        v = np.sort(v)
        cum = np.cumsum(v) / v.sum()
        return float(0.5 - cum.mean() + 0.5 / v.size)
    return dv.rolling(YDAYS, min_periods=QDAYS).apply(_l, raw=True)


def f21_dvit_282_dv_kurtosis_signal_extreme_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of rolling 252d kurtosis of log_dv — kurtosis-of-kurtosis early-warning proxy."""
    ldv = _safe_log(_dollar_vol(close, volume))
    k = ldv.rolling(YDAYS, min_periods=QDAYS).kurt()
    return _rolling_zscore(k, YDAYS)


def f21_dvit_283_dv_concentration_pareto_alpha_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Pareto-tail alpha proxy (MLE on top decile of dv in 252d): alpha = 1 / mean(log(dv/threshold))."""
    dv = _dollar_vol(close, volume)
    def _alpha(w):
        v = w[~np.isnan(w)]
        if v.size < 30 or v.sum() <= 0:
            return np.nan
        thr = np.quantile(v, 0.90)
        tail = v[v > thr]
        if tail.size < 5:
            return np.nan
        m = np.mean(np.log(tail / thr))
        if m <= 0:
            return np.nan
        return float(1.0 / m)
    return dv.rolling(YDAYS, min_periods=QDAYS).apply(_alpha, raw=True)


def f21_dvit_284_dv_gini_change_252_vs_504(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Gini coefficient of dv (252d) minus Gini (504d) — concentration regime shift."""
    dv = _dollar_vol(close, volume)
    def _g(w):
        v = w[~np.isnan(w)]
        if v.size < 5 or v.sum() <= 0:
            return np.nan
        v = np.sort(v)
        n = v.size
        idx = np.arange(1, n + 1)
        ss = v.sum()
        return float((2.0 * (idx * v).sum() / ss - (n + 1)) / n)
    g252 = dv.rolling(YDAYS, min_periods=QDAYS).apply(_g, raw=True)
    g504 = dv.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_g, raw=True)
    return g252 - g504


def f21_dvit_285_dv_top_decile_streak_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max consecutive-bar streak of (dv >= 252d 90%-quantile) in trailing 252d."""
    dv = _dollar_vol(close, volume)
    q90 = _rolling_quantile(dv, YDAYS, 0.90)
    streak = _consecutive_true_streak(dv >= q90).astype(float)
    return streak.rolling(YDAYS, min_periods=QDAYS).max()


# ============================================================
# Bucket Z — Composite intensity / exhaustion scores (286-300)
# ============================================================

def f21_dvit_286_dv_intensity_composite_score_252d_v2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite intensity v2: {z>2, pct_rank>0.9, dv/median>2, top-decile-share>0.4}. Distinct from base #136."""
    dv = _dollar_vol(close, volume)
    ldv = _safe_log(dv)
    z = _rolling_zscore(ldv, YDAYS)
    pr = _rolling_pct_rank(dv, YDAYS)
    med = dv.rolling(YDAYS, min_periods=QDAYS).median()
    q90 = _rolling_quantile(dv, YDAYS, 0.90)
    top_v = dv.where(dv >= q90, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()
    tot = dv.rolling(YDAYS, min_periods=QDAYS).sum()
    share = _safe_div(top_v, tot)
    return ((z > 2.0).astype(float) + (pr > 0.9).astype(float) + (_safe_div(dv, med) > 2.0).astype(float) + (share > 0.4).astype(float))


def f21_dvit_287_dv_exhaustion_score_252d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Exhaustion: {dv z>3 in past 21d AND price 252d-high in past 5d} indicator times negative subsequent slope."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    burst = (z > 3.0).astype(float).rolling(MDAYS, min_periods=WDAYS).max()
    is_peak = (high >= rmax).astype(float).rolling(WDAYS, min_periods=1).max()
    slope = _rolling_slope(close, MDAYS)
    return ((burst > 0) & (is_peak > 0) & (slope < 0)).astype(float)


def f21_dvit_288_dv_post_climax_decay_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d sum of (peak_dv_252 - dv_t) since the trailing 252d dv peak — area-under-decay."""
    dv = _dollar_vol(close, volume)
    def _cd(w):
        v = w[~np.isnan(w)]
        if v.size < 10:
            return np.nan
        peak_idx = int(np.argmax(w))
        peak = w[peak_idx]
        if not np.isfinite(peak):
            return np.nan
        seg = w[peak_idx + 1:]
        seg = seg[~np.isnan(seg)]
        if seg.size == 0:
            return 0.0
        return float(np.sum(peak - seg))
    return dv.rolling(YDAYS, min_periods=QDAYS).apply(_cd, raw=True)


def f21_dvit_289_dv_active_silent_balance_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d fraction in high-regime minus fraction in low-regime."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    high_dwell = (z > 0.5).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    low_dwell = (z < -0.5).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    return high_dwell - low_dwell


def f21_dvit_290_dv_burst_dryup_oscillation_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of regime-state transitions (high-mid-low) in trailing 252d — oscillation intensity."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    label = np.sign(z.where(z.abs() > 0.5, 0.0))
    trans = (label != label.shift(1)).astype(float)
    return trans.rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_291_dv_post_burst_failure_to_recover_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when trailing 21d-max-z(252d) > 3 (burst in past 21d) AND current dv < 252d-mean dv (failure to recover)."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    had_burst = (z > 3.0).astype(float).rolling(MDAYS, min_periods=WDAYS).max()
    dv = _dollar_vol(close, volume)
    below_mean = dv < dv.rolling(YDAYS, min_periods=QDAYS).mean()
    return ((had_burst > 0) & below_mean).astype(float)


def f21_dvit_292_dv_climax_signature_count_252d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of (z>3 AND price at 252d-high) — buying-climax events count."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    flag = ((z > 3.0) & (high >= rmax)).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_293_dv_climax_then_distribution_combined_252d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Climax-then-distribution: count of bars where (z>3 + price-at-high) was followed within 21d by a $-vol distribution day."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    climax = (z > 3.0) & (high >= rmax)
    pc = close.pct_change()
    dist_day = (pc < -0.002) & (z > 0)
    climax_recent = climax.shift(1).rolling(MDAYS, min_periods=1).max().fillna(0.0)
    return ((climax_recent > 0) & dist_day).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_294_dv_intensity_persistence_score(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d sum of (z>1) AND (z>1 prior day) — persistent high-intensity"""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    persist = ((z > 1.0) & (z.shift(1) > 1.0)).astype(float)
    return persist.rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_295_dv_extreme_pct_rank_persistence_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where dv pct rank(252d) > 0.95 — sustained extreme intensity."""
    dv = _dollar_vol(close, volume)
    pr = _rolling_pct_rank(dv, YDAYS)
    return (pr > 0.95).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_296_dv_intensity_zscore_diff_at_high_minus_overall(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean z(log_dv, 252d) at 252d-high bars minus mean z overall in 252d — intensity premium at price peaks."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_high = z.where(high >= rmax, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    overall = z.rolling(YDAYS, min_periods=QDAYS).mean()
    return at_high - overall


def f21_dvit_297_dv_silent_distribution_score_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where pr(log_dv,252d) < 0.5 AND close pct_change < -0.5% — silent down."""
    dv = _dollar_vol(close, volume)
    pr = _rolling_pct_rank(dv, YDAYS)
    pc = close.pct_change()
    return ((pr < 0.5) & (pc < -0.005)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_298_dv_pre_breakdown_dryup_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when close in top decile of 252d range AND dv pct_rank(252d) < 0.30 AND price slope(21d) > 0 — silent topping."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rp = _safe_div(close - rmin, rmax - rmin)
    dv = _dollar_vol(close, volume)
    pr = _rolling_pct_rank(dv, YDAYS)
    slope = _rolling_slope(close, MDAYS)
    return ((rp >= 0.90) & (pr < 0.30) & (slope > 0)).astype(float)


def f21_dvit_299_dv_pre_breakdown_dryup_dwell_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d fraction of bars in silent-topping state (per f21_dvit_298)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rp = _safe_div(close - rmin, rmax - rmin)
    dv = _dollar_vol(close, volume)
    pr = _rolling_pct_rank(dv, YDAYS)
    slope = _rolling_slope(close, MDAYS)
    return ((rp >= 0.90) & (pr < 0.30) & (slope > 0)).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f21_dvit_300_dv_master_distribution_intensity_score(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Master composite: weighted sum of {distribution-day cluster, exhaustion, post-burst-failure, dryup composite, silent-topping}."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    pc = close.pct_change()
    dd = ((pc < -0.002) & (z > 0)).astype(float)
    dd_cluster = (dd.rolling(25, min_periods=10).sum() >= 4).astype(float)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    burst_in_21d = (z > 3.0).astype(float).rolling(MDAYS, min_periods=WDAYS).max()
    is_peak_in_5d = (high >= rmax).astype(float).rolling(WDAYS, min_periods=1).max()
    slope = _rolling_slope(close, MDAYS)
    exhaustion = ((burst_in_21d > 0) & (is_peak_in_5d > 0) & (slope < 0)).astype(float)
    dv = _dollar_vol(close, volume)
    below_mean = dv < dv.rolling(YDAYS, min_periods=QDAYS).mean()
    post_burst_fail = ((burst_in_21d > 0) & below_mean).astype(float)
    hl_spread = (high - low) / close
    sp_q75 = _rolling_quantile(hl_spread, YDAYS, 0.75)
    ar = _safe_log(close).diff().abs()
    amihud = _safe_div(ar, dv)
    am_q75 = _rolling_quantile(amihud, YDAYS, 0.75)
    dryup_score = ((z < -1.0).astype(float) + (hl_spread > sp_q75).astype(float) + (amihud > am_q75).astype(float))
    pr = _rolling_pct_rank(dv, YDAYS)
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rp = _safe_div(close - rmin, rmax - rmin)
    silent_top = ((rp >= 0.90) & (pr < 0.30) & (slope > 0)).astype(float)
    return dd_cluster + 2.0 * exhaustion + 1.5 * post_burst_fail + dryup_score / 3.0 + 2.0 * silent_top


def f21_dvit_226_dv_distribution_day_indicator_d3(close, volume):
    return f21_dvit_226_dv_distribution_day_indicator(close, volume).diff().diff().diff()


def f21_dvit_227_dv_distribution_day_count_25d_d3(close, volume):
    return f21_dvit_227_dv_distribution_day_count_25d(close, volume).diff().diff().diff()


def f21_dvit_228_dv_distribution_day_count_63d_d3(close, volume):
    return f21_dvit_228_dv_distribution_day_count_63d(close, volume).diff().diff().diff()


def f21_dvit_229_dv_distribution_severity_252d_d3(close, volume):
    return f21_dvit_229_dv_distribution_severity_252d(close, volume).diff().diff().diff()


def f21_dvit_230_dv_accumulation_day_indicator_d3(close, volume):
    return f21_dvit_230_dv_accumulation_day_indicator(close, volume).diff().diff().diff()


def f21_dvit_231_dv_distribution_to_accumulation_ratio_63d_d3(close, volume):
    return f21_dvit_231_dv_distribution_to_accumulation_ratio_63d(close, volume).diff().diff().diff()


def f21_dvit_232_dv_distribution_days_cluster_5d_indicator_d3(close, volume):
    return f21_dvit_232_dv_distribution_days_cluster_5d_indicator(close, volume).diff().diff().diff()


def f21_dvit_233_dv_distribution_strict_high_dv_indicator_d3(close, volume):
    return f21_dvit_233_dv_distribution_strict_high_dv_indicator(close, volume).diff().diff().diff()


def f21_dvit_234_dv_distribution_strict_count_252d_d3(close, volume):
    return f21_dvit_234_dv_distribution_strict_count_252d(close, volume).diff().diff().diff()


def f21_dvit_235_consec_dv_distribution_days_streak_d3(close, volume):
    return f21_dvit_235_consec_dv_distribution_days_streak(close, volume).diff().diff().diff()


def f21_dvit_236_dv_running_drawdown_pct_252d_d3(close, volume):
    return f21_dvit_236_dv_running_drawdown_pct_252d(close, volume).diff().diff().diff()


def f21_dvit_237_dv_running_drawdown_log_252d_d3(close, volume):
    return f21_dvit_237_dv_running_drawdown_log_252d(close, volume).diff().diff().diff()


def f21_dvit_238_dv_drawdown_severity_252d_mean_d3(close, volume):
    return f21_dvit_238_dv_drawdown_severity_252d_mean(close, volume).diff().diff().diff()


def f21_dvit_239_dv_drawdown_time_below_minus50pct_252d_d3(close, volume):
    return f21_dvit_239_dv_drawdown_time_below_minus50pct_252d(close, volume).diff().diff().diff()


def f21_dvit_240_dv_drawdown_time_below_minus80pct_252d_d3(close, volume):
    return f21_dvit_240_dv_drawdown_time_below_minus80pct_252d(close, volume).diff().diff().diff()


def f21_dvit_241_dv_drawdown_recovery_indicator_d3(close, volume):
    return f21_dvit_241_dv_drawdown_recovery_indicator(close, volume).diff().diff().diff()


def f21_dvit_242_dv_drawdown_recovery_count_252d_d3(close, volume):
    return f21_dvit_242_dv_drawdown_recovery_count_252d(close, volume).diff().diff().diff()


def f21_dvit_243_dv_max_drawdown_in_252d_d3(close, volume):
    return f21_dvit_243_dv_max_drawdown_in_252d(close, volume).diff().diff().diff()


def f21_dvit_244_dv_drawdown_skew_252d_d3(close, volume):
    return f21_dvit_244_dv_drawdown_skew_252d(close, volume).diff().diff().diff()


def f21_dvit_245_dv_drawdown_dwell_below_zero_252d_d3(close, volume):
    return f21_dvit_245_dv_drawdown_dwell_below_zero_252d(close, volume).diff().diff().diff()


def f21_dvit_246_haar_wavelet_level1_logdv_252d_d3(close, volume):
    return f21_dvit_246_haar_wavelet_level1_logdv_252d(close, volume).diff().diff().diff()


def f21_dvit_247_haar_wavelet_level2_logdv_252d_d3(close, volume):
    return f21_dvit_247_haar_wavelet_level2_logdv_252d(close, volume).diff().diff().diff()


def f21_dvit_248_haar_wavelet_level3_logdv_252d_d3(close, volume):
    return f21_dvit_248_haar_wavelet_level3_logdv_252d(close, volume).diff().diff().diff()


def f21_dvit_249_dv_wavelet_low_to_high_ratio_252d_d3(close, volume):
    return f21_dvit_249_dv_wavelet_low_to_high_ratio_252d(close, volume).diff().diff().diff()


def f21_dvit_250_dv_smooth_minus_raw_zscore_252d_d3(close, volume):
    return f21_dvit_250_dv_smooth_minus_raw_zscore_252d(close, volume).diff().diff().diff()


def f21_dvit_251_dv_ema_diff_21_63_d3(close, volume):
    return f21_dvit_251_dv_ema_diff_21_63(close, volume).diff().diff().diff()


def f21_dvit_252_dv_ema_diff_63_252_d3(close, volume):
    return f21_dvit_252_dv_ema_diff_63_252(close, volume).diff().diff().diff()


def f21_dvit_253_dv_multi_horizon_zscore_aggregate_d3(close, volume):
    return f21_dvit_253_dv_multi_horizon_zscore_aggregate(close, volume).diff().diff().diff()


def f21_dvit_254_dv_multi_horizon_zscore_dispersion_d3(close, volume):
    return f21_dvit_254_dv_multi_horizon_zscore_dispersion(close, volume).diff().diff().diff()


def f21_dvit_255_dv_hp_filter_residual_std_252d_d3(close, volume):
    return f21_dvit_255_dv_hp_filter_residual_std_252d(close, volume).diff().diff().diff()


def f21_dvit_256_mi_logdv_logreturn_63d_d3(close, volume):
    return f21_dvit_256_mi_logdv_logreturn_63d(close, volume).diff().diff().diff()


def f21_dvit_257_mi_logdv_logreturn_252d_d3(close, volume):
    return f21_dvit_257_mi_logdv_logreturn_252d(close, volume).diff().diff().diff()


def f21_dvit_258_mi_logdv_lagged_logreturn_63d_d3(close, volume):
    return f21_dvit_258_mi_logdv_lagged_logreturn_63d(close, volume).diff().diff().diff()


def f21_dvit_259_mi_change_63_minus_252_d3(close, volume):
    return f21_dvit_259_mi_change_63_minus_252(close, volume).diff().diff().diff()


def f21_dvit_260_conditional_entropy_dv_given_return_252d_d3(close, volume):
    return f21_dvit_260_conditional_entropy_dv_given_return_252d(close, volume).diff().diff().diff()


def f21_dvit_261_dv_information_share_252d_d3(close, volume):
    return f21_dvit_261_dv_information_share_252d(close, volume).diff().diff().diff()


def f21_dvit_262_mi_logdv_abs_open_close_63d_d3(open, close, volume):
    return f21_dvit_262_mi_logdv_abs_open_close_63d(open, close, volume).diff().diff().diff()


def f21_dvit_263_dv_kl_divergence_recent_vs_baseline_252d_d3(close, volume):
    return f21_dvit_263_dv_kl_divergence_recent_vs_baseline_252d(close, volume).diff().diff().diff()


def f21_dvit_264_dv_joint_entropy_logdv_logret_252d_d3(close, volume):
    return f21_dvit_264_dv_joint_entropy_logdv_logret_252d(close, volume).diff().diff().diff()


def f21_dvit_265_dv_shannon_entropy_signed_dv_252d_d3(close, volume):
    return f21_dvit_265_dv_shannon_entropy_signed_dv_252d(close, volume).diff().diff().diff()


def f21_dvit_266_amihud_proxy_252d_mean_d3(close, volume):
    return f21_dvit_266_amihud_proxy_252d_mean(close, volume).diff().diff().diff()


def f21_dvit_267_amihud_proxy_zscore_252d_d3(close, volume):
    return f21_dvit_267_amihud_proxy_zscore_252d(close, volume).diff().diff().diff()


def f21_dvit_268_dv_per_atr_zscore_252d_v2_d3(high, low, close, volume):
    return f21_dvit_268_dv_per_atr_zscore_252d_v2(high, low, close, volume).diff().diff().diff()


def f21_dvit_269_kyle_lambda_proxy_252d_d3(close, volume):
    return f21_dvit_269_kyle_lambda_proxy_252d(close, volume).diff().diff().diff()


def f21_dvit_270_dv_per_volatility_252d_mean_d3(close, volume):
    return f21_dvit_270_dv_per_volatility_252d_mean(close, volume).diff().diff().diff()


def f21_dvit_271_dv_capacity_residual_252d_d3(close, volume):
    return f21_dvit_271_dv_capacity_residual_252d(close, volume).diff().diff().diff()


def f21_dvit_272_dv_per_corwin_schultz_spread_252d_mean_d3(high, low, close, volume):
    return f21_dvit_272_dv_per_corwin_schultz_spread_252d_mean(high, low, close, volume).diff().diff().diff()


def f21_dvit_273_liquidity_premium_proxy_252d_d3(high, low, close, volume):
    return f21_dvit_273_liquidity_premium_proxy_252d(high, low, close, volume).diff().diff().diff()


def f21_dvit_274_dv_capacity_shrinkage_indicator_252d_d3(close, volume):
    return f21_dvit_274_dv_capacity_shrinkage_indicator_252d(close, volume).diff().diff().diff()


def f21_dvit_275_dv_capacity_shrinkage_count_63d_d3(close, volume):
    return f21_dvit_275_dv_capacity_shrinkage_count_63d(close, volume).diff().diff().diff()


def f21_dvit_276_dv_top_decile_threshold_change_252d_d3(close, volume):
    return f21_dvit_276_dv_top_decile_threshold_change_252d(close, volume).diff().diff().diff()


def f21_dvit_277_dv_top_decile_count_252d_d3(close, volume):
    return f21_dvit_277_dv_top_decile_count_252d(close, volume).diff().diff().diff()


def f21_dvit_278_dv_concentration_in_top_decile_share_252d_d3(close, volume):
    return f21_dvit_278_dv_concentration_in_top_decile_share_252d(close, volume).diff().diff().diff()


def f21_dvit_279_dv_concentration_in_top_percentile_share_252d_d3(close, volume):
    return f21_dvit_279_dv_concentration_in_top_percentile_share_252d(close, volume).diff().diff().diff()


def f21_dvit_280_dv_concentration_change_252d_vs_504d_d3(close, volume):
    return f21_dvit_280_dv_concentration_change_252d_vs_504d(close, volume).diff().diff().diff()


def f21_dvit_281_dv_lorenz_area_252d_d3(close, volume):
    return f21_dvit_281_dv_lorenz_area_252d(close, volume).diff().diff().diff()


def f21_dvit_282_dv_kurtosis_signal_extreme_252d_d3(close, volume):
    return f21_dvit_282_dv_kurtosis_signal_extreme_252d(close, volume).diff().diff().diff()


def f21_dvit_283_dv_concentration_pareto_alpha_252d_d3(close, volume):
    return f21_dvit_283_dv_concentration_pareto_alpha_252d(close, volume).diff().diff().diff()


def f21_dvit_284_dv_gini_change_252_vs_504_d3(close, volume):
    return f21_dvit_284_dv_gini_change_252_vs_504(close, volume).diff().diff().diff()


def f21_dvit_285_dv_top_decile_streak_252d_d3(close, volume):
    return f21_dvit_285_dv_top_decile_streak_252d(close, volume).diff().diff().diff()


def f21_dvit_286_dv_intensity_composite_score_252d_v2_d3(close, volume):
    return f21_dvit_286_dv_intensity_composite_score_252d_v2(close, volume).diff().diff().diff()


def f21_dvit_287_dv_exhaustion_score_252d_d3(high, close, volume):
    return f21_dvit_287_dv_exhaustion_score_252d(high, close, volume).diff().diff().diff()


def f21_dvit_288_dv_post_climax_decay_252d_d3(close, volume):
    return f21_dvit_288_dv_post_climax_decay_252d(close, volume).diff().diff().diff()


def f21_dvit_289_dv_active_silent_balance_252d_d3(close, volume):
    return f21_dvit_289_dv_active_silent_balance_252d(close, volume).diff().diff().diff()


def f21_dvit_290_dv_burst_dryup_oscillation_252d_d3(close, volume):
    return f21_dvit_290_dv_burst_dryup_oscillation_252d(close, volume).diff().diff().diff()


def f21_dvit_291_dv_post_burst_failure_to_recover_indicator_d3(close, volume):
    return f21_dvit_291_dv_post_burst_failure_to_recover_indicator(close, volume).diff().diff().diff()


def f21_dvit_292_dv_climax_signature_count_252d_d3(high, close, volume):
    return f21_dvit_292_dv_climax_signature_count_252d(high, close, volume).diff().diff().diff()


def f21_dvit_293_dv_climax_then_distribution_combined_252d_d3(high, close, volume):
    return f21_dvit_293_dv_climax_then_distribution_combined_252d(high, close, volume).diff().diff().diff()


def f21_dvit_294_dv_intensity_persistence_score_d3(close, volume):
    return f21_dvit_294_dv_intensity_persistence_score(close, volume).diff().diff().diff()


def f21_dvit_295_dv_extreme_pct_rank_persistence_252d_d3(close, volume):
    return f21_dvit_295_dv_extreme_pct_rank_persistence_252d(close, volume).diff().diff().diff()


def f21_dvit_296_dv_intensity_zscore_diff_at_high_minus_overall_d3(high, close, volume):
    return f21_dvit_296_dv_intensity_zscore_diff_at_high_minus_overall(high, close, volume).diff().diff().diff()


def f21_dvit_297_dv_silent_distribution_score_252d_d3(close, volume):
    return f21_dvit_297_dv_silent_distribution_score_252d(close, volume).diff().diff().diff()


def f21_dvit_298_dv_pre_breakdown_dryup_indicator_d3(high, low, close, volume):
    return f21_dvit_298_dv_pre_breakdown_dryup_indicator(high, low, close, volume).diff().diff().diff()


def f21_dvit_299_dv_pre_breakdown_dryup_dwell_252d_d3(high, low, close, volume):
    return f21_dvit_299_dv_pre_breakdown_dryup_dwell_252d(high, low, close, volume).diff().diff().diff()


def f21_dvit_300_dv_master_distribution_intensity_score_d3(high, low, close, volume):
    return f21_dvit_300_dv_master_distribution_intensity_score(high, low, close, volume).diff().diff().diff()


# ============================================================
#                         REGISTRY 226-300
# ============================================================


DOLLAR_VOLUME_INTENSITY_D3_REGISTRY_226_300 = {
    "f21_dvit_226_dv_distribution_day_indicator_d3": {"inputs": ["close", "volume"], "func": f21_dvit_226_dv_distribution_day_indicator_d3},
    "f21_dvit_227_dv_distribution_day_count_25d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_227_dv_distribution_day_count_25d_d3},
    "f21_dvit_228_dv_distribution_day_count_63d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_228_dv_distribution_day_count_63d_d3},
    "f21_dvit_229_dv_distribution_severity_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_229_dv_distribution_severity_252d_d3},
    "f21_dvit_230_dv_accumulation_day_indicator_d3": {"inputs": ["close", "volume"], "func": f21_dvit_230_dv_accumulation_day_indicator_d3},
    "f21_dvit_231_dv_distribution_to_accumulation_ratio_63d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_231_dv_distribution_to_accumulation_ratio_63d_d3},
    "f21_dvit_232_dv_distribution_days_cluster_5d_indicator_d3": {"inputs": ["close", "volume"], "func": f21_dvit_232_dv_distribution_days_cluster_5d_indicator_d3},
    "f21_dvit_233_dv_distribution_strict_high_dv_indicator_d3": {"inputs": ["close", "volume"], "func": f21_dvit_233_dv_distribution_strict_high_dv_indicator_d3},
    "f21_dvit_234_dv_distribution_strict_count_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_234_dv_distribution_strict_count_252d_d3},
    "f21_dvit_235_consec_dv_distribution_days_streak_d3": {"inputs": ["close", "volume"], "func": f21_dvit_235_consec_dv_distribution_days_streak_d3},
    "f21_dvit_236_dv_running_drawdown_pct_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_236_dv_running_drawdown_pct_252d_d3},
    "f21_dvit_237_dv_running_drawdown_log_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_237_dv_running_drawdown_log_252d_d3},
    "f21_dvit_238_dv_drawdown_severity_252d_mean_d3": {"inputs": ["close", "volume"], "func": f21_dvit_238_dv_drawdown_severity_252d_mean_d3},
    "f21_dvit_239_dv_drawdown_time_below_minus50pct_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_239_dv_drawdown_time_below_minus50pct_252d_d3},
    "f21_dvit_240_dv_drawdown_time_below_minus80pct_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_240_dv_drawdown_time_below_minus80pct_252d_d3},
    "f21_dvit_241_dv_drawdown_recovery_indicator_d3": {"inputs": ["close", "volume"], "func": f21_dvit_241_dv_drawdown_recovery_indicator_d3},
    "f21_dvit_242_dv_drawdown_recovery_count_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_242_dv_drawdown_recovery_count_252d_d3},
    "f21_dvit_243_dv_max_drawdown_in_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_243_dv_max_drawdown_in_252d_d3},
    "f21_dvit_244_dv_drawdown_skew_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_244_dv_drawdown_skew_252d_d3},
    "f21_dvit_245_dv_drawdown_dwell_below_zero_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_245_dv_drawdown_dwell_below_zero_252d_d3},
    "f21_dvit_246_haar_wavelet_level1_logdv_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_246_haar_wavelet_level1_logdv_252d_d3},
    "f21_dvit_247_haar_wavelet_level2_logdv_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_247_haar_wavelet_level2_logdv_252d_d3},
    "f21_dvit_248_haar_wavelet_level3_logdv_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_248_haar_wavelet_level3_logdv_252d_d3},
    "f21_dvit_249_dv_wavelet_low_to_high_ratio_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_249_dv_wavelet_low_to_high_ratio_252d_d3},
    "f21_dvit_250_dv_smooth_minus_raw_zscore_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_250_dv_smooth_minus_raw_zscore_252d_d3},
    "f21_dvit_251_dv_ema_diff_21_63_d3": {"inputs": ["close", "volume"], "func": f21_dvit_251_dv_ema_diff_21_63_d3},
    "f21_dvit_252_dv_ema_diff_63_252_d3": {"inputs": ["close", "volume"], "func": f21_dvit_252_dv_ema_diff_63_252_d3},
    "f21_dvit_253_dv_multi_horizon_zscore_aggregate_d3": {"inputs": ["close", "volume"], "func": f21_dvit_253_dv_multi_horizon_zscore_aggregate_d3},
    "f21_dvit_254_dv_multi_horizon_zscore_dispersion_d3": {"inputs": ["close", "volume"], "func": f21_dvit_254_dv_multi_horizon_zscore_dispersion_d3},
    "f21_dvit_255_dv_hp_filter_residual_std_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_255_dv_hp_filter_residual_std_252d_d3},
    "f21_dvit_256_mi_logdv_logreturn_63d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_256_mi_logdv_logreturn_63d_d3},
    "f21_dvit_257_mi_logdv_logreturn_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_257_mi_logdv_logreturn_252d_d3},
    "f21_dvit_258_mi_logdv_lagged_logreturn_63d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_258_mi_logdv_lagged_logreturn_63d_d3},
    "f21_dvit_259_mi_change_63_minus_252_d3": {"inputs": ["close", "volume"], "func": f21_dvit_259_mi_change_63_minus_252_d3},
    "f21_dvit_260_conditional_entropy_dv_given_return_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_260_conditional_entropy_dv_given_return_252d_d3},
    "f21_dvit_261_dv_information_share_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_261_dv_information_share_252d_d3},
    "f21_dvit_262_mi_logdv_abs_open_close_63d_d3": {"inputs": ["open", "close", "volume"], "func": f21_dvit_262_mi_logdv_abs_open_close_63d_d3},
    "f21_dvit_263_dv_kl_divergence_recent_vs_baseline_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_263_dv_kl_divergence_recent_vs_baseline_252d_d3},
    "f21_dvit_264_dv_joint_entropy_logdv_logret_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_264_dv_joint_entropy_logdv_logret_252d_d3},
    "f21_dvit_265_dv_shannon_entropy_signed_dv_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_265_dv_shannon_entropy_signed_dv_252d_d3},
    "f21_dvit_266_amihud_proxy_252d_mean_d3": {"inputs": ["close", "volume"], "func": f21_dvit_266_amihud_proxy_252d_mean_d3},
    "f21_dvit_267_amihud_proxy_zscore_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_267_amihud_proxy_zscore_252d_d3},
    "f21_dvit_268_dv_per_atr_zscore_252d_v2_d3": {"inputs": ["high", "low", "close", "volume"], "func": f21_dvit_268_dv_per_atr_zscore_252d_v2_d3},
    "f21_dvit_269_kyle_lambda_proxy_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_269_kyle_lambda_proxy_252d_d3},
    "f21_dvit_270_dv_per_volatility_252d_mean_d3": {"inputs": ["close", "volume"], "func": f21_dvit_270_dv_per_volatility_252d_mean_d3},
    "f21_dvit_271_dv_capacity_residual_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_271_dv_capacity_residual_252d_d3},
    "f21_dvit_272_dv_per_corwin_schultz_spread_252d_mean_d3": {"inputs": ["high", "low", "close", "volume"], "func": f21_dvit_272_dv_per_corwin_schultz_spread_252d_mean_d3},
    "f21_dvit_273_liquidity_premium_proxy_252d_d3": {"inputs": ["high", "low", "close", "volume"], "func": f21_dvit_273_liquidity_premium_proxy_252d_d3},
    "f21_dvit_274_dv_capacity_shrinkage_indicator_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_274_dv_capacity_shrinkage_indicator_252d_d3},
    "f21_dvit_275_dv_capacity_shrinkage_count_63d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_275_dv_capacity_shrinkage_count_63d_d3},
    "f21_dvit_276_dv_top_decile_threshold_change_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_276_dv_top_decile_threshold_change_252d_d3},
    "f21_dvit_277_dv_top_decile_count_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_277_dv_top_decile_count_252d_d3},
    "f21_dvit_278_dv_concentration_in_top_decile_share_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_278_dv_concentration_in_top_decile_share_252d_d3},
    "f21_dvit_279_dv_concentration_in_top_percentile_share_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_279_dv_concentration_in_top_percentile_share_252d_d3},
    "f21_dvit_280_dv_concentration_change_252d_vs_504d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_280_dv_concentration_change_252d_vs_504d_d3},
    "f21_dvit_281_dv_lorenz_area_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_281_dv_lorenz_area_252d_d3},
    "f21_dvit_282_dv_kurtosis_signal_extreme_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_282_dv_kurtosis_signal_extreme_252d_d3},
    "f21_dvit_283_dv_concentration_pareto_alpha_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_283_dv_concentration_pareto_alpha_252d_d3},
    "f21_dvit_284_dv_gini_change_252_vs_504_d3": {"inputs": ["close", "volume"], "func": f21_dvit_284_dv_gini_change_252_vs_504_d3},
    "f21_dvit_285_dv_top_decile_streak_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_285_dv_top_decile_streak_252d_d3},
    "f21_dvit_286_dv_intensity_composite_score_252d_v2_d3": {"inputs": ["close", "volume"], "func": f21_dvit_286_dv_intensity_composite_score_252d_v2_d3},
    "f21_dvit_287_dv_exhaustion_score_252d_d3": {"inputs": ["high", "close", "volume"], "func": f21_dvit_287_dv_exhaustion_score_252d_d3},
    "f21_dvit_288_dv_post_climax_decay_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_288_dv_post_climax_decay_252d_d3},
    "f21_dvit_289_dv_active_silent_balance_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_289_dv_active_silent_balance_252d_d3},
    "f21_dvit_290_dv_burst_dryup_oscillation_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_290_dv_burst_dryup_oscillation_252d_d3},
    "f21_dvit_291_dv_post_burst_failure_to_recover_indicator_d3": {"inputs": ["close", "volume"], "func": f21_dvit_291_dv_post_burst_failure_to_recover_indicator_d3},
    "f21_dvit_292_dv_climax_signature_count_252d_d3": {"inputs": ["high", "close", "volume"], "func": f21_dvit_292_dv_climax_signature_count_252d_d3},
    "f21_dvit_293_dv_climax_then_distribution_combined_252d_d3": {"inputs": ["high", "close", "volume"], "func": f21_dvit_293_dv_climax_then_distribution_combined_252d_d3},
    "f21_dvit_294_dv_intensity_persistence_score_d3": {"inputs": ["close", "volume"], "func": f21_dvit_294_dv_intensity_persistence_score_d3},
    "f21_dvit_295_dv_extreme_pct_rank_persistence_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_295_dv_extreme_pct_rank_persistence_252d_d3},
    "f21_dvit_296_dv_intensity_zscore_diff_at_high_minus_overall_d3": {"inputs": ["high", "close", "volume"], "func": f21_dvit_296_dv_intensity_zscore_diff_at_high_minus_overall_d3},
    "f21_dvit_297_dv_silent_distribution_score_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_297_dv_silent_distribution_score_252d_d3},
    "f21_dvit_298_dv_pre_breakdown_dryup_indicator_d3": {"inputs": ["high", "low", "close", "volume"], "func": f21_dvit_298_dv_pre_breakdown_dryup_indicator_d3},
    "f21_dvit_299_dv_pre_breakdown_dryup_dwell_252d_d3": {"inputs": ["high", "low", "close", "volume"], "func": f21_dvit_299_dv_pre_breakdown_dryup_dwell_252d_d3},
    "f21_dvit_300_dv_master_distribution_intensity_score_d3": {"inputs": ["high", "low", "close", "volume"], "func": f21_dvit_300_dv_master_distribution_intensity_score_d3},
}
