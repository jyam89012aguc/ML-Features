"""ultimate_aroon_vortex d1 features 301-375 — Pipeline 1b-technical.

Third batch: 150 NEW atomic-leaning hypotheses (301-450). This file holds
indices 301-375. Continues the family with single-bar event detectors,
rolling-extreme atomics across distinct horizons, long-horizon dispersion,
recency-of-event atomics not in 266-280, and distribution-phase fingerprints
that read one indicator at a time. ~85% atomic single-source signals;
~15% canonical multi-indicator composites recognised in tape-reading practice
(Wilder failure swings, ADX-hook formations, Dorsey reversal bulge confirms).

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

def f29_uarn_301_di_minus_single_bar_cross_above_di_plus_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Single-bar event: DI- crossed above DI+ today (one-bar bearish DM crossover marker)."""
    p, m, _ = _dm_components(high, low, close, n=14)
    cross = (m > p) & (m.shift(1) <= p.shift(1))
    return cross.astype(float).where(p.notna() & m.notna(), np.nan).diff()

def f29_uarn_302_di_plus_first_day_below_20_after_strong_run_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """First day DI+ drops below 20 after a 21d run of DI+ above 30 — single-bar leadership-loss event."""
    p, _, _ = _dm_components(high, low, close, n=14)
    sustained = p.rolling(MDAYS, min_periods=10).min() > 30.0
    cond = (p < 20.0) & sustained.shift(1).fillna(False)
    return cond.astype(float).where(p.notna(), np.nan).diff()

def f29_uarn_303_aroon_up_failure_to_reach_100_on_new_high_d1(high: pd.Series) -> pd.Series:
    """Bar that prints a 21d new high while Aroon-Up(25) is below 100 — lower-high distribution marker."""
    au = _aroon_up(high, 25)
    new_high_21 = high >= high.rolling(MDAYS, min_periods=10).max()
    cond = new_high_21 & (au < 100.0)
    return cond.astype(float).where(au.notna(), np.nan).diff()

def f29_uarn_304_aroon_down_100_with_price_near_52w_high_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Aroon-Down(25)=100 AND close-high within 5% of 252d max — silent exhaustion (new 25d low at top)."""
    ad = _aroon_down(low, 25)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = high >= 0.95 * rmax
    cond = (ad >= 99.999) & near
    return cond.astype(float).where(ad.notna() & rmax.notna(), np.nan).diff()

def f29_uarn_305_uo_centerline_rejection_from_above_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Single-bar event: UO crossed 50 from above today (centerline-rejection / momentum-loss marker)."""
    uo = _ultimate_osc(high, low, close, 7, 14, 28)
    cond = (uo < 50.0) & (uo.shift(1) >= 50.0)
    return cond.astype(float).where(uo.notna(), np.nan).diff()

def f29_uarn_306_uo_lower_high_versus_price_higher_high_event_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Single-bar UO bearish-divergence event: price prints 21d new high, UO is below its 21d max."""
    uo = _ultimate_osc(high, low, close, 7, 14, 28)
    price_hh = high >= high.rolling(MDAYS, min_periods=10).max()
    uo_lt_recent_max = uo < uo.rolling(MDAYS, min_periods=10).max()
    cond = price_hh & uo_lt_recent_max
    return cond.astype(float).where(uo.notna(), np.nan).diff()

def f29_uarn_307_mass_index_dorsey_trigger_cross_below_265_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Dorsey reversal-bulge atomic confirm: today MI crosses below 26.5 after exceeding 27 in trailing 21d."""
    mi = _mass_index(high, low, n=25, ema_n=9)
    bulge = mi.rolling(MDAYS, min_periods=WDAYS).max() > 27.0
    cond = bulge & (mi < 26.5) & (mi.shift(1) >= 26.5)
    return cond.astype(float).where(mi.notna(), np.nan).diff()

def f29_uarn_308_choppiness_first_day_above_50_from_below_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Single-bar event: Choppiness(14) crossed above 50 today from below — regime-flip primer."""
    ci = _choppiness(high, low, close, n=14)
    cond = (ci > 50.0) & (ci.shift(1) <= 50.0)
    return cond.astype(float).where(ci.notna(), np.nan).diff()

def f29_uarn_309_vortex_vi_plus_cross_below_one_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Single-bar event: VI+(14) crossed below 1.0 today (bullish-VM-mass loss against TR-mass)."""
    vp, _ = _vortex(high, low, close, n=14)
    cond = (vp < 1.0) & (vp.shift(1) >= 1.0)
    return cond.astype(float).where(vp.notna(), np.nan).diff()

def f29_uarn_310_vortex_vi_minus_cross_above_one_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Single-bar event: VI-(14) crossed above 1.0 today (bearish-VM-mass dominance event)."""
    _, vm = _vortex(high, low, close, n=14)
    cond = (vm > 1.0) & (vm.shift(1) <= 1.0)
    return cond.astype(float).where(vm.notna(), np.nan).diff()

def f29_uarn_311_adx_first_above_25_after_long_below_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """First-day-above-25 event: ADX crosses above 25 today, ADX was below 25 for entire trailing 63d."""
    _, _, adx = _dm_components(high, low, close, n=14)
    sustained_low = adx.rolling(QDAYS, min_periods=MDAYS).max() < 25.0
    cond = (adx > 25.0) & sustained_low.shift(1).fillna(False)
    return cond.astype(float).where(adx.notna(), np.nan).diff()

def f29_uarn_312_aroon_oscillator_first_negative_after_long_positive_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """First-day-negative event: Aroon-Osc(25) goes negative today after 63d of staying positive."""
    osc = _aroon_up(high, 25) - _aroon_down(low, 25)
    sustained_pos = osc.rolling(QDAYS, min_periods=MDAYS).min() > 0
    cond = (osc < 0) & sustained_pos.shift(1).fillna(False)
    return cond.astype(float).where(osc.notna(), np.nan).diff()

def f29_uarn_313_uo_first_day_below_30_after_long_above_50_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """First-day-below-30 event after 63d of UO staying above 50 — collapse-from-strength single-bar marker."""
    uo = _ultimate_osc(high, low, close, 7, 14, 28)
    sustained_strong = uo.rolling(QDAYS, min_periods=MDAYS).min() > 50.0
    cond = (uo < 30.0) & sustained_strong.shift(1).fillna(False)
    return cond.astype(float).where(uo.notna(), np.nan).diff()

def f29_uarn_314_vortex_diff_first_negative_after_long_positive_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """First-day-negative event for Vortex-diff after 63d of staying positive — bull-vortex regime end."""
    vp, vm = _vortex(high, low, close, n=14)
    d = vp - vm
    sustained_pos = d.rolling(QDAYS, min_periods=MDAYS).min() > 0
    cond = (d < 0) & sustained_pos.shift(1).fillna(False)
    return cond.astype(float).where(d.notna(), np.nan).diff()

def f29_uarn_315_choppiness_first_day_above_62_after_long_below_38_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """First-day-above-61.8 event after 63d of CI staying below 38.2 — regime collapse from clean trend."""
    ci = _choppiness(high, low, close, n=14)
    sustained_trend = ci.rolling(QDAYS, min_periods=MDAYS).max() < 38.2
    cond = (ci > 61.8) & sustained_trend.shift(1).fillna(False)
    return cond.astype(float).where(ci.notna(), np.nan).diff()

def f29_uarn_316_adx_max_trailing_21d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Max ADX(14) in trailing 21d — monthly trend-strength peak reading (recent peak intensity)."""
    _, _, adx = _dm_components(high, low, close, n=14)
    return adx.rolling(MDAYS, min_periods=WDAYS).max().diff()

def f29_uarn_317_adx_max_trailing_63d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Max ADX(14) in trailing 63d — quarterly trend-strength peak (medium-horizon highwater)."""
    _, _, adx = _dm_components(high, low, close, n=14)
    return adx.rolling(QDAYS, min_periods=MDAYS).max().diff()

def f29_uarn_318_adx_max_trailing_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Max ADX(14) in trailing 252d — annual trend-strength highwater (regime peak)."""
    _, _, adx = _dm_components(high, low, close, n=14)
    return adx.rolling(YDAYS, min_periods=QDAYS).max().diff()

def f29_uarn_319_di_minus_max_trailing_21d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Max DI-(14) in trailing 21d — monthly bearish-DM peak intensity."""
    _, m, _ = _dm_components(high, low, close, n=14)
    return m.rolling(MDAYS, min_periods=WDAYS).max().diff()

def f29_uarn_320_di_minus_max_trailing_63d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Max DI-(14) in trailing 63d — quarterly bearish-DM highwater."""
    _, m, _ = _dm_components(high, low, close, n=14)
    return m.rolling(QDAYS, min_periods=MDAYS).max().diff()

def f29_uarn_321_di_minus_max_trailing_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Max DI-(14) in trailing 252d — annual bearish-DM highwater (most-stressed reading of year)."""
    _, m, _ = _dm_components(high, low, close, n=14)
    return m.rolling(YDAYS, min_periods=QDAYS).max().diff()

def f29_uarn_322_aroon_up_min_trailing_63d_d1(high: pd.Series) -> pd.Series:
    """Min Aroon-Up(25) in trailing 63d — deep-retracement marker (smallest recency-of-high)."""
    return _aroon_up(high, 25).rolling(QDAYS, min_periods=MDAYS).min().diff()

def f29_uarn_323_choppiness_max_trailing_63d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Max Choppiness(14) in trailing 63d — quarterly ranging-regime extreme."""
    return _choppiness(high, low, close, n=14).rolling(QDAYS, min_periods=MDAYS).max().diff()

def f29_uarn_324_mass_index_max_trailing_252d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Max Mass-Index(25) in trailing 252d — annual range-expansion highwater (peak bulge of year)."""
    return _mass_index(high, low, n=25, ema_n=9).rolling(YDAYS, min_periods=QDAYS).max().diff()

def f29_uarn_325_uo_min_trailing_21d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Min UO in trailing 21d — monthly deep-oversold history reading."""
    return _ultimate_osc(high, low, close, 7, 14, 28).rolling(MDAYS, min_periods=WDAYS).min().diff()

def f29_uarn_326_uo_min_trailing_63d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Min UO in trailing 63d — quarterly deep-oversold history reading."""
    return _ultimate_osc(high, low, close, 7, 14, 28).rolling(QDAYS, min_periods=MDAYS).min().diff()

def f29_uarn_327_vortex_diff_max_trailing_63d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Max Vortex-diff(14) in trailing 63d — quarterly bullish-vortex highwater (regime peak)."""
    vp, vm = _vortex(high, low, close, n=14)
    return (vp - vm).rolling(QDAYS, min_periods=MDAYS).max().diff()

def f29_uarn_328_vortex_diff_min_trailing_63d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Min Vortex-diff(14) in trailing 63d — quarterly bearish-vortex extreme (deepest bear-VM)."""
    vp, vm = _vortex(high, low, close, n=14)
    return (vp - vm).rolling(QDAYS, min_periods=MDAYS).min().diff()

def f29_uarn_329_adxr_max_trailing_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Max ADXR(14) in trailing 252d — annual smoothed-trend-rating peak."""
    return _adxr(high, low, close, n=14).rolling(YDAYS, min_periods=QDAYS).max().diff()

def f29_uarn_330_di_plus_min_trailing_63d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Min DI+(14) in trailing 63d — deepest bullish-DM trough of the quarter (weakness-extreme)."""
    p, _, _ = _dm_components(high, low, close, n=14)
    return p.rolling(QDAYS, min_periods=MDAYS).min().diff()

def f29_uarn_331_adx_50_minus_252_spread_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ADX(50) − ADX(252): medium vs annual trend-strength spread (long-horizon dispersion)."""
    _, _, a50 = _dm_components(high, low, close, n=50)
    _, _, a252 = _dm_components(high, low, close, n=252)
    return (a50 - a252).diff()

def f29_uarn_332_di_plus_50_minus_252_spread_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """DI+(50) − DI+(252): medium vs annual bullish-DM spread."""
    p50, _, _ = _dm_components(high, low, close, n=50)
    p252, _, _ = _dm_components(high, low, close, n=252)
    return (p50 - p252).diff()

def f29_uarn_333_di_minus_50_minus_252_spread_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """DI-(50) − DI-(252): medium vs annual bearish-DM spread (long-horizon bear-DM-leading-bull)."""
    _, m50, _ = _dm_components(high, low, close, n=50)
    _, m252, _ = _dm_components(high, low, close, n=252)
    return (m50 - m252).diff()

def f29_uarn_334_vortex_diff_14_minus_50_spread_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Vortex-diff(14) − Vortex-diff(50): short vs medium vortex-bias dispersion."""
    vp14, vm14 = _vortex(high, low, close, n=14)
    vp50, vm50 = _vortex(high, low, close, n=50)
    return (vp14 - vm14 - (vp50 - vm50)).diff()

def f29_uarn_335_aroon_up_25_minus_100_spread_d1(high: pd.Series) -> pd.Series:
    """Aroon-Up(25) − Aroon-Up(100): monthly vs quarterly recency-of-high spread."""
    return (_aroon_up(high, 25) - _aroon_up(high, 100)).diff()

def f29_uarn_336_aroon_down_25_minus_100_spread_d1(low: pd.Series) -> pd.Series:
    """Aroon-Down(25) − Aroon-Down(100): monthly vs quarterly recency-of-low spread."""
    return (_aroon_down(low, 25) - _aroon_down(low, 100)).diff()

def f29_uarn_337_choppiness_25_minus_252_spread_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Choppiness(25) − Choppiness(252): monthly vs annual regime spread."""
    return (_choppiness(high, low, close, n=25) - _choppiness(high, low, close, n=252)).diff()

def f29_uarn_338_mass_index_15_minus_50_spread_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """MI(15) − MI(50): short vs long-horizon range-expansion sensor disagreement."""
    return (_mass_index(high, low, n=15, ema_n=9) - _mass_index(high, low, n=50, ema_n=9)).diff()

def f29_uarn_339_uo_with_long_horizon_14_28_56_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """UO with longer timeframes (14/28/56) — slow-Williams composite for multi-month exhaustion."""
    return _ultimate_osc(high, low, close, 14, 28, 56).diff()

def f29_uarn_340_uo_short_minus_long_param_spread_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """UO(7,14,28) − UO(14,28,56): horizon-extension UO spread (short vs long param-set)."""
    short = _ultimate_osc(high, low, close, 7, 14, 28)
    long = _ultimate_osc(high, low, close, 14, 28, 56)
    return (short - long).diff()

def f29_uarn_341_adxr_50_minus_252_spread_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ADXR(50) − ADXR(252): medium vs annual smoothed-trend-rating spread."""
    return (_adxr(high, low, close, n=50) - _adxr(high, low, close, n=252)).diff()

def f29_uarn_342_vortex_plus_horizon_50_minus_252_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """VI+(50) − VI+(252): bullish-vortex medium vs annual horizon spread."""
    vp50, _ = _vortex(high, low, close, n=50)
    vp252, _ = _vortex(high, low, close, n=252)
    return (vp50 - vp252).diff()

def f29_uarn_343_vortex_minus_horizon_50_minus_252_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """VI-(50) − VI-(252): bearish-vortex medium vs annual horizon spread."""
    _, vm50 = _vortex(high, low, close, n=50)
    _, vm252 = _vortex(high, low, close, n=252)
    return (vm50 - vm252).diff()

def f29_uarn_344_di_balance_horizon_dispersion_3way_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Std of (DI+−DI-) across n in {14, 50, 252} — three-horizon directional-balance dispersion."""
    p14, m14, _ = _dm_components(high, low, close, n=14)
    p50, m50, _ = _dm_components(high, low, close, n=50)
    p252, m252, _ = _dm_components(high, low, close, n=252)
    df = pd.concat([(p14 - m14).rename('h14'), (p50 - m50).rename('h50'), (p252 - m252).rename('h252')], axis=1)
    return df.std(axis=1).diff()

def f29_uarn_345_aroon_osc_3horizon_sign_count_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of positive Aroon-Osc across n in {25, 100, 252} — multi-horizon directional-agreement count."""
    o25 = _aroon_up(high, 25) - _aroon_down(low, 25)
    o100 = _aroon_up(high, 100) - _aroon_down(low, 100)
    o252 = _aroon_up(high, 252) - _aroon_down(low, 252)
    pieces = [(o25 > 0).astype(float).rename('a'), (o100 > 0).astype(float).rename('b'), (o252 > 0).astype(float).rename('c')]
    return pd.concat(pieces, axis=1).sum(axis=1).diff()

def f29_uarn_346_bars_since_last_di_plus_above_25_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since DI+(14) was last > 25 — recency of any meaningful bullish-DM reading."""
    p, _, _ = _dm_components(high, low, close, n=14)
    return _bars_since((p > 25.0).astype(float), YDAYS).diff()

def f29_uarn_347_bars_since_last_aroon_up_100_d1(high: pd.Series) -> pd.Series:
    """Bars since Aroon-Up(25) was last 100 — recency of fresh 25d new-high event."""
    au = _aroon_up(high, 25)
    return _bars_since((au >= 99.999).astype(float), YDAYS).diff()

def f29_uarn_348_bars_since_last_vortex_bullish_cross_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since last VI+ crossed above VI- — recency of bullish vortex cross."""
    vp, vm = _vortex(high, low, close, n=14)
    cross = (vp > vm) & (vp.shift(1) <= vm.shift(1))
    return _bars_since(cross.astype(float), YDAYS).diff()

def f29_uarn_349_bars_since_last_vortex_bearish_cross_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since last VI- crossed above VI+ — recency of bearish vortex cross."""
    vp, vm = _vortex(high, low, close, n=14)
    cross = (vm > vp) & (vm.shift(1) <= vp.shift(1))
    return _bars_since(cross.astype(float), YDAYS).diff()

def f29_uarn_350_bars_since_last_choppiness_below_38_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since CI(14) was last < 38.2 — recency of clean-trending regime."""
    ci = _choppiness(high, low, close, n=14)
    return _bars_since((ci < 38.2).astype(float), YDAYS).diff()

def f29_uarn_351_bars_since_last_choppiness_above_50_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since CI(14) was last > 50 — recency of any range-side regime tilt."""
    ci = _choppiness(high, low, close, n=14)
    return _bars_since((ci > 50.0).astype(float), YDAYS).diff()

def f29_uarn_352_bars_since_last_di_minus_above_di_plus_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since DI- was last > DI+ — recency of bearish-dominant DI regime."""
    p, m, _ = _dm_components(high, low, close, n=14)
    return _bars_since((m > p).astype(float), YDAYS).diff()

def f29_uarn_353_bars_since_last_uo_above_50_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since UO was last above the 50 centerline — recency of upside-momentum regime."""
    uo = _ultimate_osc(high, low, close, 7, 14, 28)
    return _bars_since((uo > 50.0).astype(float), YDAYS).diff()

def f29_uarn_354_bars_since_last_mass_index_above_265_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars since MI(25) was last > 26.5 — recency of Dorsey-trigger-line tag."""
    mi = _mass_index(high, low, n=25, ema_n=9)
    return _bars_since((mi > 26.5).astype(float), YDAYS).diff()

def f29_uarn_355_bars_since_last_adxr_above_30_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since ADXR(14) was last > 30 — recency of well-established smoothed-trend regime."""
    a = _adxr(high, low, close, n=14)
    return _bars_since((a > 30.0).astype(float), YDAYS).diff()

def f29_uarn_356_bars_since_last_aroon_osc_negative_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars since Aroon-Osc(25) was last negative — recency of bearish-recency regime."""
    osc = _aroon_up(high, 25) - _aroon_down(low, 25)
    return _bars_since((osc < 0).astype(float), YDAYS).diff()

def f29_uarn_357_bars_since_last_vortex_diff_negative_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since Vortex-diff(14) was last negative — recency of bearish-vortex regime."""
    vp, vm = _vortex(high, low, close, n=14)
    return _bars_since((vp - vm < 0).astype(float), YDAYS).diff()

def f29_uarn_358_bars_since_last_adx_local_peak_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since last ADX(14) local-peak (ADX higher than both neighbors) — recency of last trend top."""
    _, _, adx = _dm_components(high, low, close, n=14)
    peak = (adx.shift(1) > adx) & (adx.shift(1) > adx.shift(2))
    return _bars_since(peak.astype(float).fillna(0.0), YDAYS).diff()

def f29_uarn_359_bars_since_last_di_minus_local_peak_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since last DI-(14) local-peak — recency of last bearish-DM peak."""
    _, m, _ = _dm_components(high, low, close, n=14)
    peak = (m.shift(1) > m) & (m.shift(1) > m.shift(2))
    return _bars_since(peak.astype(float).fillna(0.0), YDAYS).diff()

def f29_uarn_360_bars_since_last_uo_centerline_rejection_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since UO last crossed 50 from above (centerline-rejection event) — distribution staleness."""
    uo = _ultimate_osc(high, low, close, 7, 14, 28)
    cond = (uo < 50.0) & (uo.shift(1) >= 50.0)
    return _bars_since(cond.astype(float).fillna(0.0), YDAYS).diff()

def f29_uarn_361_di_minus_above_25_with_adx_rising_count_21d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars in trailing 21d where DI- > 25 AND ADX rising — bearish-trend-strengthening dwell."""
    _, m, adx = _dm_components(high, low, close, n=14)
    cond = (m > 25.0) & (adx.diff() > 0)
    return cond.astype(float).rolling(MDAYS, min_periods=WDAYS).sum().diff()

def f29_uarn_362_adx_rising_with_close_lower_low_count_21d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count in trailing 21d of bars where ADX rising AND close prints 21d new low — strengthening down-trend dwell."""
    _, _, adx = _dm_components(high, low, close, n=14)
    new_low = close <= close.rolling(MDAYS, min_periods=WDAYS).min()
    cond = (adx.diff() > 0) & new_low
    return cond.astype(float).rolling(MDAYS, min_periods=WDAYS).sum().diff()

def f29_uarn_363_di_minus_dominant_count_in_21d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars in trailing 21d where DI- > DI+ — monthly bearish-DM persistence count."""
    p, m, _ = _dm_components(high, low, close, n=14)
    return (m > p).astype(float).rolling(MDAYS, min_periods=WDAYS).sum().diff()

def f29_uarn_364_vortex_minus_dominant_count_in_21d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars in trailing 21d where VI- > VI+ — monthly bearish-vortex persistence count."""
    vp, vm = _vortex(high, low, close, n=14)
    return (vm > vp).astype(float).rolling(MDAYS, min_periods=WDAYS).sum().diff()

def f29_uarn_365_choppiness_above_50_count_in_21d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars in trailing 21d with CI(14) > 50 — monthly ranging-side persistence count."""
    ci = _choppiness(high, low, close, n=14)
    return (ci > 50.0).astype(float).rolling(MDAYS, min_periods=WDAYS).sum().diff()

def f29_uarn_366_uo_whipsaw_signature_21d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """UO whipsaw: count of 50-line crossings in trailing 21d (both directions) — indecision marker."""
    uo = _ultimate_osc(high, low, close, 7, 14, 28)
    flips = (uo > 50.0).astype(float).diff().abs()
    return flips.rolling(MDAYS, min_periods=WDAYS).sum().diff()

def f29_uarn_367_aroon_up_below_30_count_in_21d_d1(high: pd.Series) -> pd.Series:
    """Count of bars in trailing 21d with Aroon-Up(25) < 30 — monthly stale-high persistence."""
    au = _aroon_up(high, 25)
    return (au < 30.0).astype(float).rolling(MDAYS, min_periods=WDAYS).sum().diff()

def f29_uarn_368_aroon_down_above_70_count_in_21d_d1(low: pd.Series) -> pd.Series:
    """Count of bars in trailing 21d with Aroon-Down(25) > 70 — monthly recent-low persistence."""
    ad = _aroon_down(low, 25)
    return (ad > 70.0).astype(float).rolling(MDAYS, min_periods=WDAYS).sum().diff()

def f29_uarn_369_di_minus_above_30_at_252d_high_event_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """At bars where high prints 252d new max, indicator that DI-(14) is currently > 30 — silent bear-DM at peak."""
    _, m, _ = _dm_components(high, low, close, n=14)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = high >= rmax
    cond = at_peak & (m > 30.0)
    return cond.astype(float).where(at_peak & m.notna(), np.nan).diff()

def f29_uarn_370_vortex_minus_value_at_252d_high_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """At bars where high prints 252d new max, value of VI-(14) — bear-vortex reading at the peak."""
    _, vm = _vortex(high, low, close, n=14)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = high >= rmax
    return vm.where(at_peak, np.nan).diff()

def f29_uarn_371_adx_value_at_252d_high_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """At bars where high prints 252d new max, value of ADX(14) — trend-strength reading at the peak."""
    _, _, adx = _dm_components(high, low, close, n=14)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = high >= rmax
    return adx.where(at_peak, np.nan).diff()

def f29_uarn_372_mass_index_value_at_252d_high_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """At bars where high prints 252d new max, value of Mass-Index(25) — bulge reading at the peak."""
    mi = _mass_index(high, low, n=25, ema_n=9)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = high >= rmax
    return mi.where(at_peak, np.nan).diff()

def f29_uarn_373_aroon_oscillator_value_at_252d_high_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """At bars where high prints 252d new max, value of Aroon-Osc(25) — directional-balance at the peak."""
    osc = _aroon_up(high, 25) - _aroon_down(low, 25)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = high >= rmax
    return osc.where(at_peak, np.nan).diff()

def f29_uarn_374_adxr_value_at_252d_high_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """At bars where high prints 252d new max, value of ADXR(14) — smoothed trend rating at the peak."""
    a = _adxr(high, low, close, n=14)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = high >= rmax
    return a.where(at_peak, np.nan).diff()

def f29_uarn_375_vortex_diff_value_at_252d_high_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """At bars where high prints 252d new max, value of Vortex-diff(14) — vortex-bias at the peak."""
    vp, vm = _vortex(high, low, close, n=14)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = high >= rmax
    return (vp - vm).where(at_peak, np.nan).diff()
ULTIMATE_AROON_VORTEX_D1_REGISTRY_301_375 = {'f29_uarn_301_di_minus_single_bar_cross_above_di_plus_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_301_di_minus_single_bar_cross_above_di_plus_d1}, 'f29_uarn_302_di_plus_first_day_below_20_after_strong_run_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_302_di_plus_first_day_below_20_after_strong_run_d1}, 'f29_uarn_303_aroon_up_failure_to_reach_100_on_new_high_d1': {'inputs': ['high'], 'func': f29_uarn_303_aroon_up_failure_to_reach_100_on_new_high_d1}, 'f29_uarn_304_aroon_down_100_with_price_near_52w_high_d1': {'inputs': ['high', 'low'], 'func': f29_uarn_304_aroon_down_100_with_price_near_52w_high_d1}, 'f29_uarn_305_uo_centerline_rejection_from_above_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_305_uo_centerline_rejection_from_above_d1}, 'f29_uarn_306_uo_lower_high_versus_price_higher_high_event_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_306_uo_lower_high_versus_price_higher_high_event_d1}, 'f29_uarn_307_mass_index_dorsey_trigger_cross_below_265_d1': {'inputs': ['high', 'low'], 'func': f29_uarn_307_mass_index_dorsey_trigger_cross_below_265_d1}, 'f29_uarn_308_choppiness_first_day_above_50_from_below_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_308_choppiness_first_day_above_50_from_below_d1}, 'f29_uarn_309_vortex_vi_plus_cross_below_one_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_309_vortex_vi_plus_cross_below_one_d1}, 'f29_uarn_310_vortex_vi_minus_cross_above_one_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_310_vortex_vi_minus_cross_above_one_d1}, 'f29_uarn_311_adx_first_above_25_after_long_below_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_311_adx_first_above_25_after_long_below_d1}, 'f29_uarn_312_aroon_oscillator_first_negative_after_long_positive_d1': {'inputs': ['high', 'low'], 'func': f29_uarn_312_aroon_oscillator_first_negative_after_long_positive_d1}, 'f29_uarn_313_uo_first_day_below_30_after_long_above_50_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_313_uo_first_day_below_30_after_long_above_50_d1}, 'f29_uarn_314_vortex_diff_first_negative_after_long_positive_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_314_vortex_diff_first_negative_after_long_positive_d1}, 'f29_uarn_315_choppiness_first_day_above_62_after_long_below_38_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_315_choppiness_first_day_above_62_after_long_below_38_d1}, 'f29_uarn_316_adx_max_trailing_21d_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_316_adx_max_trailing_21d_d1}, 'f29_uarn_317_adx_max_trailing_63d_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_317_adx_max_trailing_63d_d1}, 'f29_uarn_318_adx_max_trailing_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_318_adx_max_trailing_252d_d1}, 'f29_uarn_319_di_minus_max_trailing_21d_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_319_di_minus_max_trailing_21d_d1}, 'f29_uarn_320_di_minus_max_trailing_63d_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_320_di_minus_max_trailing_63d_d1}, 'f29_uarn_321_di_minus_max_trailing_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_321_di_minus_max_trailing_252d_d1}, 'f29_uarn_322_aroon_up_min_trailing_63d_d1': {'inputs': ['high'], 'func': f29_uarn_322_aroon_up_min_trailing_63d_d1}, 'f29_uarn_323_choppiness_max_trailing_63d_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_323_choppiness_max_trailing_63d_d1}, 'f29_uarn_324_mass_index_max_trailing_252d_d1': {'inputs': ['high', 'low'], 'func': f29_uarn_324_mass_index_max_trailing_252d_d1}, 'f29_uarn_325_uo_min_trailing_21d_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_325_uo_min_trailing_21d_d1}, 'f29_uarn_326_uo_min_trailing_63d_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_326_uo_min_trailing_63d_d1}, 'f29_uarn_327_vortex_diff_max_trailing_63d_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_327_vortex_diff_max_trailing_63d_d1}, 'f29_uarn_328_vortex_diff_min_trailing_63d_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_328_vortex_diff_min_trailing_63d_d1}, 'f29_uarn_329_adxr_max_trailing_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_329_adxr_max_trailing_252d_d1}, 'f29_uarn_330_di_plus_min_trailing_63d_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_330_di_plus_min_trailing_63d_d1}, 'f29_uarn_331_adx_50_minus_252_spread_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_331_adx_50_minus_252_spread_d1}, 'f29_uarn_332_di_plus_50_minus_252_spread_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_332_di_plus_50_minus_252_spread_d1}, 'f29_uarn_333_di_minus_50_minus_252_spread_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_333_di_minus_50_minus_252_spread_d1}, 'f29_uarn_334_vortex_diff_14_minus_50_spread_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_334_vortex_diff_14_minus_50_spread_d1}, 'f29_uarn_335_aroon_up_25_minus_100_spread_d1': {'inputs': ['high'], 'func': f29_uarn_335_aroon_up_25_minus_100_spread_d1}, 'f29_uarn_336_aroon_down_25_minus_100_spread_d1': {'inputs': ['low'], 'func': f29_uarn_336_aroon_down_25_minus_100_spread_d1}, 'f29_uarn_337_choppiness_25_minus_252_spread_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_337_choppiness_25_minus_252_spread_d1}, 'f29_uarn_338_mass_index_15_minus_50_spread_d1': {'inputs': ['high', 'low'], 'func': f29_uarn_338_mass_index_15_minus_50_spread_d1}, 'f29_uarn_339_uo_with_long_horizon_14_28_56_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_339_uo_with_long_horizon_14_28_56_d1}, 'f29_uarn_340_uo_short_minus_long_param_spread_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_340_uo_short_minus_long_param_spread_d1}, 'f29_uarn_341_adxr_50_minus_252_spread_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_341_adxr_50_minus_252_spread_d1}, 'f29_uarn_342_vortex_plus_horizon_50_minus_252_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_342_vortex_plus_horizon_50_minus_252_d1}, 'f29_uarn_343_vortex_minus_horizon_50_minus_252_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_343_vortex_minus_horizon_50_minus_252_d1}, 'f29_uarn_344_di_balance_horizon_dispersion_3way_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_344_di_balance_horizon_dispersion_3way_d1}, 'f29_uarn_345_aroon_osc_3horizon_sign_count_d1': {'inputs': ['high', 'low'], 'func': f29_uarn_345_aroon_osc_3horizon_sign_count_d1}, 'f29_uarn_346_bars_since_last_di_plus_above_25_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_346_bars_since_last_di_plus_above_25_d1}, 'f29_uarn_347_bars_since_last_aroon_up_100_d1': {'inputs': ['high'], 'func': f29_uarn_347_bars_since_last_aroon_up_100_d1}, 'f29_uarn_348_bars_since_last_vortex_bullish_cross_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_348_bars_since_last_vortex_bullish_cross_d1}, 'f29_uarn_349_bars_since_last_vortex_bearish_cross_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_349_bars_since_last_vortex_bearish_cross_d1}, 'f29_uarn_350_bars_since_last_choppiness_below_38_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_350_bars_since_last_choppiness_below_38_d1}, 'f29_uarn_351_bars_since_last_choppiness_above_50_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_351_bars_since_last_choppiness_above_50_d1}, 'f29_uarn_352_bars_since_last_di_minus_above_di_plus_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_352_bars_since_last_di_minus_above_di_plus_d1}, 'f29_uarn_353_bars_since_last_uo_above_50_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_353_bars_since_last_uo_above_50_d1}, 'f29_uarn_354_bars_since_last_mass_index_above_265_d1': {'inputs': ['high', 'low'], 'func': f29_uarn_354_bars_since_last_mass_index_above_265_d1}, 'f29_uarn_355_bars_since_last_adxr_above_30_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_355_bars_since_last_adxr_above_30_d1}, 'f29_uarn_356_bars_since_last_aroon_osc_negative_d1': {'inputs': ['high', 'low'], 'func': f29_uarn_356_bars_since_last_aroon_osc_negative_d1}, 'f29_uarn_357_bars_since_last_vortex_diff_negative_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_357_bars_since_last_vortex_diff_negative_d1}, 'f29_uarn_358_bars_since_last_adx_local_peak_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_358_bars_since_last_adx_local_peak_d1}, 'f29_uarn_359_bars_since_last_di_minus_local_peak_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_359_bars_since_last_di_minus_local_peak_d1}, 'f29_uarn_360_bars_since_last_uo_centerline_rejection_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_360_bars_since_last_uo_centerline_rejection_d1}, 'f29_uarn_361_di_minus_above_25_with_adx_rising_count_21d_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_361_di_minus_above_25_with_adx_rising_count_21d_d1}, 'f29_uarn_362_adx_rising_with_close_lower_low_count_21d_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_362_adx_rising_with_close_lower_low_count_21d_d1}, 'f29_uarn_363_di_minus_dominant_count_in_21d_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_363_di_minus_dominant_count_in_21d_d1}, 'f29_uarn_364_vortex_minus_dominant_count_in_21d_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_364_vortex_minus_dominant_count_in_21d_d1}, 'f29_uarn_365_choppiness_above_50_count_in_21d_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_365_choppiness_above_50_count_in_21d_d1}, 'f29_uarn_366_uo_whipsaw_signature_21d_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_366_uo_whipsaw_signature_21d_d1}, 'f29_uarn_367_aroon_up_below_30_count_in_21d_d1': {'inputs': ['high'], 'func': f29_uarn_367_aroon_up_below_30_count_in_21d_d1}, 'f29_uarn_368_aroon_down_above_70_count_in_21d_d1': {'inputs': ['low'], 'func': f29_uarn_368_aroon_down_above_70_count_in_21d_d1}, 'f29_uarn_369_di_minus_above_30_at_252d_high_event_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_369_di_minus_above_30_at_252d_high_event_d1}, 'f29_uarn_370_vortex_minus_value_at_252d_high_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_370_vortex_minus_value_at_252d_high_d1}, 'f29_uarn_371_adx_value_at_252d_high_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_371_adx_value_at_252d_high_d1}, 'f29_uarn_372_mass_index_value_at_252d_high_d1': {'inputs': ['high', 'low'], 'func': f29_uarn_372_mass_index_value_at_252d_high_d1}, 'f29_uarn_373_aroon_oscillator_value_at_252d_high_d1': {'inputs': ['high', 'low'], 'func': f29_uarn_373_aroon_oscillator_value_at_252d_high_d1}, 'f29_uarn_374_adxr_value_at_252d_high_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_374_adxr_value_at_252d_high_d1}, 'f29_uarn_375_vortex_diff_value_at_252d_high_d1': {'inputs': ['high', 'low', 'close'], 'func': f29_uarn_375_vortex_diff_value_at_252d_high_d1}}