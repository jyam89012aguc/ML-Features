"""tail_risk_var_es d3 features 151-225 — Pipeline 1b-technical.

75 distinct gap-filling hypotheses extending the 150 in 001-150. Themes:
Kupiec POF / Christoffersen IND / Engle-Manganelli / breach clustering /
Basel zones / RiskMetrics EWMA / GARCH(1,1) implied / FHS / Parkinson-VaR /
GEV / Pareto MLE / Hill stability / Cushion-Lake-DDaR / quantile-regression VaR /
saddlepoint / multi-model consensus & disagreement.

Inputs: SEP OHLCV only. PIT-clean. Self-contained helpers.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504


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


def _ewma_variance(ret, lam=0.94):
    """RiskMetrics EWMA variance: sigma2 follows lam*sigma2-prev + (1-lam)*r-prev**2."""
    arr = ret.values.astype(float)
    n = arr.size
    sig2 = np.full(n, np.nan)
    init = np.nanvar(arr[:21])
    if not np.isfinite(init) or init <= 0:
        init = 1e-8
    sig2[0] = init
    for i in range(1, n):
        prev_r = arr[i - 1]
        prev_s = sig2[i - 1]
        if np.isnan(prev_r):
            prev_r = 0.0
        if np.isnan(prev_s) or prev_s <= 0:
            prev_s = init
        sig2[i] = lam * prev_s + (1.0 - lam) * (prev_r ** 2)
    return pd.Series(sig2, index=ret.index)


def _garch11_proxy_variance(ret, alpha=0.05, beta=0.93):
    """Approximation of GARCH(1,1) with fixed parameters and zero unconditional mean."""
    omega = max(1e-9, (1.0 - alpha - beta) * float(np.nanvar(ret.dropna()[:252])) if ret.dropna().size > 50 else 1e-7)
    arr = ret.values.astype(float)
    n = arr.size
    sig2 = np.full(n, np.nan)
    init = max(omega / max(1e-9, 1.0 - alpha - beta), 1e-8)
    sig2[0] = init
    for i in range(1, n):
        prev_r = arr[i - 1]
        prev_s = sig2[i - 1]
        if np.isnan(prev_r):
            prev_r = 0.0
        if np.isnan(prev_s) or prev_s <= 0:
            prev_s = init
        sig2[i] = omega + alpha * (prev_r ** 2) + beta * prev_s
    return pd.Series(sig2, index=ret.index)


def _gev_fit_params(maxima):
    """Method-of-moments GEV fit: returns (location, scale, shape).
    For block maxima with positive shape (heavy tail). Simplified."""
    valid = ~np.isnan(maxima)
    if valid.sum() < 5:
        return (np.nan, np.nan, np.nan)
    v = (maxima[valid] if not valid.all() else maxima).astype(float)
    m = float(v.mean()); s = float(v.std(ddof=1))
    if s <= 0:
        return (np.nan, np.nan, np.nan)
    sk = float(np.mean(((v - m) / s) ** 3))
    if sk < -1.139:
        xi = -0.05
    elif sk > 5.0:
        xi = 0.5
    else:
        xi = sk * 0.1
    scale = s
    loc = m - 0.5772 * scale
    return (loc, scale, xi)


def _pareto_mle_alpha(tail_values):
    """Hill MLE estimator for upper tail alpha of Pareto."""
    valid = ~np.isnan(tail_values)
    if valid.sum() < 5:
        return np.nan
    v = (tail_values[valid] if not valid.all() else tail_values).astype(float)
    v = v[v > 0]
    if v.size < 5:
        return np.nan
    v_min = float(v.min())
    if v_min <= 0:
        return np.nan
    return float(v.size / np.sum(np.log(v / v_min)))


def _quantile_regression_slope(y, x, q=0.05, n_iter=20):
    """Pinball-loss quantile-regression slope (no intercept assumed centred)."""
    mask = ~np.isnan(y) & ~np.isnan(x)
    if mask.sum() < 20:
        return np.nan
    y = y[mask]; x = x[mask]
    # Initialize with OLS slope
    if x.std() == 0:
        return np.nan
    b = float(np.cov(y, x)[0, 1] / np.var(x))
    a = float(np.median(y) - b * np.median(x))
    lr = 0.05
    for _ in range(n_iter):
        resid = y - (a + b * x)
        wgt = np.where(resid > 0, q, q - 1.0)
        ga = -float(wgt.mean())
        gb = -float((wgt * x).mean())
        a -= lr * ga; b -= lr * gb
    return b


def f43_trve_151_kupiec_pof_stat_var95_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    var95 = -r.rolling(252, min_periods=84).quantile(0.05).shift(1)
    breach = (r < -var95).astype(float).where(var95.notna(), np.nan)
    N = breach.rolling(252, min_periods=84).sum()
    T = 252.0
    p = 0.05
    lr_pof = -2.0 * (N * np.log(p) + (T - N) * np.log(1.0 - p) - N * np.log((N / T).replace(0, np.nan)) - (T - N) * np.log((1.0 - N / T).replace(0, np.nan)))
    out = lr_pof
    return out.diff().diff().diff()


def f43_trve_152_kupiec_pof_stat_var99_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    var99 = -r.rolling(252, min_periods=84).quantile(0.01).shift(1)
    breach = (r < -var99).astype(float).where(var99.notna(), np.nan)
    N = breach.rolling(252, min_periods=84).sum()
    T = 252.0
    p = 0.01
    lr_pof = -2.0 * (N * np.log(p) + (T - N) * np.log(1.0 - p) - N * np.log((N / T).replace(0, np.nan)) - (T - N) * np.log((1.0 - N / T).replace(0, np.nan)))
    out = lr_pof
    return out.diff().diff().diff()


def f43_trve_153_christoffersen_ind_stat_var95_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    var95 = -r.rolling(252, min_periods=84).quantile(0.05).shift(1)
    br = (r < -var95).astype(float).where(var95.notna(), np.nan)
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        n00 = 0; n01 = 0; n10 = 0; n11 = 0
        for i in range(1, v.size):
            a = int(v[i-1] > 0.5); b = int(v[i] > 0.5)
            if a == 0 and b == 0: n00 += 1
            elif a == 0 and b == 1: n01 += 1
            elif a == 1 and b == 0: n10 += 1
            else: n11 += 1
        n0 = n00 + n01; n1 = n10 + n11
        if n0 == 0 or n1 == 0 or n0 + n1 == 0:
            return np.nan
        pi01 = n01 / max(n0, 1); pi11 = n11 / max(n1, 1)
        pi = (n01 + n11) / (n0 + n1)
        if pi <= 0 or pi >= 1:
            return 0.0
        if pi01 <= 0 or pi01 >= 1 or pi11 <= 0 or pi11 >= 1:
            return np.nan
        ll_alt = n00 * np.log(1 - pi01) + n01 * np.log(pi01) + n10 * np.log(1 - pi11) + n11 * np.log(pi11)
        ll_null = (n00 + n10) * np.log(1 - pi) + (n01 + n11) * np.log(pi)
        return float(-2.0 * (ll_null - ll_alt))
    out = br.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff().diff()


def f43_trve_154_christoffersen_cc_stat_var95_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    var95 = -r.rolling(252, min_periods=84).quantile(0.05).shift(1)
    br = (r < -var95).astype(float).where(var95.notna(), np.nan)
    N = br.rolling(252, min_periods=84).sum(); T = 252.0; p = 0.05
    lr_pof = -2.0 * (N * np.log(p) + (T - N) * np.log(1.0 - p) - N * np.log((N / T).replace(0, np.nan)) - (T - N) * np.log((1.0 - N / T).replace(0, np.nan)))
    def _ind(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        n00 = n01 = n10 = n11 = 0
        for i in range(1, v.size):
            a = int(v[i-1] > 0.5); b = int(v[i] > 0.5)
            if a == 0 and b == 0: n00 += 1
            elif a == 0 and b == 1: n01 += 1
            elif a == 1 and b == 0: n10 += 1
            else: n11 += 1
        n0 = n00 + n01; n1 = n10 + n11
        if n0 == 0 or n1 == 0:
            return np.nan
        pi01 = n01 / max(n0, 1); pi11 = n11 / max(n1, 1)
        pi = (n01 + n11) / (n0 + n1)
        if pi <= 0 or pi >= 1 or pi01 <= 0 or pi01 >= 1 or pi11 <= 0 or pi11 >= 1:
            return 0.0
        ll_alt = n00 * np.log(1 - pi01) + n01 * np.log(pi01) + n10 * np.log(1 - pi11) + n11 * np.log(pi11)
        ll_null = (n00 + n10) * np.log(1 - pi) + (n01 + n11) * np.log(pi)
        return float(-2.0 * (ll_null - ll_alt))
    ind_stat = br.rolling(252, min_periods=84).apply(_ind, raw=True)
    out = lr_pof + ind_stat
    return out.diff().diff().diff()


def f43_trve_155_engle_manganelli_dq_proxy_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    var95 = -r.rolling(252, min_periods=84).quantile(0.05).shift(1)
    br = ((r < -var95).astype(float) - 0.05).where(var95.notna(), np.nan)
    # DQ proxy: sum of squared lagged breaches autocorrelation
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        acs = [np.corrcoef(v[k:], v[:-k])[0, 1] if v.size > k + 5 else 0.0 for k in range(1, 6)]
        return float(np.sum(np.array(acs) ** 2))
    out = br.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff().diff()


def f43_trve_156_breach_autocorr_lag1_var95_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    var95 = -r.rolling(252, min_periods=84).quantile(0.05).shift(1)
    br = (r < -var95).astype(float).where(var95.notna(), np.nan)
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        if v.size < 3:
            return np.nan
        m = v.mean(); vc = v - m
        den = float((vc ** 2).sum())
        if den == 0:
            return np.nan
        return float((vc[1:] * vc[:-1]).sum() / den)
    out = br.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff().diff()


def f43_trve_157_breach_ljung_box_q_lag5_var95_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    var95 = -r.rolling(252, min_periods=84).quantile(0.05).shift(1)
    br = (r < -var95).astype(float).where(var95.notna(), np.nan)
    def _lb(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        n = v.size
        m = v.mean(); vc = v - m
        den = float((vc ** 2).sum())
        if den == 0:
            return np.nan
        q = 0.0
        for k in range(1, 6):
            ac = float((vc[k:] * vc[:-k]).sum() / den)
            q += n * (n + 2) * (ac ** 2) / (n - k)
        return q
    out = br.rolling(252, min_periods=84).apply(_lb, raw=True)
    return out.diff().diff().diff()


def f43_trve_158_mean_inter_breach_gap_var95_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    var95 = -r.rolling(252, min_periods=84).quantile(0.05).shift(1)
    br = (r < -var95).astype(float).where(var95.notna(), np.nan)
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        idx = np.where(v > 0.5)[0]
        if idx.size < 2:
            return np.nan
        return float(np.mean(np.diff(idx)))
    out = br.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff().diff()


def f43_trve_159_max_inter_breach_gap_var95_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    var95 = -r.rolling(252, min_periods=84).quantile(0.05).shift(1)
    br = (r < -var95).astype(float).where(var95.notna(), np.nan)
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        idx = np.where(v > 0.5)[0]
        if idx.size < 2:
            return np.nan
        return float(np.max(np.diff(idx)))
    out = br.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff().diff()


def f43_trve_160_today_breach_var95_indicator_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    var95 = -r.rolling(252, min_periods=84).quantile(0.05).shift(1)
    out = (r < -var95).astype(float).where(var95.notna(), np.nan)
    return out.diff().diff().diff()


def f43_trve_161_breach_density_surge_5d_var95_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    var95 = -r.rolling(252, min_periods=84).quantile(0.05).shift(1)
    br = (r < -var95).astype(float).where(var95.notna(), np.nan)
    out = (br.rolling(5, min_periods=2).sum() > 2.0).astype(float).where(br.notna(), np.nan)
    return out.diff().diff().diff()


def f43_trve_162_bars_since_last_breach_var95_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    var95 = -r.rolling(252, min_periods=84).quantile(0.05).shift(1)
    br = (r < -var95)
    arr = br.fillna(False).astype(bool).values
    n = arr.size
    out_arr = np.full(n, np.nan)
    last = -1
    for i in range(n):
        if arr[i]: last = i
        if last >= 0: out_arr[i] = float(i - last)
    out = pd.Series(out_arr, index=close.index)
    return out.diff().diff().diff()


def f43_trve_163_realized_vs_expected_breach_ratio_var95_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    var95 = -r.rolling(252, min_periods=84).quantile(0.05).shift(1)
    br = (r < -var95).astype(float).where(var95.notna(), np.nan)
    N = br.rolling(252, min_periods=84).sum()
    out = N / (252.0 * 0.05)
    return out.diff().diff().diff()


def f43_trve_164_basel_traffic_light_zone_var99_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    var99 = -r.rolling(252, min_periods=84).quantile(0.01).shift(1)
    br = (r < -var99).astype(float).where(var99.notna(), np.nan)
    N = br.rolling(252, min_periods=84).sum()
    # Basel zones: 0-4 = green, 5-9 = yellow, 10+ = red. Encode 0/1/2.
    zone = pd.Series(np.where(N < 5, 0.0, np.where(N < 10, 1.0, 2.0)), index=N.index).where(N.notna(), np.nan)
    out = zone
    return out.diff().diff().diff()


def f43_trve_165_cond_breach_prob_given_prior_breach_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    var95 = -r.rolling(252, min_periods=84).quantile(0.05).shift(1)
    br = (r < -var95).astype(float).where(var95.notna(), np.nan)
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        if v.size < 3:
            return np.nan
        n_prior = int(v[:-1].sum())
        if n_prior == 0:
            return 0.0
        n_both = int(np.sum((v[:-1] > 0.5) & (v[1:] > 0.5)))
        return float(n_both / n_prior)
    out = br.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff().diff()


def f43_trve_166_ewma_variance_lam094_log_ret_full_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = _ewma_variance(r, lam=0.94)
    return out.diff().diff().diff()


def f43_trve_167_ewma_var95_lam094_log_ret_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sig = _ewma_variance(r, lam=0.94).pow(0.5)
    out = 1.645 * sig
    return out.diff().diff().diff()


def f43_trve_168_ewma_var99_lam094_log_ret_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sig = _ewma_variance(r, lam=0.94).pow(0.5)
    out = 2.326 * sig
    return out.diff().diff().diff()


def f43_trve_169_ewma_es95_lam094_log_ret_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sig = _ewma_variance(r, lam=0.94).pow(0.5)
    # ES95 for normal = sigma * phi(z95)/(1-0.95) = sigma * 2.063
    out = 2.063 * sig
    return out.diff().diff().diff()


def f43_trve_170_garch11_proxy_variance_full_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = _garch11_proxy_variance(r)
    return out.diff().diff().diff()


def f43_trve_171_garch11_implied_var99_log_ret_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sig = _garch11_proxy_variance(r).pow(0.5)
    out = 2.326 * sig
    return out.diff().diff().diff()


def f43_trve_172_fhs_var95_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sig = r.rolling(21, min_periods=7).std()
    long_sig = r.rolling(252, min_periods=84).std()
    scaled = r * (sig / long_sig.replace(0, np.nan))
    out = -scaled.rolling(252, min_periods=84).quantile(0.05)
    return out.diff().diff().diff()


def f43_trve_173_fhs_var99_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sig = r.rolling(21, min_periods=7).std()
    long_sig = r.rolling(252, min_periods=84).std()
    scaled = r * (sig / long_sig.replace(0, np.nan))
    out = -scaled.rolling(252, min_periods=84).quantile(0.01)
    return out.diff().diff().diff()


def f43_trve_174_parkinson_var95_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    park = (1.0 / (4.0 * np.log(2.0))) * (_safe_log(high) - _safe_log(low)) ** 2
    sig_park = park.rolling(252, min_periods=84).mean().pow(0.5)
    out = 1.645 * sig_park
    return out.diff().diff().diff()


def f43_trve_175_garman_klass_var95_252d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    lh = _safe_log(high); ll = _safe_log(low); lc = _safe_log(close); lo = _safe_log(open)
    gk = 0.5 * (lh - ll) ** 2 - (2.0 * np.log(2.0) - 1.0) * (lc - lo) ** 2
    sig_gk = gk.clip(lower=0).rolling(252, min_periods=84).mean().pow(0.5)
    out = 1.645 * sig_gk
    return out.diff().diff().diff()


def f43_trve_176_ewma_minus_hist_var95_diff_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sig = _ewma_variance(r, lam=0.94).pow(0.5)
    ewma95 = 1.645 * sig
    hist95 = -r.rolling(252, min_periods=84).quantile(0.05)
    out = ewma95 - hist95
    return out.diff().diff().diff()


def f43_trve_177_vol_of_rolling_var95_21d_in_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    v95 = -r.rolling(21, min_periods=7).quantile(0.05)
    out = v95.rolling(252, min_periods=84).std()
    return out.diff().diff().diff()


def f43_trve_178_vol_of_rolling_es95_21d_in_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _es(w):
        valid = ~np.isnan(w)
        if valid.sum() < 5:
            return np.nan
        v = w[valid] if not valid.all() else w
        th = np.percentile(v, 5)
        tail = v[v <= th]
        if tail.size == 0:
            return np.nan
        return float(-tail.mean())
    es21 = r.rolling(21, min_periods=7).apply(_es, raw=True)
    out = es21.rolling(252, min_periods=84).std()
    return out.diff().diff().diff()


def f43_trve_179_cond_var95_high_vol_regime_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    rv21 = r.rolling(21, min_periods=7).std()
    med_rv = rv21.rolling(252, min_periods=84).median()
    high_v = r.where(rv21 > med_rv, np.nan)
    out = -high_v.rolling(252, min_periods=84).quantile(0.05)
    return out.diff().diff().diff()


def f43_trve_180_cond_var95_low_vol_regime_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    rv21 = r.rolling(21, min_periods=7).std()
    med_rv = rv21.rolling(252, min_periods=84).median()
    low_v = r.where(rv21 < med_rv, np.nan)
    out = -low_v.rolling(252, min_periods=84).quantile(0.05)
    return out.diff().diff().diff()


def f43_trve_181_gev_block_maxima_21d_in_252d_location_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    loss = -r
    block_max = loss.rolling(21, min_periods=7).max()
    def _loc(w):
        return _gev_fit_params(w)[0]
    out = block_max.rolling(252, min_periods=84).apply(_loc, raw=True)
    return out.diff().diff().diff()


def f43_trve_182_gev_block_maxima_21d_in_252d_scale_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    loss = -r
    block_max = loss.rolling(21, min_periods=7).max()
    def _sc(w):
        return _gev_fit_params(w)[1]
    out = block_max.rolling(252, min_periods=84).apply(_sc, raw=True)
    return out.diff().diff().diff()


def f43_trve_183_gev_block_maxima_21d_in_252d_shape_xi_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    loss = -r
    block_max = loss.rolling(21, min_periods=7).max()
    def _xi(w):
        return _gev_fit_params(w)[2]
    out = block_max.rolling(252, min_periods=84).apply(_xi, raw=True)
    return out.diff().diff().diff()


def f43_trve_184_gev_implied_var99_block_maxima_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    loss = -r
    block_max = loss.rolling(21, min_periods=7).max()
    def _v99(w):
        loc, sc, xi = _gev_fit_params(w)
        if np.isnan(loc) or np.isnan(sc) or np.isnan(xi):
            return np.nan
        p = 0.01
        if abs(xi) < 1e-6:
            return float(loc - sc * np.log(-np.log(1.0 - p)))
        return float(loc - sc / xi * (1.0 - (-np.log(1.0 - p)) ** -xi))
    out = block_max.rolling(252, min_periods=84).apply(_v99, raw=True)
    return out.diff().diff().diff()


def f43_trve_185_pareto_mle_alpha_lower_5pct_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    loss = -r
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        th = np.percentile(v, 95)
        tail = v[v > th]
        return _pareto_mle_alpha(tail)
    out = loss.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff().diff()


def f43_trve_186_pareto_mle_alpha_upper_5pct_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        th = np.percentile(v, 95)
        tail = v[v > th]
        return _pareto_mle_alpha(tail)
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff().diff()


def f43_trve_187_hill_plot_stability_lower_5_10_15pct_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    loss = -r
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        estimates = []
        for pct in (5, 10, 15):
            th = np.percentile(v, 100 - pct)
            tail = v[v > th]
            if tail.size < 3:
                continue
            v_min = float(tail.min())
            if v_min <= 0:
                continue
            estimates.append(tail.size / np.sum(np.log(tail / v_min)))
        if len(estimates) < 2:
            return np.nan
        return float(np.std(estimates))
    out = loss.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff().diff()


def f43_trve_188_hall_bootstrap_tail_proxy_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    loss = -r
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 50:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        est = []
        for k in (5, 10, 15, 20):
            th = np.percentile(v, 100 - k)
            tail = v[v > th]
            if tail.size < 3:
                continue
            vm = float(tail.min())
            if vm <= 0:
                continue
            est.append(tail.size / np.sum(np.log(tail / vm)))
        if len(est) < 2:
            return np.nan
        return float(np.mean(est))
    out = loss.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff().diff()


def f43_trve_189_smith_tail_index_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    loss = -r
    def _smith(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        th = np.percentile(v, 90)
        tail = v[v > th] - th
        if tail.size < 3:
            return np.nan
        return float(np.mean(tail) / max(np.std(tail, ddof=1), 1e-12))
    out = loss.rolling(252, min_periods=84).apply(_smith, raw=True)
    return out.diff().diff().diff()


def f43_trve_190_evt_var99_gev_minus_cf_diff_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    loss = -r
    block_max = loss.rolling(21, min_periods=7).max()
    def _gev99(w):
        loc, sc, xi = _gev_fit_params(w)
        if np.isnan(loc) or np.isnan(sc) or np.isnan(xi):
            return np.nan
        p = 0.01
        if abs(xi) < 1e-6:
            return float(loc - sc * np.log(-np.log(1.0 - p)))
        return float(loc - sc / xi * (1.0 - (-np.log(1.0 - p)) ** -xi))
    gev99 = block_max.rolling(252, min_periods=84).apply(_gev99, raw=True)
    # Cornish-Fisher VaR 99% from moments
    def _cf99(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        m = v.mean(); s = v.std(ddof=1)
        if s <= 0:
            return np.nan
        z = -v.mean()
        sk = float(np.mean(((v - m) / s) ** 3))
        kt = float(np.mean(((v - m) / s) ** 4) - 3.0)
        z99 = 2.326
        z_adj = z99 + (z99 ** 2 - 1) * sk / 6.0 + (z99 ** 3 - 3 * z99) * kt / 24.0 - (2 * z99 ** 3 - 5 * z99) * sk ** 2 / 36.0
        return float(z_adj * s - m)
    cf99 = r.rolling(252, min_periods=84).apply(_cf99, raw=True)
    out = gev99 - cf99
    return out.diff().diff().diff()


def f43_trve_191_pot_var99_gpd_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    loss = -r
    def _gpd(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        n = v.size
        th = np.percentile(v, 90)
        exc = v[v > th] - th
        Nu = exc.size
        if Nu < 5:
            return np.nan
        mean_exc = exc.mean(); std_exc = exc.std(ddof=1)
        if std_exc <= 0:
            return np.nan
        xi = 0.5 * ((mean_exc / std_exc) ** 2 - 1.0)
        beta = 0.5 * mean_exc * ((mean_exc / std_exc) ** 2 + 1.0)
        p = 0.01
        return float(th + (beta / xi) * (((n / Nu) * p) ** (-xi) - 1.0) if abs(xi) > 1e-6 else th + beta * np.log(p * n / Nu))
    out = loss.rolling(252, min_periods=84).apply(_gpd, raw=True)
    return out.diff().diff().diff()


def f43_trve_192_evt_vs_cf_var99_disagreement_indicator_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    loss = -r
    block_max = loss.rolling(21, min_periods=7).max()
    def _gev99(w):
        loc, sc, xi = _gev_fit_params(w)
        if np.isnan(loc) or np.isnan(sc) or np.isnan(xi):
            return np.nan
        p = 0.01
        if abs(xi) < 1e-6:
            return float(loc - sc * np.log(-np.log(1.0 - p)))
        return float(loc - sc / xi * (1.0 - (-np.log(1.0 - p)) ** -xi))
    gev99 = block_max.rolling(252, min_periods=84).apply(_gev99, raw=True)
    def _cf99(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        m = v.mean(); s = v.std(ddof=1)
        if s <= 0:
            return np.nan
        sk = float(np.mean(((v - m) / s) ** 3)); kt = float(np.mean(((v - m) / s) ** 4) - 3.0)
        z99 = 2.326
        z_adj = z99 + (z99 ** 2 - 1) * sk / 6.0 + (z99 ** 3 - 3 * z99) * kt / 24.0 - (2 * z99 ** 3 - 5 * z99) * sk ** 2 / 36.0
        return float(z_adj * s - m)
    cf99 = r.rolling(252, min_periods=84).apply(_cf99, raw=True)
    diff = (gev99 - cf99).abs()
    out = (diff > 0.02).astype(float).where(gev99.notna() & cf99.notna(), np.nan)
    return out.diff().diff().diff()


def f43_trve_193_gpd_mean_excess_slope_top_decile_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    loss = -r
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        thrs = np.percentile(v, [80, 85, 90, 95])
        me = []
        for th in thrs:
            exc = v[v > th] - th
            if exc.size < 3:
                continue
            me.append((th, exc.mean()))
        if len(me) < 2:
            return np.nan
        xs = np.array([m[0] for m in me]); ys = np.array([m[1] for m in me])
        xm = xs.mean(); ym = ys.mean()
        den = float(((xs - xm) ** 2).sum())
        if den == 0:
            return np.nan
        return float(((xs - xm) * (ys - ym)).sum() / den)
    out = loss.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff().diff()


def f43_trve_194_max_monthly_loss_21d_blocks_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    loss = -r
    max_block = loss.rolling(21, min_periods=7).sum()
    out = max_block.rolling(252, min_periods=84).max()
    return out.diff().diff().diff()


def f43_trve_195_gumbel_implied_expected_max_loss_504d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    loss = -r
    block_max = loss.rolling(21, min_periods=7).max()
    def _gum(w):
        valid = ~np.isnan(w)
        if valid.sum() < 8:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        m = v.mean(); s = v.std(ddof=1)
        if s <= 0:
            return np.nan
        beta = s * np.sqrt(6.0) / np.pi
        mu = m - 0.5772 * beta
        return float(mu + beta * np.log(np.log(2.0)))
    out = block_max.rolling(504, min_periods=168).apply(_gum, raw=True)
    return out.diff().diff().diff()


def f43_trve_196_cushion_ratio_excess_ret_over_max_dd_252d_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    ret252 = lc - lc.shift(252)
    def _maxdd(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        peak = np.maximum.accumulate(v)
        dd = peak - v
        return float(dd.max())
    mdd = lc.rolling(252, min_periods=84).apply(_maxdd, raw=True)
    out = _safe_div(ret252, mdd)
    return out.diff().diff().diff()


def f43_trve_197_lake_ratio_meanDD_times_dur_252d_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    def _lake(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        peak = np.maximum.accumulate(v)
        dd = peak - v
        underwater = (dd > 0).astype(int)
        dur = float(underwater.sum())
        mean_dd = float(dd.mean())
        ret = float(v[-1] - v[0])
        if ret <= 0:
            return np.nan
        return float(mean_dd * dur / ret)
    out = lc.rolling(252, min_periods=84).apply(_lake, raw=True)
    return out.diff().diff().diff()


def f43_trve_198_frac_bars_in_dd_above_10pct_252d_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        peak = np.maximum.accumulate(v)
        dd = peak - v
        return float(np.mean(dd > 0.1))
    out = lc.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff().diff()


def f43_trve_199_dd_at_risk_95pct_252d_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        peak = np.maximum.accumulate(v)
        dd = peak - v
        return float(np.percentile(dd, 95))
    out = lc.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff().diff()


def f43_trve_200_dd_at_risk_99pct_252d_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        peak = np.maximum.accumulate(v)
        dd = peak - v
        return float(np.percentile(dd, 99))
    out = lc.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff().diff()


def f43_trve_201_conditional_dd_at_risk_95pct_252d_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        peak = np.maximum.accumulate(v)
        dd = peak - v
        th = np.percentile(dd, 95)
        tail = dd[dd >= th]
        if tail.size == 0:
            return np.nan
        return float(tail.mean())
    out = lc.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff().diff()


def f43_trve_202_dd_volatility_std_rolling_252d_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        peak = np.maximum.accumulate(v)
        dd = peak - v
        return float(np.std(dd, ddof=1))
    out = lc.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff().diff()


def f43_trve_203_mean_dd_recovery_time_252d_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        peak = np.maximum.accumulate(v)
        dd = peak - v
        underwater = dd > 0
        durations = []
        cur = 0
        for u in underwater:
            if u:
                cur += 1
            else:
                if cur > 0:
                    durations.append(cur); cur = 0
        if cur > 0:
            durations.append(cur)
        if not durations:
            return 0.0
        return float(np.mean(durations))
    out = lc.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff().diff()


def f43_trve_204_max_dd_over_max_recovery_252d_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        peak = np.maximum.accumulate(v)
        dd = peak - v
        max_dd = float(dd.max())
        underwater = dd > 0
        durations = []
        cur = 0
        for u in underwater:
            if u: cur += 1
            else:
                if cur > 0: durations.append(cur); cur = 0
        if cur > 0: durations.append(cur)
        if not durations:
            return np.nan
        return float(max_dd / max(max(durations), 1))
    out = lc.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff().diff()


def f43_trve_205_max_dd_over_var95_ratio_252d_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    r = lc.diff()
    v95 = -r.rolling(252, min_periods=84).quantile(0.05)
    def _mdd(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        peak = np.maximum.accumulate(v)
        return float((peak - v).max())
    mdd = lc.rolling(252, min_periods=84).apply(_mdd, raw=True)
    out = _safe_div(mdd, v95)
    return out.diff().diff().diff()


def f43_trve_206_count_distinct_dd_above_5pct_252d_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        peak = np.maximum.accumulate(v)
        dd = peak - v
        count = 0
        in_dd = False; max_in_dd = 0.0
        for d in dd:
            if d > 0:
                if not in_dd:
                    in_dd = True
                max_in_dd = max(max_in_dd, d)
            else:
                if in_dd and max_in_dd > 0.05:
                    count += 1
                in_dd = False; max_in_dd = 0.0
        if in_dd and max_in_dd > 0.05:
            count += 1
        return float(count)
    out = lc.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff().diff()


def f43_trve_207_sum_all_dd_above_5pct_252d_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        peak = np.maximum.accumulate(v)
        dd = peak - v
        total = 0.0
        in_dd = False; max_in_dd = 0.0
        for d in dd:
            if d > 0:
                in_dd = True
                max_in_dd = max(max_in_dd, d)
            else:
                if in_dd and max_in_dd > 0.05:
                    total += max_in_dd
                in_dd = False; max_in_dd = 0.0
        if in_dd and max_in_dd > 0.05:
            total += max_in_dd
        return float(total)
    out = lc.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff().diff()


def f43_trve_208_longest_underwater_duration_252d_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        peak = np.maximum.accumulate(v)
        underwater = (peak - v) > 0
        best = 0; cur = 0
        for u in underwater:
            if u:
                cur += 1
                if cur > best: best = cur
            else:
                cur = 0
        return float(best)
    out = lc.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff().diff()


def f43_trve_209_fraction_time_underwater_252d_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        peak = np.maximum.accumulate(v)
        return float(np.mean((peak - v) > 0))
    out = lc.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff().diff()


def f43_trve_210_dd_acceleration_change_max_dd_63d_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    def _mdd(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        peak = np.maximum.accumulate(v)
        return float((peak - v).max())
    mdd = lc.rolling(252, min_periods=84).apply(_mdd, raw=True)
    out = mdd - mdd.shift(63)
    return out.diff().diff().diff()


def f43_trve_211_qreg_slope_return_on_lag_q05_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    rl = r.shift(1)
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        # w is a single column; we use paired array via index in main loop instead
        return np.nan
    # Loop-based implementation since rolling.apply can't pass two series
    arr_y = r.values; arr_x = rl.values
    n = len(close)
    out_arr = np.full(n, np.nan)
    for i in range(84, n):
        s = max(0, i - 251)
        out_arr[i] = _quantile_regression_slope(arr_y[s:i+1], arr_x[s:i+1], q=0.05)
    out = pd.Series(out_arr, index=close.index)
    return out.diff().diff().diff()


def f43_trve_212_qreg_slope_return_on_lag_q95_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    rl = r.shift(1)
    arr_y = r.values; arr_x = rl.values
    n = len(close)
    out_arr = np.full(n, np.nan)
    for i in range(84, n):
        s = max(0, i - 251)
        out_arr[i] = _quantile_regression_slope(arr_y[s:i+1], arr_x[s:i+1], q=0.95)
    out = pd.Series(out_arr, index=close.index)
    return out.diff().diff().diff()


def f43_trve_213_cond_var95_given_last21d_negative_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    ret21 = _safe_log(close).diff(21)
    cond_r = r.where(ret21 < 0, np.nan)
    out = -cond_r.rolling(252, min_periods=84).quantile(0.05)
    return out.diff().diff().diff()


def f43_trve_214_cond_es95_given_high_vol_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    rv21 = r.rolling(21, min_periods=7).std()
    med_rv = rv21.rolling(252, min_periods=84).median()
    high_v = r.where(rv21 > med_rv, np.nan)
    def _es(w):
        valid = ~np.isnan(w)
        if valid.sum() < 10:
            return np.nan
        v = w[valid] if not valid.all() else w
        th = np.percentile(v, 5)
        tail = v[v <= th]
        if tail.size == 0:
            return np.nan
        return float(-tail.mean())
    out = high_v.rolling(252, min_periods=84).apply(_es, raw=True)
    return out.diff().diff().diff()


def f43_trve_215_prob_loss_above_10pct_in_21d_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    cum21 = r.rolling(21, min_periods=7).sum()
    large_loss = (cum21 < -0.10).astype(float).where(cum21.notna(), np.nan)
    out = large_loss.rolling(252, min_periods=84).mean()
    return out.diff().diff().diff()


def f43_trve_216_prob_loss_above_20pct_in_63d_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    cum63 = r.rolling(63, min_periods=21).sum()
    large_loss = (cum63 < -0.20).astype(float).where(cum63.notna(), np.nan)
    out = large_loss.rolling(252, min_periods=84).mean()
    return out.diff().diff().diff()


def f43_trve_217_indicator_longest_dd_above_50pct_252d_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        peak = np.maximum.accumulate(v)
        dd = peak - v
        return float((dd > 0.5).any())
    out = lc.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff().diff()


def f43_trve_218_var95_slope_change_per_bar_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    v95 = -r.rolling(252, min_periods=84).quantile(0.05)
    out = v95 - v95.shift(21)
    return out.diff().diff().diff()


def f43_trve_219_var95_autocorr_lag21_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    v95 = -r.rolling(63, min_periods=21).quantile(0.05)
    out = v95.rolling(252, min_periods=84).corr(v95.shift(21))
    return out.diff().diff().diff()


def f43_trve_220_es95_autocorr_lag1_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _es(w):
        valid = ~np.isnan(w)
        if valid.sum() < 10:
            return np.nan
        v = w[valid] if not valid.all() else w
        th = np.percentile(v, 5)
        tail = v[v <= th]
        if tail.size == 0:
            return np.nan
        return float(-tail.mean())
    es = r.rolling(63, min_periods=21).apply(_es, raw=True)
    out = es.rolling(252, min_periods=84).corr(es.shift(1))
    return out.diff().diff().diff()


def f43_trve_221_saddlepoint_var95_proxy_cf_higher_order_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        m = v.mean(); s = v.std(ddof=1)
        if s <= 0:
            return np.nan
        z = (v - m) / s
        sk = float(np.mean(z ** 3)); kt = float(np.mean(z ** 4) - 3.0)
        z95 = 1.645
        z_cf = z95 + (z95 ** 2 - 1) * sk / 6.0 + (z95 ** 3 - 3 * z95) * kt / 24.0 - (2 * z95 ** 3 - 5 * z95) * sk ** 2 / 36.0
        # Add 5th-moment saddlepoint correction (approx)
        hyper = float(np.mean(z ** 5))
        z_sp = z_cf + (z95 ** 4 - 6 * z95 ** 2 + 3) * hyper / 120.0
        return float(z_sp * s - m)
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff().diff()


def f43_trve_222_multi_model_var95_mean_consensus_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    hist = -r.rolling(252, min_periods=84).quantile(0.05)
    sig_hist = r.rolling(252, min_periods=84).std()
    param = 1.645 * sig_hist - r.rolling(252, min_periods=84).mean()
    def _cf(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        m = v.mean(); s = v.std(ddof=1)
        if s <= 0:
            return np.nan
        z = (v - m) / s
        sk = float(np.mean(z ** 3)); kt = float(np.mean(z ** 4) - 3.0)
        z95 = 1.645
        z_adj = z95 + (z95 ** 2 - 1) * sk / 6.0 + (z95 ** 3 - 3 * z95) * kt / 24.0 - (2 * z95 ** 3 - 5 * z95) * sk ** 2 / 36.0
        return float(z_adj * s - m)
    cf = r.rolling(252, min_periods=84).apply(_cf, raw=True)
    ewma_sig = _ewma_variance(r, lam=0.94).pow(0.5)
    ewma = 1.645 * ewma_sig
    out = (hist + param + cf + ewma) / 4.0
    return out.diff().diff().diff()


def f43_trve_223_multi_model_var95_disagreement_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    hist = -r.rolling(252, min_periods=84).quantile(0.05)
    sig_hist = r.rolling(252, min_periods=84).std()
    param = 1.645 * sig_hist - r.rolling(252, min_periods=84).mean()
    def _cf(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        m = v.mean(); s = v.std(ddof=1)
        if s <= 0:
            return np.nan
        z = (v - m) / s
        sk = float(np.mean(z ** 3)); kt = float(np.mean(z ** 4) - 3.0)
        z95 = 1.645
        z_adj = z95 + (z95 ** 2 - 1) * sk / 6.0 + (z95 ** 3 - 3 * z95) * kt / 24.0 - (2 * z95 ** 3 - 5 * z95) * sk ** 2 / 36.0
        return float(z_adj * s - m)
    cf = r.rolling(252, min_periods=84).apply(_cf, raw=True)
    ewma_sig = _ewma_variance(r, lam=0.94).pow(0.5)
    ewma = 1.645 * ewma_sig
    stk = pd.concat([hist.rename(0), param.rename(1), cf.rename(2), ewma.rename(3)], axis=1)
    out = stk.max(axis=1) - stk.min(axis=1)
    return out.diff().diff().diff()


def f43_trve_224_sum_worst_5_day_blocks_252d_log_ret_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    cum5 = r.rolling(5, min_periods=2).sum()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        sorted_v = np.sort(v)[:5]
        return float(sorted_v.sum())
    out = cum5.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff().diff()


def f43_trve_225_comp_ultimate_crash_prone_composite_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    lc = _safe_log(close)
    # Hill alpha low (heavy tail) + NCSKEW low + breach rate high + max DD > 20%
    def _hill(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        th = np.percentile(v, 95)
        tail = v[v > th]
        if tail.size < 3:
            return np.nan
        vm = float(tail.min())
        if vm <= 0:
            return np.nan
        return float(tail.size / np.sum(np.log(tail / vm)))
    hill_low = (r.abs().rolling(252, min_periods=84).apply(_hill, raw=True) < 3.0).astype(float)
    def _ncs(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        m = v.mean(); s = v.std(ddof=1)
        if s <= 0:
            return np.nan
        return float(-np.mean(((v - m) / s) ** 3))
    ncs_high = (r.rolling(252, min_periods=84).apply(_ncs, raw=True) > 0.5).astype(float)
    v95 = -r.rolling(252, min_periods=84).quantile(0.05).shift(1)
    br = (r < -v95).astype(float).where(v95.notna(), np.nan)
    br_rate_high = (br.rolling(252, min_periods=84).sum() > 0.07 * 252).astype(float)
    def _mdd(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        peak = np.maximum.accumulate(v)
        return float((peak - v).max())
    mdd_big = (lc.rolling(252, min_periods=84).apply(_mdd, raw=True) > 0.20).astype(float)
    out = (hill_low + ncs_high + br_rate_high + mdd_big).where(v95.notna(), np.nan)
    return out.diff().diff().diff()


# ============================================================
#                         REGISTRY 151_225 (d3)
# ============================================================

TAIL_RISK_VAR_ES_D3_REGISTRY_151_225 = {
    "f43_trve_151_kupiec_pof_stat_var95_log_ret_252d_d3": {"inputs": ["close"], "func": f43_trve_151_kupiec_pof_stat_var95_log_ret_252d_d3},
    "f43_trve_152_kupiec_pof_stat_var99_log_ret_252d_d3": {"inputs": ["close"], "func": f43_trve_152_kupiec_pof_stat_var99_log_ret_252d_d3},
    "f43_trve_153_christoffersen_ind_stat_var95_252d_d3": {"inputs": ["close"], "func": f43_trve_153_christoffersen_ind_stat_var95_252d_d3},
    "f43_trve_154_christoffersen_cc_stat_var95_252d_d3": {"inputs": ["close"], "func": f43_trve_154_christoffersen_cc_stat_var95_252d_d3},
    "f43_trve_155_engle_manganelli_dq_proxy_252d_d3": {"inputs": ["close"], "func": f43_trve_155_engle_manganelli_dq_proxy_252d_d3},
    "f43_trve_156_breach_autocorr_lag1_var95_252d_d3": {"inputs": ["close"], "func": f43_trve_156_breach_autocorr_lag1_var95_252d_d3},
    "f43_trve_157_breach_ljung_box_q_lag5_var95_252d_d3": {"inputs": ["close"], "func": f43_trve_157_breach_ljung_box_q_lag5_var95_252d_d3},
    "f43_trve_158_mean_inter_breach_gap_var95_252d_d3": {"inputs": ["close"], "func": f43_trve_158_mean_inter_breach_gap_var95_252d_d3},
    "f43_trve_159_max_inter_breach_gap_var95_252d_d3": {"inputs": ["close"], "func": f43_trve_159_max_inter_breach_gap_var95_252d_d3},
    "f43_trve_160_today_breach_var95_indicator_d3": {"inputs": ["close"], "func": f43_trve_160_today_breach_var95_indicator_d3},
    "f43_trve_161_breach_density_surge_5d_var95_252d_d3": {"inputs": ["close"], "func": f43_trve_161_breach_density_surge_5d_var95_252d_d3},
    "f43_trve_162_bars_since_last_breach_var95_252d_d3": {"inputs": ["close"], "func": f43_trve_162_bars_since_last_breach_var95_252d_d3},
    "f43_trve_163_realized_vs_expected_breach_ratio_var95_252d_d3": {"inputs": ["close"], "func": f43_trve_163_realized_vs_expected_breach_ratio_var95_252d_d3},
    "f43_trve_164_basel_traffic_light_zone_var99_252d_d3": {"inputs": ["close"], "func": f43_trve_164_basel_traffic_light_zone_var99_252d_d3},
    "f43_trve_165_cond_breach_prob_given_prior_breach_252d_d3": {"inputs": ["close"], "func": f43_trve_165_cond_breach_prob_given_prior_breach_252d_d3},
    "f43_trve_166_ewma_variance_lam094_log_ret_full_d3": {"inputs": ["close"], "func": f43_trve_166_ewma_variance_lam094_log_ret_full_d3},
    "f43_trve_167_ewma_var95_lam094_log_ret_d3": {"inputs": ["close"], "func": f43_trve_167_ewma_var95_lam094_log_ret_d3},
    "f43_trve_168_ewma_var99_lam094_log_ret_d3": {"inputs": ["close"], "func": f43_trve_168_ewma_var99_lam094_log_ret_d3},
    "f43_trve_169_ewma_es95_lam094_log_ret_d3": {"inputs": ["close"], "func": f43_trve_169_ewma_es95_lam094_log_ret_d3},
    "f43_trve_170_garch11_proxy_variance_full_d3": {"inputs": ["close"], "func": f43_trve_170_garch11_proxy_variance_full_d3},
    "f43_trve_171_garch11_implied_var99_log_ret_d3": {"inputs": ["close"], "func": f43_trve_171_garch11_implied_var99_log_ret_d3},
    "f43_trve_172_fhs_var95_252d_d3": {"inputs": ["close"], "func": f43_trve_172_fhs_var95_252d_d3},
    "f43_trve_173_fhs_var99_252d_d3": {"inputs": ["close"], "func": f43_trve_173_fhs_var99_252d_d3},
    "f43_trve_174_parkinson_var95_252d_d3": {"inputs": ["high", "low", "close"], "func": f43_trve_174_parkinson_var95_252d_d3},
    "f43_trve_175_garman_klass_var95_252d_d3": {"inputs": ["open", "high", "low", "close"], "func": f43_trve_175_garman_klass_var95_252d_d3},
    "f43_trve_176_ewma_minus_hist_var95_diff_252d_d3": {"inputs": ["close"], "func": f43_trve_176_ewma_minus_hist_var95_diff_252d_d3},
    "f43_trve_177_vol_of_rolling_var95_21d_in_252d_d3": {"inputs": ["close"], "func": f43_trve_177_vol_of_rolling_var95_21d_in_252d_d3},
    "f43_trve_178_vol_of_rolling_es95_21d_in_252d_d3": {"inputs": ["close"], "func": f43_trve_178_vol_of_rolling_es95_21d_in_252d_d3},
    "f43_trve_179_cond_var95_high_vol_regime_252d_d3": {"inputs": ["close"], "func": f43_trve_179_cond_var95_high_vol_regime_252d_d3},
    "f43_trve_180_cond_var95_low_vol_regime_252d_d3": {"inputs": ["close"], "func": f43_trve_180_cond_var95_low_vol_regime_252d_d3},
    "f43_trve_181_gev_block_maxima_21d_in_252d_location_d3": {"inputs": ["close"], "func": f43_trve_181_gev_block_maxima_21d_in_252d_location_d3},
    "f43_trve_182_gev_block_maxima_21d_in_252d_scale_d3": {"inputs": ["close"], "func": f43_trve_182_gev_block_maxima_21d_in_252d_scale_d3},
    "f43_trve_183_gev_block_maxima_21d_in_252d_shape_xi_d3": {"inputs": ["close"], "func": f43_trve_183_gev_block_maxima_21d_in_252d_shape_xi_d3},
    "f43_trve_184_gev_implied_var99_block_maxima_252d_d3": {"inputs": ["close"], "func": f43_trve_184_gev_implied_var99_block_maxima_252d_d3},
    "f43_trve_185_pareto_mle_alpha_lower_5pct_252d_d3": {"inputs": ["close"], "func": f43_trve_185_pareto_mle_alpha_lower_5pct_252d_d3},
    "f43_trve_186_pareto_mle_alpha_upper_5pct_252d_d3": {"inputs": ["close"], "func": f43_trve_186_pareto_mle_alpha_upper_5pct_252d_d3},
    "f43_trve_187_hill_plot_stability_lower_5_10_15pct_252d_d3": {"inputs": ["close"], "func": f43_trve_187_hill_plot_stability_lower_5_10_15pct_252d_d3},
    "f43_trve_188_hall_bootstrap_tail_proxy_252d_d3": {"inputs": ["close"], "func": f43_trve_188_hall_bootstrap_tail_proxy_252d_d3},
    "f43_trve_189_smith_tail_index_log_ret_252d_d3": {"inputs": ["close"], "func": f43_trve_189_smith_tail_index_log_ret_252d_d3},
    "f43_trve_190_evt_var99_gev_minus_cf_diff_252d_d3": {"inputs": ["close"], "func": f43_trve_190_evt_var99_gev_minus_cf_diff_252d_d3},
    "f43_trve_191_pot_var99_gpd_log_ret_252d_d3": {"inputs": ["close"], "func": f43_trve_191_pot_var99_gpd_log_ret_252d_d3},
    "f43_trve_192_evt_vs_cf_var99_disagreement_indicator_252d_d3": {"inputs": ["close"], "func": f43_trve_192_evt_vs_cf_var99_disagreement_indicator_252d_d3},
    "f43_trve_193_gpd_mean_excess_slope_top_decile_252d_d3": {"inputs": ["close"], "func": f43_trve_193_gpd_mean_excess_slope_top_decile_252d_d3},
    "f43_trve_194_max_monthly_loss_21d_blocks_252d_d3": {"inputs": ["close"], "func": f43_trve_194_max_monthly_loss_21d_blocks_252d_d3},
    "f43_trve_195_gumbel_implied_expected_max_loss_504d_d3": {"inputs": ["close"], "func": f43_trve_195_gumbel_implied_expected_max_loss_504d_d3},
    "f43_trve_196_cushion_ratio_excess_ret_over_max_dd_252d_d3": {"inputs": ["close"], "func": f43_trve_196_cushion_ratio_excess_ret_over_max_dd_252d_d3},
    "f43_trve_197_lake_ratio_meanDD_times_dur_252d_d3": {"inputs": ["close"], "func": f43_trve_197_lake_ratio_meanDD_times_dur_252d_d3},
    "f43_trve_198_frac_bars_in_dd_above_10pct_252d_d3": {"inputs": ["close"], "func": f43_trve_198_frac_bars_in_dd_above_10pct_252d_d3},
    "f43_trve_199_dd_at_risk_95pct_252d_d3": {"inputs": ["close"], "func": f43_trve_199_dd_at_risk_95pct_252d_d3},
    "f43_trve_200_dd_at_risk_99pct_252d_d3": {"inputs": ["close"], "func": f43_trve_200_dd_at_risk_99pct_252d_d3},
    "f43_trve_201_conditional_dd_at_risk_95pct_252d_d3": {"inputs": ["close"], "func": f43_trve_201_conditional_dd_at_risk_95pct_252d_d3},
    "f43_trve_202_dd_volatility_std_rolling_252d_d3": {"inputs": ["close"], "func": f43_trve_202_dd_volatility_std_rolling_252d_d3},
    "f43_trve_203_mean_dd_recovery_time_252d_d3": {"inputs": ["close"], "func": f43_trve_203_mean_dd_recovery_time_252d_d3},
    "f43_trve_204_max_dd_over_max_recovery_252d_d3": {"inputs": ["close"], "func": f43_trve_204_max_dd_over_max_recovery_252d_d3},
    "f43_trve_205_max_dd_over_var95_ratio_252d_d3": {"inputs": ["close"], "func": f43_trve_205_max_dd_over_var95_ratio_252d_d3},
    "f43_trve_206_count_distinct_dd_above_5pct_252d_d3": {"inputs": ["close"], "func": f43_trve_206_count_distinct_dd_above_5pct_252d_d3},
    "f43_trve_207_sum_all_dd_above_5pct_252d_d3": {"inputs": ["close"], "func": f43_trve_207_sum_all_dd_above_5pct_252d_d3},
    "f43_trve_208_longest_underwater_duration_252d_d3": {"inputs": ["close"], "func": f43_trve_208_longest_underwater_duration_252d_d3},
    "f43_trve_209_fraction_time_underwater_252d_d3": {"inputs": ["close"], "func": f43_trve_209_fraction_time_underwater_252d_d3},
    "f43_trve_210_dd_acceleration_change_max_dd_63d_d3": {"inputs": ["close"], "func": f43_trve_210_dd_acceleration_change_max_dd_63d_d3},
    "f43_trve_211_qreg_slope_return_on_lag_q05_252d_d3": {"inputs": ["close"], "func": f43_trve_211_qreg_slope_return_on_lag_q05_252d_d3},
    "f43_trve_212_qreg_slope_return_on_lag_q95_252d_d3": {"inputs": ["close"], "func": f43_trve_212_qreg_slope_return_on_lag_q95_252d_d3},
    "f43_trve_213_cond_var95_given_last21d_negative_252d_d3": {"inputs": ["close"], "func": f43_trve_213_cond_var95_given_last21d_negative_252d_d3},
    "f43_trve_214_cond_es95_given_high_vol_252d_d3": {"inputs": ["close"], "func": f43_trve_214_cond_es95_given_high_vol_252d_d3},
    "f43_trve_215_prob_loss_above_10pct_in_21d_252d_d3": {"inputs": ["close"], "func": f43_trve_215_prob_loss_above_10pct_in_21d_252d_d3},
    "f43_trve_216_prob_loss_above_20pct_in_63d_252d_d3": {"inputs": ["close"], "func": f43_trve_216_prob_loss_above_20pct_in_63d_252d_d3},
    "f43_trve_217_indicator_longest_dd_above_50pct_252d_d3": {"inputs": ["close"], "func": f43_trve_217_indicator_longest_dd_above_50pct_252d_d3},
    "f43_trve_218_var95_slope_change_per_bar_252d_d3": {"inputs": ["close"], "func": f43_trve_218_var95_slope_change_per_bar_252d_d3},
    "f43_trve_219_var95_autocorr_lag21_252d_d3": {"inputs": ["close"], "func": f43_trve_219_var95_autocorr_lag21_252d_d3},
    "f43_trve_220_es95_autocorr_lag1_252d_d3": {"inputs": ["close"], "func": f43_trve_220_es95_autocorr_lag1_252d_d3},
    "f43_trve_221_saddlepoint_var95_proxy_cf_higher_order_252d_d3": {"inputs": ["close"], "func": f43_trve_221_saddlepoint_var95_proxy_cf_higher_order_252d_d3},
    "f43_trve_222_multi_model_var95_mean_consensus_252d_d3": {"inputs": ["close"], "func": f43_trve_222_multi_model_var95_mean_consensus_252d_d3},
    "f43_trve_223_multi_model_var95_disagreement_252d_d3": {"inputs": ["close"], "func": f43_trve_223_multi_model_var95_disagreement_252d_d3},
    "f43_trve_224_sum_worst_5_day_blocks_252d_log_ret_d3": {"inputs": ["close"], "func": f43_trve_224_sum_worst_5_day_blocks_252d_log_ret_d3},
    "f43_trve_225_comp_ultimate_crash_prone_composite_252d_d3": {"inputs": ["close"], "func": f43_trve_225_comp_ultimate_crash_prone_composite_252d_d3},
}
