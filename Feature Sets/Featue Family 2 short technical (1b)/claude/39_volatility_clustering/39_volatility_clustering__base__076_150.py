"""volatility_clustering base features 076-150 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __base__001_075.py. Each feature
encodes a *different concept* in the vol-clustering / GARCH-style theme:
EGARCH leverage-effect, Hill-on-σ tail, vol run-length, vol drift, HAR-RV
components, vol-of-vol asymmetry, McLeod-Li/ARCH-LM/Hurst clustering tests,
percentile-rank σ-regime, vol-momentum, cross-lag σ-corr, vol-volume joint
clustering, vol-forecast instability, misc clustering descriptors.

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


def _log_ret(close):
    return _safe_log(close).diff()


def _rolling_sigma(r, n):
    return r.rolling(n, min_periods=max(n // 3, 2)).std()


def _ewma_vol(r, lam):
    return np.sqrt((r ** 2).ewm(alpha=1.0 - lam, min_periods=21).mean())


# ============================================================
# Bucket L — EGARCH-style asymmetric vol (076-081)
# ============================================================

def f39_vclu_076_neg_vs_pos_post_ret_sigma_63d(close: pd.Series) -> pd.Series:
    """Ratio of σ following negative r_{t-1} to σ following positive r_{t-1} over 63d."""
    r = _log_ret(close)
    after_neg = r.where(r.shift(1) < 0, np.nan)
    after_pos = r.where(r.shift(1) > 0, np.nan)
    return _safe_div(after_neg.rolling(QDAYS, min_periods=MDAYS).std(),
                     after_pos.rolling(QDAYS, min_periods=MDAYS).std())


def f39_vclu_077_neg_vs_pos_post_ret_sigma_252d(close: pd.Series) -> pd.Series:
    """Ratio of σ following negative r_{t-1} to σ following positive r_{t-1} over 252d."""
    r = _log_ret(close)
    after_neg = r.where(r.shift(1) < 0, np.nan)
    after_pos = r.where(r.shift(1) > 0, np.nan)
    return _safe_div(after_neg.rolling(YDAYS, min_periods=QDAYS).std(),
                     after_pos.rolling(YDAYS, min_periods=QDAYS).std())


def f39_vclu_078_corr_sigma_with_lag_sign_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d corr(σ_21d_t, sign(r_{t-1})) — leverage-effect proxy."""
    r = _log_ret(close)
    s = _rolling_sigma(r, MDAYS)
    return s.rolling(YDAYS, min_periods=QDAYS).corr(np.sign(r).shift(1))


def f39_vclu_079_slope_sigma_on_signed_lag_ret_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d OLS slope of σ_21d on signed r_{t-1} — explicit leverage regression."""
    r = _log_ret(close)
    s = _rolling_sigma(r, MDAYS)
    lag = r.shift(1)
    cov = s.rolling(YDAYS, min_periods=QDAYS).cov(lag)
    var = lag.rolling(YDAYS, min_periods=QDAYS).var()
    return _safe_div(cov, var)


def f39_vclu_080_leverage_cov_rsq_lag_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d β of r²_t on r_{t-1}: cov(r²_t, r_{t-1}) / var(r_{t-1}) — leverage effect."""
    r = _log_ret(close)
    r2 = r ** 2
    lag = r.shift(1)
    cov = r2.rolling(YDAYS, min_periods=QDAYS).cov(lag)
    var = lag.rolling(YDAYS, min_periods=QDAYS).var()
    return _safe_div(cov, var)


def f39_vclu_081_nic_asymmetry_var_neg_minus_pos_252d(close: pd.Series) -> pd.Series:
    """News-impact asymmetry: (var(r|r_lag<0) − var(r|r_lag>0)) / total var over 252d."""
    r = _log_ret(close)
    after_neg = r.where(r.shift(1) < 0, np.nan)
    after_pos = r.where(r.shift(1) > 0, np.nan)
    v_neg = after_neg.rolling(YDAYS, min_periods=QDAYS).var()
    v_pos = after_pos.rolling(YDAYS, min_periods=QDAYS).var()
    v_tot = r.rolling(YDAYS, min_periods=QDAYS).var()
    return _safe_div(v_neg - v_pos, v_tot)


# ============================================================
# Bucket M — Hill estimator on σ-distribution (082-085)
# ============================================================

def _hill_estimator(window: np.ndarray, top_frac: float) -> float:
    arr = window[~np.isnan(window)]
    if len(arr) < 30:
        return np.nan
    k = max(int(len(arr) * top_frac), 5)
    top = np.sort(arr)[-k:]
    th = top[0]
    if th <= 0:
        return np.nan
    lg = np.log(top / th)
    val = lg[1:].mean() if len(lg) > 1 else np.nan
    return float(val) if np.isfinite(val) and val > 0 else np.nan


def f39_vclu_082_hill_sigma21_top10_504d(close: pd.Series) -> pd.Series:
    """Hill estimator (top 10%) of σ_21d distribution over 504d — vol-tail thickness."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return s.rolling(DDAYS_2Y, min_periods=YDAYS).apply(lambda w: _hill_estimator(w, 0.10), raw=True)


def f39_vclu_083_hill_sigma21_top5_1260d(close: pd.Series) -> pd.Series:
    """Hill estimator (top 5%) of σ_21d distribution over 1260d — extreme vol-tail thickness."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return s.rolling(DDAYS_5Y, min_periods=DDAYS_2Y).apply(lambda w: _hill_estimator(w, 0.05), raw=True)


def f39_vclu_084_p99_over_p50_sigma21_252d(close: pd.Series) -> pd.Series:
    """Ratio p99(σ_21d) / p50(σ_21d) over 252d — vol-distribution skew proxy."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p99 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.99)
    p50 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.50)
    return _safe_div(p99, p50)


def f39_vclu_085_max_over_mean_sigma21_252d(close: pd.Series) -> pd.Series:
    """Vol-peak ratio: max(σ_21d) / mean(σ_21d) over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return _safe_div(s.rolling(YDAYS, min_periods=QDAYS).max(),
                     s.rolling(YDAYS, min_periods=QDAYS).mean())


# ============================================================
# Bucket N — Vol clustering via run-length (086-090)
# ============================================================

def _longest_run(w: np.ndarray) -> float:
    m = 0; c = 0
    for v in w:
        if v > 0.5:
            c += 1; m = c if c > m else m
        else:
            c = 0
    return float(m)


def f39_vclu_086_longest_run_sigma_above_median_252d(close: pd.Series) -> pd.Series:
    """Longest run of σ_21d above its trailing-252d median within 252d window."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    med = s.rolling(YDAYS, min_periods=QDAYS).median()
    return (s > med).astype(float).fillna(0.0).rolling(YDAYS, min_periods=QDAYS).apply(_longest_run, raw=True)


def f39_vclu_087_longest_run_sigma_top_decile_252d(close: pd.Series) -> pd.Series:
    """Longest run of σ_21d in top decile of its trailing 252d distribution."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p90 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    return (s > p90).astype(float).fillna(0.0).rolling(YDAYS, min_periods=QDAYS).apply(_longest_run, raw=True)


def f39_vclu_088_run_length_entropy_252d(close: pd.Series) -> pd.Series:
    """Entropy of run-lengths in the (σ>median) binary sequence over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    med = s.rolling(YDAYS, min_periods=QDAYS).median()
    hi = (s > med).astype(float).fillna(0.0)

    def _ent(w):
        runs = []
        cur = 0
        for v in w:
            if v > 0.5:
                cur += 1
            elif cur > 0:
                runs.append(cur); cur = 0
        if cur > 0:
            runs.append(cur)
        if not runs:
            return np.nan
        arr = np.array(runs, dtype=float)
        p = arr / arr.sum()
        p = p[p > 0]
        return float(-(p * np.log(p)).sum())
    return hi.rolling(YDAYS, min_periods=QDAYS).apply(_ent, raw=True)


def f39_vclu_089_current_regime_run_length(close: pd.Series) -> pd.Series:
    """Length of current consecutive run of (σ_21d > median) or (σ_21d ≤ median), signed."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    med = s.rolling(YDAYS, min_periods=QDAYS).median()
    hi = (s > med).astype(int).fillna(0)
    arr = hi.values
    out = np.zeros(len(arr), dtype=float)
    cur = 0; cur_state = None
    for i, v in enumerate(arr):
        if cur_state is None or v != cur_state:
            cur = 1; cur_state = v
        else:
            cur += 1
        out[i] = cur if v == 1 else -cur
    return pd.Series(out, index=close.index)


def f39_vclu_090_regime_change_count_252d(close: pd.Series) -> pd.Series:
    """Number of high↔low σ regime changes (crossings of median) over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    med = s.rolling(YDAYS, min_periods=QDAYS).median()
    above = (s > med).astype(float).fillna(0.0)
    return above.diff().abs().rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket O — Vol seasonality / drift (091-096)
# ============================================================

def f39_vclu_091_slope_sigma21_63d(close: pd.Series) -> pd.Series:
    """Rolling 63d slope of σ_21d — multi-week vol drift."""
    return _rolling_slope(_rolling_sigma(_log_ret(close), MDAYS), QDAYS)


def f39_vclu_092_slope_sigma21_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d slope of σ_21d — annual vol drift."""
    return _rolling_slope(_rolling_sigma(_log_ret(close), MDAYS), YDAYS)


def f39_vclu_093_slope_log_sigma21_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d slope of log(σ_21d) — log-trend of vol."""
    return _rolling_slope(_safe_log(_rolling_sigma(_log_ret(close), MDAYS)), YDAYS)


def f39_vclu_094_vol_trend_velocity_63d(close: pd.Series) -> pd.Series:
    """Rolling 63d std of σ-trend (slope_63d of σ_21d) — velocity volatility."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    sl = _rolling_slope(s, QDAYS)
    return sl.rolling(QDAYS, min_periods=MDAYS).std()


def f39_vclu_095_vol_trend_sign_changes_252d(close: pd.Series) -> pd.Series:
    """Number of sign changes in 63d σ-trend over a 252d window."""
    sl = _rolling_slope(_rolling_sigma(_log_ret(close), MDAYS), QDAYS)
    sgn = np.sign(sl).fillna(0.0)
    return sgn.diff().abs().rolling(YDAYS, min_periods=QDAYS).sum()


def f39_vclu_096_range_of_sigma21_252d(close: pd.Series) -> pd.Series:
    """Annual range of σ_21d: max − min within trailing 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return s.rolling(YDAYS, min_periods=QDAYS).max() - s.rolling(YDAYS, min_periods=QDAYS).min()


# ============================================================
# Bucket P — HAR-RV components (097-101)
# ============================================================

def f39_vclu_097_har_daily_component(close: pd.Series) -> pd.Series:
    """HAR-RV daily component: yesterday's r² (single-bar realized variance)."""
    r = _log_ret(close)
    return (r ** 2).shift(1)


def f39_vclu_098_har_weekly_component(close: pd.Series) -> pd.Series:
    """HAR-RV weekly component: mean r² over past 5 bars (excluding today)."""
    r = _log_ret(close)
    return (r ** 2).rolling(WDAYS, min_periods=2).mean().shift(1)


def f39_vclu_099_har_monthly_component(close: pd.Series) -> pd.Series:
    """HAR-RV monthly component: mean r² over past 21 bars (excluding today)."""
    r = _log_ret(close)
    return (r ** 2).rolling(MDAYS, min_periods=WDAYS).mean().shift(1)


def f39_vclu_100_har_daily_over_monthly_ratio(close: pd.Series) -> pd.Series:
    """HAR component contribution: daily / monthly component (ratio)."""
    r = _log_ret(close)
    d = (r ** 2).shift(1)
    m = (r ** 2).rolling(MDAYS, min_periods=WDAYS).mean().shift(1)
    return _safe_div(d, m)


def f39_vclu_101_har_fixed_weight_forecast(close: pd.Series) -> pd.Series:
    """HAR fixed-weight forecast: 0.4·daily + 0.3·weekly + 0.3·monthly RV components."""
    r = _log_ret(close)
    d = (r ** 2).shift(1)
    w = (r ** 2).rolling(WDAYS, min_periods=2).mean().shift(1)
    m = (r ** 2).rolling(MDAYS, min_periods=WDAYS).mean().shift(1)
    return 0.4 * d + 0.3 * w + 0.3 * m


# ============================================================
# Bucket Q — Vol-of-vol asymmetry (102-105)
# ============================================================

def f39_vclu_102_vov_on_rising_sigma_252d(close: pd.Series) -> pd.Series:
    """σ-of-σ_21d on bars where σ_21d > σ_21d.shift(1) (rising-σ subset) over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    rising = s.where(s > s.shift(1), np.nan)
    return rising.rolling(YDAYS, min_periods=QDAYS).std()


def f39_vclu_103_vov_on_falling_sigma_252d(close: pd.Series) -> pd.Series:
    """σ-of-σ_21d on bars where σ_21d < σ_21d.shift(1) (falling-σ subset) over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    falling = s.where(s < s.shift(1), np.nan)
    return falling.rolling(YDAYS, min_periods=QDAYS).std()


def f39_vclu_104_vov_rising_over_falling_ratio_252d(close: pd.Series) -> pd.Series:
    """Ratio of vol-of-vol on rising-σ days / falling-σ days over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    rising = s.where(s > s.shift(1), np.nan)
    falling = s.where(s < s.shift(1), np.nan)
    return _safe_div(rising.rolling(YDAYS, min_periods=QDAYS).std(),
                     falling.rolling(YDAYS, min_periods=QDAYS).std())


def f39_vclu_105_skew_sigma_increments_252d(close: pd.Series) -> pd.Series:
    """Skew of σ_21d-increments (Δσ) over 252d — vol-jump asymmetry."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return s.diff().rolling(YDAYS, min_periods=QDAYS).skew()


# ============================================================
# Bucket R — Vol-clustering test stats (106-110)
# ============================================================

def f39_vclu_106_mcleod_li_stat_252d(close: pd.Series) -> pd.Series:
    """McLeod-Li statistic on r² over 252d (Ljung-Box on r² with lags 1..21)."""
    r2 = _log_ret(close) ** 2
    out = pd.Series(0.0, index=close.index)
    for k in range(1, MDAYS + 1):
        c = r2.rolling(YDAYS, min_periods=QDAYS).corr(r2.shift(k))
        out = out + (c ** 2) / (YDAYS - k)
    return YDAYS * (YDAYS + 2) * out


def f39_vclu_107_arch_lm_stat_252d(close: pd.Series) -> pd.Series:
    """Engle ARCH-LM proxy: rolling 252d R² from regressing r²_t on r²_{t-1} (squared corr)."""
    r2 = _log_ret(close) ** 2
    c = r2.rolling(YDAYS, min_periods=QDAYS).corr(r2.shift(1))
    return YDAYS * (c ** 2)


def f39_vclu_108_var_ratio_rsq_5_21_252d(close: pd.Series) -> pd.Series:
    """Variance ratio of r² between 5d and 21d aggregation windows over 252d."""
    r2 = _log_ret(close) ** 2
    v5 = r2.rolling(WDAYS, min_periods=2).sum().rolling(YDAYS, min_periods=QDAYS).var()
    v21 = r2.rolling(MDAYS, min_periods=WDAYS).sum().rolling(YDAYS, min_periods=QDAYS).var()
    return _safe_div(v5, v21) * (MDAYS / WDAYS)


def f39_vclu_109_hurst_rs_absret_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d R/S Hurst exponent of |log-ret| — long-memory test on absolute returns."""
    a = _log_ret(close).abs()

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
    return a.rolling(YDAYS, min_periods=QDAYS).apply(_rs, raw=True)


def f39_vclu_110_dfa_absret_252d(close: pd.Series) -> pd.Series:
    """Detrended fluctuation analysis exponent of |log-ret| over 252d (long-memory)."""
    a = _log_ret(close).abs()

    def _dfa(w):
        x = w[~np.isnan(w)]
        n = len(x)
        if n < 60:
            return np.nan
        y = (x - x.mean()).cumsum()
        scales = [4, 8, 16, 32]
        scales = [s for s in scales if s < n // 4]
        if len(scales) < 2:
            return np.nan
        F = []
        for s in scales:
            ns = n // s
            yres = y[:ns * s].reshape(ns, s)
            xb = np.arange(s, dtype=float)
            f_sum = 0.0
            for j in range(ns):
                p = np.polyfit(xb, yres[j], 1)
                trend = np.polyval(p, xb)
                f_sum += ((yres[j] - trend) ** 2).sum()
            F.append(np.sqrt(f_sum / (ns * s)))
        lx = np.log(scales); ly = np.log(F)
        xm = lx.mean(); ym = ly.mean()
        d = ((lx - xm) ** 2).sum()
        return float(((lx - xm) * (ly - ym)).sum() / d) if d > 0 else np.nan
    return a.rolling(YDAYS, min_periods=QDAYS).apply(_dfa, raw=True)


# ============================================================
# Bucket S — Cross-window σ percentile-rank regimes (111-116)
# ============================================================

def _pct_rank_window(s: pd.Series, n: int, min_periods: int) -> pd.Series:
    return s.rolling(n, min_periods=min_periods).apply(
        lambda w: float((w[-1] >= w).sum() / len(w)) if not np.isnan(w[-1]) else np.nan,
        raw=True,
    )


def f39_vclu_111_pctrank_sigma21_in_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of current σ_21d within own past 252d distribution."""
    return _pct_rank_window(_rolling_sigma(_log_ret(close), MDAYS), YDAYS, QDAYS)


def f39_vclu_112_pctrank_sigma21_in_504d(close: pd.Series) -> pd.Series:
    """Percentile rank of current σ_21d within own past 504d distribution."""
    return _pct_rank_window(_rolling_sigma(_log_ret(close), MDAYS), DDAYS_2Y, YDAYS)


def f39_vclu_113_pctrank_sigma21_in_1260d(close: pd.Series) -> pd.Series:
    """Percentile rank of current σ_21d within own past 1260d (5y) distribution."""
    return _pct_rank_window(_rolling_sigma(_log_ret(close), MDAYS), DDAYS_5Y, DDAYS_2Y)


def f39_vclu_114_pctrank_sigma63_in_1260d(close: pd.Series) -> pd.Series:
    """Percentile rank of current σ_63d within own past 1260d distribution."""
    return _pct_rank_window(_rolling_sigma(_log_ret(close), QDAYS), DDAYS_5Y, DDAYS_2Y)


def f39_vclu_115_pctrank_sigma5_in_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of current σ_5d within own past 252d distribution."""
    return _pct_rank_window(_rolling_sigma(_log_ret(close), WDAYS), YDAYS, QDAYS)


def f39_vclu_116_pctrank_drift_63d(close: pd.Series) -> pd.Series:
    """Rank-drift: current σ_21d percentile rank − rolling 63d mean of that rank."""
    rk = _pct_rank_window(_rolling_sigma(_log_ret(close), MDAYS), YDAYS, QDAYS)
    return rk - rk.rolling(QDAYS, min_periods=MDAYS).mean()


# ============================================================
# Bucket T — Vol-momentum (117-121)
# ============================================================

def f39_vclu_117_sigma21_change_lag21(close: pd.Series) -> pd.Series:
    """Monthly vol-momentum: σ_21d − σ_21d.shift(21)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return s - s.shift(MDAYS)


def f39_vclu_118_sigma21_change_lag63(close: pd.Series) -> pd.Series:
    """Quarterly vol-momentum: σ_21d − σ_21d.shift(63)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return s - s.shift(QDAYS)


def f39_vclu_119_sigma21_ratio_lag252(close: pd.Series) -> pd.Series:
    """Annual vol-momentum ratio: σ_21d / σ_21d.shift(252)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return _safe_div(s, s.shift(YDAYS))


def f39_vclu_120_log_sigma21_ratio_lag63(close: pd.Series) -> pd.Series:
    """Log quarterly vol-momentum: log(σ_21d / σ_21d.shift(63))."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return _safe_log(s) - _safe_log(s.shift(QDAYS))


def f39_vclu_121_freq_sigma21_above_lag21_in_63d(close: pd.Series) -> pd.Series:
    """Upward vol-momentum frequency: fraction of bars where σ_21d > σ_21d.shift(21) over 63d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return (s > s.shift(MDAYS)).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()


# ============================================================
# Bucket U — Vol-clustering cross-lag corr (122-126)
# ============================================================

def f39_vclu_122_autocorr_sigma21_lag5_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d corr(σ_21d_t, σ_21d_{t-5}) — weekly-lag σ autocorr."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return s.rolling(YDAYS, min_periods=QDAYS).corr(s.shift(WDAYS))


def f39_vclu_123_autocorr_sigma21_lag10_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d corr(σ_21d_t, σ_21d_{t-10}) — 10-day-lag σ autocorr."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return s.rolling(YDAYS, min_periods=QDAYS).corr(s.shift(10))


def f39_vclu_124_autocorr_sigma21_lag21_504d(close: pd.Series) -> pd.Series:
    """Rolling 504d corr(σ_21d_t, σ_21d_{t-21}) — monthly-lag σ autocorr."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return s.rolling(DDAYS_2Y, min_periods=YDAYS).corr(s.shift(MDAYS))


def f39_vclu_125_autocorr_sigma21_lag63_504d(close: pd.Series) -> pd.Series:
    """Rolling 504d corr(σ_21d_t, σ_21d_{t-63}) — quarterly-lag σ autocorr."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return s.rolling(DDAYS_2Y, min_periods=YDAYS).corr(s.shift(QDAYS))


def f39_vclu_126_corr_sigma21_sigma5_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d corr(σ_21d, σ_5d) — short-vs-medium horizon σ co-movement."""
    r = _log_ret(close)
    return _rolling_sigma(r, MDAYS).rolling(YDAYS, min_periods=QDAYS).corr(_rolling_sigma(r, WDAYS))


# ============================================================
# Bucket V — Vol-volume joint clustering (127-130)
# ============================================================

def f39_vclu_127_corr_sigma21_with_volz_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 252d corr(σ_21d, volume z-score) — joint vol-volume cluster."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    vz = _rolling_zscore(volume, QDAYS)
    return s.rolling(YDAYS, min_periods=QDAYS).corr(vz)


def f39_vclu_128_sigma_on_high_vs_low_volume_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio σ_21d on high-volume (vz>1) vs low-volume (vz<−1) days over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    vz = _rolling_zscore(volume, QDAYS)
    hi = s.where(vz > 1.0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    lo = s.where(vz < -1.0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(hi, lo)


def f39_vclu_129_ar1_sigma_times_volume_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """AR(1) coef of σ_21d · (volume z-score) joint series over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    vz = _rolling_zscore(volume, QDAYS)
    sv = s * vz
    return sv.rolling(YDAYS, min_periods=QDAYS).corr(sv.shift(1))


def f39_vclu_130_corr_sigma_vol_lag1_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 252d corr((σ·v)_t, (σ·v)_{t-1}) — persistence of vol-volume joint product."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    vz = _rolling_zscore(volume, QDAYS)
    sv = s * vz
    return sv.rolling(YDAYS, min_periods=QDAYS).corr(sv.shift(1))


# ============================================================
# Bucket W — Vol-forecast stability / spread (131-135)
# ============================================================

def f39_vclu_131_mean_abs_delta_sigma21_63d(close: pd.Series) -> pd.Series:
    """Mean |Δσ_21d| over 63d — short-horizon vol-instability."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return s.diff().abs().rolling(QDAYS, min_periods=MDAYS).mean()


def f39_vclu_132_mean_rel_delta_sigma21_63d(close: pd.Series) -> pd.Series:
    """Mean |Δσ_21d| / σ_21d.shift(1) over 63d — relative vol-instability."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return _safe_div(s.diff().abs(), s.shift(1)).rolling(QDAYS, min_periods=MDAYS).mean()


def f39_vclu_133_mad_sigma21_63d(close: pd.Series) -> pd.Series:
    """Rolling 63d median absolute deviation of σ_21d (robust dispersion)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    med = s.rolling(QDAYS, min_periods=MDAYS).median()
    return (s - med).abs().rolling(QDAYS, min_periods=MDAYS).median()


def f39_vclu_134_cv_sigma21_252d(close: pd.Series) -> pd.Series:
    """CV (std/mean) of σ_21d over 252d — coefficient of variation of vol process."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return _safe_div(s.rolling(YDAYS, min_periods=QDAYS).std(),
                     s.rolling(YDAYS, min_periods=QDAYS).mean())


def f39_vclu_135_vol_jump_count_63d(close: pd.Series) -> pd.Series:
    """Count of bars where Δσ_21d > 0.5·σ_21d.shift(1) within 63d — vol-jump count."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return ((s.diff() > 0.5 * s.shift(1)).astype(float)
            .rolling(QDAYS, min_periods=MDAYS).sum())


# ============================================================
# Bucket X — Misc vol-clustering descriptors (136-150)
# ============================================================

def f39_vclu_136_frac_var_from_top_decile_rsq_252d(close: pd.Series) -> pd.Series:
    """Fraction of Σr² contributed by top-decile r² bars over 252d (variance concentration)."""
    r2 = _log_ret(close) ** 2
    p90 = r2.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    top = r2.where(r2 > p90, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()
    tot = r2.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(top, tot)


def f39_vclu_137_frac_var_from_bottom_decile_rsq_252d(close: pd.Series) -> pd.Series:
    """Fraction of Σr² contributed by bottom-decile r² bars over 252d."""
    r2 = _log_ret(close) ** 2
    p10 = r2.rolling(YDAYS, min_periods=QDAYS).quantile(0.10)
    bot = r2.where(r2 < p10, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()
    tot = r2.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(bot, tot)


def f39_vclu_138_gini_rsq_252d(close: pd.Series) -> pd.Series:
    """Gini coefficient of r² distribution over 252d — variance-concentration index."""
    r2 = _log_ret(close) ** 2

    def _gini(w):
        x = w[~np.isnan(w)]
        n = len(x)
        if n < 30 or x.sum() <= 0:
            return np.nan
        x = np.sort(x)
        i = np.arange(1, n + 1)
        return float((2 * (i * x).sum() - (n + 1) * x.sum()) / (n * x.sum()))
    return r2.rolling(YDAYS, min_periods=QDAYS).apply(_gini, raw=True)


def f39_vclu_139_theil_rsq_252d(close: pd.Series) -> pd.Series:
    """Theil index of r² distribution over 252d (alt variance-concentration index)."""
    r2 = _log_ret(close) ** 2

    def _theil(w):
        x = w[~np.isnan(w)]
        n = len(x)
        if n < 30 or x.sum() <= 0:
            return np.nan
        mu = x.mean()
        xp = x[x > 0]
        if len(xp) < 2:
            return np.nan
        return float(((xp / mu) * np.log(xp / mu)).sum() / n)
    return r2.rolling(YDAYS, min_periods=QDAYS).apply(_theil, raw=True)


def f39_vclu_140_continuous_entropy_rsq_252d(close: pd.Series) -> pd.Series:
    """Continuous-style entropy of r² over 252d (10-bin histogram on log-r²)."""
    r2 = _log_ret(close) ** 2

    def _ent(w):
        x = w[~np.isnan(w) & (w > 0)]
        if len(x) < 30:
            return np.nan
        lx = np.log(x)
        h, _ = np.histogram(lx, bins=10)
        p = h.astype(float) / h.sum()
        p = p[p > 0]
        return float(-(p * np.log(p)).sum())
    return r2.rolling(YDAYS, min_periods=QDAYS).apply(_ent, raw=True)


def f39_vclu_141_hhi_rsq_shares_252d(close: pd.Series) -> pd.Series:
    """HHI-style concentration index on r² shares over 252d (Σ(r²_i / Σr²)²)."""
    r2 = _log_ret(close) ** 2

    def _hhi(w):
        x = w[~np.isnan(w)]
        if len(x) < 30 or x.sum() <= 0:
            return np.nan
        p = x / x.sum()
        return float((p ** 2).sum())
    return r2.rolling(YDAYS, min_periods=QDAYS).apply(_hhi, raw=True)


def f39_vclu_142_variance_shock_count_63d(close: pd.Series) -> pd.Series:
    """Variance-shock count: bars with r² > 2·EWMA(r², λ=0.94) within 63d."""
    r = _log_ret(close)
    e = (r ** 2).ewm(alpha=0.06, min_periods=MDAYS).mean()
    return ((r ** 2) > 2 * e).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f39_vclu_143_variance_quiet_count_63d(close: pd.Series) -> pd.Series:
    """Variance-quiet count: bars with r² < 0.5·EWMA(r², λ=0.94) within 63d."""
    r = _log_ret(close)
    e = (r ** 2).ewm(alpha=0.06, min_periods=MDAYS).mean()
    return ((r ** 2) < 0.5 * e).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f39_vclu_144_max_over_median_rsq_252d(close: pd.Series) -> pd.Series:
    """Variance outlier ratio: max(r²) / median(r²) over 252d."""
    r2 = _log_ret(close) ** 2
    return _safe_div(r2.rolling(YDAYS, min_periods=QDAYS).max(),
                     r2.rolling(YDAYS, min_periods=QDAYS).median())


def f39_vclu_145_halflife_exp_decay_sigma21_63d(close: pd.Series) -> pd.Series:
    """Half-life of σ_21d shock from exponential fit log(σ) vs time over past 63d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    lg = _safe_log(s)
    sl = _rolling_slope(lg, QDAYS)
    return -_safe_div(pd.Series(np.log(2.0), index=close.index), sl).clip(lower=0.0, upper=500.0)


def f39_vclu_146_decay_lag_sigma21_252d(close: pd.Series) -> pd.Series:
    """Decay-length: lag (1..21) at which autocorr(σ_21d) first drops below 0.1, over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)

    def _decay(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < QDAYS:
            return np.nan
        m = ww.mean()
        var = ((ww - m) ** 2).sum()
        if var == 0:
            return np.nan
        for k in range(1, 22):
            c = ((ww[k:] - m) * (ww[:-k] - m)).sum() / var
            if abs(c) < 0.1:
                return float(k)
        return 22.0
    return s.rolling(YDAYS, min_periods=QDAYS).apply(_decay, raw=True)


def f39_vclu_147_corr_sigma21_sigma63_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d corr(σ_21d, σ_63d) — cross-window σ co-movement (different from 126)."""
    r = _log_ret(close)
    return _rolling_sigma(r, MDAYS).rolling(YDAYS, min_periods=QDAYS).corr(_rolling_sigma(r, QDAYS))


def f39_vclu_148_corr_sigma5_sigma252_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d corr(σ_5d, σ_252d) — extreme-cross-window σ co-movement."""
    r = _log_ret(close)
    return _rolling_sigma(r, WDAYS).rolling(YDAYS, min_periods=QDAYS).corr(_rolling_sigma(r, YDAYS))


def f39_vclu_149_longest_monotonic_rising_sigma_63d(close: pd.Series) -> pd.Series:
    """Longest consecutive run of monotonically-increasing σ_21d within 63d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    up = (s > s.shift(1)).astype(float).fillna(0.0)
    return up.rolling(QDAYS, min_periods=MDAYS).apply(_longest_run, raw=True)


def f39_vclu_150_cum_positive_sigma_increments_63d(close: pd.Series) -> pd.Series:
    """Cumulative positive σ_21d increments (Δσ clipped ≥0) over 63d — cumulative vol-rise."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return s.diff().clip(lower=0.0).rolling(QDAYS, min_periods=MDAYS).sum()


# ============================================================
#                         REGISTRY 076-150
# ============================================================

VOLATILITY_CLUSTERING_BASE_REGISTRY_076_150 = {
    "f39_vclu_076_neg_vs_pos_post_ret_sigma_63d": {"inputs": ["close"], "func": f39_vclu_076_neg_vs_pos_post_ret_sigma_63d},
    "f39_vclu_077_neg_vs_pos_post_ret_sigma_252d": {"inputs": ["close"], "func": f39_vclu_077_neg_vs_pos_post_ret_sigma_252d},
    "f39_vclu_078_corr_sigma_with_lag_sign_252d": {"inputs": ["close"], "func": f39_vclu_078_corr_sigma_with_lag_sign_252d},
    "f39_vclu_079_slope_sigma_on_signed_lag_ret_252d": {"inputs": ["close"], "func": f39_vclu_079_slope_sigma_on_signed_lag_ret_252d},
    "f39_vclu_080_leverage_cov_rsq_lag_252d": {"inputs": ["close"], "func": f39_vclu_080_leverage_cov_rsq_lag_252d},
    "f39_vclu_081_nic_asymmetry_var_neg_minus_pos_252d": {"inputs": ["close"], "func": f39_vclu_081_nic_asymmetry_var_neg_minus_pos_252d},
    "f39_vclu_082_hill_sigma21_top10_504d": {"inputs": ["close"], "func": f39_vclu_082_hill_sigma21_top10_504d},
    "f39_vclu_083_hill_sigma21_top5_1260d": {"inputs": ["close"], "func": f39_vclu_083_hill_sigma21_top5_1260d},
    "f39_vclu_084_p99_over_p50_sigma21_252d": {"inputs": ["close"], "func": f39_vclu_084_p99_over_p50_sigma21_252d},
    "f39_vclu_085_max_over_mean_sigma21_252d": {"inputs": ["close"], "func": f39_vclu_085_max_over_mean_sigma21_252d},
    "f39_vclu_086_longest_run_sigma_above_median_252d": {"inputs": ["close"], "func": f39_vclu_086_longest_run_sigma_above_median_252d},
    "f39_vclu_087_longest_run_sigma_top_decile_252d": {"inputs": ["close"], "func": f39_vclu_087_longest_run_sigma_top_decile_252d},
    "f39_vclu_088_run_length_entropy_252d": {"inputs": ["close"], "func": f39_vclu_088_run_length_entropy_252d},
    "f39_vclu_089_current_regime_run_length": {"inputs": ["close"], "func": f39_vclu_089_current_regime_run_length},
    "f39_vclu_090_regime_change_count_252d": {"inputs": ["close"], "func": f39_vclu_090_regime_change_count_252d},
    "f39_vclu_091_slope_sigma21_63d": {"inputs": ["close"], "func": f39_vclu_091_slope_sigma21_63d},
    "f39_vclu_092_slope_sigma21_252d": {"inputs": ["close"], "func": f39_vclu_092_slope_sigma21_252d},
    "f39_vclu_093_slope_log_sigma21_252d": {"inputs": ["close"], "func": f39_vclu_093_slope_log_sigma21_252d},
    "f39_vclu_094_vol_trend_velocity_63d": {"inputs": ["close"], "func": f39_vclu_094_vol_trend_velocity_63d},
    "f39_vclu_095_vol_trend_sign_changes_252d": {"inputs": ["close"], "func": f39_vclu_095_vol_trend_sign_changes_252d},
    "f39_vclu_096_range_of_sigma21_252d": {"inputs": ["close"], "func": f39_vclu_096_range_of_sigma21_252d},
    "f39_vclu_097_har_daily_component": {"inputs": ["close"], "func": f39_vclu_097_har_daily_component},
    "f39_vclu_098_har_weekly_component": {"inputs": ["close"], "func": f39_vclu_098_har_weekly_component},
    "f39_vclu_099_har_monthly_component": {"inputs": ["close"], "func": f39_vclu_099_har_monthly_component},
    "f39_vclu_100_har_daily_over_monthly_ratio": {"inputs": ["close"], "func": f39_vclu_100_har_daily_over_monthly_ratio},
    "f39_vclu_101_har_fixed_weight_forecast": {"inputs": ["close"], "func": f39_vclu_101_har_fixed_weight_forecast},
    "f39_vclu_102_vov_on_rising_sigma_252d": {"inputs": ["close"], "func": f39_vclu_102_vov_on_rising_sigma_252d},
    "f39_vclu_103_vov_on_falling_sigma_252d": {"inputs": ["close"], "func": f39_vclu_103_vov_on_falling_sigma_252d},
    "f39_vclu_104_vov_rising_over_falling_ratio_252d": {"inputs": ["close"], "func": f39_vclu_104_vov_rising_over_falling_ratio_252d},
    "f39_vclu_105_skew_sigma_increments_252d": {"inputs": ["close"], "func": f39_vclu_105_skew_sigma_increments_252d},
    "f39_vclu_106_mcleod_li_stat_252d": {"inputs": ["close"], "func": f39_vclu_106_mcleod_li_stat_252d},
    "f39_vclu_107_arch_lm_stat_252d": {"inputs": ["close"], "func": f39_vclu_107_arch_lm_stat_252d},
    "f39_vclu_108_var_ratio_rsq_5_21_252d": {"inputs": ["close"], "func": f39_vclu_108_var_ratio_rsq_5_21_252d},
    "f39_vclu_109_hurst_rs_absret_252d": {"inputs": ["close"], "func": f39_vclu_109_hurst_rs_absret_252d},
    "f39_vclu_110_dfa_absret_252d": {"inputs": ["close"], "func": f39_vclu_110_dfa_absret_252d},
    "f39_vclu_111_pctrank_sigma21_in_252d": {"inputs": ["close"], "func": f39_vclu_111_pctrank_sigma21_in_252d},
    "f39_vclu_112_pctrank_sigma21_in_504d": {"inputs": ["close"], "func": f39_vclu_112_pctrank_sigma21_in_504d},
    "f39_vclu_113_pctrank_sigma21_in_1260d": {"inputs": ["close"], "func": f39_vclu_113_pctrank_sigma21_in_1260d},
    "f39_vclu_114_pctrank_sigma63_in_1260d": {"inputs": ["close"], "func": f39_vclu_114_pctrank_sigma63_in_1260d},
    "f39_vclu_115_pctrank_sigma5_in_252d": {"inputs": ["close"], "func": f39_vclu_115_pctrank_sigma5_in_252d},
    "f39_vclu_116_pctrank_drift_63d": {"inputs": ["close"], "func": f39_vclu_116_pctrank_drift_63d},
    "f39_vclu_117_sigma21_change_lag21": {"inputs": ["close"], "func": f39_vclu_117_sigma21_change_lag21},
    "f39_vclu_118_sigma21_change_lag63": {"inputs": ["close"], "func": f39_vclu_118_sigma21_change_lag63},
    "f39_vclu_119_sigma21_ratio_lag252": {"inputs": ["close"], "func": f39_vclu_119_sigma21_ratio_lag252},
    "f39_vclu_120_log_sigma21_ratio_lag63": {"inputs": ["close"], "func": f39_vclu_120_log_sigma21_ratio_lag63},
    "f39_vclu_121_freq_sigma21_above_lag21_in_63d": {"inputs": ["close"], "func": f39_vclu_121_freq_sigma21_above_lag21_in_63d},
    "f39_vclu_122_autocorr_sigma21_lag5_252d": {"inputs": ["close"], "func": f39_vclu_122_autocorr_sigma21_lag5_252d},
    "f39_vclu_123_autocorr_sigma21_lag10_252d": {"inputs": ["close"], "func": f39_vclu_123_autocorr_sigma21_lag10_252d},
    "f39_vclu_124_autocorr_sigma21_lag21_504d": {"inputs": ["close"], "func": f39_vclu_124_autocorr_sigma21_lag21_504d},
    "f39_vclu_125_autocorr_sigma21_lag63_504d": {"inputs": ["close"], "func": f39_vclu_125_autocorr_sigma21_lag63_504d},
    "f39_vclu_126_corr_sigma21_sigma5_252d": {"inputs": ["close"], "func": f39_vclu_126_corr_sigma21_sigma5_252d},
    "f39_vclu_127_corr_sigma21_with_volz_252d": {"inputs": ["close", "volume"], "func": f39_vclu_127_corr_sigma21_with_volz_252d},
    "f39_vclu_128_sigma_on_high_vs_low_volume_252d": {"inputs": ["close", "volume"], "func": f39_vclu_128_sigma_on_high_vs_low_volume_252d},
    "f39_vclu_129_ar1_sigma_times_volume_252d": {"inputs": ["close", "volume"], "func": f39_vclu_129_ar1_sigma_times_volume_252d},
    "f39_vclu_130_corr_sigma_vol_lag1_252d": {"inputs": ["close", "volume"], "func": f39_vclu_130_corr_sigma_vol_lag1_252d},
    "f39_vclu_131_mean_abs_delta_sigma21_63d": {"inputs": ["close"], "func": f39_vclu_131_mean_abs_delta_sigma21_63d},
    "f39_vclu_132_mean_rel_delta_sigma21_63d": {"inputs": ["close"], "func": f39_vclu_132_mean_rel_delta_sigma21_63d},
    "f39_vclu_133_mad_sigma21_63d": {"inputs": ["close"], "func": f39_vclu_133_mad_sigma21_63d},
    "f39_vclu_134_cv_sigma21_252d": {"inputs": ["close"], "func": f39_vclu_134_cv_sigma21_252d},
    "f39_vclu_135_vol_jump_count_63d": {"inputs": ["close"], "func": f39_vclu_135_vol_jump_count_63d},
    "f39_vclu_136_frac_var_from_top_decile_rsq_252d": {"inputs": ["close"], "func": f39_vclu_136_frac_var_from_top_decile_rsq_252d},
    "f39_vclu_137_frac_var_from_bottom_decile_rsq_252d": {"inputs": ["close"], "func": f39_vclu_137_frac_var_from_bottom_decile_rsq_252d},
    "f39_vclu_138_gini_rsq_252d": {"inputs": ["close"], "func": f39_vclu_138_gini_rsq_252d},
    "f39_vclu_139_theil_rsq_252d": {"inputs": ["close"], "func": f39_vclu_139_theil_rsq_252d},
    "f39_vclu_140_continuous_entropy_rsq_252d": {"inputs": ["close"], "func": f39_vclu_140_continuous_entropy_rsq_252d},
    "f39_vclu_141_hhi_rsq_shares_252d": {"inputs": ["close"], "func": f39_vclu_141_hhi_rsq_shares_252d},
    "f39_vclu_142_variance_shock_count_63d": {"inputs": ["close"], "func": f39_vclu_142_variance_shock_count_63d},
    "f39_vclu_143_variance_quiet_count_63d": {"inputs": ["close"], "func": f39_vclu_143_variance_quiet_count_63d},
    "f39_vclu_144_max_over_median_rsq_252d": {"inputs": ["close"], "func": f39_vclu_144_max_over_median_rsq_252d},
    "f39_vclu_145_halflife_exp_decay_sigma21_63d": {"inputs": ["close"], "func": f39_vclu_145_halflife_exp_decay_sigma21_63d},
    "f39_vclu_146_decay_lag_sigma21_252d": {"inputs": ["close"], "func": f39_vclu_146_decay_lag_sigma21_252d},
    "f39_vclu_147_corr_sigma21_sigma63_252d": {"inputs": ["close"], "func": f39_vclu_147_corr_sigma21_sigma63_252d},
    "f39_vclu_148_corr_sigma5_sigma252_252d": {"inputs": ["close"], "func": f39_vclu_148_corr_sigma5_sigma252_252d},
    "f39_vclu_149_longest_monotonic_rising_sigma_63d": {"inputs": ["close"], "func": f39_vclu_149_longest_monotonic_rising_sigma_63d},
    "f39_vclu_150_cum_positive_sigma_increments_63d": {"inputs": ["close"], "func": f39_vclu_150_cum_positive_sigma_increments_63d},
}
