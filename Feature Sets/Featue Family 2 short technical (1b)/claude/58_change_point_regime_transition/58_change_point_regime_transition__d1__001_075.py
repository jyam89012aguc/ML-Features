"""change_point_regime_transition d1 001-075 - 1b-technical."""
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


def f58_cprt_001_cusum_pos_log_ret_21d_d1(close: pd.Series) -> pd.Series:
    """Positive CUSUM of log-returns over 21d."""
    r = _log_ret(close)
    return (_cusum_pos(r, MDAYS)).diff()

def f58_cprt_002_cusum_neg_log_ret_21d_d1(close: pd.Series) -> pd.Series:
    """Negative CUSUM (downward shift) of log-returns over 21d."""
    r = _log_ret(close)
    return (_cusum_neg(r, MDAYS)).diff()

def f58_cprt_003_cusum_diff_pos_neg_log_ret_21d_d1(close: pd.Series) -> pd.Series:
    """Pos minus Neg CUSUM over 21d."""
    r = _log_ret(close)
    u = _cusum_pos(r, MDAYS); d = _cusum_neg(r, MDAYS)
    return (u - d).diff()

def f58_cprt_004_cusum_pos_log_ret_63d_d1(close: pd.Series) -> pd.Series:
    """Positive CUSUM of log-returns over 63d."""
    r = _log_ret(close)
    return (_cusum_pos(r, QDAYS)).diff()

def f58_cprt_005_cusum_neg_log_ret_63d_d1(close: pd.Series) -> pd.Series:
    """Negative CUSUM (downward shift) of log-returns over 63d."""
    r = _log_ret(close)
    return (_cusum_neg(r, QDAYS)).diff()

def f58_cprt_006_cusum_diff_pos_neg_log_ret_63d_d1(close: pd.Series) -> pd.Series:
    """Pos minus Neg CUSUM over 63d."""
    r = _log_ret(close)
    u = _cusum_pos(r, QDAYS); d = _cusum_neg(r, QDAYS)
    return (u - d).diff()

def f58_cprt_007_cusum_pos_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Positive CUSUM of log-returns over 252d."""
    r = _log_ret(close)
    return (_cusum_pos(r, YDAYS)).diff()

def f58_cprt_008_cusum_neg_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Negative CUSUM (downward shift) of log-returns over 252d."""
    r = _log_ret(close)
    return (_cusum_neg(r, YDAYS)).diff()

def f58_cprt_009_cusum_diff_pos_neg_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Pos minus Neg CUSUM over 252d."""
    r = _log_ret(close)
    u = _cusum_pos(r, YDAYS); d = _cusum_neg(r, YDAYS)
    return (u - d).diff()

def f58_cprt_010_cusum_pos_abs_ret_63d_d1(close: pd.Series) -> pd.Series:
    """Pos CUSUM of |r| over 63d - vol increase detection."""
    x = _log_ret(close).abs()
    return (_cusum_pos(x, QDAYS)).diff()

def f58_cprt_011_cusum_variance_log_ret_63d_d1(close: pd.Series) -> pd.Series:
    """CUSUM on (r - mean)^2 over 63d - variance shift."""
    r = _log_ret(close)
    return (_cusum_variance(r, QDAYS)).diff()

def f58_cprt_012_cusum_pos_abs_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Pos CUSUM of |r| over 252d - vol increase detection."""
    x = _log_ret(close).abs()
    return (_cusum_pos(x, YDAYS)).diff()

def f58_cprt_013_cusum_variance_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """CUSUM on (r - mean)^2 over 252d - variance shift."""
    r = _log_ret(close)
    return (_cusum_variance(r, YDAYS)).diff()

def f58_cprt_014_cusum_log_close_252d_d1(close: pd.Series) -> pd.Series:
    """Pos CUSUM of log-close over 252d."""
    lc = _safe_log(close)
    return (_cusum_pos(lc, YDAYS)).diff()

def f58_cprt_015_cusum_log_close_504d_d1(close: pd.Series) -> pd.Series:
    """Pos CUSUM of log-close over 504d."""
    lc = _safe_log(close)
    return (_cusum_pos(lc, DDAYS_2Y)).diff()

def f58_cprt_016_page_hinkley_pos_log_ret_63d_d1(close: pd.Series) -> pd.Series:
    """Page-Hinkley upward-shift stat on log-returns over 63d."""
    r = _log_ret(close)
    return (_page_hinkley(r, QDAYS)).diff()

def f58_cprt_017_page_hinkley_neg_log_ret_63d_d1(close: pd.Series) -> pd.Series:
    """Page-Hinkley downward-shift stat over 63d."""
    r = _log_ret(close)
    return (_page_hinkley_neg(r, QDAYS)).diff()

def f58_cprt_018_page_hinkley_pos_abs_ret_63d_d1(close: pd.Series) -> pd.Series:
    """Page-Hinkley on |r| over 63d - vol upshift."""
    x = _log_ret(close).abs()
    return (_page_hinkley(x, QDAYS)).diff()

def f58_cprt_019_page_hinkley_pos_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Page-Hinkley upward-shift stat on log-returns over 252d."""
    r = _log_ret(close)
    return (_page_hinkley(r, YDAYS)).diff()

def f58_cprt_020_page_hinkley_neg_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Page-Hinkley downward-shift stat over 252d."""
    r = _log_ret(close)
    return (_page_hinkley_neg(r, YDAYS)).diff()

def f58_cprt_021_page_hinkley_pos_abs_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Page-Hinkley on |r| over 252d - vol upshift."""
    x = _log_ret(close).abs()
    return (_page_hinkley(x, YDAYS)).diff()

def f58_cprt_022_page_hinkley_log_close_252d_d1(close: pd.Series) -> pd.Series:
    """Page-Hinkley on log-close over 252d."""
    lc = _safe_log(close)
    return (_page_hinkley(lc, YDAYS)).diff()

def f58_cprt_023_page_hinkley_log_close_504d_d1(close: pd.Series) -> pd.Series:
    """Page-Hinkley on log-close over 504d."""
    lc = _safe_log(close)
    return (_page_hinkley(lc, DDAYS_2Y)).diff()

def f58_cprt_024_page_hinkley_delta_001_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Page-Hinkley with delta=0.001 (more sensitive) over 252d."""
    r = _log_ret(close)
    return (_page_hinkley(r, YDAYS, 0.001)).diff()

def f58_cprt_025_page_hinkley_delta_005_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Page-Hinkley with delta=0.005 (less sensitive) over 252d."""
    r = _log_ret(close)
    return (_page_hinkley(r, YDAYS, 0.005)).diff()

def f58_cprt_026_page_hinkley_neg_log_close_252d_d1(close: pd.Series) -> pd.Series:
    """Page-Hinkley downward on log-close over 252d."""
    lc = _safe_log(close)
    return (_page_hinkley_neg(lc, YDAYS)).diff()

def f58_cprt_027_page_hinkley_neg_log_close_504d_d1(close: pd.Series) -> pd.Series:
    """Page-Hinkley downward on log-close over 504d."""
    lc = _safe_log(close)
    return (_page_hinkley_neg(lc, DDAYS_2Y)).diff()

def f58_cprt_028_page_hinkley_diff_pos_neg_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """PH-pos minus PH-neg on log-returns over 252d."""
    r = _log_ret(close)
    u = _page_hinkley(r, YDAYS); d = _page_hinkley_neg(r, YDAYS)
    return (u - d).diff()

def f58_cprt_029_max_split_t_stat_log_ret_63d_d1(close: pd.Series) -> pd.Series:
    """Max t-stat for any split point in 63d window (Bai-Perron-like)."""
    r = _log_ret(close)
    return (_cumulative_t_stat_max(r, QDAYS)).diff()

def f58_cprt_030_max_split_t_stat_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Max split t-stat over 252d."""
    r = _log_ret(close)
    return (_cumulative_t_stat_max(r, YDAYS)).diff()

def f58_cprt_031_max_split_t_stat_log_ret_504d_d1(close: pd.Series) -> pd.Series:
    """Max split t-stat over 504d."""
    r = _log_ret(close)
    return (_cumulative_t_stat_max(r, DDAYS_2Y)).diff()

def f58_cprt_032_max_split_t_stat_abs_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Max split t-stat on |r| over 252d."""
    x = _log_ret(close).abs()
    return (_cumulative_t_stat_max(x, YDAYS)).diff()

def f58_cprt_033_max_split_t_stat_log_close_252d_d1(close: pd.Series) -> pd.Series:
    """Max split t-stat on log-close over 252d."""
    lc = _safe_log(close)
    return (_cumulative_t_stat_max(lc, YDAYS)).diff()

def f58_cprt_034_max_split_t_stat_log_close_504d_d1(close: pd.Series) -> pd.Series:
    """Max split t-stat on log-close over 504d."""
    lc = _safe_log(close)
    return (_cumulative_t_stat_max(lc, DDAYS_2Y)).diff()

def f58_cprt_035_max_split_t_stat_log_volume_252d_d1(volume: pd.Series) -> pd.Series:
    """Max split t-stat on log-volume over 252d."""
    lv = _safe_log(volume.replace(0, np.nan))
    return (_cumulative_t_stat_max(lv, YDAYS)).diff()

def f58_cprt_036_max_split_t_stat_high_low_range_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Max split t-stat on (high-low)/close over 252d."""
    rng = _safe_div(high - low, close)
    return (_cumulative_t_stat_max(rng, YDAYS)).diff()

def f58_cprt_037_max_split_t_stat_overnight_ret_252d_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Max split t-stat on overnight returns over 252d."""
    on = _safe_log(open) - _safe_log(close.shift(1))
    return (_cumulative_t_stat_max(on, YDAYS)).diff()

def f58_cprt_038_max_split_t_stat_dollar_vol_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max split t-stat on log dollar-volume over 252d."""
    ldv = _safe_log((close * volume).replace(0, np.nan))
    return (_cumulative_t_stat_max(ldv, YDAYS)).diff()

def f58_cprt_039_max_split_t_stat_intraday_ret_252d_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Max split t-stat on intraday returns over 252d."""
    i = _safe_log(close) - _safe_log(open)
    return (_cumulative_t_stat_max(i, YDAYS)).diff()

def f58_cprt_040_max_split_t_stat_squared_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Max split t-stat on r^2 over 252d - variance change."""
    x = _log_ret(close) ** 2
    return (_cumulative_t_stat_max(x, YDAYS)).diff()

def f58_cprt_041_split_t_zscore_log_ret_252d_252d_d1(close: pd.Series) -> pd.Series:
    """z-score over 252d of (max split t-stat 252d)."""
    r = _log_ret(close)
    t = _cumulative_t_stat_max(r, YDAYS)
    return (_rolling_zscore(t, YDAYS)).diff()

def f58_cprt_042_split_t_top_decile_indicator_252d_d1(close: pd.Series) -> pd.Series:
    """Indicator: max split t-stat over 252d > 252d-q90."""
    r = _log_ret(close)
    t = _cumulative_t_stat_max(r, YDAYS)
    p90 = t.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    return ((t > p90).astype(float).where(p90.notna(), np.nan)).diff()

def f58_cprt_043_split_t_above_threshold_at_252h_indicator_d1(close: pd.Series) -> pd.Series:
    """Max split t-stat > 3.0 (significant) AND close = 252d max."""
    r = _log_ret(close)
    t = _cumulative_t_stat_max(r, YDAYS)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return (((t > 3.0) & (close >= rmax - 1e-12)).astype(float).where(t.notna(), np.nan)).diff()

def f58_cprt_044_energy_distance_log_ret_63d_d1(close: pd.Series) -> pd.Series:
    """E-stat (energy distance) between first/second half of 63d log-returns."""
    r = _log_ret(close)
    return (_energy_distance(r, QDAYS)).diff()

def f58_cprt_045_energy_distance_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """E-stat over 252d."""
    r = _log_ret(close)
    return (_energy_distance(r, YDAYS)).diff()

def f58_cprt_046_energy_distance_log_ret_504d_d1(close: pd.Series) -> pd.Series:
    """E-stat over 504d."""
    r = _log_ret(close)
    return (_energy_distance(r, DDAYS_2Y)).diff()

def f58_cprt_047_energy_distance_abs_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """E-stat on |r| over 252d - vol distribution change."""
    x = _log_ret(close).abs()
    return (_energy_distance(x, YDAYS)).diff()

def f58_cprt_048_energy_distance_log_volume_252d_d1(volume: pd.Series) -> pd.Series:
    """E-stat on log-volume over 252d."""
    lv = _safe_log(volume.replace(0, np.nan))
    return (_energy_distance(lv, YDAYS)).diff()

def f58_cprt_049_energy_distance_atr_norm_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """E-stat on ATR/close over 252d."""
    an = _safe_div(_atr(high, low, close, MDAYS), close)
    return (_energy_distance(an, YDAYS)).diff()

def f58_cprt_050_energy_distance_overnight_ret_252d_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """E-stat on overnight returns over 252d."""
    on = _safe_log(open) - _safe_log(close.shift(1))
    return (_energy_distance(on, YDAYS)).diff()

def f58_cprt_051_energy_distance_close_pos_in_range_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """E-stat on intraday close-position over 252d."""
    p = (close - low) / (high - low).replace(0, np.nan)
    return (_energy_distance(p, YDAYS)).diff()

def f58_cprt_052_energy_distance_log_close_504d_d1(close: pd.Series) -> pd.Series:
    """E-stat on log-close over 504d."""
    lc = _safe_log(close)
    return (_energy_distance(lc, DDAYS_2Y)).diff()

def f58_cprt_053_energy_distance_squared_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """E-stat on r^2 over 252d."""
    x = _log_ret(close) ** 2
    return (_energy_distance(x, YDAYS)).diff()

def f58_cprt_054_energy_distance_zscore_252d_d1(close: pd.Series) -> pd.Series:
    """z-score over 252d of 63d-energy-distance."""
    r = _log_ret(close)
    e = _energy_distance(r, QDAYS)
    return (_rolling_zscore(e, YDAYS)).diff()

def f58_cprt_055_energy_distance_above_p90_indicator_252d_d1(close: pd.Series) -> pd.Series:
    """Indicator: E-stat 63d above 252d-p90."""
    r = _log_ret(close)
    e = _energy_distance(r, QDAYS)
    p90 = e.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    return ((e > p90).astype(float).where(p90.notna(), np.nan)).diff()

def f58_cprt_056_energy_distance_at_252h_indicator_d1(close: pd.Series) -> pd.Series:
    """E-stat in top quartile AND close = 252d max."""
    r = _log_ret(close)
    e = _energy_distance(r, QDAYS)
    p75 = e.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return (((e > p75) & (close >= rmax - 1e-12)).astype(float).where(p75.notna(), np.nan)).diff()

def f58_cprt_057_energy_distance_acceleration_21d_d1(close: pd.Series) -> pd.Series:
    """21-bar change in 63d-energy-distance."""
    r = _log_ret(close)
    e = _energy_distance(r, QDAYS)
    return (e - e.shift(MDAYS)).diff()

def f58_cprt_058_energy_distance_change_z_252d_d1(close: pd.Series) -> pd.Series:
    """z-score of (current - prior 21-bar) E-stat over 252d."""
    r = _log_ret(close)
    e = _energy_distance(r, QDAYS)
    ch = e - e.shift(MDAYS)
    return (_rolling_zscore(ch, YDAYS)).diff()

def f58_cprt_059_bcp_run_length_mean_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Bayesian online change-point: expected run-length over 252d log-returns."""
    r = _log_ret(close)
    return (_bayesian_cp_run_length_mean(r, YDAYS, 0.01)).diff()

def f58_cprt_060_bcp_run_length_mean_log_ret_504d_d1(close: pd.Series) -> pd.Series:
    """BOCP expected run-length over 504d."""
    r = _log_ret(close)
    return (_bayesian_cp_run_length_mean(r, DDAYS_2Y, 0.01)).diff()

def f58_cprt_061_bcp_run_length_mean_log_close_252d_d1(close: pd.Series) -> pd.Series:
    """BOCP on log-close over 252d."""
    lc = _safe_log(close)
    return (_bayesian_cp_run_length_mean(lc, YDAYS, 0.01)).diff()

def f58_cprt_062_bcp_run_length_mean_abs_ret_252d_d1(close: pd.Series) -> pd.Series:
    """BOCP on |r| over 252d."""
    x = _log_ret(close).abs()
    return (_bayesian_cp_run_length_mean(x, YDAYS, 0.01)).diff()

def f58_cprt_063_bcp_run_length_drop_pct_21d_d1(close: pd.Series) -> pd.Series:
    """% drop in BOCP-run-length over 21d (sharp drop = change)."""
    r = _log_ret(close)
    b = _bayesian_cp_run_length_mean(r, YDAYS, 0.01)
    return (_safe_div(b - b.shift(MDAYS), b.shift(MDAYS))).diff()

def f58_cprt_064_bcp_run_length_z_252d_d1(close: pd.Series) -> pd.Series:
    """z-score of BOCP run-length over 252d."""
    r = _log_ret(close)
    b = _bayesian_cp_run_length_mean(r, YDAYS, 0.01)
    return (_rolling_zscore(b, YDAYS)).diff()

def f58_cprt_065_bcp_run_length_low_at_252h_indicator_d1(close: pd.Series) -> pd.Series:
    """BOCP run-length < 252d-q25 AND close = 252d max (change detected at top)."""
    r = _log_ret(close)
    b = _bayesian_cp_run_length_mean(r, YDAYS, 0.01)
    q25 = b.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return (((b < q25) & (close >= rmax - 1e-12)).astype(float).where(q25.notna(), np.nan)).diff()

def f58_cprt_066_bcp_high_hazard_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """BOCP with hazard=0.05 (more change-prone) on log-returns over 252d."""
    r = _log_ret(close)
    return (_bayesian_cp_run_length_mean(r, YDAYS, 0.05)).diff()

def f58_cprt_067_bcp_low_hazard_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """BOCP with hazard=0.002 (less change-prone) on log-returns over 252d."""
    r = _log_ret(close)
    return (_bayesian_cp_run_length_mean(r, YDAYS, 0.002)).diff()

def f58_cprt_068_bcp_run_length_high_vs_low_hazard_diff_252d_d1(close: pd.Series) -> pd.Series:
    """BOCP(hazard=0.002) - BOCP(hazard=0.05) - sensitivity to hazard prior."""
    r = _log_ret(close)
    l = _bayesian_cp_run_length_mean(r, YDAYS, 0.002)
    h = _bayesian_cp_run_length_mean(r, YDAYS, 0.05)
    return (l - h).diff()

def f58_cprt_069_bcp_run_length_change_speed_5d_d1(close: pd.Series) -> pd.Series:
    """5-bar change in BOCP run-length over 252d window."""
    r = _log_ret(close)
    b = _bayesian_cp_run_length_mean(r, YDAYS, 0.01)
    return (b - b.shift(WDAYS)).diff()

def f58_cprt_070_bcp_run_length_low_persistence_63d_d1(close: pd.Series) -> pd.Series:
    """Fraction of last 63d where BOCP run-length < 252d-q25."""
    r = _log_ret(close)
    b = _bayesian_cp_run_length_mean(r, YDAYS, 0.01)
    q25 = b.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    ind = (b < q25).astype(float).where(q25.notna(), np.nan)
    return (ind.rolling(QDAYS, min_periods=MDAYS).mean()).diff()

def f58_cprt_071_bcp_minus_long_term_mean_run_length_252d_d1(close: pd.Series) -> pd.Series:
    """BOCP run-length minus 504d-mean of BOCP - deviation from baseline."""
    r = _log_ret(close)
    b = _bayesian_cp_run_length_mean(r, YDAYS, 0.01)
    bm = b.rolling(DDAYS_2Y, min_periods=YDAYS).mean()
    return (b - bm).diff()

def f58_cprt_072_bcp_run_length_at_252d_min_indicator_d1(close: pd.Series) -> pd.Series:
    """Indicator: BOCP run-length is at 252d minimum (fresh change detected)."""
    r = _log_ret(close)
    b = _bayesian_cp_run_length_mean(r, YDAYS, 0.01)
    mn = b.rolling(YDAYS, min_periods=QDAYS).min()
    return ((b <= mn + 1e-9).astype(float).where(b.notna(), np.nan)).diff()

def f58_cprt_073_bcp_run_length_acceleration_d2_252d_d1(close: pd.Series) -> pd.Series:
    """2nd-order diff of BOCP run-length over 252d."""
    r = _log_ret(close)
    b = _bayesian_cp_run_length_mean(r, YDAYS, 0.01)
    return (b.diff().diff()).diff()

def f58_cprt_074_variance_ratio_21d_over_252d_log_ret_d1(close: pd.Series) -> pd.Series:
    """Var(21dr) / Var(252dr) - sharp value increase = change."""
    r = _log_ret(close)
    return (_variance_ratio_change(r, MDAYS, YDAYS)).diff()

def f58_cprt_075_variance_ratio_63d_over_252d_log_ret_d1(close: pd.Series) -> pd.Series:
    """Var(63dr) / Var(252dr) - sharp value increase = change."""
    r = _log_ret(close)
    return (_variance_ratio_change(r, QDAYS, YDAYS)).diff()


CHANGE_POINT_REGIME_TRANSITION_D1_REGISTRY_001_075 = {
    "f58_cprt_001_cusum_pos_log_ret_21d_d1": {"inputs": ["close"], "func": f58_cprt_001_cusum_pos_log_ret_21d_d1},
    "f58_cprt_002_cusum_neg_log_ret_21d_d1": {"inputs": ["close"], "func": f58_cprt_002_cusum_neg_log_ret_21d_d1},
    "f58_cprt_003_cusum_diff_pos_neg_log_ret_21d_d1": {"inputs": ["close"], "func": f58_cprt_003_cusum_diff_pos_neg_log_ret_21d_d1},
    "f58_cprt_004_cusum_pos_log_ret_63d_d1": {"inputs": ["close"], "func": f58_cprt_004_cusum_pos_log_ret_63d_d1},
    "f58_cprt_005_cusum_neg_log_ret_63d_d1": {"inputs": ["close"], "func": f58_cprt_005_cusum_neg_log_ret_63d_d1},
    "f58_cprt_006_cusum_diff_pos_neg_log_ret_63d_d1": {"inputs": ["close"], "func": f58_cprt_006_cusum_diff_pos_neg_log_ret_63d_d1},
    "f58_cprt_007_cusum_pos_log_ret_252d_d1": {"inputs": ["close"], "func": f58_cprt_007_cusum_pos_log_ret_252d_d1},
    "f58_cprt_008_cusum_neg_log_ret_252d_d1": {"inputs": ["close"], "func": f58_cprt_008_cusum_neg_log_ret_252d_d1},
    "f58_cprt_009_cusum_diff_pos_neg_log_ret_252d_d1": {"inputs": ["close"], "func": f58_cprt_009_cusum_diff_pos_neg_log_ret_252d_d1},
    "f58_cprt_010_cusum_pos_abs_ret_63d_d1": {"inputs": ["close"], "func": f58_cprt_010_cusum_pos_abs_ret_63d_d1},
    "f58_cprt_011_cusum_variance_log_ret_63d_d1": {"inputs": ["close"], "func": f58_cprt_011_cusum_variance_log_ret_63d_d1},
    "f58_cprt_012_cusum_pos_abs_ret_252d_d1": {"inputs": ["close"], "func": f58_cprt_012_cusum_pos_abs_ret_252d_d1},
    "f58_cprt_013_cusum_variance_log_ret_252d_d1": {"inputs": ["close"], "func": f58_cprt_013_cusum_variance_log_ret_252d_d1},
    "f58_cprt_014_cusum_log_close_252d_d1": {"inputs": ["close"], "func": f58_cprt_014_cusum_log_close_252d_d1},
    "f58_cprt_015_cusum_log_close_504d_d1": {"inputs": ["close"], "func": f58_cprt_015_cusum_log_close_504d_d1},
    "f58_cprt_016_page_hinkley_pos_log_ret_63d_d1": {"inputs": ["close"], "func": f58_cprt_016_page_hinkley_pos_log_ret_63d_d1},
    "f58_cprt_017_page_hinkley_neg_log_ret_63d_d1": {"inputs": ["close"], "func": f58_cprt_017_page_hinkley_neg_log_ret_63d_d1},
    "f58_cprt_018_page_hinkley_pos_abs_ret_63d_d1": {"inputs": ["close"], "func": f58_cprt_018_page_hinkley_pos_abs_ret_63d_d1},
    "f58_cprt_019_page_hinkley_pos_log_ret_252d_d1": {"inputs": ["close"], "func": f58_cprt_019_page_hinkley_pos_log_ret_252d_d1},
    "f58_cprt_020_page_hinkley_neg_log_ret_252d_d1": {"inputs": ["close"], "func": f58_cprt_020_page_hinkley_neg_log_ret_252d_d1},
    "f58_cprt_021_page_hinkley_pos_abs_ret_252d_d1": {"inputs": ["close"], "func": f58_cprt_021_page_hinkley_pos_abs_ret_252d_d1},
    "f58_cprt_022_page_hinkley_log_close_252d_d1": {"inputs": ["close"], "func": f58_cprt_022_page_hinkley_log_close_252d_d1},
    "f58_cprt_023_page_hinkley_log_close_504d_d1": {"inputs": ["close"], "func": f58_cprt_023_page_hinkley_log_close_504d_d1},
    "f58_cprt_024_page_hinkley_delta_001_log_ret_252d_d1": {"inputs": ["close"], "func": f58_cprt_024_page_hinkley_delta_001_log_ret_252d_d1},
    "f58_cprt_025_page_hinkley_delta_005_log_ret_252d_d1": {"inputs": ["close"], "func": f58_cprt_025_page_hinkley_delta_005_log_ret_252d_d1},
    "f58_cprt_026_page_hinkley_neg_log_close_252d_d1": {"inputs": ["close"], "func": f58_cprt_026_page_hinkley_neg_log_close_252d_d1},
    "f58_cprt_027_page_hinkley_neg_log_close_504d_d1": {"inputs": ["close"], "func": f58_cprt_027_page_hinkley_neg_log_close_504d_d1},
    "f58_cprt_028_page_hinkley_diff_pos_neg_log_ret_252d_d1": {"inputs": ["close"], "func": f58_cprt_028_page_hinkley_diff_pos_neg_log_ret_252d_d1},
    "f58_cprt_029_max_split_t_stat_log_ret_63d_d1": {"inputs": ["close"], "func": f58_cprt_029_max_split_t_stat_log_ret_63d_d1},
    "f58_cprt_030_max_split_t_stat_log_ret_252d_d1": {"inputs": ["close"], "func": f58_cprt_030_max_split_t_stat_log_ret_252d_d1},
    "f58_cprt_031_max_split_t_stat_log_ret_504d_d1": {"inputs": ["close"], "func": f58_cprt_031_max_split_t_stat_log_ret_504d_d1},
    "f58_cprt_032_max_split_t_stat_abs_ret_252d_d1": {"inputs": ["close"], "func": f58_cprt_032_max_split_t_stat_abs_ret_252d_d1},
    "f58_cprt_033_max_split_t_stat_log_close_252d_d1": {"inputs": ["close"], "func": f58_cprt_033_max_split_t_stat_log_close_252d_d1},
    "f58_cprt_034_max_split_t_stat_log_close_504d_d1": {"inputs": ["close"], "func": f58_cprt_034_max_split_t_stat_log_close_504d_d1},
    "f58_cprt_035_max_split_t_stat_log_volume_252d_d1": {"inputs": ["volume"], "func": f58_cprt_035_max_split_t_stat_log_volume_252d_d1},
    "f58_cprt_036_max_split_t_stat_high_low_range_252d_d1": {"inputs": ["high", "low", "close"], "func": f58_cprt_036_max_split_t_stat_high_low_range_252d_d1},
    "f58_cprt_037_max_split_t_stat_overnight_ret_252d_d1": {"inputs": ["open", "close"], "func": f58_cprt_037_max_split_t_stat_overnight_ret_252d_d1},
    "f58_cprt_038_max_split_t_stat_dollar_vol_252d_d1": {"inputs": ["close", "volume"], "func": f58_cprt_038_max_split_t_stat_dollar_vol_252d_d1},
    "f58_cprt_039_max_split_t_stat_intraday_ret_252d_d1": {"inputs": ["open", "close"], "func": f58_cprt_039_max_split_t_stat_intraday_ret_252d_d1},
    "f58_cprt_040_max_split_t_stat_squared_ret_252d_d1": {"inputs": ["close"], "func": f58_cprt_040_max_split_t_stat_squared_ret_252d_d1},
    "f58_cprt_041_split_t_zscore_log_ret_252d_252d_d1": {"inputs": ["close"], "func": f58_cprt_041_split_t_zscore_log_ret_252d_252d_d1},
    "f58_cprt_042_split_t_top_decile_indicator_252d_d1": {"inputs": ["close"], "func": f58_cprt_042_split_t_top_decile_indicator_252d_d1},
    "f58_cprt_043_split_t_above_threshold_at_252h_indicator_d1": {"inputs": ["close"], "func": f58_cprt_043_split_t_above_threshold_at_252h_indicator_d1},
    "f58_cprt_044_energy_distance_log_ret_63d_d1": {"inputs": ["close"], "func": f58_cprt_044_energy_distance_log_ret_63d_d1},
    "f58_cprt_045_energy_distance_log_ret_252d_d1": {"inputs": ["close"], "func": f58_cprt_045_energy_distance_log_ret_252d_d1},
    "f58_cprt_046_energy_distance_log_ret_504d_d1": {"inputs": ["close"], "func": f58_cprt_046_energy_distance_log_ret_504d_d1},
    "f58_cprt_047_energy_distance_abs_log_ret_252d_d1": {"inputs": ["close"], "func": f58_cprt_047_energy_distance_abs_log_ret_252d_d1},
    "f58_cprt_048_energy_distance_log_volume_252d_d1": {"inputs": ["volume"], "func": f58_cprt_048_energy_distance_log_volume_252d_d1},
    "f58_cprt_049_energy_distance_atr_norm_252d_d1": {"inputs": ["high", "low", "close"], "func": f58_cprt_049_energy_distance_atr_norm_252d_d1},
    "f58_cprt_050_energy_distance_overnight_ret_252d_d1": {"inputs": ["open", "close"], "func": f58_cprt_050_energy_distance_overnight_ret_252d_d1},
    "f58_cprt_051_energy_distance_close_pos_in_range_252d_d1": {"inputs": ["high", "low", "close"], "func": f58_cprt_051_energy_distance_close_pos_in_range_252d_d1},
    "f58_cprt_052_energy_distance_log_close_504d_d1": {"inputs": ["close"], "func": f58_cprt_052_energy_distance_log_close_504d_d1},
    "f58_cprt_053_energy_distance_squared_log_ret_252d_d1": {"inputs": ["close"], "func": f58_cprt_053_energy_distance_squared_log_ret_252d_d1},
    "f58_cprt_054_energy_distance_zscore_252d_d1": {"inputs": ["close"], "func": f58_cprt_054_energy_distance_zscore_252d_d1},
    "f58_cprt_055_energy_distance_above_p90_indicator_252d_d1": {"inputs": ["close"], "func": f58_cprt_055_energy_distance_above_p90_indicator_252d_d1},
    "f58_cprt_056_energy_distance_at_252h_indicator_d1": {"inputs": ["close"], "func": f58_cprt_056_energy_distance_at_252h_indicator_d1},
    "f58_cprt_057_energy_distance_acceleration_21d_d1": {"inputs": ["close"], "func": f58_cprt_057_energy_distance_acceleration_21d_d1},
    "f58_cprt_058_energy_distance_change_z_252d_d1": {"inputs": ["close"], "func": f58_cprt_058_energy_distance_change_z_252d_d1},
    "f58_cprt_059_bcp_run_length_mean_log_ret_252d_d1": {"inputs": ["close"], "func": f58_cprt_059_bcp_run_length_mean_log_ret_252d_d1},
    "f58_cprt_060_bcp_run_length_mean_log_ret_504d_d1": {"inputs": ["close"], "func": f58_cprt_060_bcp_run_length_mean_log_ret_504d_d1},
    "f58_cprt_061_bcp_run_length_mean_log_close_252d_d1": {"inputs": ["close"], "func": f58_cprt_061_bcp_run_length_mean_log_close_252d_d1},
    "f58_cprt_062_bcp_run_length_mean_abs_ret_252d_d1": {"inputs": ["close"], "func": f58_cprt_062_bcp_run_length_mean_abs_ret_252d_d1},
    "f58_cprt_063_bcp_run_length_drop_pct_21d_d1": {"inputs": ["close"], "func": f58_cprt_063_bcp_run_length_drop_pct_21d_d1},
    "f58_cprt_064_bcp_run_length_z_252d_d1": {"inputs": ["close"], "func": f58_cprt_064_bcp_run_length_z_252d_d1},
    "f58_cprt_065_bcp_run_length_low_at_252h_indicator_d1": {"inputs": ["close"], "func": f58_cprt_065_bcp_run_length_low_at_252h_indicator_d1},
    "f58_cprt_066_bcp_high_hazard_log_ret_252d_d1": {"inputs": ["close"], "func": f58_cprt_066_bcp_high_hazard_log_ret_252d_d1},
    "f58_cprt_067_bcp_low_hazard_log_ret_252d_d1": {"inputs": ["close"], "func": f58_cprt_067_bcp_low_hazard_log_ret_252d_d1},
    "f58_cprt_068_bcp_run_length_high_vs_low_hazard_diff_252d_d1": {"inputs": ["close"], "func": f58_cprt_068_bcp_run_length_high_vs_low_hazard_diff_252d_d1},
    "f58_cprt_069_bcp_run_length_change_speed_5d_d1": {"inputs": ["close"], "func": f58_cprt_069_bcp_run_length_change_speed_5d_d1},
    "f58_cprt_070_bcp_run_length_low_persistence_63d_d1": {"inputs": ["close"], "func": f58_cprt_070_bcp_run_length_low_persistence_63d_d1},
    "f58_cprt_071_bcp_minus_long_term_mean_run_length_252d_d1": {"inputs": ["close"], "func": f58_cprt_071_bcp_minus_long_term_mean_run_length_252d_d1},
    "f58_cprt_072_bcp_run_length_at_252d_min_indicator_d1": {"inputs": ["close"], "func": f58_cprt_072_bcp_run_length_at_252d_min_indicator_d1},
    "f58_cprt_073_bcp_run_length_acceleration_d2_252d_d1": {"inputs": ["close"], "func": f58_cprt_073_bcp_run_length_acceleration_d2_252d_d1},
    "f58_cprt_074_variance_ratio_21d_over_252d_log_ret_d1": {"inputs": ["close"], "func": f58_cprt_074_variance_ratio_21d_over_252d_log_ret_d1},
    "f58_cprt_075_variance_ratio_63d_over_252d_log_ret_d1": {"inputs": ["close"], "func": f58_cprt_075_variance_ratio_63d_over_252d_log_ret_d1},
}
