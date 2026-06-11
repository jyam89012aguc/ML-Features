"""wave_trend_oscillator_family base features 301-375 — Pipeline 1b-technical.

Third batch (atomic-leaning). Each function = one clean single-source signal
the ML can weight independently. Focus areas in this file:

  - Bollinger Band centerline (SMA20) atomic events (close-above / rejection /
    recapture) and band-slope decomposition (upper, lower, mid at 21d / 63d).
  - BB width regime extremes (252d max event, 50% drop from peak, 21d-mean
    ratio, ATR-units, log change, 5d change).
  - Walking-the-band streak extremes (252d max, first-after-inside, dwell at
    63d, lower-band walking dwell).
  - %b atomic events: 252d max/min/skew/mean/decile counts, cross events
    (1.0 from above, 0.5 from above, 0.5 from below), dwell below zero,
    multi-horizon at 10/50/100, 252d-max event, streak below zero.
  - Bandwidth (BB-width %) atomic events: 252d max/min event, 50pct drop,
    cross above 21d mean, dwell quartiles, IQR.
  - Donchian width/breakout extremes: 252d-min compression event at 20/55,
    252d-max expansion event, failed-breakout 20d/55d within 5, 126d
    position/breakout/breakdown, 55d breakout coincident with 252d new high.
  - Keltner-channel atomic events: width percentile, multi-horizon width
    (50, 100), close above KC upper at 252d new high, close below KC lower
    after uptrend, walking-upper count + current streak, KC position.
  - BB-KC overlap at long horizon (50d) + long-horizon release.
  - Crabel patterns (canonical NR4/NR7/WR4/WR7, 2-bar NR, ID/NR4 double
    compression) and event-at-252d-high variants for blowoff context.

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


def _donchian_upper(high, n):
    return high.rolling(n, min_periods=max(n // 3, 2)).max()


def _donchian_lower(low, n):
    return low.rolling(n, min_periods=max(n // 3, 2)).min()


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


def _consec_true_streak(b):
    """Right-anchored current consecutive True-streak length (0 where False)."""
    b = b.fillna(False).astype(bool)
    idx = np.arange(len(b), dtype=float)
    last_false = pd.Series(np.where(~b, idx, np.nan), index=b.index).ffill()
    streak = pd.Series(idx, index=b.index) - last_false
    streak = streak.where(b, 0.0)
    streak.iloc[0] = float(b.iloc[0]) if len(b) > 0 else np.nan
    return streak


# ============================================================
# Bucket A — BB centerline (SMA20) atomic events (301-303)
# ============================================================


def f30_wtof_301_bb_centerline_sma20_close_above_indicator_d1(close: pd.Series) -> pd.Series:
    """Indicator: close > BB centerline (SMA20). Atomic regime flag."""
    mid, _, _ = _bb(close, n=MDAYS, mult=2.0)
    return ((close > mid).astype(float).where(mid.notna(), np.nan)).diff()

def f30_wtof_302_bb_centerline_sma20_rejection_event_d1(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Event: open > SMA20 AND close < SMA20 — one-bar centerline rejection."""
    mid, _, _ = _bb(close, n=MDAYS, mult=2.0)
    cond = (open_ > mid) & (close < mid)
    return (cond.astype(float).where(mid.notna(), np.nan)).diff()

def f30_wtof_303_bb_centerline_sma20_recapture_event_d1(close: pd.Series) -> pd.Series:
    """Event: close crosses above SMA20 from below (single bar)."""
    mid, _, _ = _bb(close, n=MDAYS, mult=2.0)
    cond = (close > mid) & (close.shift(1) <= mid.shift(1))
    return (cond.astype(float).where(mid.notna(), np.nan)).diff()

def f30_wtof_304_bb_upper_band_slope_21d_d1(close: pd.Series) -> pd.Series:
    """Slope of BB upper band over trailing 21d (regression coefficient)."""
    _, bbu, _ = _bb(close, n=MDAYS, mult=2.0)
    return (_rolling_slope(bbu, MDAYS)).diff()

def f30_wtof_305_bb_lower_band_slope_21d_d1(close: pd.Series) -> pd.Series:
    """Slope of BB lower band over trailing 21d."""
    _, _, bbl = _bb(close, n=MDAYS, mult=2.0)
    return (_rolling_slope(bbl, MDAYS)).diff()

def f30_wtof_306_bb_centerline_slope_21d_d1(close: pd.Series) -> pd.Series:
    """Slope of BB centerline (SMA20) over trailing 21d."""
    mid, _, _ = _bb(close, n=MDAYS, mult=2.0)
    return (_rolling_slope(mid, MDAYS)).diff()

def f30_wtof_307_bb_upper_band_slope_63d_d1(close: pd.Series) -> pd.Series:
    """Slope of BB upper band over trailing 63d (intermediate horizon)."""
    _, bbu, _ = _bb(close, n=MDAYS, mult=2.0)
    return (_rolling_slope(bbu, QDAYS)).diff()

def f30_wtof_308_bb_centerline_slope_63d_d1(close: pd.Series) -> pd.Series:
    """Slope of BB centerline over trailing 63d."""
    mid, _, _ = _bb(close, n=MDAYS, mult=2.0)
    return (_rolling_slope(mid, QDAYS)).diff()

def f30_wtof_309_bb_width_252d_max_event_d1(close: pd.Series) -> pd.Series:
    """Event: BB-width(20,2) equals its 252d trailing max — volatility-peak bar."""
    bw = _bb_width_pct(close, n=MDAYS, mult=2.0)
    rmax = bw.rolling(YDAYS, min_periods=QDAYS).max()
    return ((bw >= rmax).astype(float).where(rmax.notna(), np.nan)).diff()

def f30_wtof_310_bb_width_drop_50pct_from_63d_max_event_d1(close: pd.Series) -> pd.Series:
    """Event: BB-width has dropped by 50% from its trailing 63d max — post-blowoff compression."""
    bw = _bb_width_pct(close, n=MDAYS, mult=2.0)
    rmax = bw.rolling(QDAYS, min_periods=MDAYS).max()
    ratio = _safe_div(bw, rmax)
    return ((ratio <= 0.5).astype(float).where(rmax.notna(), np.nan)).diff()

def f30_wtof_311_bb_width_21d_mean_ratio_d1(close: pd.Series) -> pd.Series:
    """Continuous: BB-width / trailing 21d mean BB-width. >1 = expanding."""
    bw = _bb_width_pct(close, n=MDAYS, mult=2.0)
    m = bw.rolling(MDAYS, min_periods=WDAYS).mean()
    return (_safe_div(bw, m)).diff()

def f30_wtof_312_bb_width_normalized_atr_units_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """BB-band-width in ATR(21) units — vol-normalized expression of band thickness."""
    _, bbu, bbl = _bb(close, n=MDAYS, mult=2.0)
    a = _atr(high, low, close, n=MDAYS)
    return (_safe_div(bbu - bbl, a)).diff()

def f30_wtof_313_bb_width_log_252d_change_d1(close: pd.Series) -> pd.Series:
    """Log change of BB-width vs value 252d ago."""
    bw = _bb_width_pct(close, n=MDAYS, mult=2.0)
    return (_safe_log(bw) - _safe_log(bw.shift(YDAYS))).diff()

def f30_wtof_314_bb_width_5d_change_pct_d1(close: pd.Series) -> pd.Series:
    """5d percent change in BB-width — short-term expansion/contraction rate."""
    bw = _bb_width_pct(close, n=MDAYS, mult=2.0)
    return (_safe_div(bw, bw.shift(WDAYS)) - 1.0).diff()

def f30_wtof_315_bb_walking_upper_streak_252d_max_d1(close: pd.Series) -> pd.Series:
    """Max consecutive walking-upper (close>BB-upper) streak length over trailing 252d."""
    _, bbu, _ = _bb(close, n=MDAYS, mult=2.0)
    b = close > bbu
    streak = _consec_true_streak(b)
    return (streak.rolling(YDAYS, min_periods=QDAYS).max()).diff()

def f30_wtof_316_bb_walking_upper_first_bar_after_inside_event_d1(close: pd.Series) -> pd.Series:
    """Event: first bar with close>BB-upper after 21+ consecutive bars inside the bands."""
    _, bbu, _ = _bb(close, n=MDAYS, mult=2.0)
    above = close > bbu
    inside = ~above
    inside_streak = _consec_true_streak(inside)
    cond = above & (inside_streak.shift(1) >= MDAYS)
    return (cond.astype(float).where(bbu.notna(), np.nan)).diff()

def f30_wtof_317_bb_walking_upper_dwell_63d_count_d1(close: pd.Series) -> pd.Series:
    """Count of walking-upper bars (close>BB-upper) in trailing 63d."""
    _, bbu, _ = _bb(close, n=MDAYS, mult=2.0)
    b = (close > bbu).astype(float).where(bbu.notna(), np.nan)
    return (b.rolling(QDAYS, min_periods=MDAYS).sum()).diff()

def f30_wtof_318_bb_walking_lower_dwell_63d_count_d1(close: pd.Series) -> pd.Series:
    """Count of walking-lower bars (close<BB-lower) in trailing 63d."""
    _, _, bbl = _bb(close, n=MDAYS, mult=2.0)
    b = (close < bbl).astype(float).where(bbl.notna(), np.nan)
    return (b.rolling(QDAYS, min_periods=MDAYS).sum()).diff()

def f30_wtof_319_bb_walking_lower_streak_current_d1(close: pd.Series) -> pd.Series:
    """Current consecutive walking-lower streak length."""
    _, _, bbl = _bb(close, n=MDAYS, mult=2.0)
    b = close < bbl
    return (_consec_true_streak(b)).diff()

def f30_wtof_320_pct_b_252d_max_d1(close: pd.Series) -> pd.Series:
    """Trailing 252d max of %b — extreme penetration of upper band over a year."""
    pb = _pct_b(close, n=MDAYS, mult=2.0)
    return (pb.rolling(YDAYS, min_periods=QDAYS).max()).diff()

def f30_wtof_321_pct_b_252d_min_d1(close: pd.Series) -> pd.Series:
    """Trailing 252d min of %b — extreme penetration of lower band over a year."""
    pb = _pct_b(close, n=MDAYS, mult=2.0)
    return (pb.rolling(YDAYS, min_periods=QDAYS).min()).diff()

def f30_wtof_322_pct_b_skew_63d_d1(close: pd.Series) -> pd.Series:
    """Skewness of %b in trailing 63d — asymmetry of band penetrations."""
    pb = _pct_b(close, n=MDAYS, mult=2.0)
    return (pb.rolling(QDAYS, min_periods=MDAYS).skew()).diff()

def f30_wtof_323_pct_b_mean_21d_d1(close: pd.Series) -> pd.Series:
    """Mean of %b in trailing 21d — short-term band position."""
    pb = _pct_b(close, n=MDAYS, mult=2.0)
    return (pb.rolling(MDAYS, min_periods=WDAYS).mean()).diff()

def f30_wtof_324_pct_b_top_decile_count_63d_d1(close: pd.Series) -> pd.Series:
    """Count of bars with %b > 0.9 in trailing 63d — top-decile dwell."""
    pb = _pct_b(close, n=MDAYS, mult=2.0)
    b = (pb > 0.9).astype(float).where(pb.notna(), np.nan)
    return (b.rolling(QDAYS, min_periods=MDAYS).sum()).diff()

def f30_wtof_325_pct_b_bottom_decile_count_63d_d1(close: pd.Series) -> pd.Series:
    """Count of bars with %b < 0.1 in trailing 63d — bottom-decile dwell."""
    pb = _pct_b(close, n=MDAYS, mult=2.0)
    b = (pb < 0.1).astype(float).where(pb.notna(), np.nan)
    return (b.rolling(QDAYS, min_periods=MDAYS).sum()).diff()

def f30_wtof_326_pct_b_cross_below_half_from_above_event_d1(close: pd.Series) -> pd.Series:
    """Event: %b crosses below 0.5 from above — mid-band loss-of-momentum."""
    pb = _pct_b(close, n=MDAYS, mult=2.0)
    cond = (pb < 0.5) & (pb.shift(1) >= 0.5)
    return (cond.astype(float).where(pb.notna(), np.nan)).diff()

def f30_wtof_327_pct_b_cross_below_one_from_above_event_d1(close: pd.Series) -> pd.Series:
    """Event: %b crosses below 1.0 from above — return-to-band after upper-pierce."""
    pb = _pct_b(close, n=MDAYS, mult=2.0)
    cond = (pb < 1.0) & (pb.shift(1) >= 1.0)
    return (cond.astype(float).where(pb.notna(), np.nan)).diff()

def f30_wtof_328_pct_b_cross_above_half_from_below_event_d1(close: pd.Series) -> pd.Series:
    """Event: %b crosses above 0.5 from below — mid-band recapture."""
    pb = _pct_b(close, n=MDAYS, mult=2.0)
    cond = (pb > 0.5) & (pb.shift(1) <= 0.5)
    return (cond.astype(float).where(pb.notna(), np.nan)).diff()

def f30_wtof_329_pct_b_dwell_below_zero_5d_d1(close: pd.Series) -> pd.Series:
    """Count of bars with %b < 0 (close below lower band) in trailing 5d."""
    pb = _pct_b(close, n=MDAYS, mult=2.0)
    b = (pb < 0.0).astype(float).where(pb.notna(), np.nan)
    return (b.rolling(WDAYS, min_periods=2).sum()).diff()

def f30_wtof_330_pct_b_above_one_then_below_half_within_3_event_d1(close: pd.Series) -> pd.Series:
    """Event: %b>1 within trailing 3 bars AND %b<0.5 today — head-fake collapse fingerprint."""
    pb = _pct_b(close, n=MDAYS, mult=2.0)
    recent = (pb.shift(1) > 1.0).rolling(3, min_periods=1).max().astype(bool)
    cond = recent & (pb < 0.5)
    return (cond.astype(float).where(pb.notna(), np.nan)).diff()

def f30_wtof_331_pct_b_extreme_high_then_inside_within_5_event_d1(close: pd.Series) -> pd.Series:
    """Event: %b>1.05 within trailing 5 bars AND %b<=1 today — first re-entry to bands."""
    pb = _pct_b(close, n=MDAYS, mult=2.0)
    recent = (pb.shift(1) > 1.05).rolling(WDAYS, min_periods=1).max().astype(bool)
    cond = recent & (pb <= 1.0) & (pb.shift(1) > 1.0)
    return (cond.astype(float).where(pb.notna(), np.nan)).diff()

def f30_wtof_332_pct_b_first_bar_inside_after_walk_event_d1(close: pd.Series) -> pd.Series:
    """Event: first bar with %b<=1 after a streak of 3+ bars with %b>1 — walk-end."""
    pb = _pct_b(close, n=MDAYS, mult=2.0)
    above = pb > 1.0
    above_streak = _consec_true_streak(above)
    cond = (pb <= 1.0) & (above_streak.shift(1) >= 3)
    return (cond.astype(float).where(pb.notna(), np.nan)).diff()

def f30_wtof_333_pct_b_micro_horizon_10d_d1(close: pd.Series) -> pd.Series:
    """%b computed at horizon 10 (micro). Distinct hypothesis: short-vol band position."""
    pb = _pct_b(close, n=10, mult=2.0)
    return (pb).diff()

def f30_wtof_334_pct_b_long_horizon_50d_d1(close: pd.Series) -> pd.Series:
    """%b computed at horizon 50 — intermediate-vol band position."""
    pb = _pct_b(close, n=50, mult=2.0)
    return (pb).diff()

def f30_wtof_335_pct_b_long_horizon_100d_d1(close: pd.Series) -> pd.Series:
    """%b computed at horizon 100 — secular-vol band position."""
    pb = _pct_b(close, n=100, mult=2.0)
    return (pb).diff()

def f30_wtof_336_pct_b_at_252d_max_event_d1(close: pd.Series) -> pd.Series:
    """Event: %b equals its 252d trailing max — extreme upper-band stretch."""
    pb = _pct_b(close, n=MDAYS, mult=2.0)
    rmax = pb.rolling(YDAYS, min_periods=QDAYS).max()
    return ((pb >= rmax).astype(float).where(rmax.notna(), np.nan)).diff()

def f30_wtof_337_pct_b_streak_below_zero_max_252d_d1(close: pd.Series) -> pd.Series:
    """Max consecutive %b<0 streak in trailing 252d — capitulation regime memory."""
    pb = _pct_b(close, n=MDAYS, mult=2.0)
    b = pb < 0.0
    streak = _consec_true_streak(b)
    return (streak.rolling(YDAYS, min_periods=QDAYS).max()).diff()

def f30_wtof_338_bandwidth_at_252d_max_event_d1(close: pd.Series) -> pd.Series:
    """Event: BB-bandwidth equals its 252d trailing max (volatility-peak bar)."""
    bw = _bb_width_pct(close, n=MDAYS, mult=2.0)
    rmax = bw.rolling(YDAYS, min_periods=QDAYS).max()
    return ((bw >= rmax).astype(float).where(rmax.notna(), np.nan)).diff()

def f30_wtof_339_bandwidth_252d_max_d1(close: pd.Series) -> pd.Series:
    """Trailing 252d max of BB-bandwidth — peak-volatility level reference."""
    bw = _bb_width_pct(close, n=MDAYS, mult=2.0)
    return (bw.rolling(YDAYS, min_periods=QDAYS).max()).diff()

def f30_wtof_340_bandwidth_252d_min_d1(close: pd.Series) -> pd.Series:
    """Trailing 252d min of BB-bandwidth — compression-floor reference."""
    bw = _bb_width_pct(close, n=MDAYS, mult=2.0)
    return (bw.rolling(YDAYS, min_periods=QDAYS).min()).diff()

def f30_wtof_341_bandwidth_dropped_50pct_from_252d_max_event_d1(close: pd.Series) -> pd.Series:
    """Event: bandwidth has dropped to <=50% of its 252d max."""
    bw = _bb_width_pct(close, n=MDAYS, mult=2.0)
    rmax = bw.rolling(YDAYS, min_periods=QDAYS).max()
    ratio = _safe_div(bw, rmax)
    return ((ratio <= 0.5).astype(float).where(rmax.notna(), np.nan)).diff()

def f30_wtof_342_bandwidth_cross_above_21d_mean_event_d1(close: pd.Series) -> pd.Series:
    """Event: bandwidth crosses above its 21d mean from below — vol-expansion trigger."""
    bw = _bb_width_pct(close, n=MDAYS, mult=2.0)
    m = bw.rolling(MDAYS, min_periods=WDAYS).mean()
    cond = (bw > m) & (bw.shift(1) <= m.shift(1))
    return (cond.astype(float).where(m.notna(), np.nan)).diff()

def f30_wtof_343_bandwidth_above_75pct_dwell_63d_d1(close: pd.Series) -> pd.Series:
    """Count of bars with bandwidth percentile >0.75 in trailing 63d (high-vol dwell)."""
    bw = _bb_width_pct(close, n=MDAYS, mult=2.0)
    rank = bw.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    b = (rank > 0.75).astype(float).where(rank.notna(), np.nan)
    return (b.rolling(QDAYS, min_periods=MDAYS).sum()).diff()

def f30_wtof_344_bandwidth_below_25pct_dwell_63d_d1(close: pd.Series) -> pd.Series:
    """Count of bars with bandwidth percentile <0.25 in trailing 63d (compression dwell)."""
    bw = _bb_width_pct(close, n=MDAYS, mult=2.0)
    rank = bw.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    b = (rank < 0.25).astype(float).where(rank.notna(), np.nan)
    return (b.rolling(QDAYS, min_periods=MDAYS).sum()).diff()

def f30_wtof_345_bandwidth_iqr_252d_d1(close: pd.Series) -> pd.Series:
    """Interquartile range of bandwidth in trailing 252d (vol-regime dispersion)."""
    bw = _bb_width_pct(close, n=MDAYS, mult=2.0)
    q75 = bw.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    q25 = bw.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    return (q75 - q25).diff()

def f30_wtof_346_donchian_width_20d_252d_min_event_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Event: 20d Donchian channel width equals its 252d trailing min — extreme compression."""
    u = _donchian_upper(high, 20)
    l = _donchian_lower(low, 20)
    w = u - l
    rmin = w.rolling(YDAYS, min_periods=QDAYS).min()
    return ((w <= rmin).astype(float).where(rmin.notna(), np.nan)).diff()

def f30_wtof_347_donchian_width_55d_252d_min_event_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Event: 55d Donchian channel width equals its 252d trailing min (long compression)."""
    u = _donchian_upper(high, 55)
    l = _donchian_lower(low, 55)
    w = u - l
    rmin = w.rolling(YDAYS, min_periods=QDAYS).min()
    return ((w <= rmin).astype(float).where(rmin.notna(), np.nan)).diff()

def f30_wtof_348_donchian_width_20d_252d_max_event_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Event: 20d Donchian channel width equals its 252d trailing max — expansion extreme."""
    u = _donchian_upper(high, 20)
    l = _donchian_lower(low, 20)
    w = u - l
    rmax = w.rolling(YDAYS, min_periods=QDAYS).max()
    return ((w >= rmax).astype(float).where(rmax.notna(), np.nan)).diff()

def f30_wtof_349_donchian_width_55d_252d_max_event_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Event: 55d Donchian channel width at its 252d trailing max."""
    u = _donchian_upper(high, 55)
    l = _donchian_lower(low, 55)
    w = u - l
    rmax = w.rolling(YDAYS, min_periods=QDAYS).max()
    return ((w >= rmax).astype(float).where(rmax.notna(), np.nan)).diff()

def f30_wtof_350_donchian_breakout_20d_failed_within_5_event_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: 20d Donchian breakout (close > 20d Donchian upper-shift1) occurred within 5 bars AND close back below 20d upper today — failed Turtle entry."""
    u_prev = _donchian_upper(high, 20).shift(1)
    bo = close > u_prev
    bo_recent = bo.shift(1).fillna(False).astype(bool).rolling(WDAYS, min_periods=1).max().astype(bool)
    cond = bo_recent & (close <= u_prev)
    return (cond.astype(float).where(u_prev.notna(), np.nan)).diff()

def f30_wtof_351_donchian_breakout_55d_failed_within_5_event_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: 55d Turtle breakout occurred within trailing 5 bars AND close back below 55d upper today."""
    u_prev = _donchian_upper(high, 55).shift(1)
    bo = close > u_prev
    bo_recent = bo.shift(1).fillna(False).astype(bool).rolling(WDAYS, min_periods=1).max().astype(bool)
    cond = bo_recent & (close <= u_prev)
    return (cond.astype(float).where(u_prev.notna(), np.nan)).diff()

def f30_wtof_352_donchian_position_126d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Position of close within 126d Donchian channel: (close-L)/(U-L), 0..1."""
    u = _donchian_upper(high, 126)
    l = _donchian_lower(low, 126)
    return (_safe_div(close - l, u - l)).diff()

def f30_wtof_353_donchian_breakout_126d_event_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """Event: close > 126d Donchian upper (yesterday's value) — semi-annual breakout."""
    u_prev = _donchian_upper(high, 126).shift(1)
    return ((close > u_prev).astype(float).where(u_prev.notna(), np.nan)).diff()

def f30_wtof_354_donchian_breakdown_126d_event_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: close < 126d Donchian lower (yesterday's value) — semi-annual breakdown."""
    l_prev = _donchian_lower(low, 126).shift(1)
    return ((close < l_prev).astype(float).where(l_prev.notna(), np.nan)).diff()

def f30_wtof_355_donchian_breakout_55d_at_252d_new_high_event_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """Event: 55d Donchian breakout AND close prints a 252d-new-high — Turtle long at multi-year regime change."""
    u55 = _donchian_upper(high, 55).shift(1)
    bo55 = close > u55
    h252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    cond = bo55 & (high >= h252)
    return (cond.astype(float).where(u55.notna() & h252.notna(), np.nan)).diff()

def f30_wtof_356_kc_width_percentile_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of KC width over trailing 252d."""
    _, kcu, kcl = _kc(high, low, close, n=MDAYS, mult=1.5)
    w = kcu - kcl
    return (w.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)).diff()

def f30_wtof_357_kc_width_50d_horizon_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """KC width at horizon 50 — intermediate vol scale (different from canonical 20)."""
    _, kcu, kcl = _kc(high, low, close, n=50, mult=1.5)
    mid, _, _ = _kc(high, low, close, n=50, mult=1.5)
    return (_safe_div(kcu - kcl, mid)).diff()

def f30_wtof_358_kc_width_100d_horizon_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """KC width at horizon 100 — long-vol scale."""
    mid, kcu, kcl = _kc(high, low, close, n=100, mult=1.5)
    return (_safe_div(kcu - kcl, mid)).diff()

def f30_wtof_359_kc_close_above_upper_at_252d_high_event_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: close > KC upper AND high prints a 252d-new-high — confirmed extension."""
    _, kcu, _ = _kc(high, low, close, n=MDAYS, mult=1.5)
    h252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    cond = (close > kcu) & (high >= h252)
    return (cond.astype(float).where(kcu.notna() & h252.notna(), np.nan)).diff()

def f30_wtof_360_kc_close_below_lower_after_uptrend_event_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: close < KC lower today AND SMA21 was rising over prior 21d — trend-break."""
    _, _, kcl = _kc(high, low, close, n=MDAYS, mult=1.5)
    sma = close.rolling(MDAYS, min_periods=WDAYS).mean()
    rising = sma > sma.shift(MDAYS)
    cond = (close < kcl) & rising
    return (cond.astype(float).where(kcl.notna() & sma.notna(), np.nan)).diff()

def f30_wtof_361_kc_walking_upper_count_21d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars with close > KC upper in trailing 21d."""
    _, kcu, _ = _kc(high, low, close, n=MDAYS, mult=1.5)
    b = (close > kcu).astype(float).where(kcu.notna(), np.nan)
    return (b.rolling(MDAYS, min_periods=WDAYS).sum()).diff()

def f30_wtof_362_kc_walking_upper_current_streak_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current consecutive streak of close > KC upper bars."""
    _, kcu, _ = _kc(high, low, close, n=MDAYS, mult=1.5)
    return (_consec_true_streak(close > kcu)).diff()

def f30_wtof_363_kc_position_in_bands_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Position of close within KC channel: (close-KCL)/(KCU-KCL)."""
    _, kcu, kcl = _kc(high, low, close, n=MDAYS, mult=1.5)
    return (_safe_div(close - kcl, kcu - kcl)).diff()

def f30_wtof_364_bb_kc_overlap_horizon_50_indicator_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: BB(50,2) entirely inside KC(50,1.5) — long-horizon squeeze regime."""
    on = _ttm_squeeze_on(high, low, close, n=50, mult_bb=2.0, mult_kc=1.5)
    return (on).diff()

def f30_wtof_365_bb_kc_overlap_horizon_50_release_event_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: long-horizon (n=50) TTM-squeeze fired today (was on, now off)."""
    on = _ttm_squeeze_on(high, low, close, n=50, mult_bb=2.0, mult_kc=1.5)
    fired = (on.shift(1) == 1) & (on == 0)
    return (fired.astype(float).where(on.notna(), np.nan)).diff()

def f30_wtof_366_nr4_indicator_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Crabel NR4: today's range is the narrowest of the last 4 trading days."""
    rng = high - low
    rmin = rng.rolling(4, min_periods=4).min()
    return ((rng <= rmin).astype(float).where(rmin.notna(), np.nan)).diff()

def f30_wtof_367_nr7_indicator_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Crabel NR7: today's range is the narrowest of the last 7 trading days."""
    rng = high - low
    rmin = rng.rolling(7, min_periods=7).min()
    return ((rng <= rmin).astype(float).where(rmin.notna(), np.nan)).diff()

def f30_wtof_368_wr4_indicator_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """WR4: today's range is the widest of the last 4 trading days — vol-expansion bar."""
    rng = high - low
    rmax = rng.rolling(4, min_periods=4).max()
    return ((rng >= rmax).astype(float).where(rmax.notna(), np.nan)).diff()

def f30_wtof_369_wr7_indicator_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """WR7: today's range is the widest of the last 7 trading days."""
    rng = high - low
    rmax = rng.rolling(7, min_periods=7).max()
    return ((rng >= rmax).astype(float).where(rmax.notna(), np.nan)).diff()

def f30_wtof_370_two_bar_nr_consecutive_event_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Event: today AND yesterday are both NR4 — second consecutive narrow day (rare double compression)."""
    rng = high - low
    rmin = rng.rolling(4, min_periods=4).min()
    is_nr4 = (rng <= rmin)
    cond = is_nr4 & is_nr4.shift(1).fillna(False).astype(bool)
    return (cond.astype(float).where(rmin.notna(), np.nan)).diff()

def f30_wtof_371_nr7_at_252d_high_event_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Event: NR7 (narrowest of 7) AND high prints a 252d trailing max — compression at peak."""
    rng = high - low
    rmin = rng.rolling(7, min_periods=7).min()
    is_nr7 = (rng <= rmin)
    h252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    cond = is_nr7 & (high >= h252)
    return (cond.astype(float).where(rmin.notna() & h252.notna(), np.nan)).diff()

def f30_wtof_372_nr4_at_252d_high_event_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Event: NR4 AND high prints a 252d trailing max."""
    rng = high - low
    rmin = rng.rolling(4, min_periods=4).min()
    is_nr4 = (rng <= rmin)
    h252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    cond = is_nr4 & (high >= h252)
    return (cond.astype(float).where(rmin.notna() & h252.notna(), np.nan)).diff()

def f30_wtof_373_inside_day_at_252d_high_event_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Event: inside day (high<prior-high, low>prior-low) AND prior high is the 252d trailing max — compression at peak."""
    inside = (high < high.shift(1)) & (low > low.shift(1))
    h252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = (high.shift(1) >= h252.shift(1))
    cond = inside & at_peak
    return (cond.astype(float).where(h252.notna(), np.nan)).diff()

def f30_wtof_374_outside_day_at_252d_high_event_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Event: outside day (high>prior-high, low<prior-low) AND high prints a 252d trailing max — climactic envelope bar."""
    outside = (high > high.shift(1)) & (low < low.shift(1))
    h252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    cond = outside & (high >= h252)
    return (cond.astype(float).where(h252.notna(), np.nan)).diff()

def f30_wtof_375_id_nr4_double_compression_event_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Event: today is both an inside day AND NR4 — Crabel's ID/NR4 double-compression setup."""
    inside = (high < high.shift(1)) & (low > low.shift(1))
    rng = high - low
    rmin = rng.rolling(4, min_periods=4).min()
    is_nr4 = (rng <= rmin)
    cond = inside & is_nr4
    return (cond.astype(float).where(rmin.notna(), np.nan)).diff()


# ============================================================
#                         REGISTRY 301_375  (D1)
# ============================================================

WAVE_TREND_OSCILLATOR_FAMILY_D1_REGISTRY_301_375 = {
    "f30_wtof_301_bb_centerline_sma20_close_above_indicator_d1": {"inputs": ["close"], "func": f30_wtof_301_bb_centerline_sma20_close_above_indicator_d1},
    "f30_wtof_302_bb_centerline_sma20_rejection_event_d1": {"inputs": ["open", "close"], "func": f30_wtof_302_bb_centerline_sma20_rejection_event_d1},
    "f30_wtof_303_bb_centerline_sma20_recapture_event_d1": {"inputs": ["close"], "func": f30_wtof_303_bb_centerline_sma20_recapture_event_d1},
    "f30_wtof_304_bb_upper_band_slope_21d_d1": {"inputs": ["close"], "func": f30_wtof_304_bb_upper_band_slope_21d_d1},
    "f30_wtof_305_bb_lower_band_slope_21d_d1": {"inputs": ["close"], "func": f30_wtof_305_bb_lower_band_slope_21d_d1},
    "f30_wtof_306_bb_centerline_slope_21d_d1": {"inputs": ["close"], "func": f30_wtof_306_bb_centerline_slope_21d_d1},
    "f30_wtof_307_bb_upper_band_slope_63d_d1": {"inputs": ["close"], "func": f30_wtof_307_bb_upper_band_slope_63d_d1},
    "f30_wtof_308_bb_centerline_slope_63d_d1": {"inputs": ["close"], "func": f30_wtof_308_bb_centerline_slope_63d_d1},
    "f30_wtof_309_bb_width_252d_max_event_d1": {"inputs": ["close"], "func": f30_wtof_309_bb_width_252d_max_event_d1},
    "f30_wtof_310_bb_width_drop_50pct_from_63d_max_event_d1": {"inputs": ["close"], "func": f30_wtof_310_bb_width_drop_50pct_from_63d_max_event_d1},
    "f30_wtof_311_bb_width_21d_mean_ratio_d1": {"inputs": ["close"], "func": f30_wtof_311_bb_width_21d_mean_ratio_d1},
    "f30_wtof_312_bb_width_normalized_atr_units_d1": {"inputs": ["high", "low", "close"], "func": f30_wtof_312_bb_width_normalized_atr_units_d1},
    "f30_wtof_313_bb_width_log_252d_change_d1": {"inputs": ["close"], "func": f30_wtof_313_bb_width_log_252d_change_d1},
    "f30_wtof_314_bb_width_5d_change_pct_d1": {"inputs": ["close"], "func": f30_wtof_314_bb_width_5d_change_pct_d1},
    "f30_wtof_315_bb_walking_upper_streak_252d_max_d1": {"inputs": ["close"], "func": f30_wtof_315_bb_walking_upper_streak_252d_max_d1},
    "f30_wtof_316_bb_walking_upper_first_bar_after_inside_event_d1": {"inputs": ["close"], "func": f30_wtof_316_bb_walking_upper_first_bar_after_inside_event_d1},
    "f30_wtof_317_bb_walking_upper_dwell_63d_count_d1": {"inputs": ["close"], "func": f30_wtof_317_bb_walking_upper_dwell_63d_count_d1},
    "f30_wtof_318_bb_walking_lower_dwell_63d_count_d1": {"inputs": ["close"], "func": f30_wtof_318_bb_walking_lower_dwell_63d_count_d1},
    "f30_wtof_319_bb_walking_lower_streak_current_d1": {"inputs": ["close"], "func": f30_wtof_319_bb_walking_lower_streak_current_d1},
    "f30_wtof_320_pct_b_252d_max_d1": {"inputs": ["close"], "func": f30_wtof_320_pct_b_252d_max_d1},
    "f30_wtof_321_pct_b_252d_min_d1": {"inputs": ["close"], "func": f30_wtof_321_pct_b_252d_min_d1},
    "f30_wtof_322_pct_b_skew_63d_d1": {"inputs": ["close"], "func": f30_wtof_322_pct_b_skew_63d_d1},
    "f30_wtof_323_pct_b_mean_21d_d1": {"inputs": ["close"], "func": f30_wtof_323_pct_b_mean_21d_d1},
    "f30_wtof_324_pct_b_top_decile_count_63d_d1": {"inputs": ["close"], "func": f30_wtof_324_pct_b_top_decile_count_63d_d1},
    "f30_wtof_325_pct_b_bottom_decile_count_63d_d1": {"inputs": ["close"], "func": f30_wtof_325_pct_b_bottom_decile_count_63d_d1},
    "f30_wtof_326_pct_b_cross_below_half_from_above_event_d1": {"inputs": ["close"], "func": f30_wtof_326_pct_b_cross_below_half_from_above_event_d1},
    "f30_wtof_327_pct_b_cross_below_one_from_above_event_d1": {"inputs": ["close"], "func": f30_wtof_327_pct_b_cross_below_one_from_above_event_d1},
    "f30_wtof_328_pct_b_cross_above_half_from_below_event_d1": {"inputs": ["close"], "func": f30_wtof_328_pct_b_cross_above_half_from_below_event_d1},
    "f30_wtof_329_pct_b_dwell_below_zero_5d_d1": {"inputs": ["close"], "func": f30_wtof_329_pct_b_dwell_below_zero_5d_d1},
    "f30_wtof_330_pct_b_above_one_then_below_half_within_3_event_d1": {"inputs": ["close"], "func": f30_wtof_330_pct_b_above_one_then_below_half_within_3_event_d1},
    "f30_wtof_331_pct_b_extreme_high_then_inside_within_5_event_d1": {"inputs": ["close"], "func": f30_wtof_331_pct_b_extreme_high_then_inside_within_5_event_d1},
    "f30_wtof_332_pct_b_first_bar_inside_after_walk_event_d1": {"inputs": ["close"], "func": f30_wtof_332_pct_b_first_bar_inside_after_walk_event_d1},
    "f30_wtof_333_pct_b_micro_horizon_10d_d1": {"inputs": ["close"], "func": f30_wtof_333_pct_b_micro_horizon_10d_d1},
    "f30_wtof_334_pct_b_long_horizon_50d_d1": {"inputs": ["close"], "func": f30_wtof_334_pct_b_long_horizon_50d_d1},
    "f30_wtof_335_pct_b_long_horizon_100d_d1": {"inputs": ["close"], "func": f30_wtof_335_pct_b_long_horizon_100d_d1},
    "f30_wtof_336_pct_b_at_252d_max_event_d1": {"inputs": ["close"], "func": f30_wtof_336_pct_b_at_252d_max_event_d1},
    "f30_wtof_337_pct_b_streak_below_zero_max_252d_d1": {"inputs": ["close"], "func": f30_wtof_337_pct_b_streak_below_zero_max_252d_d1},
    "f30_wtof_338_bandwidth_at_252d_max_event_d1": {"inputs": ["close"], "func": f30_wtof_338_bandwidth_at_252d_max_event_d1},
    "f30_wtof_339_bandwidth_252d_max_d1": {"inputs": ["close"], "func": f30_wtof_339_bandwidth_252d_max_d1},
    "f30_wtof_340_bandwidth_252d_min_d1": {"inputs": ["close"], "func": f30_wtof_340_bandwidth_252d_min_d1},
    "f30_wtof_341_bandwidth_dropped_50pct_from_252d_max_event_d1": {"inputs": ["close"], "func": f30_wtof_341_bandwidth_dropped_50pct_from_252d_max_event_d1},
    "f30_wtof_342_bandwidth_cross_above_21d_mean_event_d1": {"inputs": ["close"], "func": f30_wtof_342_bandwidth_cross_above_21d_mean_event_d1},
    "f30_wtof_343_bandwidth_above_75pct_dwell_63d_d1": {"inputs": ["close"], "func": f30_wtof_343_bandwidth_above_75pct_dwell_63d_d1},
    "f30_wtof_344_bandwidth_below_25pct_dwell_63d_d1": {"inputs": ["close"], "func": f30_wtof_344_bandwidth_below_25pct_dwell_63d_d1},
    "f30_wtof_345_bandwidth_iqr_252d_d1": {"inputs": ["close"], "func": f30_wtof_345_bandwidth_iqr_252d_d1},
    "f30_wtof_346_donchian_width_20d_252d_min_event_d1": {"inputs": ["high", "low"], "func": f30_wtof_346_donchian_width_20d_252d_min_event_d1},
    "f30_wtof_347_donchian_width_55d_252d_min_event_d1": {"inputs": ["high", "low"], "func": f30_wtof_347_donchian_width_55d_252d_min_event_d1},
    "f30_wtof_348_donchian_width_20d_252d_max_event_d1": {"inputs": ["high", "low"], "func": f30_wtof_348_donchian_width_20d_252d_max_event_d1},
    "f30_wtof_349_donchian_width_55d_252d_max_event_d1": {"inputs": ["high", "low"], "func": f30_wtof_349_donchian_width_55d_252d_max_event_d1},
    "f30_wtof_350_donchian_breakout_20d_failed_within_5_event_d1": {"inputs": ["high", "low", "close"], "func": f30_wtof_350_donchian_breakout_20d_failed_within_5_event_d1},
    "f30_wtof_351_donchian_breakout_55d_failed_within_5_event_d1": {"inputs": ["high", "low", "close"], "func": f30_wtof_351_donchian_breakout_55d_failed_within_5_event_d1},
    "f30_wtof_352_donchian_position_126d_d1": {"inputs": ["high", "low", "close"], "func": f30_wtof_352_donchian_position_126d_d1},
    "f30_wtof_353_donchian_breakout_126d_event_d1": {"inputs": ["high", "close"], "func": f30_wtof_353_donchian_breakout_126d_event_d1},
    "f30_wtof_354_donchian_breakdown_126d_event_d1": {"inputs": ["low", "close"], "func": f30_wtof_354_donchian_breakdown_126d_event_d1},
    "f30_wtof_355_donchian_breakout_55d_at_252d_new_high_event_d1": {"inputs": ["high", "close"], "func": f30_wtof_355_donchian_breakout_55d_at_252d_new_high_event_d1},
    "f30_wtof_356_kc_width_percentile_252d_d1": {"inputs": ["high", "low", "close"], "func": f30_wtof_356_kc_width_percentile_252d_d1},
    "f30_wtof_357_kc_width_50d_horizon_d1": {"inputs": ["high", "low", "close"], "func": f30_wtof_357_kc_width_50d_horizon_d1},
    "f30_wtof_358_kc_width_100d_horizon_d1": {"inputs": ["high", "low", "close"], "func": f30_wtof_358_kc_width_100d_horizon_d1},
    "f30_wtof_359_kc_close_above_upper_at_252d_high_event_d1": {"inputs": ["high", "low", "close"], "func": f30_wtof_359_kc_close_above_upper_at_252d_high_event_d1},
    "f30_wtof_360_kc_close_below_lower_after_uptrend_event_d1": {"inputs": ["high", "low", "close"], "func": f30_wtof_360_kc_close_below_lower_after_uptrend_event_d1},
    "f30_wtof_361_kc_walking_upper_count_21d_d1": {"inputs": ["high", "low", "close"], "func": f30_wtof_361_kc_walking_upper_count_21d_d1},
    "f30_wtof_362_kc_walking_upper_current_streak_d1": {"inputs": ["high", "low", "close"], "func": f30_wtof_362_kc_walking_upper_current_streak_d1},
    "f30_wtof_363_kc_position_in_bands_d1": {"inputs": ["high", "low", "close"], "func": f30_wtof_363_kc_position_in_bands_d1},
    "f30_wtof_364_bb_kc_overlap_horizon_50_indicator_d1": {"inputs": ["high", "low", "close"], "func": f30_wtof_364_bb_kc_overlap_horizon_50_indicator_d1},
    "f30_wtof_365_bb_kc_overlap_horizon_50_release_event_d1": {"inputs": ["high", "low", "close"], "func": f30_wtof_365_bb_kc_overlap_horizon_50_release_event_d1},
    "f30_wtof_366_nr4_indicator_d1": {"inputs": ["high", "low"], "func": f30_wtof_366_nr4_indicator_d1},
    "f30_wtof_367_nr7_indicator_d1": {"inputs": ["high", "low"], "func": f30_wtof_367_nr7_indicator_d1},
    "f30_wtof_368_wr4_indicator_d1": {"inputs": ["high", "low"], "func": f30_wtof_368_wr4_indicator_d1},
    "f30_wtof_369_wr7_indicator_d1": {"inputs": ["high", "low"], "func": f30_wtof_369_wr7_indicator_d1},
    "f30_wtof_370_two_bar_nr_consecutive_event_d1": {"inputs": ["high", "low"], "func": f30_wtof_370_two_bar_nr_consecutive_event_d1},
    "f30_wtof_371_nr7_at_252d_high_event_d1": {"inputs": ["high", "low"], "func": f30_wtof_371_nr7_at_252d_high_event_d1},
    "f30_wtof_372_nr4_at_252d_high_event_d1": {"inputs": ["high", "low"], "func": f30_wtof_372_nr4_at_252d_high_event_d1},
    "f30_wtof_373_inside_day_at_252d_high_event_d1": {"inputs": ["high", "low"], "func": f30_wtof_373_inside_day_at_252d_high_event_d1},
    "f30_wtof_374_outside_day_at_252d_high_event_d1": {"inputs": ["high", "low"], "func": f30_wtof_374_outside_day_at_252d_high_event_d1},
    "f30_wtof_375_id_nr4_double_compression_event_d1": {"inputs": ["high", "low"], "func": f30_wtof_375_id_nr4_double_compression_event_d1},
}

