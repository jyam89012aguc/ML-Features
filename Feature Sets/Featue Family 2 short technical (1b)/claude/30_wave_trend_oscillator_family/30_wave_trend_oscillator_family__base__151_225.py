"""wave_trend_oscillator_family base features 151-225 — Pipeline 1b-technical.

Gap-fill extension to the original 150-feature family. Adds hypotheses that
plug research-identified gaps not covered by the 001-150 set:

  - WTO with alternative typical-price definitions (median(H,L), weighted
    (2C+H+L)/4, OHLC4, log-price, OC2) and alternative smoothers (HMA, DEMA,
    KAMA, weighted-MA).
  - WTO raw CI (un-WT2-smoothed), normalized rescale, multi-scale variants at
    short (3,5), mid (15,30), long (50,100), very-long (100,200) horizons.
  - WTO zero-line cross events, failed-cross (cross-then-cross-back), double
    bottom from oversold, post-overbought event chains.
  - John Carter TTM Squeeze (distinct parametrization from LazyBear), TTM dots,
    TTM 'fired' direction taxonomy.
  - SqueezePro low/mid/high compression dots and stage progression.
  - Bollinger %b (Bollinger's own indicator), %b walking/exhaustion events,
    BandWidth pct-of-mid as Bollinger defines it, BandWidth-at-126d-low
    Bollinger squeeze definition.

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


def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=max(n // 3, 2)).mean()


def _dema(s, n):
    e1 = _ema(s, n)
    e2 = _ema(e1, n)
    return 2.0 * e1 - e2


def _wma(s, n):
    """Linear-weighted moving average, safe for early short rolling windows."""
    minp = max(n // 3, 2)
    def _f(x):
        valid = ~np.isnan(x)
        if valid.sum() < minp:
            return np.nan
        xv = x[valid]
        wv = np.arange(1, len(x) + 1, dtype=float)[valid]
        return float(np.dot(xv, wv) / wv.sum())
    return s.rolling(n, min_periods=minp).apply(_f, raw=True)

def _hma(s, n):
    """Hull MA: WMA(2*WMA(n/2) - WMA(n), sqrt(n))."""
    n2 = max(int(n / 2), 2)
    nsqrt = max(int(np.sqrt(n)), 2)
    raw = 2.0 * _wma(s, n2) - _wma(s, n)
    return _wma(raw, nsqrt)


def _kama(s, n=10, fast=2, slow=30):
    """Kaufman Adaptive MA."""
    change = (s - s.shift(n)).abs()
    volatility = s.diff().abs().rolling(n, min_periods=max(n // 3, 2)).sum()
    er = _safe_div(change, volatility).clip(0, 1)
    fast_a = 2.0 / (fast + 1)
    slow_a = 2.0 / (slow + 1)
    sc = (er * (fast_a - slow_a) + slow_a) ** 2
    arr = s.to_numpy(dtype=float)
    sc_arr = sc.to_numpy(dtype=float)
    out = np.full_like(arr, np.nan)
    init = None
    for i in range(len(arr)):
        if init is None:
            if not np.isnan(arr[i]):
                init = arr[i]
                out[i] = init
        else:
            sci = sc_arr[i]
            if np.isnan(sci) or np.isnan(arr[i]):
                out[i] = init
            else:
                init = init + sci * (arr[i] - init)
                out[i] = init
    return pd.Series(out, index=s.index)


# ---------------------------- indicator primitives ----------------------------

def _wto_ap(ap, n1=10, n2=21):
    """WTO computed from a pre-given typical-price 'ap' series. Returns (WT1, WT2)."""
    esa = _ema(ap, n1)
    d = _ema((ap - esa).abs(), n1)
    ci = _safe_div(ap - esa, 0.015 * d)
    tci = _ema(ci, n2)
    wt1 = tci
    wt2 = wt1.rolling(4, min_periods=2).mean()
    return wt1, wt2


def _wto_with_smoother(ap, smoother_fn, n1=10, n2=21):
    """WTO using a custom smoother for both ESA and TCI legs."""
    esa = smoother_fn(ap, n1)
    d = smoother_fn((ap - esa).abs(), n1)
    ci = _safe_div(ap - esa, 0.015 * d)
    tci = smoother_fn(ci, n2)
    wt2 = tci.rolling(4, min_periods=2).mean()
    return tci, wt2


def _wto_default(high, low, close, n1=10, n2=21):
    ap = (high + low + close) / 3.0
    return _wto_ap(ap, n1, n2)


def _bb(close, n=20, mult=2.0):
    mid = close.rolling(n, min_periods=max(n // 3, 2)).mean()
    sd = close.rolling(n, min_periods=max(n // 3, 2)).std()
    return mid, mid + mult * sd, mid - mult * sd


def _kc(high, low, close, n=20, mult=1.5):
    mid = close.rolling(n, min_periods=max(n // 3, 2)).mean()
    tr = _true_range(high, low, close)
    rng = tr.rolling(n, min_periods=max(n // 3, 2)).mean()
    return mid, mid + mult * rng, mid - mult * rng


def _ttm_squeeze_on(high, low, close, n=20, mult_bb=2.0, mult_kc=1.5):
    """John Carter TTM Squeeze: BB(20,2) inside KC(20,1.5) using ATR-based Keltner."""
    _, bbu, bbl = _bb(close, n=n, mult=mult_bb)
    _, kcu, kcl = _kc(high, low, close, n=n, mult=mult_kc)
    on = (bbu < kcu) & (bbl > kcl)
    return on.astype(float).where(bbu.notna() & kcu.notna(), np.nan)


def _ttm_momentum(high, low, close, n=20):
    """TTM histogram: linreg endpoint of (close - 0.5*((HHn+LLn)/2 + SMA(close,n)))."""
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


def _pct_b(close, n=20, mult=2.0):
    """Bollinger %b = (close - lower) / (upper - lower)."""
    _, bbu, bbl = _bb(close, n=n, mult=mult)
    return _safe_div(close - bbl, bbu - bbl)


def _bb_width_pct(close, n=20, mult=2.0):
    mid, bbu, bbl = _bb(close, n=n, mult=mult)
    return _safe_div(bbu - bbl, mid)


def _donchian(high, low, n):
    upper = high.rolling(n, min_periods=max(n // 3, 2)).max()
    lower = low.rolling(n, min_periods=max(n // 3, 2)).min()
    return upper, lower


def _streak_true(b: pd.Series) -> pd.Series:
    """Current consecutive run-length of True values (resets at False)."""
    bb = b.fillna(False).astype(int)
    grp = (bb != bb.shift()).cumsum()
    out = bb.groupby(grp).cumsum() * bb
    return out.astype(float)


# ============================================================
# Bucket A — WTO variants: typical-price, smoothers, scale, raw CI (151-175)
# ============================================================

def f30_wtof_151_wto_typical_price_median_hl(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """WTO with typical price = median(H,L) instead of HLC3 — H/L-only momentum."""
    ap = (high + low) / 2.0
    wt1, _ = _wto_ap(ap, 10, 21)
    return wt1


def f30_wtof_152_wto_typical_price_weighted_2c_h_l(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """WTO with weighted typical (2C+H+L)/4 — close-weighted Wave Trend."""
    ap = (2.0 * close + high + low) / 4.0
    wt1, _ = _wto_ap(ap, 10, 21)
    return wt1


def f30_wtof_153_wto_typical_price_ohlc4(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """WTO with OHLC4 typical price — includes open in Wave Trend basis."""
    ap = (open_ + high + low + close) / 4.0
    wt1, _ = _wto_ap(ap, 10, 21)
    return wt1


def f30_wtof_154_wto_on_log_price(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """WTO computed on log(HLC3) — log-scale Wave Trend insensitive to absolute price."""
    ap = _safe_log((high + low + close) / 3.0)
    wt1, _ = _wto_ap(ap, 10, 21)
    return wt1


def f30_wtof_155_wto_typical_price_oc2(open_: pd.Series, close: pd.Series) -> pd.Series:
    """WTO with body midpoint (O+C)/2 — body-only Wave Trend, ignores wicks."""
    ap = (open_ + close) / 2.0
    wt1, _ = _wto_ap(ap, 10, 21)
    return wt1


def f30_wtof_156_wto_typical_price_hlc4_with_double_close(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """WTO with (H+L+2C)/4 — Bressert-style double-close weighted Wave Trend."""
    ap = (high + low + 2.0 * close) / 4.0
    wt1, _ = _wto_ap(ap, 10, 21)
    return wt1


def f30_wtof_157_wto_smoothed_with_hma(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """WTO using Hull MA in place of EMA smoothing — lag-reduced Wave Trend."""
    ap = (high + low + close) / 3.0
    wt1, _ = _wto_with_smoother(ap, _hma, n1=10, n2=21)
    return wt1


def f30_wtof_158_wto_smoothed_with_dema(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """WTO using DEMA smoothing — double-EMA reduced-lag Wave Trend."""
    ap = (high + low + close) / 3.0
    wt1, _ = _wto_with_smoother(ap, _dema, n1=10, n2=21)
    return wt1


def f30_wtof_159_wto_smoothed_with_kama(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """WTO using KAMA (Kaufman Adaptive MA) smoothing — efficiency-ratio adaptive Wave Trend."""
    ap = (high + low + close) / 3.0
    wt1, _ = _wto_with_smoother(ap, lambda s, n: _kama(s, n=n), n1=10, n2=21)
    return wt1


def f30_wtof_160_wto_smoothed_with_wma(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """WTO using linear-weighted MA smoothing — recency-weighted Wave Trend."""
    ap = (high + low + close) / 3.0
    wt1, _ = _wto_with_smoother(ap, _wma, n1=10, n2=21)
    return wt1


def f30_wtof_161_wto_raw_ci_level_unsmoothed(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Raw Channel Index of WTO (before TCI smoothing) — un-lagged Wave Trend impulse."""
    ap = (high + low + close) / 3.0
    esa = _ema(ap, 10)
    d = _ema((ap - esa).abs(), 10)
    return _safe_div(ap - esa, 0.015 * d)


def f30_wtof_162_wto_normalized_rescaled_pm100(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """WT1 rescaled to ±100 via tanh — cross-asset comparable Wave Trend reading."""
    wt1, _ = _wto_default(high, low, close, 10, 21)
    return 100.0 * np.tanh(wt1 / 100.0)


def f30_wtof_163_wto_histogram_zero_cross_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: WT1−WT2 crosses zero (i.e., histogram zero cross) regardless of direction."""
    wt1, wt2 = _wto_default(high, low, close, 10, 21)
    h = wt1 - wt2
    crossed = (np.sign(h) != np.sign(h.shift(1))) & h.notna() & h.shift(1).notna()
    return crossed.astype(float).where(h.notna(), np.nan)


def f30_wtof_164_wto_zero_line_cross_up_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: WT1 itself crosses above zero (distinct from WT1-WT2 bullish cross)."""
    wt1, _ = _wto_default(high, low, close, 10, 21)
    ev = (wt1 > 0) & (wt1.shift(1) <= 0)
    return ev.astype(float).where(wt1.notna() & wt1.shift(1).notna(), np.nan)


def f30_wtof_165_wto_zero_line_cross_down_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: WT1 crosses below zero — neutral-to-bearish regime flip."""
    wt1, _ = _wto_default(high, low, close, 10, 21)
    ev = (wt1 < 0) & (wt1.shift(1) >= 0)
    return ev.astype(float).where(wt1.notna() & wt1.shift(1).notna(), np.nan)


def f30_wtof_166_wto_bars_since_bearish_cross(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Recency: number of bars since last WT1<WT2 bearish cross — recency-of-rollover."""
    wt1, wt2 = _wto_default(high, low, close, 10, 21)
    ev = (wt1 < wt2) & (wt1.shift(1) >= wt2.shift(1))
    idx = np.arange(len(close), dtype=float)
    last = pd.Series(np.where(ev.fillna(False), idx, np.nan), index=close.index).ffill()
    out = pd.Series(idx, index=close.index) - last
    return out.where(wt1.notna(), np.nan)


def f30_wtof_167_wto_double_bottom_oversold_in_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: two distinct WT1 local-mins below −60 inside trailing 21d — bullish double-bottom mirror."""
    wt1, _ = _wto_default(high, low, close, 10, 21)
    local_min = (wt1 < wt1.shift(1)) & (wt1 < wt1.shift(-0))
    # PIT-safe local-min using only past data: dip below the trailing-2 min
    is_below = (wt1 < -60.0) & (wt1 < wt1.shift(1))
    count = is_below.rolling(MDAYS, min_periods=WDAYS).sum()
    return (count >= 2).astype(float).where(wt1.notna(), np.nan)


def f30_wtof_168_wto_overbought_then_bearish_cross_within_5(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: WT1≥60 occurred within trailing 5 bars AND bearish cross today — fast topping trigger."""
    wt1, wt2 = _wto_default(high, low, close, 10, 21)
    was_ob = (wt1 >= 60.0).rolling(WDAYS, min_periods=2).max().astype(bool)
    bear = (wt1 < wt2) & (wt1.shift(1) >= wt2.shift(1))
    cond = was_ob & bear
    return cond.astype(float).where(wt1.notna(), np.nan)


def f30_wtof_169_wto_failed_bearish_cross_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: bearish cross within trailing 5 bars then WT1 crosses back above WT2 — failed-rollover."""
    wt1, wt2 = _wto_default(high, low, close, 10, 21)
    bear = (wt1 < wt2) & (wt1.shift(1) >= wt2.shift(1))
    bear_recent = bear.rolling(WDAYS, min_periods=2).max().astype(bool)
    bull = (wt1 > wt2) & (wt1.shift(1) <= wt2.shift(1))
    cond = bear_recent & bull
    return cond.astype(float).where(wt1.notna(), np.nan)


def f30_wtof_170_wto_long_horizon_zero_cross_down_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: long-horizon WT1(20,50) crosses below zero — multi-month regime flip."""
    wt1, _ = _wto_default(high, low, close, 20, 50)
    ev = (wt1 < 0) & (wt1.shift(1) >= 0)
    return ev.astype(float).where(wt1.notna() & wt1.shift(1).notna(), np.nan)


def f30_wtof_171_wto_short_horizon_zero_cross_down_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: short-horizon WT1(5,10) crosses below zero — weekly-cycle regime flip."""
    wt1, _ = _wto_default(high, low, close, 5, 10)
    ev = (wt1 < 0) & (wt1.shift(1) >= 0)
    return ev.astype(float).where(wt1.notna() & wt1.shift(1).notna(), np.nan)


def f30_wtof_172_wto_micro_horizon_3_5(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """WT1 at micro horizon (n1=3, n2=5) — sub-week cycle hypothesis distinct from short/classic."""
    wt1, _ = _wto_default(high, low, close, 3, 5)
    return wt1


def f30_wtof_173_wto_intermediate_horizon_15_30(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """WT1 at intermediate horizon (n1=15, n2=30) — between classic and long cycle hypothesis."""
    wt1, _ = _wto_default(high, low, close, 15, 30)
    return wt1


def f30_wtof_174_wto_very_long_horizon_50_100(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """WT1 at very-long horizon (n1=50, n2=100) — half-year cycle hypothesis."""
    wt1, _ = _wto_default(high, low, close, 50, 100)
    return wt1


def f30_wtof_175_wto_secular_horizon_100_200(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """WT1 at secular horizon (n1=100, n2=200) — multi-year structural Wave Trend hypothesis."""
    wt1, _ = _wto_default(high, low, close, 100, 200)
    return wt1


# ============================================================
# Bucket B — TTM Squeeze (John Carter) and SqueezePro (176-205)
# ============================================================

def f30_wtof_176_ttm_squeeze_on_carter_classic(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """John Carter TTM Squeeze ON: BB(20,2) inside KC(20,1.5) — classic 'red dot' state."""
    return _ttm_squeeze_on(high, low, close, n=20, mult_bb=2.0, mult_kc=1.5)


def f30_wtof_177_ttm_momentum_histogram(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """TTM momentum histogram (Carter's, distinct slope formula from LazyBear's squeeze momentum)."""
    return _ttm_momentum(high, low, close, n=20)


def f30_wtof_178_ttm_fired_direction_sign(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sign of TTM momentum on the bar the squeeze fires off — release direction (+1/-1/0)."""
    on = _ttm_squeeze_on(high, low, close, n=20)
    mom = _ttm_momentum(high, low, close, n=20)
    fired = (on == 0) & (on.shift(1) == 1)
    out = np.sign(mom).where(fired.fillna(False), 0.0)
    return out.where(on.notna(), np.nan)


def f30_wtof_179_ttm_histogram_color_bull_to_bear_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: TTM histogram color flips from positive-rising/positive-falling boundary (bull→bear color change)."""
    mom = _ttm_momentum(high, low, close, n=20)
    rising = mom.diff() > 0
    pos = mom > 0
    bull = pos & rising
    flip = (~bull) & bull.shift(1)
    return flip.astype(float).where(mom.notna(), np.nan)


def f30_wtof_180_ttm_squeeze_count_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Number of trailing 63d bars in TTM squeeze ON — compression dwell."""
    on = _ttm_squeeze_on(high, low, close, n=20)
    return on.rolling(QDAYS, min_periods=MDAYS).sum()


def f30_wtof_181_ttm_bars_since_last_fire(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since last TTM squeeze fire event — recency of compression release."""
    on = _ttm_squeeze_on(high, low, close, n=20)
    fired = (on == 0) & (on.shift(1) == 1)
    idx = np.arange(len(close), dtype=float)
    last = pd.Series(np.where(fired.fillna(False), idx, np.nan), index=close.index).ffill()
    return (pd.Series(idx, index=close.index) - last).where(on.notna(), np.nan)


def f30_wtof_182_ttm_current_in_squeeze_streak(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current consecutive in-squeeze streak length — energy build-up duration (TTM)."""
    on = _ttm_squeeze_on(high, low, close, n=20)
    return _streak_true(on.astype(bool) & on.notna()).where(on.notna(), np.nan)


def f30_wtof_183_ttm_fired_with_positive_momentum_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: TTM fires AND momentum>0 — Carter's primary 'long fire' signal."""
    on = _ttm_squeeze_on(high, low, close, n=20)
    mom = _ttm_momentum(high, low, close, n=20)
    fired = (on == 0) & (on.shift(1) == 1)
    cond = fired & (mom > 0)
    return cond.astype(float).where(mom.notna(), np.nan)


def f30_wtof_184_ttm_fired_with_negative_momentum_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: TTM fires AND momentum<0 — Carter's 'short fire' signal (topping)."""
    on = _ttm_squeeze_on(high, low, close, n=20)
    mom = _ttm_momentum(high, low, close, n=20)
    fired = (on == 0) & (on.shift(1) == 1)
    cond = fired & (mom < 0)
    return cond.astype(float).where(mom.notna(), np.nan)


def f30_wtof_185_ttm_histogram_falling_after_fire_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: TTM fired within trailing 5 bars AND histogram now declining — post-fire fade."""
    on = _ttm_squeeze_on(high, low, close, n=20)
    mom = _ttm_momentum(high, low, close, n=20)
    fired = (on == 0) & (on.shift(1) == 1)
    fired_recent = fired.rolling(WDAYS, min_periods=2).max().astype(bool)
    falling = mom.diff() < 0
    cond = fired_recent & falling
    return cond.astype(float).where(mom.notna(), np.nan)


def f30_wtof_186_squeeze_pro_low_compression_on(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """SqueezePro 'low compression' (black dot): BB inside KC at mult=2.0 (widest KC)."""
    return _ttm_squeeze_on(high, low, close, n=20, mult_bb=2.0, mult_kc=2.0)


def f30_wtof_187_squeeze_pro_mid_compression_on(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """SqueezePro 'mid compression' (red dot): BB inside KC at mult=1.5 — classic TTM threshold."""
    return _ttm_squeeze_on(high, low, close, n=20, mult_bb=2.0, mult_kc=1.5)


def f30_wtof_188_squeeze_pro_high_compression_on(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """SqueezePro 'high compression' (orange dot): BB inside KC at mult=1.0 (tightest KC)."""
    return _ttm_squeeze_on(high, low, close, n=20, mult_bb=2.0, mult_kc=1.0)


def f30_wtof_189_squeeze_pro_compression_level(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """SqueezePro discrete level: 0=none, 1=low, 2=mid, 3=high — ordinal compression stage."""
    low_on = _ttm_squeeze_on(high, low, close, n=20, mult_bb=2.0, mult_kc=2.0)
    mid_on = _ttm_squeeze_on(high, low, close, n=20, mult_bb=2.0, mult_kc=1.5)
    hi_on = _ttm_squeeze_on(high, low, close, n=20, mult_bb=2.0, mult_kc=1.0)
    level = low_on.fillna(0) + mid_on.fillna(0) + hi_on.fillna(0)
    return level.where(low_on.notna(), np.nan)


def f30_wtof_190_squeeze_pro_progression_to_higher_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: SqueezePro compression level increases vs prior bar — tightening event."""
    lvl = f30_wtof_189_squeeze_pro_compression_level(high, low, close)
    ev = (lvl > lvl.shift(1)).astype(float)
    return ev.where(lvl.notna() & lvl.shift(1).notna(), np.nan)


def f30_wtof_191_squeeze_pro_high_then_release_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: was at high-compression within trailing 5 bars AND today no compression — coiled-release."""
    hi_on = _ttm_squeeze_on(high, low, close, n=20, mult_bb=2.0, mult_kc=1.0)
    lvl = f30_wtof_189_squeeze_pro_compression_level(high, low, close)
    was_hi = (hi_on == 1).rolling(WDAYS, min_periods=2).max().astype(bool)
    cond = was_hi & (lvl == 0)
    return cond.astype(float).where(lvl.notna(), np.nan)


def f30_wtof_192_squeeze_pro_high_dwell_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Trailing 63d count of bars at high-compression — persistence of tight regime."""
    hi_on = _ttm_squeeze_on(high, low, close, n=20, mult_bb=2.0, mult_kc=1.0)
    return hi_on.rolling(QDAYS, min_periods=MDAYS).sum()


def f30_wtof_193_squeeze_pro_fired_from_high_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: previously high-compression on prior bar AND today level=0 — high-energy release."""
    hi_on = _ttm_squeeze_on(high, low, close, n=20, mult_bb=2.0, mult_kc=1.0)
    lvl = f30_wtof_189_squeeze_pro_compression_level(high, low, close)
    cond = (hi_on.shift(1) == 1) & (lvl == 0)
    return cond.astype(float).where(lvl.notna(), np.nan)


def f30_wtof_194_squeeze_pro_low_dwell_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Trailing 252d count of bars at low-compression — annual fraction of base compression."""
    low_on = _ttm_squeeze_on(high, low, close, n=20, mult_bb=2.0, mult_kc=2.0)
    return low_on.rolling(YDAYS, min_periods=QDAYS).sum()


def f30_wtof_195_squeeze_pro_total_squeeze_count_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Trailing 63d count of any-compression bars (level≥1) — SqueezePro regime fraction."""
    lvl = f30_wtof_189_squeeze_pro_compression_level(high, low, close)
    return (lvl >= 1).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f30_wtof_196_squeeze_pro_aligned_with_positive_momentum(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: SqueezePro level≥2 AND TTM momentum>0 — coiled bullish setup."""
    lvl = f30_wtof_189_squeeze_pro_compression_level(high, low, close)
    mom = _ttm_momentum(high, low, close, n=20)
    cond = (lvl >= 2) & (mom > 0)
    return cond.astype(float).where(lvl.notna() & mom.notna(), np.nan)


def f30_wtof_197_squeeze_pro_aligned_with_negative_momentum(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: SqueezePro level≥2 AND TTM momentum<0 — coiled bearish setup (topping)."""
    lvl = f30_wtof_189_squeeze_pro_compression_level(high, low, close)
    mom = _ttm_momentum(high, low, close, n=20)
    cond = (lvl >= 2) & (mom < 0)
    return cond.astype(float).where(lvl.notna() & mom.notna(), np.nan)


def f30_wtof_198_ttm_fired_then_drawdown_5d_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: TTM fired within trailing 5 bars AND close has declined ≥3% from that fire bar."""
    on = _ttm_squeeze_on(high, low, close, n=20)
    fired = (on == 0) & (on.shift(1) == 1)
    idx = np.arange(len(close), dtype=float)
    last_fire = pd.Series(np.where(fired.fillna(False), idx, np.nan), index=close.index).ffill()
    bars_since = pd.Series(idx, index=close.index) - last_fire
    price_at_fire = close.where(fired.fillna(False)).ffill()
    rel = _safe_div(close, price_at_fire) - 1.0
    cond = (bars_since <= WDAYS) & (rel <= -0.03)
    return cond.astype(float).where(on.notna() & price_at_fire.notna(), np.nan)


def f30_wtof_199_ttm_squeeze_max_streak_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Trailing 252d max consecutive in-squeeze streak — longest compression episode in past year."""
    on = _ttm_squeeze_on(high, low, close, n=20)
    streak = _streak_true(on.astype(bool) & on.notna())
    return streak.rolling(YDAYS, min_periods=QDAYS).max().where(on.notna(), np.nan)


def f30_wtof_200_ttm_fired_count_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Trailing 252d count of TTM fire events — annual fire density."""
    on = _ttm_squeeze_on(high, low, close, n=20)
    fired = (on == 0) & (on.shift(1) == 1)
    return fired.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f30_wtof_201_ttm_squeeze_release_with_negative_then_positive(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: TTM fired with mom<0 within trailing 5 bars then mom flips positive — failed short-fire."""
    on = _ttm_squeeze_on(high, low, close, n=20)
    mom = _ttm_momentum(high, low, close, n=20)
    fired = (on == 0) & (on.shift(1) == 1)
    short_fire = fired & (mom < 0)
    short_recent = short_fire.rolling(WDAYS, min_periods=2).max().astype(bool)
    flip_pos = (mom > 0) & (mom.shift(1) <= 0)
    return (short_recent & flip_pos).astype(float).where(mom.notna(), np.nan)


def f30_wtof_202_ttm_momentum_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of TTM momentum histogram in trailing 252d — anomalous Carter-style impulse."""
    mom = _ttm_momentum(high, low, close, n=20)
    return _rolling_zscore(mom, YDAYS, min_periods=QDAYS)


def f30_wtof_203_ttm_momentum_above_zero_dwell_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Trailing 21d count of bars with TTM momentum>0 — recent bullish-impulse dwell."""
    mom = _ttm_momentum(high, low, close, n=20)
    return (mom > 0).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f30_wtof_204_ttm_squeeze_long_horizon_50d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """TTM squeeze ON at long horizon (50/2/1.5) — multi-month compression hypothesis."""
    return _ttm_squeeze_on(high, low, close, n=50, mult_bb=2.0, mult_kc=1.5)


def f30_wtof_205_ttm_squeeze_short_horizon_10d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """TTM squeeze ON at short horizon (10/2/1.5) — sub-month compression hypothesis."""
    return _ttm_squeeze_on(high, low, close, n=10, mult_bb=2.0, mult_kc=1.5)


# ============================================================
# Bucket C — Bollinger %b, BandWidth-as-pct, M-Top, W-Bottom (206-225 here; 226-235 in next file)
# ============================================================

def f30_wtof_206_pct_b_classic(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bollinger %b = (C−lower)/(upper−lower) — Bollinger's own normalized band position."""
    return _pct_b(close, n=20, mult=2.0)


def f30_wtof_207_pct_b_above_one_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: %b > 1 — close above upper band (Bollinger overbought)."""
    pb = _pct_b(close, n=20, mult=2.0)
    return (pb > 1.0).astype(float).where(pb.notna(), np.nan)


def f30_wtof_208_pct_b_above_one_current_streak(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current consecutive streak of %b>1 bars — band-walking persistence."""
    pb = _pct_b(close, n=20, mult=2.0)
    return _streak_true(pb > 1.0).where(pb.notna(), np.nan)


def f30_wtof_209_pct_b_deviation_from_half(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """|%b − 0.5| — magnitude of departure from band midpoint (overbought OR oversold magnitude)."""
    pb = _pct_b(close, n=20, mult=2.0)
    return (pb - 0.5).abs()


def f30_wtof_210_pct_b_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of %b in trailing 252d — anomalous band position."""
    pb = _pct_b(close, n=20, mult=2.0)
    return _rolling_zscore(pb, YDAYS, min_periods=QDAYS)


def f30_wtof_211_pct_b_cross_above_one_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: %b crosses above 1.0 from below — fresh upper-band breach."""
    pb = _pct_b(close, n=20, mult=2.0)
    ev = (pb > 1.0) & (pb.shift(1) <= 1.0)
    return ev.astype(float).where(pb.notna() & pb.shift(1).notna(), np.nan)


def f30_wtof_212_pct_b_cross_below_zero_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: %b crosses below 0 — fresh lower-band breach (mirror)."""
    pb = _pct_b(close, n=20, mult=2.0)
    ev = (pb < 0.0) & (pb.shift(1) >= 0.0)
    return ev.astype(float).where(pb.notna() & pb.shift(1).notna(), np.nan)


def f30_wtof_213_pct_b_rejection_from_above_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: %b was >1 within trailing 5 bars AND today %b < 1 — band rejection topping signal."""
    pb = _pct_b(close, n=20, mult=2.0)
    was = (pb > 1.0).rolling(WDAYS, min_periods=2).max().astype(bool)
    cond = was & (pb < 1.0)
    return cond.astype(float).where(pb.notna(), np.nan)


def f30_wtof_214_pct_b_above_eighty_pct_dwell_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Trailing 21d count of bars with %b ≥ 0.8 — upper-band-zone dwell."""
    pb = _pct_b(close, n=20, mult=2.0)
    return (pb >= 0.8).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f30_wtof_215_pct_b_long_horizon_50d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bollinger %b at 50d/2σ — intermediate-cycle band position hypothesis."""
    return _pct_b(close, n=50, mult=2.0)


def f30_wtof_216_bandwidth_pct_of_mid_classic(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bollinger BandWidth (Bollinger's pct-of-mid formula) = (upper−lower)/mid at 20d."""
    return _bb_width_pct(close, n=20, mult=2.0)


def f30_wtof_217_bandwidth_at_126d_low_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bollinger's 'squeeze': BandWidth at its 126-day (6-month) minimum — Bollinger's own definition."""
    bw = _bb_width_pct(close, n=20, mult=2.0)
    bw_min = bw.rolling(126, min_periods=QDAYS).min()
    return (bw <= bw_min * 1.0001).astype(float).where(bw.notna() & bw_min.notna(), np.nan)


def f30_wtof_218_bandwidth_released_after_126d_low_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: BW was at 126d low within trailing 5 bars AND now BW > 1.2× that low — Bollinger squeeze release."""
    bw = _bb_width_pct(close, n=20, mult=2.0)
    bw_min = bw.rolling(126, min_periods=QDAYS).min()
    was_low = (bw <= bw_min * 1.0001).rolling(WDAYS, min_periods=2).max().astype(bool)
    cond = was_low & (bw > 1.2 * bw_min)
    return cond.astype(float).where(bw.notna(), np.nan)


def f30_wtof_219_bandwidth_percentile_504d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of BW(20) in trailing 504d — biennial volatility-regime rank."""
    bw = _bb_width_pct(close, n=20, mult=2.0)
    return bw.rolling(DDAYS_2Y, min_periods=YDAYS).rank(pct=True)


def f30_wtof_220_bandwidth_vol_of_vol_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Std-dev of BW(20) over trailing 63d — vol-of-vol (BW noisiness)."""
    bw = _bb_width_pct(close, n=20, mult=2.0)
    return bw.rolling(QDAYS, min_periods=MDAYS).std()


def f30_wtof_221_bandwidth_skew_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Skewness of BW(20) over trailing 63d — asymmetric volatility regime."""
    bw = _bb_width_pct(close, n=20, mult=2.0)
    return bw.rolling(QDAYS, min_periods=MDAYS).skew()


def f30_wtof_222_bandwidth_autocorr_5d_in_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Lag-5 autocorrelation of BW(20) over trailing 63d — volatility persistence."""
    bw = _bb_width_pct(close, n=20, mult=2.0)
    def _ac(w):
        if np.isnan(w).any() or len(w) < 10:
            return np.nan
        a = w[:-5]; b = w[5:]
        sa = a.std(); sb = b.std()
        if sa == 0 or sb == 0:
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    return bw.rolling(QDAYS, min_periods=QDAYS).apply(_ac, raw=True)


def f30_wtof_223_bandwidth_above_95pct_dwell_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Trailing 252d count of bars with BW(20) ≥ 95th-pct of trailing 252d — high-vol regime fraction."""
    bw = _bb_width_pct(close, n=20, mult=2.0)
    p = bw.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    return (p >= 0.95).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f30_wtof_224_m_top_event_pct_b_lower_peak(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bollinger M-top: today price tags upper band (%b>0.95) AND prior peak within 21d had higher %b."""
    pb = _pct_b(close, n=20, mult=2.0)
    near_upper_now = pb > 0.95
    pb_prior_max = pb.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    cond = near_upper_now & (pb < pb_prior_max)
    return cond.astype(float).where(pb.notna() & pb_prior_max.notna(), np.nan)


def f30_wtof_225_m_top_count_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Trailing 63d count of M-top events — repeated upper-band-rejection-with-lower-%b density."""
    pb = _pct_b(close, n=20, mult=2.0)
    near_upper = pb > 0.95
    pb_prior_max = pb.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    ev = near_upper & (pb < pb_prior_max)
    return ev.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


# ============================================================
#                         REGISTRY 151-225
# ============================================================

WAVE_TREND_OSCILLATOR_FAMILY_BASE_REGISTRY_151_225 = {
    "f30_wtof_151_wto_typical_price_median_hl": {"inputs": ["high", "low", "close"], "func": f30_wtof_151_wto_typical_price_median_hl},
    "f30_wtof_152_wto_typical_price_weighted_2c_h_l": {"inputs": ["high", "low", "close"], "func": f30_wtof_152_wto_typical_price_weighted_2c_h_l},
    "f30_wtof_153_wto_typical_price_ohlc4": {"inputs": ["open", "high", "low", "close"], "func": f30_wtof_153_wto_typical_price_ohlc4},
    "f30_wtof_154_wto_on_log_price": {"inputs": ["high", "low", "close"], "func": f30_wtof_154_wto_on_log_price},
    "f30_wtof_155_wto_typical_price_oc2": {"inputs": ["open", "close"], "func": f30_wtof_155_wto_typical_price_oc2},
    "f30_wtof_156_wto_typical_price_hlc4_with_double_close": {"inputs": ["high", "low", "close"], "func": f30_wtof_156_wto_typical_price_hlc4_with_double_close},
    "f30_wtof_157_wto_smoothed_with_hma": {"inputs": ["high", "low", "close"], "func": f30_wtof_157_wto_smoothed_with_hma},
    "f30_wtof_158_wto_smoothed_with_dema": {"inputs": ["high", "low", "close"], "func": f30_wtof_158_wto_smoothed_with_dema},
    "f30_wtof_159_wto_smoothed_with_kama": {"inputs": ["high", "low", "close"], "func": f30_wtof_159_wto_smoothed_with_kama},
    "f30_wtof_160_wto_smoothed_with_wma": {"inputs": ["high", "low", "close"], "func": f30_wtof_160_wto_smoothed_with_wma},
    "f30_wtof_161_wto_raw_ci_level_unsmoothed": {"inputs": ["high", "low", "close"], "func": f30_wtof_161_wto_raw_ci_level_unsmoothed},
    "f30_wtof_162_wto_normalized_rescaled_pm100": {"inputs": ["high", "low", "close"], "func": f30_wtof_162_wto_normalized_rescaled_pm100},
    "f30_wtof_163_wto_histogram_zero_cross_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_163_wto_histogram_zero_cross_event},
    "f30_wtof_164_wto_zero_line_cross_up_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_164_wto_zero_line_cross_up_event},
    "f30_wtof_165_wto_zero_line_cross_down_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_165_wto_zero_line_cross_down_event},
    "f30_wtof_166_wto_bars_since_bearish_cross": {"inputs": ["high", "low", "close"], "func": f30_wtof_166_wto_bars_since_bearish_cross},
    "f30_wtof_167_wto_double_bottom_oversold_in_21d": {"inputs": ["high", "low", "close"], "func": f30_wtof_167_wto_double_bottom_oversold_in_21d},
    "f30_wtof_168_wto_overbought_then_bearish_cross_within_5": {"inputs": ["high", "low", "close"], "func": f30_wtof_168_wto_overbought_then_bearish_cross_within_5},
    "f30_wtof_169_wto_failed_bearish_cross_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_169_wto_failed_bearish_cross_event},
    "f30_wtof_170_wto_long_horizon_zero_cross_down_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_170_wto_long_horizon_zero_cross_down_event},
    "f30_wtof_171_wto_short_horizon_zero_cross_down_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_171_wto_short_horizon_zero_cross_down_event},
    "f30_wtof_172_wto_micro_horizon_3_5": {"inputs": ["high", "low", "close"], "func": f30_wtof_172_wto_micro_horizon_3_5},
    "f30_wtof_173_wto_intermediate_horizon_15_30": {"inputs": ["high", "low", "close"], "func": f30_wtof_173_wto_intermediate_horizon_15_30},
    "f30_wtof_174_wto_very_long_horizon_50_100": {"inputs": ["high", "low", "close"], "func": f30_wtof_174_wto_very_long_horizon_50_100},
    "f30_wtof_175_wto_secular_horizon_100_200": {"inputs": ["high", "low", "close"], "func": f30_wtof_175_wto_secular_horizon_100_200},
    "f30_wtof_176_ttm_squeeze_on_carter_classic": {"inputs": ["high", "low", "close"], "func": f30_wtof_176_ttm_squeeze_on_carter_classic},
    "f30_wtof_177_ttm_momentum_histogram": {"inputs": ["high", "low", "close"], "func": f30_wtof_177_ttm_momentum_histogram},
    "f30_wtof_178_ttm_fired_direction_sign": {"inputs": ["high", "low", "close"], "func": f30_wtof_178_ttm_fired_direction_sign},
    "f30_wtof_179_ttm_histogram_color_bull_to_bear_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_179_ttm_histogram_color_bull_to_bear_event},
    "f30_wtof_180_ttm_squeeze_count_63d": {"inputs": ["high", "low", "close"], "func": f30_wtof_180_ttm_squeeze_count_63d},
    "f30_wtof_181_ttm_bars_since_last_fire": {"inputs": ["high", "low", "close"], "func": f30_wtof_181_ttm_bars_since_last_fire},
    "f30_wtof_182_ttm_current_in_squeeze_streak": {"inputs": ["high", "low", "close"], "func": f30_wtof_182_ttm_current_in_squeeze_streak},
    "f30_wtof_183_ttm_fired_with_positive_momentum_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_183_ttm_fired_with_positive_momentum_event},
    "f30_wtof_184_ttm_fired_with_negative_momentum_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_184_ttm_fired_with_negative_momentum_event},
    "f30_wtof_185_ttm_histogram_falling_after_fire_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_185_ttm_histogram_falling_after_fire_event},
    "f30_wtof_186_squeeze_pro_low_compression_on": {"inputs": ["high", "low", "close"], "func": f30_wtof_186_squeeze_pro_low_compression_on},
    "f30_wtof_187_squeeze_pro_mid_compression_on": {"inputs": ["high", "low", "close"], "func": f30_wtof_187_squeeze_pro_mid_compression_on},
    "f30_wtof_188_squeeze_pro_high_compression_on": {"inputs": ["high", "low", "close"], "func": f30_wtof_188_squeeze_pro_high_compression_on},
    "f30_wtof_189_squeeze_pro_compression_level": {"inputs": ["high", "low", "close"], "func": f30_wtof_189_squeeze_pro_compression_level},
    "f30_wtof_190_squeeze_pro_progression_to_higher_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_190_squeeze_pro_progression_to_higher_event},
    "f30_wtof_191_squeeze_pro_high_then_release_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_191_squeeze_pro_high_then_release_event},
    "f30_wtof_192_squeeze_pro_high_dwell_63d": {"inputs": ["high", "low", "close"], "func": f30_wtof_192_squeeze_pro_high_dwell_63d},
    "f30_wtof_193_squeeze_pro_fired_from_high_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_193_squeeze_pro_fired_from_high_event},
    "f30_wtof_194_squeeze_pro_low_dwell_252d": {"inputs": ["high", "low", "close"], "func": f30_wtof_194_squeeze_pro_low_dwell_252d},
    "f30_wtof_195_squeeze_pro_total_squeeze_count_63d": {"inputs": ["high", "low", "close"], "func": f30_wtof_195_squeeze_pro_total_squeeze_count_63d},
    "f30_wtof_196_squeeze_pro_aligned_with_positive_momentum": {"inputs": ["high", "low", "close"], "func": f30_wtof_196_squeeze_pro_aligned_with_positive_momentum},
    "f30_wtof_197_squeeze_pro_aligned_with_negative_momentum": {"inputs": ["high", "low", "close"], "func": f30_wtof_197_squeeze_pro_aligned_with_negative_momentum},
    "f30_wtof_198_ttm_fired_then_drawdown_5d_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_198_ttm_fired_then_drawdown_5d_event},
    "f30_wtof_199_ttm_squeeze_max_streak_252d": {"inputs": ["high", "low", "close"], "func": f30_wtof_199_ttm_squeeze_max_streak_252d},
    "f30_wtof_200_ttm_fired_count_252d": {"inputs": ["high", "low", "close"], "func": f30_wtof_200_ttm_fired_count_252d},
    "f30_wtof_201_ttm_squeeze_release_with_negative_then_positive": {"inputs": ["high", "low", "close"], "func": f30_wtof_201_ttm_squeeze_release_with_negative_then_positive},
    "f30_wtof_202_ttm_momentum_zscore_252d": {"inputs": ["high", "low", "close"], "func": f30_wtof_202_ttm_momentum_zscore_252d},
    "f30_wtof_203_ttm_momentum_above_zero_dwell_21d": {"inputs": ["high", "low", "close"], "func": f30_wtof_203_ttm_momentum_above_zero_dwell_21d},
    "f30_wtof_204_ttm_squeeze_long_horizon_50d": {"inputs": ["high", "low", "close"], "func": f30_wtof_204_ttm_squeeze_long_horizon_50d},
    "f30_wtof_205_ttm_squeeze_short_horizon_10d": {"inputs": ["high", "low", "close"], "func": f30_wtof_205_ttm_squeeze_short_horizon_10d},
    "f30_wtof_206_pct_b_classic": {"inputs": ["high", "low", "close"], "func": f30_wtof_206_pct_b_classic},
    "f30_wtof_207_pct_b_above_one_indicator": {"inputs": ["high", "low", "close"], "func": f30_wtof_207_pct_b_above_one_indicator},
    "f30_wtof_208_pct_b_above_one_current_streak": {"inputs": ["high", "low", "close"], "func": f30_wtof_208_pct_b_above_one_current_streak},
    "f30_wtof_209_pct_b_deviation_from_half": {"inputs": ["high", "low", "close"], "func": f30_wtof_209_pct_b_deviation_from_half},
    "f30_wtof_210_pct_b_zscore_252d": {"inputs": ["high", "low", "close"], "func": f30_wtof_210_pct_b_zscore_252d},
    "f30_wtof_211_pct_b_cross_above_one_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_211_pct_b_cross_above_one_event},
    "f30_wtof_212_pct_b_cross_below_zero_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_212_pct_b_cross_below_zero_event},
    "f30_wtof_213_pct_b_rejection_from_above_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_213_pct_b_rejection_from_above_event},
    "f30_wtof_214_pct_b_above_eighty_pct_dwell_21d": {"inputs": ["high", "low", "close"], "func": f30_wtof_214_pct_b_above_eighty_pct_dwell_21d},
    "f30_wtof_215_pct_b_long_horizon_50d": {"inputs": ["high", "low", "close"], "func": f30_wtof_215_pct_b_long_horizon_50d},
    "f30_wtof_216_bandwidth_pct_of_mid_classic": {"inputs": ["high", "low", "close"], "func": f30_wtof_216_bandwidth_pct_of_mid_classic},
    "f30_wtof_217_bandwidth_at_126d_low_indicator": {"inputs": ["high", "low", "close"], "func": f30_wtof_217_bandwidth_at_126d_low_indicator},
    "f30_wtof_218_bandwidth_released_after_126d_low_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_218_bandwidth_released_after_126d_low_event},
    "f30_wtof_219_bandwidth_percentile_504d": {"inputs": ["high", "low", "close"], "func": f30_wtof_219_bandwidth_percentile_504d},
    "f30_wtof_220_bandwidth_vol_of_vol_63d": {"inputs": ["high", "low", "close"], "func": f30_wtof_220_bandwidth_vol_of_vol_63d},
    "f30_wtof_221_bandwidth_skew_63d": {"inputs": ["high", "low", "close"], "func": f30_wtof_221_bandwidth_skew_63d},
    "f30_wtof_222_bandwidth_autocorr_5d_in_63d": {"inputs": ["high", "low", "close"], "func": f30_wtof_222_bandwidth_autocorr_5d_in_63d},
    "f30_wtof_223_bandwidth_above_95pct_dwell_252d": {"inputs": ["high", "low", "close"], "func": f30_wtof_223_bandwidth_above_95pct_dwell_252d},
    "f30_wtof_224_m_top_event_pct_b_lower_peak": {"inputs": ["high", "low", "close"], "func": f30_wtof_224_m_top_event_pct_b_lower_peak},
    "f30_wtof_225_m_top_count_63d": {"inputs": ["high", "low", "close"], "func": f30_wtof_225_m_top_count_63d},
}
