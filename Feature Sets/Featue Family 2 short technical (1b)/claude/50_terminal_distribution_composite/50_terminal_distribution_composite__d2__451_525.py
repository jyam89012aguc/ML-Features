"""50_terminal_distribution_composite d2 features 451-525 — order-2 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff().diff(). Self-contained; helpers redefined locally per HANDOFF."""
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

def _slope_kernel(w):
    valid = ~np.isnan(w)
    mp = max(len(w) // 3, 2)
    if valid.sum() < mp:
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
    return s.rolling(n, min_periods=min_periods).apply(_slope_kernel, raw=True)

def _sma(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).mean()

def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=max(n // 3, 2)).mean()

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

def _h_amihud(close, volume, n):
    """Amihud illiquidity proxy: mean( |return| / dollar-vol ) over n bars."""
    ret = close.pct_change().abs()
    dv = (close * volume).replace(0, np.nan)
    return (ret / dv).rolling(n, min_periods=max(n // 3, 5)).mean()

def _h_roll_spread(close, n):
    """Roll spread proxy: 2 * sqrt(-cov(dP_t, dP_{t-1})), n bars."""
    dp = close.diff()
    cov = dp.rolling(n, min_periods=max(n // 3, 5)).cov(dp.shift(1))
    return 2.0 * np.sqrt((-cov).clip(lower=0))

def _h_corwin_schultz(high, low):
    """Corwin-Schultz 2-day spread proxy."""
    h2 = pd.concat([high, high.shift(1)], axis=1).max(axis=1)
    l2 = pd.concat([low, low.shift(1)], axis=1).min(axis=1)
    beta_t = np.log(_safe_div(high, low).clip(lower=1e-09)) ** 2
    beta_t1 = np.log(_safe_div(high.shift(1), low.shift(1)).clip(lower=1e-09)) ** 2
    beta = beta_t + beta_t1
    gamma = np.log(_safe_div(h2, l2).clip(lower=1e-09)) ** 2
    a_sqrt2 = np.sqrt(2.0)
    alpha = (np.sqrt(beta.clip(lower=0)) * (a_sqrt2 - 1.0) - np.sqrt(gamma.clip(lower=0))) / (3.0 - 2.0 * a_sqrt2)
    spread = 2.0 * (np.exp(alpha) - 1.0) / (1.0 + np.exp(alpha))
    return spread.clip(lower=0)

def _h_abdi_ranaldi(high, low, close):
    """Abdi-Ranaldi 2-day spread proxy."""
    eta_t = (np.log(high) + np.log(low)) / 2.0
    eta_t1 = (np.log(high.shift(1)) + np.log(low.shift(1))) / 2.0
    c_t = np.log(close)
    c_t1 = np.log(close.shift(1))
    expr = (c_t - eta_t) * (c_t - eta_t1) + (c_t1 - eta_t1) * (c_t1 - eta_t)
    s2 = 4.0 * expr.clip(lower=0)
    return np.sqrt(s2)

def _h_drawdown(high, close, n):
    rmax = high.rolling(n, min_periods=max(n // 3, 5)).max()
    return _safe_div(rmax - close, rmax)

def _h_lh_streak(high, n=WDAYS):
    h_n = high.rolling(n, min_periods=2).max()
    return _streak_true(h_n < h_n.shift(n))

def _h_dtw_kernel(w):
    """Lightweight DTW-proxy on a window vector: compares first-half to second-half via warped distance.
    Band radius 2. Used in rolling.apply(raw=True)."""
    if np.isnan(w).any():
        return np.nan
    n = len(w)
    if n < 4:
        return np.nan
    half = n // 2
    a = w[:half]
    b = w[half:half * 2]
    if len(a) != len(b):
        return np.nan
    INF = 1e+18
    m = len(a)
    cost = np.full((m + 1, m + 1), INF)
    cost[0, 0] = 0.0
    r = 2
    for i in range(1, m + 1):
        j_lo = max(1, i - r)
        j_hi = min(m, i + r)
        for j in range(j_lo, j_hi + 1):
            d = abs(a[i - 1] - b[j - 1])
            cost[i, j] = d + min(cost[i - 1, j], cost[i, j - 1], cost[i - 1, j - 1])
    if not np.isfinite(cost[m, m]):
        return np.nan
    return float(cost[m, m] / m)

def _h_template_distance(w, template):
    """Euclidean distance from z-normalized w to z-normalized template (same length)."""
    if np.isnan(w).any() or len(w) != len(template):
        return np.nan
    sd = np.std(w)
    if sd == 0 or np.isnan(sd):
        return np.nan
    wz = (w - np.mean(w)) / sd
    return float(np.sqrt(np.mean((wz - template) ** 2)))

def _h_tpl_stage4(L=63):
    x = np.linspace(0.0, 1.0, L)
    t = -x
    return (t - t.mean()) / t.std()

def _h_tpl_blowoff(L=63):
    x = np.linspace(0.0, 1.0, L)
    t = -np.abs(x - 0.4) + 0.3
    t = t - 0.5 * (x > 0.5) * (x - 0.5) * 4.0
    return (t - t.mean()) / t.std()

def _h_tpl_distribution(L=63):
    x = np.linspace(0.0, 1.0, L)
    t = np.where(x < 0.6, 0.0, -(x - 0.6) * 2.5)
    return (t - t.mean()) / (t.std() if t.std() > 0 else 1.0)

def _h_tpl_failed_breakout(L=63):
    x = np.linspace(0.0, 1.0, L)
    t = np.where(x < 0.2, x * 1.0, np.where(x < 0.3, 0.2 - (x - 0.2) * 2.0, -(x - 0.3) * 1.0))
    return (t - t.mean()) / (t.std() if t.std() > 0 else 1.0)

def _h_tpl_capitulation(L=63):
    x = np.linspace(0.0, 1.0, L)
    t = -x ** 3
    return (t - t.mean()) / t.std()

def _h_tpl_50pct_dd(L=63):
    t = np.linspace(0.0, -1.0, L)
    return (t - t.mean()) / t.std()

def _h_tpl_plateau_then_break(L=42):
    t = np.concatenate([np.zeros(14), -np.linspace(0.0, 1.0, L - 14)])
    return (t - t.mean()) / t.std()
_TPL_STAGE4_63 = _h_tpl_stage4(63)
_TPL_BLOWOFF_63 = _h_tpl_blowoff(63)
_TPL_DIST_63 = _h_tpl_distribution(63)
_TPL_FBKO_63 = _h_tpl_failed_breakout(63)
_TPL_CAPIT_63 = _h_tpl_capitulation(63)
_TPL_50DD_63 = _h_tpl_50pct_dd(63)
_TPL_PLAT_42 = _h_tpl_plateau_then_break(42)

def _h_dist_stage4_63(w):
    return _h_template_distance(w, _TPL_STAGE4_63)

def _h_dist_blowoff_63(w):
    return _h_template_distance(w, _TPL_BLOWOFF_63)

def _h_dist_distribution_63(w):
    return _h_template_distance(w, _TPL_DIST_63)

def _h_dist_fbko_63(w):
    return _h_template_distance(w, _TPL_FBKO_63)

def _h_dist_capit_63(w):
    return _h_template_distance(w, _TPL_CAPIT_63)

def _h_dist_50dd_63(w):
    return _h_template_distance(w, _TPL_50DD_63)

def _h_dist_plat_42(w):
    return _h_template_distance(w, _TPL_PLAT_42)

def _h_dist_distribution_63_neg(w):
    d = _h_template_distance(w, _TPL_DIST_63)
    if d is None or (isinstance(d, float) and np.isnan(d)):
        return np.nan
    return -d

def _h_multi_template_count_63(w):
    """Count of templates {stage4, distribution, capitulation} with distance < 1 to window w."""
    if len(w) != 63 or np.isnan(w).any():
        return np.nan
    sd = np.std(w)
    if sd == 0 or np.isnan(sd):
        return np.nan
    wz = (w - np.mean(w)) / sd
    d1 = np.sqrt(np.mean((wz - _TPL_STAGE4_63) ** 2))
    d2 = np.sqrt(np.mean((wz - _TPL_DIST_63) ** 2))
    d3 = np.sqrt(np.mean((wz - _TPL_CAPIT_63) ** 2))
    return float((d1 < 1.0) + (d2 < 1.0) + (d3 < 1.0))

def _h_recurrence_count_504(w):
    """For a 504-length returns window, count of 21-bar windows whose z-shape distance < 0.5 to current 21-bar."""
    if np.isnan(w).any() or len(w) < 42:
        return np.nan
    L = 21
    cur = w[-L:]
    sdcur = np.std(cur)
    if sdcur == 0 or np.isnan(sdcur):
        return np.nan
    cur_z = (cur - np.mean(cur)) / sdcur
    cnt = 0
    for i in range(0, len(w) - L):
        seg = w[i:i + L]
        sd = np.std(seg)
        if sd == 0 or np.isnan(sd):
            continue
        seg_z = (seg - np.mean(seg)) / sd
        d = np.sqrt(np.mean((seg_z - cur_z) ** 2))
        if d < 0.5:
            cnt += 1
    return float(cnt)

def _h_recurrence_recency_504(w):
    """For a 504-length returns window, bars since the most recent 21-bar window with z-distance < 0.5."""
    if np.isnan(w).any() or len(w) < 42:
        return np.nan
    L = 21
    cur = w[-L:]
    sdcur = np.std(cur)
    if sdcur == 0 or np.isnan(sdcur):
        return np.nan
    cur_z = (cur - np.mean(cur)) / sdcur
    last_match = -1
    for i in range(len(w) - 2 * L + 1):
        seg = w[i:i + L]
        sd = np.std(seg)
        if sd == 0 or np.isnan(sd):
            continue
        seg_z = (seg - np.mean(seg)) / sd
        d = np.sqrt(np.mean((seg_z - cur_z) ** 2))
        if d < 0.5:
            last_match = i
    if last_match < 0:
        return np.nan
    return float(len(w) - L - last_match)

def _h_attractor_strength_252(w):
    """In a 252-length returns window, count of disjoint 5-bar windows with z-distance < 0.3 to current 5-bar."""
    if np.isnan(w).any() or len(w) < 10:
        return np.nan
    L = 5
    cur = w[-L:]
    sdcur = np.std(cur)
    if sdcur == 0 or np.isnan(sdcur):
        return np.nan
    cur_z = (cur - np.mean(cur)) / sdcur
    cnt = 0
    i = 0
    while i <= len(w) - 2 * L:
        seg = w[i:i + L]
        sd = np.std(seg)
        if sd == 0 or np.isnan(sd):
            i += 1
            continue
        seg_z = (seg - np.mean(seg)) / sd
        d = np.sqrt(np.mean((seg_z - cur_z) ** 2))
        if d < 0.3:
            cnt += 1
            i += L
        else:
            i += 1
    return float(cnt)

def _h_value_area_triple(w):
    """Return (vah, val, poc) for a window of close prices. 70% mass around mode."""
    if np.isnan(w).any() or len(w) < 10:
        return (np.nan, np.nan, np.nan)
    lo = float(np.min(w))
    hi = float(np.max(w))
    if hi <= lo:
        return (hi, lo, (hi + lo) / 2.0)
    nbins = 30
    counts, edges = np.histogram(w, bins=nbins, range=(lo, hi))
    poc_bin = int(np.argmax(counts))
    poc = (edges[poc_bin] + edges[poc_bin + 1]) / 2.0
    total = counts.sum()
    if total == 0:
        return (np.nan, np.nan, poc)
    target = 0.7 * total
    inc = counts[poc_bin]
    lo_idx, hi_idx = (poc_bin, poc_bin)
    while inc < target and (lo_idx > 0 or hi_idx < nbins - 1):
        left = counts[lo_idx - 1] if lo_idx > 0 else -1
        right = counts[hi_idx + 1] if hi_idx < nbins - 1 else -1
        if right >= left:
            hi_idx += 1
            inc += counts[hi_idx]
        else:
            lo_idx -= 1
            inc += counts[lo_idx]
    vah = edges[hi_idx + 1]
    val = edges[lo_idx]
    return (float(vah), float(val), float(poc))

def _h_vah_kernel(w):
    return _h_value_area_triple(w)[0]

def _h_val_kernel(w):
    return _h_value_area_triple(w)[1]

def _h_poc_kernel(w):
    return _h_value_area_triple(w)[2]

def _h_vah_252(close):
    return close.rolling(YDAYS, min_periods=QDAYS).apply(_h_vah_kernel, raw=True)

def _h_val_252(close):
    return close.rolling(YDAYS, min_periods=QDAYS).apply(_h_val_kernel, raw=True)

def _h_poc_252(close):
    return close.rolling(YDAYS, min_periods=QDAYS).apply(_h_poc_kernel, raw=True)

def _h_skew_kernel(w):
    if np.isnan(w).any() or len(w) < 4:
        return np.nan
    sd = np.std(w)
    if sd == 0 or np.isnan(sd):
        return np.nan
    return float(np.mean(((w - np.mean(w)) / sd) ** 3))

def _h_kurt_kernel(w):
    if np.isnan(w).any() or len(w) < 4:
        return np.nan
    sd = np.std(w)
    if sd == 0 or np.isnan(sd):
        return np.nan
    return float(np.mean(((w - np.mean(w)) / sd) ** 4) - 3.0)

def _h_jb_kernel(w):
    if np.isnan(w).any() or len(w) < 6:
        return np.nan
    n = len(w)
    sd = np.std(w)
    if sd == 0 or np.isnan(sd):
        return np.nan
    z = (w - np.mean(w)) / sd
    s = float(np.mean(z ** 3))
    k = float(np.mean(z ** 4) - 3.0)
    return n / 6.0 * (s ** 2 + k ** 2 / 4.0)

def f50_tdco_451_amihud_resilience_proxy_63_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Resilience proxy: ratio of Amihud(21)_now to Amihud(21)_lagged-21 — close to 1 means quick bounce-back
    of liquidity after impact; > 1 means liquidity has decayed further (no resilience)."""
    a21 = _h_amihud(close, volume, MDAYS)
    return _safe_div(a21, a21.shift(MDAYS)).diff().diff()

def f50_tdco_452_amihud_acceleration_63_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rate of change of Amihud illiquidity over 63d: slope of Amihud(21) over 63 bars; higher = liquidity worsening."""
    a21 = _h_amihud(close, volume, MDAYS)
    return _rolling_slope(a21, QDAYS).diff().diff()

def f50_tdco_453_roll_spread_persistence_63_d2(close: pd.Series) -> pd.Series:
    """AR(1) autocorrelation of Roll spread proxy over 63d — high = persistent illiquidity."""
    rs = _h_roll_spread(close, MDAYS)
    return rs.rolling(QDAYS, min_periods=MDAYS).corr(rs.shift(1)).diff().diff()

def f50_tdco_454_roll_spread_widening_post_peak_63_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """Roll spread today minus Roll spread at most-recent 252d peak — positive = post-peak spread widening."""
    rs = _h_roll_spread(close, MDAYS)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rs_at_peak = rs.where(high == rmax).ffill()
    return (rs - rs_at_peak).diff().diff()

def f50_tdco_455_corwin_schultz_widening_post_peak_63_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Corwin-Schultz spread today minus its value at most-recent 252d peak — post-peak widening proxy."""
    cs = _h_corwin_schultz(high, low)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    cs_at_peak = cs.where(high == rmax).ffill()
    return (cs - cs_at_peak).diff().diff()

def f50_tdco_456_abdi_ranaldi_spread_widening_post_peak_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Abdi-Ranaldi 2-bar spread today minus its value at most-recent 252d peak — post-peak widening."""
    ar = _h_abdi_ranaldi(high, low, close)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    ar_at_peak = ar.where(high == rmax).ffill()
    return (ar - ar_at_peak).diff().diff()

def f50_tdco_457_effective_tick_concentration_zscore_252_d2(close: pd.Series) -> pd.Series:
    """Fraction of past 63 closes whose last 2 decimals are in {00, 25, 50, 75} (round-ish), z-scored over 252.
    High = price clustering at round levels (Holden 2009-style proxy for low informed-trade activity)."""
    last = (close * 100.0).round() % 100
    is_round = ((last == 0) | (last == 25) | (last == 50) | (last == 75)).astype(float)
    frac = is_round.rolling(QDAYS, min_periods=MDAYS).mean()
    return _rolling_zscore(frac, YDAYS).diff().diff()

def f50_tdco_458_price_clustering_at_round_numbers_pct_63_d2(close: pd.Series) -> pd.Series:
    """% of past 63 closes ending in 0 or 5 (last cent digit) — heavy clustering = thin order book."""
    last = (close * 100.0).round() % 10
    is_round = ((last == 0) | (last == 5)).astype(float)
    return is_round.rolling(QDAYS, min_periods=MDAYS).mean().diff().diff()

def f50_tdco_459_zero_volume_day_count_63_d2(volume: pd.Series) -> pd.Series:
    """Count of bars in past 63 with volume in bottom 5%ile of past 252 volume — stagnation signal."""
    q5 = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.05)
    is_low = (volume <= q5).astype(float)
    return is_low.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f50_tdco_460_trade_size_proxy_decay_63_d2(volume: pd.Series) -> pd.Series:
    """Avg volume per bar / volatility-of-volume — proxy for avg-trade-size; decay over 63 = institutional retreat.
    Returns ratio_now / ratio_63bars_ago."""
    vstd = volume.rolling(MDAYS, min_periods=WDAYS).std()
    proxy = _safe_div(_sma(volume, MDAYS), vstd)
    return _safe_div(proxy, proxy.shift(QDAYS)).diff().diff()

def f50_tdco_461_turnover_velocity_decay_zscore_252_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score over 252 of (close * volume) / (252d-avg close * volume) — turnover decay relative to history."""
    dv = close * volume
    ratio = _safe_div(dv, _sma(dv, YDAYS))
    return _rolling_zscore(ratio, YDAYS).diff().diff()

def f50_tdco_462_volume_per_atr_decay_63_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume normalized by ATR over 63d, compared to value 63 bars ago — ratio < 1 means thinner trading per unit vol."""
    atr = _atr(high, low, close, MDAYS)
    vpa = _safe_div(volume, atr)
    vpa_sm = vpa.rolling(MDAYS, min_periods=WDAYS).mean()
    return _safe_div(vpa_sm, vpa_sm.shift(QDAYS)).diff().diff()

def f50_tdco_463_dollar_volume_to_market_cap_proxy_decay_63_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar volume / (close * 1e6) [proxy assumes mcap ~ close*const] — proxy for daily turnover ratio.
    Returns z-score over 252 of (current / 63bar-prior) — strong negative = thinning relative to size."""
    dv = close * volume
    ratio = _safe_div(dv, close * 1000000.0)
    return _rolling_zscore(_safe_div(ratio, ratio.shift(QDAYS)), YDAYS).diff().diff()

def f50_tdco_464_effective_spread_proxy_2day_high_low_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """2-day max-high minus 2-day min-low, normalized by midpoint — wide intraday range proxy
    for effective spread; high = volatile but illiquid."""
    h2 = high.rolling(2, min_periods=2).max()
    l2 = low.rolling(2, min_periods=2).min()
    mid = (h2 + l2) / 2.0
    return _safe_div(h2 - l2, mid).diff().diff()

def f50_tdco_465_quoted_spread_proxy_intraday_range_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 21d median of (high - low) / close — quoted-spread proxy; rising = widening effective spread."""
    rng = _safe_div(high - low, close)
    return rng.rolling(MDAYS, min_periods=WDAYS).median().diff().diff()

def f50_tdco_466_dtw_distance_to_recent_50pct_dd_252_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """Template distance of last 63 closes' z-normalized shape vs a constant-slope -100% template
    (proxy for a 50% straight-line decline path) — low = path closely matches a steady-decline path."""
    return close.rolling(QDAYS, min_periods=MDAYS).apply(_h_dist_50dd_63, raw=True).diff().diff()

def f50_tdco_467_dtw_distance_to_recent_252h_then_breakdown_252_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """Template distance: w[:14]=high plateau, w[14:]=monotone decline. Last 42 closes' shape matched."""
    return close.rolling(42, min_periods=MDAYS).apply(_h_dist_plat_42, raw=True).diff().diff()

def f50_tdco_468_pattern_match_score_recent_topping_63_d2(close: pd.Series) -> pd.Series:
    """Negated template distance to plateau-then-distribution template — higher = better topping-pattern match."""
    return close.rolling(QDAYS, min_periods=MDAYS).apply(_h_dist_distribution_63_neg, raw=True).diff().diff()

def f50_tdco_469_dynamic_warping_drawdown_path_similarity_252_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """Lightweight DTW kernel: compares first-half vs second-half of past 42d drawdown path —
    low = self-similar decline; high = path is irregular."""
    dd = _h_drawdown(high, close, YDAYS)
    return dd.rolling(42, min_periods=MDAYS).apply(_h_dtw_kernel, raw=True).diff().diff()

def f50_tdco_470_path_similarity_to_stage_4_template_63_d2(close: pd.Series) -> pd.Series:
    """Distance from close-path (63 bars) to a monotone Stage-4 decline template; small = strong match."""
    return close.rolling(QDAYS, min_periods=MDAYS).apply(_h_dist_stage4_63, raw=True).diff().diff()

def f50_tdco_471_path_similarity_to_blowoff_template_63_d2(close: pd.Series) -> pd.Series:
    """Distance from close-path (63 bars) to a sharp-rise-then-collapse blowoff template."""
    return close.rolling(QDAYS, min_periods=MDAYS).apply(_h_dist_blowoff_63, raw=True).diff().diff()

def f50_tdco_472_path_similarity_to_distribution_template_63_d2(close: pd.Series) -> pd.Series:
    """Distance from close-path (63 bars) to a distribution (plateau then breakdown) template."""
    return close.rolling(QDAYS, min_periods=MDAYS).apply(_h_dist_distribution_63, raw=True).diff().diff()

def f50_tdco_473_path_similarity_to_failed_breakout_template_63_d2(close: pd.Series) -> pd.Series:
    """Distance from close-path (63) to spike-then-reverse-below-baseline failed-breakout template."""
    return close.rolling(QDAYS, min_periods=MDAYS).apply(_h_dist_fbko_63, raw=True).diff().diff()

def f50_tdco_474_path_similarity_to_capitulation_template_63_d2(close: pd.Series) -> pd.Series:
    """Distance from close-path (63) to gentle-decline-then-cliff-drop capitulation template."""
    return close.rolling(QDAYS, min_periods=MDAYS).apply(_h_dist_capit_63, raw=True).diff().diff()

def f50_tdco_475_self_similar_pattern_recurrence_count_504_d2(close: pd.Series) -> pd.Series:
    """Count of past-504 21-bar windows whose returns-shape z-distance to current 21-bar returns-shape < 0.5.
    High = current pattern is highly recurrent in recent history."""
    ret = close.pct_change()
    return ret.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_h_recurrence_count_504, raw=True).diff().diff()

def f50_tdco_476_self_similar_pattern_recurrence_recency_d2(close: pd.Series) -> pd.Series:
    """Bars since the most recent prior occurrence of a 21-bar return shape similar (z-distance < 0.5)
    to current 21-bar return shape, over a 504-bar window."""
    ret = close.pct_change()
    return ret.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_h_recurrence_recency_504, raw=True).diff().diff()

def f50_tdco_477_pattern_attractor_strength_252_d2(close: pd.Series) -> pd.Series:
    """How often the current 5-bar returns shape reappears in past 252 — sticky-attractor proxy.
    Count of disjoint 5-bar windows with z-distance < 0.3 to current 5-bar."""
    ret = close.pct_change()
    return ret.rolling(YDAYS, min_periods=QDAYS).apply(_h_attractor_strength_252, raw=True).diff().diff()

def f50_tdco_478_multi_template_pattern_alignment_count_252_d2(close: pd.Series) -> pd.Series:
    """At each bar, count of templates {Stage-4, distribution, capitulation} with z-distance < 1.0 to
    last 63-bar close path — multi-template alignment count (0-3)."""
    return close.rolling(QDAYS, min_periods=MDAYS).apply(_h_multi_template_count_63, raw=True).diff().diff()

def f50_tdco_479_historical_pattern_distance_aggregate_504_d2(close: pd.Series) -> pd.Series:
    """Mean Stage-4-template distance over past 504 bars — lower = more pattern matches overall in window."""
    d_series = close.rolling(QDAYS, min_periods=MDAYS).apply(_h_dist_stage4_63, raw=True)
    return d_series.rolling(DDAYS_2Y, min_periods=YDAYS).mean().diff().diff()

def f50_tdco_480_pattern_persistence_after_match_252_d2(close: pd.Series) -> pd.Series:
    """PIT proxy of: of past-252 bars where Stage-4-template distance was < 1.0, fraction where it remained
    < 1.0 for the subsequent 21 bars. We compute on a 21-lagged basis so only past observations are used."""
    d_series = close.rolling(QDAYS, min_periods=MDAYS).apply(_h_dist_stage4_63, raw=True)
    match = (d_series < 1.0).astype(float)
    sust = match.rolling(MDAYS, min_periods=WDAYS).min()
    sust_pit = match.shift(MDAYS) * sust.shift(MDAYS)
    sust_pit_sum = sust_pit.rolling(YDAYS, min_periods=QDAYS).sum()
    match_pit = match.shift(MDAYS).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(sust_pit_sum, match_pit).diff().diff()

def f50_tdco_481_distribution_signal_in_early_cycle_phase_count_252_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of distribution-days in past 252 that occurred while bars-since-252d-low was < 84 (early cycle)."""
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    bs_min = _bars_since_true(low == rmin)
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    dd = ((ret < -0.002) & (volume > vavg)).astype(float)
    early = (bs_min >= 0) & (bs_min < 84)
    return (dd * early.astype(float)).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f50_tdco_482_distribution_signal_in_late_cycle_phase_count_252_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of distribution-days in past 252 that occurred while bars-since-252d-low was >= 168 (late cycle)."""
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    bs_min = _bars_since_true(low == rmin)
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    dd = ((ret < -0.002) & (volume > vavg)).astype(float)
    late = bs_min >= 168
    return (dd * late.astype(float)).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f50_tdco_483_distribution_signal_in_markdown_phase_count_252_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of distribution-days in past 252 occurring while close < SMA50 AND SMA50 declining (markdown phase)."""
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    dd = ((ret < -0.002) & (volume > vavg)).astype(float)
    s50 = _sma(close, 50)
    markdown = (close < s50) & (s50 < s50.shift(MDAYS))
    return (dd * markdown.astype(float)).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f50_tdco_484_distribution_concentration_in_late_cycle_zscore_252_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score over 252 of (late-cycle dist count / total dist count) — concentration of distribution late in cycle."""
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    bs_min = _bars_since_true(low == rmin)
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    dd = ((ret < -0.002) & (volume > vavg)).astype(float)
    late = bs_min >= 168
    late_cnt = (dd * late.astype(float)).rolling(YDAYS, min_periods=QDAYS).sum()
    tot = dd.rolling(YDAYS, min_periods=QDAYS).sum()
    frac = _safe_div(late_cnt, tot)
    return _rolling_zscore(frac, YDAYS).diff().diff()

def f50_tdco_485_cycle_position_normalized_distribution_count_252_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """For each distribution-day in past 252, compute cycle-position = bars_since_252_low / 252;
    return mean cycle-position weighted by distribution events. Closer to 1 = distributions concentrated late."""
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    bs_min = _bars_since_true(low == rmin)
    pos = bs_min / float(YDAYS)
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    dd = ((ret < -0.002) & (volume > vavg)).astype(float)
    num = (dd * pos.fillna(0)).rolling(YDAYS, min_periods=QDAYS).sum()
    den = dd.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(num, den).diff().diff()

def f50_tdco_486_cycle_phase_consistency_with_distribution_signal_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if late-cycle (bs-since-252-low > 168) AND distribution-day-count-25 >= 4 — phase-consistent distribution."""
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    bs_min = _bars_since_true(low == rmin)
    late = bs_min > 168
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    dd25 = ((ret < -0.002) & (volume > vavg)).astype(float).rolling(25, min_periods=10).sum()
    return (late & (dd25 >= 4.0)).astype(float).where(vavg.notna(), np.nan).diff().diff()

def f50_tdco_487_cycle_completion_then_distribution_indicator_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if bars-since-252d-peak between 21 and 84 (post-peak early window) AND dist-25 >= 3 — cycle-completion-then-distribution."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    bs_peak = _bars_since_true(high == rmax)
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    dd25 = ((ret < -0.002) & (volume > vavg)).astype(float).rolling(25, min_periods=10).sum()
    return ((bs_peak > 21) & (bs_peak < 84) & (dd25 >= 3.0)).astype(float).where(vavg.notna(), np.nan).diff().diff()

def f50_tdco_488_cycle_end_signal_count_252_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of past-252 bars where cycle position is > 0.8 (late) AND close < SMA50 — cycle-end signals."""
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    bs_min = _bars_since_true(low == rmin)
    pos = bs_min / float(YDAYS)
    s50 = _sma(close, 50)
    sig = ((pos > 0.8) & (close < s50)).astype(float)
    return sig.rolling(YDAYS, min_periods=QDAYS).sum().where(s50.notna(), np.nan).diff().diff()

def f50_tdco_489_cycle_topping_pattern_score_252_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Aggregate score: sum of {late-cycle, dist-day-count-25>=3, close<SMA50, lh-streak>=3} — cycle-topping intensity."""
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    bs_min = _bars_since_true(low == rmin)
    late = (bs_min > 168).astype(float)
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    dd25 = ((ret < -0.002) & (volume > vavg)).astype(float).rolling(25, min_periods=10).sum()
    s50 = _sma(close, 50)
    lh_st = _h_lh_streak(high)
    return (late.fillna(0) + (dd25 >= 3.0).astype(float).fillna(0) + (close < s50).astype(float).fillna(0) + (lh_st >= 3).astype(float).fillna(0)).where(s50.notna() & vavg.notna(), np.nan).diff().diff()

def f50_tdco_490_cycle_terminal_phase_indicator_252_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if cycle-position > 0.85 AND drawdown_252 > 30% AND close < SMA200 — cycle terminal-phase state."""
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    bs_min = _bars_since_true(low == rmin)
    pos = bs_min / float(YDAYS)
    dd = _h_drawdown(high, close, YDAYS)
    s200 = _sma(close, 200)
    return ((pos > 0.85) & (dd > 0.3) & (close < s200)).astype(float).where(s200.notna(), np.nan).diff().diff()

def f50_tdco_491_value_area_high_proxy_252_d2(close: pd.Series) -> pd.Series:
    """Value Area High proxy from 252d close distribution: upper edge of bin range containing 70% mass around POC."""
    return _h_vah_252(close).diff().diff()

def f50_tdco_492_value_area_low_proxy_252_d2(close: pd.Series) -> pd.Series:
    """Value Area Low proxy from 252d close distribution: lower edge of bin range containing 70% mass around POC."""
    return _h_val_252(close).diff().diff()

def f50_tdco_493_close_above_value_area_high_state_d2(close: pd.Series) -> pd.Series:
    """1 if close > VAH(252) — out-of-value-area-high state."""
    vah = _h_vah_252(close)
    return (close > vah).astype(float).where(vah.notna(), np.nan).diff().diff()

def f50_tdco_494_close_below_value_area_low_state_d2(close: pd.Series) -> pd.Series:
    """1 if close < VAL(252) — out-of-value-area-low state (acceptance below value, bearish profile signal)."""
    val = _h_val_252(close)
    return (close < val).astype(float).where(val.notna(), np.nan).diff().diff()

def f50_tdco_495_point_of_control_proxy_252_d2(close: pd.Series) -> pd.Series:
    """Point of Control proxy: midpoint of bin with most close prices in past 252d distribution."""
    return _h_poc_252(close).diff().diff()

def f50_tdco_496_close_distance_from_poc_zscore_252_d2(close: pd.Series) -> pd.Series:
    """Z-score over 252 of (close - POC)/POC — distance of close from heaviest traded zone."""
    poc = _h_poc_252(close)
    dist = _safe_div(close - poc, poc)
    return _rolling_zscore(dist, YDAYS).diff().diff()

def f50_tdco_497_value_area_widening_post_peak_63_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """(VAH-VAL) today minus (VAH-VAL) at most-recent 252d peak — widening = distribution-zone broadening post-peak."""
    vah = _h_vah_252(close)
    val = _h_val_252(close)
    width = vah - val
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    width_at_peak = width.where(high == rmax).ffill()
    return (width - width_at_peak).diff().diff()

def f50_tdco_498_value_area_skew_post_peak_63_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """(POC - VAL) - (VAH - POC) — positive = POC skewed toward VAH (top-heavy);
    negative = POC near VAL (bottom-heavy) — bottom-heavy after peak = distribution into weakness."""
    vah = _h_vah_252(close)
    val = _h_val_252(close)
    poc = _h_poc_252(close)
    return (poc - val - (vah - poc)).diff().diff()

def f50_tdco_499_volume_profile_top_concentration_252_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of past-252 volume occurring on bars where close > 0.9 * 252d-high — top-of-range volume concentration."""
    h252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    high_band = close > 0.9 * h252
    vol_top = (volume * high_band.astype(float)).rolling(YDAYS, min_periods=QDAYS).sum()
    vol_all = volume.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(vol_top, vol_all).diff().diff()

def f50_tdco_500_volume_profile_distribution_index_252_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Distribution index = (top-band volume - bottom-band volume) / total volume; positive = top-heavy distribution."""
    h252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    l252 = low.rolling(YDAYS, min_periods=QDAYS).min()
    rng = h252 - l252
    top_band = close > l252 + 0.7 * rng
    bot_band = close < l252 + 0.3 * rng
    vt = (volume * top_band.astype(float)).rolling(YDAYS, min_periods=QDAYS).sum()
    vb = (volume * bot_band.astype(float)).rolling(YDAYS, min_periods=QDAYS).sum()
    vall = volume.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(vt - vb, vall).diff().diff()

def f50_tdco_501_returns_skew_evolution_post_peak_63_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """Skew of returns over past 63d minus skew of returns over the prior 63d window — change in skew.
    Negative shift = left-tail thickening over time."""
    ret = close.pct_change()
    sk_now = ret.rolling(QDAYS, min_periods=MDAYS).apply(_h_skew_kernel, raw=True)
    return (sk_now - sk_now.shift(QDAYS)).diff().diff()

def f50_tdco_502_returns_kurtosis_evolution_post_peak_63_d2(close: pd.Series) -> pd.Series:
    """Kurtosis of returns over past 63 minus kurtosis 63 bars earlier — rising = fatter tails developing."""
    ret = close.pct_change()
    kt_now = ret.rolling(QDAYS, min_periods=MDAYS).apply(_h_kurt_kernel, raw=True)
    return (kt_now - kt_now.shift(QDAYS)).diff().diff()

def f50_tdco_503_returns_skew_shift_zscore_252_d2(close: pd.Series) -> pd.Series:
    """Z-score over 252 of (skew_63 - skew_63.shift(63)) — standardized skew shift."""
    ret = close.pct_change()
    sk = ret.rolling(QDAYS, min_periods=MDAYS).apply(_h_skew_kernel, raw=True)
    shift = sk - sk.shift(QDAYS)
    return _rolling_zscore(shift, YDAYS).diff().diff()

def f50_tdco_504_returns_kurtosis_shift_zscore_252_d2(close: pd.Series) -> pd.Series:
    """Z-score over 252 of (kurt_63 - kurt_63.shift(63)) — standardized kurtosis shift."""
    ret = close.pct_change()
    kt = ret.rolling(QDAYS, min_periods=MDAYS).apply(_h_kurt_kernel, raw=True)
    shift = kt - kt.shift(QDAYS)
    return _rolling_zscore(shift, YDAYS).diff().diff()

def f50_tdco_505_returns_higher_moments_terminal_indicator_d2(close: pd.Series) -> pd.Series:
    """1 if skew(63) < -0.5 AND kurt(63) > 3 AND skew_shift < 0 AND kurt_shift > 0 — terminal-fat-left-tail signature."""
    ret = close.pct_change()
    sk = ret.rolling(QDAYS, min_periods=MDAYS).apply(_h_skew_kernel, raw=True)
    kt = ret.rolling(QDAYS, min_periods=MDAYS).apply(_h_kurt_kernel, raw=True)
    sk_shift = sk - sk.shift(QDAYS)
    kt_shift = kt - kt.shift(QDAYS)
    return ((sk < -0.5) & (kt > 3.0) & (sk_shift < 0) & (kt_shift > 0)).astype(float).where(sk.notna() & kt.notna(), np.nan).diff().diff()

def f50_tdco_506_returns_left_tail_thickening_post_peak_63_d2(close: pd.Series) -> pd.Series:
    """Fraction of returns in past 63 below the 5th percentile of returns over past 252 (extreme left-tail count)."""
    ret = close.pct_change()
    q5 = ret.rolling(YDAYS, min_periods=QDAYS).quantile(0.05)
    is_left = (ret < q5).astype(float)
    return is_left.rolling(QDAYS, min_periods=MDAYS).mean().diff().diff()

def f50_tdco_507_returns_right_tail_decay_post_peak_63_d2(close: pd.Series) -> pd.Series:
    """Fraction of returns in past 63 above 95th percentile of past-252 returns — right-tail thinning = lower."""
    ret = close.pct_change()
    q95 = ret.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    is_right = (ret > q95).astype(float)
    return is_right.rolling(QDAYS, min_periods=MDAYS).mean().diff().diff()

def f50_tdco_508_returns_jarque_bera_stat_evolution_63_d2(close: pd.Series) -> pd.Series:
    """Change in Jarque-Bera statistic of returns over 63d vs 63 bars ago — rising = increasingly non-normal."""
    ret = close.pct_change()
    jb = ret.rolling(QDAYS, min_periods=MDAYS).apply(_h_jb_kernel, raw=True)
    return (jb - jb.shift(QDAYS)).diff().diff()

def f50_tdco_509_returns_distribution_shift_pre_post_peak_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """Mean of returns in 63d window minus mean of returns in the 63d window ending at most-recent 252d peak —
    post-peak mean-return shift (negative = decline acceleration).
    Vectorized via per-row gather of mean63 at index (i - bs_peak)."""
    ret = close.pct_change()
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    bs_peak = _bars_since_true(high == rmax)
    mean63 = ret.rolling(QDAYS, min_periods=MDAYS).mean()
    n = len(ret)
    bs = bs_peak.fillna(-1).astype(int).to_numpy()
    mean_arr = mean63.to_numpy()
    out = np.full(n, np.nan)
    for i in range(n):
        b = bs[i]
        if b < 63 or b > 200:
            continue
        src_idx = i - b
        if src_idx < 0:
            continue
        v = mean_arr[src_idx]
        if not np.isnan(v) and (not np.isnan(mean_arr[i])):
            out[i] = mean_arr[i] - v
    return pd.Series(out, index=close.index).diff().diff()

def f50_tdco_510_returns_moment_alignment_terminal_signal_d2(close: pd.Series) -> pd.Series:
    """1 if skew_shift < -0.3 AND left-tail fraction > 0.15 AND kurt_shift > 1 — multi-moment terminal alignment."""
    ret = close.pct_change()
    sk = ret.rolling(QDAYS, min_periods=MDAYS).apply(_h_skew_kernel, raw=True)
    sk_shift = sk - sk.shift(QDAYS)
    q5 = ret.rolling(YDAYS, min_periods=QDAYS).quantile(0.05)
    left_frac = (ret < q5).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()
    kt = ret.rolling(QDAYS, min_periods=MDAYS).apply(_h_kurt_kernel, raw=True)
    kt_shift = kt - kt.shift(QDAYS)
    return ((sk_shift < -0.3) & (left_frac > 0.15) & (kt_shift > 1.0)).astype(float).where(sk.notna() & kt.notna(), np.nan).diff().diff()

def f50_tdco_511_sharpe_ratio_proxy_post_peak_63_d2(close: pd.Series) -> pd.Series:
    """Sharpe-ratio proxy over 63d: mean_return / std_return; negative = post-peak decline regime."""
    ret = close.pct_change()
    m = ret.rolling(QDAYS, min_periods=MDAYS).mean()
    s = ret.rolling(QDAYS, min_periods=MDAYS).std()
    return _safe_div(m, s).diff().diff()

def f50_tdco_512_sortino_ratio_proxy_post_peak_63_d2(close: pd.Series) -> pd.Series:
    """Sortino ratio proxy: mean_return / std(negative_returns_only) — sensitive to downside-only vol."""
    ret = close.pct_change()
    m = ret.rolling(QDAYS, min_periods=MDAYS).mean()
    neg = ret.where(ret < 0, 0.0)
    s_dn = neg.rolling(QDAYS, min_periods=MDAYS).std()
    return _safe_div(m, s_dn).diff().diff()

def f50_tdco_513_calmar_ratio_proxy_post_peak_252_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """Calmar ratio proxy: (252d return) / max(drawdown_252) — annual return per unit max DD; negative = bear."""
    r252 = close.pct_change(YDAYS)
    dd = _h_drawdown(high, close, YDAYS)
    max_dd = dd.rolling(YDAYS, min_periods=QDAYS).max()
    return _safe_div(r252, max_dd).diff().diff()

def f50_tdco_514_information_ratio_decay_63_d2(close: pd.Series) -> pd.Series:
    """Information ratio decay proxy: (Sharpe_63 - Sharpe_63 lagged 21) — falling = deteriorating risk-adj returns."""
    ret = close.pct_change()
    m = ret.rolling(QDAYS, min_periods=MDAYS).mean()
    s = ret.rolling(QDAYS, min_periods=MDAYS).std()
    sh = _safe_div(m, s)
    return (sh - sh.shift(MDAYS)).diff().diff()

def f50_tdco_515_risk_adjusted_breakdown_severity_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Drawdown_63 normalized by realized-vol_63 — risk-adjusted decline severity."""
    dd = _h_drawdown(high, close, QDAYS)
    vol = close.pct_change().rolling(QDAYS, min_periods=MDAYS).std()
    return _safe_div(dd, vol).diff().diff()

def f50_tdco_516_risk_adjusted_recovery_failure_63_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """(failed-recovery-fraction-63) / vol_63 — risk-adjusted recovery weakness."""
    h63 = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    bounce = close.pct_change(WDAYS) > 0.05
    failed = bounce & (high < h63)
    b_cnt = bounce.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    f_cnt = failed.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    fail_frac = _safe_div(f_cnt, b_cnt)
    vol = close.pct_change().rolling(QDAYS, min_periods=MDAYS).std()
    return _safe_div(fail_frac, vol).diff().diff()

def f50_tdco_517_risk_to_reward_ratio_decay_63_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """Downside_vol / Upside_vol over 63d — > 1 means downside risk dominates."""
    ret = close.pct_change()
    pos = ret.where(ret > 0, 0.0)
    neg = ret.where(ret < 0, 0.0)
    up = pos.rolling(QDAYS, min_periods=MDAYS).std()
    dn = neg.rolling(QDAYS, min_periods=MDAYS).std()
    return _safe_div(dn, up).diff().diff()

def f50_tdco_518_vol_adjusted_drawdown_speed_63_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """Drawdown_252 - drawdown_252.shift(21), divided by vol_63 — vol-normalized DD acceleration."""
    dd = _h_drawdown(high, close, YDAYS)
    speed = dd - dd.shift(MDAYS)
    vol = close.pct_change().rolling(QDAYS, min_periods=MDAYS).std()
    return _safe_div(speed, vol).diff().diff()

def f50_tdco_519_sharpe_ratio_terminal_decay_252_d2(close: pd.Series) -> pd.Series:
    """Sharpe(63)_now minus Sharpe(63) 252 bars ago — long-horizon risk-adj decay."""
    ret = close.pct_change()
    m = ret.rolling(QDAYS, min_periods=MDAYS).mean()
    s = ret.rolling(QDAYS, min_periods=MDAYS).std()
    sh = _safe_div(m, s)
    return (sh - sh.shift(YDAYS)).diff().diff()

def f50_tdco_520_ulcer_index_terminal_zscore_252_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """Ulcer Index over 63d (sqrt(mean(drawdown_pct^2))), z-scored over 252 — high = high pain accumulation."""
    dd = _h_drawdown(high, close, YDAYS) * 100.0
    ui = (dd ** 2).rolling(QDAYS, min_periods=MDAYS).mean()
    ui = np.sqrt(ui)
    return _rolling_zscore(ui, YDAYS).diff().diff()

def f50_tdco_521_batch_4_terminal_orthogonal_aggregate_zscore_252_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Aggregate over 5 orthogonal dimensions (microstructure, pattern-template, cycle-phase, moment, risk-adj),
    each z-scored within itself, then summed: a batch-4 terminal-orthogonal composite."""
    cs = _h_corwin_schultz(high, low)
    z_cs = _rolling_zscore(cs, YDAYS)
    pd_dist = close.rolling(QDAYS, min_periods=MDAYS).apply(_h_dist_stage4_63, raw=True)
    z_pat = -_rolling_zscore(pd_dist, YDAYS)
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    bs_min = _bars_since_true(low == rmin)
    z_cyc = _rolling_zscore(bs_min / float(YDAYS), YDAYS)
    ret = close.pct_change()
    sk = ret.rolling(QDAYS, min_periods=MDAYS).apply(_h_skew_kernel, raw=True)
    z_sk = -_rolling_zscore(sk, YDAYS)
    dd = _h_drawdown(high, close, YDAYS) * 100.0
    ui = np.sqrt((dd ** 2).rolling(QDAYS, min_periods=MDAYS).mean())
    z_ui = _rolling_zscore(ui, YDAYS)
    return (z_cs.fillna(0) + z_pat.fillna(0) + z_cyc.fillna(0) + z_sk.fillna(0) + z_ui.fillna(0)).where(cs.notna() & sk.notna(), np.nan).diff().diff()

def f50_tdco_522_terminal_recall_optimized_v4_score_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Recall-optimized v4: union of low-threshold bearish signals from batch-4 dimensions —
    sum of {cs widening > 0, template-match < median, late-cycle, neg skew, ulcer rising, dd>15%}.
    High recall, lower precision."""
    cs = _h_corwin_schultz(high, low)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    cs_widen = cs - cs.where(high == rmax).ffill()
    pd_dist = close.rolling(QDAYS, min_periods=MDAYS).apply(_h_dist_stage4_63, raw=True)
    pd_med = pd_dist.rolling(YDAYS, min_periods=QDAYS).median()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    bs_min = _bars_since_true(low == rmin)
    late = bs_min > 168
    ret = close.pct_change()
    sk = ret.rolling(QDAYS, min_periods=MDAYS).apply(_h_skew_kernel, raw=True)
    dd = _h_drawdown(high, close, YDAYS)
    ui = np.sqrt(((dd * 100.0) ** 2).rolling(QDAYS, min_periods=MDAYS).mean())
    ui_rising = ui > ui.shift(MDAYS)
    return ((cs_widen > 0).astype(float).fillna(0) + (pd_dist < pd_med).astype(float).fillna(0) + late.astype(float).fillna(0) + (sk < 0).astype(float).fillna(0) + ui_rising.astype(float).fillna(0) + (dd > 0.15).astype(float).fillna(0)).where(cs.notna() & sk.notna(), np.nan).diff().diff()

def f50_tdco_523_terminal_precision_optimized_v4_score_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Precision-optimized v4: AND of strict thresholds across all batch-4 dimensions:
    CS-widening > median, template-match < q25, late-cycle (>0.85), skew < -0.5, ulcer > q75, dd > 35%."""
    cs = _h_corwin_schultz(high, low)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    cs_widen = cs - cs.where(high == rmax).ffill()
    cs_med = cs_widen.rolling(YDAYS, min_periods=QDAYS).median()
    pd_dist = close.rolling(QDAYS, min_periods=MDAYS).apply(_h_dist_stage4_63, raw=True)
    pd_q25 = pd_dist.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    bs_min = _bars_since_true(low == rmin)
    pos = bs_min / float(YDAYS)
    ret = close.pct_change()
    sk = ret.rolling(QDAYS, min_periods=MDAYS).apply(_h_skew_kernel, raw=True)
    dd = _h_drawdown(high, close, YDAYS)
    ui = np.sqrt(((dd * 100.0) ** 2).rolling(QDAYS, min_periods=MDAYS).mean())
    ui_q75 = ui.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    return ((cs_widen > cs_med) & (pd_dist < pd_q25) & (pos > 0.85) & (sk < -0.5) & (ui > ui_q75) & (dd > 0.35)).astype(float).where(cs.notna() & sk.notna(), np.nan).diff().diff()

def f50_tdco_524_terminal_distribution_master_v4_score_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Master v4: weighted sum of new orthogonal signals — drawdown (weight 2), template-match-strength
    (weight 1.5), late-cycle (weight 1), neg-skew (weight 1), volume-distribution-index (weight 1.5),
    spread-widening (weight 1)."""
    dd = _h_drawdown(high, close, YDAYS).clip(lower=0)
    pd_dist = close.rolling(QDAYS, min_periods=MDAYS).apply(_h_dist_stage4_63, raw=True)
    pd_max = pd_dist.rolling(YDAYS, min_periods=QDAYS).max()
    pd_strength = 1.0 - _safe_div(pd_dist, pd_max)
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    bs_min = _bars_since_true(low == rmin)
    pos = bs_min / float(YDAYS)
    ret = close.pct_change()
    sk = ret.rolling(QDAYS, min_periods=MDAYS).apply(_h_skew_kernel, raw=True)
    neg_sk = (-sk).clip(lower=0)
    h252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    l252 = low.rolling(YDAYS, min_periods=QDAYS).min()
    rng = h252 - l252
    top_band = (close > l252 + 0.7 * rng).astype(float)
    bot_band = (close < l252 + 0.3 * rng).astype(float)
    vt = (volume * top_band).rolling(YDAYS, min_periods=QDAYS).sum()
    vb = (volume * bot_band).rolling(YDAYS, min_periods=QDAYS).sum()
    vall = volume.rolling(YDAYS, min_periods=QDAYS).sum()
    vd_idx = _safe_div(vt - vb, vall).clip(lower=0)
    cs = _h_corwin_schultz(high, low)
    cs_widen = (cs - cs.where(high == h252).ffill()).clip(lower=0)
    return (2.0 * dd.fillna(0) + 1.5 * pd_strength.fillna(0) + 1.0 * pos.fillna(0) + 1.0 * neg_sk.fillna(0) + 1.5 * vd_idx.fillna(0) + 1.0 * cs_widen.fillna(0)).where(cs.notna() & sk.notna(), np.nan).diff().diff()

def f50_tdco_525_absolute_terminal_stuck_v4_indicator_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Absolute v4 indicator: 1 if ALL of {dd > 60%, late-cycle (>0.85), template-match strong (dist<q25),
    skew < -0.5, kurt > 3, vol-dist-index > 0.3, ulcer > q75}."""
    dd = _h_drawdown(high, close, YDAYS)
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    bs_min = _bars_since_true(low == rmin)
    pos = bs_min / float(YDAYS)
    pd_dist = close.rolling(QDAYS, min_periods=MDAYS).apply(_h_dist_stage4_63, raw=True)
    pd_q25 = pd_dist.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    ret = close.pct_change()
    sk = ret.rolling(QDAYS, min_periods=MDAYS).apply(_h_skew_kernel, raw=True)
    kt = ret.rolling(QDAYS, min_periods=MDAYS).apply(_h_kurt_kernel, raw=True)
    h252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    l252 = low.rolling(YDAYS, min_periods=QDAYS).min()
    rng = h252 - l252
    top_band = (close > l252 + 0.7 * rng).astype(float)
    bot_band = (close < l252 + 0.3 * rng).astype(float)
    vt = (volume * top_band).rolling(YDAYS, min_periods=QDAYS).sum()
    vb = (volume * bot_band).rolling(YDAYS, min_periods=QDAYS).sum()
    vall = volume.rolling(YDAYS, min_periods=QDAYS).sum()
    vd_idx = _safe_div(vt - vb, vall)
    ui = np.sqrt(((dd * 100.0) ** 2).rolling(QDAYS, min_periods=MDAYS).mean())
    ui_q75 = ui.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    return ((dd > 0.6) & (pos > 0.85) & (pd_dist < pd_q25) & (sk < -0.5) & (kt > 3.0) & (vd_idx > 0.3) & (ui > ui_q75)).astype(float).where(sk.notna() & kt.notna(), np.nan).diff().diff()
TERMINAL_DISTRIBUTION_COMPOSITE_D2_REGISTRY_451_525 = {'f50_tdco_451_amihud_resilience_proxy_63_d2': {'inputs': ['close', 'volume'], 'func': f50_tdco_451_amihud_resilience_proxy_63_d2}, 'f50_tdco_452_amihud_acceleration_63_d2': {'inputs': ['close', 'volume'], 'func': f50_tdco_452_amihud_acceleration_63_d2}, 'f50_tdco_453_roll_spread_persistence_63_d2': {'inputs': ['close'], 'func': f50_tdco_453_roll_spread_persistence_63_d2}, 'f50_tdco_454_roll_spread_widening_post_peak_63_d2': {'inputs': ['high', 'close'], 'func': f50_tdco_454_roll_spread_widening_post_peak_63_d2}, 'f50_tdco_455_corwin_schultz_widening_post_peak_63_d2': {'inputs': ['high', 'low'], 'func': f50_tdco_455_corwin_schultz_widening_post_peak_63_d2}, 'f50_tdco_456_abdi_ranaldi_spread_widening_post_peak_63_d2': {'inputs': ['high', 'low', 'close'], 'func': f50_tdco_456_abdi_ranaldi_spread_widening_post_peak_63_d2}, 'f50_tdco_457_effective_tick_concentration_zscore_252_d2': {'inputs': ['close'], 'func': f50_tdco_457_effective_tick_concentration_zscore_252_d2}, 'f50_tdco_458_price_clustering_at_round_numbers_pct_63_d2': {'inputs': ['close'], 'func': f50_tdco_458_price_clustering_at_round_numbers_pct_63_d2}, 'f50_tdco_459_zero_volume_day_count_63_d2': {'inputs': ['volume'], 'func': f50_tdco_459_zero_volume_day_count_63_d2}, 'f50_tdco_460_trade_size_proxy_decay_63_d2': {'inputs': ['volume'], 'func': f50_tdco_460_trade_size_proxy_decay_63_d2}, 'f50_tdco_461_turnover_velocity_decay_zscore_252_d2': {'inputs': ['close', 'volume'], 'func': f50_tdco_461_turnover_velocity_decay_zscore_252_d2}, 'f50_tdco_462_volume_per_atr_decay_63_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f50_tdco_462_volume_per_atr_decay_63_d2}, 'f50_tdco_463_dollar_volume_to_market_cap_proxy_decay_63_d2': {'inputs': ['close', 'volume'], 'func': f50_tdco_463_dollar_volume_to_market_cap_proxy_decay_63_d2}, 'f50_tdco_464_effective_spread_proxy_2day_high_low_d2': {'inputs': ['high', 'low'], 'func': f50_tdco_464_effective_spread_proxy_2day_high_low_d2}, 'f50_tdco_465_quoted_spread_proxy_intraday_range_d2': {'inputs': ['high', 'low', 'close'], 'func': f50_tdco_465_quoted_spread_proxy_intraday_range_d2}, 'f50_tdco_466_dtw_distance_to_recent_50pct_dd_252_d2': {'inputs': ['high', 'close'], 'func': f50_tdco_466_dtw_distance_to_recent_50pct_dd_252_d2}, 'f50_tdco_467_dtw_distance_to_recent_252h_then_breakdown_252_d2': {'inputs': ['high', 'close'], 'func': f50_tdco_467_dtw_distance_to_recent_252h_then_breakdown_252_d2}, 'f50_tdco_468_pattern_match_score_recent_topping_63_d2': {'inputs': ['close'], 'func': f50_tdco_468_pattern_match_score_recent_topping_63_d2}, 'f50_tdco_469_dynamic_warping_drawdown_path_similarity_252_d2': {'inputs': ['high', 'close'], 'func': f50_tdco_469_dynamic_warping_drawdown_path_similarity_252_d2}, 'f50_tdco_470_path_similarity_to_stage_4_template_63_d2': {'inputs': ['close'], 'func': f50_tdco_470_path_similarity_to_stage_4_template_63_d2}, 'f50_tdco_471_path_similarity_to_blowoff_template_63_d2': {'inputs': ['close'], 'func': f50_tdco_471_path_similarity_to_blowoff_template_63_d2}, 'f50_tdco_472_path_similarity_to_distribution_template_63_d2': {'inputs': ['close'], 'func': f50_tdco_472_path_similarity_to_distribution_template_63_d2}, 'f50_tdco_473_path_similarity_to_failed_breakout_template_63_d2': {'inputs': ['close'], 'func': f50_tdco_473_path_similarity_to_failed_breakout_template_63_d2}, 'f50_tdco_474_path_similarity_to_capitulation_template_63_d2': {'inputs': ['close'], 'func': f50_tdco_474_path_similarity_to_capitulation_template_63_d2}, 'f50_tdco_475_self_similar_pattern_recurrence_count_504_d2': {'inputs': ['close'], 'func': f50_tdco_475_self_similar_pattern_recurrence_count_504_d2}, 'f50_tdco_476_self_similar_pattern_recurrence_recency_d2': {'inputs': ['close'], 'func': f50_tdco_476_self_similar_pattern_recurrence_recency_d2}, 'f50_tdco_477_pattern_attractor_strength_252_d2': {'inputs': ['close'], 'func': f50_tdco_477_pattern_attractor_strength_252_d2}, 'f50_tdco_478_multi_template_pattern_alignment_count_252_d2': {'inputs': ['close'], 'func': f50_tdco_478_multi_template_pattern_alignment_count_252_d2}, 'f50_tdco_479_historical_pattern_distance_aggregate_504_d2': {'inputs': ['close'], 'func': f50_tdco_479_historical_pattern_distance_aggregate_504_d2}, 'f50_tdco_480_pattern_persistence_after_match_252_d2': {'inputs': ['close'], 'func': f50_tdco_480_pattern_persistence_after_match_252_d2}, 'f50_tdco_481_distribution_signal_in_early_cycle_phase_count_252_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f50_tdco_481_distribution_signal_in_early_cycle_phase_count_252_d2}, 'f50_tdco_482_distribution_signal_in_late_cycle_phase_count_252_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f50_tdco_482_distribution_signal_in_late_cycle_phase_count_252_d2}, 'f50_tdco_483_distribution_signal_in_markdown_phase_count_252_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f50_tdco_483_distribution_signal_in_markdown_phase_count_252_d2}, 'f50_tdco_484_distribution_concentration_in_late_cycle_zscore_252_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f50_tdco_484_distribution_concentration_in_late_cycle_zscore_252_d2}, 'f50_tdco_485_cycle_position_normalized_distribution_count_252_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f50_tdco_485_cycle_position_normalized_distribution_count_252_d2}, 'f50_tdco_486_cycle_phase_consistency_with_distribution_signal_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f50_tdco_486_cycle_phase_consistency_with_distribution_signal_d2}, 'f50_tdco_487_cycle_completion_then_distribution_indicator_d2': {'inputs': ['high', 'close', 'volume'], 'func': f50_tdco_487_cycle_completion_then_distribution_indicator_d2}, 'f50_tdco_488_cycle_end_signal_count_252_d2': {'inputs': ['high', 'low', 'close'], 'func': f50_tdco_488_cycle_end_signal_count_252_d2}, 'f50_tdco_489_cycle_topping_pattern_score_252_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f50_tdco_489_cycle_topping_pattern_score_252_d2}, 'f50_tdco_490_cycle_terminal_phase_indicator_252_d2': {'inputs': ['high', 'low', 'close'], 'func': f50_tdco_490_cycle_terminal_phase_indicator_252_d2}, 'f50_tdco_491_value_area_high_proxy_252_d2': {'inputs': ['close'], 'func': f50_tdco_491_value_area_high_proxy_252_d2}, 'f50_tdco_492_value_area_low_proxy_252_d2': {'inputs': ['close'], 'func': f50_tdco_492_value_area_low_proxy_252_d2}, 'f50_tdco_493_close_above_value_area_high_state_d2': {'inputs': ['close'], 'func': f50_tdco_493_close_above_value_area_high_state_d2}, 'f50_tdco_494_close_below_value_area_low_state_d2': {'inputs': ['close'], 'func': f50_tdco_494_close_below_value_area_low_state_d2}, 'f50_tdco_495_point_of_control_proxy_252_d2': {'inputs': ['close'], 'func': f50_tdco_495_point_of_control_proxy_252_d2}, 'f50_tdco_496_close_distance_from_poc_zscore_252_d2': {'inputs': ['close'], 'func': f50_tdco_496_close_distance_from_poc_zscore_252_d2}, 'f50_tdco_497_value_area_widening_post_peak_63_d2': {'inputs': ['high', 'close'], 'func': f50_tdco_497_value_area_widening_post_peak_63_d2}, 'f50_tdco_498_value_area_skew_post_peak_63_d2': {'inputs': ['high', 'close'], 'func': f50_tdco_498_value_area_skew_post_peak_63_d2}, 'f50_tdco_499_volume_profile_top_concentration_252_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f50_tdco_499_volume_profile_top_concentration_252_d2}, 'f50_tdco_500_volume_profile_distribution_index_252_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f50_tdco_500_volume_profile_distribution_index_252_d2}, 'f50_tdco_501_returns_skew_evolution_post_peak_63_d2': {'inputs': ['high', 'close'], 'func': f50_tdco_501_returns_skew_evolution_post_peak_63_d2}, 'f50_tdco_502_returns_kurtosis_evolution_post_peak_63_d2': {'inputs': ['close'], 'func': f50_tdco_502_returns_kurtosis_evolution_post_peak_63_d2}, 'f50_tdco_503_returns_skew_shift_zscore_252_d2': {'inputs': ['close'], 'func': f50_tdco_503_returns_skew_shift_zscore_252_d2}, 'f50_tdco_504_returns_kurtosis_shift_zscore_252_d2': {'inputs': ['close'], 'func': f50_tdco_504_returns_kurtosis_shift_zscore_252_d2}, 'f50_tdco_505_returns_higher_moments_terminal_indicator_d2': {'inputs': ['close'], 'func': f50_tdco_505_returns_higher_moments_terminal_indicator_d2}, 'f50_tdco_506_returns_left_tail_thickening_post_peak_63_d2': {'inputs': ['close'], 'func': f50_tdco_506_returns_left_tail_thickening_post_peak_63_d2}, 'f50_tdco_507_returns_right_tail_decay_post_peak_63_d2': {'inputs': ['close'], 'func': f50_tdco_507_returns_right_tail_decay_post_peak_63_d2}, 'f50_tdco_508_returns_jarque_bera_stat_evolution_63_d2': {'inputs': ['close'], 'func': f50_tdco_508_returns_jarque_bera_stat_evolution_63_d2}, 'f50_tdco_509_returns_distribution_shift_pre_post_peak_d2': {'inputs': ['high', 'close'], 'func': f50_tdco_509_returns_distribution_shift_pre_post_peak_d2}, 'f50_tdco_510_returns_moment_alignment_terminal_signal_d2': {'inputs': ['close'], 'func': f50_tdco_510_returns_moment_alignment_terminal_signal_d2}, 'f50_tdco_511_sharpe_ratio_proxy_post_peak_63_d2': {'inputs': ['close'], 'func': f50_tdco_511_sharpe_ratio_proxy_post_peak_63_d2}, 'f50_tdco_512_sortino_ratio_proxy_post_peak_63_d2': {'inputs': ['close'], 'func': f50_tdco_512_sortino_ratio_proxy_post_peak_63_d2}, 'f50_tdco_513_calmar_ratio_proxy_post_peak_252_d2': {'inputs': ['high', 'close'], 'func': f50_tdco_513_calmar_ratio_proxy_post_peak_252_d2}, 'f50_tdco_514_information_ratio_decay_63_d2': {'inputs': ['close'], 'func': f50_tdco_514_information_ratio_decay_63_d2}, 'f50_tdco_515_risk_adjusted_breakdown_severity_63_d2': {'inputs': ['high', 'low', 'close'], 'func': f50_tdco_515_risk_adjusted_breakdown_severity_63_d2}, 'f50_tdco_516_risk_adjusted_recovery_failure_63_d2': {'inputs': ['high', 'close'], 'func': f50_tdco_516_risk_adjusted_recovery_failure_63_d2}, 'f50_tdco_517_risk_to_reward_ratio_decay_63_d2': {'inputs': ['high', 'close'], 'func': f50_tdco_517_risk_to_reward_ratio_decay_63_d2}, 'f50_tdco_518_vol_adjusted_drawdown_speed_63_d2': {'inputs': ['high', 'close'], 'func': f50_tdco_518_vol_adjusted_drawdown_speed_63_d2}, 'f50_tdco_519_sharpe_ratio_terminal_decay_252_d2': {'inputs': ['close'], 'func': f50_tdco_519_sharpe_ratio_terminal_decay_252_d2}, 'f50_tdco_520_ulcer_index_terminal_zscore_252_d2': {'inputs': ['high', 'close'], 'func': f50_tdco_520_ulcer_index_terminal_zscore_252_d2}, 'f50_tdco_521_batch_4_terminal_orthogonal_aggregate_zscore_252_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f50_tdco_521_batch_4_terminal_orthogonal_aggregate_zscore_252_d2}, 'f50_tdco_522_terminal_recall_optimized_v4_score_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f50_tdco_522_terminal_recall_optimized_v4_score_d2}, 'f50_tdco_523_terminal_precision_optimized_v4_score_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f50_tdco_523_terminal_precision_optimized_v4_score_d2}, 'f50_tdco_524_terminal_distribution_master_v4_score_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f50_tdco_524_terminal_distribution_master_v4_score_d2}, 'f50_tdco_525_absolute_terminal_stuck_v4_indicator_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f50_tdco_525_absolute_terminal_stuck_v4_indicator_d2}}