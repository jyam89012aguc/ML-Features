"""wave_trend_oscillator_family base features 226-300 — Pipeline 1b-technical.

Gap-fill extension continuation. Adds:
  - More M-top / W-bottom variants & %b exhaustion event chains.
  - Donchian channel width / position / breakout dynamics at 20 / 55 / 126 (Turtle).
  - Hull MA bands and Standard Error Bands (Andersen 1996).
  - Multi-band stack composites (Donchian + BB + KC alignment regimes).
  - PIT-clean DPO (no displacement leak), Schaff Trend Cycle (Doug Schaff).
  - Multi-horizon BB widths at 10/100/200 day cycles.
  - Composite topping events that span this family (TTM-fire + WTO bear cross,
    walk-upper-end + WTO rollover, SqueezePro-high + drawdown).

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
    n2 = max(int(n / 2), 2)
    nsqrt = max(int(np.sqrt(n)), 2)
    raw = 2.0 * _wma(s, n2) - _wma(s, n)
    return _wma(raw, nsqrt)


def _stochastic(s, n):
    lo = s.rolling(n, min_periods=max(n // 3, 2)).min()
    hi = s.rolling(n, min_periods=max(n // 3, 2)).max()
    return 100.0 * _safe_div(s - lo, hi - lo)


# ---------------------------- indicator primitives ----------------------------

def _wto_default(high, low, close, n1=10, n2=21):
    ap = (high + low + close) / 3.0
    esa = _ema(ap, n1)
    d = _ema((ap - esa).abs(), n1)
    ci = _safe_div(ap - esa, 0.015 * d)
    tci = _ema(ci, n2)
    wt2 = tci.rolling(4, min_periods=2).mean()
    return tci, wt2


def _bb(close, n=20, mult=2.0):
    mid = close.rolling(n, min_periods=max(n // 3, 2)).mean()
    sd = close.rolling(n, min_periods=max(n // 3, 2)).std()
    return mid, mid + mult * sd, mid - mult * sd


def _kc(high, low, close, n=20, mult=1.5):
    mid = close.rolling(n, min_periods=max(n // 3, 2)).mean()
    tr = _true_range(high, low, close)
    rng = tr.rolling(n, min_periods=max(n // 3, 2)).mean()
    return mid, mid + mult * rng, mid - mult * rng


def _pct_b(close, n=20, mult=2.0):
    _, bbu, bbl = _bb(close, n=n, mult=mult)
    return _safe_div(close - bbl, bbu - bbl)


def _bb_width_pct(close, n=20, mult=2.0):
    mid, bbu, bbl = _bb(close, n=n, mult=mult)
    return _safe_div(bbu - bbl, mid)


def _donchian(high, low, n):
    upper = high.rolling(n, min_periods=max(n // 3, 2)).max()
    lower = low.rolling(n, min_periods=max(n // 3, 2)).min()
    return upper, lower


def _ttm_squeeze_on(high, low, close, n=20, mult_bb=2.0, mult_kc=1.5):
    _, bbu, bbl = _bb(close, n=n, mult=mult_bb)
    _, kcu, kcl = _kc(high, low, close, n=n, mult=mult_kc)
    on = (bbu < kcu) & (bbl > kcl)
    return on.astype(float).where(bbu.notna() & kcu.notna(), np.nan)


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


def _stderr_bands(close, n=21, k=2.0):
    """Andersen Standard Error Bands: 21-period LinReg endpoint ± 2*stderr, then 3-bar SMA smoothed."""
    def _lr_end(w):
        valid = ~np.isnan(w)
        if valid.sum() < max(n // 3, 2):
            return np.nan
        x = np.arange(len(w), dtype=float)
        if valid.all():
            xv = x; wv = w
        else:
            xv = x[valid]; wv = w[valid]
        xm = xv.mean(); wm = wv.mean()
        sx = ((xv - xm) ** 2).sum()
        if sx == 0:
            return np.nan
        b = ((xv - xm) * (wv - wm)).sum() / sx
        a = wm - b * xm
        return a + b * (len(w) - 1)
    def _se_est(w):
        valid = ~np.isnan(w)
        if valid.sum() < max(n // 3, 2):
            return np.nan
        x = np.arange(len(w), dtype=float)
        if valid.all():
            xv = x; wv = w
        else:
            xv = x[valid]; wv = w[valid]
        if len(xv) < 3:
            return np.nan
        xm = xv.mean(); wm = wv.mean()
        sx = ((xv - xm) ** 2).sum()
        if sx == 0:
            return np.nan
        b = ((xv - xm) * (wv - wm)).sum() / sx
        a = wm - b * xm
        resid = wv - (a + b * xv)
        return float(np.sqrt((resid ** 2).sum() / max(len(xv) - 2, 1)))
    mid = close.rolling(n, min_periods=max(n // 3, 2)).apply(_lr_end, raw=True)
    se = close.rolling(n, min_periods=max(n // 3, 2)).apply(_se_est, raw=True)
    mid_s = mid.rolling(3, min_periods=2).mean()
    se_s = se.rolling(3, min_periods=2).mean()
    return mid_s, mid_s + k * se_s, mid_s - k * se_s


def _stc(close, fast=23, slow=50, cycle=10):
    """Schaff Trend Cycle (Doug Schaff): double-stoch of MACD."""
    macd = _ema(close, fast) - _ema(close, slow)
    k1 = _stochastic(macd, cycle)
    d1 = _ema(k1, 3)
    k2 = _stochastic(d1, cycle)
    stc = _ema(k2, 3)
    return stc


def _streak_true(b: pd.Series) -> pd.Series:
    bb = b.fillna(False).astype(int)
    grp = (bb != bb.shift()).cumsum()
    out = bb.groupby(grp).cumsum() * bb
    return out.astype(float)


# ============================================================
# Bucket C cont. — %b exhaustion and W-bottom (226-235)
# ============================================================

def f30_wtof_226_w_bottom_event_pct_b_higher_trough(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bollinger W-bottom: today %b<0.05 AND prior trough within 21d had lower %b — mirror of M-top."""
    pb = _pct_b(close, n=20, mult=2.0)
    near_lower_now = pb < 0.05
    pb_prior_min = pb.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    cond = near_lower_now & (pb > pb_prior_min)
    return cond.astype(float).where(pb.notna() & pb_prior_min.notna(), np.nan)


def f30_wtof_227_w_bottom_count_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Trailing 63d count of W-bottom events — repeated lower-band-rejection density."""
    pb = _pct_b(close, n=20, mult=2.0)
    near_lower = pb < 0.05
    pb_prior_min = pb.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    ev = near_lower & (pb > pb_prior_min)
    return ev.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f30_wtof_228_pct_b_walk_then_collapse_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: %b > 1 for ≥3 of trailing 10 bars AND today %b < 0.5 — walk-then-collapse exhaustion."""
    pb = _pct_b(close, n=20, mult=2.0)
    walked = (pb.shift(1) > 1.0).rolling(10, min_periods=3).sum() >= 3
    cond = walked & (pb < 0.5)
    return cond.astype(float).where(pb.notna(), np.nan)


def f30_wtof_229_pct_b_decline_rate_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-bar decline in %b (positive = falling toward midline) — band-position fade rate."""
    pb = _pct_b(close, n=20, mult=2.0)
    return pb.shift(5) - pb


def f30_wtof_230_pct_b_max_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Trailing 21d maximum %b — recent upper-band-reach magnitude."""
    pb = _pct_b(close, n=20, mult=2.0)
    return pb.rolling(MDAYS, min_periods=WDAYS).max()


def f30_wtof_231_pct_b_drop_from_21d_max(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """%b distance below its 21d trailing max — drop-from-peak band position."""
    pb = _pct_b(close, n=20, mult=2.0)
    mx = pb.rolling(MDAYS, min_periods=WDAYS).max()
    return mx - pb


def f30_wtof_232_m_top_then_wto_bearish_cross_within_5(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: M-top occurred within trailing 5 bars AND WTO bearish cross today — Bollinger+WT confirmation."""
    pb = _pct_b(close, n=20, mult=2.0)
    pb_prior_max = pb.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    m_top = (pb > 0.95) & (pb < pb_prior_max)
    m_recent = m_top.rolling(WDAYS, min_periods=2).max().astype(bool)
    wt1, wt2 = _wto_default(high, low, close, 10, 21)
    bear = (wt1 < wt2) & (wt1.shift(1) >= wt2.shift(1))
    return (m_recent & bear).astype(float).where(pb.notna() & wt1.notna(), np.nan)


def f30_wtof_233_pct_b_walking_upper_3_of_5_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: %b > 1 on ≥3 of trailing 5 bars — Bollinger 'walking-the-upper-band' regime."""
    pb = _pct_b(close, n=20, mult=2.0)
    cnt = (pb > 1.0).astype(float).rolling(WDAYS, min_periods=3).sum()
    return (cnt >= 3).astype(float).where(pb.notna(), np.nan)


def f30_wtof_234_pct_b_streak_above_one_then_below_half(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: %b had a ≥5-bar streak above 1 ending within trailing 5 bars AND now %b<0.5 — extreme exhaustion."""
    pb = _pct_b(close, n=20, mult=2.0)
    streak = _streak_true(pb > 1.0)
    streak_was_5 = (streak.shift(1) >= 5.0).rolling(WDAYS, min_periods=2).max().astype(bool)
    cond = streak_was_5 & (pb < 0.5)
    return cond.astype(float).where(pb.notna(), np.nan)


def f30_wtof_235_pct_b_post_walk_min_in_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Trailing 5d minimum of %b given a walk-upper event within trailing 21d — post-walk floor."""
    pb = _pct_b(close, n=20, mult=2.0)
    walked = (pb > 1.0).rolling(MDAYS, min_periods=WDAYS).max().astype(bool)
    mn5 = pb.rolling(WDAYS, min_periods=2).min()
    return mn5.where(walked, np.nan)


# ============================================================
# Bucket D — Donchian, HMA bands, StdErr bands, multi-band stack (236-260)
# ============================================================

def f30_wtof_236_donchian_width_20d_pct_of_mid(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Donchian 20d channel width as fraction of midpoint — Turtle short-term range."""
    u, l = _donchian(high, low, 20)
    return _safe_div(u - l, (u + l) / 2.0)


def f30_wtof_237_donchian_width_55d_pct_of_mid(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Donchian 55d channel width as fraction of midpoint — Turtle long-term range."""
    u, l = _donchian(high, low, 55)
    return _safe_div(u - l, (u + l) / 2.0)


def f30_wtof_238_donchian_width_126d_pct_of_mid(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Donchian 126d (6-mo) channel width — semi-annual range expansion hypothesis."""
    u, l = _donchian(high, low, 126)
    return _safe_div(u - l, (u + l) / 2.0)


def f30_wtof_239_donchian_position_20d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Position of close within 20d Donchian channel: 0=at lower, 1=at upper."""
    u, l = _donchian(high, low, 20)
    return _safe_div(close - l, u - l)


def f30_wtof_240_donchian_position_55d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Position of close within 55d Donchian channel — longer-cycle range position."""
    u, l = _donchian(high, low, 55)
    return _safe_div(close - l, u - l)


def f30_wtof_241_donchian_breakout_20d_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: high makes new 20d Donchian upper (excluding today's high in lookback) — Turtle entry."""
    u_prev = high.shift(1).rolling(20, min_periods=10).max()
    ev = high > u_prev
    return ev.astype(float).where(u_prev.notna(), np.nan)


def f30_wtof_242_donchian_breakdown_20d_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: low makes new 20d Donchian lower (excluding today) — Turtle short entry."""
    l_prev = low.shift(1).rolling(20, min_periods=10).min()
    ev = low < l_prev
    return ev.astype(float).where(l_prev.notna(), np.nan)


def f30_wtof_243_donchian_breakout_55d_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: high makes new 55d Donchian upper — Turtle System 2 long entry."""
    u_prev = high.shift(1).rolling(55, min_periods=21).max()
    ev = high > u_prev
    return ev.astype(float).where(u_prev.notna(), np.nan)


def f30_wtof_244_donchian_breakdown_55d_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: low makes new 55d Donchian lower — Turtle System 2 short entry."""
    l_prev = low.shift(1).rolling(55, min_periods=21).min()
    ev = low < l_prev
    return ev.astype(float).where(l_prev.notna(), np.nan)


def f30_wtof_245_donchian_failed_breakout_20d_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: high exceeded 20d Donchian upper within trailing 5 bars BUT close < that prior upper today — failed Turtle long."""
    u_prev = high.shift(1).rolling(20, min_periods=10).max()
    broke = high > u_prev
    broke_recent = broke.rolling(WDAYS, min_periods=2).max().astype(bool)
    u_now = high.rolling(20, min_periods=10).max()
    # require close back inside (below the breakout reference)
    cond = broke_recent & (close < u_prev)
    return cond.astype(float).where(u_prev.notna(), np.nan)


def f30_wtof_246_hma_band_upper_distance_atr_norm(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-normalized distance of close above HMA(20)+2*ATR(20) — Hull-band breach magnitude."""
    n = 20
    hma = _hma(close, n)
    a = _atr(high, low, close, n=n)
    upper = hma + 2.0 * a
    return _safe_div(close - upper, a)


def f30_wtof_247_close_above_hma_upper_band_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: close > HMA(20)+2*ATR(20) — Hull upper-band breach state."""
    n = 20
    hma = _hma(close, n)
    a = _atr(high, low, close, n=n)
    upper = hma + 2.0 * a
    return (close > upper).astype(float).where(upper.notna(), np.nan)


def f30_wtof_248_hma_distance_atr_norm(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(Close − HMA(20)) / ATR(20) — Hull-MA-based directional extension."""
    n = 20
    hma = _hma(close, n)
    a = _atr(high, low, close, n=n)
    return _safe_div(close - hma, a)


def f30_wtof_249_hma_band_width_atr_units(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Hull-band width in ATR units (constant by construction here — proxy hypothesis: 4*ATR/HMA)."""
    n = 20
    hma = _hma(close, n)
    a = _atr(high, low, close, n=n)
    return _safe_div(4.0 * a, hma)


def f30_wtof_250_hma_slope_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21d slope of HMA(20) — Hull trend velocity (less laggy than SMA slope)."""
    n = 20
    hma = _hma(close, n)
    return _rolling_slope(hma, MDAYS)


def f30_wtof_251_stderr_bands_width_pct_of_mid(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Andersen Standard Error Bands width / midline — regression-residual volatility envelope."""
    mid, u, l = _stderr_bands(close, n=21, k=2.0)
    return _safe_div(u - l, mid)


def f30_wtof_252_stderr_bands_position(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Position of close in SE bands: 0=lower, 1=upper — regression-residual band-relative position."""
    mid, u, l = _stderr_bands(close, n=21, k=2.0)
    return _safe_div(close - l, u - l)


def f30_wtof_253_stderr_bands_narrowing_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: SE-band width < its 21d trailing mean — trending-low-error regime per Andersen."""
    mid, u, l = _stderr_bands(close, n=21, k=2.0)
    w = u - l
    return (w < w.rolling(MDAYS, min_periods=WDAYS).mean()).astype(float).where(w.notna(), np.nan)


def f30_wtof_254_close_above_stderr_upper_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: close > SE upper band — regression-residual upper breach."""
    mid, u, l = _stderr_bands(close, n=21, k=2.0)
    return (close > u).astype(float).where(u.notna(), np.nan)


def f30_wtof_255_stderr_mid_slope_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21d slope of SE-band midline (LinReg endpoint) — trend regression-line velocity."""
    mid, u, l = _stderr_bands(close, n=21, k=2.0)
    return _rolling_slope(mid, MDAYS)


def f30_wtof_256_multi_band_above_upper_count(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of upper bands close exceeds (Donchian20 / BB20 / KC20) — 0-3 multi-band overshoot."""
    du, _ = _donchian(high, low, 20)
    _, bbu, _ = _bb(close, n=20, mult=2.0)
    _, kcu, _ = _kc(high, low, close, n=20, mult=1.5)
    out = ((close > du.shift(1)).astype(float)
           + (close > bbu).astype(float)
           + (close > kcu).astype(float))
    return out.where(du.notna() & bbu.notna() & kcu.notna(), np.nan)


def f30_wtof_257_multi_band_all_narrow_regime(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: Donchian20 width, BB20 width, KC20 width all below their 63d median — all-bands-tight regime."""
    du, dl = _donchian(high, low, 20)
    dw = _safe_div(du - dl, (du + dl) / 2.0)
    bw = _bb_width_pct(close, n=20, mult=2.0)
    mid_kc, kcu, kcl = _kc(high, low, close, n=20, mult=1.5)
    kw = _safe_div(kcu - kcl, mid_kc)
    cond = ((dw < dw.rolling(QDAYS, min_periods=MDAYS).median())
            & (bw < bw.rolling(QDAYS, min_periods=MDAYS).median())
            & (kw < kw.rolling(QDAYS, min_periods=MDAYS).median()))
    return cond.astype(float).where(dw.notna() & bw.notna() & kw.notna(), np.nan)


def f30_wtof_258_multi_band_breakout_event_count(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Number of upper-band breakouts (Donchian20, BB20, KC20) occurring on this bar — 0-3 aligned breakout."""
    du, _ = _donchian(high, low, 20)
    _, bbu, _ = _bb(close, n=20, mult=2.0)
    _, kcu, _ = _kc(high, low, close, n=20, mult=1.5)
    dc_break = (high > du.shift(1))
    bb_break = (close > bbu) & (close.shift(1) <= bbu.shift(1))
    kc_break = (close > kcu) & (close.shift(1) <= kcu.shift(1))
    out = dc_break.astype(float) + bb_break.astype(float) + kc_break.astype(float)
    return out.where(du.notna() & bbu.notna() & kcu.notna(), np.nan)


def f30_wtof_259_multi_band_aligned_narrow_streak(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current consecutive streak of all-bands-narrow regime — multi-band compression persistence."""
    du, dl = _donchian(high, low, 20)
    dw = _safe_div(du - dl, (du + dl) / 2.0)
    bw = _bb_width_pct(close, n=20, mult=2.0)
    mid_kc, kcu, kcl = _kc(high, low, close, n=20, mult=1.5)
    kw = _safe_div(kcu - kcl, mid_kc)
    cond = ((dw < dw.rolling(QDAYS, min_periods=MDAYS).median())
            & (bw < bw.rolling(QDAYS, min_periods=MDAYS).median())
            & (kw < kw.rolling(QDAYS, min_periods=MDAYS).median()))
    return _streak_true(cond).where(dw.notna() & bw.notna() & kw.notna(), np.nan)


def f30_wtof_260_multi_band_squeeze_release_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: was in all-bands-narrow regime within trailing 5 bars AND today regime exits — multi-band release."""
    du, dl = _donchian(high, low, 20)
    dw = _safe_div(du - dl, (du + dl) / 2.0)
    bw = _bb_width_pct(close, n=20, mult=2.0)
    mid_kc, kcu, kcl = _kc(high, low, close, n=20, mult=1.5)
    kw = _safe_div(kcu - kcl, mid_kc)
    cond = ((dw < dw.rolling(QDAYS, min_periods=MDAYS).median())
            & (bw < bw.rolling(QDAYS, min_periods=MDAYS).median())
            & (kw < kw.rolling(QDAYS, min_periods=MDAYS).median()))
    was = cond.shift(1).rolling(WDAYS, min_periods=2).max().astype(bool)
    return (was & (~cond)).astype(float).where(dw.notna() & bw.notna() & kw.notna(), np.nan)


# ============================================================
# Bucket E — PIT-DPO, Schaff Trend Cycle, multi-horizon BB (261-285)
# ============================================================

def f30_wtof_261_dpo_pit_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """PIT-clean DPO: close − trailing 21d SMA (no centered displacement) — cycle deviation 21d."""
    sma = close.rolling(MDAYS, min_periods=WDAYS).mean()
    return close - sma


def f30_wtof_262_dpo_pit_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """PIT-clean DPO: close − trailing 63d SMA — quarterly cycle deviation."""
    sma = close.rolling(QDAYS, min_periods=MDAYS).mean()
    return close - sma


def f30_wtof_263_dpo_pit_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """PIT-clean DPO: close − trailing 126d SMA — half-year cycle deviation."""
    sma = close.rolling(126, min_periods=QDAYS).mean()
    return close - sma


def f30_wtof_264_dpo_pit_21d_sign(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sign of PIT-DPO 21d — above/below cycle midline."""
    sma = close.rolling(MDAYS, min_periods=WDAYS).mean()
    return np.sign(close - sma).where((close - sma).notna(), np.nan)


def f30_wtof_265_dpo_pit_21d_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of PIT-DPO 21d in trailing 252d — anomalous cycle deviation."""
    sma = close.rolling(MDAYS, min_periods=WDAYS).mean()
    return _rolling_zscore(close - sma, YDAYS, min_periods=QDAYS)


def f30_wtof_266_schaff_trend_cycle(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Schaff Trend Cycle (Doug Schaff 1990s) — double-smoothed-stochastic of MACD oscillator."""
    return _stc(close, fast=23, slow=50, cycle=10)


def f30_wtof_267_stc_above_75_overbought_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: STC > 75 — Schaff overbought regime."""
    stc = _stc(close, fast=23, slow=50, cycle=10)
    return (stc > 75.0).astype(float).where(stc.notna(), np.nan)


def f30_wtof_268_stc_cross_below_75_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: STC crosses below 75 from above — Schaff overbought exit (topping signal)."""
    stc = _stc(close, fast=23, slow=50, cycle=10)
    ev = (stc < 75.0) & (stc.shift(1) >= 75.0)
    return ev.astype(float).where(stc.notna() & stc.shift(1).notna(), np.nan)


def f30_wtof_269_stc_bars_since_last_overbought_exit(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since last STC cross-below-75 event — recency of Schaff topping signal."""
    stc = _stc(close, fast=23, slow=50, cycle=10)
    ev = (stc < 75.0) & (stc.shift(1) >= 75.0)
    idx = np.arange(len(close), dtype=float)
    last = pd.Series(np.where(ev.fillna(False), idx, np.nan), index=close.index).ffill()
    return (pd.Series(idx, index=close.index) - last).where(stc.notna(), np.nan)


def f30_wtof_270_stc_peaks_count_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Trailing 252d count of STC cross-below-75 events — annual Schaff topping density."""
    stc = _stc(close, fast=23, slow=50, cycle=10)
    ev = (stc < 75.0) & (stc.shift(1) >= 75.0)
    return ev.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f30_wtof_271_stc_long_horizon_46_100(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """STC at long horizon (fast=46, slow=100, cycle=20) — multi-month Schaff Cycle hypothesis."""
    return _stc(close, fast=46, slow=100, cycle=20)


def f30_wtof_272_stc_wto_aligned_overbought(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: STC>75 AND WT1>60 — double overbought confirmation."""
    stc = _stc(close, fast=23, slow=50, cycle=10)
    wt1, _ = _wto_default(high, low, close, 10, 21)
    cond = (stc > 75.0) & (wt1 > 60.0)
    return cond.astype(float).where(stc.notna() & wt1.notna(), np.nan)


def f30_wtof_273_stc_falling_from_above_90_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: STC > 90 yesterday AND STC falling today — extreme Schaff exhaustion."""
    stc = _stc(close, fast=23, slow=50, cycle=10)
    cond = (stc.shift(1) > 90.0) & (stc < stc.shift(1))
    return cond.astype(float).where(stc.notna() & stc.shift(1).notna(), np.nan)


def f30_wtof_274_bb_width_10d_horizon(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """BB width pct-of-mid at 10d — sub-month volatility cycle hypothesis."""
    return _bb_width_pct(close, n=10, mult=2.0)


def f30_wtof_275_bb_width_100d_horizon(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """BB width pct-of-mid at 100d — multi-month volatility regime hypothesis."""
    return _bb_width_pct(close, n=100, mult=2.0)


def f30_wtof_276_bb_width_200d_horizon(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """BB width pct-of-mid at 200d — long-term structural volatility hypothesis."""
    return _bb_width_pct(close, n=200, mult=2.0)


def f30_wtof_277_bb_width_horizon_rank_mean(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean percentile rank of BW across 10/20/50/100d horizons in trailing 252d — composite vol-regime rank."""
    bws = [
        _bb_width_pct(close, n=10, mult=2.0),
        _bb_width_pct(close, n=20, mult=2.0),
        _bb_width_pct(close, n=50, mult=2.0),
        _bb_width_pct(close, n=100, mult=2.0),
    ]
    ranks = [b.rolling(YDAYS, min_periods=QDAYS).rank(pct=True) for b in bws]
    return pd.concat([r.rename(i) for i, r in enumerate(ranks)], axis=1).mean(axis=1)


def f30_wtof_278_bb_position_at_200d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """%b at 200d/2σ — structural-cycle band position hypothesis."""
    return _pct_b(close, n=200, mult=2.0)


def f30_wtof_279_bb_width_regime_low_fraction_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Trailing 252d fraction of bars in low-BW regime (BW percentile ≤ 25th)."""
    bw = _bb_width_pct(close, n=20, mult=2.0)
    p = bw.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    return (p <= 0.25).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f30_wtof_280_bb_width_regime_mid_fraction_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Trailing 252d fraction of bars in mid-BW regime (25th < BW pct ≤ 75th)."""
    bw = _bb_width_pct(close, n=20, mult=2.0)
    p = bw.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    return ((p > 0.25) & (p <= 0.75)).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f30_wtof_281_bb_width_regime_high_fraction_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Trailing 252d fraction of bars in high-BW regime (BW percentile > 75th)."""
    bw = _bb_width_pct(close, n=20, mult=2.0)
    p = bw.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    return (p > 0.75).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f30_wtof_282_bb_width_50_vs_200_spread(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Spread between BW(50) and BW(200) — short-vs-long volatility regime divergence."""
    return _bb_width_pct(close, n=50, mult=2.0) - _bb_width_pct(close, n=200, mult=2.0)


def f30_wtof_283_squeeze_momentum_long_100d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Squeeze Momentum at 100d horizon (LazyBear formula) — secular impulse hypothesis."""
    n = 100
    hh = high.rolling(n, min_periods=max(n // 3, 2)).max()
    ll = low.rolling(n, min_periods=max(n // 3, 2)).min()
    sma_c = close.rolling(n, min_periods=max(n // 3, 2)).mean()
    val = close - ((hh + ll) / 2.0 + sma_c) / 2.0
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


def f30_wtof_284_bb_walking_lower_band_count_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Trailing 21d count of bars with close < lower BB(20,2) — walking-the-lower-band (mirror)."""
    _, _, bbl = _bb(close, n=20, mult=2.0)
    return (close < bbl).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f30_wtof_285_bb_width_change_long_horizon_504d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """504d log change in BB(20) width — biennial structural volatility shift."""
    bw = _bb_width_pct(close, n=20, mult=2.0)
    return _safe_log(bw) - _safe_log(bw.shift(DDAYS_2Y))


# ============================================================
# Bucket F — Composites and event-recency cross-family-within-wtof (286-300)
# ============================================================

def f30_wtof_286_bars_since_ttm_fire(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Recency: bars since most recent TTM squeeze fire — Carter-event timing."""
    on = _ttm_squeeze_on(high, low, close, n=20)
    fired = (on == 0) & (on.shift(1) == 1)
    idx = np.arange(len(close), dtype=float)
    last = pd.Series(np.where(fired.fillna(False), idx, np.nan), index=close.index).ffill()
    return (pd.Series(idx, index=close.index) - last).where(on.notna(), np.nan)


def f30_wtof_287_bars_since_wto_ob_exit(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Recency: bars since most recent WT1 exit below 60 from above — WTO overbought-exit timing."""
    wt1, _ = _wto_default(high, low, close, 10, 21)
    ev = (wt1 < 60.0) & (wt1.shift(1) >= 60.0)
    idx = np.arange(len(close), dtype=float)
    last = pd.Series(np.where(ev.fillna(False), idx, np.nan), index=close.index).ffill()
    return (pd.Series(idx, index=close.index) - last).where(wt1.notna(), np.nan)


def f30_wtof_288_bars_since_wto_zero_cross_down(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Recency: bars since WT1 last crossed below zero — recency of WTO regime-flip-down."""
    wt1, _ = _wto_default(high, low, close, 10, 21)
    ev = (wt1 < 0) & (wt1.shift(1) >= 0)
    idx = np.arange(len(close), dtype=float)
    last = pd.Series(np.where(ev.fillna(False), idx, np.nan), index=close.index).ffill()
    return (pd.Series(idx, index=close.index) - last).where(wt1.notna(), np.nan)


def f30_wtof_289_bars_since_pct_b_walk_end(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Recency: bars since walking-upper-band (%b>1) regime ended — recency of walk-end."""
    pb = _pct_b(close, n=20, mult=2.0)
    walking = (pb > 1.0)
    end = walking.shift(1).fillna(False) & (~walking.fillna(False))
    idx = np.arange(len(close), dtype=float)
    last = pd.Series(np.where(end, idx, np.nan), index=close.index).ffill()
    return (pd.Series(idx, index=close.index) - last).where(pb.notna(), np.nan)


def f30_wtof_290_walk_upper_then_ttm_fire_within_5_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: walking-upper (%b>1) within trailing 21d AND TTM fires today — euphoric-release topping."""
    pb = _pct_b(close, n=20, mult=2.0)
    walked = (pb > 1.0).rolling(MDAYS, min_periods=WDAYS).max().astype(bool)
    on = _ttm_squeeze_on(high, low, close, n=20)
    fired = (on == 0) & (on.shift(1) == 1)
    return (walked & fired).astype(float).where(pb.notna() & on.notna(), np.nan)


def f30_wtof_291_ttm_fire_then_21d_drawdown(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: TTM fired within trailing 21d AND close ≤ −5% from that fire bar — failed-fire setup."""
    on = _ttm_squeeze_on(high, low, close, n=20)
    fired = (on == 0) & (on.shift(1) == 1)
    idx = np.arange(len(close), dtype=float)
    last_fire = pd.Series(np.where(fired.fillna(False), idx, np.nan), index=close.index).ffill()
    bars_since = pd.Series(idx, index=close.index) - last_fire
    price_at_fire = close.where(fired.fillna(False)).ffill()
    rel = _safe_div(close, price_at_fire) - 1.0
    cond = (bars_since <= MDAYS) & (rel <= -0.05)
    return cond.astype(float).where(on.notna() & price_at_fire.notna(), np.nan)


def f30_wtof_292_multi_band_release_count_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Trailing 21d count of multi-band squeeze releases (Donchian+BB+KC all-narrow regime ends)."""
    du, dl = _donchian(high, low, 20)
    dw = _safe_div(du - dl, (du + dl) / 2.0)
    bw = _bb_width_pct(close, n=20, mult=2.0)
    mid_kc, kcu, kcl = _kc(high, low, close, n=20, mult=1.5)
    kw = _safe_div(kcu - kcl, mid_kc)
    cond = ((dw < dw.rolling(QDAYS, min_periods=MDAYS).median())
            & (bw < bw.rolling(QDAYS, min_periods=MDAYS).median())
            & (kw < kw.rolling(QDAYS, min_periods=MDAYS).median()))
    release = cond.shift(1).fillna(False) & (~cond.fillna(False))
    return release.astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f30_wtof_293_pct_b_streak_end_then_drawdown_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: %b>1 streak of ≥5 ended within trailing 5 bars AND close ≤ −3% from streak-end."""
    pb = _pct_b(close, n=20, mult=2.0)
    walking = (pb > 1.0)
    streak = _streak_true(walking)
    end_5 = (streak.shift(1) >= 5) & (~walking.fillna(False))
    idx = np.arange(len(close), dtype=float)
    last_end = pd.Series(np.where(end_5.fillna(False), idx, np.nan), index=close.index).ffill()
    bars_since = pd.Series(idx, index=close.index) - last_end
    price_at_end = close.where(end_5.fillna(False)).ffill()
    rel = _safe_div(close, price_at_end) - 1.0
    cond = (bars_since <= WDAYS) & (rel <= -0.03)
    return cond.astype(float).where(pb.notna() & price_at_end.notna(), np.nan)


def f30_wtof_294_full_topping_complex_pro_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: TTM fire (mom<0) AND WTO bearish cross AND %b walk ended within trailing 5 bars — full topping confluence."""
    on = _ttm_squeeze_on(high, low, close, n=20)
    mom = _ttm_momentum(high, low, close, n=20)
    fired = (on == 0) & (on.shift(1) == 1)
    bear_fire = fired & (mom < 0)
    bf_recent = bear_fire.rolling(WDAYS, min_periods=2).max().astype(bool)
    wt1, wt2 = _wto_default(high, low, close, 10, 21)
    wt_bear = (wt1 < wt2) & (wt1.shift(1) >= wt2.shift(1))
    wt_recent = wt_bear.rolling(WDAYS, min_periods=2).max().astype(bool)
    pb = _pct_b(close, n=20, mult=2.0)
    walking = (pb > 1.0)
    walk_end = walking.shift(1).fillna(False) & (~walking.fillna(False))
    walk_recent = walk_end.rolling(WDAYS, min_periods=2).max().astype(bool)
    cond = bf_recent & wt_recent & walk_recent
    return cond.astype(float).where(on.notna() & wt1.notna() & pb.notna(), np.nan)


def f30_wtof_295_full_topping_density_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Trailing 63d sum of full_topping_complex_pro events — multi-month topping density."""
    on = _ttm_squeeze_on(high, low, close, n=20)
    mom = _ttm_momentum(high, low, close, n=20)
    fired = (on == 0) & (on.shift(1) == 1)
    bear_fire = fired & (mom < 0)
    bf_recent = bear_fire.rolling(WDAYS, min_periods=2).max().astype(bool)
    wt1, wt2 = _wto_default(high, low, close, 10, 21)
    wt_bear = (wt1 < wt2) & (wt1.shift(1) >= wt2.shift(1))
    wt_recent = wt_bear.rolling(WDAYS, min_periods=2).max().astype(bool)
    pb = _pct_b(close, n=20, mult=2.0)
    walking = (pb > 1.0)
    walk_end = walking.shift(1).fillna(False) & (~walking.fillna(False))
    walk_recent = walk_end.rolling(WDAYS, min_periods=2).max().astype(bool)
    ev = bf_recent & wt_recent & walk_recent
    return ev.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f30_wtof_296_short_squeeze_on_long_wto_overbought(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: TTM squeeze ON at 10d AND WT1(20,50) > 60 — short-cycle coil + long-cycle overbought."""
    on_short = _ttm_squeeze_on(high, low, close, n=10, mult_bb=2.0, mult_kc=1.5)
    wt1_long, _ = _wto_default(high, low, close, 20, 50)
    cond = (on_short == 1) & (wt1_long > 60.0)
    return cond.astype(float).where(on_short.notna() & wt1_long.notna(), np.nan)


def f30_wtof_297_walk_upper_streak_end_then_wto_bear_within_5(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: walking-upper streak of ≥5 ended within trailing 5 bars AND WTO bearish cross today."""
    pb = _pct_b(close, n=20, mult=2.0)
    walking = (pb > 1.0)
    streak = _streak_true(walking)
    end_5 = (streak.shift(1) >= 5) & (~walking.fillna(False))
    end_recent = end_5.rolling(WDAYS, min_periods=2).max().astype(bool)
    wt1, wt2 = _wto_default(high, low, close, 10, 21)
    bear = (wt1 < wt2) & (wt1.shift(1) >= wt2.shift(1))
    return (end_recent & bear).astype(float).where(pb.notna() & wt1.notna(), np.nan)


def f30_wtof_298_pct_b_above_one_n_then_below_half_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: %b>1 on ≥10 of trailing 21 bars AND today %b<0.5 — sustained walk then sharp drop."""
    pb = _pct_b(close, n=20, mult=2.0)
    cnt = (pb.shift(1) > 1.0).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    return ((cnt >= 10) & (pb < 0.5)).astype(float).where(pb.notna() & cnt.notna(), np.nan)


def f30_wtof_299_squeeze_pro_high_compression_then_21d_drawdown(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: SqueezePro high-compression fired within trailing 21d AND close ≤ −5% from fire bar."""
    hi_on = _ttm_squeeze_on(high, low, close, n=20, mult_bb=2.0, mult_kc=1.0)
    fired = (hi_on.shift(1) == 1) & (hi_on == 0)
    idx = np.arange(len(close), dtype=float)
    last_fire = pd.Series(np.where(fired.fillna(False), idx, np.nan), index=close.index).ffill()
    bars_since = pd.Series(idx, index=close.index) - last_fire
    price_at_fire = close.where(fired.fillna(False)).ffill()
    rel = _safe_div(close, price_at_fire) - 1.0
    cond = (bars_since <= MDAYS) & (rel <= -0.05)
    return cond.astype(float).where(hi_on.notna() & price_at_fire.notna(), np.nan)


def f30_wtof_300_dpo_pos_then_wto_zero_cross_down_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: PIT-DPO 21d was positive within trailing 5 bars AND WT1 crosses below zero today — cycle peak rollover."""
    sma = close.rolling(MDAYS, min_periods=WDAYS).mean()
    dpo = close - sma
    pos_recent = (dpo.shift(1) > 0).rolling(WDAYS, min_periods=2).max().astype(bool)
    wt1, _ = _wto_default(high, low, close, 10, 21)
    cross_down = (wt1 < 0) & (wt1.shift(1) >= 0)
    return (pos_recent & cross_down).astype(float).where(dpo.notna() & wt1.notna(), np.nan)


# ============================================================
#                         REGISTRY 226-300
# ============================================================

WAVE_TREND_OSCILLATOR_FAMILY_BASE_REGISTRY_226_300 = {
    "f30_wtof_226_w_bottom_event_pct_b_higher_trough": {"inputs": ["high", "low", "close"], "func": f30_wtof_226_w_bottom_event_pct_b_higher_trough},
    "f30_wtof_227_w_bottom_count_63d": {"inputs": ["high", "low", "close"], "func": f30_wtof_227_w_bottom_count_63d},
    "f30_wtof_228_pct_b_walk_then_collapse_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_228_pct_b_walk_then_collapse_event},
    "f30_wtof_229_pct_b_decline_rate_5d": {"inputs": ["high", "low", "close"], "func": f30_wtof_229_pct_b_decline_rate_5d},
    "f30_wtof_230_pct_b_max_21d": {"inputs": ["high", "low", "close"], "func": f30_wtof_230_pct_b_max_21d},
    "f30_wtof_231_pct_b_drop_from_21d_max": {"inputs": ["high", "low", "close"], "func": f30_wtof_231_pct_b_drop_from_21d_max},
    "f30_wtof_232_m_top_then_wto_bearish_cross_within_5": {"inputs": ["high", "low", "close"], "func": f30_wtof_232_m_top_then_wto_bearish_cross_within_5},
    "f30_wtof_233_pct_b_walking_upper_3_of_5_indicator": {"inputs": ["high", "low", "close"], "func": f30_wtof_233_pct_b_walking_upper_3_of_5_indicator},
    "f30_wtof_234_pct_b_streak_above_one_then_below_half": {"inputs": ["high", "low", "close"], "func": f30_wtof_234_pct_b_streak_above_one_then_below_half},
    "f30_wtof_235_pct_b_post_walk_min_in_5d": {"inputs": ["high", "low", "close"], "func": f30_wtof_235_pct_b_post_walk_min_in_5d},
    "f30_wtof_236_donchian_width_20d_pct_of_mid": {"inputs": ["high", "low", "close"], "func": f30_wtof_236_donchian_width_20d_pct_of_mid},
    "f30_wtof_237_donchian_width_55d_pct_of_mid": {"inputs": ["high", "low", "close"], "func": f30_wtof_237_donchian_width_55d_pct_of_mid},
    "f30_wtof_238_donchian_width_126d_pct_of_mid": {"inputs": ["high", "low", "close"], "func": f30_wtof_238_donchian_width_126d_pct_of_mid},
    "f30_wtof_239_donchian_position_20d": {"inputs": ["high", "low", "close"], "func": f30_wtof_239_donchian_position_20d},
    "f30_wtof_240_donchian_position_55d": {"inputs": ["high", "low", "close"], "func": f30_wtof_240_donchian_position_55d},
    "f30_wtof_241_donchian_breakout_20d_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_241_donchian_breakout_20d_event},
    "f30_wtof_242_donchian_breakdown_20d_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_242_donchian_breakdown_20d_event},
    "f30_wtof_243_donchian_breakout_55d_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_243_donchian_breakout_55d_event},
    "f30_wtof_244_donchian_breakdown_55d_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_244_donchian_breakdown_55d_event},
    "f30_wtof_245_donchian_failed_breakout_20d_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_245_donchian_failed_breakout_20d_event},
    "f30_wtof_246_hma_band_upper_distance_atr_norm": {"inputs": ["high", "low", "close"], "func": f30_wtof_246_hma_band_upper_distance_atr_norm},
    "f30_wtof_247_close_above_hma_upper_band_indicator": {"inputs": ["high", "low", "close"], "func": f30_wtof_247_close_above_hma_upper_band_indicator},
    "f30_wtof_248_hma_distance_atr_norm": {"inputs": ["high", "low", "close"], "func": f30_wtof_248_hma_distance_atr_norm},
    "f30_wtof_249_hma_band_width_atr_units": {"inputs": ["high", "low", "close"], "func": f30_wtof_249_hma_band_width_atr_units},
    "f30_wtof_250_hma_slope_21d": {"inputs": ["high", "low", "close"], "func": f30_wtof_250_hma_slope_21d},
    "f30_wtof_251_stderr_bands_width_pct_of_mid": {"inputs": ["high", "low", "close"], "func": f30_wtof_251_stderr_bands_width_pct_of_mid},
    "f30_wtof_252_stderr_bands_position": {"inputs": ["high", "low", "close"], "func": f30_wtof_252_stderr_bands_position},
    "f30_wtof_253_stderr_bands_narrowing_indicator": {"inputs": ["high", "low", "close"], "func": f30_wtof_253_stderr_bands_narrowing_indicator},
    "f30_wtof_254_close_above_stderr_upper_indicator": {"inputs": ["high", "low", "close"], "func": f30_wtof_254_close_above_stderr_upper_indicator},
    "f30_wtof_255_stderr_mid_slope_21d": {"inputs": ["high", "low", "close"], "func": f30_wtof_255_stderr_mid_slope_21d},
    "f30_wtof_256_multi_band_above_upper_count": {"inputs": ["high", "low", "close"], "func": f30_wtof_256_multi_band_above_upper_count},
    "f30_wtof_257_multi_band_all_narrow_regime": {"inputs": ["high", "low", "close"], "func": f30_wtof_257_multi_band_all_narrow_regime},
    "f30_wtof_258_multi_band_breakout_event_count": {"inputs": ["high", "low", "close"], "func": f30_wtof_258_multi_band_breakout_event_count},
    "f30_wtof_259_multi_band_aligned_narrow_streak": {"inputs": ["high", "low", "close"], "func": f30_wtof_259_multi_band_aligned_narrow_streak},
    "f30_wtof_260_multi_band_squeeze_release_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_260_multi_band_squeeze_release_event},
    "f30_wtof_261_dpo_pit_21d": {"inputs": ["high", "low", "close"], "func": f30_wtof_261_dpo_pit_21d},
    "f30_wtof_262_dpo_pit_63d": {"inputs": ["high", "low", "close"], "func": f30_wtof_262_dpo_pit_63d},
    "f30_wtof_263_dpo_pit_126d": {"inputs": ["high", "low", "close"], "func": f30_wtof_263_dpo_pit_126d},
    "f30_wtof_264_dpo_pit_21d_sign": {"inputs": ["high", "low", "close"], "func": f30_wtof_264_dpo_pit_21d_sign},
    "f30_wtof_265_dpo_pit_21d_zscore_252d": {"inputs": ["high", "low", "close"], "func": f30_wtof_265_dpo_pit_21d_zscore_252d},
    "f30_wtof_266_schaff_trend_cycle": {"inputs": ["high", "low", "close"], "func": f30_wtof_266_schaff_trend_cycle},
    "f30_wtof_267_stc_above_75_overbought_indicator": {"inputs": ["high", "low", "close"], "func": f30_wtof_267_stc_above_75_overbought_indicator},
    "f30_wtof_268_stc_cross_below_75_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_268_stc_cross_below_75_event},
    "f30_wtof_269_stc_bars_since_last_overbought_exit": {"inputs": ["high", "low", "close"], "func": f30_wtof_269_stc_bars_since_last_overbought_exit},
    "f30_wtof_270_stc_peaks_count_252d": {"inputs": ["high", "low", "close"], "func": f30_wtof_270_stc_peaks_count_252d},
    "f30_wtof_271_stc_long_horizon_46_100": {"inputs": ["high", "low", "close"], "func": f30_wtof_271_stc_long_horizon_46_100},
    "f30_wtof_272_stc_wto_aligned_overbought": {"inputs": ["high", "low", "close"], "func": f30_wtof_272_stc_wto_aligned_overbought},
    "f30_wtof_273_stc_falling_from_above_90_indicator": {"inputs": ["high", "low", "close"], "func": f30_wtof_273_stc_falling_from_above_90_indicator},
    "f30_wtof_274_bb_width_10d_horizon": {"inputs": ["high", "low", "close"], "func": f30_wtof_274_bb_width_10d_horizon},
    "f30_wtof_275_bb_width_100d_horizon": {"inputs": ["high", "low", "close"], "func": f30_wtof_275_bb_width_100d_horizon},
    "f30_wtof_276_bb_width_200d_horizon": {"inputs": ["high", "low", "close"], "func": f30_wtof_276_bb_width_200d_horizon},
    "f30_wtof_277_bb_width_horizon_rank_mean": {"inputs": ["high", "low", "close"], "func": f30_wtof_277_bb_width_horizon_rank_mean},
    "f30_wtof_278_bb_position_at_200d": {"inputs": ["high", "low", "close"], "func": f30_wtof_278_bb_position_at_200d},
    "f30_wtof_279_bb_width_regime_low_fraction_252d": {"inputs": ["high", "low", "close"], "func": f30_wtof_279_bb_width_regime_low_fraction_252d},
    "f30_wtof_280_bb_width_regime_mid_fraction_252d": {"inputs": ["high", "low", "close"], "func": f30_wtof_280_bb_width_regime_mid_fraction_252d},
    "f30_wtof_281_bb_width_regime_high_fraction_252d": {"inputs": ["high", "low", "close"], "func": f30_wtof_281_bb_width_regime_high_fraction_252d},
    "f30_wtof_282_bb_width_50_vs_200_spread": {"inputs": ["high", "low", "close"], "func": f30_wtof_282_bb_width_50_vs_200_spread},
    "f30_wtof_283_squeeze_momentum_long_100d": {"inputs": ["high", "low", "close"], "func": f30_wtof_283_squeeze_momentum_long_100d},
    "f30_wtof_284_bb_walking_lower_band_count_21d": {"inputs": ["high", "low", "close"], "func": f30_wtof_284_bb_walking_lower_band_count_21d},
    "f30_wtof_285_bb_width_change_long_horizon_504d": {"inputs": ["high", "low", "close"], "func": f30_wtof_285_bb_width_change_long_horizon_504d},
    "f30_wtof_286_bars_since_ttm_fire": {"inputs": ["high", "low", "close"], "func": f30_wtof_286_bars_since_ttm_fire},
    "f30_wtof_287_bars_since_wto_ob_exit": {"inputs": ["high", "low", "close"], "func": f30_wtof_287_bars_since_wto_ob_exit},
    "f30_wtof_288_bars_since_wto_zero_cross_down": {"inputs": ["high", "low", "close"], "func": f30_wtof_288_bars_since_wto_zero_cross_down},
    "f30_wtof_289_bars_since_pct_b_walk_end": {"inputs": ["high", "low", "close"], "func": f30_wtof_289_bars_since_pct_b_walk_end},
    "f30_wtof_290_walk_upper_then_ttm_fire_within_5_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_290_walk_upper_then_ttm_fire_within_5_event},
    "f30_wtof_291_ttm_fire_then_21d_drawdown": {"inputs": ["high", "low", "close"], "func": f30_wtof_291_ttm_fire_then_21d_drawdown},
    "f30_wtof_292_multi_band_release_count_21d": {"inputs": ["high", "low", "close"], "func": f30_wtof_292_multi_band_release_count_21d},
    "f30_wtof_293_pct_b_streak_end_then_drawdown_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_293_pct_b_streak_end_then_drawdown_event},
    "f30_wtof_294_full_topping_complex_pro_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_294_full_topping_complex_pro_event},
    "f30_wtof_295_full_topping_density_63d": {"inputs": ["high", "low", "close"], "func": f30_wtof_295_full_topping_density_63d},
    "f30_wtof_296_short_squeeze_on_long_wto_overbought": {"inputs": ["high", "low", "close"], "func": f30_wtof_296_short_squeeze_on_long_wto_overbought},
    "f30_wtof_297_walk_upper_streak_end_then_wto_bear_within_5": {"inputs": ["high", "low", "close"], "func": f30_wtof_297_walk_upper_streak_end_then_wto_bear_within_5},
    "f30_wtof_298_pct_b_above_one_n_then_below_half_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_298_pct_b_above_one_n_then_below_half_event},
    "f30_wtof_299_squeeze_pro_high_compression_then_21d_drawdown": {"inputs": ["high", "low", "close"], "func": f30_wtof_299_squeeze_pro_high_compression_then_21d_drawdown},
    "f30_wtof_300_dpo_pos_then_wto_zero_cross_down_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_300_dpo_pos_then_wto_zero_cross_down_event},
}
