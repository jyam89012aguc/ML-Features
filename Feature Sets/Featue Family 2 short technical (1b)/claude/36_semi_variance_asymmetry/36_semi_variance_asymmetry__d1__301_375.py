"""36_semi_variance_asymmetry d1 features 301-375 — order-1 difference of corresponding base features.

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

def _underwater(close: pd.Series) -> pd.Series:
    return 1.0 - close / close.cummax()

def _gpd_mom(excesses: np.ndarray):
    """Method-of-moments GPD fit. Returns (xi, sigma) — shape and scale parameters."""
    if excesses.size < 10:
        return (np.nan, np.nan)
    m = excesses.mean()
    v = excesses.var(ddof=1)
    if v <= 0 or m <= 0:
        return (np.nan, np.nan)
    xi = 0.5 * (1.0 - m * m / v)
    sigma = 0.5 * m * (1.0 + m * m / v)
    return (float(xi), float(sigma))

def _gpd_excesses_left(r: np.ndarray, q: float=0.9):
    v = r[~np.isnan(r)]
    if v.size < 30:
        return (None, None)
    neg = -v[v < 0]
    if neg.size < 10:
        return (None, None)
    thr = np.quantile(neg, q)
    exc = neg[neg > thr] - thr
    return (exc, thr)

def _gpd_excesses_right(r: np.ndarray, q: float=0.9):
    v = r[~np.isnan(r)]
    if v.size < 30:
        return (None, None)
    pos = v[v > 0]
    if pos.size < 10:
        return (None, None)
    thr = np.quantile(pos, q)
    exc = pos[pos > thr] - thr
    return (exc, thr)

def _norm_ppf_approx(p: float) -> float:
    """Beasley-Springer-Moro approximation of normal inverse CDF."""
    if p <= 0 or p >= 1:
        return float('nan')
    a = [-39.69683028665376, 220.9460984245205, -275.9285104469687, 138.357751867269, -30.66479806614716, 2.506628277459239]
    b = [-54.47609879822406, 161.5858368580409, -155.6989798598866, 66.80131188771972, -13.28068155288572]
    c = [-0.007784894002430293, -0.3223964580411365, -2.400758277161838, -2.549732539343734, 4.374664141464968, 2.938163982698783]
    d = [0.007784695709041462, 0.3224671290700398, 2.445134137142996, 3.754408661907416]
    plow = 0.02425
    phigh = 1 - plow
    if p < plow:
        q = np.sqrt(-2 * np.log(p))
        return float((((((c[0] * q + c[1]) * q + c[2]) * q + c[3]) * q + c[4]) * q + c[5]) / ((((d[0] * q + d[1]) * q + d[2]) * q + d[3]) * q + 1))
    if p <= phigh:
        q = p - 0.5
        r2 = q * q
        return float((((((a[0] * r2 + a[1]) * r2 + a[2]) * r2 + a[3]) * r2 + a[4]) * r2 + a[5]) * q / (((((b[0] * r2 + b[1]) * r2 + b[2]) * r2 + b[3]) * r2 + b[4]) * r2 + 1))
    q = np.sqrt(-2 * np.log(1 - p))
    return float(-(((((c[0] * q + c[1]) * q + c[2]) * q + c[3]) * q + c[4]) * q + c[5]) / ((((d[0] * q + d[1]) * q + d[2]) * q + d[3]) * q + 1))

def _in_drawdown_mask(close: pd.Series) -> pd.Series:
    return close < close.cummax()

def _recovery_durations(w: np.ndarray):
    v = w[~np.isnan(w)]
    if v.size < 21:
        return None
    peak = np.maximum.accumulate(v)
    dd = 1.0 - v / peak
    recs = []
    in_dd = False
    start = 0
    for i, d in enumerate(dd):
        if d > 0 and (not in_dd):
            in_dd = True
            start = i
        elif d == 0 and in_dd:
            recs.append(i - start)
            in_dd = False
    return recs if recs else None

def f36_svas_301_gpd_xi_left_tail_252d_d1(close: pd.Series) -> pd.Series:
    """GPD shape parameter xi (Pickands) fit to left-tail excesses over 252d — positive xi = heavy left tail."""
    r = _log_returns(close)

    def _xi(w):
        exc, _ = _gpd_excesses_left(w)
        if exc is None or exc.size < 10:
            return np.nan
        return _gpd_mom(exc)[0]
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_xi, raw=True).diff()

def f36_svas_302_gpd_sigma_left_tail_252d_d1(close: pd.Series) -> pd.Series:
    """GPD scale parameter sigma fit to left-tail excesses over 252d — tail-spread severity."""
    r = _log_returns(close)

    def _sigma(w):
        exc, _ = _gpd_excesses_left(w)
        if exc is None or exc.size < 10:
            return np.nan
        return _gpd_mom(exc)[1]
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_sigma, raw=True).diff()

def f36_svas_303_gpd_xi_right_tail_252d_d1(close: pd.Series) -> pd.Series:
    """GPD shape xi fit to right-tail excesses over 252d — symmetric right-tail heaviness."""
    r = _log_returns(close)

    def _xi(w):
        exc, _ = _gpd_excesses_right(w)
        if exc is None or exc.size < 10:
            return np.nan
        return _gpd_mom(exc)[0]
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_xi, raw=True).diff()

def f36_svas_304_gpd_xi_asymmetry_left_minus_right_252d_d1(close: pd.Series) -> pd.Series:
    """GPD xi(left) - xi(right) over 252d — additive tail-shape asymmetry (>0 = left heavier)."""
    r = _log_returns(close)

    def _diff(w):
        el, _ = _gpd_excesses_left(w)
        er, _ = _gpd_excesses_right(w)
        if el is None or er is None or el.size < 10 or (er.size < 10):
            return np.nan
        xil = _gpd_mom(el)[0]
        xir = _gpd_mom(er)[0]
        if np.isnan(xil) or np.isnan(xir):
            return np.nan
        return float(xil - xir)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_diff, raw=True).diff()

def f36_svas_305_gpd_extrapolated_var_001pct_left_252d_d1(close: pd.Series) -> pd.Series:
    """GPD-extrapolated VaR at 0.1% tail level (using POT fit on left tail) over 252d — deep-tail VaR."""
    r = _log_returns(close)

    def _var(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        neg = -v[v < 0]
        if neg.size < 10:
            return np.nan
        thr = np.quantile(neg, 0.9)
        exc = neg[neg > thr] - thr
        if exc.size < 10:
            return np.nan
        xi, sigma = _gpd_mom(exc)
        if np.isnan(xi) or sigma <= 0:
            return np.nan
        p_exceed_thr = exc.size / v.size
        target_p = 0.001 / p_exceed_thr
        if target_p >= 1 or target_p <= 0:
            return np.nan
        if abs(xi) < 1e-06:
            y = -sigma * np.log(target_p)
        else:
            y = sigma / xi * (target_p ** (-xi) - 1.0)
        return float(-(thr + y))
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_var, raw=True).diff()

def f36_svas_306_gpd_es_5pct_left_252d_d1(close: pd.Series) -> pd.Series:
    """GPD-implied ES at 5% lower tail over 252d (using POT) — coherent tail expectation."""
    r = _log_returns(close)

    def _es(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        neg = -v[v < 0]
        if neg.size < 10:
            return np.nan
        thr = np.quantile(neg, 0.9)
        exc = neg[neg > thr] - thr
        if exc.size < 10:
            return np.nan
        xi, sigma = _gpd_mom(exc)
        if np.isnan(xi) or sigma <= 0 or xi >= 1:
            return np.nan
        p_exceed_thr = exc.size / v.size
        target_p = 0.05 / p_exceed_thr
        if target_p >= 1 or target_p <= 0:
            return np.nan
        if abs(xi) < 1e-06:
            var_y = -sigma * np.log(target_p)
        else:
            var_y = sigma / xi * (target_p ** (-xi) - 1.0)
        var_total = thr + var_y
        es_total = (var_total + sigma - xi * thr) / (1.0 - xi)
        return float(-es_total)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_es, raw=True).diff()

def f36_svas_307_mef_left_at_p90_252d_d1(close: pd.Series) -> pd.Series:
    """Mean excess of |neg returns| above their 90th percentile over 252d — left-tail MEF at p90."""
    r = _log_returns(close)

    def _mef(w):
        v = w[~np.isnan(w)]
        neg = -v[v < 0]
        if neg.size < 10:
            return np.nan
        thr = np.quantile(neg, 0.9)
        exc = neg[neg > thr] - thr
        return float(exc.mean()) if exc.size else np.nan
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_mef, raw=True).diff()

def f36_svas_308_mef_left_at_p95_252d_d1(close: pd.Series) -> pd.Series:
    """Mean excess of |neg returns| above their 95th percentile over 252d — deeper left-tail MEF."""
    r = _log_returns(close)

    def _mef(w):
        v = w[~np.isnan(w)]
        neg = -v[v < 0]
        if neg.size < 10:
            return np.nan
        thr = np.quantile(neg, 0.95)
        exc = neg[neg > thr] - thr
        return float(exc.mean()) if exc.size else np.nan
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_mef, raw=True).diff()

def f36_svas_309_mef_right_at_p90_252d_d1(close: pd.Series) -> pd.Series:
    """Mean excess of pos returns above their 90th percentile over 252d — right-tail MEF."""
    r = _log_returns(close)

    def _mef(w):
        v = w[~np.isnan(w)]
        pos = v[v > 0]
        if pos.size < 10:
            return np.nan
        thr = np.quantile(pos, 0.9)
        exc = pos[pos > thr] - thr
        return float(exc.mean()) if exc.size else np.nan
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_mef, raw=True).diff()

def f36_svas_310_mef_asymmetry_left_minus_right_p90_252d_d1(close: pd.Series) -> pd.Series:
    """MEF(left, p90) - MEF(right, p90) over 252d — tail-excess asymmetry; >0 = left tail's heavier."""
    r = _log_returns(close)

    def _diff(w):
        v = w[~np.isnan(w)]
        neg = -v[v < 0]
        pos = v[v > 0]
        if neg.size < 10 or pos.size < 10:
            return np.nan
        tn = np.quantile(neg, 0.9)
        tp = np.quantile(pos, 0.9)
        en = neg[neg > tn] - tn
        ep = pos[pos > tp] - tp
        if en.size == 0 or ep.size == 0:
            return np.nan
        return float(en.mean() - ep.mean())
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_diff, raw=True).diff()

def f36_svas_311_stutzer_index_252d_d1(close: pd.Series) -> pd.Series:
    """Stutzer performance index over 252d — Stutzer 2000 information-theoretic generalized Sharpe."""
    r = _log_returns(close)

    def _stutzer(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        mu = v.mean()
        sd = v.std(ddof=1)
        if sd == 0:
            return np.nan
        sr = mu / sd
        m3 = ((v - mu) ** 3).mean()
        m4 = ((v - mu) ** 4).mean()
        S = m3 / sd ** 3
        K = m4 / sd ** 4
        inside = 1.0 - S * sr / 3.0 + (K - 3.0) * sr ** 2 / 4.0
        if inside <= 0:
            return np.nan
        return float(sr * np.sqrt(inside))
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_stutzer, raw=True).diff()

def f36_svas_312_stutzer_index_504d_d1(close: pd.Series) -> pd.Series:
    """Stutzer index over 504d — biennial generalized Sharpe."""
    r = _log_returns(close)

    def _stutzer(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        mu = v.mean()
        sd = v.std(ddof=1)
        if sd == 0:
            return np.nan
        sr = mu / sd
        m3 = ((v - mu) ** 3).mean()
        m4 = ((v - mu) ** 4).mean()
        S = m3 / sd ** 3
        K = m4 / sd ** 4
        inside = 1.0 - S * sr / 3.0 + (K - 3.0) * sr ** 2 / 4.0
        if inside <= 0:
            return np.nan
        return float(sr * np.sqrt(inside))
    return r.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_stutzer, raw=True).diff()

def f36_svas_313_stutzer_minus_sharpe_252d_d1(close: pd.Series) -> pd.Series:
    """Stutzer index - raw Sharpe over 252d — degree to which non-normality penalizes/rewards the SR."""
    r = _log_returns(close)

    def _diff(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        mu = v.mean()
        sd = v.std(ddof=1)
        if sd == 0:
            return np.nan
        sr = mu / sd
        m3 = ((v - mu) ** 3).mean()
        m4 = ((v - mu) ** 4).mean()
        S = m3 / sd ** 3
        K = m4 / sd ** 4
        inside = 1.0 - S * sr / 3.0 + (K - 3.0) * sr ** 2 / 4.0
        if inside <= 0:
            return np.nan
        return float(sr * np.sqrt(inside) - sr)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_diff, raw=True).diff()

def f36_svas_314_bias_ratio_252d_d1(close: pd.Series) -> pd.Series:
    """Bias ratio (Abdulali 2006) over 252d: count(r in (0, +sigma)) / (1 + count(r in (-sigma, 0)))."""
    r = _log_returns(close)

    def _br(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        sd = v.std(ddof=1)
        if sd == 0:
            return np.nan
        pos_small = ((v > 0) & (v < sd)).sum()
        neg_small = ((v < 0) & (v > -sd)).sum()
        return float(pos_small / (1.0 + neg_small))
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_br, raw=True).diff()

def f36_svas_315_bias_ratio_504d_d1(close: pd.Series) -> pd.Series:
    """Bias ratio over 504d — biennial managed-returns indicator."""
    r = _log_returns(close)

    def _br(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        sd = v.std(ddof=1)
        if sd == 0:
            return np.nan
        pos_small = ((v > 0) & (v < sd)).sum()
        neg_small = ((v < 0) & (v > -sd)).sum()
        return float(pos_small / (1.0 + neg_small))
    return r.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_br, raw=True).diff()

def f36_svas_316_bias_ratio_zscore_in_1260d_d1(close: pd.Series) -> pd.Series:
    """Z-score of bias ratio (252d) in 1260d distribution — extremity of managed-return-like pattern."""
    r = _log_returns(close)

    def _br(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        sd = v.std(ddof=1)
        if sd == 0:
            return np.nan
        pos_small = ((v > 0) & (v < sd)).sum()
        neg_small = ((v < 0) & (v > -sd)).sum()
        return float(pos_small / (1.0 + neg_small))
    br = r.rolling(YDAYS, min_periods=QDAYS).apply(_br, raw=True)
    return _rolling_zscore(br, DDAYS_5Y, min_periods=YDAYS).diff()

def f36_svas_317_modified_sharpe_5pct_252d_d1(close: pd.Series) -> pd.Series:
    """Favre-Galeano modified Sharpe over 252d at alpha=5%: mean(r) / |CF-VaR(5%)|."""
    r = _log_returns(close)

    def _ms(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        mu = v.mean()
        sd = v.std(ddof=1)
        if sd == 0:
            return np.nan
        m3 = ((v - mu) ** 3).mean()
        m4 = ((v - mu) ** 4).mean()
        S = m3 / sd ** 3
        K = m4 / sd ** 4 - 3.0
        z = _norm_ppf_approx(0.05)
        z_cf = z + (z * z - 1) * S / 6 + (z ** 3 - 3 * z) * K / 24 - (2 * z ** 3 - 5 * z) * S ** 2 / 36
        cf_var = mu + z_cf * sd
        if cf_var >= 0:
            return np.nan
        return float(mu / abs(cf_var))
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_ms, raw=True).diff()

def f36_svas_318_modified_sharpe_1pct_252d_d1(close: pd.Series) -> pd.Series:
    """Modified Sharpe at alpha=1% over 252d — deep-tail-aware Sharpe."""
    r = _log_returns(close)

    def _ms(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        mu = v.mean()
        sd = v.std(ddof=1)
        if sd == 0:
            return np.nan
        m3 = ((v - mu) ** 3).mean()
        m4 = ((v - mu) ** 4).mean()
        S = m3 / sd ** 3
        K = m4 / sd ** 4 - 3.0
        z = _norm_ppf_approx(0.01)
        z_cf = z + (z * z - 1) * S / 6 + (z ** 3 - 3 * z) * K / 24 - (2 * z ** 3 - 5 * z) * S ** 2 / 36
        cf_var = mu + z_cf * sd
        if cf_var >= 0:
            return np.nan
        return float(mu / abs(cf_var))
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_ms, raw=True).diff()

def f36_svas_319_modified_sharpe_5pct_504d_d1(close: pd.Series) -> pd.Series:
    """Modified Sharpe at alpha=5% over 504d — biennial CF-adjusted Sharpe."""
    r = _log_returns(close)

    def _ms(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        mu = v.mean()
        sd = v.std(ddof=1)
        if sd == 0:
            return np.nan
        m3 = ((v - mu) ** 3).mean()
        m4 = ((v - mu) ** 4).mean()
        S = m3 / sd ** 3
        K = m4 / sd ** 4 - 3.0
        z = _norm_ppf_approx(0.05)
        z_cf = z + (z * z - 1) * S / 6 + (z ** 3 - 3 * z) * K / 24 - (2 * z ** 3 - 5 * z) * S ** 2 / 36
        cf_var = mu + z_cf * sd
        if cf_var >= 0:
            return np.nan
        return float(mu / abs(cf_var))
    return r.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_ms, raw=True).diff()

def f36_svas_320_modified_sharpe_minus_raw_sharpe_252d_d1(close: pd.Series) -> pd.Series:
    """Modified Sharpe(5%) - raw Sharpe over 252d — penalty/reward from CF adjustment."""
    r = _log_returns(close)

    def _diff(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        mu = v.mean()
        sd = v.std(ddof=1)
        if sd == 0:
            return np.nan
        m3 = ((v - mu) ** 3).mean()
        m4 = ((v - mu) ** 4).mean()
        S = m3 / sd ** 3
        K = m4 / sd ** 4 - 3.0
        z = _norm_ppf_approx(0.05)
        z_cf = z + (z * z - 1) * S / 6 + (z ** 3 - 3 * z) * K / 24 - (2 * z ** 3 - 5 * z) * S ** 2 / 36
        cf_var = mu + z_cf * sd
        if cf_var >= 0:
            return np.nan
        return float(mu / abs(cf_var) - mu / sd)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_diff, raw=True).diff()

def f36_svas_321_corr_abs_r_with_r_252d_d1(close: pd.Series) -> pd.Series:
    """corr(|r_t|, r_t) over 252d — sign of correlation = direction of vol-return coupling."""
    r = _log_returns(close)
    pairs = pd.concat([r.abs().rename('a'), r.rename('r')], axis=1)
    return pairs['a'].rolling(YDAYS, min_periods=QDAYS).corr(pairs['r']).diff()

def f36_svas_322_corr_abs_r_with_r_504d_d1(close: pd.Series) -> pd.Series:
    """corr(|r_t|, r_t) over 504d — biennial vol-return-coupling sign."""
    r = _log_returns(close)
    pairs = pd.concat([r.abs().rename('a'), r.rename('r')], axis=1)
    return pairs['a'].rolling(DDAYS_2Y, min_periods=YDAYS).corr(pairs['r']).diff()

def f36_svas_323_corr_abs_r_with_r_zscore_in_1260d_d1(close: pd.Series) -> pd.Series:
    """Z-score of 252d corr(|r|,r) in 1260d distribution — regime extremity of vol-return coupling."""
    r = _log_returns(close)
    pairs = pd.concat([r.abs().rename('a'), r.rename('r')], axis=1)
    c = pairs['a'].rolling(YDAYS, min_periods=QDAYS).corr(pairs['r'])
    return _rolling_zscore(c, DDAYS_5Y, min_periods=YDAYS).diff()

def f36_svas_324_corr_rsq_with_r_252d_d1(close: pd.Series) -> pd.Series:
    """corr(r^2, r) over 252d — squared-return-vs-return; alternative skewness proxy."""
    r = _log_returns(close)
    pairs = pd.concat([(r ** 2).rename('s'), r.rename('r')], axis=1)
    return pairs['s'].rolling(YDAYS, min_periods=QDAYS).corr(pairs['r']).diff()

def f36_svas_325_skew_returns_in_drawdown_252d_d1(close: pd.Series) -> pd.Series:
    """Skewness of returns restricted to in-drawdown bars over 252d."""
    r = _log_returns(close)
    mask = _in_drawdown_mask(close)
    sub = r.where(mask)

    def _sk(w):
        v = w[~np.isnan(w)]
        if v.size < 21:
            return np.nan
        m = v.mean()
        s = v.std(ddof=1)
        if s == 0:
            return np.nan
        return float(((v - m) ** 3).mean() / s ** 3)
    return sub.rolling(YDAYS, min_periods=QDAYS).apply(_sk, raw=True).diff()

def f36_svas_326_skew_returns_at_new_highs_252d_d1(close: pd.Series) -> pd.Series:
    """Skewness of returns restricted to at-or-above expanding-max bars over 252d."""
    r = _log_returns(close)
    mask = close >= close.cummax()
    sub = r.where(mask)

    def _sk(w):
        v = w[~np.isnan(w)]
        if v.size < 21:
            return np.nan
        m = v.mean()
        s = v.std(ddof=1)
        if s == 0:
            return np.nan
        return float(((v - m) ** 3).mean() / s ** 3)
    return sub.rolling(YDAYS, min_periods=QDAYS).apply(_sk, raw=True).diff()

def f36_svas_327_skew_conditional_asymmetry_dd_vs_high_252d_d1(close: pd.Series) -> pd.Series:
    """skew(in-DD) - skew(at-highs) over 252d — direct DD-vs-highs skew asymmetry."""
    r = _log_returns(close)
    in_dd = _in_drawdown_mask(close)
    at_hi = close >= close.cummax()

    def _sk(w):
        v = w[~np.isnan(w)]
        if v.size < 21:
            return np.nan
        m = v.mean()
        s = v.std(ddof=1)
        if s == 0:
            return np.nan
        return float(((v - m) ** 3).mean() / s ** 3)
    skd = r.where(in_dd).rolling(YDAYS, min_periods=QDAYS).apply(_sk, raw=True)
    skh = r.where(at_hi).rolling(YDAYS, min_periods=QDAYS).apply(_sk, raw=True)
    return (skd - skh).diff()

def f36_svas_328_kurt_returns_in_drawdown_252d_d1(close: pd.Series) -> pd.Series:
    """Kurtosis of returns in-drawdown over 252d — fat tails during DD periods."""
    r = _log_returns(close)
    sub = r.where(_in_drawdown_mask(close))

    def _k(w):
        v = w[~np.isnan(w)]
        if v.size < 21:
            return np.nan
        m = v.mean()
        s = v.std(ddof=1)
        if s == 0:
            return np.nan
        return float(((v - m) ** 4).mean() / s ** 4 - 3.0)
    return sub.rolling(YDAYS, min_periods=QDAYS).apply(_k, raw=True).diff()

def f36_svas_329_mean_return_in_drawdown_252d_d1(close: pd.Series) -> pd.Series:
    """Mean return restricted to in-drawdown bars over 252d — typical bar-return during DD."""
    r = _log_returns(close)
    return r.where(_in_drawdown_mask(close)).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f36_svas_330_frac_bars_dd_above_10pct_252d_d1(close: pd.Series) -> pd.Series:
    """Fraction of trailing 252d bars where DD (from expanding max) > 10% — chronic mild-DD share."""
    uw = _underwater(close)
    return (uw > 0.1).astype(float).where(uw.notna(), np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f36_svas_331_frac_bars_dd_above_20pct_252d_d1(close: pd.Series) -> pd.Series:
    """Fraction of trailing 252d bars where DD > 20% — sustained moderate-DD share."""
    uw = _underwater(close)
    return (uw > 0.2).astype(float).where(uw.notna(), np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f36_svas_332_frac_bars_dd_above_30pct_252d_d1(close: pd.Series) -> pd.Series:
    """Fraction of trailing 252d bars where DD > 30%."""
    uw = _underwater(close)
    return (uw > 0.3).astype(float).where(uw.notna(), np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f36_svas_333_frac_bars_dd_above_50pct_504d_d1(close: pd.Series) -> pd.Series:
    """Fraction of trailing 504d bars where DD > 50% — biennial deep-DD share (direct stuck-peak proxy)."""
    uw = _underwater(close)
    return (uw > 0.5).astype(float).where(uw.notna(), np.nan).rolling(DDAYS_2Y, min_periods=YDAYS).mean().diff()

def f36_svas_334_count_distinct_dd_events_above_10pct_252d_d1(close: pd.Series) -> pd.Series:
    """Count of distinct drawdown events exceeding 10% depth in trailing 252d."""
    uw = _underwater(close)

    def _cnt(w):
        v = w[~np.isnan(w)]
        if v.size < 21:
            return np.nan
        in_dd_deep = v > 0.1
        cnt = 0
        prev = False
        for x in in_dd_deep:
            if x and (not prev):
                cnt += 1
            prev = x
        return float(cnt)
    return uw.rolling(YDAYS, min_periods=QDAYS).apply(_cnt, raw=True).diff()

def f36_svas_335_count_distinct_dd_events_above_20pct_504d_d1(close: pd.Series) -> pd.Series:
    """Count of distinct drawdown events exceeding 20% depth in trailing 504d."""
    uw = _underwater(close)

    def _cnt(w):
        v = w[~np.isnan(w)]
        if v.size < 21:
            return np.nan
        in_dd_deep = v > 0.2
        cnt = 0
        prev = False
        for x in in_dd_deep:
            if x and (not prev):
                cnt += 1
            prev = x
        return float(cnt)
    return uw.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_cnt, raw=True).diff()

def f36_svas_336_dd_autocorr_lag1_252d_d1(close: pd.Series) -> pd.Series:
    """Autocorrelation of underwater curve at lag 1 over 252d — daily DD persistence."""
    uw = _underwater(close)
    pairs = pd.concat([uw.shift(1).rename('ul'), uw.rename('u')], axis=1)
    return pairs['ul'].rolling(YDAYS, min_periods=QDAYS).corr(pairs['u']).diff()

def f36_svas_337_dd_autocorr_lag5_252d_d1(close: pd.Series) -> pd.Series:
    """Autocorrelation of underwater curve at lag 5 over 252d — weekly DD persistence."""
    uw = _underwater(close)
    pairs = pd.concat([uw.shift(5).rename('ul'), uw.rename('u')], axis=1)
    return pairs['ul'].rolling(YDAYS, min_periods=QDAYS).corr(pairs['u']).diff()

def f36_svas_338_dd_autocorr_lag63_504d_d1(close: pd.Series) -> pd.Series:
    """Autocorrelation of underwater curve at lag 63 over 504d — quarterly DD persistence."""
    uw = _underwater(close)
    pairs = pd.concat([uw.shift(63).rename('ul'), uw.rename('u')], axis=1)
    return pairs['ul'].rolling(DDAYS_2Y, min_periods=YDAYS).corr(pairs['u']).diff()

def f36_svas_339_dd_clustering_mean_event_gap_504d_d1(close: pd.Series) -> pd.Series:
    """Mean bars between drawdown-start events (DD crossing 0) in trailing 504d — DD inter-arrival cadence."""
    in_dd = (close < close.cummax()).astype(int)
    starts = (in_dd == 1) & (in_dd.shift(1, fill_value=0) == 0)
    arr = starts.values

    def _ia(w):
        idx = np.where(w > 0)[0]
        if idx.size < 2:
            return np.nan
        return float(np.diff(idx).mean())
    return pd.Series(arr.astype(float), index=close.index).rolling(DDAYS_2Y, min_periods=YDAYS).apply(_ia, raw=True).diff()

def f36_svas_340_recovery_median_duration_504d_d1(close: pd.Series) -> pd.Series:
    """Median bars-to-recovery for completed DDs in trailing 504d — typical bounce-back."""

    def _med(w):
        recs = _recovery_durations(w)
        if recs is None:
            return np.nan
        return float(np.median(recs))
    return close.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_med, raw=True).diff()

def f36_svas_341_recovery_max_duration_504d_d1(close: pd.Series) -> pd.Series:
    """Max bars-to-recovery in 504d — worst observed bounce-back time."""

    def _mx(w):
        recs = _recovery_durations(w)
        if recs is None:
            return np.nan
        return float(np.max(recs))
    return close.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_mx, raw=True).diff()

def f36_svas_342_recovery_std_duration_504d_d1(close: pd.Series) -> pd.Series:
    """Std of bars-to-recovery in 504d — recovery-time variability."""

    def _sd(w):
        recs = _recovery_durations(w)
        if recs is None or len(recs) < 2:
            return np.nan
        return float(np.std(recs, ddof=1))
    return close.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_sd, raw=True).diff()

def f36_svas_343_recovery_skewness_504d_d1(close: pd.Series) -> pd.Series:
    """Skewness of bars-to-recovery distribution in 504d — positive = long-tail recovery times."""

    def _sk(w):
        recs = _recovery_durations(w)
        if recs is None or len(recs) < 3:
            return np.nan
        v = np.array(recs, dtype=float)
        m = v.mean()
        s = v.std(ddof=1)
        if s == 0:
            return np.nan
        return float(((v - m) ** 3).mean() / s ** 3)
    return close.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_sk, raw=True).diff()

def f36_svas_344_recovery_count_504d_d1(close: pd.Series) -> pd.Series:
    """Count of completed drawdown-recovery cycles in trailing 504d — DD cadence."""

    def _cnt(w):
        recs = _recovery_durations(w)
        if recs is None:
            return 0.0
        return float(len(recs))
    return close.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_cnt, raw=True).diff()

def f36_svas_345_worst_3d_return_in_252d_d1(close: pd.Series) -> pd.Series:
    """Min trailing-3d cumulative return seen in last 252d — worst 3-day decline."""
    r = _log_returns(close)
    r3 = r.rolling(3, min_periods=2).sum()
    return r3.rolling(YDAYS, min_periods=QDAYS).min().diff()

def f36_svas_346_worst_10d_return_in_252d_d1(close: pd.Series) -> pd.Series:
    """Min trailing-10d cumulative return in last 252d — worst 10-day decline."""
    r = _log_returns(close)
    r10 = r.rolling(10, min_periods=3).sum()
    return r10.rolling(YDAYS, min_periods=QDAYS).min().diff()

def f36_svas_347_worst_63d_return_in_252d_d1(close: pd.Series) -> pd.Series:
    """Min trailing-63d cumulative return in last 252d — worst quarterly decline."""
    r = _log_returns(close)
    r63 = r.rolling(QDAYS, min_periods=MDAYS).sum()
    return r63.rolling(YDAYS, min_periods=QDAYS).min().diff()

def f36_svas_348_worst_126d_return_in_504d_d1(close: pd.Series) -> pd.Series:
    """Min trailing-126d cumulative return in last 504d — worst half-year decline."""
    r = _log_returns(close)
    r126 = r.rolling(126, min_periods=QDAYS).sum()
    return r126.rolling(DDAYS_2Y, min_periods=YDAYS).min().diff()

def f36_svas_349_worst_252d_return_in_504d_d1(close: pd.Series) -> pd.Series:
    """Min trailing-252d cumulative return in last 504d — worst annual decline."""
    r = _log_returns(close)
    r252 = r.rolling(YDAYS, min_periods=QDAYS).sum()
    return r252.rolling(DDAYS_2Y, min_periods=YDAYS).min().diff()

def f36_svas_350_current_drawdown_minus_worst_252d_return_ratio_d1(close: pd.Series) -> pd.Series:
    """Current DD depth / |worst 252d return| — how deep is now vs the worst annual stretch."""
    uw = _underwater(close)
    r = _log_returns(close)
    r252 = r.rolling(YDAYS, min_periods=QDAYS).sum()
    worst_252 = r252.rolling(DDAYS_2Y, min_periods=YDAYS).min()
    return _safe_div(uw, worst_252.abs()).diff()

def f36_svas_351_cum_loss_during_current_loss_streak_d1(close: pd.Series) -> pd.Series:
    """Cumulative log return during the current consecutive-negative-return streak (else 0)."""
    r = _log_returns(close).values
    n = r.size
    out = np.full(n, np.nan, dtype=float)
    cum = 0.0
    for i in range(n):
        if np.isnan(r[i]):
            cum = 0.0
            out[i] = np.nan
            continue
        if r[i] < 0:
            cum += r[i]
        else:
            cum = 0.0
        out[i] = cum
    return pd.Series(out, index=close.index).diff()

def f36_svas_352_max_streak_cum_loss_in_252d_d1(close: pd.Series) -> pd.Series:
    """Largest (most-negative) cumulative loss during a consecutive-loss streak in last 252d."""
    r = _log_returns(close).values
    n = r.size
    streak_cums = []
    cur = 0.0
    out = np.full(n, np.nan, dtype=float)
    win = YDAYS
    for i in range(n):
        if np.isnan(r[i]):
            if cur < 0:
                streak_cums.append((i, cur))
            cur = 0.0
            out[i] = np.nan
            continue
        if r[i] < 0:
            cur += r[i]
        else:
            if cur < 0:
                streak_cums.append((i, cur))
            cur = 0.0
        relevant = [c for j, c in streak_cums if i - j < win]
        if cur < 0:
            relevant.append(cur)
        if relevant:
            out[i] = float(min(relevant))
    return pd.Series(out, index=close.index).diff()

def f36_svas_353_mean_streak_cum_loss_in_252d_d1(close: pd.Series) -> pd.Series:
    """Mean cum-loss across completed loss streaks in trailing 252d — typical-streak severity."""

    def _ms(w):
        v = w[~np.isnan(w)]
        if v.size < 21:
            return np.nan
        streaks = []
        cur = 0.0
        for x in v:
            if x < 0:
                cur += x
            else:
                if cur < 0:
                    streaks.append(cur)
                cur = 0.0
        if cur < 0:
            streaks.append(cur)
        return float(np.mean(streaks)) if streaks else 0.0
    r = _log_returns(close)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_ms, raw=True).diff()

def f36_svas_354_count_loss_streaks_above_5pct_252d_d1(close: pd.Series) -> pd.Series:
    """Count of completed loss streaks with cum loss > 5% in trailing 252d."""

    def _cnt(w):
        v = w[~np.isnan(w)]
        if v.size < 21:
            return np.nan
        cnt = 0
        cur = 0.0
        for x in v:
            if x < 0:
                cur += x
            else:
                if cur < -0.05:
                    cnt += 1
                cur = 0.0
        if cur < -0.05:
            cnt += 1
        return float(cnt)
    r = _log_returns(close)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_cnt, raw=True).diff()

def f36_svas_355_loss_streak_severity_zscore_504d_d1(close: pd.Series) -> pd.Series:
    """Z-score of trailing 252d max-streak-cum-loss in 504d distribution."""

    def _max(w):
        v = w[~np.isnan(w)]
        if v.size < 21:
            return np.nan
        streaks = []
        cur = 0.0
        for x in v:
            if x < 0:
                cur += x
            else:
                if cur < 0:
                    streaks.append(cur)
                cur = 0.0
        if cur < 0:
            streaks.append(cur)
        return float(min(streaks)) if streaks else 0.0
    r = _log_returns(close)
    ms = r.rolling(YDAYS, min_periods=QDAYS).apply(_max, raw=True)
    return _rolling_zscore(ms, DDAYS_2Y, min_periods=YDAYS).diff()

def f36_svas_356_dd_energy_squared_252d_d1(close: pd.Series) -> pd.Series:
    """Sum of DD^2 over trailing 252d — "energy" of underwater path."""
    uw = _underwater(close)
    return (uw ** 2).rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f36_svas_357_dd_energy_cubed_252d_d1(close: pd.Series) -> pd.Series:
    """Sum of DD^3 over trailing 252d — convex penalty on deeper DDs."""
    uw = _underwater(close)
    return (uw ** 3).rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f36_svas_358_dd_energy_squared_504d_d1(close: pd.Series) -> pd.Series:
    """Sum of DD^2 over trailing 504d — biennial DD energy."""
    uw = _underwater(close)
    return (uw ** 2).rolling(DDAYS_2Y, min_periods=YDAYS).sum().diff()

def f36_svas_359_log_dd_energy_squared_252d_d1(close: pd.Series) -> pd.Series:
    """log(sum DD^2 + eps) over 252d — log-compressed DD energy."""
    uw = _underwater(close)
    e = (uw ** 2).rolling(YDAYS, min_periods=QDAYS).sum()
    return np.log(e + 1e-12).where(e > 0, np.nan).diff()

def f36_svas_360_hist_var_5pct_252d_d1(close: pd.Series) -> pd.Series:
    """Historical VaR at 5% over 252d — empirical lower-tail quantile."""
    r = _log_returns(close)
    return r.rolling(YDAYS, min_periods=QDAYS).quantile(0.05).diff()

def f36_svas_361_parametric_var_5pct_252d_d1(close: pd.Series) -> pd.Series:
    """Parametric VaR at 5% over 252d — mean - 1.645 * std (normal approx)."""
    r = _log_returns(close)
    mu = r.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    return (mu - 1.6449 * sd).diff()

def f36_svas_362_hist_minus_parametric_var_5pct_252d_d1(close: pd.Series) -> pd.Series:
    """Hist VaR - parametric VaR at 5% over 252d — gap indicating non-normality of left tail."""
    r = _log_returns(close)
    hist = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.05)
    mu = r.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    par = mu - 1.6449 * sd
    return (hist - par).diff()

def f36_svas_363_hist_over_parametric_var_5pct_252d_d1(close: pd.Series) -> pd.Series:
    """|Hist VaR| / |parametric VaR| at 5% over 252d — multiplicative tail-fatness factor."""
    r = _log_returns(close)
    hist = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.05)
    mu = r.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    par = mu - 1.6449 * sd
    return _safe_div(hist.abs(), par.abs()).diff()

def f36_svas_364_tail_severity_full_composite_252d_d1(close: pd.Series) -> pd.Series:
    """Z-blend of GPD xi-left + MEF-left-p95 + |hist VaR 5%| + DD energy — overall tail severity."""
    r = _log_returns(close)

    def _xi(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        neg = -v[v < 0]
        if neg.size < 10:
            return np.nan
        thr = np.quantile(neg, 0.9)
        exc = neg[neg > thr] - thr
        if exc.size < 10:
            return np.nan
        return _gpd_mom(exc)[0]
    xi_l = r.rolling(YDAYS, min_periods=QDAYS).apply(_xi, raw=True)

    def _mef(w):
        v = w[~np.isnan(w)]
        neg = -v[v < 0]
        if neg.size < 10:
            return np.nan
        thr = np.quantile(neg, 0.95)
        exc = neg[neg > thr] - thr
        return float(exc.mean()) if exc.size else np.nan
    mef = r.rolling(YDAYS, min_periods=QDAYS).apply(_mef, raw=True)
    var5 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.05).abs()
    uw = _underwater(close)
    energy = (uw ** 2).rolling(YDAYS, min_periods=QDAYS).sum()
    z_xi = _rolling_zscore(xi_l, DDAYS_2Y, min_periods=YDAYS)
    z_mef = _rolling_zscore(mef, DDAYS_2Y, min_periods=YDAYS)
    z_var = _rolling_zscore(var5, DDAYS_2Y, min_periods=YDAYS)
    z_e = _rolling_zscore(energy, DDAYS_2Y, min_periods=YDAYS)
    pieces = pd.concat([z_xi.rename('x'), z_mef.rename('m'), z_var.rename('v'), z_e.rename('e')], axis=1)
    return pieces.mean(axis=1, skipna=True).diff()

def f36_svas_365_chronic_dd_composite_504d_d1(close: pd.Series) -> pd.Series:
    """Z-blend of frac_bars_dd>10% + frac_bars_dd>30% + DD autocorr lag5 — chronic-DD profile."""
    uw = _underwater(close)
    f10 = (uw > 0.1).astype(float).where(uw.notna(), np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    f30 = (uw > 0.3).astype(float).where(uw.notna(), np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    pairs = pd.concat([uw.shift(5).rename('ul'), uw.rename('u')], axis=1)
    ac5 = pairs['ul'].rolling(YDAYS, min_periods=QDAYS).corr(pairs['u'])
    z10 = _rolling_zscore(f10, DDAYS_2Y, min_periods=YDAYS)
    z30 = _rolling_zscore(f30, DDAYS_2Y, min_periods=YDAYS)
    z_ac = _rolling_zscore(ac5, DDAYS_2Y, min_periods=YDAYS)
    pieces = pd.concat([z10.rename('a'), z30.rename('b'), z_ac.rename('c')], axis=1)
    return pieces.mean(axis=1, skipna=True).diff()

def f36_svas_366_recovery_failure_composite_504d_d1(close: pd.Series) -> pd.Series:
    """Z-blend of recovery_max_duration + recovery_skewness + recovery_count (negated) — slow recovery indicator."""

    def _mx(w):
        recs = _recovery_durations(w)
        if recs is None:
            return np.nan
        return float(np.max(recs))

    def _sk(w):
        recs = _recovery_durations(w)
        if recs is None or len(recs) < 3:
            return np.nan
        v = np.array(recs, dtype=float)
        m = v.mean()
        s = v.std(ddof=1)
        if s == 0:
            return np.nan
        return float(((v - m) ** 3).mean() / s ** 3)

    def _cnt(w):
        recs = _recovery_durations(w)
        if recs is None:
            return 0.0
        return float(len(recs))
    mx = close.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_mx, raw=True)
    sk = close.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_sk, raw=True)
    cnt = close.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_cnt, raw=True)
    z_mx = _rolling_zscore(mx, DDAYS_5Y, min_periods=YDAYS)
    z_sk = _rolling_zscore(sk, DDAYS_5Y, min_periods=YDAYS)
    z_cn = _rolling_zscore(-cnt, DDAYS_5Y, min_periods=YDAYS)
    pieces = pd.concat([z_mx.rename('a'), z_sk.rename('b'), z_cn.rename('c')], axis=1)
    return pieces.mean(axis=1, skipna=True).diff()

def f36_svas_367_loss_streak_severity_composite_252d_d1(close: pd.Series) -> pd.Series:
    """Z-blend of max-streak-cum-loss (negated) + count-loss-streaks-above-5% + mean-streak-cum-loss (negated)."""

    def _mx(w):
        v = w[~np.isnan(w)]
        if v.size < 21:
            return np.nan
        streaks = []
        cur = 0.0
        for x in v:
            if x < 0:
                cur += x
            elif cur < 0:
                streaks.append(cur)
                cur = 0.0
        if cur < 0:
            streaks.append(cur)
        return float(min(streaks)) if streaks else 0.0

    def _cnt(w):
        v = w[~np.isnan(w)]
        if v.size < 21:
            return np.nan
        cnt = 0
        cur = 0.0
        for x in v:
            if x < 0:
                cur += x
            else:
                if cur < -0.05:
                    cnt += 1
                cur = 0.0
        if cur < -0.05:
            cnt += 1
        return float(cnt)

    def _ms(w):
        v = w[~np.isnan(w)]
        if v.size < 21:
            return np.nan
        streaks = []
        cur = 0.0
        for x in v:
            if x < 0:
                cur += x
            elif cur < 0:
                streaks.append(cur)
                cur = 0.0
        if cur < 0:
            streaks.append(cur)
        return float(np.mean(streaks)) if streaks else 0.0
    r = _log_returns(close)
    mx = r.rolling(YDAYS, min_periods=QDAYS).apply(_mx, raw=True)
    cnt = r.rolling(YDAYS, min_periods=QDAYS).apply(_cnt, raw=True)
    ms = r.rolling(YDAYS, min_periods=QDAYS).apply(_ms, raw=True)
    z_mx = _rolling_zscore(-mx, DDAYS_2Y, min_periods=YDAYS)
    z_cn = _rolling_zscore(cnt, DDAYS_2Y, min_periods=YDAYS)
    z_ms = _rolling_zscore(-ms, DDAYS_2Y, min_periods=YDAYS)
    pieces = pd.concat([z_mx.rename('a'), z_cn.rename('b'), z_ms.rename('c')], axis=1)
    return pieces.mean(axis=1, skipna=True).diff()

def f36_svas_368_non_normal_tail_composite_252d_d1(close: pd.Series) -> pd.Series:
    """Z-blend of (hist VaR - param VaR) + MEF-asymmetry + bias-ratio — distributional non-normality severity."""
    r = _log_returns(close)
    hist = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.05)
    mu = r.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    par = mu - 1.6449 * sd
    gap = hist - par

    def _mef_diff(w):
        v = w[~np.isnan(w)]
        neg = -v[v < 0]
        pos = v[v > 0]
        if neg.size < 10 or pos.size < 10:
            return np.nan
        tn = np.quantile(neg, 0.9)
        tp = np.quantile(pos, 0.9)
        en = neg[neg > tn] - tn
        ep = pos[pos > tp] - tp
        if en.size == 0 or ep.size == 0:
            return np.nan
        return float(en.mean() - ep.mean())
    mef = r.rolling(YDAYS, min_periods=QDAYS).apply(_mef_diff, raw=True)

    def _br(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        s = v.std(ddof=1)
        if s == 0:
            return np.nan
        return float(((v > 0) & (v < s)).sum() / (1.0 + ((v < 0) & (v > -s)).sum()))
    br = r.rolling(YDAYS, min_periods=QDAYS).apply(_br, raw=True)
    z_g = _rolling_zscore(gap, DDAYS_2Y, min_periods=YDAYS)
    z_m = _rolling_zscore(mef, DDAYS_2Y, min_periods=YDAYS)
    z_b = _rolling_zscore(br, DDAYS_2Y, min_periods=YDAYS)
    pieces = pd.concat([z_g.rename('g'), z_m.rename('m'), z_b.rename('b')], axis=1)
    return pieces.mean(axis=1, skipna=True).diff()

def f36_svas_369_dd_in_drawdown_distributional_composite_252d_d1(close: pd.Series) -> pd.Series:
    """Z-blend of skew-in-DD (negated) + kurt-in-DD + mean-return-in-DD (negated) — DD-period distributional severity."""
    r = _log_returns(close)
    sub = r.where(_in_drawdown_mask(close))

    def _sk(w):
        v = w[~np.isnan(w)]
        if v.size < 21:
            return np.nan
        m = v.mean()
        s = v.std(ddof=1)
        if s == 0:
            return np.nan
        return float(((v - m) ** 3).mean() / s ** 3)

    def _k(w):
        v = w[~np.isnan(w)]
        if v.size < 21:
            return np.nan
        m = v.mean()
        s = v.std(ddof=1)
        if s == 0:
            return np.nan
        return float(((v - m) ** 4).mean() / s ** 4 - 3.0)
    sk = sub.rolling(YDAYS, min_periods=QDAYS).apply(_sk, raw=True)
    kt = sub.rolling(YDAYS, min_periods=QDAYS).apply(_k, raw=True)
    mn = sub.rolling(YDAYS, min_periods=QDAYS).mean()
    z_s = _rolling_zscore(-sk, DDAYS_2Y, min_periods=YDAYS)
    z_k = _rolling_zscore(kt, DDAYS_2Y, min_periods=YDAYS)
    z_m = _rolling_zscore(-mn, DDAYS_2Y, min_periods=YDAYS)
    pieces = pd.concat([z_s.rename('s'), z_k.rename('k'), z_m.rename('m')], axis=1)
    return pieces.mean(axis=1, skipna=True).diff()

def f36_svas_370_worst_k_day_composite_252d_d1(close: pd.Series) -> pd.Series:
    """Z-blend of |worst-3d| + |worst-10d| + |worst-63d| over 252d — multi-horizon worst-K-day severity."""
    r = _log_returns(close)
    w3 = r.rolling(3, min_periods=2).sum().rolling(YDAYS, min_periods=QDAYS).min().abs()
    w10 = r.rolling(10, min_periods=3).sum().rolling(YDAYS, min_periods=QDAYS).min().abs()
    w63 = r.rolling(QDAYS, min_periods=MDAYS).sum().rolling(YDAYS, min_periods=QDAYS).min().abs()
    z3 = _rolling_zscore(w3, DDAYS_2Y, min_periods=YDAYS)
    z10 = _rolling_zscore(w10, DDAYS_2Y, min_periods=YDAYS)
    z63 = _rolling_zscore(w63, DDAYS_2Y, min_periods=YDAYS)
    pieces = pd.concat([z3.rename('a'), z10.rename('b'), z63.rename('c')], axis=1)
    return pieces.mean(axis=1, skipna=True).diff()

def f36_svas_371_dd_intensity_composite_504d_d1(close: pd.Series) -> pd.Series:
    """Z-blend of DD-energy-squared + DD-energy-cubed + log-DD-energy — intensity of underwater path."""
    uw = _underwater(close)
    e2 = (uw ** 2).rolling(YDAYS, min_periods=QDAYS).sum()
    e3 = (uw ** 3).rolling(YDAYS, min_periods=QDAYS).sum()
    le = np.log(e2 + 1e-12).where(e2 > 0, np.nan)
    z2 = _rolling_zscore(e2, DDAYS_2Y, min_periods=YDAYS)
    z3 = _rolling_zscore(e3, DDAYS_2Y, min_periods=YDAYS)
    zl = _rolling_zscore(le, DDAYS_2Y, min_periods=YDAYS)
    pieces = pd.concat([z2.rename('a'), z3.rename('b'), zl.rename('c')], axis=1)
    return pieces.mean(axis=1, skipna=True).diff()

def f36_svas_372_corr_abs_r_negative_at_peak_indicator_d1(close: pd.Series) -> pd.Series:
    """Indicator: corr(|r|, r) < 0 AND price within 5% of 252d peak — leverage effect active at peak."""
    r = _log_returns(close)
    pairs = pd.concat([r.abs().rename('a'), r.rename('r')], axis=1)
    c = pairs['a'].rolling(YDAYS, min_periods=QDAYS).corr(pairs['r'])
    peak = close.rolling(YDAYS, min_periods=QDAYS).max()
    near_peak = close >= 0.95 * peak
    return ((c < 0) & near_peak).astype(float).where(c.notna() & peak.notna(), np.nan).diff()

def f36_svas_373_modified_sharpe_at_peak_252d_d1(close: pd.Series) -> pd.Series:
    """Modified Sharpe(5%) evaluated only at near-peak bars — CF-adjusted risk-adjusted return at peak."""
    r = _log_returns(close)

    def _ms(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        mu = v.mean()
        sd = v.std(ddof=1)
        if sd == 0:
            return np.nan
        m3 = ((v - mu) ** 3).mean()
        m4 = ((v - mu) ** 4).mean()
        S = m3 / sd ** 3
        K = m4 / sd ** 4 - 3.0
        z = _norm_ppf_approx(0.05)
        z_cf = z + (z * z - 1) * S / 6 + (z ** 3 - 3 * z) * K / 24 - (2 * z ** 3 - 5 * z) * S ** 2 / 36
        cf_var = mu + z_cf * sd
        if cf_var >= 0:
            return np.nan
        return float(mu / abs(cf_var))
    ms = r.rolling(YDAYS, min_periods=QDAYS).apply(_ms, raw=True)
    peak = close.rolling(YDAYS, min_periods=QDAYS).max()
    near_peak = close >= 0.95 * peak
    return ms.where(near_peak, np.nan).diff()

def f36_svas_374_p_dd_above_50pct_at_peak_504d_d1(close: pd.Series) -> pd.Series:
    """frac_bars_dd>50% (504d) evaluated at near-peak bars — chronic-deep-DD profile encountered at peaks."""
    uw = _underwater(close)
    f50 = (uw > 0.5).astype(float).where(uw.notna(), np.nan).rolling(DDAYS_2Y, min_periods=YDAYS).mean()
    peak = close.rolling(YDAYS, min_periods=QDAYS).max()
    near_peak = close >= 0.95 * peak
    return f50.where(near_peak, np.nan).diff()

def f36_svas_375_stuck_peak_full_asymmetry_composite_504d_d1(close: pd.Series) -> pd.Series:
    """Master asymmetry composite for stuck-peak: GPD xi-left + recovery-failure + DD-intensity + non-normal-tail."""
    r = _log_returns(close)

    def _xi(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        neg = -v[v < 0]
        if neg.size < 10:
            return np.nan
        thr = np.quantile(neg, 0.9)
        exc = neg[neg > thr] - thr
        if exc.size < 10:
            return np.nan
        return _gpd_mom(exc)[0]
    xi_l = r.rolling(YDAYS, min_periods=QDAYS).apply(_xi, raw=True)
    z_xi = _rolling_zscore(xi_l, DDAYS_2Y, min_periods=YDAYS)

    def _mx(w):
        recs = _recovery_durations(w)
        if recs is None:
            return np.nan
        return float(np.max(recs))
    mx = close.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_mx, raw=True)
    z_mx = _rolling_zscore(mx, DDAYS_5Y, min_periods=YDAYS)
    uw = _underwater(close)
    e2 = (uw ** 2).rolling(YDAYS, min_periods=QDAYS).sum()
    z_e = _rolling_zscore(e2, DDAYS_2Y, min_periods=YDAYS)
    hist = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.05)
    mu = r.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    par = mu - 1.6449 * sd
    gap = hist - par
    z_g = _rolling_zscore(gap, DDAYS_2Y, min_periods=YDAYS)
    pieces = pd.concat([z_xi.rename('a'), z_mx.rename('b'), z_e.rename('c'), z_g.rename('d')], axis=1)
    return pieces.mean(axis=1, skipna=True).diff()
SEMI_VARIANCE_ASYMMETRY_D1_REGISTRY_301_375 = {'f36_svas_301_gpd_xi_left_tail_252d_d1': {'inputs': ['close'], 'func': f36_svas_301_gpd_xi_left_tail_252d_d1}, 'f36_svas_302_gpd_sigma_left_tail_252d_d1': {'inputs': ['close'], 'func': f36_svas_302_gpd_sigma_left_tail_252d_d1}, 'f36_svas_303_gpd_xi_right_tail_252d_d1': {'inputs': ['close'], 'func': f36_svas_303_gpd_xi_right_tail_252d_d1}, 'f36_svas_304_gpd_xi_asymmetry_left_minus_right_252d_d1': {'inputs': ['close'], 'func': f36_svas_304_gpd_xi_asymmetry_left_minus_right_252d_d1}, 'f36_svas_305_gpd_extrapolated_var_001pct_left_252d_d1': {'inputs': ['close'], 'func': f36_svas_305_gpd_extrapolated_var_001pct_left_252d_d1}, 'f36_svas_306_gpd_es_5pct_left_252d_d1': {'inputs': ['close'], 'func': f36_svas_306_gpd_es_5pct_left_252d_d1}, 'f36_svas_307_mef_left_at_p90_252d_d1': {'inputs': ['close'], 'func': f36_svas_307_mef_left_at_p90_252d_d1}, 'f36_svas_308_mef_left_at_p95_252d_d1': {'inputs': ['close'], 'func': f36_svas_308_mef_left_at_p95_252d_d1}, 'f36_svas_309_mef_right_at_p90_252d_d1': {'inputs': ['close'], 'func': f36_svas_309_mef_right_at_p90_252d_d1}, 'f36_svas_310_mef_asymmetry_left_minus_right_p90_252d_d1': {'inputs': ['close'], 'func': f36_svas_310_mef_asymmetry_left_minus_right_p90_252d_d1}, 'f36_svas_311_stutzer_index_252d_d1': {'inputs': ['close'], 'func': f36_svas_311_stutzer_index_252d_d1}, 'f36_svas_312_stutzer_index_504d_d1': {'inputs': ['close'], 'func': f36_svas_312_stutzer_index_504d_d1}, 'f36_svas_313_stutzer_minus_sharpe_252d_d1': {'inputs': ['close'], 'func': f36_svas_313_stutzer_minus_sharpe_252d_d1}, 'f36_svas_314_bias_ratio_252d_d1': {'inputs': ['close'], 'func': f36_svas_314_bias_ratio_252d_d1}, 'f36_svas_315_bias_ratio_504d_d1': {'inputs': ['close'], 'func': f36_svas_315_bias_ratio_504d_d1}, 'f36_svas_316_bias_ratio_zscore_in_1260d_d1': {'inputs': ['close'], 'func': f36_svas_316_bias_ratio_zscore_in_1260d_d1}, 'f36_svas_317_modified_sharpe_5pct_252d_d1': {'inputs': ['close'], 'func': f36_svas_317_modified_sharpe_5pct_252d_d1}, 'f36_svas_318_modified_sharpe_1pct_252d_d1': {'inputs': ['close'], 'func': f36_svas_318_modified_sharpe_1pct_252d_d1}, 'f36_svas_319_modified_sharpe_5pct_504d_d1': {'inputs': ['close'], 'func': f36_svas_319_modified_sharpe_5pct_504d_d1}, 'f36_svas_320_modified_sharpe_minus_raw_sharpe_252d_d1': {'inputs': ['close'], 'func': f36_svas_320_modified_sharpe_minus_raw_sharpe_252d_d1}, 'f36_svas_321_corr_abs_r_with_r_252d_d1': {'inputs': ['close'], 'func': f36_svas_321_corr_abs_r_with_r_252d_d1}, 'f36_svas_322_corr_abs_r_with_r_504d_d1': {'inputs': ['close'], 'func': f36_svas_322_corr_abs_r_with_r_504d_d1}, 'f36_svas_323_corr_abs_r_with_r_zscore_in_1260d_d1': {'inputs': ['close'], 'func': f36_svas_323_corr_abs_r_with_r_zscore_in_1260d_d1}, 'f36_svas_324_corr_rsq_with_r_252d_d1': {'inputs': ['close'], 'func': f36_svas_324_corr_rsq_with_r_252d_d1}, 'f36_svas_325_skew_returns_in_drawdown_252d_d1': {'inputs': ['close'], 'func': f36_svas_325_skew_returns_in_drawdown_252d_d1}, 'f36_svas_326_skew_returns_at_new_highs_252d_d1': {'inputs': ['close'], 'func': f36_svas_326_skew_returns_at_new_highs_252d_d1}, 'f36_svas_327_skew_conditional_asymmetry_dd_vs_high_252d_d1': {'inputs': ['close'], 'func': f36_svas_327_skew_conditional_asymmetry_dd_vs_high_252d_d1}, 'f36_svas_328_kurt_returns_in_drawdown_252d_d1': {'inputs': ['close'], 'func': f36_svas_328_kurt_returns_in_drawdown_252d_d1}, 'f36_svas_329_mean_return_in_drawdown_252d_d1': {'inputs': ['close'], 'func': f36_svas_329_mean_return_in_drawdown_252d_d1}, 'f36_svas_330_frac_bars_dd_above_10pct_252d_d1': {'inputs': ['close'], 'func': f36_svas_330_frac_bars_dd_above_10pct_252d_d1}, 'f36_svas_331_frac_bars_dd_above_20pct_252d_d1': {'inputs': ['close'], 'func': f36_svas_331_frac_bars_dd_above_20pct_252d_d1}, 'f36_svas_332_frac_bars_dd_above_30pct_252d_d1': {'inputs': ['close'], 'func': f36_svas_332_frac_bars_dd_above_30pct_252d_d1}, 'f36_svas_333_frac_bars_dd_above_50pct_504d_d1': {'inputs': ['close'], 'func': f36_svas_333_frac_bars_dd_above_50pct_504d_d1}, 'f36_svas_334_count_distinct_dd_events_above_10pct_252d_d1': {'inputs': ['close'], 'func': f36_svas_334_count_distinct_dd_events_above_10pct_252d_d1}, 'f36_svas_335_count_distinct_dd_events_above_20pct_504d_d1': {'inputs': ['close'], 'func': f36_svas_335_count_distinct_dd_events_above_20pct_504d_d1}, 'f36_svas_336_dd_autocorr_lag1_252d_d1': {'inputs': ['close'], 'func': f36_svas_336_dd_autocorr_lag1_252d_d1}, 'f36_svas_337_dd_autocorr_lag5_252d_d1': {'inputs': ['close'], 'func': f36_svas_337_dd_autocorr_lag5_252d_d1}, 'f36_svas_338_dd_autocorr_lag63_504d_d1': {'inputs': ['close'], 'func': f36_svas_338_dd_autocorr_lag63_504d_d1}, 'f36_svas_339_dd_clustering_mean_event_gap_504d_d1': {'inputs': ['close'], 'func': f36_svas_339_dd_clustering_mean_event_gap_504d_d1}, 'f36_svas_340_recovery_median_duration_504d_d1': {'inputs': ['close'], 'func': f36_svas_340_recovery_median_duration_504d_d1}, 'f36_svas_341_recovery_max_duration_504d_d1': {'inputs': ['close'], 'func': f36_svas_341_recovery_max_duration_504d_d1}, 'f36_svas_342_recovery_std_duration_504d_d1': {'inputs': ['close'], 'func': f36_svas_342_recovery_std_duration_504d_d1}, 'f36_svas_343_recovery_skewness_504d_d1': {'inputs': ['close'], 'func': f36_svas_343_recovery_skewness_504d_d1}, 'f36_svas_344_recovery_count_504d_d1': {'inputs': ['close'], 'func': f36_svas_344_recovery_count_504d_d1}, 'f36_svas_345_worst_3d_return_in_252d_d1': {'inputs': ['close'], 'func': f36_svas_345_worst_3d_return_in_252d_d1}, 'f36_svas_346_worst_10d_return_in_252d_d1': {'inputs': ['close'], 'func': f36_svas_346_worst_10d_return_in_252d_d1}, 'f36_svas_347_worst_63d_return_in_252d_d1': {'inputs': ['close'], 'func': f36_svas_347_worst_63d_return_in_252d_d1}, 'f36_svas_348_worst_126d_return_in_504d_d1': {'inputs': ['close'], 'func': f36_svas_348_worst_126d_return_in_504d_d1}, 'f36_svas_349_worst_252d_return_in_504d_d1': {'inputs': ['close'], 'func': f36_svas_349_worst_252d_return_in_504d_d1}, 'f36_svas_350_current_drawdown_minus_worst_252d_return_ratio_d1': {'inputs': ['close'], 'func': f36_svas_350_current_drawdown_minus_worst_252d_return_ratio_d1}, 'f36_svas_351_cum_loss_during_current_loss_streak_d1': {'inputs': ['close'], 'func': f36_svas_351_cum_loss_during_current_loss_streak_d1}, 'f36_svas_352_max_streak_cum_loss_in_252d_d1': {'inputs': ['close'], 'func': f36_svas_352_max_streak_cum_loss_in_252d_d1}, 'f36_svas_353_mean_streak_cum_loss_in_252d_d1': {'inputs': ['close'], 'func': f36_svas_353_mean_streak_cum_loss_in_252d_d1}, 'f36_svas_354_count_loss_streaks_above_5pct_252d_d1': {'inputs': ['close'], 'func': f36_svas_354_count_loss_streaks_above_5pct_252d_d1}, 'f36_svas_355_loss_streak_severity_zscore_504d_d1': {'inputs': ['close'], 'func': f36_svas_355_loss_streak_severity_zscore_504d_d1}, 'f36_svas_356_dd_energy_squared_252d_d1': {'inputs': ['close'], 'func': f36_svas_356_dd_energy_squared_252d_d1}, 'f36_svas_357_dd_energy_cubed_252d_d1': {'inputs': ['close'], 'func': f36_svas_357_dd_energy_cubed_252d_d1}, 'f36_svas_358_dd_energy_squared_504d_d1': {'inputs': ['close'], 'func': f36_svas_358_dd_energy_squared_504d_d1}, 'f36_svas_359_log_dd_energy_squared_252d_d1': {'inputs': ['close'], 'func': f36_svas_359_log_dd_energy_squared_252d_d1}, 'f36_svas_360_hist_var_5pct_252d_d1': {'inputs': ['close'], 'func': f36_svas_360_hist_var_5pct_252d_d1}, 'f36_svas_361_parametric_var_5pct_252d_d1': {'inputs': ['close'], 'func': f36_svas_361_parametric_var_5pct_252d_d1}, 'f36_svas_362_hist_minus_parametric_var_5pct_252d_d1': {'inputs': ['close'], 'func': f36_svas_362_hist_minus_parametric_var_5pct_252d_d1}, 'f36_svas_363_hist_over_parametric_var_5pct_252d_d1': {'inputs': ['close'], 'func': f36_svas_363_hist_over_parametric_var_5pct_252d_d1}, 'f36_svas_364_tail_severity_full_composite_252d_d1': {'inputs': ['close'], 'func': f36_svas_364_tail_severity_full_composite_252d_d1}, 'f36_svas_365_chronic_dd_composite_504d_d1': {'inputs': ['close'], 'func': f36_svas_365_chronic_dd_composite_504d_d1}, 'f36_svas_366_recovery_failure_composite_504d_d1': {'inputs': ['close'], 'func': f36_svas_366_recovery_failure_composite_504d_d1}, 'f36_svas_367_loss_streak_severity_composite_252d_d1': {'inputs': ['close'], 'func': f36_svas_367_loss_streak_severity_composite_252d_d1}, 'f36_svas_368_non_normal_tail_composite_252d_d1': {'inputs': ['close'], 'func': f36_svas_368_non_normal_tail_composite_252d_d1}, 'f36_svas_369_dd_in_drawdown_distributional_composite_252d_d1': {'inputs': ['close'], 'func': f36_svas_369_dd_in_drawdown_distributional_composite_252d_d1}, 'f36_svas_370_worst_k_day_composite_252d_d1': {'inputs': ['close'], 'func': f36_svas_370_worst_k_day_composite_252d_d1}, 'f36_svas_371_dd_intensity_composite_504d_d1': {'inputs': ['close'], 'func': f36_svas_371_dd_intensity_composite_504d_d1}, 'f36_svas_372_corr_abs_r_negative_at_peak_indicator_d1': {'inputs': ['close'], 'func': f36_svas_372_corr_abs_r_negative_at_peak_indicator_d1}, 'f36_svas_373_modified_sharpe_at_peak_252d_d1': {'inputs': ['close'], 'func': f36_svas_373_modified_sharpe_at_peak_252d_d1}, 'f36_svas_374_p_dd_above_50pct_at_peak_504d_d1': {'inputs': ['close'], 'func': f36_svas_374_p_dd_above_50pct_at_peak_504d_d1}, 'f36_svas_375_stuck_peak_full_asymmetry_composite_504d_d1': {'inputs': ['close'], 'func': f36_svas_375_stuck_peak_full_asymmetry_composite_504d_d1}}