"""ultimate_aroon_vortex d2 features 076-150 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __base__001_075.py. Family theme:
Ultimate Oscillator, Aroon (Up/Down/Osc), Vortex (VI+/VI-), ADX/DI+/DI-,
Choppiness Index, Mass Index, and composite cross-indicator events.

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
    """Wilder's smoothing: EMA with alpha = 1/n."""
    return s.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()


# ---------------------------- indicator primitives ----------------------------

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


def _dm_components(high, low, close, n=14):
    up = high.diff()
    dn = -low.diff()
    plus_dm = np.where((up > dn) & (up > 0), up, 0.0)
    minus_dm = np.where((dn > up) & (dn > 0), dn, 0.0)
    plus_dm = pd.Series(plus_dm, index=high.index)
    minus_dm = pd.Series(minus_dm, index=high.index)
    tr = _true_range(high, low, close)
    atr = _wilder_ema(tr, n)
    plus_di = 100.0 * _safe_div(_wilder_ema(plus_dm, n), atr)
    minus_di = 100.0 * _safe_div(_wilder_ema(minus_dm, n), atr)
    dx = 100.0 * _safe_div((plus_di - minus_di).abs(), (plus_di + minus_di))
    adx = _wilder_ema(dx, n)
    return plus_di, minus_di, adx


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


# ============================================================
# Bucket D continued — ADX / DI+ / DI- (076-080)
# ============================================================

def f29_uarn_076_adx_dwell_above_40_in_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars in trailing 63d with ADX(14) > 40 — extreme-trend dwell time (exhaustion fuel)."""
    _, _, adx = _dm_components(high, low, close, n=14)
    above = (adx > 40.0).astype(float)
    return (above.rolling(QDAYS, min_periods=MDAYS).sum()).diff().diff()


def f29_uarn_077_adx_long_minus_short_horizon_spread_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ADX(14) − ADX(25): short vs slow trend strength differential — short-leading-slow signal."""
    _, _, adx14 = _dm_components(high, low, close, n=14)
    _, _, adx25 = _dm_components(high, low, close, n=25)
    return (adx14 - adx25).diff().diff()


def f29_uarn_078_di_plus_dominance_streak_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Consecutive-bar streak of DI+(14) > DI−(14) — bullish-regime persistence length."""
    plus_di, minus_di, _ = _dm_components(high, low, close, n=14)
    pos = (plus_di > minus_di).astype(float).values
    n = len(pos)
    out = np.full(n, np.nan, dtype=float)
    streak = 0
    for i in range(n):
        if pd.isna(plus_di.iat[i]) or pd.isna(minus_di.iat[i]):
            streak = 0
            out[i] = np.nan
        else:
            streak = streak + 1 if pos[i] > 0 else 0
            out[i] = float(streak)
    return (pd.Series(out, index=plus_di.index)).diff().diff()


def f29_uarn_079_di_balance_zero_crossings_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of DI+(14) − DI−(14) zero crossings in trailing 63d — regime-flip cadence."""
    plus_di, minus_di, _ = _dm_components(high, low, close, n=14)
    sign = np.sign((plus_di - minus_di).fillna(0.0))
    flips = (sign != sign.shift(1)).astype(float)
    flips.iloc[0] = 0.0
    return (flips.rolling(QDAYS, min_periods=MDAYS).sum()).diff().diff()


def f29_uarn_080_di_minus_zscore_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of DI−(14) in 252d window — anomalously hot bearish-DM reading."""
    _, minus_di, _ = _dm_components(high, low, close, n=14)
    return (_rolling_zscore(minus_di, YDAYS, min_periods=QDAYS)).diff().diff()


# ============================================================
# Bucket E — Choppiness Index (081-095)
# ============================================================

def f29_uarn_081_choppiness_14d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Choppiness Index (14) — short-horizon trending vs ranging regime measure."""
    return (_choppiness(high, low, close, n=14)).diff().diff()


def f29_uarn_082_choppiness_25d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Choppiness Index (25) — classic monthly-horizon variant."""
    return (_choppiness(high, low, close, n=25)).diff().diff()


def f29_uarn_083_choppiness_50d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Choppiness Index (50) — long-horizon regime-classification variant."""
    return (_choppiness(high, low, close, n=50)).diff().diff()


def f29_uarn_084_choppiness_below_38_trending_indicator_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: Choppiness(14) < 38.2 — strongly-trending regime."""
    ci = _choppiness(high, low, close, n=14)
    return ((ci < 38.2).astype(float).where(ci.notna(), np.nan)).diff().diff()


def f29_uarn_085_choppiness_above_62_ranging_indicator_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: Choppiness(14) > 61.8 — strongly-ranging regime."""
    ci = _choppiness(high, low, close, n=14)
    return ((ci > 61.8).astype(float).where(ci.notna(), np.nan)).diff().diff()


def f29_uarn_086_choppiness_trending_dwell_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars in trailing 63d with Choppiness(14) < 38.2 — sustained-trending dwell."""
    ci = _choppiness(high, low, close, n=14)
    cond = (ci < 38.2).astype(float)
    return (cond.rolling(QDAYS, min_periods=MDAYS).sum()).diff().diff()


def f29_uarn_087_choppiness_ranging_dwell_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars in trailing 63d with Choppiness(14) > 61.8 — sustained-ranging dwell."""
    ci = _choppiness(high, low, close, n=14)
    cond = (ci > 61.8).astype(float)
    return (cond.rolling(QDAYS, min_periods=MDAYS).sum()).diff().diff()


def f29_uarn_088_choppiness_zscore_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of Choppiness(14) in 252d window — anomalous regime reading."""
    ci = _choppiness(high, low, close, n=14)
    return (_rolling_zscore(ci, YDAYS, min_periods=QDAYS)).diff().diff()


def f29_uarn_089_choppiness_amplitude_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63d max − min of Choppiness(14) — regime-oscillation amplitude."""
    ci = _choppiness(high, low, close, n=14)
    return (ci.rolling(QDAYS, min_periods=MDAYS).max() - ci.rolling(QDAYS, min_periods=MDAYS).min()).diff().diff()


def f29_uarn_090_choppiness_minimum_in_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Minimum Choppiness(14) value in trailing 63d — strongest-trend reading in quarter."""
    ci = _choppiness(high, low, close, n=14)
    return (ci.rolling(QDAYS, min_periods=MDAYS).min()).diff().diff()


def f29_uarn_091_choppiness_trend_to_range_transition_event_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: Choppiness(14) crossed up through 50 today (trending → choppy transition)."""
    ci = _choppiness(high, low, close, n=14)
    cond = (ci.shift(1) <= 50.0) & (ci > 50.0)
    return (cond.astype(float).where(ci.notna() & ci.shift(1).notna(), np.nan)).diff().diff()


def f29_uarn_092_choppiness_slope_21d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21d slope of Choppiness(14) — regime-direction velocity."""
    ci = _choppiness(high, low, close, n=14)
    return (_rolling_slope(ci, MDAYS)).diff().diff()


def f29_uarn_093_choppiness_short_minus_long_horizon_spread_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Choppiness(14) − Choppiness(50): short vs long-horizon regime spread."""
    return (_choppiness(high, low, close, n=14) - _choppiness(high, low, close, n=50)).diff().diff()


def f29_uarn_094_choppiness_bars_since_last_trending_below_38_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since Choppiness(14) was last below 38.2 — staleness of trending regime."""
    ci = _choppiness(high, low, close, n=14)
    below = (ci < 38.2).astype(float)
    def _bsm(w):
        idx = np.where(w > 0)[0]
        if idx.size == 0:
            return float(len(w))
        return float((len(w) - 1) - idx[-1])
    return (below.rolling(YDAYS, min_periods=MDAYS).apply(_bsm, raw=True)).diff().diff()


def f29_uarn_095_choppiness_volatility_21d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21d std-dev of Choppiness(14) — regime-instability measure."""
    ci = _choppiness(high, low, close, n=14)
    return (ci.rolling(MDAYS, min_periods=WDAYS).std()).diff().diff()


# ============================================================
# Bucket F — Mass Index (096-105)
# ============================================================

def f29_uarn_096_mass_index_classic_25d_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Mass Index (25, ema9): classic reversal-bulge measure."""
    return (_mass_index(high, low, n=25, ema_n=9)).diff().diff()


def f29_uarn_097_mass_index_reversal_bulge_indicator_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Indicator: Mass Index > 27 — Donald Dorsey reversal-bulge trigger."""
    mi = _mass_index(high, low, n=25, ema_n=9)
    return ((mi > 27.0).astype(float).where(mi.notna(), np.nan)).diff().diff()


def f29_uarn_098_mass_index_bulge_and_drop_below_265_event_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Event: MI exceeded 27 within last 21 bars and is now below 26.5 — classic Dorsey reversal."""
    mi = _mass_index(high, low, n=25, ema_n=9)
    bulge = (mi.rolling(MDAYS, min_periods=WDAYS).max() > 27.0)
    cond = bulge & (mi < 26.5)
    return (cond.astype(float).where(mi.notna(), np.nan)).diff().diff()


def f29_uarn_099_mass_index_distance_from_25_mean_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Mass Index minus its trailing 252d mean — anomaly vs personal baseline."""
    mi = _mass_index(high, low, n=25, ema_n=9)
    return (mi - mi.rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff()


def f29_uarn_100_mass_index_zscore_252d_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of Mass Index in 252d window — anomalous-range-expansion reading."""
    mi = _mass_index(high, low, n=25, ema_n=9)
    return (_rolling_zscore(mi, YDAYS, min_periods=QDAYS)).diff().diff()


def f29_uarn_101_mass_index_amplitude_63d_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """63d max − min of Mass Index — range-expansion oscillation amplitude."""
    mi = _mass_index(high, low, n=25, ema_n=9)
    return (mi.rolling(QDAYS, min_periods=MDAYS).max() - mi.rolling(QDAYS, min_periods=MDAYS).min()).diff().diff()


def f29_uarn_102_mass_index_short_horizon_15d_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Mass Index (15, ema9) — faster reversal-bulge sensor for shorter setups."""
    return (_mass_index(high, low, n=15, ema_n=9)).diff().diff()


def f29_uarn_103_mass_index_above_27_dwell_63d_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars in trailing 63d with MI > 27 — sustained-bulge dwell time."""
    mi = _mass_index(high, low, n=25, ema_n=9)
    cond = (mi > 27.0).astype(float)
    return (cond.rolling(QDAYS, min_periods=MDAYS).sum()).diff().diff()


def f29_uarn_104_mass_index_rate_of_change_5d_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """5d ROC of Mass Index — range-expansion acceleration."""
    mi = _mass_index(high, low, n=25, ema_n=9)
    return (mi - mi.shift(WDAYS)).diff().diff()


def f29_uarn_105_mass_index_at_252d_high_value_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """At bars where high == 252d max, value of MI(25) — range-expansion at the peak."""
    mi = _mass_index(high, low, n=25, ema_n=9)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = (high >= rmax)
    return (mi.where(at_peak, np.nan)).diff().diff()


# ============================================================
# Bucket G — Composite / cross-indicator events (106-130)
# ============================================================

def f29_uarn_106_adx_rising_and_uo_overbought_composite_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite: ADX(14) rising AND UO > 70 — strengthening trend with overbought reading."""
    _, _, adx = _dm_components(high, low, close, n=14)
    uo = _ultimate_osc(high, low, close, 7, 14, 28)
    cond = (adx.diff() > 0) & (uo > 70.0)
    return (cond.astype(float).where(adx.notna() & uo.notna(), np.nan)).diff().diff()


def f29_uarn_107_vortex_bearish_cross_with_di_minus_dominant_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: Vortex bearish cross (VI− > VI+) AND DI−(14) > DI+(14) — double bearish confirmation."""
    vp, vm = _vortex(high, low, close, n=14)
    plus_di, minus_di, _ = _dm_components(high, low, close, n=14)
    vortex_bear = (vm > vp) & (vm.shift(1) <= vp.shift(1))
    cond = vortex_bear & (minus_di > plus_di)
    return (cond.astype(float).where(vp.notna() & plus_di.notna(), np.nan)).diff().diff()


def f29_uarn_108_choppy_to_trend_with_adx_above_25_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite: Choppiness(14) < 38.2 AND ADX(14) > 25 — confirmed strong-trend regime."""
    ci = _choppiness(high, low, close, n=14)
    _, _, adx = _dm_components(high, low, close, n=14)
    cond = (ci < 38.2) & (adx > 25.0)
    return (cond.astype(float).where(ci.notna() & adx.notna(), np.nan)).diff().diff()


def f29_uarn_109_aroon_osc_falling_with_di_minus_rising_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite: Aroon-Osc(25) falling AND DI−(14) rising — bearish-momentum build."""
    osc = _aroon_up(high, 25) - _aroon_down(low, 25)
    _, minus_di, _ = _dm_components(high, low, close, n=14)
    cond = (osc.diff() < 0) & (minus_di.diff() > 0)
    return (cond.astype(float).where(osc.notna() & minus_di.notna(), np.nan)).diff().diff()


def f29_uarn_110_mass_index_bulge_with_close_below_ma21_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite: MI > 27 AND close < 21d SMA — range expansion with breakdown."""
    mi = _mass_index(high, low, n=25, ema_n=9)
    ma21 = close.rolling(MDAYS, min_periods=WDAYS).mean()
    cond = (mi > 27.0) & (close < ma21)
    return (cond.astype(float).where(mi.notna() & ma21.notna(), np.nan)).diff().diff()


def f29_uarn_111_multi_indicator_bearish_alignment_count_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bearish indicators currently active: {UO>70, Aroon-Osc<0, VI−>VI+, DI−>DI+, MI>27}."""
    uo = _ultimate_osc(high, low, close, 7, 14, 28)
    osc = _aroon_up(high, 25) - _aroon_down(low, 25)
    vp, vm = _vortex(high, low, close, n=14)
    plus_di, minus_di, _ = _dm_components(high, low, close, n=14)
    mi = _mass_index(high, low, n=25, ema_n=9)
    pieces = [
        (uo > 70.0).astype(float).rename("uo"),
        (osc < 0).astype(float).rename("ar"),
        (vm > vp).astype(float).rename("vx"),
        (minus_di > plus_di).astype(float).rename("di"),
        (mi > 27.0).astype(float).rename("mi"),
    ]
    return (pd.concat(pieces, axis=1).sum(axis=1)).diff().diff()


def f29_uarn_112_uo_overbought_with_aroon_up_at_100_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite: UO > 80 AND Aroon-Up(25) = 100 — peak-extension confluence."""
    uo = _ultimate_osc(high, low, close, 7, 14, 28)
    au = _aroon_up(high, 25)
    cond = (uo > 80.0) & (au >= 99.999)
    return (cond.astype(float).where(uo.notna() & au.notna(), np.nan)).diff().diff()


def f29_uarn_113_adx_above_40_with_vortex_bearish_cross_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite: ADX(14) > 40 AND VI− crossed above VI+ today — extreme-trend reversal trigger."""
    _, _, adx = _dm_components(high, low, close, n=14)
    vp, vm = _vortex(high, low, close, n=14)
    cross = (vm > vp) & (vm.shift(1) <= vp.shift(1))
    cond = (adx > 40.0) & cross
    return (cond.astype(float).where(adx.notna() & vp.notna() & vm.notna(), np.nan)).diff().diff()


def f29_uarn_114_uo_below_50_with_di_minus_above_30_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite: UO < 50 AND DI−(14) > 30 — bearish-momentum + bearish-DM alignment."""
    uo = _ultimate_osc(high, low, close, 7, 14, 28)
    _, minus_di, _ = _dm_components(high, low, close, n=14)
    cond = (uo < 50.0) & (minus_di > 30.0)
    return (cond.astype(float).where(uo.notna() & minus_di.notna(), np.nan)).diff().diff()


def f29_uarn_115_choppy_squeeze_with_mass_index_bulge_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite: Choppiness(14) > 61.8 AND MI > 27 — range-bound regime with bulge (breakout primer)."""
    ci = _choppiness(high, low, close, n=14)
    mi = _mass_index(high, low, n=25, ema_n=9)
    cond = (ci > 61.8) & (mi > 27.0)
    return (cond.astype(float).where(ci.notna() & mi.notna(), np.nan)).diff().diff()


def f29_uarn_116_aroon_collapse_with_uo_failure_swing_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite: Aroon-Up(25) dropped from 100 in last 5 bars AND UO failure swing today."""
    au = _aroon_up(high, 25)
    recent_peak = (au.rolling(WDAYS, min_periods=2).max() >= 99.999)
    uo = _ultimate_osc(high, low, close, 7, 14, 28)
    prior_max = uo.rolling(14, min_periods=5).max().shift(1)
    prior_min = uo.rolling(14, min_periods=5).min().shift(1)
    fs = (prior_max > 70.0) & (uo < prior_min)
    cond = recent_peak.shift(1).fillna(False) & (au < 70.0) & fs
    return (cond.astype(float).where(au.notna() & uo.notna(), np.nan)).diff().diff()


def f29_uarn_117_count_overbought_signals_active_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of overbought conditions active: {UO>70, Aroon-Up(25)>=80, ADX>25 & DI+>DI−, VI+>1.1}."""
    uo = _ultimate_osc(high, low, close, 7, 14, 28)
    au = _aroon_up(high, 25)
    plus_di, minus_di, adx = _dm_components(high, low, close, n=14)
    vp, _ = _vortex(high, low, close, n=14)
    pieces = [
        (uo > 70.0).astype(float).rename("uo"),
        (au >= 80.0).astype(float).rename("au"),
        ((adx > 25.0) & (plus_di > minus_di)).astype(float).rename("ad"),
        (vp > 1.1).astype(float).rename("vp"),
    ]
    return (pd.concat(pieces, axis=1).sum(axis=1)).diff().diff()


def f29_uarn_118_first_di_minus_dominance_after_63d_di_plus_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: first DI−>DI+ flip after 63 consecutive bars of DI+>DI− — regime-end signal."""
    plus_di, minus_di, _ = _dm_components(high, low, close, n=14)
    bull_dwell = (plus_di > minus_di).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    cross = (minus_di > plus_di) & (minus_di.shift(1) <= plus_di.shift(1))
    cond = cross & (bull_dwell.shift(1) >= QDAYS - 1)
    return (cond.astype(float).where(plus_di.notna() & minus_di.notna(), np.nan)).diff().diff()


def f29_uarn_119_aroon_dn_above_aroon_up_at_252d_high_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """At bars where high == 252d max, indicator that Aroon-Down(25) > Aroon-Up(25) — bearish divergence at peak."""
    au = _aroon_up(high, 25)
    ad = _aroon_down(low, 25)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = (high >= rmax)
    val = (ad > au).astype(float)
    return (val.where(at_peak & au.notna() & ad.notna(), np.nan)).diff().diff()


def f29_uarn_120_uo_at_252d_high_value_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """At bars where high == 252d max, value of UO — overbought reading right at the peak."""
    uo = _ultimate_osc(high, low, close, 7, 14, 28)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = (high >= rmax)
    return (uo.where(at_peak, np.nan)).diff().diff()


def f29_uarn_121_choppiness_below_30_with_di_minus_dominant_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite: Choppiness(14) < 30 AND DI−>DI+ — strong-trend down regime."""
    ci = _choppiness(high, low, close, n=14)
    plus_di, minus_di, _ = _dm_components(high, low, close, n=14)
    cond = (ci < 30.0) & (minus_di > plus_di)
    return (cond.astype(float).where(ci.notna() & plus_di.notna(), np.nan)).diff().diff()


def f29_uarn_122_vortex_diff_neg_with_adx_rising_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite: Vortex-diff(14) < 0 AND ADX(14) rising — bearish trend strengthening."""
    vp, vm = _vortex(high, low, close, n=14)
    _, _, adx = _dm_components(high, low, close, n=14)
    cond = ((vp - vm) < 0) & (adx.diff() > 0)
    return (cond.astype(float).where(vp.notna() & adx.notna(), np.nan)).diff().diff()


def f29_uarn_123_mass_index_bulge_with_aroon_down_above_70_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Composite: MI > 27 AND Aroon-Down(25) > 70 — range expansion with bearish recency."""
    mi = _mass_index(high, low, n=25, ema_n=9)
    ad = _aroon_down(low, 25)
    cond = (mi > 27.0) & (ad > 70.0)
    return (cond.astype(float).where(mi.notna() & ad.notna(), np.nan)).diff().diff()


def f29_uarn_124_uo_dropped_below_50_after_above_80_event_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: UO crossed below 50 today AND was above 80 within last 21 bars — exhaustion-then-fail."""
    uo = _ultimate_osc(high, low, close, 7, 14, 28)
    recent_extreme = (uo.rolling(MDAYS, min_periods=WDAYS).max() > 80.0)
    cond = recent_extreme.shift(1).fillna(False) & (uo.shift(1) >= 50.0) & (uo < 50.0)
    return (cond.astype(float).where(uo.notna() & uo.shift(1).notna(), np.nan)).diff().diff()


def f29_uarn_125_adx_peak_then_fall_with_di_minus_take_over_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite: ADX peaked > 40 in last 21d, now falling, AND DI− crossed above DI+ today."""
    plus_di, minus_di, adx = _dm_components(high, low, close, n=14)
    recent_hot = (adx.rolling(MDAYS, min_periods=WDAYS).max() > 40.0)
    cross = (minus_di > plus_di) & (minus_di.shift(1) <= plus_di.shift(1))
    cond = recent_hot.shift(1).fillna(False) & (adx.diff() < 0) & cross
    return (cond.astype(float).where(adx.notna() & plus_di.notna(), np.nan)).diff().diff()


def f29_uarn_126_uo_short_long_negative_spread_with_di_minus_rising_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite: UO BP(7)−BP(28) < 0 (long-TF stronger than short) AND DI− rising."""
    pc = close.shift(1)
    bp = close - pd.concat([low, pc], axis=1).min(axis=1)
    tr = pd.concat([high, pc], axis=1).max(axis=1) - pd.concat([low, pc], axis=1).min(axis=1)
    a = _safe_div(bp.rolling(7, min_periods=3).sum(), tr.rolling(7, min_periods=3).sum())
    c = _safe_div(bp.rolling(28, min_periods=10).sum(), tr.rolling(28, min_periods=10).sum())
    spread = a - c
    _, minus_di, _ = _dm_components(high, low, close, n=14)
    cond = (spread < 0) & (minus_di.diff() > 0)
    return (cond.astype(float).where(spread.notna() & minus_di.notna(), np.nan)).diff().diff()


def f29_uarn_127_aroon_osc_collapsed_more_than_100_in_21d_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Indicator: Aroon-Osc(25) value 21 bars ago minus current value > 100 — collapse magnitude."""
    osc = _aroon_up(high, 25) - _aroon_down(low, 25)
    drop = osc.shift(MDAYS) - osc
    return ((drop > 100.0).astype(float).where(osc.notna() & osc.shift(MDAYS).notna(), np.nan)).diff().diff()


def f29_uarn_128_choppiness_breakout_event_above_60_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: Choppiness(14) crossed up through 61.8 today — ranging-regime onset."""
    ci = _choppiness(high, low, close, n=14)
    cond = (ci.shift(1) <= 61.8) & (ci > 61.8)
    return (cond.astype(float).where(ci.notna() & ci.shift(1).notna(), np.nan)).diff().diff()


def f29_uarn_129_uo_aroon_vortex_all_bearish_alignment_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: UO < 50 AND Aroon-Osc(25) < 0 AND VI− > VI+ — three-way bearish alignment."""
    uo = _ultimate_osc(high, low, close, 7, 14, 28)
    osc = _aroon_up(high, 25) - _aroon_down(low, 25)
    vp, vm = _vortex(high, low, close, n=14)
    cond = (uo < 50.0) & (osc < 0) & (vm > vp)
    return (cond.astype(float).where(uo.notna() & osc.notna() & vp.notna(), np.nan)).diff().diff()


def f29_uarn_130_composite_trend_exhaustion_score_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Score: ADX/100 * (UO−50)/50 — combined trend-strength-times-momentum-extension reading."""
    _, _, adx = _dm_components(high, low, close, n=14)
    uo = _ultimate_osc(high, low, close, 7, 14, 28)
    return ((adx / 100.0) * ((uo - 50.0) / 50.0)).diff().diff()


# ============================================================
# Bucket H — Multi-horizon spreads / dispersion (131-150)
# ============================================================

def f29_uarn_131_adx_14_minus_50_spread_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ADX(14) − ADX(50): short-horizon trend strength vs long-horizon — leading-lagging spread."""
    _, _, adx14 = _dm_components(high, low, close, n=14)
    _, _, adx50 = _dm_components(high, low, close, n=50)
    return (adx14 - adx50).diff().diff()


def f29_uarn_132_di_plus_14_minus_50_spread_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """DI+(14) − DI+(50): short vs long-horizon bullish-DM spread."""
    plus14, _, _ = _dm_components(high, low, close, n=14)
    plus50, _, _ = _dm_components(high, low, close, n=50)
    return (plus14 - plus50).diff().diff()


def f29_uarn_133_di_minus_14_minus_50_spread_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """DI−(14) − DI−(50): short vs long-horizon bearish-DM spread."""
    _, minus14, _ = _dm_components(high, low, close, n=14)
    _, minus50, _ = _dm_components(high, low, close, n=50)
    return (minus14 - minus50).diff().diff()


def f29_uarn_134_vortex_diff_14_minus_25_spread_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Vortex-diff(14) − Vortex-diff(25): short vs long-horizon directional spread."""
    vp14, vm14 = _vortex(high, low, close, n=14)
    vp25, vm25 = _vortex(high, low, close, n=25)
    return ((vp14 - vm14) - (vp25 - vm25)).diff().diff()


def f29_uarn_135_aroon_osc_dispersion_across_horizons_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Std-dev of Aroon-Osc across horizons {14, 25, 50} — cross-horizon directional agreement."""
    o14 = _aroon_up(high, 14) - _aroon_down(low, 14)
    o25 = _aroon_up(high, 25) - _aroon_down(low, 25)
    o50 = _aroon_up(high, 50) - _aroon_down(low, 50)
    df = pd.concat([o14.rename("o14"), o25.rename("o25"), o50.rename("o50")], axis=1)
    return (df.std(axis=1)).diff().diff()


def f29_uarn_136_choppiness_14_minus_50_spread_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Choppiness(14) − Choppiness(50): short vs long regime-classification spread."""
    return (_choppiness(high, low, close, n=14) - _choppiness(high, low, close, n=50)).diff().diff()


def f29_uarn_137_uo_minus_smoothed_uo_residual_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """UO − 21d-mean(UO): raw vs smoothed UO residual — momentum-jitter component."""
    uo = _ultimate_osc(high, low, close, 7, 14, 28)
    return (uo - uo.rolling(MDAYS, min_periods=WDAYS).mean()).diff().diff()


def f29_uarn_138_aroon_up_14_minus_252_spread_d2(high: pd.Series) -> pd.Series:
    """Aroon-Up(14) − Aroon-Up(252): short vs annual recency-of-high spread."""
    return (_aroon_up(high, 14) - _aroon_up(high, 252)).diff().diff()


def f29_uarn_139_aroon_down_14_minus_252_spread_d2(low: pd.Series) -> pd.Series:
    """Aroon-Down(14) − Aroon-Down(252): short vs annual recency-of-low spread."""
    return (_aroon_down(low, 14) - _aroon_down(low, 252)).diff().diff()


def f29_uarn_140_di_balance_14_minus_50_spread_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(DI+−DI−)(14) − (DI+−DI−)(50): short vs long directional-balance spread."""
    p14, m14, _ = _dm_components(high, low, close, n=14)
    p50, m50, _ = _dm_components(high, low, close, n=50)
    return ((p14 - m14) - (p50 - m50)).diff().diff()


def f29_uarn_141_mass_index_25_minus_15_spread_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Mass-Index(25) − Mass-Index(15): long vs short-horizon range-expansion spread."""
    return (_mass_index(high, low, n=25, ema_n=9) - _mass_index(high, low, n=15, ema_n=9)).diff().diff()


def f29_uarn_142_adx_horizon_dispersion_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Std-dev of ADX across horizons {14, 25, 50} — cross-horizon trend-strength agreement."""
    _, _, a14 = _dm_components(high, low, close, n=14)
    _, _, a25 = _dm_components(high, low, close, n=25)
    _, _, a50 = _dm_components(high, low, close, n=50)
    df = pd.concat([a14.rename("a14"), a25.rename("a25"), a50.rename("a50")], axis=1)
    return (df.std(axis=1)).diff().diff()


def f29_uarn_143_vortex_plus_horizon_dispersion_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Std-dev of VI+ across horizons {14, 25, 50} — cross-horizon bullish-vortex agreement."""
    vp14, _ = _vortex(high, low, close, n=14)
    vp25, _ = _vortex(high, low, close, n=25)
    vp50, _ = _vortex(high, low, close, n=50)
    df = pd.concat([vp14.rename("v14"), vp25.rename("v25"), vp50.rename("v50")], axis=1)
    return (df.std(axis=1)).diff().diff()


def f29_uarn_144_choppiness_horizon_max_minus_min_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Max − min of Choppiness across horizons {14, 25, 50} — regime-classification dispersion."""
    c14 = _choppiness(high, low, close, n=14)
    c25 = _choppiness(high, low, close, n=25)
    c50 = _choppiness(high, low, close, n=50)
    df = pd.concat([c14.rename("c14"), c25.rename("c25"), c50.rename("c50")], axis=1)
    return (df.max(axis=1) - df.min(axis=1)).diff().diff()


def f29_uarn_145_di_minus_horizon_dispersion_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Std-dev of DI− across horizons {14, 25, 50} — cross-horizon bearish-DM agreement."""
    _, m14, _ = _dm_components(high, low, close, n=14)
    _, m25, _ = _dm_components(high, low, close, n=25)
    _, m50, _ = _dm_components(high, low, close, n=50)
    df = pd.concat([m14.rename("m14"), m25.rename("m25"), m50.rename("m50")], axis=1)
    return (df.std(axis=1)).diff().diff()


def f29_uarn_146_aroon_up_minus_down_long_horizon_minus_short_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Aroon-Osc(50) − Aroon-Osc(14): long-horizon directional bias minus short-horizon."""
    o14 = _aroon_up(high, 14) - _aroon_down(low, 14)
    o50 = _aroon_up(high, 50) - _aroon_down(low, 50)
    return (o50 - o14).diff().diff()


def f29_uarn_147_vortex_diff_horizon_agreement_signed_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sign-product of Vortex-diff(14) * Vortex-diff(50) — +1 = horizons agree, -1 = disagree."""
    vp14, vm14 = _vortex(high, low, close, n=14)
    vp50, vm50 = _vortex(high, low, close, n=50)
    s1 = np.sign(vp14 - vm14)
    s2 = np.sign(vp50 - vm50)
    return (s1 * s2).diff().diff()


def f29_uarn_148_adx_to_choppiness_ratio_14d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ADX(14) / Choppiness(14) — trend-strength normalized by regime classification (high = strong-trend)."""
    _, _, adx = _dm_components(high, low, close, n=14)
    ci = _choppiness(high, low, close, n=14)
    return (_safe_div(adx, ci)).diff().diff()


def f29_uarn_149_aroon_up_long_horizon_decay_indicator_d2(high: pd.Series) -> pd.Series:
    """Indicator: Aroon-Up(252) > 80 AND Aroon-Up(14) < 30 — long-term peak with fresh decay."""
    a252 = _aroon_up(high, 252)
    a14 = _aroon_up(high, 14)
    cond = (a252 > 80.0) & (a14 < 30.0)
    return (cond.astype(float).where(a252.notna() & a14.notna(), np.nan)).diff().diff()


def f29_uarn_150_composite_uarn_bearish_score_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite bearish score: normalized sum of (DI−−DI+)/100 + (50−UO)/50 + (Aroon-Down−Aroon-Up)/100."""
    plus_di, minus_di, _ = _dm_components(high, low, close, n=14)
    uo = _ultimate_osc(high, low, close, 7, 14, 28)
    au = _aroon_up(high, 25)
    ad = _aroon_down(low, 25)
    a = (minus_di - plus_di) / 100.0
    b = (50.0 - uo) / 50.0
    c = (ad - au) / 100.0
    return ((a + b + c) / 3.0).diff().diff()


# ============================================================
#                         REGISTRY 076-150
# ============================================================

ULTIMATE_AROON_VORTEX_D2_REGISTRY_076_150 = {
    "f29_uarn_076_adx_dwell_above_40_in_63d_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_076_adx_dwell_above_40_in_63d_d2},
    "f29_uarn_077_adx_long_minus_short_horizon_spread_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_077_adx_long_minus_short_horizon_spread_d2},
    "f29_uarn_078_di_plus_dominance_streak_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_078_di_plus_dominance_streak_d2},
    "f29_uarn_079_di_balance_zero_crossings_63d_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_079_di_balance_zero_crossings_63d_d2},
    "f29_uarn_080_di_minus_zscore_252d_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_080_di_minus_zscore_252d_d2},
    "f29_uarn_081_choppiness_14d_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_081_choppiness_14d_d2},
    "f29_uarn_082_choppiness_25d_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_082_choppiness_25d_d2},
    "f29_uarn_083_choppiness_50d_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_083_choppiness_50d_d2},
    "f29_uarn_084_choppiness_below_38_trending_indicator_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_084_choppiness_below_38_trending_indicator_d2},
    "f29_uarn_085_choppiness_above_62_ranging_indicator_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_085_choppiness_above_62_ranging_indicator_d2},
    "f29_uarn_086_choppiness_trending_dwell_63d_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_086_choppiness_trending_dwell_63d_d2},
    "f29_uarn_087_choppiness_ranging_dwell_63d_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_087_choppiness_ranging_dwell_63d_d2},
    "f29_uarn_088_choppiness_zscore_252d_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_088_choppiness_zscore_252d_d2},
    "f29_uarn_089_choppiness_amplitude_63d_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_089_choppiness_amplitude_63d_d2},
    "f29_uarn_090_choppiness_minimum_in_63d_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_090_choppiness_minimum_in_63d_d2},
    "f29_uarn_091_choppiness_trend_to_range_transition_event_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_091_choppiness_trend_to_range_transition_event_d2},
    "f29_uarn_092_choppiness_slope_21d_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_092_choppiness_slope_21d_d2},
    "f29_uarn_093_choppiness_short_minus_long_horizon_spread_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_093_choppiness_short_minus_long_horizon_spread_d2},
    "f29_uarn_094_choppiness_bars_since_last_trending_below_38_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_094_choppiness_bars_since_last_trending_below_38_d2},
    "f29_uarn_095_choppiness_volatility_21d_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_095_choppiness_volatility_21d_d2},
    "f29_uarn_096_mass_index_classic_25d_d2": {"inputs": ["high", "low"], "func": f29_uarn_096_mass_index_classic_25d_d2},
    "f29_uarn_097_mass_index_reversal_bulge_indicator_d2": {"inputs": ["high", "low"], "func": f29_uarn_097_mass_index_reversal_bulge_indicator_d2},
    "f29_uarn_098_mass_index_bulge_and_drop_below_265_event_d2": {"inputs": ["high", "low"], "func": f29_uarn_098_mass_index_bulge_and_drop_below_265_event_d2},
    "f29_uarn_099_mass_index_distance_from_25_mean_d2": {"inputs": ["high", "low"], "func": f29_uarn_099_mass_index_distance_from_25_mean_d2},
    "f29_uarn_100_mass_index_zscore_252d_d2": {"inputs": ["high", "low"], "func": f29_uarn_100_mass_index_zscore_252d_d2},
    "f29_uarn_101_mass_index_amplitude_63d_d2": {"inputs": ["high", "low"], "func": f29_uarn_101_mass_index_amplitude_63d_d2},
    "f29_uarn_102_mass_index_short_horizon_15d_d2": {"inputs": ["high", "low"], "func": f29_uarn_102_mass_index_short_horizon_15d_d2},
    "f29_uarn_103_mass_index_above_27_dwell_63d_d2": {"inputs": ["high", "low"], "func": f29_uarn_103_mass_index_above_27_dwell_63d_d2},
    "f29_uarn_104_mass_index_rate_of_change_5d_d2": {"inputs": ["high", "low"], "func": f29_uarn_104_mass_index_rate_of_change_5d_d2},
    "f29_uarn_105_mass_index_at_252d_high_value_d2": {"inputs": ["high", "low"], "func": f29_uarn_105_mass_index_at_252d_high_value_d2},
    "f29_uarn_106_adx_rising_and_uo_overbought_composite_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_106_adx_rising_and_uo_overbought_composite_d2},
    "f29_uarn_107_vortex_bearish_cross_with_di_minus_dominant_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_107_vortex_bearish_cross_with_di_minus_dominant_d2},
    "f29_uarn_108_choppy_to_trend_with_adx_above_25_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_108_choppy_to_trend_with_adx_above_25_d2},
    "f29_uarn_109_aroon_osc_falling_with_di_minus_rising_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_109_aroon_osc_falling_with_di_minus_rising_d2},
    "f29_uarn_110_mass_index_bulge_with_close_below_ma21_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_110_mass_index_bulge_with_close_below_ma21_d2},
    "f29_uarn_111_multi_indicator_bearish_alignment_count_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_111_multi_indicator_bearish_alignment_count_d2},
    "f29_uarn_112_uo_overbought_with_aroon_up_at_100_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_112_uo_overbought_with_aroon_up_at_100_d2},
    "f29_uarn_113_adx_above_40_with_vortex_bearish_cross_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_113_adx_above_40_with_vortex_bearish_cross_d2},
    "f29_uarn_114_uo_below_50_with_di_minus_above_30_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_114_uo_below_50_with_di_minus_above_30_d2},
    "f29_uarn_115_choppy_squeeze_with_mass_index_bulge_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_115_choppy_squeeze_with_mass_index_bulge_d2},
    "f29_uarn_116_aroon_collapse_with_uo_failure_swing_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_116_aroon_collapse_with_uo_failure_swing_d2},
    "f29_uarn_117_count_overbought_signals_active_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_117_count_overbought_signals_active_d2},
    "f29_uarn_118_first_di_minus_dominance_after_63d_di_plus_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_118_first_di_minus_dominance_after_63d_di_plus_d2},
    "f29_uarn_119_aroon_dn_above_aroon_up_at_252d_high_d2": {"inputs": ["high", "low"], "func": f29_uarn_119_aroon_dn_above_aroon_up_at_252d_high_d2},
    "f29_uarn_120_uo_at_252d_high_value_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_120_uo_at_252d_high_value_d2},
    "f29_uarn_121_choppiness_below_30_with_di_minus_dominant_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_121_choppiness_below_30_with_di_minus_dominant_d2},
    "f29_uarn_122_vortex_diff_neg_with_adx_rising_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_122_vortex_diff_neg_with_adx_rising_d2},
    "f29_uarn_123_mass_index_bulge_with_aroon_down_above_70_d2": {"inputs": ["high", "low"], "func": f29_uarn_123_mass_index_bulge_with_aroon_down_above_70_d2},
    "f29_uarn_124_uo_dropped_below_50_after_above_80_event_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_124_uo_dropped_below_50_after_above_80_event_d2},
    "f29_uarn_125_adx_peak_then_fall_with_di_minus_take_over_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_125_adx_peak_then_fall_with_di_minus_take_over_d2},
    "f29_uarn_126_uo_short_long_negative_spread_with_di_minus_rising_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_126_uo_short_long_negative_spread_with_di_minus_rising_d2},
    "f29_uarn_127_aroon_osc_collapsed_more_than_100_in_21d_d2": {"inputs": ["high", "low"], "func": f29_uarn_127_aroon_osc_collapsed_more_than_100_in_21d_d2},
    "f29_uarn_128_choppiness_breakout_event_above_60_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_128_choppiness_breakout_event_above_60_d2},
    "f29_uarn_129_uo_aroon_vortex_all_bearish_alignment_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_129_uo_aroon_vortex_all_bearish_alignment_d2},
    "f29_uarn_130_composite_trend_exhaustion_score_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_130_composite_trend_exhaustion_score_d2},
    "f29_uarn_131_adx_14_minus_50_spread_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_131_adx_14_minus_50_spread_d2},
    "f29_uarn_132_di_plus_14_minus_50_spread_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_132_di_plus_14_minus_50_spread_d2},
    "f29_uarn_133_di_minus_14_minus_50_spread_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_133_di_minus_14_minus_50_spread_d2},
    "f29_uarn_134_vortex_diff_14_minus_25_spread_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_134_vortex_diff_14_minus_25_spread_d2},
    "f29_uarn_135_aroon_osc_dispersion_across_horizons_d2": {"inputs": ["high", "low"], "func": f29_uarn_135_aroon_osc_dispersion_across_horizons_d2},
    "f29_uarn_136_choppiness_14_minus_50_spread_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_136_choppiness_14_minus_50_spread_d2},
    "f29_uarn_137_uo_minus_smoothed_uo_residual_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_137_uo_minus_smoothed_uo_residual_d2},
    "f29_uarn_138_aroon_up_14_minus_252_spread_d2": {"inputs": ["high"], "func": f29_uarn_138_aroon_up_14_minus_252_spread_d2},
    "f29_uarn_139_aroon_down_14_minus_252_spread_d2": {"inputs": ["low"], "func": f29_uarn_139_aroon_down_14_minus_252_spread_d2},
    "f29_uarn_140_di_balance_14_minus_50_spread_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_140_di_balance_14_minus_50_spread_d2},
    "f29_uarn_141_mass_index_25_minus_15_spread_d2": {"inputs": ["high", "low"], "func": f29_uarn_141_mass_index_25_minus_15_spread_d2},
    "f29_uarn_142_adx_horizon_dispersion_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_142_adx_horizon_dispersion_d2},
    "f29_uarn_143_vortex_plus_horizon_dispersion_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_143_vortex_plus_horizon_dispersion_d2},
    "f29_uarn_144_choppiness_horizon_max_minus_min_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_144_choppiness_horizon_max_minus_min_d2},
    "f29_uarn_145_di_minus_horizon_dispersion_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_145_di_minus_horizon_dispersion_d2},
    "f29_uarn_146_aroon_up_minus_down_long_horizon_minus_short_d2": {"inputs": ["high", "low"], "func": f29_uarn_146_aroon_up_minus_down_long_horizon_minus_short_d2},
    "f29_uarn_147_vortex_diff_horizon_agreement_signed_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_147_vortex_diff_horizon_agreement_signed_d2},
    "f29_uarn_148_adx_to_choppiness_ratio_14d_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_148_adx_to_choppiness_ratio_14d_d2},
    "f29_uarn_149_aroon_up_long_horizon_decay_indicator_d2": {"inputs": ["high"], "func": f29_uarn_149_aroon_up_long_horizon_decay_indicator_d2},
    "f29_uarn_150_composite_uarn_bearish_score_d2": {"inputs": ["high", "low", "close"], "func": f29_uarn_150_composite_uarn_bearish_score_d2},
}
