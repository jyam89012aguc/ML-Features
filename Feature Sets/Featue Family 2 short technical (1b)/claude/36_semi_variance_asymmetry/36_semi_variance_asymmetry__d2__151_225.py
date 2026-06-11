"""semi_variance_asymmetry d2 features 151-225 — Pipeline 1b-technical.

Gap-filling extension to family 36. 75 distinct hypotheses NOT covered by
the original 150 features. Sources for the canonical metrics added here:

  - Realized skewness / kurtosis: Amaya, Christoffersen, Jacobs, Vasquez 2015
    ("Does realized skewness predict the cross-section of equity returns?")
  - Calmar / Sterling / Burke / Pain / Martin ratios: Bacon, "Practical
    Portfolio Performance Measurement and Attribution"; PerformanceAnalytics R pkg
  - Ulcer Index: Peter Martin 1989
  - Omega ratio: Keating & Shadwick 2002
  - Cornish-Fisher VaR/ES: Cornish & Fisher 1937; Favre & Galeano 2002 "Modified VaR"
  - Hill estimator (EVT tail index): Hill 1975
  - Loss aversion / prospect theory: Kahneman & Tversky 1979 (kappa=2.25 standard)
  - Engle-Ng sign bias test: Engle & Ng 1993

Buckets in this file:
  QQ Realized skewness / kurtosis / semi-skew (151-158)
  RR Drawdown-based risk-adjusted ratios (159-167)
  SS Ulcer / Pain indices (168-173)
  TT Omega ratio (174-177)
  UU Cornish-Fisher VaR / ES (178-183)
  VV Hill estimator (EVT tail) (184-187)
  WW Drawdown duration / underwater / time-to-recovery (188-193)
  XX Loss-aversion / prospect-theory (194-197)
  YY Skewness term structure (198-202)
  ZZ Vol-conditional skewness (203-206)
  AB Multi-horizon hit ratio / win rate (207-210)
  AC Max consecutive loss days (additional horizons) (211-213)
  AD k-day rolling drawdown / runup (214-218)
  AE Engle-Ng sign / size bias test stats (219-222)
  AF Stuck-peak composites (223-225)

Inputs: SEP OHLCV only. PIT-clean: right-anchored, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers — no cross-
family imports.
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


def _neg_part(r: pd.Series) -> pd.Series:
    return r.where(r < 0, 0.0)


def _pos_part(r: pd.Series) -> pd.Series:
    return r.where(r > 0, 0.0)


def _when_neg(r: pd.Series) -> pd.Series:
    return r.where(r < 0)


def _when_pos(r: pd.Series) -> pd.Series:
    return r.where(r > 0)


# ============================================================
# Bucket QQ — Realized skewness / kurtosis (Amaya et al. 2015) (151-158)
# RSk = sqrt(N) * sum(r^3) / RV^(3/2); RKt = N * sum(r^4) / RV^2.
# These differ from sample skew/kurt (already in 33-36, 49-52) because
# they are *high-frequency moments* scaled by RV — a different quantity
# with a different signal interpretation (cross-sectional return predictor).
# ============================================================

def _realized_skewness(r: pd.Series, n: int, mp: int) -> pd.Series:
    rv = (r ** 2).rolling(n, min_periods=mp).sum()
    s3 = (r ** 3).rolling(n, min_periods=mp).sum()
    return _safe_div(np.sqrt(float(n)) * s3, rv ** 1.5)


def _realized_kurtosis(r: pd.Series, n: int, mp: int) -> pd.Series:
    rv = (r ** 2).rolling(n, min_periods=mp).sum()
    s4 = (r ** 4).rolling(n, min_periods=mp).sum()
    return _safe_div(float(n) * s4, rv ** 2)


def f36_svas_151_realized_skewness_21d(close: pd.Series) -> pd.Series:
    """Realized skewness sqrt(N)*sum(r^3)/RV^1.5 at 21d (Amaya-Christoffersen-Jacobs-Vasquez 2015) — monthly RV-scaled skew."""
    r = _log_returns(close)
    return _realized_skewness(r, MDAYS, WDAYS)


def f36_svas_152_realized_skewness_63d(close: pd.Series) -> pd.Series:
    """Realized skewness at 63d — quarterly RV-scaled skew."""
    r = _log_returns(close)
    return _realized_skewness(r, QDAYS, MDAYS)


def f36_svas_153_realized_skewness_252d(close: pd.Series) -> pd.Series:
    """Realized skewness at 252d — annual RV-scaled skew."""
    r = _log_returns(close)
    return _realized_skewness(r, YDAYS, QDAYS)


def f36_svas_154_realized_kurtosis_21d(close: pd.Series) -> pd.Series:
    """Realized kurtosis N*sum(r^4)/RV^2 at 21d — monthly RV-scaled kurt."""
    r = _log_returns(close)
    return _realized_kurtosis(r, MDAYS, WDAYS)


def f36_svas_155_realized_kurtosis_63d(close: pd.Series) -> pd.Series:
    """Realized kurtosis at 63d — quarterly RV-scaled kurt."""
    r = _log_returns(close)
    return _realized_kurtosis(r, QDAYS, MDAYS)


def f36_svas_156_realized_kurtosis_252d(close: pd.Series) -> pd.Series:
    """Realized kurtosis at 252d — annual RV-scaled kurt."""
    r = _log_returns(close)
    return _realized_kurtosis(r, YDAYS, QDAYS)


def f36_svas_157_realized_semi_skewness_pos_252d(close: pd.Series) -> pd.Series:
    """sqrt(N)*sum(r^3 | r>0)/RV^1.5 at 252d — positive-half realized skewness contribution."""
    r = _log_returns(close)
    rv = (r ** 2).rolling(YDAYS, min_periods=QDAYS).sum()
    s3p = ((r ** 3).where(r > 0, 0.0)).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(np.sqrt(float(YDAYS)) * s3p, rv ** 1.5)


def f36_svas_158_realized_semi_skewness_neg_252d(close: pd.Series) -> pd.Series:
    """sqrt(N)*sum(r^3 | r<0)/RV^1.5 at 252d — negative-half realized skewness contribution (sign preserved)."""
    r = _log_returns(close)
    rv = (r ** 2).rolling(YDAYS, min_periods=QDAYS).sum()
    s3n = ((r ** 3).where(r < 0, 0.0)).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(np.sqrt(float(YDAYS)) * s3n, rv ** 1.5)


# ============================================================
# Bucket RR — Drawdown-based risk-adjusted ratios (159-167)
# Standard formulas. All computed on the PRICE close (cum-product of
# 1+ret), with the rolling max as the peak. Annualization uses 252.
# ============================================================

def _max_drawdown_from_close(close: pd.Series, n: int, mp: int) -> pd.Series:
    """Max drawdown (negative number, e.g., -0.4) over trailing n bars of close."""
    def _mdd(w):
        v = w[~np.isnan(w)]
        if v.size < 5:
            return np.nan
        peak = np.maximum.accumulate(v)
        dd = v / peak - 1.0
        return float(dd.min())
    return close.rolling(n, min_periods=mp).apply(_mdd, raw=True)


def _annualized_return(close: pd.Series, n: int, mp: int) -> pd.Series:
    """Annualized log return over trailing n bars (sum log returns * 252/n)."""
    r = _log_returns(close)
    return r.rolling(n, min_periods=mp).sum() * (252.0 / float(n))


def f36_svas_159_calmar_ratio_252d(close: pd.Series) -> pd.Series:
    """Annualized return / |max drawdown| over 252d — classical Calmar ratio (1y window)."""
    ann_ret = _annualized_return(close, YDAYS, QDAYS)
    mdd = _max_drawdown_from_close(close, YDAYS, QDAYS)
    return _safe_div(ann_ret, mdd.abs())


def f36_svas_160_calmar_ratio_504d(close: pd.Series) -> pd.Series:
    """Annualized return / |max drawdown| over 504d — 2y Calmar ratio."""
    ann_ret = _annualized_return(close, DDAYS_2Y, YDAYS)
    mdd = _max_drawdown_from_close(close, DDAYS_2Y, YDAYS)
    return _safe_div(ann_ret, mdd.abs())


def f36_svas_161_sterling_ratio_252d(close: pd.Series) -> pd.Series:
    """Annualized return / (|max DD| + 0.10) at 252d — Sterling ratio (Deane Sterling Jones original)."""
    ann_ret = _annualized_return(close, YDAYS, QDAYS)
    mdd = _max_drawdown_from_close(close, YDAYS, QDAYS)
    return _safe_div(ann_ret, mdd.abs() + 0.10)


def f36_svas_162_burke_ratio_252d(close: pd.Series) -> pd.Series:
    """Annualized return / sqrt(sum(DD_i^2)) over 252d — Burke ratio; less outlier-sensitive than Sterling."""
    ann_ret = _annualized_return(close, YDAYS, QDAYS)
    def _burke_den(w):
        v = w[~np.isnan(w)]
        if v.size < 21:
            return np.nan
        peak = np.maximum.accumulate(v)
        dd = v / peak - 1.0   # <= 0
        # use the worst 5 drawdowns (or all drawdowns if fewer than 5)
        worst = np.sort(dd)[:max(5, dd.size // 20)]
        return float(np.sqrt((worst ** 2).sum()))
    den = close.rolling(YDAYS, min_periods=QDAYS).apply(_burke_den, raw=True)
    return _safe_div(ann_ret, den)


def f36_svas_163_pain_ratio_252d(close: pd.Series) -> pd.Series:
    """Annualized return / mean drawdown depth (Pain index) over 252d — Becker pain ratio."""
    ann_ret = _annualized_return(close, YDAYS, QDAYS)
    def _pain_idx(w):
        v = w[~np.isnan(w)]
        if v.size < 21:
            return np.nan
        peak = np.maximum.accumulate(v)
        dd = 1.0 - v / peak   # >= 0
        return float(dd.mean())
    pain = close.rolling(YDAYS, min_periods=QDAYS).apply(_pain_idx, raw=True)
    return _safe_div(ann_ret, pain)


def f36_svas_164_martin_ratio_252d(close: pd.Series) -> pd.Series:
    """Annualized return / Ulcer index over 252d — Martin ratio (uses sqrt(mean(DD^2)) denominator)."""
    ann_ret = _annualized_return(close, YDAYS, QDAYS)
    def _ulcer(w):
        v = w[~np.isnan(w)]
        if v.size < 21:
            return np.nan
        peak = np.maximum.accumulate(v)
        dd = 1.0 - v / peak
        return float(np.sqrt((dd ** 2).mean()))
    uic = close.rolling(YDAYS, min_periods=QDAYS).apply(_ulcer, raw=True)
    return _safe_div(ann_ret, uic)


def f36_svas_165_log_calmar_ratio_252d(close: pd.Series) -> pd.Series:
    """log(ann ret + 1) / log(|max DD| + 1) over 252d — symmetric-scale Calmar form."""
    ann_ret = _annualized_return(close, YDAYS, QDAYS)
    mdd = _max_drawdown_from_close(close, YDAYS, QDAYS)
    return _safe_div(np.log1p(ann_ret), np.log1p(mdd.abs()))


def f36_svas_166_calmar_ratio_1260d(close: pd.Series) -> pd.Series:
    """Annualized return / |max DD| over 1260d (5y) — long-horizon Calmar ratio."""
    ann_ret = _annualized_return(close, DDAYS_5Y, DDAYS_2Y)
    mdd = _max_drawdown_from_close(close, DDAYS_5Y, DDAYS_2Y)
    return _safe_div(ann_ret, mdd.abs())


def f36_svas_167_sterling_ratio_504d(close: pd.Series) -> pd.Series:
    """Annualized return / (|max DD| + 0.10) at 504d — biennial Sterling ratio."""
    ann_ret = _annualized_return(close, DDAYS_2Y, YDAYS)
    mdd = _max_drawdown_from_close(close, DDAYS_2Y, YDAYS)
    return _safe_div(ann_ret, mdd.abs() + 0.10)


# ============================================================
# Bucket SS — Ulcer / Pain indices (168-173)
# Ulcer index = sqrt(mean(DD^2)) where DD = 1 - close/running_max (>= 0).
# Pain index  = mean(DD).
# ============================================================

def _ulcer_index_window(w: np.ndarray) -> float:
    v = w[~np.isnan(w)]
    if v.size < 21:
        return np.nan
    peak = np.maximum.accumulate(v)
    dd = 1.0 - v / peak
    return float(np.sqrt((dd ** 2).mean()))


def _pain_index_window(w: np.ndarray) -> float:
    v = w[~np.isnan(w)]
    if v.size < 21:
        return np.nan
    peak = np.maximum.accumulate(v)
    dd = 1.0 - v / peak
    return float(dd.mean())


def f36_svas_168_ulcer_index_252d(close: pd.Series) -> pd.Series:
    """Ulcer index (Martin 1989) over 252d — sqrt of mean squared drawdown depth."""
    return close.rolling(YDAYS, min_periods=QDAYS).apply(_ulcer_index_window, raw=True)


def f36_svas_169_ulcer_index_504d(close: pd.Series) -> pd.Series:
    """Ulcer index over 504d — biennial DD-severity-and-duration metric."""
    return close.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_ulcer_index_window, raw=True)


def f36_svas_170_pain_index_252d(close: pd.Series) -> pd.Series:
    """Pain index over 252d — mean drawdown depth (Becker)."""
    return close.rolling(YDAYS, min_periods=QDAYS).apply(_pain_index_window, raw=True)


def f36_svas_171_pain_index_504d(close: pd.Series) -> pd.Series:
    """Pain index over 504d — biennial mean drawdown depth."""
    return close.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_pain_index_window, raw=True)


def f36_svas_172_max_single_drawdown_pct_252d(close: pd.Series) -> pd.Series:
    """Max drawdown (positive percent depth) over 252d — computed on close, not log returns; distinct from 109."""
    return _max_drawdown_from_close(close, YDAYS, QDAYS).abs()


def f36_svas_173_mean_drawdown_at_troughs_252d(close: pd.Series) -> pd.Series:
    """Mean drawdown depth measured only at local troughs in 252d — typical trough magnitude (distinct from Pain index, which averages every bar)."""
    def _mean_trough_dd(w):
        v = w[~np.isnan(w)]
        if v.size < 21:
            return np.nan
        peak = np.maximum.accumulate(v)
        dd = 1.0 - v / peak   # >= 0
        # local troughs: dd[i] > dd[i-1] and dd[i] >= dd[i+1]
        troughs = []
        for i in range(1, len(dd) - 1):
            if dd[i] > dd[i - 1] and dd[i] >= dd[i + 1] and dd[i] > 0:
                troughs.append(dd[i])
        # boundary trough
        if len(dd) >= 2 and dd[-1] > dd[-2] and dd[-1] > 0:
            troughs.append(dd[-1])
        return float(np.mean(troughs)) if troughs else 0.0
    return close.rolling(YDAYS, min_periods=QDAYS).apply(_mean_trough_dd, raw=True)


# ============================================================
# Bucket TT — Omega ratio (174-177)
# Omega(theta) = E[max(r-theta, 0)] / E[max(theta-r, 0)] — probability-
# weighted gain/loss ratio above threshold theta.
# ============================================================

def _omega_window(w: np.ndarray, theta: float) -> float:
    v = w[~np.isnan(w)]
    if v.size < 21:
        return np.nan
    g = np.maximum(v - theta, 0.0).mean()
    l = np.maximum(theta - v, 0.0).mean()
    if l <= 0:
        return np.nan
    return float(g / l)


def f36_svas_174_omega_ratio_theta0_252d(close: pd.Series) -> pd.Series:
    """Omega ratio at threshold theta=0 over 252d — gain-vs-loss area ratio at zero (Keating-Shadwick 2002)."""
    r = _log_returns(close)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _omega_window(w, 0.0), raw=True)


def f36_svas_175_omega_ratio_theta0_504d(close: pd.Series) -> pd.Series:
    """Omega ratio at theta=0 over 504d — biennial Omega."""
    r = _log_returns(close)
    return r.rolling(DDAYS_2Y, min_periods=YDAYS).apply(lambda w: _omega_window(w, 0.0), raw=True)


def f36_svas_176_omega_ratio_theta_rf_2pct_252d(close: pd.Series) -> pd.Series:
    """Omega ratio at theta = 2%/year per-day (log(1.02)/252) over 252d — risk-free-threshold Omega."""
    r = _log_returns(close)
    theta = np.log(1.02) / 252.0
    return r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _omega_window(w, theta), raw=True)


def f36_svas_177_log_omega_ratio_theta0_252d(close: pd.Series) -> pd.Series:
    """log(Omega ratio at theta=0) over 252d — symmetric scale, 0 = balanced."""
    r = _log_returns(close)
    omega = r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _omega_window(w, 0.0), raw=True)
    return np.log(omega.where(omega > 0, np.nan))


# ============================================================
# Bucket UU — Cornish-Fisher VaR / ES (178-183)
# CF: tail quantile adjusted for skew (S) and excess kurtosis (K):
# z_cf = z + (z^2 - 1)*S/6 + (z^3 - 3z)*K/24 - (2z^3 - 5z)*S^2/36
# VaR_cf = mean + z_cf * sigma. ES analog: take CF of conditional mean of tail.
# ============================================================

def _cf_quantile(z: float, S: float, K: float) -> float:
    """Cornish-Fisher adjusted standard-normal quantile (S=sample skew, K=excess kurt)."""
    return z + (z * z - 1.0) * S / 6.0 + (z ** 3 - 3.0 * z) * K / 24.0 - (2.0 * z ** 3 - 5.0 * z) * (S ** 2) / 36.0


def _cf_var_window(w: np.ndarray, alpha: float) -> float:
    """Cornish-Fisher VaR at lower-tail probability alpha."""
    v = w[~np.isnan(w)]
    if v.size < 30:
        return np.nan
    mu = v.mean(); sd = v.std(ddof=1)
    if sd == 0:
        return np.nan
    # sample skew (g1) and excess kurt (g2)
    cm3 = ((v - mu) ** 3).mean()
    cm4 = ((v - mu) ** 4).mean()
    S = cm3 / (sd ** 3)
    K = cm4 / (sd ** 4) - 3.0
    # standard-normal lower-tail quantile
    z = _norm_ppf(alpha)
    z_cf = _cf_quantile(z, S, K)
    return float(mu + z_cf * sd)


def _norm_ppf(p: float) -> float:
    """Beasley-Springer-Moro inverse normal CDF approximation (good to 5e-7)."""
    # Coefficients from Acklam's algorithm (well-known)
    if p <= 0.0 or p >= 1.0:
        return float('nan')
    a = [-3.969683028665376e+01, 2.209460984245205e+02, -2.759285104469687e+02,
         1.383577518672690e+02, -3.066479806614716e+01, 2.506628277459239e+00]
    b = [-5.447609879822406e+01, 1.615858368580409e+02, -1.556989798598866e+02,
         6.680131188771972e+01, -1.328068155288572e+01]
    c = [-7.784894002430293e-03, -3.223964580411365e-01, -2.400758277161838e+00,
         -2.549732539343734e+00, 4.374664141464968e+00, 2.938163982698783e+00]
    d = [7.784695709041462e-03, 3.224671290700398e-01, 2.445134137142996e+00,
         3.754408661907416e+00]
    plow = 0.02425
    phigh = 1 - plow
    if p < plow:
        q = np.sqrt(-2 * np.log(p))
        return float((((((c[0] * q + c[1]) * q + c[2]) * q + c[3]) * q + c[4]) * q + c[5]) /
                     ((((d[0] * q + d[1]) * q + d[2]) * q + d[3]) * q + 1))
    if p <= phigh:
        q = p - 0.5
        r2 = q * q
        return float((((((a[0] * r2 + a[1]) * r2 + a[2]) * r2 + a[3]) * r2 + a[4]) * r2 + a[5]) * q /
                     (((((b[0] * r2 + b[1]) * r2 + b[2]) * r2 + b[3]) * r2 + b[4]) * r2 + 1))
    q = np.sqrt(-2 * np.log(1 - p))
    return float(-(((((c[0] * q + c[1]) * q + c[2]) * q + c[3]) * q + c[4]) * q + c[5]) /
                 ((((d[0] * q + d[1]) * q + d[2]) * q + d[3]) * q + 1))


def f36_svas_178_cornish_fisher_var_5pct_252d(close: pd.Series) -> pd.Series:
    """Cornish-Fisher VaR at 5% lower tail over 252d — skew/kurt-adjusted parametric VaR."""
    r = _log_returns(close)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _cf_var_window(w, 0.05), raw=True)


def f36_svas_179_cornish_fisher_var_1pct_252d(close: pd.Series) -> pd.Series:
    """Cornish-Fisher VaR at 1% lower tail over 252d — deep-tail CF VaR."""
    r = _log_returns(close)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _cf_var_window(w, 0.01), raw=True)


def f36_svas_180_cornish_fisher_es_5pct_252d(close: pd.Series) -> pd.Series:
    """CF-ES at 5%: mean of returns <= CF VaR(0.05) over 252d — skew/kurt-aware tail expectation."""
    r = _log_returns(close)
    def _cf_es(w):
        cf = _cf_var_window(w, 0.05)
        if np.isnan(cf):
            return np.nan
        v = w[~np.isnan(w)]
        tail = v[v <= cf]
        return float(tail.mean()) if tail.size else np.nan
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_cf_es, raw=True)


def f36_svas_181_cf_var_minus_parametric_var_5pct_252d(close: pd.Series) -> pd.Series:
    """CF VaR(5%) - parametric VaR(5%) over 252d — pure skew/kurt adjustment magnitude (negative = CF deeper)."""
    r = _log_returns(close)
    def _delta(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        mu = v.mean(); sd = v.std(ddof=1)
        if sd == 0:
            return np.nan
        cm3 = ((v - mu) ** 3).mean(); cm4 = ((v - mu) ** 4).mean()
        S = cm3 / sd ** 3; K = cm4 / sd ** 4 - 3.0
        z = _norm_ppf(0.05)
        z_cf = _cf_quantile(z, S, K)
        return float((mu + z_cf * sd) - (mu + z * sd))
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_delta, raw=True)


def f36_svas_182_cornish_fisher_var_5pct_504d(close: pd.Series) -> pd.Series:
    """CF VaR(5%) over 504d — biennial skew/kurt-adjusted tail."""
    r = _log_returns(close)
    return r.rolling(DDAYS_2Y, min_periods=YDAYS).apply(lambda w: _cf_var_window(w, 0.05), raw=True)


def f36_svas_183_cornish_fisher_var_5pct_21d(close: pd.Series) -> pd.Series:
    """CF VaR(5%) over 21d — short-horizon CF VaR (fragile but fast-reacting)."""
    r = _log_returns(close)
    return r.rolling(MDAYS, min_periods=WDAYS).apply(lambda w: _cf_var_window(w, 0.05), raw=True)


# ============================================================
# Bucket VV — Hill estimator (EVT tail index) (184-187)
# Hill 1975: alpha_hat = 1 / (mean of log(X_k/X_{k+1})) for top-k order
# statistics. Smaller alpha = heavier tail.
# ============================================================

def _hill_estimator(w: np.ndarray, side: str = "left", k_frac: float = 0.10) -> float:
    """Hill estimator on the chosen tail. side='left' uses |r| restricted to r<0; side='right' uses r restricted to r>0."""
    v = w[~np.isnan(w)]
    if v.size < 30:
        return np.nan
    if side == "left":
        tail = -v[v < 0]   # positive magnitudes of negative returns
    else:
        tail = v[v > 0]
    if tail.size < 10:
        return np.nan
    tail = np.sort(tail)[::-1]   # descending
    k = max(2, int(tail.size * k_frac))
    if tail[k] <= 0:
        return np.nan
    # alpha = 1 / (mean of log(X_i / X_{k+1}) for i=1..k)
    logs = np.log(tail[:k] / tail[k])
    m = logs.mean()
    if m == 0:
        return np.nan
    return float(1.0 / m)


def f36_svas_184_hill_estimator_left_tail_10pct_252d(close: pd.Series) -> pd.Series:
    """Hill estimator (k=10% of sample) on left tail of returns over 252d — lower alpha = heavier loss tail."""
    r = _log_returns(close)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _hill_estimator(w, "left", 0.10), raw=True)


def f36_svas_185_hill_estimator_right_tail_10pct_252d(close: pd.Series) -> pd.Series:
    """Hill estimator (k=10%) on right tail over 252d — lower alpha = heavier gain tail."""
    r = _log_returns(close)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _hill_estimator(w, "right", 0.10), raw=True)


def f36_svas_186_hill_left_minus_right_252d(close: pd.Series) -> pd.Series:
    """Hill(left) - Hill(right) at 252d — additive tail-index asymmetry; negative = left tail heavier."""
    r = _log_returns(close)
    hl = r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _hill_estimator(w, "left", 0.10), raw=True)
    hr = r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _hill_estimator(w, "right", 0.10), raw=True)
    return hl - hr


def f36_svas_187_hill_left_over_right_252d(close: pd.Series) -> pd.Series:
    """Hill(left) / Hill(right) at 252d — ratio form of tail-index asymmetry."""
    r = _log_returns(close)
    hl = r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _hill_estimator(w, "left", 0.10), raw=True)
    hr = r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _hill_estimator(w, "right", 0.10), raw=True)
    return _safe_div(hl, hr)


# ============================================================
# Bucket WW — Drawdown duration / underwater / time-to-recovery (188-193)
# Critical for "stuck" peak detection: a stock that touches -80% and stays
# down is the *target* of this whole pipeline. These features directly
# encode "how long has it been below its peak" and "how long was the
# typical drawdown".
# ============================================================

def f36_svas_188_current_drawdown_duration(close: pd.Series) -> pd.Series:
    """Bars since the most recent expanding-window running-max of close — current underwater duration."""
    arr = close.values
    n = arr.size
    out = np.full(n, np.nan, dtype=float)
    cur_max = -np.inf
    cur_max_idx = -1
    for i in range(n):
        v = arr[i]
        if np.isnan(v):
            continue
        if v >= cur_max:
            cur_max = v
            cur_max_idx = i
        if cur_max_idx >= 0:
            out[i] = float(i - cur_max_idx)
    return pd.Series(out, index=close.index)


def f36_svas_189_mean_drawdown_duration_252d(close: pd.Series) -> pd.Series:
    """Mean drawdown duration (bars per peak-to-peak excursion) over trailing 252d."""
    def _mdd_dur(w):
        v = w[~np.isnan(w)]
        if v.size < 21:
            return np.nan
        peak_idx = -1
        durations = []
        cur_dur = 0
        cur_max = -np.inf
        for i, x in enumerate(v):
            if x >= cur_max:
                if cur_dur > 0:
                    durations.append(cur_dur)
                cur_max = x
                cur_dur = 0
            else:
                cur_dur += 1
        if cur_dur > 0:
            durations.append(cur_dur)
        return float(np.mean(durations)) if durations else 0.0
    return close.rolling(YDAYS, min_periods=QDAYS).apply(_mdd_dur, raw=True)


def f36_svas_190_max_drawdown_duration_252d(close: pd.Series) -> pd.Series:
    """Max drawdown duration (longest underwater stretch in bars) over 252d."""
    def _max_dur(w):
        v = w[~np.isnan(w)]
        if v.size < 21:
            return np.nan
        best = 0
        cur_dur = 0
        cur_max = -np.inf
        for x in v:
            if x >= cur_max:
                if cur_dur > best:
                    best = cur_dur
                cur_max = x
                cur_dur = 0
            else:
                cur_dur += 1
        if cur_dur > best:
            best = cur_dur
        return float(best)
    return close.rolling(YDAYS, min_periods=QDAYS).apply(_max_dur, raw=True)


def f36_svas_191_underwater_fraction_252d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 252d bars where close < trailing-window expanding max — time spent underwater."""
    def _uw(w):
        v = w[~np.isnan(w)]
        if v.size < 21:
            return np.nan
        peak = np.maximum.accumulate(v)
        return float((v < peak).sum() / v.size)
    return close.rolling(YDAYS, min_periods=QDAYS).apply(_uw, raw=True)


def f36_svas_192_underwater_fraction_504d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 504d underwater — biennial underwater share."""
    def _uw(w):
        v = w[~np.isnan(w)]
        if v.size < 21:
            return np.nan
        peak = np.maximum.accumulate(v)
        return float((v < peak).sum() / v.size)
    return close.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_uw, raw=True)


def f36_svas_193_time_to_recovery_last_drawdown_504d(close: pd.Series) -> pd.Series:
    """For the most recent COMPLETED drawdown in trailing 504d, the # bars from trough to recovery (peak retake)."""
    def _ttr(w):
        v = w[~np.isnan(w)]
        if v.size < 21:
            return np.nan
        peak = np.maximum.accumulate(v)
        dd = 1.0 - v / peak
        # find drawdowns: contiguous segments where dd>0
        segments = []
        i = 0
        while i < len(dd):
            if dd[i] > 0:
                j = i
                while j < len(dd) and dd[j] > 0:
                    j += 1
                # trough_idx within [i, j-1]
                trough = i + int(np.argmax(dd[i:j]))
                # recovery bar = j (if j < len) else not recovered
                if j < len(dd):
                    segments.append((trough, j))
                i = j
            else:
                i += 1
        if not segments:
            return 0.0
        # most recent COMPLETED
        trough, recovery = segments[-1]
        return float(recovery - trough)
    return close.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_ttr, raw=True)


# ============================================================
# Bucket XX — Loss-aversion / prospect-theory (194-197)
# Kahneman-Tversky 1979: utility is concave for gains (v(x) = x^0.88),
# convex for losses (v(x) = -2.25 * |x|^0.88). Decision weights are
# inverse-S transformed probabilities.
# ============================================================

KT_ALPHA = 0.88
KT_LAMBDA = 2.25


def f36_svas_194_loss_aversion_ratio_252d(close: pd.Series) -> pd.Series:
    """P(gain)*E[gain] - 2.25*P(loss)*E[|loss|] over 252d — prospect-theory net expected utility (KT lambda=2.25)."""
    r = _log_returns(close)
    pu = (r > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    pl = (r < 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    g = _when_pos(r).rolling(YDAYS, min_periods=QDAYS).mean()
    l = (-_when_neg(r)).rolling(YDAYS, min_periods=QDAYS).mean()
    return pu * g - KT_LAMBDA * pl * l


def f36_svas_195_prospect_theory_utility_252d(close: pd.Series) -> pd.Series:
    """Mean of KT utility v(r) = sign(r)*|r|^0.88 for r>0, -2.25*|r|^0.88 for r<0, over 252d."""
    r = _log_returns(close)
    util = np.where(r > 0, r ** KT_ALPHA, -KT_LAMBDA * (-r.where(r <= 0, 0.0)) ** KT_ALPHA)
    return pd.Series(util, index=close.index).rolling(YDAYS, min_periods=QDAYS).mean()


def f36_svas_196_inverse_s_weight_asymmetry_252d(close: pd.Series) -> pd.Series:
    """Tversky-Kahneman 1992 inverse-S decision weights: w(P)=P^delta/(P^delta+(1-P)^delta)^(1/delta).
    Compute w(P(gain)) with delta=0.61 minus w(P(loss)) with delta=0.69 over 252d — inverse-S weight asymmetry."""
    r = _log_returns(close)
    pu = (r > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    pl = (r < 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    def _w(p, d):
        return p ** d / ((p ** d + (1.0 - p) ** d) ** (1.0 / d))
    return _w(pu, 0.61) - _w(pl, 0.69)


def f36_svas_197_loss_aversion_zscore_504d(close: pd.Series) -> pd.Series:
    """Z-score (over 504d) of the 252d loss-aversion ratio — regime-relative prospect-theory deficit."""
    r = _log_returns(close)
    pu = (r > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    pl = (r < 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    g = _when_pos(r).rolling(YDAYS, min_periods=QDAYS).mean()
    l = (-_when_neg(r)).rolling(YDAYS, min_periods=QDAYS).mean()
    la = pu * g - KT_LAMBDA * pl * l
    return _rolling_zscore(la, DDAYS_2Y, min_periods=YDAYS)


# ============================================================
# Bucket YY — Skewness term structure (198-202)
# Skew at multiple horizons fit to a line/quadratic vs log(horizon).
# ============================================================

def _skew_term_struct_fit(close: pd.Series, hzs: list, lookup: dict, kind: str) -> pd.Series:
    """Fit skew(hz) vs log(hz) and return slope / intercept / R^2 / curvature according to `kind`.
    `lookup` maps each hz to a precomputed rolling-skew Series."""
    sks = [lookup[h] for h in hzs]
    xs = np.log(np.array(hzs, dtype=float))
    # Build a per-bar 4-vector, then linear regression.
    df = pd.concat([s.rename(f"hz{h}") for s, h in zip(sks, hzs)], axis=1)
    def _fit(row):
        y = row.values
        if np.isnan(y).any():
            return np.nan
        x = xs
        xm = x.mean(); ym = y.mean()
        num = ((x - xm) * (y - ym)).sum()
        den = ((x - xm) ** 2).sum()
        if den == 0:
            return np.nan
        b = num / den
        a = ym - b * xm
        if kind == "slope":
            return float(b)
        if kind == "intercept":
            return float(a)
        if kind == "r2":
            yhat = a + b * x
            ssr = ((y - yhat) ** 2).sum()
            sst = ((y - ym) ** 2).sum()
            if sst == 0:
                return np.nan
            return float(1.0 - ssr / sst)
        if kind == "curvature":
            # second-difference of skew across horizons (proxy for quadratic curvature)
            if len(y) < 3:
                return np.nan
            return float(y[-1] - 2.0 * y[len(y) // 2] + y[0])
        return np.nan
    return df.apply(_fit, axis=1)


def _skew_lookup(close: pd.Series, hzs):
    r = _log_returns(close)
    return {h: r.rolling(h, min_periods=max(h // 3, WDAYS)).skew() for h in hzs}


def f36_svas_198_skew_term_structure_slope_3pt(close: pd.Series) -> pd.Series:
    """Slope of skew vs log(horizon) over horizons {21, 63, 252} — 3-point term-structure slope."""
    hzs = [21, 63, 252]
    return _skew_term_struct_fit(close, hzs, _skew_lookup(close, hzs), "slope")


def f36_svas_199_skew_term_structure_curvature_3pt(close: pd.Series) -> pd.Series:
    """Second-difference curvature of skew across horizons {21, 63, 252} — 3-point curvature."""
    hzs = [21, 63, 252]
    return _skew_term_struct_fit(close, hzs, _skew_lookup(close, hzs), "curvature")


def f36_svas_200_skew_term_structure_slope_4pt(close: pd.Series) -> pd.Series:
    """Slope of skew vs log(horizon) over {5, 21, 63, 252} — 4-point term-structure slope."""
    hzs = [5, 21, 63, 252]
    return _skew_term_struct_fit(close, hzs, _skew_lookup(close, hzs), "slope")


def f36_svas_201_skew_term_structure_intercept_4pt(close: pd.Series) -> pd.Series:
    """Intercept of skew-vs-log(horizon) regression over {5, 21, 63, 252} — extrapolated short-horizon skew."""
    hzs = [5, 21, 63, 252]
    return _skew_term_struct_fit(close, hzs, _skew_lookup(close, hzs), "intercept")


def f36_svas_202_skew_term_structure_r2_4pt(close: pd.Series) -> pd.Series:
    """R^2 of skew-vs-log(horizon) regression over {5, 21, 63, 252} — how well does skew obey a log-horizon line."""
    hzs = [5, 21, 63, 252]
    return _skew_term_struct_fit(close, hzs, _skew_lookup(close, hzs), "r2")


# ============================================================
# Bucket ZZ — Vol-conditional skewness (203-206)
# Skew computed on subsets of returns conditioned on vol-regime state.
# ============================================================

def _skew_on_subset(r: pd.Series, mask: pd.Series, n: int, mp: int) -> pd.Series:
    """Rolling skew of r restricted to bars where mask is True."""
    rs = r.where(mask)
    def _sk(w):
        v = w[~np.isnan(w)]
        if v.size < 10:
            return np.nan
        m = v.mean(); s = v.std(ddof=1)
        if s == 0:
            return np.nan
        return float(((v - m) ** 3).mean() / s ** 3)
    return rs.rolling(n, min_periods=mp).apply(_sk, raw=True)


def f36_svas_203_skew_in_high_vol_regime_252d(close: pd.Series) -> pd.Series:
    """Skewness of returns on bars where RV21 > median(RV21)_504d, over 252d — high-vol-regime conditional skew."""
    r = _log_returns(close)
    rv21 = r.rolling(MDAYS, min_periods=WDAYS).std()
    med = rv21.rolling(DDAYS_2Y, min_periods=YDAYS).median()
    mask = rv21 > med
    return _skew_on_subset(r, mask, YDAYS, QDAYS)


def f36_svas_204_skew_in_low_vol_regime_252d(close: pd.Series) -> pd.Series:
    """Skewness of returns on bars where RV21 <= median(RV21)_504d, over 252d — low-vol-regime conditional skew."""
    r = _log_returns(close)
    rv21 = r.rolling(MDAYS, min_periods=WDAYS).std()
    med = rv21.rolling(DDAYS_2Y, min_periods=YDAYS).median()
    mask = rv21 <= med
    return _skew_on_subset(r, mask, YDAYS, QDAYS)


def f36_svas_205_conditional_skew_asymmetry_high_low_252d(close: pd.Series) -> pd.Series:
    """skew(high-vol days) - skew(low-vol days) at 252d — additive vol-regime-conditional skew asymmetry."""
    r = _log_returns(close)
    rv21 = r.rolling(MDAYS, min_periods=WDAYS).std()
    med = rv21.rolling(DDAYS_2Y, min_periods=YDAYS).median()
    hi = _skew_on_subset(r, rv21 > med, YDAYS, QDAYS)
    lo = _skew_on_subset(r, rv21 <= med, YDAYS, QDAYS)
    return hi - lo


def f36_svas_206_skew_in_top_quintile_vol_252d(close: pd.Series) -> pd.Series:
    """Skewness of returns on bars where RV21 in top quintile (>p80) of 504d, over 252d — extreme-vol-regime skew."""
    r = _log_returns(close)
    rv21 = r.rolling(MDAYS, min_periods=WDAYS).std()
    q80 = rv21.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.80)
    mask = rv21 > q80
    return _skew_on_subset(r, mask, YDAYS, QDAYS)


# ============================================================
# Bucket AB — Multi-horizon hit ratio / win rate (207-210)
# (Family already has up_fraction at 252d; these add 21d, 63d, 504d, +
#  a regime-relative z-score.)
# ============================================================

def f36_svas_207_up_fraction_21d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 21d with positive return — short-horizon win rate."""
    r = _log_returns(close)
    return (r > 0).astype(float).rolling(MDAYS, min_periods=WDAYS).mean()


def f36_svas_208_up_fraction_63d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 63d with positive return — quarter-horizon win rate."""
    r = _log_returns(close)
    return (r > 0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()


def f36_svas_209_up_fraction_504d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 504d with positive return — biennial win rate."""
    r = _log_returns(close)
    return (r > 0).astype(float).rolling(DDAYS_2Y, min_periods=YDAYS).mean()


def f36_svas_210_up_fraction_zscore_in_1260d(close: pd.Series) -> pd.Series:
    """Z-score of 252d up-fraction within 1260d distribution — regime-relative win-rate extremity."""
    r = _log_returns(close)
    uf = (r > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    return _rolling_zscore(uf, DDAYS_5Y, min_periods=YDAYS)


# ============================================================
# Bucket AC — Max consecutive loss days at additional horizons (211-213)
# (Family already has longest_down_streak at 252d; here we add 21d, 63d, 504d.)
# ============================================================

def _longest_neg_run_window(w: np.ndarray) -> float:
    if w.size == 0 or np.isnan(w).all():
        return np.nan
    best = 0; cur = 0
    for v in w:
        if np.isnan(v):
            cur = 0
            continue
        if v < 0:
            cur += 1
            if cur > best:
                best = cur
        else:
            cur = 0
    return float(best)


def f36_svas_211_max_consecutive_loss_days_21d(close: pd.Series) -> pd.Series:
    """Longest consecutive losing streak in trailing 21d — short-horizon loss persistence."""
    r = _log_returns(close)
    return r.rolling(MDAYS, min_periods=WDAYS).apply(_longest_neg_run_window, raw=True)


def f36_svas_212_max_consecutive_loss_days_63d(close: pd.Series) -> pd.Series:
    """Longest consecutive losing streak in trailing 63d — quarter-horizon loss persistence."""
    r = _log_returns(close)
    return r.rolling(QDAYS, min_periods=MDAYS).apply(_longest_neg_run_window, raw=True)


def f36_svas_213_max_consecutive_loss_days_504d(close: pd.Series) -> pd.Series:
    """Longest consecutive losing streak in trailing 504d — biennial loss persistence."""
    r = _log_returns(close)
    return r.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_longest_neg_run_window, raw=True)


# ============================================================
# Bucket AD — k-day rolling drawdown / runup (214-218)
# Worst k-day return vs best k-day return within trailing window —
# captures k-day swings rather than single-day extremes.
# ============================================================

def f36_svas_214_largest_5d_drawdown_252d(close: pd.Series) -> pd.Series:
    """Worst (most-negative) trailing-5d return seen anywhere in trailing 252d — biggest weekly drawdown."""
    r = _log_returns(close)
    r5 = r.rolling(WDAYS, min_periods=2).sum()
    return r5.rolling(YDAYS, min_periods=QDAYS).min()


def f36_svas_215_largest_5d_runup_252d(close: pd.Series) -> pd.Series:
    """Best trailing-5d return seen anywhere in trailing 252d — biggest weekly runup."""
    r = _log_returns(close)
    r5 = r.rolling(WDAYS, min_periods=2).sum()
    return r5.rolling(YDAYS, min_periods=QDAYS).max()


def f36_svas_216_5d_drawdown_runup_asymmetry_252d(close: pd.Series) -> pd.Series:
    """|largest 5d drawdown| - largest 5d runup in 252d — additive weekly swing asymmetry."""
    r = _log_returns(close)
    r5 = r.rolling(WDAYS, min_periods=2).sum()
    dd = r5.rolling(YDAYS, min_periods=QDAYS).min()
    ru = r5.rolling(YDAYS, min_periods=QDAYS).max()
    return dd.abs() - ru


def f36_svas_217_largest_21d_drawdown_252d(close: pd.Series) -> pd.Series:
    """Worst trailing-21d return seen anywhere in trailing 252d — biggest monthly drawdown."""
    r = _log_returns(close)
    r21 = r.rolling(MDAYS, min_periods=WDAYS).sum()
    return r21.rolling(YDAYS, min_periods=QDAYS).min()


def f36_svas_218_largest_21d_runup_252d(close: pd.Series) -> pd.Series:
    """Best trailing-21d return seen anywhere in trailing 252d — biggest monthly runup."""
    r = _log_returns(close)
    r21 = r.rolling(MDAYS, min_periods=WDAYS).sum()
    return r21.rolling(YDAYS, min_periods=QDAYS).max()


# ============================================================
# Bucket AE — Engle-Ng sign / size bias test stats (219-222)
# Engle-Ng 1993: regress r^2 on lagged sign and sign*magnitude to test
# for asymmetric vol response. We compute the t-stats / coefficients.
# ============================================================

def _sign_bias_window(w: np.ndarray) -> float:
    """Engle-Ng sign bias test: regress r_t^2 on intercept and S_{t-1}^- (=1 if r_{t-1}<0)."""
    v = w[~np.isnan(w)]
    if v.size < 30:
        return np.nan
    rr = v[1:]
    sneg = (v[:-1] < 0).astype(float)
    y = rr ** 2
    X = sneg
    if X.std() == 0:
        return np.nan
    beta = np.cov(y, X, bias=False)[0, 1] / X.var(ddof=1)
    return float(beta)


def _neg_size_bias_window(w: np.ndarray) -> float:
    """Engle-Ng negative size bias: regress r_t^2 on S_{t-1}^- * r_{t-1}."""
    v = w[~np.isnan(w)]
    if v.size < 30:
        return np.nan
    rr = v[1:]
    sneg = (v[:-1] < 0).astype(float)
    z = sneg * v[:-1]
    y = rr ** 2
    if z.std() == 0:
        return np.nan
    beta = np.cov(y, z, bias=False)[0, 1] / z.var(ddof=1)
    return float(beta)


def _pos_size_bias_window(w: np.ndarray) -> float:
    """Engle-Ng positive size bias: regress r_t^2 on S_{t-1}^+ * r_{t-1}."""
    v = w[~np.isnan(w)]
    if v.size < 30:
        return np.nan
    rr = v[1:]
    spos = (v[:-1] >= 0).astype(float)
    z = spos * v[:-1]
    y = rr ** 2
    if z.std() == 0:
        return np.nan
    beta = np.cov(y, z, bias=False)[0, 1] / z.var(ddof=1)
    return float(beta)


def f36_svas_219_engle_ng_sign_bias_252d(close: pd.Series) -> pd.Series:
    """Engle-Ng sign-bias coefficient over 252d — non-zero indicates asymmetric vol response to sign of prior return."""
    r = _log_returns(close)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_sign_bias_window, raw=True)


def f36_svas_220_engle_ng_negative_size_bias_252d(close: pd.Series) -> pd.Series:
    """Engle-Ng negative-size-bias coefficient over 252d — captures vol response to size of negative returns."""
    r = _log_returns(close)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_neg_size_bias_window, raw=True)


def f36_svas_221_engle_ng_positive_size_bias_252d(close: pd.Series) -> pd.Series:
    """Engle-Ng positive-size-bias coefficient over 252d — captures vol response to size of positive returns."""
    r = _log_returns(close)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_pos_size_bias_window, raw=True)


def f36_svas_222_joint_sign_bias_composite_252d(close: pd.Series) -> pd.Series:
    """sign_bias + |neg_size_bias| + |pos_size_bias| over 252d — joint Engle-Ng asymmetry composite."""
    r = _log_returns(close)
    sb = r.rolling(YDAYS, min_periods=QDAYS).apply(_sign_bias_window, raw=True)
    nsb = r.rolling(YDAYS, min_periods=QDAYS).apply(_neg_size_bias_window, raw=True)
    psb = r.rolling(YDAYS, min_periods=QDAYS).apply(_pos_size_bias_window, raw=True)
    return sb + nsb.abs() + psb.abs()


# ============================================================
# Bucket AF — Stuck-peak composites (223-225)
# Tailored to the label this pipeline targets: stocks that touch -80%
# and never recover above -50% within 5 years.
# ============================================================

def f36_svas_223_stuck_peak_risk_composite_504d(close: pd.Series) -> pd.Series:
    """Z-blend of: max-DD depth + DD duration + neg-tail RSk + Hill(left tail) — overall stuck-peak risk score."""
    r = _log_returns(close)
    mdd = _max_drawdown_from_close(close, DDAYS_2Y, YDAYS).abs()
    def _max_dur(w):
        v = w[~np.isnan(w)]
        if v.size < 21:
            return np.nan
        best = 0; cur = 0; cur_max = -np.inf
        for x in v:
            if x >= cur_max:
                if cur > best: best = cur
                cur_max = x; cur = 0
            else:
                cur += 1
        if cur > best: best = cur
        return float(best)
    dur = close.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_max_dur, raw=True)
    rsk_n = _realized_skewness(r, DDAYS_2Y, YDAYS)   # more-negative = more loss skew
    hill_l = r.rolling(DDAYS_2Y, min_periods=YDAYS).apply(lambda w: _hill_estimator(w, "left", 0.10), raw=True)
    z_mdd = _rolling_zscore(mdd, DDAYS_5Y, min_periods=YDAYS)
    z_dur = _rolling_zscore(dur, DDAYS_5Y, min_periods=YDAYS)
    z_rsk = _rolling_zscore(-rsk_n, DDAYS_5Y, min_periods=YDAYS)
    z_hill = _rolling_zscore(-hill_l, DDAYS_5Y, min_periods=YDAYS)   # lower alpha = heavier tail = riskier
    return (z_mdd + z_dur + z_rsk + z_hill) / 4.0


def f36_svas_224_realized_moment_asymmetry_composite_252d(close: pd.Series) -> pd.Series:
    """Z-blend of: realized_skew_252 (negated) + realized_kurt_252 + Calmar_252 (negated) —
    higher = more left-skewed / heavier-tailed / worse risk-adjusted return."""
    r = _log_returns(close)
    rsk = _realized_skewness(r, YDAYS, QDAYS)
    rkt = _realized_kurtosis(r, YDAYS, QDAYS)
    ann_ret = _annualized_return(close, YDAYS, QDAYS)
    mdd = _max_drawdown_from_close(close, YDAYS, QDAYS)
    calmar = _safe_div(ann_ret, mdd.abs())
    z_rsk = _rolling_zscore(-rsk, DDAYS_2Y, min_periods=YDAYS)
    z_rkt = _rolling_zscore(rkt, DDAYS_2Y, min_periods=YDAYS)
    z_cal = _rolling_zscore(-calmar, DDAYS_2Y, min_periods=YDAYS)
    return (z_rsk + z_rkt + z_cal) / 3.0


def f36_svas_225_prospect_theory_stuck_peak_composite_504d(close: pd.Series) -> pd.Series:
    """Z-blend of: loss-aversion-ratio (negated) + Ulcer-504 + underwater-fraction-504 —
    high = prospect-theory-bad regime with high DD intensity and time underwater."""
    r = _log_returns(close)
    pu = (r > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    pl = (r < 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    g = _when_pos(r).rolling(YDAYS, min_periods=QDAYS).mean()
    l = (-_when_neg(r)).rolling(YDAYS, min_periods=QDAYS).mean()
    la = pu * g - KT_LAMBDA * pl * l
    ulc = close.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_ulcer_index_window, raw=True)
    def _uw(w):
        v = w[~np.isnan(w)]
        if v.size < 21:
            return np.nan
        peak = np.maximum.accumulate(v)
        return float((v < peak).sum() / v.size)
    uw = close.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_uw, raw=True)
    z_la = _rolling_zscore(-la, DDAYS_5Y, min_periods=YDAYS)
    z_u = _rolling_zscore(ulc, DDAYS_5Y, min_periods=YDAYS)
    z_w = _rolling_zscore(uw, DDAYS_5Y, min_periods=YDAYS)
    return (z_la + z_u + z_w) / 3.0


# ============================================================
#                         REGISTRY 151-225
# ============================================================



def f36_svas_151_realized_skewness_21d_d2(close):
    return f36_svas_151_realized_skewness_21d(close).diff().diff()


def f36_svas_152_realized_skewness_63d_d2(close):
    return f36_svas_152_realized_skewness_63d(close).diff().diff()


def f36_svas_153_realized_skewness_252d_d2(close):
    return f36_svas_153_realized_skewness_252d(close).diff().diff()


def f36_svas_154_realized_kurtosis_21d_d2(close):
    return f36_svas_154_realized_kurtosis_21d(close).diff().diff()


def f36_svas_155_realized_kurtosis_63d_d2(close):
    return f36_svas_155_realized_kurtosis_63d(close).diff().diff()


def f36_svas_156_realized_kurtosis_252d_d2(close):
    return f36_svas_156_realized_kurtosis_252d(close).diff().diff()


def f36_svas_157_realized_semi_skewness_pos_252d_d2(close):
    return f36_svas_157_realized_semi_skewness_pos_252d(close).diff().diff()


def f36_svas_158_realized_semi_skewness_neg_252d_d2(close):
    return f36_svas_158_realized_semi_skewness_neg_252d(close).diff().diff()


def f36_svas_159_calmar_ratio_252d_d2(close):
    return f36_svas_159_calmar_ratio_252d(close).diff().diff()


def f36_svas_160_calmar_ratio_504d_d2(close):
    return f36_svas_160_calmar_ratio_504d(close).diff().diff()


def f36_svas_161_sterling_ratio_252d_d2(close):
    return f36_svas_161_sterling_ratio_252d(close).diff().diff()


def f36_svas_162_burke_ratio_252d_d2(close):
    return f36_svas_162_burke_ratio_252d(close).diff().diff()


def f36_svas_163_pain_ratio_252d_d2(close):
    return f36_svas_163_pain_ratio_252d(close).diff().diff()


def f36_svas_164_martin_ratio_252d_d2(close):
    return f36_svas_164_martin_ratio_252d(close).diff().diff()


def f36_svas_165_log_calmar_ratio_252d_d2(close):
    return f36_svas_165_log_calmar_ratio_252d(close).diff().diff()


def f36_svas_166_calmar_ratio_1260d_d2(close):
    return f36_svas_166_calmar_ratio_1260d(close).diff().diff()


def f36_svas_167_sterling_ratio_504d_d2(close):
    return f36_svas_167_sterling_ratio_504d(close).diff().diff()


def f36_svas_168_ulcer_index_252d_d2(close):
    return f36_svas_168_ulcer_index_252d(close).diff().diff()


def f36_svas_169_ulcer_index_504d_d2(close):
    return f36_svas_169_ulcer_index_504d(close).diff().diff()


def f36_svas_170_pain_index_252d_d2(close):
    return f36_svas_170_pain_index_252d(close).diff().diff()


def f36_svas_171_pain_index_504d_d2(close):
    return f36_svas_171_pain_index_504d(close).diff().diff()


def f36_svas_172_max_single_drawdown_pct_252d_d2(close):
    return f36_svas_172_max_single_drawdown_pct_252d(close).diff().diff()


def f36_svas_173_mean_drawdown_at_troughs_252d_d2(close):
    return f36_svas_173_mean_drawdown_at_troughs_252d(close).diff().diff()


def f36_svas_174_omega_ratio_theta0_252d_d2(close):
    return f36_svas_174_omega_ratio_theta0_252d(close).diff().diff()


def f36_svas_175_omega_ratio_theta0_504d_d2(close):
    return f36_svas_175_omega_ratio_theta0_504d(close).diff().diff()


def f36_svas_176_omega_ratio_theta_rf_2pct_252d_d2(close):
    return f36_svas_176_omega_ratio_theta_rf_2pct_252d(close).diff().diff()


def f36_svas_177_log_omega_ratio_theta0_252d_d2(close):
    return f36_svas_177_log_omega_ratio_theta0_252d(close).diff().diff()


def f36_svas_178_cornish_fisher_var_5pct_252d_d2(close):
    return f36_svas_178_cornish_fisher_var_5pct_252d(close).diff().diff()


def f36_svas_179_cornish_fisher_var_1pct_252d_d2(close):
    return f36_svas_179_cornish_fisher_var_1pct_252d(close).diff().diff()


def f36_svas_180_cornish_fisher_es_5pct_252d_d2(close):
    return f36_svas_180_cornish_fisher_es_5pct_252d(close).diff().diff()


def f36_svas_181_cf_var_minus_parametric_var_5pct_252d_d2(close):
    return f36_svas_181_cf_var_minus_parametric_var_5pct_252d(close).diff().diff()


def f36_svas_182_cornish_fisher_var_5pct_504d_d2(close):
    return f36_svas_182_cornish_fisher_var_5pct_504d(close).diff().diff()


def f36_svas_183_cornish_fisher_var_5pct_21d_d2(close):
    return f36_svas_183_cornish_fisher_var_5pct_21d(close).diff().diff()


def f36_svas_184_hill_estimator_left_tail_10pct_252d_d2(close):
    return f36_svas_184_hill_estimator_left_tail_10pct_252d(close).diff().diff()


def f36_svas_185_hill_estimator_right_tail_10pct_252d_d2(close):
    return f36_svas_185_hill_estimator_right_tail_10pct_252d(close).diff().diff()


def f36_svas_186_hill_left_minus_right_252d_d2(close):
    return f36_svas_186_hill_left_minus_right_252d(close).diff().diff()


def f36_svas_187_hill_left_over_right_252d_d2(close):
    return f36_svas_187_hill_left_over_right_252d(close).diff().diff()


def f36_svas_188_current_drawdown_duration_d2(close):
    return f36_svas_188_current_drawdown_duration(close).diff().diff()


def f36_svas_189_mean_drawdown_duration_252d_d2(close):
    return f36_svas_189_mean_drawdown_duration_252d(close).diff().diff()


def f36_svas_190_max_drawdown_duration_252d_d2(close):
    return f36_svas_190_max_drawdown_duration_252d(close).diff().diff()


def f36_svas_191_underwater_fraction_252d_d2(close):
    return f36_svas_191_underwater_fraction_252d(close).diff().diff()


def f36_svas_192_underwater_fraction_504d_d2(close):
    return f36_svas_192_underwater_fraction_504d(close).diff().diff()


def f36_svas_193_time_to_recovery_last_drawdown_504d_d2(close):
    return f36_svas_193_time_to_recovery_last_drawdown_504d(close).diff().diff()


def f36_svas_194_loss_aversion_ratio_252d_d2(close):
    return f36_svas_194_loss_aversion_ratio_252d(close).diff().diff()


def f36_svas_195_prospect_theory_utility_252d_d2(close):
    return f36_svas_195_prospect_theory_utility_252d(close).diff().diff()


def f36_svas_196_inverse_s_weight_asymmetry_252d_d2(close):
    return f36_svas_196_inverse_s_weight_asymmetry_252d(close).diff().diff()


def f36_svas_197_loss_aversion_zscore_504d_d2(close):
    return f36_svas_197_loss_aversion_zscore_504d(close).diff().diff()


def f36_svas_198_skew_term_structure_slope_3pt_d2(close):
    return f36_svas_198_skew_term_structure_slope_3pt(close).diff().diff()


def f36_svas_199_skew_term_structure_curvature_3pt_d2(close):
    return f36_svas_199_skew_term_structure_curvature_3pt(close).diff().diff()


def f36_svas_200_skew_term_structure_slope_4pt_d2(close):
    return f36_svas_200_skew_term_structure_slope_4pt(close).diff().diff()


def f36_svas_201_skew_term_structure_intercept_4pt_d2(close):
    return f36_svas_201_skew_term_structure_intercept_4pt(close).diff().diff()


def f36_svas_202_skew_term_structure_r2_4pt_d2(close):
    return f36_svas_202_skew_term_structure_r2_4pt(close).diff().diff()


def f36_svas_203_skew_in_high_vol_regime_252d_d2(close):
    return f36_svas_203_skew_in_high_vol_regime_252d(close).diff().diff()


def f36_svas_204_skew_in_low_vol_regime_252d_d2(close):
    return f36_svas_204_skew_in_low_vol_regime_252d(close).diff().diff()


def f36_svas_205_conditional_skew_asymmetry_high_low_252d_d2(close):
    return f36_svas_205_conditional_skew_asymmetry_high_low_252d(close).diff().diff()


def f36_svas_206_skew_in_top_quintile_vol_252d_d2(close):
    return f36_svas_206_skew_in_top_quintile_vol_252d(close).diff().diff()


def f36_svas_207_up_fraction_21d_d2(close):
    return f36_svas_207_up_fraction_21d(close).diff().diff()


def f36_svas_208_up_fraction_63d_d2(close):
    return f36_svas_208_up_fraction_63d(close).diff().diff()


def f36_svas_209_up_fraction_504d_d2(close):
    return f36_svas_209_up_fraction_504d(close).diff().diff()


def f36_svas_210_up_fraction_zscore_in_1260d_d2(close):
    return f36_svas_210_up_fraction_zscore_in_1260d(close).diff().diff()


def f36_svas_211_max_consecutive_loss_days_21d_d2(close):
    return f36_svas_211_max_consecutive_loss_days_21d(close).diff().diff()


def f36_svas_212_max_consecutive_loss_days_63d_d2(close):
    return f36_svas_212_max_consecutive_loss_days_63d(close).diff().diff()


def f36_svas_213_max_consecutive_loss_days_504d_d2(close):
    return f36_svas_213_max_consecutive_loss_days_504d(close).diff().diff()


def f36_svas_214_largest_5d_drawdown_252d_d2(close):
    return f36_svas_214_largest_5d_drawdown_252d(close).diff().diff()


def f36_svas_215_largest_5d_runup_252d_d2(close):
    return f36_svas_215_largest_5d_runup_252d(close).diff().diff()


def f36_svas_216_5d_drawdown_runup_asymmetry_252d_d2(close):
    return f36_svas_216_5d_drawdown_runup_asymmetry_252d(close).diff().diff()


def f36_svas_217_largest_21d_drawdown_252d_d2(close):
    return f36_svas_217_largest_21d_drawdown_252d(close).diff().diff()


def f36_svas_218_largest_21d_runup_252d_d2(close):
    return f36_svas_218_largest_21d_runup_252d(close).diff().diff()


def f36_svas_219_engle_ng_sign_bias_252d_d2(close):
    return f36_svas_219_engle_ng_sign_bias_252d(close).diff().diff()


def f36_svas_220_engle_ng_negative_size_bias_252d_d2(close):
    return f36_svas_220_engle_ng_negative_size_bias_252d(close).diff().diff()


def f36_svas_221_engle_ng_positive_size_bias_252d_d2(close):
    return f36_svas_221_engle_ng_positive_size_bias_252d(close).diff().diff()


def f36_svas_222_joint_sign_bias_composite_252d_d2(close):
    return f36_svas_222_joint_sign_bias_composite_252d(close).diff().diff()


def f36_svas_223_stuck_peak_risk_composite_504d_d2(close):
    return f36_svas_223_stuck_peak_risk_composite_504d(close).diff().diff()


def f36_svas_224_realized_moment_asymmetry_composite_252d_d2(close):
    return f36_svas_224_realized_moment_asymmetry_composite_252d(close).diff().diff()


def f36_svas_225_prospect_theory_stuck_peak_composite_504d_d2(close):
    return f36_svas_225_prospect_theory_stuck_peak_composite_504d(close).diff().diff()


SEMI_VARIANCE_ASYMMETRY_D2_REGISTRY_151_225 = {
    "f36_svas_151_realized_skewness_21d_d2": {"inputs": ["close"], "func": f36_svas_151_realized_skewness_21d_d2},
    "f36_svas_152_realized_skewness_63d_d2": {"inputs": ["close"], "func": f36_svas_152_realized_skewness_63d_d2},
    "f36_svas_153_realized_skewness_252d_d2": {"inputs": ["close"], "func": f36_svas_153_realized_skewness_252d_d2},
    "f36_svas_154_realized_kurtosis_21d_d2": {"inputs": ["close"], "func": f36_svas_154_realized_kurtosis_21d_d2},
    "f36_svas_155_realized_kurtosis_63d_d2": {"inputs": ["close"], "func": f36_svas_155_realized_kurtosis_63d_d2},
    "f36_svas_156_realized_kurtosis_252d_d2": {"inputs": ["close"], "func": f36_svas_156_realized_kurtosis_252d_d2},
    "f36_svas_157_realized_semi_skewness_pos_252d_d2": {"inputs": ["close"], "func": f36_svas_157_realized_semi_skewness_pos_252d_d2},
    "f36_svas_158_realized_semi_skewness_neg_252d_d2": {"inputs": ["close"], "func": f36_svas_158_realized_semi_skewness_neg_252d_d2},
    "f36_svas_159_calmar_ratio_252d_d2": {"inputs": ["close"], "func": f36_svas_159_calmar_ratio_252d_d2},
    "f36_svas_160_calmar_ratio_504d_d2": {"inputs": ["close"], "func": f36_svas_160_calmar_ratio_504d_d2},
    "f36_svas_161_sterling_ratio_252d_d2": {"inputs": ["close"], "func": f36_svas_161_sterling_ratio_252d_d2},
    "f36_svas_162_burke_ratio_252d_d2": {"inputs": ["close"], "func": f36_svas_162_burke_ratio_252d_d2},
    "f36_svas_163_pain_ratio_252d_d2": {"inputs": ["close"], "func": f36_svas_163_pain_ratio_252d_d2},
    "f36_svas_164_martin_ratio_252d_d2": {"inputs": ["close"], "func": f36_svas_164_martin_ratio_252d_d2},
    "f36_svas_165_log_calmar_ratio_252d_d2": {"inputs": ["close"], "func": f36_svas_165_log_calmar_ratio_252d_d2},
    "f36_svas_166_calmar_ratio_1260d_d2": {"inputs": ["close"], "func": f36_svas_166_calmar_ratio_1260d_d2},
    "f36_svas_167_sterling_ratio_504d_d2": {"inputs": ["close"], "func": f36_svas_167_sterling_ratio_504d_d2},
    "f36_svas_168_ulcer_index_252d_d2": {"inputs": ["close"], "func": f36_svas_168_ulcer_index_252d_d2},
    "f36_svas_169_ulcer_index_504d_d2": {"inputs": ["close"], "func": f36_svas_169_ulcer_index_504d_d2},
    "f36_svas_170_pain_index_252d_d2": {"inputs": ["close"], "func": f36_svas_170_pain_index_252d_d2},
    "f36_svas_171_pain_index_504d_d2": {"inputs": ["close"], "func": f36_svas_171_pain_index_504d_d2},
    "f36_svas_172_max_single_drawdown_pct_252d_d2": {"inputs": ["close"], "func": f36_svas_172_max_single_drawdown_pct_252d_d2},
    "f36_svas_173_mean_drawdown_at_troughs_252d_d2": {"inputs": ["close"], "func": f36_svas_173_mean_drawdown_at_troughs_252d_d2},
    "f36_svas_174_omega_ratio_theta0_252d_d2": {"inputs": ["close"], "func": f36_svas_174_omega_ratio_theta0_252d_d2},
    "f36_svas_175_omega_ratio_theta0_504d_d2": {"inputs": ["close"], "func": f36_svas_175_omega_ratio_theta0_504d_d2},
    "f36_svas_176_omega_ratio_theta_rf_2pct_252d_d2": {"inputs": ["close"], "func": f36_svas_176_omega_ratio_theta_rf_2pct_252d_d2},
    "f36_svas_177_log_omega_ratio_theta0_252d_d2": {"inputs": ["close"], "func": f36_svas_177_log_omega_ratio_theta0_252d_d2},
    "f36_svas_178_cornish_fisher_var_5pct_252d_d2": {"inputs": ["close"], "func": f36_svas_178_cornish_fisher_var_5pct_252d_d2},
    "f36_svas_179_cornish_fisher_var_1pct_252d_d2": {"inputs": ["close"], "func": f36_svas_179_cornish_fisher_var_1pct_252d_d2},
    "f36_svas_180_cornish_fisher_es_5pct_252d_d2": {"inputs": ["close"], "func": f36_svas_180_cornish_fisher_es_5pct_252d_d2},
    "f36_svas_181_cf_var_minus_parametric_var_5pct_252d_d2": {"inputs": ["close"], "func": f36_svas_181_cf_var_minus_parametric_var_5pct_252d_d2},
    "f36_svas_182_cornish_fisher_var_5pct_504d_d2": {"inputs": ["close"], "func": f36_svas_182_cornish_fisher_var_5pct_504d_d2},
    "f36_svas_183_cornish_fisher_var_5pct_21d_d2": {"inputs": ["close"], "func": f36_svas_183_cornish_fisher_var_5pct_21d_d2},
    "f36_svas_184_hill_estimator_left_tail_10pct_252d_d2": {"inputs": ["close"], "func": f36_svas_184_hill_estimator_left_tail_10pct_252d_d2},
    "f36_svas_185_hill_estimator_right_tail_10pct_252d_d2": {"inputs": ["close"], "func": f36_svas_185_hill_estimator_right_tail_10pct_252d_d2},
    "f36_svas_186_hill_left_minus_right_252d_d2": {"inputs": ["close"], "func": f36_svas_186_hill_left_minus_right_252d_d2},
    "f36_svas_187_hill_left_over_right_252d_d2": {"inputs": ["close"], "func": f36_svas_187_hill_left_over_right_252d_d2},
    "f36_svas_188_current_drawdown_duration_d2": {"inputs": ["close"], "func": f36_svas_188_current_drawdown_duration_d2},
    "f36_svas_189_mean_drawdown_duration_252d_d2": {"inputs": ["close"], "func": f36_svas_189_mean_drawdown_duration_252d_d2},
    "f36_svas_190_max_drawdown_duration_252d_d2": {"inputs": ["close"], "func": f36_svas_190_max_drawdown_duration_252d_d2},
    "f36_svas_191_underwater_fraction_252d_d2": {"inputs": ["close"], "func": f36_svas_191_underwater_fraction_252d_d2},
    "f36_svas_192_underwater_fraction_504d_d2": {"inputs": ["close"], "func": f36_svas_192_underwater_fraction_504d_d2},
    "f36_svas_193_time_to_recovery_last_drawdown_504d_d2": {"inputs": ["close"], "func": f36_svas_193_time_to_recovery_last_drawdown_504d_d2},
    "f36_svas_194_loss_aversion_ratio_252d_d2": {"inputs": ["close"], "func": f36_svas_194_loss_aversion_ratio_252d_d2},
    "f36_svas_195_prospect_theory_utility_252d_d2": {"inputs": ["close"], "func": f36_svas_195_prospect_theory_utility_252d_d2},
    "f36_svas_196_inverse_s_weight_asymmetry_252d_d2": {"inputs": ["close"], "func": f36_svas_196_inverse_s_weight_asymmetry_252d_d2},
    "f36_svas_197_loss_aversion_zscore_504d_d2": {"inputs": ["close"], "func": f36_svas_197_loss_aversion_zscore_504d_d2},
    "f36_svas_198_skew_term_structure_slope_3pt_d2": {"inputs": ["close"], "func": f36_svas_198_skew_term_structure_slope_3pt_d2},
    "f36_svas_199_skew_term_structure_curvature_3pt_d2": {"inputs": ["close"], "func": f36_svas_199_skew_term_structure_curvature_3pt_d2},
    "f36_svas_200_skew_term_structure_slope_4pt_d2": {"inputs": ["close"], "func": f36_svas_200_skew_term_structure_slope_4pt_d2},
    "f36_svas_201_skew_term_structure_intercept_4pt_d2": {"inputs": ["close"], "func": f36_svas_201_skew_term_structure_intercept_4pt_d2},
    "f36_svas_202_skew_term_structure_r2_4pt_d2": {"inputs": ["close"], "func": f36_svas_202_skew_term_structure_r2_4pt_d2},
    "f36_svas_203_skew_in_high_vol_regime_252d_d2": {"inputs": ["close"], "func": f36_svas_203_skew_in_high_vol_regime_252d_d2},
    "f36_svas_204_skew_in_low_vol_regime_252d_d2": {"inputs": ["close"], "func": f36_svas_204_skew_in_low_vol_regime_252d_d2},
    "f36_svas_205_conditional_skew_asymmetry_high_low_252d_d2": {"inputs": ["close"], "func": f36_svas_205_conditional_skew_asymmetry_high_low_252d_d2},
    "f36_svas_206_skew_in_top_quintile_vol_252d_d2": {"inputs": ["close"], "func": f36_svas_206_skew_in_top_quintile_vol_252d_d2},
    "f36_svas_207_up_fraction_21d_d2": {"inputs": ["close"], "func": f36_svas_207_up_fraction_21d_d2},
    "f36_svas_208_up_fraction_63d_d2": {"inputs": ["close"], "func": f36_svas_208_up_fraction_63d_d2},
    "f36_svas_209_up_fraction_504d_d2": {"inputs": ["close"], "func": f36_svas_209_up_fraction_504d_d2},
    "f36_svas_210_up_fraction_zscore_in_1260d_d2": {"inputs": ["close"], "func": f36_svas_210_up_fraction_zscore_in_1260d_d2},
    "f36_svas_211_max_consecutive_loss_days_21d_d2": {"inputs": ["close"], "func": f36_svas_211_max_consecutive_loss_days_21d_d2},
    "f36_svas_212_max_consecutive_loss_days_63d_d2": {"inputs": ["close"], "func": f36_svas_212_max_consecutive_loss_days_63d_d2},
    "f36_svas_213_max_consecutive_loss_days_504d_d2": {"inputs": ["close"], "func": f36_svas_213_max_consecutive_loss_days_504d_d2},
    "f36_svas_214_largest_5d_drawdown_252d_d2": {"inputs": ["close"], "func": f36_svas_214_largest_5d_drawdown_252d_d2},
    "f36_svas_215_largest_5d_runup_252d_d2": {"inputs": ["close"], "func": f36_svas_215_largest_5d_runup_252d_d2},
    "f36_svas_216_5d_drawdown_runup_asymmetry_252d_d2": {"inputs": ["close"], "func": f36_svas_216_5d_drawdown_runup_asymmetry_252d_d2},
    "f36_svas_217_largest_21d_drawdown_252d_d2": {"inputs": ["close"], "func": f36_svas_217_largest_21d_drawdown_252d_d2},
    "f36_svas_218_largest_21d_runup_252d_d2": {"inputs": ["close"], "func": f36_svas_218_largest_21d_runup_252d_d2},
    "f36_svas_219_engle_ng_sign_bias_252d_d2": {"inputs": ["close"], "func": f36_svas_219_engle_ng_sign_bias_252d_d2},
    "f36_svas_220_engle_ng_negative_size_bias_252d_d2": {"inputs": ["close"], "func": f36_svas_220_engle_ng_negative_size_bias_252d_d2},
    "f36_svas_221_engle_ng_positive_size_bias_252d_d2": {"inputs": ["close"], "func": f36_svas_221_engle_ng_positive_size_bias_252d_d2},
    "f36_svas_222_joint_sign_bias_composite_252d_d2": {"inputs": ["close"], "func": f36_svas_222_joint_sign_bias_composite_252d_d2},
    "f36_svas_223_stuck_peak_risk_composite_504d_d2": {"inputs": ["close"], "func": f36_svas_223_stuck_peak_risk_composite_504d_d2},
    "f36_svas_224_realized_moment_asymmetry_composite_252d_d2": {"inputs": ["close"], "func": f36_svas_224_realized_moment_asymmetry_composite_252d_d2},
    "f36_svas_225_prospect_theory_stuck_peak_composite_504d_d2": {"inputs": ["close"], "func": f36_svas_225_prospect_theory_stuck_peak_composite_504d_d2},
}
