"""ultimate_aroon_vortex base features 226-300 — Pipeline 1b-technical.

Gap-fill extension to the original 150-feature family (continuation). Fills:
  - Choppiness-Index zone/regime features beyond cross-events
  - Mass-Index sensitivity / Donald-Dorsey reversal-bulge taxonomy / inner
    range-expansion ratio EMA9(H-L)/EMA9(EMA9(H-L)) as standalone
  - Composite cross-indicator alignments not in original 150:
    Aroon-Up x DI+ / Aroon-Down x DI-, ADXR x CI, UO-oversold x DI- trend,
    CI-rising x MI-bulge transition, ADX x Vortex combined
  - Event-recency / bars-since features for the major event types
  - Regime histograms / fractions over multi-year windows
  - True multi-horizon hypotheses for ADXR, Choppiness, Mass-Index, Vortex

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers — no cross-family
imports.
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


def _wilder_ema(s, n):
    return s.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()


# ---------------------------- indicator primitives ----------------------------

def _dm_raw(high, low):
    up = high.diff()
    dn = -low.diff()
    plus_dm = pd.Series(np.where((up > dn) & (up > 0), up, 0.0), index=high.index)
    minus_dm = pd.Series(np.where((dn > up) & (dn > 0), dn, 0.0), index=high.index)
    return plus_dm, minus_dm


def _dm_components(high, low, close, n=14):
    plus_dm, minus_dm = _dm_raw(high, low)
    tr = _true_range(high, low, close)
    atr = _wilder_ema(tr, n)
    plus_di = 100.0 * _safe_div(_wilder_ema(plus_dm, n), atr)
    minus_di = 100.0 * _safe_div(_wilder_ema(minus_dm, n), atr)
    dx = 100.0 * _safe_div((plus_di - minus_di).abs(), (plus_di + minus_di))
    adx = _wilder_ema(dx, n)
    return plus_di, minus_di, adx


def _adxr(high, low, close, n=14):
    _, _, adx = _dm_components(high, low, close, n=n)
    return 0.5 * (adx + adx.shift(n - 1))


def _aroon_up(high, n):
    def _f(w):
        if np.isnan(w).all():
            return np.nan
        idx = int(np.nanargmax(w))
        return 100.0 * (idx) / (len(w) - 1) if len(w) > 1 else np.nan
    return high.rolling(n + 1, min_periods=max((n + 1) // 2, 2)).apply(_f, raw=True)


def _aroon_down(low, n):
    def _f(w):
        if np.isnan(w).all():
            return np.nan
        idx = int(np.nanargmin(w))
        return 100.0 * (idx) / (len(w) - 1) if len(w) > 1 else np.nan
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
    return _safe_div(sum_vm_plus, sum_tr), _safe_div(sum_vm_minus, sum_tr)


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
    """Inner ratio of Mass Index: EMA9(H-L) / EMA9(EMA9(H-L)) — standalone range-expansion metric."""
    rng = high - low
    e1 = rng.ewm(span=ema_n, adjust=False, min_periods=ema_n).mean()
    e2 = e1.ewm(span=ema_n, adjust=False, min_periods=ema_n).mean()
    return _safe_div(e1, e2)


def _bars_since(condition_series, lookback):
    def _bsm(w):
        idx = np.where(w > 0)[0]
        if idx.size == 0:
            return float(len(w))
        return float((len(w) - 1) - idx[-1])
    return condition_series.astype(float).rolling(lookback, min_periods=max(lookback // 3, 2)).apply(_bsm, raw=True)


# ============================================================
# Bucket H — Choppiness regime histograms / fractions (226-235)
# ============================================================

def f29_uarn_226_choppiness_25_minus_50_spread(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Choppiness(25) − Choppiness(50): mid vs long-horizon regime spread."""
    return _choppiness(high, low, close, n=25) - _choppiness(high, low, close, n=50)


def f29_uarn_227_choppiness_fraction_trending_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of bars in trailing 252d where Choppiness(14) < 38.2 — annual trending share."""
    ci = _choppiness(high, low, close, n=14)
    return (ci < 38.2).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f29_uarn_228_choppiness_fraction_ranging_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of bars in trailing 252d where Choppiness(14) > 61.8 — annual ranging share."""
    ci = _choppiness(high, low, close, n=14)
    return (ci > 61.8).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f29_uarn_229_choppiness_bars_since_last_ranging_above_62(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since Choppiness(14) was last > 61.8 — staleness of ranging regime."""
    ci = _choppiness(high, low, close, n=14)
    cond = (ci > 61.8).astype(float)
    return _bars_since(cond, YDAYS)


def f29_uarn_230_choppiness_regime_transition_count_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of CI(14) Fibonacci-band crossings (in/out of [38.2, 61.8]) in trailing 252d — regime instability."""
    ci = _choppiness(high, low, close, n=14)
    inside = ((ci >= 38.2) & (ci <= 61.8)).astype(float)
    flips = (inside != inside.shift(1)).astype(float)
    flips.iloc[0] = 0.0
    return flips.rolling(YDAYS, min_periods=QDAYS).sum()


def f29_uarn_231_choppiness_long_100d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Choppiness(100) — very-long-horizon regime classification (multi-month structural)."""
    return _choppiness(high, low, close, n=100)


def f29_uarn_232_choppiness_at_252d_high_value(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """At bars where high == 252d max, value of Choppiness(14) — regime reading right at the peak."""
    ci = _choppiness(high, low, close, n=14)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = (high >= rmax)
    return ci.where(at_peak, np.nan)


def f29_uarn_233_choppiness_persistence_above_50_streak(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current consecutive-bar streak where Choppiness(14) > 50 — ranging-side persistence."""
    ci = _choppiness(high, low, close, n=14)
    above = (ci > 50.0).astype(float).values
    n = len(above)
    out = np.full(n, np.nan, dtype=float)
    streak = 0
    for i in range(n):
        if pd.isna(ci.iat[i]):
            streak = 0
            out[i] = np.nan
        else:
            streak = streak + 1 if above[i] > 0 else 0
            out[i] = float(streak)
    return pd.Series(out, index=ci.index)


def f29_uarn_234_choppiness_distance_from_50_midline(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """|Choppiness(14) − 50|: distance from regime-neutral midline (high = extreme regime, either side)."""
    ci = _choppiness(high, low, close, n=14)
    return (ci - 50.0).abs()


def f29_uarn_235_choppiness_min_in_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252d min of Choppiness(14) — strongest-trending reading in the year (lower = stronger)."""
    return _choppiness(high, low, close, n=14).rolling(YDAYS, min_periods=QDAYS).min()


# ============================================================
# Bucket I — Mass Index / range-expansion extensions (236-245)
# ============================================================

def f29_uarn_236_mass_index_long_horizon_50d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Mass-Index(50, ema9) — long-horizon bulge sensor (slower variant for monthly regime)."""
    return _mass_index(high, low, n=50, ema_n=9)


def f29_uarn_237_range_expansion_ratio_inner_ema9(high: pd.Series, low: pd.Series) -> pd.Series:
    """EMA9(H-L) / EMA9(EMA9(H-L)) — standalone inner ratio of Mass Index (range-expansion intensity)."""
    return _range_expansion_ratio(high, low, ema_n=9)


def f29_uarn_238_range_expansion_ratio_above_1_indicator(high: pd.Series, low: pd.Series) -> pd.Series:
    """Indicator: EMA9(H-L)/EMA9(EMA9(H-L)) > 1 — current range expanding vs its EMA baseline."""
    r = _range_expansion_ratio(high, low, ema_n=9)
    return (r > 1.0).astype(float).where(r.notna(), np.nan)


def f29_uarn_239_range_expansion_ratio_zscore_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of range-expansion ratio in 252d window — anomalous expansion reading."""
    r = _range_expansion_ratio(high, low, ema_n=9)
    return _rolling_zscore(r, YDAYS, min_periods=QDAYS)


def f29_uarn_240_mass_index_bars_since_last_bulge_event(high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars since last Donald-Dorsey reversal bulge event (MI>27 then drop below 26.5)."""
    mi = _mass_index(high, low, n=25, ema_n=9)
    bulge = (mi.rolling(MDAYS, min_periods=WDAYS).max() > 27.0)
    bulge_event = (bulge & (mi < 26.5)).astype(float)
    return _bars_since(bulge_event, YDAYS)


def f29_uarn_241_mass_index_bulge_count_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of Donald-Dorsey reversal-bulge events in trailing 252d — annual bulge cadence."""
    mi = _mass_index(high, low, n=25, ema_n=9)
    bulge = (mi.rolling(MDAYS, min_periods=WDAYS).max() > 27.0)
    event = (bulge & (mi < 26.5)).astype(float)
    return event.rolling(YDAYS, min_periods=QDAYS).sum()


def f29_uarn_242_mass_index_horizon_dispersion(high: pd.Series, low: pd.Series) -> pd.Series:
    """Std-dev of MI across horizons {15, 25, 50} — cross-horizon bulge agreement."""
    m15 = _mass_index(high, low, n=15, ema_n=9)
    m25 = _mass_index(high, low, n=25, ema_n=9)
    m50 = _mass_index(high, low, n=50, ema_n=9)
    df = pd.concat([m15.rename("m15"), m25.rename("m25"), m50.rename("m50")], axis=1)
    return df.std(axis=1)


def f29_uarn_243_range_expansion_ratio_5d_slope(high: pd.Series, low: pd.Series) -> pd.Series:
    """5d slope of inner range-expansion ratio — bulge-rising velocity."""
    r = _range_expansion_ratio(high, low, ema_n=9)
    return _rolling_slope(r, WDAYS, min_periods=3)


def f29_uarn_244_mass_index_25_minus_50_spread(high: pd.Series, low: pd.Series) -> pd.Series:
    """MI(25) − MI(50): classic vs long-horizon bulge spread (short-leading-long signal)."""
    return _mass_index(high, low, n=25, ema_n=9) - _mass_index(high, low, n=50, ema_n=9)


def f29_uarn_245_range_expansion_ratio_at_252d_high(high: pd.Series, low: pd.Series) -> pd.Series:
    """At bars where high == 252d max, value of inner range-expansion ratio — expansion-state at peak."""
    r = _range_expansion_ratio(high, low, ema_n=9)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = (high >= rmax)
    return r.where(at_peak, np.nan)


# ============================================================
# Bucket J — New cross-indicator composites (246-265)
# ============================================================

def f29_uarn_246_aroon_up_with_di_plus_dominant_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: Aroon-Up(25) > 70 AND DI+(14) > DI-(14) — bullish-recency aligned with bullish-DM."""
    au = _aroon_up(high, 25)
    plus_di, minus_di, _ = _dm_components(high, low, close, n=14)
    cond = (au > 70.0) & (plus_di > minus_di)
    return cond.astype(float).where(au.notna() & plus_di.notna(), np.nan)


def f29_uarn_247_aroon_down_with_di_minus_dominant_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: Aroon-Down(25) > 70 AND DI-(14) > DI+(14) — bearish-recency aligned with bearish-DM."""
    ad = _aroon_down(low, 25)
    plus_di, minus_di, _ = _dm_components(high, low, close, n=14)
    cond = (ad > 70.0) & (minus_di > plus_di)
    return cond.astype(float).where(ad.notna() & plus_di.notna(), np.nan)


def f29_uarn_248_adx_times_vortex_diff_combined(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ADX(14) * (VI+ − VI-)(14): Wilder strength × Botes-Siepman direction — signed combined trend."""
    _, _, adx = _dm_components(high, low, close, n=14)
    vp, vm = _vortex(high, low, close, n=14)
    return adx * (vp - vm)


def f29_uarn_249_adxr_with_choppiness_low_trend_health(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: ADXR(14) > 25 AND Choppiness(14) < 38.2 — Wilder-smoothed trend confirmed by CI."""
    a = _adxr(high, low, close, n=14)
    ci = _choppiness(high, low, close, n=14)
    cond = (a > 25.0) & (ci < 38.2)
    return cond.astype(float).where(a.notna() & ci.notna(), np.nan)


def f29_uarn_250_uo_oversold_with_di_minus_rising_failure(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite: UO < 30 AND DI-(14) rising — bearish-trend-bottom failure (oversold meets bear-DM)."""
    uo = _ultimate_osc(high, low, close, 7, 14, 28)
    _, minus_di, _ = _dm_components(high, low, close, n=14)
    cond = (uo < 30.0) & (minus_di.diff() > 0)
    return cond.astype(float).where(uo.notna() & minus_di.notna(), np.nan)


def f29_uarn_251_choppiness_rising_with_mass_bulge_transition(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite: Choppiness(14) rising AND Mass Index > 27 — transition-to-range-bound primer."""
    ci = _choppiness(high, low, close, n=14)
    mi = _mass_index(high, low, n=25, ema_n=9)
    cond = (ci.diff() > 0) & (mi > 27.0)
    return cond.astype(float).where(ci.notna() & mi.notna(), np.nan)


def f29_uarn_252_trend_health_composite_score(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Trend-health score: count of {ADX>25, CI<38, Vortex-diff>0, DI+>DI-} all true — max 4."""
    _, _, adx = _dm_components(high, low, close, n=14)
    ci = _choppiness(high, low, close, n=14)
    vp, vm = _vortex(high, low, close, n=14)
    plus_di, minus_di, _ = _dm_components(high, low, close, n=14)
    pieces = [
        (adx > 25.0).astype(float).rename("a"),
        (ci < 38.0).astype(float).rename("c"),
        ((vp - vm) > 0).astype(float).rename("v"),
        (plus_di > minus_di).astype(float).rename("d"),
    ]
    return pd.concat(pieces, axis=1).sum(axis=1)


def f29_uarn_253_bearish_trend_health_composite_score(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish-trend-health score: count of {ADX>25, CI<38, Vortex-diff<0, DI->DI+} — bear regime quality."""
    _, _, adx = _dm_components(high, low, close, n=14)
    ci = _choppiness(high, low, close, n=14)
    vp, vm = _vortex(high, low, close, n=14)
    plus_di, minus_di, _ = _dm_components(high, low, close, n=14)
    pieces = [
        (adx > 25.0).astype(float).rename("a"),
        (ci < 38.0).astype(float).rename("c"),
        ((vp - vm) < 0).astype(float).rename("v"),
        (minus_di > plus_di).astype(float).rename("d"),
    ]
    return pd.concat(pieces, axis=1).sum(axis=1)


def f29_uarn_254_vortex_bear_cross_with_adxr_above_25(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite: VI- crossed above VI+ today AND ADXR(14) > 25 — bear-cross in confirmed-trend regime."""
    vp, vm = _vortex(high, low, close, n=14)
    cross = (vm > vp) & (vm.shift(1) <= vp.shift(1))
    a = _adxr(high, low, close, n=14)
    cond = cross & (a > 25.0)
    return cond.astype(float).where(vp.notna() & a.notna(), np.nan)


def f29_uarn_255_aroon_up_collapse_with_vortex_bear_cross(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite: Aroon-Up(25) was 100 within 5 bars, now < 70, AND VI- crossed above VI+ today."""
    au = _aroon_up(high, 25)
    recent_peak = (au.rolling(WDAYS, min_periods=2).max() >= 99.999)
    vp, vm = _vortex(high, low, close, n=14)
    cross = (vm > vp) & (vm.shift(1) <= vp.shift(1))
    cond = recent_peak.shift(1).fillna(False) & (au < 70.0) & cross
    return cond.astype(float).where(au.notna() & vp.notna(), np.nan)


def f29_uarn_256_dx_above_50_extreme_imbalance(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: raw DX(14) > 50 — extreme directional-imbalance reading before any ADX smoothing."""
    p, m, _ = _dm_components(high, low, close, n=14)
    dx = 100.0 * _safe_div((p - m).abs(), p + m)
    return (dx > 50.0).astype(float).where(dx.notna(), np.nan)


def f29_uarn_257_mass_bulge_with_di_minus_dominant(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite: MI > 27 AND DI-(14) > DI+(14) — range-expansion with bearish-DM dominance."""
    mi = _mass_index(high, low, n=25, ema_n=9)
    plus_di, minus_di, _ = _dm_components(high, low, close, n=14)
    cond = (mi > 27.0) & (minus_di > plus_di)
    return cond.astype(float).where(mi.notna() & plus_di.notna(), np.nan)


def f29_uarn_258_uo_falling_with_aroon_down_rising(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite: UO falling AND Aroon-Down(25) rising — momentum-decay confirmed by recency-of-low."""
    uo = _ultimate_osc(high, low, close, 7, 14, 28)
    ad = _aroon_down(low, 25)
    cond = (uo.diff() < 0) & (ad.diff() > 0)
    return cond.astype(float).where(uo.notna() & ad.notna(), np.nan)


def f29_uarn_259_adxr_falling_with_vortex_bear_dominant(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite: ADXR(14) falling AND VI- > VI+ — smoothed trend weakening into bearish-vortex regime."""
    a = _adxr(high, low, close, n=14)
    vp, vm = _vortex(high, low, close, n=14)
    cond = (a.diff() < 0) & (vm > vp)
    return cond.astype(float).where(a.notna() & vp.notna(), np.nan)


def f29_uarn_260_choppiness_low_with_di_balance_negative(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: Choppiness(14) < 38.2 AND (DI+ − DI-) < 0 — confirmed bearish-trending regime."""
    ci = _choppiness(high, low, close, n=14)
    p, m, _ = _dm_components(high, low, close, n=14)
    cond = (ci < 38.2) & ((p - m) < 0)
    return cond.astype(float).where(ci.notna() & p.notna(), np.nan)


def f29_uarn_261_vortex_diff_below_zero_with_aroon_down_above_70(high: pd.Series, low: pd.Series) -> pd.Series:
    """Composite: a degenerate-input variant — VI requires close so use only HL: replaced by Aroon-Up(25)<30 AND Aroon-Down(25)>70 — bear-recency double-confirm."""
    au = _aroon_up(high, 25)
    ad = _aroon_down(low, 25)
    cond = (au < 30.0) & (ad > 70.0)
    return cond.astype(float).where(au.notna() & ad.notna(), np.nan)


def f29_uarn_262_aroon_oscillator_with_di_balance_sign_agreement(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sign agreement of Aroon-Osc(25) and (DI+−DI-)(14): +1 = agree, -1 = disagree, 0 = either zero."""
    osc = _aroon_up(high, 25) - _aroon_down(low, 25)
    p, m, _ = _dm_components(high, low, close, n=14)
    return np.sign(osc) * np.sign(p - m)


def f29_uarn_263_uo_with_adxr_strong_bearish_combo(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: UO < 40 AND ADXR(14) > 30 — confirmed strong-bearish-trend exhaustion."""
    uo = _ultimate_osc(high, low, close, 7, 14, 28)
    a = _adxr(high, low, close, n=14)
    cond = (uo < 40.0) & (a > 30.0)
    return cond.astype(float).where(uo.notna() & a.notna(), np.nan)


def f29_uarn_264_mass_bulge_with_choppiness_breakout(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite: MI > 27 AND Choppiness(14) crossing above 50 today — range-expansion at chop ignition."""
    mi = _mass_index(high, low, n=25, ema_n=9)
    ci = _choppiness(high, low, close, n=14)
    cross = (ci > 50.0) & (ci.shift(1) <= 50.0)
    cond = (mi > 27.0) & cross
    return cond.astype(float).where(mi.notna() & ci.notna(), np.nan)


def f29_uarn_265_vortex_diff_with_adx_disagreement(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """|sign(Vortex-diff(14)) − sign(DI+ − DI-)(14)|: 0 = agree, 2 = full disagree — indicator-divergence measure."""
    vp, vm = _vortex(high, low, close, n=14)
    p, m, _ = _dm_components(high, low, close, n=14)
    return (np.sign(vp - vm) - np.sign(p - m)).abs()


# ============================================================
# Bucket K — Event recency / bars-since features (266-280)
# ============================================================

def f29_uarn_266_bars_since_last_di_cross(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since last DI+/DI- crossover (either direction) in 14d — staleness of last directional flip."""
    p, m, _ = _dm_components(high, low, close, n=14)
    flip = (np.sign(p - m) != np.sign(p - m).shift(1)).astype(float)
    flip.iloc[0] = 0.0
    return _bars_since(flip, YDAYS)


def f29_uarn_267_bars_since_last_vortex_cross(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since last VI+/VI- crossover (either direction) in 14d — staleness of last vortex flip."""
    vp, vm = _vortex(high, low, close, n=14)
    flip = (np.sign(vp - vm) != np.sign(vp - vm).shift(1)).astype(float)
    flip.iloc[0] = 0.0
    return _bars_since(flip, YDAYS)


def f29_uarn_268_bars_since_last_adx_peak_above_40(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since ADX(14) was last above 40 — staleness of last extreme-trend reading."""
    _, _, adx = _dm_components(high, low, close, n=14)
    cond = (adx > 40.0).astype(float)
    return _bars_since(cond, YDAYS)


def f29_uarn_269_bars_since_last_mass_bulge_above_27(high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars since Mass Index was last above 27 — staleness of last range-expansion bulge."""
    mi = _mass_index(high, low, n=25, ema_n=9)
    cond = (mi > 27.0).astype(float)
    return _bars_since(cond, YDAYS)


def f29_uarn_270_bars_since_last_aroon_osc_zero_cross(high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars since last Aroon-Osc(25) zero crossing — staleness of last directional flip."""
    osc = _aroon_up(high, 25) - _aroon_down(low, 25)
    flip = (np.sign(osc) != np.sign(osc).shift(1)).astype(float)
    flip.iloc[0] = 0.0
    return _bars_since(flip, YDAYS)


def f29_uarn_271_bars_since_last_uo_above_80(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since UO was last above the 80 extreme line — staleness of last extreme-overbought reading."""
    uo = _ultimate_osc(high, low, close, 7, 14, 28)
    cond = (uo > 80.0).astype(float)
    return _bars_since(cond, YDAYS)


def f29_uarn_272_bars_since_last_uo_below_20(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since UO was last below the 20 extreme-oversold line — staleness of last oversold reading."""
    uo = _ultimate_osc(high, low, close, 7, 14, 28)
    cond = (uo < 20.0).astype(float)
    return _bars_since(cond, YDAYS)


def f29_uarn_273_bars_since_last_di_minus_above_30(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since DI-(14) was last above 30 — staleness of last hot bearish-DM reading."""
    _, minus_di, _ = _dm_components(high, low, close, n=14)
    cond = (minus_di > 30.0).astype(float)
    return _bars_since(cond, YDAYS)


def f29_uarn_274_bars_since_last_di_plus_above_30(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since DI+(14) was last above 30 — staleness of last hot bullish-DM reading."""
    plus_di, _, _ = _dm_components(high, low, close, n=14)
    cond = (plus_di > 30.0).astype(float)
    return _bars_since(cond, YDAYS)


def f29_uarn_275_bars_since_last_choppiness_below_30(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since Choppiness(14) was last below 30 — staleness of last strong-trending regime."""
    ci = _choppiness(high, low, close, n=14)
    cond = (ci < 30.0).astype(float)
    return _bars_since(cond, YDAYS)


def f29_uarn_276_bars_since_last_aroon_down_100(low: pd.Series) -> pd.Series:
    """Bars since Aroon-Down(25) was last 100 — staleness of most-recent fresh new low."""
    ad = _aroon_down(low, 25)
    cond = (ad >= 99.999).astype(float)
    return _bars_since(cond, YDAYS)


def f29_uarn_277_bars_since_last_vortex_diff_extreme_pos(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since Vortex-diff(14) was last > 0.3 — staleness of last strong-bullish-vortex reading."""
    vp, vm = _vortex(high, low, close, n=14)
    cond = ((vp - vm) > 0.3).astype(float)
    return _bars_since(cond, YDAYS)


def f29_uarn_278_bars_since_last_vortex_diff_extreme_neg(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since Vortex-diff(14) was last < -0.3 — staleness of last strong-bearish-vortex reading."""
    vp, vm = _vortex(high, low, close, n=14)
    cond = ((vp - vm) < -0.3).astype(float)
    return _bars_since(cond, YDAYS)


def f29_uarn_279_bars_since_last_adx_below_15_reset(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since ADXR(14) was last below 15 — staleness of last smoothed-rating reset (long-term trend baseline)."""
    a = _adxr(high, low, close, n=14)
    cond = (a < 15.0).astype(float)
    return _bars_since(cond, YDAYS)


def f29_uarn_280_bars_since_last_di_plus_above_di_minus(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since DI+(14) was last > DI-(14) — staleness of last bullish-dominant regime."""
    p, m, _ = _dm_components(high, low, close, n=14)
    cond = (p > m).astype(float)
    return _bars_since(cond, YDAYS)


# ============================================================
# Bucket L — Regime histograms / fractions over long windows (281-290)
# ============================================================

def f29_uarn_281_fraction_di_minus_dominant_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of bars in trailing 252d where DI-(14) > DI+(14) — annual bearish-regime share."""
    p, m, _ = _dm_components(high, low, close, n=14)
    return (m > p).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f29_uarn_282_count_di_crossovers_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of DI+/DI- crossovers in trailing 252d — annual regime-flip cadence."""
    p, m, _ = _dm_components(high, low, close, n=14)
    flip = (np.sign(p - m) != np.sign(p - m).shift(1)).astype(float)
    flip.iloc[0] = 0.0
    return flip.rolling(YDAYS, min_periods=QDAYS).sum()


def f29_uarn_283_count_vortex_crossovers_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of VI+/VI- crossovers in trailing 252d — annual vortex-flip cadence."""
    vp, vm = _vortex(high, low, close, n=14)
    flip = (np.sign(vp - vm) != np.sign(vp - vm).shift(1)).astype(float)
    flip.iloc[0] = 0.0
    return flip.rolling(YDAYS, min_periods=QDAYS).sum()


def f29_uarn_284_fraction_adx_above_25_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of bars in trailing 252d with ADX(14) > 25 — annual strong-trend share."""
    _, _, adx = _dm_components(high, low, close, n=14)
    return (adx > 25.0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f29_uarn_285_fraction_aroon_up_above_70_252d(high: pd.Series) -> pd.Series:
    """Fraction of bars in trailing 252d with Aroon-Up(25) > 70 — annual recent-high dominance share."""
    au = _aroon_up(high, 25)
    return (au > 70.0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f29_uarn_286_fraction_aroon_down_above_70_252d(low: pd.Series) -> pd.Series:
    """Fraction of bars in trailing 252d with Aroon-Down(25) > 70 — annual recent-low dominance share."""
    ad = _aroon_down(low, 25)
    return (ad > 70.0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f29_uarn_287_fraction_mass_above_27_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of bars in trailing 252d with Mass Index > 27 — annual bulge share."""
    mi = _mass_index(high, low, n=25, ema_n=9)
    return (mi > 27.0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f29_uarn_288_fraction_uo_above_70_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of bars in trailing 252d with UO > 70 — annual overbought share."""
    uo = _ultimate_osc(high, low, close, 7, 14, 28)
    return (uo > 70.0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f29_uarn_289_fraction_vortex_bull_504d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of bars in trailing 504d (2y) with VI+(14) > VI-(14) — biennial bullish-vortex share."""
    vp, vm = _vortex(high, low, close, n=14)
    return (vp > vm).astype(float).rolling(DDAYS_2Y, min_periods=YDAYS).mean()


def f29_uarn_290_count_aroon_up_at_100_252d(high: pd.Series) -> pd.Series:
    """Count of bars in trailing 252d with Aroon-Up(25) = 100 — annual fresh-high count."""
    au = _aroon_up(high, 25)
    return (au >= 99.999).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket M — Long-horizon / multi-year distinct (291-300)
# ============================================================

def f29_uarn_291_adxr_504d_horizon(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ADXR(50) — biennial-scale smoothed trend rating (long-term cycle position)."""
    return _adxr(high, low, close, n=50)


def f29_uarn_292_aroon_oscillator_756d_3y_horizon(high: pd.Series, low: pd.Series) -> pd.Series:
    """Aroon-Osc(756) — 3y multi-year cycle directional bias."""
    return _aroon_up(high, 756) - _aroon_down(low, 756)


def f29_uarn_293_choppiness_252d_annual_regime(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Choppiness(252) — annual-scale regime classification (multi-year structural)."""
    return _choppiness(high, low, close, n=252)


def f29_uarn_294_mass_index_100d_horizon(high: pd.Series, low: pd.Series) -> pd.Series:
    """Mass-Index(100, ema9) — long-horizon range-expansion sensor (multi-month bulge)."""
    return _mass_index(high, low, n=100, ema_n=9)


def f29_uarn_295_vortex_diff_long_50d_to_short_14d_ratio(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(Vortex-diff(50) − Vortex-diff(14)) / |Vortex-diff(14)|: relative long-horizon disagreement."""
    vp14, vm14 = _vortex(high, low, close, n=14)
    vp50, vm50 = _vortex(high, low, close, n=50)
    d14 = vp14 - vm14
    d50 = vp50 - vm50
    return _safe_div(d50 - d14, d14.abs())


def f29_uarn_296_adx_504d_horizon(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ADX(100) — multi-month trend-strength reading for very-slow regime."""
    _, _, adx = _dm_components(high, low, close, n=100)
    return adx


def f29_uarn_297_aroon_up_minus_down_at_log_close_252d(close: pd.Series) -> pd.Series:
    """Aroon-Osc(252) computed on log-close — annual log-domain recency-balance signal."""
    return _aroon_up(_safe_log(close), 252) - _aroon_down(_safe_log(close), 252)


def f29_uarn_298_adxr_minus_adxr_long_horizon_spread(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ADXR(14) − ADXR(50): short vs biennial smoothed trend rating — leading-rating spread."""
    return _adxr(high, low, close, n=14) - _adxr(high, low, close, n=50)


def f29_uarn_299_aroon_oscillator_100d_minus_25d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Aroon-Osc(100) − Aroon-Osc(25): multi-month vs monthly directional-balance spread."""
    o100 = _aroon_up(high, 100) - _aroon_down(low, 100)
    o25 = _aroon_up(high, 25) - _aroon_down(low, 25)
    return o100 - o25


def f29_uarn_300_composite_uarn_long_horizon_bearish_score(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Long-horizon composite bearish score using slow indicators: weighted blend of ADXR(50)*sign(DI-(50)-DI+(50)), Aroon-Osc(100), Vortex-diff(50)."""
    a50 = _adxr(high, low, close, n=50)
    p50, m50, _ = _dm_components(high, low, close, n=50)
    o100 = _aroon_up(high, 100) - _aroon_down(low, 100)
    vp50, vm50 = _vortex(high, low, close, n=50)
    score = (a50 / 100.0) * np.sign(m50 - p50) + (-o100 / 100.0) + (vm50 - vp50)
    return score / 3.0


# ============================================================
#                         REGISTRY 226-300
# ============================================================

ULTIMATE_AROON_VORTEX_BASE_REGISTRY_226_300 = {
    "f29_uarn_226_choppiness_25_minus_50_spread": {"inputs": ["high", "low", "close"], "func": f29_uarn_226_choppiness_25_minus_50_spread},
    "f29_uarn_227_choppiness_fraction_trending_252d": {"inputs": ["high", "low", "close"], "func": f29_uarn_227_choppiness_fraction_trending_252d},
    "f29_uarn_228_choppiness_fraction_ranging_252d": {"inputs": ["high", "low", "close"], "func": f29_uarn_228_choppiness_fraction_ranging_252d},
    "f29_uarn_229_choppiness_bars_since_last_ranging_above_62": {"inputs": ["high", "low", "close"], "func": f29_uarn_229_choppiness_bars_since_last_ranging_above_62},
    "f29_uarn_230_choppiness_regime_transition_count_252d": {"inputs": ["high", "low", "close"], "func": f29_uarn_230_choppiness_regime_transition_count_252d},
    "f29_uarn_231_choppiness_long_100d": {"inputs": ["high", "low", "close"], "func": f29_uarn_231_choppiness_long_100d},
    "f29_uarn_232_choppiness_at_252d_high_value": {"inputs": ["high", "low", "close"], "func": f29_uarn_232_choppiness_at_252d_high_value},
    "f29_uarn_233_choppiness_persistence_above_50_streak": {"inputs": ["high", "low", "close"], "func": f29_uarn_233_choppiness_persistence_above_50_streak},
    "f29_uarn_234_choppiness_distance_from_50_midline": {"inputs": ["high", "low", "close"], "func": f29_uarn_234_choppiness_distance_from_50_midline},
    "f29_uarn_235_choppiness_min_in_252d": {"inputs": ["high", "low", "close"], "func": f29_uarn_235_choppiness_min_in_252d},
    "f29_uarn_236_mass_index_long_horizon_50d": {"inputs": ["high", "low"], "func": f29_uarn_236_mass_index_long_horizon_50d},
    "f29_uarn_237_range_expansion_ratio_inner_ema9": {"inputs": ["high", "low"], "func": f29_uarn_237_range_expansion_ratio_inner_ema9},
    "f29_uarn_238_range_expansion_ratio_above_1_indicator": {"inputs": ["high", "low"], "func": f29_uarn_238_range_expansion_ratio_above_1_indicator},
    "f29_uarn_239_range_expansion_ratio_zscore_252d": {"inputs": ["high", "low"], "func": f29_uarn_239_range_expansion_ratio_zscore_252d},
    "f29_uarn_240_mass_index_bars_since_last_bulge_event": {"inputs": ["high", "low"], "func": f29_uarn_240_mass_index_bars_since_last_bulge_event},
    "f29_uarn_241_mass_index_bulge_count_252d": {"inputs": ["high", "low"], "func": f29_uarn_241_mass_index_bulge_count_252d},
    "f29_uarn_242_mass_index_horizon_dispersion": {"inputs": ["high", "low"], "func": f29_uarn_242_mass_index_horizon_dispersion},
    "f29_uarn_243_range_expansion_ratio_5d_slope": {"inputs": ["high", "low"], "func": f29_uarn_243_range_expansion_ratio_5d_slope},
    "f29_uarn_244_mass_index_25_minus_50_spread": {"inputs": ["high", "low"], "func": f29_uarn_244_mass_index_25_minus_50_spread},
    "f29_uarn_245_range_expansion_ratio_at_252d_high": {"inputs": ["high", "low"], "func": f29_uarn_245_range_expansion_ratio_at_252d_high},
    "f29_uarn_246_aroon_up_with_di_plus_dominant_indicator": {"inputs": ["high", "low", "close"], "func": f29_uarn_246_aroon_up_with_di_plus_dominant_indicator},
    "f29_uarn_247_aroon_down_with_di_minus_dominant_indicator": {"inputs": ["high", "low", "close"], "func": f29_uarn_247_aroon_down_with_di_minus_dominant_indicator},
    "f29_uarn_248_adx_times_vortex_diff_combined": {"inputs": ["high", "low", "close"], "func": f29_uarn_248_adx_times_vortex_diff_combined},
    "f29_uarn_249_adxr_with_choppiness_low_trend_health": {"inputs": ["high", "low", "close"], "func": f29_uarn_249_adxr_with_choppiness_low_trend_health},
    "f29_uarn_250_uo_oversold_with_di_minus_rising_failure": {"inputs": ["high", "low", "close"], "func": f29_uarn_250_uo_oversold_with_di_minus_rising_failure},
    "f29_uarn_251_choppiness_rising_with_mass_bulge_transition": {"inputs": ["high", "low", "close"], "func": f29_uarn_251_choppiness_rising_with_mass_bulge_transition},
    "f29_uarn_252_trend_health_composite_score": {"inputs": ["high", "low", "close"], "func": f29_uarn_252_trend_health_composite_score},
    "f29_uarn_253_bearish_trend_health_composite_score": {"inputs": ["high", "low", "close"], "func": f29_uarn_253_bearish_trend_health_composite_score},
    "f29_uarn_254_vortex_bear_cross_with_adxr_above_25": {"inputs": ["high", "low", "close"], "func": f29_uarn_254_vortex_bear_cross_with_adxr_above_25},
    "f29_uarn_255_aroon_up_collapse_with_vortex_bear_cross": {"inputs": ["high", "low", "close"], "func": f29_uarn_255_aroon_up_collapse_with_vortex_bear_cross},
    "f29_uarn_256_dx_above_50_extreme_imbalance": {"inputs": ["high", "low", "close"], "func": f29_uarn_256_dx_above_50_extreme_imbalance},
    "f29_uarn_257_mass_bulge_with_di_minus_dominant": {"inputs": ["high", "low", "close"], "func": f29_uarn_257_mass_bulge_with_di_minus_dominant},
    "f29_uarn_258_uo_falling_with_aroon_down_rising": {"inputs": ["high", "low", "close"], "func": f29_uarn_258_uo_falling_with_aroon_down_rising},
    "f29_uarn_259_adxr_falling_with_vortex_bear_dominant": {"inputs": ["high", "low", "close"], "func": f29_uarn_259_adxr_falling_with_vortex_bear_dominant},
    "f29_uarn_260_choppiness_low_with_di_balance_negative": {"inputs": ["high", "low", "close"], "func": f29_uarn_260_choppiness_low_with_di_balance_negative},
    "f29_uarn_261_vortex_diff_below_zero_with_aroon_down_above_70": {"inputs": ["high", "low"], "func": f29_uarn_261_vortex_diff_below_zero_with_aroon_down_above_70},
    "f29_uarn_262_aroon_oscillator_with_di_balance_sign_agreement": {"inputs": ["high", "low", "close"], "func": f29_uarn_262_aroon_oscillator_with_di_balance_sign_agreement},
    "f29_uarn_263_uo_with_adxr_strong_bearish_combo": {"inputs": ["high", "low", "close"], "func": f29_uarn_263_uo_with_adxr_strong_bearish_combo},
    "f29_uarn_264_mass_bulge_with_choppiness_breakout": {"inputs": ["high", "low", "close"], "func": f29_uarn_264_mass_bulge_with_choppiness_breakout},
    "f29_uarn_265_vortex_diff_with_adx_disagreement": {"inputs": ["high", "low", "close"], "func": f29_uarn_265_vortex_diff_with_adx_disagreement},
    "f29_uarn_266_bars_since_last_di_cross": {"inputs": ["high", "low", "close"], "func": f29_uarn_266_bars_since_last_di_cross},
    "f29_uarn_267_bars_since_last_vortex_cross": {"inputs": ["high", "low", "close"], "func": f29_uarn_267_bars_since_last_vortex_cross},
    "f29_uarn_268_bars_since_last_adx_peak_above_40": {"inputs": ["high", "low", "close"], "func": f29_uarn_268_bars_since_last_adx_peak_above_40},
    "f29_uarn_269_bars_since_last_mass_bulge_above_27": {"inputs": ["high", "low"], "func": f29_uarn_269_bars_since_last_mass_bulge_above_27},
    "f29_uarn_270_bars_since_last_aroon_osc_zero_cross": {"inputs": ["high", "low"], "func": f29_uarn_270_bars_since_last_aroon_osc_zero_cross},
    "f29_uarn_271_bars_since_last_uo_above_80": {"inputs": ["high", "low", "close"], "func": f29_uarn_271_bars_since_last_uo_above_80},
    "f29_uarn_272_bars_since_last_uo_below_20": {"inputs": ["high", "low", "close"], "func": f29_uarn_272_bars_since_last_uo_below_20},
    "f29_uarn_273_bars_since_last_di_minus_above_30": {"inputs": ["high", "low", "close"], "func": f29_uarn_273_bars_since_last_di_minus_above_30},
    "f29_uarn_274_bars_since_last_di_plus_above_30": {"inputs": ["high", "low", "close"], "func": f29_uarn_274_bars_since_last_di_plus_above_30},
    "f29_uarn_275_bars_since_last_choppiness_below_30": {"inputs": ["high", "low", "close"], "func": f29_uarn_275_bars_since_last_choppiness_below_30},
    "f29_uarn_276_bars_since_last_aroon_down_100": {"inputs": ["low"], "func": f29_uarn_276_bars_since_last_aroon_down_100},
    "f29_uarn_277_bars_since_last_vortex_diff_extreme_pos": {"inputs": ["high", "low", "close"], "func": f29_uarn_277_bars_since_last_vortex_diff_extreme_pos},
    "f29_uarn_278_bars_since_last_vortex_diff_extreme_neg": {"inputs": ["high", "low", "close"], "func": f29_uarn_278_bars_since_last_vortex_diff_extreme_neg},
    "f29_uarn_279_bars_since_last_adx_below_15_reset": {"inputs": ["high", "low", "close"], "func": f29_uarn_279_bars_since_last_adx_below_15_reset},
    "f29_uarn_280_bars_since_last_di_plus_above_di_minus": {"inputs": ["high", "low", "close"], "func": f29_uarn_280_bars_since_last_di_plus_above_di_minus},
    "f29_uarn_281_fraction_di_minus_dominant_252d": {"inputs": ["high", "low", "close"], "func": f29_uarn_281_fraction_di_minus_dominant_252d},
    "f29_uarn_282_count_di_crossovers_252d": {"inputs": ["high", "low", "close"], "func": f29_uarn_282_count_di_crossovers_252d},
    "f29_uarn_283_count_vortex_crossovers_252d": {"inputs": ["high", "low", "close"], "func": f29_uarn_283_count_vortex_crossovers_252d},
    "f29_uarn_284_fraction_adx_above_25_252d": {"inputs": ["high", "low", "close"], "func": f29_uarn_284_fraction_adx_above_25_252d},
    "f29_uarn_285_fraction_aroon_up_above_70_252d": {"inputs": ["high"], "func": f29_uarn_285_fraction_aroon_up_above_70_252d},
    "f29_uarn_286_fraction_aroon_down_above_70_252d": {"inputs": ["low"], "func": f29_uarn_286_fraction_aroon_down_above_70_252d},
    "f29_uarn_287_fraction_mass_above_27_252d": {"inputs": ["high", "low"], "func": f29_uarn_287_fraction_mass_above_27_252d},
    "f29_uarn_288_fraction_uo_above_70_252d": {"inputs": ["high", "low", "close"], "func": f29_uarn_288_fraction_uo_above_70_252d},
    "f29_uarn_289_fraction_vortex_bull_504d": {"inputs": ["high", "low", "close"], "func": f29_uarn_289_fraction_vortex_bull_504d},
    "f29_uarn_290_count_aroon_up_at_100_252d": {"inputs": ["high"], "func": f29_uarn_290_count_aroon_up_at_100_252d},
    "f29_uarn_291_adxr_504d_horizon": {"inputs": ["high", "low", "close"], "func": f29_uarn_291_adxr_504d_horizon},
    "f29_uarn_292_aroon_oscillator_756d_3y_horizon": {"inputs": ["high", "low"], "func": f29_uarn_292_aroon_oscillator_756d_3y_horizon},
    "f29_uarn_293_choppiness_252d_annual_regime": {"inputs": ["high", "low", "close"], "func": f29_uarn_293_choppiness_252d_annual_regime},
    "f29_uarn_294_mass_index_100d_horizon": {"inputs": ["high", "low"], "func": f29_uarn_294_mass_index_100d_horizon},
    "f29_uarn_295_vortex_diff_long_50d_to_short_14d_ratio": {"inputs": ["high", "low", "close"], "func": f29_uarn_295_vortex_diff_long_50d_to_short_14d_ratio},
    "f29_uarn_296_adx_504d_horizon": {"inputs": ["high", "low", "close"], "func": f29_uarn_296_adx_504d_horizon},
    "f29_uarn_297_aroon_up_minus_down_at_log_close_252d": {"inputs": ["close"], "func": f29_uarn_297_aroon_up_minus_down_at_log_close_252d},
    "f29_uarn_298_adxr_minus_adxr_long_horizon_spread": {"inputs": ["high", "low", "close"], "func": f29_uarn_298_adxr_minus_adxr_long_horizon_spread},
    "f29_uarn_299_aroon_oscillator_100d_minus_25d": {"inputs": ["high", "low"], "func": f29_uarn_299_aroon_oscillator_100d_minus_25d},
    "f29_uarn_300_composite_uarn_long_horizon_bearish_score": {"inputs": ["high", "low", "close"], "func": f29_uarn_300_composite_uarn_long_horizon_bearish_score},
}
