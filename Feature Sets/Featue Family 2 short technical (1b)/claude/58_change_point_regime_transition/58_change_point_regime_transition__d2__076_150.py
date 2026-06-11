"""change_point_regime_transition d2 076-150 - 1b-technical."""
import numpy as np
import pandas as pd

YDAYS = 252; QDAYS = 63; MDAYS = 21; WDAYS = 5
DDAYS_2Y = 504; DDAYS_3Y = 756; DDAYS_5Y = 1260


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
        num = ((x - xm) * (wv - wm)).sum(); den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)


def _sma(s, n, mp=None):
    if mp is None: mp = max(n // 3, 2)
    return s.rolling(n, min_periods=mp).mean()


def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=max(n // 3, 2)).mean()


def _log_ret(close):
    return _safe_log(close).diff()


def _rolling_q(s, n, q, min_periods=None):
    if min_periods is None: min_periods = max(n // 3, 10)
    return s.rolling(n, min_periods=min_periods).quantile(q)


def _bars_since_last_event(ind):
    arr = ind.values; nb = len(arr); out = np.full(nb, np.nan, dtype=float); last = -1
    for i in range(nb):
        if not np.isnan(arr[i]) and arr[i] > 0.5:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=ind.index)


def _rsi(close, n=14):
    d = close.diff()
    up = d.clip(lower=0.0); dn = (-d).clip(lower=0.0)
    a = up.ewm(alpha=1.0/n, adjust=False, min_periods=n).mean()
    b = dn.ewm(alpha=1.0/n, adjust=False, min_periods=n).mean().replace(0, np.nan)
    return 100.0 - 100.0 / (1.0 + a / b)


def _obv(close, volume):
    return (np.sign(close.diff()).fillna(0.0) * volume).cumsum()


def _macd(close, fast=12, slow=26):
    return _ema(close, fast) - _ema(close, slow)

def _cusum_pos(s, n, k=0.0):
    """Positive CUSUM: max running sum of (x - mean - k) over n. Reset at zero."""
    mp = max(n // 3, 20)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 20: return np.nan
        mu = v.mean()
        cs = 0.0; mx = 0.0
        for x in v:
            cs = max(0.0, cs + (x - mu - k))
            if cs > mx: mx = cs
        return float(mx)
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _cusum_neg(s, n, k=0.0):
    """Negative CUSUM: max accumulated decrease."""
    mp = max(n // 3, 20)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 20: return np.nan
        mu = v.mean()
        cs = 0.0; mx = 0.0
        for x in v:
            cs = max(0.0, cs - (x - mu + k))
            if cs > mx: mx = cs
        return float(mx)
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _page_hinkley(s, n, delta=0.0):
    """Page-Hinkley test stat: max(U_t - min(U_t)). Detects upward mean shifts."""
    mp = max(n // 3, 20)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 20: return np.nan
        mu = v.mean()
        u = np.cumsum(v - mu - delta)
        return float((u - np.minimum.accumulate(u)).max())
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _page_hinkley_neg(s, n, delta=0.0):
    mp = max(n // 3, 20)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 20: return np.nan
        mu = v.mean()
        u = np.cumsum(-(v - mu) - delta)
        return float((u - np.minimum.accumulate(u)).max())
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _cusum_variance(s, n):
    """CUSUM on (x - mean)^2 deviations (variance shift detection)."""
    mp = max(n // 3, 20)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 20: return np.nan
        v2 = (v - v.mean()) ** 2; mu = v2.mean()
        cs = 0.0; mx = 0.0
        for x in v2:
            cs = max(0.0, cs + (x - mu))
            if cs > mx: mx = cs
        return float(mx)
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _cumulative_t_stat_max(s, n):
    """Max t-statistic for split point in n-window (Bai-Perron-like for univariate mean)."""
    mp = max(n // 3, 30)
    def _f(w):
        v = w[~np.isnan(w)]
        nv = v.size
        if nv < 30: return np.nan
        best = 0.0
        for k in range(10, nv - 10):
            m1 = v[:k].mean(); m2 = v[k:].mean()
            s1 = v[:k].std(ddof=1); s2 = v[k:].std(ddof=1)
            se = np.sqrt(s1 ** 2 / k + s2 ** 2 / (nv - k))
            if se > 0:
                t = abs(m1 - m2) / se
                if t > best: best = t
        return float(best)
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _energy_distance(s, n):
    """E-statistic for testing equality of distribution between first/second half."""
    mp = max(n // 3, 30)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 30: return np.nan
        half = v.size // 2
        a = v[:half]; b = v[half:]
        # E = 2*mean(|a-b|) - mean(|a-a|) - mean(|b-b|)
        if a.size > 40: a = a[::2]
        if b.size > 40: b = b[::2]
        d_ab = np.abs(a[:, None] - b[None, :]).mean()
        d_aa = np.abs(a[:, None] - a[None, :]).mean()
        d_bb = np.abs(b[:, None] - b[None, :]).mean()
        return float(2.0 * d_ab - d_aa - d_bb)
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _bayesian_cp_run_length_mean(s, n, hazard=0.01):
    """Bayesian online change-point: expected run length under conjugate-prior model.

    Approximation: maintain run-length distribution over the last n bars,
    return its mean. Drops sharply when a change is detected.
    """
    mp = max(n // 3, 30)
    def _f(w):
        v = w[~np.isnan(w)]
        nv = v.size
        if nv < 30: return np.nan
        # run-length probabilities
        p = np.array([1.0])  # P(r=0) at start
        mu_prior = 0.0; kappa_prior = 1.0; alpha_prior = 1.0; beta_prior = 1.0
        sums = np.array([0.0]); ssqs = np.array([0.0]); counts = np.array([0.0])
        means = []
        for x in v:
            counts_new = counts + 1
            sums_new = sums + x
            ssqs_new = ssqs + x * x
            mu_post = (kappa_prior * mu_prior + sums_new) / (kappa_prior + counts_new)
            # predictive log-prob (simplified): Gaussian with var depending on counts
            var_post = (beta_prior + 0.5 * (ssqs_new - sums_new ** 2 / np.maximum(counts_new, 1))) / np.maximum(alpha_prior + counts_new / 2, 0.5)
            var_post = np.maximum(var_post, 1e-8)
            # likelihood under each hypothesis
            lik = np.exp(-0.5 * (x - mu_post) ** 2 / var_post) / np.sqrt(2.0 * np.pi * var_post)
            # update run-length: grow + change-point
            grow = p * lik * (1.0 - hazard)
            cp = (p * lik * hazard).sum()
            p = np.concatenate(([cp], grow))
            # update sufficient stats (shift)
            sums = np.concatenate(([0.0], sums + x))
            ssqs = np.concatenate(([0.0], ssqs + x * x))
            counts = np.concatenate(([0.0], counts + 1))
            # normalize
            ps = p.sum()
            if ps > 0: p = p / ps
            # cap memory
            if p.size > 100:
                p = p[-100:]; sums = sums[-100:]; ssqs = ssqs[-100:]; counts = counts[-100:]
            rls = np.arange(p.size, dtype=float)
            means.append(float((rls * p).sum()))
        return means[-1] if means else np.nan
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _variance_ratio_change(s, n_short, n_long):
    """Short-window variance / long-window variance - sharp jump indicates change."""
    mp_s = max(n_short // 3, 10); mp_l = max(n_long // 3, 30)
    sv = s.rolling(n_short, min_periods=mp_s).var()
    lv = s.rolling(n_long, min_periods=mp_l).var()
    return _safe_div(sv, lv)


def _mean_shift_z(s, n_short, n_long):
    """(Short-window mean - long-window mean) / long-window std."""
    mp_s = max(n_short // 3, 10); mp_l = max(n_long // 3, 30)
    sm = s.rolling(n_short, min_periods=mp_s).mean()
    lm = s.rolling(n_long, min_periods=mp_l).mean()
    ls = s.rolling(n_long, min_periods=mp_l).std()
    return _safe_div(sm - lm, ls)


def f58_cprt_076_variance_ratio_21d_over_504d_log_ret_d2(close: pd.Series) -> pd.Series:
    """Var(21dr) / Var(504dr) - sharp value increase = change."""
    r = _log_ret(close)
    return (_variance_ratio_change(r, MDAYS, DDAYS_2Y)).diff().diff()

def f58_cprt_077_variance_ratio_63d_over_504d_log_ret_d2(close: pd.Series) -> pd.Series:
    """Var(63dr) / Var(504dr) - sharp value increase = change."""
    r = _log_ret(close)
    return (_variance_ratio_change(r, QDAYS, DDAYS_2Y)).diff().diff()

def f58_cprt_078_variance_ratio_21d_over_252d_abs_ret_d2(close: pd.Series) -> pd.Series:
    """Var-ratio of |r| - vol-regime change."""
    x = _log_ret(close).abs()
    return (_variance_ratio_change(x, MDAYS, YDAYS)).diff().diff()

def f58_cprt_079_variance_ratio_63d_over_252d_abs_ret_d2(close: pd.Series) -> pd.Series:
    """Var-ratio of |r| - vol-regime change."""
    x = _log_ret(close).abs()
    return (_variance_ratio_change(x, QDAYS, YDAYS)).diff().diff()

def f58_cprt_080_mean_shift_z_21d_over_252d_log_ret_d2(close: pd.Series) -> pd.Series:
    """(21d-mean - 252d-mean)/252d-std - mean-shift z-score."""
    r = _log_ret(close)
    return (_mean_shift_z(r, MDAYS, YDAYS)).diff().diff()

def f58_cprt_081_mean_shift_z_63d_over_252d_log_ret_d2(close: pd.Series) -> pd.Series:
    """Mean shift z 63d vs 252d."""
    r = _log_ret(close)
    return (_mean_shift_z(r, QDAYS, YDAYS)).diff().diff()

def f58_cprt_082_mean_shift_z_21d_over_504d_log_ret_d2(close: pd.Series) -> pd.Series:
    """Mean shift z 21d vs 504d."""
    r = _log_ret(close)
    return (_mean_shift_z(r, MDAYS, DDAYS_2Y)).diff().diff()

def f58_cprt_083_mean_shift_z_neg_21d_over_252d_log_ret_d2(close: pd.Series) -> pd.Series:
    """Negative mean shift z (downward) 21d vs 252d."""
    r = _log_ret(close)
    return (-_mean_shift_z(r, MDAYS, YDAYS)).diff().diff()

def f58_cprt_084_variance_ratio_acceleration_21d_d2(close: pd.Series) -> pd.Series:
    """21-bar change in variance ratio 21d/252d."""
    r = _log_ret(close)
    vr = _variance_ratio_change(r, MDAYS, YDAYS)
    return (vr - vr.shift(MDAYS)).diff().diff()

def f58_cprt_085_variance_ratio_above_3_indicator_d2(close: pd.Series) -> pd.Series:
    """Indicator: variance ratio 21d/252d > 3 (vol regime change)."""
    r = _log_ret(close)
    vr = _variance_ratio_change(r, MDAYS, YDAYS)
    return ((vr > 3.0).astype(float).where(vr.notna(), np.nan)).diff().diff()

def f58_cprt_086_variance_ratio_at_252h_indicator_d2(close: pd.Series) -> pd.Series:
    """Variance ratio 21d/252d > 252d-p90 AND close = 252d max."""
    r = _log_ret(close)
    vr = _variance_ratio_change(r, MDAYS, YDAYS)
    p90 = vr.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return (((vr > p90) & (close >= rmax - 1e-12)).astype(float).where(p90.notna(), np.nan)).diff().diff()

def f58_cprt_087_mean_log_ret_sign_flip_recent_21d_vs_252d_d2(close: pd.Series) -> pd.Series:
    """Sign(21d mean) != Sign(252d mean) - regime sign flip indicator."""
    r = _log_ret(close)
    m21 = r.rolling(MDAYS, min_periods=10).mean(); m252 = r.rolling(YDAYS, min_periods=QDAYS).mean()
    return ((np.sign(m21) != np.sign(m252)).astype(float).where(m21.notna() & m252.notna(), np.nan)).diff().diff()

def f58_cprt_088_vol_regime_sign_flip_recent_21d_vs_252d_d2(close: pd.Series) -> pd.Series:
    """Sign(21d - 252d realized vol) flips - vol regime shift."""
    r = _log_ret(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=10).mean(); rv252 = (r ** 2).rolling(YDAYS, min_periods=QDAYS).mean()
    diff = rv21 - rv252
    return (((diff > 0) != (diff.shift(1) > 0)).astype(float).where(diff.notna() & diff.shift(1).notna(), np.nan)).diff().diff()

def f58_cprt_089_rsi_regime_below_50_break_after_above_70_indicator_d2(close: pd.Series) -> pd.Series:
    """RSI drops below 50 within 21 bars after being above 70 - momentum regime break."""
    rsi = _rsi(close, 14)
    ob = (rsi > 70.0).astype(float)
    ob21 = ob.shift(WDAYS).rolling(MDAYS, min_periods=5).max()
    b50 = (rsi < 50.0).astype(float)
    return (((ob21 > 0.5) & (b50 > 0.5)).astype(float).where(rsi.notna(), np.nan)).diff().diff()

def f58_cprt_090_trend_break_close_to_sma200_from_above_indicator_d2(close: pd.Series) -> pd.Series:
    """Close crosses below SMA200 (price-trend regime break)."""
    sma = _sma(close, 200)
    cd = (close < sma) & (close.shift(1) >= sma.shift(1))
    return (cd.astype(float).where(sma.notna(), np.nan)).diff().diff()

def f58_cprt_091_trend_break_close_to_sma50_from_above_indicator_d2(close: pd.Series) -> pd.Series:
    """Close crosses below SMA50 (medium trend break)."""
    sma = _sma(close, 50)
    cd = (close < sma) & (close.shift(1) >= sma.shift(1))
    return (cd.astype(float).where(sma.notna(), np.nan)).diff().diff()

def f58_cprt_092_trend_break_sma50_to_sma200_below_indicator_d2(close: pd.Series) -> pd.Series:
    """SMA50 crosses below SMA200 (Death Cross - long-term trend regime break)."""
    s50 = _sma(close, 50); s200 = _sma(close, 200)
    cd = (s50 < s200) & (s50.shift(1) >= s200.shift(1))
    return (cd.astype(float).where(s200.notna(), np.nan)).diff().diff()

def f58_cprt_093_regime_break_count_in_252d_d2(close: pd.Series) -> pd.Series:
    """Count of bars in 252d where (SMA50 cross SMA200 OR close cross SMA200)."""
    s50 = _sma(close, 50); s200 = _sma(close, 200)
    dc = ((s50 < s200) & (s50.shift(1) >= s200.shift(1))).astype(float)
    cd = ((close < s200) & (close.shift(1) >= s200.shift(1))).astype(float)
    comb = (dc.fillna(0) + cd.fillna(0)).clip(upper=1.0)
    return (comb.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff()

def f58_cprt_094_regime_break_days_since_last_252d_capped_d2(close: pd.Series) -> pd.Series:
    """Bars since last regime break (close cross SMA200) capped at 252."""
    sma = _sma(close, 200)
    cd = ((close < sma) & (close.shift(1) >= sma.shift(1))).astype(float)
    return (_bars_since_last_event(cd).clip(upper=float(YDAYS))).diff().diff()

def f58_cprt_095_rolling_t_test_z_recent_vs_baseline_252d_d2(close: pd.Series) -> pd.Series:
    """Welch-t-z for (21d mean) vs (252d-21d mean) over 252d."""
    r = _log_ret(close)
    def _wt(w):
        v = w[~np.isnan(w)]
        if v.size < 60: return np.nan
        a = v[-MDAYS:]; b = v[:-MDAYS]
        sa = a.std(ddof=1); sb = b.std(ddof=1)
        se = np.sqrt(sa ** 2 / a.size + sb ** 2 / b.size)
        if se <= 0: return np.nan
        return float((a.mean() - b.mean()) / se)
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_wt, raw=True)
    return (res).diff().diff()

def f58_cprt_096_rolling_f_test_recent_vs_baseline_var_252d_d2(close: pd.Series) -> pd.Series:
    """F-stat (21d-var) / (252d-21d var) over 252d."""
    r = _log_ret(close)
    def _ft(w):
        v = w[~np.isnan(w)]
        if v.size < 60: return np.nan
        a = v[-MDAYS:]; b = v[:-MDAYS]
        sa = a.var(ddof=1); sb = b.var(ddof=1)
        if sb <= 0: return np.nan
        return float(sa / sb)
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_ft, raw=True)
    return (res).diff().diff()

def f58_cprt_097_rolling_ks_recent_vs_baseline_dist_252d_d2(close: pd.Series) -> pd.Series:
    """KS distance between (21d) and (252d-21d) distributions of log-returns."""
    r = _log_ret(close)
    def _ks(w):
        v = w[~np.isnan(w)]
        if v.size < 60: return np.nan
        a = np.sort(v[-MDAYS:]); b = np.sort(v[:-MDAYS])
        all_v = np.union1d(a, b)
        ca = np.searchsorted(a, all_v, side='right') / a.size
        cb = np.searchsorted(b, all_v, side='right') / b.size
        return float(np.max(np.abs(ca - cb)))
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_ks, raw=True)
    return (res).diff().diff()

def f58_cprt_098_rolling_mann_whitney_u_z_252d_d2(close: pd.Series) -> pd.Series:
    """Mann-Whitney U z-stat for (21d) vs (252d-21d) over 252d."""
    r = _log_ret(close)
    def _mw(w):
        v = w[~np.isnan(w)]
        if v.size < 60: return np.nan
        a = v[-MDAYS:]; b = v[:-MDAYS]
        ranks = pd.Series(np.concatenate([a, b])).rank().values
        R1 = ranks[:a.size].sum()
        n1 = a.size; n2 = b.size
        U = R1 - n1 * (n1 + 1) / 2.0
        mu = n1 * n2 / 2.0; sd = np.sqrt(n1 * n2 * (n1 + n2 + 1) / 12.0)
        if sd <= 0: return np.nan
        return float((U - mu) / sd)
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_mw, raw=True)
    return (res).diff().diff()

def f58_cprt_099_rolling_distribution_skew_change_recent_vs_baseline_252d_d2(close: pd.Series) -> pd.Series:
    """Skew(21d) minus skew(252d-21d) over 252d."""
    r = _log_ret(close)
    def _sk(w):
        v = w[~np.isnan(w)]
        if v.size < 60: return np.nan
        a = v[-MDAYS:]; b = v[:-MDAYS]
        if a.std(ddof=1) == 0 or b.std(ddof=1) == 0: return np.nan
        ska = ((a - a.mean()) ** 3).mean() / a.std(ddof=1) ** 3
        skb = ((b - b.mean()) ** 3).mean() / b.std(ddof=1) ** 3
        return float(ska - skb)
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_sk, raw=True)
    return (res).diff().diff()

def f58_cprt_100_rolling_distribution_kurt_change_recent_vs_baseline_252d_d2(close: pd.Series) -> pd.Series:
    """Excess-kurt(21d) minus excess-kurt(252d-21d) over 252d."""
    r = _log_ret(close)
    def _kt(w):
        v = w[~np.isnan(w)]
        if v.size < 60: return np.nan
        a = v[-MDAYS:]; b = v[:-MDAYS]
        if a.std(ddof=1) == 0 or b.std(ddof=1) == 0: return np.nan
        ka = ((a - a.mean()) ** 4).mean() / a.std(ddof=1) ** 4 - 3
        kb = ((b - b.mean()) ** 4).mean() / b.std(ddof=1) ** 4 - 3
        return float(ka - kb)
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_kt, raw=True)
    return (res).diff().diff()

def f58_cprt_101_trend_slope_break_chow_proxy_252d_d2(close: pd.Series) -> pd.Series:
    """Max F-stat (Chow-test proxy) testing slope-break in linear-regression of log-close vs time."""
    lc = _safe_log(close)
    def _ch(w):
        v = w[~np.isnan(w)]
        nv = v.size
        if nv < 60: return np.nan
        x = np.arange(nv, dtype=float)
        best = 0.0
        for k in range(20, nv - 20):
            x1, y1 = x[:k], v[:k]; x2, y2 = x[k:], v[k:]
            s1 = np.polyfit(x1, y1, 1)[0]; s2 = np.polyfit(x2, y2, 1)[0]
            if abs(s1 - s2) > best: best = abs(s1 - s2)
        return float(best)
    res = lc.rolling(YDAYS, min_periods=QDAYS).apply(_ch, raw=True)
    return (res).diff().diff()

def f58_cprt_102_trend_slope_recent_vs_baseline_252d_d2(close: pd.Series) -> pd.Series:
    """Slope(21d log-close) minus slope(252d-21d log-close)."""
    lc = _safe_log(close)
    def _ds(w):
        v = w[~np.isnan(w)]
        if v.size < 60: return np.nan
        x = np.arange(v.size, dtype=float)
        s_rec = np.polyfit(x[-MDAYS:], v[-MDAYS:], 1)[0]
        s_base = np.polyfit(x[:-MDAYS], v[:-MDAYS], 1)[0]
        return float(s_rec - s_base)
    res = lc.rolling(YDAYS, min_periods=QDAYS).apply(_ds, raw=True)
    return (res).diff().diff()

def f58_cprt_103_trend_slope_zscore_change_252d_d2(close: pd.Series) -> pd.Series:
    """z-score of (21d slope - 252d-21d slope) over 252d."""
    lc = _safe_log(close)
    def _ds(w):
        v = w[~np.isnan(w)]
        if v.size < 60: return np.nan
        x = np.arange(v.size, dtype=float)
        s_rec = np.polyfit(x[-MDAYS:], v[-MDAYS:], 1)[0]
        s_base = np.polyfit(x[:-MDAYS], v[:-MDAYS], 1)[0]
        return float(s_rec - s_base)
    ch = lc.rolling(YDAYS, min_periods=QDAYS).apply(_ds, raw=True)
    return (_rolling_zscore(ch, YDAYS)).diff().diff()

def f58_cprt_104_trend_slope_sign_flip_recent_vs_baseline_indicator_d2(close: pd.Series) -> pd.Series:
    """Sign(21d slope) != sign(252d-21d slope) - trend-direction regime flip."""
    lc = _safe_log(close)
    def _ds(w):
        v = w[~np.isnan(w)]
        if v.size < 60: return np.nan
        x = np.arange(v.size, dtype=float)
        s_rec = np.polyfit(x[-MDAYS:], v[-MDAYS:], 1)[0]
        s_base = np.polyfit(x[:-MDAYS], v[:-MDAYS], 1)[0]
        return 1.0 if (s_rec * s_base < 0) else 0.0
    res = lc.rolling(YDAYS, min_periods=QDAYS).apply(_ds, raw=True)
    return (res).diff().diff()

def f58_cprt_105_trend_break_count_252d_d2(close: pd.Series) -> pd.Series:
    """Count of bars in 252d where (trend-slope sign flip in 21d vs 252d-21d)."""
    lc = _safe_log(close)
    def _ds(w):
        v = w[~np.isnan(w)]
        if v.size < 60: return np.nan
        x = np.arange(v.size, dtype=float)
        s_rec = np.polyfit(x[-MDAYS:], v[-MDAYS:], 1)[0]
        s_base = np.polyfit(x[:-MDAYS], v[:-MDAYS], 1)[0]
        return 1.0 if (s_rec * s_base < 0) else 0.0
    ev = lc.rolling(YDAYS, min_periods=QDAYS).apply(_ds, raw=True)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff()

def f58_cprt_106_trend_curvature_change_indicator_d2(close: pd.Series) -> pd.Series:
    """Sign change of 2nd derivative of SMA63 (concavity flip) - regime curvature change."""
    s = _sma(close, 63); d2 = s.diff().diff()
    sgn = np.sign(d2)
    return (((sgn != sgn.shift(1)) & (sgn != 0)).astype(float).where(d2.notna(), np.nan)).diff().diff()

def f58_cprt_107_trend_curvature_change_count_252d_d2(close: pd.Series) -> pd.Series:
    """Count of curvature flips of SMA63 in 252d."""
    s = _sma(close, 63); d2 = s.diff().diff()
    sgn = np.sign(d2)
    ev = ((sgn != sgn.shift(1)) & (sgn != 0)).astype(float).where(d2.notna(), np.nan)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff()

def f58_cprt_108_structural_break_quandt_andrews_proxy_252d_d2(close: pd.Series) -> pd.Series:
    """Sup-F (max F-stat) for breakpoint detection on log-close trend regression over 252d."""
    lc = _safe_log(close)
    def _qa(w):
        v = w[~np.isnan(w)]
        nv = v.size
        if nv < 60: return np.nan
        x = np.arange(nv, dtype=float)
        rss_full = np.sum((v - (np.polyval(np.polyfit(x, v, 1), x))) ** 2)
        best_f = 0.0
        for k in range(20, nv - 20):
            x1, y1 = x[:k], v[:k]; x2, y2 = x[k:], v[k:]
            rss1 = np.sum((y1 - np.polyval(np.polyfit(x1, y1, 1), x1)) ** 2)
            rss2 = np.sum((y2 - np.polyval(np.polyfit(x2, y2, 1), x2)) ** 2)
            if rss1 + rss2 > 0:
                f = ((rss_full - rss1 - rss2) / 2.0) / ((rss1 + rss2) / (nv - 4))
                if f > best_f: best_f = f
        return float(best_f)
    res = lc.rolling(YDAYS, min_periods=QDAYS).apply(_qa, raw=True)
    return (res).diff().diff()

def f58_cprt_109_regime_shift_intensity_composite_252d_d2(close: pd.Series) -> pd.Series:
    """Z-sum of: CUSUM-pos, PH-pos, max-split-t, E-stat over 252d."""
    r = _log_ret(close)
    u = _cusum_pos(r, YDAYS); ph = _page_hinkley(r, YDAYS); t = _cumulative_t_stat_max(r, YDAYS); e = _energy_distance(r, YDAYS)
    z = _rolling_zscore(u, YDAYS) + _rolling_zscore(ph, YDAYS) + _rolling_zscore(t, YDAYS) + _rolling_zscore(e, YDAYS)
    return (z).diff().diff()

def f58_cprt_110_regime_shift_intensity_above_p90_at_252h_indicator_d2(close: pd.Series) -> pd.Series:
    """Regime-shift intensity composite > 252d-p90 AND close = 252d max."""
    r = _log_ret(close)
    u = _cusum_pos(r, YDAYS); ph = _page_hinkley(r, YDAYS); t = _cumulative_t_stat_max(r, YDAYS); e = _energy_distance(r, YDAYS)
    z = (_rolling_zscore(u, YDAYS) + _rolling_zscore(ph, YDAYS) + _rolling_zscore(t, YDAYS) + _rolling_zscore(e, YDAYS))
    p90 = z.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return (((z > p90) & (close >= rmax - 1e-12)).astype(float).where(p90.notna(), np.nan)).diff().diff()

def f58_cprt_111_cp_intensity_overnight_ret_252d_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    """Page-Hinkley on overnight log-returns over 252d."""
    on = _safe_log(open) - _safe_log(close.shift(1))
    return (_page_hinkley(on, YDAYS)).diff().diff()

def f58_cprt_112_cp_intensity_intraday_ret_252d_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    """Page-Hinkley on intraday returns over 252d."""
    i = _safe_log(close) - _safe_log(open)
    return (_page_hinkley(i, YDAYS)).diff().diff()

def f58_cprt_113_cp_intensity_log_volume_252d_d2(volume: pd.Series) -> pd.Series:
    """Page-Hinkley on log-volume over 252d (volume regime change)."""
    lv = _safe_log(volume.replace(0, np.nan))
    return (_page_hinkley(lv, YDAYS)).diff().diff()

def f58_cprt_114_cp_intensity_log_dollar_volume_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Page-Hinkley on log dollar-volume over 252d."""
    ldv = _safe_log((close * volume).replace(0, np.nan))
    return (_page_hinkley(ldv, YDAYS)).diff().diff()

def f58_cprt_115_cp_intensity_high_low_range_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Page-Hinkley on (high-low)/close over 252d (range regime change)."""
    rn = _safe_div(high - low, close)
    return (_page_hinkley(rn, YDAYS)).diff().diff()

def f58_cprt_116_cp_intensity_close_pos_in_range_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Page-Hinkley on intraday close-position over 252d."""
    p = (close - low) / (high - low).replace(0, np.nan)
    return (_page_hinkley(p, YDAYS)).diff().diff()

def f58_cprt_117_cp_intensity_log_atr_norm_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Page-Hinkley on log(ATR/close) over 252d."""
    an = _safe_log(_safe_div(_atr(high, low, close, MDAYS), close))
    return (_page_hinkley(an, YDAYS)).diff().diff()

def f58_cprt_118_cp_intensity_rsi_14_252d_d2(close: pd.Series) -> pd.Series:
    """Page-Hinkley on RSI14 over 252d."""
    rsi = _rsi(close, 14)
    return (_page_hinkley(rsi, YDAYS)).diff().diff()

def f58_cprt_119_cp_intensity_macd_252d_d2(close: pd.Series) -> pd.Series:
    """Page-Hinkley on MACD line over 252d."""
    m = _macd(close)
    return (_page_hinkley(m, YDAYS)).diff().diff()

def f58_cprt_120_cp_intensity_obv_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Page-Hinkley on OBV over 252d."""
    o = _obv(close, volume)
    return (_page_hinkley(o, YDAYS)).diff().diff()

def f58_cprt_121_cp_intensity_cross_stream_consensus_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of z(PH) across {ret, abs-ret, vol, range, RSI, MACD, OBV} - cross-stream change consensus."""
    r = _log_ret(close); x = r.abs()
    lv = _safe_log(volume.replace(0, np.nan)); rn = _safe_div(high - low, close)
    rsi = _rsi(close, 14); m = _macd(close); o = _obv(close, volume)
    z1 = _rolling_zscore(_page_hinkley(r, YDAYS), YDAYS); z2 = _rolling_zscore(_page_hinkley(x, YDAYS), YDAYS)
    z3 = _rolling_zscore(_page_hinkley(lv, YDAYS), YDAYS); z4 = _rolling_zscore(_page_hinkley(rn, YDAYS), YDAYS)
    z5 = _rolling_zscore(_page_hinkley(rsi, YDAYS), YDAYS); z6 = _rolling_zscore(_page_hinkley(m, YDAYS), YDAYS); z7 = _rolling_zscore(_page_hinkley(o, YDAYS), YDAYS)
    return (z1.fillna(0) + z2.fillna(0) + z3.fillna(0) + z4.fillna(0) + z5.fillna(0) + z6.fillna(0) + z7.fillna(0)).diff().diff()

def f58_cprt_122_cp_intensity_at_252h_volume_indicator_d2(close: pd.Series, volume: pd.Series, high: pd.Series) -> pd.Series:
    """PH(log-vol)>252d-p90 AND close=252d max (volume regime change at top)."""
    lv = _safe_log(volume.replace(0, np.nan))
    ph = _page_hinkley(lv, YDAYS); p90 = ph.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return (((ph > p90) & (high >= rmax - 1e-12)).astype(float).where(p90.notna(), np.nan)).diff().diff()

def f58_cprt_123_cp_intensity_at_252h_atr_indicator_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """PH(log-ATR)>252d-p90 AND close=252d max (vol regime change at top)."""
    an = _safe_log(_safe_div(_atr(high, low, close, MDAYS), close))
    ph = _page_hinkley(an, YDAYS); p90 = ph.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return (((ph > p90) & (high >= rmax - 1e-12)).astype(float).where(p90.notna(), np.nan)).diff().diff()

def f58_cprt_124_cp_intensity_at_252h_rsi_indicator_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """PH(RSI14)>252d-p90 AND close=252d max."""
    rsi = _rsi(close, 14)
    ph = _page_hinkley(rsi, YDAYS); p90 = ph.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return (((ph > p90) & (high >= rmax - 1e-12)).astype(float).where(p90.notna(), np.nan)).diff().diff()

def f58_cprt_125_cp_simultaneous_3_streams_at_252h_indicator_d2(close: pd.Series, volume: pd.Series, high: pd.Series) -> pd.Series:
    """>=3 streams (PH on r, |r|, vol, RSI, MACD) all in their respective 252d-top-decile AND at 252h."""
    r = _log_ret(close); x = r.abs(); lv = _safe_log(volume.replace(0, np.nan)); rsi = _rsi(close, 14); m = _macd(close)
    p1 = _page_hinkley(r, YDAYS); p2 = _page_hinkley(x, YDAYS); p3 = _page_hinkley(lv, YDAYS); p4 = _page_hinkley(rsi, YDAYS); p5 = _page_hinkley(m, YDAYS)
    q1 = p1.rolling(YDAYS, min_periods=QDAYS).quantile(0.90); q2 = p2.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    q3 = p3.rolling(YDAYS, min_periods=QDAYS).quantile(0.90); q4 = p4.rolling(YDAYS, min_periods=QDAYS).quantile(0.90); q5 = p5.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    cnt = ((p1 > q1).astype(float) + (p2 > q2).astype(float) + (p3 > q3).astype(float) + (p4 > q4).astype(float) + (p5 > q5).astype(float))
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return (((cnt >= 3) & (high >= rmax - 1e-12)).astype(float).where(q1.notna() & q2.notna() & q3.notna(), np.nan)).diff().diff()

def f58_cprt_126_regime_shift_persistence_density_63d_d2(close: pd.Series) -> pd.Series:
    """Fraction of last 63d where regime-shift intensity > 252d-mean."""
    r = _log_ret(close)
    z = _rolling_zscore(_cusum_pos(r, YDAYS), YDAYS) + _rolling_zscore(_page_hinkley(r, YDAYS), YDAYS)
    mu = z.rolling(YDAYS, min_periods=QDAYS).mean()
    ind = (z > mu).astype(float).where(mu.notna(), np.nan)
    return (ind.rolling(QDAYS, min_periods=MDAYS).mean()).diff().diff()

def f58_cprt_127_regime_shift_bars_since_last_z_above_2_capped_252_d2(close: pd.Series) -> pd.Series:
    """Bars since regime-shift intensity z>2 (capped 252)."""
    r = _log_ret(close)
    z = _rolling_zscore(_page_hinkley(r, YDAYS), YDAYS)
    ev = (z > 2.0).astype(float).where(z.notna(), np.nan)
    return (_bars_since_last_event(ev).clip(upper=float(YDAYS))).diff().diff()

def f58_cprt_128_regime_shift_count_z_above_2_in_252d_d2(close: pd.Series) -> pd.Series:
    """Count of bars in 252d where regime-shift z>2."""
    r = _log_ret(close)
    z = _rolling_zscore(_page_hinkley(r, YDAYS), YDAYS)
    ev = (z > 2.0).astype(float).where(z.notna(), np.nan)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff()

def f58_cprt_129_regime_shift_count_at_252h_in_252d_d2(close: pd.Series) -> pd.Series:
    """Count of bars in 252d with regime-shift z>2 AND close=252d max."""
    r = _log_ret(close)
    z = _rolling_zscore(_page_hinkley(r, YDAYS), YDAYS)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    ev = ((z > 2.0) & (close >= rmax - 1e-12)).astype(float).where(z.notna(), np.nan)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff()

def f58_cprt_130_regime_shift_acceleration_252d_d2(close: pd.Series) -> pd.Series:
    """21-bar diff of regime-shift intensity z."""
    r = _log_ret(close)
    z = _rolling_zscore(_page_hinkley(r, YDAYS), YDAYS)
    return (z - z.shift(MDAYS)).diff().diff()

def f58_cprt_131_regime_shift_volatility_in_intensity_252d_d2(close: pd.Series) -> pd.Series:
    """63d std of regime-shift intensity z over 252d - regime-of-regime-changes volatility."""
    r = _log_ret(close)
    z = _rolling_zscore(_page_hinkley(r, YDAYS), YDAYS)
    return (z.rolling(QDAYS, min_periods=MDAYS).std()).diff().diff()

def f58_cprt_132_recent_regime_shift_intensity_minus_long_term_252d_d2(close: pd.Series) -> pd.Series:
    """21d-mean regime-shift z minus 504d-mean regime-shift z."""
    r = _log_ret(close)
    z = _rolling_zscore(_page_hinkley(r, YDAYS), YDAYS)
    m21 = z.rolling(MDAYS, min_periods=10).mean(); m504 = z.rolling(DDAYS_2Y, min_periods=YDAYS).mean()
    return (m21 - m504).diff().diff()

def f58_cprt_133_regime_shift_clustering_pair_count_252d_d2(close: pd.Series) -> pd.Series:
    """Count of consecutive-bar pairs with regime-shift z>2 in last 252d."""
    r = _log_ret(close)
    z = _rolling_zscore(_page_hinkley(r, YDAYS), YDAYS)
    ev = (z > 2.0).astype(float).where(z.notna(), np.nan)
    pair = (ev * ev.shift(1)).fillna(0.0)
    return (pair.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff()

def f58_cprt_134_cusum_pos_above_p90_persistence_63d_d2(close: pd.Series) -> pd.Series:
    """Fraction of last 63d with CUSUM-pos > 252d-p90."""
    r = _log_ret(close)
    u = _cusum_pos(r, YDAYS); p90 = u.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    ind = (u > p90).astype(float).where(p90.notna(), np.nan)
    return (ind.rolling(QDAYS, min_periods=MDAYS).mean()).diff().diff()

def f58_cprt_135_cumulative_change_metric_diff_pos_neg_252d_d2(close: pd.Series) -> pd.Series:
    """Sum of pos-CUSUM minus sum of neg-CUSUM over 252d window - directional regime sum."""
    r = _log_ret(close)
    u = _cusum_pos(r, YDAYS); d = _cusum_neg(r, YDAYS)
    return (u.rolling(YDAYS, min_periods=QDAYS).sum() - d.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff()

def f58_cprt_136_regime_shift_at_252h_composite_score_d2(close: pd.Series) -> pd.Series:
    """Z-sum of (CUSUM-pos + Page-Hinkley + max-split-t + E-stat) restricted to bars at 252d high."""
    r = _log_ret(close)
    z = (_rolling_zscore(_cusum_pos(r, YDAYS), YDAYS) + _rolling_zscore(_page_hinkley(r, YDAYS), YDAYS) + _rolling_zscore(_cumulative_t_stat_max(r, YDAYS), YDAYS) + _rolling_zscore(_energy_distance(r, YDAYS), YDAYS))
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return (z.where(close >= rmax - 1e-12, np.nan)).diff().diff()

def f58_cprt_137_regime_shift_max_z_in_63d_d2(close: pd.Series) -> pd.Series:
    """Max regime-shift z observed in last 63d."""
    r = _log_ret(close)
    z = _rolling_zscore(_page_hinkley(r, YDAYS), YDAYS)
    return (z.rolling(QDAYS, min_periods=MDAYS).max()).diff().diff()

def f58_cprt_138_regime_shift_z_above_3_indicator_d2(close: pd.Series) -> pd.Series:
    """Regime-shift intensity z > 3 (very strong change signal)."""
    r = _log_ret(close)
    z = _rolling_zscore(_page_hinkley(r, YDAYS), YDAYS)
    return ((z > 3.0).astype(float).where(z.notna(), np.nan)).diff().diff()

def f58_cprt_139_regime_shift_z_above_3_at_252h_indicator_d2(close: pd.Series) -> pd.Series:
    """Regime-shift z > 3 AND close = 252d max."""
    r = _log_ret(close)
    z = _rolling_zscore(_page_hinkley(r, YDAYS), YDAYS)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return (((z > 3.0) & (close >= rmax - 1e-12)).astype(float).where(z.notna(), np.nan)).diff().diff()

def f58_cprt_140_regime_shift_in_overnight_ret_at_252h_indicator_d2(open: pd.Series, close: pd.Series, high: pd.Series) -> pd.Series:
    """PH on overnight returns > 252d-p90 AND close = 252d max."""
    on = _safe_log(open) - _safe_log(close.shift(1))
    ph = _page_hinkley(on, YDAYS); p90 = ph.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return (((ph > p90) & (high >= rmax - 1e-12)).astype(float).where(p90.notna(), np.nan)).diff().diff()

def f58_cprt_141_regime_shift_in_intraday_ret_at_252h_indicator_d2(open: pd.Series, close: pd.Series, high: pd.Series) -> pd.Series:
    """PH on intraday returns > 252d-p90 AND close = 252d max."""
    i = _safe_log(close) - _safe_log(open)
    ph = _page_hinkley(i, YDAYS); p90 = ph.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return (((ph > p90) & (high >= rmax - 1e-12)).astype(float).where(p90.notna(), np.nan)).diff().diff()

def f58_cprt_142_regime_shift_in_macd_at_252h_indicator_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """PH on MACD > 252d-p90 AND close = 252d max."""
    m = _macd(close)
    ph = _page_hinkley(m, YDAYS); p90 = ph.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return (((ph > p90) & (high >= rmax - 1e-12)).astype(float).where(p90.notna(), np.nan)).diff().diff()

def f58_cprt_143_regime_shift_in_obv_at_252h_indicator_d2(close: pd.Series, volume: pd.Series, high: pd.Series) -> pd.Series:
    """PH on OBV > 252d-p90 AND close = 252d max."""
    o = _obv(close, volume)
    ph = _page_hinkley(o, YDAYS); p90 = ph.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return (((ph > p90) & (high >= rmax - 1e-12)).astype(float).where(p90.notna(), np.nan)).diff().diff()

def f58_cprt_144_regime_break_count_negative_cusum_252d_d2(close: pd.Series) -> pd.Series:
    """Count of bars in 252d where neg-CUSUM > 252d-p90 (downward-shift events)."""
    r = _log_ret(close)
    d = _cusum_neg(r, YDAYS); p90 = d.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    ev = (d > p90).astype(float).where(p90.notna(), np.nan)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff()

def f58_cprt_145_max_split_t_stat_minus_baseline_504d_d2(close: pd.Series) -> pd.Series:
    """Max-split-t-stat 252d minus its 504d-mean - relative regime-change intensity."""
    r = _log_ret(close)
    t = _cumulative_t_stat_max(r, YDAYS); bm = t.rolling(DDAYS_2Y, min_periods=YDAYS).mean()
    return (t - bm).diff().diff()

def f58_cprt_146_regime_shift_z_above_4_indicator_d2(close: pd.Series) -> pd.Series:
    """Regime-shift z > 4 (extreme change event)."""
    r = _log_ret(close)
    z = _rolling_zscore(_page_hinkley(r, YDAYS), YDAYS)
    return ((z > 4.0).astype(float).where(z.notna(), np.nan)).diff().diff()

def f58_cprt_147_regime_shift_recent_decay_indicator_d2(close: pd.Series) -> pd.Series:
    """Regime-shift z was >2 in last 21 bars BUT now <0.5 (event aftermath)."""
    r = _log_ret(close)
    z = _rolling_zscore(_page_hinkley(r, YDAYS), YDAYS)
    high_recent = (z > 2.0).astype(float).rolling(MDAYS, min_periods=5).max()
    return (((high_recent > 0.5) & (z < 0.5)).astype(float).where(z.notna(), np.nan)).diff().diff()

def f58_cprt_148_regime_shift_consistency_3of3_streams_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """All 3 streams (PH on r, |r|, log-vol) above their 252d-medians simultaneously."""
    r = _log_ret(close); x = r.abs(); lv = _safe_log(volume.replace(0, np.nan))
    ph1 = _page_hinkley(r, YDAYS); ph2 = _page_hinkley(x, YDAYS); ph3 = _page_hinkley(lv, YDAYS)
    m1 = ph1.rolling(YDAYS, min_periods=QDAYS).median(); m2 = ph2.rolling(YDAYS, min_periods=QDAYS).median(); m3 = ph3.rolling(YDAYS, min_periods=QDAYS).median()
    return (((ph1 > m1) & (ph2 > m2) & (ph3 > m3)).astype(float).where(m1.notna() & m2.notna() & m3.notna(), np.nan)).diff().diff()

def f58_cprt_149_regime_shift_amplitude_max_in_504d_d2(close: pd.Series) -> pd.Series:
    """Max regime-shift z observed in trailing 504d."""
    r = _log_ret(close)
    z = _rolling_zscore(_page_hinkley(r, YDAYS), YDAYS)
    return (z.rolling(DDAYS_2Y, min_periods=YDAYS).max()).diff().diff()

def f58_cprt_150_master_regime_break_composite_252d_d2(close: pd.Series) -> pd.Series:
    """Average z-rank of: CUSUM, PH, max-split-t, E-stat, BOCP-inverted, var-ratio, mean-shift over 252d."""
    r = _log_ret(close)
    z1 = _rolling_zscore(_cusum_pos(r, YDAYS), YDAYS); z2 = _rolling_zscore(_page_hinkley(r, YDAYS), YDAYS)
    z3 = _rolling_zscore(_cumulative_t_stat_max(r, YDAYS), YDAYS); z4 = _rolling_zscore(_energy_distance(r, YDAYS), YDAYS)
    z5 = -_rolling_zscore(_bayesian_cp_run_length_mean(r, YDAYS, 0.01), YDAYS)
    z6 = _rolling_zscore(_variance_ratio_change(r, MDAYS, YDAYS), YDAYS)
    z7 = _rolling_zscore(_mean_shift_z(r, MDAYS, YDAYS), YDAYS)
    return ((z1.fillna(0) + z2.fillna(0) + z3.fillna(0) + z4.fillna(0) + z5.fillna(0) + z6.fillna(0) + z7.fillna(0)) / 7.0).diff().diff()


CHANGE_POINT_REGIME_TRANSITION_D2_REGISTRY_076_150 = {
    "f58_cprt_076_variance_ratio_21d_over_504d_log_ret_d2": {"inputs": ["close"], "func": f58_cprt_076_variance_ratio_21d_over_504d_log_ret_d2},
    "f58_cprt_077_variance_ratio_63d_over_504d_log_ret_d2": {"inputs": ["close"], "func": f58_cprt_077_variance_ratio_63d_over_504d_log_ret_d2},
    "f58_cprt_078_variance_ratio_21d_over_252d_abs_ret_d2": {"inputs": ["close"], "func": f58_cprt_078_variance_ratio_21d_over_252d_abs_ret_d2},
    "f58_cprt_079_variance_ratio_63d_over_252d_abs_ret_d2": {"inputs": ["close"], "func": f58_cprt_079_variance_ratio_63d_over_252d_abs_ret_d2},
    "f58_cprt_080_mean_shift_z_21d_over_252d_log_ret_d2": {"inputs": ["close"], "func": f58_cprt_080_mean_shift_z_21d_over_252d_log_ret_d2},
    "f58_cprt_081_mean_shift_z_63d_over_252d_log_ret_d2": {"inputs": ["close"], "func": f58_cprt_081_mean_shift_z_63d_over_252d_log_ret_d2},
    "f58_cprt_082_mean_shift_z_21d_over_504d_log_ret_d2": {"inputs": ["close"], "func": f58_cprt_082_mean_shift_z_21d_over_504d_log_ret_d2},
    "f58_cprt_083_mean_shift_z_neg_21d_over_252d_log_ret_d2": {"inputs": ["close"], "func": f58_cprt_083_mean_shift_z_neg_21d_over_252d_log_ret_d2},
    "f58_cprt_084_variance_ratio_acceleration_21d_d2": {"inputs": ["close"], "func": f58_cprt_084_variance_ratio_acceleration_21d_d2},
    "f58_cprt_085_variance_ratio_above_3_indicator_d2": {"inputs": ["close"], "func": f58_cprt_085_variance_ratio_above_3_indicator_d2},
    "f58_cprt_086_variance_ratio_at_252h_indicator_d2": {"inputs": ["close"], "func": f58_cprt_086_variance_ratio_at_252h_indicator_d2},
    "f58_cprt_087_mean_log_ret_sign_flip_recent_21d_vs_252d_d2": {"inputs": ["close"], "func": f58_cprt_087_mean_log_ret_sign_flip_recent_21d_vs_252d_d2},
    "f58_cprt_088_vol_regime_sign_flip_recent_21d_vs_252d_d2": {"inputs": ["close"], "func": f58_cprt_088_vol_regime_sign_flip_recent_21d_vs_252d_d2},
    "f58_cprt_089_rsi_regime_below_50_break_after_above_70_indicator_d2": {"inputs": ["close"], "func": f58_cprt_089_rsi_regime_below_50_break_after_above_70_indicator_d2},
    "f58_cprt_090_trend_break_close_to_sma200_from_above_indicator_d2": {"inputs": ["close"], "func": f58_cprt_090_trend_break_close_to_sma200_from_above_indicator_d2},
    "f58_cprt_091_trend_break_close_to_sma50_from_above_indicator_d2": {"inputs": ["close"], "func": f58_cprt_091_trend_break_close_to_sma50_from_above_indicator_d2},
    "f58_cprt_092_trend_break_sma50_to_sma200_below_indicator_d2": {"inputs": ["close"], "func": f58_cprt_092_trend_break_sma50_to_sma200_below_indicator_d2},
    "f58_cprt_093_regime_break_count_in_252d_d2": {"inputs": ["close"], "func": f58_cprt_093_regime_break_count_in_252d_d2},
    "f58_cprt_094_regime_break_days_since_last_252d_capped_d2": {"inputs": ["close"], "func": f58_cprt_094_regime_break_days_since_last_252d_capped_d2},
    "f58_cprt_095_rolling_t_test_z_recent_vs_baseline_252d_d2": {"inputs": ["close"], "func": f58_cprt_095_rolling_t_test_z_recent_vs_baseline_252d_d2},
    "f58_cprt_096_rolling_f_test_recent_vs_baseline_var_252d_d2": {"inputs": ["close"], "func": f58_cprt_096_rolling_f_test_recent_vs_baseline_var_252d_d2},
    "f58_cprt_097_rolling_ks_recent_vs_baseline_dist_252d_d2": {"inputs": ["close"], "func": f58_cprt_097_rolling_ks_recent_vs_baseline_dist_252d_d2},
    "f58_cprt_098_rolling_mann_whitney_u_z_252d_d2": {"inputs": ["close"], "func": f58_cprt_098_rolling_mann_whitney_u_z_252d_d2},
    "f58_cprt_099_rolling_distribution_skew_change_recent_vs_baseline_252d_d2": {"inputs": ["close"], "func": f58_cprt_099_rolling_distribution_skew_change_recent_vs_baseline_252d_d2},
    "f58_cprt_100_rolling_distribution_kurt_change_recent_vs_baseline_252d_d2": {"inputs": ["close"], "func": f58_cprt_100_rolling_distribution_kurt_change_recent_vs_baseline_252d_d2},
    "f58_cprt_101_trend_slope_break_chow_proxy_252d_d2": {"inputs": ["close"], "func": f58_cprt_101_trend_slope_break_chow_proxy_252d_d2},
    "f58_cprt_102_trend_slope_recent_vs_baseline_252d_d2": {"inputs": ["close"], "func": f58_cprt_102_trend_slope_recent_vs_baseline_252d_d2},
    "f58_cprt_103_trend_slope_zscore_change_252d_d2": {"inputs": ["close"], "func": f58_cprt_103_trend_slope_zscore_change_252d_d2},
    "f58_cprt_104_trend_slope_sign_flip_recent_vs_baseline_indicator_d2": {"inputs": ["close"], "func": f58_cprt_104_trend_slope_sign_flip_recent_vs_baseline_indicator_d2},
    "f58_cprt_105_trend_break_count_252d_d2": {"inputs": ["close"], "func": f58_cprt_105_trend_break_count_252d_d2},
    "f58_cprt_106_trend_curvature_change_indicator_d2": {"inputs": ["close"], "func": f58_cprt_106_trend_curvature_change_indicator_d2},
    "f58_cprt_107_trend_curvature_change_count_252d_d2": {"inputs": ["close"], "func": f58_cprt_107_trend_curvature_change_count_252d_d2},
    "f58_cprt_108_structural_break_quandt_andrews_proxy_252d_d2": {"inputs": ["close"], "func": f58_cprt_108_structural_break_quandt_andrews_proxy_252d_d2},
    "f58_cprt_109_regime_shift_intensity_composite_252d_d2": {"inputs": ["close"], "func": f58_cprt_109_regime_shift_intensity_composite_252d_d2},
    "f58_cprt_110_regime_shift_intensity_above_p90_at_252h_indicator_d2": {"inputs": ["close"], "func": f58_cprt_110_regime_shift_intensity_above_p90_at_252h_indicator_d2},
    "f58_cprt_111_cp_intensity_overnight_ret_252d_d2": {"inputs": ["open", "close"], "func": f58_cprt_111_cp_intensity_overnight_ret_252d_d2},
    "f58_cprt_112_cp_intensity_intraday_ret_252d_d2": {"inputs": ["open", "close"], "func": f58_cprt_112_cp_intensity_intraday_ret_252d_d2},
    "f58_cprt_113_cp_intensity_log_volume_252d_d2": {"inputs": ["volume"], "func": f58_cprt_113_cp_intensity_log_volume_252d_d2},
    "f58_cprt_114_cp_intensity_log_dollar_volume_252d_d2": {"inputs": ["close", "volume"], "func": f58_cprt_114_cp_intensity_log_dollar_volume_252d_d2},
    "f58_cprt_115_cp_intensity_high_low_range_252d_d2": {"inputs": ["high", "low", "close"], "func": f58_cprt_115_cp_intensity_high_low_range_252d_d2},
    "f58_cprt_116_cp_intensity_close_pos_in_range_252d_d2": {"inputs": ["high", "low", "close"], "func": f58_cprt_116_cp_intensity_close_pos_in_range_252d_d2},
    "f58_cprt_117_cp_intensity_log_atr_norm_252d_d2": {"inputs": ["high", "low", "close"], "func": f58_cprt_117_cp_intensity_log_atr_norm_252d_d2},
    "f58_cprt_118_cp_intensity_rsi_14_252d_d2": {"inputs": ["close"], "func": f58_cprt_118_cp_intensity_rsi_14_252d_d2},
    "f58_cprt_119_cp_intensity_macd_252d_d2": {"inputs": ["close"], "func": f58_cprt_119_cp_intensity_macd_252d_d2},
    "f58_cprt_120_cp_intensity_obv_252d_d2": {"inputs": ["close", "volume"], "func": f58_cprt_120_cp_intensity_obv_252d_d2},
    "f58_cprt_121_cp_intensity_cross_stream_consensus_252d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f58_cprt_121_cp_intensity_cross_stream_consensus_252d_d2},
    "f58_cprt_122_cp_intensity_at_252h_volume_indicator_d2": {"inputs": ["close", "volume", "high"], "func": f58_cprt_122_cp_intensity_at_252h_volume_indicator_d2},
    "f58_cprt_123_cp_intensity_at_252h_atr_indicator_d2": {"inputs": ["close", "high", "low"], "func": f58_cprt_123_cp_intensity_at_252h_atr_indicator_d2},
    "f58_cprt_124_cp_intensity_at_252h_rsi_indicator_d2": {"inputs": ["close", "high"], "func": f58_cprt_124_cp_intensity_at_252h_rsi_indicator_d2},
    "f58_cprt_125_cp_simultaneous_3_streams_at_252h_indicator_d2": {"inputs": ["close", "volume", "high"], "func": f58_cprt_125_cp_simultaneous_3_streams_at_252h_indicator_d2},
    "f58_cprt_126_regime_shift_persistence_density_63d_d2": {"inputs": ["close"], "func": f58_cprt_126_regime_shift_persistence_density_63d_d2},
    "f58_cprt_127_regime_shift_bars_since_last_z_above_2_capped_252_d2": {"inputs": ["close"], "func": f58_cprt_127_regime_shift_bars_since_last_z_above_2_capped_252_d2},
    "f58_cprt_128_regime_shift_count_z_above_2_in_252d_d2": {"inputs": ["close"], "func": f58_cprt_128_regime_shift_count_z_above_2_in_252d_d2},
    "f58_cprt_129_regime_shift_count_at_252h_in_252d_d2": {"inputs": ["close"], "func": f58_cprt_129_regime_shift_count_at_252h_in_252d_d2},
    "f58_cprt_130_regime_shift_acceleration_252d_d2": {"inputs": ["close"], "func": f58_cprt_130_regime_shift_acceleration_252d_d2},
    "f58_cprt_131_regime_shift_volatility_in_intensity_252d_d2": {"inputs": ["close"], "func": f58_cprt_131_regime_shift_volatility_in_intensity_252d_d2},
    "f58_cprt_132_recent_regime_shift_intensity_minus_long_term_252d_d2": {"inputs": ["close"], "func": f58_cprt_132_recent_regime_shift_intensity_minus_long_term_252d_d2},
    "f58_cprt_133_regime_shift_clustering_pair_count_252d_d2": {"inputs": ["close"], "func": f58_cprt_133_regime_shift_clustering_pair_count_252d_d2},
    "f58_cprt_134_cusum_pos_above_p90_persistence_63d_d2": {"inputs": ["close"], "func": f58_cprt_134_cusum_pos_above_p90_persistence_63d_d2},
    "f58_cprt_135_cumulative_change_metric_diff_pos_neg_252d_d2": {"inputs": ["close"], "func": f58_cprt_135_cumulative_change_metric_diff_pos_neg_252d_d2},
    "f58_cprt_136_regime_shift_at_252h_composite_score_d2": {"inputs": ["close"], "func": f58_cprt_136_regime_shift_at_252h_composite_score_d2},
    "f58_cprt_137_regime_shift_max_z_in_63d_d2": {"inputs": ["close"], "func": f58_cprt_137_regime_shift_max_z_in_63d_d2},
    "f58_cprt_138_regime_shift_z_above_3_indicator_d2": {"inputs": ["close"], "func": f58_cprt_138_regime_shift_z_above_3_indicator_d2},
    "f58_cprt_139_regime_shift_z_above_3_at_252h_indicator_d2": {"inputs": ["close"], "func": f58_cprt_139_regime_shift_z_above_3_at_252h_indicator_d2},
    "f58_cprt_140_regime_shift_in_overnight_ret_at_252h_indicator_d2": {"inputs": ["open", "close", "high"], "func": f58_cprt_140_regime_shift_in_overnight_ret_at_252h_indicator_d2},
    "f58_cprt_141_regime_shift_in_intraday_ret_at_252h_indicator_d2": {"inputs": ["open", "close", "high"], "func": f58_cprt_141_regime_shift_in_intraday_ret_at_252h_indicator_d2},
    "f58_cprt_142_regime_shift_in_macd_at_252h_indicator_d2": {"inputs": ["close", "high"], "func": f58_cprt_142_regime_shift_in_macd_at_252h_indicator_d2},
    "f58_cprt_143_regime_shift_in_obv_at_252h_indicator_d2": {"inputs": ["close", "volume", "high"], "func": f58_cprt_143_regime_shift_in_obv_at_252h_indicator_d2},
    "f58_cprt_144_regime_break_count_negative_cusum_252d_d2": {"inputs": ["close"], "func": f58_cprt_144_regime_break_count_negative_cusum_252d_d2},
    "f58_cprt_145_max_split_t_stat_minus_baseline_504d_d2": {"inputs": ["close"], "func": f58_cprt_145_max_split_t_stat_minus_baseline_504d_d2},
    "f58_cprt_146_regime_shift_z_above_4_indicator_d2": {"inputs": ["close"], "func": f58_cprt_146_regime_shift_z_above_4_indicator_d2},
    "f58_cprt_147_regime_shift_recent_decay_indicator_d2": {"inputs": ["close"], "func": f58_cprt_147_regime_shift_recent_decay_indicator_d2},
    "f58_cprt_148_regime_shift_consistency_3of3_streams_252d_d2": {"inputs": ["close", "volume"], "func": f58_cprt_148_regime_shift_consistency_3of3_streams_252d_d2},
    "f58_cprt_149_regime_shift_amplitude_max_in_504d_d2": {"inputs": ["close"], "func": f58_cprt_149_regime_shift_amplitude_max_in_504d_d2},
    "f58_cprt_150_master_regime_break_composite_252d_d2": {"inputs": ["close"], "func": f58_cprt_150_master_regime_break_composite_252d_d2},
}
