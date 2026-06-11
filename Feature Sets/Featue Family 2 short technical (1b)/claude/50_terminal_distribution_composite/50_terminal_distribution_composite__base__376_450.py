"""terminal_distribution_composite base features 376-450 — Pipeline 1b-technical.

Stuck-time + multi-resolution + cross-pattern + master scores.
75 distinct hypotheses targeting stuck-stock (-80% DD, no recovery > -50% in 5y).

P: stuck-stock-specific time signals (time since first ..., hazard, projection).
Q: multi-resolution / variance-ratio / wavelet proxy / scale aggregates.
R: cross-pattern interactions (Wyckoff x DD, candle x volume, etc.).
S: practitioner stuck signals (Worden, TC2000, StockCharts, O'Neill, Weinstein, Livermore, Lefevre).
T: ML-friendly entropy / complexity (sample, permutation, Hurst-DFA, Lempel-Ziv).
U: master ML aggregates (probability, recall/precision-optimized, orthogonal, terminal v3).

Inputs: SEP OHLCV. PIT-clean. Self-contained helpers at module top.
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
    xm = x.mean(); wm = wv.mean()
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


def _perm_entropy_kernel(w):
    """Permutation entropy, order 3, normalized [0, 1]. Used in rolling.apply(raw=True)."""
    if np.isnan(w).any() or len(w) < 6:
        return np.nan
    n = len(w)
    counts = {}
    for i in range(n - 2):
        a, b, c = w[i], w[i + 1], w[i + 2]
        # rank pattern as a tuple of ranks
        s = sorted(((a, 0), (b, 1), (c, 2)))
        pat = tuple(idx for _, idx in s)
        counts[pat] = counts.get(pat, 0) + 1
    total = sum(counts.values())
    if total == 0:
        return np.nan
    h = 0.0
    for k in counts.values():
        p = k / total
        if p > 0:
            h -= p * np.log(p)
    return h / np.log(6.0)  # 3! = 6


def _sample_entropy_kernel(w, m=2, r_mult=0.2):
    """Sample entropy of a vector w with embedding m=2, tolerance r = r_mult*std(w)."""
    if np.isnan(w).any() or len(w) < (m + 2):
        return np.nan
    sd = np.std(w)
    if sd == 0 or np.isnan(sd):
        return np.nan
    r = r_mult * sd
    n = len(w)
    def _phi(mm):
        x = np.array([w[i:i + mm] for i in range(n - mm + 1)])
        count = 0
        total = 0
        for i in range(len(x)):
            dist = np.max(np.abs(x - x[i]), axis=1)
            cnt = np.sum(dist <= r) - 1  # exclude self
            count += cnt
            total += len(x) - 1
        return count / total if total > 0 else np.nan
    a = _phi(m + 1)
    b = _phi(m)
    if a is None or b is None or np.isnan(a) or np.isnan(b) or b == 0 or a == 0:
        return np.nan
    return -np.log(a / b)


def _higuchi_fd_kernel(w, k_max=5):
    """Higuchi fractal dimension."""
    if np.isnan(w).any() or len(w) < 2 * k_max + 1:
        return np.nan
    n = len(w)
    lks = []
    log_ks = []
    for k in range(1, k_max + 1):
        lm = []
        for m in range(k):
            idx = np.arange(m, n, k)
            if len(idx) < 2:
                continue
            diffs = np.abs(np.diff(w[idx]))
            norm = (n - 1) / (((n - m - 1) // k) * k)
            lm.append(diffs.sum() * norm / k)
        if not lm:
            continue
        lk = np.mean(lm)
        if lk <= 0:
            continue
        lks.append(np.log(lk))
        log_ks.append(np.log(1.0 / k))
    if len(lks) < 2:
        return np.nan
    coeffs = np.polyfit(log_ks, lks, 1)
    return float(coeffs[0])


def _dfa_kernel(w, scale=10):
    """Detrended fluctuation analysis: returns single scaling exponent at given scale via cumulative-diff."""
    if np.isnan(w).any() or len(w) < 4 * scale:
        return np.nan
    n = len(w)
    y = np.cumsum(w - np.mean(w))
    n_seg = n // scale
    if n_seg < 2:
        return np.nan
    rms_list = []
    x = np.arange(scale, dtype=float)
    for i in range(n_seg):
        seg = y[i * scale:(i + 1) * scale]
        c = np.polyfit(x, seg, 1)
        trend = c[0] * x + c[1]
        rms_list.append(np.sqrt(np.mean((seg - trend) ** 2)))
    return float(np.mean(rms_list))


def _lempel_ziv_kernel(w):
    """Lempel-Ziv complexity on binary-encoded series (above/below median)."""
    if np.isnan(w).any() or len(w) < 4:
        return np.nan
    med = np.median(w)
    s = "".join("1" if x > med else "0" for x in w)
    n = len(s)
    i, c, k, kmax = 0, 1, 1, 1
    while True:
        if i + k > n:
            c += 1
            break
        sub1 = s[i:i + k]
        sub2 = s[:i + k - 1]
        if sub1 in sub2:
            k += 1
            if i + k > n:
                c += 1
                break
        else:
            c += 1
            if k > kmax:
                kmax = k
            i += k
            k = 1
            if i >= n:
                break
    return float(c / (n / np.log2(n))) if n > 1 else np.nan


def _rs_kernel(w):
    """Rescaled-range R/S statistic — Hurst-related persistence index."""
    if np.isnan(w).any() or len(w) < 8:
        return np.nan
    m = np.mean(w)
    y = np.cumsum(w - m)
    r = np.max(y) - np.min(y)
    s = np.std(w)
    if s == 0 or np.isnan(s):
        return np.nan
    return float(r / s)


# ============================================================
# P — stuck-stock-specific time signals (376-390)
# ============================================================

def f50_tdco_376_time_since_first_significant_lower_high_post_peak(high: pd.Series) -> pd.Series:
    """Bars since first 5d-high that is < 5d-high from 5 bars earlier AFTER the most-recent 252d peak.
    Time elapsed since first confirmed lower-high after peak."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    h5 = high.rolling(WDAYS, min_periods=2).max()
    lh = h5 < h5.shift(WDAYS)
    is_peak = (high == rmax)
    # find first lh after a peak: lh AND prior peak occurred (bars_since peak > 0)
    bs_peak = _bars_since_true(is_peak)
    first_lh = lh & (bs_peak > 0) & (bs_peak <= YDAYS)
    return _bars_since_true(first_lh)


def f50_tdco_377_time_since_first_close_below_sma200_post_peak(high: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since first close < SMA200 that occurred AFTER most-recent 252d peak."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    s200 = _sma(close, 200)
    bs_peak = _bars_since_true(high == rmax)
    ev = (close < s200) & (bs_peak > 0) & (bs_peak <= YDAYS)
    return _bars_since_true(ev)


def f50_tdco_378_time_since_first_20pct_drawdown_252(high: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since first time drawdown from 252d max exceeded 20% — bear-onset-to-20pct recency."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    return _bars_since_true(dd > 0.20)


def f50_tdco_379_time_since_first_30pct_drawdown_252(high: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since first time drawdown from 252d max exceeded 30% — deeper bear-onset recency."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    return _bars_since_true(dd > 0.30)


def f50_tdco_380_time_since_first_volume_climax_post_peak(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since first volume-climax (volume > 3x prior 50d avg) after most-recent 252d peak."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    bs_peak = _bars_since_true(high == rmax)
    ev = (volume > 3.0 * vavg) & (bs_peak > 0) & (bs_peak <= YDAYS)
    return _bars_since_true(ev)


def f50_tdco_381_time_since_first_distribution_cluster_post_peak(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since first occurrence of >=3 distribution days within 25 bars AFTER 252d peak."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    dd_count = ((ret < -0.002) & (volume > vavg)).astype(float).rolling(25, min_periods=10).sum()
    bs_peak = _bars_since_true(high == rmax)
    ev = (dd_count >= 3.0) & (bs_peak > 0) & (bs_peak <= YDAYS)
    return _bars_since_true(ev)


def f50_tdco_382_recovery_time_projection_252(high: pd.Series, close: pd.Series) -> pd.Series:
    """Avg historical recovery time (avg duration of drawdown episodes in past 504 bars) × current drawdown.
    Projection of how long to recover at average historical rate."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    in_dd = (dd > 0.05).astype(float)
    # avg duration of consecutive in_dd runs in past 504 bars
    streak = _streak_true(in_dd > 0)
    # mean of streak at every end of an episode: approximate via mean of streak max-per-episode over 504
    mean_streak = streak.rolling(DDAYS_2Y, min_periods=YDAYS).mean()
    return mean_streak * dd


def f50_tdco_383_time_in_stage_4_episode(close: pd.Series) -> pd.Series:
    """Current streak length of consecutive bars in Stage 4 (close < SMA30 AND SMA30 declining)."""
    s30 = _sma(close, 30)
    stage4 = (close < s30) & (s30 < s30.shift(30))
    return _streak_true(stage4).where(s30.notna(), np.nan)


def f50_tdco_384_time_in_drawdown_below_q90_252(high: pd.Series, close: pd.Series) -> pd.Series:
    """Current streak of consecutive bars with drawdown >= 90th percentile of past-252 drawdown distribution."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    q90 = dd.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    return _streak_true(dd >= q90).where(q90.notna(), np.nan)


def f50_tdco_385_age_current_lower_high_lower_low_regime(high: pd.Series, low: pd.Series) -> pd.Series:
    """Current streak of bars where simultaneously 5d-high < 5d-high.shift(5) AND 5d-low < 5d-low.shift(5)
    — full Dow-theory bearish regime age."""
    h5 = high.rolling(WDAYS, min_periods=2).max()
    l5 = low.rolling(WDAYS, min_periods=2).min()
    regime = (h5 < h5.shift(WDAYS)) & (l5 < l5.shift(WDAYS))
    return _streak_true(regime).where(h5.notna() & l5.notna(), np.nan)


def f50_tdco_386_age_current_below_sma200_episode_252(close: pd.Series) -> pd.Series:
    """Current streak of consecutive bars with close < SMA200 — below-major-trend episode age."""
    s200 = _sma(close, 200)
    return _streak_true(close < s200).where(s200.notna(), np.nan)


def f50_tdco_387_time_between_consecutive_breakdowns_avg_252(low: pd.Series, close: pd.Series) -> pd.Series:
    """In past 252: avg gap between consecutive break-21d-low events (close < prior 21d low first-occurrence after non-break).
    Computed as 252 / (number of breakdowns in 252) — smaller = more frequent."""
    ll21 = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    new_break = (close < ll21) & (close.shift(1) >= ll21.shift(1))
    cnt = new_break.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(float(YDAYS), cnt)


def f50_tdco_388_time_to_next_breakdown_hazard_proxy_252(low: pd.Series, close: pd.Series) -> pd.Series:
    """Hazard proxy: (count of breakdowns in past 252) / 252 — empirical hazard rate; higher = sooner next break."""
    ll21 = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    new_break = (close < ll21) & (close.shift(1) >= ll21.shift(1))
    cnt = new_break.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return cnt / float(YDAYS)


def f50_tdco_389_time_to_first_minus50_from_peak_if_yet(high: pd.Series, close: pd.Series) -> pd.Series:
    """Bars elapsed FROM most-recent 252d peak UNTIL first time drawdown > 50%. NaN if never reached yet.
    Latches when 50% threshold first crossed: returns (current i - peak i) at that crossing, frozen thereafter."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    bs_peak = _bars_since_true(high == rmax)
    first_cross = (dd > 0.50) & ~((dd > 0.50).shift(1).fillna(False))
    val = bs_peak.where(first_cross, np.nan)
    # forward-fill stays valid until next peak (when bs_peak resets to 0)
    return val.ffill().where(bs_peak.notna(), np.nan)


def f50_tdco_390_time_to_full_capitulation_proxy_252(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars from most-recent 252d peak until first 'capitulation' (vol > 3x avg AND return < -5%). NaN if not yet.
    Latches on first crossing, propagated until next peak."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    bs_peak = _bars_since_true(high == rmax)
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    ret = close.pct_change()
    cap = (volume > 3.0 * vavg) & (ret < -0.05) & (bs_peak > 0)
    first_cap = cap & ~cap.shift(1).fillna(False)
    val = bs_peak.where(first_cap, np.nan)
    return val.ffill().where(bs_peak.notna(), np.nan)


# ============================================================
# Q — multi-resolution / variance-ratio / wavelet (391-405)
# ============================================================

def f50_tdco_391_variance_ratio_test_2_5_proxy(close: pd.Series) -> pd.Series:
    """Variance ratio test: var(r_5)/5 / var(r_1) over 63d window — <1 mean-reverting, >1 trending."""
    r1 = close.pct_change()
    r5 = close.pct_change(WDAYS)
    v1 = r1.rolling(QDAYS, min_periods=MDAYS).var()
    v5 = r5.rolling(QDAYS, min_periods=MDAYS).var()
    return _safe_div(v5 / float(WDAYS), v1)


def f50_tdco_392_variance_ratio_test_5_21_proxy(close: pd.Series) -> pd.Series:
    """Variance ratio: var(r_21)/21 / var(r_5)/5 — long-vs-medium horizon ratio."""
    r5 = close.pct_change(WDAYS)
    r21 = close.pct_change(MDAYS)
    v5 = r5.rolling(QDAYS, min_periods=MDAYS).var()
    v21 = r21.rolling(QDAYS, min_periods=MDAYS).var()
    return _safe_div(v21 / float(MDAYS), v5 / float(WDAYS))


def f50_tdco_393_variance_ratio_test_21_63_proxy(close: pd.Series) -> pd.Series:
    """Variance ratio: var(r_63)/63 / var(r_21)/21 — very long horizon ratio."""
    r21 = close.pct_change(MDAYS)
    r63 = close.pct_change(QDAYS)
    v21 = r21.rolling(YDAYS, min_periods=QDAYS).var()
    v63 = r63.rolling(YDAYS, min_periods=QDAYS).var()
    return _safe_div(v63 / float(QDAYS), v21 / float(MDAYS))


def f50_tdco_394_variance_ratio_breakdown_indicator(close: pd.Series) -> pd.Series:
    """1 if VR(2,5) shifted from >1 (trending regime) to <1 (mean-reverting/breakdown regime) within past 63 bars."""
    r1 = close.pct_change()
    r5 = close.pct_change(WDAYS)
    v1 = r1.rolling(QDAYS, min_periods=MDAYS).var()
    v5 = r5.rolling(QDAYS, min_periods=MDAYS).var()
    vr = _safe_div(v5 / float(WDAYS), v1)
    was_high = (vr.shift(QDAYS) > 1.0)
    now_low = (vr < 1.0)
    return (was_high & now_low).astype(float).where(vr.notna(), np.nan)


def f50_tdco_395_multi_scale_volatility_decay_aggregate(close: pd.Series) -> pd.Series:
    """Aggregate: (vol_21 - vol_252) + (vol_63 - vol_252) summed; positive = short-term vol > long-term (decay)."""
    ret = close.pct_change()
    v21 = ret.rolling(MDAYS, min_periods=WDAYS).std()
    v63 = ret.rolling(QDAYS, min_periods=MDAYS).std()
    v252 = ret.rolling(YDAYS, min_periods=QDAYS).std()
    return (v21 - v252) + (v63 - v252)


def f50_tdco_396_multi_scale_drawdown_consistency(high: pd.Series, close: pd.Series) -> pd.Series:
    """Aggregate consistency: count of horizons {21, 63, 252} with drawdown > median historical — multi-scale DD consensus."""
    cnt = pd.Series(0.0, index=close.index)
    for n in (MDAYS, QDAYS, YDAYS):
        rmax = high.rolling(n, min_periods=max(n // 3, 5)).max()
        dd = _safe_div(rmax - close, rmax)
        med = dd.rolling(YDAYS, min_periods=QDAYS).median()
        cnt = cnt + (dd > med).astype(float).fillna(0)
    return cnt.where(close.notna(), np.nan)


def f50_tdco_397_wavelet_proxy_low_freq_component_decay(close: pd.Series) -> pd.Series:
    """Low-frequency wavelet proxy: 63d slope of close.rolling(63).mean() — long-trend rate-of-change.
    Strongly negative = decaying low-freq component (terminal decline)."""
    smooth = close.rolling(QDAYS, min_periods=MDAYS).mean()
    return _rolling_slope(smooth, QDAYS)


def f50_tdco_398_wavelet_proxy_high_freq_residual_amplitude(close: pd.Series) -> pd.Series:
    """High-frequency residual: std of (close - close.rolling(63).mean()) over 21 — high-freq amplitude."""
    smooth = close.rolling(QDAYS, min_periods=MDAYS).mean()
    resid = close - smooth
    return resid.rolling(MDAYS, min_periods=WDAYS).std()


def f50_tdco_399_multi_scale_topping_consensus(high: pd.Series) -> pd.Series:
    """Count of horizons {21, 63, 252} where high is currently within 1% of N-day max AND N-day max has been
    declining vs the prior N-day max (multi-scale topping)."""
    cnt = pd.Series(0.0, index=high.index)
    for n in (MDAYS, QDAYS, YDAYS):
        m = high.rolling(n, min_periods=max(n // 3, 5)).max()
        near = high >= 0.99 * m
        decl = m < m.shift(n)
        cnt = cnt + (near & decl).astype(float).fillna(0)
    return cnt.where(high.notna(), np.nan)


def f50_tdco_400_multi_scale_breakdown_consensus(low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of horizons {21, 63, 252} where close < prior N-day low — multi-scale breakdown consensus."""
    cnt = pd.Series(0.0, index=close.index)
    for n in (MDAYS, QDAYS, YDAYS):
        ll = low.shift(1).rolling(n, min_periods=max(n // 3, 5)).min()
        cnt = cnt + (close < ll).astype(float).fillna(0)
    return cnt.where(close.notna(), np.nan)


def f50_tdco_401_multi_resolution_distribution_score_aggregate(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum over horizons {25, 50, 100} of: distribution-day count in N — multi-scale distribution score."""
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    dd = ((ret < -0.002) & (volume > vavg)).astype(float)
    s = pd.Series(0.0, index=close.index)
    for n in (25, 50, 100):
        s = s + dd.rolling(n, min_periods=max(n // 3, 5)).sum().fillna(0)
    return s.where(vavg.notna(), np.nan)


def f50_tdco_402_multi_resolution_recovery_failure_aggregate(high: pd.Series, close: pd.Series) -> pd.Series:
    """Sum over horizons {21, 63, 252} of fraction of bounces (>5% in N bars) that failed to reach prior N-day high."""
    s = pd.Series(0.0, index=close.index)
    for n in (MDAYS, QDAYS, YDAYS):
        hN = high.shift(1).rolling(n, min_periods=max(n // 3, 5)).max()
        bounce = close.pct_change(WDAYS) > 0.05
        failed = bounce & (high < hN)
        b_cnt = bounce.astype(float).rolling(n, min_periods=max(n // 3, 5)).sum()
        f_cnt = failed.astype(float).rolling(n, min_periods=max(n // 3, 5)).sum()
        s = s + _safe_div(f_cnt, b_cnt).fillna(0)
    return s.where(close.notna(), np.nan)


def f50_tdco_403_multi_resolution_failure_pattern_count(high: pd.Series, close: pd.Series) -> pd.Series:
    """Count of horizons {5, 21, 63} where close just dropped below its N-day EMA for the first time
    in the past 5 bars — multi-resolution failure-of-EMA pattern."""
    cnt = pd.Series(0.0, index=close.index)
    for n in (WDAYS, MDAYS, QDAYS):
        em = _ema(close, n)
        cross = (close.shift(1) >= em.shift(1)) & (close < em)
        recent = cross.astype(float).rolling(WDAYS, min_periods=1).sum() > 0
        cnt = cnt + recent.astype(float).fillna(0)
    return cnt.where(close.notna(), np.nan)


def f50_tdco_404_multi_resolution_persistence_after_extreme(high: pd.Series, close: pd.Series) -> pd.Series:
    """Persistence after extreme: fraction of past {21, 63, 252} bars where drawdown > 20%, averaged across horizons."""
    s = pd.Series(0.0, index=close.index)
    cnt = 0
    for n in (MDAYS, QDAYS, YDAYS):
        rmax = high.rolling(n, min_periods=max(n // 3, 5)).max()
        dd = _safe_div(rmax - close, rmax)
        frac = (dd > 0.20).astype(float).rolling(n, min_periods=max(n // 3, 5)).mean()
        s = s + frac.fillna(0)
        cnt += 1
    return (s / float(cnt)).where(close.notna(), np.nan)


def f50_tdco_405_multi_resolution_post_peak_decay_aggregate(high: pd.Series, close: pd.Series) -> pd.Series:
    """Aggregate post-peak decay metric: sum over horizons {21, 63, 252} of (1 - close / N-day max) — multi-scale decay magnitude."""
    s = pd.Series(0.0, index=close.index)
    for n in (MDAYS, QDAYS, YDAYS):
        m = high.rolling(n, min_periods=max(n // 3, 5)).max()
        dec = _safe_div(m - close, m)
        s = s + dec.fillna(0)
    return s.where(close.notna(), np.nan)


# ============================================================
# R — cross-pattern interactions (406-420)
# ============================================================

def f50_tdco_406_wyckoff_plus_drawdown_combined_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if Wyckoff distribution proxy (close near high of past 63 AND vol > 1.5x avg) AND drawdown_63 > 10%."""
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    h63 = high.rolling(QDAYS, min_periods=MDAYS).max()
    near_hi = close >= 0.95 * h63
    heavy = volume > 1.5 * vavg
    rmax = high.rolling(QDAYS, min_periods=MDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    return (near_hi & heavy & (dd > 0.10)).astype(float).where(vavg.notna() & h63.notna(), np.nan)


def f50_tdco_407_distribution_day_plus_wyckoff_upthrust_count_63(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count in past 63 bars of (distribution-day AND Wyckoff upthrust: high > 21d high but close < 21d high)."""
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    dd = (ret < -0.002) & (volume > vavg)
    h21 = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    upthrust = (high > h21) & (close < h21)
    ev = (dd & upthrust).astype(float)
    return ev.rolling(QDAYS, min_periods=MDAYS).sum().where(vavg.notna() & h21.notna(), np.nan)


def f50_tdco_408_candle_pattern_plus_volume_confirmation_count_63(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count in past 63 of bearish candles (close < open AND upper shadow > 2x body) with volume > 1.5x avg."""
    body = (close - open).abs()
    upper = high - pd.concat([open.rename("a"), close.rename("b")], axis=1).max(axis=1)
    bearish_candle = (close < open) & (upper > 2.0 * body) & (body > 0)
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    confirmed = bearish_candle & (volume > 1.5 * vavg)
    return confirmed.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(vavg.notna(), np.nan)


def f50_tdco_409_multi_bar_pattern_plus_breakdown_count_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count in past 63 of (3-bar lower-high sequence) immediately followed by close < 21d-low — multi-bar pattern + breakdown."""
    h_lh = (high < high.shift(1)) & (high.shift(1) < high.shift(2))
    ll21 = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    brk = close < ll21
    ev = (h_lh & brk).astype(float)
    return ev.rolling(QDAYS, min_periods=MDAYS).sum().where(ll21.notna(), np.nan)


def f50_tdco_410_candle_plus_macd_failure_count_63(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count in past 63 of (bearish candle near 21d-high AND MACD-proxy declining: EMA12 - EMA26 falling)."""
    body = (close - open).abs()
    upper = high - pd.concat([open.rename("a"), close.rename("b")], axis=1).max(axis=1)
    bear = (close < open) & (upper > 2.0 * body)
    h21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    near_hi = high >= 0.95 * h21
    macd = _ema(close, 12) - _ema(close, 26)
    macd_decl = macd < macd.shift(WDAYS)
    ev = (bear & near_hi & macd_decl).astype(float)
    return ev.rolling(QDAYS, min_periods=MDAYS).sum().where(h21.notna() & macd.notna(), np.nan)


def f50_tdco_411_wyckoff_plus_chronic_weakness_signal(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if Wyckoff upthrust occurred in past 63 AND % bars below SMA50 > 0.6 in past 252 — distribution + chronic weakness."""
    h21 = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    upthrust = (high > h21) & (close < h21)
    upthrust_recent = upthrust.astype(float).rolling(QDAYS, min_periods=MDAYS).sum() > 0
    s50 = _sma(close, 50)
    weak = (close < s50).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    return (upthrust_recent & (weak > 0.6)).astype(float).where(h21.notna() & s50.notna(), np.nan)


def f50_tdco_412_candle_plus_drawdown_acceleration_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if bearish-engulfing-like candle (close < open AND today's open >= prior close AND today's close < prior open)
    AND drawdown-63 accelerating (63d slope > 0)."""
    engulf = (close < open) & (open >= close.shift(1)) & (close < open.shift(1)) & (open > close)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    dd_sl = _rolling_slope(dd, QDAYS)
    return (engulf & (dd_sl > 0)).astype(float).where(rmax.notna(), np.nan)


def f50_tdco_413_multi_bar_pattern_plus_stage_4_signal(low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 3-bar lower-low pattern AND in Stage 4 — multi-bar bearish + confirmed downtrend regime."""
    pattern_3 = (low < low.shift(1)) & (low.shift(1) < low.shift(2))
    s30 = _sma(close, 30)
    stage4 = (close < s30) & (s30 < s30.shift(30))
    return (pattern_3 & stage4).astype(float).where(s30.notna(), np.nan)


def f50_tdco_414_distribution_plus_post_peak_decay_signal(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if distribution-day-count(25) >= 4 AND bars-since-252d-peak between 21 and 126 — early-stage post-peak distribution."""
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    dd25 = ((ret < -0.002) & (volume > vavg)).astype(float).rolling(25, min_periods=10).sum()
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    bs = _bars_since_true(high == rmax)
    return ((dd25 >= 4.0) & (bs > MDAYS) & (bs <= 126)).astype(float).where(vavg.notna(), np.nan)


def f50_tdco_415_breakdown_plus_stage_4_alignment_signal(low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if today's close broke 63d-low AND we're in Stage 4 — major breakdown WITHIN confirmed downtrend."""
    ll63 = low.shift(1).rolling(QDAYS, min_periods=MDAYS).min()
    brk = close < ll63
    s30 = _sma(close, 30)
    stage4 = (close < s30) & (s30 < s30.shift(30))
    return (brk & stage4).astype(float).where(s30.notna() & ll63.notna(), np.nan)


def f50_tdco_416_wyckoff_plus_breakdown_severity_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite: (Wyckoff upthrust count past 63) × (breakdown-21d-low count past 21) — Wyckoff × breakdown severity."""
    h21 = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    upthrust = (high > h21) & (close < h21)
    up_cnt = upthrust.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    ll21 = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    brk = close < ll21
    brk_cnt = brk.astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    return (up_cnt * brk_cnt).where(h21.notna() & ll21.notna(), np.nan)


def f50_tdco_417_candle_plus_recovery_failure_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if shooting-star-like (upper shadow > 2x body AND close < open) AND in drawdown > 20% — bearish candle in bear regime."""
    body = (close - open).abs()
    upper = high - pd.concat([open.rename("a"), close.rename("b")], axis=1).max(axis=1)
    ss = (close < open) & (upper > 2.0 * body) & (body > 0)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    return (ss & (dd > 0.20)).astype(float).where(rmax.notna(), np.nan)


def f50_tdco_418_multi_bar_plus_terminal_pattern_score(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Score combining multi-bar patterns: lower-low-streak >= 3, lower-high-streak >= 3, close < SMA50 — sum."""
    h5 = high.rolling(WDAYS, min_periods=2).max()
    l5 = low.rolling(WDAYS, min_periods=2).min()
    lh_streak = _streak_true(h5 < h5.shift(WDAYS))
    ll_streak = _streak_true(l5 < l5.shift(WDAYS))
    s50 = _sma(close, 50)
    return ((lh_streak >= 3).astype(float).fillna(0)
            + (ll_streak >= 3).astype(float).fillna(0)
            + (close < s50).astype(float).fillna(0)).where(s50.notna(), np.nan)


def f50_tdco_419_distribution_plus_terminal_breakdown_score(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Score combining distribution + breakdown:
    {dist-25>=4, close<SMA200, broke-63d-low past-21, drawdown>30%} — sum."""
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    dd25 = ((ret < -0.002) & (volume > vavg)).astype(float).rolling(25, min_periods=10).sum()
    s200 = _sma(close, 200)
    ll63 = low.shift(1).rolling(QDAYS, min_periods=MDAYS).min()
    brk = (close < ll63).astype(float).rolling(MDAYS, min_periods=WDAYS).max()
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    drawdown = _safe_div(rmax - close, rmax)
    return ((dd25 >= 4.0).astype(float).fillna(0)
            + (close < s200).astype(float).fillna(0)
            + (brk > 0).astype(float).fillna(0)
            + (drawdown > 0.30).astype(float).fillna(0)).where(vavg.notna() & s200.notna(), np.nan)


def f50_tdco_420_cross_pattern_topping_intensity_aggregate(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Aggregate intensity: sum normalized by 5 of {upthrust-count63, breakdown-count21, distribution-count25,
    lower-high-streak, lower-low-streak} — multi-domain topping pressure."""
    h21 = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    upthrust = ((high > h21) & (close < h21)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    ll21 = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    brk = (close < ll21).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    dd25 = ((ret < -0.002) & (volume > vavg)).astype(float).rolling(25, min_periods=10).sum()
    h5 = high.rolling(WDAYS, min_periods=2).max()
    l5 = low.rolling(WDAYS, min_periods=2).min()
    lh_st = _streak_true(h5 < h5.shift(WDAYS))
    ll_st = _streak_true(l5 < l5.shift(WDAYS))
    # normalize each via clip then average
    return ((upthrust.clip(upper=10) / 10.0
             + brk.clip(upper=10) / 10.0
             + dd25.clip(upper=10) / 10.0
             + lh_st.clip(upper=15) / 15.0
             + ll_st.clip(upper=15) / 15.0) / 5.0).where(vavg.notna(), np.nan)


# ============================================================
# S — practitioner stuck signals (421-435)
# ============================================================

def f50_tdco_421_worden_hotlist_decline_pattern_proxy(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Worden hotlist decline pattern: 21d return < -10% AND 21d-avg-volume > 50d-avg-volume * 1.2 AND SMA50 declining."""
    r21 = close.pct_change(MDAYS)
    v21 = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    v50 = volume.rolling(50, min_periods=10).mean()
    s50 = _sma(close, 50)
    s50_decl = s50 < s50.shift(MDAYS)
    return ((r21 < -0.10) & (v21 > 1.2 * v50) & s50_decl).astype(float).where(s50.notna(), np.nan)


def f50_tdco_422_tc2000_stage_4_pattern_proxy(close: pd.Series) -> pd.Series:
    """TC2000 Stage-4 pattern proxy: close < SMA30wk (=SMA150d), close < SMA10wk (=SMA50d),
    SMA30wk declining — Stan Weinstein 30-week-MA convention via daily."""
    s150 = _sma(close, 150)
    s50 = _sma(close, 50)
    s150_decl = s150 < s150.shift(MDAYS)
    return ((close < s150) & (close < s50) & s150_decl).astype(float).where(s150.notna(), np.nan)


def f50_tdco_423_stockcharts_stage_4_criteria_proxy(close: pd.Series) -> pd.Series:
    """StockCharts Stage-4: close < 30wk SMA AND 30wk SMA slope < 0 (over 30 weeks = 150 trading days)."""
    s150 = _sma(close, 150)
    sl150 = _rolling_slope(s150, 150)
    return ((close < s150) & (sl150 < 0)).astype(float).where(sl150.notna(), np.nan)


def f50_tdco_424_cansim_failure_pattern_proxy(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """CANSLIM/breakout-failure: high broke 63d high in past 21 bars AND close has since fallen back below it
    AND breakdown occurred on heavy volume (vol > 1.5x avg on the failure bar) — failed breakout reverse."""
    h63 = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    new_high = (high > h63).astype(float).rolling(MDAYS, min_periods=1).max()
    fall_back = close < h63
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    heavy_fail = (close < low.shift(1)) & (volume > 1.5 * vavg)
    heavy_fail_recent = heavy_fail.astype(float).rolling(WDAYS, min_periods=1).max()
    return ((new_high > 0) & fall_back & (heavy_fail_recent > 0)).astype(float).where(h63.notna() & vavg.notna(), np.nan)


def f50_tdco_425_weinstein_stage_4_entry_proxy(close: pd.Series) -> pd.Series:
    """1 on first close < 30wk SMA (=SMA150) after a stage-3 period (SMA150 was flat with |slope|/close < 0.0005 for 30 prior bars)."""
    s150 = _sma(close, 150)
    sl150 = _rolling_slope(s150, 30)
    flat_prior = (sl150.shift(1).abs() / close.shift(1)) < 0.0005
    cross_down = (close.shift(1) >= s150.shift(1)) & (close < s150)
    return (cross_down & flat_prior).astype(float).where(s150.notna(), np.nan)


def f50_tdco_426_oneill_breakout_failure_count_252(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """O'Neill breakout-failure: count past-252 of (close > 63d-high then within 14 bars close < breakout level by > 8%)."""
    h63 = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    breakout = close > h63
    breakout_lvl = close.where(breakout)
    breakout_lvl_ff = breakout_lvl.ffill()
    bs_break = _bars_since_true(breakout)
    fail = (bs_break > 0) & (bs_break <= 14) & (close < 0.92 * breakout_lvl_ff)
    return fail.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(h63.notna(), np.nan)


def f50_tdco_427_oneill_climax_top_proxy(close: pd.Series) -> pd.Series:
    """O'Neill climax top: parabolic ascent (21d return > 25% AND 63d return > 50%) immediately followed by
    a reversal day (today's return < -3%) — exhaustion + reversal proxy."""
    r21 = close.pct_change(MDAYS)
    r63 = close.pct_change(QDAYS)
    parabolic = (r21.shift(1) > 0.25) & (r63.shift(1) > 0.50)
    reversal = close.pct_change() < -0.03
    return (parabolic & reversal).astype(float).where(r63.notna(), np.nan)


def f50_tdco_428_oneill_distribution_count_alert_state(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if distribution-day count in past 25 bars >= 5 — O'Neill IBD red-flag threshold."""
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    dd_count = ((ret < -0.002) & (volume > vavg)).astype(float).rolling(25, min_periods=10).sum()
    return (dd_count >= 5.0).astype(float).where(vavg.notna(), np.nan)


def f50_tdco_429_zweig_breadth_thrust_failure_indicator_proxy(close: pd.Series) -> pd.Series:
    """Zweig-breadth-thrust failure proxy (single-stock): 10d EMA of (1 if up else 0) goes from > 0.6 to < 0.4 within 10d."""
    up = (close.diff() > 0).astype(float)
    ema10 = _ema(up, 10)
    was_high = ema10.shift(10) > 0.6
    now_low = ema10 < 0.4
    return (was_high & now_low).astype(float).where(ema10.notna(), np.nan)


def f50_tdco_430_livermore_pivotal_top_indicator_proxy(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Livermore pivotal-point top: today's high > 21d high, today's close in bottom 30% of today's range,
    AND today's volume not known here — use range-position only (drop volume condition)."""
    h21 = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    new_hi = high > h21
    rng = high - low
    pos = _safe_div(close - low, rng)
    bottom_close = pos < 0.3
    return (new_hi & bottom_close).astype(float).where(h21.notna(), np.nan)


def f50_tdco_431_marc_chaikin_money_flow_failure_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Chaikin Money Flow proxy turning negative: CMF(20) was > 0.1 in past 20 bars but is now < -0.1."""
    mfm = _safe_div((close - low) - (high - close), high - low)
    mfv = mfm * volume
    cmf = mfv.rolling(20, min_periods=5).sum() / volume.rolling(20, min_periods=5).sum()
    was_pos = cmf.shift(20) > 0.1
    now_neg = cmf < -0.1
    return (was_pos & now_neg).astype(float).where(cmf.notna(), np.nan)


def f50_tdco_432_wyckoff_distribution_phase_complete_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Wyckoff distribution complete (proxy): all 3 of {upthrust in past 63, no-demand day in past 21, breakdown of 63d low}."""
    h21 = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    upthrust = ((high > h21) & (close < h21)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum() > 0
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    # no-demand: narrow range + below-avg volume + up-close-but-stuck
    rng = high - low
    rng_med = rng.rolling(MDAYS, min_periods=WDAYS).median()
    nd = (rng < 0.7 * rng_med) & (volume < 0.8 * vavg) & (close > close.shift(1))
    nd_recent = nd.astype(float).rolling(MDAYS, min_periods=WDAYS).sum() > 0
    ll63 = low.shift(1).rolling(QDAYS, min_periods=MDAYS).min()
    brk = close < ll63
    return (upthrust & nd_recent & brk).astype(float).where(vavg.notna() & ll63.notna(), np.nan)


def f50_tdco_433_weinstein_pretrend_breakdown_proxy(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Weinstein pre-trend breakdown: close cross down through SMA150 on volume > 1.5x avg — high-conviction stage-4 entry."""
    s150 = _sma(close, 150)
    cross_dn = (close.shift(1) >= s150.shift(1)) & (close < s150)
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    return (cross_dn & (volume > 1.5 * vavg)).astype(float).where(s150.notna() & vavg.notna(), np.nan)


def f50_tdco_434_lefevre_topping_pattern_proxy(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Lefevre topping pattern: 3 consecutive lower-highs, 3 consecutive lower-lows, AND close near 63d low — Reminiscences-style topping."""
    lh3 = (high < high.shift(1)) & (high.shift(1) < high.shift(2)) & (high.shift(2) < high.shift(3))
    ll3 = (low < low.shift(1)) & (low.shift(1) < low.shift(2)) & (low.shift(2) < low.shift(3))
    l63 = low.rolling(QDAYS, min_periods=MDAYS).min()
    near_low = close <= 1.05 * l63
    return (lh3 & ll3 & near_low).astype(float).where(l63.notna(), np.nan)


def f50_tdco_435_livermore_reaction_high_failure_indicator(high: pd.Series, close: pd.Series) -> pd.Series:
    """Livermore reaction-high failure: high reached >= 95% of prior 21d max but failed to exceed it for 5 bars,
    then close fell > 5% from that reaction high — failed reaction rally."""
    h21 = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    reaction = high >= 0.95 * h21
    failed = reaction.astype(float).rolling(WDAYS, min_periods=2).sum() >= 3
    drop = close.pct_change(WDAYS) < -0.05
    return (failed & drop).astype(float).where(h21.notna(), np.nan)


# ============================================================
# T — ML-friendly entropy / complexity (436-445)
# ============================================================

def f50_tdco_436_close_sample_entropy_21(close: pd.Series) -> pd.Series:
    """Sample entropy of close over 21d window — pattern complexity (higher = more random)."""
    return close.rolling(MDAYS, min_periods=10).apply(_sample_entropy_kernel, raw=True)


def f50_tdco_437_close_permutation_entropy_63_order3(close: pd.Series) -> pd.Series:
    """Permutation entropy (order 3) of close over 63d — ordinal-pattern complexity, normalized."""
    return close.rolling(QDAYS, min_periods=MDAYS).apply(_perm_entropy_kernel, raw=True)


def f50_tdco_438_close_multiscale_entropy_scale2(close: pd.Series) -> pd.Series:
    """Multi-scale entropy (scale 2): sample entropy on 2-bar smoothed close — sub-sampled complexity proxy."""
    coarse = close.rolling(2, min_periods=2).mean()
    return coarse.rolling(MDAYS, min_periods=10).apply(_sample_entropy_kernel, raw=True)


def f50_tdco_439_close_fractal_dimension_higuchi_63(close: pd.Series) -> pd.Series:
    """Higuchi fractal dimension of close over 63d — higher = rougher (more breakdown-prone)."""
    return close.rolling(QDAYS, min_periods=MDAYS).apply(_higuchi_fd_kernel, raw=True)


def f50_tdco_440_close_hurst_dfa_252(close: pd.Series) -> pd.Series:
    """Detrended-fluctuation-analysis Hurst proxy on close over 252d at scale 10."""
    return close.rolling(YDAYS, min_periods=QDAYS).apply(_dfa_kernel, raw=True)


def f50_tdco_441_close_lempel_ziv_complexity_63(close: pd.Series) -> pd.Series:
    """Lempel-Ziv complexity (normalized) on binary-encoded close over 63d."""
    return close.rolling(QDAYS, min_periods=MDAYS).apply(_lempel_ziv_kernel, raw=True)


def f50_tdco_442_returns_sample_entropy_63(close: pd.Series) -> pd.Series:
    """Sample entropy of returns over 63d — return-pattern complexity."""
    ret = close.pct_change()
    return ret.rolling(QDAYS, min_periods=MDAYS).apply(_sample_entropy_kernel, raw=True)


def f50_tdco_443_returns_permutation_entropy_63(close: pd.Series) -> pd.Series:
    """Permutation entropy (order 3) on returns over 63d."""
    ret = close.pct_change()
    return ret.rolling(QDAYS, min_periods=MDAYS).apply(_perm_entropy_kernel, raw=True)


def f50_tdco_444_returns_persistence_index_rs_63(close: pd.Series) -> pd.Series:
    """Rescaled-range R/S statistic on returns over 63d — Hurst-like persistence."""
    ret = close.pct_change()
    return ret.rolling(QDAYS, min_periods=MDAYS).apply(_rs_kernel, raw=True)


def f50_tdco_445_returns_predictability_horizon_63(close: pd.Series) -> pd.Series:
    """Predictability proxy: 1 - permutation_entropy_of_returns(63) — higher = more predictable
    (terminal regimes often have monotone bear drift = high predictability of down move)."""
    ret = close.pct_change()
    pe = ret.rolling(QDAYS, min_periods=MDAYS).apply(_perm_entropy_kernel, raw=True)
    return 1.0 - pe


# ============================================================
# U — master ML aggregates (446-450)
# ============================================================

def f50_tdco_446_stuck_probability_master_score_v3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Master probability proxy: sum of standardized {drawdown_252, dist-day-count-25, stage-4-persistence,
    multi-scale-breakdown-consensus, weinstein-stage-4} — broad stuck-stock probability composite v3."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax).clip(lower=0)
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    dd25 = ((ret < -0.002) & (volume > vavg)).astype(float).rolling(25, min_periods=10).sum()
    s30 = _sma(close, 30)
    stage4 = ((close < s30) & (s30 < s30.shift(30))).astype(float)
    stage4_pers = stage4.rolling(YDAYS, min_periods=QDAYS).mean()
    breakdown_cnt = pd.Series(0.0, index=close.index)
    for n in (MDAYS, QDAYS, YDAYS):
        ll = low.shift(1).rolling(n, min_periods=max(n // 3, 5)).min()
        breakdown_cnt = breakdown_cnt + (close < ll).astype(float).fillna(0)
    return (dd.fillna(0) + (dd25 / 10.0).fillna(0)
            + stage4_pers.fillna(0) + (breakdown_cnt / 3.0).fillna(0)
            + stage4.fillna(0)).where(s30.notna() & vavg.notna(), np.nan)


def f50_tdco_447_terminal_distribution_recall_optimized_score_v3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Recall-optimized: union-style OR of many weakly-correlated bearish signals — high recall, lower precision.
    Sum of indicators with low thresholds: {dd>10%, dist-day-count>=2, close<SMA50, lh-streak>=2, broke-21d-low}."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    dd25 = ((ret < -0.002) & (volume > vavg)).astype(float).rolling(25, min_periods=10).sum()
    s50 = _sma(close, 50)
    h5 = high.rolling(WDAYS, min_periods=2).max()
    lh_st = _streak_true(h5 < h5.shift(WDAYS))
    ll21 = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    return ((dd > 0.10).astype(float).fillna(0)
            + (dd25 >= 2).astype(float).fillna(0)
            + (close < s50).astype(float).fillna(0)
            + (lh_st >= 2).astype(float).fillna(0)
            + (close < ll21).astype(float).fillna(0)).where(s50.notna() & vavg.notna(), np.nan)


def f50_tdco_448_terminal_distribution_precision_optimized_score_v3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Precision-optimized: intersection-style AND of stringent conditions — low recall, high precision.
    1 if ALL of: dd>40%, dist-25>=6, stage-4, broke-63d-low past-21, weak: ema50 < ema200 ratio < 0.9."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    dd25 = ((ret < -0.002) & (volume > vavg)).astype(float).rolling(25, min_periods=10).sum()
    s30 = _sma(close, 30)
    stage4 = (close < s30) & (s30 < s30.shift(30))
    ll63 = low.shift(1).rolling(QDAYS, min_periods=MDAYS).min()
    brk = (close < ll63).astype(float).rolling(MDAYS, min_periods=WDAYS).max()
    e50 = _ema(close, 50)
    e200 = _ema(close, 200)
    weak = _safe_div(e50, e200) < 0.9
    return ((dd > 0.40) & (dd25 >= 6) & stage4 & (brk > 0) & weak).astype(float).where(s30.notna() & vavg.notna() & e200.notna(), np.nan)


def f50_tdco_449_stuck_pattern_orthogonal_aggregate_v3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Aggregate of orthogonal stuck patterns (5 independent dimensions): drawdown depth, time-underwater,
    institutional behavior, structural age, multi-resolution consistency — sum of standardized values."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax).clip(lower=0)
    # time-underwater fraction
    tu = (dd > 0.20).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    # institutional: stealth distribution count past 63
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    s21 = _sma(close, MDAYS)
    down = close.diff() < 0
    normal_vol = (volume >= 0.8 * vavg) & (volume <= 1.2 * vavg)
    stealth = (down & normal_vol & (close < s21)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    # structural age: bars below SMA200 streak / 252
    s200 = _sma(close, 200)
    age = _streak_true(close < s200) / float(YDAYS)
    # multi-res consistency: count horizons with dd > median
    cnt = pd.Series(0.0, index=close.index)
    for n in (MDAYS, QDAYS, YDAYS):
        rmax_n = high.rolling(n, min_periods=max(n // 3, 5)).max()
        dd_n = _safe_div(rmax_n - close, rmax_n)
        med_n = dd_n.rolling(YDAYS, min_periods=QDAYS).median()
        cnt = cnt + (dd_n > med_n).astype(float).fillna(0)
    return (dd.fillna(0) + tu.fillna(0) + (stealth / 10.0).fillna(0)
            + age.fillna(0) + (cnt / 3.0).fillna(0)).where(s200.notna() & vavg.notna(), np.nan)


def f50_tdco_450_absolute_terminal_stuck_indicator_extended_v3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Absolute v3 terminal-stuck indicator: requires hard combination of catastrophic decline + cascade + secular bear.
    1 if drawdown > 60% AND stage-4-age > 63 AND multi-scale-breakdown-count == 3 AND time-underwater-20pct-252 > 0.5."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    s30 = _sma(close, 30)
    stage4 = (close < s30) & (s30 < s30.shift(30))
    entry = stage4 & ~stage4.shift(1).fillna(False)
    age = _bars_since_true(entry)
    breakdown_cnt = pd.Series(0.0, index=close.index)
    for n in (MDAYS, QDAYS, YDAYS):
        ll = low.shift(1).rolling(n, min_periods=max(n // 3, 5)).min()
        breakdown_cnt = breakdown_cnt + (close < ll).astype(float).fillna(0)
    tu20 = (dd > 0.20).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    return ((dd > 0.60) & (age > 63) & (breakdown_cnt == 3) & (tu20 > 0.5)).astype(float).where(s30.notna(), np.nan)


# ============================================================
#                         REGISTRY 376-450
# ============================================================

TERMINAL_DISTRIBUTION_COMPOSITE_BASE_REGISTRY_376_450 = {
    "f50_tdco_376_time_since_first_significant_lower_high_post_peak": {"inputs": ["high"], "func": f50_tdco_376_time_since_first_significant_lower_high_post_peak},
    "f50_tdco_377_time_since_first_close_below_sma200_post_peak": {"inputs": ["high", "close"], "func": f50_tdco_377_time_since_first_close_below_sma200_post_peak},
    "f50_tdco_378_time_since_first_20pct_drawdown_252": {"inputs": ["high", "close"], "func": f50_tdco_378_time_since_first_20pct_drawdown_252},
    "f50_tdco_379_time_since_first_30pct_drawdown_252": {"inputs": ["high", "close"], "func": f50_tdco_379_time_since_first_30pct_drawdown_252},
    "f50_tdco_380_time_since_first_volume_climax_post_peak": {"inputs": ["high", "volume"], "func": f50_tdco_380_time_since_first_volume_climax_post_peak},
    "f50_tdco_381_time_since_first_distribution_cluster_post_peak": {"inputs": ["high", "close", "volume"], "func": f50_tdco_381_time_since_first_distribution_cluster_post_peak},
    "f50_tdco_382_recovery_time_projection_252": {"inputs": ["high", "close"], "func": f50_tdco_382_recovery_time_projection_252},
    "f50_tdco_383_time_in_stage_4_episode": {"inputs": ["close"], "func": f50_tdco_383_time_in_stage_4_episode},
    "f50_tdco_384_time_in_drawdown_below_q90_252": {"inputs": ["high", "close"], "func": f50_tdco_384_time_in_drawdown_below_q90_252},
    "f50_tdco_385_age_current_lower_high_lower_low_regime": {"inputs": ["high", "low"], "func": f50_tdco_385_age_current_lower_high_lower_low_regime},
    "f50_tdco_386_age_current_below_sma200_episode_252": {"inputs": ["close"], "func": f50_tdco_386_age_current_below_sma200_episode_252},
    "f50_tdco_387_time_between_consecutive_breakdowns_avg_252": {"inputs": ["low", "close"], "func": f50_tdco_387_time_between_consecutive_breakdowns_avg_252},
    "f50_tdco_388_time_to_next_breakdown_hazard_proxy_252": {"inputs": ["low", "close"], "func": f50_tdco_388_time_to_next_breakdown_hazard_proxy_252},
    "f50_tdco_389_time_to_first_minus50_from_peak_if_yet": {"inputs": ["high", "close"], "func": f50_tdco_389_time_to_first_minus50_from_peak_if_yet},
    "f50_tdco_390_time_to_full_capitulation_proxy_252": {"inputs": ["high", "close", "volume"], "func": f50_tdco_390_time_to_full_capitulation_proxy_252},
    "f50_tdco_391_variance_ratio_test_2_5_proxy": {"inputs": ["close"], "func": f50_tdco_391_variance_ratio_test_2_5_proxy},
    "f50_tdco_392_variance_ratio_test_5_21_proxy": {"inputs": ["close"], "func": f50_tdco_392_variance_ratio_test_5_21_proxy},
    "f50_tdco_393_variance_ratio_test_21_63_proxy": {"inputs": ["close"], "func": f50_tdco_393_variance_ratio_test_21_63_proxy},
    "f50_tdco_394_variance_ratio_breakdown_indicator": {"inputs": ["close"], "func": f50_tdco_394_variance_ratio_breakdown_indicator},
    "f50_tdco_395_multi_scale_volatility_decay_aggregate": {"inputs": ["close"], "func": f50_tdco_395_multi_scale_volatility_decay_aggregate},
    "f50_tdco_396_multi_scale_drawdown_consistency": {"inputs": ["high", "close"], "func": f50_tdco_396_multi_scale_drawdown_consistency},
    "f50_tdco_397_wavelet_proxy_low_freq_component_decay": {"inputs": ["close"], "func": f50_tdco_397_wavelet_proxy_low_freq_component_decay},
    "f50_tdco_398_wavelet_proxy_high_freq_residual_amplitude": {"inputs": ["close"], "func": f50_tdco_398_wavelet_proxy_high_freq_residual_amplitude},
    "f50_tdco_399_multi_scale_topping_consensus": {"inputs": ["high"], "func": f50_tdco_399_multi_scale_topping_consensus},
    "f50_tdco_400_multi_scale_breakdown_consensus": {"inputs": ["low", "close"], "func": f50_tdco_400_multi_scale_breakdown_consensus},
    "f50_tdco_401_multi_resolution_distribution_score_aggregate": {"inputs": ["close", "volume"], "func": f50_tdco_401_multi_resolution_distribution_score_aggregate},
    "f50_tdco_402_multi_resolution_recovery_failure_aggregate": {"inputs": ["high", "close"], "func": f50_tdco_402_multi_resolution_recovery_failure_aggregate},
    "f50_tdco_403_multi_resolution_failure_pattern_count": {"inputs": ["high", "close"], "func": f50_tdco_403_multi_resolution_failure_pattern_count},
    "f50_tdco_404_multi_resolution_persistence_after_extreme": {"inputs": ["high", "close"], "func": f50_tdco_404_multi_resolution_persistence_after_extreme},
    "f50_tdco_405_multi_resolution_post_peak_decay_aggregate": {"inputs": ["high", "close"], "func": f50_tdco_405_multi_resolution_post_peak_decay_aggregate},
    "f50_tdco_406_wyckoff_plus_drawdown_combined_indicator": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_406_wyckoff_plus_drawdown_combined_indicator},
    "f50_tdco_407_distribution_day_plus_wyckoff_upthrust_count_63": {"inputs": ["open", "high", "low", "close", "volume"], "func": f50_tdco_407_distribution_day_plus_wyckoff_upthrust_count_63},
    "f50_tdco_408_candle_pattern_plus_volume_confirmation_count_63": {"inputs": ["open", "high", "low", "close", "volume"], "func": f50_tdco_408_candle_pattern_plus_volume_confirmation_count_63},
    "f50_tdco_409_multi_bar_pattern_plus_breakdown_count_63": {"inputs": ["high", "low", "close"], "func": f50_tdco_409_multi_bar_pattern_plus_breakdown_count_63},
    "f50_tdco_410_candle_plus_macd_failure_count_63": {"inputs": ["open", "high", "low", "close"], "func": f50_tdco_410_candle_plus_macd_failure_count_63},
    "f50_tdco_411_wyckoff_plus_chronic_weakness_signal": {"inputs": ["high", "close", "volume"], "func": f50_tdco_411_wyckoff_plus_chronic_weakness_signal},
    "f50_tdco_412_candle_plus_drawdown_acceleration_signal": {"inputs": ["open", "high", "low", "close"], "func": f50_tdco_412_candle_plus_drawdown_acceleration_signal},
    "f50_tdco_413_multi_bar_pattern_plus_stage_4_signal": {"inputs": ["low", "close"], "func": f50_tdco_413_multi_bar_pattern_plus_stage_4_signal},
    "f50_tdco_414_distribution_plus_post_peak_decay_signal": {"inputs": ["high", "close", "volume"], "func": f50_tdco_414_distribution_plus_post_peak_decay_signal},
    "f50_tdco_415_breakdown_plus_stage_4_alignment_signal": {"inputs": ["low", "close"], "func": f50_tdco_415_breakdown_plus_stage_4_alignment_signal},
    "f50_tdco_416_wyckoff_plus_breakdown_severity_signal": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_416_wyckoff_plus_breakdown_severity_signal},
    "f50_tdco_417_candle_plus_recovery_failure_signal": {"inputs": ["open", "high", "low", "close"], "func": f50_tdco_417_candle_plus_recovery_failure_signal},
    "f50_tdco_418_multi_bar_plus_terminal_pattern_score": {"inputs": ["high", "low", "close"], "func": f50_tdco_418_multi_bar_plus_terminal_pattern_score},
    "f50_tdco_419_distribution_plus_terminal_breakdown_score": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_419_distribution_plus_terminal_breakdown_score},
    "f50_tdco_420_cross_pattern_topping_intensity_aggregate": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_420_cross_pattern_topping_intensity_aggregate},
    "f50_tdco_421_worden_hotlist_decline_pattern_proxy": {"inputs": ["close", "volume"], "func": f50_tdco_421_worden_hotlist_decline_pattern_proxy},
    "f50_tdco_422_tc2000_stage_4_pattern_proxy": {"inputs": ["close"], "func": f50_tdco_422_tc2000_stage_4_pattern_proxy},
    "f50_tdco_423_stockcharts_stage_4_criteria_proxy": {"inputs": ["close"], "func": f50_tdco_423_stockcharts_stage_4_criteria_proxy},
    "f50_tdco_424_cansim_failure_pattern_proxy": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_424_cansim_failure_pattern_proxy},
    "f50_tdco_425_weinstein_stage_4_entry_proxy": {"inputs": ["close"], "func": f50_tdco_425_weinstein_stage_4_entry_proxy},
    "f50_tdco_426_oneill_breakout_failure_count_252": {"inputs": ["high", "close", "volume"], "func": f50_tdco_426_oneill_breakout_failure_count_252},
    "f50_tdco_427_oneill_climax_top_proxy": {"inputs": ["close"], "func": f50_tdco_427_oneill_climax_top_proxy},
    "f50_tdco_428_oneill_distribution_count_alert_state": {"inputs": ["close", "volume"], "func": f50_tdco_428_oneill_distribution_count_alert_state},
    "f50_tdco_429_zweig_breadth_thrust_failure_indicator_proxy": {"inputs": ["close"], "func": f50_tdco_429_zweig_breadth_thrust_failure_indicator_proxy},
    "f50_tdco_430_livermore_pivotal_top_indicator_proxy": {"inputs": ["high", "low", "close"], "func": f50_tdco_430_livermore_pivotal_top_indicator_proxy},
    "f50_tdco_431_marc_chaikin_money_flow_failure_indicator": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_431_marc_chaikin_money_flow_failure_indicator},
    "f50_tdco_432_wyckoff_distribution_phase_complete_indicator": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_432_wyckoff_distribution_phase_complete_indicator},
    "f50_tdco_433_weinstein_pretrend_breakdown_proxy": {"inputs": ["close", "volume"], "func": f50_tdco_433_weinstein_pretrend_breakdown_proxy},
    "f50_tdco_434_lefevre_topping_pattern_proxy": {"inputs": ["high", "low", "close"], "func": f50_tdco_434_lefevre_topping_pattern_proxy},
    "f50_tdco_435_livermore_reaction_high_failure_indicator": {"inputs": ["high", "close"], "func": f50_tdco_435_livermore_reaction_high_failure_indicator},
    "f50_tdco_436_close_sample_entropy_21": {"inputs": ["close"], "func": f50_tdco_436_close_sample_entropy_21},
    "f50_tdco_437_close_permutation_entropy_63_order3": {"inputs": ["close"], "func": f50_tdco_437_close_permutation_entropy_63_order3},
    "f50_tdco_438_close_multiscale_entropy_scale2": {"inputs": ["close"], "func": f50_tdco_438_close_multiscale_entropy_scale2},
    "f50_tdco_439_close_fractal_dimension_higuchi_63": {"inputs": ["close"], "func": f50_tdco_439_close_fractal_dimension_higuchi_63},
    "f50_tdco_440_close_hurst_dfa_252": {"inputs": ["close"], "func": f50_tdco_440_close_hurst_dfa_252},
    "f50_tdco_441_close_lempel_ziv_complexity_63": {"inputs": ["close"], "func": f50_tdco_441_close_lempel_ziv_complexity_63},
    "f50_tdco_442_returns_sample_entropy_63": {"inputs": ["close"], "func": f50_tdco_442_returns_sample_entropy_63},
    "f50_tdco_443_returns_permutation_entropy_63": {"inputs": ["close"], "func": f50_tdco_443_returns_permutation_entropy_63},
    "f50_tdco_444_returns_persistence_index_rs_63": {"inputs": ["close"], "func": f50_tdco_444_returns_persistence_index_rs_63},
    "f50_tdco_445_returns_predictability_horizon_63": {"inputs": ["close"], "func": f50_tdco_445_returns_predictability_horizon_63},
    "f50_tdco_446_stuck_probability_master_score_v3": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_446_stuck_probability_master_score_v3},
    "f50_tdco_447_terminal_distribution_recall_optimized_score_v3": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_447_terminal_distribution_recall_optimized_score_v3},
    "f50_tdco_448_terminal_distribution_precision_optimized_score_v3": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_448_terminal_distribution_precision_optimized_score_v3},
    "f50_tdco_449_stuck_pattern_orthogonal_aggregate_v3": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_449_stuck_pattern_orthogonal_aggregate_v3},
    "f50_tdco_450_absolute_terminal_stuck_indicator_extended_v3": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_450_absolute_terminal_stuck_indicator_extended_v3},
}
