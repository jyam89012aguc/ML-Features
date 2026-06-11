"""27_macd_topping_dynamics d2 features 376-450 — order-2 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff().diff(). Self-contained; helpers redefined locally per HANDOFF."""
import numpy as np
import pandas as pd
YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
DDAYS_5Y = 1260
_BFS = [(5, 35), (12, 26), (19, 39), (50, 200)]
_BFSS = [(5, 35, 5), (12, 26, 9), (19, 39, 9), (50, 200, 30)]

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

def _slope_inner(w):
    valid = ~np.isnan(w)
    if valid.sum() < 2:
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

def _rolling_slope(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    return s.rolling(n, min_periods=min_periods).apply(_slope_inner, raw=True)

def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=max(n // 2, 2)).mean()

def _macd(close, fast=12, slow=26, signal=9):
    macd = _ema(close, fast) - _ema(close, slow)
    sig = _ema(macd, signal)
    histo = macd - sig
    return (macd, sig, histo)

def _bars_since_true(mask: pd.Series) -> pd.Series:
    arr = mask.astype(bool).to_numpy()
    out = np.full(arr.shape, np.nan)
    last = -1
    for i in range(arr.size):
        if arr[i]:
            last = i
            out[i] = 0.0
        elif last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=mask.index)

def _streak_true(mask: pd.Series) -> pd.Series:
    arr = mask.astype(bool).to_numpy()
    out = np.zeros(arr.shape, dtype=float)
    c = 0
    for i in range(arr.size):
        c = c + 1 if arr[i] else 0
        out[i] = float(c)
    return pd.Series(out, index=mask.index)

def _pct_rank_window(w):
    if np.isnan(w).all():
        return np.nan
    last = w[-1]
    if np.isnan(last):
        return np.nan
    v = w[~np.isnan(w)]
    if v.size == 0:
        return np.nan
    return float((v <= last).sum()) / float(v.size)

def _entropy_window(w):
    v = w[~np.isnan(w)]
    if v.size < MDAYS:
        return np.nan
    q = np.quantile(v, [0.2, 0.4, 0.6, 0.8])
    bins = np.digitize(v, q)
    p = np.array([(bins == k).sum() for k in range(5)], dtype=float) / v.size
    p = p[p > 0]
    if p.size == 0:
        return np.nan
    return float(-(p * np.log(p)).sum())

def _sample_entropy_window(w, m=2, r=0.2):
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < m + 2:
        return np.nan
    sd = v.std()
    if sd <= 0:
        return np.nan
    tol = r * sd

    def _count(mm):
        templ = np.array([v[i:i + mm] for i in range(nn - mm + 1)])
        c = 0
        for i in range(len(templ)):
            d = np.max(np.abs(templ - templ[i]), axis=1)
            c += int((d <= tol).sum() - 1)
        return c
    a = _count(m + 1)
    b = _count(m)
    if a <= 0 or b <= 0:
        return np.nan
    return float(-np.log(a / b))

def _approx_entropy_window(w, m=2, r=0.2):
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < m + 2:
        return np.nan
    sd = v.std()
    if sd <= 0:
        return np.nan
    tol = r * sd

    def _phi(mm):
        templ = np.array([v[i:i + mm] for i in range(nn - mm + 1)])
        C = []
        for i in range(len(templ)):
            d = np.max(np.abs(templ - templ[i]), axis=1)
            C.append((d <= tol).sum() / float(nn - mm + 1))
        C = np.array(C)
        C = C[C > 0]
        return float(np.log(C).mean()) if C.size else np.nan
    p1 = _phi(m)
    p2 = _phi(m + 1)
    if np.isnan(p1) or np.isnan(p2):
        return np.nan
    return float(p1 - p2)

def _perm_entropy_window(w, order=3):
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < order + 2:
        return np.nan
    patterns = {}
    for i in range(nn - order + 1):
        seg = v[i:i + order]
        rank = tuple(np.argsort(seg))
        patterns[rank] = patterns.get(rank, 0) + 1
    total = float(sum(patterns.values()))
    p = np.array([c / total for c in patterns.values()])
    p = p[p > 0]
    return float(-(p * np.log(p)).sum())

def _multiscale_entropy_window(w, scale=2):
    v = w[~np.isnan(w)]
    if v.size < scale * 10:
        return np.nan
    nn = v.size // scale
    coarse = np.array([v[i * scale:(i + 1) * scale].mean() for i in range(nn)])
    return _sample_entropy_window(coarse, m=2, r=0.2)

def _higuchi_fd_window(w, k_max=8):
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < k_max + 2:
        return np.nan
    L = []
    x = np.arange(1, nn + 1)
    for k in range(1, k_max + 1):
        Lk = []
        for mi in range(k):
            idx = np.arange(mi, nn, k)
            if idx.size < 2:
                continue
            d = np.abs(np.diff(v[idx])).sum()
            norm = (nn - 1) / float((idx.size - 1) * k)
            Lk.append(d * norm / k)
        if Lk:
            L.append(np.mean(Lk))
    if len(L) < 3:
        return np.nan
    kk = np.arange(1, len(L) + 1, dtype=float)
    lL = np.log(np.array(L))
    lk = np.log(1.0 / kk)
    sl = np.polyfit(lk, lL, 1)[0]
    return float(sl)

def _petrosian_fd_window(w):
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < 4:
        return np.nan
    d = np.diff(v)
    N_delta = int((d[:-1] * d[1:] < 0).sum())
    if N_delta == 0:
        return np.nan
    return float(np.log10(nn) / (np.log10(nn) + np.log10(nn / (nn + 0.4 * N_delta))))

def _hurst_rs_window(w):
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < 32:
        return np.nan
    m0 = v.mean()
    y = np.cumsum(v - m0)
    R = y.max() - y.min()
    S = v.std()
    if S <= 0 or R <= 0:
        return np.nan
    return float(np.log(R / S) / np.log(nn))

def _hurst_dfa_window(w):
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < 32:
        return np.nan
    y = np.cumsum(v - v.mean())
    scales = [4, 8, 16, 32]
    F = []
    for s in scales:
        if nn < s * 2:
            continue
        segs = nn // s
        f_s = []
        for i in range(segs):
            seg = y[i * s:(i + 1) * s]
            x = np.arange(s, dtype=float)
            p = np.polyfit(x, seg, 1)
            fit = np.polyval(p, x)
            f_s.append(np.sqrt(((seg - fit) ** 2).mean()))
        if f_s:
            F.append(np.mean(f_s))
    if len(F) < 2:
        return np.nan
    sc = np.array(scales[:len(F)], dtype=float)
    return float(np.polyfit(np.log(sc), np.log(F), 1)[0])

def _recurrence_rate_window(w):
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < MDAYS:
        return np.nan
    s = v.std()
    if s <= 0:
        return np.nan
    diff = v[:, None] - v[None, :]
    rec = (np.abs(diff) < 0.1 * s).sum() - nn
    return float(rec) / float(nn * (nn - 1))

def _recurrence_determinism_window(w):
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < MDAYS:
        return np.nan
    s = v.std()
    if s <= 0:
        return np.nan
    R = (np.abs(v[:, None] - v[None, :]) < 0.1 * s).astype(int)
    np.fill_diagonal(R, 0)
    diag_count = 0
    line_count = 0
    for k in range(1, nn):
        d = np.diag(R, k=k)
        run = 0
        for x in d:
            if x:
                run += 1
            else:
                if run >= 2:
                    diag_count += run
                run = 0
        if run >= 2:
            diag_count += run
        line_count += int(d.sum())
    if line_count == 0:
        return np.nan
    return float(diag_count) / float(line_count)

def _lz_complexity_window(w):
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < 5:
        return np.nan
    med = np.median(v)
    s = ''.join(('1' if x > med else '0' for x in v))
    i = 0
    k = 1
    c = 1
    while i + k <= len(s):
        if s[i:i + k] not in s[:i] + s[i:i + k - 1]:
            c += 1
            i += k
            k = 1
        else:
            k += 1
            if i + k > len(s):
                break
    return float(c) / (float(nn) / np.log2(nn) if nn > 1 else 1.0)

def _kolmogorov_proxy_window(w):
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < 8:
        return np.nan
    import zlib
    med = np.median(v)
    s = bytes(''.join(('1' if x > med else '0' for x in v)), 'ascii')
    return float(len(zlib.compress(s))) / float(nn)

def _predictability_horizon_window(w):
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < MDAYS:
        return np.nan
    for k in range(1, min(nn // 2, MDAYS)):
        a = v[:-k]
        b = v[k:]
        if a.std() == 0 or b.std() == 0:
            continue
        c = np.corrcoef(a, b)[0, 1]
        if abs(c) < 0.2:
            return float(k)
    return float(min(nn // 2, MDAYS))

def _info_dim_window(w):
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < MDAYS:
        return np.nan
    eps_list = [0.05, 0.1, 0.2, 0.4]
    H = []
    sd = v.std()
    if sd <= 0:
        return np.nan
    for eps in eps_list:
        bins = np.floor(v / (eps * sd)).astype(int)
        uniq, cnt = np.unique(bins, return_counts=True)
        p = cnt / cnt.sum()
        h = -(p * np.log(p)).sum()
        H.append(h)
    return float(np.polyfit(np.log(1.0 / np.array(eps_list)), H, 1)[0])

def _corr_dim_window(w):
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < MDAYS:
        return np.nan
    sd = v.std()
    if sd <= 0:
        return np.nan
    r_list = [0.1 * sd, 0.2 * sd, 0.4 * sd]
    C = []
    diff = np.abs(v[:, None] - v[None, :])
    for r in r_list:
        c = (diff < r).sum() - nn
        C.append(float(c) / float(nn * (nn - 1)))
    C = np.array(C)
    if (C <= 0).any():
        return np.nan
    return float(np.polyfit(np.log(np.array(r_list)), np.log(C), 1)[0])

def _lyapunov_proxy_window(w):
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < 5:
        return np.nan
    delta = np.abs(np.diff(v))
    delta = delta[delta > 0]
    if delta.size == 0:
        return np.nan
    return float(np.log(delta).mean())

def _persistence_rs_window(w):
    h = _hurst_rs_window(w)
    if h is None or np.isnan(h):
        return np.nan
    return float(h - 0.5)

def _basket_blowoff_count(close):
    cnt = pd.Series(0.0, index=close.index)
    for f, sl in _BFS:
        mm = _ema(close, f) - _ema(close, sl)
        rmax = mm.rolling(YDAYS, min_periods=QDAYS).max()
        bs = _bars_since_true(mm == rmax)
        drop = rmax - mm > 0.5 * rmax.abs()
        cnt = cnt + ((bs <= QDAYS) & drop).astype(float).fillna(0)
    return cnt

def _basket_div_count(high, close):
    cnt = pd.Series(0.0, index=close.index)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    for f, sl in _BFS:
        mm = _ema(close, f) - _ema(close, sl)
        prior = mm.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
        cnt = cnt + (p_new & (mm < prior)).astype(float).fillna(0)
    return cnt

def _regime_overdue(close):
    m, _, _ = _macd(close)
    sg = np.sign(m).fillna(0).astype(int)
    block = (sg != sg.shift(1)).fillna(False).cumsum()
    age = (sg.groupby(block).cumcount() + 1).where(m.notna(), np.nan).astype(float)
    flip = (sg != sg.shift(1)).fillna(False).astype(float)
    avg = _safe_div(float(YDAYS), flip.rolling(YDAYS, min_periods=QDAYS).sum())
    return (age > 2.0 * avg).astype(float).fillna(0)

def _vol_confirmed_cross_21d(close, volume):
    m, s, _ = _macd(close)
    d = m - s
    cross = (d.shift(1) > 0) & (d <= 0)
    va = volume.rolling(50, min_periods=10).mean().shift(1)
    return ((cross & (volume > 1.3 * va)).astype(float).rolling(MDAYS, min_periods=1).sum() > 0).astype(float).fillna(0)

def f27_mcdt_376_macd_persistent_weakness_while_price_holds_63_d2(close: pd.Series) -> pd.Series:
    """1 if MACD < 0 for > 40 of past 63 bars AND close > SMA200 — internal weakness while price holds."""
    m, _, _ = _macd(close)
    sma200 = close.rolling(200, min_periods=50).mean()
    weak = (m < 0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum() > 40
    return (weak & (close > sma200)).astype(float).where(m.notna() & sma200.notna(), np.nan).diff().diff()

def f27_mcdt_377_macd_failure_to_recover_above_zero_post_peak_63_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if MACD < 0 for entire past 63 bars AND high hit 252d max within last 126 bars — failure-to-recover."""
    m, _, _ = _macd(close)
    all_neg = (m < 0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum() == QDAYS
    at_252h = high == high.rolling(YDAYS, min_periods=QDAYS).max()
    recent_peak = at_252h.rolling(126, min_periods=MDAYS).sum() > 0
    return (all_neg & recent_peak).astype(float).where(m.notna(), np.nan).diff().diff()

def f27_mcdt_378_macd_lower_high_with_histogram_confirmation_63_d2(close: pd.Series) -> pd.Series:
    """1 if MACD line 21d max is below its prior 21d max AND histogram 21d max is below its prior 21d max — both lower-highs."""
    m, _, h = _macd(close)
    mh = m.rolling(MDAYS, min_periods=WDAYS).max()
    hh = h.rolling(MDAYS, min_periods=WDAYS).max()
    return ((mh < mh.shift(MDAYS)) & (hh < hh.shift(MDAYS))).astype(float).where(m.notna() & h.notna(), np.nan).diff().diff()

def f27_mcdt_379_macd_topping_configuration_v2_d2(close: pd.Series) -> pd.Series:
    """3 successively lower MACD peaks at price highs over 63d windows (split into 3): p1>p2>p3."""
    m, _, _ = _macd(close)
    p1 = m.shift(42).rolling(MDAYS, min_periods=WDAYS).max()
    p2 = m.shift(21).rolling(MDAYS, min_periods=WDAYS).max()
    p3 = m.rolling(MDAYS, min_periods=WDAYS).max()
    return ((p1 > p2) & (p2 > p3) & (p1 > 0)).astype(float).where(m.notna(), np.nan).diff().diff()

def f27_mcdt_380_macd_post_peak_decay_rate_63_d2(close: pd.Series) -> pd.Series:
    """5d slope of (63d MACD max - current MACD) — rate of decay after recent peak."""
    m, _, _ = _macd(close)
    decay = m.rolling(QDAYS, min_periods=MDAYS).max() - m
    return _rolling_slope(decay, WDAYS).diff().diff()

def f27_mcdt_381_macd_chronic_signal_failure_count_252_d2(close: pd.Series) -> pd.Series:
    """Annual count of bullish MACD/signal crosses that failed within 10 bars — chronic-failure count."""
    m, s, _ = _macd(close)
    d = m - s
    bu = ((d.shift(1) <= 0) & (d > 0)).astype(float)
    be = ((d.shift(1) > 0) & (d <= 0)).astype(float)
    bu_10 = bu.shift(10)
    be_in_10 = be.rolling(10, min_periods=1).sum()
    fail = (bu_10 > 0) & (be_in_10 > 0)
    return fail.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(d.notna(), np.nan).diff().diff()

def f27_mcdt_382_macd_blowoff_then_collapse_v2_indicator_d2(close: pd.Series) -> pd.Series:
    """v2: MACD hit 504d max within last 126 bars AND has dropped by > 75% of that peak magnitude."""
    m, _, _ = _macd(close)
    rmax = m.rolling(DDAYS_2Y, min_periods=YDAYS).max()
    bs = _bars_since_true(m == rmax)
    drop = rmax - m > 0.75 * rmax.abs()
    return ((bs <= 126) & drop).astype(float).where(m.notna(), np.nan).diff().diff()

def f27_mcdt_383_macd_failed_recovery_signal_count_63_d2(close: pd.Series) -> pd.Series:
    """Count of histogram sign-flips up that reverted within 10 bars, past 63d — quarterly failed-recovery count."""
    _, _, h = _macd(close)
    up = ((h.shift(1) <= 0) & (h > 0)).astype(float)
    dn = ((h.shift(1) >= 0) & (h < 0)).astype(float)
    up_10 = up.shift(10)
    dn_in_10 = dn.rolling(10, min_periods=1).sum()
    fail = (up_10 > 0) & (dn_in_10 > 0)
    return fail.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(h.notna(), np.nan).diff().diff()

def f27_mcdt_384_macd_capitulation_after_persistence_indicator_d2(close: pd.Series) -> pd.Series:
    """1 if MACD > 0 for >= 100 of past 252 bars AND MACD just crossed below its 252d 5th-percentile."""
    m, _, _ = _macd(close)
    persist = (m > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum() >= 100
    q5 = m.rolling(YDAYS, min_periods=QDAYS).quantile(0.05)
    capit = (m.shift(1) >= q5) & (m < q5)
    return (persist & capit).astype(float).where(m.notna() & q5.notna(), np.nan).diff().diff()

def f27_mcdt_385_macd_distribution_zone_indicator_63_d2(close: pd.Series) -> pd.Series:
    """1 if MACD dwelling near zero (|MACD| < 0.5 * 21d std of MACD) AND 21d max of MACD declining over 63d."""
    m, _, _ = _macd(close)
    sd = m.rolling(MDAYS, min_periods=WDAYS).std()
    near_zero = m.abs() < 0.5 * sd
    rmax21 = m.rolling(MDAYS, min_periods=WDAYS).max()
    declining = rmax21 < rmax21.shift(QDAYS)
    return (near_zero & declining).astype(float).where(m.notna() & sd.notna(), np.nan).diff().diff()

def f27_mcdt_386_macd_recovery_failure_to_q90_252_count_d2(close: pd.Series) -> pd.Series:
    """Count in past 252d of bars where MACD crossed above own 252d q50 but failed to reach own q90 within 21 bars."""
    m, _, _ = _macd(close)
    q50 = m.rolling(YDAYS, min_periods=QDAYS).quantile(0.5)
    q90 = m.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    up = ((m.shift(1) <= q50.shift(1)) & (m > q50)).astype(float)
    up_21 = up.shift(MDAYS)
    reached = (m >= q90).astype(float).rolling(MDAYS, min_periods=1).sum()
    fail = (up_21 > 0) & (reached <= 0)
    return fail.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(m.notna(), np.nan).diff().diff()

def f27_mcdt_387_macd_lower_high_in_histogram_streak_63_d2(close: pd.Series) -> pd.Series:
    """Longest streak of consecutive bars where 5d histo-max < 5d histo-max from 5 bars ago, past 63d."""
    _, _, h = _macd(close)
    rmax = h.rolling(WDAYS, min_periods=2).max()
    lh = rmax < rmax.shift(WDAYS)
    streak = _streak_true(lh)
    return streak.rolling(QDAYS, min_periods=MDAYS).max().where(h.notna(), np.nan).diff().diff()

def f27_mcdt_388_macd_lower_low_in_histogram_streak_63_d2(close: pd.Series) -> pd.Series:
    """Longest streak where 5d histo-min < 5d histo-min from 5 bars ago, past 63d — lower-low cascade."""
    _, _, h = _macd(close)
    rmin = h.rolling(WDAYS, min_periods=2).min()
    ll = rmin < rmin.shift(WDAYS)
    streak = _streak_true(ll)
    return streak.rolling(QDAYS, min_periods=MDAYS).max().where(h.notna(), np.nan).diff().diff()

def f27_mcdt_389_macd_post_252h_decay_velocity_63_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """5d slope of MACD during the 63d window following the most recent 252d high — post-peak velocity."""
    m, _, _ = _macd(close)
    at_252h = high == high.rolling(YDAYS, min_periods=QDAYS).max()
    bs = _bars_since_true(at_252h)
    within_63 = bs <= QDAYS
    sl = _rolling_slope(m, WDAYS)
    return sl.where(within_63, np.nan).diff().diff()

def f27_mcdt_390_macd_post_252h_below_zero_persistence_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of bars in past 63 with MACD<0, conditioned on a 252d-high having occurred in past 126d."""
    m, _, _ = _macd(close)
    at_252h = high == high.rolling(YDAYS, min_periods=QDAYS).max()
    recent_peak = at_252h.rolling(126, min_periods=MDAYS).sum() > 0
    frac_neg = (m < 0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()
    return frac_neg.where(recent_peak, np.nan).diff().diff()

def f27_mcdt_391_macd_chronic_negative_persistence_252_d2(close: pd.Series) -> pd.Series:
    """Fraction of past 252 bars with MACD<0 — chronic-bearish persistence."""
    m, _, _ = _macd(close)
    return (m < 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(m.notna(), np.nan).diff().diff()

def f27_mcdt_392_macd_long_negative_run_with_price_below_sma200_indicator_d2(close: pd.Series) -> pd.Series:
    """1 if MACD<0 for >= 40 of past 63 bars AND close < SMA200 — sustained-weakness state."""
    m, _, _ = _macd(close)
    sma = close.rolling(200, min_periods=50).mean()
    neg = (m < 0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum() >= 40
    return (neg & (close < sma)).astype(float).where(m.notna() & sma.notna(), np.nan).diff().diff()

def f27_mcdt_393_macd_failed_breakout_pattern_count_252_d2(close: pd.Series) -> pd.Series:
    """Annual count of MACD-line breakouts (cross above own 21d max) that reverted (below own 21d min) within 21 bars."""
    m, _, _ = _macd(close)
    rmax21 = m.rolling(MDAYS, min_periods=WDAYS).max().shift(1)
    rmin21 = m.rolling(MDAYS, min_periods=WDAYS).min().shift(1)
    brk = ((m > rmax21) & (m.shift(1) <= rmax21)).astype(float)
    revert = (m < rmin21).astype(float)
    brk_21 = brk.shift(MDAYS)
    revert_in_21 = revert.rolling(MDAYS, min_periods=1).sum()
    fail = (brk_21 > 0) & (revert_in_21 > 0)
    return fail.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(m.notna(), np.nan).diff().diff()

def f27_mcdt_394_macd_terminal_breakdown_signature_v3_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """v3: MACD<0 AND 21d slope<0 AND 252d-high in past 126d AND histo<0 for >40 of past 63 — terminal pattern."""
    m, _, h = _macd(close)
    sl = _rolling_slope(m, MDAYS)
    at_252h = high == high.rolling(YDAYS, min_periods=QDAYS).max()
    recent_peak = at_252h.rolling(126, min_periods=MDAYS).sum() > 0
    histo_neg = (h < 0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum() > 40
    return ((m < 0) & (sl < 0) & recent_peak & histo_neg).astype(float).where(m.notna() & sl.notna(), np.nan).diff().diff()

def f27_mcdt_395_macd_chronic_weakness_score_252_d2(close: pd.Series) -> pd.Series:
    """Composite chronic-weakness score: fraction MACD<0 (252d) + fraction histo<0 (252d) + bars-since-MACD-252-max/252."""
    m, _, h = _macd(close)
    f1 = (m < 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    f2 = (h < 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    bs = _bars_since_true(m == m.rolling(YDAYS, min_periods=QDAYS).max())
    f3 = (bs / float(YDAYS)).clip(0, 1)
    return (f1.fillna(0) + f2.fillna(0) + f3.fillna(0)).where(m.notna(), np.nan).diff().diff()

def f27_mcdt_396_macd_sample_entropy_21_d2(close: pd.Series) -> pd.Series:
    """21d Sample Entropy of MACD (m=2, r=0.2*std)."""
    m, _, _ = _macd(close)
    return m.rolling(MDAYS, min_periods=WDAYS).apply(_sample_entropy_window, raw=True).diff().diff()

def f27_mcdt_397_macd_sample_entropy_63_d2(close: pd.Series) -> pd.Series:
    """63d Sample Entropy of MACD."""
    m, _, _ = _macd(close)
    return m.rolling(QDAYS, min_periods=MDAYS).apply(_sample_entropy_window, raw=True).diff().diff()

def f27_mcdt_398_macd_approximate_entropy_21_d2(close: pd.Series) -> pd.Series:
    """21d Approximate Entropy of MACD (m=2, r=0.2*std)."""
    m, _, _ = _macd(close)
    return m.rolling(MDAYS, min_periods=WDAYS).apply(_approx_entropy_window, raw=True).diff().diff()

def f27_mcdt_399_macd_permutation_entropy_21_order3_d2(close: pd.Series) -> pd.Series:
    """21d Permutation Entropy of MACD (order=3)."""
    m, _, _ = _macd(close)
    return m.rolling(MDAYS, min_periods=WDAYS).apply(_perm_entropy_window, raw=True).diff().diff()

def f27_mcdt_400_macd_permutation_entropy_63_order3_d2(close: pd.Series) -> pd.Series:
    """63d Permutation Entropy of MACD (order=3)."""
    m, _, _ = _macd(close)
    return m.rolling(QDAYS, min_periods=MDAYS).apply(_perm_entropy_window, raw=True).diff().diff()

def f27_mcdt_401_macd_multiscale_entropy_scale2_d2(close: pd.Series) -> pd.Series:
    """Multi-scale (scale=2) sample entropy of MACD over 63d."""
    m, _, _ = _macd(close)
    return m.rolling(QDAYS, min_periods=MDAYS).apply(_multiscale_entropy_window, raw=True).diff().diff()

def f27_mcdt_402_macd_multiscale_entropy_scale5_d2(close: pd.Series) -> pd.Series:
    """Multi-scale (scale=5) sample entropy of MACD over 126d."""
    m, _, _ = _macd(close)

    def _fn(w):
        return _multiscale_entropy_window(w, scale=5)
    return m.rolling(126, min_periods=QDAYS).apply(_fn, raw=True).diff().diff()

def f27_mcdt_403_macd_fractal_dimension_higuchi_63_d2(close: pd.Series) -> pd.Series:
    """63d Higuchi fractal dimension of MACD."""
    m, _, _ = _macd(close)
    return m.rolling(QDAYS, min_periods=MDAYS).apply(_higuchi_fd_window, raw=True).diff().diff()

def f27_mcdt_404_macd_fractal_dimension_petrosian_21_d2(close: pd.Series) -> pd.Series:
    """21d Petrosian fractal dimension of MACD."""
    m, _, _ = _macd(close)
    return m.rolling(MDAYS, min_periods=WDAYS).apply(_petrosian_fd_window, raw=True).diff().diff()

def f27_mcdt_405_macd_hurst_rs_63_d2(close: pd.Series) -> pd.Series:
    """63d R/S Hurst exponent of MACD."""
    m, _, _ = _macd(close)
    return m.rolling(QDAYS, min_periods=MDAYS).apply(_hurst_rs_window, raw=True).diff().diff()

def f27_mcdt_406_macd_hurst_dfa_252_d2(close: pd.Series) -> pd.Series:
    """252d DFA Hurst exponent of MACD."""
    m, _, _ = _macd(close)
    return m.rolling(YDAYS, min_periods=QDAYS).apply(_hurst_dfa_window, raw=True).diff().diff()

def f27_mcdt_407_macd_recurrence_rate_21_d2(close: pd.Series) -> pd.Series:
    """21d recurrence rate of MACD."""
    m, _, _ = _macd(close)
    return m.rolling(MDAYS, min_periods=WDAYS).apply(_recurrence_rate_window, raw=True).diff().diff()

def f27_mcdt_408_macd_recurrence_determinism_21_d2(close: pd.Series) -> pd.Series:
    """21d recurrence-determinism of MACD."""
    m, _, _ = _macd(close)
    return m.rolling(MDAYS, min_periods=WDAYS).apply(_recurrence_determinism_window, raw=True).diff().diff()

def f27_mcdt_409_macd_lempel_ziv_complexity_63_d2(close: pd.Series) -> pd.Series:
    """63d Lempel-Ziv complexity of MACD binarized at median."""
    m, _, _ = _macd(close)
    return m.rolling(QDAYS, min_periods=MDAYS).apply(_lz_complexity_window, raw=True).diff().diff()

def f27_mcdt_410_macd_kolmogorov_complexity_proxy_63_d2(close: pd.Series) -> pd.Series:
    """63d Kolmogorov-complexity proxy (zlib compression ratio of binarized MACD)."""
    m, _, _ = _macd(close)
    return m.rolling(QDAYS, min_periods=MDAYS).apply(_kolmogorov_proxy_window, raw=True).diff().diff()

def f27_mcdt_411_macd_predictability_horizon_63_d2(close: pd.Series) -> pd.Series:
    """Horizon (lag) at which 63d autocorr of MACD drops below 0.2."""
    m, _, _ = _macd(close)
    return m.rolling(QDAYS, min_periods=MDAYS).apply(_predictability_horizon_window, raw=True).diff().diff()

def f27_mcdt_412_macd_information_dimension_63_d2(close: pd.Series) -> pd.Series:
    """63d Information-dimension proxy of MACD."""
    m, _, _ = _macd(close)
    return m.rolling(QDAYS, min_periods=MDAYS).apply(_info_dim_window, raw=True).diff().diff()

def f27_mcdt_413_macd_correlation_dimension_proxy_63_d2(close: pd.Series) -> pd.Series:
    """63d Correlation-dimension proxy of MACD."""
    m, _, _ = _macd(close)
    return m.rolling(QDAYS, min_periods=MDAYS).apply(_corr_dim_window, raw=True).diff().diff()

def f27_mcdt_414_macd_lyapunov_proxy_63_d2(close: pd.Series) -> pd.Series:
    """63d Lyapunov-exponent proxy of MACD (mean log|diff|)."""
    m, _, _ = _macd(close)
    return m.rolling(QDAYS, min_periods=MDAYS).apply(_lyapunov_proxy_window, raw=True).diff().diff()

def f27_mcdt_415_macd_persistence_index_rs_21_d2(close: pd.Series) -> pd.Series:
    """21d persistence index = R/S Hurst - 0.5 of MACD."""
    m, _, _ = _macd(close)
    return m.rolling(MDAYS, min_periods=WDAYS).apply(_persistence_rs_window, raw=True).diff().diff()

def f27_mcdt_416_macd_universe_with_volume_confirmed_count_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of MACD configs {fast, classical, slow, long} with vol-confirmed bearish cross in past 21d
    (vol>1.3x 50d avg)."""
    cnt = pd.Series(0.0, index=close.index)
    va = volume.rolling(50, min_periods=10).mean().shift(1)
    for f, sl, sg in _BFSS:
        mm, ss, _ = _macd(close, f, sl, sg)
        dd = mm - ss
        cross = (dd.shift(1) > 0) & (dd <= 0) & (volume > 1.3 * va)
        cnt = cnt + (cross.rolling(MDAYS, min_periods=1).sum() > 0).astype(float).fillna(0)
    return cnt.where(close.notna(), np.nan).diff().diff()

def f27_mcdt_417_macd_universe_failure_breadth_at_top_score_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """At bars where high = 252d max: count of MACD configs in basket where bullish cross failed within 21d (past 63)."""
    cnt = pd.Series(0.0, index=close.index)
    for f, sl, sg in _BFSS:
        mm, ss, _ = _macd(close, f, sl, sg)
        dd = mm - ss
        bu = ((dd.shift(1) <= 0) & (dd > 0)).astype(float)
        be = ((dd.shift(1) > 0) & (dd <= 0)).astype(float)
        bu21 = bu.shift(MDAYS)
        be_in21 = be.rolling(MDAYS, min_periods=1).sum()
        fail = ((bu21 > 0) & (be_in21 > 0)).astype(float)
        cnt = cnt + (fail.rolling(QDAYS, min_periods=MDAYS).sum() > 0).astype(float).fillna(0)
    at_max = high == high.rolling(YDAYS, min_periods=QDAYS).max()
    return cnt.where(at_max, np.nan).diff().diff()

def f27_mcdt_418_macd_universe_decay_velocity_post_peak_d2(close: pd.Series) -> pd.Series:
    """Average 5d slope of (63d max - current MACD) across basket — basket decay velocity."""
    slopes = []
    for f, sl in _BFS:
        mm = _ema(close, f) - _ema(close, sl)
        decay = mm.rolling(QDAYS, min_periods=MDAYS).max() - mm
        slopes.append(_rolling_slope(decay, WDAYS))
    return (sum(slopes) / float(len(slopes))).diff().diff()

def f27_mcdt_419_macd_universe_chronic_weakness_score_252_d2(close: pd.Series) -> pd.Series:
    """Average fraction of past 252d with MACD<0 across basket configs."""
    parts = []
    for f, sl in _BFS:
        mm = _ema(close, f) - _ema(close, sl)
        parts.append((mm < 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean())
    return (sum(parts) / float(len(parts))).diff().diff()

def f27_mcdt_420_macd_universe_post_breakdown_recovery_failure_count_d2(close: pd.Series) -> pd.Series:
    """Sum across basket of recovery-failure counts (cross above 0 then below within 21) past 63."""
    parts = pd.Series(0.0, index=close.index)
    for f, sl in _BFS:
        mm = _ema(close, f) - _ema(close, sl)
        up = ((mm.shift(1) <= 0) & (mm > 0)).astype(float)
        dn = ((mm.shift(1) >= 0) & (mm < 0)).astype(float)
        u21 = up.shift(MDAYS)
        d_in_21 = dn.rolling(MDAYS, min_periods=1).sum()
        fail = ((u21 > 0) & (d_in_21 > 0)).astype(float)
        parts = parts + fail.rolling(QDAYS, min_periods=MDAYS).sum().fillna(0)
    return parts.where(close.notna(), np.nan).diff().diff()

def f27_mcdt_421_macd_universe_distribution_signal_aggregate_d2(close: pd.Series) -> pd.Series:
    """Sum of (MACD dwelling near zero & 21d-max declining over 63d) across basket configs."""
    parts = pd.Series(0.0, index=close.index)
    for f, sl in _BFS:
        mm = _ema(close, f) - _ema(close, sl)
        sd = mm.rolling(MDAYS, min_periods=WDAYS).std()
        near = mm.abs() < 0.5 * sd
        rmax21 = mm.rolling(MDAYS, min_periods=WDAYS).max()
        decl = rmax21 < rmax21.shift(QDAYS)
        parts = parts + (near & decl).astype(float).fillna(0)
    return parts.where(close.notna(), np.nan).diff().diff()

def f27_mcdt_422_macd_universe_blowoff_collapse_indicator_d2(close: pd.Series) -> pd.Series:
    """Count of basket configs in blowoff-collapse state (252d max within 63d AND >50% drop)."""
    return _basket_blowoff_count(close).where(close.notna(), np.nan).diff().diff()

def f27_mcdt_423_macd_universe_terminal_pattern_aggregate_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """Sum across basket of terminal-pattern: MACD<0 AND 21d slope<0 AND 252h in past 126d."""
    parts = pd.Series(0.0, index=close.index)
    at_252h = high == high.rolling(YDAYS, min_periods=QDAYS).max()
    recent = at_252h.rolling(126, min_periods=MDAYS).sum() > 0
    for f, sl in _BFS:
        mm = _ema(close, f) - _ema(close, sl)
        sl_m = _rolling_slope(mm, MDAYS)
        parts = parts + ((mm < 0) & (sl_m < 0) & recent).astype(float).fillna(0)
    return parts.where(close.notna(), np.nan).diff().diff()

def f27_mcdt_424_macd_universe_extreme_z_score_max_252_d2(close: pd.Series) -> pd.Series:
    """Max 252d z-score across basket configs — peak extension across cycles."""
    zs = []
    for f, sl in _BFS:
        mm = _ema(close, f) - _ema(close, sl)
        zs.append(_rolling_zscore(mm, YDAYS, min_periods=QDAYS))
    return pd.concat([zs[i].rename(i) for i in range(len(zs))], axis=1).max(axis=1).diff().diff()

def f27_mcdt_425_macd_universe_z_score_range_63_d2(close: pd.Series) -> pd.Series:
    """Range (max - min) of 63d z-scores across basket — cycle disagreement intensity."""
    zs = []
    for f, sl in _BFS:
        mm = _ema(close, f) - _ema(close, sl)
        zs.append(_rolling_zscore(mm, QDAYS, min_periods=MDAYS))
    df = pd.concat([zs[i].rename(i) for i in range(len(zs))], axis=1)
    return (df.max(axis=1) - df.min(axis=1)).diff().diff()

def f27_mcdt_426_macd_universe_correlation_breakdown_zscore_252_d2(close: pd.Series) -> pd.Series:
    """252d z-score of average pairwise 63d correlation among basket — corr-breakdown z."""
    f1 = _ema(close, 5) - _ema(close, 35)
    f2 = _ema(close, 12) - _ema(close, 26)
    f3 = _ema(close, 19) - _ema(close, 39)
    f4 = _ema(close, 50) - _ema(close, 200)
    pairs = [f1.rolling(QDAYS, min_periods=MDAYS).corr(f2), f1.rolling(QDAYS, min_periods=MDAYS).corr(f3), f1.rolling(QDAYS, min_periods=MDAYS).corr(f4), f2.rolling(QDAYS, min_periods=MDAYS).corr(f3), f2.rolling(QDAYS, min_periods=MDAYS).corr(f4), f3.rolling(QDAYS, min_periods=MDAYS).corr(f4)]
    avg = sum(pairs) / float(len(pairs))
    return _rolling_zscore(avg, YDAYS, min_periods=QDAYS).diff().diff()

def f27_mcdt_427_macd_universe_extreme_event_clustering_index_63_d2(close: pd.Series) -> pd.Series:
    """Sum across basket of count(extreme-z>2 events) in past 63d divided by 63 — clustering rate."""
    parts = pd.Series(0.0, index=close.index)
    for f, sl in _BFS:
        mm = _ema(close, f) - _ema(close, sl)
        z = _rolling_zscore(mm, YDAYS, min_periods=QDAYS)
        ev = (z.abs() > 2).astype(float)
        parts = parts + ev.rolling(QDAYS, min_periods=MDAYS).sum().fillna(0)
    return (parts / (4.0 * float(QDAYS))).where(close.notna(), np.nan).diff().diff()

def f27_mcdt_428_macd_universe_recall_optimized_score_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """Recall-optimized: sum of ANY-of-many topping signals (bearish cross, div, MACD<0, slope<0,
    histo<0, basket blowoff-collapse, low-q breach) — designed for high recall."""
    m, s, h = _macd(close)
    d = m - s
    cross = ((d.shift(1) > 0) & (d <= 0)).astype(float).rolling(MDAYS, min_periods=1).sum() > 0
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    prior_max = m.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    div = (p_new & (m < prior_max)).astype(float).rolling(MDAYS, min_periods=1).sum() > 0
    macd_neg = m < 0
    sl = _rolling_slope(m, MDAYS)
    sl_neg = sl < 0
    histo_neg = h < 0
    bo_cnt = _basket_blowoff_count(close)
    bo = bo_cnt >= 1
    q05 = m.rolling(YDAYS, min_periods=QDAYS).quantile(0.05)
    q_breach = m < q05
    return (cross.astype(float).fillna(0) + div.astype(float).fillna(0) + macd_neg.astype(float).fillna(0) + sl_neg.astype(float).fillna(0) + histo_neg.astype(float).fillna(0) + bo.astype(float).fillna(0) + q_breach.astype(float).fillna(0)).where(m.notna(), np.nan).diff().diff()

def f27_mcdt_429_macd_universe_precision_optimized_score_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """Precision-optimized: 1 only when ALL of {bearish cross, div, MACD<0, slope<0, basket blowoff>=2}."""
    m, s, _ = _macd(close)
    d = m - s
    cross = ((d.shift(1) > 0) & (d <= 0)).astype(float).rolling(MDAYS, min_periods=1).sum() > 0
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    prior_max = m.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    div = (p_new & (m < prior_max)).astype(float).rolling(MDAYS, min_periods=1).sum() > 0
    macd_neg = m < 0
    sl = _rolling_slope(m, MDAYS)
    sl_neg = sl < 0
    bo = _basket_blowoff_count(close) >= 2
    return (cross & div & macd_neg & sl_neg & bo).astype(float).where(m.notna() & sl.notna(), np.nan).diff().diff()

def f27_mcdt_430_macd_terminal_distribution_score_v3_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """At close=252d max: sum of {chronic-weakness (50%>0 past 252), 21d slope<0, basket blowoff>=2, histo
    declining 21d-max over 63d, 252d z-score>1.5}."""
    m, _, h = _macd(close)
    at_max = close == close.rolling(YDAYS, min_periods=QDAYS).max()
    a = ((m > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean() > 0.5).astype(float).fillna(0)
    sl = _rolling_slope(m, MDAYS)
    b = (sl < 0).astype(float).fillna(0)
    c = (_basket_blowoff_count(close) >= 2).astype(float).fillna(0)
    rmax21h = h.rolling(MDAYS, min_periods=WDAYS).max()
    d = (rmax21h < rmax21h.shift(QDAYS)).astype(float).fillna(0)
    z = _rolling_zscore(m, YDAYS, min_periods=QDAYS)
    e = (z > 1.5).astype(float).fillna(0)
    return (a + b + c + d + e).where(at_max, np.nan).diff().diff()

def f27_mcdt_431_macd_universe_orthogonal_signal_aggregate_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Aggregate of orthogonal MACD signals: line, histo, divergence, volume-confirmed, basket-vol-corr."""
    m, _, h = _macd(close)
    a = (m < 0).astype(float).fillna(0)
    b = (h < 0).astype(float).fillna(0)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    prior_max = m.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    c = (p_new & (m < prior_max)).astype(float).fillna(0)
    s = _ema(m, 9)
    d_g = m - s
    cross = (d_g.shift(1) > 0) & (d_g <= 0)
    va = volume.rolling(50, min_periods=10).mean().shift(1)
    d = (cross & (volume > 1.3 * va)).astype(float).rolling(MDAYS, min_periods=1).sum() > 0
    ac = m.rolling(QDAYS, min_periods=MDAYS).corr(m.shift(MDAYS))
    e = (ac < 0.2).astype(float).fillna(0)
    return (a + b + c + d.astype(float).fillna(0) + e).where(m.notna(), np.nan).diff().diff()

def f27_mcdt_432_multi_macd_consensus_topping_at_252h_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """At close=252d max: count of basket configs with bearish cross in past 21 + bearish div in past 63."""
    parts = pd.Series(0.0, index=close.index)
    at_max = close == close.rolling(YDAYS, min_periods=QDAYS).max()
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    for f, sl in _BFS:
        mm = _ema(close, f) - _ema(close, sl)
        ss = _ema(mm, 9)
        dd = mm - ss
        cross = ((dd.shift(1) > 0) & (dd <= 0)).astype(float).rolling(MDAYS, min_periods=1).sum() > 0
        prior_max = mm.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
        div = (p_new & (mm < prior_max)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum() > 0
        parts = parts + cross.astype(float).fillna(0) + div.astype(float).fillna(0)
    return parts.where(at_max, np.nan).diff().diff()

def f27_mcdt_433_macd_basket_chronic_failure_count_252_d2(close: pd.Series) -> pd.Series:
    """Sum across basket of chronic-failure counts (bullish cross failed in 10 bars), past 252."""
    parts = pd.Series(0.0, index=close.index)
    for f, sl in _BFS:
        mm = _ema(close, f) - _ema(close, sl)
        ss = _ema(mm, 9)
        dd = mm - ss
        bu = ((dd.shift(1) <= 0) & (dd > 0)).astype(float)
        be = ((dd.shift(1) > 0) & (dd <= 0)).astype(float)
        b10 = bu.shift(10)
        e10 = be.rolling(10, min_periods=1).sum()
        fail = ((b10 > 0) & (e10 > 0)).astype(float)
        parts = parts + fail.rolling(YDAYS, min_periods=QDAYS).sum().fillna(0)
    return parts.where(close.notna(), np.nan).diff().diff()

def f27_mcdt_434_macd_topping_intensity_score_extended_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """Extended topping-intensity score: sum of {bearish cross in 21d, div in 63d, MACD<0, slope<0,
    histo<0, basket blowoff>=2, basket div>=2, MACD pct-rank>0.95, chronic-neg>0.5}."""
    m, s, h = _macd(close)
    d = m - s
    a = (((d.shift(1) > 0) & (d <= 0)).astype(float).rolling(MDAYS, min_periods=1).sum() > 0).astype(float).fillna(0)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    prior_max = m.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    b = ((p_new & (m < prior_max)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum() > 0).astype(float).fillna(0)
    c = (m < 0).astype(float).fillna(0)
    sl = _rolling_slope(m, MDAYS)
    d_part = (sl < 0).astype(float).fillna(0)
    e = (h < 0).astype(float).fillna(0)
    f_b = (_basket_blowoff_count(close) >= 2).astype(float).fillna(0)
    g_b = (_basket_div_count(high, close) >= 2).astype(float).fillna(0)
    pr = m.rolling(YDAYS, min_periods=QDAYS).apply(_pct_rank_window, raw=True)
    h_b = (pr > 0.95).astype(float).fillna(0)
    chronic = (m < 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    i_b = (chronic > 0.5).astype(float).fillna(0)
    return (a + b + c + d_part + e + f_b + g_b + h_b + i_b).where(m.notna(), np.nan).diff().diff()

def f27_mcdt_435_macd_blowoff_then_decay_velocity_universe_d2(close: pd.Series) -> pd.Series:
    """For each basket config in blowoff (252d max in 63d), compute decay velocity; sum across."""
    total = pd.Series(0.0, index=close.index)
    for f, sl in _BFS:
        mm = _ema(close, f) - _ema(close, sl)
        rmax = mm.rolling(YDAYS, min_periods=QDAYS).max()
        bs = _bars_since_true(mm == rmax)
        in_window = bs <= QDAYS
        decay = (rmax - mm).where(in_window, np.nan)
        vel = _rolling_slope(decay, WDAYS)
        total = total + vel.fillna(0)
    return total.where(close.notna(), np.nan).diff().diff()

def f27_mcdt_436_macd_universe_alignment_score_extended_d2(close: pd.Series) -> pd.Series:
    """Extended alignment: count of basket configs with sign(MACD)<0 + count with histo<0 + count with slope<0."""
    parts = pd.Series(0.0, index=close.index)
    for f, sl in _BFS:
        mm = _ema(close, f) - _ema(close, sl)
        ss = _ema(mm, 9)
        hh = mm - ss
        sl_m = _rolling_slope(mm, MDAYS)
        parts = parts + (mm < 0).astype(float).fillna(0) + (hh < 0).astype(float).fillna(0) + (sl_m < 0).astype(float).fillna(0)
    return parts.where(close.notna(), np.nan).diff().diff()

def f27_mcdt_437_macd_universe_persistence_after_extreme_252_d2(close: pd.Series) -> pd.Series:
    """Sum across basket of (fraction of past 63 with MACD<0 GIVEN had MACD-z>2 in past 252)."""
    parts = pd.Series(0.0, index=close.index)
    for f, sl in _BFS:
        mm = _ema(close, f) - _ema(close, sl)
        z = _rolling_zscore(mm, YDAYS, min_periods=QDAYS)
        had_extreme = (z > 2).astype(float).rolling(YDAYS, min_periods=QDAYS).sum() > 0
        frac_neg = (mm < 0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()
        parts = parts + frac_neg.where(had_extreme, 0).fillna(0)
    return parts.where(close.notna(), np.nan).diff().diff()

def f27_mcdt_438_macd_universe_lower_high_breadth_count_63_d2(close: pd.Series) -> pd.Series:
    """Count of basket configs where 21d MACD-max < prior 21d MACD-max, past 63 bars (current snapshot)."""
    parts = pd.Series(0.0, index=close.index)
    for f, sl in _BFS:
        mm = _ema(close, f) - _ema(close, sl)
        rmax = mm.rolling(MDAYS, min_periods=WDAYS).max()
        lh = rmax < rmax.shift(MDAYS)
        parts = parts + lh.astype(float).fillna(0)
    return parts.where(close.notna(), np.nan).diff().diff()

def f27_mcdt_439_macd_universe_failure_signal_density_63_d2(close: pd.Series) -> pd.Series:
    """Sum across basket of bullish-cross-failure events / 63 over past 63 — failure density."""
    parts = pd.Series(0.0, index=close.index)
    for f, sl in _BFS:
        mm = _ema(close, f) - _ema(close, sl)
        ss = _ema(mm, 9)
        dd = mm - ss
        bu = ((dd.shift(1) <= 0) & (dd > 0)).astype(float)
        be = ((dd.shift(1) > 0) & (dd <= 0)).astype(float)
        b21 = bu.shift(MDAYS)
        e21 = be.rolling(MDAYS, min_periods=1).sum()
        fail = ((b21 > 0) & (e21 > 0)).astype(float)
        parts = parts + fail.rolling(QDAYS, min_periods=MDAYS).sum().fillna(0) / float(QDAYS)
    return parts.where(close.notna(), np.nan).diff().diff()

def f27_mcdt_440_macd_universe_breakdown_confirmation_count_d2(close: pd.Series) -> pd.Series:
    """Count of basket configs with sustained breakdown: MACD < 0 for >= 40 of past 63 AND close < SMA(slow)."""
    parts = pd.Series(0.0, index=close.index)
    for f, sl in _BFS:
        mm = _ema(close, f) - _ema(close, sl)
        sma_slow = close.rolling(sl, min_periods=max(sl // 3, 5)).mean()
        cond = ((mm < 0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum() >= 40) & (close < sma_slow)
        parts = parts + cond.astype(float).fillna(0)
    return parts.where(close.notna(), np.nan).diff().diff()

def f27_mcdt_441_macd_stuck_probability_proxy_252_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """Stuck-probability proxy: weighted sum of {chronic-neg-frac, recovery-failure-count/252,
    bars-since-252max/252, basket-decay-velocity-rank, distribution-shift-z}, normalized 0-1."""
    m, _, _ = _macd(close)
    chronic = (m < 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().fillna(0)
    up = ((m.shift(1) <= 0) & (m > 0)).astype(float)
    dn = ((m.shift(1) >= 0) & (m < 0)).astype(float)
    u21 = up.shift(MDAYS)
    d_in_21 = dn.rolling(MDAYS, min_periods=1).sum()
    fail = ((u21 > 0) & (d_in_21 > 0)).astype(float)
    rec_fail = (fail.rolling(YDAYS, min_periods=QDAYS).sum() / float(YDAYS)).fillna(0)
    bs = _bars_since_true(m == m.rolling(YDAYS, min_periods=QDAYS).max())
    bs_norm = (bs / float(YDAYS)).clip(0, 1).fillna(0)
    rec_mean = m.rolling(QDAYS, min_periods=MDAYS).mean()
    pr_mean = m.shift(QDAYS).rolling(189, min_periods=QDAYS).mean()
    sd252 = m.rolling(YDAYS, min_periods=QDAYS).std()
    dsh = _safe_div(rec_mean - pr_mean, sd252).clip(-3, 3).fillna(0)
    dsh_n = (-dsh + 3.0) / 6.0
    raw = 0.35 * chronic + 0.25 * rec_fail + 0.2 * bs_norm + 0.2 * dsh_n
    return raw.where(m.notna(), np.nan).diff().diff()

def f27_mcdt_442_macd_topping_aggregate_orthogonal_v3_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Orthogonal v3: count of orthogonal-family triggers active {value-line, histo, divergence,
    volume-confirmed cross, basket decay, regime overdue, entropy-low}."""
    m, s, h = _macd(close)
    a = (m < 0).astype(float).fillna(0)
    b = (h < 0).astype(float).fillna(0)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    prior_max = m.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    c = ((p_new & (m < prior_max)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum() > 0).astype(float).fillna(0)
    d = m - s
    cross = (d.shift(1) > 0) & (d <= 0)
    va = volume.rolling(50, min_periods=10).mean().shift(1)
    d_part = ((cross & (volume > 1.3 * va)).astype(float).rolling(MDAYS, min_periods=1).sum() > 0).astype(float).fillna(0)
    e = (_basket_blowoff_count(close) >= 2).astype(float).fillna(0)
    f_part = _regime_overdue(close)
    pe = m.rolling(MDAYS, min_periods=WDAYS).apply(_perm_entropy_window, raw=True)
    pe_q = pe.rolling(YDAYS, min_periods=QDAYS).quantile(0.1)
    g = (pe < pe_q).astype(float).fillna(0)
    return (a + b + c + d_part + e + f_part + g).where(m.notna(), np.nan).diff().diff()

def f27_mcdt_443_macd_ml_aggregate_terminal_score_v3_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """Terminal ML-aggregate v3: at high=252d max: sum of weighted {basket-blowoff/4, chronic/100,
    basket-div/4, age-overdue, lower-high-breadth/4}."""
    m, _, _ = _macd(close)
    at_max = high == high.rolling(YDAYS, min_periods=QDAYS).max()
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    bo_cnt = _basket_blowoff_count(close)
    div_cnt = _basket_div_count(high, close)
    lh_cnt = pd.Series(0.0, index=close.index)
    for f, sl_p in _BFS:
        mm = _ema(close, f) - _ema(close, sl_p)
        rmax21 = mm.rolling(MDAYS, min_periods=WDAYS).max()
        lh_cnt = lh_cnt + (rmax21 < rmax21.shift(MDAYS)).astype(float).fillna(0)
    chronic = (m < 0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().fillna(0)
    overdue = _regime_overdue(close)
    score = bo_cnt / 4.0 + chronic / 100.0 + div_cnt / 4.0 + overdue + lh_cnt / 4.0
    return score.where(at_max, np.nan).diff().diff()

def f27_mcdt_444_macd_ml_aggregate_distribution_score_v3_d2(close: pd.Series) -> pd.Series:
    """Distribution ML-aggregate v3: count of {MACD in own-q90 dwell>0.3, histo near-zero dwell>0.3,
    basket lower-high breadth>=2, chronic-neg>0.4, entropy-low signal active}."""
    m, _, h = _macd(close)
    q = m.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    dwell_q90 = (m > q).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()
    a = (dwell_q90 > 0.3).astype(float).fillna(0)
    sd = h.rolling(MDAYS, min_periods=WDAYS).std()
    near = (h.abs() < 0.5 * sd).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()
    b = (near > 0.3).astype(float).fillna(0)
    lh_cnt = pd.Series(0.0, index=close.index)
    for f, sl_p in _BFS:
        mm = _ema(close, f) - _ema(close, sl_p)
        rmax21 = mm.rolling(MDAYS, min_periods=WDAYS).max()
        lh_cnt = lh_cnt + (rmax21 < rmax21.shift(MDAYS)).astype(float).fillna(0)
    c = (lh_cnt >= 2).astype(float).fillna(0)
    chronic = (m < 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    d = (chronic > 0.4).astype(float).fillna(0)
    pe = m.rolling(MDAYS, min_periods=WDAYS).apply(_perm_entropy_window, raw=True)
    pe_q = pe.rolling(YDAYS, min_periods=QDAYS).quantile(0.1)
    e = (pe < pe_q).astype(float).fillna(0)
    return (a + b + c + d + e).where(m.notna(), np.nan).diff().diff()

def f27_mcdt_445_macd_terminal_breakdown_severity_extended_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """Severity: max(0, prior 252d MACD max - current MACD) / |prior 252d max| AND condition on close < SMA200."""
    m, _, _ = _macd(close)
    rmax = m.rolling(YDAYS, min_periods=QDAYS).max()
    sev = _safe_div((rmax - m).clip(lower=0), rmax.abs())
    sma200 = close.rolling(200, min_periods=50).mean()
    cond = close < sma200
    return sev.where(cond, 0.0).diff().diff()

def f27_mcdt_446_macd_chronic_distribution_score_extended_d2(close: pd.Series) -> pd.Series:
    """Extended chronic-distribution: chronic-neg-frac + entropy-low-frac + own-q90-dwell + sign-flip rate."""
    m, _, _ = _macd(close)
    a = (m < 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().fillna(0)
    pe = m.rolling(MDAYS, min_periods=WDAYS).apply(_perm_entropy_window, raw=True)
    pe_q = pe.rolling(YDAYS, min_periods=QDAYS).quantile(0.1)
    b = (pe < pe_q).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().fillna(0)
    q = m.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    c = (m > q).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().fillna(0)
    flip = (np.sign(m) != np.sign(m.shift(1))).astype(float)
    d = flip.rolling(YDAYS, min_periods=QDAYS).mean().fillna(0)
    return (a + b + c + d).where(m.notna(), np.nan).diff().diff()

def f27_mcdt_447_macd_failure_to_recover_aggregate_extended_d2(close: pd.Series) -> pd.Series:
    """Extended failure-to-recover: counts of {bullish cross failed in 21d, MACD-up-zero failed in 21d,
    histo-up-zero failed in 21d, breakout-of-21-max failed in 21d} past 252."""
    m, s, h = _macd(close)
    d = m - s
    bu = ((d.shift(1) <= 0) & (d > 0)).astype(float)
    be = ((d.shift(1) > 0) & (d <= 0)).astype(float)
    f1 = ((bu.shift(MDAYS) > 0) & (be.rolling(MDAYS, min_periods=1).sum() > 0)).astype(float)
    up = ((m.shift(1) <= 0) & (m > 0)).astype(float)
    dn = ((m.shift(1) >= 0) & (m < 0)).astype(float)
    f2 = ((up.shift(MDAYS) > 0) & (dn.rolling(MDAYS, min_periods=1).sum() > 0)).astype(float)
    h_up = ((h.shift(1) <= 0) & (h > 0)).astype(float)
    h_dn = ((h.shift(1) >= 0) & (h < 0)).astype(float)
    f3 = ((h_up.shift(MDAYS) > 0) & (h_dn.rolling(MDAYS, min_periods=1).sum() > 0)).astype(float)
    rmax21 = m.rolling(MDAYS, min_periods=WDAYS).max().shift(1)
    rmin21 = m.rolling(MDAYS, min_periods=WDAYS).min().shift(1)
    brk = ((m > rmax21) & (m.shift(1) <= rmax21)).astype(float)
    revert = (m < rmin21).astype(float)
    f4 = ((brk.shift(MDAYS) > 0) & (revert.rolling(MDAYS, min_periods=1).sum() > 0)).astype(float)
    return (f1.rolling(YDAYS, min_periods=QDAYS).sum().fillna(0) + f2.rolling(YDAYS, min_periods=QDAYS).sum().fillna(0) + f3.rolling(YDAYS, min_periods=QDAYS).sum().fillna(0) + f4.rolling(YDAYS, min_periods=QDAYS).sum().fillna(0)).where(m.notna(), np.nan).diff().diff()

def f27_mcdt_448_macd_universe_blowoff_collapse_master_score_d2(close: pd.Series) -> pd.Series:
    """Master blowoff-collapse: average across basket of (peak magnitude * decay velocity)."""
    parts = []
    for f, sl in _BFS:
        mm = _ema(close, f) - _ema(close, sl)
        rmax = mm.rolling(YDAYS, min_periods=QDAYS).max()
        decay = (rmax - mm) / rmax.abs().replace(0, np.nan)
        vel = _rolling_slope(decay, WDAYS)
        parts.append((decay * vel).fillna(0))
    return (sum(parts) / float(len(parts))).diff().diff()

def f27_mcdt_449_macd_extended_universe_topping_master_v3_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Master extended-topping v3 — aggregate of {orthogonal_v3, terminal-distribution v3 at top,
    chronic-distribution, basket alignment-score, vol-confirmed cross density}, each contributes 0/1."""
    m, s, h = _macd(close)
    a = (m < 0).astype(float).fillna(0)
    b = (h < 0).astype(float).fillna(0)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    prior_max = m.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    c = ((p_new & (m < prior_max)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum() > 0).astype(float).fillna(0)
    d_g = m - s
    cross = (d_g.shift(1) > 0) & (d_g <= 0)
    va = volume.rolling(50, min_periods=10).mean().shift(1)
    dvc = ((cross & (volume > 1.3 * va)).astype(float).rolling(MDAYS, min_periods=1).sum() > 0).astype(float).fillna(0)
    e = (_basket_blowoff_count(close) >= 2).astype(float).fillna(0)
    s1 = (a + b + c + dvc + e >= 4).astype(float)
    chronic = (m < 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().fillna(0)
    q = m.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    dq = (m > q).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().fillna(0)
    s2 = (chronic + dq > 1.0).astype(float)
    align = pd.Series(0.0, index=close.index)
    for f, sl_p in _BFS:
        mm = _ema(close, f) - _ema(close, sl_p)
        ss = _ema(mm, 9)
        hh = mm - ss
        sl_m = _rolling_slope(mm, MDAYS)
        align = align + (mm < 0).astype(float).fillna(0) + (hh < 0).astype(float).fillna(0) + (sl_m < 0).astype(float).fillna(0)
    s3 = (align >= 6).astype(float).fillna(0)
    s4 = ((cross & (volume > 1.3 * va)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum() > 0).astype(float).fillna(0)
    return (s1 + s2 + s3 + s4).where(m.notna(), np.nan).diff().diff()

def f27_mcdt_450_absolute_terminal_macd_indicator_extended_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Absolute-terminal v-extended: 1 only when ALL of {MACD<0, slope<0, histo<0, basket bearish-cross>=3,
    vol-confirmed cross in 21d, regime overdue, basket blowoff>=2, chronic-neg>0.5} are active."""
    m, s, h = _macd(close)
    sl = _rolling_slope(m, MDAYS)
    a = m < 0
    b = sl < 0
    c = h < 0
    cnt = pd.Series(0.0, index=close.index)
    for f, sl_p in _BFS:
        mm = _ema(close, f) - _ema(close, sl_p)
        ss = _ema(mm, 9)
        dd = mm - ss
        cnt = cnt + ((dd.shift(1) > 0) & (dd <= 0)).astype(float).rolling(MDAYS, min_periods=1).sum().fillna(0).clip(0, 1)
    d_part = cnt >= 3
    e = _vol_confirmed_cross_21d(close, volume) > 0
    f_part = _regime_overdue(close) > 0
    g = _basket_blowoff_count(close) >= 2
    chronic = (m < 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    i = chronic > 0.5
    return (a & b & c & d_part & e & f_part & g & i).astype(float).where(m.notna() & sl.notna(), np.nan).diff().diff()
MACD_TOPPING_DYNAMICS_D2_REGISTRY_376_450 = {'f27_mcdt_376_macd_persistent_weakness_while_price_holds_63_d2': {'inputs': ['close'], 'func': f27_mcdt_376_macd_persistent_weakness_while_price_holds_63_d2}, 'f27_mcdt_377_macd_failure_to_recover_above_zero_post_peak_63_d2': {'inputs': ['high', 'close'], 'func': f27_mcdt_377_macd_failure_to_recover_above_zero_post_peak_63_d2}, 'f27_mcdt_378_macd_lower_high_with_histogram_confirmation_63_d2': {'inputs': ['close'], 'func': f27_mcdt_378_macd_lower_high_with_histogram_confirmation_63_d2}, 'f27_mcdt_379_macd_topping_configuration_v2_d2': {'inputs': ['close'], 'func': f27_mcdt_379_macd_topping_configuration_v2_d2}, 'f27_mcdt_380_macd_post_peak_decay_rate_63_d2': {'inputs': ['close'], 'func': f27_mcdt_380_macd_post_peak_decay_rate_63_d2}, 'f27_mcdt_381_macd_chronic_signal_failure_count_252_d2': {'inputs': ['close'], 'func': f27_mcdt_381_macd_chronic_signal_failure_count_252_d2}, 'f27_mcdt_382_macd_blowoff_then_collapse_v2_indicator_d2': {'inputs': ['close'], 'func': f27_mcdt_382_macd_blowoff_then_collapse_v2_indicator_d2}, 'f27_mcdt_383_macd_failed_recovery_signal_count_63_d2': {'inputs': ['close'], 'func': f27_mcdt_383_macd_failed_recovery_signal_count_63_d2}, 'f27_mcdt_384_macd_capitulation_after_persistence_indicator_d2': {'inputs': ['close'], 'func': f27_mcdt_384_macd_capitulation_after_persistence_indicator_d2}, 'f27_mcdt_385_macd_distribution_zone_indicator_63_d2': {'inputs': ['close'], 'func': f27_mcdt_385_macd_distribution_zone_indicator_63_d2}, 'f27_mcdt_386_macd_recovery_failure_to_q90_252_count_d2': {'inputs': ['close'], 'func': f27_mcdt_386_macd_recovery_failure_to_q90_252_count_d2}, 'f27_mcdt_387_macd_lower_high_in_histogram_streak_63_d2': {'inputs': ['close'], 'func': f27_mcdt_387_macd_lower_high_in_histogram_streak_63_d2}, 'f27_mcdt_388_macd_lower_low_in_histogram_streak_63_d2': {'inputs': ['close'], 'func': f27_mcdt_388_macd_lower_low_in_histogram_streak_63_d2}, 'f27_mcdt_389_macd_post_252h_decay_velocity_63_d2': {'inputs': ['high', 'close'], 'func': f27_mcdt_389_macd_post_252h_decay_velocity_63_d2}, 'f27_mcdt_390_macd_post_252h_below_zero_persistence_d2': {'inputs': ['high', 'close'], 'func': f27_mcdt_390_macd_post_252h_below_zero_persistence_d2}, 'f27_mcdt_391_macd_chronic_negative_persistence_252_d2': {'inputs': ['close'], 'func': f27_mcdt_391_macd_chronic_negative_persistence_252_d2}, 'f27_mcdt_392_macd_long_negative_run_with_price_below_sma200_indicator_d2': {'inputs': ['close'], 'func': f27_mcdt_392_macd_long_negative_run_with_price_below_sma200_indicator_d2}, 'f27_mcdt_393_macd_failed_breakout_pattern_count_252_d2': {'inputs': ['close'], 'func': f27_mcdt_393_macd_failed_breakout_pattern_count_252_d2}, 'f27_mcdt_394_macd_terminal_breakdown_signature_v3_d2': {'inputs': ['high', 'close'], 'func': f27_mcdt_394_macd_terminal_breakdown_signature_v3_d2}, 'f27_mcdt_395_macd_chronic_weakness_score_252_d2': {'inputs': ['close'], 'func': f27_mcdt_395_macd_chronic_weakness_score_252_d2}, 'f27_mcdt_396_macd_sample_entropy_21_d2': {'inputs': ['close'], 'func': f27_mcdt_396_macd_sample_entropy_21_d2}, 'f27_mcdt_397_macd_sample_entropy_63_d2': {'inputs': ['close'], 'func': f27_mcdt_397_macd_sample_entropy_63_d2}, 'f27_mcdt_398_macd_approximate_entropy_21_d2': {'inputs': ['close'], 'func': f27_mcdt_398_macd_approximate_entropy_21_d2}, 'f27_mcdt_399_macd_permutation_entropy_21_order3_d2': {'inputs': ['close'], 'func': f27_mcdt_399_macd_permutation_entropy_21_order3_d2}, 'f27_mcdt_400_macd_permutation_entropy_63_order3_d2': {'inputs': ['close'], 'func': f27_mcdt_400_macd_permutation_entropy_63_order3_d2}, 'f27_mcdt_401_macd_multiscale_entropy_scale2_d2': {'inputs': ['close'], 'func': f27_mcdt_401_macd_multiscale_entropy_scale2_d2}, 'f27_mcdt_402_macd_multiscale_entropy_scale5_d2': {'inputs': ['close'], 'func': f27_mcdt_402_macd_multiscale_entropy_scale5_d2}, 'f27_mcdt_403_macd_fractal_dimension_higuchi_63_d2': {'inputs': ['close'], 'func': f27_mcdt_403_macd_fractal_dimension_higuchi_63_d2}, 'f27_mcdt_404_macd_fractal_dimension_petrosian_21_d2': {'inputs': ['close'], 'func': f27_mcdt_404_macd_fractal_dimension_petrosian_21_d2}, 'f27_mcdt_405_macd_hurst_rs_63_d2': {'inputs': ['close'], 'func': f27_mcdt_405_macd_hurst_rs_63_d2}, 'f27_mcdt_406_macd_hurst_dfa_252_d2': {'inputs': ['close'], 'func': f27_mcdt_406_macd_hurst_dfa_252_d2}, 'f27_mcdt_407_macd_recurrence_rate_21_d2': {'inputs': ['close'], 'func': f27_mcdt_407_macd_recurrence_rate_21_d2}, 'f27_mcdt_408_macd_recurrence_determinism_21_d2': {'inputs': ['close'], 'func': f27_mcdt_408_macd_recurrence_determinism_21_d2}, 'f27_mcdt_409_macd_lempel_ziv_complexity_63_d2': {'inputs': ['close'], 'func': f27_mcdt_409_macd_lempel_ziv_complexity_63_d2}, 'f27_mcdt_410_macd_kolmogorov_complexity_proxy_63_d2': {'inputs': ['close'], 'func': f27_mcdt_410_macd_kolmogorov_complexity_proxy_63_d2}, 'f27_mcdt_411_macd_predictability_horizon_63_d2': {'inputs': ['close'], 'func': f27_mcdt_411_macd_predictability_horizon_63_d2}, 'f27_mcdt_412_macd_information_dimension_63_d2': {'inputs': ['close'], 'func': f27_mcdt_412_macd_information_dimension_63_d2}, 'f27_mcdt_413_macd_correlation_dimension_proxy_63_d2': {'inputs': ['close'], 'func': f27_mcdt_413_macd_correlation_dimension_proxy_63_d2}, 'f27_mcdt_414_macd_lyapunov_proxy_63_d2': {'inputs': ['close'], 'func': f27_mcdt_414_macd_lyapunov_proxy_63_d2}, 'f27_mcdt_415_macd_persistence_index_rs_21_d2': {'inputs': ['close'], 'func': f27_mcdt_415_macd_persistence_index_rs_21_d2}, 'f27_mcdt_416_macd_universe_with_volume_confirmed_count_d2': {'inputs': ['close', 'volume'], 'func': f27_mcdt_416_macd_universe_with_volume_confirmed_count_d2}, 'f27_mcdt_417_macd_universe_failure_breadth_at_top_score_d2': {'inputs': ['high', 'close'], 'func': f27_mcdt_417_macd_universe_failure_breadth_at_top_score_d2}, 'f27_mcdt_418_macd_universe_decay_velocity_post_peak_d2': {'inputs': ['close'], 'func': f27_mcdt_418_macd_universe_decay_velocity_post_peak_d2}, 'f27_mcdt_419_macd_universe_chronic_weakness_score_252_d2': {'inputs': ['close'], 'func': f27_mcdt_419_macd_universe_chronic_weakness_score_252_d2}, 'f27_mcdt_420_macd_universe_post_breakdown_recovery_failure_count_d2': {'inputs': ['close'], 'func': f27_mcdt_420_macd_universe_post_breakdown_recovery_failure_count_d2}, 'f27_mcdt_421_macd_universe_distribution_signal_aggregate_d2': {'inputs': ['close'], 'func': f27_mcdt_421_macd_universe_distribution_signal_aggregate_d2}, 'f27_mcdt_422_macd_universe_blowoff_collapse_indicator_d2': {'inputs': ['close'], 'func': f27_mcdt_422_macd_universe_blowoff_collapse_indicator_d2}, 'f27_mcdt_423_macd_universe_terminal_pattern_aggregate_d2': {'inputs': ['high', 'close'], 'func': f27_mcdt_423_macd_universe_terminal_pattern_aggregate_d2}, 'f27_mcdt_424_macd_universe_extreme_z_score_max_252_d2': {'inputs': ['close'], 'func': f27_mcdt_424_macd_universe_extreme_z_score_max_252_d2}, 'f27_mcdt_425_macd_universe_z_score_range_63_d2': {'inputs': ['close'], 'func': f27_mcdt_425_macd_universe_z_score_range_63_d2}, 'f27_mcdt_426_macd_universe_correlation_breakdown_zscore_252_d2': {'inputs': ['close'], 'func': f27_mcdt_426_macd_universe_correlation_breakdown_zscore_252_d2}, 'f27_mcdt_427_macd_universe_extreme_event_clustering_index_63_d2': {'inputs': ['close'], 'func': f27_mcdt_427_macd_universe_extreme_event_clustering_index_63_d2}, 'f27_mcdt_428_macd_universe_recall_optimized_score_d2': {'inputs': ['high', 'close'], 'func': f27_mcdt_428_macd_universe_recall_optimized_score_d2}, 'f27_mcdt_429_macd_universe_precision_optimized_score_d2': {'inputs': ['high', 'close'], 'func': f27_mcdt_429_macd_universe_precision_optimized_score_d2}, 'f27_mcdt_430_macd_terminal_distribution_score_v3_d2': {'inputs': ['high', 'close'], 'func': f27_mcdt_430_macd_terminal_distribution_score_v3_d2}, 'f27_mcdt_431_macd_universe_orthogonal_signal_aggregate_d2': {'inputs': ['high', 'close', 'volume'], 'func': f27_mcdt_431_macd_universe_orthogonal_signal_aggregate_d2}, 'f27_mcdt_432_multi_macd_consensus_topping_at_252h_d2': {'inputs': ['high', 'close'], 'func': f27_mcdt_432_multi_macd_consensus_topping_at_252h_d2}, 'f27_mcdt_433_macd_basket_chronic_failure_count_252_d2': {'inputs': ['close'], 'func': f27_mcdt_433_macd_basket_chronic_failure_count_252_d2}, 'f27_mcdt_434_macd_topping_intensity_score_extended_d2': {'inputs': ['high', 'close'], 'func': f27_mcdt_434_macd_topping_intensity_score_extended_d2}, 'f27_mcdt_435_macd_blowoff_then_decay_velocity_universe_d2': {'inputs': ['close'], 'func': f27_mcdt_435_macd_blowoff_then_decay_velocity_universe_d2}, 'f27_mcdt_436_macd_universe_alignment_score_extended_d2': {'inputs': ['close'], 'func': f27_mcdt_436_macd_universe_alignment_score_extended_d2}, 'f27_mcdt_437_macd_universe_persistence_after_extreme_252_d2': {'inputs': ['close'], 'func': f27_mcdt_437_macd_universe_persistence_after_extreme_252_d2}, 'f27_mcdt_438_macd_universe_lower_high_breadth_count_63_d2': {'inputs': ['close'], 'func': f27_mcdt_438_macd_universe_lower_high_breadth_count_63_d2}, 'f27_mcdt_439_macd_universe_failure_signal_density_63_d2': {'inputs': ['close'], 'func': f27_mcdt_439_macd_universe_failure_signal_density_63_d2}, 'f27_mcdt_440_macd_universe_breakdown_confirmation_count_d2': {'inputs': ['close'], 'func': f27_mcdt_440_macd_universe_breakdown_confirmation_count_d2}, 'f27_mcdt_441_macd_stuck_probability_proxy_252_d2': {'inputs': ['high', 'close'], 'func': f27_mcdt_441_macd_stuck_probability_proxy_252_d2}, 'f27_mcdt_442_macd_topping_aggregate_orthogonal_v3_d2': {'inputs': ['high', 'close', 'volume'], 'func': f27_mcdt_442_macd_topping_aggregate_orthogonal_v3_d2}, 'f27_mcdt_443_macd_ml_aggregate_terminal_score_v3_d2': {'inputs': ['high', 'close'], 'func': f27_mcdt_443_macd_ml_aggregate_terminal_score_v3_d2}, 'f27_mcdt_444_macd_ml_aggregate_distribution_score_v3_d2': {'inputs': ['close'], 'func': f27_mcdt_444_macd_ml_aggregate_distribution_score_v3_d2}, 'f27_mcdt_445_macd_terminal_breakdown_severity_extended_d2': {'inputs': ['high', 'close'], 'func': f27_mcdt_445_macd_terminal_breakdown_severity_extended_d2}, 'f27_mcdt_446_macd_chronic_distribution_score_extended_d2': {'inputs': ['close'], 'func': f27_mcdt_446_macd_chronic_distribution_score_extended_d2}, 'f27_mcdt_447_macd_failure_to_recover_aggregate_extended_d2': {'inputs': ['close'], 'func': f27_mcdt_447_macd_failure_to_recover_aggregate_extended_d2}, 'f27_mcdt_448_macd_universe_blowoff_collapse_master_score_d2': {'inputs': ['close'], 'func': f27_mcdt_448_macd_universe_blowoff_collapse_master_score_d2}, 'f27_mcdt_449_macd_extended_universe_topping_master_v3_d2': {'inputs': ['high', 'close', 'volume'], 'func': f27_mcdt_449_macd_extended_universe_topping_master_v3_d2}, 'f27_mcdt_450_absolute_terminal_macd_indicator_extended_d2': {'inputs': ['high', 'close', 'volume'], 'func': f27_mcdt_450_absolute_terminal_macd_indicator_extended_d2}}