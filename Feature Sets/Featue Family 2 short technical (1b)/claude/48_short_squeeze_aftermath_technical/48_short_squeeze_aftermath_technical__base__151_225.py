"""short_squeeze_aftermath_technical base features 151-225 — Pipeline 1b-technical.

Gap-fill extension. Covers post-collapse swing structure (lower-highs/lows,
bear flags, failed rallies), anchored-VWAP from peak, extended decline-volume
analytics, terminal-phase volatility contraction, distribution-day events,
distribution-shape statistics, bear-trend persistence, and squeeze-decay
composites that join NSIR signals with price/MA breakdown.

Bucket M: Post-collapse swing structure (151-160).
Bucket N: Anchored-VWAP from peak / structural levels (161-168).
Bucket O: Volume during decline — extended (169-175).
Bucket P: Volatility / range terminal phase (176-184).
Bucket Q: Distribution / pattern events (185-194).
Bucket R: Statistical / distribution-shape after collapse (195-202).
Bucket S: Bear-trend persistence / fail-recovery (203-210).
Bucket T: Composite squeeze-decay (211-225).

Inputs: SEP OHLCV (always) + NSIR (NaN-stubbed when absent). Self-contained
helpers; PIT-clean.
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


def _bars_since_true(mask):
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


def _streak_true(mask):
    arr = mask.astype(bool).to_numpy()
    out = np.zeros(arr.shape, dtype=float)
    c = 0
    for i in range(arr.size):
        c = c + 1 if arr[i] else 0
        out[i] = float(c)
    return pd.Series(out, index=mask.index)


def _sma(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).mean()


def _rsi(close, n=14):
    delta = close.diff()
    up = delta.clip(lower=0); dn = (-delta).clip(lower=0)
    au = up.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    ad = dn.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    return 100.0 - 100.0 / (1.0 + _safe_div(au, ad))


def _anchored_vwap_from_rolling_high(close, volume, high, n):
    """Anchored VWAP starting from the bar with max-high in trailing-n window."""
    high_arr = high.to_numpy(dtype=float)
    pv = (close * volume).to_numpy(dtype=float)
    vol_arr = volume.to_numpy(dtype=float)
    out = np.full(high_arr.size, np.nan)
    for t in range(high_arr.size):
        lo = max(0, t - n + 1)
        w = high_arr[lo : t + 1]
        if w.size == 0 or np.isnan(w).all():
            continue
        rel = int(np.nanargmax(w))
        k = lo + rel
        sum_pv = np.nansum(pv[k : t + 1])
        sum_v = np.nansum(vol_arr[k : t + 1])
        if sum_v == 0:
            continue
        out[t] = sum_pv / sum_v
    return pd.Series(out, index=close.index)


# ============================================================
# Bucket M — Post-collapse swing structure (151-160)
# ============================================================

def f48_ssat_151_lower_high_count_63(high: pd.Series) -> pd.Series:
    """Count past 63 of bars where 21d-rolling-high < 21d-rolling-high 21 bars ago — failing-highs."""
    rh = high.rolling(MDAYS, min_periods=WDAYS).max()
    lh = (rh < rh.shift(MDAYS)).astype(float)
    return lh.rolling(QDAYS, min_periods=MDAYS).sum().where(rh.notna() & rh.shift(MDAYS).notna(), np.nan)


def f48_ssat_152_lower_high_count_252(high: pd.Series) -> pd.Series:
    """Annual lower-high count."""
    rh = high.rolling(MDAYS, min_periods=WDAYS).max()
    lh = (rh < rh.shift(MDAYS)).astype(float)
    return lh.rolling(YDAYS, min_periods=QDAYS).sum().where(rh.notna() & rh.shift(MDAYS).notna(), np.nan)


def f48_ssat_153_lower_low_count_63(low: pd.Series) -> pd.Series:
    """Count past 63 of bars where 21d-rolling-low < 21d-rolling-low 21 bars ago — cascading lows."""
    rl = low.rolling(MDAYS, min_periods=WDAYS).min()
    ll = (rl < rl.shift(MDAYS)).astype(float)
    return ll.rolling(QDAYS, min_periods=MDAYS).sum().where(rl.notna() & rl.shift(MDAYS).notna(), np.nan)


def f48_ssat_154_lower_low_count_252(low: pd.Series) -> pd.Series:
    """Annual lower-low count."""
    rl = low.rolling(MDAYS, min_periods=WDAYS).min()
    ll = (rl < rl.shift(MDAYS)).astype(float)
    return ll.rolling(YDAYS, min_periods=QDAYS).sum().where(rl.notna() & rl.shift(MDAYS).notna(), np.nan)


def f48_ssat_155_bars_since_new_252d_low(low: pd.Series) -> pd.Series:
    """Bars since low equals its trailing 252d min — recency of annual low."""
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    return _bars_since_true(low == rmin)


def f48_ssat_156_count_new_252d_lows_past_252(low: pd.Series) -> pd.Series:
    """Annual count of new 252d-low bars."""
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    return (low == rmin).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(rmin.notna(), np.nan)


def f48_ssat_157_bear_flag_flag(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if (63d slope < -1*ATR21/bar) AND (21d HL range < 0.5x 63d HL range) — bear-flag consolidation."""
    sl = _rolling_slope(close, QDAYS)
    a = _atr(high, low, close, MDAYS)
    rng_21 = (high.rolling(MDAYS, min_periods=WDAYS).max() - low.rolling(MDAYS, min_periods=WDAYS).min())
    rng_63 = (high.rolling(QDAYS, min_periods=MDAYS).max() - low.rolling(QDAYS, min_periods=MDAYS).min())
    return ((sl < -1.0 * a) & (rng_21 < 0.5 * rng_63)).astype(float).where(sl.notna() & a.notna(), np.nan)


def f48_ssat_158_bear_pennant_compression(high: pd.Series, low: pd.Series) -> pd.Series:
    """Range compression past 21: (21d HL range) / (5d HL range mean) — high values = compressed after wide bars."""
    rng_21 = (high.rolling(MDAYS, min_periods=WDAYS).max() - low.rolling(MDAYS, min_periods=WDAYS).min())
    rng_5 = (high - low).rolling(WDAYS, min_periods=2).mean()
    return _safe_div(rng_5, rng_21)


def f48_ssat_159_failed_rally_count_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count past 63 of bars where 21d max-of-21d-rolling-high < 21d-rolling-high 42 bars ago — repeated failed rallies."""
    rh = high.rolling(MDAYS, min_periods=WDAYS).max()
    failed = (rh.rolling(MDAYS, min_periods=WDAYS).max() < rh.shift(2 * MDAYS)).astype(float)
    return failed.rolling(QDAYS, min_periods=MDAYS).sum().where(rh.notna() & rh.shift(2 * MDAYS).notna(), np.nan)


def f48_ssat_160_close_below_sma200_streak(close: pd.Series) -> pd.Series:
    """Current consecutive run of close <= SMA200 — long-term breakdown streak."""
    sma = _sma(close, 200)
    return _streak_true(close <= sma).where(sma.notna(), np.nan)


# ============================================================
# Bucket N — Anchored-VWAP from peak / structural levels (161-168)
# ============================================================

def f48_ssat_161_dist_aVWAP_from_252d_peak_atr21(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(close - anchored-VWAP-from-252d-peak) / ATR21 — distance below the peak's VWAP in ATR units (usually <0 post-collapse)."""
    avwap = _anchored_vwap_from_rolling_high(close, volume, high, YDAYS)
    return _safe_div(close - avwap, _atr(high, low, close, MDAYS))


def f48_ssat_162_dist_aVWAP_from_252d_peak_pct(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(close / anchored-VWAP-from-252d-peak) - 1 — pct distance from peak-anchored VWAP."""
    avwap = _anchored_vwap_from_rolling_high(close, volume, high, YDAYS)
    return _safe_div(close, avwap) - 1.0


def f48_ssat_163_bars_since_touched_aVWAP_from_peak(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since close last crossed above anchored-VWAP-from-peak (recency of the reclaim test)."""
    avwap = _anchored_vwap_from_rolling_high(close, volume, high, YDAYS)
    return _bars_since_true(close >= avwap)


def f48_ssat_164_close_above_aVWAP_from_peak_state(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if close > anchored-VWAP-from-peak — rare post-collapse, but a meaningful reclaim flag."""
    avwap = _anchored_vwap_from_rolling_high(close, volume, high, YDAYS)
    return (close > avwap).astype(float).where(avwap.notna(), np.nan)


def f48_ssat_165_dist_sma200_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - SMA200) / ATR21 — signed distance from 200d MA in ATR units (deeply negative = post-collapse)."""
    return _safe_div(close - _sma(close, 200), _atr(high, low, close, MDAYS))


def f48_ssat_166_dist_sma200_pct(close: pd.Series) -> pd.Series:
    """(close / SMA200) - 1 — signed % distance from 200d MA."""
    return _safe_div(close, _sma(close, 200)) - 1.0


def f48_ssat_167_below_sma200_streak_current(close: pd.Series) -> pd.Series:
    """Current consecutive bars-below-SMA200 streak."""
    sma = _sma(close, 200)
    return _streak_true(close < sma).where(sma.notna(), np.nan)


def f48_ssat_168_longest_below_sma200_streak_252(close: pd.Series) -> pd.Series:
    """Longest below-SMA200 streak in trailing 252d."""
    sma = _sma(close, 200)
    s = _streak_true(close < sma)
    return s.rolling(YDAYS, min_periods=QDAYS).max().where(sma.notna(), np.nan)


# ============================================================
# Bucket O — Volume during decline — extended (169-175)
# ============================================================

def f48_ssat_169_up_over_down_vol_ratio_252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Up-volume / down-volume past 252 — annual flow ratio (low when bearish)."""
    up = (close > close.shift(1)).astype(float)
    dn = (close < close.shift(1)).astype(float)
    uv = (up * volume).rolling(YDAYS, min_periods=QDAYS).sum()
    dv = (dn * volume).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(uv, dv)


def f48_ssat_170_down_vol_zscore_252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of down-day volume vs trailing 252d distribution — identifies heavy-down-day events."""
    dn_vol = volume.where(close < close.shift(1), np.nan)
    return _rolling_zscore(dn_vol, YDAYS, min_periods=QDAYS)


def f48_ssat_171_low_vol_rally_count_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count past 63 of up-close bars where volume < 70% of 21d avg — weak-buy bars (lack of buyers)."""
    up = (close > close.shift(1))
    v_avg = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    cond = up & (volume < 0.7 * v_avg)
    return cond.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(v_avg.notna(), np.nan)


def f48_ssat_172_capit_then_rally_count_63(close: pd.Series) -> pd.Series:
    """Count past 63 of bars where (1-bar return < -10%) AND (3-bar forward-looking? NO — backward: prior bar return < -10% AND today + next 2 bars cumulative return > 5%)."""
    r1_prev = close.pct_change().shift(1)
    r3_fwd_lookback = close.pct_change(3)  # 3-bar return ending today, includes the capit bar at t-3
    # We mark "capitulation 3 bars ago + recovery to today": prior_cap_3_bars_ago AND r3_today > 5%
    cap_3_ago = (close.pct_change().shift(3) < -0.10)
    return (cap_3_ago & (r3_fwd_lookback > 0.05)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(close.shift(3).notna(), np.nan)


def f48_ssat_173_failed_rally_volume_pattern_63(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count past 63 of bars where (close > prev close AND vol > 1.5x 21d avg) followed by lower-21d-high
    within next 5 bars (PIT-safe historical observation)."""
    up_on_vol = (close > close.shift(1)) & (volume > 1.5 * volume.rolling(MDAYS, min_periods=WDAYS).mean())
    rh = high.rolling(MDAYS, min_periods=WDAYS).max()
    # at bar t: was there an up-on-vol bar in [t-5..t-1] AND rh today < rh of that bar?
    # implementation: shift up_on_vol by 1..5, check any historical hit followed by lower rh today
    any_recent_uov = up_on_vol.shift(1).rolling(WDAYS, min_periods=1).max() > 0
    lower_rh = (rh < rh.shift(WDAYS))
    return (any_recent_uov & lower_rh).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(rh.notna(), np.nan)


def f48_ssat_174_low_vol_rally_count_21(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count past 21 of weak-buy bars — short-horizon variant."""
    up = (close > close.shift(1))
    v_avg = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    cond = up & (volume < 0.7 * v_avg)
    return cond.astype(float).rolling(MDAYS, min_periods=WDAYS).sum().where(v_avg.notna(), np.nan)


def f48_ssat_175_rally_vol_decay_slope_21(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21d slope of volume restricted to up-close days — falling = rally-vol decay (declining demand)."""
    up_vol = volume.where(close > close.shift(1), np.nan)
    return _rolling_slope(up_vol, MDAYS)


# ============================================================
# Bucket P — Volatility / range terminal phase (176-184)
# ============================================================

def f48_ssat_176_atr21_in_lowest_decile_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if ATR21 <= 10th-pct of trailing 252d ATR21 distribution — terminal vol contraction."""
    a = _atr(high, low, close, MDAYS)
    q = a.rolling(YDAYS, min_periods=QDAYS).quantile(0.10)
    return (a <= q).astype(float).where(q.notna(), np.nan)


def f48_ssat_177_atr21_in_lowest_quintile_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if ATR21 <= 20th-pct of trailing 252d ATR21 — vol-contraction state."""
    a = _atr(high, low, close, MDAYS)
    q = a.rolling(YDAYS, min_periods=QDAYS).quantile(0.20)
    return (a <= q).astype(float).where(q.notna(), np.nan)


def f48_ssat_178_bars_since_atr21_top_decile_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since ATR21 was in top-decile of trailing 252d — recency of last vol-extreme."""
    a = _atr(high, low, close, MDAYS)
    q = a.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    return _bars_since_true(a >= q)


def f48_ssat_179_nr7_count_63(high: pd.Series, low: pd.Series) -> pd.Series:
    """NR7 count past 63 — narrow-range-7 events (compression in declining tape)."""
    r = high - low
    rm = r.rolling(7, min_periods=7).min()
    return (r == rm).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(rm.notna(), np.nan)


def f48_ssat_180_range_21_over_range_252(high: pd.Series, low: pd.Series) -> pd.Series:
    """21d-avg HL range / 252d-avg HL range — terminal range compression (low value = orderly bear)."""
    r = high - low
    return _safe_div(r.rolling(MDAYS, min_periods=WDAYS).mean(), r.rolling(YDAYS, min_periods=QDAYS).mean())


def f48_ssat_181_hl_range_slope_63_negative(high: pd.Series, low: pd.Series) -> pd.Series:
    """1 if 63d slope of HL range < 0 — range trending down (post-shock quietening)."""
    sl = _rolling_slope(high - low, QDAYS)
    return (sl < 0).astype(float).where(sl.notna(), np.nan)


def f48_ssat_182_intra_bar_range_expansion_zscore(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score (252d) of (TR / 21d-ATR) — bar-by-bar range-expansion regime."""
    return _rolling_zscore(_safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS)), YDAYS, min_periods=QDAYS)


def f48_ssat_183_hl_range_pct_close(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(high - low) / close — daily range as % of price (decays during slow grind)."""
    return _safe_div(high - low, close)


def f48_ssat_184_vol_regime_cross_below_median_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if ATR21 crossed below its trailing 252d median AND was above for prior 21+ bars — vol regime shift."""
    a = _atr(high, low, close, MDAYS)
    med = a.rolling(YDAYS, min_periods=QDAYS).median()
    above = (a > med)
    streak_prev = _streak_true(above).shift(1)
    return ((a <= med) & (streak_prev >= MDAYS)).astype(float).where(med.notna(), np.nan)


# ============================================================
# Bucket Q — Distribution / pattern events (185-194)
# ============================================================

def f48_ssat_185_dist_day_cluster_5_in_21_state(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if 5+ distribution days (down-close on vol > 50d avg) in past 21 — IBD cluster warning."""
    down = close < close.shift(1)
    bigvol = volume > volume.rolling(50, min_periods=20).mean()
    cnt = (down & bigvol).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    return (cnt >= 5).astype(float).where(close.notna(), np.nan)


def f48_ssat_186_dist_day_count_252_post_peak(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Annual count of distribution days — post-peak high count indicates sustained institutional selling."""
    down = close < close.shift(1)
    bigvol = volume > volume.rolling(50, min_periods=20).mean()
    return (down & bigvol).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(close.notna(), np.nan)


def f48_ssat_187_5bar_down_over_up_vol_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-bar sum of down-day vol / 5-bar sum of up-day vol — short-window pressure ratio."""
    up = (close > close.shift(1)).astype(float)
    dn = (close < close.shift(1)).astype(float)
    uv = (up * volume).rolling(WDAYS, min_periods=2).sum()
    dv = (dn * volume).rolling(WDAYS, min_periods=2).sum()
    return _safe_div(dv, uv)


def f48_ssat_188_bearish_gap_count_63(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Count past 63 of gap-down events (open < prev close by > 0.5%) — bearish overnight sentiment."""
    g = _safe_div(open_ - close.shift(1), close.shift(1))
    return (g < -0.005).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(g.notna(), np.nan)


def f48_ssat_189_bearish_gap_unfilled_5_count_63(high: pd.Series, open_: pd.Series, close: pd.Series) -> pd.Series:
    """Count past 63 of gap-down bars whose gap was NOT filled within 5 subsequent bars (PIT-historical).

    Implementation: at bar t, check if t-k (k in 1..5) had gap-down AND the high in [t-k..t] never reached prev_close[t-k]."""
    pc = close.shift(1)
    g = (open_ - pc) / pc
    gap_dn = (g < -0.005)
    not_filled = pd.Series(0.0, index=close.index)
    for k in range(1, 6):
        # at bar t: gap_dn at t-k. The bar's prev_close was pc[t-k]. Was max(high) from t-k+1..t < pc[t-k]?
        gd = gap_dn.shift(k)
        pc_k = pc.shift(k)
        # Max high from k-1 prior bars back through today
        max_high_window = high.rolling(k, min_periods=1).max()
        cond = gd & (max_high_window < pc_k)
        not_filled = not_filled + cond.astype(float).fillna(0.0)
    # not_filled counts the same gap multiple times (once per k); cap at 1 per gap event
    # Simpler: count gap-down events at t-5 that were never filled in t-4..t
    gd5 = gap_dn.shift(5)
    pc5 = pc.shift(5)
    max_high_4 = high.rolling(5, min_periods=1).max()
    cond5 = gd5 & (max_high_4 < pc5)
    return cond5.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(pc5.notna(), np.nan)


def f48_ssat_190_close_in_lowest_10pct_of_21d_range_state(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if close is in lowest 10% of past 21 days' HL range — short-term bottom-of-range state."""
    hmax = high.rolling(MDAYS, min_periods=WDAYS).max()
    lmin = low.rolling(MDAYS, min_periods=WDAYS).min()
    pos = _safe_div(close - lmin, hmax - lmin)
    return (pos < 0.10).astype(float).where(pos.notna(), np.nan)


def f48_ssat_191_close_in_lowest_10pct_of_63d_range_state(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if close in lowest 10% of past 63 days' HL range — medium-term bottom-of-range."""
    hmax = high.rolling(QDAYS, min_periods=MDAYS).max()
    lmin = low.rolling(QDAYS, min_periods=MDAYS).min()
    pos = _safe_div(close - lmin, hmax - lmin)
    return (pos < 0.10).astype(float).where(pos.notna(), np.nan)


def f48_ssat_192_opening_strength_fail_count_63(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Count past 63 of bars where open > prev close (gap up) BUT close < open (opening strength faded)."""
    pc = close.shift(1)
    cond = (open_ > pc) & (close < open_)
    return cond.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(pc.notna(), np.nan)


def f48_ssat_193_close_in_bottom_quartile_count_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count past 21 of bars where (close - low)/(high - low) < 0.25 — bottom-of-day-close count."""
    pos = _safe_div(close - low, high - low)
    return (pos < 0.25).astype(float).rolling(MDAYS, min_periods=WDAYS).sum().where(pos.notna(), np.nan)


def f48_ssat_194_close_in_bottom_quartile_count_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count past 63 of bottom-of-day-close bars."""
    pos = _safe_div(close - low, high - low)
    return (pos < 0.25).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(pos.notna(), np.nan)


# ============================================================
# Bucket R — Statistical / distribution-shape after collapse (195-202)
# ============================================================

def f48_ssat_195_returns_skew_63(close: pd.Series) -> pd.Series:
    """Skew of returns past 63 — negative = downside-heavy distribution."""
    return close.pct_change().rolling(QDAYS, min_periods=MDAYS).skew()


def f48_ssat_196_returns_skew_252(close: pd.Series) -> pd.Series:
    """Annual skew of returns."""
    return close.pct_change().rolling(YDAYS, min_periods=QDAYS).skew()


def f48_ssat_197_returns_kurt_252(close: pd.Series) -> pd.Series:
    """Annual kurtosis of returns — fat-tail measure."""
    return close.pct_change().rolling(YDAYS, min_periods=QDAYS).kurt()


def f48_ssat_198_frac_bars_ret_below_neg1sigma_63(close: pd.Series) -> pd.Series:
    """Fraction of past 63 bars with return < -1*(rolling 63d std)."""
    r = close.pct_change()
    s = r.rolling(QDAYS, min_periods=MDAYS).std()
    return (r < -s).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(s.notna(), np.nan)


def f48_ssat_199_frac_bars_ret_below_neg2sigma_63(close: pd.Series) -> pd.Series:
    """Fraction of past 63 bars with return < -2*sigma (left-tail event frequency)."""
    r = close.pct_change()
    s = r.rolling(QDAYS, min_periods=MDAYS).std()
    return (r < -2 * s).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(s.notna(), np.nan)


def f48_ssat_200_rolling_63d_sum_returns(close: pd.Series) -> pd.Series:
    """Sum of returns past 63 (~quarterly return) — net signed performance."""
    return close.pct_change().rolling(QDAYS, min_periods=MDAYS).sum()


def f48_ssat_201_var95_past_63(close: pd.Series) -> pd.Series:
    """5th percentile of returns past 63 — 95% Value-at-Risk (negative)."""
    return close.pct_change().rolling(QDAYS, min_periods=MDAYS).quantile(0.05)


def f48_ssat_202_var99_past_252(close: pd.Series) -> pd.Series:
    """1st percentile of returns past 252 — 99% VaR (deeply negative)."""
    return close.pct_change().rolling(YDAYS, min_periods=QDAYS).quantile(0.01)


# ============================================================
# Bucket S — Bear-trend persistence / fail-recovery (203-210)
# ============================================================

def f48_ssat_203_longest_below_sma50_streak_252(close: pd.Series) -> pd.Series:
    """Longest below-SMA50 streak in past 252."""
    sma = _sma(close, 50)
    s = _streak_true(close < sma)
    return s.rolling(YDAYS, min_periods=QDAYS).max().where(sma.notna(), np.nan)


def f48_ssat_204_longest_below_sma200_streak_252(close: pd.Series) -> pd.Series:
    """Longest below-SMA200 streak in past 252."""
    sma = _sma(close, 200)
    s = _streak_true(close < sma)
    return s.rolling(YDAYS, min_periods=QDAYS).max().where(sma.notna(), np.nan)


def f48_ssat_205_recovery_attempt_count_63(close: pd.Series) -> pd.Series:
    """Count past 63 of bars where 5d return > 5% — count of upside rally attempts."""
    return (close.pct_change(WDAYS) > 0.05).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(close.pct_change(WDAYS).notna(), np.nan)


def f48_ssat_206_failed_recovery_count_63(close: pd.Series) -> pd.Series:
    """Count past 63 of recovery attempts (5d return > 5%) followed by 5 bars later return < starting price.

    Implementation: at bar t, was there a 5d rally at t-5 (5d return at t-5 > 5%) AND close[t] < close[t-10]?"""
    r5_past = close.pct_change(WDAYS).shift(WDAYS)
    rally_then_below = (r5_past > 0.05) & (close < close.shift(2 * WDAYS))
    return rally_then_below.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(r5_past.notna(), np.nan)


def f48_ssat_207_bearish_ma_stack_state(close: pd.Series) -> pd.Series:
    """1 if SMA21 < SMA50 < SMA200 — bearish MA stack."""
    s21 = _sma(close, MDAYS); s50 = _sma(close, 50); s200 = _sma(close, 200)
    return ((s21 < s50) & (s50 < s200)).astype(float).where(s200.notna(), np.nan)


def f48_ssat_208_bearish_ma_stack_dwell_63(close: pd.Series) -> pd.Series:
    """Fraction past 63 bars in bearish MA stack."""
    s21 = _sma(close, MDAYS); s50 = _sma(close, 50); s200 = _sma(close, 200)
    return ((s21 < s50) & (s50 < s200)).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(s200.notna(), np.nan)


def f48_ssat_209_avg_drawdown_past_63(high: pd.Series, close: pd.Series) -> pd.Series:
    """Mean drawdown over past 63 bars (drawdown = close / 252d-cummax - 1)."""
    dd = _safe_div(close, high.rolling(YDAYS, min_periods=QDAYS).max()) - 1.0
    return dd.rolling(QDAYS, min_periods=MDAYS).mean()


def f48_ssat_210_avg_drawdown_past_252(high: pd.Series, close: pd.Series) -> pd.Series:
    """Annual mean drawdown — sustained underwater regime measure."""
    dd = _safe_div(close, high.rolling(YDAYS, min_periods=QDAYS).max()) - 1.0
    return dd.rolling(YDAYS, min_periods=QDAYS).mean()


# ============================================================
# Bucket T — Composite squeeze-decay (211-225)
# ============================================================

def f48_ssat_211_si_3m_declining_and_below_sma50(shortinterest: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 3 consecutive 21d SI %-changes < 0 AND close < SMA50 — sustained NSIR unwind in down-trend."""
    s = shortinterest.astype(float)
    chg = s.pct_change(MDAYS)
    cond = (chg < 0) & (chg.shift(MDAYS) < 0) & (chg.shift(2 * MDAYS) < 0)
    sma = _sma(close, 50)
    return (cond & (close < sma)).astype(float).where(sma.notna() & chg.notna(), np.nan)


def f48_ssat_212_dtc_decline_and_lower_low_21(daystocover: pd.Series, low: pd.Series) -> pd.Series:
    """1 if daystocover 21d slope < 0 AND 21d-rolling-low fell from 21 bars ago — DTC down + price-structure-breaking."""
    dtc_sl = _rolling_slope(daystocover.astype(float), MDAYS)
    rl = low.rolling(MDAYS, min_periods=WDAYS).min()
    return ((dtc_sl < 0) & (rl < rl.shift(MDAYS))).astype(float).where(dtc_sl.notna() & rl.shift(MDAYS).notna(), np.nan)


def f48_ssat_213_no_shorts_left_but_selling(shortpctfloat: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if short %-float < 5% (shorts gone) AND drawdown <= -50% — fundamental selling, not short-cover."""
    spf = shortpctfloat.astype(float)
    dd = _safe_div(close, high.rolling(YDAYS, min_periods=QDAYS).max()) - 1.0
    return ((spf < 5.0) & (dd <= -0.5)).astype(float).where(spf.notna() & dd.notna(), np.nan)


def f48_ssat_214_si_mean_reverted_plus_drawdown(shortinterest: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if |SI - SI's trailing 252d mean| < 0.5 * SI's trailing 252d std AND drawdown <= -20% — mean-reverted SI + bear price."""
    s = shortinterest.astype(float)
    m = s.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = s.rolling(YDAYS, min_periods=QDAYS).std()
    reverted = ((s - m).abs() < 0.5 * sd)
    dd = _safe_div(close, high.rolling(YDAYS, min_periods=QDAYS).max()) - 1.0
    return (reverted & (dd <= -0.2)).astype(float).where(sd.notna() & dd.notna(), np.nan)


def f48_ssat_215_si_new_252d_low_below_sma200(shortinterest: pd.Series, close: pd.Series) -> pd.Series:
    """1 if SI at trailing 252d min AND close < SMA200 — no short-cover support left + bear price-trend."""
    s = shortinterest.astype(float)
    si_min = s.rolling(YDAYS, min_periods=QDAYS).min()
    sma = _sma(close, 200)
    return ((s <= si_min) & (close < sma)).astype(float).where(si_min.notna() & sma.notna(), np.nan)


def f48_ssat_216_parabolic_ended_with_5plus_capit_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if past-252d 63d-return-max > 100% AND 5+ capitulation bars in past 63 — sustained-selling-post-parabolic."""
    had_parabolic = (close.pct_change(QDAYS).rolling(YDAYS, min_periods=QDAYS).max() > 1.0)
    a = _atr(high, low, close, MDAYS)
    move = close - close.shift(1)
    v_ratio = _safe_div(volume, volume.rolling(MDAYS, min_periods=WDAYS).mean())
    capit_cnt = ((move < -3.0 * a) & (v_ratio > 3.0)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    return (had_parabolic & (capit_cnt >= 5)).astype(float).where(a.notna() & v_ratio.notna(), np.nan)


def f48_ssat_217_capit_streak_count_past_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Longest consecutive capitulation-bar streak in past 63."""
    a = _atr(high, low, close, MDAYS)
    move = close - close.shift(1)
    v_ratio = _safe_div(volume, volume.rolling(MDAYS, min_periods=WDAYS).mean())
    capit = (move < -3.0 * a) & (v_ratio > 3.0)
    s = _streak_true(capit)
    return s.rolling(QDAYS, min_periods=MDAYS).max().where(a.notna() & v_ratio.notna(), np.nan)


def f48_ssat_218_down_streak_with_low_vol_state(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if 5+ down-close streak AND volume < 21d avg — orderly decline (low-vol bleed)."""
    down_streak = _streak_true(close < close.shift(1))
    v_avg = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    return ((down_streak >= 5) & (volume < v_avg)).astype(float).where(v_avg.notna(), np.nan)


def f48_ssat_219_bear_cross_and_rsi_below_50_and_below_sma200(close: pd.Series) -> pd.Series:
    """1 if SMA50 < SMA200 AND RSI(14) < 50 AND close < SMA200 — 3-condition bearish confirmation."""
    s50 = _sma(close, 50); s200 = _sma(close, 200)
    r = _rsi(close, 14)
    return ((s50 < s200) & (r < 50) & (close < s200)).astype(float).where(s200.notna() & r.notna(), np.nan)


def f48_ssat_220_3m_down_vol_dominant_state(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if down-vol > up-vol over each of past 3 months (21d windows) — sustained selling pressure."""
    up = (close > close.shift(1)).astype(float)
    dn = (close < close.shift(1)).astype(float)
    uv_21 = (up * volume).rolling(MDAYS, min_periods=WDAYS).sum()
    dv_21 = (dn * volume).rolling(MDAYS, min_periods=WDAYS).sum()
    dom = (dv_21 > uv_21)
    return (dom & dom.shift(MDAYS) & dom.shift(2 * MDAYS)).astype(float).where(uv_21.notna(), np.nan)


def f48_ssat_221_consecutive_close_below_21d_high_streak(high: pd.Series, close: pd.Series) -> pd.Series:
    """Current consecutive run of close < 21d-rolling-high — time-below-recent-high."""
    rh = high.rolling(MDAYS, min_periods=WDAYS).max()
    return _streak_true(close < rh).where(rh.notna(), np.nan)


def f48_ssat_222_aftermath_severity_dd_x_bars_since_peak(high: pd.Series, close: pd.Series) -> pd.Series:
    """|drawdown| * bars-since-252d-high — aftermath severity score (deeper + longer = worse)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd_abs = (_safe_div(close, rmax) - 1.0).abs()
    bs = _bars_since_true(high == rmax)
    return dd_abs * bs


def f48_ssat_223_terminal_decline_acceleration(close: pd.Series) -> pd.Series:
    """1 if 21d slope of log-close < -0.005 per bar — accelerating decline state."""
    sl = _rolling_slope(_safe_log(close), MDAYS)
    return (sl < -0.005).astype(float).where(sl.notna(), np.nan)


def f48_ssat_224_orderly_bear_vol_of_vol_falling(close: pd.Series) -> pd.Series:
    """1 if 21d vol-of-realized-vol falling (21d slope < 0) AND 21d return < 0 — orderly bear."""
    rv = close.pct_change().rolling(MDAYS, min_periods=WDAYS).std()
    rv_slope = _rolling_slope(rv, MDAYS)
    r21 = close.pct_change(MDAYS)
    return ((rv_slope < 0) & (r21 < 0)).astype(float).where(rv_slope.notna() & r21.notna(), np.nan)


def f48_ssat_225_si_below_sma63_and_near_252d_low(shortinterest: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if SI < SMA63(SI) AND close within 5% of 252d low — final-stage indicator (low SI + low price)."""
    s = shortinterest.astype(float)
    sma_si = _sma(s, QDAYS)
    lmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    near_low = (close / lmin - 1.0) < 0.05
    return ((s < sma_si) & near_low).astype(float).where(sma_si.notna() & lmin.notna(), np.nan)


# ============================================================
#                         REGISTRY 151-225
# ============================================================

_HC = ["high", "close"]
_HLC = ["high", "low", "close"]
_HLCV = ["high", "low", "close", "volume"]
_CV = ["close", "volume"]
_HCV = ["high", "close", "volume"]
_LC = ["low", "close"]

SHORT_SQUEEZE_AFTERMATH_TECHNICAL_BASE_REGISTRY_151_225 = {
    "f48_ssat_151_lower_high_count_63": {"inputs": ["high"], "func": f48_ssat_151_lower_high_count_63},
    "f48_ssat_152_lower_high_count_252": {"inputs": ["high"], "func": f48_ssat_152_lower_high_count_252},
    "f48_ssat_153_lower_low_count_63": {"inputs": ["low"], "func": f48_ssat_153_lower_low_count_63},
    "f48_ssat_154_lower_low_count_252": {"inputs": ["low"], "func": f48_ssat_154_lower_low_count_252},
    "f48_ssat_155_bars_since_new_252d_low": {"inputs": ["low"], "func": f48_ssat_155_bars_since_new_252d_low},
    "f48_ssat_156_count_new_252d_lows_past_252": {"inputs": ["low"], "func": f48_ssat_156_count_new_252d_lows_past_252},
    "f48_ssat_157_bear_flag_flag": {"inputs": _HLC, "func": f48_ssat_157_bear_flag_flag},
    "f48_ssat_158_bear_pennant_compression": {"inputs": ["high", "low"], "func": f48_ssat_158_bear_pennant_compression},
    "f48_ssat_159_failed_rally_count_63": {"inputs": _HLC, "func": f48_ssat_159_failed_rally_count_63},
    "f48_ssat_160_close_below_sma200_streak": {"inputs": ["close"], "func": f48_ssat_160_close_below_sma200_streak},
    "f48_ssat_161_dist_aVWAP_from_252d_peak_atr21": {"inputs": _HLCV, "func": f48_ssat_161_dist_aVWAP_from_252d_peak_atr21},
    "f48_ssat_162_dist_aVWAP_from_252d_peak_pct": {"inputs": _HCV, "func": f48_ssat_162_dist_aVWAP_from_252d_peak_pct},
    "f48_ssat_163_bars_since_touched_aVWAP_from_peak": {"inputs": _HCV, "func": f48_ssat_163_bars_since_touched_aVWAP_from_peak},
    "f48_ssat_164_close_above_aVWAP_from_peak_state": {"inputs": _HCV, "func": f48_ssat_164_close_above_aVWAP_from_peak_state},
    "f48_ssat_165_dist_sma200_atr21": {"inputs": _HLC, "func": f48_ssat_165_dist_sma200_atr21},
    "f48_ssat_166_dist_sma200_pct": {"inputs": ["close"], "func": f48_ssat_166_dist_sma200_pct},
    "f48_ssat_167_below_sma200_streak_current": {"inputs": ["close"], "func": f48_ssat_167_below_sma200_streak_current},
    "f48_ssat_168_longest_below_sma200_streak_252": {"inputs": ["close"], "func": f48_ssat_168_longest_below_sma200_streak_252},
    "f48_ssat_169_up_over_down_vol_ratio_252": {"inputs": _CV, "func": f48_ssat_169_up_over_down_vol_ratio_252},
    "f48_ssat_170_down_vol_zscore_252": {"inputs": _CV, "func": f48_ssat_170_down_vol_zscore_252},
    "f48_ssat_171_low_vol_rally_count_63": {"inputs": _CV, "func": f48_ssat_171_low_vol_rally_count_63},
    "f48_ssat_172_capit_then_rally_count_63": {"inputs": ["close"], "func": f48_ssat_172_capit_then_rally_count_63},
    "f48_ssat_173_failed_rally_volume_pattern_63": {"inputs": _HCV, "func": f48_ssat_173_failed_rally_volume_pattern_63},
    "f48_ssat_174_low_vol_rally_count_21": {"inputs": _CV, "func": f48_ssat_174_low_vol_rally_count_21},
    "f48_ssat_175_rally_vol_decay_slope_21": {"inputs": _CV, "func": f48_ssat_175_rally_vol_decay_slope_21},
    "f48_ssat_176_atr21_in_lowest_decile_252": {"inputs": _HLC, "func": f48_ssat_176_atr21_in_lowest_decile_252},
    "f48_ssat_177_atr21_in_lowest_quintile_252": {"inputs": _HLC, "func": f48_ssat_177_atr21_in_lowest_quintile_252},
    "f48_ssat_178_bars_since_atr21_top_decile_252": {"inputs": _HLC, "func": f48_ssat_178_bars_since_atr21_top_decile_252},
    "f48_ssat_179_nr7_count_63": {"inputs": ["high", "low"], "func": f48_ssat_179_nr7_count_63},
    "f48_ssat_180_range_21_over_range_252": {"inputs": ["high", "low"], "func": f48_ssat_180_range_21_over_range_252},
    "f48_ssat_181_hl_range_slope_63_negative": {"inputs": ["high", "low"], "func": f48_ssat_181_hl_range_slope_63_negative},
    "f48_ssat_182_intra_bar_range_expansion_zscore": {"inputs": _HLC, "func": f48_ssat_182_intra_bar_range_expansion_zscore},
    "f48_ssat_183_hl_range_pct_close": {"inputs": _HLC, "func": f48_ssat_183_hl_range_pct_close},
    "f48_ssat_184_vol_regime_cross_below_median_event": {"inputs": _HLC, "func": f48_ssat_184_vol_regime_cross_below_median_event},
    "f48_ssat_185_dist_day_cluster_5_in_21_state": {"inputs": _CV, "func": f48_ssat_185_dist_day_cluster_5_in_21_state},
    "f48_ssat_186_dist_day_count_252_post_peak": {"inputs": _CV, "func": f48_ssat_186_dist_day_count_252_post_peak},
    "f48_ssat_187_5bar_down_over_up_vol_ratio": {"inputs": _CV, "func": f48_ssat_187_5bar_down_over_up_vol_ratio},
    "f48_ssat_188_bearish_gap_count_63": {"inputs": ["open", "close"], "func": f48_ssat_188_bearish_gap_count_63},
    "f48_ssat_189_bearish_gap_unfilled_5_count_63": {"inputs": ["high", "open", "close"], "func": f48_ssat_189_bearish_gap_unfilled_5_count_63},
    "f48_ssat_190_close_in_lowest_10pct_of_21d_range_state": {"inputs": _HLC, "func": f48_ssat_190_close_in_lowest_10pct_of_21d_range_state},
    "f48_ssat_191_close_in_lowest_10pct_of_63d_range_state": {"inputs": _HLC, "func": f48_ssat_191_close_in_lowest_10pct_of_63d_range_state},
    "f48_ssat_192_opening_strength_fail_count_63": {"inputs": ["open", "close"], "func": f48_ssat_192_opening_strength_fail_count_63},
    "f48_ssat_193_close_in_bottom_quartile_count_21": {"inputs": _HLC, "func": f48_ssat_193_close_in_bottom_quartile_count_21},
    "f48_ssat_194_close_in_bottom_quartile_count_63": {"inputs": _HLC, "func": f48_ssat_194_close_in_bottom_quartile_count_63},
    "f48_ssat_195_returns_skew_63": {"inputs": ["close"], "func": f48_ssat_195_returns_skew_63},
    "f48_ssat_196_returns_skew_252": {"inputs": ["close"], "func": f48_ssat_196_returns_skew_252},
    "f48_ssat_197_returns_kurt_252": {"inputs": ["close"], "func": f48_ssat_197_returns_kurt_252},
    "f48_ssat_198_frac_bars_ret_below_neg1sigma_63": {"inputs": ["close"], "func": f48_ssat_198_frac_bars_ret_below_neg1sigma_63},
    "f48_ssat_199_frac_bars_ret_below_neg2sigma_63": {"inputs": ["close"], "func": f48_ssat_199_frac_bars_ret_below_neg2sigma_63},
    "f48_ssat_200_rolling_63d_sum_returns": {"inputs": ["close"], "func": f48_ssat_200_rolling_63d_sum_returns},
    "f48_ssat_201_var95_past_63": {"inputs": ["close"], "func": f48_ssat_201_var95_past_63},
    "f48_ssat_202_var99_past_252": {"inputs": ["close"], "func": f48_ssat_202_var99_past_252},
    "f48_ssat_203_longest_below_sma50_streak_252": {"inputs": ["close"], "func": f48_ssat_203_longest_below_sma50_streak_252},
    "f48_ssat_204_longest_below_sma200_streak_252": {"inputs": ["close"], "func": f48_ssat_204_longest_below_sma200_streak_252},
    "f48_ssat_205_recovery_attempt_count_63": {"inputs": ["close"], "func": f48_ssat_205_recovery_attempt_count_63},
    "f48_ssat_206_failed_recovery_count_63": {"inputs": ["close"], "func": f48_ssat_206_failed_recovery_count_63},
    "f48_ssat_207_bearish_ma_stack_state": {"inputs": ["close"], "func": f48_ssat_207_bearish_ma_stack_state},
    "f48_ssat_208_bearish_ma_stack_dwell_63": {"inputs": ["close"], "func": f48_ssat_208_bearish_ma_stack_dwell_63},
    "f48_ssat_209_avg_drawdown_past_63": {"inputs": _HC, "func": f48_ssat_209_avg_drawdown_past_63},
    "f48_ssat_210_avg_drawdown_past_252": {"inputs": _HC, "func": f48_ssat_210_avg_drawdown_past_252},
    "f48_ssat_211_si_3m_declining_and_below_sma50": {"inputs": ["shortinterest", "close"], "func": f48_ssat_211_si_3m_declining_and_below_sma50},
    "f48_ssat_212_dtc_decline_and_lower_low_21": {"inputs": ["daystocover", "low"], "func": f48_ssat_212_dtc_decline_and_lower_low_21},
    "f48_ssat_213_no_shorts_left_but_selling": {"inputs": ["shortpctfloat", "high", "close"], "func": f48_ssat_213_no_shorts_left_but_selling},
    "f48_ssat_214_si_mean_reverted_plus_drawdown": {"inputs": ["shortinterest", "high", "close"], "func": f48_ssat_214_si_mean_reverted_plus_drawdown},
    "f48_ssat_215_si_new_252d_low_below_sma200": {"inputs": ["shortinterest", "close"], "func": f48_ssat_215_si_new_252d_low_below_sma200},
    "f48_ssat_216_parabolic_ended_with_5plus_capit_63": {"inputs": _HLCV, "func": f48_ssat_216_parabolic_ended_with_5plus_capit_63},
    "f48_ssat_217_capit_streak_count_past_63": {"inputs": _HLCV, "func": f48_ssat_217_capit_streak_count_past_63},
    "f48_ssat_218_down_streak_with_low_vol_state": {"inputs": _CV, "func": f48_ssat_218_down_streak_with_low_vol_state},
    "f48_ssat_219_bear_cross_and_rsi_below_50_and_below_sma200": {"inputs": ["close"], "func": f48_ssat_219_bear_cross_and_rsi_below_50_and_below_sma200},
    "f48_ssat_220_3m_down_vol_dominant_state": {"inputs": _CV, "func": f48_ssat_220_3m_down_vol_dominant_state},
    "f48_ssat_221_consecutive_close_below_21d_high_streak": {"inputs": _HC, "func": f48_ssat_221_consecutive_close_below_21d_high_streak},
    "f48_ssat_222_aftermath_severity_dd_x_bars_since_peak": {"inputs": _HC, "func": f48_ssat_222_aftermath_severity_dd_x_bars_since_peak},
    "f48_ssat_223_terminal_decline_acceleration": {"inputs": ["close"], "func": f48_ssat_223_terminal_decline_acceleration},
    "f48_ssat_224_orderly_bear_vol_of_vol_falling": {"inputs": ["close"], "func": f48_ssat_224_orderly_bear_vol_of_vol_falling},
    "f48_ssat_225_si_below_sma63_and_near_252d_low": {"inputs": ["shortinterest", "low", "close"], "func": f48_ssat_225_si_below_sma63_and_near_252d_low},
}
