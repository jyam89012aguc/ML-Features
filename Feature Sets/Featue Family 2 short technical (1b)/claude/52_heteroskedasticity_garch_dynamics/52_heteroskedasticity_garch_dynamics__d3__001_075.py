"""heteroskedasticity_garch_dynamics d3 features 001-075 - Pipeline 1b-technical.

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


def f52_hgrd_001_ewma_var_lambda094_log_ret_d3(close: pd.Series) -> pd.Series:
    """RiskMetrics EWMA variance with lambda=0.94 - standard short-memory vol estimate."""
    r = _log_ret(close)
    return (_ewma_var(r ** 2, 0.94)).diff().diff().diff()

def f52_hgrd_002_ewma_var_lambda097_log_ret_d3(close: pd.Series) -> pd.Series:
    """EWMA variance with lambda=0.97 - longer memory (RiskMetrics long horizon)."""
    r = _log_ret(close)
    return (_ewma_var(r ** 2, 0.97)).diff().diff().diff()

def f52_hgrd_003_ewma_var_lambda090_log_ret_d3(close: pd.Series) -> pd.Series:
    """EWMA variance with lambda=0.90 - shorter memory (more responsive)."""
    r = _log_ret(close)
    return (_ewma_var(r ** 2, 0.90)).diff().diff().diff()

def f52_hgrd_004_ewma_vol_lambda094_log_ret_d3(close: pd.Series) -> pd.Series:
    """RiskMetrics EWMA volatility (sqrt of variance) - daily vol estimate."""
    r = _log_ret(close)
    return (_ewma_vol(r, 0.94)).diff().diff().diff()

def f52_hgrd_005_ewma_vol_lambda094_pct_change_21d_d3(close: pd.Series) -> pd.Series:
    """21-bar percentage change in EWMA-0.94 volatility - vol acceleration."""
    r = _log_ret(close)
    v = _ewma_vol(r, 0.94)
    return (_safe_div(v - v.shift(MDAYS), v.shift(MDAYS))).diff().diff().diff()

def f52_hgrd_006_ewma_filtered_standardized_log_ret_d3(close: pd.Series) -> pd.Series:
    """r_t / EWMA-0.94-vol_t - standardized innovation (z-score under EWMA)."""
    r = _log_ret(close)
    v = _ewma_vol(r, 0.94)
    return (_safe_div(r, v)).diff().diff().diff()

def f52_hgrd_007_ewma_var_persistence_acf1_252d_d3(close: pd.Series) -> pd.Series:
    """AR(1) of EWMA-0.94 variance series over 252d - vol persistence under EWMA model."""
    r = _log_ret(close)
    v = _ewma_var(r ** 2, 0.94)
    def _ac(w):
        x = w[~np.isnan(w)]
        if x.size < 20:
            return np.nan
        a = x[:-1]; b = x[1:]
        if a.std() == 0 or b.std() == 0:
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    res = v.rolling(YDAYS, min_periods=QDAYS).apply(_ac, raw=True)
    return (res).diff().diff().diff()

def f52_hgrd_008_ewma_var_to_realized_var_ratio_63d_d3(close: pd.Series) -> pd.Series:
    """EWMA-0.94 variance / 63d realized variance - model/empirical gap."""
    r = _log_ret(close)
    v = _ewma_var(r ** 2, 0.94)
    rv = (r ** 2).rolling(QDAYS, min_periods=MDAYS).mean()
    return (_safe_div(v, rv)).diff().diff().diff()

def f52_hgrd_009_ewma_innovation_variance_252d_d3(close: pd.Series) -> pd.Series:
    """Variance of standardized residuals r/EWMA-vol over 252d - should be ~1 if model fits."""
    r = _log_ret(close)
    v = _ewma_vol(r, 0.94)
    z = _safe_div(r, v)
    return (z.rolling(YDAYS, min_periods=QDAYS).var()).diff().diff().diff()

def f52_hgrd_010_ewma_short_minus_long_vol_diff_d3(close: pd.Series) -> pd.Series:
    """EWMA(0.90) vol minus EWMA(0.97) vol - short vs long memory gap (>0 means recent vol up)."""
    r = _log_ret(close)
    vs = _ewma_vol(r, 0.90)
    vl = _ewma_vol(r, 0.97)
    return (vs - vl).diff().diff().diff()

def f52_hgrd_011_garch11_alpha_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """GARCH(1,1) ARCH coefficient alpha estimated over 252d via grid-search MLE."""
    r = _log_ret(close)
    return (_rolling_garch11(r, YDAYS, 0)).diff().diff().diff()

def f52_hgrd_012_garch11_beta_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """GARCH(1,1) GARCH coefficient beta over 252d."""
    r = _log_ret(close)
    return (_rolling_garch11(r, YDAYS, 1)).diff().diff().diff()

def f52_hgrd_013_garch11_omega_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """GARCH(1,1) intercept omega over 252d (= (1-alpha-beta) * uncond_var)."""
    r = _log_ret(close)
    return (_rolling_garch11(r, YDAYS, 2)).diff().diff().diff()

def f52_hgrd_014_garch11_persistence_alpha_plus_beta_252d_d3(close: pd.Series) -> pd.Series:
    """GARCH(1,1) persistence (alpha + beta) over 252d - close to 1 = high vol persistence."""
    r = _log_ret(close)
    return (_rolling_garch11(r, YDAYS, 3)).diff().diff().diff()

def f52_hgrd_015_garch11_current_sigma2_252d_d3(close: pd.Series) -> pd.Series:
    """GARCH(1,1) current-bar conditional variance estimate over 252d."""
    r = _log_ret(close)
    return (_rolling_garch11(r, YDAYS, 4)).diff().diff().diff()

def f52_hgrd_016_garch11_loglikelihood_252d_d3(close: pd.Series) -> pd.Series:
    """GARCH(1,1) maximized log-likelihood over 252d - model fit quality."""
    r = _log_ret(close)
    return (_rolling_garch11(r, YDAYS, 5)).diff().diff().diff()

def f52_hgrd_017_garch11_long_run_var_252d_d3(close: pd.Series) -> pd.Series:
    """GARCH(1,1) long-run variance omega/(1-alpha-beta) over 252d."""
    r = _log_ret(close)
    return (_rolling_garch11(r, YDAYS, 6)).diff().diff().diff()

def f52_hgrd_018_garch11_aic_252d_d3(close: pd.Series) -> pd.Series:
    """GARCH(1,1) Akaike Information Criterion over 252d (-2LL + 2k)."""
    r = _log_ret(close)
    return (_rolling_garch11(r, YDAYS, 7)).diff().diff().diff()

def f52_hgrd_019_garch11_alpha_to_beta_ratio_252d_d3(close: pd.Series) -> pd.Series:
    """GARCH(1,1) alpha/beta ratio - relative ARCH vs GARCH contribution."""
    r = _log_ret(close)
    a = _rolling_garch11(r, YDAYS, 0)
    b = _rolling_garch11(r, YDAYS, 1)
    return (_safe_div(a, b)).diff().diff().diff()

def f52_hgrd_020_garch11_persistence_504d_d3(close: pd.Series) -> pd.Series:
    """GARCH(1,1) persistence over 504d window - long-horizon vol persistence."""
    r = _log_ret(close)
    return (_rolling_garch11(r, DDAYS_2Y, 3)).diff().diff().diff()

def f52_hgrd_021_gjr_garch_leverage_gamma_252d_d3(close: pd.Series) -> pd.Series:
    """GJR-GARCH leverage parameter gamma over 252d - asymmetric impact of negative shocks on vol."""
    r = _log_ret(close)
    return (_rolling_gjr_garch(r, YDAYS, 2)).diff().diff().diff()

def f52_hgrd_022_gjr_garch_alpha_252d_d3(close: pd.Series) -> pd.Series:
    """GJR-GARCH alpha coefficient over 252d."""
    r = _log_ret(close)
    return (_rolling_gjr_garch(r, YDAYS, 0)).diff().diff().diff()

def f52_hgrd_023_gjr_garch_beta_252d_d3(close: pd.Series) -> pd.Series:
    """GJR-GARCH beta coefficient over 252d."""
    r = _log_ret(close)
    return (_rolling_gjr_garch(r, YDAYS, 1)).diff().diff().diff()

def f52_hgrd_024_gjr_garch_persistence_252d_d3(close: pd.Series) -> pd.Series:
    """GJR-GARCH persistence (alpha + beta + gamma/2) over 252d."""
    r = _log_ret(close)
    return (_rolling_gjr_garch(r, YDAYS, 4)).diff().diff().diff()

def f52_hgrd_025_gjr_garch_current_sigma2_252d_d3(close: pd.Series) -> pd.Series:
    """GJR-GARCH current conditional variance over 252d."""
    r = _log_ret(close)
    return (_rolling_gjr_garch(r, YDAYS, 5)).diff().diff().diff()

def f52_hgrd_026_gjr_garch_loglikelihood_252d_d3(close: pd.Series) -> pd.Series:
    """GJR-GARCH log-likelihood over 252d."""
    r = _log_ret(close)
    return (_rolling_gjr_garch(r, YDAYS, 6)).diff().diff().diff()

def f52_hgrd_027_gjr_garch_leverage_gamma_to_alpha_ratio_252d_d3(close: pd.Series) -> pd.Series:
    """GJR gamma / alpha ratio over 252d - relative leverage vs symmetric response."""
    r = _log_ret(close)
    g = _rolling_gjr_garch(r, YDAYS, 2)
    a = _rolling_gjr_garch(r, YDAYS, 0)
    return (_safe_div(g, a)).diff().diff().diff()

def f52_hgrd_028_gjr_garch_minus_garch11_persistence_252d_d3(close: pd.Series) -> pd.Series:
    """GJR-GARCH persistence minus GARCH(1,1) persistence over 252d - extra persistence from leverage."""
    r = _log_ret(close)
    p_gjr = _rolling_gjr_garch(r, YDAYS, 4)
    p_grc = _rolling_garch11(r, YDAYS, 3)
    return (p_gjr - p_grc).diff().diff().diff()

def f52_hgrd_029_egarch_leverage_proxy_corr_neg_r_log_vol_252d_d3(close: pd.Series) -> pd.Series:
    """EGARCH leverage proxy: corr( I(r<0)*|r| , log_vol_next ) over 252d."""
    r = _log_ret(close)
    lv = np.log(((r ** 2).rolling(5, min_periods=2).mean()).replace(0, np.nan))
    neg_amp = ((r < 0).astype(float) * r.abs()).shift(1)
    return (neg_amp.rolling(YDAYS, min_periods=QDAYS).corr(lv)).diff().diff().diff()

def f52_hgrd_030_egarch_persistence_log_vol_ar1_252d_d3(close: pd.Series) -> pd.Series:
    """AR(1) of log realized vol (EGARCH persistence proxy) over 252d."""
    r = _log_ret(close)
    lv = np.log(((r ** 2).rolling(5, min_periods=2).mean()).replace(0, np.nan))
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

def f52_hgrd_031_arch_lm_lag5_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Engle ARCH-LM test stat at lag 5 over 252d."""
    r = _log_ret(close)
    return (_arch_lm_stat(r, YDAYS, 5)).diff().diff().diff()

def f52_hgrd_032_arch_lm_lag10_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """ARCH-LM at lag 10 over 252d."""
    r = _log_ret(close)
    return (_arch_lm_stat(r, YDAYS, 10)).diff().diff().diff()

def f52_hgrd_033_arch_lm_lag21_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """ARCH-LM at lag 21 over 252d."""
    r = _log_ret(close)
    return (_arch_lm_stat(r, YDAYS, 21)).diff().diff().diff()

def f52_hgrd_034_arch_lm_lag5_log_ret_504d_d3(close: pd.Series) -> pd.Series:
    """ARCH-LM at lag 5 over 504d."""
    r = _log_ret(close)
    return (_arch_lm_stat(r, DDAYS_2Y, 5)).diff().diff().diff()

def f52_hgrd_035_mcleod_li_lag10_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """McLeod-Li (Ljung-Box on r^2) at lag 10 over 252d."""
    r = _log_ret(close)
    return (_ljung_box_q_on_sq(r, YDAYS, 10)).diff().diff().diff()

def f52_hgrd_036_mcleod_li_lag21_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """McLeod-Li at lag 21 over 252d."""
    r = _log_ret(close)
    return (_ljung_box_q_on_sq(r, YDAYS, 21)).diff().diff().diff()

def f52_hgrd_037_white_heteroskedasticity_test_proxy_252d_d3(close: pd.Series) -> pd.Series:
    """White heteroskedasticity test: R^2 of r^2 ~ a + b*r + c*r^2 (sigma vs sign+level)."""
    r = _log_ret(close)
    mp = max(YDAYS // 3, 30)
    def _wh(w):
        v = w[~np.isnan(w)]
        if v.size < 60:
            return np.nan
        sq = v * v
        X = np.column_stack([np.ones(v.size), v, sq])
        try:
            beta, *_ = np.linalg.lstsq(X, sq, rcond=None)
        except np.linalg.LinAlgError:
            return np.nan
        pred = X @ beta
        ss_res = float(np.sum((sq - pred) ** 2)); ss_tot = float(np.sum((sq - sq.mean()) ** 2))
        if ss_tot <= 0:
            return np.nan
        r2 = 1.0 - ss_res / ss_tot
        return float(v.size * r2)
    res = r.rolling(YDAYS, min_periods=mp).apply(_wh, raw=True)
    return (res).diff().diff().diff()

def f52_hgrd_038_breusch_pagan_test_proxy_252d_d3(close: pd.Series) -> pd.Series:
    """Breusch-Pagan test proxy: BP = 0.5 * R^2_explained over 252d using r as regressor."""
    r = _log_ret(close)
    mp = max(YDAYS // 3, 30)
    def _bp(w):
        v = w[~np.isnan(w)]
        if v.size < 60:
            return np.nan
        sq = v * v
        X = np.column_stack([np.ones(v.size), v])
        try:
            beta, *_ = np.linalg.lstsq(X, sq, rcond=None)
        except np.linalg.LinAlgError:
            return np.nan
        pred = X @ beta
        ss_res = float(np.sum((sq - pred) ** 2)); ss_tot = float(np.sum((sq - sq.mean()) ** 2))
        if ss_tot <= 0:
            return np.nan
        return float(0.5 * v.size * (1.0 - ss_res / ss_tot))
    res = r.rolling(YDAYS, min_periods=mp).apply(_bp, raw=True)
    return (res).diff().diff().diff()

def f52_hgrd_039_arch_effect_intensity_zscore_252d_d3(close: pd.Series) -> pd.Series:
    """Z-score over 252d of ARCH-LM(10) stat - relative regime of ARCH effects."""
    r = _log_ret(close)
    lm = _arch_lm_stat(r, YDAYS, 10)
    return (_rolling_zscore(lm, YDAYS)).diff().diff().diff()

def f52_hgrd_040_standardized_resid_normality_jb_garch_252d_d3(close: pd.Series) -> pd.Series:
    """Jarque-Bera on GARCH(1,1)-standardized residuals over 252d."""
    r = _log_ret(close)
    s2 = _rolling_garch11(r, YDAYS, 4)
    z = _safe_div(r, s2.pow(0.5))
    mp = max(YDAYS // 3, 10)
    sk = z.rolling(YDAYS, min_periods=mp).skew()
    kt = z.rolling(YDAYS, min_periods=mp).kurt()
    cnt = z.rolling(YDAYS, min_periods=mp).count()
    return ((cnt / 6.0) * (sk ** 2 + 0.25 * (kt ** 2))).diff().diff().diff()

def f52_hgrd_041_vol_of_ewma_vol_lambda094_252d_d3(close: pd.Series) -> pd.Series:
    """Rolling 252d std of EWMA-0.94 daily vol - vol-of-vol under EWMA model."""
    r = _log_ret(close)
    v = _ewma_vol(r, 0.94)
    return (v.rolling(YDAYS, min_periods=QDAYS).std()).diff().diff().diff()

def f52_hgrd_042_vol_of_garch_vol_252d_d3(close: pd.Series) -> pd.Series:
    """Rolling 252d std of GARCH-conditional vol estimate."""
    r = _log_ret(close)
    s2 = _rolling_garch11(r, YDAYS, 4)
    return (s2.pow(0.5).rolling(YDAYS, min_periods=QDAYS).std()).diff().diff().diff()

def f52_hgrd_043_ratio_ewma_var_to_garch_var_252d_d3(close: pd.Series) -> pd.Series:
    """EWMA-0.94 variance divided by GARCH-current variance over 252d."""
    r = _log_ret(close)
    ve = _ewma_var(r ** 2, 0.94)
    vg = _rolling_garch11(r, YDAYS, 4)
    return (_safe_div(ve, vg)).diff().diff().diff()

def f52_hgrd_044_garch_vol_acceleration_252d_d3(close: pd.Series) -> pd.Series:
    """21-bar diff of GARCH conditional vol divided by current GARCH vol."""
    r = _log_ret(close)
    v = _rolling_garch11(r, YDAYS, 4).pow(0.5)
    return (_safe_div(v - v.shift(MDAYS), v)).diff().diff().diff()

def f52_hgrd_045_conditional_vol_skewness_252d_d3(close: pd.Series) -> pd.Series:
    """Skewness of EWMA daily vol distribution over 252d."""
    r = _log_ret(close)
    v = _ewma_vol(r, 0.94)
    return (v.rolling(YDAYS, min_periods=QDAYS).skew()).diff().diff().diff()

def f52_hgrd_046_conditional_vol_kurtosis_252d_d3(close: pd.Series) -> pd.Series:
    """Excess kurtosis of EWMA vol over 252d."""
    r = _log_ret(close)
    v = _ewma_vol(r, 0.94)
    return (v.rolling(YDAYS, min_periods=QDAYS).kurt()).diff().diff().diff()

def f52_hgrd_047_vol_clustering_intensity_via_arch_lm_252d_d3(close: pd.Series) -> pd.Series:
    """ARCH-LM(5) stat normalized by 252d-rolling 90th-percentile - vol clustering intensity."""
    r = _log_ret(close)
    lm = _arch_lm_stat(r, YDAYS, 5)
    p90 = lm.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    return (_safe_div(lm, p90)).diff().diff().diff()

def f52_hgrd_048_vol_acceleration_z_score_252d_d3(close: pd.Series) -> pd.Series:
    """Z-score over 252d of 21-bar EWMA-vol change."""
    r = _log_ret(close)
    v = _ewma_vol(r, 0.94)
    ch = v - v.shift(MDAYS)
    return (_rolling_zscore(ch, YDAYS)).diff().diff().diff()

def f52_hgrd_049_conditional_vol_autocorr_lag1_252d_d3(close: pd.Series) -> pd.Series:
    """ACF(1) of EWMA vol over 252d."""
    r = _log_ret(close)
    v = _ewma_vol(r, 0.94)
    def _ac(w):
        x = w[~np.isnan(w)]
        if x.size < 20:
            return np.nan
        a = x[:-1]; b = x[1:]
        if a.std() == 0 or b.std() == 0:
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    res = v.rolling(YDAYS, min_periods=QDAYS).apply(_ac, raw=True)
    return (res).diff().diff().diff()

def f52_hgrd_050_conditional_vol_autocorr_lag21_252d_d3(close: pd.Series) -> pd.Series:
    """ACF(21) of EWMA vol over 252d - monthly persistence."""
    r = _log_ret(close)
    v = _ewma_vol(r, 0.94)
    def _ac(w):
        x = w[~np.isnan(w)]
        if x.size < 30:
            return np.nan
        a = x[:-21]; b = x[21:]
        if a.std() == 0 or b.std() == 0:
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    res = v.rolling(YDAYS, min_periods=QDAYS).apply(_ac, raw=True)
    return (res).diff().diff().diff()

def f52_hgrd_051_fhs_var_95_ewma094_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Filtered Historical Simulation 95% VaR (EWMA-0.94 filter) over 252d."""
    r = _log_ret(close)
    return (_fhs_var(r, YDAYS, 0.95, 0.94)).diff().diff().diff()

def f52_hgrd_052_fhs_var_99_ewma094_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """FHS 99% VaR (EWMA-0.94) over 252d."""
    r = _log_ret(close)
    return (_fhs_var(r, YDAYS, 0.99, 0.94)).diff().diff().diff()

def f52_hgrd_053_fhs_var_995_ewma094_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """FHS 99.5% VaR over 252d."""
    r = _log_ret(close)
    return (_fhs_var(r, YDAYS, 0.995, 0.94)).diff().diff().diff()

def f52_hgrd_054_fhs_es_95_ewma094_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """FHS 95% Expected Shortfall over 252d."""
    r = _log_ret(close)
    return (_fhs_es(r, YDAYS, 0.95, 0.94)).diff().diff().diff()

def f52_hgrd_055_fhs_es_99_ewma094_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """FHS 99% ES over 252d."""
    r = _log_ret(close)
    return (_fhs_es(r, YDAYS, 0.99, 0.94)).diff().diff().diff()

def f52_hgrd_056_fhs_var_minus_hist_var_95_252d_d3(close: pd.Series) -> pd.Series:
    """FHS VaR(95) minus historical VaR(95) over 252d - filter contribution."""
    r = _log_ret(close)
    fh = _fhs_var(r, YDAYS, 0.95, 0.94)
    hi = -_rolling_q(r, YDAYS, 0.05)
    return (fh - hi).diff().diff().diff()

def f52_hgrd_057_fhs_innovation_skew_252d_d3(close: pd.Series) -> pd.Series:
    """Skewness of FHS innovations (r / EWMA-vol) over 252d."""
    r = _log_ret(close)
    v = _ewma_vol(r, 0.94)
    z = _safe_div(r, v)
    return (_rolling_skew(z, YDAYS)).diff().diff().diff()

def f52_hgrd_058_fhs_innovation_kurt_252d_d3(close: pd.Series) -> pd.Series:
    """Excess kurt of FHS innovations over 252d."""
    r = _log_ret(close)
    v = _ewma_vol(r, 0.94)
    z = _safe_div(r, v)
    return (_rolling_kurt(z, YDAYS)).diff().diff().diff()

def f52_hgrd_059_fhs_innovation_var_252d_d3(close: pd.Series) -> pd.Series:
    """Variance of FHS innovations over 252d - should be ~1 if EWMA fits."""
    r = _log_ret(close)
    v = _ewma_vol(r, 0.94)
    z = _safe_div(r, v)
    return (z.rolling(YDAYS, min_periods=QDAYS).var()).diff().diff().diff()

def f52_hgrd_060_fhs_es_to_var_ratio_95_252d_d3(close: pd.Series) -> pd.Series:
    """FHS ES(95) / FHS VaR(95) over 252d - tail conditional severity under filter."""
    r = _log_ret(close)
    es = _fhs_es(r, YDAYS, 0.95, 0.94)
    v = _fhs_var(r, YDAYS, 0.95, 0.94)
    return (_safe_div(es, v)).diff().diff().diff()

def f52_hgrd_061_std_resid_skew_garch11_252d_d3(close: pd.Series) -> pd.Series:
    """Skewness of GARCH(1,1)-standardized residuals z=r/sigma over 252d."""
    r = _log_ret(close)
    s2 = _rolling_garch11(r, YDAYS, 4)
    z = _safe_div(r, s2.pow(0.5))
    return (_rolling_skew(z, YDAYS)).diff().diff().diff()

def f52_hgrd_062_std_resid_kurt_garch11_252d_d3(close: pd.Series) -> pd.Series:
    """Excess kurt of GARCH(1,1)-standardized residuals over 252d."""
    r = _log_ret(close)
    s2 = _rolling_garch11(r, YDAYS, 4)
    z = _safe_div(r, s2.pow(0.5))
    return (_rolling_kurt(z, YDAYS)).diff().diff().diff()

def f52_hgrd_063_std_resid_ks_normality_garch11_252d_d3(close: pd.Series) -> pd.Series:
    """KS distance of GARCH-standardized residuals to N(0,1) over 252d."""
    r = _log_ret(close)
    s2 = _rolling_garch11(r, YDAYS, 4)
    z = _safe_div(r, s2.pow(0.5))
    mp = max(YDAYS // 3, 30)
    def _ks(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        v = np.sort(v)
        cdf = np.array([_norm_cdf(zi) for zi in v])
        ec = np.arange(1, v.size + 1, dtype=float) / v.size
        return float(np.max(np.abs(cdf - ec)))
    res = z.rolling(YDAYS, min_periods=mp).apply(_ks, raw=True)
    return (res).diff().diff().diff()

def f52_hgrd_064_std_resid_ljung_box_lag10_garch11_252d_d3(close: pd.Series) -> pd.Series:
    """Ljung-Box Q at lag 10 on GARCH-standardized residuals over 252d."""
    r = _log_ret(close)
    s2 = _rolling_garch11(r, YDAYS, 4)
    z = _safe_div(r, s2.pow(0.5))
    mp = max(YDAYS // 3, 30)
    def _lb(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        v = v - v.mean()
        den = float(np.dot(v, v))
        if den <= 0:
            return np.nan
        nv = v.size; q = 0.0
        for k in range(1, 11):
            rho = float(np.dot(v[:nv - k], v[k:]) / den)
            q += rho * rho / (nv - k)
        return float(nv * (nv + 2) * q)
    res = z.rolling(YDAYS, min_periods=mp).apply(_lb, raw=True)
    return (res).diff().diff().diff()

def f52_hgrd_065_std_resid_squared_arch_lm_garch11_252d_d3(close: pd.Series) -> pd.Series:
    """ARCH-LM(5) on GARCH-standardized squared residuals over 252d - should be small if GARCH fits."""
    r = _log_ret(close)
    s2 = _rolling_garch11(r, YDAYS, 4)
    z = _safe_div(r, s2.pow(0.5))
    return (_arch_lm_stat(z, YDAYS, 5)).diff().diff().diff()

def f52_hgrd_066_ewma_std_resid_skew_252d_d3(close: pd.Series) -> pd.Series:
    """Skew of EWMA-standardized residuals over 252d."""
    r = _log_ret(close)
    v = _ewma_vol(r, 0.94)
    z = _safe_div(r, v)
    return (_rolling_skew(z, YDAYS)).diff().diff().diff()

def f52_hgrd_067_ewma_std_resid_kurt_252d_d3(close: pd.Series) -> pd.Series:
    """Excess kurt of EWMA-standardized residuals over 252d."""
    r = _log_ret(close)
    v = _ewma_vol(r, 0.94)
    z = _safe_div(r, v)
    return (_rolling_kurt(z, YDAYS)).diff().diff().diff()

def f52_hgrd_068_ewma_std_resid_arch_lm_lag5_252d_d3(close: pd.Series) -> pd.Series:
    """ARCH-LM(5) on EWMA-standardized residuals over 252d."""
    r = _log_ret(close)
    v = _ewma_vol(r, 0.94)
    z = _safe_div(r, v)
    return (_arch_lm_stat(z, YDAYS, 5)).diff().diff().diff()

def f52_hgrd_069_heteroskedasticity_adjusted_acf_lag1_252d_d3(close: pd.Series) -> pd.Series:
    """ACF(1) of EWMA-standardized residuals over 252d - true return autocorrelation net of vol clustering."""
    r = _log_ret(close)
    v = _ewma_vol(r, 0.94)
    z = _safe_div(r, v)
    def _ac(w):
        x = w[~np.isnan(w)]
        if x.size < 20:
            return np.nan
        a = x[:-1]; b = x[1:]
        if a.std() == 0 or b.std() == 0:
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    res = z.rolling(YDAYS, min_periods=QDAYS).apply(_ac, raw=True)
    return (res).diff().diff().diff()

def f52_hgrd_070_ratio_garch_resid_var_to_1_252d_d3(close: pd.Series) -> pd.Series:
    """Variance of GARCH-standardized residuals over 252d (~1 if model is correct)."""
    r = _log_ret(close)
    s2 = _rolling_garch11(r, YDAYS, 4)
    z = _safe_div(r, s2.pow(0.5))
    return (z.rolling(YDAYS, min_periods=QDAYS).var()).diff().diff().diff()

def f52_hgrd_071_parkinson_var_21d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Parkinson realized variance (high-low range) over 21d."""
    return (_parkinson_var(high, low, MDAYS)).diff().diff().diff()

def f52_hgrd_072_parkinson_var_63d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Parkinson variance over 63d."""
    return (_parkinson_var(high, low, QDAYS)).diff().diff().diff()

def f52_hgrd_073_garman_klass_var_21d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Garman-Klass realized variance over 21d."""
    return (_garman_klass_var(open, high, low, close, MDAYS)).diff().diff().diff()

def f52_hgrd_074_garman_klass_var_63d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Garman-Klass variance over 63d."""
    return (_garman_klass_var(open, high, low, close, QDAYS)).diff().diff().diff()

def f52_hgrd_075_yang_zhang_var_21d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Yang-Zhang variance (overnight + open-close + Rogers-Satchell) over 21d."""
    return (_yang_zhang_var(open, high, low, close, MDAYS)).diff().diff().diff()


# ============================================================
#                         REGISTRY 001_075 (d3)
# ============================================================

HETEROSKEDASTICITY_GARCH_DYNAMICS_D3_REGISTRY_001_075 = {
    "f52_hgrd_001_ewma_var_lambda094_log_ret_d3": {"inputs": ["close"], "func": f52_hgrd_001_ewma_var_lambda094_log_ret_d3},
    "f52_hgrd_002_ewma_var_lambda097_log_ret_d3": {"inputs": ["close"], "func": f52_hgrd_002_ewma_var_lambda097_log_ret_d3},
    "f52_hgrd_003_ewma_var_lambda090_log_ret_d3": {"inputs": ["close"], "func": f52_hgrd_003_ewma_var_lambda090_log_ret_d3},
    "f52_hgrd_004_ewma_vol_lambda094_log_ret_d3": {"inputs": ["close"], "func": f52_hgrd_004_ewma_vol_lambda094_log_ret_d3},
    "f52_hgrd_005_ewma_vol_lambda094_pct_change_21d_d3": {"inputs": ["close"], "func": f52_hgrd_005_ewma_vol_lambda094_pct_change_21d_d3},
    "f52_hgrd_006_ewma_filtered_standardized_log_ret_d3": {"inputs": ["close"], "func": f52_hgrd_006_ewma_filtered_standardized_log_ret_d3},
    "f52_hgrd_007_ewma_var_persistence_acf1_252d_d3": {"inputs": ["close"], "func": f52_hgrd_007_ewma_var_persistence_acf1_252d_d3},
    "f52_hgrd_008_ewma_var_to_realized_var_ratio_63d_d3": {"inputs": ["close"], "func": f52_hgrd_008_ewma_var_to_realized_var_ratio_63d_d3},
    "f52_hgrd_009_ewma_innovation_variance_252d_d3": {"inputs": ["close"], "func": f52_hgrd_009_ewma_innovation_variance_252d_d3},
    "f52_hgrd_010_ewma_short_minus_long_vol_diff_d3": {"inputs": ["close"], "func": f52_hgrd_010_ewma_short_minus_long_vol_diff_d3},
    "f52_hgrd_011_garch11_alpha_log_ret_252d_d3": {"inputs": ["close"], "func": f52_hgrd_011_garch11_alpha_log_ret_252d_d3},
    "f52_hgrd_012_garch11_beta_log_ret_252d_d3": {"inputs": ["close"], "func": f52_hgrd_012_garch11_beta_log_ret_252d_d3},
    "f52_hgrd_013_garch11_omega_log_ret_252d_d3": {"inputs": ["close"], "func": f52_hgrd_013_garch11_omega_log_ret_252d_d3},
    "f52_hgrd_014_garch11_persistence_alpha_plus_beta_252d_d3": {"inputs": ["close"], "func": f52_hgrd_014_garch11_persistence_alpha_plus_beta_252d_d3},
    "f52_hgrd_015_garch11_current_sigma2_252d_d3": {"inputs": ["close"], "func": f52_hgrd_015_garch11_current_sigma2_252d_d3},
    "f52_hgrd_016_garch11_loglikelihood_252d_d3": {"inputs": ["close"], "func": f52_hgrd_016_garch11_loglikelihood_252d_d3},
    "f52_hgrd_017_garch11_long_run_var_252d_d3": {"inputs": ["close"], "func": f52_hgrd_017_garch11_long_run_var_252d_d3},
    "f52_hgrd_018_garch11_aic_252d_d3": {"inputs": ["close"], "func": f52_hgrd_018_garch11_aic_252d_d3},
    "f52_hgrd_019_garch11_alpha_to_beta_ratio_252d_d3": {"inputs": ["close"], "func": f52_hgrd_019_garch11_alpha_to_beta_ratio_252d_d3},
    "f52_hgrd_020_garch11_persistence_504d_d3": {"inputs": ["close"], "func": f52_hgrd_020_garch11_persistence_504d_d3},
    "f52_hgrd_021_gjr_garch_leverage_gamma_252d_d3": {"inputs": ["close"], "func": f52_hgrd_021_gjr_garch_leverage_gamma_252d_d3},
    "f52_hgrd_022_gjr_garch_alpha_252d_d3": {"inputs": ["close"], "func": f52_hgrd_022_gjr_garch_alpha_252d_d3},
    "f52_hgrd_023_gjr_garch_beta_252d_d3": {"inputs": ["close"], "func": f52_hgrd_023_gjr_garch_beta_252d_d3},
    "f52_hgrd_024_gjr_garch_persistence_252d_d3": {"inputs": ["close"], "func": f52_hgrd_024_gjr_garch_persistence_252d_d3},
    "f52_hgrd_025_gjr_garch_current_sigma2_252d_d3": {"inputs": ["close"], "func": f52_hgrd_025_gjr_garch_current_sigma2_252d_d3},
    "f52_hgrd_026_gjr_garch_loglikelihood_252d_d3": {"inputs": ["close"], "func": f52_hgrd_026_gjr_garch_loglikelihood_252d_d3},
    "f52_hgrd_027_gjr_garch_leverage_gamma_to_alpha_ratio_252d_d3": {"inputs": ["close"], "func": f52_hgrd_027_gjr_garch_leverage_gamma_to_alpha_ratio_252d_d3},
    "f52_hgrd_028_gjr_garch_minus_garch11_persistence_252d_d3": {"inputs": ["close"], "func": f52_hgrd_028_gjr_garch_minus_garch11_persistence_252d_d3},
    "f52_hgrd_029_egarch_leverage_proxy_corr_neg_r_log_vol_252d_d3": {"inputs": ["close"], "func": f52_hgrd_029_egarch_leverage_proxy_corr_neg_r_log_vol_252d_d3},
    "f52_hgrd_030_egarch_persistence_log_vol_ar1_252d_d3": {"inputs": ["close"], "func": f52_hgrd_030_egarch_persistence_log_vol_ar1_252d_d3},
    "f52_hgrd_031_arch_lm_lag5_log_ret_252d_d3": {"inputs": ["close"], "func": f52_hgrd_031_arch_lm_lag5_log_ret_252d_d3},
    "f52_hgrd_032_arch_lm_lag10_log_ret_252d_d3": {"inputs": ["close"], "func": f52_hgrd_032_arch_lm_lag10_log_ret_252d_d3},
    "f52_hgrd_033_arch_lm_lag21_log_ret_252d_d3": {"inputs": ["close"], "func": f52_hgrd_033_arch_lm_lag21_log_ret_252d_d3},
    "f52_hgrd_034_arch_lm_lag5_log_ret_504d_d3": {"inputs": ["close"], "func": f52_hgrd_034_arch_lm_lag5_log_ret_504d_d3},
    "f52_hgrd_035_mcleod_li_lag10_log_ret_252d_d3": {"inputs": ["close"], "func": f52_hgrd_035_mcleod_li_lag10_log_ret_252d_d3},
    "f52_hgrd_036_mcleod_li_lag21_log_ret_252d_d3": {"inputs": ["close"], "func": f52_hgrd_036_mcleod_li_lag21_log_ret_252d_d3},
    "f52_hgrd_037_white_heteroskedasticity_test_proxy_252d_d3": {"inputs": ["close"], "func": f52_hgrd_037_white_heteroskedasticity_test_proxy_252d_d3},
    "f52_hgrd_038_breusch_pagan_test_proxy_252d_d3": {"inputs": ["close"], "func": f52_hgrd_038_breusch_pagan_test_proxy_252d_d3},
    "f52_hgrd_039_arch_effect_intensity_zscore_252d_d3": {"inputs": ["close"], "func": f52_hgrd_039_arch_effect_intensity_zscore_252d_d3},
    "f52_hgrd_040_standardized_resid_normality_jb_garch_252d_d3": {"inputs": ["close"], "func": f52_hgrd_040_standardized_resid_normality_jb_garch_252d_d3},
    "f52_hgrd_041_vol_of_ewma_vol_lambda094_252d_d3": {"inputs": ["close"], "func": f52_hgrd_041_vol_of_ewma_vol_lambda094_252d_d3},
    "f52_hgrd_042_vol_of_garch_vol_252d_d3": {"inputs": ["close"], "func": f52_hgrd_042_vol_of_garch_vol_252d_d3},
    "f52_hgrd_043_ratio_ewma_var_to_garch_var_252d_d3": {"inputs": ["close"], "func": f52_hgrd_043_ratio_ewma_var_to_garch_var_252d_d3},
    "f52_hgrd_044_garch_vol_acceleration_252d_d3": {"inputs": ["close"], "func": f52_hgrd_044_garch_vol_acceleration_252d_d3},
    "f52_hgrd_045_conditional_vol_skewness_252d_d3": {"inputs": ["close"], "func": f52_hgrd_045_conditional_vol_skewness_252d_d3},
    "f52_hgrd_046_conditional_vol_kurtosis_252d_d3": {"inputs": ["close"], "func": f52_hgrd_046_conditional_vol_kurtosis_252d_d3},
    "f52_hgrd_047_vol_clustering_intensity_via_arch_lm_252d_d3": {"inputs": ["close"], "func": f52_hgrd_047_vol_clustering_intensity_via_arch_lm_252d_d3},
    "f52_hgrd_048_vol_acceleration_z_score_252d_d3": {"inputs": ["close"], "func": f52_hgrd_048_vol_acceleration_z_score_252d_d3},
    "f52_hgrd_049_conditional_vol_autocorr_lag1_252d_d3": {"inputs": ["close"], "func": f52_hgrd_049_conditional_vol_autocorr_lag1_252d_d3},
    "f52_hgrd_050_conditional_vol_autocorr_lag21_252d_d3": {"inputs": ["close"], "func": f52_hgrd_050_conditional_vol_autocorr_lag21_252d_d3},
    "f52_hgrd_051_fhs_var_95_ewma094_log_ret_252d_d3": {"inputs": ["close"], "func": f52_hgrd_051_fhs_var_95_ewma094_log_ret_252d_d3},
    "f52_hgrd_052_fhs_var_99_ewma094_log_ret_252d_d3": {"inputs": ["close"], "func": f52_hgrd_052_fhs_var_99_ewma094_log_ret_252d_d3},
    "f52_hgrd_053_fhs_var_995_ewma094_log_ret_252d_d3": {"inputs": ["close"], "func": f52_hgrd_053_fhs_var_995_ewma094_log_ret_252d_d3},
    "f52_hgrd_054_fhs_es_95_ewma094_log_ret_252d_d3": {"inputs": ["close"], "func": f52_hgrd_054_fhs_es_95_ewma094_log_ret_252d_d3},
    "f52_hgrd_055_fhs_es_99_ewma094_log_ret_252d_d3": {"inputs": ["close"], "func": f52_hgrd_055_fhs_es_99_ewma094_log_ret_252d_d3},
    "f52_hgrd_056_fhs_var_minus_hist_var_95_252d_d3": {"inputs": ["close"], "func": f52_hgrd_056_fhs_var_minus_hist_var_95_252d_d3},
    "f52_hgrd_057_fhs_innovation_skew_252d_d3": {"inputs": ["close"], "func": f52_hgrd_057_fhs_innovation_skew_252d_d3},
    "f52_hgrd_058_fhs_innovation_kurt_252d_d3": {"inputs": ["close"], "func": f52_hgrd_058_fhs_innovation_kurt_252d_d3},
    "f52_hgrd_059_fhs_innovation_var_252d_d3": {"inputs": ["close"], "func": f52_hgrd_059_fhs_innovation_var_252d_d3},
    "f52_hgrd_060_fhs_es_to_var_ratio_95_252d_d3": {"inputs": ["close"], "func": f52_hgrd_060_fhs_es_to_var_ratio_95_252d_d3},
    "f52_hgrd_061_std_resid_skew_garch11_252d_d3": {"inputs": ["close"], "func": f52_hgrd_061_std_resid_skew_garch11_252d_d3},
    "f52_hgrd_062_std_resid_kurt_garch11_252d_d3": {"inputs": ["close"], "func": f52_hgrd_062_std_resid_kurt_garch11_252d_d3},
    "f52_hgrd_063_std_resid_ks_normality_garch11_252d_d3": {"inputs": ["close"], "func": f52_hgrd_063_std_resid_ks_normality_garch11_252d_d3},
    "f52_hgrd_064_std_resid_ljung_box_lag10_garch11_252d_d3": {"inputs": ["close"], "func": f52_hgrd_064_std_resid_ljung_box_lag10_garch11_252d_d3},
    "f52_hgrd_065_std_resid_squared_arch_lm_garch11_252d_d3": {"inputs": ["close"], "func": f52_hgrd_065_std_resid_squared_arch_lm_garch11_252d_d3},
    "f52_hgrd_066_ewma_std_resid_skew_252d_d3": {"inputs": ["close"], "func": f52_hgrd_066_ewma_std_resid_skew_252d_d3},
    "f52_hgrd_067_ewma_std_resid_kurt_252d_d3": {"inputs": ["close"], "func": f52_hgrd_067_ewma_std_resid_kurt_252d_d3},
    "f52_hgrd_068_ewma_std_resid_arch_lm_lag5_252d_d3": {"inputs": ["close"], "func": f52_hgrd_068_ewma_std_resid_arch_lm_lag5_252d_d3},
    "f52_hgrd_069_heteroskedasticity_adjusted_acf_lag1_252d_d3": {"inputs": ["close"], "func": f52_hgrd_069_heteroskedasticity_adjusted_acf_lag1_252d_d3},
    "f52_hgrd_070_ratio_garch_resid_var_to_1_252d_d3": {"inputs": ["close"], "func": f52_hgrd_070_ratio_garch_resid_var_to_1_252d_d3},
    "f52_hgrd_071_parkinson_var_21d_d3": {"inputs": ["high", "low"], "func": f52_hgrd_071_parkinson_var_21d_d3},
    "f52_hgrd_072_parkinson_var_63d_d3": {"inputs": ["high", "low"], "func": f52_hgrd_072_parkinson_var_63d_d3},
    "f52_hgrd_073_garman_klass_var_21d_d3": {"inputs": ["open", "high", "low", "close"], "func": f52_hgrd_073_garman_klass_var_21d_d3},
    "f52_hgrd_074_garman_klass_var_63d_d3": {"inputs": ["open", "high", "low", "close"], "func": f52_hgrd_074_garman_klass_var_63d_d3},
    "f52_hgrd_075_yang_zhang_var_21d_d3": {"inputs": ["open", "high", "low", "close"], "func": f52_hgrd_075_yang_zhang_var_21d_d3},
}
