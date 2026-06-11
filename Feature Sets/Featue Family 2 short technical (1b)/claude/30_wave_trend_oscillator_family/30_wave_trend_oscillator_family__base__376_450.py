"""wave_trend_oscillator_family base features 376-450 — Pipeline 1b-technical.

Third batch (continued). Atomic-leaning. Focus areas in this file:

  - WTO atomic events: WT1 252d max/min event, WT2 252d max event, WT1-WT2
    gap extremes (max gap event, narrowing event), days-since-extreme
    overbought / oversold, oscillation zero-cross count, amplitude trailing
    63d, swing-count above 60 in 252d, streak above 60 / below -60 max in
    252d, bearish/bullish cross strictly inside OB/OS zones, distance from
    252d max normalized, lower-high event, WT2 dwell, velocity-extreme,
    regime-swing within 21d, decline-from-above-80 in 5d pct.

  - TTM Squeeze + momentum atomic events: max in-squeeze run 252d,
    failed-release (no 21d-new-high in 5 bars), squeeze re-enters after
    release within 5, fire-bull-then-sign-flip-within-5, fire-bear mirror,
    momentum velocity 5d, momentum local-max-then-falling, momentum zero-
    cross count 63d, momentum above/below zero streak max 252d.

  - SqueezePro tier-progression atomic events: release-from-low / mid,
    low-to-high progression, high-release-failed-within-5, bars-since-high-
    release.

  - Canonical composites (~15% of file): Bollinger stack-and-rip,
    Bollinger head-fake (up/down), Linda Raschke 80-20 (bull/bear), Turtle
    Soup (long/short), Crabel ORB proxy, %b-decay band-walk, WT1-decay
    new-high.

  - Additional BB/bandwidth atomic gaps: vol-cone position 252d, compression-
    then-expansion within 21d, bandwidth decline/expansion streak, BW local
    min/max event, KC/BB ratio, BB upper/lower first-touch after 21d-inside,
    super-short 5d squeeze on/release, walking-upper-then-walking-lower
    regime flip, 3-day-avg %b extremes, %b above/below extreme streak,
    BB at-band count 252d, BB walking-upper streak at 252d max event,
    BB width <5% event, donchian-position top-decile dwell, TTM momentum
    amplitude, TTM squeeze density ratio, WT1 vol-of-vol, WT1 correlation-
    with-close 63d.

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


def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=max(n // 3, 2)).mean()


# ---------------------------- indicator primitives ----------------------------

def _bb(close, n=20, mult=2.0):
    mp = max(n // 3, 2)
    mid = close.rolling(n, min_periods=mp).mean()
    sd = close.rolling(n, min_periods=mp).std()
    return mid, mid + mult * sd, mid - mult * sd


def _kc(high, low, close, n=20, mult=1.5):
    mp = max(n // 3, 2)
    mid = close.rolling(n, min_periods=mp).mean()
    tr = _true_range(high, low, close)
    rng = tr.rolling(n, min_periods=mp).mean()
    return mid, mid + mult * rng, mid - mult * rng


def _pct_b(close, n=20, mult=2.0):
    _, bbu, bbl = _bb(close, n=n, mult=mult)
    return _safe_div(close - bbl, bbu - bbl)


def _bb_width_pct(close, n=20, mult=2.0):
    mid, bbu, bbl = _bb(close, n=n, mult=mult)
    return _safe_div(bbu - bbl, mid)


def _wto_default(high, low, close, n1=10, n2=21):
    ap = (high + low + close) / 3.0
    esa = _ema(ap, n1)
    d = _ema((ap - esa).abs(), n1)
    ci = _safe_div(ap - esa, 0.015 * d)
    tci = _ema(ci, n2)
    wt2 = tci.rolling(4, min_periods=2).mean()
    return tci, wt2


def _ttm_squeeze_on(high, low, close, n=20, mult_bb=2.0, mult_kc=1.5):
    _, bbu, bbl = _bb(close, n=n, mult=mult_bb)
    _, kcu, kcl = _kc(high, low, close, n=n, mult=mult_kc)
    on = (bbu < kcu) & (bbl > kcl)
    return on.astype(float).where(bbu.notna() & kcu.notna(), np.nan)


def _donchian_upper_helper(high, n):
    return high.rolling(n, min_periods=max(n // 3, 2)).max()


def _donchian_lower_helper(low, n):
    return low.rolling(n, min_periods=max(n // 3, 2)).min()


def _ttm_momentum(high, low, close, n=20):
    hh = high.rolling(n, min_periods=max(n // 3, 2)).max()
    ll = low.rolling(n, min_periods=max(n // 3, 2)).min()
    sma_c = close.rolling(n, min_periods=max(n // 3, 2)).mean()
    val = close - 0.5 * ((hh + ll) / 2.0 + sma_c)
    def _lr_end(w):
        valid = ~np.isnan(w)
        m = max(n // 3, 2)
        if valid.sum() < m:
            return np.nan
        x = np.arange(len(w), dtype=float)
        if valid.all():
            wv = w
        else:
            x = x[valid]
            wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        sx = ((x - xm) ** 2).sum()
        if sx == 0:
            return np.nan
        b = ((x - xm) * (wv - wm)).sum() / sx
        a = wm - b * xm
        return a + b * (len(w) - 1)
    return val.rolling(n, min_periods=max(n // 3, 2)).apply(_lr_end, raw=True)


def _consec_true_streak(b):
    """Right-anchored current consecutive True-streak length (0 where False)."""
    b = b.fillna(False).astype(bool)
    idx = np.arange(len(b), dtype=float)
    last_false = pd.Series(np.where(~b, idx, np.nan), index=b.index).ffill()
    streak = pd.Series(idx, index=b.index) - last_false
    streak = streak.where(b, 0.0)
    streak.iloc[0] = float(b.iloc[0]) if len(b) > 0 else np.nan
    return streak


def _bars_since_true(b):
    """Bars since last True (NaN until first True)."""
    b = b.fillna(False).astype(bool)
    idx = np.arange(len(b), dtype=float)
    last_true = pd.Series(np.where(b, idx, np.nan), index=b.index).ffill()
    return pd.Series(idx, index=b.index) - last_true


# ============================================================
# Bucket K — WTO atomic events (376-395)
# ============================================================

def f30_wtof_376_wto_wt1_252d_max_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: WT1 equals its trailing 252d max — extreme cycle-peak bar."""
    wt1, _ = _wto_default(high, low, close, 10, 21)
    rmax = wt1.rolling(YDAYS, min_periods=QDAYS).max()
    return (wt1 >= rmax).astype(float).where(rmax.notna(), np.nan)


def f30_wtof_377_wto_wt1_252d_min_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: WT1 equals its trailing 252d min — extreme cycle-trough bar."""
    wt1, _ = _wto_default(high, low, close, 10, 21)
    rmin = wt1.rolling(YDAYS, min_periods=QDAYS).min()
    return (wt1 <= rmin).astype(float).where(rmin.notna(), np.nan)


def f30_wtof_378_wto_wt2_252d_max_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: WT2 (signal line) equals its trailing 252d max."""
    _, wt2 = _wto_default(high, low, close, 10, 21)
    rmax = wt2.rolling(YDAYS, min_periods=QDAYS).max()
    return (wt2 >= rmax).astype(float).where(rmax.notna(), np.nan)


def f30_wtof_379_wto_gap_wt1_minus_wt2_252d_max_gap_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: |WT1-WT2| equals its 252d trailing max — widest divergence between fast/slow."""
    wt1, wt2 = _wto_default(high, low, close, 10, 21)
    gap = (wt1 - wt2).abs()
    rmax = gap.rolling(YDAYS, min_periods=QDAYS).max()
    return (gap >= rmax).astype(float).where(rmax.notna(), np.nan)


def f30_wtof_380_wto_gap_wt1_minus_wt2_narrowing_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: |WT1-WT2| was wide (>21d-mean*1.5) yesterday AND is below 21d-mean today — convergence bar."""
    wt1, wt2 = _wto_default(high, low, close, 10, 21)
    gap = (wt1 - wt2).abs()
    m = gap.rolling(MDAYS, min_periods=WDAYS).mean()
    cond = (gap.shift(1) > 1.5 * m.shift(1)) & (gap < m)
    return cond.astype(float).where(m.notna(), np.nan)


def f30_wtof_381_wto_wt1_days_since_extreme_overbought_above_80(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since WT1 was last > 80 (extreme overbought) — cycle-stretch memory."""
    wt1, _ = _wto_default(high, low, close, 10, 21)
    return _bars_since_true(wt1 > 80.0)


def f30_wtof_382_wto_wt1_days_since_extreme_oversold_below_minus80(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since WT1 was last < -80 (extreme oversold) — capitulation-distance memory."""
    wt1, _ = _wto_default(high, low, close, 10, 21)
    return _bars_since_true(wt1 < -80.0)


def f30_wtof_383_wto_wt1_oscillation_zero_cross_count_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of WT1 zero-line crossings (sign changes) in trailing 63d."""
    wt1, _ = _wto_default(high, low, close, 10, 21)
    sign = np.sign(wt1)
    cross = (sign != sign.shift(1)) & sign.notna() & sign.shift(1).notna()
    return cross.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f30_wtof_384_wto_wt1_amplitude_max_minus_min_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Trailing 63d (WT1 max - WT1 min) — amplitude of cycle."""
    wt1, _ = _wto_default(high, low, close, 10, 21)
    rmax = wt1.rolling(QDAYS, min_periods=MDAYS).max()
    rmin = wt1.rolling(QDAYS, min_periods=MDAYS).min()
    return rmax - rmin


def f30_wtof_385_wto_wt1_above_60_count_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars with WT1 > 60 (overbought) in trailing 252d — secular overbought frequency."""
    wt1, _ = _wto_default(high, low, close, 10, 21)
    b = (wt1 > 60.0).astype(float).where(wt1.notna(), np.nan)
    return b.rolling(YDAYS, min_periods=QDAYS).sum()


def f30_wtof_386_wto_wt1_streak_above_60_max_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Max consecutive WT1>60 streak length in trailing 252d."""
    wt1, _ = _wto_default(high, low, close, 10, 21)
    streak = _consec_true_streak(wt1 > 60.0)
    return streak.rolling(YDAYS, min_periods=QDAYS).max()


def f30_wtof_387_wto_wt1_streak_below_minus60_max_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Max consecutive WT1<-60 streak length in trailing 252d."""
    wt1, _ = _wto_default(high, low, close, 10, 21)
    streak = _consec_true_streak(wt1 < -60.0)
    return streak.rolling(YDAYS, min_periods=QDAYS).max()


def f30_wtof_388_wto_wt1_bearish_cross_strict_in_ob_zone_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: bearish cross (WT1<WT2 today, WT1>=WT2 yesterday) AND both WT1 and WT2 > 60 — strict-OB cross."""
    wt1, wt2 = _wto_default(high, low, close, 10, 21)
    cross = (wt1 < wt2) & (wt1.shift(1) >= wt2.shift(1))
    cond = cross & (wt1 > 60.0) & (wt2 > 60.0)
    return cond.astype(float).where(wt1.notna() & wt2.notna(), np.nan)


def f30_wtof_389_wto_wt1_bullish_cross_strict_in_os_zone_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: bullish cross AND both WT1 and WT2 < -60 — strict-OS cross."""
    wt1, wt2 = _wto_default(high, low, close, 10, 21)
    cross = (wt1 > wt2) & (wt1.shift(1) <= wt2.shift(1))
    cond = cross & (wt1 < -60.0) & (wt2 < -60.0)
    return cond.astype(float).where(wt1.notna() & wt2.notna(), np.nan)


def f30_wtof_390_wto_wt1_distance_from_252d_max_normalized(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(WT1 - WT1_252d_max) / amplitude_252d — distance below cycle peak normalized by range."""
    wt1, _ = _wto_default(high, low, close, 10, 21)
    rmax = wt1.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = wt1.rolling(YDAYS, min_periods=QDAYS).min()
    return _safe_div(wt1 - rmax, rmax - rmin)


def f30_wtof_391_wto_wt1_lower_high_event_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: WT1 21d-trailing-max is lower than WT1 21d-trailing-max one bar ago (lower-high in oscillator)."""
    wt1, _ = _wto_default(high, low, close, 10, 21)
    rmax = wt1.rolling(MDAYS, min_periods=WDAYS).max()
    cond = (rmax < rmax.shift(1)) & rmax.notna() & rmax.shift(1).notna()
    return cond.astype(float).where(wt1.notna(), np.nan)


def f30_wtof_392_wto_wt2_above_zero_dwell_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars with WT2 > 0 in trailing 21d — slow-line bullish dwell."""
    _, wt2 = _wto_default(high, low, close, 10, 21)
    b = (wt2 > 0.0).astype(float).where(wt2.notna(), np.nan)
    return b.rolling(MDAYS, min_periods=WDAYS).sum()


def f30_wtof_393_wto_wt1_velocity_252d_max_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: |WT1.diff(1)| equals its 252d trailing max — peak-velocity bar."""
    wt1, _ = _wto_default(high, low, close, 10, 21)
    v = wt1.diff().abs()
    rmax = v.rolling(YDAYS, min_periods=QDAYS).max()
    return (v >= rmax).astype(float).where(rmax.notna(), np.nan)


def f30_wtof_394_wto_wt1_regime_swing_within_21d_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: WT1 > 60 today AND WT1 < -60 within trailing 21d — extreme regime swing."""
    wt1, _ = _wto_default(high, low, close, 10, 21)
    os_recent = (wt1.shift(1) < -60.0).rolling(MDAYS, min_periods=1).max().astype(bool)
    cond = (wt1 > 60.0) & os_recent
    return cond.astype(float).where(wt1.notna(), np.nan)


def f30_wtof_395_wto_wt1_decline_from_above_80_pct_in_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Pct decline of WT1 over trailing 5 bars when starting from WT1>80, else NaN — sharpness of cycle drop."""
    wt1, _ = _wto_default(high, low, close, 10, 21)
    prev = wt1.shift(WDAYS)
    cond = prev > 80.0
    pct = _safe_div(wt1 - prev, prev.abs())
    return pct.where(cond, np.nan)


# ============================================================
# Bucket L — TTM Squeeze atomic events (396-405)
# ============================================================

def f30_wtof_396_ttm_squeeze_max_in_squeeze_run_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Max consecutive TTM-squeeze-on run length in trailing 252d."""
    on = _ttm_squeeze_on(high, low, close, n=MDAYS, mult_bb=2.0, mult_kc=1.5)
    streak = _consec_true_streak(on == 1)
    return streak.rolling(YDAYS, min_periods=QDAYS).max()


def f30_wtof_397_ttm_squeeze_release_no_21d_high_within_5_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: TTM squeeze fired within trailing 5 bars AND high has NOT printed a 21d-new-high since fire — failed breakout."""
    on = _ttm_squeeze_on(high, low, close, n=MDAYS, mult_bb=2.0, mult_kc=1.5)
    fired = (on.shift(1) == 1) & (on == 0)
    fired_recent = fired.fillna(False).astype(bool).rolling(WDAYS, min_periods=1).max().astype(bool)
    h21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    no_new_high = (high < h21.shift(1))
    cond = fired_recent & no_new_high & (~fired.fillna(False).astype(bool))
    return cond.astype(float).where(on.notna() & h21.notna(), np.nan)


def f30_wtof_398_ttm_squeeze_release_then_back_in_squeeze_within_5_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: TTM squeeze fired within trailing 5 bars AND squeeze is back on today — failed-release re-compression."""
    on = _ttm_squeeze_on(high, low, close, n=MDAYS, mult_bb=2.0, mult_kc=1.5)
    fired = (on.shift(1) == 1) & (on == 0)
    fired_recent = fired.fillna(False).astype(bool).rolling(WDAYS, min_periods=1).max().astype(bool)
    cond = fired_recent & (on == 1) & (~fired.fillna(False).astype(bool))
    return cond.astype(float).where(on.notna(), np.nan)


def f30_wtof_399_ttm_fired_bull_then_sign_flip_within_5_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: TTM fire happened with positive momentum within trailing 5 bars AND momentum is negative today."""
    on = _ttm_squeeze_on(high, low, close, n=MDAYS, mult_bb=2.0, mult_kc=1.5)
    mom = _ttm_momentum(high, low, close, n=MDAYS)
    fired = (on.shift(1) == 1) & (on == 0)
    fired_bull = fired & (mom > 0)
    fired_bull_recent = fired_bull.fillna(False).astype(bool).rolling(WDAYS, min_periods=1).max().astype(bool)
    cond = fired_bull_recent & (mom < 0)
    return cond.astype(float).where(on.notna() & mom.notna(), np.nan)


def f30_wtof_400_ttm_fired_bear_then_sign_flip_within_5_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: TTM fire happened with negative momentum within trailing 5 bars AND momentum is positive today."""
    on = _ttm_squeeze_on(high, low, close, n=MDAYS, mult_bb=2.0, mult_kc=1.5)
    mom = _ttm_momentum(high, low, close, n=MDAYS)
    fired = (on.shift(1) == 1) & (on == 0)
    fired_bear = fired & (mom < 0)
    fired_bear_recent = fired_bear.fillna(False).astype(bool).rolling(WDAYS, min_periods=1).max().astype(bool)
    cond = fired_bear_recent & (mom > 0)
    return cond.astype(float).where(on.notna() & mom.notna(), np.nan)


def f30_wtof_401_ttm_momentum_velocity_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Trailing 5d slope of TTM-momentum histogram — momentum-of-momentum."""
    mom = _ttm_momentum(high, low, close, n=MDAYS)
    return _rolling_slope(mom, WDAYS)


def f30_wtof_402_ttm_momentum_local_max_then_falling_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: TTM momentum was its 21d max yesterday AND is lower today — local-peak rollover."""
    mom = _ttm_momentum(high, low, close, n=MDAYS)
    rmax_y = mom.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    was_max = mom.shift(1) >= rmax_y
    cond = was_max & (mom < mom.shift(1))
    return cond.astype(float).where(mom.notna(), np.nan)


def f30_wtof_403_ttm_momentum_zero_cross_count_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of TTM momentum zero-line crossings in trailing 63d."""
    mom = _ttm_momentum(high, low, close, n=MDAYS)
    sign = np.sign(mom)
    cross = (sign != sign.shift(1)) & sign.notna() & sign.shift(1).notna()
    return cross.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f30_wtof_404_ttm_momentum_above_zero_streak_max_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Max consecutive TTM momentum >0 streak length in trailing 252d."""
    mom = _ttm_momentum(high, low, close, n=MDAYS)
    streak = _consec_true_streak(mom > 0)
    return streak.rolling(YDAYS, min_periods=QDAYS).max()


def f30_wtof_405_ttm_momentum_below_zero_streak_max_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Max consecutive TTM momentum <0 streak length in trailing 252d."""
    mom = _ttm_momentum(high, low, close, n=MDAYS)
    streak = _consec_true_streak(mom < 0)
    return streak.rolling(YDAYS, min_periods=QDAYS).max()


# ============================================================
# Bucket M — SqueezePro tier-progression atomic events (406-410)
# ============================================================

def f30_wtof_406_squeeze_pro_release_from_low_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: SqueezePro low-compression (mult_kc=2.0) fired today (was on, now off)."""
    low_on = _ttm_squeeze_on(high, low, close, n=MDAYS, mult_bb=2.0, mult_kc=2.0)
    fired = (low_on.shift(1) == 1) & (low_on == 0)
    return fired.astype(float).where(low_on.notna(), np.nan)


def f30_wtof_407_squeeze_pro_release_from_mid_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: SqueezePro mid-compression (mult_kc=1.5) fired today (was on, now off)."""
    mid_on = _ttm_squeeze_on(high, low, close, n=MDAYS, mult_bb=2.0, mult_kc=1.5)
    fired = (mid_on.shift(1) == 1) & (mid_on == 0)
    return fired.astype(float).where(mid_on.notna(), np.nan)


def f30_wtof_408_squeeze_pro_low_to_high_progression_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: SqueezePro tightened today — was low-compression yesterday AND is high-compression (mult_kc=1.0) today."""
    low_on = _ttm_squeeze_on(high, low, close, n=MDAYS, mult_bb=2.0, mult_kc=2.0)
    hi_on = _ttm_squeeze_on(high, low, close, n=MDAYS, mult_bb=2.0, mult_kc=1.0)
    cond = (low_on.shift(1) == 1) & (hi_on == 1) & (hi_on.shift(1) == 0)
    return cond.astype(float).where(low_on.notna() & hi_on.notna(), np.nan)


def f30_wtof_409_squeeze_pro_high_release_failed_within_5_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: SqueezePro high-compression (mult_kc=1.0) fired within trailing 5 bars AND high has NOT printed a 21d-new-high since."""
    hi_on = _ttm_squeeze_on(high, low, close, n=MDAYS, mult_bb=2.0, mult_kc=1.0)
    fired = (hi_on.shift(1) == 1) & (hi_on == 0)
    fired_recent = fired.fillna(False).astype(bool).rolling(WDAYS, min_periods=1).max().astype(bool)
    h21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    no_new_high = high < h21.shift(1)
    cond = fired_recent & no_new_high & (~fired.fillna(False).astype(bool))
    return cond.astype(float).where(hi_on.notna() & h21.notna(), np.nan)


def f30_wtof_410_squeeze_pro_bars_since_high_release(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since last SqueezePro high-compression release (NaN until first fire)."""
    hi_on = _ttm_squeeze_on(high, low, close, n=MDAYS, mult_bb=2.0, mult_kc=1.0)
    fired = (hi_on.shift(1) == 1) & (hi_on == 0)
    return _bars_since_true(fired)


# ============================================================
# Bucket N — Canonical composites (~15%) (411-420)
# ============================================================

def f30_wtof_411_bollinger_stack_and_rip_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Canonical Carter 'stack-and-rip': TTM squeeze-on yesterday AND fired today AND TTM momentum>0 today."""
    on = _ttm_squeeze_on(high, low, close, n=MDAYS, mult_bb=2.0, mult_kc=1.5)
    mom = _ttm_momentum(high, low, close, n=MDAYS)
    cond = (on.shift(1) == 1) & (on == 0) & (mom > 0)
    return cond.astype(float).where(on.notna() & mom.notna(), np.nan)


def f30_wtof_412_bollinger_head_fake_up_event(close: pd.Series) -> pd.Series:
    """Canonical Bollinger head-fake (up): %b>1 yesterday AND close<SMA20 today — fake breakout collapse."""
    pb = _pct_b(close, n=MDAYS, mult=2.0)
    mid, _, _ = _bb(close, n=MDAYS, mult=2.0)
    cond = (pb.shift(1) > 1.0) & (close < mid)
    return cond.astype(float).where(pb.notna() & mid.notna(), np.nan)


def f30_wtof_413_bollinger_head_fake_down_event(close: pd.Series) -> pd.Series:
    """Canonical Bollinger head-fake (down): %b<0 yesterday AND close>SMA20 today — fake breakdown reversal."""
    pb = _pct_b(close, n=MDAYS, mult=2.0)
    mid, _, _ = _bb(close, n=MDAYS, mult=2.0)
    cond = (pb.shift(1) < 0.0) & (close > mid)
    return cond.astype(float).where(pb.notna() & mid.notna(), np.nan)


def f30_wtof_414_raschke_80_20_bullish_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Canonical Linda Raschke 80-20 (bull): close in top 20% of bar range AND close > prior close — continuation/reversal proxy."""
    rng = high - low
    pos = _safe_div(close - low, rng)
    cond = (pos >= 0.8) & (close > close.shift(1))
    return cond.astype(float).where(rng.notna() & (rng > 0), np.nan)


def f30_wtof_415_raschke_80_20_bearish_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Canonical Linda Raschke 80-20 (bear): close in bottom 20% of bar range AND close < prior close."""
    rng = high - low
    pos = _safe_div(close - low, rng)
    cond = (pos <= 0.2) & (close < close.shift(1))
    return cond.astype(float).where(rng.notna() & (rng > 0), np.nan)


def f30_wtof_416_turtle_soup_long_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Canonical Connors/Raschke 'Turtle Soup' (long): today's low broke a 20d-new-low (low < 20d-prior-min) BUT close > 20d-prior-min — false breakdown reversal."""
    l20_prev = low.shift(1).rolling(20, min_periods=10).min()
    cond = (low < l20_prev) & (close > l20_prev)
    return cond.astype(float).where(l20_prev.notna(), np.nan)


def f30_wtof_417_turtle_soup_short_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Canonical 'Turtle Soup' (short): today's high broke a 20d-new-high BUT close < 20d-prior-max — false breakout reversal."""
    h20_prev = high.shift(1).rolling(20, min_periods=10).max()
    cond = (high > h20_prev) & (close < h20_prev)
    return cond.astype(float).where(h20_prev.notna(), np.nan)


def f30_wtof_418_crabel_orb_proxy_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Crabel ORB proxy (daily): close > prior 5d-high AND prior bar was an NR4 — compression-then-breakout."""
    rng = high - low
    rmin = rng.rolling(4, min_periods=4).min()
    is_nr4 = (rng <= rmin)
    h5_prev = high.shift(1).rolling(WDAYS, min_periods=2).max()
    cond = (close > h5_prev) & is_nr4.shift(1).fillna(False).astype(bool)
    return cond.astype(float).where(h5_prev.notna() & rmin.notna(), np.nan)


def f30_wtof_419_pct_b_decay_in_band_walk_event(high: pd.Series, close: pd.Series) -> pd.Series:
    """Event: today high is a 21d-new-high BUT %b is lower than %b at the prior 21d-high — penetration-depth fading."""
    pb = _pct_b(close, n=MDAYS, mult=2.0)
    h21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    is_new_high = high >= h21
    pb_at_high = pb.where(is_new_high).ffill()
    prev_pb_at_high = pb_at_high.shift(1)
    cond = is_new_high & (pb < prev_pb_at_high)
    return cond.astype(float).where(pb.notna() & h21.notna(), np.nan)


def f30_wtof_420_wto_wt1_decay_at_new_high_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: today high is a 21d-new-high BUT WT1 is lower than WT1 at the prior 21d-high — momentum divergence."""
    wt1, _ = _wto_default(high, low, close, 10, 21)
    h21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    is_new_high = high >= h21
    wt1_at_high = wt1.where(is_new_high).ffill()
    prev_wt1_at_high = wt1_at_high.shift(1)
    cond = is_new_high & (wt1 < prev_wt1_at_high)
    return cond.astype(float).where(wt1.notna() & h21.notna(), np.nan)


# ============================================================
# Bucket O — Additional BB / bandwidth / WTO atomic gaps (421-450)
# ============================================================

def f30_wtof_421_bb_width_vol_cone_position_252d(close: pd.Series) -> pd.Series:
    """BB-width percentile vs trailing 252d (vol-cone position 0..1)."""
    bw = _bb_width_pct(close, n=MDAYS, mult=2.0)
    return bw.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)


def f30_wtof_422_bandwidth_compression_then_expansion_event_21d(close: pd.Series) -> pd.Series:
    """Event: bandwidth percentile was <0.25 within trailing 21d AND bandwidth percentile is >0.75 today — compression→expansion flip."""
    bw = _bb_width_pct(close, n=MDAYS, mult=2.0)
    rank = bw.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    low_recent = (rank.shift(1) < 0.25).rolling(MDAYS, min_periods=1).max().astype(bool)
    cond = low_recent & (rank > 0.75)
    return cond.astype(float).where(rank.notna(), np.nan)


def f30_wtof_423_bandwidth_decline_streak_consecutive(close: pd.Series) -> pd.Series:
    """Current consecutive streak of bandwidth.diff()<0 — sustained vol-compression."""
    bw = _bb_width_pct(close, n=MDAYS, mult=2.0)
    return _consec_true_streak(bw.diff() < 0)


def f30_wtof_424_bandwidth_expansion_streak_consecutive(close: pd.Series) -> pd.Series:
    """Current consecutive streak of bandwidth.diff()>0 — sustained vol-expansion."""
    bw = _bb_width_pct(close, n=MDAYS, mult=2.0)
    return _consec_true_streak(bw.diff() > 0)


def f30_wtof_425_bb_width_local_max_event(close: pd.Series) -> pd.Series:
    """Event: BB-width is a 3-bar local max (BW[t-1]<BW[t]>BW[t+0+1] not allowed — PIT, so use t-1<t today AND t-2<t-1)."""
    bw = _bb_width_pct(close, n=MDAYS, mult=2.0)
    cond = (bw.shift(1) > bw) & (bw.shift(2) < bw.shift(1))
    return cond.astype(float).where(bw.notna(), np.nan)


def f30_wtof_426_bb_width_local_min_event(close: pd.Series) -> pd.Series:
    """Event: BB-width is a 3-bar local min (PIT-clean: yesterday was lower than day-before AND today is higher than yesterday)."""
    bw = _bb_width_pct(close, n=MDAYS, mult=2.0)
    cond = (bw.shift(1) < bw) & (bw.shift(2) > bw.shift(1))
    return cond.astype(float).where(bw.notna(), np.nan)


def f30_wtof_427_donchian_compressed_then_breakout_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: 20d-Donchian width was at its 63d-min within trailing 10 bars AND close > prior 20d-Donchian upper today."""
    u20 = _donchian_upper_helper(high, 20)
    l20 = _donchian_lower_helper(low, 20)
    w = u20 - l20
    rmin = w.rolling(QDAYS, min_periods=MDAYS).min()
    was_min = (w.shift(1) <= rmin.shift(1)).rolling(10, min_periods=1).max().astype(bool)
    bo = close > u20.shift(1)
    cond = was_min & bo
    return cond.astype(float).where(rmin.notna(), np.nan)


def f30_wtof_428_kc_width_to_bb_width_ratio(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """KC width / BB width — when <1 means BB outside KC (release regime). Continuous KC/BB ratio."""
    _, bbu, bbl = _bb(close, n=MDAYS, mult=2.0)
    _, kcu, kcl = _kc(high, low, close, n=MDAYS, mult=1.5)
    return _safe_div(kcu - kcl, bbu - bbl)


def f30_wtof_429_kc_width_minus_bb_width_atr_norm(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(KC-width - BB-width) in ATR units — positive = squeeze regime, negative = release regime."""
    _, bbu, bbl = _bb(close, n=MDAYS, mult=2.0)
    _, kcu, kcl = _kc(high, low, close, n=MDAYS, mult=1.5)
    a = _atr(high, low, close, n=MDAYS)
    return _safe_div((kcu - kcl) - (bbu - bbl), a)


def f30_wtof_430_pct_b_acceleration_5d(close: pd.Series) -> pd.Series:
    """Second difference of raw %b over 5-bar gap — short-horizon %b acceleration."""
    pb = _pct_b(close, n=MDAYS, mult=2.0)
    return pb.diff(WDAYS).diff(WDAYS)


def f30_wtof_431_pct_b_above_eighty_count_252d(close: pd.Series) -> pd.Series:
    """Count of bars with %b > 0.8 in trailing 252d (long-run upper-band dwell)."""
    pb = _pct_b(close, n=MDAYS, mult=2.0)
    b = (pb > 0.8).astype(float).where(pb.notna(), np.nan)
    return b.rolling(YDAYS, min_periods=QDAYS).sum()


def f30_wtof_432_pct_b_below_twenty_count_252d(close: pd.Series) -> pd.Series:
    """Count of bars with %b < 0.2 in trailing 252d (long-run lower-band dwell)."""
    pb = _pct_b(close, n=MDAYS, mult=2.0)
    b = (pb < 0.2).astype(float).where(pb.notna(), np.nan)
    return b.rolling(YDAYS, min_periods=QDAYS).sum()


def f30_wtof_433_bb_upper_first_touch_after_21d_inside_event(close: pd.Series) -> pd.Series:
    """Event: close >= BB-upper today AND close was strictly inside bands for prior 21+ bars — first upper-touch after compression."""
    _, bbu, bbl = _bb(close, n=MDAYS, mult=2.0)
    inside = (close > bbl) & (close < bbu)
    inside_streak = _consec_true_streak(inside)
    cond = (close >= bbu) & (inside_streak.shift(1) >= MDAYS)
    return cond.astype(float).where(bbu.notna(), np.nan)


def f30_wtof_434_bb_lower_first_touch_after_21d_inside_event(close: pd.Series) -> pd.Series:
    """Event: close <= BB-lower today AND close was strictly inside bands for prior 21+ bars — first lower-touch after compression."""
    _, bbu, bbl = _bb(close, n=MDAYS, mult=2.0)
    inside = (close > bbl) & (close < bbu)
    inside_streak = _consec_true_streak(inside)
    cond = (close <= bbl) & (inside_streak.shift(1) >= MDAYS)
    return cond.astype(float).where(bbl.notna(), np.nan)


def f30_wtof_435_bollinger_squeeze_short_term_5d_on(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: TTM squeeze ON at very-short horizon n=5 — ultra-short compression."""
    on = _ttm_squeeze_on(high, low, close, n=WDAYS, mult_bb=2.0, mult_kc=1.5)
    return on


def f30_wtof_436_bollinger_squeeze_super_short_5d_release_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: TTM squeeze (n=5) fired today (was on, now off)."""
    on = _ttm_squeeze_on(high, low, close, n=WDAYS, mult_bb=2.0, mult_kc=1.5)
    fired = (on.shift(1) == 1) & (on == 0)
    return fired.astype(float).where(on.notna(), np.nan)


def f30_wtof_437_walking_upper_then_walking_lower_within_21d_event(close: pd.Series) -> pd.Series:
    """Event: close < BB-lower today AND close > BB-upper occurred within trailing 21 bars — regime flip from walk-up to walk-down."""
    _, bbu, bbl = _bb(close, n=MDAYS, mult=2.0)
    up = (close > bbu)
    up_recent = up.shift(1).fillna(False).astype(bool).rolling(MDAYS, min_periods=1).max().astype(bool)
    cond = up_recent & (close < bbl)
    return cond.astype(float).where(bbu.notna() & bbl.notna(), np.nan)


def f30_wtof_438_pct_b_3day_avg_below_zero_event(close: pd.Series) -> pd.Series:
    """Event: 3-day rolling mean of %b < 0 — persistent below-lower-band penetration."""
    pb = _pct_b(close, n=MDAYS, mult=2.0)
    m3 = pb.rolling(3, min_periods=2).mean()
    return (m3 < 0).astype(float).where(m3.notna(), np.nan)


def f30_wtof_439_pct_b_3day_avg_above_one_event(close: pd.Series) -> pd.Series:
    """Event: 3-day rolling mean of %b > 1 — persistent above-upper-band penetration."""
    pb = _pct_b(close, n=MDAYS, mult=2.0)
    m3 = pb.rolling(3, min_periods=2).mean()
    return (m3 > 1).astype(float).where(m3.notna(), np.nan)


def f30_wtof_440_pct_b_above_1_consecutive_streak(close: pd.Series) -> pd.Series:
    """Current consecutive streak of %b > 1.0 bars."""
    pb = _pct_b(close, n=MDAYS, mult=2.0)
    return _consec_true_streak(pb > 1.0)


def f30_wtof_441_pct_b_below_0_consecutive_streak(close: pd.Series) -> pd.Series:
    """Current consecutive streak of %b < 0.0 bars."""
    pb = _pct_b(close, n=MDAYS, mult=2.0)
    return _consec_true_streak(pb < 0.0)


def f30_wtof_442_bb_close_at_upper_band_count_252d(close: pd.Series) -> pd.Series:
    """Count of bars with close within 1% of BB-upper in trailing 252d — frequency of upper-band touch."""
    _, bbu, _ = _bb(close, n=MDAYS, mult=2.0)
    near = (_safe_div((bbu - close).abs(), bbu) < 0.01)
    b = near.astype(float).where(bbu.notna(), np.nan)
    return b.rolling(YDAYS, min_periods=QDAYS).sum()


def f30_wtof_443_bb_close_at_lower_band_count_252d(close: pd.Series) -> pd.Series:
    """Count of bars with close within 1% of BB-lower in trailing 252d."""
    _, _, bbl = _bb(close, n=MDAYS, mult=2.0)
    near = (_safe_div((close - bbl).abs(), bbl) < 0.01)
    b = near.astype(float).where(bbl.notna(), np.nan)
    return b.rolling(YDAYS, min_periods=QDAYS).sum()


def f30_wtof_444_bb_walking_upper_streak_at_252d_max_event(close: pd.Series) -> pd.Series:
    """Event: current walking-upper streak length equals the 252d trailing max of streak length — longest walk in a year."""
    _, bbu, _ = _bb(close, n=MDAYS, mult=2.0)
    streak = _consec_true_streak(close > bbu)
    rmax = streak.rolling(YDAYS, min_periods=QDAYS).max()
    cond = (streak >= rmax) & (streak > 0)
    return cond.astype(float).where(rmax.notna(), np.nan)


def f30_wtof_445_bb_width_below_5pct_event(close: pd.Series) -> pd.Series:
    """Event: BB-width (% of mid) < 0.05 — absolute-compression threshold extreme."""
    bw = _bb_width_pct(close, n=MDAYS, mult=2.0)
    return (bw < 0.05).astype(float).where(bw.notna(), np.nan)


def f30_wtof_446_donchian_position_55d_top_decile_dwell_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars with 55d-Donchian-position > 0.9 in trailing 21d — sustained upper-channel dwell."""
    u = _donchian_upper_helper(high, 55)
    l = _donchian_lower_helper(low, 55)
    pos = _safe_div(close - l, u - l)
    b = (pos > 0.9).astype(float).where(pos.notna(), np.nan)
    return b.rolling(MDAYS, min_periods=WDAYS).sum()


def f30_wtof_447_ttm_momentum_amplitude_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """TTM momentum amplitude (max - min) in trailing 63d."""
    mom = _ttm_momentum(high, low, close, n=MDAYS)
    rmax = mom.rolling(QDAYS, min_periods=MDAYS).max()
    rmin = mom.rolling(QDAYS, min_periods=MDAYS).min()
    return rmax - rmin


def f30_wtof_448_ttm_squeeze_density_ratio_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of trailing 252d bars in TTM-squeeze (on/total)."""
    on = _ttm_squeeze_on(high, low, close, n=MDAYS, mult_bb=2.0, mult_kc=1.5)
    s = on.rolling(YDAYS, min_periods=QDAYS).sum()
    c = on.rolling(YDAYS, min_periods=QDAYS).count()
    return _safe_div(s, c)


def f30_wtof_449_wto_wt1_volatility_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Trailing 63d std of WT1 — vol-of-oscillator (regime-instability measure)."""
    wt1, _ = _wto_default(high, low, close, 10, 21)
    return wt1.rolling(QDAYS, min_periods=MDAYS).std()


def f30_wtof_450_wto_wt1_rolling_corr_with_close_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Trailing 63d rolling correlation between WT1 and close — negative values flag divergence regime."""
    wt1, _ = _wto_default(high, low, close, 10, 21)
    return wt1.rolling(QDAYS, min_periods=MDAYS).corr(close)


# ============================================================
#                         REGISTRY 376-450
# ============================================================

WAVE_TREND_OSCILLATOR_FAMILY_BASE_REGISTRY_376_450 = {
    "f30_wtof_376_wto_wt1_252d_max_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_376_wto_wt1_252d_max_event},
    "f30_wtof_377_wto_wt1_252d_min_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_377_wto_wt1_252d_min_event},
    "f30_wtof_378_wto_wt2_252d_max_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_378_wto_wt2_252d_max_event},
    "f30_wtof_379_wto_gap_wt1_minus_wt2_252d_max_gap_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_379_wto_gap_wt1_minus_wt2_252d_max_gap_event},
    "f30_wtof_380_wto_gap_wt1_minus_wt2_narrowing_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_380_wto_gap_wt1_minus_wt2_narrowing_event},
    "f30_wtof_381_wto_wt1_days_since_extreme_overbought_above_80": {"inputs": ["high", "low", "close"], "func": f30_wtof_381_wto_wt1_days_since_extreme_overbought_above_80},
    "f30_wtof_382_wto_wt1_days_since_extreme_oversold_below_minus80": {"inputs": ["high", "low", "close"], "func": f30_wtof_382_wto_wt1_days_since_extreme_oversold_below_minus80},
    "f30_wtof_383_wto_wt1_oscillation_zero_cross_count_63d": {"inputs": ["high", "low", "close"], "func": f30_wtof_383_wto_wt1_oscillation_zero_cross_count_63d},
    "f30_wtof_384_wto_wt1_amplitude_max_minus_min_63d": {"inputs": ["high", "low", "close"], "func": f30_wtof_384_wto_wt1_amplitude_max_minus_min_63d},
    "f30_wtof_385_wto_wt1_above_60_count_252d": {"inputs": ["high", "low", "close"], "func": f30_wtof_385_wto_wt1_above_60_count_252d},
    "f30_wtof_386_wto_wt1_streak_above_60_max_252d": {"inputs": ["high", "low", "close"], "func": f30_wtof_386_wto_wt1_streak_above_60_max_252d},
    "f30_wtof_387_wto_wt1_streak_below_minus60_max_252d": {"inputs": ["high", "low", "close"], "func": f30_wtof_387_wto_wt1_streak_below_minus60_max_252d},
    "f30_wtof_388_wto_wt1_bearish_cross_strict_in_ob_zone_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_388_wto_wt1_bearish_cross_strict_in_ob_zone_event},
    "f30_wtof_389_wto_wt1_bullish_cross_strict_in_os_zone_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_389_wto_wt1_bullish_cross_strict_in_os_zone_event},
    "f30_wtof_390_wto_wt1_distance_from_252d_max_normalized": {"inputs": ["high", "low", "close"], "func": f30_wtof_390_wto_wt1_distance_from_252d_max_normalized},
    "f30_wtof_391_wto_wt1_lower_high_event_21d": {"inputs": ["high", "low", "close"], "func": f30_wtof_391_wto_wt1_lower_high_event_21d},
    "f30_wtof_392_wto_wt2_above_zero_dwell_21d": {"inputs": ["high", "low", "close"], "func": f30_wtof_392_wto_wt2_above_zero_dwell_21d},
    "f30_wtof_393_wto_wt1_velocity_252d_max_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_393_wto_wt1_velocity_252d_max_event},
    "f30_wtof_394_wto_wt1_regime_swing_within_21d_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_394_wto_wt1_regime_swing_within_21d_event},
    "f30_wtof_395_wto_wt1_decline_from_above_80_pct_in_5d": {"inputs": ["high", "low", "close"], "func": f30_wtof_395_wto_wt1_decline_from_above_80_pct_in_5d},
    "f30_wtof_396_ttm_squeeze_max_in_squeeze_run_252d": {"inputs": ["high", "low", "close"], "func": f30_wtof_396_ttm_squeeze_max_in_squeeze_run_252d},
    "f30_wtof_397_ttm_squeeze_release_no_21d_high_within_5_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_397_ttm_squeeze_release_no_21d_high_within_5_event},
    "f30_wtof_398_ttm_squeeze_release_then_back_in_squeeze_within_5_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_398_ttm_squeeze_release_then_back_in_squeeze_within_5_event},
    "f30_wtof_399_ttm_fired_bull_then_sign_flip_within_5_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_399_ttm_fired_bull_then_sign_flip_within_5_event},
    "f30_wtof_400_ttm_fired_bear_then_sign_flip_within_5_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_400_ttm_fired_bear_then_sign_flip_within_5_event},
    "f30_wtof_401_ttm_momentum_velocity_5d": {"inputs": ["high", "low", "close"], "func": f30_wtof_401_ttm_momentum_velocity_5d},
    "f30_wtof_402_ttm_momentum_local_max_then_falling_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_402_ttm_momentum_local_max_then_falling_event},
    "f30_wtof_403_ttm_momentum_zero_cross_count_63d": {"inputs": ["high", "low", "close"], "func": f30_wtof_403_ttm_momentum_zero_cross_count_63d},
    "f30_wtof_404_ttm_momentum_above_zero_streak_max_252d": {"inputs": ["high", "low", "close"], "func": f30_wtof_404_ttm_momentum_above_zero_streak_max_252d},
    "f30_wtof_405_ttm_momentum_below_zero_streak_max_252d": {"inputs": ["high", "low", "close"], "func": f30_wtof_405_ttm_momentum_below_zero_streak_max_252d},
    "f30_wtof_406_squeeze_pro_release_from_low_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_406_squeeze_pro_release_from_low_event},
    "f30_wtof_407_squeeze_pro_release_from_mid_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_407_squeeze_pro_release_from_mid_event},
    "f30_wtof_408_squeeze_pro_low_to_high_progression_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_408_squeeze_pro_low_to_high_progression_event},
    "f30_wtof_409_squeeze_pro_high_release_failed_within_5_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_409_squeeze_pro_high_release_failed_within_5_event},
    "f30_wtof_410_squeeze_pro_bars_since_high_release": {"inputs": ["high", "low", "close"], "func": f30_wtof_410_squeeze_pro_bars_since_high_release},
    "f30_wtof_411_bollinger_stack_and_rip_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_411_bollinger_stack_and_rip_event},
    "f30_wtof_412_bollinger_head_fake_up_event": {"inputs": ["close"], "func": f30_wtof_412_bollinger_head_fake_up_event},
    "f30_wtof_413_bollinger_head_fake_down_event": {"inputs": ["close"], "func": f30_wtof_413_bollinger_head_fake_down_event},
    "f30_wtof_414_raschke_80_20_bullish_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_414_raschke_80_20_bullish_event},
    "f30_wtof_415_raschke_80_20_bearish_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_415_raschke_80_20_bearish_event},
    "f30_wtof_416_turtle_soup_long_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_416_turtle_soup_long_event},
    "f30_wtof_417_turtle_soup_short_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_417_turtle_soup_short_event},
    "f30_wtof_418_crabel_orb_proxy_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_418_crabel_orb_proxy_event},
    "f30_wtof_419_pct_b_decay_in_band_walk_event": {"inputs": ["high", "close"], "func": f30_wtof_419_pct_b_decay_in_band_walk_event},
    "f30_wtof_420_wto_wt1_decay_at_new_high_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_420_wto_wt1_decay_at_new_high_event},
    "f30_wtof_421_bb_width_vol_cone_position_252d": {"inputs": ["close"], "func": f30_wtof_421_bb_width_vol_cone_position_252d},
    "f30_wtof_422_bandwidth_compression_then_expansion_event_21d": {"inputs": ["close"], "func": f30_wtof_422_bandwidth_compression_then_expansion_event_21d},
    "f30_wtof_423_bandwidth_decline_streak_consecutive": {"inputs": ["close"], "func": f30_wtof_423_bandwidth_decline_streak_consecutive},
    "f30_wtof_424_bandwidth_expansion_streak_consecutive": {"inputs": ["close"], "func": f30_wtof_424_bandwidth_expansion_streak_consecutive},
    "f30_wtof_425_bb_width_local_max_event": {"inputs": ["close"], "func": f30_wtof_425_bb_width_local_max_event},
    "f30_wtof_426_bb_width_local_min_event": {"inputs": ["close"], "func": f30_wtof_426_bb_width_local_min_event},
    "f30_wtof_427_donchian_compressed_then_breakout_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_427_donchian_compressed_then_breakout_event},
    "f30_wtof_428_kc_width_to_bb_width_ratio": {"inputs": ["high", "low", "close"], "func": f30_wtof_428_kc_width_to_bb_width_ratio},
    "f30_wtof_429_kc_width_minus_bb_width_atr_norm": {"inputs": ["high", "low", "close"], "func": f30_wtof_429_kc_width_minus_bb_width_atr_norm},
    "f30_wtof_430_pct_b_acceleration_5d": {"inputs": ["close"], "func": f30_wtof_430_pct_b_acceleration_5d},
    "f30_wtof_431_pct_b_above_eighty_count_252d": {"inputs": ["close"], "func": f30_wtof_431_pct_b_above_eighty_count_252d},
    "f30_wtof_432_pct_b_below_twenty_count_252d": {"inputs": ["close"], "func": f30_wtof_432_pct_b_below_twenty_count_252d},
    "f30_wtof_433_bb_upper_first_touch_after_21d_inside_event": {"inputs": ["close"], "func": f30_wtof_433_bb_upper_first_touch_after_21d_inside_event},
    "f30_wtof_434_bb_lower_first_touch_after_21d_inside_event": {"inputs": ["close"], "func": f30_wtof_434_bb_lower_first_touch_after_21d_inside_event},
    "f30_wtof_435_bollinger_squeeze_short_term_5d_on": {"inputs": ["high", "low", "close"], "func": f30_wtof_435_bollinger_squeeze_short_term_5d_on},
    "f30_wtof_436_bollinger_squeeze_super_short_5d_release_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_436_bollinger_squeeze_super_short_5d_release_event},
    "f30_wtof_437_walking_upper_then_walking_lower_within_21d_event": {"inputs": ["close"], "func": f30_wtof_437_walking_upper_then_walking_lower_within_21d_event},
    "f30_wtof_438_pct_b_3day_avg_below_zero_event": {"inputs": ["close"], "func": f30_wtof_438_pct_b_3day_avg_below_zero_event},
    "f30_wtof_439_pct_b_3day_avg_above_one_event": {"inputs": ["close"], "func": f30_wtof_439_pct_b_3day_avg_above_one_event},
    "f30_wtof_440_pct_b_above_1_consecutive_streak": {"inputs": ["close"], "func": f30_wtof_440_pct_b_above_1_consecutive_streak},
    "f30_wtof_441_pct_b_below_0_consecutive_streak": {"inputs": ["close"], "func": f30_wtof_441_pct_b_below_0_consecutive_streak},
    "f30_wtof_442_bb_close_at_upper_band_count_252d": {"inputs": ["close"], "func": f30_wtof_442_bb_close_at_upper_band_count_252d},
    "f30_wtof_443_bb_close_at_lower_band_count_252d": {"inputs": ["close"], "func": f30_wtof_443_bb_close_at_lower_band_count_252d},
    "f30_wtof_444_bb_walking_upper_streak_at_252d_max_event": {"inputs": ["close"], "func": f30_wtof_444_bb_walking_upper_streak_at_252d_max_event},
    "f30_wtof_445_bb_width_below_5pct_event": {"inputs": ["close"], "func": f30_wtof_445_bb_width_below_5pct_event},
    "f30_wtof_446_donchian_position_55d_top_decile_dwell_21d": {"inputs": ["high", "low", "close"], "func": f30_wtof_446_donchian_position_55d_top_decile_dwell_21d},
    "f30_wtof_447_ttm_momentum_amplitude_63d": {"inputs": ["high", "low", "close"], "func": f30_wtof_447_ttm_momentum_amplitude_63d},
    "f30_wtof_448_ttm_squeeze_density_ratio_252d": {"inputs": ["high", "low", "close"], "func": f30_wtof_448_ttm_squeeze_density_ratio_252d},
    "f30_wtof_449_wto_wt1_volatility_63d": {"inputs": ["high", "low", "close"], "func": f30_wtof_449_wto_wt1_volatility_63d},
    "f30_wtof_450_wto_wt1_rolling_corr_with_close_63d": {"inputs": ["high", "low", "close"], "func": f30_wtof_450_wto_wt1_rolling_corr_with_close_63d},
}
