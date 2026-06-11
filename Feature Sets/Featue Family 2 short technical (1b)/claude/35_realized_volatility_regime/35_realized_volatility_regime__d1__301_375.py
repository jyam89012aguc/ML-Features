"""35_realized_volatility_regime d1 features 301-375 — order-1 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff(). Self-contained; helpers redefined locally per HANDOFF."""
import numpy as np
import pandas as pd
YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
DDAYS_3Y = 756
DDAYS_5Y = 1260

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
    idx = num.index if hasattr(num, 'index') else None
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
        xm = x.mean()
        wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)

def _log_returns(close: pd.Series) -> pd.Series:
    return _safe_log(close).diff()

def _bpv(r: pd.Series, n: int, mp: int) -> pd.Series:
    """Bipower variation over window n (mu1^{-2} * sum |r_t||r_{t-1}|)."""
    return (np.pi / 2.0 * r.abs() * r.shift(1).abs()).rolling(n, min_periods=mp).sum()

def _rv(r: pd.Series, n: int, mp: int) -> pd.Series:
    return (r ** 2).rolling(n, min_periods=mp).sum()

def _ols_kvar(y: np.ndarray, X: np.ndarray):
    """Solve OLS y = X*beta, return beta or array of NaN if singular."""
    try:
        beta, *_ = np.linalg.lstsq(X, y, rcond=None)
        return beta
    except np.linalg.LinAlgError:
        return np.full(X.shape[1], np.nan)

def _har_coefs_window(close: pd.Series, win: int) -> tuple:
    """Return (intercept, b_d, b_w, b_m) from rolling-OLS HAR fit over win bars."""
    r = _log_returns(close)
    rv_d = r ** 2
    rv_w = rv_d.rolling(WDAYS, min_periods=2).mean()
    rv_m = rv_d.rolling(22, min_periods=WDAYS).mean()
    y = rv_d.values
    x1 = rv_d.shift(1).values
    x2 = rv_w.shift(1).values
    x3 = rv_m.shift(1).values
    n = len(y)
    b0 = np.full(n, np.nan)
    b1 = np.full(n, np.nan)
    b2 = np.full(n, np.nan)
    b3 = np.full(n, np.nan)
    for i in range(win, n):
        lo = i - win
        mask = ~(np.isnan(y[lo:i]) | np.isnan(x1[lo:i]) | np.isnan(x2[lo:i]) | np.isnan(x3[lo:i]))
        if mask.sum() < 30:
            continue
        X = np.column_stack([np.ones(mask.sum()), x1[lo:i][mask], x2[lo:i][mask], x3[lo:i][mask]])
        beta = _ols_kvar(y[lo:i][mask], X)
        b0[i] = beta[0]
        b1[i] = beta[1]
        b2[i] = beta[2]
        b3[i] = beta[3]
    return (pd.Series(b0, index=close.index), pd.Series(b1, index=close.index), pd.Series(b2, index=close.index), pd.Series(b3, index=close.index))

def _tbpv(r: pd.Series, n: int, mp: int, k: float=3.0) -> pd.Series:
    sigma = r.rolling(MDAYS, min_periods=WDAYS).std().shift(1)
    thr = k * sigma
    small_r = r.abs().where(r.abs() <= thr, 0.0)
    return (np.pi / 2.0 * small_r * small_r.shift(1)).rolling(n, min_periods=mp).sum()

def _carr_coefs(high: pd.Series, low: pd.Series, win: int=YDAYS):
    """Rolling OLS: log_hl_t = omega + alpha * log_hl_{t-1} + beta * mean(log_hl_{t-1:t-5})."""
    log_hl = np.log(_safe_div(high, low))
    y = log_hl.values
    x1 = log_hl.shift(1).values
    x2 = log_hl.shift(1).rolling(WDAYS, min_periods=2).mean().values
    n = len(y)
    omega = np.full(n, np.nan)
    alpha = np.full(n, np.nan)
    beta = np.full(n, np.nan)
    for i in range(win, n):
        lo = i - win
        mask = ~(np.isnan(y[lo:i]) | np.isnan(x1[lo:i]) | np.isnan(x2[lo:i]))
        if mask.sum() < 50:
            continue
        X = np.column_stack([np.ones(mask.sum()), x1[lo:i][mask], x2[lo:i][mask]])
        b = _ols_kvar(y[lo:i][mask], X)
        omega[i] = b[0]
        alpha[i] = b[1]
        beta[i] = b[2]
    return (pd.Series(omega, index=high.index), pd.Series(alpha, index=high.index), pd.Series(beta, index=high.index))

def _egarch_proxy_coefs(close: pd.Series, win: int=YDAYS):
    """Rolling OLS: log_rv21_t = omega + alpha*|z_lag| + gamma*z_lag + beta*log_rv21_lag, where z = r/sigma."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    log_rv = np.log(rv21 + 1e-12)
    sigma21 = np.sqrt(rv21 / float(MDAYS))
    z = _safe_div(r, sigma21).shift(1)
    y = log_rv.values
    x1 = z.abs().values
    x2 = z.values
    x3 = log_rv.shift(1).values
    n = len(y)
    om = np.full(n, np.nan)
    a = np.full(n, np.nan)
    g = np.full(n, np.nan)
    b = np.full(n, np.nan)
    for i in range(win, n):
        lo = i - win
        mask = ~(np.isnan(y[lo:i]) | np.isnan(x1[lo:i]) | np.isnan(x2[lo:i]) | np.isnan(x3[lo:i]))
        if mask.sum() < 50:
            continue
        X = np.column_stack([np.ones(mask.sum()), x1[lo:i][mask], x2[lo:i][mask], x3[lo:i][mask]])
        beta = _ols_kvar(y[lo:i][mask], X)
        om[i] = beta[0]
        a[i] = beta[1]
        g[i] = beta[2]
        b[i] = beta[3]
    return (pd.Series(om, index=close.index), pd.Series(a, index=close.index), pd.Series(g, index=close.index), pd.Series(b, index=close.index))

def _near_peak_mask(close: pd.Series, lookback: int=YDAYS, tol: float=0.95) -> pd.Series:
    return close >= tol * close.rolling(lookback, min_periods=max(lookback // 3, 2)).max()

def _rolling_beta(y: pd.Series, x: pd.Series, win: int, mp: int) -> pd.Series:
    df = pd.concat([y.rename('y'), x.rename('x')], axis=1)
    y_v = df['y'].values
    x_v = df['x'].values
    n = len(y_v)
    out = np.full(n, np.nan)
    for i in range(win - 1, n):
        lo = i - win + 1
        m = ~(np.isnan(y_v[lo:i + 1]) | np.isnan(x_v[lo:i + 1]))
        if m.sum() < mp:
            continue
        xx = x_v[lo:i + 1][m]
        yy = y_v[lo:i + 1][m]
        if xx.std() == 0:
            continue
        out[i] = float(np.cov(yy, xx, bias=False)[0, 1] / xx.var(ddof=1))
    return pd.Series(out, index=y.index)

def f35_rvre_301_continuous_var_21d_d1(close: pd.Series) -> pd.Series:
    """Continuous variation component (BPV) at 21d — jump-removed monthly variance, HAR-CJ input."""
    r = _log_returns(close)
    return _bpv(r, MDAYS, WDAYS).diff()

def f35_rvre_302_jump_var_diff_at_21d_d1(close: pd.Series) -> pd.Series:
    """Discontinuous variation J = max(0, RV - BPV) at 21d — HAR-CJ jump component, monthly."""
    r = _log_returns(close)
    return (_rv(r, MDAYS, WDAYS) - _bpv(r, MDAYS, WDAYS)).clip(lower=0.0).diff()

def f35_rvre_303_har_cj_continuous_share_weekly_d1(close: pd.Series) -> pd.Series:
    """BPV(5d) / (BPV(5d) + Jump(5d)) — weekly continuous-share of HAR-CJ decomposition."""
    r = _log_returns(close)
    c = _bpv(r, WDAYS, 2)
    j = (_rv(r, WDAYS, 2) - c).clip(lower=0.0)
    return _safe_div(c, c + j).diff()

def f35_rvre_304_har_cj_jump_share_monthly_d1(close: pd.Series) -> pd.Series:
    """J(21d) / RV(21d) — monthly jump share of HAR-CJ; high values precede regime stress."""
    r = _log_returns(close)
    rv = _rv(r, MDAYS, WDAYS)
    bpv = _bpv(r, MDAYS, WDAYS)
    return _safe_div((rv - bpv).clip(lower=0.0), rv).diff()

def f35_rvre_305_har_cj_jump_minus_continuous_252d_d1(close: pd.Series) -> pd.Series:
    """J(252d) - C(252d) — annual signed dominance of jump vs continuous variation; >0 = jumps dominate."""
    r = _log_returns(close)
    rv = _rv(r, YDAYS, QDAYS)
    c = _bpv(r, YDAYS, QDAYS)
    j = (rv - c).clip(lower=0.0)
    return (j - c).diff()

def f35_rvre_306_har_leverage_neg_return_term_21d_d1(close: pd.Series) -> pd.Series:
    """sum(r^2 | r<0) over 21d — HAR-S leverage term: vol contribution from negative returns."""
    r = _log_returns(close)
    neg_sq = (r ** 2).where(r < 0, 0.0)
    return neg_sq.rolling(MDAYS, min_periods=WDAYS).sum().diff()

def f35_rvre_307_har_leverage_pos_return_term_21d_d1(close: pd.Series) -> pd.Series:
    """sum(r^2 | r>0) over 21d — symmetric positive-return term."""
    r = _log_returns(close)
    pos_sq = (r ** 2).where(r > 0, 0.0)
    return pos_sq.rolling(MDAYS, min_periods=WDAYS).sum().diff()

def f35_rvre_308_har_s_asymmetry_252d_d1(close: pd.Series) -> pd.Series:
    """sum(r^2 | r<0) - sum(r^2 | r>0) at 252d — direct asymmetric-vol-contribution at annual horizon."""
    r = _log_returns(close)
    neg = (r ** 2).where(r < 0, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()
    pos = (r ** 2).where(r > 0, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()
    return (neg - pos).diff()

def f35_rvre_309_har_s_leverage_beta_252d_d1(close: pd.Series) -> pd.Series:
    """Rolling OLS coefficient on lagged neg-return-r^2 in HAR-S regression — leverage parameter."""
    r = _log_returns(close)
    rv = r ** 2
    rv_w = rv.rolling(WDAYS, min_periods=2).mean()
    rv_m = rv.rolling(22, min_periods=WDAYS).mean()
    neg_sq_lag = (r ** 2).where(r < 0, 0.0).shift(1)
    y = rv.values
    X_cols = [np.ones_like(y), rv.shift(1).values, rv_w.shift(1).values, rv_m.shift(1).values, neg_sq_lag.values]
    n = len(y)
    out = np.full(n, np.nan)
    for i in range(YDAYS, n):
        lo = i - YDAYS
        y_w = y[lo:i]
        X_w = np.column_stack([c[lo:i] for c in X_cols])
        mask = ~(np.isnan(y_w) | np.isnan(X_w).any(axis=1))
        if mask.sum() < 50:
            continue
        beta = _ols_kvar(y_w[mask], X_w[mask])
        out[i] = beta[-1]
    return pd.Series(out, index=close.index).diff()

def f35_rvre_310_neg_return_var_share_252d_d1(close: pd.Series) -> pd.Series:
    """sum(r^2 | r<0) / sum(r^2) at 252d — share of annual realized variance from negative returns."""
    r = _log_returns(close)
    neg = (r ** 2).where(r < 0, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()
    tot = (r ** 2).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(neg, tot).diff()

def f35_rvre_311_har_persistence_b_d_plus_b_w_plus_b_m_252d_d1(close: pd.Series) -> pd.Series:
    """b_d + b_w + b_m from rolling HAR(252d) — total persistence (close to 1 = unit-root vol)."""
    _, b1, b2, b3 = _har_coefs_window(close, YDAYS)
    return (b1 + b2 + b3).diff()

def f35_rvre_312_har_intercept_252d_d1(close: pd.Series) -> pd.Series:
    """HAR intercept (omega) from rolling 252d fit — long-run vol scale."""
    b0, _, _, _ = _har_coefs_window(close, YDAYS)
    return b0.diff()

def f35_rvre_313_har_b_d_weight_252d_d1(close: pd.Series) -> pd.Series:
    """HAR coefficient on RV_d — daily component weight; high = more weight on most recent RV."""
    _, b1, _, _ = _har_coefs_window(close, YDAYS)
    return b1.diff()

def f35_rvre_314_har_b_m_weight_252d_d1(close: pd.Series) -> pd.Series:
    """HAR coefficient on RV_m — monthly component weight; high = vol is determined by long-window average."""
    _, _, _, b3 = _har_coefs_window(close, YDAYS)
    return b3.diff()

def f35_rvre_315_har_5_step_implied_vol_252d_d1(close: pd.Series) -> pd.Series:
    """5-step-ahead implied vol forecast: scale 1-step forecast by persistence^5 — quick proxy for HAR 5d ahead."""
    r = _log_returns(close)
    rv_d = r ** 2
    rv_w = rv_d.rolling(WDAYS, min_periods=2).mean()
    rv_m = rv_d.rolling(22, min_periods=WDAYS).mean()
    b0, b1, b2, b3 = _har_coefs_window(close, YDAYS)
    pers = b1 + b2 + b3
    one_step = b0 + b1 * rv_d + b2 * rv_w + b3 * rv_m
    long_run = _safe_div(b0, 1.0 - pers.where((pers > 0) & (pers < 1)))
    return (long_run + pers ** 5 * (one_step - long_run)).diff()

def f35_rvre_316_mean_jump_size_252d_d1(close: pd.Series) -> pd.Series:
    """Mean |r_t| restricted to bars where |r_t| > 3 * lagged 21d sigma over 252d — typical jump magnitude."""
    r = _log_returns(close)
    sigma = r.rolling(MDAYS, min_periods=WDAYS).std().shift(1)
    jump_size = r.abs().where(r.abs() > 3.0 * sigma)
    return jump_size.rolling(YDAYS, min_periods=WDAYS).mean().diff()

def f35_rvre_317_std_jump_size_252d_d1(close: pd.Series) -> pd.Series:
    """Std of |r_t| restricted to jump bars over 252d — jump-magnitude dispersion."""
    r = _log_returns(close)
    sigma = r.rolling(MDAYS, min_periods=WDAYS).std().shift(1)
    jump_size = r.abs().where(r.abs() > 3.0 * sigma)
    return jump_size.rolling(YDAYS, min_periods=WDAYS).std().diff()

def f35_rvre_318_max_jump_size_252d_d1(close: pd.Series) -> pd.Series:
    """Max |r_t| restricted to jump bars over 252d — biggest jump magnitude."""
    r = _log_returns(close)
    sigma = r.rolling(MDAYS, min_periods=WDAYS).std().shift(1)
    jump_size = r.abs().where(r.abs() > 3.0 * sigma)
    return jump_size.rolling(YDAYS, min_periods=WDAYS).max().diff()

def f35_rvre_319_jump_intensity_per_year_252d_d1(close: pd.Series) -> pd.Series:
    """Jumps per year (count / 252) over 252d — annualized jump rate."""
    r = _log_returns(close)
    sigma = r.rolling(MDAYS, min_periods=WDAYS).std().shift(1)
    is_jump = (r.abs() > 3.0 * sigma).astype(float).where(sigma.notna(), np.nan)
    return is_jump.rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f35_rvre_320_jump_signed_skew_252d_d1(close: pd.Series) -> pd.Series:
    """Skewness of signed r_t restricted to jump bars over 252d — are jumps biased up or down?"""
    r = _log_returns(close)
    sigma = r.rolling(MDAYS, min_periods=WDAYS).std().shift(1)
    jump_signed = r.where(r.abs() > 3.0 * sigma)

    def _sk(w):
        v = w[~np.isnan(w)]
        if v.size < 5:
            return np.nan
        m = v.mean()
        s = v.std(ddof=1)
        if s == 0:
            return np.nan
        return float(((v - m) ** 3).mean() / s ** 3)
    return jump_signed.rolling(YDAYS, min_periods=WDAYS).apply(_sk, raw=True).diff()

def f35_rvre_321_mean_jump_interarrival_252d_d1(close: pd.Series) -> pd.Series:
    """Mean bars between jumps in trailing 252d — jump-recurrence cadence."""
    r = _log_returns(close)
    sigma = r.rolling(MDAYS, min_periods=WDAYS).std().shift(1)
    is_jump = (r.abs() > 3.0 * sigma).values

    def _ia(w):
        idx = np.where(w > 0)[0]
        if idx.size < 2:
            return np.nan
        return float(np.diff(idx).mean())
    return pd.Series(is_jump.astype(float), index=close.index).rolling(YDAYS, min_periods=QDAYS).apply(_ia, raw=True).diff()

def f35_rvre_322_bars_since_last_jump_d1(close: pd.Series) -> pd.Series:
    """Bars since the most-recent jump (|r| > 3*lagged 21d sigma) — jump-recency clock."""
    r = _log_returns(close)
    sigma = r.rolling(MDAYS, min_periods=WDAYS).std().shift(1)
    is_jump = (r.abs() > 3.0 * sigma).values
    n = len(is_jump)
    out = np.full(n, np.nan)
    last = -1
    for i in range(n):
        if not np.isnan(sigma.iat[i]):
            if is_jump[i]:
                last = i
            if last >= 0:
                out[i] = float(i - last)
    return pd.Series(out, index=close.index).diff()

def f35_rvre_323_jump_neg_minus_pos_count_252d_d1(close: pd.Series) -> pd.Series:
    """count(neg jumps) - count(pos jumps) over 252d — signed jump-count asymmetry."""
    r = _log_returns(close)
    sigma = r.rolling(MDAYS, min_periods=WDAYS).std().shift(1)
    neg_jump = (r < -3.0 * sigma).astype(float).where(sigma.notna(), np.nan)
    pos_jump = (r > 3.0 * sigma).astype(float).where(sigma.notna(), np.nan)
    return (neg_jump.rolling(YDAYS, min_periods=QDAYS).sum() - pos_jump.rolling(YDAYS, min_periods=QDAYS).sum()).diff()

def f35_rvre_324_tbpv_21d_k3_d1(close: pd.Series) -> pd.Series:
    """Threshold Bipower Variation over 21d (k=3) — jump-and-cluster-robust monthly continuous variance."""
    r = _log_returns(close)
    return _tbpv(r, MDAYS, WDAYS, 3.0).diff()

def f35_rvre_325_tbpv_252d_k3_d1(close: pd.Series) -> pd.Series:
    """TBPV over 252d (k=3) — annual continuous variance, robust to clustered jumps."""
    r = _log_returns(close)
    return _tbpv(r, YDAYS, QDAYS, 3.0).diff()

def f35_rvre_326_tbpv_minus_bpv_252d_d1(close: pd.Series) -> pd.Series:
    """TBPV(252d) - BPV(252d) — divergence indicator; <0 = clustered jumps inflate BPV beyond TBPV."""
    r = _log_returns(close)
    return (_tbpv(r, YDAYS, QDAYS, 3.0) - _bpv(r, YDAYS, QDAYS)).diff()

def f35_rvre_327_threshold_jump_share_252d_d1(close: pd.Series) -> pd.Series:
    """1 - TBPV/RV at 252d — threshold-corrected jump share; cleaner than simple jump_share."""
    r = _log_returns(close)
    tb = _tbpv(r, YDAYS, QDAYS, 3.0)
    rv = _rv(r, YDAYS, QDAYS)
    return (1.0 - _safe_div(tb, rv)).clip(lower=0.0).diff()

def f35_rvre_328_carr_alpha_252d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """CARR alpha (Chou 2005): coefficient on lagged log range — range shock-impact."""
    _, a, _ = _carr_coefs(high, low)
    return a.diff()

def f35_rvre_329_carr_beta_252d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """CARR beta: coefficient on lagged range-mean — range persistence parameter."""
    _, _, b = _carr_coefs(high, low)
    return b.diff()

def f35_rvre_330_carr_persistence_alpha_plus_beta_252d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """alpha + beta from CARR — total range-process persistence."""
    _, a, b = _carr_coefs(high, low)
    return (a + b).diff()

def f35_rvre_331_carr_omega_252d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """CARR intercept (omega) — long-run-range scale parameter."""
    w, _, _ = _carr_coefs(high, low)
    return w.diff()

def f35_rvre_332_carr_implied_long_run_log_hl_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """omega / (1 - alpha - beta) — CARR-implied long-run log range; spikes indicate non-stationary range."""
    w, a, b = _carr_coefs(high, low)
    denom = 1.0 - (a + b)
    return _safe_div(w, denom.where(denom > 0)).diff()

def f35_rvre_333_egarch_alpha_252d_d1(close: pd.Series) -> pd.Series:
    """EGARCH-proxy alpha — magnitude response of log-vol to |z|."""
    _, a, _, _ = _egarch_proxy_coefs(close)
    return a.diff()

def f35_rvre_334_egarch_gamma_252d_d1(close: pd.Series) -> pd.Series:
    """EGARCH-proxy gamma — sign response of log-vol; negative = leverage effect."""
    _, _, g, _ = _egarch_proxy_coefs(close)
    return g.diff()

def f35_rvre_335_egarch_beta_252d_d1(close: pd.Series) -> pd.Series:
    """EGARCH-proxy beta — log-vol persistence parameter."""
    _, _, _, b = _egarch_proxy_coefs(close)
    return b.diff()

def f35_rvre_336_egarch_asymmetry_strength_252d_d1(close: pd.Series) -> pd.Series:
    """|gamma| / alpha from EGARCH — relative strength of sign vs magnitude effects."""
    _, a, g, _ = _egarch_proxy_coefs(close)
    return _safe_div(g.abs(), a).diff()

def f35_rvre_337_rv21_at_peak_mean_252d_d1(close: pd.Series) -> pd.Series:
    """Mean RV21 restricted to near-peak bars (within 5% of 252d high) over 252d — typical vol at peak."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    mask = _near_peak_mask(close)
    return rv21.where(mask).rolling(YDAYS, min_periods=WDAYS).mean().diff()

def f35_rvre_338_rv21_at_peak_std_252d_d1(close: pd.Series) -> pd.Series:
    """Std of RV21 at near-peak bars over 252d — vol-volatility at peak."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    mask = _near_peak_mask(close)
    return rv21.where(mask).rolling(YDAYS, min_periods=WDAYS).std().diff()

def f35_rvre_339_rv21_at_peak_vs_off_peak_ratio_252d_d1(close: pd.Series) -> pd.Series:
    """RV21 mean at peak / RV21 mean off-peak over 252d — does vol cluster at price highs?"""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    mask = _near_peak_mask(close)
    at_peak = rv21.where(mask).rolling(YDAYS, min_periods=WDAYS).mean()
    off_peak = rv21.where(~mask).rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(at_peak, off_peak).diff()

def f35_rvre_340_jump_count_at_peak_252d_d1(close: pd.Series) -> pd.Series:
    """Count of jumps (|r| > 3*lagged-21d-sigma) at near-peak bars over 252d — jump intensity at peak."""
    r = _log_returns(close)
    sigma = r.rolling(MDAYS, min_periods=WDAYS).std().shift(1)
    is_jump = (r.abs() > 3.0 * sigma).astype(float).where(sigma.notna(), np.nan)
    mask = _near_peak_mask(close)
    return is_jump.where(mask).rolling(YDAYS, min_periods=WDAYS).sum().diff()

def f35_rvre_341_bpv_at_peak_252d_d1(close: pd.Series) -> pd.Series:
    """Mean BPV(21d) at near-peak bars over 252d — continuous-vol intensity at peak."""
    r = _log_returns(close)
    bpv = _bpv(r, MDAYS, WDAYS)
    mask = _near_peak_mask(close)
    return bpv.where(mask).rolling(YDAYS, min_periods=WDAYS).mean().diff()

def f35_rvre_342_har_forecast_residual_at_peak_252d_d1(close: pd.Series) -> pd.Series:
    """Mean HAR forecast residual (forecast - realized) at near-peak bars over 252d — model surprise at peak."""
    r = _log_returns(close)
    rv_d = r ** 2
    rv_w = rv_d.rolling(WDAYS, min_periods=2).mean()
    rv_m = rv_d.rolling(22, min_periods=WDAYS).mean()
    b0, b1, b2, b3 = _har_coefs_window(close, YDAYS)
    fc = b0 + b1 * rv_d.shift(1) + b2 * rv_w.shift(1) + b3 * rv_m.shift(1)
    resid = fc - rv_d
    mask = _near_peak_mask(close)
    return resid.where(mask).rolling(YDAYS, min_periods=WDAYS).mean().diff()

def f35_rvre_343_vol_overshoot_at_peak_252d_d1(close: pd.Series) -> pd.Series:
    """Mean (RV21 / long-run-mean-RV21) at near-peak bars over 252d — vol-overshoot factor at peak."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    long_run = rv21.rolling(DDAYS_2Y, min_periods=YDAYS).mean()
    overshoot = _safe_div(rv21, long_run)
    mask = _near_peak_mask(close)
    return overshoot.where(mask).rolling(YDAYS, min_periods=WDAYS).mean().diff()

def f35_rvre_344_leverage_corr_at_peak_252d_d1(close: pd.Series) -> pd.Series:
    """corr(r_{t-1}, |r_t|) using only near-peak bars over 252d — leverage effect strength at peak."""
    r = _log_returns(close)
    abs_r = r.abs()
    mask = _near_peak_mask(close)
    pairs = pd.concat([r.shift(1).where(mask).rename('rl'), abs_r.where(mask).rename('ar')], axis=1)
    return pairs['rl'].rolling(YDAYS, min_periods=WDAYS).corr(pairs['ar']).diff()

def f35_rvre_345_ewma_neg_var_lambda094_d1(close: pd.Series) -> pd.Series:
    """EWMA(lambda=0.94) of r^2 restricted to bars where r<0 — fast-decay downside variance."""
    r = _log_returns(close)
    neg_sq = (r ** 2).where(r < 0, 0.0)
    return neg_sq.ewm(alpha=1.0 - 0.94, adjust=False, min_periods=10).mean().diff()

def f35_rvre_346_ewma_pos_var_lambda094_d1(close: pd.Series) -> pd.Series:
    """EWMA(lambda=0.94) of r^2 restricted to bars where r>0 — fast-decay upside variance."""
    r = _log_returns(close)
    pos_sq = (r ** 2).where(r > 0, 0.0)
    return pos_sq.ewm(alpha=1.0 - 0.94, adjust=False, min_periods=10).mean().diff()

def f35_rvre_347_ewma_asymmetry_neg_over_pos_lambda094_d1(close: pd.Series) -> pd.Series:
    """EWMA-neg / EWMA-pos at lambda=0.94 — fast-decay leverage asymmetry."""
    r = _log_returns(close)
    neg = (r ** 2).where(r < 0, 0.0).ewm(alpha=0.06, adjust=False, min_periods=10).mean()
    pos = (r ** 2).where(r > 0, 0.0).ewm(alpha=0.06, adjust=False, min_periods=10).mean()
    return _safe_div(neg, pos).diff()

def f35_rvre_348_ewma_neg_var_lambda097_d1(close: pd.Series) -> pd.Series:
    """EWMA(0.97) of negative r^2 — slower-decay downside variance."""
    r = _log_returns(close)
    return (r ** 2).where(r < 0, 0.0).ewm(alpha=0.03, adjust=False, min_periods=20).mean().diff()

def f35_rvre_349_ewma_asymmetry_log_neg_minus_pos_d1(close: pd.Series) -> pd.Series:
    """log(EWMA-neg + eps) - log(EWMA-pos + eps) at lambda=0.94 — log-space leverage asymmetry."""
    r = _log_returns(close)
    neg = (r ** 2).where(r < 0, 0.0).ewm(alpha=0.06, adjust=False, min_periods=10).mean()
    pos = (r ** 2).where(r > 0, 0.0).ewm(alpha=0.06, adjust=False, min_periods=10).mean()
    return (np.log(neg + 1e-12) - np.log(pos + 1e-12)).diff()

def f35_rvre_350_vol_cycle_count_252d_d1(close: pd.Series) -> pd.Series:
    """Count of RV21 cycles (peak-trough-peak) in 252d — vol oscillation cadence."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum().values
    n = len(rv21)
    out = np.full(n, np.nan)
    for i in range(YDAYS - 1, n):
        lo = i - YDAYS + 1
        seg = rv21[lo:i + 1]
        valid = ~np.isnan(seg)
        if valid.sum() < 30:
            continue
        v = seg[valid]
        cnt = 0
        for k in range(1, len(v) - 1):
            if v[k] > v[k - 1] and v[k] > v[k + 1]:
                cnt += 1
        out[i] = float(cnt)
    return pd.Series(out, index=close.index).diff()

def f35_rvre_351_vol_zero_crossings_of_demean_252d_d1(close: pd.Series) -> pd.Series:
    """Zero-crossings of (RV21 - 252d-mean) over 252d — oscillation diagnostic."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    demean = rv21 - rv21.rolling(YDAYS, min_periods=QDAYS).mean()
    sign_changes = np.sign(demean).diff().abs() / 2.0
    return sign_changes.rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f35_rvre_352_vol_path_monotonicity_63d_d1(close: pd.Series) -> pd.Series:
    """Spearman rank correlation of RV21 with time over trailing 63d — vol monotonicity (1=monotone up, -1=down)."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()

    def _sr(w):
        v = w[~np.isnan(w)]
        if v.size < 21:
            return np.nan
        rk = v.argsort().argsort().astype(float)
        x = np.arange(v.size, dtype=float)
        xm = x.mean()
        rm = rk.mean()
        num = ((x - xm) * (rk - rm)).sum()
        den = np.sqrt(((x - xm) ** 2).sum() * ((rk - rm) ** 2).sum())
        if den == 0:
            return np.nan
        return float(num / den)
    return rv21.rolling(QDAYS, min_periods=MDAYS).apply(_sr, raw=True).diff()

def f35_rvre_353_vol_corr_with_log_price_252d_d1(close: pd.Series) -> pd.Series:
    """corr(RV21, log(close)) over 252d — does vol move with price level? Positive = vol-price coupling."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    log_close = _safe_log(close)
    pairs = pd.concat([rv21.rename('v'), log_close.rename('p')], axis=1)
    return pairs['v'].rolling(YDAYS, min_periods=QDAYS).corr(pairs['p']).diff()

def f35_rvre_354_vol_regime_entropy_252d_d1(close: pd.Series) -> pd.Series:
    """Shannon entropy of RV21 quintile-state visits in trailing 252d — regime diversity."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()

    def _ent(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        q = np.quantile(v, [0.2, 0.4, 0.6, 0.8])
        bins = np.digitize(v, q)
        _, cnts = np.unique(bins, return_counts=True)
        p = cnts / cnts.sum()
        return float(-(p * np.log2(p)).sum())
    return rv21.rolling(YDAYS, min_periods=QDAYS).apply(_ent, raw=True).diff()

def f35_rvre_355_vol_regime_dwell_concentration_252d_d1(close: pd.Series) -> pd.Series:
    """Herfindahl index of RV21-quintile visit shares in 252d — concentration of regime time (1 = single regime)."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()

    def _hhi(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        q = np.quantile(v, [0.2, 0.4, 0.6, 0.8])
        bins = np.digitize(v, q)
        _, cnts = np.unique(bins, return_counts=True)
        p = cnts / cnts.sum()
        return float((p ** 2).sum())
    return rv21.rolling(YDAYS, min_periods=QDAYS).apply(_hhi, raw=True).diff()

def f35_rvre_356_distinct_vol_regimes_visited_252d_d1(close: pd.Series) -> pd.Series:
    """Number of distinct RV21 quintiles visited in 252d (out of 5) — regime exploration breadth."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()

    def _dist(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        q = np.quantile(v, [0.2, 0.4, 0.6, 0.8])
        bins = np.digitize(v, q)
        return float(np.unique(bins).size)
    return rv21.rolling(YDAYS, min_periods=QDAYS).apply(_dist, raw=True).diff()

def f35_rvre_357_vix_proxy_30d_annualized_d1(close: pd.Series) -> pd.Series:
    """sqrt(RV30) * sqrt(252) * 100 — annualized 30-day RV in VIX-like points (no options needed)."""
    r = _log_returns(close)
    rv30 = (r ** 2).rolling(30, min_periods=10).mean()
    return (np.sqrt(rv30) * np.sqrt(252.0) * 100.0).diff()

def f35_rvre_358_vix_proxy_change_5d_d1(close: pd.Series) -> pd.Series:
    """Change in 30d VIX proxy over 5 bars — short-term implied-vol-proxy momentum."""
    r = _log_returns(close)
    rv30 = (r ** 2).rolling(30, min_periods=10).mean()
    vix = np.sqrt(rv30) * np.sqrt(252.0) * 100.0
    return (vix - vix.shift(WDAYS)).diff()

def f35_rvre_359_vix_proxy_zscore_in_252d_d1(close: pd.Series) -> pd.Series:
    """Z-score of 30d VIX proxy in 252d distribution — current 'implied' vol extremity."""
    r = _log_returns(close)
    rv30 = (r ** 2).rolling(30, min_periods=10).mean()
    vix = np.sqrt(rv30) * np.sqrt(252.0) * 100.0
    return _rolling_zscore(vix, YDAYS, min_periods=QDAYS).diff()

def f35_rvre_360_vix_proxy_above_30_indicator_d1(close: pd.Series) -> pd.Series:
    """Indicator: VIX proxy > 30 — elevated-vol regime flag (S&P 500 long-term VIX threshold; idiosyncratic vol of single stock will exceed often)."""
    r = _log_returns(close)
    rv30 = (r ** 2).rolling(30, min_periods=10).mean()
    vix = np.sqrt(rv30) * np.sqrt(252.0) * 100.0
    return (vix > 30.0).astype(float).where(vix.notna(), np.nan).diff()

def f35_rvre_361_vol_after_small_return_252d_d1(close: pd.Series) -> pd.Series:
    """Mean RV21 on days following |r_{t-1}| in bottom tercile of trailing 252d |r| — vol after calm days."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    abs_r_lag = r.abs().shift(1)
    p33 = abs_r_lag.rolling(YDAYS, min_periods=QDAYS).quantile(0.33)
    mask = abs_r_lag <= p33
    return rv21.where(mask).rolling(YDAYS, min_periods=WDAYS).mean().diff()

def f35_rvre_362_vol_after_large_return_252d_d1(close: pd.Series) -> pd.Series:
    """Mean RV21 on days following |r_{t-1}| in top tercile of trailing 252d |r| — vol after big days."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    abs_r_lag = r.abs().shift(1)
    p67 = abs_r_lag.rolling(YDAYS, min_periods=QDAYS).quantile(0.67)
    mask = abs_r_lag >= p67
    return rv21.where(mask).rolling(YDAYS, min_periods=WDAYS).mean().diff()

def f35_rvre_363_vol_response_slope_size_252d_d1(close: pd.Series) -> pd.Series:
    """OLS slope of RV21_t on |r_{t-1}| over 252d — news-impact-curve magnitude slope."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    return _rolling_beta(rv21, r.abs().shift(1), YDAYS, QDAYS).diff()

def f35_rvre_364_vol_response_convexity_252d_d1(close: pd.Series) -> pd.Series:
    """OLS slope of RV21_t on r^2_{t-1} - r^2_{t-1}^median over 252d — convex (>0) vs concave (<0) news-impact."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    rsq_lag = (r ** 2).shift(1)
    med = rsq_lag.rolling(YDAYS, min_periods=QDAYS).median()
    centered = rsq_lag - med
    return _rolling_beta(rv21, centered, YDAYS, QDAYS).diff()

def f35_rvre_365_vol_at_large_pos_vs_neg_return_diff_252d_d1(close: pd.Series) -> pd.Series:
    """Mean RV21 after large positive vs large negative returns over 252d — sign asymmetry in vol response."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    abs_r_lag = r.abs().shift(1)
    p67 = abs_r_lag.rolling(YDAYS, min_periods=QDAYS).quantile(0.67)
    big = abs_r_lag >= p67
    pos_big = big & (r.shift(1) > 0)
    neg_big = big & (r.shift(1) < 0)
    vol_pos = rv21.where(pos_big).rolling(YDAYS, min_periods=WDAYS).mean()
    vol_neg = rv21.where(neg_big).rolling(YDAYS, min_periods=WDAYS).mean()
    return (vol_neg - vol_pos).diff()

def f35_rvre_366_vol_response_intercept_252d_d1(close: pd.Series) -> pd.Series:
    """OLS intercept of RV21_t on |r_{t-1}| over 252d — base vol level when previous return is zero."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    abs_r_lag = r.abs().shift(1)
    y = rv21.values
    x = abs_r_lag.values
    n = len(y)
    out = np.full(n, np.nan)
    for i in range(YDAYS - 1, n):
        lo = i - YDAYS + 1
        m = ~(np.isnan(y[lo:i + 1]) | np.isnan(x[lo:i + 1]))
        if m.sum() < QDAYS:
            continue
        xx = x[lo:i + 1][m]
        yy = y[lo:i + 1][m]
        if xx.std() == 0:
            continue
        slope = np.cov(yy, xx, bias=False)[0, 1] / xx.var(ddof=1)
        out[i] = float(yy.mean() - slope * xx.mean())
    return pd.Series(out, index=close.index).diff()

def f35_rvre_367_vol_response_r2_size_252d_d1(close: pd.Series) -> pd.Series:
    """R^2 of RV21_t on |r_{t-1}| over 252d — explanatory power of past size for current vol."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    abs_r_lag = r.abs().shift(1)
    pairs = pd.concat([rv21.rename('y'), abs_r_lag.rename('x')], axis=1)
    return (pairs['y'].rolling(YDAYS, min_periods=QDAYS).corr(pairs['x']) ** 2).diff()

def f35_rvre_368_vol_at_zero_return_252d_d1(close: pd.Series) -> pd.Series:
    """Mean RV21 on bars where |r_{t-1}| was in bottom 5% of trailing 252d — calm-day-following vol."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    abs_r_lag = r.abs().shift(1)
    p05 = abs_r_lag.rolling(YDAYS, min_periods=QDAYS).quantile(0.05)
    mask = abs_r_lag <= p05
    return rv21.where(mask).rolling(YDAYS, min_periods=WDAYS).mean().diff()

def f35_rvre_369_har_cj_jump_dominance_at_peak_252d_d1(close: pd.Series) -> pd.Series:
    """Jump share (1 - BPV/RV) at near-peak bars — jump-driven peak indicator."""
    r = _log_returns(close)
    rv = _rv(r, YDAYS, QDAYS)
    bpv = _bpv(r, YDAYS, QDAYS)
    jshare = (1.0 - _safe_div(bpv, rv)).clip(lower=0.0)
    mask = _near_peak_mask(close)
    return jshare.where(mask).rolling(YDAYS, min_periods=WDAYS).mean().diff()

def f35_rvre_370_egarch_leverage_at_peak_252d_d1(close: pd.Series) -> pd.Series:
    """EGARCH gamma (sign response) evaluated at near-peak bars — leverage strength at peak."""
    _, _, g, _ = _egarch_proxy_coefs(close)
    mask = _near_peak_mask(close)
    return g.where(mask).diff()

def f35_rvre_371_har_persistence_at_peak_252d_d1(close: pd.Series) -> pd.Series:
    """HAR persistence (b_d + b_w + b_m) evaluated at near-peak bars — vol-persistence at peak."""
    _, b1, b2, b3 = _har_coefs_window(close, YDAYS)
    mask = _near_peak_mask(close)
    return (b1 + b2 + b3).where(mask).diff()

def f35_rvre_372_vix_proxy_at_peak_252d_d1(close: pd.Series) -> pd.Series:
    """30d VIX proxy at near-peak bars — 'implied' vol at peak."""
    r = _log_returns(close)
    rv30 = (r ** 2).rolling(30, min_periods=10).mean()
    vix = np.sqrt(rv30) * np.sqrt(252.0) * 100.0
    mask = _near_peak_mask(close)
    return vix.where(mask).diff()

def f35_rvre_373_vol_ramp_into_peak_composite_252d_d1(close: pd.Series) -> pd.Series:
    """Z-blend of vol-corr-with-price + vol-monotonicity-63d + log-vol-overshoot — vol ramping into peak."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    log_close = _safe_log(close)
    pairs = pd.concat([rv21.rename('v'), log_close.rename('p')], axis=1)
    cor = pairs['v'].rolling(YDAYS, min_periods=QDAYS).corr(pairs['p'])

    def _sr(w):
        v = w[~np.isnan(w)]
        if v.size < 21:
            return np.nan
        rk = v.argsort().argsort().astype(float)
        x = np.arange(v.size, dtype=float)
        xm = x.mean()
        rm = rk.mean()
        num = ((x - xm) * (rk - rm)).sum()
        den = np.sqrt(((x - xm) ** 2).sum() * ((rk - rm) ** 2).sum())
        if den == 0:
            return np.nan
        return float(num / den)
    mono = rv21.rolling(QDAYS, min_periods=MDAYS).apply(_sr, raw=True)
    overshoot_log = np.log(rv21 + 1e-12) - np.log(rv21.rolling(YDAYS, min_periods=QDAYS).mean() + 1e-12)
    z_c = _rolling_zscore(cor, DDAYS_2Y, min_periods=YDAYS)
    z_m = _rolling_zscore(mono, DDAYS_2Y, min_periods=YDAYS)
    z_o = _rolling_zscore(overshoot_log, DDAYS_2Y, min_periods=YDAYS)
    return ((z_c + z_m + z_o) / 3.0).diff()

def f35_rvre_374_jump_dominant_peak_composite_252d_d1(close: pd.Series) -> pd.Series:
    """Z-blend of jump share at peak + jump intensity + max jump size — jump-driven peak severity."""
    r = _log_returns(close)
    rv = _rv(r, YDAYS, QDAYS)
    bpv = _bpv(r, YDAYS, QDAYS)
    jshare = (1.0 - _safe_div(bpv, rv)).clip(lower=0.0)
    mask = _near_peak_mask(close)
    jshare_peak = jshare.where(mask).rolling(YDAYS, min_periods=WDAYS).mean()
    sigma = r.rolling(MDAYS, min_periods=WDAYS).std().shift(1)
    is_jump = (r.abs() > 3.0 * sigma).astype(float).where(sigma.notna(), np.nan)
    intensity = is_jump.rolling(YDAYS, min_periods=QDAYS).sum()
    max_jump = r.abs().where(r.abs() > 3.0 * sigma).rolling(YDAYS, min_periods=WDAYS).max()
    z_jp = _rolling_zscore(jshare_peak, DDAYS_2Y, min_periods=YDAYS)
    z_in = _rolling_zscore(intensity, DDAYS_2Y, min_periods=YDAYS)
    z_mj = _rolling_zscore(max_jump, DDAYS_2Y, min_periods=YDAYS)
    pieces = pd.concat([z_jp.rename('j'), z_in.rename('i'), z_mj.rename('m')], axis=1)
    return pieces.mean(axis=1, skipna=True).diff()

def f35_rvre_375_stuck_peak_full_vol_composite_504d_d1(close: pd.Series) -> pd.Series:
    """Master vol composite for short-side stuck-peak: blend of CARR persistence + EGARCH leverage + VIX proxy + vol-at-peak ratio.
    Components averaged with skipna."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    log_rv = np.log(rv21 + 1e-12)

    def _ac1(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        a = v[:-1]
        b = v[1:]
        if a.std() == 0 or b.std() == 0:
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    pers = log_rv.rolling(YDAYS, min_periods=QDAYS).apply(_ac1, raw=True)
    _, _, g, _ = _egarch_proxy_coefs(close)
    rv30 = (r ** 2).rolling(30, min_periods=10).mean()
    vix = np.sqrt(rv30) * np.sqrt(252.0) * 100.0
    mask = _near_peak_mask(close)
    at_peak = rv21.where(mask).rolling(YDAYS, min_periods=WDAYS).mean()
    off_peak = rv21.where(~mask).rolling(YDAYS, min_periods=QDAYS).mean()
    peak_ratio = _safe_div(at_peak, off_peak)
    z_p = _rolling_zscore(pers, DDAYS_2Y, min_periods=YDAYS)
    z_g = _rolling_zscore(-g, DDAYS_2Y, min_periods=YDAYS)
    z_v = _rolling_zscore(vix, DDAYS_2Y, min_periods=YDAYS)
    z_r = _rolling_zscore(peak_ratio, DDAYS_2Y, min_periods=YDAYS)
    pieces = pd.concat([z_p.rename('p'), z_g.rename('g'), z_v.rename('v'), z_r.rename('r')], axis=1)
    return pieces.mean(axis=1, skipna=True).diff()
REALIZED_VOLATILITY_REGIME_D1_REGISTRY_301_375 = {'f35_rvre_301_continuous_var_21d_d1': {'inputs': ['close'], 'func': f35_rvre_301_continuous_var_21d_d1}, 'f35_rvre_302_jump_var_diff_at_21d_d1': {'inputs': ['close'], 'func': f35_rvre_302_jump_var_diff_at_21d_d1}, 'f35_rvre_303_har_cj_continuous_share_weekly_d1': {'inputs': ['close'], 'func': f35_rvre_303_har_cj_continuous_share_weekly_d1}, 'f35_rvre_304_har_cj_jump_share_monthly_d1': {'inputs': ['close'], 'func': f35_rvre_304_har_cj_jump_share_monthly_d1}, 'f35_rvre_305_har_cj_jump_minus_continuous_252d_d1': {'inputs': ['close'], 'func': f35_rvre_305_har_cj_jump_minus_continuous_252d_d1}, 'f35_rvre_306_har_leverage_neg_return_term_21d_d1': {'inputs': ['close'], 'func': f35_rvre_306_har_leverage_neg_return_term_21d_d1}, 'f35_rvre_307_har_leverage_pos_return_term_21d_d1': {'inputs': ['close'], 'func': f35_rvre_307_har_leverage_pos_return_term_21d_d1}, 'f35_rvre_308_har_s_asymmetry_252d_d1': {'inputs': ['close'], 'func': f35_rvre_308_har_s_asymmetry_252d_d1}, 'f35_rvre_309_har_s_leverage_beta_252d_d1': {'inputs': ['close'], 'func': f35_rvre_309_har_s_leverage_beta_252d_d1}, 'f35_rvre_310_neg_return_var_share_252d_d1': {'inputs': ['close'], 'func': f35_rvre_310_neg_return_var_share_252d_d1}, 'f35_rvre_311_har_persistence_b_d_plus_b_w_plus_b_m_252d_d1': {'inputs': ['close'], 'func': f35_rvre_311_har_persistence_b_d_plus_b_w_plus_b_m_252d_d1}, 'f35_rvre_312_har_intercept_252d_d1': {'inputs': ['close'], 'func': f35_rvre_312_har_intercept_252d_d1}, 'f35_rvre_313_har_b_d_weight_252d_d1': {'inputs': ['close'], 'func': f35_rvre_313_har_b_d_weight_252d_d1}, 'f35_rvre_314_har_b_m_weight_252d_d1': {'inputs': ['close'], 'func': f35_rvre_314_har_b_m_weight_252d_d1}, 'f35_rvre_315_har_5_step_implied_vol_252d_d1': {'inputs': ['close'], 'func': f35_rvre_315_har_5_step_implied_vol_252d_d1}, 'f35_rvre_316_mean_jump_size_252d_d1': {'inputs': ['close'], 'func': f35_rvre_316_mean_jump_size_252d_d1}, 'f35_rvre_317_std_jump_size_252d_d1': {'inputs': ['close'], 'func': f35_rvre_317_std_jump_size_252d_d1}, 'f35_rvre_318_max_jump_size_252d_d1': {'inputs': ['close'], 'func': f35_rvre_318_max_jump_size_252d_d1}, 'f35_rvre_319_jump_intensity_per_year_252d_d1': {'inputs': ['close'], 'func': f35_rvre_319_jump_intensity_per_year_252d_d1}, 'f35_rvre_320_jump_signed_skew_252d_d1': {'inputs': ['close'], 'func': f35_rvre_320_jump_signed_skew_252d_d1}, 'f35_rvre_321_mean_jump_interarrival_252d_d1': {'inputs': ['close'], 'func': f35_rvre_321_mean_jump_interarrival_252d_d1}, 'f35_rvre_322_bars_since_last_jump_d1': {'inputs': ['close'], 'func': f35_rvre_322_bars_since_last_jump_d1}, 'f35_rvre_323_jump_neg_minus_pos_count_252d_d1': {'inputs': ['close'], 'func': f35_rvre_323_jump_neg_minus_pos_count_252d_d1}, 'f35_rvre_324_tbpv_21d_k3_d1': {'inputs': ['close'], 'func': f35_rvre_324_tbpv_21d_k3_d1}, 'f35_rvre_325_tbpv_252d_k3_d1': {'inputs': ['close'], 'func': f35_rvre_325_tbpv_252d_k3_d1}, 'f35_rvre_326_tbpv_minus_bpv_252d_d1': {'inputs': ['close'], 'func': f35_rvre_326_tbpv_minus_bpv_252d_d1}, 'f35_rvre_327_threshold_jump_share_252d_d1': {'inputs': ['close'], 'func': f35_rvre_327_threshold_jump_share_252d_d1}, 'f35_rvre_328_carr_alpha_252d_d1': {'inputs': ['high', 'low'], 'func': f35_rvre_328_carr_alpha_252d_d1}, 'f35_rvre_329_carr_beta_252d_d1': {'inputs': ['high', 'low'], 'func': f35_rvre_329_carr_beta_252d_d1}, 'f35_rvre_330_carr_persistence_alpha_plus_beta_252d_d1': {'inputs': ['high', 'low'], 'func': f35_rvre_330_carr_persistence_alpha_plus_beta_252d_d1}, 'f35_rvre_331_carr_omega_252d_d1': {'inputs': ['high', 'low'], 'func': f35_rvre_331_carr_omega_252d_d1}, 'f35_rvre_332_carr_implied_long_run_log_hl_d1': {'inputs': ['high', 'low'], 'func': f35_rvre_332_carr_implied_long_run_log_hl_d1}, 'f35_rvre_333_egarch_alpha_252d_d1': {'inputs': ['close'], 'func': f35_rvre_333_egarch_alpha_252d_d1}, 'f35_rvre_334_egarch_gamma_252d_d1': {'inputs': ['close'], 'func': f35_rvre_334_egarch_gamma_252d_d1}, 'f35_rvre_335_egarch_beta_252d_d1': {'inputs': ['close'], 'func': f35_rvre_335_egarch_beta_252d_d1}, 'f35_rvre_336_egarch_asymmetry_strength_252d_d1': {'inputs': ['close'], 'func': f35_rvre_336_egarch_asymmetry_strength_252d_d1}, 'f35_rvre_337_rv21_at_peak_mean_252d_d1': {'inputs': ['close'], 'func': f35_rvre_337_rv21_at_peak_mean_252d_d1}, 'f35_rvre_338_rv21_at_peak_std_252d_d1': {'inputs': ['close'], 'func': f35_rvre_338_rv21_at_peak_std_252d_d1}, 'f35_rvre_339_rv21_at_peak_vs_off_peak_ratio_252d_d1': {'inputs': ['close'], 'func': f35_rvre_339_rv21_at_peak_vs_off_peak_ratio_252d_d1}, 'f35_rvre_340_jump_count_at_peak_252d_d1': {'inputs': ['close'], 'func': f35_rvre_340_jump_count_at_peak_252d_d1}, 'f35_rvre_341_bpv_at_peak_252d_d1': {'inputs': ['close'], 'func': f35_rvre_341_bpv_at_peak_252d_d1}, 'f35_rvre_342_har_forecast_residual_at_peak_252d_d1': {'inputs': ['close'], 'func': f35_rvre_342_har_forecast_residual_at_peak_252d_d1}, 'f35_rvre_343_vol_overshoot_at_peak_252d_d1': {'inputs': ['close'], 'func': f35_rvre_343_vol_overshoot_at_peak_252d_d1}, 'f35_rvre_344_leverage_corr_at_peak_252d_d1': {'inputs': ['close'], 'func': f35_rvre_344_leverage_corr_at_peak_252d_d1}, 'f35_rvre_345_ewma_neg_var_lambda094_d1': {'inputs': ['close'], 'func': f35_rvre_345_ewma_neg_var_lambda094_d1}, 'f35_rvre_346_ewma_pos_var_lambda094_d1': {'inputs': ['close'], 'func': f35_rvre_346_ewma_pos_var_lambda094_d1}, 'f35_rvre_347_ewma_asymmetry_neg_over_pos_lambda094_d1': {'inputs': ['close'], 'func': f35_rvre_347_ewma_asymmetry_neg_over_pos_lambda094_d1}, 'f35_rvre_348_ewma_neg_var_lambda097_d1': {'inputs': ['close'], 'func': f35_rvre_348_ewma_neg_var_lambda097_d1}, 'f35_rvre_349_ewma_asymmetry_log_neg_minus_pos_d1': {'inputs': ['close'], 'func': f35_rvre_349_ewma_asymmetry_log_neg_minus_pos_d1}, 'f35_rvre_350_vol_cycle_count_252d_d1': {'inputs': ['close'], 'func': f35_rvre_350_vol_cycle_count_252d_d1}, 'f35_rvre_351_vol_zero_crossings_of_demean_252d_d1': {'inputs': ['close'], 'func': f35_rvre_351_vol_zero_crossings_of_demean_252d_d1}, 'f35_rvre_352_vol_path_monotonicity_63d_d1': {'inputs': ['close'], 'func': f35_rvre_352_vol_path_monotonicity_63d_d1}, 'f35_rvre_353_vol_corr_with_log_price_252d_d1': {'inputs': ['close'], 'func': f35_rvre_353_vol_corr_with_log_price_252d_d1}, 'f35_rvre_354_vol_regime_entropy_252d_d1': {'inputs': ['close'], 'func': f35_rvre_354_vol_regime_entropy_252d_d1}, 'f35_rvre_355_vol_regime_dwell_concentration_252d_d1': {'inputs': ['close'], 'func': f35_rvre_355_vol_regime_dwell_concentration_252d_d1}, 'f35_rvre_356_distinct_vol_regimes_visited_252d_d1': {'inputs': ['close'], 'func': f35_rvre_356_distinct_vol_regimes_visited_252d_d1}, 'f35_rvre_357_vix_proxy_30d_annualized_d1': {'inputs': ['close'], 'func': f35_rvre_357_vix_proxy_30d_annualized_d1}, 'f35_rvre_358_vix_proxy_change_5d_d1': {'inputs': ['close'], 'func': f35_rvre_358_vix_proxy_change_5d_d1}, 'f35_rvre_359_vix_proxy_zscore_in_252d_d1': {'inputs': ['close'], 'func': f35_rvre_359_vix_proxy_zscore_in_252d_d1}, 'f35_rvre_360_vix_proxy_above_30_indicator_d1': {'inputs': ['close'], 'func': f35_rvre_360_vix_proxy_above_30_indicator_d1}, 'f35_rvre_361_vol_after_small_return_252d_d1': {'inputs': ['close'], 'func': f35_rvre_361_vol_after_small_return_252d_d1}, 'f35_rvre_362_vol_after_large_return_252d_d1': {'inputs': ['close'], 'func': f35_rvre_362_vol_after_large_return_252d_d1}, 'f35_rvre_363_vol_response_slope_size_252d_d1': {'inputs': ['close'], 'func': f35_rvre_363_vol_response_slope_size_252d_d1}, 'f35_rvre_364_vol_response_convexity_252d_d1': {'inputs': ['close'], 'func': f35_rvre_364_vol_response_convexity_252d_d1}, 'f35_rvre_365_vol_at_large_pos_vs_neg_return_diff_252d_d1': {'inputs': ['close'], 'func': f35_rvre_365_vol_at_large_pos_vs_neg_return_diff_252d_d1}, 'f35_rvre_366_vol_response_intercept_252d_d1': {'inputs': ['close'], 'func': f35_rvre_366_vol_response_intercept_252d_d1}, 'f35_rvre_367_vol_response_r2_size_252d_d1': {'inputs': ['close'], 'func': f35_rvre_367_vol_response_r2_size_252d_d1}, 'f35_rvre_368_vol_at_zero_return_252d_d1': {'inputs': ['close'], 'func': f35_rvre_368_vol_at_zero_return_252d_d1}, 'f35_rvre_369_har_cj_jump_dominance_at_peak_252d_d1': {'inputs': ['close'], 'func': f35_rvre_369_har_cj_jump_dominance_at_peak_252d_d1}, 'f35_rvre_370_egarch_leverage_at_peak_252d_d1': {'inputs': ['close'], 'func': f35_rvre_370_egarch_leverage_at_peak_252d_d1}, 'f35_rvre_371_har_persistence_at_peak_252d_d1': {'inputs': ['close'], 'func': f35_rvre_371_har_persistence_at_peak_252d_d1}, 'f35_rvre_372_vix_proxy_at_peak_252d_d1': {'inputs': ['close'], 'func': f35_rvre_372_vix_proxy_at_peak_252d_d1}, 'f35_rvre_373_vol_ramp_into_peak_composite_252d_d1': {'inputs': ['close'], 'func': f35_rvre_373_vol_ramp_into_peak_composite_252d_d1}, 'f35_rvre_374_jump_dominant_peak_composite_252d_d1': {'inputs': ['close'], 'func': f35_rvre_374_jump_dominant_peak_composite_252d_d1}, 'f35_rvre_375_stuck_peak_full_vol_composite_504d_d1': {'inputs': ['close'], 'func': f35_rvre_375_stuck_peak_full_vol_composite_504d_d1}}