"""35_realized_volatility_regime d2 features 226-300 — order-2 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff().diff(). Self-contained; helpers redefined locally per HANDOFF."""
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

def _ols_2var(y: np.ndarray, x1: np.ndarray, x2: np.ndarray):
    """OLS of y on [1, x1, x2]. Returns (intercept, b1, b2) or (nan, nan, nan) if singular."""
    mask = ~(np.isnan(y) | np.isnan(x1) | np.isnan(x2))
    if mask.sum() < 10:
        return (np.nan, np.nan, np.nan)
    y, x1, x2 = (y[mask], x1[mask], x2[mask])
    X = np.column_stack([np.ones_like(y), x1, x2])
    try:
        beta, *_ = np.linalg.lstsq(X, y, rcond=None)
        return (float(beta[0]), float(beta[1]), float(beta[2]))
    except np.linalg.LinAlgError:
        return (np.nan, np.nan, np.nan)

def _ols_3var(y: np.ndarray, x1: np.ndarray, x2: np.ndarray, x3: np.ndarray):
    mask = ~(np.isnan(y) | np.isnan(x1) | np.isnan(x2) | np.isnan(x3))
    if mask.sum() < 15:
        return (np.nan, np.nan, np.nan, np.nan)
    y, x1, x2, x3 = (y[mask], x1[mask], x2[mask], x3[mask])
    X = np.column_stack([np.ones_like(y), x1, x2, x3])
    try:
        beta, *_ = np.linalg.lstsq(X, y, rcond=None)
        return (float(beta[0]), float(beta[1]), float(beta[2]), float(beta[3]))
    except np.linalg.LinAlgError:
        return (np.nan, np.nan, np.nan, np.nan)

def _garch_coefs(close: pd.Series, win: int=YDAYS, mp: int=QDAYS):
    """Return per-bar (omega, alpha, beta) by rolling OLS of RV21 on lagged r^2 and lagged RV21."""
    r = _log_returns(close)
    rv = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    y = rv.values
    x1 = (r ** 2).shift(1).values
    x2 = rv.shift(1).values
    n = len(y)
    omega = np.full(n, np.nan)
    alpha = np.full(n, np.nan)
    beta = np.full(n, np.nan)
    for i in range(win - 1, n):
        lo = i - win + 1
        w, a, b = _ols_2var(y[lo:i + 1], x1[lo:i + 1], x2[lo:i + 1])
        omega[i] = w
        alpha[i] = a
        beta[i] = b
    return (pd.Series(omega, index=close.index), pd.Series(alpha, index=close.index), pd.Series(beta, index=close.index))

def _har_one_step_forecast(close: pd.Series, win: int=YDAYS, mp: int=QDAYS) -> pd.Series:
    """One-step-ahead HAR-RV forecast using rolling-OLS coefficients on lagged d/w/m components."""
    r = _log_returns(close)
    rv_d = r ** 2
    rv_w = rv_d.rolling(WDAYS, min_periods=2).mean()
    rv_m = rv_d.rolling(22, min_periods=WDAYS).mean()
    y = rv_d.values
    x1 = rv_d.shift(1).values
    x2 = rv_w.shift(1).values
    x3 = rv_m.shift(1).values
    n = len(y)
    fc = np.full(n, np.nan)
    for i in range(win, n):
        lo = i - win
        b0, b1, b2, b3 = _ols_3var(y[lo:i], x1[lo:i], x2[lo:i], x3[lo:i])
        if not np.isnan(b0):
            fc[i] = b0 + b1 * rv_d.iat[i - 1] + b2 * rv_w.iat[i - 1] + b3 * rv_m.iat[i - 1]
    return pd.Series(fc, index=close.index)

def _arch_lm(r: pd.Series, lag: int, win: int, mp: int) -> pd.Series:
    """ARCH-LM test stat at given lag: T*R^2 from regressing r^2 on its 1..lag lags."""
    rsq = r ** 2
    arr = rsq.values
    n = len(arr)
    out = np.full(n, np.nan)
    for i in range(win - 1, n):
        lo = i - win + 1
        v = arr[lo:i + 1]
        v = v[~np.isnan(v)]
        if v.size < max(mp, 30 + lag):
            continue
        y = v[lag:]
        X = np.column_stack([np.ones(y.size)] + [v[lag - k:-k] if k > 0 else v[lag:] for k in range(1, lag + 1)])
        try:
            beta, _, _, _ = np.linalg.lstsq(X, y, rcond=None)
            yhat = X @ beta
            ssr = ((y - yhat) ** 2).sum()
            sst = ((y - y.mean()) ** 2).sum()
            r2 = 1.0 - ssr / sst if sst > 0 else 0.0
            out[i] = y.size * r2
        except np.linalg.LinAlgError:
            continue
    return pd.Series(out, index=r.index)

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

def _parkinson_sigma(high: pd.Series, low: pd.Series, n: int, mp: int) -> pd.Series:
    """Parkinson sigma at horizon n (per-day, not annualized)."""
    k = 1.0 / (4.0 * np.log(2.0))
    var = (np.log(_safe_div(high, low)) ** 2).rolling(n, min_periods=mp).mean() * k
    return np.sqrt(var.where(var > 0))

def f35_rvre_226_garch_alpha_252d_d2(close: pd.Series) -> pd.Series:
    """Rolling-OLS GARCH(1,1) alpha coefficient over 252d — shock-impact parameter on RV21."""
    _, a, _ = _garch_coefs(close)
    return a.diff().diff()

def f35_rvre_227_garch_beta_252d_d2(close: pd.Series) -> pd.Series:
    """Rolling-OLS GARCH(1,1) beta coefficient over 252d — vol-persistence parameter on RV21."""
    _, _, b = _garch_coefs(close)
    return b.diff().diff()

def f35_rvre_228_garch_persistence_alpha_plus_beta_252d_d2(close: pd.Series) -> pd.Series:
    """alpha + beta from rolling-OLS GARCH(1,1) — total vol persistence; > 1 indicates non-stationarity."""
    _, a, b = _garch_coefs(close)
    return (a + b).diff().diff()

def f35_rvre_229_garch_omega_252d_d2(close: pd.Series) -> pd.Series:
    """Intercept (omega) from rolling-OLS GARCH(1,1) — long-run-vol scale parameter."""
    w, _, _ = _garch_coefs(close)
    return w.diff().diff()

def f35_rvre_230_garch_long_run_variance_252d_d2(close: pd.Series) -> pd.Series:
    """omega / (1 - alpha - beta) — implied long-run unconditional variance from rolling GARCH params."""
    w, a, b = _garch_coefs(close)
    denom = 1.0 - (a + b)
    return _safe_div(w, denom.where(denom > 0)).diff().diff()

def f35_rvre_231_garch_one_step_forecast_252d_d2(close: pd.Series) -> pd.Series:
    """One-step-ahead RV forecast from rolling GARCH params: omega + alpha*r^2_t + beta*RV21_t."""
    w, a, b = _garch_coefs(close)
    r = _log_returns(close)
    rv = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    return (w + a * r ** 2 + b * rv).diff().diff()

def f35_rvre_232_gjr_gamma_asymmetric_term_252d_d2(close: pd.Series) -> pd.Series:
    """GJR-GARCH asymmetric coefficient gamma via rolling OLS:
    RV21_t = omega + alpha*r^2_{t-1} + gamma*r^2_{t-1}*I{r_{t-1}<0} + beta*RV21_{t-1}.
    Returns gamma — positive value indicates leverage effect."""
    r = _log_returns(close)
    rv = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    y = rv.values
    rsq_lag = (r ** 2).shift(1).values
    neg_indicator_lag = (r.shift(1) < 0).astype(float).values
    asym_lag = rsq_lag * neg_indicator_lag
    rv_lag = rv.shift(1).values
    n = len(y)
    out = np.full(n, np.nan)
    for i in range(YDAYS - 1, n):
        lo = i - YDAYS + 1
        _, _, g, _ = _ols_3var(y[lo:i + 1], rsq_lag[lo:i + 1], asym_lag[lo:i + 1], rv_lag[lo:i + 1])
        out[i] = g
    return pd.Series(out, index=close.index).diff().diff()

def f35_rvre_233_arch_persistence_proxy_lag1_corr_rsq_252d_d2(close: pd.Series) -> pd.Series:
    """Cheap GARCH-persistence proxy: lag-1 autocorrelation of r^2 over 252d (= alpha+beta in degenerate GARCH)."""
    r = _log_returns(close)
    rsq = r ** 2

    def _ac(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        a = v[:-1]
        b = v[1:]
        if a.std() == 0 or b.std() == 0:
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    return rsq.rolling(YDAYS, min_periods=QDAYS).apply(_ac, raw=True).diff().diff()

def f35_rvre_234_leverage_corr_lag1_252d_d2(close: pd.Series) -> pd.Series:
    """corr(r_{t-1}, |r_t|) over 252d — leverage-effect strength; negative = leverage effect present."""
    r = _log_returns(close)
    abs_r = r.abs()

    def _lc(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        n2 = v.size // 2
        a = v[:n2]
        b = v[n2:n2 * 2]
        if a.std() == 0 or b.std() == 0:
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    pairs = pd.concat([r.shift(1).rename('rlag'), abs_r.rename('absr')], axis=1)
    return pairs['rlag'].rolling(YDAYS, min_periods=QDAYS).corr(pairs['absr']).diff().diff()

def f35_rvre_235_leverage_corr_lag1_504d_d2(close: pd.Series) -> pd.Series:
    """corr(r_{t-1}, |r_t|) over 504d — long-window leverage-effect measure."""
    r = _log_returns(close)
    pairs = pd.concat([r.shift(1).rename('rlag'), r.abs().rename('absr')], axis=1)
    return pairs['rlag'].rolling(DDAYS_2Y, min_periods=YDAYS).corr(pairs['absr']).diff().diff()

def f35_rvre_236_leverage_corr_r_with_rv21_lead_252d_d2(close: pd.Series) -> pd.Series:
    """corr(r_t, RV21_{t+1}) over 252d — direct contemporaneous leverage indicator at vol horizon."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    pairs = pd.concat([r.rename('r'), rv21.shift(1).rename('rvlead')], axis=1)
    pairs = pd.concat([r.shift(1).rename('rlag'), rv21.rename('rv')], axis=1)
    return pairs['rlag'].rolling(YDAYS, min_periods=QDAYS).corr(pairs['rv']).diff().diff()

def f35_rvre_237_vol_response_after_down_day_252d_d2(close: pd.Series) -> pd.Series:
    """Mean RV21 on days following a -2sigma return over 252d — conditional vol after bad news.
    min_periods=5 because qualifying events are sparse — 5+ -2sigma days gives a usable mean."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    sd = r.rolling(MDAYS, min_periods=WDAYS).std()
    bad_yday = r.shift(1) < -2.0 * sd.shift(1)
    return rv21.where(bad_yday).rolling(YDAYS, min_periods=WDAYS).mean().diff().diff()

def f35_rvre_238_vol_response_after_up_day_252d_d2(close: pd.Series) -> pd.Series:
    """Mean RV21 on days following a +2sigma return over 252d — conditional vol after good news."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    sd = r.rolling(MDAYS, min_periods=WDAYS).std()
    good_yday = r.shift(1) > 2.0 * sd.shift(1)
    return rv21.where(good_yday).rolling(YDAYS, min_periods=WDAYS).mean().diff().diff()

def f35_rvre_239_asymmetric_vol_response_gap_252d_d2(close: pd.Series) -> pd.Series:
    """Vol after big down day - vol after big up day over 252d — direct leverage-effect magnitude."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    sd = r.rolling(MDAYS, min_periods=WDAYS).std()
    down = rv21.where(r.shift(1) < -2.0 * sd.shift(1)).rolling(YDAYS, min_periods=WDAYS).mean()
    up = rv21.where(r.shift(1) > 2.0 * sd.shift(1)).rolling(YDAYS, min_periods=WDAYS).mean()
    return (down - up).diff().diff()

def f35_rvre_240_vol_amplification_ratio_after_down_252d_d2(close: pd.Series) -> pd.Series:
    """Mean(RV21_t / RV21_{t-1}) on bars where r_{t-1} < 0 over 252d — bigger-than-1 = vol amplifies on bad news."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    ratio = _safe_div(rv21, rv21.shift(1))
    return ratio.where(r.shift(1) < 0).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f35_rvre_241_vol_amplification_ratio_after_up_252d_d2(close: pd.Series) -> pd.Series:
    """Mean(RV21_t / RV21_{t-1}) on bars where r_{t-1} > 0 over 252d — vol-amplification on up days."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    ratio = _safe_div(rv21, rv21.shift(1))
    return ratio.where(r.shift(1) > 0).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f35_rvre_242_leverage_gap_amplification_252d_d2(close: pd.Series) -> pd.Series:
    """Vol-amplification(down) - vol-amplification(up) over 252d — leverage effect on the multiplicative scale."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    ratio = _safe_div(rv21, rv21.shift(1))
    down = ratio.where(r.shift(1) < 0).rolling(YDAYS, min_periods=QDAYS).mean()
    up = ratio.where(r.shift(1) > 0).rolling(YDAYS, min_periods=QDAYS).mean()
    return (down - up).diff().diff()

def f35_rvre_243_corr_neg_r_with_rv_change_252d_d2(close: pd.Series) -> pd.Series:
    """corr(r_{t-1} where r<0, RV21_t - RV21_{t-1}) over 252d — direct downside-shock vs vol-change linkage."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    drv = rv21.diff()
    r_neg = r.where(r < 0).shift(1)
    pairs = pd.concat([r_neg.rename('rn'), drv.rename('d')], axis=1)
    return pairs['rn'].rolling(YDAYS, min_periods=QDAYS).corr(pairs['d']).diff().diff()

def f35_rvre_244_har_one_step_forecast_252d_d2(close: pd.Series) -> pd.Series:
    """HAR-RV one-step-ahead forecast (Corsi 2009) using 252d rolling OLS — quant practitioner's vol forecast."""
    return _har_one_step_forecast(close, YDAYS, QDAYS).diff().diff()

def f35_rvre_245_har_forecast_error_252d_d2(close: pd.Series) -> pd.Series:
    """HAR forecast - realized r^2 — signed forecast error (positive = over-forecasted vol)."""
    r = _log_returns(close)
    rv_d = r ** 2
    fc = _har_one_step_forecast(close, YDAYS, QDAYS)
    return (fc - rv_d).diff().diff()

def f35_rvre_246_har_forecast_abs_error_252d_d2(close: pd.Series) -> pd.Series:
    """|HAR forecast - realized r^2| — absolute forecast error magnitude."""
    r = _log_returns(close)
    rv_d = r ** 2
    fc = _har_one_step_forecast(close, YDAYS, QDAYS)
    return (fc - rv_d).abs().diff().diff()

def f35_rvre_247_har_forecast_mse_63d_d2(close: pd.Series) -> pd.Series:
    """63d rolling mean-squared HAR forecast error — recent forecast quality (lower = better)."""
    r = _log_returns(close)
    rv_d = r ** 2
    fc = _har_one_step_forecast(close, YDAYS, QDAYS)
    err_sq = (fc - rv_d) ** 2
    return err_sq.rolling(QDAYS, min_periods=MDAYS).mean().diff().diff()

def f35_rvre_248_har_forecast_bias_63d_d2(close: pd.Series) -> pd.Series:
    """63d mean of HAR forecast error — positive = HAR systematically over-forecasts."""
    r = _log_returns(close)
    rv_d = r ** 2
    fc = _har_one_step_forecast(close, YDAYS, QDAYS)
    err = fc - rv_d
    return err.rolling(QDAYS, min_periods=MDAYS).mean().diff().diff()

def f35_rvre_249_har_vs_naive_skill_ratio_63d_d2(close: pd.Series) -> pd.Series:
    """1 - MSE(HAR) / MSE(naive=lag1) over 63d — Theil U2 style; >0 means HAR beats naive."""
    r = _log_returns(close)
    rv_d = r ** 2
    fc = _har_one_step_forecast(close, YDAYS, QDAYS)
    err_har = (fc - rv_d) ** 2
    err_naive = (rv_d.shift(1) - rv_d) ** 2
    mse_har = err_har.rolling(QDAYS, min_periods=MDAYS).mean()
    mse_naive = err_naive.rolling(QDAYS, min_periods=MDAYS).mean()
    return (1.0 - _safe_div(mse_har, mse_naive)).diff().diff()

def f35_rvre_250_har_forecast_direction_hit_rate_63d_d2(close: pd.Series) -> pd.Series:
    """Hit rate (fraction) where sign(HAR forecast - lag-RV) == sign(realized RV change) over 63d."""
    r = _log_returns(close)
    rv_d = r ** 2
    fc = _har_one_step_forecast(close, YDAYS, QDAYS)
    pred_dir = np.sign(fc - rv_d.shift(1))
    real_dir = np.sign(rv_d.diff())
    hit = (pred_dir == real_dir).astype(float).where(pred_dir.notna() & real_dir.notna(), np.nan)
    return hit.rolling(QDAYS, min_periods=MDAYS).mean().diff().diff()

def f35_rvre_251_har_forecast_minus_realized_smoothed_21d_d2(close: pd.Series) -> pd.Series:
    """21d EWMA of (HAR forecast - realized) — smoothed forecast bias; persistent positives = persistently overestimating."""
    r = _log_returns(close)
    rv_d = r ** 2
    fc = _har_one_step_forecast(close, YDAYS, QDAYS)
    return (fc - rv_d).ewm(span=MDAYS, adjust=False, min_periods=WDAYS).mean().diff().diff()

def f35_rvre_252_har_forecast_z_score_in_252d_d2(close: pd.Series) -> pd.Series:
    """Z-score of HAR forecast in its own 252d distribution — current forecast extremity vs recent forecasts."""
    fc = _har_one_step_forecast(close, YDAYS, QDAYS)
    return _rolling_zscore(fc, YDAYS, min_periods=QDAYS).diff().diff()

def f35_rvre_253_har_forecast_vs_ewma094_ratio_d2(close: pd.Series) -> pd.Series:
    """HAR forecast / EWMA(0.94) variance — agreement between two industry vol forecasters."""
    r = _log_returns(close)
    fc = _har_one_step_forecast(close, YDAYS, QDAYS)
    ew = (r ** 2).ewm(alpha=1.0 - 0.94, adjust=False, min_periods=10).mean()
    return _safe_div(fc, ew).diff().diff()

def f35_rvre_254_vol_half_life_from_ac1_252d_d2(close: pd.Series) -> pd.Series:
    """Vol shock half-life (bars) = -ln(2)/ln(AR1 coef of log RV21) — speed of vol-shock decay."""
    r = _log_returns(close)
    log_rv21 = np.log((r ** 2).rolling(MDAYS, min_periods=WDAYS).sum() + 1e-12)

    def _ac1(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        a = v[:-1]
        b = v[1:]
        if a.std() == 0 or b.std() == 0:
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    ac1 = log_rv21.rolling(YDAYS, min_periods=QDAYS).apply(_ac1, raw=True)
    return (-np.log(2.0) / np.log(ac1.where((ac1 > 0) & (ac1 < 1)))).diff().diff()

def f35_rvre_255_vol_mean_reversion_speed_252d_d2(close: pd.Series) -> pd.Series:
    """OU mean-reversion speed kappa for log RV21: dx = kappa*(theta-x)dt + sigma dW.
    Proxy: kappa ~ -ln(AR1 coef) — bars-per-shock-half."""
    r = _log_returns(close)
    log_rv21 = np.log((r ** 2).rolling(MDAYS, min_periods=WDAYS).sum() + 1e-12)

    def _ac1(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        a = v[:-1]
        b = v[1:]
        if a.std() == 0 or b.std() == 0:
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    ac1 = log_rv21.rolling(YDAYS, min_periods=QDAYS).apply(_ac1, raw=True)
    return (-np.log(ac1.where((ac1 > 0) & (ac1 < 1)))).diff().diff()

def f35_rvre_256_vol_overshoot_ratio_252d_d2(close: pd.Series) -> pd.Series:
    """Current RV21 / 252d-mean RV21 — degree to which vol is above long-run average."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(rv21, rv21.rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff()

def f35_rvre_257_vol_overshoot_ratio_504d_d2(close: pd.Series) -> pd.Series:
    """Current RV21 / 504d-mean RV21 — longer-baseline overshoot."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(rv21, rv21.rolling(DDAYS_2Y, min_periods=YDAYS).mean()).diff().diff()

def f35_rvre_258_log_vol_overshoot_252d_d2(close: pd.Series) -> pd.Series:
    """log(RV21) - log(mean RV21_252d) — additive overshoot in log space (more linear ML signal)."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    return (np.log(rv21 + 1e-12) - np.log(rv21.rolling(YDAYS, min_periods=QDAYS).mean() + 1e-12)).diff().diff()

def f35_rvre_259_vol_undershoot_indicator_252d_d2(close: pd.Series) -> pd.Series:
    """Indicator: RV21 < 0.5 * 252d-mean RV21 — vol meaningfully suppressed below baseline (calm-before-storm proxy)."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    baseline = rv21.rolling(YDAYS, min_periods=QDAYS).mean()
    return (rv21 < 0.5 * baseline).astype(float).where(baseline.notna() & rv21.notna(), np.nan).diff().diff()

def f35_rvre_260_consecutive_top_quartile_vol_streak_d2(close: pd.Series) -> pd.Series:
    """Current consecutive-bar streak where RV21 is in top quartile (>p75) of 504d distribution."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    q75 = rv21.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.75)
    flag = (rv21 > q75).values
    n = len(flag)
    out = np.full(n, np.nan)
    streak = 0
    for i in range(n):
        if np.isnan(rv21.iat[i]) or np.isnan(q75.iat[i]):
            out[i] = np.nan
            streak = 0
        else:
            streak = streak + 1 if flag[i] else 0
            out[i] = float(streak)
    return pd.Series(out, index=close.index).diff().diff()

def f35_rvre_261_consecutive_bottom_quartile_vol_streak_d2(close: pd.Series) -> pd.Series:
    """Current consecutive-bar streak where RV21 is in bottom quartile (<p25) of 504d distribution."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    q25 = rv21.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.25)
    flag = (rv21 < q25).values
    n = len(flag)
    out = np.full(n, np.nan)
    streak = 0
    for i in range(n):
        if np.isnan(rv21.iat[i]) or np.isnan(q25.iat[i]):
            out[i] = np.nan
            streak = 0
        else:
            streak = streak + 1 if flag[i] else 0
            out[i] = float(streak)
    return pd.Series(out, index=close.index).diff().diff()

def f35_rvre_262_fraction_bars_in_top_quartile_vol_252d_d2(close: pd.Series) -> pd.Series:
    """Fraction of trailing 252d where RV21 was in top quartile (>p75) of 504d distribution — sustained-stress share."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    q75 = rv21.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.75)
    flag = (rv21 > q75).astype(float).where(q75.notna(), np.nan)
    return flag.rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f35_rvre_263_count_high_vol_clusters_252d_d2(close: pd.Series) -> pd.Series:
    """Number of *new* entries into top-quartile vol state in trailing 252d — count of distinct stress events."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    q75 = rv21.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.75)
    in_top = rv21 > q75
    entered = in_top & ~in_top.shift(1, fill_value=False)
    return entered.astype(float).where(rv21.notna() & q75.notna(), np.nan).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f35_rvre_264_mean_high_vol_cluster_duration_252d_d2(close: pd.Series) -> pd.Series:
    """Mean duration (bars) of top-quartile vol clusters in trailing 252d — typical-cluster-length signal."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()

    def _mean_cluster(w_rv, w_q):
        valid = ~(np.isnan(w_rv) | np.isnan(w_q))
        if valid.sum() < 30:
            return np.nan
        flag = (w_rv > w_q) & valid
        clusters = []
        cur = 0
        for f in flag:
            if f:
                cur += 1
            elif cur > 0:
                clusters.append(cur)
                cur = 0
        if cur > 0:
            clusters.append(cur)
        return float(np.mean(clusters)) if clusters else 0.0
    q75 = rv21.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.75)
    out = pd.Series(np.nan, index=close.index)
    arr_rv = rv21.values
    arr_q = q75.values
    for i in range(YDAYS - 1, len(arr_rv)):
        lo = i - YDAYS + 1
        out.iat[i] = _mean_cluster(arr_rv[lo:i + 1], arr_q[lo:i + 1])
    return out.diff().diff()

def f35_rvre_265_arch_lm_stat_lag1_252d_d2(close: pd.Series) -> pd.Series:
    """ARCH-LM test statistic at lag 1 over 252d — significance of conditional heteroskedasticity."""
    return _arch_lm(_log_returns(close), 1, YDAYS, QDAYS).diff().diff()

def f35_rvre_266_arch_lm_stat_lag5_252d_d2(close: pd.Series) -> pd.Series:
    """ARCH-LM test statistic at lag 5 over 252d — weekly-horizon heteroskedasticity test."""
    return _arch_lm(_log_returns(close), 5, YDAYS, QDAYS).diff().diff()

def f35_rvre_267_arch_lm_stat_lag21_504d_d2(close: pd.Series) -> pd.Series:
    """ARCH-LM test statistic at lag 21 over 504d — monthly-horizon heteroskedasticity test."""
    return _arch_lm(_log_returns(close), 21, DDAYS_2Y, YDAYS).diff().diff()

def f35_rvre_268_engle_ng_joint_chi_sq_252d_d2(close: pd.Series) -> pd.Series:
    """Engle-Ng joint test (sign + neg-size + pos-size biases) chi-sq statistic at 252d — composite vol-asymmetry."""
    r = _log_returns(close)

    def _joint(w):
        v = w[~np.isnan(w)]
        if v.size < 50:
            return np.nan
        rsq = v[1:] ** 2
        s_neg = (v[:-1] < 0).astype(float)
        z_neg = s_neg * v[:-1]
        z_pos = (1.0 - s_neg) * v[:-1]
        X = np.column_stack([np.ones(rsq.size), s_neg, z_neg, z_pos])
        try:
            beta, _, _, _ = np.linalg.lstsq(X, rsq, rcond=None)
            resid = rsq - X @ beta
            sigma2 = (resid ** 2).mean()
            if sigma2 == 0:
                return np.nan
            yhat = X @ beta
            ssr = ((rsq - yhat) ** 2).sum()
            sst = ((rsq - rsq.mean()) ** 2).sum()
            r2 = 1.0 - ssr / sst if sst > 0 else 0.0
            return float(rsq.size * r2)
        except np.linalg.LinAlgError:
            return np.nan
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_joint, raw=True).diff().diff()

def f35_rvre_269_bds_proxy_corr_dim_2_252d_d2(close: pd.Series) -> pd.Series:
    """Brock-Dechert-Scheinkman proxy: correlation dimension 2 of |r| — non-linearity strength."""
    r = _log_returns(close)
    abs_r = r.abs()

    def _bds(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        eps = np.std(v) * 0.5
        if eps == 0:
            return np.nan
        n = v.size - 1
        if n < 5:
            return np.nan
        v1 = v[:-1]
        v2 = v[1:]
        count = 0
        total = 0
        for k in range(n):
            d1 = np.abs(v1 - v1[k]) < eps
            d2 = np.abs(v2 - v2[k]) < eps
            count += (d1 & d2).sum()
            total += n
        return float(count / total) if total else np.nan
    return abs_r.rolling(YDAYS, min_periods=QDAYS).apply(_bds, raw=True).diff().diff()

def f35_rvre_270_beta_rv_on_lagged_rsq_252d_d2(close: pd.Series) -> pd.Series:
    """Rolling OLS beta of RV21_t on r^2_{t-1} over 252d — single-shock vol-impact magnitude."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    return _rolling_beta(rv21, (r ** 2).shift(1), YDAYS, QDAYS).diff().diff()

def f35_rvre_271_beta_rv_on_lagged_rv21_252d_d2(close: pd.Series) -> pd.Series:
    """Rolling OLS beta of RV21_t on RV21_{t-1} over 252d — vol-persistence beta in single-lag AR."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    return _rolling_beta(rv21, rv21.shift(1), YDAYS, QDAYS).diff().diff()

def f35_rvre_272_beta_rv_on_drvchange_252d_d2(close: pd.Series) -> pd.Series:
    """Rolling OLS beta of RV21_t on delta(RV21_{t-1}) over 252d — vol-acceleration carry-over."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    return _rolling_beta(rv21, rv21.diff().shift(1), YDAYS, QDAYS).diff().diff()

def f35_rvre_273_cross_horizon_convergence_speed_21_252_252d_d2(close: pd.Series) -> pd.Series:
    """Half-life (bars) of |RV21 - RV252| convergence — speed at which short-horizon vol reverts to long-horizon."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    rv252 = (r ** 2).rolling(YDAYS, min_periods=QDAYS).sum() / float(YDAYS) * float(MDAYS)
    spread = (rv21 - rv252).abs()

    def _ac1(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        a = v[:-1]
        b = v[1:]
        if a.std() == 0 or b.std() == 0:
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    ac1 = spread.rolling(YDAYS, min_periods=QDAYS).apply(_ac1, raw=True)
    return (-np.log(2.0) / np.log(ac1.where((ac1 > 0) & (ac1 < 1)))).diff().diff()

def f35_rvre_274_vol_roll_signal_rv5_minus_rv21_d2(close: pd.Series) -> pd.Series:
    """RV5 (per-day) - RV21 (per-day) — short-vs-monthly vol-curve roll signal; positive = front-month vol exceeds back."""
    r = _log_returns(close)
    rv5 = (r ** 2).rolling(WDAYS, min_periods=2).mean()
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).mean()
    return (rv5 - rv21).diff().diff()

def f35_rvre_275_vol_curve_inversion_indicator_5_21_63_d2(close: pd.Series) -> pd.Series:
    """Indicator: RV5 > RV21 > RV63 (vol curve fully inverted) — short-term shock dominates regime."""
    r = _log_returns(close)
    rv5 = (r ** 2).rolling(WDAYS, min_periods=2).mean()
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).mean()
    rv63 = (r ** 2).rolling(QDAYS, min_periods=MDAYS).mean()
    inv = (rv5 > rv21) & (rv21 > rv63)
    return inv.astype(float).where(rv5.notna() & rv21.notna() & rv63.notna(), np.nan).diff().diff()

def f35_rvre_276_vol_catchup_factor_21d_d2(close: pd.Series) -> pd.Series:
    """RV21_t / EWMA(0.94)_{t-21d} — how much vol has caught up vs 1-month-old EWMA forecast."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    ewma = (r ** 2).ewm(alpha=1.0 - 0.94, adjust=False, min_periods=10).mean()
    return _safe_div(rv21, ewma.shift(MDAYS) * MDAYS).diff().diff()

def f35_rvre_277_vol_decay_after_last_spike_252d_d2(close: pd.Series) -> pd.Series:
    """Bars since the last RV21 max in trailing 252d, as a fraction of 252 — recovery clock for vol overshoot."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()

    def _bars_since_max(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        return float(v.size - 1 - int(np.argmax(v))) / float(YDAYS)
    return rv21.rolling(YDAYS, min_periods=QDAYS).apply(_bars_since_max, raw=True).diff().diff()

def f35_rvre_278_vol_shock_magnitude_x_persistence_252d_d2(close: pd.Series) -> pd.Series:
    """max(RV21)_252d * (1 - bars_since_max / 252) — combined shock-size and recency interaction."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    rmax = rv21.rolling(YDAYS, min_periods=QDAYS).max()

    def _bars_since_max(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        return float(v.size - 1 - int(np.argmax(v))) / float(YDAYS)
    bsm = rv21.rolling(YDAYS, min_periods=QDAYS).apply(_bars_since_max, raw=True)
    return (rmax * (1.0 - bsm)).diff().diff()

def f35_rvre_279_largest_rv_jump_in_21d_in_252d_d2(close: pd.Series) -> pd.Series:
    """Largest single-day RV21 jump (RV21_t - RV21_{t-1}) seen in trailing 252d — biggest vol-shock event."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    return rv21.diff().rolling(YDAYS, min_periods=QDAYS).max().diff().diff()

def f35_rvre_280_time_between_vol_clusters_252d_d2(close: pd.Series) -> pd.Series:
    """Mean inter-arrival time (bars) between top-quartile-vol cluster *starts* in trailing 252d."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    q75 = rv21.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.75)
    flag = ((rv21 > q75) & ~(rv21.shift(1) > q75)).values
    arr_q = q75.values
    n = len(flag)
    out = np.full(n, np.nan)
    for i in range(YDAYS - 1, n):
        lo = i - YDAYS + 1
        idx = np.where(flag[lo:i + 1])[0]
        if idx.size < 2 or np.isnan(arr_q[i]):
            continue
        out[i] = float(np.diff(idx).mean())
    return pd.Series(out, index=close.index).diff().diff()

def f35_rvre_281_vol_shock_bayesian_update_factor_252d_d2(close: pd.Series) -> pd.Series:
    """Bayes-like update factor: RV21 / (alpha*RV21_lag + (1-alpha)*long_run_mean), alpha=0.94 — surprise factor."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    long_run = rv21.rolling(DDAYS_2Y, min_periods=YDAYS).mean()
    prior = 0.94 * rv21.shift(1) + 0.06 * long_run
    return _safe_div(rv21, prior).diff().diff()

def f35_rvre_282_vol_carry_rv21_minus_rv63_d2(close: pd.Series) -> pd.Series:
    """RV21 (annualized) - RV63 (annualized) — monthly minus quarterly vol carry (front-vs-back month spread)."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).mean() * 252.0
    rv63 = (r ** 2).rolling(QDAYS, min_periods=MDAYS).mean() * 252.0
    return (rv21 - rv63).diff().diff()

def f35_rvre_283_vol_carry_rv63_minus_rv252_d2(close: pd.Series) -> pd.Series:
    """RV63 (annualized) - RV252 (annualized) — quarterly minus annual vol carry."""
    r = _log_returns(close)
    rv63 = (r ** 2).rolling(QDAYS, min_periods=MDAYS).mean() * 252.0
    rv252 = (r ** 2).rolling(YDAYS, min_periods=QDAYS).mean() * 252.0
    return (rv63 - rv252).diff().diff()

def f35_rvre_284_vol_carry_log_ratio_rv21_rv63_d2(close: pd.Series) -> pd.Series:
    """log(RV21/RV63) — multiplicative vol carry between monthly and quarterly horizons."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).mean()
    rv63 = (r ** 2).rolling(QDAYS, min_periods=MDAYS).mean()
    return np.log(_safe_div(rv21, rv63)).diff().diff()

def f35_rvre_285_vol_carry_zscore_in_504d_d2(close: pd.Series) -> pd.Series:
    """Z-score of (RV21 - RV63) in 504d distribution — extremity of monthly-vs-quarterly carry."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).mean()
    rv63 = (r ** 2).rolling(QDAYS, min_periods=MDAYS).mean()
    return _rolling_zscore(rv21 - rv63, DDAYS_2Y, min_periods=YDAYS).diff().diff()

def f35_rvre_286_vol_curve_full_normal_indicator_d2(close: pd.Series) -> pd.Series:
    """Indicator: RV5 < RV21 < RV63 < RV252 (vol curve in *normal* upward-sloping shape) — calm-regime flag."""
    r = _log_returns(close)
    rv5 = (r ** 2).rolling(WDAYS, min_periods=2).mean()
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).mean()
    rv63 = (r ** 2).rolling(QDAYS, min_periods=MDAYS).mean()
    rv252 = (r ** 2).rolling(YDAYS, min_periods=QDAYS).mean()
    normal = (rv5 < rv21) & (rv21 < rv63) & (rv63 < rv252)
    return normal.astype(float).where(rv5.notna() & rv252.notna(), np.nan).diff().diff()

def f35_rvre_287_park_vs_cc_sigma_diff_21d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Parkinson sigma 21d - close-to-close sigma 21d — divergence (negative = intraday range is smaller than CC vol)."""
    r = _log_returns(close)
    cc = r.rolling(MDAYS, min_periods=WDAYS).std()
    pk = _parkinson_sigma(high, low, MDAYS, WDAYS)
    return (pk - cc).diff().diff()

def f35_rvre_288_park_vs_cc_sigma_diff_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Parkinson sigma 63d - close-to-close sigma 63d — quarterly divergence."""
    r = _log_returns(close)
    cc = r.rolling(QDAYS, min_periods=MDAYS).std()
    pk = _parkinson_sigma(high, low, QDAYS, MDAYS)
    return (pk - cc).diff().diff()

def f35_rvre_289_park_over_cc_sigma_ratio_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Parkinson sigma 252d / close-to-close sigma 252d — efficiency ratio; >1 means range vol exceeds CC vol."""
    r = _log_returns(close)
    cc = r.rolling(YDAYS, min_periods=QDAYS).std()
    pk = _parkinson_sigma(high, low, YDAYS, QDAYS)
    return _safe_div(pk, cc).diff().diff()

def f35_rvre_290_range_rv_disagreement_zscore_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score (in 252d) of (Parkinson sigma 21d - CC sigma 21d) — extremity of vol-estimator disagreement."""
    r = _log_returns(close)
    cc = r.rolling(MDAYS, min_periods=WDAYS).std()
    pk = _parkinson_sigma(high, low, MDAYS, WDAYS)
    return _rolling_zscore(pk - cc, YDAYS, min_periods=QDAYS).diff().diff()

def f35_rvre_291_overnight_share_of_total_var_252d_d2(close: pd.Series, open_: pd.Series) -> pd.Series:
    """(overnight log-ret)^2 sum / (close-to-close + intraday) variance sum over 252d — overnight-vs-total-day variance share."""
    overnight = np.log(_safe_div(open_, close.shift(1)))
    intraday = np.log(_safe_div(close, open_))
    total = overnight + intraday
    over_var = (overnight ** 2).rolling(YDAYS, min_periods=QDAYS).sum()
    tot_var = (total ** 2).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(over_var, tot_var).diff().diff()

def f35_rvre_292_vol_persistence_at_peak_composite_252d_d2(close: pd.Series) -> pd.Series:
    """Z-blend of GARCH-persistence + ARCH-LM(5) + high-vol-cluster fraction — overall vol-persistence score."""
    _, a, b = _garch_coefs(close)
    pers = a + b
    arch5 = _arch_lm(_log_returns(close), 5, YDAYS, QDAYS)
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    q75 = rv21.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.75)
    frac_top = (rv21 > q75).astype(float).where(q75.notna(), np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    z_pers = _rolling_zscore(pers, DDAYS_2Y, min_periods=YDAYS)
    z_arch = _rolling_zscore(arch5, DDAYS_2Y, min_periods=YDAYS)
    z_frac = _rolling_zscore(frac_top, DDAYS_2Y, min_periods=YDAYS)
    return ((z_pers + z_arch + z_frac) / 3.0).diff().diff()

def f35_rvre_293_leverage_effect_composite_252d_d2(close: pd.Series) -> pd.Series:
    """Z-blend of leverage_corr + GJR-gamma + leverage_gap_amp — overall leverage-effect strength score."""
    r = _log_returns(close)
    pairs = pd.concat([r.shift(1).rename('rlag'), r.abs().rename('absr')], axis=1)
    lc = pairs['rlag'].rolling(YDAYS, min_periods=QDAYS).corr(pairs['absr'])
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    ratio = _safe_div(rv21, rv21.shift(1))
    down = ratio.where(r.shift(1) < 0).rolling(YDAYS, min_periods=QDAYS).mean()
    up = ratio.where(r.shift(1) > 0).rolling(YDAYS, min_periods=QDAYS).mean()
    gap = down - up
    rsq_lag = (r ** 2).shift(1).values
    asym_lag = rsq_lag * (r.shift(1) < 0).astype(float).values
    rv_lag = rv21.shift(1).values
    y = rv21.values
    n = len(y)
    gamma = np.full(n, np.nan)
    for i in range(YDAYS - 1, n):
        lo = i - YDAYS + 1
        _, _, g, _ = _ols_3var(y[lo:i + 1], rsq_lag[lo:i + 1], asym_lag[lo:i + 1], rv_lag[lo:i + 1])
        gamma[i] = g
    gamma_s = pd.Series(gamma, index=close.index)
    z_lc = _rolling_zscore(-lc, DDAYS_2Y, min_periods=YDAYS)
    z_gp = _rolling_zscore(gap, DDAYS_2Y, min_periods=YDAYS)
    z_gm = _rolling_zscore(gamma_s, DDAYS_2Y, min_periods=YDAYS)
    return ((z_lc + z_gp + z_gm) / 3.0).diff().diff()

def f35_rvre_294_high_vol_at_recent_peak_indicator_252d_d2(close: pd.Series) -> pd.Series:
    """Indicator: today is within 5% of trailing 252d high AND RV21 > p80 of 504d — high-vol-at-peak (classic blowoff)."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    p80 = rv21.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.8)
    peak = close.rolling(YDAYS, min_periods=QDAYS).max()
    near_peak = close >= 0.95 * peak
    high_vol = rv21 > p80
    return (near_peak & high_vol).astype(float).where(p80.notna() & peak.notna(), np.nan).diff().diff()

def f35_rvre_295_vol_acceleration_into_peak_63d_d2(close: pd.Series) -> pd.Series:
    """Slope of RV21 over last 63d, evaluated only at bars within 5% of trailing 252d peak — vol ramping into highs."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    slope = _rolling_slope(rv21, QDAYS)
    peak = close.rolling(YDAYS, min_periods=QDAYS).max()
    near_peak = close >= 0.95 * peak
    return slope.where(near_peak, np.nan).diff().diff()

def f35_rvre_296_vol_forecast_excess_at_peak_252d_d2(close: pd.Series) -> pd.Series:
    """(HAR forecast - long-run RV mean) evaluated only at near-peak bars — model's view that vol stays elevated."""
    r = _log_returns(close)
    fc = _har_one_step_forecast(close, YDAYS, QDAYS)
    long_run = (r ** 2).rolling(DDAYS_2Y, min_periods=YDAYS).mean()
    peak = close.rolling(YDAYS, min_periods=QDAYS).max()
    near_peak = close >= 0.95 * peak
    return (fc - long_run).where(near_peak, np.nan).diff().diff()

def f35_rvre_297_vol_regime_severity_at_peak_252d_d2(close: pd.Series) -> pd.Series:
    """RV21 percentile in 1260d distribution evaluated at near-peak bars — vol-severity ranking at recent high."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    pct = rv21.rolling(DDAYS_5Y, min_periods=YDAYS).rank(pct=True)
    peak = close.rolling(YDAYS, min_periods=QDAYS).max()
    near_peak = close >= 0.95 * peak
    return pct.where(near_peak, np.nan).diff().diff()

def f35_rvre_298_vol_decay_after_peak_63d_d2(close: pd.Series) -> pd.Series:
    """Mean RV21 in last 63d minus RV21 at most-recent 252d peak — vol decay since peak."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    arr = close.values
    rv = rv21.values
    n = len(arr)
    rv_at_peak = np.full(n, np.nan)
    win = YDAYS
    for i in range(win - 1, n):
        lo = i - win + 1
        seg = arr[lo:i + 1]
        if np.isnan(seg).all():
            continue
        k = int(np.nanargmax(seg))
        rv_at_peak[i] = rv[lo + k]
    rv_at_peak_s = pd.Series(rv_at_peak, index=close.index)
    recent_rv = rv21.rolling(QDAYS, min_periods=MDAYS).mean()
    return (recent_rv - rv_at_peak_s).diff().diff()

def f35_rvre_299_har_overshoot_minus_realized_zscore_504d_d2(close: pd.Series) -> pd.Series:
    """Z-score (504d) of HAR forecast minus realized r^2 — persistent-overforecasting regime indicator."""
    r = _log_returns(close)
    rv_d = r ** 2
    fc = _har_one_step_forecast(close, YDAYS, QDAYS)
    err = fc - rv_d
    return _rolling_zscore(err, DDAYS_2Y, min_periods=YDAYS).diff().diff()

def f35_rvre_300_stuck_peak_vol_composite_504d_d2(close: pd.Series) -> pd.Series:
    """Z-blend of GARCH persistence + leverage_corr (negated) + vol overshoot + vol regime severity,
    output then masked to near-peak bars (within 5% of 252d high). Composite is undefined off-peak."""
    _, a, b = _garch_coefs(close)
    pers = a + b
    r = _log_returns(close)
    pairs = pd.concat([r.shift(1).rename('rl'), r.abs().rename('ar')], axis=1)
    lev = pairs['rl'].rolling(YDAYS, min_periods=QDAYS).corr(pairs['ar'])
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    overshoot = _safe_div(rv21, rv21.rolling(DDAYS_2Y, min_periods=YDAYS).mean())
    pct = rv21.rolling(DDAYS_5Y, min_periods=YDAYS).rank(pct=True)
    peak = close.rolling(YDAYS, min_periods=QDAYS).max()
    z_p = _rolling_zscore(pers, DDAYS_2Y, min_periods=YDAYS)
    z_l = _rolling_zscore(-lev, DDAYS_2Y, min_periods=YDAYS)
    z_o = _rolling_zscore(overshoot, DDAYS_2Y, min_periods=YDAYS)
    z_s = _rolling_zscore(pct, DDAYS_2Y, min_periods=YDAYS)
    combo = (z_p + z_l + z_o + z_s) / 4.0
    return combo.where(close >= 0.95 * peak, np.nan).diff().diff()
REALIZED_VOLATILITY_REGIME_D2_REGISTRY_226_300 = {'f35_rvre_226_garch_alpha_252d_d2': {'inputs': ['close'], 'func': f35_rvre_226_garch_alpha_252d_d2}, 'f35_rvre_227_garch_beta_252d_d2': {'inputs': ['close'], 'func': f35_rvre_227_garch_beta_252d_d2}, 'f35_rvre_228_garch_persistence_alpha_plus_beta_252d_d2': {'inputs': ['close'], 'func': f35_rvre_228_garch_persistence_alpha_plus_beta_252d_d2}, 'f35_rvre_229_garch_omega_252d_d2': {'inputs': ['close'], 'func': f35_rvre_229_garch_omega_252d_d2}, 'f35_rvre_230_garch_long_run_variance_252d_d2': {'inputs': ['close'], 'func': f35_rvre_230_garch_long_run_variance_252d_d2}, 'f35_rvre_231_garch_one_step_forecast_252d_d2': {'inputs': ['close'], 'func': f35_rvre_231_garch_one_step_forecast_252d_d2}, 'f35_rvre_232_gjr_gamma_asymmetric_term_252d_d2': {'inputs': ['close'], 'func': f35_rvre_232_gjr_gamma_asymmetric_term_252d_d2}, 'f35_rvre_233_arch_persistence_proxy_lag1_corr_rsq_252d_d2': {'inputs': ['close'], 'func': f35_rvre_233_arch_persistence_proxy_lag1_corr_rsq_252d_d2}, 'f35_rvre_234_leverage_corr_lag1_252d_d2': {'inputs': ['close'], 'func': f35_rvre_234_leverage_corr_lag1_252d_d2}, 'f35_rvre_235_leverage_corr_lag1_504d_d2': {'inputs': ['close'], 'func': f35_rvre_235_leverage_corr_lag1_504d_d2}, 'f35_rvre_236_leverage_corr_r_with_rv21_lead_252d_d2': {'inputs': ['close'], 'func': f35_rvre_236_leverage_corr_r_with_rv21_lead_252d_d2}, 'f35_rvre_237_vol_response_after_down_day_252d_d2': {'inputs': ['close'], 'func': f35_rvre_237_vol_response_after_down_day_252d_d2}, 'f35_rvre_238_vol_response_after_up_day_252d_d2': {'inputs': ['close'], 'func': f35_rvre_238_vol_response_after_up_day_252d_d2}, 'f35_rvre_239_asymmetric_vol_response_gap_252d_d2': {'inputs': ['close'], 'func': f35_rvre_239_asymmetric_vol_response_gap_252d_d2}, 'f35_rvre_240_vol_amplification_ratio_after_down_252d_d2': {'inputs': ['close'], 'func': f35_rvre_240_vol_amplification_ratio_after_down_252d_d2}, 'f35_rvre_241_vol_amplification_ratio_after_up_252d_d2': {'inputs': ['close'], 'func': f35_rvre_241_vol_amplification_ratio_after_up_252d_d2}, 'f35_rvre_242_leverage_gap_amplification_252d_d2': {'inputs': ['close'], 'func': f35_rvre_242_leverage_gap_amplification_252d_d2}, 'f35_rvre_243_corr_neg_r_with_rv_change_252d_d2': {'inputs': ['close'], 'func': f35_rvre_243_corr_neg_r_with_rv_change_252d_d2}, 'f35_rvre_244_har_one_step_forecast_252d_d2': {'inputs': ['close'], 'func': f35_rvre_244_har_one_step_forecast_252d_d2}, 'f35_rvre_245_har_forecast_error_252d_d2': {'inputs': ['close'], 'func': f35_rvre_245_har_forecast_error_252d_d2}, 'f35_rvre_246_har_forecast_abs_error_252d_d2': {'inputs': ['close'], 'func': f35_rvre_246_har_forecast_abs_error_252d_d2}, 'f35_rvre_247_har_forecast_mse_63d_d2': {'inputs': ['close'], 'func': f35_rvre_247_har_forecast_mse_63d_d2}, 'f35_rvre_248_har_forecast_bias_63d_d2': {'inputs': ['close'], 'func': f35_rvre_248_har_forecast_bias_63d_d2}, 'f35_rvre_249_har_vs_naive_skill_ratio_63d_d2': {'inputs': ['close'], 'func': f35_rvre_249_har_vs_naive_skill_ratio_63d_d2}, 'f35_rvre_250_har_forecast_direction_hit_rate_63d_d2': {'inputs': ['close'], 'func': f35_rvre_250_har_forecast_direction_hit_rate_63d_d2}, 'f35_rvre_251_har_forecast_minus_realized_smoothed_21d_d2': {'inputs': ['close'], 'func': f35_rvre_251_har_forecast_minus_realized_smoothed_21d_d2}, 'f35_rvre_252_har_forecast_z_score_in_252d_d2': {'inputs': ['close'], 'func': f35_rvre_252_har_forecast_z_score_in_252d_d2}, 'f35_rvre_253_har_forecast_vs_ewma094_ratio_d2': {'inputs': ['close'], 'func': f35_rvre_253_har_forecast_vs_ewma094_ratio_d2}, 'f35_rvre_254_vol_half_life_from_ac1_252d_d2': {'inputs': ['close'], 'func': f35_rvre_254_vol_half_life_from_ac1_252d_d2}, 'f35_rvre_255_vol_mean_reversion_speed_252d_d2': {'inputs': ['close'], 'func': f35_rvre_255_vol_mean_reversion_speed_252d_d2}, 'f35_rvre_256_vol_overshoot_ratio_252d_d2': {'inputs': ['close'], 'func': f35_rvre_256_vol_overshoot_ratio_252d_d2}, 'f35_rvre_257_vol_overshoot_ratio_504d_d2': {'inputs': ['close'], 'func': f35_rvre_257_vol_overshoot_ratio_504d_d2}, 'f35_rvre_258_log_vol_overshoot_252d_d2': {'inputs': ['close'], 'func': f35_rvre_258_log_vol_overshoot_252d_d2}, 'f35_rvre_259_vol_undershoot_indicator_252d_d2': {'inputs': ['close'], 'func': f35_rvre_259_vol_undershoot_indicator_252d_d2}, 'f35_rvre_260_consecutive_top_quartile_vol_streak_d2': {'inputs': ['close'], 'func': f35_rvre_260_consecutive_top_quartile_vol_streak_d2}, 'f35_rvre_261_consecutive_bottom_quartile_vol_streak_d2': {'inputs': ['close'], 'func': f35_rvre_261_consecutive_bottom_quartile_vol_streak_d2}, 'f35_rvre_262_fraction_bars_in_top_quartile_vol_252d_d2': {'inputs': ['close'], 'func': f35_rvre_262_fraction_bars_in_top_quartile_vol_252d_d2}, 'f35_rvre_263_count_high_vol_clusters_252d_d2': {'inputs': ['close'], 'func': f35_rvre_263_count_high_vol_clusters_252d_d2}, 'f35_rvre_264_mean_high_vol_cluster_duration_252d_d2': {'inputs': ['close'], 'func': f35_rvre_264_mean_high_vol_cluster_duration_252d_d2}, 'f35_rvre_265_arch_lm_stat_lag1_252d_d2': {'inputs': ['close'], 'func': f35_rvre_265_arch_lm_stat_lag1_252d_d2}, 'f35_rvre_266_arch_lm_stat_lag5_252d_d2': {'inputs': ['close'], 'func': f35_rvre_266_arch_lm_stat_lag5_252d_d2}, 'f35_rvre_267_arch_lm_stat_lag21_504d_d2': {'inputs': ['close'], 'func': f35_rvre_267_arch_lm_stat_lag21_504d_d2}, 'f35_rvre_268_engle_ng_joint_chi_sq_252d_d2': {'inputs': ['close'], 'func': f35_rvre_268_engle_ng_joint_chi_sq_252d_d2}, 'f35_rvre_269_bds_proxy_corr_dim_2_252d_d2': {'inputs': ['close'], 'func': f35_rvre_269_bds_proxy_corr_dim_2_252d_d2}, 'f35_rvre_270_beta_rv_on_lagged_rsq_252d_d2': {'inputs': ['close'], 'func': f35_rvre_270_beta_rv_on_lagged_rsq_252d_d2}, 'f35_rvre_271_beta_rv_on_lagged_rv21_252d_d2': {'inputs': ['close'], 'func': f35_rvre_271_beta_rv_on_lagged_rv21_252d_d2}, 'f35_rvre_272_beta_rv_on_drvchange_252d_d2': {'inputs': ['close'], 'func': f35_rvre_272_beta_rv_on_drvchange_252d_d2}, 'f35_rvre_273_cross_horizon_convergence_speed_21_252_252d_d2': {'inputs': ['close'], 'func': f35_rvre_273_cross_horizon_convergence_speed_21_252_252d_d2}, 'f35_rvre_274_vol_roll_signal_rv5_minus_rv21_d2': {'inputs': ['close'], 'func': f35_rvre_274_vol_roll_signal_rv5_minus_rv21_d2}, 'f35_rvre_275_vol_curve_inversion_indicator_5_21_63_d2': {'inputs': ['close'], 'func': f35_rvre_275_vol_curve_inversion_indicator_5_21_63_d2}, 'f35_rvre_276_vol_catchup_factor_21d_d2': {'inputs': ['close'], 'func': f35_rvre_276_vol_catchup_factor_21d_d2}, 'f35_rvre_277_vol_decay_after_last_spike_252d_d2': {'inputs': ['close'], 'func': f35_rvre_277_vol_decay_after_last_spike_252d_d2}, 'f35_rvre_278_vol_shock_magnitude_x_persistence_252d_d2': {'inputs': ['close'], 'func': f35_rvre_278_vol_shock_magnitude_x_persistence_252d_d2}, 'f35_rvre_279_largest_rv_jump_in_21d_in_252d_d2': {'inputs': ['close'], 'func': f35_rvre_279_largest_rv_jump_in_21d_in_252d_d2}, 'f35_rvre_280_time_between_vol_clusters_252d_d2': {'inputs': ['close'], 'func': f35_rvre_280_time_between_vol_clusters_252d_d2}, 'f35_rvre_281_vol_shock_bayesian_update_factor_252d_d2': {'inputs': ['close'], 'func': f35_rvre_281_vol_shock_bayesian_update_factor_252d_d2}, 'f35_rvre_282_vol_carry_rv21_minus_rv63_d2': {'inputs': ['close'], 'func': f35_rvre_282_vol_carry_rv21_minus_rv63_d2}, 'f35_rvre_283_vol_carry_rv63_minus_rv252_d2': {'inputs': ['close'], 'func': f35_rvre_283_vol_carry_rv63_minus_rv252_d2}, 'f35_rvre_284_vol_carry_log_ratio_rv21_rv63_d2': {'inputs': ['close'], 'func': f35_rvre_284_vol_carry_log_ratio_rv21_rv63_d2}, 'f35_rvre_285_vol_carry_zscore_in_504d_d2': {'inputs': ['close'], 'func': f35_rvre_285_vol_carry_zscore_in_504d_d2}, 'f35_rvre_286_vol_curve_full_normal_indicator_d2': {'inputs': ['close'], 'func': f35_rvre_286_vol_curve_full_normal_indicator_d2}, 'f35_rvre_287_park_vs_cc_sigma_diff_21d_d2': {'inputs': ['high', 'low', 'close'], 'func': f35_rvre_287_park_vs_cc_sigma_diff_21d_d2}, 'f35_rvre_288_park_vs_cc_sigma_diff_63d_d2': {'inputs': ['high', 'low', 'close'], 'func': f35_rvre_288_park_vs_cc_sigma_diff_63d_d2}, 'f35_rvre_289_park_over_cc_sigma_ratio_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f35_rvre_289_park_over_cc_sigma_ratio_252d_d2}, 'f35_rvre_290_range_rv_disagreement_zscore_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f35_rvre_290_range_rv_disagreement_zscore_252d_d2}, 'f35_rvre_291_overnight_share_of_total_var_252d_d2': {'inputs': ['close', 'open'], 'func': f35_rvre_291_overnight_share_of_total_var_252d_d2}, 'f35_rvre_292_vol_persistence_at_peak_composite_252d_d2': {'inputs': ['close'], 'func': f35_rvre_292_vol_persistence_at_peak_composite_252d_d2}, 'f35_rvre_293_leverage_effect_composite_252d_d2': {'inputs': ['close'], 'func': f35_rvre_293_leverage_effect_composite_252d_d2}, 'f35_rvre_294_high_vol_at_recent_peak_indicator_252d_d2': {'inputs': ['close'], 'func': f35_rvre_294_high_vol_at_recent_peak_indicator_252d_d2}, 'f35_rvre_295_vol_acceleration_into_peak_63d_d2': {'inputs': ['close'], 'func': f35_rvre_295_vol_acceleration_into_peak_63d_d2}, 'f35_rvre_296_vol_forecast_excess_at_peak_252d_d2': {'inputs': ['close'], 'func': f35_rvre_296_vol_forecast_excess_at_peak_252d_d2}, 'f35_rvre_297_vol_regime_severity_at_peak_252d_d2': {'inputs': ['close'], 'func': f35_rvre_297_vol_regime_severity_at_peak_252d_d2}, 'f35_rvre_298_vol_decay_after_peak_63d_d2': {'inputs': ['close'], 'func': f35_rvre_298_vol_decay_after_peak_63d_d2}, 'f35_rvre_299_har_overshoot_minus_realized_zscore_504d_d2': {'inputs': ['close'], 'func': f35_rvre_299_har_overshoot_minus_realized_zscore_504d_d2}, 'f35_rvre_300_stuck_peak_vol_composite_504d_d2': {'inputs': ['close'], 'func': f35_rvre_300_stuck_peak_vol_composite_504d_d2}}