"""ultimate_aroon_vortex base features 001-075 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __base__076_150.py. Family theme:
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
    """Williams' Ultimate Oscillator (0-100). Weighted blend of three TF BP/TR ratios."""
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
    """Aroon Up: 100 * (n - bars since max in window) / n."""
    def _f(w):
        if np.isnan(w).all():
            return np.nan
        idx = int(np.nanargmax(w))
        return 100.0 * (idx) / (len(w) - 1) if len(w) > 1 else np.nan
    return high.rolling(n + 1, min_periods=max((n + 1) // 2, 2)).apply(_f, raw=True)


def _aroon_down(low, n):
    """Aroon Down: 100 * (n - bars since min in window) / n."""
    def _f(w):
        if np.isnan(w).all():
            return np.nan
        idx = int(np.nanargmin(w))
        return 100.0 * (idx) / (len(w) - 1) if len(w) > 1 else np.nan
    return low.rolling(n + 1, min_periods=max((n + 1) // 2, 2)).apply(_f, raw=True)


def _vortex(high, low, close, n=14):
    """Returns (VI_plus, VI_minus)."""
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
    """Returns (DI_plus, DI_minus, ADX) Wilder-smoothed."""
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
    """Choppiness Index: 100 * log10(sum(ATR1)/(max-min)) / log10(n)."""
    tr = _true_range(high, low, close)
    sum_tr = tr.rolling(n, min_periods=max(n // 2, 2)).sum()
    hi = high.rolling(n, min_periods=max(n // 2, 2)).max()
    lo = low.rolling(n, min_periods=max(n // 2, 2)).min()
    ratio = _safe_div(sum_tr, hi - lo)
    return 100.0 * np.log10(ratio.where(ratio > 0, np.nan)) / np.log10(n)


def _mass_index(high, low, n=25, ema_n=9):
    """Mass Index: sum over n of (ema(range)/ema(ema(range)))."""
    rng = high - low
    e1 = rng.ewm(span=ema_n, adjust=False, min_periods=ema_n).mean()
    e2 = e1.ewm(span=ema_n, adjust=False, min_periods=ema_n).mean()
    r = _safe_div(e1, e2)
    return r.rolling(n, min_periods=max(n // 2, 2)).sum()


# ============================================================
# Bucket A — Ultimate Oscillator (001-015)
# ============================================================

def f29_uarn_001_ultimate_oscillator_classic(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Classic Ultimate Oscillator (7/14/28) — composite overbought/oversold."""
    return _ultimate_osc(high, low, close, 7, 14, 28)


def f29_uarn_002_uo_distance_above_70_overbought(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Distance of UO above the 70 overbought line (negative when below)."""
    uo = _ultimate_osc(high, low, close, 7, 14, 28)
    return uo - 70.0


def f29_uarn_003_uo_extreme_above_80_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: UO above the extreme 80 line."""
    uo = _ultimate_osc(high, low, close, 7, 14, 28)
    return (uo > 80.0).astype(float).where(uo.notna(), np.nan)


def f29_uarn_004_uo_dwell_above_70_in_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars in trailing 21d with UO above 70 — sustained overbought dwell."""
    uo = _ultimate_osc(high, low, close, 7, 14, 28)
    above = (uo > 70.0).astype(float)
    return above.rolling(MDAYS, min_periods=WDAYS).sum()


def f29_uarn_005_uo_distance_from_midline_50(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Signed distance of UO from neutral midline 50."""
    uo = _ultimate_osc(high, low, close, 7, 14, 28)
    return uo - 50.0


def f29_uarn_006_uo_short_timeframe_bp_ratio_7d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Short-TF buying-pressure ratio (BP_7/TR_7) — UO's fastest leg in isolation."""
    pc = close.shift(1)
    bp = close - pd.concat([low, pc], axis=1).min(axis=1)
    tr = pd.concat([high, pc], axis=1).max(axis=1) - pd.concat([low, pc], axis=1).min(axis=1)
    return _safe_div(bp.rolling(7, min_periods=3).sum(), tr.rolling(7, min_periods=3).sum())


def f29_uarn_007_uo_medium_timeframe_bp_ratio_14d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Medium-TF buying-pressure ratio (BP_14/TR_14) — classic ATR-horizon balance."""
    pc = close.shift(1)
    bp = close - pd.concat([low, pc], axis=1).min(axis=1)
    tr = pd.concat([high, pc], axis=1).max(axis=1) - pd.concat([low, pc], axis=1).min(axis=1)
    return _safe_div(bp.rolling(14, min_periods=5).sum(), tr.rolling(14, min_periods=5).sum())


def f29_uarn_008_uo_long_timeframe_bp_ratio_28d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Long-TF buying-pressure ratio (BP_28/TR_28) — monthly buying-pressure balance."""
    pc = close.shift(1)
    bp = close - pd.concat([low, pc], axis=1).min(axis=1)
    tr = pd.concat([high, pc], axis=1).max(axis=1) - pd.concat([low, pc], axis=1).min(axis=1)
    return _safe_div(bp.rolling(28, min_periods=10).sum(), tr.rolling(28, min_periods=10).sum())


def f29_uarn_009_uo_short_minus_long_tf_spread(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """BP/TR(7) − BP/TR(28): short-vs-long TF spread (front-loaded buying pressure)."""
    pc = close.shift(1)
    bp = close - pd.concat([low, pc], axis=1).min(axis=1)
    tr = pd.concat([high, pc], axis=1).max(axis=1) - pd.concat([low, pc], axis=1).min(axis=1)
    a = _safe_div(bp.rolling(7, min_periods=3).sum(), tr.rolling(7, min_periods=3).sum())
    c = _safe_div(bp.rolling(28, min_periods=10).sum(), tr.rolling(28, min_periods=10).sum())
    return a - c


def f29_uarn_010_uo_smoothed_5d_median(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5d-median-smoothed UO — denoised overbought signal."""
    uo = _ultimate_osc(high, low, close, 7, 14, 28)
    return uo.rolling(WDAYS, min_periods=2).median()


def f29_uarn_011_uo_exhaustion_distance_from_63d_max(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """UO minus its 63d trailing max — exhaustion from quarterly peak (<= 0)."""
    uo = _ultimate_osc(high, low, close, 7, 14, 28)
    return uo - uo.rolling(QDAYS, min_periods=MDAYS).max()


def f29_uarn_012_uo_failure_swing_bearish_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish UO failure swing: UO falls below prior 14d UO-trough after a 70+ peak."""
    uo = _ultimate_osc(high, low, close, 7, 14, 28)
    prior_max = uo.rolling(14, min_periods=5).max().shift(1)
    prior_min = uo.rolling(14, min_periods=5).min().shift(1)
    cond = (prior_max > 70.0) & (uo < prior_min)
    return cond.astype(float).where(uo.notna() & prior_min.notna(), np.nan)


def f29_uarn_013_uo_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of UO in trailing 252d distribution — anomalously hot/cold reading."""
    uo = _ultimate_osc(high, low, close, 7, 14, 28)
    return _rolling_zscore(uo, YDAYS, min_periods=QDAYS)


def f29_uarn_014_uo_bars_since_last_above_70(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since UO was last above the 70 line — staleness of overbought peak."""
    uo = _ultimate_osc(high, low, close, 7, 14, 28)
    above = (uo > 70.0).astype(float)
    def _bsm(w):
        idx = np.where(w > 0)[0]
        if idx.size == 0:
            return float(len(w))
        return float((len(w) - 1) - idx[-1])
    return above.rolling(YDAYS, min_periods=MDAYS).apply(_bsm, raw=True)


def f29_uarn_015_uo_crossdown_from_above_70_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: UO crossed down through 70 today (was > 70 yesterday, < 70 today)."""
    uo = _ultimate_osc(high, low, close, 7, 14, 28)
    cond = (uo.shift(1) > 70.0) & (uo <= 70.0)
    return cond.astype(float).where(uo.notna() & uo.shift(1).notna(), np.nan)


# ============================================================
# Bucket B — Aroon Up/Down/Osc (016-040)
# ============================================================

def f29_uarn_016_aroon_up_short_term_14d(high: pd.Series) -> pd.Series:
    """Aroon Up (14) — short-term recency-of-high signal."""
    return _aroon_up(high, 14)


def f29_uarn_017_aroon_up_classic_25d(high: pd.Series) -> pd.Series:
    """Aroon Up (25) — classic monthly-horizon recency-of-high."""
    return _aroon_up(high, 25)


def f29_uarn_018_aroon_up_long_term_50d(high: pd.Series) -> pd.Series:
    """Aroon Up (50) — quarter-scale persistence of new-high cadence."""
    return _aroon_up(high, 50)


def f29_uarn_019_aroon_up_annual_252d(high: pd.Series) -> pd.Series:
    """Aroon Up (252) — annual cycle recency of high (regime-scale)."""
    return _aroon_up(high, 252)


def f29_uarn_020_aroon_down_short_term_14d(low: pd.Series) -> pd.Series:
    """Aroon Down (14) — short-term recency of low (breakdown speed)."""
    return _aroon_down(low, 14)


def f29_uarn_021_aroon_down_classic_25d(low: pd.Series) -> pd.Series:
    """Aroon Down (25) — classic monthly recency of low."""
    return _aroon_down(low, 25)


def f29_uarn_022_aroon_down_long_term_50d(low: pd.Series) -> pd.Series:
    """Aroon Down (50) — quarter-scale recency of low."""
    return _aroon_down(low, 50)


def f29_uarn_023_aroon_down_annual_252d(low: pd.Series) -> pd.Series:
    """Aroon Down (252) — annual recency of low."""
    return _aroon_down(low, 252)


def f29_uarn_024_aroon_oscillator_25d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Aroon Oscillator (25) = Up − Down: classic trend-direction balance."""
    return _aroon_up(high, 25) - _aroon_down(low, 25)


def f29_uarn_025_aroon_oscillator_short_14d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Aroon Oscillator (14): short-term up/down balance."""
    return _aroon_up(high, 14) - _aroon_down(low, 14)


def f29_uarn_026_aroon_oscillator_long_50d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Aroon Oscillator (50): quarter-scale up/down balance."""
    return _aroon_up(high, 50) - _aroon_down(low, 50)


def f29_uarn_027_aroon_oscillator_annual_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Aroon Oscillator (252): annual up/down balance."""
    return _aroon_up(high, 252) - _aroon_down(low, 252)


def f29_uarn_028_aroon_up_dwell_above_70_in_21d(high: pd.Series) -> pd.Series:
    """Bars in trailing 21d with Aroon-Up(25) above 70 — sustained strong-up regime."""
    au = _aroon_up(high, 25)
    above = (au > 70.0).astype(float)
    return above.rolling(MDAYS, min_periods=WDAYS).sum()


def f29_uarn_029_aroon_up_recoil_from_100_event(high: pd.Series) -> pd.Series:
    """Event: Aroon-Up(25) was 100 yesterday, dropped today — recency-of-high lost."""
    au = _aroon_up(high, 25)
    cond = (au.shift(1) >= 99.999) & (au < 99.999)
    return cond.astype(float).where(au.notna() & au.shift(1).notna(), np.nan)


def f29_uarn_030_aroon_oscillator_zero_crossings_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of Aroon-Osc(25) zero crossings in trailing 63d — regime-change frequency."""
    osc = _aroon_up(high, 25) - _aroon_down(low, 25)
    sign = np.sign(osc.fillna(0.0))
    flips = (sign != sign.shift(1)).astype(float)
    flips.iloc[0] = 0.0
    return flips.rolling(QDAYS, min_periods=MDAYS).sum()


def f29_uarn_031_aroon_oscillator_positive_streak(high: pd.Series, low: pd.Series) -> pd.Series:
    """Current consecutive-bar streak where Aroon-Osc(25) > 0 (positive regime length)."""
    osc = _aroon_up(high, 25) - _aroon_down(low, 25)
    pos = (osc > 0).astype(float).values
    n = len(pos)
    out = np.full(n, np.nan, dtype=float)
    streak = 0
    for i in range(n):
        if np.isnan(osc.iat[i]):
            streak = 0
            out[i] = np.nan
        else:
            streak = streak + 1 if pos[i] > 0 else 0
            out[i] = float(streak)
    return pd.Series(out, index=osc.index)


def f29_uarn_032_aroon_up_minus_down_25_extreme_indicator(high: pd.Series, low: pd.Series) -> pd.Series:
    """Indicator: Aroon-Osc(25) > 80 — extreme trend dominance reading."""
    osc = _aroon_up(high, 25) - _aroon_down(low, 25)
    return (osc > 80.0).astype(float).where(osc.notna(), np.nan)


def f29_uarn_033_aroon_down_acceleration_event(low: pd.Series) -> pd.Series:
    """Event: Aroon-Down(25) crossed up through 50 today — bearish momentum onset."""
    ad = _aroon_down(low, 25)
    cond = (ad.shift(1) <= 50.0) & (ad > 50.0)
    return cond.astype(float).where(ad.notna() & ad.shift(1).notna(), np.nan)


def f29_uarn_034_aroon_up_decay_after_peak_21d(high: pd.Series) -> pd.Series:
    """Aroon-Up(25) drop from its 21d max — how far recency-of-high has decayed."""
    au = _aroon_up(high, 25)
    return au - au.rolling(MDAYS, min_periods=WDAYS).max()


def f29_uarn_035_aroon_oscillator_volatility_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """63d std-dev of Aroon-Osc(25) — directional-balance instability."""
    osc = _aroon_up(high, 25) - _aroon_down(low, 25)
    return osc.rolling(QDAYS, min_periods=MDAYS).std()


def f29_uarn_036_aroon_up_zscore_252d(high: pd.Series) -> pd.Series:
    """Z-score of Aroon-Up(25) in 252d window — anomalously fresh/stale high."""
    au = _aroon_up(high, 25)
    return _rolling_zscore(au, YDAYS, min_periods=QDAYS)


def f29_uarn_037_aroon_down_dominance_indicator(high: pd.Series, low: pd.Series) -> pd.Series:
    """Indicator: Aroon-Down(25) > Aroon-Up(25) — bearish-recency dominance."""
    au = _aroon_up(high, 25)
    ad = _aroon_down(low, 25)
    return (ad > au).astype(float).where(au.notna() & ad.notna(), np.nan)


def f29_uarn_038_aroon_up_crossdown_from_100_to_below_50_event(high: pd.Series) -> pd.Series:
    """Event: Aroon-Up(25) was 100 within last 5 bars but is now below 50 — collapse."""
    au = _aroon_up(high, 25)
    recent_peak = (au.rolling(WDAYS, min_periods=2).max() >= 99.999)
    cond = recent_peak.shift(1).fillna(False) & (au < 50.0)
    return cond.astype(float).where(au.notna(), np.nan)


def f29_uarn_039_aroon_oscillator_negative_dwell_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars in trailing 21d with Aroon-Osc(25) < 0 — bearish-regime dwell time."""
    osc = _aroon_up(high, 25) - _aroon_down(low, 25)
    neg = (osc < 0).astype(float)
    return neg.rolling(MDAYS, min_periods=WDAYS).sum()


def f29_uarn_040_aroon_up_falling_consecutive_streak_25d(high: pd.Series) -> pd.Series:
    """Consecutive-bar streak of Aroon-Up(25) falling (.diff() < 0) — relentless recency-decay."""
    au = _aroon_up(high, 25)
    fall = (au.diff() < 0).astype(float).values
    n = len(fall)
    out = np.full(n, np.nan, dtype=float)
    streak = 0
    for i in range(n):
        if np.isnan(au.iat[i]):
            streak = 0
            out[i] = np.nan
        else:
            streak = streak + 1 if fall[i] > 0 else 0
            out[i] = float(streak)
    return pd.Series(out, index=au.index)


# ============================================================
# Bucket C — Vortex (041-055)
# ============================================================

def f29_uarn_041_vortex_plus_14d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Vortex VI+ (14): bullish vortex strength (classic horizon)."""
    vp, _ = _vortex(high, low, close, n=14)
    return vp


def f29_uarn_042_vortex_minus_14d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Vortex VI- (14): bearish vortex strength (classic horizon)."""
    _, vm = _vortex(high, low, close, n=14)
    return vm


def f29_uarn_043_vortex_diff_14d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Vortex (14): VI+ − VI− directional balance."""
    vp, vm = _vortex(high, low, close, n=14)
    return vp - vm


def f29_uarn_044_vortex_plus_25d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Vortex VI+ (25): bullish vortex at monthly horizon — slower-trend variant."""
    vp, _ = _vortex(high, low, close, n=25)
    return vp


def f29_uarn_045_vortex_minus_25d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Vortex VI- (25): bearish vortex at monthly horizon."""
    _, vm = _vortex(high, low, close, n=25)
    return vm


def f29_uarn_046_vortex_diff_25d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Vortex (25): VI+ − VI− directional balance at slower horizon."""
    vp, vm = _vortex(high, low, close, n=25)
    return vp - vm


def f29_uarn_047_vortex_bearish_cross_event_14d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: VI− crossed above VI+ today (14d) — bearish vortex flip."""
    vp, vm = _vortex(high, low, close, n=14)
    cond = (vm > vp) & (vm.shift(1) <= vp.shift(1))
    return cond.astype(float).where(vp.notna() & vm.notna() & vp.shift(1).notna(), np.nan)


def f29_uarn_048_vortex_first_bearish_cross_after_63d_bull(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: first VI−-over-VI+ cross after 63 consecutive bars of VI+ > VI− (regime end)."""
    vp, vm = _vortex(high, low, close, n=14)
    bull_dwell = (vp > vm).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    cross = (vm > vp) & (vm.shift(1) <= vp.shift(1))
    cond = cross & (bull_dwell.shift(1) >= QDAYS - 1)
    return cond.astype(float).where(vp.notna() & vm.notna(), np.nan)


def f29_uarn_049_vortex_minus_dwell_above_one_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars in trailing 21d with VI−(14) > 1.0 — sustained bearish-vortex regime."""
    _, vm = _vortex(high, low, close, n=14)
    above = (vm > 1.0).astype(float)
    return above.rolling(MDAYS, min_periods=WDAYS).sum()


def f29_uarn_050_vortex_diff_decay_from_63d_max(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """VI+−VI− minus its 63d rolling max — decay from peak bullish trend."""
    vp, vm = _vortex(high, low, close, n=14)
    diff = vp - vm
    return diff - diff.rolling(QDAYS, min_periods=MDAYS).max()


def f29_uarn_051_vortex_diff_smoothed_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5d-mean-smoothed Vortex diff(14) — denoised directional signal."""
    vp, vm = _vortex(high, low, close, n=14)
    return (vp - vm).rolling(WDAYS, min_periods=2).mean()


def f29_uarn_052_vortex_diff_persistence_sign_streak(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Consecutive-bar streak of Vortex-diff(14) sign — regime persistence length."""
    vp, vm = _vortex(high, low, close, n=14)
    diff = vp - vm
    sign = np.sign(diff)
    n = len(diff)
    out = np.full(n, np.nan, dtype=float)
    streak = 0
    last_sign = 0.0
    for i in range(n):
        s = sign.iat[i]
        if pd.isna(s):
            streak = 0
            out[i] = np.nan
            last_sign = 0.0
        else:
            if s != last_sign:
                streak = 1
            else:
                streak += 1
            last_sign = s
            out[i] = float(streak) * (1.0 if s > 0 else (-1.0 if s < 0 else 0.0))
    return pd.Series(out, index=diff.index)


def f29_uarn_053_vortex_diff_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of Vortex-diff(14) in 252d window — anomalously strong directional reading."""
    vp, vm = _vortex(high, low, close, n=14)
    return _rolling_zscore(vp - vm, YDAYS, min_periods=QDAYS)


def f29_uarn_054_vortex_minus_acceleration_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5d slope of VI−(14) — bearish vortex acceleration."""
    _, vm = _vortex(high, low, close, n=14)
    return _rolling_slope(vm, WDAYS, min_periods=3)


def f29_uarn_055_vortex_minus_minus_plus_at_252d_high(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """At bars where high == 252d max, value of VI−(14) − VI+(14) — bearish vortex at the peak."""
    vp, vm = _vortex(high, low, close, n=14)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = (high >= rmax)
    diff = vm - vp
    return diff.where(at_peak, np.nan)


# ============================================================
# Bucket D — ADX / DI+ / DI- (056-080) -- part 1: 056-075
# ============================================================

def f29_uarn_056_adx_classic_14d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Wilder ADX (14) — classic trend-strength reading."""
    _, _, adx = _dm_components(high, low, close, n=14)
    return adx


def f29_uarn_057_di_plus_14d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Wilder DI+ (14) — directional-index up component."""
    plus_di, _, _ = _dm_components(high, low, close, n=14)
    return plus_di


def f29_uarn_058_di_minus_14d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Wilder DI− (14) — directional-index down component."""
    _, minus_di, _ = _dm_components(high, low, close, n=14)
    return minus_di


def f29_uarn_059_di_balance_diff_14d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """DI+ − DI− (14) — directional-balance signed measure."""
    plus_di, minus_di, _ = _dm_components(high, low, close, n=14)
    return plus_di - minus_di


def f29_uarn_060_adx_above_25_strong_trend_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: ADX(14) > 25 — strong-trend regime."""
    _, _, adx = _dm_components(high, low, close, n=14)
    return (adx > 25.0).astype(float).where(adx.notna(), np.nan)


def f29_uarn_061_adx_above_40_extreme_trend_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: ADX(14) > 40 — extreme trend regime (exhaustion candidate)."""
    _, _, adx = _dm_components(high, low, close, n=14)
    return (adx > 40.0).astype(float).where(adx.notna(), np.nan)


def f29_uarn_062_adx_dwell_above_25_in_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars in trailing 63d with ADX(14) > 25 — strong-trend regime dwell time."""
    _, _, adx = _dm_components(high, low, close, n=14)
    above = (adx > 25.0).astype(float)
    return above.rolling(QDAYS, min_periods=MDAYS).sum()


def f29_uarn_063_adx_falling_from_above_40_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: ADX(14) was > 40 within last 5 bars and is now falling (today < yesterday)."""
    _, _, adx = _dm_components(high, low, close, n=14)
    recent_hot = (adx.rolling(WDAYS, min_periods=2).max() > 40.0)
    cond = recent_hot.shift(1).fillna(False) & (adx.diff() < 0)
    return cond.astype(float).where(adx.notna(), np.nan)


def f29_uarn_064_adx_peak_decay_from_63d_max(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ADX(14) minus its 63d max — trend-strength decay from quarterly peak (<=0)."""
    _, _, adx = _dm_components(high, low, close, n=14)
    return adx - adx.rolling(QDAYS, min_periods=MDAYS).max()


def f29_uarn_065_adx_long_25d_slow(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Wilder ADX(25) — slower trend-strength reading for monthly-horizon regime."""
    _, _, adx = _dm_components(high, low, close, n=25)
    return adx


def f29_uarn_066_di_minus_minus_di_plus_25d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """DI−(25) − DI+(25) — slow-horizon bearish dominance reading."""
    plus_di, minus_di, _ = _dm_components(high, low, close, n=25)
    return minus_di - plus_di


def f29_uarn_067_di_minus_dominance_event_14d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: DI−(14) crossed above DI+(14) today — bearish-directional flip."""
    plus_di, minus_di, _ = _dm_components(high, low, close, n=14)
    cond = (minus_di > plus_di) & (minus_di.shift(1) <= plus_di.shift(1))
    return cond.astype(float).where(plus_di.notna() & minus_di.notna(), np.nan)


def f29_uarn_068_di_minus_acceleration_above_30_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: DI−(14) crossed above 30 today — bearish-pressure ignition."""
    _, minus_di, _ = _dm_components(high, low, close, n=14)
    cond = (minus_di > 30.0) & (minus_di.shift(1) <= 30.0)
    return cond.astype(float).where(minus_di.notna() & minus_di.shift(1).notna(), np.nan)


def f29_uarn_069_adx_zscore_504d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of ADX(14) in trailing 504d distribution — anomalously hot trend reading."""
    _, _, adx = _dm_components(high, low, close, n=14)
    return _rolling_zscore(adx, DDAYS_2Y, min_periods=YDAYS)


def f29_uarn_070_adx_5d_slope_post_peak(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5d slope of ADX(14) — trend-strength acceleration (negative = top exhaustion)."""
    _, _, adx = _dm_components(high, low, close, n=14)
    return _rolling_slope(adx, WDAYS, min_periods=3)


def f29_uarn_071_di_plus_falling_streak(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Consecutive-bar streak of DI+(14) falling — relentless decay of bullish DM."""
    plus_di, _, _ = _dm_components(high, low, close, n=14)
    fall = (plus_di.diff() < 0).astype(float).values
    n = len(fall)
    out = np.full(n, np.nan, dtype=float)
    streak = 0
    for i in range(n):
        if pd.isna(plus_di.iat[i]):
            streak = 0
            out[i] = np.nan
        else:
            streak = streak + 1 if fall[i] > 0 else 0
            out[i] = float(streak)
    return pd.Series(out, index=plus_di.index)


def f29_uarn_072_di_minus_rising_streak(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Consecutive-bar streak of DI−(14) rising — relentless bearish-DM build."""
    _, minus_di, _ = _dm_components(high, low, close, n=14)
    rise = (minus_di.diff() > 0).astype(float).values
    n = len(rise)
    out = np.full(n, np.nan, dtype=float)
    streak = 0
    for i in range(n):
        if pd.isna(minus_di.iat[i]):
            streak = 0
            out[i] = np.nan
        else:
            streak = streak + 1 if rise[i] > 0 else 0
            out[i] = float(streak)
    return pd.Series(out, index=minus_di.index)


def f29_uarn_073_adx_rising_with_di_minus_dominant_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: ADX(14) rising AND DI−(14) > DI+(14) — strengthening bearish trend."""
    plus_di, minus_di, adx = _dm_components(high, low, close, n=14)
    cond = (adx.diff() > 0) & (minus_di > plus_di)
    return cond.astype(float).where(adx.notna() & plus_di.notna() & minus_di.notna(), np.nan)


def f29_uarn_074_di_diff_dwell_negative_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars in trailing 21d with DI+(14) − DI−(14) < 0 — sustained bearish-DM dwell."""
    plus_di, minus_di, _ = _dm_components(high, low, close, n=14)
    neg = ((plus_di - minus_di) < 0).astype(float)
    return neg.rolling(MDAYS, min_periods=WDAYS).sum()


def f29_uarn_075_adx_at_252d_high_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """At bars where high == 252d max, value of ADX(14) — trend strength right at the peak."""
    _, _, adx = _dm_components(high, low, close, n=14)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = (high >= rmax)
    return adx.where(at_peak, np.nan)


# ============================================================
#                         REGISTRY 001-075
# ============================================================

ULTIMATE_AROON_VORTEX_BASE_REGISTRY_001_075 = {
    "f29_uarn_001_ultimate_oscillator_classic": {"inputs": ["high", "low", "close"], "func": f29_uarn_001_ultimate_oscillator_classic},
    "f29_uarn_002_uo_distance_above_70_overbought": {"inputs": ["high", "low", "close"], "func": f29_uarn_002_uo_distance_above_70_overbought},
    "f29_uarn_003_uo_extreme_above_80_indicator": {"inputs": ["high", "low", "close"], "func": f29_uarn_003_uo_extreme_above_80_indicator},
    "f29_uarn_004_uo_dwell_above_70_in_21d": {"inputs": ["high", "low", "close"], "func": f29_uarn_004_uo_dwell_above_70_in_21d},
    "f29_uarn_005_uo_distance_from_midline_50": {"inputs": ["high", "low", "close"], "func": f29_uarn_005_uo_distance_from_midline_50},
    "f29_uarn_006_uo_short_timeframe_bp_ratio_7d": {"inputs": ["high", "low", "close"], "func": f29_uarn_006_uo_short_timeframe_bp_ratio_7d},
    "f29_uarn_007_uo_medium_timeframe_bp_ratio_14d": {"inputs": ["high", "low", "close"], "func": f29_uarn_007_uo_medium_timeframe_bp_ratio_14d},
    "f29_uarn_008_uo_long_timeframe_bp_ratio_28d": {"inputs": ["high", "low", "close"], "func": f29_uarn_008_uo_long_timeframe_bp_ratio_28d},
    "f29_uarn_009_uo_short_minus_long_tf_spread": {"inputs": ["high", "low", "close"], "func": f29_uarn_009_uo_short_minus_long_tf_spread},
    "f29_uarn_010_uo_smoothed_5d_median": {"inputs": ["high", "low", "close"], "func": f29_uarn_010_uo_smoothed_5d_median},
    "f29_uarn_011_uo_exhaustion_distance_from_63d_max": {"inputs": ["high", "low", "close"], "func": f29_uarn_011_uo_exhaustion_distance_from_63d_max},
    "f29_uarn_012_uo_failure_swing_bearish_event": {"inputs": ["high", "low", "close"], "func": f29_uarn_012_uo_failure_swing_bearish_event},
    "f29_uarn_013_uo_zscore_252d": {"inputs": ["high", "low", "close"], "func": f29_uarn_013_uo_zscore_252d},
    "f29_uarn_014_uo_bars_since_last_above_70": {"inputs": ["high", "low", "close"], "func": f29_uarn_014_uo_bars_since_last_above_70},
    "f29_uarn_015_uo_crossdown_from_above_70_event": {"inputs": ["high", "low", "close"], "func": f29_uarn_015_uo_crossdown_from_above_70_event},
    "f29_uarn_016_aroon_up_short_term_14d": {"inputs": ["high"], "func": f29_uarn_016_aroon_up_short_term_14d},
    "f29_uarn_017_aroon_up_classic_25d": {"inputs": ["high"], "func": f29_uarn_017_aroon_up_classic_25d},
    "f29_uarn_018_aroon_up_long_term_50d": {"inputs": ["high"], "func": f29_uarn_018_aroon_up_long_term_50d},
    "f29_uarn_019_aroon_up_annual_252d": {"inputs": ["high"], "func": f29_uarn_019_aroon_up_annual_252d},
    "f29_uarn_020_aroon_down_short_term_14d": {"inputs": ["low"], "func": f29_uarn_020_aroon_down_short_term_14d},
    "f29_uarn_021_aroon_down_classic_25d": {"inputs": ["low"], "func": f29_uarn_021_aroon_down_classic_25d},
    "f29_uarn_022_aroon_down_long_term_50d": {"inputs": ["low"], "func": f29_uarn_022_aroon_down_long_term_50d},
    "f29_uarn_023_aroon_down_annual_252d": {"inputs": ["low"], "func": f29_uarn_023_aroon_down_annual_252d},
    "f29_uarn_024_aroon_oscillator_25d": {"inputs": ["high", "low"], "func": f29_uarn_024_aroon_oscillator_25d},
    "f29_uarn_025_aroon_oscillator_short_14d": {"inputs": ["high", "low"], "func": f29_uarn_025_aroon_oscillator_short_14d},
    "f29_uarn_026_aroon_oscillator_long_50d": {"inputs": ["high", "low"], "func": f29_uarn_026_aroon_oscillator_long_50d},
    "f29_uarn_027_aroon_oscillator_annual_252d": {"inputs": ["high", "low"], "func": f29_uarn_027_aroon_oscillator_annual_252d},
    "f29_uarn_028_aroon_up_dwell_above_70_in_21d": {"inputs": ["high"], "func": f29_uarn_028_aroon_up_dwell_above_70_in_21d},
    "f29_uarn_029_aroon_up_recoil_from_100_event": {"inputs": ["high"], "func": f29_uarn_029_aroon_up_recoil_from_100_event},
    "f29_uarn_030_aroon_oscillator_zero_crossings_63d": {"inputs": ["high", "low"], "func": f29_uarn_030_aroon_oscillator_zero_crossings_63d},
    "f29_uarn_031_aroon_oscillator_positive_streak": {"inputs": ["high", "low"], "func": f29_uarn_031_aroon_oscillator_positive_streak},
    "f29_uarn_032_aroon_up_minus_down_25_extreme_indicator": {"inputs": ["high", "low"], "func": f29_uarn_032_aroon_up_minus_down_25_extreme_indicator},
    "f29_uarn_033_aroon_down_acceleration_event": {"inputs": ["low"], "func": f29_uarn_033_aroon_down_acceleration_event},
    "f29_uarn_034_aroon_up_decay_after_peak_21d": {"inputs": ["high"], "func": f29_uarn_034_aroon_up_decay_after_peak_21d},
    "f29_uarn_035_aroon_oscillator_volatility_63d": {"inputs": ["high", "low"], "func": f29_uarn_035_aroon_oscillator_volatility_63d},
    "f29_uarn_036_aroon_up_zscore_252d": {"inputs": ["high"], "func": f29_uarn_036_aroon_up_zscore_252d},
    "f29_uarn_037_aroon_down_dominance_indicator": {"inputs": ["high", "low"], "func": f29_uarn_037_aroon_down_dominance_indicator},
    "f29_uarn_038_aroon_up_crossdown_from_100_to_below_50_event": {"inputs": ["high"], "func": f29_uarn_038_aroon_up_crossdown_from_100_to_below_50_event},
    "f29_uarn_039_aroon_oscillator_negative_dwell_21d": {"inputs": ["high", "low"], "func": f29_uarn_039_aroon_oscillator_negative_dwell_21d},
    "f29_uarn_040_aroon_up_falling_consecutive_streak_25d": {"inputs": ["high"], "func": f29_uarn_040_aroon_up_falling_consecutive_streak_25d},
    "f29_uarn_041_vortex_plus_14d": {"inputs": ["high", "low", "close"], "func": f29_uarn_041_vortex_plus_14d},
    "f29_uarn_042_vortex_minus_14d": {"inputs": ["high", "low", "close"], "func": f29_uarn_042_vortex_minus_14d},
    "f29_uarn_043_vortex_diff_14d": {"inputs": ["high", "low", "close"], "func": f29_uarn_043_vortex_diff_14d},
    "f29_uarn_044_vortex_plus_25d": {"inputs": ["high", "low", "close"], "func": f29_uarn_044_vortex_plus_25d},
    "f29_uarn_045_vortex_minus_25d": {"inputs": ["high", "low", "close"], "func": f29_uarn_045_vortex_minus_25d},
    "f29_uarn_046_vortex_diff_25d": {"inputs": ["high", "low", "close"], "func": f29_uarn_046_vortex_diff_25d},
    "f29_uarn_047_vortex_bearish_cross_event_14d": {"inputs": ["high", "low", "close"], "func": f29_uarn_047_vortex_bearish_cross_event_14d},
    "f29_uarn_048_vortex_first_bearish_cross_after_63d_bull": {"inputs": ["high", "low", "close"], "func": f29_uarn_048_vortex_first_bearish_cross_after_63d_bull},
    "f29_uarn_049_vortex_minus_dwell_above_one_21d": {"inputs": ["high", "low", "close"], "func": f29_uarn_049_vortex_minus_dwell_above_one_21d},
    "f29_uarn_050_vortex_diff_decay_from_63d_max": {"inputs": ["high", "low", "close"], "func": f29_uarn_050_vortex_diff_decay_from_63d_max},
    "f29_uarn_051_vortex_diff_smoothed_5d": {"inputs": ["high", "low", "close"], "func": f29_uarn_051_vortex_diff_smoothed_5d},
    "f29_uarn_052_vortex_diff_persistence_sign_streak": {"inputs": ["high", "low", "close"], "func": f29_uarn_052_vortex_diff_persistence_sign_streak},
    "f29_uarn_053_vortex_diff_zscore_252d": {"inputs": ["high", "low", "close"], "func": f29_uarn_053_vortex_diff_zscore_252d},
    "f29_uarn_054_vortex_minus_acceleration_5d": {"inputs": ["high", "low", "close"], "func": f29_uarn_054_vortex_minus_acceleration_5d},
    "f29_uarn_055_vortex_minus_minus_plus_at_252d_high": {"inputs": ["high", "low", "close"], "func": f29_uarn_055_vortex_minus_minus_plus_at_252d_high},
    "f29_uarn_056_adx_classic_14d": {"inputs": ["high", "low", "close"], "func": f29_uarn_056_adx_classic_14d},
    "f29_uarn_057_di_plus_14d": {"inputs": ["high", "low", "close"], "func": f29_uarn_057_di_plus_14d},
    "f29_uarn_058_di_minus_14d": {"inputs": ["high", "low", "close"], "func": f29_uarn_058_di_minus_14d},
    "f29_uarn_059_di_balance_diff_14d": {"inputs": ["high", "low", "close"], "func": f29_uarn_059_di_balance_diff_14d},
    "f29_uarn_060_adx_above_25_strong_trend_indicator": {"inputs": ["high", "low", "close"], "func": f29_uarn_060_adx_above_25_strong_trend_indicator},
    "f29_uarn_061_adx_above_40_extreme_trend_indicator": {"inputs": ["high", "low", "close"], "func": f29_uarn_061_adx_above_40_extreme_trend_indicator},
    "f29_uarn_062_adx_dwell_above_25_in_63d": {"inputs": ["high", "low", "close"], "func": f29_uarn_062_adx_dwell_above_25_in_63d},
    "f29_uarn_063_adx_falling_from_above_40_event": {"inputs": ["high", "low", "close"], "func": f29_uarn_063_adx_falling_from_above_40_event},
    "f29_uarn_064_adx_peak_decay_from_63d_max": {"inputs": ["high", "low", "close"], "func": f29_uarn_064_adx_peak_decay_from_63d_max},
    "f29_uarn_065_adx_long_25d_slow": {"inputs": ["high", "low", "close"], "func": f29_uarn_065_adx_long_25d_slow},
    "f29_uarn_066_di_minus_minus_di_plus_25d": {"inputs": ["high", "low", "close"], "func": f29_uarn_066_di_minus_minus_di_plus_25d},
    "f29_uarn_067_di_minus_dominance_event_14d": {"inputs": ["high", "low", "close"], "func": f29_uarn_067_di_minus_dominance_event_14d},
    "f29_uarn_068_di_minus_acceleration_above_30_event": {"inputs": ["high", "low", "close"], "func": f29_uarn_068_di_minus_acceleration_above_30_event},
    "f29_uarn_069_adx_zscore_504d": {"inputs": ["high", "low", "close"], "func": f29_uarn_069_adx_zscore_504d},
    "f29_uarn_070_adx_5d_slope_post_peak": {"inputs": ["high", "low", "close"], "func": f29_uarn_070_adx_5d_slope_post_peak},
    "f29_uarn_071_di_plus_falling_streak": {"inputs": ["high", "low", "close"], "func": f29_uarn_071_di_plus_falling_streak},
    "f29_uarn_072_di_minus_rising_streak": {"inputs": ["high", "low", "close"], "func": f29_uarn_072_di_minus_rising_streak},
    "f29_uarn_073_adx_rising_with_di_minus_dominant_event": {"inputs": ["high", "low", "close"], "func": f29_uarn_073_adx_rising_with_di_minus_dominant_event},
    "f29_uarn_074_di_diff_dwell_negative_21d": {"inputs": ["high", "low", "close"], "func": f29_uarn_074_di_diff_dwell_negative_21d},
    "f29_uarn_075_adx_at_252d_high_indicator": {"inputs": ["high", "low", "close"], "func": f29_uarn_075_adx_at_252d_high_indicator},
}
