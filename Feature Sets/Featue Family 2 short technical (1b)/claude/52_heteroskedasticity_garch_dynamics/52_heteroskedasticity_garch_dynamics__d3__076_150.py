"""heteroskedasticity_garch_dynamics d3 features 076-150 - Pipeline 1b-technical.

150 distinct hypotheses across __base__001_075.py and __base__076_150.py.
Each feature encodes a *different concept*.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers - no cross-family imports.
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


def _norm_ppf(p):
    """Rational approximation of standard-normal inverse CDF (Beasley-Springer-Moro simplified)."""
    p = float(p)
    if not (0.0 < p < 1.0):
        return np.nan
    if p < 0.5:
        t = np.sqrt(-2.0 * np.log(p))
        x = t - (2.515517 + 0.802853 * t + 0.010328 * t * t) / (
            1.0 + 1.432788 * t + 0.189269 * t * t + 0.001308 * t ** 3)
        return -x
    else:
        t = np.sqrt(-2.0 * np.log(1.0 - p))
        x = t - (2.515517 + 0.802853 * t + 0.010328 * t * t) / (
            1.0 + 1.432788 * t + 0.189269 * t * t + 0.001308 * t ** 3)
        return x


def _norm_cdf(x):
    """Standard normal CDF via erf."""
    from math import erf, sqrt
    return 0.5 * (1.0 + erf(x / sqrt(2.0)))


def _rolling_q(s, n, q, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 10)
    return s.rolling(n, min_periods=min_periods).quantile(q)


def _rolling_skew(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 10)
    return s.rolling(n, min_periods=min_periods).skew()


def _rolling_kurt(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 10)
    return s.rolling(n, min_periods=min_periods).kurt()

def _ewma_var(r_sq, lam):
    """RiskMetrics-style EWMA variance. lam in (0,1). Returns Series same index."""
    arr = r_sq.values
    out = np.full(len(arr), np.nan, dtype=float)
    s = np.nan
    for i in range(len(arr)):
        x = arr[i]
        if np.isnan(x):
            out[i] = s
            continue
        if np.isnan(s):
            s = x
        else:
            s = lam * s + (1.0 - lam) * x
        out[i] = s
    return pd.Series(out, index=r_sq.index)


def _ewma_vol(r, lam):
    """RiskMetrics EWMA volatility (sqrt of EWMA variance of r^2)."""
    return _ewma_var(r ** 2, lam).pow(0.5)


def _garch11_fit_window(v, alphas=None, betas=None):
    """Variance-targeting GARCH(1,1) grid-search MLE on a single 1-D array.

    Returns (alpha, beta, omega, persistence, sigma2_now, log_lik, long_run_var, aic).
    """
    if alphas is None:
        alphas = (0.05, 0.10, 0.15, 0.20)
    if betas is None:
        betas = (0.70, 0.80, 0.85, 0.90, 0.93)
    v = v[~np.isnan(v)]
    if v.size < 60:
        return (np.nan,) * 8
    uncond = max(float(np.var(v, ddof=1)), 1e-12)
    n = v.size
    best = (np.nan, np.nan, np.nan, np.nan, np.nan, -np.inf, np.nan, np.nan)
    sq = v * v
    for a in alphas:
        for b in betas:
            if a + b >= 0.99:
                continue
            omega = (1.0 - a - b) * uncond
            s2 = uncond
            ll = 0.0
            ok = True
            for i in range(1, n):
                s2 = omega + a * sq[i - 1] + b * s2
                if s2 <= 0:
                    ok = False
                    break
                ll += -0.5 * np.log(2.0 * np.pi * s2) - 0.5 * sq[i] / s2
            if ok and ll > best[5]:
                long_run = omega / max(1e-12, 1.0 - a - b)
                aic = 2.0 * 3 - 2.0 * ll
                best = (a, b, omega, a + b, s2, ll, long_run, aic)
    return best


def _rolling_garch11(s, n, want_idx):
    """Apply variance-targeting GARCH(1,1) over rolling window n. want_idx=0..7.
    Refits every 21 bars to save cost (forward-filled in between)."""
    mp = max(n // 3, 60)
    arr = s.values
    nb = len(arr)
    out = np.full(nb, np.nan, dtype=float)
    last = (np.nan,) * 8
    for i in range(nb):
        if i < mp - 1:
            continue
        if i % 21 == 0 or np.isnan(last[want_idx]):
            lo = max(0, i - n + 1)
            last = _garch11_fit_window(arr[lo:i + 1])
        out[i] = last[want_idx]
    return pd.Series(out, index=s.index)


def _gjr_garch_fit_window(v, alphas=None, betas=None, gammas=None):
    """GJR-GARCH grid search. Returns (alpha, beta, gamma, omega, persistence, sigma2_now, ll)."""
    if alphas is None:
        alphas = (0.03, 0.07, 0.12)
    if betas is None:
        betas = (0.75, 0.85, 0.90)
    if gammas is None:
        gammas = (0.05, 0.10, 0.20)
    v = v[~np.isnan(v)]
    if v.size < 60:
        return (np.nan,) * 7
    uncond = max(float(np.var(v, ddof=1)), 1e-12)
    n = v.size
    sq = v * v
    sgn_neg = (v < 0).astype(float)
    best = (np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, -np.inf)
    for a in alphas:
        for b in betas:
            for g in gammas:
                pers = a + b + 0.5 * g
                if pers >= 0.99:
                    continue
                omega = (1.0 - pers) * uncond
                s2 = uncond
                ll = 0.0
                ok = True
                for i in range(1, n):
                    s2 = omega + a * sq[i - 1] + g * sgn_neg[i - 1] * sq[i - 1] + b * s2
                    if s2 <= 0:
                        ok = False
                        break
                    ll += -0.5 * np.log(2.0 * np.pi * s2) - 0.5 * sq[i] / s2
                if ok and ll > best[6]:
                    best = (a, b, g, omega, pers, s2, ll)
    return best


def _rolling_gjr_garch(s, n, want_idx):
    mp = max(n // 3, 60)
    arr = s.values
    nb = len(arr)
    out = np.full(nb, np.nan, dtype=float)
    last = (np.nan,) * 7
    for i in range(nb):
        if i < mp - 1:
            continue
        if i % 21 == 0 or np.isnan(last[want_idx]):
            lo = max(0, i - n + 1)
            last = _gjr_garch_fit_window(arr[lo:i + 1])
        out[i] = last[want_idx]
    return pd.Series(out, index=s.index)


def _arch_lm_stat(r, n, p):
    """Engle ARCH-LM test stat = n * R^2 of regression r^2_t ~ const + r^2_{t-1} + ... + r^2_{t-p}."""
    mp = max(n // 3, max(3 * p + 10, 30))
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 3 * p + 10:
            return np.nan
        sq = v * v
        T = sq.size - p
        Y = sq[p:]
        X = np.ones((T, p + 1))
        for j in range(p):
            X[:, j + 1] = sq[p - j - 1: sq.size - j - 1]
        try:
            beta, *_ = np.linalg.lstsq(X, Y, rcond=None)
        except np.linalg.LinAlgError:
            return np.nan
        pred = X @ beta
        ss_res = float(np.sum((Y - pred) ** 2))
        ss_tot = float(np.sum((Y - Y.mean()) ** 2))
        if ss_tot <= 0:
            return np.nan
        r2 = 1.0 - ss_res / ss_tot
        return float(T * r2)
    return r.rolling(n, min_periods=mp).apply(_f, raw=True)


def _ljung_box_q_on_sq(r, n, max_lag):
    """Ljung-Box Q applied to r^2 (McLeod-Li test)."""
    mp = max(n // 3, max(2 * max_lag + 8, 30))
    def _f(w):
        v = w[~np.isnan(w)]
        nv = v.size
        if nv < max_lag + 15:
            return np.nan
        sq = v * v
        sq = sq - sq.mean()
        denom = float(np.dot(sq, sq))
        if denom <= 0:
            return np.nan
        q = 0.0
        for k in range(1, max_lag + 1):
            rho_k = float(np.dot(sq[:nv - k], sq[k:]) / denom)
            q += (rho_k * rho_k) / (nv - k)
        return float(nv * (nv + 2) * q)
    return r.rolling(n, min_periods=mp).apply(_f, raw=True)


def _fhs_var(r, n, q, lam=0.94):
    """Filtered Historical Simulation VaR: standardize r by EWMA vol, take quantile, rescale."""
    sd = _ewma_vol(r, lam)
    z = (r / sd.replace(0, np.nan))
    mp = max(n // 3, 30)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        return float(np.quantile(v, 1.0 - q))
    z_q = z.rolling(n, min_periods=mp).apply(_f, raw=True)
    return -(z_q * sd)


def _fhs_es(r, n, q, lam=0.94):
    """FHS Expected Shortfall."""
    sd = _ewma_vol(r, lam)
    z = (r / sd.replace(0, np.nan))
    mp = max(n // 3, 30)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        thr = np.quantile(v, 1.0 - q)
        tail = v[v <= thr]
        return float(tail.mean()) if tail.size > 0 else np.nan
    z_es = z.rolling(n, min_periods=mp).apply(_f, raw=True)
    return -(z_es * sd)


def _parkinson_var(high, low, n=21):
    """Parkinson realized variance from intra-day range."""
    ln_hl = (_safe_log(high) - _safe_log(low)) ** 2
    return ln_hl.rolling(n, min_periods=max(n // 3, 5)).mean() / (4.0 * np.log(2.0))


def _garman_klass_var(open_, high, low, close, n=21):
    """Garman-Klass realized variance."""
    rs = 0.5 * (_safe_log(high) - _safe_log(low)) ** 2 - (2.0 * np.log(2.0) - 1.0) * (_safe_log(close) - _safe_log(open_)) ** 2
    return rs.rolling(n, min_periods=max(n // 3, 5)).mean()


def _yang_zhang_var(open_, high, low, close, n=21):
    """Yang-Zhang variance (combines overnight, opening, Rogers-Satchell)."""
    log_o = _safe_log(open_); log_c = _safe_log(close)
    log_h = _safe_log(high); log_l = _safe_log(low)
    log_cp = log_c.shift(1)
    overnight = (log_o - log_cp) ** 2
    open_close = (log_c - log_o) ** 2
    rs = (log_h - log_c) * (log_h - log_o) + (log_l - log_c) * (log_l - log_o)
    on_var = overnight.rolling(n, min_periods=max(n // 3, 5)).var()
    oc_var = open_close.rolling(n, min_periods=max(n // 3, 5)).var()
    rs_avg = rs.rolling(n, min_periods=max(n // 3, 5)).mean()
    k = 0.34 / (1.34 + (n + 1.0) / (n - 1.0))
    return on_var + k * oc_var + (1.0 - k) * rs_avg


def f52_hgrd_076_yang_zhang_var_63d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Yang-Zhang variance over 63d."""
    return (_yang_zhang_var(open, high, low, close, QDAYS)).diff().diff().diff()

def f52_hgrd_077_ratio_parkinson_to_close_close_var_21d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Parkinson(21d) / 21d realized variance from close-close log returns - efficiency ratio."""
    r = _log_ret(close)
    rv = (r ** 2).rolling(MDAYS, min_periods=10).mean()
    pk = _parkinson_var(high, low, MDAYS)
    return (_safe_div(pk, rv)).diff().diff().diff()

def f52_hgrd_078_ratio_garman_klass_to_close_close_var_21d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Garman-Klass(21d) / close-close variance."""
    r = _log_ret(close)
    rv = (r ** 2).rolling(MDAYS, min_periods=10).mean()
    gk = _garman_klass_var(open, high, low, close, MDAYS)
    return (_safe_div(gk, rv)).diff().diff().diff()

def f52_hgrd_079_ratio_yang_zhang_to_close_close_var_21d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Yang-Zhang(21d) / close-close variance."""
    r = _log_ret(close)
    rv = (r ** 2).rolling(MDAYS, min_periods=10).mean()
    yz = _yang_zhang_var(open, high, low, close, MDAYS)
    return (_safe_div(yz, rv)).diff().diff().diff()

def f52_hgrd_080_range_efficiency_ratio_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean (high-low)/close divided by std(log_ret) over 252d - intraday vs interday vol ratio."""
    r = _log_ret(close)
    rng = _safe_div(high - low, close).rolling(YDAYS, min_periods=QDAYS).mean()
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    return (_safe_div(rng, sd)).diff().diff().diff()

def f52_hgrd_081_garch_vol_forecast_1step_252d_d3(close: pd.Series) -> pd.Series:
    """GARCH(1,1) one-step-ahead vol forecast = sqrt(omega + alpha*r_t^2 + beta*sigma_t^2)."""
    r = _log_ret(close)
    a = _rolling_garch11(r, YDAYS, 0)
    b = _rolling_garch11(r, YDAYS, 1)
    om = _rolling_garch11(r, YDAYS, 2)
    s2 = _rolling_garch11(r, YDAYS, 4)
    fwd = om + a * (r ** 2) + b * s2
    return (fwd.pow(0.5)).diff().diff().diff()

def f52_hgrd_082_garch_vol_forecast_21step_252d_d3(close: pd.Series) -> pd.Series:
    """GARCH(1,1) 21-step-ahead vol = sqrt(long_run + (sigma^2 - long_run) * (alpha+beta)^21)."""
    r = _log_ret(close)
    p = _rolling_garch11(r, YDAYS, 3)
    lr = _rolling_garch11(r, YDAYS, 6)
    s2 = _rolling_garch11(r, YDAYS, 4)
    return ((lr + (s2 - lr) * p ** 21).clip(lower=0).pow(0.5)).diff().diff().diff()

def f52_hgrd_083_vol_forecast_diff_ewma_garch_1step_252d_d3(close: pd.Series) -> pd.Series:
    """EWMA(0.94) vol vs GARCH 1-step vol-forecast difference over 252d."""
    r = _log_ret(close)
    ve = _ewma_vol(r, 0.94)
    a = _rolling_garch11(r, YDAYS, 0); b = _rolling_garch11(r, YDAYS, 1)
    om = _rolling_garch11(r, YDAYS, 2); s2 = _rolling_garch11(r, YDAYS, 4)
    vg = (om + a * (r ** 2) + b * s2).pow(0.5)
    return (ve - vg).diff().diff().diff()

def f52_hgrd_084_vol_mean_reversion_speed_garch_252d_d3(close: pd.Series) -> pd.Series:
    """1 - GARCH persistence = vol mean-reversion speed over 252d."""
    r = _log_ret(close)
    p = _rolling_garch11(r, YDAYS, 3)
    return (1.0 - p).diff().diff().diff()

def f52_hgrd_085_vol_half_life_garch_252d_d3(close: pd.Series) -> pd.Series:
    """Half-life of vol shocks under GARCH(1,1) = log(0.5)/log(persistence) over 252d."""
    r = _log_ret(close)
    p = _rolling_garch11(r, YDAYS, 3).clip(upper=0.999).replace(0, np.nan)
    return (-np.log(2.0) / np.log(p)).diff().diff().diff()

def f52_hgrd_086_current_vs_long_run_vol_ratio_garch_252d_d3(close: pd.Series) -> pd.Series:
    """Current GARCH conditional vol / long-run vol over 252d."""
    r = _log_ret(close)
    s2 = _rolling_garch11(r, YDAYS, 4)
    lr = _rolling_garch11(r, YDAYS, 6)
    return (_safe_div(s2.pow(0.5), lr.pow(0.5))).diff().diff().diff()

def f52_hgrd_087_log_vol_persistence_ar1_252d_d3(close: pd.Series) -> pd.Series:
    """AR(1) of log(EWMA-vol) over 252d - log-vol persistence."""
    r = _log_ret(close)
    lv = np.log(_ewma_vol(r, 0.94).replace(0, np.nan))
    def _ac(w):
        x = w[~np.isnan(w)]
        if x.size < 20:
            return np.nan
        a = x[:-1]; b = x[1:]
        if a.std() == 0 or b.std() == 0:
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    res = lv.rolling(YDAYS, min_periods=QDAYS).apply(_ac, raw=True)
    return (res).diff().diff().diff()

def f52_hgrd_088_log_vol_unit_root_proxy_adf_252d_d3(close: pd.Series) -> pd.Series:
    """Unit-root proxy for log-vol: AR(1) coefficient close to 1 = non-stationary log-vol."""
    r = _log_ret(close)
    lv = np.log(_ewma_vol(r, 0.94).replace(0, np.nan))
    def _ac(w):
        x = w[~np.isnan(w)]
        if x.size < 20:
            return np.nan
        a = x[:-1]; b = x[1:]
        if a.std() == 0 or b.std() == 0:
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    ar1 = lv.rolling(YDAYS, min_periods=QDAYS).apply(_ac, raw=True)
    return (ar1 - 1.0).diff().diff().diff()

def f52_hgrd_089_ewma_vol_change_speed_acf1_252d_d3(close: pd.Series) -> pd.Series:
    """ACF(1) of daily change in EWMA vol over 252d - momentum in vol shocks."""
    r = _log_ret(close)
    ch = _ewma_vol(r, 0.94).diff()
    def _ac(w):
        x = w[~np.isnan(w)]
        if x.size < 20:
            return np.nan
        a = x[:-1]; b = x[1:]
        if a.std() == 0 or b.std() == 0:
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    res = ch.rolling(YDAYS, min_periods=QDAYS).apply(_ac, raw=True)
    return (res).diff().diff().diff()

def f52_hgrd_090_garch_long_run_var_change_speed_252d_d3(close: pd.Series) -> pd.Series:
    """21-bar pct change of GARCH long-run variance over 252d."""
    r = _log_ret(close)
    lr = _rolling_garch11(r, YDAYS, 6)
    return (_safe_div(lr - lr.shift(MDAYS), lr.shift(MDAYS))).diff().diff().diff()

def f52_hgrd_091_vol_regime_high_above_p75_252d_indicator_d3(close: pd.Series) -> pd.Series:
    """Indicator: EWMA vol > 252d 75th-percentile."""
    r = _log_ret(close)
    v = _ewma_vol(r, 0.94)
    p75 = v.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    return ((v > p75).astype(float).where(p75.notna(), np.nan)).diff().diff().diff()

def f52_hgrd_092_vol_regime_low_below_p25_252d_indicator_d3(close: pd.Series) -> pd.Series:
    """Indicator: EWMA vol < 252d 25th-percentile."""
    r = _log_ret(close)
    v = _ewma_vol(r, 0.94)
    p25 = v.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    return ((v < p25).astype(float).where(p25.notna(), np.nan)).diff().diff().diff()

def f52_hgrd_093_vol_regime_above_p75_persistence_63d_d3(close: pd.Series) -> pd.Series:
    """Fraction of last 63d with EWMA vol above 252d-p75."""
    r = _log_ret(close)
    v = _ewma_vol(r, 0.94)
    p75 = v.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    ind = (v > p75).astype(float).where(p75.notna(), np.nan)
    return (ind.rolling(QDAYS, min_periods=MDAYS).mean()).diff().diff().diff()

def f52_hgrd_094_vol_regime_transitions_count_252d_d3(close: pd.Series) -> pd.Series:
    """Count of high/low regime flips (EWMA vol crossing 252d-median) over 252d."""
    r = _log_ret(close)
    v = _ewma_vol(r, 0.94)
    med = v.rolling(YDAYS, min_periods=QDAYS).median()
    sgn = np.sign(v - med)
    flip = ((sgn != sgn.shift(1)) & (sgn != 0)).astype(float)
    return (flip.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()

def f52_hgrd_095_vol_breakout_above_2sigma_252d_count_d3(close: pd.Series) -> pd.Series:
    """Count of bars where |r_t| > 2*EWMA-vol_{t-1} in last 252d - extreme-vol shocks."""
    r = _log_ret(close)
    v = _ewma_vol(r, 0.94).shift(1)
    br = (r.abs() > 2.0 * v).astype(float).where(v.notna(), np.nan)
    return (br.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()

def f52_hgrd_096_vol_compression_below_bb_lower_252d_count_d3(close: pd.Series) -> pd.Series:
    """Count of bars where EWMA vol < (mean - 2*std) over 252d."""
    r = _log_ret(close)
    v = _ewma_vol(r, 0.94)
    mu = v.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = v.rolling(YDAYS, min_periods=QDAYS).std()
    ind = (v < mu - 2.0 * sd).astype(float).where(sd.notna(), np.nan)
    return (ind.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()

def f52_hgrd_097_vol_zscore_above_2_count_252d_d3(close: pd.Series) -> pd.Series:
    """Count of bars in last 252d where rolling-252d z-score of EWMA-vol > 2."""
    r = _log_ret(close)
    v = _ewma_vol(r, 0.94)
    z = _rolling_zscore(v, YDAYS)
    return ((z > 2.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()

def f52_hgrd_098_vol_drawdown_max_252d_d3(close: pd.Series) -> pd.Series:
    """Max drop (252d-mean - 252d-min) of EWMA vol."""
    r = _log_ret(close)
    v = _ewma_vol(r, 0.94)
    mu = v.rolling(YDAYS, min_periods=QDAYS).mean()
    mn = v.rolling(YDAYS, min_periods=QDAYS).min()
    return (mu - mn).diff().diff().diff()

def f52_hgrd_099_vol_drawup_max_252d_d3(close: pd.Series) -> pd.Series:
    """Max rise (252d-max - 252d-mean) of EWMA vol."""
    r = _log_ret(close)
    v = _ewma_vol(r, 0.94)
    mu = v.rolling(YDAYS, min_periods=QDAYS).mean()
    mx = v.rolling(YDAYS, min_periods=QDAYS).max()
    return (mx - mu).diff().diff().diff()

def f52_hgrd_100_vol_skewness_in_vol_space_252d_d3(close: pd.Series) -> pd.Series:
    """Skewness of log-EWMA-vol over 252d - asymmetry in log-vol distribution."""
    r = _log_ret(close)
    lv = np.log(_ewma_vol(r, 0.94).replace(0, np.nan))
    return (_rolling_skew(lv, YDAYS)).diff().diff().diff()

def f52_hgrd_101_asymmetric_vol_after_neg_252d_d3(close: pd.Series) -> pd.Series:
    """Mean r^2 conditional on prior-day negative return over 252d - vol after a down day."""
    r = _log_ret(close)
    sq = r ** 2
    cond = sq.where(r.shift(1) < 0, np.nan)
    return (cond.rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff().diff()

def f52_hgrd_102_asymmetric_vol_after_pos_252d_d3(close: pd.Series) -> pd.Series:
    """Mean r^2 conditional on prior-day positive return over 252d."""
    r = _log_ret(close)
    sq = r ** 2
    cond = sq.where(r.shift(1) > 0, np.nan)
    return (cond.rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff().diff()

def f52_hgrd_103_asymmetric_vol_ratio_neg_to_pos_252d_d3(close: pd.Series) -> pd.Series:
    """(E[r^2|prev<0]) / (E[r^2|prev>0]) over 252d - direct leverage-effect ratio."""
    r = _log_ret(close)
    sq = r ** 2
    vn = sq.where(r.shift(1) < 0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    vp = sq.where(r.shift(1) > 0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    return (_safe_div(vn, vp)).diff().diff().diff()

def f52_hgrd_104_news_impact_curve_slope_neg_252d_d3(close: pd.Series) -> pd.Series:
    """Slope of regression r^2_t = a + b * I(r_{t-1}<0) * |r_{t-1}| over 252d - asymmetric impact."""
    r = _log_ret(close)
    def _nic(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        sq = v[1:] ** 2
        x = ((v[:-1] < 0).astype(float) * np.abs(v[:-1]))
        if x.std() == 0:
            return np.nan
        xm = x.mean(); sxx = ((x - xm) ** 2).sum()
        return float(((x - xm) * (sq - sq.mean())).sum() / sxx) if sxx > 0 else np.nan
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_nic, raw=True)
    return (res).diff().diff().diff()

def f52_hgrd_105_news_impact_curve_slope_pos_252d_d3(close: pd.Series) -> pd.Series:
    """Slope on r^2_t = a + b * I(r_{t-1}>0) * |r_{t-1}| over 252d."""
    r = _log_ret(close)
    def _nip(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        sq = v[1:] ** 2
        x = ((v[:-1] > 0).astype(float) * np.abs(v[:-1]))
        if x.std() == 0:
            return np.nan
        xm = x.mean(); sxx = ((x - xm) ** 2).sum()
        return float(((x - xm) * (sq - sq.mean())).sum() / sxx) if sxx > 0 else np.nan
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_nip, raw=True)
    return (res).diff().diff().diff()

def f52_hgrd_106_realized_semi_var_negative_63d_d3(close: pd.Series) -> pd.Series:
    """Sum r^2 (r<0) over 63d - downside realized semivariance."""
    r = _log_ret(close)
    neg_sq = (r ** 2).where(r < 0, 0.0)
    return (neg_sq.rolling(QDAYS, min_periods=MDAYS).sum()).diff().diff().diff()

def f52_hgrd_107_realized_semi_var_positive_63d_d3(close: pd.Series) -> pd.Series:
    """Sum r^2 (r>0) over 63d."""
    r = _log_ret(close)
    pos_sq = (r ** 2).where(r > 0, 0.0)
    return (pos_sq.rolling(QDAYS, min_periods=MDAYS).sum()).diff().diff().diff()

def f52_hgrd_108_semi_var_persistence_negative_ar1_252d_d3(close: pd.Series) -> pd.Series:
    """AR(1) of downside semivariance series over 252d - vol persistence on downside."""
    r = _log_ret(close)
    neg_sq = (r ** 2).where(r < 0, 0.0)
    def _ac(w):
        x = w[~np.isnan(w)]
        if x.size < 20:
            return np.nan
        a = x[:-1]; b = x[1:]
        if a.std() == 0 or b.std() == 0:
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    res = neg_sq.rolling(YDAYS, min_periods=QDAYS).apply(_ac, raw=True)
    return (res).diff().diff().diff()

def f52_hgrd_109_semi_var_persistence_positive_ar1_252d_d3(close: pd.Series) -> pd.Series:
    """AR(1) of upside semivariance series over 252d."""
    r = _log_ret(close)
    pos_sq = (r ** 2).where(r > 0, 0.0)
    def _ac(w):
        x = w[~np.isnan(w)]
        if x.size < 20:
            return np.nan
        a = x[:-1]; b = x[1:]
        if a.std() == 0 or b.std() == 0:
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    res = pos_sq.rolling(YDAYS, min_periods=QDAYS).apply(_ac, raw=True)
    return (res).diff().diff().diff()

def f52_hgrd_110_asymmetric_realized_vol_diff_252d_d3(close: pd.Series) -> pd.Series:
    """Downside realized semivar minus upside semivar over 252d - signed asymmetry."""
    r = _log_ret(close)
    neg = (r ** 2).where(r < 0, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()
    pos = (r ** 2).where(r > 0, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()
    return (neg - pos).diff().diff().diff()

def f52_hgrd_111_realized_minus_ewma_vol_252d_d3(close: pd.Series) -> pd.Series:
    """63d realized vol minus EWMA-0.94 vol over 252d - empirical vs filter gap."""
    r = _log_ret(close)
    rv = ((r ** 2).rolling(QDAYS, min_periods=MDAYS).mean()).pow(0.5)
    v = _ewma_vol(r, 0.94)
    return (rv - v).diff().diff().diff()

def f52_hgrd_112_realized_minus_garch_vol_252d_d3(close: pd.Series) -> pd.Series:
    """63d realized vol minus GARCH(1,1) conditional vol over 252d."""
    r = _log_ret(close)
    rv = ((r ** 2).rolling(QDAYS, min_periods=MDAYS).mean()).pow(0.5)
    vg = _rolling_garch11(r, YDAYS, 4).pow(0.5)
    return (rv - vg).diff().diff().diff()

def f52_hgrd_113_vol_term_struct_short_minus_long_realized_252d_d3(close: pd.Series) -> pd.Series:
    """21d realized vol minus 252d realized vol over 252d - term structure slope."""
    r = _log_ret(close)
    vs = ((r ** 2).rolling(MDAYS, min_periods=10).mean()).pow(0.5)
    vl = ((r ** 2).rolling(YDAYS, min_periods=QDAYS).mean()).pow(0.5)
    return (vs - vl).diff().diff().diff()

def f52_hgrd_114_realized_vol_curve_slope_5_21_63_252d_d3(close: pd.Series) -> pd.Series:
    """Linear-regression slope of (vol at 5d, 21d, 63d) over rolling 252d."""
    r = _log_ret(close)
    v5 = ((r ** 2).rolling(5, min_periods=3).mean()).pow(0.5)
    v21 = ((r ** 2).rolling(MDAYS, min_periods=10).mean()).pow(0.5)
    v63 = ((r ** 2).rolling(QDAYS, min_periods=MDAYS).mean()).pow(0.5)
    x = np.array([np.log(5.0), np.log(21.0), np.log(63.0)])
    df = pd.concat([v5.rename('a'), v21.rename('b'), v63.rename('c')], axis=1)
    vals = df.values
    out = np.full(len(vals), np.nan, dtype=float)
    for i in range(len(vals)):
        row = vals[i]
        if np.isnan(row).any():
            continue
        y = np.log(row + 1e-12)
        xm = x.mean(); ym = y.mean(); sxx = ((x - xm) ** 2).sum()
        if sxx == 0:
            continue
        out[i] = float(((x - xm) * (y - ym)).sum() / sxx)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff().diff()

def f52_hgrd_115_vol_skew_realized_proxy_252d_d3(close: pd.Series) -> pd.Series:
    """63d-realized downside vol minus 63d-realized upside vol normalized by total - signed vol-skew."""
    r = _log_ret(close)
    neg = ((r ** 2).where(r < 0, 0.0).rolling(QDAYS, min_periods=MDAYS).mean()).pow(0.5)
    pos = ((r ** 2).where(r > 0, 0.0).rolling(QDAYS, min_periods=MDAYS).mean()).pow(0.5)
    return (_safe_div(neg - pos, neg + pos)).diff().diff().diff()

def f52_hgrd_116_vol_uncertainty_index_252d_d3(close: pd.Series) -> pd.Series:
    """Rolling 21d std of EWMA-0.94-vol / mean over 252d - relative uncertainty in vol estimate."""
    r = _log_ret(close)
    v = _ewma_vol(r, 0.94)
    vv = v.rolling(MDAYS, min_periods=10).std()
    vm = v.rolling(MDAYS, min_periods=10).mean()
    return (_safe_div(vv, vm)).diff().diff().diff()

def f52_hgrd_117_vol_dispersion_within_window_iqr_252d_d3(close: pd.Series) -> pd.Series:
    """IQR of EWMA-vol distribution over 252d / median."""
    r = _log_ret(close)
    v = _ewma_vol(r, 0.94)
    iqr = v.rolling(YDAYS, min_periods=QDAYS).quantile(0.75) - v.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    med = v.rolling(YDAYS, min_periods=QDAYS).median()
    return (_safe_div(iqr, med)).diff().diff().diff()

def f52_hgrd_118_vol_dispersion_between_horizons_21_63_252d_d3(close: pd.Series) -> pd.Series:
    """Std across (vol_21d, vol_63d, vol_252d) at current time - horizon disagreement."""
    r = _log_ret(close)
    v5 = ((r ** 2).rolling(MDAYS, min_periods=10).mean()).pow(0.5)
    v63 = ((r ** 2).rolling(QDAYS, min_periods=MDAYS).mean()).pow(0.5)
    v252 = ((r ** 2).rolling(YDAYS, min_periods=QDAYS).mean()).pow(0.5)
    df = pd.concat([v5.rename('a'), v63.rename('b'), v252.rename('c')], axis=1)
    return (df.std(axis=1)).diff().diff().diff()

def f52_hgrd_119_vol_premium_term_struct_change_252d_d3(close: pd.Series) -> pd.Series:
    """21-bar change of (vol_21d - vol_252d) - term-structure-slope momentum."""
    r = _log_ret(close)
    vs = ((r ** 2).rolling(MDAYS, min_periods=10).mean()).pow(0.5)
    vl = ((r ** 2).rolling(YDAYS, min_periods=QDAYS).mean()).pow(0.5)
    spread = vs - vl
    return (spread - spread.shift(MDAYS)).diff().diff().diff()

def f52_hgrd_120_backward_looking_vol_curve_convexity_252d_d3(close: pd.Series) -> pd.Series:
    """(vol_21d + vol_252d) / 2 - vol_63d - curvature of vol term structure over 252d."""
    r = _log_ret(close)
    vs = ((r ** 2).rolling(MDAYS, min_periods=10).mean()).pow(0.5)
    vm = ((r ** 2).rolling(QDAYS, min_periods=MDAYS).mean()).pow(0.5)
    vl = ((r ** 2).rolling(YDAYS, min_periods=QDAYS).mean()).pow(0.5)
    return ((vs + vl) / 2.0 - vm).diff().diff().diff()

def f52_hgrd_121_igarch_persistence_distance_to_one_252d_d3(close: pd.Series) -> pd.Series:
    """1 - GARCH persistence over 252d - distance from IGARCH (=0 if integrated)."""
    r = _log_ret(close)
    p = _rolling_garch11(r, YDAYS, 3)
    return (1.0 - p).diff().diff().diff()

def f52_hgrd_122_vol_persistence_unit_root_proxy_252d_d3(close: pd.Series) -> pd.Series:
    """AR(1) of log-vol minus 1 over 252d - close to 0 = unit root in log-vol."""
    r = _log_ret(close)
    lv = np.log(_ewma_vol(r, 0.94).replace(0, np.nan))
    def _ac(w):
        x = w[~np.isnan(w)]
        if x.size < 20:
            return np.nan
        a = x[:-1]; b = x[1:]
        if a.std() == 0 or b.std() == 0:
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    ar1 = lv.rolling(YDAYS, min_periods=QDAYS).apply(_ac, raw=True)
    return (ar1 - 1.0).diff().diff().diff()

def f52_hgrd_123_integrated_vol_5d_252d_d3(close: pd.Series) -> pd.Series:
    """Rolling 5d cumulative realized variance over 252d."""
    r = _log_ret(close)
    rv = (r ** 2).rolling(5, min_periods=3).sum()
    return (rv).diff().diff().diff()

def f52_hgrd_124_integrated_vol_21d_252d_d3(close: pd.Series) -> pd.Series:
    """Rolling 21d cumulative realized variance."""
    r = _log_ret(close)
    return ((r ** 2).rolling(MDAYS, min_periods=10).sum()).diff().diff().diff()

def f52_hgrd_125_cumulative_vol_persistence_504d_d3(close: pd.Series) -> pd.Series:
    """Cumulative ACF of absolute returns over 504d up to lag 21 - long-memory vol intensity."""
    r = _log_ret(close).abs()
    def _ck(w):
        v = w[~np.isnan(w)]
        if v.size < 50:
            return np.nan
        v = v - v.mean()
        den = float(np.dot(v, v))
        if den <= 0:
            return np.nan
        nv = v.size
        s = 0.0
        for k in range(1, 22):
            if k >= nv:
                break
            s += float(np.dot(v[:nv - k], v[k:]) / den)
        return float(s)
    res = r.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_ck, raw=True)
    return (res).diff().diff().diff()

def f52_hgrd_126_vol_long_memory_via_gph_d_252d_proxy_d3(close: pd.Series) -> pd.Series:
    """Slope of log(periodogram) vs log(freq) at low freq, on |r|, over 252d - long-memory d proxy."""
    x = _log_ret(close).abs()
    def _gph(w):
        v = w[~np.isnan(w)]
        if v.size < 60:
            return np.nan
        v = v - v.mean()
        psd = (np.abs(np.fft.rfft(v)) ** 2)[1:]
        m = max(int(np.sqrt(v.size)), 5)
        if m >= len(psd):
            m = len(psd) - 1
        if m < 5:
            return np.nan
        freqs = 2.0 * np.pi * np.arange(1, m + 1, dtype=float) / v.size
        xs = np.log(2.0 * np.sin(freqs / 2.0))
        ys = np.log(psd[:m])
        mask = np.isfinite(xs) & np.isfinite(ys)
        if mask.sum() < 5:
            return np.nan
        xs = xs[mask]; ys = ys[mask]
        if np.var(xs) == 0:
            return np.nan
        return float(-np.polyfit(xs, ys, 1)[0])
    res = x.rolling(YDAYS, min_periods=QDAYS).apply(_gph, raw=True)
    return (res).diff().diff().diff()

def f52_hgrd_127_vol_stationary_indicator_persistence_lt_0_98_252d_d3(close: pd.Series) -> pd.Series:
    """Indicator: GARCH persistence < 0.98 over 252d (stationary vol)."""
    r = _log_ret(close)
    p = _rolling_garch11(r, YDAYS, 3)
    return ((p < 0.98).astype(float).where(p.notna(), np.nan)).diff().diff().diff()

def f52_hgrd_128_vol_burstiness_index_kurt_norm_252d_d3(close: pd.Series) -> pd.Series:
    """Burstiness B = (sd-mean)/(sd+mean) of inter-event times for |r| > 2*sigma over 252d."""
    r = _log_ret(close)
    sd = _ewma_vol(r, 0.94)
    ind = (r.abs() > 2.0 * sd).astype(float).where(sd.notna(), np.nan)
    def _bb(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        idx = np.where(v > 0.5)[0]
        if idx.size < 3:
            return np.nan
        diffs = np.diff(idx)
        if diffs.size < 2:
            return np.nan
        m = diffs.mean(); s = diffs.std(ddof=1)
        return float((s - m) / (s + m)) if (s + m) > 0 else np.nan
    res = ind.rolling(YDAYS, min_periods=QDAYS).apply(_bb, raw=True)
    return (res).diff().diff().diff()

def f52_hgrd_129_vol_inter_event_time_mean_252d_d3(close: pd.Series) -> pd.Series:
    """Mean bars between |r| > 2*sigma events over 252d."""
    r = _log_ret(close)
    sd = _ewma_vol(r, 0.94)
    ind = (r.abs() > 2.0 * sd).astype(float).where(sd.notna(), np.nan)
    def _ie(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        idx = np.where(v > 0.5)[0]
        if idx.size < 2:
            return np.nan
        return float(np.diff(idx).mean())
    res = ind.rolling(YDAYS, min_periods=QDAYS).apply(_ie, raw=True)
    return (res).diff().diff().diff()

def f52_hgrd_130_vol_squared_acf_intensity_5_252d_d3(close: pd.Series) -> pd.Series:
    """Sum of squared ACF(|r|, k) for k=1..5 over 252d - short-memory vol-cluster intensity."""
    x = _log_ret(close).abs()
    def _sa(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        v = v - v.mean()
        den = float(np.dot(v, v))
        if den <= 0:
            return np.nan
        nv = v.size
        s = 0.0
        for k in range(1, 6):
            rho = float(np.dot(v[:nv - k], v[k:]) / den)
            s += rho * rho
        return float(s)
    res = x.rolling(YDAYS, min_periods=QDAYS).apply(_sa, raw=True)
    return (res).diff().diff().diff()

def f52_hgrd_131_corr_r_with_lag1_absr_252d_leverage_d3(close: pd.Series) -> pd.Series:
    """Pearson corr(r_t, |r_{t-1}|) over 252d - direct leverage-effect signature."""
    r = _log_ret(close)
    lag_abs = r.shift(1).abs()
    return (r.rolling(YDAYS, min_periods=QDAYS).corr(lag_abs)).diff().diff().diff()

def f52_hgrd_132_corr_r_with_lag1_rsq_252d_d3(close: pd.Series) -> pd.Series:
    """Pearson corr(r_t, r_{t-1}^2) over 252d."""
    r = _log_ret(close)
    lag_sq = (r.shift(1)) ** 2
    return (r.rolling(YDAYS, min_periods=QDAYS).corr(lag_sq)).diff().diff().diff()

def f52_hgrd_133_corr_neg_r_lag_with_lead_vol_252d_d3(close: pd.Series) -> pd.Series:
    """Corr(I(r_{t-1}<0)*|r_{t-1}|, EWMA-vol_t) over 252d."""
    r = _log_ret(close)
    lag_neg_amp = ((r.shift(1) < 0).astype(float) * r.shift(1).abs())
    v = _ewma_vol(r, 0.94)
    return (lag_neg_amp.rolling(YDAYS, min_periods=QDAYS).corr(v)).diff().diff().diff()

def f52_hgrd_134_corr_pos_r_lag_with_lead_vol_252d_d3(close: pd.Series) -> pd.Series:
    """Corr(I(r_{t-1}>0)*r_{t-1}, EWMA-vol_t) over 252d."""
    r = _log_ret(close)
    lag_pos_amp = ((r.shift(1) > 0).astype(float) * r.shift(1))
    v = _ewma_vol(r, 0.94)
    return (lag_pos_amp.rolling(YDAYS, min_periods=QDAYS).corr(v)).diff().diff().diff()

def f52_hgrd_135_leverage_asymmetry_index_252d_d3(close: pd.Series) -> pd.Series:
    """Corr(neg-amp, vol) minus corr(pos-amp, vol) over 252d - leverage asymmetry."""
    r = _log_ret(close)
    lag_neg = ((r.shift(1) < 0).astype(float) * r.shift(1).abs())
    lag_pos = ((r.shift(1) > 0).astype(float) * r.shift(1))
    v = _ewma_vol(r, 0.94)
    cn = lag_neg.rolling(YDAYS, min_periods=QDAYS).corr(v)
    cp = lag_pos.rolling(YDAYS, min_periods=QDAYS).corr(v)
    return (cn - cp).diff().diff().diff()

def f52_hgrd_136_squared_return_sign_corr_lag1_252d_d3(close: pd.Series) -> pd.Series:
    """Corr(r_t^2, sign(r_{t-1})) over 252d."""
    r = _log_ret(close)
    sq = r ** 2
    lag_sign = np.sign(r.shift(1))
    return (sq.rolling(YDAYS, min_periods=QDAYS).corr(lag_sign)).diff().diff().diff()

def f52_hgrd_137_squared_return_sign_corr_lag5_252d_d3(close: pd.Series) -> pd.Series:
    """Corr(r_t^2, sign(r_{t-5})) over 252d."""
    r = _log_ret(close)
    sq = r ** 2
    lag5_sign = np.sign(r.shift(5))
    return (sq.rolling(YDAYS, min_periods=QDAYS).corr(lag5_sign)).diff().diff().diff()

def f52_hgrd_138_abs_return_sign_corr_lag1_252d_d3(close: pd.Series) -> pd.Series:
    """Corr(|r_t|, sign(r_{t-1})) over 252d."""
    r = _log_ret(close)
    absr = r.abs()
    lag_sign = np.sign(r.shift(1))
    return (absr.rolling(YDAYS, min_periods=QDAYS).corr(lag_sign)).diff().diff().diff()

def f52_hgrd_139_abs_return_sign_corr_lag5_252d_d3(close: pd.Series) -> pd.Series:
    """Corr(|r_t|, sign(r_{t-5})) over 252d."""
    r = _log_ret(close)
    absr = r.abs()
    lag5_sign = np.sign(r.shift(5))
    return (absr.rolling(YDAYS, min_periods=QDAYS).corr(lag5_sign)).diff().diff().diff()

def f52_hgrd_140_sign_dependence_vol_amp_252d_d3(close: pd.Series) -> pd.Series:
    """Mean( sign(r_{t-1}) * |r_t| ) over 252d - signed return-vol coupling."""
    r = _log_ret(close)
    x = np.sign(r.shift(1)) * r.abs()
    return (x.rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff().diff()

def f52_hgrd_141_composite_garch_persistence_score_252d_d3(close: pd.Series) -> pd.Series:
    """Z-score of GARCH persistence over 252d - regime persistence intensity."""
    r = _log_ret(close)
    p = _rolling_garch11(r, YDAYS, 3)
    return (_rolling_zscore(p, YDAYS)).diff().diff().diff()

def f52_hgrd_142_composite_leverage_score_252d_d3(close: pd.Series) -> pd.Series:
    """Z-sum of GJR-gamma, EGARCH-leverage-proxy, and asym-vol-ratio over 252d."""
    r = _log_ret(close)
    g = _rolling_gjr_garch(r, YDAYS, 2)
    lv = np.log(((r ** 2).rolling(5, min_periods=2).mean()).replace(0, np.nan))
    neg_amp = ((r < 0).astype(float) * r.abs()).shift(1)
    egl = neg_amp.rolling(YDAYS, min_periods=QDAYS).corr(lv)
    sq = r ** 2
    vn = sq.where(r.shift(1) < 0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    vp = sq.where(r.shift(1) > 0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    asym = _safe_div(vn, vp)
    z1 = _rolling_zscore(g, YDAYS); z2 = _rolling_zscore(egl, YDAYS); z3 = _rolling_zscore(asym, YDAYS)
    return (z1.fillna(0.0) + z2.fillna(0.0) + z3.fillna(0.0)).diff().diff().diff()

def f52_hgrd_143_composite_vol_regime_score_252d_d3(close: pd.Series) -> pd.Series:
    """Sum of (vol-zscore + vol-acceleration-zscore + vol-burstiness) over 252d."""
    r = _log_ret(close)
    v = _ewma_vol(r, 0.94)
    z1 = _rolling_zscore(v, YDAYS)
    ch = v - v.shift(MDAYS); z2 = _rolling_zscore(ch, YDAYS)
    sd = _ewma_vol(r, 0.94)
    ind = (r.abs() > 2.0 * sd).astype(float).where(sd.notna(), np.nan)
    def _bb(w):
        v2 = w[~np.isnan(w)]
        if v2.size < 30:
            return np.nan
        idx = np.where(v2 > 0.5)[0]
        if idx.size < 3:
            return np.nan
        diffs = np.diff(idx)
        if diffs.size < 2:
            return np.nan
        m = diffs.mean(); s = diffs.std(ddof=1)
        return float((s - m) / (s + m)) if (s + m) > 0 else np.nan
    b = ind.rolling(YDAYS, min_periods=QDAYS).apply(_bb, raw=True)
    z3 = _rolling_zscore(b, YDAYS)
    return (z1.fillna(0.0) + z2.fillna(0.0) + z3.fillna(0.0)).diff().diff().diff()

def f52_hgrd_144_vol_term_structure_signature_252d_d3(close: pd.Series) -> pd.Series:
    """(vol_21d - vol_252d) z-scored over 252d - term-structure regime indicator."""
    r = _log_ret(close)
    vs = ((r ** 2).rolling(MDAYS, min_periods=10).mean()).pow(0.5)
    vl = ((r ** 2).rolling(YDAYS, min_periods=QDAYS).mean()).pow(0.5)
    spread = vs - vl
    return (_rolling_zscore(spread, YDAYS)).diff().diff().diff()

def f52_hgrd_145_heteroskedasticity_intensity_score_252d_d3(close: pd.Series) -> pd.Series:
    """Sum of ARCH-LM(5) z + ARCH-LM(10) z + ARCH-LM(21) z over 252d."""
    r = _log_ret(close)
    lm5 = _arch_lm_stat(r, YDAYS, 5)
    lm10 = _arch_lm_stat(r, YDAYS, 10)
    lm21 = _arch_lm_stat(r, YDAYS, 21)
    z1 = _rolling_zscore(lm5, YDAYS)
    z2 = _rolling_zscore(lm10, YDAYS); z3 = _rolling_zscore(lm21, YDAYS)
    return (z1.fillna(0.0) + z2.fillna(0.0) + z3.fillna(0.0)).diff().diff().diff()

def f52_hgrd_146_vol_acceleration_composite_252d_d3(close: pd.Series) -> pd.Series:
    """Z-score of GARCH vol minus z-score of long-run vol over 252d."""
    r = _log_ret(close)
    v = _rolling_garch11(r, YDAYS, 4).pow(0.5)
    lr = _rolling_garch11(r, YDAYS, 6).pow(0.5)
    return (_rolling_zscore(v, YDAYS) - _rolling_zscore(lr, YDAYS)).diff().diff().diff()

def f52_hgrd_147_crash_vol_signature_score_252d_d3(close: pd.Series) -> pd.Series:
    """GARCH persistence * GJR leverage gamma * vol z-score over 252d - crash precursor composite."""
    r = _log_ret(close)
    p = _rolling_garch11(r, YDAYS, 3)
    g = _rolling_gjr_garch(r, YDAYS, 2)
    v = _ewma_vol(r, 0.94)
    z = _rolling_zscore(v, YDAYS)
    return (p * g * z).diff().diff().diff()

def f52_hgrd_148_vol_clustering_density_252d_d3(close: pd.Series) -> pd.Series:
    """Mean( I(|r_t| > 2*sigma) * I(|r_{t-1}| > 2*sigma) ) over 252d - paired vol-event density."""
    r = _log_ret(close)
    sd = _ewma_vol(r, 0.94)
    br = (r.abs() > 2.0 * sd).astype(float)
    pair = br * br.shift(1)
    return (pair.rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff().diff()

def f52_hgrd_149_vol_burst_count_above_2sigma_252d_d3(close: pd.Series) -> pd.Series:
    """Count of bars where |r_t| > 2*EWMA-vol_t in last 252d."""
    r = _log_ret(close)
    sd = _ewma_vol(r, 0.94)
    br = (r.abs() > 2.0 * sd).astype(float).where(sd.notna(), np.nan)
    return (br.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()

def f52_hgrd_150_heteroskedasticity_regime_combined_indicator_252d_d3(close: pd.Series) -> pd.Series:
    """Composite: GARCH persistence > 0.95 AND ARCH-LM > 95th pct AND vol-z > 1 over 252d."""
    r = _log_ret(close)
    p = _rolling_garch11(r, YDAYS, 3)
    lm = _arch_lm_stat(r, YDAYS, 10)
    p95_lm = lm.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    v = _ewma_vol(r, 0.94)
    z = _rolling_zscore(v, YDAYS)
    ind = ((p > 0.95) & (lm > p95_lm) & (z > 1.0)).astype(float).where(
        p.notna() & lm.notna() & z.notna(), np.nan)
    return (ind).diff().diff().diff()


# ============================================================
#                         REGISTRY 076_150 (d3)
# ============================================================

HETEROSKEDASTICITY_GARCH_DYNAMICS_D3_REGISTRY_076_150 = {
    "f52_hgrd_076_yang_zhang_var_63d_d3": {"inputs": ["open", "high", "low", "close"], "func": f52_hgrd_076_yang_zhang_var_63d_d3},
    "f52_hgrd_077_ratio_parkinson_to_close_close_var_21d_d3": {"inputs": ["close", "high", "low"], "func": f52_hgrd_077_ratio_parkinson_to_close_close_var_21d_d3},
    "f52_hgrd_078_ratio_garman_klass_to_close_close_var_21d_d3": {"inputs": ["open", "high", "low", "close"], "func": f52_hgrd_078_ratio_garman_klass_to_close_close_var_21d_d3},
    "f52_hgrd_079_ratio_yang_zhang_to_close_close_var_21d_d3": {"inputs": ["open", "high", "low", "close"], "func": f52_hgrd_079_ratio_yang_zhang_to_close_close_var_21d_d3},
    "f52_hgrd_080_range_efficiency_ratio_252d_d3": {"inputs": ["close", "high", "low"], "func": f52_hgrd_080_range_efficiency_ratio_252d_d3},
    "f52_hgrd_081_garch_vol_forecast_1step_252d_d3": {"inputs": ["close"], "func": f52_hgrd_081_garch_vol_forecast_1step_252d_d3},
    "f52_hgrd_082_garch_vol_forecast_21step_252d_d3": {"inputs": ["close"], "func": f52_hgrd_082_garch_vol_forecast_21step_252d_d3},
    "f52_hgrd_083_vol_forecast_diff_ewma_garch_1step_252d_d3": {"inputs": ["close"], "func": f52_hgrd_083_vol_forecast_diff_ewma_garch_1step_252d_d3},
    "f52_hgrd_084_vol_mean_reversion_speed_garch_252d_d3": {"inputs": ["close"], "func": f52_hgrd_084_vol_mean_reversion_speed_garch_252d_d3},
    "f52_hgrd_085_vol_half_life_garch_252d_d3": {"inputs": ["close"], "func": f52_hgrd_085_vol_half_life_garch_252d_d3},
    "f52_hgrd_086_current_vs_long_run_vol_ratio_garch_252d_d3": {"inputs": ["close"], "func": f52_hgrd_086_current_vs_long_run_vol_ratio_garch_252d_d3},
    "f52_hgrd_087_log_vol_persistence_ar1_252d_d3": {"inputs": ["close"], "func": f52_hgrd_087_log_vol_persistence_ar1_252d_d3},
    "f52_hgrd_088_log_vol_unit_root_proxy_adf_252d_d3": {"inputs": ["close"], "func": f52_hgrd_088_log_vol_unit_root_proxy_adf_252d_d3},
    "f52_hgrd_089_ewma_vol_change_speed_acf1_252d_d3": {"inputs": ["close"], "func": f52_hgrd_089_ewma_vol_change_speed_acf1_252d_d3},
    "f52_hgrd_090_garch_long_run_var_change_speed_252d_d3": {"inputs": ["close"], "func": f52_hgrd_090_garch_long_run_var_change_speed_252d_d3},
    "f52_hgrd_091_vol_regime_high_above_p75_252d_indicator_d3": {"inputs": ["close"], "func": f52_hgrd_091_vol_regime_high_above_p75_252d_indicator_d3},
    "f52_hgrd_092_vol_regime_low_below_p25_252d_indicator_d3": {"inputs": ["close"], "func": f52_hgrd_092_vol_regime_low_below_p25_252d_indicator_d3},
    "f52_hgrd_093_vol_regime_above_p75_persistence_63d_d3": {"inputs": ["close"], "func": f52_hgrd_093_vol_regime_above_p75_persistence_63d_d3},
    "f52_hgrd_094_vol_regime_transitions_count_252d_d3": {"inputs": ["close"], "func": f52_hgrd_094_vol_regime_transitions_count_252d_d3},
    "f52_hgrd_095_vol_breakout_above_2sigma_252d_count_d3": {"inputs": ["close"], "func": f52_hgrd_095_vol_breakout_above_2sigma_252d_count_d3},
    "f52_hgrd_096_vol_compression_below_bb_lower_252d_count_d3": {"inputs": ["close"], "func": f52_hgrd_096_vol_compression_below_bb_lower_252d_count_d3},
    "f52_hgrd_097_vol_zscore_above_2_count_252d_d3": {"inputs": ["close"], "func": f52_hgrd_097_vol_zscore_above_2_count_252d_d3},
    "f52_hgrd_098_vol_drawdown_max_252d_d3": {"inputs": ["close"], "func": f52_hgrd_098_vol_drawdown_max_252d_d3},
    "f52_hgrd_099_vol_drawup_max_252d_d3": {"inputs": ["close"], "func": f52_hgrd_099_vol_drawup_max_252d_d3},
    "f52_hgrd_100_vol_skewness_in_vol_space_252d_d3": {"inputs": ["close"], "func": f52_hgrd_100_vol_skewness_in_vol_space_252d_d3},
    "f52_hgrd_101_asymmetric_vol_after_neg_252d_d3": {"inputs": ["close"], "func": f52_hgrd_101_asymmetric_vol_after_neg_252d_d3},
    "f52_hgrd_102_asymmetric_vol_after_pos_252d_d3": {"inputs": ["close"], "func": f52_hgrd_102_asymmetric_vol_after_pos_252d_d3},
    "f52_hgrd_103_asymmetric_vol_ratio_neg_to_pos_252d_d3": {"inputs": ["close"], "func": f52_hgrd_103_asymmetric_vol_ratio_neg_to_pos_252d_d3},
    "f52_hgrd_104_news_impact_curve_slope_neg_252d_d3": {"inputs": ["close"], "func": f52_hgrd_104_news_impact_curve_slope_neg_252d_d3},
    "f52_hgrd_105_news_impact_curve_slope_pos_252d_d3": {"inputs": ["close"], "func": f52_hgrd_105_news_impact_curve_slope_pos_252d_d3},
    "f52_hgrd_106_realized_semi_var_negative_63d_d3": {"inputs": ["close"], "func": f52_hgrd_106_realized_semi_var_negative_63d_d3},
    "f52_hgrd_107_realized_semi_var_positive_63d_d3": {"inputs": ["close"], "func": f52_hgrd_107_realized_semi_var_positive_63d_d3},
    "f52_hgrd_108_semi_var_persistence_negative_ar1_252d_d3": {"inputs": ["close"], "func": f52_hgrd_108_semi_var_persistence_negative_ar1_252d_d3},
    "f52_hgrd_109_semi_var_persistence_positive_ar1_252d_d3": {"inputs": ["close"], "func": f52_hgrd_109_semi_var_persistence_positive_ar1_252d_d3},
    "f52_hgrd_110_asymmetric_realized_vol_diff_252d_d3": {"inputs": ["close"], "func": f52_hgrd_110_asymmetric_realized_vol_diff_252d_d3},
    "f52_hgrd_111_realized_minus_ewma_vol_252d_d3": {"inputs": ["close"], "func": f52_hgrd_111_realized_minus_ewma_vol_252d_d3},
    "f52_hgrd_112_realized_minus_garch_vol_252d_d3": {"inputs": ["close"], "func": f52_hgrd_112_realized_minus_garch_vol_252d_d3},
    "f52_hgrd_113_vol_term_struct_short_minus_long_realized_252d_d3": {"inputs": ["close"], "func": f52_hgrd_113_vol_term_struct_short_minus_long_realized_252d_d3},
    "f52_hgrd_114_realized_vol_curve_slope_5_21_63_252d_d3": {"inputs": ["close"], "func": f52_hgrd_114_realized_vol_curve_slope_5_21_63_252d_d3},
    "f52_hgrd_115_vol_skew_realized_proxy_252d_d3": {"inputs": ["close"], "func": f52_hgrd_115_vol_skew_realized_proxy_252d_d3},
    "f52_hgrd_116_vol_uncertainty_index_252d_d3": {"inputs": ["close"], "func": f52_hgrd_116_vol_uncertainty_index_252d_d3},
    "f52_hgrd_117_vol_dispersion_within_window_iqr_252d_d3": {"inputs": ["close"], "func": f52_hgrd_117_vol_dispersion_within_window_iqr_252d_d3},
    "f52_hgrd_118_vol_dispersion_between_horizons_21_63_252d_d3": {"inputs": ["close"], "func": f52_hgrd_118_vol_dispersion_between_horizons_21_63_252d_d3},
    "f52_hgrd_119_vol_premium_term_struct_change_252d_d3": {"inputs": ["close"], "func": f52_hgrd_119_vol_premium_term_struct_change_252d_d3},
    "f52_hgrd_120_backward_looking_vol_curve_convexity_252d_d3": {"inputs": ["close"], "func": f52_hgrd_120_backward_looking_vol_curve_convexity_252d_d3},
    "f52_hgrd_121_igarch_persistence_distance_to_one_252d_d3": {"inputs": ["close"], "func": f52_hgrd_121_igarch_persistence_distance_to_one_252d_d3},
    "f52_hgrd_122_vol_persistence_unit_root_proxy_252d_d3": {"inputs": ["close"], "func": f52_hgrd_122_vol_persistence_unit_root_proxy_252d_d3},
    "f52_hgrd_123_integrated_vol_5d_252d_d3": {"inputs": ["close"], "func": f52_hgrd_123_integrated_vol_5d_252d_d3},
    "f52_hgrd_124_integrated_vol_21d_252d_d3": {"inputs": ["close"], "func": f52_hgrd_124_integrated_vol_21d_252d_d3},
    "f52_hgrd_125_cumulative_vol_persistence_504d_d3": {"inputs": ["close"], "func": f52_hgrd_125_cumulative_vol_persistence_504d_d3},
    "f52_hgrd_126_vol_long_memory_via_gph_d_252d_proxy_d3": {"inputs": ["close"], "func": f52_hgrd_126_vol_long_memory_via_gph_d_252d_proxy_d3},
    "f52_hgrd_127_vol_stationary_indicator_persistence_lt_0_98_252d_d3": {"inputs": ["close"], "func": f52_hgrd_127_vol_stationary_indicator_persistence_lt_0_98_252d_d3},
    "f52_hgrd_128_vol_burstiness_index_kurt_norm_252d_d3": {"inputs": ["close"], "func": f52_hgrd_128_vol_burstiness_index_kurt_norm_252d_d3},
    "f52_hgrd_129_vol_inter_event_time_mean_252d_d3": {"inputs": ["close"], "func": f52_hgrd_129_vol_inter_event_time_mean_252d_d3},
    "f52_hgrd_130_vol_squared_acf_intensity_5_252d_d3": {"inputs": ["close"], "func": f52_hgrd_130_vol_squared_acf_intensity_5_252d_d3},
    "f52_hgrd_131_corr_r_with_lag1_absr_252d_leverage_d3": {"inputs": ["close"], "func": f52_hgrd_131_corr_r_with_lag1_absr_252d_leverage_d3},
    "f52_hgrd_132_corr_r_with_lag1_rsq_252d_d3": {"inputs": ["close"], "func": f52_hgrd_132_corr_r_with_lag1_rsq_252d_d3},
    "f52_hgrd_133_corr_neg_r_lag_with_lead_vol_252d_d3": {"inputs": ["close"], "func": f52_hgrd_133_corr_neg_r_lag_with_lead_vol_252d_d3},
    "f52_hgrd_134_corr_pos_r_lag_with_lead_vol_252d_d3": {"inputs": ["close"], "func": f52_hgrd_134_corr_pos_r_lag_with_lead_vol_252d_d3},
    "f52_hgrd_135_leverage_asymmetry_index_252d_d3": {"inputs": ["close"], "func": f52_hgrd_135_leverage_asymmetry_index_252d_d3},
    "f52_hgrd_136_squared_return_sign_corr_lag1_252d_d3": {"inputs": ["close"], "func": f52_hgrd_136_squared_return_sign_corr_lag1_252d_d3},
    "f52_hgrd_137_squared_return_sign_corr_lag5_252d_d3": {"inputs": ["close"], "func": f52_hgrd_137_squared_return_sign_corr_lag5_252d_d3},
    "f52_hgrd_138_abs_return_sign_corr_lag1_252d_d3": {"inputs": ["close"], "func": f52_hgrd_138_abs_return_sign_corr_lag1_252d_d3},
    "f52_hgrd_139_abs_return_sign_corr_lag5_252d_d3": {"inputs": ["close"], "func": f52_hgrd_139_abs_return_sign_corr_lag5_252d_d3},
    "f52_hgrd_140_sign_dependence_vol_amp_252d_d3": {"inputs": ["close"], "func": f52_hgrd_140_sign_dependence_vol_amp_252d_d3},
    "f52_hgrd_141_composite_garch_persistence_score_252d_d3": {"inputs": ["close"], "func": f52_hgrd_141_composite_garch_persistence_score_252d_d3},
    "f52_hgrd_142_composite_leverage_score_252d_d3": {"inputs": ["close"], "func": f52_hgrd_142_composite_leverage_score_252d_d3},
    "f52_hgrd_143_composite_vol_regime_score_252d_d3": {"inputs": ["close"], "func": f52_hgrd_143_composite_vol_regime_score_252d_d3},
    "f52_hgrd_144_vol_term_structure_signature_252d_d3": {"inputs": ["close"], "func": f52_hgrd_144_vol_term_structure_signature_252d_d3},
    "f52_hgrd_145_heteroskedasticity_intensity_score_252d_d3": {"inputs": ["close"], "func": f52_hgrd_145_heteroskedasticity_intensity_score_252d_d3},
    "f52_hgrd_146_vol_acceleration_composite_252d_d3": {"inputs": ["close"], "func": f52_hgrd_146_vol_acceleration_composite_252d_d3},
    "f52_hgrd_147_crash_vol_signature_score_252d_d3": {"inputs": ["close"], "func": f52_hgrd_147_crash_vol_signature_score_252d_d3},
    "f52_hgrd_148_vol_clustering_density_252d_d3": {"inputs": ["close"], "func": f52_hgrd_148_vol_clustering_density_252d_d3},
    "f52_hgrd_149_vol_burst_count_above_2sigma_252d_d3": {"inputs": ["close"], "func": f52_hgrd_149_vol_burst_count_above_2sigma_252d_d3},
    "f52_hgrd_150_heteroskedasticity_regime_combined_indicator_252d_d3": {"inputs": ["close"], "func": f52_hgrd_150_heteroskedasticity_regime_combined_indicator_252d_d3},
}
