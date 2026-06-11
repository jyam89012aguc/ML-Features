"""advanced_tail_drawdown_structure d2 features 076-150 - Pipeline 1b-technical.

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


def f53_atds_076_circular_block_var_95_block5_252d_d2(close: pd.Series) -> pd.Series:
    """Circular-block bootstrap VaR(95) block=5 over 252d."""
    r = _log_ret(close)
    def _cb(w):
        v = w[~np.isnan(w)]
        if v.size < 60:
            return np.nan
        block = 5
        rng = np.random.default_rng(42)
        starts = rng.integers(0, v.size, size=10)
        sample = np.concatenate([np.take(v, np.arange(s, s + block), mode='wrap') for s in starts])
        return float(-np.quantile(sample, 0.05))
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_cb, raw=True)
    return (res).diff().diff()

def f53_atds_077_stationary_bootstrap_var_95_p_005_252d_d2(close: pd.Series) -> pd.Series:
    """Stationary bootstrap VaR(95) with geometric-block mean=20 over 252d."""
    r = _log_ret(close)
    def _sb(w):
        v = w[~np.isnan(w)]
        if v.size < 60:
            return np.nan
        rng = np.random.default_rng(42)
        p = 1.0 / 20.0
        out_sample = []
        while len(out_sample) < v.size:
            start = rng.integers(0, v.size)
            length = rng.geometric(p)
            for k in range(length):
                out_sample.append(v[(start + k) % v.size])
                if len(out_sample) >= v.size:
                    break
        return float(-np.quantile(np.array(out_sample), 0.05))
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_sb, raw=True)
    return (res).diff().diff()

def f53_atds_078_block_bootstrap_es_95_block5_252d_d2(close: pd.Series) -> pd.Series:
    """Block bootstrap ES(95) block=5 over 252d."""
    r = _log_ret(close)
    def _bb(w):
        v = w[~np.isnan(w)]
        if v.size < 60:
            return np.nan
        block = 5; n_blocks = v.size // block
        if n_blocks < 2:
            return np.nan
        rng = np.random.default_rng(42)
        idx = rng.integers(0, n_blocks, size=n_blocks)
        sample = np.concatenate([v[i * block:(i + 1) * block] for i in idx])
        thr = np.quantile(sample, 0.05)
        tail = sample[sample <= thr]
        return float(-tail.mean()) if tail.size > 0 else np.nan
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_bb, raw=True)
    return (res).diff().diff()

def f53_atds_079_block_bootstrap_var_uncertainty_es_252d_d2(close: pd.Series) -> pd.Series:
    """Std of 10 block-bootstrap ES(95) estimates over 252d."""
    r = _log_ret(close)
    def _be(w):
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
            thr = np.quantile(sample, 0.05)
            tail = sample[sample <= thr]
            if tail.size > 0:
                vals.append(-tail.mean())
        if len(vals) < 2:
            return np.nan
        return float(np.std(vals, ddof=1))
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_be, raw=True)
    return (res).diff().diff()

def f53_atds_080_bootstrap_var_minus_hist_var_95_252d_d2(close: pd.Series) -> pd.Series:
    """Block-bootstrap VaR(95) minus historical VaR(95) over 252d."""
    r = _log_ret(close)
    def _bb(w):
        v = w[~np.isnan(w)]
        if v.size < 60:
            return np.nan
        block = 5; n_blocks = v.size // block
        if n_blocks < 2:
            return np.nan
        rng = np.random.default_rng(42)
        idx = rng.integers(0, n_blocks, size=n_blocks)
        sample = np.concatenate([v[i * block:(i + 1) * block] for i in idx])
        return float(-np.quantile(sample, 0.05))
    bs = r.rolling(YDAYS, min_periods=QDAYS).apply(_bb, raw=True)
    hv = -_rolling_q(r, YDAYS, 0.05)
    return (bs - hv).diff().diff()

def f53_atds_081_ulcer_index_504d_d2(close: pd.Series) -> pd.Series:
    """Ulcer index (RMS drawdown) over 504d."""
    lc = _safe_log(close)
    def _u(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        cm = np.maximum.accumulate(v)
        dd = v - cm
        return float(np.sqrt(np.mean(dd ** 2)))
    res = lc.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_u, raw=True)
    return (res).diff().diff()

def f53_atds_082_ulcer_index_1260d_d2(close: pd.Series) -> pd.Series:
    """Ulcer index over 1260d (5y)."""
    lc = _safe_log(close)
    def _u(w):
        v = w[~np.isnan(w)]
        if v.size < 60:
            return np.nan
        cm = np.maximum.accumulate(v)
        dd = v - cm
        return float(np.sqrt(np.mean(dd ** 2)))
    res = lc.rolling(DDAYS_5Y, min_periods=DDAYS_2Y).apply(_u, raw=True)
    return (res).diff().diff()

def f53_atds_083_ulcer_index_change_speed_21d_252d_d2(close: pd.Series) -> pd.Series:
    """21-bar diff of 252d Ulcer index."""
    lc = _safe_log(close)
    def _u(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        cm = np.maximum.accumulate(v)
        dd = v - cm
        return float(np.sqrt(np.mean(dd ** 2)))
    ulc = lc.rolling(YDAYS, min_periods=QDAYS).apply(_u, raw=True)
    return (ulc - ulc.shift(MDAYS)).diff().diff()

def f53_atds_084_lake_ratio_252d_d2(close: pd.Series) -> pd.Series:
    """Lake ratio = area under drawdown curve / area under cumulative-equity curve over 252d."""
    lc = _safe_log(close)
    def _lk(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        cm = np.maximum.accumulate(v)
        dd = -(v - cm)
        eq = v - v[0]
        eq_area = np.maximum(eq.sum(), 1e-12)
        return float(dd.sum() / eq_area)
    res = lc.rolling(YDAYS, min_periods=QDAYS).apply(_lk, raw=True)
    return (res).diff().diff()

def f53_atds_085_mean_squared_drawdown_252d_d2(close: pd.Series) -> pd.Series:
    """Mean of squared drawdown depths over 252d."""
    lc = _safe_log(close)
    def _msd(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        cm = np.maximum.accumulate(v)
        return float(np.mean((v - cm) ** 2))
    res = lc.rolling(YDAYS, min_periods=QDAYS).apply(_msd, raw=True)
    return (res).diff().diff()

def f53_atds_086_max_drawdown_decay_rate_504d_d2(close: pd.Series) -> pd.Series:
    """Decay rate of max drawdown: (max_dd_504d - max_dd_252d) / 252 over 504d."""
    mdd_504 = -_rolling_max_drawdown(close, DDAYS_2Y)
    mdd_252 = -_rolling_max_drawdown(close, YDAYS)
    return ((mdd_504 - mdd_252) / float(YDAYS)).diff().diff()

def f53_atds_087_pain_index_504d_d2(close: pd.Series) -> pd.Series:
    """Mean drawdown magnitude (Pain Index) over 504d."""
    lc = _safe_log(close)
    def _pi(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        cm = np.maximum.accumulate(v)
        return float((-(v - cm)).mean())
    res = lc.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_pi, raw=True)
    return (res).diff().diff()

def f53_atds_088_pain_index_acceleration_21d_252d_d2(close: pd.Series) -> pd.Series:
    """21-bar diff of 252d Pain Index."""
    lc = _safe_log(close)
    def _pi(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        cm = np.maximum.accumulate(v)
        return float((-(v - cm)).mean())
    pi = lc.rolling(YDAYS, min_periods=QDAYS).apply(_pi, raw=True)
    return (pi - pi.shift(MDAYS)).diff().diff()

def f53_atds_089_ulcer_minus_pain_252d_d2(close: pd.Series) -> pd.Series:
    """Ulcer index minus Pain index over 252d - RMS vs L1 gap (= 0 only for uniform DD)."""
    lc = _safe_log(close)
    def _u(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        cm = np.maximum.accumulate(v)
        return float(np.sqrt(np.mean((v - cm) ** 2)))
    def _pi(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        cm = np.maximum.accumulate(v)
        return float((-(v - cm)).mean())
    ulc = lc.rolling(YDAYS, min_periods=QDAYS).apply(_u, raw=True)
    pn = lc.rolling(YDAYS, min_periods=QDAYS).apply(_pi, raw=True)
    return (ulc - pn).diff().diff()

def f53_atds_090_drawdown_severity_index_depth_times_duration_252d_d2(close: pd.Series) -> pd.Series:
    """Mean of (depth * duration) across drawdowns in 252d."""
    mp = max(YDAYS // 3, 30)
    episodes_list = _drawdown_episodes(close)
    nb = len(close)
    out = np.full(nb, np.nan, dtype=float)
    for i in range(nb):
        if i < mp - 1:
            continue
        lo = max(0, i - YDAYS + 1)
        vals = [e[3] * e[4] for e in episodes_list if lo <= e[1] <= i]
        if len(vals) >= 2:
            out[i] = float(np.mean(vals))
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()

def f53_atds_091_consecutive_neg_returns_max_252d_d2(close: pd.Series) -> pd.Series:
    """Longest streak of consecutive negative log-returns in last 252d."""
    r = _log_ret(close)
    return (_consecutive_neg_max(r, YDAYS)).diff().diff()

def f53_atds_092_consecutive_neg_returns_max_504d_d2(close: pd.Series) -> pd.Series:
    """Longest run of consecutive negative log-returns in last 504d."""
    r = _log_ret(close)
    return (_consecutive_neg_max(r, DDAYS_2Y)).diff().diff()

def f53_atds_093_consecutive_loss_streak_count_above_3_252d_d2(close: pd.Series) -> pd.Series:
    """Count of distinct streaks of >=3 consecutive negative returns in last 252d."""
    r = _log_ret(close)
    neg = (r < 0).astype(float).where(r.notna(), np.nan)
    def _cs(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        cnt = 0; run = 0
        for x in v:
            if x > 0.5:
                run += 1
                if run == 3:
                    cnt += 1
            else:
                run = 0
        return float(cnt)
    res = neg.rolling(YDAYS, min_periods=QDAYS).apply(_cs, raw=True)
    return (res).diff().diff()

def f53_atds_094_consecutive_loss_streak_p95_length_252d_d2(close: pd.Series) -> pd.Series:
    """95th percentile of length of distinct negative-return streaks in last 252d."""
    r = _log_ret(close)
    neg = (r < 0).astype(float).where(r.notna(), np.nan)
    def _p95(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        runs = []; run = 0
        for x in v:
            if x > 0.5:
                run += 1
            else:
                if run > 0:
                    runs.append(run); run = 0
        if run > 0:
            runs.append(run)
        if len(runs) < 3:
            return np.nan
        return float(np.quantile(runs, 0.95))
    res = neg.rolling(YDAYS, min_periods=QDAYS).apply(_p95, raw=True)
    return (res).diff().diff()

def f53_atds_095_consecutive_loss_severity_mean_252d_d2(close: pd.Series) -> pd.Series:
    """Mean cumulative loss magnitude across negative-return streaks in last 252d."""
    r = _log_ret(close)
    def _sv(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        sevs = []; cur = 0.0; in_run = False
        for x in v:
            if x < 0:
                cur += x; in_run = True
            else:
                if in_run:
                    sevs.append(-cur); cur = 0.0; in_run = False
        if in_run:
            sevs.append(-cur)
        if len(sevs) < 3:
            return np.nan
        return float(np.mean(sevs))
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_sv, raw=True)
    return (res).diff().diff()

def f53_atds_096_hot_hand_index_neg_252d_d2(close: pd.Series) -> pd.Series:
    """P(r_t < 0 | r_{t-1} < 0) - P(r_t < 0) over 252d - downside persistence excess."""
    r = _log_ret(close)
    neg = (r < 0).astype(float).where(r.notna(), np.nan)
    lag_neg = neg.shift(1)
    p_given = neg.where(lag_neg > 0.5, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    p_uncond = neg.rolling(YDAYS, min_periods=QDAYS).mean()
    return (p_given - p_uncond).diff().diff()

def f53_atds_097_hot_hand_index_pos_252d_d2(close: pd.Series) -> pd.Series:
    """P(r_t > 0 | r_{t-1} > 0) - P(r_t > 0) over 252d."""
    r = _log_ret(close)
    pos = (r > 0).astype(float).where(r.notna(), np.nan)
    lag_pos = pos.shift(1)
    p_given = pos.where(lag_pos > 0.5, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    p_uncond = pos.rolling(YDAYS, min_periods=QDAYS).mean()
    return (p_given - p_uncond).diff().diff()

def f53_atds_098_cold_streak_recovery_time_252d_d2(close: pd.Series) -> pd.Series:
    """Mean number of bars to recover above prior-bar value after a streak of >=3 neg returns over 252d."""
    r = _log_ret(close)
    lc = _safe_log(close)
    def _rt(w):
        v = w[~np.isnan(w)]
        if v.size < 60:
            return np.nan
        diffs = np.diff(v)
        neg = diffs < 0
        times = []; i = 0
        while i < neg.size - 3:
            if neg[i] and neg[i + 1] and neg[i + 2]:
                ref = v[i + 3] if i + 3 < v.size else None
                if ref is None:
                    break
                j = i + 3
                while j < v.size and v[j] < ref:
                    j += 1
                times.append(j - (i + 3))
                i = j
            else:
                i += 1
        if not times:
            return np.nan
        return float(np.mean(times))
    res = lc.rolling(YDAYS, min_periods=QDAYS).apply(_rt, raw=True)
    return (res).diff().diff()

def f53_atds_099_gambler_fallacy_proxy_neg_252d_d2(close: pd.Series) -> pd.Series:
    """P(r_t > 0 | r_{t-1} < 0) - P(r_t > 0) over 252d - reversal-after-down strength."""
    r = _log_ret(close)
    pos = (r > 0).astype(float).where(r.notna(), np.nan)
    neg = (r < 0).astype(float).where(r.notna(), np.nan)
    lag_neg = neg.shift(1)
    p_given = pos.where(lag_neg > 0.5, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    p_uncond = pos.rolling(YDAYS, min_periods=QDAYS).mean()
    return (p_given - p_uncond).diff().diff()

def f53_atds_100_gambler_fallacy_proxy_pos_252d_d2(close: pd.Series) -> pd.Series:
    """P(r_t < 0 | r_{t-1} > 0) - P(r_t < 0) over 252d."""
    r = _log_ret(close)
    pos = (r > 0).astype(float).where(r.notna(), np.nan)
    neg = (r < 0).astype(float).where(r.notna(), np.nan)
    lag_pos = pos.shift(1)
    p_given = neg.where(lag_pos > 0.5, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    p_uncond = neg.rolling(YDAYS, min_periods=QDAYS).mean()
    return (p_given - p_uncond).diff().diff()

def f53_atds_101_signed_es_95_negative_only_252d_d2(close: pd.Series) -> pd.Series:
    """Mean of returns in bottom 5% over 252d (ES on losses)."""
    r = _log_ret(close)
    def _es(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        thr = np.quantile(v, 0.05)
        tail = v[v <= thr]
        return float(tail.mean()) if tail.size > 0 else np.nan
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_es, raw=True)
    return (res).diff().diff()

def f53_atds_102_signed_es_95_positive_only_252d_d2(close: pd.Series) -> pd.Series:
    """Mean of returns in top 5% over 252d (signed positive)."""
    r = _log_ret(close)
    def _es(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        thr = np.quantile(v, 0.95)
        tail = v[v >= thr]
        return float(tail.mean()) if tail.size > 0 else np.nan
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_es, raw=True)
    return (res).diff().diff()

def f53_atds_103_signed_var_95_negative_only_252d_d2(close: pd.Series) -> pd.Series:
    """5th percentile of returns over 252d (signed; equals -VaR(95))."""
    r = _log_ret(close)
    return (_rolling_q(r, YDAYS, 0.05)).diff().diff()

def f53_atds_104_signed_var_95_positive_only_252d_d2(close: pd.Series) -> pd.Series:
    """95th percentile of returns over 252d."""
    r = _log_ret(close)
    return (_rolling_q(r, YDAYS, 0.95)).diff().diff()

def f53_atds_105_asymmetric_es_sum_signed_252d_d2(close: pd.Series) -> pd.Series:
    """Signed ES(95 lower) + signed ES(95 upper) over 252d - tail mass imbalance."""
    r = _log_ret(close)
    def _esl(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        thr = np.quantile(v, 0.05)
        tail = v[v <= thr]
        return float(tail.mean()) if tail.size > 0 else np.nan
    def _esu(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        thr = np.quantile(v, 0.95)
        tail = v[v >= thr]
        return float(tail.mean()) if tail.size > 0 else np.nan
    esl = r.rolling(YDAYS, min_periods=QDAYS).apply(_esl, raw=True)
    esu = r.rolling(YDAYS, min_periods=QDAYS).apply(_esu, raw=True)
    return (esl + esu).diff().diff()

def f53_atds_106_asymmetric_var_diff_signed_252d_d2(close: pd.Series) -> pd.Series:
    """(Signed VaR95+ + Signed VaR95-) / (VaR95+ - VaR95-) over 252d - normalized tail-skew via VaR."""
    r = _log_ret(close)
    vl = _rolling_q(r, YDAYS, 0.05)
    vu = _rolling_q(r, YDAYS, 0.95)
    return (_safe_div(vu + vl, vu - vl)).diff().diff()

def f53_atds_107_directional_tail_dominance_signed_252d_d2(close: pd.Series) -> pd.Series:
    """Sign of (|ES95-| - ES95+) over 252d - +1 = downside heavier, -1 = upside heavier."""
    r = _log_ret(close)
    def _esl(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        thr = np.quantile(v, 0.05)
        tail = v[v <= thr]
        return float(-tail.mean()) if tail.size > 0 else np.nan
    def _esu(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        thr = np.quantile(v, 0.95)
        tail = v[v >= thr]
        return float(tail.mean()) if tail.size > 0 else np.nan
    esl_mag = r.rolling(YDAYS, min_periods=QDAYS).apply(_esl, raw=True)
    esu = r.rolling(YDAYS, min_periods=QDAYS).apply(_esu, raw=True)
    return (np.sign(esl_mag - esu)).diff().diff()

def f53_atds_108_tail_skew_via_var_signed_252d_d2(close: pd.Series) -> pd.Series:
    """VaR95+ + VaR95- over 252d (sum of signed quantiles, =0 if symmetric)."""
    r = _log_ret(close)
    vl = _rolling_q(r, YDAYS, 0.05)
    vu = _rolling_q(r, YDAYS, 0.95)
    return (vu + vl).diff().diff()

def f53_atds_109_tail_skew_via_es_signed_252d_d2(close: pd.Series) -> pd.Series:
    """Same sum but with ES instead of VaR over 252d."""
    r = _log_ret(close)
    def _esl(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        thr = np.quantile(v, 0.05)
        tail = v[v <= thr]
        return float(tail.mean()) if tail.size > 0 else np.nan
    def _esu(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        thr = np.quantile(v, 0.95)
        tail = v[v >= thr]
        return float(tail.mean()) if tail.size > 0 else np.nan
    esl = r.rolling(YDAYS, min_periods=QDAYS).apply(_esl, raw=True)
    esu = r.rolling(YDAYS, min_periods=QDAYS).apply(_esu, raw=True)
    return (esu + esl).diff().diff()

def f53_atds_110_tail_balance_score_252d_d2(close: pd.Series) -> pd.Series:
    """(VaR95+ / |VaR95-|) - 1 over 252d - upside/downside tail balance."""
    r = _log_ret(close)
    vl = _rolling_q(r, YDAYS, 0.05)
    vu = _rolling_q(r, YDAYS, 0.95)
    return (_safe_div(vu, -vl) - 1.0).diff().diff()

def f53_atds_111_covid_proxy_stress_loss_count_5pct_252d_d2(close: pd.Series) -> pd.Series:
    """Count of bars in last 252d with single-day log-loss > 5%."""
    r = _log_ret(close)
    ev = (r < -0.05).astype(float).where(r.notna(), np.nan)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff()

def f53_atds_112_flash_crash_proxy_count_3pct_252d_d2(close: pd.Series) -> pd.Series:
    """Count of bars in last 252d with single-day log-loss > 3%."""
    r = _log_ret(close)
    ev = (r < -0.03).astype(float).where(r.notna(), np.nan)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff()

def f53_atds_113_lehman_proxy_stress_loss_week_10pct_252d_d2(close: pd.Series) -> pd.Series:
    """Count of bars where 5-day cum log-loss > 10% over last 252d."""
    r = _log_ret(close)
    rf = r.rolling(5, min_periods=3).sum()
    ev = (rf < -0.10).astype(float).where(rf.notna(), np.nan)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff()

def f53_atds_114_black_monday_proxy_20pct_one_day_252d_d2(close: pd.Series) -> pd.Series:
    """Count of single-day log-loss > 20% over last 252d (Black Monday-class)."""
    r = _log_ret(close)
    ev = (r < -0.20).astype(float).where(r.notna(), np.nan)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff()

def f53_atds_115_flash_move_count_above_2pct_either_direction_252d_d2(close: pd.Series) -> pd.Series:
    """Count of bars in last 252d where |r| > 2% (rapid-move events)."""
    r = _log_ret(close)
    ev = (r.abs() > 0.02).astype(float).where(r.notna(), np.nan)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff()

def f53_atds_116_macro_stress_event_count_5sigma_252d_d2(close: pd.Series) -> pd.Series:
    """Count of |r| > 5 * EWMA-vol_{t-1} events in last 252d."""
    r = _log_ret(close)
    sd = _safe_log(close).diff().abs().ewm(alpha=0.06, adjust=False, min_periods=20).mean().shift(1)
    ev = (r.abs() > 5.0 * sd).astype(float).where(sd.notna(), np.nan)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff()

def f53_atds_117_tail_event_clustering_5sigma_paired_252d_d2(close: pd.Series) -> pd.Series:
    """Count of consecutive-bar (5 sigma) tail events in last 252d."""
    r = _log_ret(close)
    sd = _safe_log(close).diff().abs().ewm(alpha=0.06, adjust=False, min_periods=20).mean().shift(1)
    ev = (r.abs() > 5.0 * sd).astype(float).where(sd.notna(), np.nan)
    pair = (ev * ev.shift(1)).fillna(0.0)
    return (pair.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff()

def f53_atds_118_stress_period_persistence_252d_d2(close: pd.Series) -> pd.Series:
    """Longest run of consecutive bars where loss < -3% in last 252d."""
    r = _log_ret(close)
    def _lr(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        cur = 0; best = 0
        for x in v:
            if x < -0.03:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return float(best)
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_lr, raw=True)
    return (res).diff().diff()

def f53_atds_119_expected_clustered_tail_event_rate_252d_d2(close: pd.Series) -> pd.Series:
    """Observed paired tail rate / Bernoulli expectation under independence over 252d."""
    r = _log_ret(close)
    sd = _safe_log(close).diff().abs().ewm(alpha=0.06, adjust=False, min_periods=20).mean().shift(1)
    ev = (r.abs() > 3.0 * sd).astype(float).where(sd.notna(), np.nan)
    p = ev.rolling(YDAYS, min_periods=QDAYS).mean()
    pair = (ev * ev.shift(1)).rolling(YDAYS, min_periods=QDAYS).mean()
    return (_safe_div(pair, p * p)).diff().diff()

def f53_atds_120_crisis_indicator_combined_252d_d2(close: pd.Series) -> pd.Series:
    """1.0 if (drawdown > 20% AND >5% loss event AND vol-z > 2) over 252d, else 0.0."""
    r = _log_ret(close)
    mdd = -_rolling_max_drawdown(close, YDAYS)
    loss_event = (r < -0.05).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    sd = _safe_log(close).diff().abs().ewm(alpha=0.06, adjust=False, min_periods=20).mean()
    z = _rolling_zscore(sd, YDAYS)
    ind = ((mdd > 0.20) & (loss_event > 0) & (z > 2.0)).astype(float).where(
        mdd.notna() & z.notna(), np.nan)
    return (ind).diff().diff()

def f53_atds_121_var_innovation_504d_log_ret_d2(close: pd.Series) -> pd.Series:
    """1-day change in VaR(95) computed over 504d window."""
    r = _log_ret(close)
    v = -_rolling_q(r, DDAYS_2Y, 0.05)
    return (v.diff()).diff().diff()

def f53_atds_122_es_innovation_252d_log_ret_d2(close: pd.Series) -> pd.Series:
    """1-day change in ES(95) over 252d."""
    r = _log_ret(close)
    def _es(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        thr = np.quantile(v, 0.05)
        tail = v[v <= thr]
        return float(-tail.mean()) if tail.size > 0 else np.nan
    es = r.rolling(YDAYS, min_periods=QDAYS).apply(_es, raw=True)
    return (es.diff()).diff().diff()

def f53_atds_123_var_jump_component_252d_via_3sigma_d2(close: pd.Series) -> pd.Series:
    """VaR(95) computed only on jump returns (|r| > 3 sigma) over 252d."""
    r = _log_ret(close)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    jumps = r.where(r.abs() > 3.0 * sd, np.nan)
    return (-_rolling_q(jumps, YDAYS, 0.05)).diff().diff()

def f53_atds_124_var_continuous_component_252d_via_3sigma_d2(close: pd.Series) -> pd.Series:
    """VaR(95) on continuous returns (|r| <= 3 sigma) over 252d."""
    r = _log_ret(close)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    cont = r.where(r.abs() <= 3.0 * sd, np.nan)
    return (-_rolling_q(cont, YDAYS, 0.05)).diff().diff()

def f53_atds_125_es_jump_component_252d_via_3sigma_d2(close: pd.Series) -> pd.Series:
    """ES(95) on jump returns (|r| > 3 sigma) over 252d."""
    r = _log_ret(close)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    jumps = r.where(r.abs() > 3.0 * sd, np.nan)
    def _es(w):
        v = w[~np.isnan(w)]
        if v.size < 5:
            return np.nan
        thr = np.quantile(v, 0.05)
        tail = v[v <= thr]
        return float(-tail.mean()) if tail.size > 0 else np.nan
    res = jumps.rolling(YDAYS, min_periods=QDAYS).apply(_es, raw=True)
    return (res).diff().diff()

def f53_atds_126_es_continuous_component_252d_via_3sigma_d2(close: pd.Series) -> pd.Series:
    """ES(95) on continuous returns over 252d."""
    r = _log_ret(close)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    cont = r.where(r.abs() <= 3.0 * sd, np.nan)
    def _es(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        thr = np.quantile(v, 0.05)
        tail = v[v <= thr]
        return float(-tail.mean()) if tail.size > 0 else np.nan
    res = cont.rolling(YDAYS, min_periods=QDAYS).apply(_es, raw=True)
    return (res).diff().diff()

def f53_atds_127_var_attribution_to_skew_252d_d2(close: pd.Series) -> pd.Series:
    """Cornish-Fisher skew contribution to VaR(95): (z^2 - 1)/6 * skew * sd over 252d."""
    r = _log_ret(close)
    sk = _rolling_skew(r, YDAYS)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    z = _norm_ppf(0.05)
    return ((z * z - 1.0) / 6.0 * sk * sd).diff().diff()

def f53_atds_128_var_attribution_to_kurt_252d_d2(close: pd.Series) -> pd.Series:
    """Cornish-Fisher kurt contribution: (z^3 - 3z)/24 * excess_kurt * sd over 252d."""
    r = _log_ret(close)
    kt = _rolling_kurt(r, YDAYS)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    z = _norm_ppf(0.05)
    return ((z ** 3 - 3.0 * z) / 24.0 * kt * sd).diff().diff()

def f53_atds_129_var_change_attribution_vol_252d_d2(close: pd.Series) -> pd.Series:
    """Change in VaR(95) attributable to vol change: -z * dsd over 252d."""
    r = _log_ret(close)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    z = _norm_ppf(0.05)
    return (-z * sd.diff()).diff().diff()

def f53_atds_130_var_change_attribution_skew_252d_d2(close: pd.Series) -> pd.Series:
    """Change in VaR(95) attributable to skew change: (z^2-1)/6 * dskew * sd over 252d."""
    r = _log_ret(close)
    sk = _rolling_skew(r, YDAYS)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    z = _norm_ppf(0.05)
    return ((z * z - 1.0) / 6.0 * sk.diff() * sd).diff().diff()

def f53_atds_131_recovery_speed_post_dd_avg_252d_d2(close: pd.Series) -> pd.Series:
    """Mean log_ret in 21 bars following the trough of each drawdown in last 252d."""
    lc = _safe_log(close)
    r = lc.diff()
    episodes_list = _drawdown_episodes(close)
    nb = len(close)
    out = np.full(nb, np.nan, dtype=float)
    for i in range(nb):
        if i < QDAYS:
            continue
        lo = max(0, i - YDAYS + 1)
        speeds = []
        for e in episodes_list:
            if lo <= e[1] <= i:
                ts = e[1]
                te = min(ts + MDAYS, i + 1)
                if te > ts:
                    segs = r.values[ts + 1:te + 1]
                    segs = segs[~np.isnan(segs)]
                    if segs.size > 0:
                        speeds.append(float(segs.mean()))
        if len(speeds) >= 1:
            out[i] = float(np.mean(speeds))
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()

def f53_atds_132_drawdown_recovery_time_mean_252d_d2(close: pd.Series) -> pd.Series:
    """Mean recovery time (bars from trough to new high) of drawdowns in last 252d."""
    episodes_list = _drawdown_episodes(close)
    mp = max(YDAYS // 3, 30)
    nb = len(close)
    out = np.full(nb, np.nan, dtype=float)
    for i in range(nb):
        if i < mp - 1:
            continue
        lo = max(0, i - YDAYS + 1)
        times = [float(e[2] - e[1]) for e in episodes_list if lo <= e[1] <= i and e[2] > e[1]]
        if len(times) >= 2:
            out[i] = float(np.mean(times))
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()

def f53_atds_133_drawdown_recovery_time_median_252d_d2(close: pd.Series) -> pd.Series:
    """Median recovery time of drawdowns in last 252d."""
    episodes_list = _drawdown_episodes(close)
    mp = max(YDAYS // 3, 30)
    nb = len(close)
    out = np.full(nb, np.nan, dtype=float)
    for i in range(nb):
        if i < mp - 1:
            continue
        lo = max(0, i - YDAYS + 1)
        times = [float(e[2] - e[1]) for e in episodes_list if lo <= e[1] <= i and e[2] > e[1]]
        if len(times) >= 2:
            out[i] = float(np.median(times))
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()

def f53_atds_134_drawdown_recovery_failure_indicator_252d_d2(close: pd.Series) -> pd.Series:
    """Indicator: any drawdown in last 252d with duration > 252d AND not recovered."""
    lc = _safe_log(close)
    rmax = lc.expanding(min_periods=1).max()
    uw = (lc < rmax - 1e-12).astype(float).where(lc.notna(), np.nan)
    max_uw = _max_time_under_water_in_window(close, YDAYS)
    return ((max_uw > YDAYS / 2).astype(float).where(max_uw.notna(), np.nan)).diff().diff()

def f53_atds_135_drawdown_count_per_unit_time_252d_d2(close: pd.Series) -> pd.Series:
    """Drawdown count / drawdown total duration over 252d - frequency normalized by total dd time."""
    ct = _drawdown_count_within_window(close, YDAYS)
    tw = _time_under_water_fraction(close, YDAYS)
    return (_safe_div(ct, tw * float(YDAYS))).diff().diff()

def f53_atds_136_max_dd_recovery_efficiency_252d_d2(close: pd.Series) -> pd.Series:
    """(Max drawdown depth) / (max time-under-water) over 252d - depth per time efficiency."""
    mdd = -_rolling_max_drawdown(close, YDAYS)
    muw = _max_time_under_water_in_window(close, YDAYS)
    return (_safe_div(mdd, muw)).diff().diff()

def f53_atds_137_ratio_recent_dd_count_to_long_term_504d_d2(close: pd.Series) -> pd.Series:
    """Drawdown count in last 252d / drawdown count in last 504d - regime acceleration."""
    ct252 = _drawdown_count_within_window(close, YDAYS)
    ct504 = _drawdown_count_within_window(close, DDAYS_2Y)
    return (_safe_div(ct252, ct504)).diff().diff()

def f53_atds_138_ratio_recent_pain_to_long_term_504d_d2(close: pd.Series) -> pd.Series:
    """Pain index over 252d / pain index over 504d - relative pain intensity."""
    lc = _safe_log(close)
    def _pi(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        cm = np.maximum.accumulate(v)
        return float((-(v - cm)).mean())
    pi252 = lc.rolling(YDAYS, min_periods=QDAYS).apply(_pi, raw=True)
    pi504 = lc.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_pi, raw=True)
    return (_safe_div(pi252, pi504)).diff().diff()

def f53_atds_139_drawdown_severity_zscore_252d_d2(close: pd.Series) -> pd.Series:
    """Z-score over 252d of (mean drawdown depth * mean duration) - regime severity intensity."""
    depth = _drawdown_depth_stats(close, YDAYS, 'mean')
    dur = _drawdown_duration_stats(close, YDAYS, 'mean')
    sev = depth * dur
    return (_rolling_zscore(sev, YDAYS)).diff().diff()

def f53_atds_140_recovery_failure_probability_proxy_252d_d2(close: pd.Series) -> pd.Series:
    """Fraction of last 252d drawdowns that did not recover within their own duration window."""
    episodes_list = _drawdown_episodes(close)
    mp = max(YDAYS // 3, 30)
    nb = len(close)
    out = np.full(nb, np.nan, dtype=float)
    for i in range(nb):
        if i < mp - 1:
            continue
        lo = max(0, i - YDAYS + 1)
        eps_in = [e for e in episodes_list if lo <= e[1] <= i]
        if len(eps_in) < 2:
            continue
        failed = sum(1 for e in eps_in if e[2] >= i)
        out[i] = float(failed) / float(len(eps_in))
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()

def f53_atds_141_crash_signature_composite_score_252d_d2(close: pd.Series) -> pd.Series:
    """Z-score-sum of (ES(95), GARCH-persistence proxy, max-drawdown, breach count) - omnibus crash precursor."""
    r = _log_ret(close)
    def _es(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        thr = np.quantile(v, 0.05)
        tail = v[v <= thr]
        return float(-tail.mean()) if tail.size > 0 else np.nan
    es = r.rolling(YDAYS, min_periods=QDAYS).apply(_es, raw=True)
    absr = r.abs()
    def _ac(w):
        x = w[~np.isnan(w)]
        if x.size < 30:
            return np.nan
        a = x[:-1]; b = x[1:]
        if a.std() == 0 or b.std() == 0:
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    persist = absr.rolling(YDAYS, min_periods=QDAYS).apply(_ac, raw=True)
    mdd = -_rolling_max_drawdown(close, YDAYS)
    v = -_rolling_q(r, YDAYS, 0.05)
    br = (-r > v).astype(float).where(v.notna(), np.nan)
    bc = br.rolling(YDAYS, min_periods=QDAYS).sum()
    z1 = _rolling_zscore(es, YDAYS); z2 = _rolling_zscore(persist, YDAYS)
    z3 = _rolling_zscore(mdd, YDAYS); z4 = _rolling_zscore(bc, YDAYS)
    return (z1.fillna(0.0) + z2.fillna(0.0) + z3.fillna(0.0) + z4.fillna(0.0)).diff().diff()

def f53_atds_142_blowoff_top_indicator_composite_252d_d2(close: pd.Series) -> pd.Series:
    """Indicator: vol-z > 1 AND ES(95) above 75th pct AND recovery time > median over 252d - blowoff regime."""
    r = _log_ret(close)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    z = _rolling_zscore(sd, YDAYS)
    def _es(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        thr = np.quantile(v, 0.05)
        tail = v[v <= thr]
        return float(-tail.mean()) if tail.size > 0 else np.nan
    es = r.rolling(YDAYS, min_periods=QDAYS).apply(_es, raw=True)
    p75_es = es.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    tuw = _time_under_water_fraction(close, YDAYS)
    med_tuw = tuw.rolling(DDAYS_2Y, min_periods=YDAYS).median()
    ind = ((z > 1.0) & (es > p75_es) & (tuw > med_tuw)).astype(float).where(
        z.notna() & es.notna() & tuw.notna(), np.nan)
    return (ind).diff().diff()

def f53_atds_143_multi_horizon_tail_alignment_score_252d_d2(close: pd.Series) -> pd.Series:
    """Sum of z-scored VaR(95) at 21d, 63d, 252d aligned = +3 if all-extreme."""
    r = _log_ret(close)
    v21 = -_rolling_q(r, MDAYS, 0.05)
    v63 = -_rolling_q(r, QDAYS, 0.05)
    v252 = -_rolling_q(r, YDAYS, 0.05)
    z1 = _rolling_zscore(v21, YDAYS); z2 = _rolling_zscore(v63, YDAYS); z3 = _rolling_zscore(v252, YDAYS)
    return (z1.fillna(0.0) + z2.fillna(0.0) + z3.fillna(0.0)).diff().diff()

def f53_atds_144_coherent_risk_term_structure_score_252d_d2(close: pd.Series) -> pd.Series:
    """Sign-aligned product of (VaR(95) term-struct slope, ES(95) term-struct slope) over 252d."""
    r = _log_ret(close)
    v21 = -_rolling_q(r, MDAYS, 0.05)
    v252 = -_rolling_q(r, YDAYS, 0.05)
    slope_v = _safe_log(v21) - _safe_log(v252)
    def _es(w, q):
        x = w[~np.isnan(w)]
        if x.size < 30:
            return np.nan
        thr = np.quantile(x, 1.0 - q)
        tail = x[x <= thr]
        return float(-tail.mean()) if tail.size > 0 else np.nan
    es21 = r.rolling(MDAYS, min_periods=10).apply(lambda w: _es(w, 0.95), raw=True)
    es252 = r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _es(w, 0.95), raw=True)
    slope_e = _safe_log(es21) - _safe_log(es252)
    return (np.sign(slope_v * slope_e) * (slope_v.abs() + slope_e.abs())).diff().diff()

def f53_atds_145_tail_risk_aggregation_score_252d_d2(close: pd.Series) -> pd.Series:
    """Sum of normalized: ES(95), MDD, CDaR(95), Ulcer over 252d - aggregate tail risk."""
    r = _log_ret(close)
    def _es(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        thr = np.quantile(v, 0.05)
        tail = v[v <= thr]
        return float(-tail.mean()) if tail.size > 0 else np.nan
    es = r.rolling(YDAYS, min_periods=QDAYS).apply(_es, raw=True)
    mdd = -_rolling_max_drawdown(close, YDAYS)
    lc = _safe_log(close)
    def _cdar(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        cm = np.maximum.accumulate(v); dd = -(v - cm)
        thr = np.quantile(dd, 0.95)
        tail = dd[dd >= thr]
        return float(tail.mean()) if tail.size > 0 else np.nan
    cdar = lc.rolling(YDAYS, min_periods=QDAYS).apply(_cdar, raw=True)
    def _u(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        cm = np.maximum.accumulate(v)
        return float(np.sqrt(np.mean((v - cm) ** 2)))
    ulc = lc.rolling(YDAYS, min_periods=QDAYS).apply(_u, raw=True)
    z1 = _rolling_zscore(es, YDAYS); z2 = _rolling_zscore(mdd, YDAYS)
    z3 = _rolling_zscore(cdar, YDAYS); z4 = _rolling_zscore(ulc, YDAYS)
    return (z1.fillna(0.0) + z2.fillna(0.0) + z3.fillna(0.0) + z4.fillna(0.0)).diff().diff()

def f53_atds_146_drawdown_recovery_composite_252d_d2(close: pd.Series) -> pd.Series:
    """(Max drawdown depth * max time-under-water) / (sum log_ret in 252d + 1) - composite recovery risk."""
    r = _log_ret(close)
    cum = r.rolling(YDAYS, min_periods=QDAYS).sum()
    mdd = -_rolling_max_drawdown(close, YDAYS)
    muw = _max_time_under_water_in_window(close, YDAYS)
    return (_safe_div(mdd * muw, cum + 1.0)).diff().diff()

def f53_atds_147_tail_dependence_breakdown_proxy_252d_d2(close: pd.Series) -> pd.Series:
    """Sign change indicator of tail_dep_lower over 252d - dependence regime transition."""
    r = _log_ret(close)
    lc = _safe_log(close)
    lag = lc.diff().shift(1)
    joint_low = ((r < r.rolling(YDAYS, min_periods=QDAYS).quantile(0.05)) & (lag < lag.rolling(YDAYS, min_periods=QDAYS).quantile(0.05))).astype(float)
    td = joint_low.rolling(YDAYS, min_periods=QDAYS).mean()
    ch = td.diff()
    return (ch).diff().diff()

def f53_atds_148_systemic_tail_indicator_combined_252d_d2(close: pd.Series) -> pd.Series:
    """Indicator: |VaR(99)|+MDD+TuW > 90th-pct composite over 252d."""
    r = _log_ret(close)
    v99 = -_rolling_q(r, YDAYS, 0.01)
    mdd = -_rolling_max_drawdown(close, YDAYS)
    tuw = _time_under_water_fraction(close, YDAYS)
    z1 = _rolling_zscore(v99, YDAYS); z2 = _rolling_zscore(mdd, YDAYS); z3 = _rolling_zscore(tuw, YDAYS)
    comp = z1.fillna(0.0) + z2.fillna(0.0) + z3.fillna(0.0)
    p90 = comp.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    return ((comp > p90).astype(float).where(p90.notna(), np.nan)).diff().diff()

def f53_atds_149_blowoff_imminence_composite_252d_d2(close: pd.Series) -> pd.Series:
    """Z-score sum: positive return skew + low ES(95) + small drawdown + high recovery rate - top-formation regime."""
    r = _log_ret(close)
    sk = _rolling_skew(r, YDAYS)
    def _es(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        thr = np.quantile(v, 0.05)
        tail = v[v <= thr]
        return float(-tail.mean()) if tail.size > 0 else np.nan
    es = r.rolling(YDAYS, min_periods=QDAYS).apply(_es, raw=True)
    mdd = -_rolling_max_drawdown(close, YDAYS)
    lc = _safe_log(close); rmax = lc.expanding(min_periods=1).max()
    at_high = (lc >= rmax - 1e-12).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    z1 = _rolling_zscore(sk, YDAYS); z2 = -_rolling_zscore(es, YDAYS)
    z3 = -_rolling_zscore(mdd, YDAYS); z4 = _rolling_zscore(at_high, YDAYS)
    return (z1.fillna(0.0) + z2.fillna(0.0) + z3.fillna(0.0) + z4.fillna(0.0)).diff().diff()

def f53_atds_150_expected_post_blowoff_drawdown_proxy_252d_d2(close: pd.Series) -> pd.Series:
    """ES(95) * (1 + GARCH-persistence-proxy) - expected post-blowoff loss magnitude under high persistence."""
    r = _log_ret(close)
    def _es(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        thr = np.quantile(v, 0.05)
        tail = v[v <= thr]
        return float(-tail.mean()) if tail.size > 0 else np.nan
    es = r.rolling(YDAYS, min_periods=QDAYS).apply(_es, raw=True)
    absr = r.abs()
    def _ac(w):
        x = w[~np.isnan(w)]
        if x.size < 30:
            return np.nan
        a = x[:-1]; b = x[1:]
        if a.std() == 0 or b.std() == 0:
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    p = absr.rolling(YDAYS, min_periods=QDAYS).apply(_ac, raw=True)
    return (es * (1.0 + p)).diff().diff()


# ============================================================
#                         REGISTRY 076_150 (d2)
# ============================================================

ADVANCED_TAIL_DRAWDOWN_STRUCTURE_D2_REGISTRY_076_150 = {
    "f53_atds_076_circular_block_var_95_block5_252d_d2": {"inputs": ["close"], "func": f53_atds_076_circular_block_var_95_block5_252d_d2},
    "f53_atds_077_stationary_bootstrap_var_95_p_005_252d_d2": {"inputs": ["close"], "func": f53_atds_077_stationary_bootstrap_var_95_p_005_252d_d2},
    "f53_atds_078_block_bootstrap_es_95_block5_252d_d2": {"inputs": ["close"], "func": f53_atds_078_block_bootstrap_es_95_block5_252d_d2},
    "f53_atds_079_block_bootstrap_var_uncertainty_es_252d_d2": {"inputs": ["close"], "func": f53_atds_079_block_bootstrap_var_uncertainty_es_252d_d2},
    "f53_atds_080_bootstrap_var_minus_hist_var_95_252d_d2": {"inputs": ["close"], "func": f53_atds_080_bootstrap_var_minus_hist_var_95_252d_d2},
    "f53_atds_081_ulcer_index_504d_d2": {"inputs": ["close"], "func": f53_atds_081_ulcer_index_504d_d2},
    "f53_atds_082_ulcer_index_1260d_d2": {"inputs": ["close"], "func": f53_atds_082_ulcer_index_1260d_d2},
    "f53_atds_083_ulcer_index_change_speed_21d_252d_d2": {"inputs": ["close"], "func": f53_atds_083_ulcer_index_change_speed_21d_252d_d2},
    "f53_atds_084_lake_ratio_252d_d2": {"inputs": ["close"], "func": f53_atds_084_lake_ratio_252d_d2},
    "f53_atds_085_mean_squared_drawdown_252d_d2": {"inputs": ["close"], "func": f53_atds_085_mean_squared_drawdown_252d_d2},
    "f53_atds_086_max_drawdown_decay_rate_504d_d2": {"inputs": ["close"], "func": f53_atds_086_max_drawdown_decay_rate_504d_d2},
    "f53_atds_087_pain_index_504d_d2": {"inputs": ["close"], "func": f53_atds_087_pain_index_504d_d2},
    "f53_atds_088_pain_index_acceleration_21d_252d_d2": {"inputs": ["close"], "func": f53_atds_088_pain_index_acceleration_21d_252d_d2},
    "f53_atds_089_ulcer_minus_pain_252d_d2": {"inputs": ["close"], "func": f53_atds_089_ulcer_minus_pain_252d_d2},
    "f53_atds_090_drawdown_severity_index_depth_times_duration_252d_d2": {"inputs": ["close"], "func": f53_atds_090_drawdown_severity_index_depth_times_duration_252d_d2},
    "f53_atds_091_consecutive_neg_returns_max_252d_d2": {"inputs": ["close"], "func": f53_atds_091_consecutive_neg_returns_max_252d_d2},
    "f53_atds_092_consecutive_neg_returns_max_504d_d2": {"inputs": ["close"], "func": f53_atds_092_consecutive_neg_returns_max_504d_d2},
    "f53_atds_093_consecutive_loss_streak_count_above_3_252d_d2": {"inputs": ["close"], "func": f53_atds_093_consecutive_loss_streak_count_above_3_252d_d2},
    "f53_atds_094_consecutive_loss_streak_p95_length_252d_d2": {"inputs": ["close"], "func": f53_atds_094_consecutive_loss_streak_p95_length_252d_d2},
    "f53_atds_095_consecutive_loss_severity_mean_252d_d2": {"inputs": ["close"], "func": f53_atds_095_consecutive_loss_severity_mean_252d_d2},
    "f53_atds_096_hot_hand_index_neg_252d_d2": {"inputs": ["close"], "func": f53_atds_096_hot_hand_index_neg_252d_d2},
    "f53_atds_097_hot_hand_index_pos_252d_d2": {"inputs": ["close"], "func": f53_atds_097_hot_hand_index_pos_252d_d2},
    "f53_atds_098_cold_streak_recovery_time_252d_d2": {"inputs": ["close"], "func": f53_atds_098_cold_streak_recovery_time_252d_d2},
    "f53_atds_099_gambler_fallacy_proxy_neg_252d_d2": {"inputs": ["close"], "func": f53_atds_099_gambler_fallacy_proxy_neg_252d_d2},
    "f53_atds_100_gambler_fallacy_proxy_pos_252d_d2": {"inputs": ["close"], "func": f53_atds_100_gambler_fallacy_proxy_pos_252d_d2},
    "f53_atds_101_signed_es_95_negative_only_252d_d2": {"inputs": ["close"], "func": f53_atds_101_signed_es_95_negative_only_252d_d2},
    "f53_atds_102_signed_es_95_positive_only_252d_d2": {"inputs": ["close"], "func": f53_atds_102_signed_es_95_positive_only_252d_d2},
    "f53_atds_103_signed_var_95_negative_only_252d_d2": {"inputs": ["close"], "func": f53_atds_103_signed_var_95_negative_only_252d_d2},
    "f53_atds_104_signed_var_95_positive_only_252d_d2": {"inputs": ["close"], "func": f53_atds_104_signed_var_95_positive_only_252d_d2},
    "f53_atds_105_asymmetric_es_sum_signed_252d_d2": {"inputs": ["close"], "func": f53_atds_105_asymmetric_es_sum_signed_252d_d2},
    "f53_atds_106_asymmetric_var_diff_signed_252d_d2": {"inputs": ["close"], "func": f53_atds_106_asymmetric_var_diff_signed_252d_d2},
    "f53_atds_107_directional_tail_dominance_signed_252d_d2": {"inputs": ["close"], "func": f53_atds_107_directional_tail_dominance_signed_252d_d2},
    "f53_atds_108_tail_skew_via_var_signed_252d_d2": {"inputs": ["close"], "func": f53_atds_108_tail_skew_via_var_signed_252d_d2},
    "f53_atds_109_tail_skew_via_es_signed_252d_d2": {"inputs": ["close"], "func": f53_atds_109_tail_skew_via_es_signed_252d_d2},
    "f53_atds_110_tail_balance_score_252d_d2": {"inputs": ["close"], "func": f53_atds_110_tail_balance_score_252d_d2},
    "f53_atds_111_covid_proxy_stress_loss_count_5pct_252d_d2": {"inputs": ["close"], "func": f53_atds_111_covid_proxy_stress_loss_count_5pct_252d_d2},
    "f53_atds_112_flash_crash_proxy_count_3pct_252d_d2": {"inputs": ["close"], "func": f53_atds_112_flash_crash_proxy_count_3pct_252d_d2},
    "f53_atds_113_lehman_proxy_stress_loss_week_10pct_252d_d2": {"inputs": ["close"], "func": f53_atds_113_lehman_proxy_stress_loss_week_10pct_252d_d2},
    "f53_atds_114_black_monday_proxy_20pct_one_day_252d_d2": {"inputs": ["close"], "func": f53_atds_114_black_monday_proxy_20pct_one_day_252d_d2},
    "f53_atds_115_flash_move_count_above_2pct_either_direction_252d_d2": {"inputs": ["close"], "func": f53_atds_115_flash_move_count_above_2pct_either_direction_252d_d2},
    "f53_atds_116_macro_stress_event_count_5sigma_252d_d2": {"inputs": ["close"], "func": f53_atds_116_macro_stress_event_count_5sigma_252d_d2},
    "f53_atds_117_tail_event_clustering_5sigma_paired_252d_d2": {"inputs": ["close"], "func": f53_atds_117_tail_event_clustering_5sigma_paired_252d_d2},
    "f53_atds_118_stress_period_persistence_252d_d2": {"inputs": ["close"], "func": f53_atds_118_stress_period_persistence_252d_d2},
    "f53_atds_119_expected_clustered_tail_event_rate_252d_d2": {"inputs": ["close"], "func": f53_atds_119_expected_clustered_tail_event_rate_252d_d2},
    "f53_atds_120_crisis_indicator_combined_252d_d2": {"inputs": ["close"], "func": f53_atds_120_crisis_indicator_combined_252d_d2},
    "f53_atds_121_var_innovation_504d_log_ret_d2": {"inputs": ["close"], "func": f53_atds_121_var_innovation_504d_log_ret_d2},
    "f53_atds_122_es_innovation_252d_log_ret_d2": {"inputs": ["close"], "func": f53_atds_122_es_innovation_252d_log_ret_d2},
    "f53_atds_123_var_jump_component_252d_via_3sigma_d2": {"inputs": ["close"], "func": f53_atds_123_var_jump_component_252d_via_3sigma_d2},
    "f53_atds_124_var_continuous_component_252d_via_3sigma_d2": {"inputs": ["close"], "func": f53_atds_124_var_continuous_component_252d_via_3sigma_d2},
    "f53_atds_125_es_jump_component_252d_via_3sigma_d2": {"inputs": ["close"], "func": f53_atds_125_es_jump_component_252d_via_3sigma_d2},
    "f53_atds_126_es_continuous_component_252d_via_3sigma_d2": {"inputs": ["close"], "func": f53_atds_126_es_continuous_component_252d_via_3sigma_d2},
    "f53_atds_127_var_attribution_to_skew_252d_d2": {"inputs": ["close"], "func": f53_atds_127_var_attribution_to_skew_252d_d2},
    "f53_atds_128_var_attribution_to_kurt_252d_d2": {"inputs": ["close"], "func": f53_atds_128_var_attribution_to_kurt_252d_d2},
    "f53_atds_129_var_change_attribution_vol_252d_d2": {"inputs": ["close"], "func": f53_atds_129_var_change_attribution_vol_252d_d2},
    "f53_atds_130_var_change_attribution_skew_252d_d2": {"inputs": ["close"], "func": f53_atds_130_var_change_attribution_skew_252d_d2},
    "f53_atds_131_recovery_speed_post_dd_avg_252d_d2": {"inputs": ["close"], "func": f53_atds_131_recovery_speed_post_dd_avg_252d_d2},
    "f53_atds_132_drawdown_recovery_time_mean_252d_d2": {"inputs": ["close"], "func": f53_atds_132_drawdown_recovery_time_mean_252d_d2},
    "f53_atds_133_drawdown_recovery_time_median_252d_d2": {"inputs": ["close"], "func": f53_atds_133_drawdown_recovery_time_median_252d_d2},
    "f53_atds_134_drawdown_recovery_failure_indicator_252d_d2": {"inputs": ["close"], "func": f53_atds_134_drawdown_recovery_failure_indicator_252d_d2},
    "f53_atds_135_drawdown_count_per_unit_time_252d_d2": {"inputs": ["close"], "func": f53_atds_135_drawdown_count_per_unit_time_252d_d2},
    "f53_atds_136_max_dd_recovery_efficiency_252d_d2": {"inputs": ["close"], "func": f53_atds_136_max_dd_recovery_efficiency_252d_d2},
    "f53_atds_137_ratio_recent_dd_count_to_long_term_504d_d2": {"inputs": ["close"], "func": f53_atds_137_ratio_recent_dd_count_to_long_term_504d_d2},
    "f53_atds_138_ratio_recent_pain_to_long_term_504d_d2": {"inputs": ["close"], "func": f53_atds_138_ratio_recent_pain_to_long_term_504d_d2},
    "f53_atds_139_drawdown_severity_zscore_252d_d2": {"inputs": ["close"], "func": f53_atds_139_drawdown_severity_zscore_252d_d2},
    "f53_atds_140_recovery_failure_probability_proxy_252d_d2": {"inputs": ["close"], "func": f53_atds_140_recovery_failure_probability_proxy_252d_d2},
    "f53_atds_141_crash_signature_composite_score_252d_d2": {"inputs": ["close"], "func": f53_atds_141_crash_signature_composite_score_252d_d2},
    "f53_atds_142_blowoff_top_indicator_composite_252d_d2": {"inputs": ["close"], "func": f53_atds_142_blowoff_top_indicator_composite_252d_d2},
    "f53_atds_143_multi_horizon_tail_alignment_score_252d_d2": {"inputs": ["close"], "func": f53_atds_143_multi_horizon_tail_alignment_score_252d_d2},
    "f53_atds_144_coherent_risk_term_structure_score_252d_d2": {"inputs": ["close"], "func": f53_atds_144_coherent_risk_term_structure_score_252d_d2},
    "f53_atds_145_tail_risk_aggregation_score_252d_d2": {"inputs": ["close"], "func": f53_atds_145_tail_risk_aggregation_score_252d_d2},
    "f53_atds_146_drawdown_recovery_composite_252d_d2": {"inputs": ["close"], "func": f53_atds_146_drawdown_recovery_composite_252d_d2},
    "f53_atds_147_tail_dependence_breakdown_proxy_252d_d2": {"inputs": ["close"], "func": f53_atds_147_tail_dependence_breakdown_proxy_252d_d2},
    "f53_atds_148_systemic_tail_indicator_combined_252d_d2": {"inputs": ["close"], "func": f53_atds_148_systemic_tail_indicator_combined_252d_d2},
    "f53_atds_149_blowoff_imminence_composite_252d_d2": {"inputs": ["close"], "func": f53_atds_149_blowoff_imminence_composite_252d_d2},
    "f53_atds_150_expected_post_blowoff_drawdown_proxy_252d_d2": {"inputs": ["close"], "func": f53_atds_150_expected_post_blowoff_drawdown_proxy_252d_d2},
}
