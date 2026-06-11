"""stochastic_williams_family base features 376-450 — Pipeline 1b-technical.

75 distinct "self-history rank + event-conditional + composites" hypotheses. Themes:
Within-own-history percentile rank (376-395),
Event-conditional stoch behavior (396-415),
Composite & ensemble across multi-oscillator universe (416-440),
Master/aggregate top scores (441-450).

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers — no cross-file imports.
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


def _ema(s, span, min_periods=None):
    if min_periods is None:
        min_periods = max(span // 2, 2)
    return s.ewm(span=span, adjust=False, min_periods=min_periods).mean()


def _stoch_k(high, low, close, n, smooth_k=1):
    ll = low.rolling(n, min_periods=max(n // 3, 2)).min()
    hh = high.rolling(n, min_periods=max(n // 3, 2)).max()
    k = 100.0 * _safe_div(close - ll, hh - ll)
    if smooth_k > 1:
        k = k.rolling(smooth_k, min_periods=max(smooth_k // 2, 1)).mean()
    return k


def _stoch_d(k, n_d):
    return k.rolling(n_d, min_periods=max(n_d // 2, 1)).mean()


def _williams_r(high, low, close, n):
    ll = low.rolling(n, min_periods=max(n // 3, 2)).min()
    hh = high.rolling(n, min_periods=max(n // 3, 2)).max()
    return -100.0 * _safe_div(hh - close, hh - ll)


def _rsi(close, n=14):
    delta = close.diff()
    up = delta.clip(lower=0)
    dn = (-delta).clip(lower=0)
    au = up.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    ad = dn.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    rs = _safe_div(au, ad)
    return 100.0 - 100.0 / (1.0 + rs)


def _stoch_rsi_k(close, n_rsi=14, n_k=14, smooth_k=3):
    r = _rsi(close, n_rsi)
    ll = r.rolling(n_k, min_periods=max(n_k // 3, 2)).min()
    hh = r.rolling(n_k, min_periods=max(n_k // 3, 2)).max()
    raw_k = 100.0 * _safe_div(r - ll, hh - ll)
    return raw_k.rolling(smooth_k, min_periods=max(smooth_k // 2, 1)).mean()


def _pct_rank(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    return s.rolling(window, min_periods=min_periods).apply(_rk, raw=True)


def _quantile_rolling(s, window, q, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    return s.rolling(window, min_periods=min_periods).quantile(q)


def _vwap_n(close, volume, n):
    pv = (close * volume).rolling(n, min_periods=max(n // 3, 2)).sum()
    vv = volume.rolling(n, min_periods=max(n // 3, 2)).sum()
    return _safe_div(pv, vv)


def _ultimate_osc(high, low, close):
    bp = close - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    tr = _true_range(high, low, close)
    a7 = bp.rolling(7, min_periods=3).sum() / tr.rolling(7, min_periods=3).sum().replace(0, np.nan)
    a14 = bp.rolling(14, min_periods=5).sum() / tr.rolling(14, min_periods=5).sum().replace(0, np.nan)
    a28 = bp.rolling(28, min_periods=10).sum() / tr.rolling(28, min_periods=10).sum().replace(0, np.nan)
    return 100.0 * (4 * a7 + 2 * a14 + a28) / 7.0


def _smi(high, low, close, n=14):
    mid = (high.rolling(n, min_periods=max(n // 3, 2)).max() + low.rolling(n, min_periods=max(n // 3, 2)).min()) / 2.0
    diff = close - mid
    hl = high.rolling(n, min_periods=max(n // 3, 2)).max() - low.rolling(n, min_periods=max(n // 3, 2)).min()
    return 100.0 * _safe_div(_ema(_ema(diff, 3), 3), 0.5 * _ema(_ema(hl, 3), 3))


def _all_oscillators(high, low, close):
    """Return dict of canonical oscillators used across composites."""
    k = _stoch_k(high, low, close, 14)
    wr = _williams_r(high, low, close, 14)
    sk = _stoch_rsi_k(close, 14, 14, 3)
    uo = _ultimate_osc(high, low, close)
    smi = _smi(high, low, close, 14)
    return {"k": k, "wr": wr, "sk": sk, "uo": uo, "smi": smi}


def _is_swing_high(high, n=5):
    """Pivot high: high[t-n] is max of high[t-2n..t]. Identifies past pivot at lag n."""
    rmax = high.rolling(2 * n + 1, min_periods=2 * n + 1).max()
    # is_pivot True at bar t when high[t-n] equals max of past 2n+1
    return (high.shift(n) == rmax) & rmax.notna()


def _is_swing_low(low, n=5):
    rmin = low.rolling(2 * n + 1, min_periods=2 * n + 1).min()
    return (low.shift(n) == rmin) & rmin.notna()


def _last_value_at_event(s, event_mask):
    """At each bar, value of s at most recent True in event_mask (forward-fill from event bars)."""
    return s.where(event_mask, np.nan).ffill()


# ============================================================
# Within-own-history percentile rank (376-395)
# ============================================================


def f26_stwf_376_stoch_pct_rank_within_504d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of Stoch K(14) within trailing 504d — long-history calibration."""
    k = _stoch_k(high, low, close, 14)
    return _pct_rank(k, DDAYS_2Y, min_periods=QDAYS) * 100.0


def f26_stwf_377_stoch_pct_rank_within_1260d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of Stoch K(14) within trailing 1260d (5y) — multi-year calibration."""
    k = _stoch_k(high, low, close, 14)
    return _pct_rank(k, DDAYS_5Y, min_periods=YDAYS) * 100.0


def f26_stwf_378_williams_r_pct_rank_within_504d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of Williams %R(14) within trailing 504d."""
    wr = _williams_r(high, low, close, 14)
    return _pct_rank(wr, DDAYS_2Y, min_periods=QDAYS) * 100.0


def f26_stwf_379_williams_r_pct_rank_within_1260d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of Williams %R(14) within trailing 1260d."""
    wr = _williams_r(high, low, close, 14)
    return _pct_rank(wr, DDAYS_5Y, min_periods=YDAYS) * 100.0


def f26_stwf_380_srsi_pct_rank_within_504d(close: pd.Series) -> pd.Series:
    """Percentile rank of Stoch RSI K within trailing 504d."""
    sk = _stoch_rsi_k(close, 14, 14, 3)
    return _pct_rank(sk, DDAYS_2Y, min_periods=QDAYS) * 100.0


def f26_stwf_381_stoch_above_own_q95_504_state(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if Stoch K(14) > own 504d 95th percentile."""
    k = _stoch_k(high, low, close, 14)
    q = _quantile_rolling(k, DDAYS_2Y, 0.95, min_periods=QDAYS)
    return (k > q).astype(float).where(q.notna(), np.nan)


def f26_stwf_382_stoch_above_own_q99_1260_state(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if Stoch K(14) > own 1260d 99th percentile — extremely rare event."""
    k = _stoch_k(high, low, close, 14)
    q = _quantile_rolling(k, DDAYS_5Y, 0.99, min_periods=YDAYS)
    return (k > q).astype(float).where(q.notna(), np.nan)


def f26_stwf_383_stoch_within_vol_bucketed_history_q90(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rank K within bars of similar vol regime: separate q90 for low-vol vs high-vol historical bars."""
    k = _stoch_k(high, low, close, 14)
    vol = close.pct_change().rolling(QDAYS, min_periods=MDAYS).std()
    med = vol.rolling(DDAYS_2Y, min_periods=QDAYS).median()
    hi_vol = (vol > med).astype(float)
    # rolling 504d quantile of K conditional on bucket: use weighted approximation
    k_low_only = k.where(hi_vol == 0, np.nan)
    k_high_only = k.where(hi_vol == 1, np.nan)
    q_low = _quantile_rolling(k_low_only, DDAYS_2Y, 0.90, min_periods=QDAYS)
    q_high = _quantile_rolling(k_high_only, DDAYS_2Y, 0.90, min_periods=QDAYS)
    return q_low.where(hi_vol == 0.0, q_high).where(hi_vol.notna(), np.nan)


def f26_stwf_384_stoch_within_price_bucketed_history_q90(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rank K within bars of similar price level: separate q90 for low-half vs high-half of 504d range."""
    k = _stoch_k(high, low, close, 14)
    p_med = close.rolling(DDAYS_2Y, min_periods=QDAYS).median()
    above = (close > p_med).astype(float)
    k_below = k.where(above == 0, np.nan)
    k_above = k.where(above == 1, np.nan)
    q_below = _quantile_rolling(k_below, DDAYS_2Y, 0.90, min_periods=QDAYS)
    q_above = _quantile_rolling(k_above, DDAYS_2Y, 0.90, min_periods=QDAYS)
    return q_below.where(above == 0.0, q_above).where(above.notna(), np.nan)


def f26_stwf_385_stoch_within_trend_bucketed_history_q90(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rank K within bars of similar-trend regime: separate q90 for up-trend (close>SMA200) vs down-trend."""
    k = _stoch_k(high, low, close, 14)
    sma200 = close.rolling(200, min_periods=63).mean()
    up = (close > sma200).astype(float)
    k_dn = k.where(up == 0, np.nan)
    k_up = k.where(up == 1, np.nan)
    q_dn = _quantile_rolling(k_dn, DDAYS_2Y, 0.90, min_periods=QDAYS)
    q_up = _quantile_rolling(k_up, DDAYS_2Y, 0.90, min_periods=QDAYS)
    return q_dn.where(up == 0.0, q_up).where(up.notna(), np.nan)


def f26_stwf_386_stoch_dwell_above_own_q90_504_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of past 63 bars where K > own 504d q90 — self-calibrated dwell."""
    k = _stoch_k(high, low, close, 14)
    q = _quantile_rolling(k, DDAYS_2Y, 0.90, min_periods=QDAYS)
    above = (k > q).astype(float)
    return above.rolling(QDAYS, min_periods=MDAYS).mean().where(q.notna(), np.nan)


def f26_stwf_387_stoch_consecutive_above_own_q90_504_streak(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current consecutive-streak length of bars where K > own 504d q90."""
    k = _stoch_k(high, low, close, 14)
    q = _quantile_rolling(k, DDAYS_2Y, 0.90, min_periods=QDAYS)
    return _streak_true(k > q).where(q.notna(), np.nan)


def f26_stwf_388_stoch_first_breach_of_own_q99_504_age(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since most recent breach of own 504d q99 (rare event)."""
    k = _stoch_k(high, low, close, 14)
    q = _quantile_rolling(k, DDAYS_2Y, 0.99, min_periods=QDAYS)
    return _bars_since_true(k > q).where(q.notna(), np.nan)


def f26_stwf_389_stoch_pct_rank_decay_velocity_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Velocity of K-percentile-rank decay over 63d: pct_rank(504) - pct_rank(504).shift(63)."""
    k = _stoch_k(high, low, close, 14)
    pr = _pct_rank(k, DDAYS_2Y, min_periods=QDAYS)
    return pr - pr.shift(QDAYS)


def f26_stwf_390_stoch_dispersion_within_own_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Standard deviation of K(14) within trailing 252d — measures historical oscillator volatility."""
    k = _stoch_k(high, low, close, 14)
    return k.rolling(YDAYS, min_periods=QDAYS).std()


def f26_stwf_391_stoch_distance_from_own_median_504d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(K - 504d median K) / 504d std K — robust z-score of K vs own history."""
    k = _stoch_k(high, low, close, 14)
    med = k.rolling(DDAYS_2Y, min_periods=QDAYS).median()
    sd = k.rolling(DDAYS_2Y, min_periods=QDAYS).std().replace(0, np.nan)
    return _safe_div(k - med, sd)


def f26_stwf_392_stoch_skew_within_own_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 252d skewness of K(14) — distribution shape (negative = OB-clustered)."""
    k = _stoch_k(high, low, close, 14)
    return k.rolling(YDAYS, min_periods=QDAYS).skew()


def f26_stwf_393_stoch_kurtosis_within_own_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 252d excess kurtosis of K(14) — fat-tail measure."""
    k = _stoch_k(high, low, close, 14)
    return k.rolling(YDAYS, min_periods=QDAYS).kurt()


def f26_stwf_394_williams_r_distribution_shift_zscore_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score: (mean WR over recent 63d - mean WR over prior 189d) / pooled std — distribution shift."""
    wr = _williams_r(high, low, close, 14)
    recent = wr.rolling(QDAYS, min_periods=MDAYS).mean()
    prior = wr.shift(QDAYS).rolling(189, min_periods=QDAYS).mean()
    sd_all = wr.rolling(YDAYS, min_periods=QDAYS).std().replace(0, np.nan)
    return _safe_div(recent - prior, sd_all)


def f26_stwf_395_stoch_distribution_shift_indicator_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """KS-test-like indicator: max gap between recent (63d) and distant (189d) CDFs of K."""
    k = _stoch_k(high, low, close, 14)
    def _ks(w):
        v = w[~np.isnan(w)]
        if v.size < 100:
            return np.nan
        recent = v[-QDAYS:]
        prior = v[-(QDAYS + 189):-QDAYS]
        if recent.size < 21 or prior.size < 21:
            return np.nan
        thresholds = np.linspace(0, 100, 21)
        max_gap = 0.0
        for thr in thresholds:
            cdf_r = float((recent <= thr).sum()) / recent.size
            cdf_p = float((prior <= thr).sum()) / prior.size
            gap = abs(cdf_r - cdf_p)
            if gap > max_gap:
                max_gap = gap
        return max_gap
    return k.rolling(YDAYS, min_periods=YDAYS).apply(_ks, raw=True)


# ============================================================
# Event-conditional stoch behavior (396-415)
# ============================================================


def f26_stwf_396_stoch_at_sma50_cross_above_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Value of Stoch K(14) at most recent close-crosses-above-SMA50 event (held forward)."""
    k = _stoch_k(high, low, close, 14)
    sma50 = close.rolling(50, min_periods=15).mean()
    cross = (close.shift(1) <= sma50.shift(1)) & (close > sma50)
    return _last_value_at_event(k, cross)


def f26_stwf_397_stoch_at_sma200_cross_above_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Value of Stoch K(14) at most recent close-crosses-above-SMA200 event."""
    k = _stoch_k(high, low, close, 14)
    sma200 = close.rolling(200, min_periods=63).mean()
    cross = (close.shift(1) <= sma200.shift(1)) & (close > sma200)
    return _last_value_at_event(k, cross)


def f26_stwf_398_stoch_at_gap_up_event_value(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Value of Stoch K(14) at most recent gap-up event (today's low > yesterday's high)."""
    k = _stoch_k(high, low, close, 14)
    gap_up = low > high.shift(1)
    return _last_value_at_event(k, gap_up)


def f26_stwf_399_stoch_at_gap_down_event_value(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Value of Stoch K(14) at most recent gap-down event (today's high < yesterday's low)."""
    k = _stoch_k(high, low, close, 14)
    gap_dn = high < low.shift(1)
    return _last_value_at_event(k, gap_dn)


def f26_stwf_400_stoch_at_volume_spike_event_value(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Value of Stoch K(14) at most recent volume-spike event (volume > 3x SMA21(volume))."""
    k = _stoch_k(high, low, close, 14)
    spike = volume > 3.0 * volume.rolling(MDAYS, min_periods=WDAYS).mean()
    return _last_value_at_event(k, spike)


def f26_stwf_401_stoch_after_first_distribution_day_21(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """K(14) value 21 bars after most recent distribution day (>1% decline on above-avg volume)."""
    k = _stoch_k(high, low, close, 14)
    ret = close.pct_change()
    avg_v = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    dist = (ret < -0.01) & (volume > avg_v)
    dist_shifted = dist.shift(MDAYS).fillna(False)
    return _last_value_at_event(k, dist_shifted)


def f26_stwf_402_stoch_at_first_lower_high_post_peak(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """K(14) value at most recent swing pivot high (5-bar pivot) that is LOWER than the prior swing pivot."""
    k = _stoch_k(high, low, close, 14)
    pivot = _is_swing_high(high, n=3).fillna(False)
    # capture pivot-high values
    pivot_val = high.shift(3).where(pivot, np.nan)
    prior_pivot_val = pivot_val.shift(1).ffill()
    lower_pivot = pivot & (pivot_val < prior_pivot_val)
    return _last_value_at_event(k, lower_pivot.fillna(False))


def f26_stwf_403_stoch_at_252h_value(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Value of Stoch K(14) at most recent 252d-high event (close >= close.rolling(252).max())."""
    k = _stoch_k(high, low, close, 14)
    is_252h = close >= close.rolling(YDAYS, min_periods=QDAYS).max()
    return _last_value_at_event(k, is_252h.fillna(False))


def f26_stwf_404_williams_r_at_252h_value(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Value of Williams %R(14) at most recent 252d-high event."""
    wr = _williams_r(high, low, close, 14)
    is_252h = close >= close.rolling(YDAYS, min_periods=QDAYS).max()
    return _last_value_at_event(wr, is_252h.fillna(False))


def f26_stwf_405_stoch_post_breakdown_failed_recovery_count_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of breakdowns (close < SMA50) in past 63d where K failed to retest 80 in next 21 bars."""
    k = _stoch_k(high, low, close, 14)
    sma50 = close.rolling(50, min_periods=15).mean()
    breakdown = (close.shift(1) >= sma50.shift(1)) & (close < sma50)
    # at bar t, did breakdown happen at t-21 AND K never hit 80 in t-20..t?
    bd_shifted = breakdown.shift(MDAYS).fillna(False).astype(float)
    max_next = k.rolling(MDAYS, min_periods=1).max()
    failed = (bd_shifted > 0) & (max_next < 80.0)
    return failed.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(k.notna(), np.nan)


def f26_stwf_406_stoch_post_breakdown_zone_persistence(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of past 63 bars where K < 60 AND close < SMA50 — post-breakdown stuck-in-weak-zone."""
    k = _stoch_k(high, low, close, 14)
    sma50 = close.rolling(50, min_periods=15).mean()
    weak = (k < 60.0) & (close < sma50)
    return weak.astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(k.notna(), np.nan)


def f26_stwf_407_stoch_at_atr_expansion_event_value(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """K(14) value at most recent ATR-expansion event (ATR21 > 1.5x ATR21.shift(21))."""
    k = _stoch_k(high, low, close, 14)
    atr = _atr(high, low, close, MDAYS)
    expand = atr > 1.5 * atr.shift(MDAYS)
    return _last_value_at_event(k, expand.fillna(False))


def f26_stwf_408_stoch_at_atr_contraction_event_value(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """K(14) value at most recent ATR-contraction event (ATR21 < 0.66x ATR21.shift(21))."""
    k = _stoch_k(high, low, close, 14)
    atr = _atr(high, low, close, MDAYS)
    contract = atr < 0.66 * atr.shift(MDAYS)
    return _last_value_at_event(k, contract.fillna(False))


def f26_stwf_409_stoch_when_high_volume_down_day(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """K(14) value on most recent high-volume down day (volume > 1.5x SMA21 AND close < open)."""
    k = _stoch_k(high, low, close, 14)
    avg_v = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    # use close.shift(1) as proxy for open since open not in signature
    down = close < close.shift(1)
    spike = volume > 1.5 * avg_v
    return _last_value_at_event(k, (spike & down).fillna(False))


def f26_stwf_410_stoch_when_low_volume_up_day(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """K(14) value on most recent low-volume up day (volume < 0.7x SMA21 AND close > close.shift(1))."""
    k = _stoch_k(high, low, close, 14)
    avg_v = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    up = close > close.shift(1)
    quiet = volume < 0.7 * avg_v
    return _last_value_at_event(k, (quiet & up).fillna(False))


def f26_stwf_411_stoch_when_widerange_red_bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """K(14) value on most recent wide-range red bar: (high-low) > 1.5*ATR21 AND close < close.shift(1)."""
    k = _stoch_k(high, low, close, 14)
    atr = _atr(high, low, close, MDAYS)
    wide = (high - low) > 1.5 * atr
    red = close < close.shift(1)
    return _last_value_at_event(k, (wide & red).fillna(False))


def f26_stwf_412_stoch_at_swing_high_value(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """K(14) value at most recent 5-bar swing-pivot high event (uses high.shift(5) pivot identification)."""
    k = _stoch_k(high, low, close, 14)
    pivot = _is_swing_high(high, n=5).fillna(False)
    return _last_value_at_event(k, pivot)


def f26_stwf_413_stoch_at_swing_low_value(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """K(14) value at most recent 5-bar swing-pivot low event."""
    k = _stoch_k(high, low, close, 14)
    pivot = _is_swing_low(low, n=5).fillna(False)
    return _last_value_at_event(k, pivot)


def f26_stwf_414_stoch_during_consolidation_phase_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if low-vol consolidation: (21d range / 21d close mean) < 0.10 — sideways stoch is meaningless here."""
    rng21 = high.rolling(MDAYS, min_periods=WDAYS).max() - low.rolling(MDAYS, min_periods=WDAYS).min()
    mean21 = close.rolling(MDAYS, min_periods=WDAYS).mean()
    return (_safe_div(rng21, mean21) < 0.10).astype(float).where(mean21.notna(), np.nan)


def f26_stwf_415_stoch_at_breakout_failure_event_value(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """K(14) value at most recent breakout-failure event: close crosses ABOVE 21d-high then BELOW within 5 bars."""
    k = _stoch_k(high, low, close, 14)
    h21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    breakout = (close.shift(1) <= h21.shift(1)) & (close > h21)
    # at bar t, did breakout happen at t-5..t-1 AND close[t] < h21[t-5]?
    bd_in_window = breakout.rolling(5, min_periods=1).max() > 0
    bk_level = h21.shift(5)
    failure = bd_in_window & (close < bk_level)
    return _last_value_at_event(k, failure.fillna(False))


# ============================================================
# Composite & ensemble (416-440)
# ============================================================


def f26_stwf_416_modern_classical_stoch_basket_avg_zscore_504(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Average 504d z-score across K, WR, SRSI, UO, SMI basket — universe-level distance from norm."""
    o = _all_oscillators(high, low, close)
    z_list = [_rolling_zscore(s, DDAYS_2Y, min_periods=QDAYS) for s in o.values()]
    df = pd.concat([z.rename(i) for i, z in enumerate(z_list)], axis=1)
    return df.mean(axis=1)


def f26_stwf_417_modern_classical_stoch_basket_extreme_count_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of basket oscillators with z-score > 2 over 252d — extreme-state breadth."""
    o = _all_oscillators(high, low, close)
    cnt = pd.Series(0.0, index=close.index)
    for s in o.values():
        z = _rolling_zscore(s, YDAYS, min_periods=QDAYS)
        cnt = cnt + (z > 2.0).astype(float).fillna(0)
    return cnt


def f26_stwf_418_modern_classical_stoch_basket_bearish_alignment_count(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of basket oscillators currently below their own 21d max (turn-down alignment)."""
    o = _all_oscillators(high, low, close)
    cnt = pd.Series(0.0, index=close.index)
    for s in o.values():
        mx = s.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
        cnt = cnt + (s < mx).astype(float).fillna(0)
    return cnt


def f26_stwf_419_oscillator_universe_correlation_breakdown_zscore_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of pairwise correlation collapse: drop in avg pair-corr of basket vs 252d avg."""
    o = _all_oscillators(high, low, close)
    keys = list(o.keys())
    # rolling pair corr avg over 63d
    pair_corrs = []
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            a = o[keys[i]]; b = o[keys[j]]
            c = a.rolling(QDAYS, min_periods=MDAYS).corr(b)
            pair_corrs.append(c)
    avg = pd.concat([c.rename(idx) for idx, c in enumerate(pair_corrs)], axis=1).mean(axis=1)
    z = _rolling_zscore(avg, YDAYS, min_periods=QDAYS)
    # breakdown = negative z (corr lower than typical)
    return -z


def f26_stwf_420_oscillator_universe_decay_velocity_post_peak_aggregate(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Avg decay velocity across basket: mean of (osc - osc_21d_max)/bars_since_max."""
    o = _all_oscillators(high, low, close)
    vels = []
    for s in o.values():
        peak = s.rolling(MDAYS, min_periods=WDAYS).max()
        bars = _bars_since_true(s >= peak)
        vels.append(_safe_div(s - peak, bars.where(bars > 0, np.nan)))
    df = pd.concat([v.rename(i) for i, v in enumerate(vels)], axis=1)
    return df.mean(axis=1)


def f26_stwf_421_oscillator_universe_failure_breadth_at_top_score(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """At 63d new close-high: count of basket oscillators failing to make 63d new high — breadth-of-failure."""
    o = _all_oscillators(high, low, close)
    p_new = close >= close.rolling(QDAYS, min_periods=MDAYS).max()
    cnt = pd.Series(0.0, index=close.index)
    for s in o.values():
        smax = s.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
        cnt = cnt + ((s < smax) & p_new).astype(float).fillna(0)
    return cnt.where(p_new, np.nan)


def f26_stwf_422_oscillator_universe_persistence_after_extreme_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of past 252d where >=3 of 5 basket oscillators were in extreme state (z>2)."""
    o = _all_oscillators(high, low, close)
    cnt = pd.Series(0.0, index=close.index)
    for s in o.values():
        z = _rolling_zscore(s, YDAYS, min_periods=QDAYS)
        cnt = cnt + (z > 2.0).astype(float).fillna(0)
    return (cnt >= 3).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(close.notna(), np.nan)


def f26_stwf_423_oscillator_universe_terminal_pattern_aggregate_score(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Terminal pattern score: count of basket oscillators that had blow-off (z>3) then now z<0."""
    o = _all_oscillators(high, low, close)
    cnt = pd.Series(0.0, index=close.index)
    for s in o.values():
        z = _rolling_zscore(s, YDAYS, min_periods=QDAYS)
        blowoff = (z > 3.0).astype(float).rolling(QDAYS, min_periods=1).max()
        cnt = cnt + ((blowoff > 0) & (z < 0)).astype(float).fillna(0)
    return cnt


def f26_stwf_424_multi_oscillator_topping_intensity_score(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Topping intensity: sum of (osc OB-distance) across basket, where OB-distance = max(0, osc - osc_q90)."""
    o = _all_oscillators(high, low, close)
    score = pd.Series(0.0, index=close.index)
    for s in o.values():
        q = _quantile_rolling(s, YDAYS, 0.90, min_periods=QDAYS)
        score = score + (s - q).clip(lower=0).fillna(0)
    return score


def f26_stwf_425_multi_oscillator_distribution_signal_aggregate(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Aggregate distribution signal: count of basket osc in 60-80 zone with declining 21d max AND price at 63d new high."""
    o = _all_oscillators(high, low, close)
    p_new = close >= close.rolling(QDAYS, min_periods=MDAYS).max()
    cnt = pd.Series(0.0, index=close.index)
    for s in o.values():
        in_zone = (s >= 60.0) & (s <= 80.0)
        mx21 = s.rolling(MDAYS, min_periods=WDAYS).max()
        decl = _rolling_slope(mx21, QDAYS, min_periods=MDAYS) < 0
        cnt = cnt + (in_zone & decl & p_new).astype(float).fillna(0)
    return cnt.where(p_new, np.nan)


def f26_stwf_426_multi_oscillator_blowoff_then_failure_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if all 5 basket osc had z>3 in past 21d AND >=3 now have z<0 — universal blow-off + failure."""
    o = _all_oscillators(high, low, close)
    blow_cnt = pd.Series(0.0, index=close.index)
    fail_cnt = pd.Series(0.0, index=close.index)
    for s in o.values():
        z = _rolling_zscore(s, YDAYS, min_periods=QDAYS)
        bo = (z > 3.0).astype(float).rolling(MDAYS, min_periods=1).max()
        blow_cnt = blow_cnt + (bo > 0).astype(float).fillna(0)
        fail_cnt = fail_cnt + (z < 0).astype(float).fillna(0)
    return ((blow_cnt >= 5) & (fail_cnt >= 3)).astype(float).where(close.notna(), np.nan)


def f26_stwf_427_multi_oscillator_chronic_weakness_score_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Chronic weakness: avg fraction of past 252d each basket osc spent below 50."""
    o = _all_oscillators(high, low, close)
    fracs = []
    for s in o.values():
        # WR uses [-100, 0] so adjust: < -50 is equivalent to <50 for [0,100]-scaled
        if s.name == "wr" or False:
            below = (s < -50.0).astype(float)
        else:
            below = (s < 50.0).astype(float)
        fracs.append(below.rolling(YDAYS, min_periods=QDAYS).mean())
    df = pd.concat([f.rename(i) for i, f in enumerate(fracs)], axis=1)
    return df.mean(axis=1)


def f26_stwf_428_multi_oscillator_post_peak_decay_aggregate(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Aggregate post-peak decay: avg of (current osc) / (osc_252d_max) across basket — value < 1 means below historical peak."""
    o = _all_oscillators(high, low, close)
    ratios = []
    for s in o.values():
        mx = s.rolling(YDAYS, min_periods=QDAYS).max().replace(0, np.nan)
        ratios.append(_safe_div(s, mx))
    df = pd.concat([r.rename(i) for i, r in enumerate(ratios)], axis=1)
    return df.mean(axis=1)


def f26_stwf_429_multi_oscillator_recovery_failure_count_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of basket oscillators in past 63d that fell from OB and failed to retest OB (k<80 dwelling persistently)."""
    o = _all_oscillators(high, low, close)
    cnt = pd.Series(0.0, index=close.index)
    for s in o.values():
        was_ob = (s > 80.0).astype(float).rolling(QDAYS, min_periods=MDAYS).max()
        retest_max = s.rolling(QDAYS, min_periods=MDAYS).max()
        fail = ((was_ob > 0) & (retest_max < 80.0)).astype(float)
        cnt = cnt + fail.fillna(0)
    return cnt


def f26_stwf_430_multi_oscillator_lower_high_breadth_count_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of basket oscillators where 21d-max < 21d-max.shift(21) AND close at 63d new high — lower-osc-high breadth."""
    o = _all_oscillators(high, low, close)
    p_new = close >= close.rolling(QDAYS, min_periods=MDAYS).max()
    cnt = pd.Series(0.0, index=close.index)
    for s in o.values():
        mx_now = s.rolling(MDAYS, min_periods=WDAYS).max()
        mx_prev = mx_now.shift(MDAYS)
        cnt = cnt + ((mx_now < mx_prev) & p_new).astype(float).fillna(0)
    return cnt.where(p_new, np.nan)


def f26_stwf_431_multi_oscillator_failure_signal_density_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Density of failure signals: count of {OB-exit, lower-high, blow-off-fail} events across basket / 63 bars."""
    o = _all_oscillators(high, low, close)
    total = pd.Series(0.0, index=close.index)
    for s in o.values():
        ob_exit = ((s.shift(1) > 80.0) & (s <= 80.0)).astype(float)
        mx21 = s.rolling(MDAYS, min_periods=WDAYS).max()
        lh = (mx21 < mx21.shift(MDAYS)).astype(float)
        z = _rolling_zscore(s, YDAYS, min_periods=QDAYS)
        bo_fail = ((z.shift(5) > 3.0) & (z < 0)).astype(float)
        ev = ob_exit + lh + bo_fail
        total = total + ev.fillna(0)
    return total.rolling(QDAYS, min_periods=MDAYS).sum() / (QDAYS * 5.0)


def f26_stwf_432_multi_oscillator_breakdown_confirmation_count(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of basket osc that crossed below 50 in past 5 bars (breakdown confirmation breadth)."""
    o = _all_oscillators(high, low, close)
    cnt = pd.Series(0.0, index=close.index)
    for s in o.values():
        # WR uses [-100,0]: < -50 equivalent
        if hasattr(s, "name") and s.name == "wr":
            cross = (s.shift(5) > -50.0) & (s <= -50.0)
        else:
            cross = (s.shift(5) > 50.0) & (s <= 50.0)
        cnt = cnt + cross.astype(float).fillna(0)
    return cnt


def f26_stwf_433_oscillator_blow_off_indicator_universe_count(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of basket osc with z > 3 in past 21d (extreme blow-off events)."""
    o = _all_oscillators(high, low, close)
    cnt = pd.Series(0.0, index=close.index)
    for s in o.values():
        z = _rolling_zscore(s, YDAYS, min_periods=QDAYS)
        bo = (z > 3.0).astype(float).rolling(MDAYS, min_periods=1).max()
        cnt = cnt + (bo > 0).astype(float).fillna(0)
    return cnt


def f26_stwf_434_multi_oscillator_consensus_topping_at_252h(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if at 252d new close-high AND >=4 of 5 basket osc in their own q90+ zone — strong consensus topping."""
    o = _all_oscillators(high, low, close)
    is_top = close >= close.rolling(YDAYS, min_periods=QDAYS).max()
    cnt = pd.Series(0.0, index=close.index)
    for s in o.values():
        q = _quantile_rolling(s, YDAYS, 0.90, min_periods=QDAYS)
        cnt = cnt + (s > q).astype(float).fillna(0)
    return (is_top & (cnt >= 4)).astype(float).where(is_top, np.nan)


def f26_stwf_435_oscillator_universe_extreme_z_score_max_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Max z-score across basket in past 252d — captures the most extreme single-oscillator state recently."""
    o = _all_oscillators(high, low, close)
    z_list = [_rolling_zscore(s, YDAYS, min_periods=QDAYS) for s in o.values()]
    df = pd.concat([z.rename(i) for i, z in enumerate(z_list)], axis=1)
    return df.max(axis=1)


def f26_stwf_436_oscillator_universe_extreme_z_score_min_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Min z-score across basket in past 252d — captures the most negative single-oscillator state recently."""
    o = _all_oscillators(high, low, close)
    z_list = [_rolling_zscore(s, YDAYS, min_periods=QDAYS) for s in o.values()]
    df = pd.concat([z.rename(i) for i, z in enumerate(z_list)], axis=1)
    return df.min(axis=1)


def f26_stwf_437_oscillator_universe_z_score_range_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score range = max - min across basket — dispersion of basket osc states."""
    o = _all_oscillators(high, low, close)
    z_list = [_rolling_zscore(s, QDAYS, min_periods=MDAYS) for s in o.values()]
    df = pd.concat([z.rename(i) for i, z in enumerate(z_list)], axis=1)
    return df.max(axis=1) - df.min(axis=1)


def f26_stwf_438_oscillator_extreme_event_clustering_index_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Clustering index: count of bars in past 63 where any basket osc had z>2 / total — concentration of extreme events."""
    o = _all_oscillators(high, low, close)
    any_extreme = pd.Series(False, index=close.index)
    for s in o.values():
        z = _rolling_zscore(s, YDAYS, min_periods=QDAYS)
        any_extreme = any_extreme | (z > 2.0).fillna(False)
    return any_extreme.astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(close.notna(), np.nan)


def f26_stwf_439_oscillator_basket_terminal_score_with_volume_weight(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted terminal score: basket extreme-count weighted by volume z-score (high-vol distribution amplifies)."""
    o = _all_oscillators(high, low, close)
    cnt = pd.Series(0.0, index=close.index)
    for s in o.values():
        z = _rolling_zscore(s, YDAYS, min_periods=QDAYS)
        cnt = cnt + (z > 2.0).astype(float).fillna(0)
    v_z = _rolling_zscore(volume, YDAYS, min_periods=QDAYS).clip(lower=0)
    return cnt * (1.0 + v_z.fillna(0))


def f26_stwf_440_oscillator_topping_master_score_extended_v3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Master extended v3 score: (extreme_cnt z>2) + (failure_breadth) + (post_peak_decay_aggregate) + (volume_zscore)."""
    o = _all_oscillators(high, low, close)
    ec = pd.Series(0.0, index=close.index)
    fb = pd.Series(0.0, index=close.index)
    p_new = close >= close.rolling(QDAYS, min_periods=MDAYS).max()
    ratios = []
    for s in o.values():
        z = _rolling_zscore(s, YDAYS, min_periods=QDAYS)
        ec = ec + (z > 2.0).astype(float).fillna(0)
        smax = s.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
        fb = fb + ((s < smax) & p_new).astype(float).fillna(0)
        mx = s.rolling(YDAYS, min_periods=QDAYS).max().replace(0, np.nan)
        ratios.append(_safe_div(s, mx))
    df = pd.concat([r.rename(i) for i, r in enumerate(ratios)], axis=1)
    decay = 1.0 - df.mean(axis=1)
    v_z = _rolling_zscore(volume, YDAYS, min_periods=QDAYS).clip(lower=0).fillna(0)
    return (ec + fb + decay + v_z)


# ============================================================
# Master/aggregate top scores (441-450)
# ============================================================


def f26_stwf_441_stuck_probability_oscillator_universe_proxy_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Stuck-probability proxy: weighted combo of (chronic OB dwell) + (post-blowoff fail) + (multi-osc weakness)."""
    o = _all_oscillators(high, low, close)
    # chronic OB
    chr_ob = pd.Series(0.0, index=close.index)
    for s in o.values():
        ob = (s > 80.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()
        chr_ob = chr_ob + ob.fillna(0)
    # post-blowoff fail count
    pf = pd.Series(0.0, index=close.index)
    for s in o.values():
        z = _rolling_zscore(s, YDAYS, min_periods=QDAYS)
        bo = (z.shift(MDAYS) > 3.0).astype(float)
        now_low = (z < 0).astype(float)
        pf = pf + (bo * now_low).fillna(0)
    # weakness
    wk = pd.Series(0.0, index=close.index)
    for s in o.values():
        below = (s < 50.0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
        wk = wk + below.fillna(0)
    return 0.3 * chr_ob + 0.3 * pf + 0.4 * wk


def f26_stwf_442_oscillator_basket_recall_optimized_score(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Recall-optimized: sum of ALL topping signals (any OB, any divergence, any weakness, any blow-off) — high-recall."""
    o = _all_oscillators(high, low, close)
    score = pd.Series(0.0, index=close.index)
    p_new = close >= close.rolling(QDAYS, min_periods=MDAYS).max()
    for s in o.values():
        # any OB
        score = score + (s > 80.0).astype(float).fillna(0)
        # any divergence at top
        smax = s.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
        score = score + ((s < smax) & p_new).astype(float).fillna(0)
        # any weakness
        score = score + (s < 30.0).astype(float).fillna(0)
        # blow-off
        z = _rolling_zscore(s, YDAYS, min_periods=QDAYS)
        score = score + (z > 3.0).astype(float).fillna(0)
    return score


def f26_stwf_443_oscillator_basket_precision_optimized_score(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Precision-optimized: only fires when multi-signal consensus is high (>=4 indicators agree)."""
    o = _all_oscillators(high, low, close)
    p_new = close >= close.rolling(QDAYS, min_periods=MDAYS).max()
    is_top = close >= close.rolling(YDAYS, min_periods=QDAYS).max()
    cnt_ob = pd.Series(0.0, index=close.index)
    cnt_div = pd.Series(0.0, index=close.index)
    cnt_lh = pd.Series(0.0, index=close.index)
    cnt_bo = pd.Series(0.0, index=close.index)
    for s in o.values():
        cnt_ob = cnt_ob + (s > 80.0).astype(float).fillna(0)
        smax = s.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
        cnt_div = cnt_div + ((s < smax) & p_new).astype(float).fillna(0)
        mx21 = s.rolling(MDAYS, min_periods=WDAYS).max()
        cnt_lh = cnt_lh + (mx21 < mx21.shift(MDAYS)).astype(float).fillna(0)
        z = _rolling_zscore(s, YDAYS, min_periods=QDAYS)
        cnt_bo = cnt_bo + (z > 3.0).astype(float).fillna(0)
    # require all 4 conditions strongly met + at 252d top
    return ((cnt_ob >= 3).astype(float) * (cnt_div >= 3).astype(float)
            * (cnt_lh >= 3).astype(float) * (cnt_bo >= 2).astype(float) * is_top.astype(float)).where(close.notna(), np.nan)


def f26_stwf_444_oscillator_topping_signal_orthogonal_aggregate(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Aggregate of orthogonal signal axes: extreme-z + chronic-OB + decay-velocity + recent-failure (z-normalized)."""
    o = _all_oscillators(high, low, close)
    # axis 1: max z
    z_list = [_rolling_zscore(s, YDAYS, min_periods=QDAYS) for s in o.values()]
    a1 = pd.concat([z.rename(i) for i, z in enumerate(z_list)], axis=1).max(axis=1)
    # axis 2: chronic OB across basket (sum of dwells)
    a2 = pd.Series(0.0, index=close.index)
    for s in o.values():
        a2 = a2 + (s > 80.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().fillna(0)
    # axis 3: decay velocity mean
    vels = []
    for s in o.values():
        peak = s.rolling(MDAYS, min_periods=WDAYS).max()
        bars = _bars_since_true(s >= peak)
        vels.append(_safe_div(s - peak, bars.where(bars > 0, np.nan)))
    a3 = -pd.concat([v.rename(i) for i, v in enumerate(vels)], axis=1).mean(axis=1)
    # axis 4: recent OB-exit count
    a4 = pd.Series(0.0, index=close.index)
    for s in o.values():
        exit_ev = ((s.shift(1) > 80.0) & (s <= 80.0)).astype(float).rolling(MDAYS, min_periods=1).sum()
        a4 = a4 + exit_ev.fillna(0)
    # normalize each by rolling 252 zscore then sum
    nz = lambda x: _rolling_zscore(x, YDAYS, min_periods=QDAYS).fillna(0)
    return nz(a1) + nz(a2) + nz(a3) + nz(a4)


def f26_stwf_445_oscillator_terminal_distribution_score_v3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Terminal distribution v3: (basket in 60-80 zone count) * (declining 21d-max count) * (volume-z weighting)."""
    o = _all_oscillators(high, low, close)
    in_zone = pd.Series(0.0, index=close.index)
    decline = pd.Series(0.0, index=close.index)
    for s in o.values():
        in_zone = in_zone + ((s >= 60.0) & (s <= 80.0)).astype(float).fillna(0)
        mx21 = s.rolling(MDAYS, min_periods=WDAYS).max()
        sl = _rolling_slope(mx21, QDAYS, min_periods=MDAYS)
        decline = decline + (sl < 0).astype(float).fillna(0)
    v_z = _rolling_zscore(volume, YDAYS, min_periods=QDAYS).fillna(0)
    return (in_zone * decline) * (1.0 + v_z.clip(lower=0))


def f26_stwf_446_stoch_ml_feature_aggregate_topping_v3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ML feature aggregate v3 (stoch-centric): K-z + (1 if K>q90 504) + (K-decay velocity) - (K-21d-min).
    Combines magnitude, rare-event, decay, and floor signals from K(14)."""
    k = _stoch_k(high, low, close, 14)
    z = _rolling_zscore(k, YDAYS, min_periods=QDAYS).fillna(0)
    q90 = _quantile_rolling(k, DDAYS_2Y, 0.90, min_periods=QDAYS)
    above = (k > q90).astype(float).fillna(0)
    peak = k.rolling(MDAYS, min_periods=WDAYS).max()
    bars = _bars_since_true(k >= peak)
    decay = _safe_div(k - peak, bars.where(bars > 0, np.nan)).fillna(0)
    k_min21 = k.rolling(MDAYS, min_periods=WDAYS).min()
    floor_z = _rolling_zscore(k_min21, YDAYS, min_periods=QDAYS).fillna(0)
    return z + above - decay - floor_z


def f26_stwf_447_oscillator_ml_aggregate_distribution_v3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ML aggregate v3 (basket-centric distribution): in-zone + declining-max + lower-high count -- distribution signature."""
    o = _all_oscillators(high, low, close)
    in_zone_cnt = pd.Series(0.0, index=close.index)
    declining_cnt = pd.Series(0.0, index=close.index)
    lh_cnt = pd.Series(0.0, index=close.index)
    for s in o.values():
        in_zone_cnt = in_zone_cnt + ((s >= 60.0) & (s <= 80.0)).astype(float).fillna(0)
        mx21 = s.rolling(MDAYS, min_periods=WDAYS).max()
        declining_cnt = declining_cnt + (_rolling_slope(mx21, QDAYS, min_periods=MDAYS) < 0).astype(float).fillna(0)
        lh_cnt = lh_cnt + (mx21 < mx21.shift(MDAYS)).astype(float).fillna(0)
    return in_zone_cnt + declining_cnt + lh_cnt


def f26_stwf_448_oscillator_terminal_pattern_master_v3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Terminal pattern master v3: combines blow-off-then-fail + chronic-OB-no-progress + capitulation indicators."""
    o = _all_oscillators(high, low, close)
    bo_fail = pd.Series(0.0, index=close.index)
    chr_ob = pd.Series(0.0, index=close.index)
    cap = pd.Series(0.0, index=close.index)
    for s in o.values():
        z = _rolling_zscore(s, YDAYS, min_periods=QDAYS)
        bo = (z.shift(MDAYS) > 3.0).astype(float)
        now_l = (z < 0).astype(float)
        bo_fail = bo_fail + (bo * now_l).fillna(0)
        ob_days = (s > 80.0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
        p_max = close.rolling(QDAYS, min_periods=MDAYS).max()
        chr_ob = chr_ob + ((ob_days > 40.0) & (close < p_max)).astype(float).fillna(0)
        ob_recent = (s.shift(1) > 80.0).astype(float).rolling(5, min_periods=1).max()
        cap = cap + ((ob_recent > 0) & (s < 20.0)).astype(float).fillna(0)
    v_z = _rolling_zscore(volume, YDAYS, min_periods=QDAYS).fillna(0).clip(lower=-2, upper=2)
    return (bo_fail + chr_ob + cap) * (1.0 + 0.25 * v_z)


def f26_stwf_449_oscillator_extended_universe_blowoff_collapse_score(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Blow-off collapse: (extreme z>3 in past 63d, count) * (current drawdown from K-peak) * (volume z)."""
    o = _all_oscillators(high, low, close)
    bo_cnt = pd.Series(0.0, index=close.index)
    dd_avg = pd.Series(0.0, index=close.index)
    n_o = 0
    for s in o.values():
        z = _rolling_zscore(s, YDAYS, min_periods=QDAYS)
        bo = (z > 3.0).astype(float).rolling(QDAYS, min_periods=1).max()
        bo_cnt = bo_cnt + (bo > 0).astype(float).fillna(0)
        peak = s.rolling(QDAYS, min_periods=MDAYS).max().replace(0, np.nan)
        dd_avg = dd_avg + (1.0 - _safe_div(s, peak)).fillna(0)
        n_o += 1
    if n_o > 0:
        dd_avg = dd_avg / float(n_o)
    v_z = _rolling_zscore(volume, YDAYS, min_periods=QDAYS).fillna(0).clip(lower=-2, upper=3)
    return bo_cnt * dd_avg * (1.0 + 0.5 * v_z)


def f26_stwf_450_absolute_terminal_oscillator_indicator_extended(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Final extended absolute-terminal indicator: 1 if (basket extreme-z count >= 3) AND (post-peak decay across basket > median)
    AND (volume z > 1) AND (close at 252d high) — captures the apex pattern."""
    o = _all_oscillators(high, low, close)
    ec = pd.Series(0.0, index=close.index)
    ratios = []
    for s in o.values():
        z = _rolling_zscore(s, YDAYS, min_periods=QDAYS)
        ec = ec + (z > 2.0).astype(float).fillna(0)
        mx = s.rolling(YDAYS, min_periods=QDAYS).max().replace(0, np.nan)
        ratios.append(_safe_div(s, mx))
    df = pd.concat([r.rename(i) for i, r in enumerate(ratios)], axis=1)
    decay = 1.0 - df.mean(axis=1)
    decay_med = decay.rolling(YDAYS, min_periods=QDAYS).median()
    v_z = _rolling_zscore(volume, YDAYS, min_periods=QDAYS)
    is_top = close >= close.rolling(YDAYS, min_periods=QDAYS).max()
    return ((ec >= 3) & (decay > decay_med) & (v_z > 1.0) & is_top).astype(float).where(close.notna(), np.nan)


# ============================================================
#                         REGISTRY 376-450
# ============================================================

STOCHASTIC_WILLIAMS_FAMILY_BASE_REGISTRY_376_450 = {
    "f26_stwf_376_stoch_pct_rank_within_504d": {"inputs": ["high", "low", "close"], "func": f26_stwf_376_stoch_pct_rank_within_504d},
    "f26_stwf_377_stoch_pct_rank_within_1260d": {"inputs": ["high", "low", "close"], "func": f26_stwf_377_stoch_pct_rank_within_1260d},
    "f26_stwf_378_williams_r_pct_rank_within_504d": {"inputs": ["high", "low", "close"], "func": f26_stwf_378_williams_r_pct_rank_within_504d},
    "f26_stwf_379_williams_r_pct_rank_within_1260d": {"inputs": ["high", "low", "close"], "func": f26_stwf_379_williams_r_pct_rank_within_1260d},
    "f26_stwf_380_srsi_pct_rank_within_504d": {"inputs": ["close"], "func": f26_stwf_380_srsi_pct_rank_within_504d},
    "f26_stwf_381_stoch_above_own_q95_504_state": {"inputs": ["high", "low", "close"], "func": f26_stwf_381_stoch_above_own_q95_504_state},
    "f26_stwf_382_stoch_above_own_q99_1260_state": {"inputs": ["high", "low", "close"], "func": f26_stwf_382_stoch_above_own_q99_1260_state},
    "f26_stwf_383_stoch_within_vol_bucketed_history_q90": {"inputs": ["high", "low", "close"], "func": f26_stwf_383_stoch_within_vol_bucketed_history_q90},
    "f26_stwf_384_stoch_within_price_bucketed_history_q90": {"inputs": ["high", "low", "close"], "func": f26_stwf_384_stoch_within_price_bucketed_history_q90},
    "f26_stwf_385_stoch_within_trend_bucketed_history_q90": {"inputs": ["high", "low", "close"], "func": f26_stwf_385_stoch_within_trend_bucketed_history_q90},
    "f26_stwf_386_stoch_dwell_above_own_q90_504_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_386_stoch_dwell_above_own_q90_504_63},
    "f26_stwf_387_stoch_consecutive_above_own_q90_504_streak": {"inputs": ["high", "low", "close"], "func": f26_stwf_387_stoch_consecutive_above_own_q90_504_streak},
    "f26_stwf_388_stoch_first_breach_of_own_q99_504_age": {"inputs": ["high", "low", "close"], "func": f26_stwf_388_stoch_first_breach_of_own_q99_504_age},
    "f26_stwf_389_stoch_pct_rank_decay_velocity_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_389_stoch_pct_rank_decay_velocity_63},
    "f26_stwf_390_stoch_dispersion_within_own_252d": {"inputs": ["high", "low", "close"], "func": f26_stwf_390_stoch_dispersion_within_own_252d},
    "f26_stwf_391_stoch_distance_from_own_median_504d": {"inputs": ["high", "low", "close"], "func": f26_stwf_391_stoch_distance_from_own_median_504d},
    "f26_stwf_392_stoch_skew_within_own_252d": {"inputs": ["high", "low", "close"], "func": f26_stwf_392_stoch_skew_within_own_252d},
    "f26_stwf_393_stoch_kurtosis_within_own_252d": {"inputs": ["high", "low", "close"], "func": f26_stwf_393_stoch_kurtosis_within_own_252d},
    "f26_stwf_394_williams_r_distribution_shift_zscore_252": {"inputs": ["high", "low", "close"], "func": f26_stwf_394_williams_r_distribution_shift_zscore_252},
    "f26_stwf_395_stoch_distribution_shift_indicator_252": {"inputs": ["high", "low", "close"], "func": f26_stwf_395_stoch_distribution_shift_indicator_252},
    "f26_stwf_396_stoch_at_sma50_cross_above_indicator": {"inputs": ["high", "low", "close"], "func": f26_stwf_396_stoch_at_sma50_cross_above_indicator},
    "f26_stwf_397_stoch_at_sma200_cross_above_indicator": {"inputs": ["high", "low", "close"], "func": f26_stwf_397_stoch_at_sma200_cross_above_indicator},
    "f26_stwf_398_stoch_at_gap_up_event_value": {"inputs": ["high", "low", "close"], "func": f26_stwf_398_stoch_at_gap_up_event_value},
    "f26_stwf_399_stoch_at_gap_down_event_value": {"inputs": ["high", "low", "close"], "func": f26_stwf_399_stoch_at_gap_down_event_value},
    "f26_stwf_400_stoch_at_volume_spike_event_value": {"inputs": ["high", "low", "close", "volume"], "func": f26_stwf_400_stoch_at_volume_spike_event_value},
    "f26_stwf_401_stoch_after_first_distribution_day_21": {"inputs": ["high", "low", "close", "volume"], "func": f26_stwf_401_stoch_after_first_distribution_day_21},
    "f26_stwf_402_stoch_at_first_lower_high_post_peak": {"inputs": ["high", "low", "close"], "func": f26_stwf_402_stoch_at_first_lower_high_post_peak},
    "f26_stwf_403_stoch_at_252h_value": {"inputs": ["high", "low", "close"], "func": f26_stwf_403_stoch_at_252h_value},
    "f26_stwf_404_williams_r_at_252h_value": {"inputs": ["high", "low", "close"], "func": f26_stwf_404_williams_r_at_252h_value},
    "f26_stwf_405_stoch_post_breakdown_failed_recovery_count_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_405_stoch_post_breakdown_failed_recovery_count_63},
    "f26_stwf_406_stoch_post_breakdown_zone_persistence": {"inputs": ["high", "low", "close"], "func": f26_stwf_406_stoch_post_breakdown_zone_persistence},
    "f26_stwf_407_stoch_at_atr_expansion_event_value": {"inputs": ["high", "low", "close"], "func": f26_stwf_407_stoch_at_atr_expansion_event_value},
    "f26_stwf_408_stoch_at_atr_contraction_event_value": {"inputs": ["high", "low", "close"], "func": f26_stwf_408_stoch_at_atr_contraction_event_value},
    "f26_stwf_409_stoch_when_high_volume_down_day": {"inputs": ["high", "low", "close", "volume"], "func": f26_stwf_409_stoch_when_high_volume_down_day},
    "f26_stwf_410_stoch_when_low_volume_up_day": {"inputs": ["high", "low", "close", "volume"], "func": f26_stwf_410_stoch_when_low_volume_up_day},
    "f26_stwf_411_stoch_when_widerange_red_bar": {"inputs": ["high", "low", "close"], "func": f26_stwf_411_stoch_when_widerange_red_bar},
    "f26_stwf_412_stoch_at_swing_high_value": {"inputs": ["high", "low", "close"], "func": f26_stwf_412_stoch_at_swing_high_value},
    "f26_stwf_413_stoch_at_swing_low_value": {"inputs": ["high", "low", "close"], "func": f26_stwf_413_stoch_at_swing_low_value},
    "f26_stwf_414_stoch_during_consolidation_phase_indicator": {"inputs": ["high", "low", "close"], "func": f26_stwf_414_stoch_during_consolidation_phase_indicator},
    "f26_stwf_415_stoch_at_breakout_failure_event_value": {"inputs": ["high", "low", "close"], "func": f26_stwf_415_stoch_at_breakout_failure_event_value},
    "f26_stwf_416_modern_classical_stoch_basket_avg_zscore_504": {"inputs": ["high", "low", "close"], "func": f26_stwf_416_modern_classical_stoch_basket_avg_zscore_504},
    "f26_stwf_417_modern_classical_stoch_basket_extreme_count_252": {"inputs": ["high", "low", "close"], "func": f26_stwf_417_modern_classical_stoch_basket_extreme_count_252},
    "f26_stwf_418_modern_classical_stoch_basket_bearish_alignment_count": {"inputs": ["high", "low", "close"], "func": f26_stwf_418_modern_classical_stoch_basket_bearish_alignment_count},
    "f26_stwf_419_oscillator_universe_correlation_breakdown_zscore_252": {"inputs": ["high", "low", "close"], "func": f26_stwf_419_oscillator_universe_correlation_breakdown_zscore_252},
    "f26_stwf_420_oscillator_universe_decay_velocity_post_peak_aggregate": {"inputs": ["high", "low", "close"], "func": f26_stwf_420_oscillator_universe_decay_velocity_post_peak_aggregate},
    "f26_stwf_421_oscillator_universe_failure_breadth_at_top_score": {"inputs": ["high", "low", "close"], "func": f26_stwf_421_oscillator_universe_failure_breadth_at_top_score},
    "f26_stwf_422_oscillator_universe_persistence_after_extreme_252": {"inputs": ["high", "low", "close"], "func": f26_stwf_422_oscillator_universe_persistence_after_extreme_252},
    "f26_stwf_423_oscillator_universe_terminal_pattern_aggregate_score": {"inputs": ["high", "low", "close"], "func": f26_stwf_423_oscillator_universe_terminal_pattern_aggregate_score},
    "f26_stwf_424_multi_oscillator_topping_intensity_score": {"inputs": ["high", "low", "close"], "func": f26_stwf_424_multi_oscillator_topping_intensity_score},
    "f26_stwf_425_multi_oscillator_distribution_signal_aggregate": {"inputs": ["high", "low", "close"], "func": f26_stwf_425_multi_oscillator_distribution_signal_aggregate},
    "f26_stwf_426_multi_oscillator_blowoff_then_failure_indicator": {"inputs": ["high", "low", "close"], "func": f26_stwf_426_multi_oscillator_blowoff_then_failure_indicator},
    "f26_stwf_427_multi_oscillator_chronic_weakness_score_252": {"inputs": ["high", "low", "close"], "func": f26_stwf_427_multi_oscillator_chronic_weakness_score_252},
    "f26_stwf_428_multi_oscillator_post_peak_decay_aggregate": {"inputs": ["high", "low", "close"], "func": f26_stwf_428_multi_oscillator_post_peak_decay_aggregate},
    "f26_stwf_429_multi_oscillator_recovery_failure_count_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_429_multi_oscillator_recovery_failure_count_63},
    "f26_stwf_430_multi_oscillator_lower_high_breadth_count_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_430_multi_oscillator_lower_high_breadth_count_63},
    "f26_stwf_431_multi_oscillator_failure_signal_density_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_431_multi_oscillator_failure_signal_density_63},
    "f26_stwf_432_multi_oscillator_breakdown_confirmation_count": {"inputs": ["high", "low", "close"], "func": f26_stwf_432_multi_oscillator_breakdown_confirmation_count},
    "f26_stwf_433_oscillator_blow_off_indicator_universe_count": {"inputs": ["high", "low", "close"], "func": f26_stwf_433_oscillator_blow_off_indicator_universe_count},
    "f26_stwf_434_multi_oscillator_consensus_topping_at_252h": {"inputs": ["high", "low", "close"], "func": f26_stwf_434_multi_oscillator_consensus_topping_at_252h},
    "f26_stwf_435_oscillator_universe_extreme_z_score_max_252": {"inputs": ["high", "low", "close"], "func": f26_stwf_435_oscillator_universe_extreme_z_score_max_252},
    "f26_stwf_436_oscillator_universe_extreme_z_score_min_252": {"inputs": ["high", "low", "close"], "func": f26_stwf_436_oscillator_universe_extreme_z_score_min_252},
    "f26_stwf_437_oscillator_universe_z_score_range_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_437_oscillator_universe_z_score_range_63},
    "f26_stwf_438_oscillator_extreme_event_clustering_index_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_438_oscillator_extreme_event_clustering_index_63},
    "f26_stwf_439_oscillator_basket_terminal_score_with_volume_weight": {"inputs": ["high", "low", "close", "volume"], "func": f26_stwf_439_oscillator_basket_terminal_score_with_volume_weight},
    "f26_stwf_440_oscillator_topping_master_score_extended_v3": {"inputs": ["high", "low", "close", "volume"], "func": f26_stwf_440_oscillator_topping_master_score_extended_v3},
    "f26_stwf_441_stuck_probability_oscillator_universe_proxy_252": {"inputs": ["high", "low", "close"], "func": f26_stwf_441_stuck_probability_oscillator_universe_proxy_252},
    "f26_stwf_442_oscillator_basket_recall_optimized_score": {"inputs": ["high", "low", "close"], "func": f26_stwf_442_oscillator_basket_recall_optimized_score},
    "f26_stwf_443_oscillator_basket_precision_optimized_score": {"inputs": ["high", "low", "close"], "func": f26_stwf_443_oscillator_basket_precision_optimized_score},
    "f26_stwf_444_oscillator_topping_signal_orthogonal_aggregate": {"inputs": ["high", "low", "close"], "func": f26_stwf_444_oscillator_topping_signal_orthogonal_aggregate},
    "f26_stwf_445_oscillator_terminal_distribution_score_v3": {"inputs": ["high", "low", "close", "volume"], "func": f26_stwf_445_oscillator_terminal_distribution_score_v3},
    "f26_stwf_446_stoch_ml_feature_aggregate_topping_v3": {"inputs": ["high", "low", "close"], "func": f26_stwf_446_stoch_ml_feature_aggregate_topping_v3},
    "f26_stwf_447_oscillator_ml_aggregate_distribution_v3": {"inputs": ["high", "low", "close"], "func": f26_stwf_447_oscillator_ml_aggregate_distribution_v3},
    "f26_stwf_448_oscillator_terminal_pattern_master_v3": {"inputs": ["high", "low", "close", "volume"], "func": f26_stwf_448_oscillator_terminal_pattern_master_v3},
    "f26_stwf_449_oscillator_extended_universe_blowoff_collapse_score": {"inputs": ["high", "low", "close", "volume"], "func": f26_stwf_449_oscillator_extended_universe_blowoff_collapse_score},
    "f26_stwf_450_absolute_terminal_oscillator_indicator_extended": {"inputs": ["high", "low", "close", "volume"], "func": f26_stwf_450_absolute_terminal_oscillator_indicator_extended},
}
