"""advanced_tail_drawdown_structure d3 features 001-075 - Pipeline 1b-technical.

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

def _drawdown_episodes(close):
    """Identify drawdown episodes. Returns lists of (start_idx, trough_idx, end_idx, depth, duration).
    end_idx = first new-high after the trough (or last idx if not yet recovered)."""
    lc = _safe_log(close).values
    n = len(lc)
    peaks = np.maximum.accumulate(lc)
    in_dd = lc < peaks - 1e-12
    episodes = []
    i = 0
    while i < n:
        if not np.isnan(lc[i]) and in_dd[i] and (i == 0 or not in_dd[i - 1]):
            start = i
            trough_idx = start
            trough_val = lc[start]
            cur_peak = peaks[start]
            j = i
            while j < n and (np.isnan(lc[j]) or lc[j] < cur_peak - 1e-12):
                if not np.isnan(lc[j]) and lc[j] < trough_val:
                    trough_val = lc[j]; trough_idx = j
                j += 1
            end = j if j < n else n - 1
            depth = cur_peak - trough_val  # positive
            duration = end - start
            episodes.append((start, trough_idx, end, depth, duration))
            i = j
        else:
            i += 1
    return episodes


def _drawdown_count_within_window(close, n):
    """Number of drawdown episodes whose trough falls within rolling n-bar window."""
    mp = max(n // 3, 30)
    episodes = _drawdown_episodes(close)
    troughs = np.array([e[1] for e in episodes], dtype=int) if episodes else np.array([], dtype=int)
    nb = len(close)
    out = np.full(nb, np.nan, dtype=float)
    for i in range(nb):
        if i < mp - 1:
            continue
        lo = max(0, i - n + 1)
        if troughs.size > 0:
            out[i] = float(((troughs >= lo) & (troughs <= i)).sum())
        else:
            out[i] = 0.0
    return pd.Series(out, index=close.index)


def _drawdown_depth_stats(close, n, stat):
    """Statistic on drawdown depths whose troughs lie in rolling n-bar window.
    stat in {'mean','median','skew','kurt','p95','count'}."""
    mp = max(n // 3, 30)
    episodes = _drawdown_episodes(close)
    nb = len(close)
    out = np.full(nb, np.nan, dtype=float)
    for i in range(nb):
        if i < mp - 1:
            continue
        lo = max(0, i - n + 1)
        depths = np.array([e[3] for e in episodes if lo <= e[1] <= i])
        if depths.size < 2:
            continue
        if stat == "mean":
            out[i] = float(depths.mean())
        elif stat == "median":
            out[i] = float(np.median(depths))
        elif stat == "p95":
            out[i] = float(np.quantile(depths, 0.95))
        elif stat == "skew":
            if depths.size < 3:
                continue
            mu = depths.mean(); sd = depths.std(ddof=1)
            if sd == 0:
                continue
            out[i] = float(((depths - mu) ** 3).mean() / sd ** 3)
        elif stat == "kurt":
            if depths.size < 4:
                continue
            mu = depths.mean(); sd = depths.std(ddof=1)
            if sd == 0:
                continue
            out[i] = float(((depths - mu) ** 4).mean() / sd ** 4 - 3.0)
        elif stat == "count":
            out[i] = float(depths.size)
    return pd.Series(out, index=close.index)


def _drawdown_duration_stats(close, n, stat):
    """Statistic on drawdown durations whose troughs lie in rolling n-bar window."""
    mp = max(n // 3, 30)
    episodes = _drawdown_episodes(close)
    nb = len(close)
    out = np.full(nb, np.nan, dtype=float)
    for i in range(nb):
        if i < mp - 1:
            continue
        lo = max(0, i - n + 1)
        durs = np.array([e[4] for e in episodes if lo <= e[1] <= i], dtype=float)
        if durs.size < 2:
            continue
        if stat == "mean":
            out[i] = float(durs.mean())
        elif stat == "median":
            out[i] = float(np.median(durs))
        elif stat == "max":
            out[i] = float(durs.max())
        elif stat == "p95":
            out[i] = float(np.quantile(durs, 0.95))
        elif stat == "skew":
            if durs.size < 3:
                continue
            mu = durs.mean(); sd = durs.std(ddof=1)
            if sd == 0:
                continue
            out[i] = float(((durs - mu) ** 3).mean() / sd ** 3)
        elif stat == "kurt":
            if durs.size < 4:
                continue
            mu = durs.mean(); sd = durs.std(ddof=1)
            if sd == 0:
                continue
            out[i] = float(((durs - mu) ** 4).mean() / sd ** 4 - 3.0)
    return pd.Series(out, index=close.index)


def _time_under_water_fraction(close, n):
    """Fraction of bars in rolling n-window where price is below its running max."""
    mp = max(n // 3, 20)
    lc = _safe_log(close)
    rmax = lc.expanding(min_periods=1).max()
    uw = (lc < rmax - 1e-12).astype(float).where(lc.notna(), np.nan)
    return uw.rolling(n, min_periods=mp).mean()


def _max_time_under_water_in_window(close, n):
    """Longest continuous time-under-water in rolling n-bar window."""
    mp = max(n // 3, 20)
    lc = _safe_log(close)
    rmax = lc.expanding(min_periods=1).max()
    uw = (lc < rmax - 1e-12).astype(float).where(lc.notna(), np.nan)
    arr = uw.values
    out = np.full(len(arr), np.nan, dtype=float)
    for i in range(len(arr)):
        if i < mp - 1:
            continue
        lo = max(0, i - n + 1)
        cur = 0; best = 0
        for x in arr[lo:i + 1]:
            if np.isnan(x):
                cur = 0
            elif x > 0.5:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        out[i] = float(best)
    return pd.Series(out, index=close.index)


def _consecutive_neg_max(r, n):
    """Longest run of consecutive negative returns in rolling n-bar window."""
    mp = max(n // 3, 20)
    arr = r.values
    out = np.full(len(arr), np.nan, dtype=float)
    for i in range(len(arr)):
        if i < mp - 1:
            continue
        lo = max(0, i - n + 1)
        cur = 0; best = 0
        for x in arr[lo:i + 1]:
            if np.isnan(x):
                cur = 0
            elif x < 0:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        out[i] = float(best)
    return pd.Series(out, index=r.index)


def _kupiec_pof_lr(r, n, q):
    """Kupiec POF likelihood-ratio: -2*log[((1-p)^(n-x) p^x) / ((1-x/n)^(n-x) (x/n)^x)] for p=1-q."""
    mp = max(n // 3, 30)
    v = -r
    var_s = _rolling_q(v, n, q)
    breach = (v > var_s).astype(float).where(var_s.notna(), np.nan)
    breach_cnt = breach.rolling(n, min_periods=mp).sum()
    valid_cnt = breach.rolling(n, min_periods=mp).count()
    p = 1.0 - q
    eps = 1e-9
    pi_hat = (breach_cnt / valid_cnt.replace(0, np.nan)).clip(lower=eps, upper=1.0 - eps)
    ll_null = breach_cnt * np.log(p) + (valid_cnt - breach_cnt) * np.log(1.0 - p)
    ll_alt = breach_cnt * np.log(pi_hat) + (valid_cnt - breach_cnt) * np.log(1.0 - pi_hat)
    return -2.0 * (ll_null - ll_alt)


def _christoffersen_independence_lr(r, n, q):
    """LR_ind statistic for breach independence (Markov-chain). 0 = independent breaches."""
    mp = max(n // 3, 30)
    v = -r
    var_s = _rolling_q(v, n, q)
    breach = (v > var_s).astype(float).where(var_s.notna(), np.nan)
    arr = breach.values
    out = np.full(len(arr), np.nan, dtype=float)
    eps = 1e-9
    for i in range(len(arr)):
        if i < mp - 1:
            continue
        lo = max(0, i - n + 1)
        seq = arr[lo:i + 1]
        seq = seq[~np.isnan(seq)]
        if seq.size < 30:
            continue
        n00 = n01 = n10 = n11 = 0
        for j in range(1, seq.size):
            a = int(seq[j - 1]); b = int(seq[j])
            if a == 0 and b == 0:
                n00 += 1
            elif a == 0 and b == 1:
                n01 += 1
            elif a == 1 and b == 0:
                n10 += 1
            else:
                n11 += 1
            j += 0
        pi01 = n01 / max(n00 + n01, 1)
        pi11 = n11 / max(n10 + n11, 1)
        pi = (n01 + n11) / max(n00 + n01 + n10 + n11, 1)
        pi01_c = min(max(pi01, eps), 1.0 - eps)
        pi11_c = min(max(pi11, eps), 1.0 - eps)
        pi_c = min(max(pi, eps), 1.0 - eps)
        ll_null = (n01 + n11) * np.log(pi_c) + (n00 + n10) * np.log(1.0 - pi_c)
        ll_alt = (n01 * np.log(pi01_c) + n00 * np.log(1.0 - pi01_c)
                  + n11 * np.log(pi11_c) + n10 * np.log(1.0 - pi11_c))
        out[i] = -2.0 * (ll_null - ll_alt)
    return pd.Series(out, index=r.index)


def _acerbi_szekely_z1(r, n, q):
    """Acerbi-Szekely Z1 = mean(loss/ES on breach days) + 1. Reject if << 0."""
    mp = max(n // 3, 30)
    v = -r
    var_s = _rolling_q(v, n, q)
    def _es_window(w, q_):
        x = w[~np.isnan(w)]
        if x.size < 30:
            return np.nan
        thr = np.quantile(x, q_)
        tail = x[x >= thr]
        return float(tail.mean()) if tail.size > 0 else np.nan
    es = v.rolling(n, min_periods=mp).apply(lambda w: _es_window(w, q), raw=True)
    breach = (v > var_s).astype(float).where(var_s.notna(), np.nan)
    breach_loss = v.where(breach > 0.5, np.nan)
    ratio = breach_loss / es.replace(0, np.nan)
    mean_ratio = ratio.rolling(n, min_periods=mp).mean()
    return -(mean_ratio - 1.0)


def _acerbi_szekely_z2(r, n, q):
    """Acerbi-Szekely Z2 = sum(loss * I_breach / ES) / ((1-q)*N) + 1."""
    mp = max(n // 3, 30)
    v = -r
    var_s = _rolling_q(v, n, q)
    def _es_window(w, q_):
        x = w[~np.isnan(w)]
        if x.size < 30:
            return np.nan
        thr = np.quantile(x, q_)
        tail = x[x >= thr]
        return float(tail.mean()) if tail.size > 0 else np.nan
    es = v.rolling(n, min_periods=mp).apply(lambda w: _es_window(w, q), raw=True)
    breach = (v > var_s).astype(float).where(var_s.notna(), np.nan)
    contribution = (v * breach / es.replace(0, np.nan)).fillna(0.0)
    sum_contrib = contribution.rolling(n, min_periods=mp).sum()
    cnt = breach.rolling(n, min_periods=mp).count()
    return -(sum_contrib / ((1.0 - q) * cnt.replace(0, np.nan)) - 1.0)


def _caviar_sav_fit_window(v, q, b1_grid=None, b2_grid=None, b3_grid=None):
    """CAViaR SAV: q_t = b1 + b2 * q_{t-1} + b3 * |r_{t-1}|. Returns (b1, b2, b3, current_q, loss)."""
    if b1_grid is None:
        b1_grid = (0.001, 0.003, 0.005, 0.010)
    if b2_grid is None:
        b2_grid = (0.50, 0.70, 0.85, 0.95)
    if b3_grid is None:
        b3_grid = (0.10, 0.30, 0.50, 0.80)
    v = v[~np.isnan(v)]
    if v.size < 60:
        return (np.nan, np.nan, np.nan, np.nan, np.nan)
    init = -np.quantile(v[:min(60, v.size)], 1.0 - q)  # initial VaR
    if not np.isfinite(init):
        init = 0.01
    best = (np.nan, np.nan, np.nan, np.nan, np.inf)
    p = 1.0 - q
    for b1 in b1_grid:
        for b2 in b2_grid:
            for b3 in b3_grid:
                qt = init; loss = 0.0
                for x in v[1:]:
                    qt = b1 + b2 * qt + b3 * abs(x)
                    if qt <= 0:
                        loss = np.inf; break
                    excess = -x - qt
                    loss += (p - (1.0 if excess > 0 else 0.0)) * excess
                if loss < best[4]:
                    best = (b1, b2, b3, qt, loss)
    return best


def _rolling_caviar_sav(s, n, q, want_idx):
    """Rolling CAViaR SAV (refit every 21 bars). want_idx 0..4."""
    mp = max(n // 3, 60)
    arr = s.values
    nb = len(arr)
    out = np.full(nb, np.nan, dtype=float)
    last = (np.nan,) * 5
    for i in range(nb):
        if i < mp - 1:
            continue
        if i % 21 == 0 or np.isnan(last[want_idx]):
            lo = max(0, i - n + 1)
            last = _caviar_sav_fit_window(arr[lo:i + 1], q)
        out[i] = last[want_idx]
    return pd.Series(out, index=s.index)


def _caviar_asym_fit_window(v, q):
    """CAViaR asymmetric-slope: q_t = b1 + b2*q_{t-1} + b3+ * pos + b3- * neg."""
    v = v[~np.isnan(v)]
    if v.size < 60:
        return (np.nan,) * 5
    init = -np.quantile(v[:min(60, v.size)], 1.0 - q)
    if not np.isfinite(init):
        init = 0.01
    best = (np.nan, np.nan, np.nan, np.nan, np.inf)
    p = 1.0 - q
    for b1 in (0.001, 0.005, 0.010):
        for b2 in (0.70, 0.85, 0.95):
            for b3p in (0.05, 0.20, 0.40):
                for b3n in (0.20, 0.50, 0.80):
                    qt = init; loss = 0.0
                    for x in v[1:]:
                        pos_term = max(x, 0.0); neg_term = max(-x, 0.0)
                        qt = b1 + b2 * qt + b3p * pos_term + b3n * neg_term
                        if qt <= 0:
                            loss = np.inf; break
                        excess = -x - qt
                        loss += (p - (1.0 if excess > 0 else 0.0)) * excess
                    if loss < best[4]:
                        best = (b2, b3p, b3n, qt, loss)
    return best


def _rolling_caviar_asym(s, n, q, want_idx):
    """Rolling CAViaR asymmetric (refit every 21 bars). want_idx 0..4."""
    mp = max(n // 3, 60)
    arr = s.values
    nb = len(arr)
    out = np.full(nb, np.nan, dtype=float)
    last = (np.nan,) * 5
    for i in range(nb):
        if i < mp - 1:
            continue
        if i % 21 == 0 or np.isnan(last[want_idx]):
            lo = max(0, i - n + 1)
            last = _caviar_asym_fit_window(arr[lo:i + 1], q)
        out[i] = last[want_idx]
    return pd.Series(out, index=s.index)


def _range_based_var(high, low, close, n, q):
    """Range-based VaR using Parkinson std and normal-quantile."""
    ln_hl = (_safe_log(high) - _safe_log(low)) ** 2
    park_var = ln_hl.rolling(n, min_periods=max(n // 3, 5)).mean() / (4.0 * np.log(2.0))
    sd = park_var.pow(0.5)
    z = _norm_ppf(1.0 - q)
    return -(sd * z)


def _atr_based_var(high, low, close, n, q):
    """ATR-implied VaR using ATR/close * |z_q|."""
    atr = _atr(high, low, close, n=MDAYS)
    z = _norm_ppf(1.0 - q)
    return -(_safe_div(atr, close) * z).rolling(n, min_periods=max(n // 3, 10)).mean()


def _rolling_max_drawdown(close, n):
    mp = max(n // 3, 20)
    lc = _safe_log(close)
    def _md(w):
        v = w[~np.isnan(w)]
        if v.size < 10:
            return np.nan
        cm = np.maximum.accumulate(v)
        return float((v - cm).min())
    return lc.rolling(n, min_periods=mp).apply(_md, raw=True)


def f53_atds_001_drawdown_count_252d_d3(close: pd.Series) -> pd.Series:
    """Number of distinct drawdown episodes in last 252d."""
    return (_drawdown_count_within_window(close, YDAYS)).diff().diff().diff()

def f53_atds_002_drawdown_count_504d_d3(close: pd.Series) -> pd.Series:
    """Number of distinct drawdown episodes in last 504d."""
    return (_drawdown_count_within_window(close, DDAYS_2Y)).diff().diff().diff()

def f53_atds_003_drawdown_mean_depth_252d_d3(close: pd.Series) -> pd.Series:
    """Mean depth of drawdowns whose troughs occurred in last 252d."""
    return (_drawdown_depth_stats(close, YDAYS, 'mean')).diff().diff().diff()

def f53_atds_004_drawdown_median_depth_252d_d3(close: pd.Series) -> pd.Series:
    """Median depth of drawdowns in 252d."""
    return (_drawdown_depth_stats(close, YDAYS, 'median')).diff().diff().diff()

def f53_atds_005_drawdown_p95_depth_252d_d3(close: pd.Series) -> pd.Series:
    """95th percentile of drawdown depths in 252d."""
    return (_drawdown_depth_stats(close, YDAYS, 'p95')).diff().diff().diff()

def f53_atds_006_drawdown_depth_skew_252d_d3(close: pd.Series) -> pd.Series:
    """Skewness of drawdown depths in 252d."""
    return (_drawdown_depth_stats(close, YDAYS, 'skew')).diff().diff().diff()

def f53_atds_007_drawdown_depth_kurt_252d_d3(close: pd.Series) -> pd.Series:
    """Excess kurt of drawdown depths in 252d."""
    return (_drawdown_depth_stats(close, YDAYS, 'kurt')).diff().diff().diff()

def f53_atds_008_drawdown_mean_duration_252d_d3(close: pd.Series) -> pd.Series:
    """Mean duration (bars) of drawdowns in 252d."""
    return (_drawdown_duration_stats(close, YDAYS, 'mean')).diff().diff().diff()

def f53_atds_009_drawdown_median_duration_252d_d3(close: pd.Series) -> pd.Series:
    """Median duration of drawdowns in 252d."""
    return (_drawdown_duration_stats(close, YDAYS, 'median')).diff().diff().diff()

def f53_atds_010_drawdown_count_per_year_proxy_504d_d3(close: pd.Series) -> pd.Series:
    """Drawdown count per 252-bar year over a 504d window = count_504d / 2."""
    ct = _drawdown_count_within_window(close, DDAYS_2Y)
    return (ct / 2.0).diff().diff().diff()

def f53_atds_011_time_under_water_frac_252d_d3(close: pd.Series) -> pd.Series:
    """Fraction of last 252d below the running peak."""
    return (_time_under_water_fraction(close, YDAYS)).diff().diff().diff()

def f53_atds_012_time_under_water_frac_504d_d3(close: pd.Series) -> pd.Series:
    """Fraction of last 504d below the running peak."""
    return (_time_under_water_fraction(close, DDAYS_2Y)).diff().diff().diff()

def f53_atds_013_time_under_water_frac_1260d_d3(close: pd.Series) -> pd.Series:
    """Fraction of last 1260d below the running peak."""
    return (_time_under_water_fraction(close, DDAYS_5Y)).diff().diff().diff()

def f53_atds_014_max_time_under_water_252d_d3(close: pd.Series) -> pd.Series:
    """Longest continuous bars-under-water in last 252d."""
    return (_max_time_under_water_in_window(close, YDAYS)).diff().diff().diff()

def f53_atds_015_max_time_under_water_504d_d3(close: pd.Series) -> pd.Series:
    """Longest continuous bars-under-water in last 504d."""
    return (_max_time_under_water_in_window(close, DDAYS_2Y)).diff().diff().diff()

def f53_atds_016_drawdown_duration_max_252d_d3(close: pd.Series) -> pd.Series:
    """Maximum duration of any drawdown in 252d."""
    return (_drawdown_duration_stats(close, YDAYS, 'max')).diff().diff().diff()

def f53_atds_017_drawdown_duration_p95_252d_d3(close: pd.Series) -> pd.Series:
    """95th percentile of drawdown durations in 252d."""
    return (_drawdown_duration_stats(close, YDAYS, 'p95')).diff().diff().diff()

def f53_atds_018_drawdown_duration_skew_252d_d3(close: pd.Series) -> pd.Series:
    """Skewness of drawdown durations in 252d."""
    return (_drawdown_duration_stats(close, YDAYS, 'skew')).diff().diff().diff()

def f53_atds_019_recovery_attempts_count_252d_d3(close: pd.Series) -> pd.Series:
    """Count of recovered drawdowns in 252d (those that ended within the window)."""
    lc = _safe_log(close)
    rmax = lc.expanding(min_periods=1).max()
    is_high = (lc >= rmax - 1e-12).astype(float)
    new_high = ((is_high > 0.5) & (is_high.shift(1) < 0.5)).astype(float)
    return (new_high.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()

def f53_atds_020_recovery_efficiency_index_252d_d3(close: pd.Series) -> pd.Series:
    """Drawdown count / time_under_water_fraction over 252d - frequency-vs-depth recovery efficiency."""
    ct = _drawdown_count_within_window(close, YDAYS)
    tw = _time_under_water_fraction(close, YDAYS)
    return (_safe_div(ct, tw)).diff().diff().diff()

def f53_atds_021_acerbi_szekely_z1_es95_252d_d3(close: pd.Series) -> pd.Series:
    """Acerbi-Szekely Z1 backtest stat for ES(95) over 252d - >0 = ES under-estimates losses."""
    r = _log_ret(close)
    return (_acerbi_szekely_z1(r, YDAYS, 0.95)).diff().diff().diff()

def f53_atds_022_acerbi_szekely_z2_es95_252d_d3(close: pd.Series) -> pd.Series:
    """Acerbi-Szekely Z2 backtest stat for ES(95) over 252d."""
    r = _log_ret(close)
    return (_acerbi_szekely_z2(r, YDAYS, 0.95)).diff().diff().diff()

def f53_atds_023_acerbi_szekely_z1_es99_252d_d3(close: pd.Series) -> pd.Series:
    """Acerbi-Szekely Z1 for ES(99) over 252d."""
    r = _log_ret(close)
    return (_acerbi_szekely_z1(r, YDAYS, 0.99)).diff().diff().diff()

def f53_atds_024_acerbi_szekely_z2_es99_252d_d3(close: pd.Series) -> pd.Series:
    """Acerbi-Szekely Z2 for ES(99) over 252d."""
    r = _log_ret(close)
    return (_acerbi_szekely_z2(r, YDAYS, 0.99)).diff().diff().diff()

def f53_atds_025_es_breach_count_95_in_504d_d3(close: pd.Series) -> pd.Series:
    """Count of bars where loss > VaR(95) using 504d window for both VaR estimate and counting."""
    r = _log_ret(close)
    v = -_rolling_q(r, DDAYS_2Y, 0.05)
    br = (-r > v).astype(float).where(v.notna(), np.nan)
    return (br.rolling(DDAYS_2Y, min_periods=YDAYS).sum()).diff().diff().diff()

def f53_atds_026_es_breach_rate_minus_5pct_504d_d3(close: pd.Series) -> pd.Series:
    """VaR(95) breach rate minus 5% over 504d - coverage error at longer horizon."""
    r = _log_ret(close)
    v = -_rolling_q(r, DDAYS_2Y, 0.05)
    br = (-r > v).astype(float).where(v.notna(), np.nan)
    rate = br.rolling(DDAYS_2Y, min_periods=YDAYS).mean()
    return (rate - 0.05).diff().diff().diff()

def f53_atds_027_es_conditional_severity_score_252d_d3(close: pd.Series) -> pd.Series:
    """Mean (loss / ES_95) on breach days over 252d - >1 = ES under-estimates."""
    r = _log_ret(close)
    v = -_rolling_q(r, YDAYS, 0.05)
    def _es(w):
        x = -w[~np.isnan(w)]
        if x.size < 30:
            return np.nan
        thr = np.quantile(x, 0.95)
        tail = x[x >= thr]
        return float(tail.mean()) if tail.size > 0 else np.nan
    es = r.rolling(YDAYS, min_periods=QDAYS).apply(_es, raw=True)
    loss_on_breach = (-r).where(-r > v, np.nan)
    ratio = loss_on_breach / es.replace(0, np.nan)
    return (ratio.rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff().diff()

def f53_atds_028_es_pearson_consistency_252d_d3(close: pd.Series) -> pd.Series:
    """Pearson goodness-of-fit-like ES consistency = (observed loss sum - expected ES_95 * count) / count."""
    r = _log_ret(close)
    v = -_rolling_q(r, YDAYS, 0.05)
    def _es(w):
        x = -w[~np.isnan(w)]
        if x.size < 30:
            return np.nan
        thr = np.quantile(x, 0.95)
        tail = x[x >= thr]
        return float(tail.mean()) if tail.size > 0 else np.nan
    es = r.rolling(YDAYS, min_periods=QDAYS).apply(_es, raw=True)
    br = (-r > v).astype(float).where(v.notna(), np.nan)
    loss_sum = ((-r) * br).rolling(YDAYS, min_periods=QDAYS).sum()
    cnt = br.rolling(YDAYS, min_periods=QDAYS).sum()
    return (_safe_div(loss_sum - es * cnt, cnt)).diff().diff().diff()

def f53_atds_029_max_loss_div_es_95_252d_d3(close: pd.Series) -> pd.Series:
    """Maximum (loss / ES_95) ratio observed in last 252d."""
    r = _log_ret(close)
    def _es(w):
        x = -w[~np.isnan(w)]
        if x.size < 30:
            return np.nan
        thr = np.quantile(x, 0.95)
        tail = x[x >= thr]
        return float(tail.mean()) if tail.size > 0 else np.nan
    es = r.rolling(YDAYS, min_periods=QDAYS).apply(_es, raw=True)
    ratio = (-r) / es.replace(0, np.nan)
    return (ratio.rolling(YDAYS, min_periods=QDAYS).max()).diff().diff().diff()

def f53_atds_030_es_backtest_failure_rate_zscore_95_252d_d3(close: pd.Series) -> pd.Series:
    """Z-score of (breach rate - 5%) over 252d, normalized by sqrt(0.05*0.95/252)."""
    r = _log_ret(close)
    v = -_rolling_q(r, YDAYS, 0.05)
    br = (-r > v).astype(float).where(v.notna(), np.nan)
    rate = br.rolling(YDAYS, min_periods=QDAYS).mean()
    return ((rate - 0.05) / np.sqrt(0.05 * 0.95 / float(YDAYS))).diff().diff().diff()

def f53_atds_031_kupiec_pof_lr_var95_252d_d3(close: pd.Series) -> pd.Series:
    """Kupiec POF likelihood-ratio test stat for VaR(95) coverage over 252d."""
    r = _log_ret(close)
    return (_kupiec_pof_lr(r, YDAYS, 0.95)).diff().diff().diff()

def f53_atds_032_kupiec_pof_lr_var99_252d_d3(close: pd.Series) -> pd.Series:
    """Kupiec POF LR for VaR(99) coverage over 252d."""
    r = _log_ret(close)
    return (_kupiec_pof_lr(r, YDAYS, 0.99)).diff().diff().diff()

def f53_atds_033_kupiec_pof_lr_var95_504d_d3(close: pd.Series) -> pd.Series:
    """Kupiec POF LR for VaR(95) over 504d."""
    r = _log_ret(close)
    return (_kupiec_pof_lr(r, DDAYS_2Y, 0.95)).diff().diff().diff()

def f53_atds_034_christoffersen_independence_lr_var95_252d_d3(close: pd.Series) -> pd.Series:
    """Christoffersen independence-of-breaches LR for VaR(95) over 252d - tests clustered breaches."""
    r = _log_ret(close)
    return (_christoffersen_independence_lr(r, YDAYS, 0.95)).diff().diff().diff()

def f53_atds_035_christoffersen_independence_lr_var99_252d_d3(close: pd.Series) -> pd.Series:
    """Christoffersen independence LR for VaR(99) over 252d."""
    r = _log_ret(close)
    return (_christoffersen_independence_lr(r, YDAYS, 0.99)).diff().diff().diff()

def f53_atds_036_christoffersen_joint_lr_var95_252d_d3(close: pd.Series) -> pd.Series:
    """Christoffersen joint test = Kupiec POF + Independence LR for VaR(95) over 252d."""
    r = _log_ret(close)
    kp = _kupiec_pof_lr(r, YDAYS, 0.95)
    ci = _christoffersen_independence_lr(r, YDAYS, 0.95)
    return (kp + ci).diff().diff().diff()

def f53_atds_037_christoffersen_joint_lr_var99_252d_d3(close: pd.Series) -> pd.Series:
    """Christoffersen joint test for VaR(99) over 252d."""
    r = _log_ret(close)
    kp = _kupiec_pof_lr(r, YDAYS, 0.99)
    ci = _christoffersen_independence_lr(r, YDAYS, 0.99)
    return (kp + ci).diff().diff().diff()

def f53_atds_038_dq_test_stat_proxy_var95_252d_d3(close: pd.Series) -> pd.Series:
    """Dynamic Quantile test proxy: regression of hit-indicator on its lag1 over 252d (LB-style)."""
    r = _log_ret(close)
    v = -_rolling_q(r, YDAYS, 0.05)
    hit = ((-r > v).astype(float) - 0.05).where(v.notna(), np.nan)
    lag = hit.shift(1)
    return (hit.rolling(YDAYS, min_periods=QDAYS).corr(lag) ** 2 * YDAYS).diff().diff().diff()

def f53_atds_039_breach_first_order_autocorr_var95_252d_d3(close: pd.Series) -> pd.Series:
    """ACF(1) of VaR(95) breach indicator over 252d."""
    r = _log_ret(close)
    v = -_rolling_q(r, YDAYS, 0.05)
    br = (-r > v).astype(float).where(v.notna(), np.nan)
    lag = br.shift(1)
    return (br.rolling(YDAYS, min_periods=QDAYS).corr(lag)).diff().diff().diff()

def f53_atds_040_breach_clustering_pair_count_var99_252d_d3(close: pd.Series) -> pd.Series:
    """Count of consecutive-bar VaR(99) breaches over 252d."""
    r = _log_ret(close)
    v = -_rolling_q(r, YDAYS, 0.01)
    br = (-r > v).astype(float).where(v.notna(), np.nan)
    pair = (br * br.shift(1)).fillna(0.0)
    return (pair.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()

def f53_atds_041_caviar_sav_b2_persistence_q95_252d_d3(close: pd.Series) -> pd.Series:
    """CAViaR SAV autoregressive coefficient b2 for 95% VaR over 252d."""
    r = _log_ret(close)
    return (_rolling_caviar_sav(r, YDAYS, 0.95, 1)).diff().diff().diff()

def f53_atds_042_caviar_sav_b3_shock_q95_252d_d3(close: pd.Series) -> pd.Series:
    """CAViaR SAV shock coefficient b3 (on |r_{t-1}|) for 95% VaR over 252d."""
    r = _log_ret(close)
    return (_rolling_caviar_sav(r, YDAYS, 0.95, 2)).diff().diff().diff()

def f53_atds_043_caviar_sav_current_var_q95_252d_d3(close: pd.Series) -> pd.Series:
    """CAViaR SAV current VaR(95) estimate over 252d."""
    r = _log_ret(close)
    return (_rolling_caviar_sav(r, YDAYS, 0.95, 3)).diff().diff().diff()

def f53_atds_044_caviar_sav_quantile_loss_q95_252d_d3(close: pd.Series) -> pd.Series:
    """CAViaR SAV minimum quantile-loss over 252d."""
    r = _log_ret(close)
    return (_rolling_caviar_sav(r, YDAYS, 0.95, 4)).diff().diff().diff()

def f53_atds_045_caviar_sav_b2_persistence_q99_252d_d3(close: pd.Series) -> pd.Series:
    """CAViaR SAV b2 for 99% VaR over 252d."""
    r = _log_ret(close)
    return (_rolling_caviar_sav(r, YDAYS, 0.99, 1)).diff().diff().diff()

def f53_atds_046_caviar_asym_slope_b3pos_q95_252d_d3(close: pd.Series) -> pd.Series:
    """CAViaR Asymmetric-Slope coefficient on positive returns (b3+) for 95% VaR over 252d."""
    r = _log_ret(close)
    return (_rolling_caviar_asym(r, YDAYS, 0.95, 1)).diff().diff().diff()

def f53_atds_047_caviar_asym_slope_b3neg_q95_252d_d3(close: pd.Series) -> pd.Series:
    """CAViaR Asymmetric-Slope coefficient on negative returns (b3-) for 95% VaR over 252d."""
    r = _log_ret(close)
    return (_rolling_caviar_asym(r, YDAYS, 0.95, 2)).diff().diff().diff()

def f53_atds_048_caviar_asym_slope_neg_minus_pos_q95_252d_d3(close: pd.Series) -> pd.Series:
    """CAViaR Asym b3- minus b3+ over 252d - direct leverage in VaR dynamics."""
    r = _log_ret(close)
    bn = _rolling_caviar_asym(r, YDAYS, 0.95, 2)
    bp = _rolling_caviar_asym(r, YDAYS, 0.95, 1)
    return (bn - bp).diff().diff().diff()

def f53_atds_049_caviar_asym_current_var_q95_252d_d3(close: pd.Series) -> pd.Series:
    """CAViaR Asymmetric-Slope current VaR(95) estimate over 252d."""
    r = _log_ret(close)
    return (_rolling_caviar_asym(r, YDAYS, 0.95, 3)).diff().diff().diff()

def f53_atds_050_caviar_sav_minus_hist_var_q95_252d_d3(close: pd.Series) -> pd.Series:
    """CAViaR-SAV VaR(95) minus historical VaR(95) over 252d."""
    r = _log_ret(close)
    cv = _rolling_caviar_sav(r, YDAYS, 0.95, 3)
    hv = -_rolling_q(r, YDAYS, 0.05)
    return (cv - hv).diff().diff().diff()

def f53_atds_051_range_based_var_95_log_ret_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Range-based (Parkinson) VaR(95) over 252d using high-low ranges, normal-quantile assumption."""
    return (_range_based_var(high, low, close, YDAYS, 0.95)).diff().diff().diff()

def f53_atds_052_range_based_var_99_log_ret_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Range-based VaR(99) over 252d."""
    return (_range_based_var(high, low, close, YDAYS, 0.99)).diff().diff().diff()

def f53_atds_053_atr_based_var_95_log_ret_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-based VaR(95) over 252d = ATR21/close * |z_q|."""
    return (_atr_based_var(high, low, close, YDAYS, 0.95)).diff().diff().diff()

def f53_atds_054_atr_based_var_99_log_ret_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-based VaR(99) over 252d."""
    return (_atr_based_var(high, low, close, YDAYS, 0.99)).diff().diff().diff()

def f53_atds_055_garman_klass_var_95_log_ret_252d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Garman-Klass-vol-based VaR(95) over 252d."""
    ln_hl = (_safe_log(high) - _safe_log(low)) ** 2
    rs = 0.5 * ln_hl - (2.0 * np.log(2.0) - 1.0) * (_safe_log(close) - _safe_log(open)) ** 2
    gk_var = rs.rolling(MDAYS, min_periods=10).mean()
    sd = gk_var.clip(lower=0).pow(0.5)
    z = _norm_ppf(0.05)
    return (-(sd * z).rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff().diff()

def f53_atds_056_yang_zhang_var_95_log_ret_252d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Yang-Zhang-vol-based VaR(95) over 252d."""
    log_o = _safe_log(open); log_c = _safe_log(close); log_h = _safe_log(high); log_l = _safe_log(low)
    log_cp = log_c.shift(1)
    overnight = (log_o - log_cp) ** 2; open_close = (log_c - log_o) ** 2
    rs = (log_h - log_c) * (log_h - log_o) + (log_l - log_c) * (log_l - log_o)
    on_var = overnight.rolling(MDAYS, min_periods=10).var()
    oc_var = open_close.rolling(MDAYS, min_periods=10).var()
    rs_avg = rs.rolling(MDAYS, min_periods=10).mean()
    k = 0.34 / (1.34 + (MDAYS + 1.0) / (MDAYS - 1.0))
    yz = on_var + k * oc_var + (1.0 - k) * rs_avg
    sd = yz.clip(lower=0).pow(0.5)
    z = _norm_ppf(0.05)
    return (-(sd * z).rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff().diff()

def f53_atds_057_range_var_to_close_var_ratio_95_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Range-based VaR(95) / historical VaR(95) over 252d."""
    r = _log_ret(close)
    rv = _range_based_var(high, low, close, YDAYS, 0.95)
    hv = -_rolling_q(r, YDAYS, 0.05)
    return (_safe_div(rv, hv)).diff().diff().diff()

def f53_atds_058_atr_var_to_close_var_ratio_95_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-based VaR(95) / historical VaR(95) over 252d."""
    r = _log_ret(close)
    av = _atr_based_var(high, low, close, YDAYS, 0.95)
    hv = -_rolling_q(r, YDAYS, 0.05)
    return (_safe_div(av, hv)).diff().diff().diff()

def f53_atds_059_range_minus_close_var_95_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Range-based VaR(95) minus historical VaR(95) over 252d."""
    r = _log_ret(close)
    rv = _range_based_var(high, low, close, YDAYS, 0.95)
    hv = -_rolling_q(r, YDAYS, 0.05)
    return (rv - hv).diff().diff().diff()

def f53_atds_060_efficiency_range_var_intraday_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(Range-based VaR - close-close VaR) / close-close VaR over 252d - intraday-extra-risk share."""
    r = _log_ret(close)
    rv = _range_based_var(high, low, close, YDAYS, 0.95)
    hv = -_rolling_q(r, YDAYS, 0.05)
    return (_safe_div(rv - hv, hv)).diff().diff().diff()

def f53_atds_061_var99_to_var95_ratio_252d_d3(close: pd.Series) -> pd.Series:
    """Historical VaR(99) / VaR(95) over 252d - tail steepness."""
    r = _log_ret(close)
    v99 = -_rolling_q(r, YDAYS, 0.01)
    v95 = -_rolling_q(r, YDAYS, 0.05)
    return (_safe_div(v99, v95)).diff().diff().diff()

def f53_atds_062_var995_to_var99_ratio_252d_d3(close: pd.Series) -> pd.Series:
    """VaR(99.5) / VaR(99) over 252d."""
    r = _log_ret(close)
    v995 = -_rolling_q(r, YDAYS, 0.005)
    v99 = -_rolling_q(r, YDAYS, 0.01)
    return (_safe_div(v995, v99)).diff().diff().diff()

def f53_atds_063_es99_to_es95_ratio_252d_d3(close: pd.Series) -> pd.Series:
    """ES(99) / ES(95) over 252d."""
    r = _log_ret(close)
    def _es(w, q):
        x = w[~np.isnan(w)]
        if x.size < 30:
            return np.nan
        thr = np.quantile(x, 1.0 - q)
        tail = x[x <= thr]
        return float(-tail.mean()) if tail.size > 0 else np.nan
    es99 = r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _es(w, 0.99), raw=True)
    es95 = r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _es(w, 0.95), raw=True)
    return (_safe_div(es99, es95)).diff().diff().diff()

def f53_atds_064_risk_curve_steepness_var_p1_to_p10_252d_d3(close: pd.Series) -> pd.Series:
    """(VaR(99) - VaR(95)) / (VaR(95) - VaR(90)) over 252d - convexity of VaR-curve."""
    r = _log_ret(close)
    v99 = -_rolling_q(r, YDAYS, 0.01)
    v95 = -_rolling_q(r, YDAYS, 0.05)
    v90 = -_rolling_q(r, YDAYS, 0.10)
    return (_safe_div(v99 - v95, v95 - v90)).diff().diff().diff()

def f53_atds_065_var_curve_convexity_252d_d3(close: pd.Series) -> pd.Series:
    """VaR(99) - 2*VaR(95) + VaR(90) over 252d - signed curvature of VaR profile."""
    r = _log_ret(close)
    v99 = -_rolling_q(r, YDAYS, 0.01)
    v95 = -_rolling_q(r, YDAYS, 0.05)
    v90 = -_rolling_q(r, YDAYS, 0.10)
    return (v99 - 2.0 * v95 + v90).diff().diff().diff()

def f53_atds_066_es_minus_var_at_95_normalized_252d_d3(close: pd.Series) -> pd.Series:
    """(ES(95) - VaR(95)) / VaR(95) over 252d - conditional excess severity."""
    r = _log_ret(close)
    def _es(w):
        x = w[~np.isnan(w)]
        if x.size < 30:
            return np.nan
        thr = np.quantile(x, 0.05)
        tail = x[x <= thr]
        return float(-tail.mean()) if tail.size > 0 else np.nan
    es = r.rolling(YDAYS, min_periods=QDAYS).apply(_es, raw=True)
    v = -_rolling_q(r, YDAYS, 0.05)
    return (_safe_div(es - v, v)).diff().diff().diff()

def f53_atds_067_var_term_struct_slope_21_63_252d_d3(close: pd.Series) -> pd.Series:
    """VaR(95) at 21d vs at 63d window: log(v95_21 / v95_63) over 252d."""
    r = _log_ret(close)
    v21 = -_rolling_q(r, MDAYS, 0.05)
    v63 = -_rolling_q(r, QDAYS, 0.05)
    return (_safe_log(v21) - _safe_log(v63)).diff().diff().diff()

def f53_atds_068_var_term_struct_convexity_21_63_252d_d3(close: pd.Series) -> pd.Series:
    """VaR(95) at 21d - 2*at 63d + at 252d over 252d."""
    r = _log_ret(close)
    v21 = -_rolling_q(r, MDAYS, 0.05)
    v63 = -_rolling_q(r, QDAYS, 0.05)
    v252 = -_rolling_q(r, YDAYS, 0.05)
    return (v21 - 2.0 * v63 + v252).diff().diff().diff()

def f53_atds_069_tail_loss_concentration_index_252d_d3(close: pd.Series) -> pd.Series:
    """(sum of bottom-5% returns) / (sum of all negative returns) over 252d."""
    r = _log_ret(close)
    def _tc(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        neg = v[v < 0]
        if neg.size == 0 or neg.sum() == 0:
            return np.nan
        k = max(int(0.05 * v.size), 1)
        bot = np.sort(v)[:k]
        return float(bot.sum() / neg.sum())
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_tc, raw=True)
    return (res).diff().diff().diff()

def f53_atds_070_worst_5pct_loss_sum_to_total_var_252d_d3(close: pd.Series) -> pd.Series:
    """Sum of worst 5% losses / 252d realized variance - tail-loss density."""
    r = _log_ret(close)
    def _ts(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        k = max(int(0.05 * v.size), 1)
        bot = np.sort(v)[:k]
        return float(-bot.sum())
    ts = r.rolling(YDAYS, min_periods=QDAYS).apply(_ts, raw=True)
    var_r = (r ** 2).rolling(YDAYS, min_periods=QDAYS).sum()
    return (_safe_div(ts, var_r)).diff().diff().diff()

def f53_atds_071_block_bootstrap_var_95_block5_252d_d3(close: pd.Series) -> pd.Series:
    """Block bootstrap VaR(95) with block size 5 over 252d (single-resample proxy)."""
    r = _log_ret(close)
    def _bb(w):
        v = w[~np.isnan(w)]
        if v.size < 50:
            return np.nan
        block = 5; n_blocks = v.size // block
        rng = np.random.default_rng(42)
        idx = rng.integers(0, n_blocks, size=n_blocks)
        sample = np.concatenate([v[i * block:(i + 1) * block] for i in idx])
        return float(-np.quantile(sample, 0.05))
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_bb, raw=True)
    return (res).diff().diff().diff()

def f53_atds_072_block_bootstrap_var_99_block5_252d_d3(close: pd.Series) -> pd.Series:
    """Block bootstrap VaR(99) block=5 over 252d."""
    r = _log_ret(close)
    def _bb(w):
        v = w[~np.isnan(w)]
        if v.size < 50:
            return np.nan
        block = 5; n_blocks = v.size // block
        rng = np.random.default_rng(42)
        idx = rng.integers(0, n_blocks, size=n_blocks)
        sample = np.concatenate([v[i * block:(i + 1) * block] for i in idx])
        return float(-np.quantile(sample, 0.01))
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_bb, raw=True)
    return (res).diff().diff().diff()

def f53_atds_073_block_bootstrap_var_95_block21_252d_d3(close: pd.Series) -> pd.Series:
    """Block bootstrap VaR(95) block=21 over 252d."""
    r = _log_ret(close)
    def _bb(w):
        v = w[~np.isnan(w)]
        if v.size < 60:
            return np.nan
        block = MDAYS; n_blocks = v.size // block
        if n_blocks < 2:
            return np.nan
        rng = np.random.default_rng(42)
        idx = rng.integers(0, n_blocks, size=n_blocks)
        sample = np.concatenate([v[i * block:(i + 1) * block] for i in idx])
        return float(-np.quantile(sample, 0.05))
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_bb, raw=True)
    return (res).diff().diff().diff()

def f53_atds_074_block_bootstrap_var_uncertainty_block5_252d_d3(close: pd.Series) -> pd.Series:
    """Std of 10 block-bootstrap VaR(95) estimates with block=5 over 252d."""
    r = _log_ret(close)
    def _bb(w):
        v = w[~np.isnan(w)]
        if v.size < 60:
            return np.nan
        block = 5; n_blocks = v.size // block
        if n_blocks < 2:
            return np.nan
        rng = np.random.default_rng(42)
        vals = []
        for _ in range(10):
            idx = rng.integers(0, n_blocks, size=n_blocks)
            sample = np.concatenate([v[i * block:(i + 1) * block] for i in idx])
            vals.append(-np.quantile(sample, 0.05))
        return float(np.std(vals, ddof=1))
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_bb, raw=True)
    return (res).diff().diff().diff()

def f53_atds_075_moving_block_var_95_block21_252d_d3(close: pd.Series) -> pd.Series:
    """Moving-block bootstrap (10 blocks of size 21, single resample) VaR(95) over 252d."""
    r = _log_ret(close)
    def _mb(w):
        v = w[~np.isnan(w)]
        if v.size < 60:
            return np.nan
        block = MDAYS
        rng = np.random.default_rng(42)
        starts = rng.integers(0, max(v.size - block + 1, 1), size=10)
        sample = np.concatenate([v[s:s + block] for s in starts])
        return float(-np.quantile(sample, 0.05))
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_mb, raw=True)
    return (res).diff().diff().diff()


# ============================================================
#                         REGISTRY 001_075 (d3)
# ============================================================

ADVANCED_TAIL_DRAWDOWN_STRUCTURE_D3_REGISTRY_001_075 = {
    "f53_atds_001_drawdown_count_252d_d3": {"inputs": ["close"], "func": f53_atds_001_drawdown_count_252d_d3},
    "f53_atds_002_drawdown_count_504d_d3": {"inputs": ["close"], "func": f53_atds_002_drawdown_count_504d_d3},
    "f53_atds_003_drawdown_mean_depth_252d_d3": {"inputs": ["close"], "func": f53_atds_003_drawdown_mean_depth_252d_d3},
    "f53_atds_004_drawdown_median_depth_252d_d3": {"inputs": ["close"], "func": f53_atds_004_drawdown_median_depth_252d_d3},
    "f53_atds_005_drawdown_p95_depth_252d_d3": {"inputs": ["close"], "func": f53_atds_005_drawdown_p95_depth_252d_d3},
    "f53_atds_006_drawdown_depth_skew_252d_d3": {"inputs": ["close"], "func": f53_atds_006_drawdown_depth_skew_252d_d3},
    "f53_atds_007_drawdown_depth_kurt_252d_d3": {"inputs": ["close"], "func": f53_atds_007_drawdown_depth_kurt_252d_d3},
    "f53_atds_008_drawdown_mean_duration_252d_d3": {"inputs": ["close"], "func": f53_atds_008_drawdown_mean_duration_252d_d3},
    "f53_atds_009_drawdown_median_duration_252d_d3": {"inputs": ["close"], "func": f53_atds_009_drawdown_median_duration_252d_d3},
    "f53_atds_010_drawdown_count_per_year_proxy_504d_d3": {"inputs": ["close"], "func": f53_atds_010_drawdown_count_per_year_proxy_504d_d3},
    "f53_atds_011_time_under_water_frac_252d_d3": {"inputs": ["close"], "func": f53_atds_011_time_under_water_frac_252d_d3},
    "f53_atds_012_time_under_water_frac_504d_d3": {"inputs": ["close"], "func": f53_atds_012_time_under_water_frac_504d_d3},
    "f53_atds_013_time_under_water_frac_1260d_d3": {"inputs": ["close"], "func": f53_atds_013_time_under_water_frac_1260d_d3},
    "f53_atds_014_max_time_under_water_252d_d3": {"inputs": ["close"], "func": f53_atds_014_max_time_under_water_252d_d3},
    "f53_atds_015_max_time_under_water_504d_d3": {"inputs": ["close"], "func": f53_atds_015_max_time_under_water_504d_d3},
    "f53_atds_016_drawdown_duration_max_252d_d3": {"inputs": ["close"], "func": f53_atds_016_drawdown_duration_max_252d_d3},
    "f53_atds_017_drawdown_duration_p95_252d_d3": {"inputs": ["close"], "func": f53_atds_017_drawdown_duration_p95_252d_d3},
    "f53_atds_018_drawdown_duration_skew_252d_d3": {"inputs": ["close"], "func": f53_atds_018_drawdown_duration_skew_252d_d3},
    "f53_atds_019_recovery_attempts_count_252d_d3": {"inputs": ["close"], "func": f53_atds_019_recovery_attempts_count_252d_d3},
    "f53_atds_020_recovery_efficiency_index_252d_d3": {"inputs": ["close"], "func": f53_atds_020_recovery_efficiency_index_252d_d3},
    "f53_atds_021_acerbi_szekely_z1_es95_252d_d3": {"inputs": ["close"], "func": f53_atds_021_acerbi_szekely_z1_es95_252d_d3},
    "f53_atds_022_acerbi_szekely_z2_es95_252d_d3": {"inputs": ["close"], "func": f53_atds_022_acerbi_szekely_z2_es95_252d_d3},
    "f53_atds_023_acerbi_szekely_z1_es99_252d_d3": {"inputs": ["close"], "func": f53_atds_023_acerbi_szekely_z1_es99_252d_d3},
    "f53_atds_024_acerbi_szekely_z2_es99_252d_d3": {"inputs": ["close"], "func": f53_atds_024_acerbi_szekely_z2_es99_252d_d3},
    "f53_atds_025_es_breach_count_95_in_504d_d3": {"inputs": ["close"], "func": f53_atds_025_es_breach_count_95_in_504d_d3},
    "f53_atds_026_es_breach_rate_minus_5pct_504d_d3": {"inputs": ["close"], "func": f53_atds_026_es_breach_rate_minus_5pct_504d_d3},
    "f53_atds_027_es_conditional_severity_score_252d_d3": {"inputs": ["close"], "func": f53_atds_027_es_conditional_severity_score_252d_d3},
    "f53_atds_028_es_pearson_consistency_252d_d3": {"inputs": ["close"], "func": f53_atds_028_es_pearson_consistency_252d_d3},
    "f53_atds_029_max_loss_div_es_95_252d_d3": {"inputs": ["close"], "func": f53_atds_029_max_loss_div_es_95_252d_d3},
    "f53_atds_030_es_backtest_failure_rate_zscore_95_252d_d3": {"inputs": ["close"], "func": f53_atds_030_es_backtest_failure_rate_zscore_95_252d_d3},
    "f53_atds_031_kupiec_pof_lr_var95_252d_d3": {"inputs": ["close"], "func": f53_atds_031_kupiec_pof_lr_var95_252d_d3},
    "f53_atds_032_kupiec_pof_lr_var99_252d_d3": {"inputs": ["close"], "func": f53_atds_032_kupiec_pof_lr_var99_252d_d3},
    "f53_atds_033_kupiec_pof_lr_var95_504d_d3": {"inputs": ["close"], "func": f53_atds_033_kupiec_pof_lr_var95_504d_d3},
    "f53_atds_034_christoffersen_independence_lr_var95_252d_d3": {"inputs": ["close"], "func": f53_atds_034_christoffersen_independence_lr_var95_252d_d3},
    "f53_atds_035_christoffersen_independence_lr_var99_252d_d3": {"inputs": ["close"], "func": f53_atds_035_christoffersen_independence_lr_var99_252d_d3},
    "f53_atds_036_christoffersen_joint_lr_var95_252d_d3": {"inputs": ["close"], "func": f53_atds_036_christoffersen_joint_lr_var95_252d_d3},
    "f53_atds_037_christoffersen_joint_lr_var99_252d_d3": {"inputs": ["close"], "func": f53_atds_037_christoffersen_joint_lr_var99_252d_d3},
    "f53_atds_038_dq_test_stat_proxy_var95_252d_d3": {"inputs": ["close"], "func": f53_atds_038_dq_test_stat_proxy_var95_252d_d3},
    "f53_atds_039_breach_first_order_autocorr_var95_252d_d3": {"inputs": ["close"], "func": f53_atds_039_breach_first_order_autocorr_var95_252d_d3},
    "f53_atds_040_breach_clustering_pair_count_var99_252d_d3": {"inputs": ["close"], "func": f53_atds_040_breach_clustering_pair_count_var99_252d_d3},
    "f53_atds_041_caviar_sav_b2_persistence_q95_252d_d3": {"inputs": ["close"], "func": f53_atds_041_caviar_sav_b2_persistence_q95_252d_d3},
    "f53_atds_042_caviar_sav_b3_shock_q95_252d_d3": {"inputs": ["close"], "func": f53_atds_042_caviar_sav_b3_shock_q95_252d_d3},
    "f53_atds_043_caviar_sav_current_var_q95_252d_d3": {"inputs": ["close"], "func": f53_atds_043_caviar_sav_current_var_q95_252d_d3},
    "f53_atds_044_caviar_sav_quantile_loss_q95_252d_d3": {"inputs": ["close"], "func": f53_atds_044_caviar_sav_quantile_loss_q95_252d_d3},
    "f53_atds_045_caviar_sav_b2_persistence_q99_252d_d3": {"inputs": ["close"], "func": f53_atds_045_caviar_sav_b2_persistence_q99_252d_d3},
    "f53_atds_046_caviar_asym_slope_b3pos_q95_252d_d3": {"inputs": ["close"], "func": f53_atds_046_caviar_asym_slope_b3pos_q95_252d_d3},
    "f53_atds_047_caviar_asym_slope_b3neg_q95_252d_d3": {"inputs": ["close"], "func": f53_atds_047_caviar_asym_slope_b3neg_q95_252d_d3},
    "f53_atds_048_caviar_asym_slope_neg_minus_pos_q95_252d_d3": {"inputs": ["close"], "func": f53_atds_048_caviar_asym_slope_neg_minus_pos_q95_252d_d3},
    "f53_atds_049_caviar_asym_current_var_q95_252d_d3": {"inputs": ["close"], "func": f53_atds_049_caviar_asym_current_var_q95_252d_d3},
    "f53_atds_050_caviar_sav_minus_hist_var_q95_252d_d3": {"inputs": ["close"], "func": f53_atds_050_caviar_sav_minus_hist_var_q95_252d_d3},
    "f53_atds_051_range_based_var_95_log_ret_252d_d3": {"inputs": ["high", "low", "close"], "func": f53_atds_051_range_based_var_95_log_ret_252d_d3},
    "f53_atds_052_range_based_var_99_log_ret_252d_d3": {"inputs": ["high", "low", "close"], "func": f53_atds_052_range_based_var_99_log_ret_252d_d3},
    "f53_atds_053_atr_based_var_95_log_ret_252d_d3": {"inputs": ["high", "low", "close"], "func": f53_atds_053_atr_based_var_95_log_ret_252d_d3},
    "f53_atds_054_atr_based_var_99_log_ret_252d_d3": {"inputs": ["high", "low", "close"], "func": f53_atds_054_atr_based_var_99_log_ret_252d_d3},
    "f53_atds_055_garman_klass_var_95_log_ret_252d_d3": {"inputs": ["open", "high", "low", "close"], "func": f53_atds_055_garman_klass_var_95_log_ret_252d_d3},
    "f53_atds_056_yang_zhang_var_95_log_ret_252d_d3": {"inputs": ["open", "high", "low", "close"], "func": f53_atds_056_yang_zhang_var_95_log_ret_252d_d3},
    "f53_atds_057_range_var_to_close_var_ratio_95_252d_d3": {"inputs": ["high", "low", "close"], "func": f53_atds_057_range_var_to_close_var_ratio_95_252d_d3},
    "f53_atds_058_atr_var_to_close_var_ratio_95_252d_d3": {"inputs": ["high", "low", "close"], "func": f53_atds_058_atr_var_to_close_var_ratio_95_252d_d3},
    "f53_atds_059_range_minus_close_var_95_252d_d3": {"inputs": ["high", "low", "close"], "func": f53_atds_059_range_minus_close_var_95_252d_d3},
    "f53_atds_060_efficiency_range_var_intraday_252d_d3": {"inputs": ["high", "low", "close"], "func": f53_atds_060_efficiency_range_var_intraday_252d_d3},
    "f53_atds_061_var99_to_var95_ratio_252d_d3": {"inputs": ["close"], "func": f53_atds_061_var99_to_var95_ratio_252d_d3},
    "f53_atds_062_var995_to_var99_ratio_252d_d3": {"inputs": ["close"], "func": f53_atds_062_var995_to_var99_ratio_252d_d3},
    "f53_atds_063_es99_to_es95_ratio_252d_d3": {"inputs": ["close"], "func": f53_atds_063_es99_to_es95_ratio_252d_d3},
    "f53_atds_064_risk_curve_steepness_var_p1_to_p10_252d_d3": {"inputs": ["close"], "func": f53_atds_064_risk_curve_steepness_var_p1_to_p10_252d_d3},
    "f53_atds_065_var_curve_convexity_252d_d3": {"inputs": ["close"], "func": f53_atds_065_var_curve_convexity_252d_d3},
    "f53_atds_066_es_minus_var_at_95_normalized_252d_d3": {"inputs": ["close"], "func": f53_atds_066_es_minus_var_at_95_normalized_252d_d3},
    "f53_atds_067_var_term_struct_slope_21_63_252d_d3": {"inputs": ["close"], "func": f53_atds_067_var_term_struct_slope_21_63_252d_d3},
    "f53_atds_068_var_term_struct_convexity_21_63_252d_d3": {"inputs": ["close"], "func": f53_atds_068_var_term_struct_convexity_21_63_252d_d3},
    "f53_atds_069_tail_loss_concentration_index_252d_d3": {"inputs": ["close"], "func": f53_atds_069_tail_loss_concentration_index_252d_d3},
    "f53_atds_070_worst_5pct_loss_sum_to_total_var_252d_d3": {"inputs": ["close"], "func": f53_atds_070_worst_5pct_loss_sum_to_total_var_252d_d3},
    "f53_atds_071_block_bootstrap_var_95_block5_252d_d3": {"inputs": ["close"], "func": f53_atds_071_block_bootstrap_var_95_block5_252d_d3},
    "f53_atds_072_block_bootstrap_var_99_block5_252d_d3": {"inputs": ["close"], "func": f53_atds_072_block_bootstrap_var_99_block5_252d_d3},
    "f53_atds_073_block_bootstrap_var_95_block21_252d_d3": {"inputs": ["close"], "func": f53_atds_073_block_bootstrap_var_95_block21_252d_d3},
    "f53_atds_074_block_bootstrap_var_uncertainty_block5_252d_d3": {"inputs": ["close"], "func": f53_atds_074_block_bootstrap_var_uncertainty_block5_252d_d3},
    "f53_atds_075_moving_block_var_95_block21_252d_d3": {"inputs": ["close"], "func": f53_atds_075_moving_block_var_95_block21_252d_d3},
}
