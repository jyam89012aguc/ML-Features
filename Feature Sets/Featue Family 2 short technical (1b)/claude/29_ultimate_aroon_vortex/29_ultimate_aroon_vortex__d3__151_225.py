"""ultimate_aroon_vortex d3 features 151-225 — Pipeline 1b-technical.

Gap-fill extension to the original 150-feature family. Adds hypotheses that fill
the following research-identified gaps:
  - ADXR (Wilder's Average Directional Movement Rating) at multiple horizons,
    plus ADXR-vs-ADX residuals and rate measures.
  - Raw +DM/-DM pre-normalization, DM sum, DI sum, and Wilder-smoothed-TR /
    Wilder-smoothed-DM ratios as alternative directional measures.
  - ADX trough/peak/hook taxonomy: cross-up-25 (trend birth), cross-down-20
    (trend death), 'hook' patterns (rise then dip then resume).
  - Aroon extensions: Aroon sum (Up+Down), normalized (Up-Down)/(Up+Down),
    midpoint-50 crosses, Aroon-Osc absolute value, Aroon on log-price.
  - Ultimate Oscillator extensions: bullish failure swing, TF-component cross
    events, BP/TR midline alignment, weighted-variant UO, 50-cross events.

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

def _dm_raw(high, low):
    """Returns raw (+DM, -DM) per Wilder before any smoothing."""
    up = high.diff()
    dn = -low.diff()
    plus_dm = pd.Series(np.where((up > dn) & (up > 0), up, 0.0), index=high.index)
    minus_dm = pd.Series(np.where((dn > up) & (dn > 0), dn, 0.0), index=high.index)
    return plus_dm, minus_dm


def _dm_components(high, low, close, n=14):
    """Returns (DI_plus, DI_minus, ADX) Wilder-smoothed."""
    plus_dm, minus_dm = _dm_raw(high, low)
    tr = _true_range(high, low, close)
    atr = _wilder_ema(tr, n)
    plus_di = 100.0 * _safe_div(_wilder_ema(plus_dm, n), atr)
    minus_di = 100.0 * _safe_div(_wilder_ema(minus_dm, n), atr)
    dx = 100.0 * _safe_div((plus_di - minus_di).abs(), (plus_di + minus_di))
    adx = _wilder_ema(dx, n)
    return plus_di, minus_di, adx


def _adxr(high, low, close, n=14):
    """Wilder ADXR = (ADX_t + ADX_{t-(n-1)}) / 2 — averaged directional movement rating."""
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


def _ultimate_osc(high, low, close, n1=7, n2=14, n3=28, w1=4.0, w2=2.0, w3=1.0):
    """Williams' Ultimate Oscillator with configurable weights (default 4/2/1)."""
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
    wsum = w1 + w2 + w3
    return 100.0 * (w1 * a1 + w2 * a2 + w3 * a3) / wsum


def _choppiness(high, low, close, n=14):
    tr = _true_range(high, low, close)
    sum_tr = tr.rolling(n, min_periods=max(n // 2, 2)).sum()
    hi = high.rolling(n, min_periods=max(n // 2, 2)).max()
    lo = low.rolling(n, min_periods=max(n // 2, 2)).min()
    ratio = _safe_div(sum_tr, hi - lo)
    return 100.0 * np.log10(ratio.where(ratio > 0, np.nan)) / np.log10(n)


def _bars_since(condition_series, lookback):
    """Bars since condition was last true in window. If never true → len(window)."""
    def _bsm(w):
        idx = np.where(w > 0)[0]
        if idx.size == 0:
            return float(len(w))
        return float((len(w) - 1) - idx[-1])
    return condition_series.astype(float).rolling(lookback, min_periods=max(lookback // 3, 2)).apply(_bsm, raw=True)


# ============================================================
# Bucket A — ADXR (Wilder's Averaged Directional Movement Rating) (151-160)
# ============================================================

def f29_uarn_151_adxr_classic_14d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Wilder ADXR(14) = (ADX_t + ADX_{t-13})/2 — classic averaged trend-strength rating."""
    return (_adxr(high, low, close, n=14)).diff().diff().diff()


def f29_uarn_152_adxr_long_25d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Wilder ADXR(25) — monthly-horizon averaged rating (slower regime classifier)."""
    return (_adxr(high, low, close, n=25)).diff().diff().diff()


def f29_uarn_153_adxr_minus_adx_residual_14d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ADXR(14) − ADX(14) — when negative, ADX is accelerating ahead of its rating (peak proximity)."""
    _, _, adx = _dm_components(high, low, close, n=14)
    adxr = _adxr(high, low, close, n=14)
    return (adxr - adx).diff().diff().diff()


def f29_uarn_154_adxr_above_25_strong_trend_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: ADXR(14) > 25 — Wilder's smoothed strong-trend regime per New Concepts."""
    a = _adxr(high, low, close, n=14)
    return ((a > 25.0).astype(float).where(a.notna(), np.nan)).diff().diff().diff()


def f29_uarn_155_adxr_below_20_no_trend_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: ADXR(14) < 20 — Wilder's smoothed 'no-trend' regime."""
    a = _adxr(high, low, close, n=14)
    return ((a < 20.0).astype(float).where(a.notna(), np.nan)).diff().diff().diff()


def f29_uarn_156_adxr_cross_above_25_event_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: ADXR(14) crossed up through 25 today — Wilder smoothed trend ignition."""
    a = _adxr(high, low, close, n=14)
    cond = (a > 25.0) & (a.shift(1) <= 25.0)
    return (cond.astype(float).where(a.notna() & a.shift(1).notna(), np.nan)).diff().diff().diff()


def f29_uarn_157_adxr_5d_slope_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5d slope of ADXR(14) — smoothed trend-strength velocity (lagging vs ADX slope)."""
    a = _adxr(high, low, close, n=14)
    return (_rolling_slope(a, WDAYS, min_periods=3)).diff().diff().diff()


def f29_uarn_158_adxr_dwell_above_25_in_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars in trailing 63d with ADXR(14) > 25 — smoothed strong-trend dwell."""
    a = _adxr(high, low, close, n=14)
    return ((a > 25.0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()).diff().diff().diff()


def f29_uarn_159_adxr_zscore_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of ADXR(14) in 252d window — anomalously hot smoothed trend rating."""
    a = _adxr(high, low, close, n=14)
    return (_rolling_zscore(a, YDAYS, min_periods=QDAYS)).diff().diff().diff()


def f29_uarn_160_adxr_peak_decay_from_63d_max_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ADXR(14) minus its 63d rolling max — smoothed trend-rating decay from quarterly peak (<=0)."""
    a = _adxr(high, low, close, n=14)
    return (a - a.rolling(QDAYS, min_periods=MDAYS).max()).diff().diff().diff()


# ============================================================
# Bucket B — Raw DM components and DM/TR ratios (161-170)
# ============================================================

def f29_uarn_161_plus_dm_raw_wilder14_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Raw +DM Wilder-smoothed (14) — pre-normalization bullish directional movement."""
    pdm, _ = _dm_raw(high, low)
    return (_wilder_ema(pdm, 14)).diff().diff().diff()


def f29_uarn_162_minus_dm_raw_wilder14_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Raw -DM Wilder-smoothed (14) — pre-normalization bearish directional movement."""
    _, mdm = _dm_raw(high, low)
    return (_wilder_ema(mdm, 14)).diff().diff().diff()


def f29_uarn_163_dm_total_wilder14_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """+DM_W(14) + -DM_W(14): total directional-movement pressure (regardless of sign)."""
    pdm, mdm = _dm_raw(high, low)
    return (_wilder_ema(pdm, 14) + _wilder_ema(mdm, 14)).diff().diff().diff()


def f29_uarn_164_dm_raw_imbalance_chande_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Chande-style normalized DM imbalance: (+DM_W − -DM_W) / (+DM_W + -DM_W) ∈ [-1, 1]."""
    pdm, mdm = _dm_raw(high, low)
    p = _wilder_ema(pdm, 14)
    m = _wilder_ema(mdm, 14)
    return (_safe_div(p - m, p + m)).diff().diff().diff()


def f29_uarn_165_di_sum_14d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """DI+(14) + DI-(14): total directional pressure — large = high directional activity."""
    p, m, _ = _dm_components(high, low, close, n=14)
    return (p + m).diff().diff().diff()


def f29_uarn_166_atr_wilder_to_dm_total_ratio_14d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR_W(14) / (+DM_W + -DM_W)(14): wasted-range ratio — high = chop, low = clean directional."""
    pdm, mdm = _dm_raw(high, low)
    tr = _true_range(high, low, close)
    return (_safe_div(_wilder_ema(tr, 14), _wilder_ema(pdm, 14) + _wilder_ema(mdm, 14))).diff().diff().diff()


def f29_uarn_167_dx_raw_no_adx_smoothing_14d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Raw DX(14) = 100*|DI+ − DI-|/(DI+ + DI-) — unsmoothed pre-ADX directional strength."""
    p, m, _ = _dm_components(high, low, close, n=14)
    return (100.0 * _safe_div((p - m).abs(), p + m)).diff().diff().diff()


def f29_uarn_168_plus_dm_to_minus_dm_ratio_14d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """+DM_W(14) / -DM_W(14): pure-DM directional balance ratio."""
    pdm, mdm = _dm_raw(high, low)
    return (_safe_div(_wilder_ema(pdm, 14), _wilder_ema(mdm, 14))).diff().diff().diff()


def f29_uarn_169_minus_dm_zscore_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of -DM_W(14) in trailing 252d — anomalously hot raw bearish-DM reading."""
    _, mdm = _dm_raw(high, low)
    m = _wilder_ema(mdm, 14)
    return (_rolling_zscore(m, YDAYS, min_periods=QDAYS)).diff().diff().diff()


def f29_uarn_170_dm_total_at_252d_high_value_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """At bars where high == 252d max, value of (+DM_W + -DM_W)(14) — directional intensity at peak."""
    pdm, mdm = _dm_raw(high, low)
    total = _wilder_ema(pdm, 14) + _wilder_ema(mdm, 14)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = (high >= rmax)
    return (total.where(at_peak, np.nan)).diff().diff().diff()


# ============================================================
# Bucket C — ADX trough/peak/hook taxonomy (171-180)
# ============================================================

def f29_uarn_171_adx_cross_above_20_event_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: ADX(14) crossed up through 20 today — Wilder's trend-birth threshold."""
    _, _, adx = _dm_components(high, low, close, n=14)
    cond = (adx > 20.0) & (adx.shift(1) <= 20.0)
    return (cond.astype(float).where(adx.notna() & adx.shift(1).notna(), np.nan)).diff().diff().diff()


def f29_uarn_172_adx_cross_below_20_event_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: ADX(14) crossed down through 20 today — Wilder's trend-death threshold."""
    _, _, adx = _dm_components(high, low, close, n=14)
    cond = (adx < 20.0) & (adx.shift(1) >= 20.0)
    return (cond.astype(float).where(adx.notna() & adx.shift(1).notna(), np.nan)).diff().diff().diff()


def f29_uarn_173_adx_cross_above_25_event_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: ADX(14) crossed up through 25 today — strong-trend ignition (classic)."""
    _, _, adx = _dm_components(high, low, close, n=14)
    cond = (adx > 25.0) & (adx.shift(1) <= 25.0)
    return (cond.astype(float).where(adx.notna() & adx.shift(1).notna(), np.nan)).diff().diff().diff()


def f29_uarn_174_adx_cross_below_25_event_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: ADX(14) crossed down through 25 today — strong-trend exit."""
    _, _, adx = _dm_components(high, low, close, n=14)
    cond = (adx < 25.0) & (adx.shift(1) >= 25.0)
    return (cond.astype(float).where(adx.notna() & adx.shift(1).notna(), np.nan)).diff().diff().diff()


def f29_uarn_175_adx_hook_continuation_pattern_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ADX-hook continuation: ADX > 25 5 bars ago, dipped, now rising again — Wilder's hook."""
    _, _, adx = _dm_components(high, low, close, n=14)
    was_strong = (adx.shift(5) > 25.0)
    dipped = (adx.rolling(5, min_periods=3).min() < adx.shift(5))
    now_rising = (adx.diff() > 0) & (adx.diff().shift(1) > 0)
    cond = was_strong & dipped & now_rising & (adx > 25.0)
    return (cond.astype(float).where(adx.notna() & adx.shift(5).notna(), np.nan)).diff().diff().diff()


def f29_uarn_176_adx_post_cross25_persistence_21d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars-with-ADX>25 in 21d after last cross-above-25 event — trend-confirmation persistence."""
    _, _, adx = _dm_components(high, low, close, n=14)
    above = (adx > 25.0).astype(float)
    return (above.rolling(MDAYS, min_periods=WDAYS).sum()).diff().diff().diff()


def f29_uarn_177_adx_bars_since_last_cross_25_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since the last ADX(14) cross-above-25 event — staleness of trend ignition."""
    _, _, adx = _dm_components(high, low, close, n=14)
    cross = ((adx > 25.0) & (adx.shift(1) <= 25.0)).astype(float)
    return (_bars_since(cross, YDAYS)).diff().diff().diff()


def f29_uarn_178_adx_local_trough_event_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: ADX(14) made a 5d local trough today (prior 4 bars > today, today < tomorrow not used; PIT version: yesterday > today and today < min of last 4)."""
    _, _, adx = _dm_components(high, low, close, n=14)
    prior_min = adx.shift(1).rolling(4, min_periods=2).min()
    cond = (adx < prior_min) & (adx.diff() < 0) & (adx.diff().shift(1) > 0)
    return (cond.astype(float).where(adx.notna() & prior_min.notna(), np.nan)).diff().diff().diff()


def f29_uarn_179_adx_local_peak_event_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: ADX(14) just made a local peak (turn negative after positive streak ≥3 bars)."""
    _, _, adx = _dm_components(high, low, close, n=14)
    d = adx.diff()
    rose3 = (d.shift(1) > 0) & (d.shift(2) > 0) & (d.shift(3) > 0)
    now_fall = (d < 0)
    cond = rose3 & now_fall
    return (cond.astype(float).where(adx.notna() & d.shift(3).notna(), np.nan)).diff().diff().diff()


def f29_uarn_180_adx_reset_bars_below_15_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars-since-last-time ADX(14) was below 15 — staleness of last full trend reset."""
    _, _, adx = _dm_components(high, low, close, n=14)
    reset = (adx < 15.0).astype(float)
    return (_bars_since(reset, YDAYS)).diff().diff().diff()


# ============================================================
# Bucket D — Aroon extensions (181-195)
# ============================================================

def f29_uarn_181_aroon_sum_up_plus_down_25d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Aroon-Up(25) + Aroon-Down(25): total recency-state intensity (range-bound = high)."""
    return (_aroon_up(high, 25) + _aroon_down(low, 25)).diff().diff().diff()


def f29_uarn_182_aroon_normalized_imbalance_25d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """(Aroon-Up − Aroon-Down) / (Aroon-Up + Aroon-Down) at 25d — Chande-style normalized ∈ [-1, 1]."""
    au = _aroon_up(high, 25)
    ad = _aroon_down(low, 25)
    return (_safe_div(au - ad, au + ad)).diff().diff().diff()


def f29_uarn_183_aroon_osc_absolute_25d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """|Aroon-Osc(25)|: directional-intensity magnitude (ignores sign)."""
    return ((_aroon_up(high, 25) - _aroon_down(low, 25)).abs()).diff().diff().diff()


def f29_uarn_184_aroon_up_cross_above_50_event_d3(high: pd.Series) -> pd.Series:
    """Event: Aroon-Up(25) crossed up through 50 today — recency-of-high midpoint cross."""
    au = _aroon_up(high, 25)
    cond = (au > 50.0) & (au.shift(1) <= 50.0)
    return (cond.astype(float).where(au.notna() & au.shift(1).notna(), np.nan)).diff().diff().diff()


def f29_uarn_185_aroon_up_cross_below_50_event_d3(high: pd.Series) -> pd.Series:
    """Event: Aroon-Up(25) crossed down through 50 today — recency-of-high decay through midpoint."""
    au = _aroon_up(high, 25)
    cond = (au < 50.0) & (au.shift(1) >= 50.0)
    return (cond.astype(float).where(au.notna() & au.shift(1).notna(), np.nan)).diff().diff().diff()


def f29_uarn_186_aroon_down_cross_above_50_event_d3(low: pd.Series) -> pd.Series:
    """Event: Aroon-Down(25) crossed up through 50 today — bearish-recency midpoint cross."""
    ad = _aroon_down(low, 25)
    cond = (ad > 50.0) & (ad.shift(1) <= 50.0)
    return (cond.astype(float).where(ad.notna() & ad.shift(1).notna(), np.nan)).diff().diff().diff()


def f29_uarn_187_aroon_up_on_log_close_25d_d3(close: pd.Series) -> pd.Series:
    """Aroon-Up(25) computed on log-close instead of raw high — log-domain recency-of-max."""
    return (_aroon_up(_safe_log(close), 25)).diff().diff().diff()


def f29_uarn_188_aroon_up_on_smoothed_high_25d_d3(high: pd.Series) -> pd.Series:
    """Aroon-Up(25) computed on 5d-EMA-smoothed-high — denoised recency-of-high (Chande-style smoothed input)."""
    sm = high.ewm(span=WDAYS, adjust=False, min_periods=2).mean()
    return (_aroon_up(sm, 25)).diff().diff().diff()


def f29_uarn_189_aroon_both_above_70_dwell_21d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars in trailing 21d with both Aroon-Up(25) > 70 AND Aroon-Down(25) > 70 — high-energy chop regime."""
    au = _aroon_up(high, 25)
    ad = _aroon_down(low, 25)
    cond = ((au > 70.0) & (ad > 70.0)).astype(float)
    return (cond.rolling(MDAYS, min_periods=WDAYS).sum()).diff().diff().diff()


def f29_uarn_190_aroon_both_below_30_dwell_21d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars in trailing 21d with both Aroon-Up(25) < 30 AND Aroon-Down(25) < 30 — stale-extreme dwell."""
    au = _aroon_up(high, 25)
    ad = _aroon_down(low, 25)
    cond = ((au < 30.0) & (ad < 30.0)).astype(float)
    return (cond.rolling(MDAYS, min_periods=WDAYS).sum()).diff().diff().diff()


def f29_uarn_191_aroon_sum_zscore_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of Aroon-Up(25) + Aroon-Down(25) in 252d — anomalous total recency-state reading."""
    s = _aroon_up(high, 25) + _aroon_down(low, 25)
    return (_rolling_zscore(s, YDAYS, min_periods=QDAYS)).diff().diff().diff()


def f29_uarn_192_aroon_up_long_horizon_100d_d3(high: pd.Series) -> pd.Series:
    """Aroon-Up(100) — multi-month lifecycle recency-of-high signal."""
    return (_aroon_up(high, 100)).diff().diff().diff()


def f29_uarn_193_aroon_down_long_horizon_100d_d3(low: pd.Series) -> pd.Series:
    """Aroon-Down(100) — multi-month lifecycle recency-of-low signal."""
    return (_aroon_down(low, 100)).diff().diff().diff()


def f29_uarn_194_aroon_oscillator_504d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Aroon-Osc(504) — 2-year multi-year regime balance (long-cycle directional bias)."""
    return (_aroon_up(high, 504) - _aroon_down(low, 504)).diff().diff().diff()


def f29_uarn_195_aroon_bars_since_up_100_d3(high: pd.Series) -> pd.Series:
    """Bars since Aroon-Up(25) was last 100 — staleness of most-recent fresh new high."""
    au = _aroon_up(high, 25)
    cond = (au >= 99.999).astype(float)
    return (_bars_since(cond, YDAYS)).diff().diff().diff()


# ============================================================
# Bucket E — Ultimate Oscillator extensions (196-205)
# ============================================================

def f29_uarn_196_uo_bullish_failure_swing_event_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bullish UO failure swing: UO rises above prior 14d UO-peak after a 30- trough — Wilder mirror taxonomy."""
    uo = _ultimate_osc(high, low, close, 7, 14, 28)
    prior_min = uo.rolling(14, min_periods=5).min().shift(1)
    prior_max = uo.rolling(14, min_periods=5).max().shift(1)
    cond = (prior_min < 30.0) & (uo > prior_max)
    return (cond.astype(float).where(uo.notna() & prior_max.notna(), np.nan)).diff().diff().diff()


def f29_uarn_197_uo_short_tf_above_medium_event_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: BP/TR(7) crossed above BP/TR(14) today — short TF leading medium TF (acceleration)."""
    pc = close.shift(1)
    bp = close - pd.concat([low, pc], axis=1).min(axis=1)
    tr = pd.concat([high, pc], axis=1).max(axis=1) - pd.concat([low, pc], axis=1).min(axis=1)
    a = _safe_div(bp.rolling(7, min_periods=3).sum(), tr.rolling(7, min_periods=3).sum())
    b = _safe_div(bp.rolling(14, min_periods=5).sum(), tr.rolling(14, min_periods=5).sum())
    cond = (a > b) & (a.shift(1) <= b.shift(1))
    return (cond.astype(float).where(a.notna() & b.notna() & a.shift(1).notna(), np.nan)).diff().diff().diff()


def f29_uarn_198_uo_medium_minus_long_tf_spread_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """BP/TR(14) − BP/TR(28): medium vs long TF spread — independent middle-vs-back leg signal."""
    pc = close.shift(1)
    bp = close - pd.concat([low, pc], axis=1).min(axis=1)
    tr = pd.concat([high, pc], axis=1).max(axis=1) - pd.concat([low, pc], axis=1).min(axis=1)
    b = _safe_div(bp.rolling(14, min_periods=5).sum(), tr.rolling(14, min_periods=5).sum())
    c = _safe_div(bp.rolling(28, min_periods=10).sum(), tr.rolling(28, min_periods=10).sum())
    return (b - c).diff().diff().diff()


def f29_uarn_199_uo_all_three_tfs_below_midline_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: all three BP/TR(7,14,28) below 0.5 — unanimous-bearish triple-TF alignment."""
    pc = close.shift(1)
    bp = close - pd.concat([low, pc], axis=1).min(axis=1)
    tr = pd.concat([high, pc], axis=1).max(axis=1) - pd.concat([low, pc], axis=1).min(axis=1)
    a = _safe_div(bp.rolling(7, min_periods=3).sum(), tr.rolling(7, min_periods=3).sum())
    b = _safe_div(bp.rolling(14, min_periods=5).sum(), tr.rolling(14, min_periods=5).sum())
    c = _safe_div(bp.rolling(28, min_periods=10).sum(), tr.rolling(28, min_periods=10).sum())
    cond = (a < 0.5) & (b < 0.5) & (c < 0.5)
    return (cond.astype(float).where(a.notna() & b.notna() & c.notna(), np.nan)).diff().diff().diff()


def f29_uarn_200_uo_equal_weights_variant_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """UO with equal weights (1/1/1) across 7/14/28 TFs — neutral-weight variant vs classic 4/2/1."""
    return (_ultimate_osc(high, low, close, 7, 14, 28, w1=1.0, w2=1.0, w3=1.0)).diff().diff().diff()


def f29_uarn_201_uo_back_heavy_weights_variant_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """UO with back-heavy weights (1/2/4) — emphasizes slow TF over fast (different hypothesis)."""
    return (_ultimate_osc(high, low, close, 7, 14, 28, w1=1.0, w2=2.0, w3=4.0)).diff().diff().diff()


def f29_uarn_202_uo_cross_above_50_event_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: UO crossed up through 50 today — momentum-midline transition (bullish)."""
    uo = _ultimate_osc(high, low, close, 7, 14, 28)
    cond = (uo > 50.0) & (uo.shift(1) <= 50.0)
    return (cond.astype(float).where(uo.notna() & uo.shift(1).notna(), np.nan)).diff().diff().diff()


def f29_uarn_203_uo_cross_below_50_event_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: UO crossed down through 50 today — momentum-midline transition (bearish)."""
    uo = _ultimate_osc(high, low, close, 7, 14, 28)
    cond = (uo < 50.0) & (uo.shift(1) >= 50.0)
    return (cond.astype(float).where(uo.notna() & uo.shift(1).notna(), np.nan)).diff().diff().diff()


def f29_uarn_204_uo_bars_since_last_failure_swing_bearish_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since last bearish UO failure swing — staleness of bearish-divergence event."""
    uo = _ultimate_osc(high, low, close, 7, 14, 28)
    prior_max = uo.rolling(14, min_periods=5).max().shift(1)
    prior_min = uo.rolling(14, min_periods=5).min().shift(1)
    fs = ((prior_max > 70.0) & (uo < prior_min)).astype(float)
    return (_bars_since(fs, YDAYS)).diff().diff().diff()


def f29_uarn_205_uo_at_252d_high_minus_uo_now_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """UO value at the 252d-high bar minus current UO — divergence dwell magnitude from peak-day momentum."""
    uo = _ultimate_osc(high, low, close, 7, 14, 28)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = (high >= rmax)
    uo_at_peak = uo.where(at_peak, np.nan).ffill(limit=YDAYS)
    return (uo_at_peak - uo).diff().diff().diff()


# ============================================================
# Bucket F — Vortex extensions (206-220)
# ============================================================

def f29_uarn_206_vortex_vm_pressure_sum_14d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum |+VM| + |-VM| over 14d, normalized by sum TR — total vortex pressure regardless of sign."""
    pc = close.shift(1)
    ph = high.shift(1)
    pl = low.shift(1)
    vm_plus = (high - pl).abs()
    vm_minus = (low - ph).abs()
    tr = pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    s_vm = (vm_plus + vm_minus).rolling(14, min_periods=7).sum()
    s_tr = tr.rolling(14, min_periods=7).sum()
    return (_safe_div(s_vm, s_tr)).diff().diff().diff()


def f29_uarn_207_vortex_normalized_imbalance_14d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(VI+ − VI-) / (VI+ + VI-) at 14d — Chande-style normalized vortex imbalance ∈ [-1, 1]."""
    vp, vm = _vortex(high, low, close, n=14)
    return (_safe_div(vp - vm, vp + vm)).diff().diff().diff()


def f29_uarn_208_vortex_plus_regime_ratio_to_ma63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """VI+(14) / 63d-mean(VI+) — bullish-vortex regime relative to its own quarterly baseline."""
    vp, _ = _vortex(high, low, close, n=14)
    return (_safe_div(vp, vp.rolling(QDAYS, min_periods=MDAYS).mean())).diff().diff().diff()


def f29_uarn_209_vortex_minus_regime_ratio_to_ma63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """VI-(14) / 63d-mean(VI-) — bearish-vortex regime relative to its own quarterly baseline."""
    _, vm = _vortex(high, low, close, n=14)
    return (_safe_div(vm, vm.rolling(QDAYS, min_periods=MDAYS).mean())).diff().diff().diff()


def f29_uarn_210_vortex_diff_macd_style_signal_residual_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """MACD-style residual: Vortex-diff(14) − 9d-EMA(Vortex-diff(14)) — vortex signal-line histogram."""
    vp, vm = _vortex(high, low, close, n=14)
    diff = vp - vm
    sig = diff.ewm(span=9, adjust=False, min_periods=4).mean()
    return (diff - sig).diff().diff().diff()


def f29_uarn_211_vortex_signal_line_cross_event_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: Vortex-diff(14) crossed below its 9d-EMA signal line — MACD-style bearish signal."""
    vp, vm = _vortex(high, low, close, n=14)
    diff = vp - vm
    sig = diff.ewm(span=9, adjust=False, min_periods=4).mean()
    cond = (diff < sig) & (diff.shift(1) >= sig.shift(1))
    return (cond.astype(float).where(diff.notna() & sig.notna() & diff.shift(1).notna(), np.nan)).diff().diff().diff()


def f29_uarn_212_vortex_plus_5d_slope_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5d slope of VI+(14) — bullish vortex acceleration (counterpart to existing VI- slope)."""
    vp, _ = _vortex(high, low, close, n=14)
    return (_rolling_slope(vp, WDAYS, min_periods=3)).diff().diff().diff()


def f29_uarn_213_vortex_long_horizon_50d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """VI+(50) − VI-(50) — long-horizon vortex directional balance (multi-month regime variant)."""
    vp, vm = _vortex(high, low, close, n=50)
    return (vp - vm).diff().diff().diff()


def f29_uarn_214_vortex_very_long_horizon_100d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """VI+(100) − VI-(100) — very-long-horizon vortex (multi-month lifecycle regime)."""
    vp, vm = _vortex(high, low, close, n=100)
    return (vp - vm).diff().diff().diff()


def f29_uarn_215_vortex_minus_above_one_streak_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Consecutive-bar streak of VI-(14) > 1.0 — bearish-vortex persistence length."""
    _, vm = _vortex(high, low, close, n=14)
    above = (vm > 1.0).astype(float).values
    n = len(above)
    out = np.full(n, np.nan, dtype=float)
    streak = 0
    for i in range(n):
        if pd.isna(vm.iat[i]):
            streak = 0
            out[i] = np.nan
        else:
            streak = streak + 1 if above[i] > 0 else 0
            out[i] = float(streak)
    return (pd.Series(out, index=vm.index)).diff().diff().diff()


def f29_uarn_216_vortex_bullish_cross_event_14d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: VI+ crossed above VI- today (14d) — bullish vortex flip (counterpart to existing bearish cross)."""
    vp, vm = _vortex(high, low, close, n=14)
    cond = (vp > vm) & (vp.shift(1) <= vm.shift(1))
    return (cond.astype(float).where(vp.notna() & vm.notna() & vp.shift(1).notna(), np.nan)).diff().diff().diff()


def f29_uarn_217_vortex_bars_since_last_bullish_cross_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since last VI+ > VI- bullish cross — staleness of bullish-vortex ignition."""
    vp, vm = _vortex(high, low, close, n=14)
    cross = ((vp > vm) & (vp.shift(1) <= vm.shift(1))).astype(float)
    return (_bars_since(cross, YDAYS)).diff().diff().diff()


def f29_uarn_218_vortex_diff_amplitude_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63d max − min of Vortex-diff(14) — directional-pressure oscillation amplitude."""
    vp, vm = _vortex(high, low, close, n=14)
    diff = vp - vm
    return (diff.rolling(QDAYS, min_periods=MDAYS).max() - diff.rolling(QDAYS, min_periods=MDAYS).min()).diff().diff().diff()


def f29_uarn_219_vortex_minus_zscore_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of VI-(14) in 252d window — anomalously hot bearish-vortex reading."""
    _, vm = _vortex(high, low, close, n=14)
    return (_rolling_zscore(vm, YDAYS, min_periods=QDAYS)).diff().diff().diff()


def f29_uarn_220_vortex_diff_negative_dwell_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars in trailing 63d with Vortex-diff(14) < 0 — sustained bearish-vortex regime dwell."""
    vp, vm = _vortex(high, low, close, n=14)
    diff = vp - vm
    return ((diff < 0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()).diff().diff().diff()


# ============================================================
# Bucket G — Choppiness extensions and CI x ADX alignment (221-225)
# ============================================================

def f29_uarn_221_choppiness_roc_5d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5d ROC of Choppiness(14) — regime-change velocity (counterpart to slope-based)."""
    ci = _choppiness(high, low, close, n=14)
    return (ci - ci.shift(WDAYS)).diff().diff().diff()


def f29_uarn_222_choppiness_cross_below_38_event_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: Choppiness(14) crossed down through 38.2 today — chop-to-trend transition (Fib pivot)."""
    ci = _choppiness(high, low, close, n=14)
    cond = (ci < 38.2) & (ci.shift(1) >= 38.2)
    return (cond.astype(float).where(ci.notna() & ci.shift(1).notna(), np.nan)).diff().diff().diff()


def f29_uarn_223_choppiness_high_with_adx_low_alignment_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: Choppiness(14) > 60 AND ADX(14) < 20 — confirmed double-range-bound regime."""
    ci = _choppiness(high, low, close, n=14)
    _, _, adx = _dm_components(high, low, close, n=14)
    cond = (ci > 60.0) & (adx < 20.0)
    return (cond.astype(float).where(ci.notna() & adx.notna(), np.nan)).diff().diff().diff()


def f29_uarn_224_choppiness_disagreement_with_adx_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """|Choppiness(14)/100 − (1 − ADX(14)/100)|: disagreement between two regime-classifiers."""
    ci = _choppiness(high, low, close, n=14)
    _, _, adx = _dm_components(high, low, close, n=14)
    return ((ci / 100.0 - (1.0 - adx / 100.0)).abs()).diff().diff().diff()


def f29_uarn_225_choppiness_cross_above_50_event_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: Choppiness(14) crossed up through 50 today — midline regime transition (chop ignition)."""
    ci = _choppiness(high, low, close, n=14)
    cond = (ci > 50.0) & (ci.shift(1) <= 50.0)
    return (cond.astype(float).where(ci.notna() & ci.shift(1).notna(), np.nan)).diff().diff().diff()


# ============================================================
#                         REGISTRY 151-225
# ============================================================

ULTIMATE_AROON_VORTEX_D3_REGISTRY_151_225 = {
    "f29_uarn_151_adxr_classic_14d_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_151_adxr_classic_14d_d3},
    "f29_uarn_152_adxr_long_25d_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_152_adxr_long_25d_d3},
    "f29_uarn_153_adxr_minus_adx_residual_14d_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_153_adxr_minus_adx_residual_14d_d3},
    "f29_uarn_154_adxr_above_25_strong_trend_indicator_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_154_adxr_above_25_strong_trend_indicator_d3},
    "f29_uarn_155_adxr_below_20_no_trend_indicator_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_155_adxr_below_20_no_trend_indicator_d3},
    "f29_uarn_156_adxr_cross_above_25_event_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_156_adxr_cross_above_25_event_d3},
    "f29_uarn_157_adxr_5d_slope_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_157_adxr_5d_slope_d3},
    "f29_uarn_158_adxr_dwell_above_25_in_63d_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_158_adxr_dwell_above_25_in_63d_d3},
    "f29_uarn_159_adxr_zscore_252d_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_159_adxr_zscore_252d_d3},
    "f29_uarn_160_adxr_peak_decay_from_63d_max_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_160_adxr_peak_decay_from_63d_max_d3},
    "f29_uarn_161_plus_dm_raw_wilder14_d3": {"inputs": ["high", "low"], "func": f29_uarn_161_plus_dm_raw_wilder14_d3},
    "f29_uarn_162_minus_dm_raw_wilder14_d3": {"inputs": ["high", "low"], "func": f29_uarn_162_minus_dm_raw_wilder14_d3},
    "f29_uarn_163_dm_total_wilder14_d3": {"inputs": ["high", "low"], "func": f29_uarn_163_dm_total_wilder14_d3},
    "f29_uarn_164_dm_raw_imbalance_chande_d3": {"inputs": ["high", "low"], "func": f29_uarn_164_dm_raw_imbalance_chande_d3},
    "f29_uarn_165_di_sum_14d_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_165_di_sum_14d_d3},
    "f29_uarn_166_atr_wilder_to_dm_total_ratio_14d_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_166_atr_wilder_to_dm_total_ratio_14d_d3},
    "f29_uarn_167_dx_raw_no_adx_smoothing_14d_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_167_dx_raw_no_adx_smoothing_14d_d3},
    "f29_uarn_168_plus_dm_to_minus_dm_ratio_14d_d3": {"inputs": ["high", "low"], "func": f29_uarn_168_plus_dm_to_minus_dm_ratio_14d_d3},
    "f29_uarn_169_minus_dm_zscore_252d_d3": {"inputs": ["high", "low"], "func": f29_uarn_169_minus_dm_zscore_252d_d3},
    "f29_uarn_170_dm_total_at_252d_high_value_d3": {"inputs": ["high", "low"], "func": f29_uarn_170_dm_total_at_252d_high_value_d3},
    "f29_uarn_171_adx_cross_above_20_event_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_171_adx_cross_above_20_event_d3},
    "f29_uarn_172_adx_cross_below_20_event_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_172_adx_cross_below_20_event_d3},
    "f29_uarn_173_adx_cross_above_25_event_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_173_adx_cross_above_25_event_d3},
    "f29_uarn_174_adx_cross_below_25_event_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_174_adx_cross_below_25_event_d3},
    "f29_uarn_175_adx_hook_continuation_pattern_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_175_adx_hook_continuation_pattern_d3},
    "f29_uarn_176_adx_post_cross25_persistence_21d_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_176_adx_post_cross25_persistence_21d_d3},
    "f29_uarn_177_adx_bars_since_last_cross_25_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_177_adx_bars_since_last_cross_25_d3},
    "f29_uarn_178_adx_local_trough_event_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_178_adx_local_trough_event_d3},
    "f29_uarn_179_adx_local_peak_event_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_179_adx_local_peak_event_d3},
    "f29_uarn_180_adx_reset_bars_below_15_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_180_adx_reset_bars_below_15_d3},
    "f29_uarn_181_aroon_sum_up_plus_down_25d_d3": {"inputs": ["high", "low"], "func": f29_uarn_181_aroon_sum_up_plus_down_25d_d3},
    "f29_uarn_182_aroon_normalized_imbalance_25d_d3": {"inputs": ["high", "low"], "func": f29_uarn_182_aroon_normalized_imbalance_25d_d3},
    "f29_uarn_183_aroon_osc_absolute_25d_d3": {"inputs": ["high", "low"], "func": f29_uarn_183_aroon_osc_absolute_25d_d3},
    "f29_uarn_184_aroon_up_cross_above_50_event_d3": {"inputs": ["high"], "func": f29_uarn_184_aroon_up_cross_above_50_event_d3},
    "f29_uarn_185_aroon_up_cross_below_50_event_d3": {"inputs": ["high"], "func": f29_uarn_185_aroon_up_cross_below_50_event_d3},
    "f29_uarn_186_aroon_down_cross_above_50_event_d3": {"inputs": ["low"], "func": f29_uarn_186_aroon_down_cross_above_50_event_d3},
    "f29_uarn_187_aroon_up_on_log_close_25d_d3": {"inputs": ["close"], "func": f29_uarn_187_aroon_up_on_log_close_25d_d3},
    "f29_uarn_188_aroon_up_on_smoothed_high_25d_d3": {"inputs": ["high"], "func": f29_uarn_188_aroon_up_on_smoothed_high_25d_d3},
    "f29_uarn_189_aroon_both_above_70_dwell_21d_d3": {"inputs": ["high", "low"], "func": f29_uarn_189_aroon_both_above_70_dwell_21d_d3},
    "f29_uarn_190_aroon_both_below_30_dwell_21d_d3": {"inputs": ["high", "low"], "func": f29_uarn_190_aroon_both_below_30_dwell_21d_d3},
    "f29_uarn_191_aroon_sum_zscore_252d_d3": {"inputs": ["high", "low"], "func": f29_uarn_191_aroon_sum_zscore_252d_d3},
    "f29_uarn_192_aroon_up_long_horizon_100d_d3": {"inputs": ["high"], "func": f29_uarn_192_aroon_up_long_horizon_100d_d3},
    "f29_uarn_193_aroon_down_long_horizon_100d_d3": {"inputs": ["low"], "func": f29_uarn_193_aroon_down_long_horizon_100d_d3},
    "f29_uarn_194_aroon_oscillator_504d_d3": {"inputs": ["high", "low"], "func": f29_uarn_194_aroon_oscillator_504d_d3},
    "f29_uarn_195_aroon_bars_since_up_100_d3": {"inputs": ["high"], "func": f29_uarn_195_aroon_bars_since_up_100_d3},
    "f29_uarn_196_uo_bullish_failure_swing_event_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_196_uo_bullish_failure_swing_event_d3},
    "f29_uarn_197_uo_short_tf_above_medium_event_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_197_uo_short_tf_above_medium_event_d3},
    "f29_uarn_198_uo_medium_minus_long_tf_spread_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_198_uo_medium_minus_long_tf_spread_d3},
    "f29_uarn_199_uo_all_three_tfs_below_midline_indicator_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_199_uo_all_three_tfs_below_midline_indicator_d3},
    "f29_uarn_200_uo_equal_weights_variant_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_200_uo_equal_weights_variant_d3},
    "f29_uarn_201_uo_back_heavy_weights_variant_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_201_uo_back_heavy_weights_variant_d3},
    "f29_uarn_202_uo_cross_above_50_event_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_202_uo_cross_above_50_event_d3},
    "f29_uarn_203_uo_cross_below_50_event_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_203_uo_cross_below_50_event_d3},
    "f29_uarn_204_uo_bars_since_last_failure_swing_bearish_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_204_uo_bars_since_last_failure_swing_bearish_d3},
    "f29_uarn_205_uo_at_252d_high_minus_uo_now_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_205_uo_at_252d_high_minus_uo_now_d3},
    "f29_uarn_206_vortex_vm_pressure_sum_14d_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_206_vortex_vm_pressure_sum_14d_d3},
    "f29_uarn_207_vortex_normalized_imbalance_14d_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_207_vortex_normalized_imbalance_14d_d3},
    "f29_uarn_208_vortex_plus_regime_ratio_to_ma63_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_208_vortex_plus_regime_ratio_to_ma63_d3},
    "f29_uarn_209_vortex_minus_regime_ratio_to_ma63_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_209_vortex_minus_regime_ratio_to_ma63_d3},
    "f29_uarn_210_vortex_diff_macd_style_signal_residual_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_210_vortex_diff_macd_style_signal_residual_d3},
    "f29_uarn_211_vortex_signal_line_cross_event_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_211_vortex_signal_line_cross_event_d3},
    "f29_uarn_212_vortex_plus_5d_slope_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_212_vortex_plus_5d_slope_d3},
    "f29_uarn_213_vortex_long_horizon_50d_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_213_vortex_long_horizon_50d_d3},
    "f29_uarn_214_vortex_very_long_horizon_100d_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_214_vortex_very_long_horizon_100d_d3},
    "f29_uarn_215_vortex_minus_above_one_streak_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_215_vortex_minus_above_one_streak_d3},
    "f29_uarn_216_vortex_bullish_cross_event_14d_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_216_vortex_bullish_cross_event_14d_d3},
    "f29_uarn_217_vortex_bars_since_last_bullish_cross_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_217_vortex_bars_since_last_bullish_cross_d3},
    "f29_uarn_218_vortex_diff_amplitude_63d_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_218_vortex_diff_amplitude_63d_d3},
    "f29_uarn_219_vortex_minus_zscore_252d_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_219_vortex_minus_zscore_252d_d3},
    "f29_uarn_220_vortex_diff_negative_dwell_63d_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_220_vortex_diff_negative_dwell_63d_d3},
    "f29_uarn_221_choppiness_roc_5d_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_221_choppiness_roc_5d_d3},
    "f29_uarn_222_choppiness_cross_below_38_event_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_222_choppiness_cross_below_38_event_d3},
    "f29_uarn_223_choppiness_high_with_adx_low_alignment_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_223_choppiness_high_with_adx_low_alignment_d3},
    "f29_uarn_224_choppiness_disagreement_with_adx_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_224_choppiness_disagreement_with_adx_d3},
    "f29_uarn_225_choppiness_cross_above_50_event_d3": {"inputs": ["high", "low", "close"], "func": f29_uarn_225_choppiness_cross_above_50_event_d3},
}
