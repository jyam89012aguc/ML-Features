"""ultimate_aroon_vortex d1 features 376-450 — Pipeline 1b-technical.

Third batch (second file): continues 150 NEW atomic-leaning hypotheses.
Indices 376-450. Range-expansion / Mass-Index ingredient atomics,
Wilder failure-swing taxonomy (UO / DMI / Aroon variants), Choppiness /
Vortex / Aroon-specific atomic gaps, bar-pattern detectors at the high,
long-horizon ADX/ADXR fingerprints, and consecutive-bar streak atomics.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit
min_periods, no centered windows, no .shift(N). Self-contained helpers — no
cross-family imports.
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
        xm = x.mean()
        wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)

def _wilder_ema(s, n):
    return s.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()

def _dm_raw(high, low):
    up = high.diff()
    dn = -low.diff()
    plus_dm = pd.Series(np.where((up > dn) & (up > 0), up, 0.0), index=high.index)
    minus_dm = pd.Series(np.where((dn > up) & (dn > 0), dn, 0.0), index=high.index)
    return (plus_dm, minus_dm)

def _dm_components(high, low, close, n=14):
    plus_dm, minus_dm = _dm_raw(high, low)
    tr = _true_range(high, low, close)
    atr = _wilder_ema(tr, n)
    plus_di = 100.0 * _safe_div(_wilder_ema(plus_dm, n), atr)
    minus_di = 100.0 * _safe_div(_wilder_ema(minus_dm, n), atr)
    dx = 100.0 * _safe_div((plus_di - minus_di).abs(), plus_di + minus_di)
    adx = _wilder_ema(dx, n)
    return (plus_di, minus_di, adx)

def _adxr(high, low, close, n=14):
    _, _, adx = _dm_components(high, low, close, n=n)
    return 0.5 * (adx + adx.shift(n - 1))

def _aroon_up(high, n):

    def _f(w):
        if np.isnan(w).all():
            return np.nan
        idx = int(np.nanargmax(w))
        return 100.0 * idx / (len(w) - 1) if len(w) > 1 else np.nan
    return high.rolling(n + 1, min_periods=max((n + 1) // 2, 2)).apply(_f, raw=True)

def _aroon_down(low, n):

    def _f(w):
        if np.isnan(w).all():
            return np.nan
        idx = int(np.nanargmin(w))
        return 100.0 * idx / (len(w) - 1) if len(w) > 1 else np.nan
    return low.rolling(n + 1, min_periods=max((n + 1) // 2, 2)).apply(_f, raw=True)

def _vortex(high, low, close, n=14):
    pc = close.shift(1)
    ph = high.shift(1)
    pl = low.shift(1)
    vm_plus = (high - pl).abs()
    vm_minus = (low - ph).abs()
    tr = pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    sum_vm_plus = vm_plus.rolling(n, min_periods=max(n // 2, 2)).sum()
    sum_vm_minus = vm_minus.rolling(n, min_periods=max(n // 2, 2)).sum()
    sum_tr = tr.rolling(n, min_periods=max(n // 2, 2)).sum()
    return (_safe_div(sum_vm_plus, sum_tr), _safe_div(sum_vm_minus, sum_tr))

def _ultimate_osc(high, low, close, n1=7, n2=14, n3=28):
    pc = close.shift(1)
    bp = close - pd.concat([low, pc], axis=1).min(axis=1)
    tr = pd.concat([high, pc], axis=1).max(axis=1) - pd.concat([low, pc], axis=1).min(axis=1)
    bp_s1 = bp.rolling(n1, min_periods=max(n1 // 2, 2)).sum()
    tr_s1 = tr.rolling(n1, min_periods=max(n1 // 2, 2)).sum()
    bp_s2 = bp.rolling(n2, min_periods=max(n2 // 2, 2)).sum()
    tr_s2 = tr.rolling(n2, min_periods=max(n2 // 2, 2)).sum()
    bp_s3 = bp.rolling(n3, min_periods=max(n3 // 2, 2)).sum()
    tr_s3 = tr.rolling(n3, min_periods=max(n3 // 2, 2)).sum()
    a1 = _safe_div(bp_s1, tr_s1)
    a2 = _safe_div(bp_s2, tr_s2)
    a3 = _safe_div(bp_s3, tr_s3)
    return 100.0 * (4.0 * a1 + 2.0 * a2 + a3) / 7.0

def _choppiness(high, low, close, n=14):
    tr = _true_range(high, low, close)
    sum_tr = tr.rolling(n, min_periods=max(n // 2, 2)).sum()
    hi = high.rolling(n, min_periods=max(n // 2, 2)).max()
    lo = low.rolling(n, min_periods=max(n // 2, 2)).min()
    ratio = _safe_div(sum_tr, hi - lo)
    return 100.0 * np.log10(ratio.where(ratio > 0, np.nan)) / np.log10(n)

def _mass_index(high, low, n=25, ema_n=9):
    rng = high - low
    e1 = rng.ewm(span=ema_n, adjust=False, min_periods=ema_n).mean()
    e2 = e1.ewm(span=ema_n, adjust=False, min_periods=ema_n).mean()
    r = _safe_div(e1, e2)
    return r.rolling(n, min_periods=max(n // 2, 2)).sum()

def _range_expansion_ratio(high, low, ema_n=9):
    rng = high - low
    e1 = rng.ewm(span=ema_n, adjust=False, min_periods=ema_n).mean()
    e2 = e1.ewm(span=ema_n, adjust=False, min_periods=ema_n).mean()
    return _safe_div(e1, e2)

def _bars_since(condition_series, lookback):

    def _bsm(w):
        idx = np.where(w > 0)[0]
        if idx.size == 0:
            return float(len(w))
        return float(len(w) - 1 - idx[-1])
    return condition_series.astype(float).rolling(lookback, min_periods=max(lookback // 3, 2)).apply(_bsm, raw=True)

def _streak_true(cond):
    """Running consecutive-bar streak that `cond` is True (resets to 0 when False)."""
    c = cond.astype(float).fillna(0.0).values
    n = len(c)
    out = np.zeros(n, dtype=float)
    s = 0
    for i in range(n):
        s = s + 1 if c[i] > 0 else 0
        out[i] = float(s)
    res = pd.Series(out, index=cond.index)
    return res.where(cond.notna(), np.nan)

def f29_uarn_376_true_range_percentile_rank_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of today's TR in trailing 252d — range-expansion intensity (0-1 scale)."""
    tr = _true_range(high, low, close)
    return tr.rolling(YDAYS, min_periods=QDAYS).rank(pct=True).diff()

def f29_uarn_377_high_low_range_percentile_rank_252d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of today's H-L range in trailing 252d (Mass-Index input atomic)."""
    rng = high - low
    return rng.rolling(YDAYS, min_periods=QDAYS).rank(pct=True).diff()

def f29_uarn_378_ema9_hl_percentile_rank_252d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of EMA9(H-L) in trailing 252d — Mass-Index inner smoothed input."""
    rng = high - low
    e1 = rng.ewm(span=9, adjust=False, min_periods=9).mean()
    return e1.rolling(YDAYS, min_periods=QDAYS).rank(pct=True).diff()

def f29_uarn_379_double_ema9_hl_percentile_rank_252d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of EMA9(EMA9(H-L)) in trailing 252d — Mass-Index denominator atomic."""
    rng = high - low
    e1 = rng.ewm(span=9, adjust=False, min_periods=9).mean()
    e2 = e1.ewm(span=9, adjust=False, min_periods=9).mean()
    return e2.rolling(YDAYS, min_periods=QDAYS).rank(pct=True).diff()

def f29_uarn_380_wide_range_days_count_21d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of bars in trailing 21d with H-L > 2 × mean(H-L over 21d) — wide-range-bar burst count."""
    rng = high - low
    m = rng.rolling(MDAYS, min_periods=WDAYS).mean()
    cond = rng > 2.0 * m
    return cond.astype(float).rolling(MDAYS, min_periods=WDAYS).sum().diff()

def f29_uarn_381_mass_index_value_normalized_to_252d_range_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """(MI − min(MI, 252)) / (max(MI, 252) − min(MI, 252)): MI percentile in annual range."""
    mi = _mass_index(high, low, n=25, ema_n=9)
    rmin = mi.rolling(YDAYS, min_periods=QDAYS).min()
    rmax = mi.rolling(YDAYS, min_periods=QDAYS).max()
    return _safe_div(mi - rmin, rmax - rmin).diff()

def f29_uarn_382_range_expansion_ratio_smoothed_5d_median_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """5d rolling median of EMA9(H-L)/EMA9(EMA9(H-L)) — smoothed range-expansion ratio."""
    r = _range_expansion_ratio(high, low, ema_n=9)
    return r.rolling(WDAYS, min_periods=2).median().diff()

def f29_uarn_383_atr_to_atr252_ratio_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR(21) / ATR(252): short vs annual volatility regime (>1 = expansion)."""
    atr_s = _atr(high, low, close, n=MDAYS)
    atr_l = _atr(high, low, close, n=YDAYS)
    return _safe_div(atr_s, atr_l).diff()

def f29_uarn_384_close_to_close_range_percentile_252d_d1(close: pd.Series) -> pd.Series:
    """Percentile rank of |close_change| in trailing 252d — annual close-to-close move intensity."""
    chg = close.diff().abs()
    return chg.rolling(YDAYS, min_periods=QDAYS).rank(pct=True).diff()

def f29_uarn_385_mass_index_above_25_count_21d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count in trailing 21d where MI(25) > 25 (above mean baseline) — monthly bulge-formation count."""
    mi = _mass_index(high, low, n=25, ema_n=9)
    return (mi > 25.0).astype(float).rolling(MDAYS, min_periods=WDAYS).sum().diff()

def f29_uarn_386_range_expansion_ratio_above_one_streak_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Current consecutive-bar streak with inner range-expansion ratio > 1 — expansion-persistence."""
    r = _range_expansion_ratio(high, low, ema_n=9)
    cond = r > 1.0
    return _streak_true(cond).diff()

def f29_uarn_387_mass_index_minus_25_smoothed_5d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """5d-mean of (MI(25) − 25) — smoothed deviation above mean baseline."""
    mi = _mass_index(high, low, n=25, ema_n=9)
    return (mi - 25.0).rolling(WDAYS, min_periods=2).mean().diff()

def f29_uarn_388_true_range_atr_ratio_21d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Today's TR / ATR(21): single-bar range relative to monthly average — anomaly score."""
    tr = _true_range(high, low, close)
    atr = _atr(high, low, close, n=MDAYS)
    return _safe_div(tr, atr).diff()

def f29_uarn_389_high_low_range_zscore_63d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of H-L range in trailing 63d — quarterly range-anomaly atomic."""
    return _rolling_zscore(high - low, QDAYS, min_periods=MDAYS).diff()

def f29_uarn_390_mass_index_distance_above_27_clipped_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """max(MI(25) − 27, 0): non-negative distance above the 27 setup line (zero outside bulge zone)."""
    mi = _mass_index(high, low, n=25, ema_n=9)
    return (mi - 27.0).clip(lower=0.0).diff()

def f29_uarn_391_uo_wilder_failure_swing_bearish_full_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Wilder bearish failure swing for UO: lower-high formation above 70 followed by failure below interim low."""
    uo = _ultimate_osc(high, low, close, 7, 14, 28)
    high20 = uo.rolling(MDAYS, min_periods=WDAYS).max()
    low_between = uo.rolling(WDAYS, min_periods=2).min().shift(1)
    prior_high = uo.rolling(MDAYS, min_periods=WDAYS).max().shift(MDAYS)
    cond = (prior_high > 70.0) & (high20 < prior_high) & (uo < low_between)
    return cond.astype(float).where(uo.notna(), np.nan).diff()

def f29_uarn_392_uo_wilder_failure_swing_bullish_full_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Wilder bullish failure swing for UO: higher-low formation below 30 followed by rally above interim high."""
    uo = _ultimate_osc(high, low, close, 7, 14, 28)
    low20 = uo.rolling(MDAYS, min_periods=WDAYS).min()
    high_between = uo.rolling(WDAYS, min_periods=2).max().shift(1)
    prior_low = uo.rolling(MDAYS, min_periods=WDAYS).min().shift(MDAYS)
    cond = (prior_low < 30.0) & (low20 > prior_low) & (uo > high_between)
    return cond.astype(float).where(uo.notna(), np.nan).diff()

def f29_uarn_393_dmi_bearish_failure_swing_event_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """DMI bearish failure swing: DI- spiked above DI+ in trailing 14d, DI+ recovered, but lower than its prior peak."""
    p, m, _ = _dm_components(high, low, close, n=14)
    dm_spike = (m > p).rolling(MDAYS, min_periods=WDAYS).max() > 0
    p_curr_above = p > m
    p_curr_lt_recent_peak = p < p.rolling(MDAYS, min_periods=WDAYS).max()
    cond = dm_spike & p_curr_above & p_curr_lt_recent_peak
    return cond.astype(float).where(p.notna() & m.notna(), np.nan).diff()

def f29_uarn_394_aroon_failure_swing_up_to_down_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Aroon failure swing: Aroon-Up was 100 within 21 bars AND Aroon-Down hits 100 today."""
    au = _aroon_up(high, 25)
    ad = _aroon_down(low, 25)
    recent_up_peak = ((au >= 99.999).rolling(MDAYS, min_periods=WDAYS).max() > 0).shift(1).fillna(False)
    cond = recent_up_peak & (ad >= 99.999)
    return cond.astype(float).where(au.notna() & ad.notna(), np.nan).diff()

def f29_uarn_395_adx_hook_formation_after_50_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ADX-hook event: ADX peaked above 50 in trailing 21d and ADX has now turned down for 2 consecutive bars."""
    _, _, adx = _dm_components(high, low, close, n=14)
    peak_above_50 = adx.rolling(MDAYS, min_periods=WDAYS).max() > 50.0
    turning_down = (adx.diff() < 0) & (adx.diff().shift(1) < 0)
    cond = peak_above_50 & turning_down
    return cond.astype(float).where(adx.notna(), np.nan).diff()

def f29_uarn_396_adx_hook_formation_after_40_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ADX-hook event (lower threshold): ADX peaked above 40 in trailing 21d and now 2-bar declining."""
    _, _, adx = _dm_components(high, low, close, n=14)
    peak_above_40 = adx.rolling(MDAYS, min_periods=WDAYS).max() > 40.0
    turning_down = (adx.diff() < 0) & (adx.diff().shift(1) < 0)
    cond = peak_above_40 & turning_down
    return cond.astype(float).where(adx.notna(), np.nan).diff()

def f29_uarn_397_di_minus_above_di_plus_with_adx_falling_from_high_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Canonical sell-takeover: DI- crosses above DI+ while ADX is falling from a peak above 40 in 21d."""
    p, m, _ = _dm_components(high, low, close, n=14)
    _, _, adx = _dm_components(high, low, close, n=14)
    cross = (m > p) & (m.shift(1) <= p.shift(1))
    peak40 = adx.rolling(MDAYS, min_periods=WDAYS).max() > 40.0
    falling = adx.diff() < 0
    cond = cross & peak40 & falling
    return cond.astype(float).where(p.notna() & adx.notna(), np.nan).diff()

def f29_uarn_398_bearish_outside_day_at_252d_high_d1(high: pd.Series, low: pd.Series, close: pd.Series, open_: pd.Series) -> pd.Series:
    """Bearish outside-day at 252d high: today high == 252d max, close < open, today H-L engulfs prior bar's range."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = high >= rmax
    bearish = close < open_
    engulf = (high > high.shift(1)) & (low < low.shift(1))
    cond = at_peak & bearish & engulf
    return cond.astype(float).where(close.notna(), np.nan).diff()

def f29_uarn_399_close_below_open_on_new_252d_high_d1(open_: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    """Single-bar bearish-marker at peak: today high prints 252d new max, close ends below open."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = high >= rmax
    cond = at_peak & (close < open_)
    return cond.astype(float).where(close.notna(), np.nan).diff()

def f29_uarn_400_lower_high_with_di_minus_rising_3d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite: today lower-high vs yesterday AND DI-(14) rising for 3 consecutive bars."""
    _, m, _ = _dm_components(high, low, close, n=14)
    lower_hi = high < high.shift(1)
    rising3 = (m.diff() > 0) & (m.diff().shift(1) > 0) & (m.diff().shift(2) > 0)
    cond = lower_hi & rising3
    return cond.astype(float).where(m.notna(), np.nan).diff()

def f29_uarn_401_mass_bulge_with_close_below_open_d1(high: pd.Series, low: pd.Series, close: pd.Series, open_: pd.Series) -> pd.Series:
    """Composite: Dorsey reversal-bulge confirm (MI > 27 then below 26.5) AND today close < open."""
    mi = _mass_index(high, low, n=25, ema_n=9)
    bulge = mi.rolling(MDAYS, min_periods=WDAYS).max() > 27.0
    trigger = bulge & (mi < 26.5) & (mi.shift(1) >= 26.5)
    cond = trigger & (close < open_)
    return cond.astype(float).where(mi.notna(), np.nan).diff()

def f29_uarn_402_adx_local_peak_above_50_event_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ADX(14) local peak (higher than both neighbors) AND that peak value > 50 — extreme-trend peak event."""
    _, _, adx = _dm_components(high, low, close, n=14)
    is_peak = (adx.shift(1) > adx) & (adx.shift(1) > adx.shift(2))
    above_50 = adx.shift(1) > 50.0
    cond = is_peak & above_50
    return cond.astype(float).where(adx.notna(), np.nan).diff()

def f29_uarn_403_uo_failure_swing_at_top_25d_window_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """UO failure-swing condition formed in 25d window WHILE price near 252d max (within 5%)."""
    uo = _ultimate_osc(high, low, close, 7, 14, 28)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near_peak = high >= 0.95 * rmax
    prior_high = uo.rolling(MDAYS, min_periods=WDAYS).max().shift(MDAYS)
    curr_high = uo.rolling(MDAYS, min_periods=WDAYS).max()
    cond = near_peak & (prior_high > 70.0) & (curr_high < prior_high)
    return cond.astype(float).where(uo.notna(), np.nan).diff()

def f29_uarn_404_aroon_lower_high_oscillator_event_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Aroon-Osc(25) lower-high formation: current 21d max < previous 21d max — recency-balance deterioration."""
    osc = _aroon_up(high, 25) - _aroon_down(low, 25)
    curr = osc.rolling(MDAYS, min_periods=WDAYS).max()
    prior = osc.rolling(MDAYS, min_periods=WDAYS).max().shift(MDAYS)
    cond = (curr < prior) & (prior > 0)
    return cond.astype(float).where(osc.notna(), np.nan).diff()

def f29_uarn_405_di_minus_higher_high_with_price_lower_high_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """DI- prints 21d higher-high while price prints 21d lower-high — DM divergence at top."""
    _, m, _ = _dm_components(high, low, close, n=14)
    m_hh = m >= m.rolling(MDAYS, min_periods=WDAYS).max()
    price_lh = high < high.rolling(MDAYS, min_periods=WDAYS).max().shift(1)
    cond = m_hh & price_lh
    return cond.astype(float).where(m.notna(), np.nan).diff()

def f29_uarn_406_choppiness_at_252d_max_indicator_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: today Choppiness(14) equals its 252d max — at-regime-extreme marker."""
    ci = _choppiness(high, low, close, n=14)
    rmax = ci.rolling(YDAYS, min_periods=QDAYS).max()
    cond = (ci >= rmax) & ci.notna()
    return cond.astype(float).where(ci.notna(), np.nan).diff()

def f29_uarn_407_choppiness_at_252d_min_indicator_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: today Choppiness(14) equals its 252d min — strongest-trend-of-year marker."""
    ci = _choppiness(high, low, close, n=14)
    rmin = ci.rolling(YDAYS, min_periods=QDAYS).min()
    cond = (ci <= rmin) & ci.notna()
    return cond.astype(float).where(ci.notna(), np.nan).diff()

def f29_uarn_408_choppiness_distance_from_252d_min_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """CI(14) − min(CI(14), 252d): distance from annual trough — recovery into ranging-side."""
    ci = _choppiness(high, low, close, n=14)
    return (ci - ci.rolling(YDAYS, min_periods=QDAYS).min()).diff()

def f29_uarn_409_choppiness_distance_from_252d_max_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """max(CI(14), 252d) − CI(14): distance below annual peak — descent off ranging-extreme."""
    ci = _choppiness(high, low, close, n=14)
    return (ci.rolling(YDAYS, min_periods=QDAYS).max() - ci).diff()

def f29_uarn_410_choppiness_above_61_streak_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current consecutive-bar streak with CI(14) > 61.8 — ranging-regime persistence."""
    ci = _choppiness(high, low, close, n=14)
    return _streak_true(ci > 61.8).diff()

def f29_uarn_411_choppiness_below_38_streak_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current consecutive-bar streak with CI(14) < 38.2 — trending-regime persistence."""
    ci = _choppiness(high, low, close, n=14)
    return _streak_true(ci < 38.2).diff()

def f29_uarn_412_choppiness_inside_band_streak_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current consecutive-bar streak with CI(14) in [38.2, 61.8] band — transitional-zone dwell."""
    ci = _choppiness(high, low, close, n=14)
    inside = (ci >= 38.2) & (ci <= 61.8)
    return _streak_true(inside).diff()

def f29_uarn_413_choppiness_rise_in_21d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """CI(14) today − CI(14) 21d ago: monthly regime-tilt direction (positive = becoming more ranging)."""
    ci = _choppiness(high, low, close, n=14)
    return (ci - ci.shift(MDAYS)).diff()

def f29_uarn_414_choppiness_long_50d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Choppiness(50) — bi-monthly regime classification (slow regime atomic; long-horizon hypothesis)."""
    return _choppiness(high, low, close, n=50).diff()

def f29_uarn_415_choppiness_short_7d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Choppiness(7) — weekly micro-regime classification (very-short-horizon hypothesis)."""
    return _choppiness(high, low, close, n=7).diff()

def f29_uarn_416_choppiness_volatility_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Std-dev of CI(14) in trailing 252d — annual regime-stability metric (high = regime-shifting year)."""
    return _choppiness(high, low, close, n=14).rolling(YDAYS, min_periods=QDAYS).std().diff()

def f29_uarn_417_choppiness_at_252d_high_event_only_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """At bars where price-high == 252d max, CI(14) > 50 indicator — ranging-regime at peak."""
    ci = _choppiness(high, low, close, n=14)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = high >= rmax
    cond = at_peak & (ci > 50.0)
    return cond.astype(float).where(at_peak & ci.notna(), np.nan).diff()

def f29_uarn_418_choppiness_rate_change_21d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21d rate-of-change of CI(14) — slower CI velocity (different horizon from existing roc_5d)."""
    ci = _choppiness(high, low, close, n=14)
    return ci.pct_change(MDAYS).diff()

def f29_uarn_419_choppiness_skew_63d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Skewness of CI(14) in trailing 63d — asymmetry in quarterly regime-distribution."""
    ci = _choppiness(high, low, close, n=14)
    return ci.rolling(QDAYS, min_periods=MDAYS).skew().diff()

def f29_uarn_420_choppiness_kurtosis_63d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Kurtosis of CI(14) in trailing 63d — fat-tailedness in quarterly regime-distribution."""
    ci = _choppiness(high, low, close, n=14)
    return ci.rolling(QDAYS, min_periods=MDAYS).kurt().diff()

def f29_uarn_421_vi_plus_falling_consecutive_streak_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current consecutive-bar streak where VI+(14) is falling — bullish-vortex decay duration."""
    vp, _ = _vortex(high, low, close, n=14)
    return _streak_true(vp.diff() < 0).diff()

def f29_uarn_422_vi_minus_rising_consecutive_streak_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current consecutive-bar streak where VI-(14) is rising — bearish-vortex acceleration duration."""
    _, vm = _vortex(high, low, close, n=14)
    return _streak_true(vm.diff() > 0).diff()

def f29_uarn_423_vortex_diff_at_63d_min_indicator_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: Vortex-diff(14) equals its 63d trailing min — quarterly bearish-extreme marker."""
    vp, vm = _vortex(high, low, close, n=14)
    d = vp - vm
    rmin = d.rolling(QDAYS, min_periods=MDAYS).min()
    cond = (d <= rmin) & d.notna()
    return cond.astype(float).where(d.notna(), np.nan).diff()

def f29_uarn_424_vortex_diff_at_63d_max_indicator_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: Vortex-diff(14) equals its 63d trailing max — quarterly bullish-extreme marker."""
    vp, vm = _vortex(high, low, close, n=14)
    d = vp - vm
    rmax = d.rolling(QDAYS, min_periods=MDAYS).max()
    cond = (d >= rmax) & d.notna()
    return cond.astype(float).where(d.notna(), np.nan).diff()

def f29_uarn_425_vortex_minus_at_252d_max_indicator_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: VI-(14) equals its 252d max — annual bear-vortex extreme."""
    _, vm = _vortex(high, low, close, n=14)
    rmax = vm.rolling(YDAYS, min_periods=QDAYS).max()
    cond = (vm >= rmax) & vm.notna()
    return cond.astype(float).where(vm.notna(), np.nan).diff()

def f29_uarn_426_vortex_plus_at_252d_min_indicator_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: VI+(14) equals its 252d min — annual bull-vortex collapse extreme."""
    vp, _ = _vortex(high, low, close, n=14)
    rmin = vp.rolling(YDAYS, min_periods=QDAYS).min()
    cond = (vp <= rmin) & vp.notna()
    return cond.astype(float).where(vp.notna(), np.nan).diff()

def f29_uarn_427_aroon_up_falling_streak_d1(high: pd.Series) -> pd.Series:
    """Current consecutive-bar streak where Aroon-Up(25) is falling — recency-of-high decay duration."""
    au = _aroon_up(high, 25)
    return _streak_true(au.diff() < 0).diff()

def f29_uarn_428_aroon_down_rising_streak_d1(low: pd.Series) -> pd.Series:
    """Current consecutive-bar streak where Aroon-Down(25) is rising — recency-of-low acceleration duration."""
    ad = _aroon_down(low, 25)
    return _streak_true(ad.diff() > 0).diff()

def f29_uarn_429_aroon_up_dwell_above_70_streak_d1(high: pd.Series) -> pd.Series:
    """Current consecutive-bar streak with Aroon-Up(25) > 70 — sustained-fresh-high regime duration."""
    au = _aroon_up(high, 25)
    return _streak_true(au > 70.0).diff()

def f29_uarn_430_aroon_down_dwell_above_70_streak_d1(low: pd.Series) -> pd.Series:
    """Current consecutive-bar streak with Aroon-Down(25) > 70 — sustained-fresh-low regime duration."""
    ad = _aroon_down(low, 25)
    return _streak_true(ad > 70.0).diff()

def f29_uarn_431_di_minus_rising_streak_alt_horizon_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current consecutive-bar streak where DI-(50) is rising — slower-horizon bear-DM accelerator."""
    _, m50, _ = _dm_components(high, low, close, n=50)
    return _streak_true(m50.diff() > 0).diff()

def f29_uarn_432_di_plus_falling_streak_alt_horizon_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current consecutive-bar streak where DI+(50) is falling — slower-horizon bull-DM decay."""
    p50, _, _ = _dm_components(high, low, close, n=50)
    return _streak_true(p50.diff() < 0).diff()

def f29_uarn_433_adx_rising_streak_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current consecutive-bar streak where ADX(14) is rising — trend-strength build-up duration."""
    _, _, adx = _dm_components(high, low, close, n=14)
    return _streak_true(adx.diff() > 0).diff()

def f29_uarn_434_adx_falling_streak_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current consecutive-bar streak where ADX(14) is falling — trend-strength erosion duration."""
    _, _, adx = _dm_components(high, low, close, n=14)
    return _streak_true(adx.diff() < 0).diff()

def f29_uarn_435_uo_below_50_streak_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current consecutive-bar streak with UO < 50 — sustained below-centerline weakness."""
    uo = _ultimate_osc(high, low, close, 7, 14, 28)
    return _streak_true(uo < 50.0).diff()

def f29_uarn_436_adx_50_percentile_rank_504d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of ADX(50) in trailing 504d — biennial slow-trend regime ranking."""
    _, _, adx50 = _dm_components(high, low, close, n=50)
    return adx50.rolling(DDAYS_2Y, min_periods=YDAYS).rank(pct=True).diff()

def f29_uarn_437_adxr_14_minus_adx_14_residual_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ADXR(14) − ADX(14): smoothed-rating early-warning residual (positive = ADXR leading down)."""
    _, _, adx = _dm_components(high, low, close, n=14)
    a = _adxr(high, low, close, n=14)
    return (a - adx).diff()

def f29_uarn_438_adx_252_percentile_rank_504d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of ADX(252) in trailing 504d — multi-year trend-strength positioning."""
    _, _, adx252 = _dm_components(high, low, close, n=252)
    return adx252.rolling(DDAYS_2Y, min_periods=YDAYS).rank(pct=True).diff()

def f29_uarn_439_adx_max_minus_adx_now_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """max(ADX(14), 252d) − ADX(14)_now: distance below annual peak — trend-strength deflation amount."""
    _, _, adx = _dm_components(high, low, close, n=14)
    return (adx.rolling(YDAYS, min_periods=QDAYS).max() - adx).diff()

def f29_uarn_440_adx_now_minus_adx_min_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ADX(14)_now − min(ADX(14), 252d): distance above annual trough — current build-up amount."""
    _, _, adx = _dm_components(high, low, close, n=14)
    return (adx - adx.rolling(YDAYS, min_periods=QDAYS).min()).diff()

def f29_uarn_441_outside_day_at_252d_high_event_d1(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Outside-day at 252d high: today high == 252d max AND H > H(prev) AND L < L(prev) — wide-range reversal day."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = high >= rmax
    outside = (high > high.shift(1)) & (low < low.shift(1))
    cond = at_peak & outside
    return cond.astype(float).where(high.notna(), np.nan).diff()

def f29_uarn_442_close_in_lower_third_at_252d_high_d1(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """At bars where high prints 252d new max, indicator that close is in lower third of today's H-L range."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = high >= rmax
    pos = _safe_div(close - low, high - low)
    cond = at_peak & (pos < 1.0 / 3.0)
    return cond.astype(float).where(at_peak, np.nan).diff()

def f29_uarn_443_gap_down_after_252d_high_d1(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Gap-down event: prior bar high == 252d max AND today open < prior bar low — exhaustion-gap signature."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    prior_at_peak = high.shift(1) >= rmax.shift(1)
    gap_down = open_ < low.shift(1)
    cond = prior_at_peak & gap_down
    return cond.astype(float).where(open_.notna(), np.nan).diff()

def f29_uarn_444_three_consecutive_lower_closes_at_252d_high_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """Three-bar lower-close sequence following a 252d high in trailing 5 bars — distribution micro-pattern."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    recent_peak = (high >= rmax).rolling(WDAYS, min_periods=2).max() > 0
    three_lower = (close < close.shift(1)) & (close.shift(1) < close.shift(2)) & (close.shift(2) < close.shift(3))
    cond = recent_peak & three_lower
    return cond.astype(float).where(close.notna(), np.nan).diff()

def f29_uarn_445_adx_above_50_dwell_21d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars in trailing 21d with ADX(14) > 50 — monthly extreme-trend dwell (parabolic-trend marker)."""
    _, _, adx = _dm_components(high, low, close, n=14)
    return (adx > 50.0).astype(float).rolling(MDAYS, min_periods=WDAYS).sum().diff()

def f29_uarn_446_adx_above_50_indicator_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: ADX(14) > 50 today — current parabolic-trend regime marker (very-extreme threshold)."""
    _, _, adx = _dm_components(high, low, close, n=14)
    return (adx > 50.0).astype(float).where(adx.notna(), np.nan).diff()

def f29_uarn_447_adxr_below_15_indicator_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: ADXR(14) < 15 today — exceptionally-weak smoothed-trend regime (full-trend-reset marker)."""
    a = _adxr(high, low, close, n=14)
    return (a < 15.0).astype(float).where(a.notna(), np.nan).diff()

def f29_uarn_448_di_plus_minus_di_minus_signed_zscore_63d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of (DI+ − DI-) in trailing 63d — quarterly directional-balance anomaly atomic."""
    p, m, _ = _dm_components(high, low, close, n=14)
    return _rolling_zscore(p - m, QDAYS, min_periods=MDAYS).diff()

def f29_uarn_449_aroon_up_minus_down_zscore_63d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of Aroon-Osc(25) in trailing 63d — quarterly recency-balance anomaly atomic."""
    osc = _aroon_up(high, 25) - _aroon_down(low, 25)
    return _rolling_zscore(osc, QDAYS, min_periods=MDAYS).diff()

def f29_uarn_450_choppiness_zscore_63d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of Choppiness(14) in trailing 63d — quarterly regime-anomaly atomic."""
    return _rolling_zscore(_choppiness(high, low, close, n=14), QDAYS, min_periods=MDAYS).diff()
ULTIMATE_AROON_VORTEX_D1_REGISTRY_376_450 = {'f29_uarn_376_true_range_percentile_rank_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_376_true_range_percentile_rank_252d_d1}, 'f29_uarn_377_high_low_range_percentile_rank_252d_d1': {'inputs': ['high', 'low'], 'func': f29_uarn_377_high_low_range_percentile_rank_252d_d1}, 'f29_uarn_378_ema9_hl_percentile_rank_252d_d1': {'inputs': ['high', 'low'], 'func': f29_uarn_378_ema9_hl_percentile_rank_252d_d1}, 'f29_uarn_379_double_ema9_hl_percentile_rank_252d_d1': {'inputs': ['high', 'low'], 'func': f29_uarn_379_double_ema9_hl_percentile_rank_252d_d1}, 'f29_uarn_380_wide_range_days_count_21d_d1': {'inputs': ['high', 'low'], 'func': f29_uarn_380_wide_range_days_count_21d_d1}, 'f29_uarn_381_mass_index_value_normalized_to_252d_range_d1': {'inputs': ['high', 'low'], 'func': f29_uarn_381_mass_index_value_normalized_to_252d_range_d1}, 'f29_uarn_382_range_expansion_ratio_smoothed_5d_median_d1': {'inputs': ['high', 'low'], 'func': f29_uarn_382_range_expansion_ratio_smoothed_5d_median_d1}, 'f29_uarn_383_atr_to_atr252_ratio_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_383_atr_to_atr252_ratio_d1}, 'f29_uarn_384_close_to_close_range_percentile_252d_d1': {'inputs': ['close'], 'func': f29_uarn_384_close_to_close_range_percentile_252d_d1}, 'f29_uarn_385_mass_index_above_25_count_21d_d1': {'inputs': ['high', 'low'], 'func': f29_uarn_385_mass_index_above_25_count_21d_d1}, 'f29_uarn_386_range_expansion_ratio_above_one_streak_d1': {'inputs': ['high', 'low'], 'func': f29_uarn_386_range_expansion_ratio_above_one_streak_d1}, 'f29_uarn_387_mass_index_minus_25_smoothed_5d_d1': {'inputs': ['high', 'low'], 'func': f29_uarn_387_mass_index_minus_25_smoothed_5d_d1}, 'f29_uarn_388_true_range_atr_ratio_21d_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_388_true_range_atr_ratio_21d_d1}, 'f29_uarn_389_high_low_range_zscore_63d_d1': {'inputs': ['high', 'low'], 'func': f29_uarn_389_high_low_range_zscore_63d_d1}, 'f29_uarn_390_mass_index_distance_above_27_clipped_d1': {'inputs': ['high', 'low'], 'func': f29_uarn_390_mass_index_distance_above_27_clipped_d1}, 'f29_uarn_391_uo_wilder_failure_swing_bearish_full_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_391_uo_wilder_failure_swing_bearish_full_d1}, 'f29_uarn_392_uo_wilder_failure_swing_bullish_full_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_392_uo_wilder_failure_swing_bullish_full_d1}, 'f29_uarn_393_dmi_bearish_failure_swing_event_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_393_dmi_bearish_failure_swing_event_d1}, 'f29_uarn_394_aroon_failure_swing_up_to_down_d1': {'inputs': ['high', 'low'], 'func': f29_uarn_394_aroon_failure_swing_up_to_down_d1}, 'f29_uarn_395_adx_hook_formation_after_50_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_395_adx_hook_formation_after_50_d1}, 'f29_uarn_396_adx_hook_formation_after_40_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_396_adx_hook_formation_after_40_d1}, 'f29_uarn_397_di_minus_above_di_plus_with_adx_falling_from_high_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_397_di_minus_above_di_plus_with_adx_falling_from_high_d1}, 'f29_uarn_398_bearish_outside_day_at_252d_high_d1': {'inputs': ['high', 'low', 'close', 'open'], 'func': f29_uarn_398_bearish_outside_day_at_252d_high_d1}, 'f29_uarn_399_close_below_open_on_new_252d_high_d1': {'inputs': ['open', 'high', 'close'], 'func': f29_uarn_399_close_below_open_on_new_252d_high_d1}, 'f29_uarn_400_lower_high_with_di_minus_rising_3d_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_400_lower_high_with_di_minus_rising_3d_d1}, 'f29_uarn_401_mass_bulge_with_close_below_open_d1': {'inputs': ['high', 'low', 'close', 'open'], 'func': f29_uarn_401_mass_bulge_with_close_below_open_d1}, 'f29_uarn_402_adx_local_peak_above_50_event_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_402_adx_local_peak_above_50_event_d1}, 'f29_uarn_403_uo_failure_swing_at_top_25d_window_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_403_uo_failure_swing_at_top_25d_window_d1}, 'f29_uarn_404_aroon_lower_high_oscillator_event_d1': {'inputs': ['high', 'low'], 'func': f29_uarn_404_aroon_lower_high_oscillator_event_d1}, 'f29_uarn_405_di_minus_higher_high_with_price_lower_high_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_405_di_minus_higher_high_with_price_lower_high_d1}, 'f29_uarn_406_choppiness_at_252d_max_indicator_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_406_choppiness_at_252d_max_indicator_d1}, 'f29_uarn_407_choppiness_at_252d_min_indicator_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_407_choppiness_at_252d_min_indicator_d1}, 'f29_uarn_408_choppiness_distance_from_252d_min_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_408_choppiness_distance_from_252d_min_d1}, 'f29_uarn_409_choppiness_distance_from_252d_max_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_409_choppiness_distance_from_252d_max_d1}, 'f29_uarn_410_choppiness_above_61_streak_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_410_choppiness_above_61_streak_d1}, 'f29_uarn_411_choppiness_below_38_streak_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_411_choppiness_below_38_streak_d1}, 'f29_uarn_412_choppiness_inside_band_streak_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_412_choppiness_inside_band_streak_d1}, 'f29_uarn_413_choppiness_rise_in_21d_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_413_choppiness_rise_in_21d_d1}, 'f29_uarn_414_choppiness_long_50d_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_414_choppiness_long_50d_d1}, 'f29_uarn_415_choppiness_short_7d_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_415_choppiness_short_7d_d1}, 'f29_uarn_416_choppiness_volatility_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_416_choppiness_volatility_252d_d1}, 'f29_uarn_417_choppiness_at_252d_high_event_only_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_417_choppiness_at_252d_high_event_only_d1}, 'f29_uarn_418_choppiness_rate_change_21d_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_418_choppiness_rate_change_21d_d1}, 'f29_uarn_419_choppiness_skew_63d_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_419_choppiness_skew_63d_d1}, 'f29_uarn_420_choppiness_kurtosis_63d_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_420_choppiness_kurtosis_63d_d1}, 'f29_uarn_421_vi_plus_falling_consecutive_streak_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_421_vi_plus_falling_consecutive_streak_d1}, 'f29_uarn_422_vi_minus_rising_consecutive_streak_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_422_vi_minus_rising_consecutive_streak_d1}, 'f29_uarn_423_vortex_diff_at_63d_min_indicator_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_423_vortex_diff_at_63d_min_indicator_d1}, 'f29_uarn_424_vortex_diff_at_63d_max_indicator_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_424_vortex_diff_at_63d_max_indicator_d1}, 'f29_uarn_425_vortex_minus_at_252d_max_indicator_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_425_vortex_minus_at_252d_max_indicator_d1}, 'f29_uarn_426_vortex_plus_at_252d_min_indicator_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_426_vortex_plus_at_252d_min_indicator_d1}, 'f29_uarn_427_aroon_up_falling_streak_d1': {'inputs': ['high'], 'func': f29_uarn_427_aroon_up_falling_streak_d1}, 'f29_uarn_428_aroon_down_rising_streak_d1': {'inputs': ['low'], 'func': f29_uarn_428_aroon_down_rising_streak_d1}, 'f29_uarn_429_aroon_up_dwell_above_70_streak_d1': {'inputs': ['high'], 'func': f29_uarn_429_aroon_up_dwell_above_70_streak_d1}, 'f29_uarn_430_aroon_down_dwell_above_70_streak_d1': {'inputs': ['low'], 'func': f29_uarn_430_aroon_down_dwell_above_70_streak_d1}, 'f29_uarn_431_di_minus_rising_streak_alt_horizon_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_431_di_minus_rising_streak_alt_horizon_d1}, 'f29_uarn_432_di_plus_falling_streak_alt_horizon_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_432_di_plus_falling_streak_alt_horizon_d1}, 'f29_uarn_433_adx_rising_streak_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_433_adx_rising_streak_d1}, 'f29_uarn_434_adx_falling_streak_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_434_adx_falling_streak_d1}, 'f29_uarn_435_uo_below_50_streak_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_435_uo_below_50_streak_d1}, 'f29_uarn_436_adx_50_percentile_rank_504d_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_436_adx_50_percentile_rank_504d_d1}, 'f29_uarn_437_adxr_14_minus_adx_14_residual_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_437_adxr_14_minus_adx_14_residual_d1}, 'f29_uarn_438_adx_252_percentile_rank_504d_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_438_adx_252_percentile_rank_504d_d1}, 'f29_uarn_439_adx_max_minus_adx_now_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_439_adx_max_minus_adx_now_252d_d1}, 'f29_uarn_440_adx_now_minus_adx_min_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_440_adx_now_minus_adx_min_252d_d1}, 'f29_uarn_441_outside_day_at_252d_high_event_d1': {'inputs': ['open', 'high', 'low', 'close'], 'func': f29_uarn_441_outside_day_at_252d_high_event_d1}, 'f29_uarn_442_close_in_lower_third_at_252d_high_d1': {'inputs': ['open', 'high', 'low', 'close'], 'func': f29_uarn_442_close_in_lower_third_at_252d_high_d1}, 'f29_uarn_443_gap_down_after_252d_high_d1': {'inputs': ['open', 'high', 'low', 'close'], 'func': f29_uarn_443_gap_down_after_252d_high_d1}, 'f29_uarn_444_three_consecutive_lower_closes_at_252d_high_d1': {'inputs': ['high', 'close'], 'func': f29_uarn_444_three_consecutive_lower_closes_at_252d_high_d1}, 'f29_uarn_445_adx_above_50_dwell_21d_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_445_adx_above_50_dwell_21d_d1}, 'f29_uarn_446_adx_above_50_indicator_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_446_adx_above_50_indicator_d1}, 'f29_uarn_447_adxr_below_15_indicator_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_447_adxr_below_15_indicator_d1}, 'f29_uarn_448_di_plus_minus_di_minus_signed_zscore_63d_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_448_di_plus_minus_di_minus_signed_zscore_63d_d1}, 'f29_uarn_449_aroon_up_minus_down_zscore_63d_d1': {'inputs': ['high', 'low'], 'func': f29_uarn_449_aroon_up_minus_down_zscore_63d_d1}, 'f29_uarn_450_choppiness_zscore_63d_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_450_choppiness_zscore_63d_d1}}