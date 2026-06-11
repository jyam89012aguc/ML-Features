"""semi_variance_asymmetry base features 226-300 — Pipeline 1b-technical.

Practical-signal extension to family 36. 75 distinct hypotheses NOT covered
by the existing 225 features. Focus: drawdown dynamics, risk-adjusted
ratios with statistical corrections, and tail behavior measures that are
*actually used in live risk management*.

Buckets:
  AA Drawdown velocity / acceleration / time-to-trough (226-233)
  BB Adjusted Sharpe / PSR / Lo-Sharpe / multi-horizon Sharpe (234-240)
  CC VaR backtesting (Kupiec POF, Christoffersen IND, exceedance clustering) (241-246)
  DD Conditional Drawdown at Risk (CDaR) (247-251)
  EE MAR ratios at multiple thresholds (252-256)
  FF K-ratio (Kestner) (257-260)
  GG Recovery factor / new-high frequency (261-266)
  HH L-moments (Hosking) skew & kurt (267-271)
  II Tail-cluster / consecutive-loss measures (272-278)
  JJ Drawdown survival / hazard / recovery probability (279-283)
  KK Underwater-curve statistics (284-289)
  LL Stuck-peak label-proxy composites (290-300)

Inputs: SEP OHLCV only. PIT-clean: right-anchored, explicit min_periods.
Self-contained helpers — no cross-family imports.
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
            x = x[valid]; wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)


def _log_returns(close: pd.Series) -> pd.Series:
    return _safe_log(close).diff()


def _underwater(close: pd.Series) -> pd.Series:
    """Underwater curve: 1 - close / running_max (>= 0). Expanding-window peak."""
    peak = close.cummax()
    return 1.0 - close / peak


def _underwater_window(close: pd.Series, n: int, mp: int) -> pd.Series:
    """Underwater curve within rolling window (peak resets per window)."""
    def _uw(w):
        v = w[~np.isnan(w)]
        if v.size < 5:
            return np.nan
        peak = np.maximum.accumulate(v)
        return float(1.0 - v[-1] / peak[-1])
    return close.rolling(n, min_periods=mp).apply(_uw, raw=True)


# ============================================================
# Bucket AA — Drawdown velocity / acceleration / time-to-trough (226-233)
# Capture the *dynamics* of drawdowns, not just their depth.
# ============================================================

def f35_svas_dummy(): pass  # placeholder removed — function below uses correct prefix


def f36_svas_226_dd_velocity_21d(close: pd.Series) -> pd.Series:
    """Slope of underwater curve over trailing 21d — drawdown velocity (positive = getting deeper)."""
    uw = _underwater(close)
    return _rolling_slope(uw, MDAYS)


def f36_svas_227_dd_velocity_63d(close: pd.Series) -> pd.Series:
    """Slope of underwater curve over trailing 63d — quarterly drawdown velocity."""
    uw = _underwater(close)
    return _rolling_slope(uw, QDAYS)


def f36_svas_228_dd_acceleration_21d(close: pd.Series) -> pd.Series:
    """Acceleration: slope(slope(underwater)_21d)_21d — drawdown second derivative."""
    uw = _underwater(close)
    slope = _rolling_slope(uw, MDAYS)
    return _rolling_slope(slope, MDAYS)


def f36_svas_229_dd_acceleration_63d(close: pd.Series) -> pd.Series:
    """Quarterly drawdown acceleration."""
    uw = _underwater(close)
    slope = _rolling_slope(uw, QDAYS)
    return _rolling_slope(slope, QDAYS)


def f36_svas_230_new_low_count_252d(close: pd.Series) -> pd.Series:
    """Count of bars in trailing 252d that printed a new expanding-window low — chronic-decline indicator."""
    rmin = close.expanding(min_periods=5).min()
    is_new_low = (close <= rmin)
    return is_new_low.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f36_svas_231_max_single_day_dd_increase_252d(close: pd.Series) -> pd.Series:
    """Largest single-day jump in underwater curve over trailing 252d — biggest one-day drawdown event."""
    uw = _underwater(close)
    return uw.diff().rolling(YDAYS, min_periods=QDAYS).max()


def f36_svas_232_time_from_peak_to_trough_in_252d(close: pd.Series) -> pd.Series:
    """Bars from the trailing-252d peak to the trailing-252d trough (peak is detected first if it precedes trough)."""
    def _gap(w):
        v = w[~np.isnan(w)]
        if v.size < 21:
            return np.nan
        pk = int(np.argmax(v))
        if pk == v.size - 1:
            return 0.0
        tr = pk + int(np.argmin(v[pk:]))
        return float(tr - pk)
    return close.rolling(YDAYS, min_periods=QDAYS).apply(_gap, raw=True)


def f36_svas_233_dd_velocity_zscore_in_504d(close: pd.Series) -> pd.Series:
    """Z-score of 21d DD velocity in 504d distribution — regime-relative drawdown speed."""
    uw = _underwater(close)
    vel = _rolling_slope(uw, MDAYS)
    return _rolling_zscore(vel, DDAYS_2Y, min_periods=YDAYS)


# ============================================================
# Bucket BB — Adjusted Sharpe / PSR / Lo-Sharpe (234-240)
# Pezier-White Adjusted Sharpe = SR * (1 + S/6 * SR - (K-3)/24 * SR^2).
# Probabilistic SR (López de Prado): P(SR > SR_benchmark).
# Lo's autocorrelation-adjusted Sharpe (Lo 2002).
# ============================================================

def _sharpe_window(w: np.ndarray) -> float:
    v = w[~np.isnan(w)]
    if v.size < 21:
        return np.nan
    mu = v.mean(); sd = v.std(ddof=1)
    if sd == 0:
        return np.nan
    return float(mu / sd)


def f36_svas_234_sharpe_21d(close: pd.Series) -> pd.Series:
    """Sharpe ratio over 21d (mean return / std, daily units) — short-horizon risk-adjusted return."""
    r = _log_returns(close)
    return r.rolling(MDAYS, min_periods=WDAYS).apply(_sharpe_window, raw=True)


def f36_svas_235_sharpe_63d(close: pd.Series) -> pd.Series:
    """Sharpe ratio over 63d (daily units) — quarterly risk-adjusted return."""
    r = _log_returns(close)
    return r.rolling(QDAYS, min_periods=MDAYS).apply(_sharpe_window, raw=True)


def f36_svas_236_sharpe_504d(close: pd.Series) -> pd.Series:
    """Sharpe ratio over 504d (daily units) — biennial risk-adjusted return."""
    r = _log_returns(close)
    return r.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_sharpe_window, raw=True)


def f36_svas_237_pezier_white_adjusted_sharpe_252d(close: pd.Series) -> pd.Series:
    """Pezier-White adjusted Sharpe = SR * (1 + S/6 * SR - (K-3)/24 * SR^2) over 252d — skew/kurt-aware SR."""
    def _adj(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        mu = v.mean(); sd = v.std(ddof=1)
        if sd == 0:
            return np.nan
        sr = mu / sd
        S = ((v - mu) ** 3).mean() / sd ** 3
        K = ((v - mu) ** 4).mean() / sd ** 4
        return float(sr * (1.0 + (S / 6.0) * sr - ((K - 3.0) / 24.0) * sr ** 2))
    r = _log_returns(close)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_adj, raw=True)


def f36_svas_238_probabilistic_sharpe_ratio_252d(close: pd.Series) -> pd.Series:
    """Probabilistic SR (López de Prado): P(SR > 0) with skew/kurt-adjusted variance of SR estimator."""
    def _psr(w):
        v = w[~np.isnan(w)]
        n = v.size
        if n < 30:
            return np.nan
        mu = v.mean(); sd = v.std(ddof=1)
        if sd == 0:
            return np.nan
        sr = mu / sd
        S = ((v - mu) ** 3).mean() / sd ** 3
        K = ((v - mu) ** 4).mean() / sd ** 4
        var_sr = (1.0 - S * sr + ((K - 1.0) / 4.0) * sr ** 2) / (n - 1.0)
        if var_sr <= 0:
            return np.nan
        # Phi(sr / sqrt(var_sr)) using a fast approximation (Hastings)
        z = sr / np.sqrt(var_sr)
        return float(0.5 * (1.0 + np.tanh(0.7978845608028654 * (z + 0.044715 * z ** 3))))
    r = _log_returns(close)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_psr, raw=True)


def f36_svas_239_lo_autocorr_adjusted_sharpe_252d(close: pd.Series) -> pd.Series:
    """Lo (2002) autocorr-adjusted Sharpe: SR / sqrt(1 + 2*sum_k=1..N-1 (1-k/N)*rho_k) over 252d."""
    def _lo(w):
        v = w[~np.isnan(w)]
        n = v.size
        if n < 30:
            return np.nan
        mu = v.mean(); sd = v.std(ddof=1)
        if sd == 0:
            return np.nan
        sr = mu / sd
        # autocovariances
        v0 = v - mu
        c0 = (v0 * v0).sum()
        if c0 == 0:
            return np.nan
        K = min(n - 1, 21)   # truncate to monthly lag
        adj_sum = 0.0
        for k in range(1, K + 1):
            rho = (v0[k:] * v0[:-k]).sum() / c0
            adj_sum += (1.0 - k / n) * rho
        denom = 1.0 + 2.0 * adj_sum
        if denom <= 0:
            return np.nan
        return float(sr / np.sqrt(denom))
    r = _log_returns(close)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_lo, raw=True)


def f36_svas_240_sharpe_zscore_in_1260d(close: pd.Series) -> pd.Series:
    """Z-score of 252d Sharpe within 1260d distribution — regime-relative Sharpe extremity."""
    r = _log_returns(close)
    sr = r.rolling(YDAYS, min_periods=QDAYS).apply(_sharpe_window, raw=True)
    return _rolling_zscore(sr, DDAYS_5Y, min_periods=YDAYS)


# ============================================================
# Bucket CC — VaR backtesting (241-246)
# Kupiec POF (proportion of failures) test; Christoffersen independence test;
# exceedance clustering. These are standard *live-risk* monitors.
# ============================================================

def _var_quantile_window(w: np.ndarray, alpha: float) -> float:
    v = w[~np.isnan(w)]
    if v.size < 21:
        return np.nan
    return float(np.quantile(v, alpha))


def f36_svas_241_var5_exceedance_count_252d(close: pd.Series) -> pd.Series:
    """Count of trailing-252d bars where return < trailing-252d-VaR(5%) — historical VaR breach count."""
    r = _log_returns(close)
    var5 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.05)
    breach = (r < var5.shift(1))   # shift to ensure VaR is from prior bar
    return breach.astype(float).where(var5.shift(1).notna(), np.nan).rolling(YDAYS, min_periods=QDAYS).sum()


def f36_svas_242_var5_exceedance_rate_252d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 252d bars where return < lagged VaR(5%) — empirical breach rate (target = 0.05)."""
    r = _log_returns(close)
    var5 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.05)
    breach = (r < var5.shift(1)).astype(float).where(var5.shift(1).notna(), np.nan)
    return breach.rolling(YDAYS, min_periods=QDAYS).mean()


def f36_svas_243_var1_exceedance_count_252d(close: pd.Series) -> pd.Series:
    """Count of trailing-252d VaR(1%) breaches — deep-tail VaR breach count."""
    r = _log_returns(close)
    var1 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.01)
    breach = (r < var1.shift(1))
    return breach.astype(float).where(var1.shift(1).notna(), np.nan).rolling(YDAYS, min_periods=QDAYS).sum()


def f36_svas_244_kupiec_pof_stat_252d(close: pd.Series) -> pd.Series:
    """Kupiec POF likelihood-ratio test stat (target alpha=0.05) for VaR breach frequency over 252d.
    POF = -2 * [ln((1-p)^(T-x) * p^x) - ln((1-x/T)^(T-x) * (x/T)^x)]. ~chi^2(1)."""
    r = _log_returns(close)
    var5 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.05)
    breach = (r < var5.shift(1)).astype(float).where(var5.shift(1).notna(), np.nan)
    cnt = breach.rolling(YDAYS, min_periods=QDAYS).sum()
    T = YDAYS
    p = 0.05
    def _pof(x):
        if np.isnan(x):
            return np.nan
        x = float(x)
        if x <= 0 or x >= T:
            return 0.0
        pi = x / T
        lr_h0 = (T - x) * np.log(1.0 - p) + x * np.log(p)
        lr_h1 = (T - x) * np.log(1.0 - pi) + x * np.log(pi)
        return float(-2.0 * (lr_h0 - lr_h1))
    return cnt.apply(_pof)


def f36_svas_245_christoffersen_ind_stat_252d(close: pd.Series) -> pd.Series:
    """Christoffersen independence test stat for VaR-breach clustering over 252d.
    Compares P(breach_t | breach_{t-1}) to P(breach_t | no breach_{t-1}). ~chi^2(1)."""
    r = _log_returns(close)
    var5 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.05)
    breach = (r < var5.shift(1)).astype(float).where(var5.shift(1).notna(), np.nan)
    arr = breach.values
    n = len(arr)
    out = np.full(n, np.nan)
    for i in range(YDAYS - 1, n):
        lo = i - YDAYS + 1
        seg = arr[lo:i + 1]
        mask = ~np.isnan(seg)
        if mask.sum() < 30:
            continue
        seg = seg[mask].astype(int)
        if seg.size < 2:
            continue
        # transition counts
        n00 = n01 = n10 = n11 = 0
        for j in range(1, seg.size):
            a, b = seg[j - 1], seg[j]
            if a == 0 and b == 0: n00 += 1
            elif a == 0 and b == 1: n01 += 1
            elif a == 1 and b == 0: n10 += 1
            else: n11 += 1
            if n01 + n11 == 0 or n00 + n10 == 0:
                continue
        if (n00 + n01) == 0 or (n10 + n11) == 0 or (n01 + n11) == 0:
            continue
        pi01 = n01 / (n00 + n01) if (n00 + n01) > 0 else 0.0
        pi11 = n11 / (n10 + n11) if (n10 + n11) > 0 else 0.0
        pi = (n01 + n11) / (n00 + n01 + n10 + n11)
        if pi <= 0 or pi >= 1 or pi01 <= 0 or pi01 >= 1 or pi11 <= 0 or pi11 >= 1:
            continue
        l_h0 = (n00 + n10) * np.log(1.0 - pi) + (n01 + n11) * np.log(pi)
        l_h1 = (n00) * np.log(1.0 - pi01) + n01 * np.log(pi01) + n10 * np.log(1.0 - pi11) + n11 * np.log(pi11)
        out[i] = -2.0 * (l_h0 - l_h1)
    return pd.Series(out, index=close.index)


def f36_svas_246_max_consecutive_var_breaches_252d(close: pd.Series) -> pd.Series:
    """Max consecutive VaR(5%) breaches in trailing 252d — exceedance-clustering severity."""
    r = _log_returns(close)
    var5 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.05)
    breach = (r < var5.shift(1)).astype(float).where(var5.shift(1).notna(), np.nan)
    def _maxrun(w):
        v = w[~np.isnan(w)]
        if v.size < 21:
            return np.nan
        best = 0; cur = 0
        for x in v:
            if x > 0:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return float(best)
    return breach.rolling(YDAYS, min_periods=QDAYS).apply(_maxrun, raw=True)


# ============================================================
# Bucket DD — Conditional Drawdown at Risk (CDaR) (247-251)
# CDaR(alpha) = mean of the (alpha*N) worst drawdowns in the window.
# Chekhlov-Uryasev (2000): coherent risk measure for path-dependent risk.
# ============================================================

def _cdar_window(w: np.ndarray, alpha: float) -> float:
    v = w[~np.isnan(w)]
    if v.size < 21:
        return np.nan
    peak = np.maximum.accumulate(v)
    dd = 1.0 - v / peak   # >= 0
    k = max(1, int(np.ceil(alpha * v.size)))
    worst = np.sort(dd)[-k:]
    return float(worst.mean())


def f36_svas_247_cdar_5pct_252d(close: pd.Series) -> pd.Series:
    """CDaR at alpha=5% over 252d — mean of worst 5% drawdowns; coherent path-risk measure."""
    return close.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _cdar_window(w, 0.05), raw=True)


def f36_svas_248_cdar_10pct_252d(close: pd.Series) -> pd.Series:
    """CDaR at alpha=10% over 252d — mean of worst 10% drawdowns."""
    return close.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _cdar_window(w, 0.10), raw=True)


def f36_svas_249_cdar_5pct_504d(close: pd.Series) -> pd.Series:
    """CDaR at alpha=5% over 504d — biennial conditional drawdown at risk."""
    return close.rolling(DDAYS_2Y, min_periods=YDAYS).apply(lambda w: _cdar_window(w, 0.05), raw=True)


def f36_svas_250_cdar_ratio_252_over_504(close: pd.Series) -> pd.Series:
    """CDaR(5%)_252 / CDaR(5%)_504 — short-vs-long drawdown-concentration ratio."""
    c252 = close.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _cdar_window(w, 0.05), raw=True)
    c504 = close.rolling(DDAYS_2Y, min_periods=YDAYS).apply(lambda w: _cdar_window(w, 0.05), raw=True)
    return _safe_div(c252, c504)


def f36_svas_251_cdar_1pct_252d(close: pd.Series) -> pd.Series:
    """CDaR at alpha=1% over 252d — extreme-tail conditional drawdown measure."""
    return close.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _cdar_window(w, 0.01), raw=True)


# ============================================================
# Bucket EE — MAR ratios at multiple thresholds (252-256)
# MAR = minimum acceptable return. Sortino with different MAR.
# ============================================================

def _sortino_mar(close: pd.Series, mar: float, n: int, mp: int) -> pd.Series:
    r = _log_returns(close)
    excess = r - mar
    downside = excess.where(excess < 0, 0.0)
    mr = excess.rolling(n, min_periods=mp).mean()
    dd = np.sqrt((downside ** 2).rolling(n, min_periods=mp).mean())
    return _safe_div(mr, dd)


def f36_svas_252_sortino_mar_mean_252d(close: pd.Series) -> pd.Series:
    """Sortino with MAR = rolling 252d mean(r) — risk-adjusted return *above the typical*."""
    r = _log_returns(close)
    mr = r.rolling(YDAYS, min_periods=QDAYS).mean()
    excess = r - mr
    downside = excess.where(excess < 0, 0.0)
    num = excess.rolling(YDAYS, min_periods=QDAYS).mean()
    dd = np.sqrt((downside ** 2).rolling(YDAYS, min_periods=QDAYS).mean())
    return _safe_div(num, dd)


def f36_svas_253_sortino_mar_5pct_year_252d(close: pd.Series) -> pd.Series:
    """Sortino with MAR = 5%/year (log(1.05)/252 daily) over 252d — RF=5% style risk-adjusted return."""
    return _sortino_mar(close, np.log(1.05) / 252.0, YDAYS, QDAYS)


def f36_svas_254_sortino_mar_10pct_year_252d(close: pd.Series) -> pd.Series:
    """Sortino with MAR = 10%/year over 252d."""
    return _sortino_mar(close, np.log(1.10) / 252.0, YDAYS, QDAYS)


def f36_svas_255_mar_ratio_linear_downside_252d(close: pd.Series) -> pd.Series:
    """Mean(r) / mean(|r-|) over 252d — Bernardo-Ledoit gain/loss with raw magnitudes, sums-form."""
    r = _log_returns(close)
    mu = r.rolling(YDAYS, min_periods=QDAYS).mean()
    abs_neg = (-r).where(r < 0, 0.0).rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(mu, abs_neg)


def f36_svas_256_mar_ratio_linear_downside_504d(close: pd.Series) -> pd.Series:
    """Mean(r) / mean(|r-|) over 504d — biennial MAR-linear ratio."""
    r = _log_returns(close)
    mu = r.rolling(DDAYS_2Y, min_periods=YDAYS).mean()
    abs_neg = (-r).where(r < 0, 0.0).rolling(DDAYS_2Y, min_periods=YDAYS).mean()
    return _safe_div(mu, abs_neg)


# ============================================================
# Bucket FF — K-ratio (Kestner) (257-260)
# K-ratio = slope(cum log-return) / std-err(slope) * 1/sqrt(N). Measures
# how linearly a return stream grows — higher = smoother equity curve.
# ============================================================

def _k_ratio_window(w: np.ndarray) -> float:
    v = w[~np.isnan(w)]
    n = v.size
    if n < 30:
        return np.nan
    y = np.cumsum(v)
    x = np.arange(n, dtype=float)
    xm = x.mean(); ym = y.mean()
    sxx = ((x - xm) ** 2).sum()
    sxy = ((x - xm) * (y - ym)).sum()
    if sxx == 0:
        return np.nan
    b = sxy / sxx
    a = ym - b * xm
    resid = y - (a + b * x)
    s_resid = resid.std(ddof=2)
    if s_resid == 0:
        return np.nan
    se_b = s_resid / np.sqrt(sxx)
    if se_b == 0:
        return np.nan
    return float(b / se_b / np.sqrt(n))


def f36_svas_257_k_ratio_252d(close: pd.Series) -> pd.Series:
    """Kestner K-ratio over 252d — equity-curve linearity / smoothness."""
    r = _log_returns(close)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_k_ratio_window, raw=True)


def f36_svas_258_k_ratio_504d(close: pd.Series) -> pd.Series:
    """K-ratio over 504d — biennial equity-curve linearity."""
    r = _log_returns(close)
    return r.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_k_ratio_window, raw=True)


def f36_svas_259_k_ratio_1260d(close: pd.Series) -> pd.Series:
    """K-ratio over 1260d — 5y equity-curve linearity."""
    r = _log_returns(close)
    return r.rolling(DDAYS_5Y, min_periods=DDAYS_2Y).apply(_k_ratio_window, raw=True)


def f36_svas_260_k_ratio_zscore_in_1260d(close: pd.Series) -> pd.Series:
    """Z-score of 252d K-ratio in 1260d distribution — regime-relative path-linearity extremity."""
    r = _log_returns(close)
    kr = r.rolling(YDAYS, min_periods=QDAYS).apply(_k_ratio_window, raw=True)
    return _rolling_zscore(kr, DDAYS_5Y, min_periods=YDAYS)


# ============================================================
# Bucket GG — Recovery factor / new-high frequency (261-266)
# Recovery factor = total return / |max DD|. New-high freq = how often
# the stock prints fresh 252d highs.
# ============================================================

def _recovery_factor(close: pd.Series, n: int, mp: int) -> pd.Series:
    r = _log_returns(close)
    cum_ret = r.rolling(n, min_periods=mp).sum()
    def _mdd(w):
        v = w[~np.isnan(w)]
        if v.size < 5:
            return np.nan
        peak = np.maximum.accumulate(v)
        return float((1.0 - v / peak).max())
    mdd = close.rolling(n, min_periods=mp).apply(_mdd, raw=True)
    return _safe_div(cum_ret, mdd)


def f36_svas_261_recovery_factor_252d(close: pd.Series) -> pd.Series:
    """Total log return / |max DD| over 252d — annual recovery factor (Bacon)."""
    return _recovery_factor(close, YDAYS, QDAYS)


def f36_svas_262_recovery_factor_504d(close: pd.Series) -> pd.Series:
    """Recovery factor over 504d — biennial."""
    return _recovery_factor(close, DDAYS_2Y, YDAYS)


def f36_svas_263_recovery_factor_1260d(close: pd.Series) -> pd.Series:
    """Recovery factor over 1260d — 5y recovery measure."""
    return _recovery_factor(close, DDAYS_5Y, DDAYS_2Y)


def f36_svas_264_new_252d_high_count_252d(close: pd.Series) -> pd.Series:
    """Count of bars in trailing 252d that printed a new trailing-252d high — frequency of fresh highs."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    is_new = (close >= rmax)
    return is_new.astype(float).where(rmax.notna(), np.nan).rolling(YDAYS, min_periods=QDAYS).sum()


def f36_svas_265_bars_since_last_new_252d_high(close: pd.Series) -> pd.Series:
    """Bars since last new 252d high — staleness of the most recent fresh peak."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    is_new = (close >= rmax).values
    n = len(is_new)
    out = np.full(n, np.nan)
    last = -1
    for i in range(n):
        if not np.isnan(rmax.iat[i]) and is_new[i]:
            last = i
        if last >= 0 and not np.isnan(close.iat[i]):
            out[i] = float(i - last)
    return pd.Series(out, index=close.index)


def f36_svas_266_recovery_factor_zscore_in_1260d(close: pd.Series) -> pd.Series:
    """Z-score of 252d recovery factor in 1260d distribution — regime-relative recovery quality."""
    rf = _recovery_factor(close, YDAYS, QDAYS)
    return _rolling_zscore(rf, DDAYS_5Y, min_periods=YDAYS)


# ============================================================
# Bucket HH — L-moments (Hosking) skew & kurt (267-271)
# L-moments are linear combinations of order statistics. More robust than
# product moments to outliers.
# ============================================================

def _l_moments_window(w: np.ndarray):
    """Return (lambda1, lambda2, tau3=L-skew, tau4=L-kurt) for the window."""
    v = w[~np.isnan(w)]
    n = v.size
    if n < 21:
        return np.nan, np.nan, np.nan, np.nan
    x = np.sort(v)
    i = np.arange(1, n + 1, dtype=float)
    # PWMs (unbiased estimators)
    b0 = x.mean()
    b1 = ((i - 1.0) / (n - 1.0) * x).sum() / n
    b2 = ((i - 1.0) * (i - 2.0) / ((n - 1.0) * (n - 2.0)) * x).sum() / n
    b3 = ((i - 1.0) * (i - 2.0) * (i - 3.0) / ((n - 1.0) * (n - 2.0) * (n - 3.0)) * x).sum() / n
    l1 = b0
    l2 = 2.0 * b1 - b0
    l3 = 6.0 * b2 - 6.0 * b1 + b0
    l4 = 20.0 * b3 - 30.0 * b2 + 12.0 * b1 - b0
    if l2 == 0:
        return np.nan, np.nan, np.nan, np.nan
    return l1, l2, l3 / l2, l4 / l2


def f36_svas_267_l_skew_252d(close: pd.Series) -> pd.Series:
    """L-skewness (Hosking) over 252d — robust quantile-based skew (less outlier-sensitive than sample skew)."""
    r = _log_returns(close)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _l_moments_window(w)[2], raw=True)


def f36_svas_268_l_skew_504d(close: pd.Series) -> pd.Series:
    """L-skewness over 504d — biennial robust skew."""
    r = _log_returns(close)
    return r.rolling(DDAYS_2Y, min_periods=YDAYS).apply(lambda w: _l_moments_window(w)[2], raw=True)


def f36_svas_269_l_kurt_252d(close: pd.Series) -> pd.Series:
    """L-kurtosis (Hosking) over 252d — robust tail-thickness measure."""
    r = _log_returns(close)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _l_moments_window(w)[3], raw=True)


def f36_svas_270_l_kurt_504d(close: pd.Series) -> pd.Series:
    """L-kurtosis over 504d — biennial robust tail-thickness."""
    r = _log_returns(close)
    return r.rolling(DDAYS_2Y, min_periods=YDAYS).apply(lambda w: _l_moments_window(w)[3], raw=True)


def f36_svas_271_l_skew_minus_pearson_skew_252d(close: pd.Series) -> pd.Series:
    """L-skew - Pearson moment skew over 252d — disagreement between robust and moment-based skew (outlier signal)."""
    r = _log_returns(close)
    ls = r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _l_moments_window(w)[2], raw=True)
    ps = r.rolling(YDAYS, min_periods=QDAYS).skew()
    return ls - ps


# ============================================================
# Bucket II — Tail-cluster / consecutive-loss measures (272-278)
# ============================================================

def f36_svas_272_consecutive_1sigma_loss_pairs_252d(close: pd.Series) -> pd.Series:
    """Count of consecutive-bar pairs in 252d where BOTH r_{t-1} and r_t are < -1*sigma_lag — loss-cluster pairs."""
    r = _log_returns(close)
    sigma = r.rolling(YDAYS, min_periods=QDAYS).std().shift(1)
    bad = (r < -sigma).astype(float)
    pair = (bad * bad.shift(1)).where(sigma.notna(), np.nan)
    return pair.rolling(YDAYS, min_periods=QDAYS).sum()


def f36_svas_273_consecutive_2sigma_loss_pairs_252d(close: pd.Series) -> pd.Series:
    """Same as 272 but at -2 sigma threshold — extreme consecutive-loss pairs."""
    r = _log_returns(close)
    sigma = r.rolling(YDAYS, min_periods=QDAYS).std().shift(1)
    bad = (r < -2.0 * sigma).astype(float)
    pair = (bad * bad.shift(1)).where(sigma.notna(), np.nan)
    return pair.rolling(YDAYS, min_periods=QDAYS).sum()


def f36_svas_274_conditional_sharpe_after_loss_252d(close: pd.Series) -> pd.Series:
    """Sharpe ratio of r_t on bars where r_{t-1} < 0 over 252d — momentum/mean-reversion after losses."""
    r = _log_returns(close)
    sub = r.where(r.shift(1) < 0)
    return sub.rolling(YDAYS, min_periods=QDAYS).apply(_sharpe_window, raw=True)


def f36_svas_275_conditional_sharpe_after_gain_252d(close: pd.Series) -> pd.Series:
    """Sharpe ratio of r_t on bars where r_{t-1} > 0 over 252d — momentum/mean-reversion after gains."""
    r = _log_returns(close)
    sub = r.where(r.shift(1) > 0)
    return sub.rolling(YDAYS, min_periods=QDAYS).apply(_sharpe_window, raw=True)


def f36_svas_276_mean_negative_cluster_size_252d(close: pd.Series) -> pd.Series:
    """Mean size of consecutive-negative-return clusters in 252d — typical loss-cluster length."""
    r = _log_returns(close)
    def _mean_cluster(w):
        v = w[~np.isnan(w)]
        if v.size < 21:
            return np.nan
        clusters = []; cur = 0
        for x in v:
            if x < 0:
                cur += 1
            else:
                if cur > 0:
                    clusters.append(cur); cur = 0
        if cur > 0:
            clusters.append(cur)
        return float(np.mean(clusters)) if clusters else 0.0
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_mean_cluster, raw=True)


def f36_svas_277_bars_since_last_loss_cluster_end_252d(close: pd.Series) -> pd.Series:
    """Bars since the end of the last consecutive-negative-return cluster (length >= 3) in trailing 252d."""
    r = _log_returns(close)
    arr = r.values
    n = arr.size
    out = np.full(n, np.nan)
    cur = 0
    last_end = -1
    for i in range(n):
        v = arr[i]
        if np.isnan(v):
            continue
        if v < 0:
            cur += 1
        else:
            if cur >= 3:
                last_end = i - 1
            cur = 0
        if last_end >= 0:
            out[i] = float(i - last_end)
    return pd.Series(out, index=close.index)


def f36_svas_278_markov_p_loss_loss_minus_p_gain_gain_252d(close: pd.Series) -> pd.Series:
    """P(r_t<0 | r_{t-1}<0) - P(r_t>0 | r_{t-1}>0) over 252d — sign-persistence asymmetry from Markov transitions."""
    r = _log_returns(close)
    rl = r.shift(1)
    pl = ((r < 0).astype(float).where(rl < 0)).rolling(YDAYS, min_periods=QDAYS).sum()
    nl = ((rl < 0).astype(float)).rolling(YDAYS, min_periods=QDAYS).sum()
    pg = ((r > 0).astype(float).where(rl > 0)).rolling(YDAYS, min_periods=QDAYS).sum()
    ng = ((rl > 0).astype(float)).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(pl, nl) - _safe_div(pg, ng)


# ============================================================
# Bucket JJ — Drawdown survival / hazard / recovery probability (279-283)
# ============================================================

def f36_svas_279_dd_hazard_rate_252d(close: pd.Series) -> pd.Series:
    """Empirical hazard rate of NEW drawdown events in trailing 252d (count distinct DD-starts / window-length)."""
    peak = close.cummax()
    in_dd = close < peak
    new_dd = in_dd & (~in_dd.shift(1, fill_value=False))
    return new_dd.astype(float).where(peak.notna(), np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f36_svas_280_empirical_p_dd20_in_next_252d(close: pd.Series) -> pd.Series:
    """Empirical P(drawdown depth > 20% in trailing 504d window | at peak at start) — historical KM-style estimate.
    Approx: number of bars where DD>20% / total bars in last 504d. PIT — uses only past data."""
    peak = close.cummax()
    dd = 1.0 - close / peak
    deep = (dd > 0.20).astype(float).where(peak.notna(), np.nan)
    return deep.rolling(DDAYS_2Y, min_periods=YDAYS).mean()


def f36_svas_281_empirical_p_dd50_in_504d(close: pd.Series) -> pd.Series:
    """Empirical P(DD > 50% in trailing 504d) — base rate for severe drawdowns. Stuck-peak label proxy."""
    peak = close.cummax()
    dd = 1.0 - close / peak
    deep = (dd > 0.50).astype(float).where(peak.notna(), np.nan)
    return deep.rolling(DDAYS_2Y, min_periods=YDAYS).mean()


def f36_svas_282_mean_time_to_recovery_504d(close: pd.Series) -> pd.Series:
    """Mean bars-to-recovery for completed drawdowns in trailing 504d. Measures typical bounce-back speed."""
    def _mttr(w):
        v = w[~np.isnan(w)]
        if v.size < 60:
            return np.nan
        peak = np.maximum.accumulate(v)
        dd = 1.0 - v / peak
        recoveries = []
        in_dd = False; start = 0; trough_dd = 0.0
        for i, d in enumerate(dd):
            if d > 0 and not in_dd:
                in_dd = True; start = i; trough_dd = d
            elif d > trough_dd:
                trough_dd = d
            elif d == 0 and in_dd:
                recoveries.append(i - start)
                in_dd = False
        return float(np.mean(recoveries)) if recoveries else np.nan
    return close.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_mttr, raw=True)


def f36_svas_283_survival_probability_within_10pct_252d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 252d where DD stays within -10% of peak — calm-survival share."""
    peak = close.cummax()
    dd = 1.0 - close / peak
    within = (dd < 0.10).astype(float).where(peak.notna(), np.nan)
    return within.rolling(YDAYS, min_periods=QDAYS).mean()


# ============================================================
# Bucket KK — Underwater-curve statistics (284-289)
# Treat the underwater curve itself as a time-series; compute moments.
# ============================================================

def f36_svas_284_std_underwater_252d(close: pd.Series) -> pd.Series:
    """Std of underwater curve over 252d — variability of drawdown depth."""
    uw = _underwater(close)
    return uw.rolling(YDAYS, min_periods=QDAYS).std()


def f36_svas_285_skew_underwater_252d(close: pd.Series) -> pd.Series:
    """Skewness of underwater curve over 252d — positive = occasional deep drawdowns."""
    uw = _underwater(close)
    return uw.rolling(YDAYS, min_periods=QDAYS).skew()


def f36_svas_286_kurt_underwater_252d(close: pd.Series) -> pd.Series:
    """Kurtosis of underwater curve over 252d — fat-tailed drawdown distribution."""
    uw = _underwater(close)
    return uw.rolling(YDAYS, min_periods=QDAYS).kurt()


def f36_svas_287_hurst_underwater_504d(close: pd.Series) -> pd.Series:
    """R/S Hurst exponent of underwater curve over 504d — long memory of drawdowns; >0.5 = trending DDs."""
    uw = _underwater(close)
    def _h(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        mean = v.mean()
        devs = np.cumsum(v - mean)
        R = devs.max() - devs.min()
        S = v.std(ddof=1)
        if S == 0 or R == 0:
            return np.nan
        return float(np.log(R / S) / np.log(v.size))
    return uw.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_h, raw=True)


def f36_svas_288_underwater_auc_over_max_dd_252d(close: pd.Series) -> pd.Series:
    """Area under underwater curve / max underwater depth over 252d — pain-concentration index."""
    uw = _underwater(close)
    auc = uw.rolling(YDAYS, min_periods=QDAYS).sum()
    mdd = uw.rolling(YDAYS, min_periods=QDAYS).max()
    return _safe_div(auc, mdd)


def f36_svas_289_underwater_autocorr_lag21_252d(close: pd.Series) -> pd.Series:
    """Autocorrelation of underwater curve at lag 21 over 252d — monthly-spaced DD persistence."""
    uw = _underwater(close)
    pairs = pd.concat([uw.shift(21).rename("ul"), uw.rename("u")], axis=1)
    return pairs["ul"].rolling(YDAYS, min_periods=QDAYS).corr(pairs["u"])


# ============================================================
# Bucket LL — Stuck-peak label-proxy composites (290-300)
# Targeted directly at the label: stocks that touch -80% and don't recover above -50% in 5y.
# ============================================================

def f36_svas_290_dd_dynamics_composite_252d(close: pd.Series) -> pd.Series:
    """Z-blend of DD velocity + DD acceleration + max single-day DD increase — drawdown-dynamics severity."""
    uw = _underwater(close)
    vel = _rolling_slope(uw, MDAYS)
    acc = _rolling_slope(vel, MDAYS)
    msi = uw.diff().rolling(YDAYS, min_periods=QDAYS).max()
    z_v = _rolling_zscore(vel, DDAYS_2Y, min_periods=YDAYS)
    z_a = _rolling_zscore(acc, DDAYS_2Y, min_periods=YDAYS)
    z_m = _rolling_zscore(msi, DDAYS_2Y, min_periods=YDAYS)
    return (z_v + z_a + z_m) / 3.0


def f36_svas_291_risk_adjusted_quality_composite_252d(close: pd.Series) -> pd.Series:
    """Z-blend of (Pezier-White adj-Sharpe) + PSR + (K-ratio) — overall path-quality composite."""
    r = _log_returns(close)
    def _adj(w):
        v = w[~np.isnan(w)]
        if v.size < 30: return np.nan
        mu = v.mean(); sd = v.std(ddof=1)
        if sd == 0: return np.nan
        sr = mu / sd
        S = ((v - mu) ** 3).mean() / sd ** 3
        K = ((v - mu) ** 4).mean() / sd ** 4
        return float(sr * (1.0 + (S / 6.0) * sr - ((K - 3.0) / 24.0) * sr ** 2))
    adj = r.rolling(YDAYS, min_periods=QDAYS).apply(_adj, raw=True)
    def _psr(w):
        v = w[~np.isnan(w)]
        n = v.size
        if n < 30: return np.nan
        mu = v.mean(); sd = v.std(ddof=1)
        if sd == 0: return np.nan
        sr = mu / sd
        S = ((v - mu) ** 3).mean() / sd ** 3
        K = ((v - mu) ** 4).mean() / sd ** 4
        var_sr = (1.0 - S * sr + ((K - 1.0) / 4.0) * sr ** 2) / (n - 1.0)
        if var_sr <= 0: return np.nan
        z = sr / np.sqrt(var_sr)
        return float(0.5 * (1.0 + np.tanh(0.7978845608028654 * (z + 0.044715 * z ** 3))))
    psr = r.rolling(YDAYS, min_periods=QDAYS).apply(_psr, raw=True)
    kr = r.rolling(YDAYS, min_periods=QDAYS).apply(_k_ratio_window, raw=True)
    z_adj = _rolling_zscore(adj, DDAYS_2Y, min_periods=YDAYS)
    z_psr = _rolling_zscore(psr, DDAYS_2Y, min_periods=YDAYS)
    z_kr = _rolling_zscore(kr, DDAYS_2Y, min_periods=YDAYS)
    return (z_adj + z_psr + z_kr) / 3.0


def f36_svas_292_tail_concentration_composite_252d(close: pd.Series) -> pd.Series:
    """Z-blend of CDaR(5%) + Ulcer + Pain-index — composite of drawdown depth and persistence."""
    cdar = close.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _cdar_window(w, 0.05), raw=True)
    def _u(w):
        v = w[~np.isnan(w)]
        if v.size < 21: return np.nan
        peak = np.maximum.accumulate(v)
        dd = 1.0 - v / peak
        return float(np.sqrt((dd ** 2).mean()))
    ulc = close.rolling(YDAYS, min_periods=QDAYS).apply(_u, raw=True)
    def _p(w):
        v = w[~np.isnan(w)]
        if v.size < 21: return np.nan
        peak = np.maximum.accumulate(v)
        return float((1.0 - v / peak).mean())
    pn = close.rolling(YDAYS, min_periods=QDAYS).apply(_p, raw=True)
    z_c = _rolling_zscore(cdar, DDAYS_2Y, min_periods=YDAYS)
    z_u = _rolling_zscore(ulc, DDAYS_2Y, min_periods=YDAYS)
    z_p = _rolling_zscore(pn, DDAYS_2Y, min_periods=YDAYS)
    return (z_c + z_u + z_p) / 3.0


def f36_svas_293_loss_cluster_persistence_composite_252d(close: pd.Series) -> pd.Series:
    """Z-blend of consecutive-2sigma-loss pairs + mean-neg-cluster-size + Markov P(loss|loss)-P(gain|gain) —
    composite of bad-news persistence."""
    r = _log_returns(close)
    sigma = r.rolling(YDAYS, min_periods=QDAYS).std().shift(1)
    bad2 = (r < -2.0 * sigma).astype(float)
    pair2 = (bad2 * bad2.shift(1)).where(sigma.notna(), np.nan).rolling(YDAYS, min_periods=QDAYS).sum()
    def _mc(w):
        v = w[~np.isnan(w)]
        if v.size < 21: return np.nan
        cs = []; cur = 0
        for x in v:
            if x < 0: cur += 1
            else:
                if cur > 0: cs.append(cur); cur = 0
        if cur > 0: cs.append(cur)
        return float(np.mean(cs)) if cs else 0.0
    mcs = r.rolling(YDAYS, min_periods=QDAYS).apply(_mc, raw=True)
    rl = r.shift(1)
    pl = ((r < 0).astype(float).where(rl < 0)).rolling(YDAYS, min_periods=QDAYS).sum()
    nl = ((rl < 0).astype(float)).rolling(YDAYS, min_periods=QDAYS).sum()
    pg = ((r > 0).astype(float).where(rl > 0)).rolling(YDAYS, min_periods=QDAYS).sum()
    ng = ((rl > 0).astype(float)).rolling(YDAYS, min_periods=QDAYS).sum()
    diff = _safe_div(pl, nl) - _safe_div(pg, ng)
    z_p = _rolling_zscore(pair2, DDAYS_2Y, min_periods=YDAYS)
    z_m = _rolling_zscore(mcs, DDAYS_2Y, min_periods=YDAYS)
    z_d = _rolling_zscore(diff, DDAYS_2Y, min_periods=YDAYS)
    return (z_p + z_m + z_d) / 3.0


def f36_svas_294_p_stuck_proxy_score_504d(close: pd.Series) -> pd.Series:
    """Probability-of-stuck proxy: P(DD>50% in 504d) * underwater fraction 252d — direct label-style score."""
    peak = close.cummax()
    dd = 1.0 - close / peak
    deep = (dd > 0.50).astype(float).where(peak.notna(), np.nan)
    p_dd50 = deep.rolling(DDAYS_2Y, min_periods=YDAYS).mean()
    uw_frac = ((close < peak).astype(float).where(peak.notna(), np.nan)).rolling(YDAYS, min_periods=QDAYS).mean()
    return p_dd50 * uw_frac


def f36_svas_295_recovery_unlikely_composite_504d(close: pd.Series) -> pd.Series:
    """Z-blend of recovery factor (negated) + mean-time-to-recovery + survival-within-10pct (negated) —
    high = recovery is unlikely / slow."""
    rf = _recovery_factor(close, DDAYS_2Y, YDAYS)
    def _mttr(w):
        v = w[~np.isnan(w)]
        if v.size < 60: return np.nan
        peak = np.maximum.accumulate(v)
        dd = 1.0 - v / peak
        recs = []; in_dd = False; start = 0; td = 0.0
        for i, d in enumerate(dd):
            if d > 0 and not in_dd:
                in_dd = True; start = i; td = d
            elif d > td: td = d
            elif d == 0 and in_dd:
                recs.append(i - start); in_dd = False
        return float(np.mean(recs)) if recs else np.nan
    mttr = close.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_mttr, raw=True)
    peak = close.cummax()
    dd = 1.0 - close / peak
    surv = (dd < 0.10).astype(float).where(peak.notna(), np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    z_r = _rolling_zscore(-rf, DDAYS_5Y, min_periods=YDAYS)
    z_m = _rolling_zscore(mttr, DDAYS_5Y, min_periods=YDAYS)
    z_s = _rolling_zscore(-surv, DDAYS_5Y, min_periods=YDAYS)
    return (z_r + z_m + z_s) / 3.0


def f36_svas_296_tail_asymmetry_severity_composite_252d(close: pd.Series) -> pd.Series:
    """Z-blend of L-skew (negated, more-negative = more left-skewed) + L-kurt + tail-magnitude-asym —
    composite of distributional left-tail-dominance."""
    r = _log_returns(close)
    ls = r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _l_moments_window(w)[2], raw=True)
    lk = r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _l_moments_window(w)[3], raw=True)
    ql = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.05)
    qh = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    tail_asym = ql.abs() - qh
    z_ls = _rolling_zscore(-ls, DDAYS_2Y, min_periods=YDAYS)
    z_lk = _rolling_zscore(lk, DDAYS_2Y, min_periods=YDAYS)
    z_ta = _rolling_zscore(tail_asym, DDAYS_2Y, min_periods=YDAYS)
    return (z_ls + z_lk + z_ta) / 3.0


def f36_svas_297_var_breach_severity_composite_252d(close: pd.Series) -> pd.Series:
    """Z-blend of VaR(5%) breach count + VaR(1%) breach count + max consecutive breaches — risk-model-failure severity."""
    r = _log_returns(close)
    var5 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.05)
    var1 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.01)
    b5 = (r < var5.shift(1)).astype(float).where(var5.shift(1).notna(), np.nan)
    b1 = (r < var1.shift(1)).astype(float).where(var1.shift(1).notna(), np.nan)
    c5 = b5.rolling(YDAYS, min_periods=QDAYS).sum()
    c1 = b1.rolling(YDAYS, min_periods=QDAYS).sum()
    def _maxrun(w):
        v = w[~np.isnan(w)]
        if v.size < 21: return np.nan
        best = 0; cur = 0
        for x in v:
            if x > 0: cur += 1; best = max(best, cur)
            else: cur = 0
        return float(best)
    mc = b5.rolling(YDAYS, min_periods=QDAYS).apply(_maxrun, raw=True)
    z_c5 = _rolling_zscore(c5, DDAYS_2Y, min_periods=YDAYS)
    z_c1 = _rolling_zscore(c1, DDAYS_2Y, min_periods=YDAYS)
    z_mc = _rolling_zscore(mc, DDAYS_2Y, min_periods=YDAYS)
    return (z_c5 + z_c1 + z_mc) / 3.0


def f36_svas_298_uw_curve_pathology_composite_252d(close: pd.Series) -> pd.Series:
    """Z-blend of underwater std + underwater skew + underwater Hurst — composite of pathological DD-curve shape."""
    uw = _underwater(close)
    us = uw.rolling(YDAYS, min_periods=QDAYS).std()
    usk = uw.rolling(YDAYS, min_periods=QDAYS).skew()
    def _h(w):
        v = w[~np.isnan(w)]
        if v.size < 30: return np.nan
        m = v.mean(); d = np.cumsum(v - m)
        R = d.max() - d.min(); S = v.std(ddof=1)
        if S == 0 or R == 0: return np.nan
        return float(np.log(R / S) / np.log(v.size))
    uh = uw.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_h, raw=True)
    z_us = _rolling_zscore(us, DDAYS_2Y, min_periods=YDAYS)
    z_usk = _rolling_zscore(usk, DDAYS_2Y, min_periods=YDAYS)
    z_uh = _rolling_zscore(uh, DDAYS_5Y, min_periods=YDAYS)
    return (z_us + z_usk + z_uh) / 3.0


def f36_svas_299_post_peak_decline_intensity_252d(close: pd.Series) -> pd.Series:
    """Slope of underwater curve evaluated only on bars within 60 days after a 252d-window high — peak-aftermath decline rate."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    is_new_high = (close >= rmax)
    arr = is_new_high.values
    n = len(arr)
    bars_since_peak = np.full(n, np.nan)
    last_peak = -1
    for i in range(n):
        if not np.isnan(close.iat[i]) and arr[i]:
            last_peak = i
        if last_peak >= 0:
            bars_since_peak[i] = float(i - last_peak)
    bsp = pd.Series(bars_since_peak, index=close.index)
    uw = _underwater(close)
    slope = _rolling_slope(uw, MDAYS)
    return slope.where(bsp < 60, np.nan)


def f36_svas_300_final_stuck_peak_composite_504d(close: pd.Series) -> pd.Series:
    """Master composite: blend of dd_dynamics + recovery_unlikely + tail_asymmetry + p_stuck_proxy.
    Designed as a direct stuck-peak proxy signal. Components z-scored over 504d (min 63 obs)
    and averaged with skipna so the composite is defined whenever ANY component is."""
    uw = _underwater(close)
    vel = _rolling_slope(uw, MDAYS)
    acc = _rolling_slope(vel, MDAYS)
    z_v = _rolling_zscore(vel, DDAYS_2Y, min_periods=QDAYS)
    z_a = _rolling_zscore(acc, DDAYS_2Y, min_periods=QDAYS)
    peak = close.cummax()
    dd = 1.0 - close / peak
    uw_frac = ((close < peak).astype(float).where(peak.notna(), np.nan)).rolling(DDAYS_2Y, min_periods=YDAYS).mean()
    z_uw = _rolling_zscore(uw_frac, DDAYS_2Y, min_periods=QDAYS)
    r = _log_returns(close)
    ls = r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _l_moments_window(w)[2], raw=True)
    z_ls = _rolling_zscore(-ls, DDAYS_2Y, min_periods=QDAYS)
    deep = (dd > 0.50).astype(float).where(peak.notna(), np.nan)
    p_dd50 = deep.rolling(DDAYS_2Y, min_periods=YDAYS).mean()
    z_p = _rolling_zscore(p_dd50, DDAYS_2Y, min_periods=QDAYS)
    pieces = pd.concat([z_v.rename("v"), z_a.rename("a"), z_uw.rename("u"), z_ls.rename("l"), z_p.rename("p")], axis=1)
    return pieces.mean(axis=1, skipna=True)


# ============================================================
#                         REGISTRY 226-300
# ============================================================

SEMI_VARIANCE_ASYMMETRY_BASE_REGISTRY_226_300 = {
    "f36_svas_226_dd_velocity_21d": {"inputs": ["close"], "func": f36_svas_226_dd_velocity_21d},
    "f36_svas_227_dd_velocity_63d": {"inputs": ["close"], "func": f36_svas_227_dd_velocity_63d},
    "f36_svas_228_dd_acceleration_21d": {"inputs": ["close"], "func": f36_svas_228_dd_acceleration_21d},
    "f36_svas_229_dd_acceleration_63d": {"inputs": ["close"], "func": f36_svas_229_dd_acceleration_63d},
    "f36_svas_230_new_low_count_252d": {"inputs": ["close"], "func": f36_svas_230_new_low_count_252d},
    "f36_svas_231_max_single_day_dd_increase_252d": {"inputs": ["close"], "func": f36_svas_231_max_single_day_dd_increase_252d},
    "f36_svas_232_time_from_peak_to_trough_in_252d": {"inputs": ["close"], "func": f36_svas_232_time_from_peak_to_trough_in_252d},
    "f36_svas_233_dd_velocity_zscore_in_504d": {"inputs": ["close"], "func": f36_svas_233_dd_velocity_zscore_in_504d},
    "f36_svas_234_sharpe_21d": {"inputs": ["close"], "func": f36_svas_234_sharpe_21d},
    "f36_svas_235_sharpe_63d": {"inputs": ["close"], "func": f36_svas_235_sharpe_63d},
    "f36_svas_236_sharpe_504d": {"inputs": ["close"], "func": f36_svas_236_sharpe_504d},
    "f36_svas_237_pezier_white_adjusted_sharpe_252d": {"inputs": ["close"], "func": f36_svas_237_pezier_white_adjusted_sharpe_252d},
    "f36_svas_238_probabilistic_sharpe_ratio_252d": {"inputs": ["close"], "func": f36_svas_238_probabilistic_sharpe_ratio_252d},
    "f36_svas_239_lo_autocorr_adjusted_sharpe_252d": {"inputs": ["close"], "func": f36_svas_239_lo_autocorr_adjusted_sharpe_252d},
    "f36_svas_240_sharpe_zscore_in_1260d": {"inputs": ["close"], "func": f36_svas_240_sharpe_zscore_in_1260d},
    "f36_svas_241_var5_exceedance_count_252d": {"inputs": ["close"], "func": f36_svas_241_var5_exceedance_count_252d},
    "f36_svas_242_var5_exceedance_rate_252d": {"inputs": ["close"], "func": f36_svas_242_var5_exceedance_rate_252d},
    "f36_svas_243_var1_exceedance_count_252d": {"inputs": ["close"], "func": f36_svas_243_var1_exceedance_count_252d},
    "f36_svas_244_kupiec_pof_stat_252d": {"inputs": ["close"], "func": f36_svas_244_kupiec_pof_stat_252d},
    "f36_svas_245_christoffersen_ind_stat_252d": {"inputs": ["close"], "func": f36_svas_245_christoffersen_ind_stat_252d},
    "f36_svas_246_max_consecutive_var_breaches_252d": {"inputs": ["close"], "func": f36_svas_246_max_consecutive_var_breaches_252d},
    "f36_svas_247_cdar_5pct_252d": {"inputs": ["close"], "func": f36_svas_247_cdar_5pct_252d},
    "f36_svas_248_cdar_10pct_252d": {"inputs": ["close"], "func": f36_svas_248_cdar_10pct_252d},
    "f36_svas_249_cdar_5pct_504d": {"inputs": ["close"], "func": f36_svas_249_cdar_5pct_504d},
    "f36_svas_250_cdar_ratio_252_over_504": {"inputs": ["close"], "func": f36_svas_250_cdar_ratio_252_over_504},
    "f36_svas_251_cdar_1pct_252d": {"inputs": ["close"], "func": f36_svas_251_cdar_1pct_252d},
    "f36_svas_252_sortino_mar_mean_252d": {"inputs": ["close"], "func": f36_svas_252_sortino_mar_mean_252d},
    "f36_svas_253_sortino_mar_5pct_year_252d": {"inputs": ["close"], "func": f36_svas_253_sortino_mar_5pct_year_252d},
    "f36_svas_254_sortino_mar_10pct_year_252d": {"inputs": ["close"], "func": f36_svas_254_sortino_mar_10pct_year_252d},
    "f36_svas_255_mar_ratio_linear_downside_252d": {"inputs": ["close"], "func": f36_svas_255_mar_ratio_linear_downside_252d},
    "f36_svas_256_mar_ratio_linear_downside_504d": {"inputs": ["close"], "func": f36_svas_256_mar_ratio_linear_downside_504d},
    "f36_svas_257_k_ratio_252d": {"inputs": ["close"], "func": f36_svas_257_k_ratio_252d},
    "f36_svas_258_k_ratio_504d": {"inputs": ["close"], "func": f36_svas_258_k_ratio_504d},
    "f36_svas_259_k_ratio_1260d": {"inputs": ["close"], "func": f36_svas_259_k_ratio_1260d},
    "f36_svas_260_k_ratio_zscore_in_1260d": {"inputs": ["close"], "func": f36_svas_260_k_ratio_zscore_in_1260d},
    "f36_svas_261_recovery_factor_252d": {"inputs": ["close"], "func": f36_svas_261_recovery_factor_252d},
    "f36_svas_262_recovery_factor_504d": {"inputs": ["close"], "func": f36_svas_262_recovery_factor_504d},
    "f36_svas_263_recovery_factor_1260d": {"inputs": ["close"], "func": f36_svas_263_recovery_factor_1260d},
    "f36_svas_264_new_252d_high_count_252d": {"inputs": ["close"], "func": f36_svas_264_new_252d_high_count_252d},
    "f36_svas_265_bars_since_last_new_252d_high": {"inputs": ["close"], "func": f36_svas_265_bars_since_last_new_252d_high},
    "f36_svas_266_recovery_factor_zscore_in_1260d": {"inputs": ["close"], "func": f36_svas_266_recovery_factor_zscore_in_1260d},
    "f36_svas_267_l_skew_252d": {"inputs": ["close"], "func": f36_svas_267_l_skew_252d},
    "f36_svas_268_l_skew_504d": {"inputs": ["close"], "func": f36_svas_268_l_skew_504d},
    "f36_svas_269_l_kurt_252d": {"inputs": ["close"], "func": f36_svas_269_l_kurt_252d},
    "f36_svas_270_l_kurt_504d": {"inputs": ["close"], "func": f36_svas_270_l_kurt_504d},
    "f36_svas_271_l_skew_minus_pearson_skew_252d": {"inputs": ["close"], "func": f36_svas_271_l_skew_minus_pearson_skew_252d},
    "f36_svas_272_consecutive_1sigma_loss_pairs_252d": {"inputs": ["close"], "func": f36_svas_272_consecutive_1sigma_loss_pairs_252d},
    "f36_svas_273_consecutive_2sigma_loss_pairs_252d": {"inputs": ["close"], "func": f36_svas_273_consecutive_2sigma_loss_pairs_252d},
    "f36_svas_274_conditional_sharpe_after_loss_252d": {"inputs": ["close"], "func": f36_svas_274_conditional_sharpe_after_loss_252d},
    "f36_svas_275_conditional_sharpe_after_gain_252d": {"inputs": ["close"], "func": f36_svas_275_conditional_sharpe_after_gain_252d},
    "f36_svas_276_mean_negative_cluster_size_252d": {"inputs": ["close"], "func": f36_svas_276_mean_negative_cluster_size_252d},
    "f36_svas_277_bars_since_last_loss_cluster_end_252d": {"inputs": ["close"], "func": f36_svas_277_bars_since_last_loss_cluster_end_252d},
    "f36_svas_278_markov_p_loss_loss_minus_p_gain_gain_252d": {"inputs": ["close"], "func": f36_svas_278_markov_p_loss_loss_minus_p_gain_gain_252d},
    "f36_svas_279_dd_hazard_rate_252d": {"inputs": ["close"], "func": f36_svas_279_dd_hazard_rate_252d},
    "f36_svas_280_empirical_p_dd20_in_next_252d": {"inputs": ["close"], "func": f36_svas_280_empirical_p_dd20_in_next_252d},
    "f36_svas_281_empirical_p_dd50_in_504d": {"inputs": ["close"], "func": f36_svas_281_empirical_p_dd50_in_504d},
    "f36_svas_282_mean_time_to_recovery_504d": {"inputs": ["close"], "func": f36_svas_282_mean_time_to_recovery_504d},
    "f36_svas_283_survival_probability_within_10pct_252d": {"inputs": ["close"], "func": f36_svas_283_survival_probability_within_10pct_252d},
    "f36_svas_284_std_underwater_252d": {"inputs": ["close"], "func": f36_svas_284_std_underwater_252d},
    "f36_svas_285_skew_underwater_252d": {"inputs": ["close"], "func": f36_svas_285_skew_underwater_252d},
    "f36_svas_286_kurt_underwater_252d": {"inputs": ["close"], "func": f36_svas_286_kurt_underwater_252d},
    "f36_svas_287_hurst_underwater_504d": {"inputs": ["close"], "func": f36_svas_287_hurst_underwater_504d},
    "f36_svas_288_underwater_auc_over_max_dd_252d": {"inputs": ["close"], "func": f36_svas_288_underwater_auc_over_max_dd_252d},
    "f36_svas_289_underwater_autocorr_lag21_252d": {"inputs": ["close"], "func": f36_svas_289_underwater_autocorr_lag21_252d},
    "f36_svas_290_dd_dynamics_composite_252d": {"inputs": ["close"], "func": f36_svas_290_dd_dynamics_composite_252d},
    "f36_svas_291_risk_adjusted_quality_composite_252d": {"inputs": ["close"], "func": f36_svas_291_risk_adjusted_quality_composite_252d},
    "f36_svas_292_tail_concentration_composite_252d": {"inputs": ["close"], "func": f36_svas_292_tail_concentration_composite_252d},
    "f36_svas_293_loss_cluster_persistence_composite_252d": {"inputs": ["close"], "func": f36_svas_293_loss_cluster_persistence_composite_252d},
    "f36_svas_294_p_stuck_proxy_score_504d": {"inputs": ["close"], "func": f36_svas_294_p_stuck_proxy_score_504d},
    "f36_svas_295_recovery_unlikely_composite_504d": {"inputs": ["close"], "func": f36_svas_295_recovery_unlikely_composite_504d},
    "f36_svas_296_tail_asymmetry_severity_composite_252d": {"inputs": ["close"], "func": f36_svas_296_tail_asymmetry_severity_composite_252d},
    "f36_svas_297_var_breach_severity_composite_252d": {"inputs": ["close"], "func": f36_svas_297_var_breach_severity_composite_252d},
    "f36_svas_298_uw_curve_pathology_composite_252d": {"inputs": ["close"], "func": f36_svas_298_uw_curve_pathology_composite_252d},
    "f36_svas_299_post_peak_decline_intensity_252d": {"inputs": ["close"], "func": f36_svas_299_post_peak_decline_intensity_252d},
    "f36_svas_300_final_stuck_peak_composite_504d": {"inputs": ["close"], "func": f36_svas_300_final_stuck_peak_composite_504d},
}
