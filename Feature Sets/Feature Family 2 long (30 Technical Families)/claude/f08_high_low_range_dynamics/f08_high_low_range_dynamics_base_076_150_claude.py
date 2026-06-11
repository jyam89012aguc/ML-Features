"""f08_high_low_range_dynamics base features 076-150.

Second batch of high-low range dynamics features. All structurally
distinct from base_001_075. Focuses on TR percentiles, ratio
structures, multi-window comparisons, regime transition signals,
asymmetric range contributions, and entropy/distribution shape.

NaN policy: never fillna(0); only replace([inf,-inf], nan) at return.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _tr(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    pc = close.shift(1)
    a = (high - low).abs()
    b = (high - pc).abs()
    c = (low - pc).abs()
    return pd.concat([a, b, c], axis=1).max(axis=1)


# ---------------------------------------------------------------------------
# Features 076-150
# ---------------------------------------------------------------------------


# --- Group A: Wilder ATR at varied N ---------------------------------------


def f08hl_f08_high_low_range_dynamics_atrwild_5d_base_v076_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Wilder ATR(5)/close. Very short-term ATR proxy."""
    pc = close.shift(1)
    a = (high - low).abs(); b = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, b, c], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 5.0, adjust=False, min_periods=5).mean()
    out = atr / close.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_atrlog_100d_base_v077_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """log(Wilder ATR(100) / closeadj). Long-horizon log relative ATR."""
    pc = closeadj.shift(1)
    a = (high - low).abs(); b = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, b, c], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 100.0, adjust=False, min_periods=100).mean()
    out = np.log(atr / closeadj.replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_atrshort_long_base_v078_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """log(Wilder ATR(7) / Wilder ATR(50)). Short vs long ATR ratio.
    Captures ATR regime momentum."""
    pc = closeadj.shift(1)
    a = (high - low).abs(); b = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, b, c], axis=1).max(axis=1)
    a7 = tr.ewm(alpha=1.0 / 7.0, adjust=False, min_periods=7).mean()
    a50 = tr.ewm(alpha=1.0 / 50.0, adjust=False, min_periods=50).mean()
    out = np.log(a7.replace(0.0, np.nan)) - np.log(a50.replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_atrslope_30d_base_v079_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Wilder ATR(30).diff(10) / ATR(30). Normalized ATR slope."""
    pc = closeadj.shift(1)
    a = (high - low).abs(); b = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, b, c], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 30.0, adjust=False, min_periods=30).mean()
    out = atr.diff(10) / atr.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_atrcurv_50d_base_v080_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Curvature of log(ATR(50)): l - 2*l.shift(10) + l.shift(20)."""
    pc = closeadj.shift(1)
    a = (high - low).abs(); b = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, b, c], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 50.0, adjust=False, min_periods=50).mean()
    la = np.log(atr.replace(0.0, np.nan))
    out = la - 2.0 * la.shift(10) + la.shift(20)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group B: TR distribution shape ----------------------------------------


def f08hl_f08_high_low_range_dynamics_trsk_60d_base_v081_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Skewness of TR over 60 bars."""
    pc = closeadj.shift(1)
    a = (high - low).abs(); b = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, b, c], axis=1).max(axis=1)
    out = tr.rolling(60, min_periods=60).skew()
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_trkur_60d_base_v082_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Median(TR,60) / Mean(TR,60). A robust-vs-mean ratio for TR
    distribution — captures shape asymmetry independent of skew."""
    pc = closeadj.shift(1)
    a = (high - low).abs(); b = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, b, c], axis=1).max(axis=1)
    md = tr.rolling(60, min_periods=60).median()
    mn = tr.rolling(60, min_periods=60).mean()
    out = md / mn.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_trmadr_40d_base_v083_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """MAD/std of TR in 40 bars. TR tail-fatness."""
    pc = closeadj.shift(1)
    a = (high - low).abs(); b = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, b, c], axis=1).max(axis=1)
    m = tr.rolling(40, min_periods=40).mean()
    mad = (tr - m).abs().rolling(40, min_periods=40).mean()
    sd = tr.rolling(40, min_periods=40).std()
    out = mad / sd.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group C: range above/below mean structural -----------------------------


def f08hl_f08_high_low_range_dynamics_rngdowncnt_50d_base_v084_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of bars in trailing 50 where range decreased vs prior bar."""
    rng = high - low
    down = (rng.diff() < 0.0).astype(float).where(~rng.diff().isna())
    out = down.rolling(50, min_periods=30).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngconseccnt_30d_base_v085_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Sum of (range.diff > 0)*(range.diff.shift(1)>0): consecutive
    range expansions in trailing 30 bars."""
    rng = high - low
    d = rng.diff()
    cur = (d > 0.0).astype(float)
    prv = (d.shift(1) > 0.0).astype(float)
    pair = cur * prv
    out = pair.rolling(30, min_periods=30).sum()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group D: range entropy via histogram-ish proxy ------------------------


def f08hl_f08_high_low_range_dynamics_rngent_60d_base_v086_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Shannon entropy of binned log range over 60 bars (8 bins via even
    width). High entropy = mixed bar sizes; low = uniform sizing."""
    rng = (high - low).replace(0.0, np.nan)
    lr = np.log(rng)

    def _ent(x: np.ndarray) -> float:
        if np.isnan(x).any():
            return np.nan
        lo = float(np.min(x))
        hi = float(np.max(x))
        if hi - lo == 0.0:
            return np.nan
        edges = np.linspace(lo, hi, 9)
        b = np.digitize(x, edges[1:-1])
        c = np.bincount(b, minlength=8).astype(float)
        c = c[c > 0]
        p = c / c.sum()
        return float(-np.sum(p * np.log(p)))

    out = lr.rolling(60, min_periods=60).apply(_ent, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group E: range vs prior range rolling stats ---------------------------


def f08hl_f08_high_low_range_dynamics_rngmom_10d_base_v087_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """log(range / range.shift(10)). 10-bar range momentum."""
    rng = (high - low).replace(0.0, np.nan)
    out = np.log(rng / rng.shift(10).replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngmom_50d_base_v088_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """log(SMA(range,10) / SMA(range,10).shift(50)). 50-bar momentum of
    smoothed range level. Uses closeadj-relevant horizon."""
    rng = (high - low)
    sm = rng.rolling(10, min_periods=10).mean()
    out = np.log(sm.replace(0.0, np.nan) / sm.shift(50).replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group F: high-low overlap with prior bar ------------------------------


def f08hl_f08_high_low_range_dynamics_overlap_15d_base_v089_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """SMA over 15 of bar-overlap ratio: max(0, min(high,high.shift1)-
    max(low,low.shift1)) / (high-low). 1 = total overlap, 0 = gap."""
    h_prev = high.shift(1); l_prev = low.shift(1)
    overlap_top = np.minimum(high, h_prev)
    overlap_bot = np.maximum(low, l_prev)
    overlap = (overlap_top - overlap_bot).clip(lower=0.0)
    r = overlap / (high - low).replace(0.0, np.nan)
    out = r.rolling(15, min_periods=15).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_overlapstd_30d_base_v090_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Std of overlap ratio over 30 bars. Stability of bar overlap."""
    h_prev = high.shift(1); l_prev = low.shift(1)
    overlap_top = np.minimum(high, h_prev)
    overlap_bot = np.maximum(low, l_prev)
    overlap = (overlap_top - overlap_bot).clip(lower=0.0)
    r = overlap / (high - low).replace(0.0, np.nan)
    out = r.rolling(30, min_periods=30).std()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group G: structural patterns - 2-bar / 3-bar combinations -------------


def f08hl_f08_high_low_range_dynamics_hihigher_30d_base_v091_signal(high: pd.Series) -> pd.Series:
    """Mean over 30 bars of (high > high.shift(1)) — frequency of higher
    highs. Pure-high structural counter."""
    flag = (high > high.shift(1)).astype(float).where(~high.shift(1).isna())
    out = flag.rolling(30, min_periods=30).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_lolower_30d_base_v092_signal(low: pd.Series) -> pd.Series:
    """Mean over 30 bars of (low < low.shift(1))."""
    flag = (low < low.shift(1)).astype(float).where(~low.shift(1).isna())
    out = flag.rolling(30, min_periods=30).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_hhll_diff_30d_base_v093_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """30-bar count of bars where BOTH (high > high.shift1 AND low > low.shift1).
    Coherent up-shift bars (trending range structure)."""
    both = ((high > high.shift(1)) & (low > low.shift(1))).astype(float).where(~high.shift(1).isna())
    out = both.rolling(30, min_periods=30).sum()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group H: extreme TR / range tail-frequency ----------------------------


def f08hl_f08_high_low_range_dynamics_trextqt_50d_base_v094_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Fraction of bars in trailing 50 where TR > rolling 50-bar 90th
    percentile of TR (recomputed at each end). Persistent tail-frequency."""
    pc = closeadj.shift(1)
    a = (high - low).abs(); b = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, b, c], axis=1).max(axis=1)
    p90 = tr.rolling(50, min_periods=50).quantile(0.90)
    flag = (tr > p90).astype(float).where(~p90.isna())
    out = flag.rolling(50, min_periods=30).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group I: range vs prior-bar / prior-range slope -----------------------


def f08hl_f08_high_low_range_dynamics_rngratrng_30d_base_v095_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean over 30 bars of log(range / range.shift(1)). Smoothed
    bar-to-bar log range change."""
    rng = (high - low).replace(0.0, np.nan)
    r = np.log(rng / rng.shift(1).replace(0.0, np.nan))
    out = r.rolling(30, min_periods=30).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group J: range scale-free measures via L^p norms ---------------------


def f08hl_f08_high_low_range_dynamics_rngenrm_30d_base_v096_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Energy ratio: sum(range^2,30) / (sum(range,30))^2 * 30.
    Equal to mean(range^2)/mean(range)^2 = 1 + CV^2."""
    rng = high - low
    s1 = rng.rolling(30, min_periods=30).sum()
    s2 = (rng ** 2).rolling(30, min_periods=30).sum()
    out = (30.0 * s2) / (s1 ** 2).replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group K: range vs absolute return -------------------------------------


def f08hl_f08_high_low_range_dynamics_rngabsretr_30d_base_v097_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Mean over 30 bars of range / (|return| * closeadj). Bar-level
    efficiency: high values = ranging without going anywhere."""
    rng = high - low
    aret = closeadj.diff().abs()
    r = rng / aret.replace(0.0, np.nan)
    rcl = r.clip(upper=20.0)
    out = rcl.rolling(30, min_periods=30).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group L: TR-based percentile decay ------------------------------------


def f08hl_f08_high_low_range_dynamics_trrnk100_base_v098_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Percentile rank of Wilder ATR(20) in trailing 100 bars."""
    pc = closeadj.shift(1)
    a = (high - low).abs(); b = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, b, c], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 20.0, adjust=False, min_periods=20).mean()
    out = atr.rolling(100, min_periods=60).rank(pct=True)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group M: range cumulative drift ---------------------------------------


def f08hl_f08_high_low_range_dynamics_rngsum_100d_base_v099_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """log(sum(range,100) / (100 * closeadj)). Long-horizon avg relative
    range on log scale."""
    rng = high - low
    s = rng.rolling(100, min_periods=100).sum()
    out = np.log(s / (100.0 * closeadj.replace(0.0, np.nan)))
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group N: rolling regression slope of range -----------------------------


def f08hl_f08_high_low_range_dynamics_rngreg_50d_base_v100_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope of log(range) on index t over 50 bars, normalized by
    mean(log(range), 50). Robust trend in range scale."""
    rng = (high - low).replace(0.0, np.nan)
    lr = np.log(rng)
    n = 50
    x = np.arange(n, dtype=float)
    x_mean = float(x.mean())
    xx = float(((x - x_mean) ** 2).sum())

    def _slp(y: np.ndarray) -> float:
        if np.isnan(y).any():
            return np.nan
        y_mean = float(np.mean(y))
        s = float(np.sum((x - x_mean) * (y - y_mean))) / xx
        return s

    slope = lr.rolling(n, min_periods=n).apply(_slp, raw=True)
    base = lr.rolling(n, min_periods=n).mean().abs().replace(0.0, np.nan)
    out = slope / base
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group O: range cluster regimes ----------------------------------------


def f08hl_f08_high_low_range_dynamics_rngabvavg_60d_base_v101_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Days-since-last range below 60-bar median. Capped at 60."""
    rng = high - low
    med = rng.rolling(60, min_periods=60).median()
    below = (rng < med).where(~med.isna())

    def _since(x: np.ndarray) -> float:
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return float(len(x))
        return float(len(x) - 1 - idx[-1])

    out = below.rolling(60, min_periods=60).apply(_since, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngblwavg_60d_base_v102_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Days-since-last range above 60-bar median. Capped at 60."""
    rng = high - low
    med = rng.rolling(60, min_periods=60).median()
    above = (rng > med).where(~med.isna())

    def _since(x: np.ndarray) -> float:
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return float(len(x))
        return float(len(x) - 1 - idx[-1])

    out = above.rolling(60, min_periods=60).apply(_since, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group P: TR shocks and outliers ---------------------------------------


def f08hl_f08_high_low_range_dynamics_trshock_30d_base_v103_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """log((TR / SMA(TR, 30))). Per-bar TR shock on log scale."""
    pc = closeadj.shift(1)
    a = (high - low).abs(); b = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, b, c], axis=1).max(axis=1).replace(0.0, np.nan)
    sm = tr.rolling(30, min_periods=30).mean()
    out = np.log(tr / sm.replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group Q: range geometric properties -----------------------------------


def f08hl_f08_high_low_range_dynamics_rnghigh_30d_base_v104_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """corr(high, range) over 30 bars. Tells whether range rises when
    highs are extending vs lows are extending."""
    rng = high - low
    out = rng.rolling(30, min_periods=30).corr(high)
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rnglow_30d_base_v105_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """corr(low, range) over 30 bars. Complement to v104."""
    rng = high - low
    out = rng.rolling(30, min_periods=30).corr(low)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group R: 5-bar range trends and slopes --------------------------------


def f08hl_f08_high_low_range_dynamics_emarng_20d_base_v106_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """EMA(20) of range / EMA(50) of range - 1. Smooth differential."""
    rng = high - low
    e20 = rng.ewm(span=20, adjust=False, min_periods=20).mean()
    e50 = rng.ewm(span=50, adjust=False, min_periods=50).mean()
    out = (e20 / e50.replace(0.0, np.nan)) - 1.0
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group S: outlier-related range diagnostics ---------------------------


def f08hl_f08_high_low_range_dynamics_rngwinsor_40d_base_v107_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """40-bar mean(range) / 40-bar median(range). Tail-bias diagnostic:
    > 1 means heavy upper tail."""
    rng = high - low
    m = rng.rolling(40, min_periods=40).mean()
    md = rng.rolling(40, min_periods=40).median()
    out = m / md.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group T: trough / peak relative position of range --------------------


def f08hl_f08_high_low_range_dynamics_rngfromtmin_60d_base_v108_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Position relative to trailing-60 range minimum: log(range/min)."""
    rng = (high - low).replace(0.0, np.nan)
    mn = rng.rolling(60, min_periods=40).min()
    out = np.log(rng / mn.replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngfromtmax_60d_base_v109_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Position relative to trailing-60 range maximum: log(range/max)."""
    rng = (high - low).replace(0.0, np.nan)
    mx = rng.rolling(60, min_periods=40).max()
    out = np.log(rng / mx.replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group U: range-derived breakout signals ------------------------------


def f08hl_f08_high_low_range_dynamics_rngbo_20d_base_v110_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Range breakout: 1 if range > trailing 20 max(range).shift(1), else 0.
    A new vol-spike day."""
    rng = high - low
    mx = rng.rolling(20, min_periods=20).max().shift(1)
    out = (rng > mx).astype(float).where(~mx.isna())
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngbocnt_50d_base_v111_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of range-breakouts in trailing 50 bars."""
    rng = high - low
    mx = rng.rolling(20, min_periods=20).max().shift(1)
    bo = (rng > mx).astype(float).where(~mx.isna())
    out = bo.rolling(50, min_periods=30).sum()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group V: range concentration / Gini-like ------------------------------


def f08hl_f08_high_low_range_dynamics_rnggini_30d_base_v112_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Pseudo-Gini of range over 30 bars: mean(|range - median|) / mean(range).
    Concentration of range mass."""
    rng = high - low

    def _gini(x: np.ndarray) -> float:
        m = float(np.median(x))
        mn = float(np.mean(x))
        if mn == 0.0:
            return np.nan
        return float(np.mean(np.abs(x - m)) / mn)

    out = rng.rolling(30, min_periods=30).apply(_gini, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group W: range zigzag / sign change frequency ------------------------


def f08hl_f08_high_low_range_dynamics_rngzigzag_30d_base_v113_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean over 30 bars of (sign(range.diff) != sign(range.diff.shift(1))).
    Frequency of range direction reversals."""
    rng = high - low
    d = rng.diff()
    s = np.sign(d)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    out = flip.rolling(30, min_periods=30).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group X: high or low diff vs prior close (gap-like for range) --------


def f08hl_f08_high_low_range_dynamics_hivspc_20d_base_v114_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """SMA over 20 bars of (high - close.shift(1)) / close.shift(1).
    Mean upside excursion vs prior close — TR upper component."""
    pc = close.shift(1)
    r = (high - pc) / pc.replace(0.0, np.nan)
    out = r.rolling(20, min_periods=20).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_lovspc_20d_base_v115_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """SMA over 20 bars of (close.shift(1) - low) / close.shift(1).
    Mean downside excursion vs prior close — TR lower component."""
    pc = close.shift(1)
    r = (pc - low) / pc.replace(0.0, np.nan)
    out = r.rolling(20, min_periods=20).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group Y: range pattern composite -------------------------------------


def f08hl_f08_high_low_range_dynamics_rngnetexp_50d_base_v116_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Magnitude-weighted net range expansion: sum over 50 bars of
    log(range/range.shift(1)) (signed). Captures whether expansion or
    contraction has dominated by amount, not just count."""
    rng = (high - low).replace(0.0, np.nan)
    r = np.log(rng / rng.shift(1).replace(0.0, np.nan))
    out = r.rolling(50, min_periods=30).sum()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group Z: range vs ATR cross-window ------------------------------------


def f08hl_f08_high_low_range_dynamics_atr14sma14_base_v117_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """log(Wilder ATR(14) / SMA(TR,14)). Differential between Wilder smoother
    and SMA on same window — captures lead/lag."""
    pc = close.shift(1)
    a = (high - low).abs(); b = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, b, c], axis=1).max(axis=1)
    w = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    s = tr.rolling(14, min_periods=14).mean()
    out = np.log(w.replace(0.0, np.nan)) - np.log(s.replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group AA: cycles within range -----------------------------------------


def f08hl_f08_high_low_range_dynamics_rngfourier_60d_base_v118_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Dominant low-freq cycle strength: power at freq=1 / total power
    of log range over trailing 60 bars (DFT-based)."""
    rng = (high - low).replace(0.0, np.nan)
    lr = np.log(rng)

    def _f(x: np.ndarray) -> float:
        if np.isnan(x).any():
            return np.nan
        x = x - x.mean()
        f = np.fft.rfft(x)
        p = np.abs(f) ** 2
        if p.sum() == 0.0:
            return np.nan
        return float(p[1] / p.sum())

    out = lr.rolling(60, min_periods=60).apply(_f, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group AB: range vs close trend correlation ----------------------------


def f08hl_f08_high_low_range_dynamics_rngtrcl_30d_base_v119_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """corr(range, |close.diff(1)|) over 30 bars. Tells whether wide bars
    coincide with big closes."""
    rng = high - low
    cd = close.diff(1).abs()
    out = rng.rolling(30, min_periods=30).corr(cd)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group AC: TR / range pattern at 60-day scale --------------------------


def f08hl_f08_high_low_range_dynamics_trrngrat_30d_base_v120_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """SMA over 30 of TR/range. Average gap-component share over a month."""
    pc = close.shift(1)
    a = (high - low).abs(); b = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, b, c], axis=1).max(axis=1)
    rng = (high - low).replace(0.0, np.nan)
    r = tr / rng
    out = r.rolling(30, min_periods=30).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group AD: outer/inner range trend ------------------------------------


def f08hl_f08_high_low_range_dynamics_donchwid_50d_base_v121_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Donchian-channel width over 50 bars: (max(high,50) - min(low,50))/
    closeadj. Container range, not per-bar range."""
    hh = high.rolling(50, min_periods=50).max()
    ll = low.rolling(50, min_periods=50).min()
    out = (hh - ll) / closeadj.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)






# --- Group AE: Yang-Zhang and Parkinson volatilities ----------------------


def f08hl_f08_high_low_range_dynamics_parkvol_20d_base_v124_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Parkinson vol over 20 bars: sqrt(mean((log h/l)^2,20) / (4*ln(2)))."""
    lr2 = (np.log(high.replace(0.0, np.nan)) - np.log(low.replace(0.0, np.nan))) ** 2
    out = np.sqrt(lr2.rolling(20, min_periods=20).mean() / (4.0 * np.log(2.0)))
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_parkvolratio_50d_base_v125_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """log(Parkinson vol(20) / Parkinson vol(50)). Ratio of two horizons of
    Parkinson — short vs long high-low vol."""
    lr2 = (np.log(high.replace(0.0, np.nan)) - np.log(low.replace(0.0, np.nan))) ** 2
    p20 = np.sqrt(lr2.rolling(20, min_periods=20).mean() / (4.0 * np.log(2.0)))
    p50 = np.sqrt(lr2.rolling(50, min_periods=50).mean() / (4.0 * np.log(2.0)))
    out = np.log(p20.replace(0.0, np.nan) / p50.replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_gkvol_30d_base_v126_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Garman-Klass vol over 30 bars: sqrt(mean(0.5*(log h/l)^2 -
    (2*ln 2 - 1)*(log c/o)^2, 30))."""
    lhl2 = (np.log(high.replace(0.0, np.nan)) - np.log(low.replace(0.0, np.nan))) ** 2
    lco2 = (np.log(close.replace(0.0, np.nan)) - np.log(open.replace(0.0, np.nan))) ** 2
    gk = 0.5 * lhl2 - (2.0 * np.log(2.0) - 1.0) * lco2
    gk_pos = gk.where(gk >= 0.0)
    out = np.sqrt(gk_pos.rolling(30, min_periods=30).mean())
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group AF: range pattern - inside/outside contextual -------------------


def f08hl_f08_high_low_range_dynamics_insouttrend_60d_base_v127_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Inside-bar fraction minus outside-bar fraction over 60 bars.
    Compression vs expansion regime indicator."""
    ins = ((high < high.shift(1)) & (low > low.shift(1))).astype(float)
    out_b = ((high > high.shift(1)) & (low < low.shift(1))).astype(float)
    di = ins.rolling(60, min_periods=40).mean() - out_b.rolling(60, min_periods=40).mean()
    return di.replace([np.inf, -np.inf], np.nan)


# --- Group AG: range fft secondary cycle ---------------------------------


def f08hl_f08_high_low_range_dynamics_rngslowcyc_60d_base_v128_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Spectral entropy of log range over 60 bars (4-bin freq decomposition).
    Range process complexity."""
    rng = (high - low).replace(0.0, np.nan)
    lr = np.log(rng)

    def _se(x: np.ndarray) -> float:
        if np.isnan(x).any():
            return np.nan
        x = x - x.mean()
        f = np.fft.rfft(x)
        p = np.abs(f) ** 2
        s = p.sum()
        if s == 0.0:
            return np.nan
        pn = p / s
        pn = pn[pn > 0]
        return float(-np.sum(pn * np.log(pn)))

    out = lr.rolling(60, min_periods=60).apply(_se, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group AH: range slope at very long horizon ---------------------------


def f08hl_f08_high_low_range_dynamics_rngslope_100d_base_v129_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """SMA(range,100).diff(21) / SMA(range,100). Annual range slope."""
    rng = high - low
    sma = rng.rolling(100, min_periods=100).mean()
    out = sma.diff(21) / sma.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngslope_5d_base_v130_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """SMA(range,5).diff(3) / SMA(range,5). Very-short MA-range slope."""
    rng = high - low
    sma = rng.rolling(5, min_periods=5).mean()
    out = sma.diff(3) / sma.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group AI: TR sign and tilt -------------------------------------------


def f08hl_f08_high_low_range_dynamics_trupcomp_30d_base_v131_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Avg over 30 of max(0, high - close.shift(1)) / TR. Mean fraction of
    TR contributed by upside extension beyond prior close."""
    pc = closeadj.shift(1)
    a = (high - low).abs(); b = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, b, c], axis=1).max(axis=1).replace(0.0, np.nan)
    upcomp = (high - pc).clip(lower=0.0)
    r = upcomp / tr
    out = r.rolling(30, min_periods=30).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_trdncomp_30d_base_v132_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Variability of TR-extension asymmetry: 30-bar std of
    ((high-pc).clip(0) - (pc-low).clip(0)) / TR. High = volatile asymmetry."""
    pc = closeadj.shift(1)
    a = (high - low).abs(); b = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, b, c], axis=1).max(axis=1).replace(0.0, np.nan)
    asym = ((high - pc).clip(lower=0.0) - (pc - low).clip(lower=0.0)) / tr
    out = asym.rolling(30, min_periods=30).std()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group AJ: high or low new-extreme frequency --------------------------


def f08hl_f08_high_low_range_dynamics_newhi_20d_base_v133_signal(high: pd.Series) -> pd.Series:
    """Days since new 20-bar high. Output in [0, 20]."""
    win = 20
    mx = high.rolling(win, min_periods=win).max()
    flag = (high >= mx).where(~mx.isna())

    def _since(x: np.ndarray) -> float:
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return float(len(x))
        return float(len(x) - 1 - idx[-1])

    out = flag.rolling(win, min_periods=win).apply(_since, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_newlo_20d_base_v134_signal(low: pd.Series) -> pd.Series:
    """Days since new 20-bar low. Output in [0, 20]."""
    win = 20
    mn = low.rolling(win, min_periods=win).min()
    flag = (low <= mn).where(~mn.isna())

    def _since(x: np.ndarray) -> float:
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return float(len(x))
        return float(len(x) - 1 - idx[-1])

    out = flag.rolling(win, min_periods=win).apply(_since, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group AK: range / sub-window decomposition ---------------------------


def f08hl_f08_high_low_range_dynamics_rngratlog_25d_base_v135_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """log(SMA(range,10)) - log(SMA(range,25)). Mid-window log differential."""
    rng = (high - low).replace(0.0, np.nan)
    s10 = rng.rolling(10, min_periods=10).mean()
    s25 = rng.rolling(25, min_periods=25).mean()
    out = np.log(s10.replace(0.0, np.nan)) - np.log(s25.replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngratlog_long_base_v136_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """log(SMA(range,50)) - log(SMA(range,200)). Long-window log differential."""
    rng = (high - low).replace(0.0, np.nan)
    s50 = rng.rolling(50, min_periods=50).mean()
    s200 = rng.rolling(200, min_periods=200).mean()
    out = np.log(s50.replace(0.0, np.nan)) - np.log(s200.replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group AL: range quantile spread --------------------------------------


def f08hl_f08_high_low_range_dynamics_rngq90q10_50d_base_v137_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """log(Q90(range,50)) - log(Q10(range,50)). Inter-decile width of range
    distribution. Wider = more bimodal/regimes."""
    rng = (high - low).replace(0.0, np.nan)
    lr = np.log(rng)
    q90 = lr.rolling(50, min_periods=50).quantile(0.90)
    q10 = lr.rolling(50, min_periods=50).quantile(0.10)
    out = q90 - q10
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group AM: high-low ratio --------------------------------------------


def f08hl_f08_high_low_range_dynamics_hlratio_50d_base_v138_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """SMA over 50 bars of high/low - 1. Mean intra-bar ratio - 1."""
    r = (high / low.replace(0.0, np.nan)) - 1.0
    out = r.rolling(50, min_periods=50).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group AN: range tail incidence ---------------------------------------


def f08hl_f08_high_low_range_dynamics_rngtailcnt_60d_base_v139_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of bars in trailing 60 where log(range) > rolling 60-bar
    median(log range) + std(log range)."""
    rng = (high - low).replace(0.0, np.nan)
    lr = np.log(rng)
    md = lr.rolling(60, min_periods=60).median()
    sd = lr.rolling(60, min_periods=60).std()
    thresh = md + sd
    flag = (lr > thresh).astype(float).where(~thresh.isna())
    out = flag.rolling(60, min_periods=40).sum()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group AO: range vs rolling close-vol ---------------------------------


def f08hl_f08_high_low_range_dynamics_parkvscclvol_60d_base_v140_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Parkinson(20) vol / close-return std(20). Should be ~1.0 in Brownian
    motion. Departures = systematic intra-bar mean reversion or trending."""
    lr2 = (np.log(high.replace(0.0, np.nan)) - np.log(low.replace(0.0, np.nan))) ** 2
    pv = np.sqrt(lr2.rolling(20, min_periods=20).mean() / (4.0 * np.log(2.0)))
    cret = np.log(closeadj.replace(0.0, np.nan)).diff()
    cv = cret.rolling(20, min_periods=20).std()
    out = pv / cv.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group AP: range cross-corr with itself ratio -------------------------


def f08hl_f08_high_low_range_dynamics_rngnegcorr_40d_base_v141_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """corr(range, range.shift(20)) over 40 bars. Lag-20 cyclical memory."""
    rng = (high - low).replace(0.0, np.nan)
    lr = np.log(rng)
    out = lr.rolling(40, min_periods=40).corr(lr.shift(20))
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group AQ: very-short range expansion ---------------------------------


def f08hl_f08_high_low_range_dynamics_rng3of5_base_v142_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of bars in trailing 5 where range > range.shift(1)."""
    rng = high - low
    flag = (rng > rng.shift(1)).astype(float).where(~rng.shift(1).isna())
    out = flag.rolling(5, min_periods=5).sum()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group AR: range vs close range -----------------------------------------


def f08hl_f08_high_low_range_dynamics_closecov_40d_base_v143_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """SMA over 40 of (high-low)/|close - close.shift(1)|. Per-bar
    intraday-vs-overnight efficiency."""
    pc = close.shift(1)
    rng = high - low
    nc = (close - pc).abs().replace(0.0, np.nan)
    r = (rng / nc).clip(upper=50.0)
    out = r.rolling(40, min_periods=40).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group AS: high/low extension events ----------------------------------


def f08hl_f08_high_low_range_dynamics_hiltrkurt_30d_base_v144_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Difference of skews: skew(log range,30) - kurt(log range,30)/3.
    A composite of distributional shape diagnostics."""
    lr = np.log((high - low).replace(0.0, np.nan))
    sk = lr.rolling(30, min_periods=30).skew()
    kt = lr.rolling(30, min_periods=30).kurt()
    out = sk - kt / 3.0
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group AT: TR ATR-divergence -------------------------------------------


def f08hl_f08_high_low_range_dynamics_atrnormdev_50d_base_v145_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """(TR - ATR(20)) / ATR(20). Per-bar TR-shock vs slow ATR. Smoothed over 5."""
    pc = closeadj.shift(1)
    a = (high - low).abs(); b = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, b, c], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 20.0, adjust=False, min_periods=20).mean()
    dev = (tr - atr) / atr.replace(0.0, np.nan)
    out = dev.rolling(5, min_periods=5).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group AU: log-range running max/min --------------------------------


def f08hl_f08_high_low_range_dynamics_logrngwid_60d_base_v146_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """log(max(range,60)) - log(min(range,60)). Range-of-range span."""
    rng = (high - low).replace(0.0, np.nan)
    lr = np.log(rng)
    out = lr.rolling(60, min_periods=60).max() - lr.rolling(60, min_periods=60).min()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group AV: 7-bar range vs 30-bar range trends -----------------------


def f08hl_f08_high_low_range_dynamics_rngclasif_30d_base_v147_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Sign(SMA(range,7) - SMA(range,30)). Discrete regime sign."""
    rng = high - low
    s7 = rng.rolling(7, min_periods=7).mean()
    s30 = rng.rolling(30, min_periods=30).mean()
    d = s7 - s30
    out = pd.Series(np.sign(d.values), index=d.index, dtype=float).where(~d.isna())
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group AW: range cross-correlation with prior shift --------------------


def f08hl_f08_high_low_range_dynamics_rngacrng_30d_base_v148_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """corr(log range, log range.shift(2)) over 30 bars. Lag-2 persistence."""
    rng = (high - low).replace(0.0, np.nan)
    lr = np.log(rng)
    out = lr.rolling(30, min_periods=30).corr(lr.shift(2))
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group AX: SMA range slope discrete --------------------------------


def f08hl_f08_high_low_range_dynamics_rngslpsig_50d_base_v149_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Fraction over 50 bars where SMA(range,10).diff(3) > 0. Long-horizon
    expansion frequency."""
    rng = high - low
    sma = rng.rolling(10, min_periods=10).mean()
    pos = (sma.diff(3) > 0.0).astype(float).where(~sma.diff(3).isna())
    out = pos.rolling(50, min_periods=30).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group AY: range path / scale via Hurst-like -------------------------


def f08hl_f08_high_low_range_dynamics_rngfractal_60d_base_v150_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Box-count proxy for range path length / chord:
    sum(|range.diff|, 60) / (max(range,60) - min(range,60)).
    Higher = more zigzag in range path."""
    rng = high - low
    pl = rng.diff().abs().rolling(60, min_periods=60).sum()
    chord = rng.rolling(60, min_periods=60).max() - rng.rolling(60, min_periods=60).min()
    out = pl / chord.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f08_high_low_range_dynamics_base_076_150_REGISTRY = {
    "f08hl_f08_high_low_range_dynamics_atrwild_5d_base_v076_signal": {"inputs": ["high", "low", "close"], "func": f08hl_f08_high_low_range_dynamics_atrwild_5d_base_v076_signal},
    "f08hl_f08_high_low_range_dynamics_atrlog_100d_base_v077_signal": {"inputs": ["high", "low", "closeadj"], "func": f08hl_f08_high_low_range_dynamics_atrlog_100d_base_v077_signal},
    "f08hl_f08_high_low_range_dynamics_atrshort_long_base_v078_signal": {"inputs": ["high", "low", "closeadj"], "func": f08hl_f08_high_low_range_dynamics_atrshort_long_base_v078_signal},
    "f08hl_f08_high_low_range_dynamics_atrslope_30d_base_v079_signal": {"inputs": ["high", "low", "closeadj"], "func": f08hl_f08_high_low_range_dynamics_atrslope_30d_base_v079_signal},
    "f08hl_f08_high_low_range_dynamics_atrcurv_50d_base_v080_signal": {"inputs": ["high", "low", "closeadj"], "func": f08hl_f08_high_low_range_dynamics_atrcurv_50d_base_v080_signal},
    "f08hl_f08_high_low_range_dynamics_trsk_60d_base_v081_signal": {"inputs": ["high", "low", "closeadj"], "func": f08hl_f08_high_low_range_dynamics_trsk_60d_base_v081_signal},
    "f08hl_f08_high_low_range_dynamics_trkur_60d_base_v082_signal": {"inputs": ["high", "low", "closeadj"], "func": f08hl_f08_high_low_range_dynamics_trkur_60d_base_v082_signal},
    "f08hl_f08_high_low_range_dynamics_trmadr_40d_base_v083_signal": {"inputs": ["high", "low", "closeadj"], "func": f08hl_f08_high_low_range_dynamics_trmadr_40d_base_v083_signal},
    "f08hl_f08_high_low_range_dynamics_rngdowncnt_50d_base_v084_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngdowncnt_50d_base_v084_signal},
    "f08hl_f08_high_low_range_dynamics_rngconseccnt_30d_base_v085_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngconseccnt_30d_base_v085_signal},
    "f08hl_f08_high_low_range_dynamics_rngent_60d_base_v086_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngent_60d_base_v086_signal},
    "f08hl_f08_high_low_range_dynamics_rngmom_10d_base_v087_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngmom_10d_base_v087_signal},
    "f08hl_f08_high_low_range_dynamics_rngmom_50d_base_v088_signal": {"inputs": ["high", "low", "closeadj"], "func": f08hl_f08_high_low_range_dynamics_rngmom_50d_base_v088_signal},
    "f08hl_f08_high_low_range_dynamics_overlap_15d_base_v089_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_overlap_15d_base_v089_signal},
    "f08hl_f08_high_low_range_dynamics_overlapstd_30d_base_v090_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_overlapstd_30d_base_v090_signal},
    "f08hl_f08_high_low_range_dynamics_hihigher_30d_base_v091_signal": {"inputs": ["high"], "func": f08hl_f08_high_low_range_dynamics_hihigher_30d_base_v091_signal},
    "f08hl_f08_high_low_range_dynamics_lolower_30d_base_v092_signal": {"inputs": ["low"], "func": f08hl_f08_high_low_range_dynamics_lolower_30d_base_v092_signal},
    "f08hl_f08_high_low_range_dynamics_hhll_diff_30d_base_v093_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_hhll_diff_30d_base_v093_signal},
    "f08hl_f08_high_low_range_dynamics_trextqt_50d_base_v094_signal": {"inputs": ["high", "low", "closeadj"], "func": f08hl_f08_high_low_range_dynamics_trextqt_50d_base_v094_signal},
    "f08hl_f08_high_low_range_dynamics_rngratrng_30d_base_v095_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngratrng_30d_base_v095_signal},
    "f08hl_f08_high_low_range_dynamics_rngenrm_30d_base_v096_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngenrm_30d_base_v096_signal},
    "f08hl_f08_high_low_range_dynamics_rngabsretr_30d_base_v097_signal": {"inputs": ["high", "low", "closeadj"], "func": f08hl_f08_high_low_range_dynamics_rngabsretr_30d_base_v097_signal},
    "f08hl_f08_high_low_range_dynamics_trrnk100_base_v098_signal": {"inputs": ["high", "low", "closeadj"], "func": f08hl_f08_high_low_range_dynamics_trrnk100_base_v098_signal},
    "f08hl_f08_high_low_range_dynamics_rngsum_100d_base_v099_signal": {"inputs": ["high", "low", "closeadj"], "func": f08hl_f08_high_low_range_dynamics_rngsum_100d_base_v099_signal},
    "f08hl_f08_high_low_range_dynamics_rngreg_50d_base_v100_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngreg_50d_base_v100_signal},
    "f08hl_f08_high_low_range_dynamics_rngabvavg_60d_base_v101_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngabvavg_60d_base_v101_signal},
    "f08hl_f08_high_low_range_dynamics_rngblwavg_60d_base_v102_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngblwavg_60d_base_v102_signal},
    "f08hl_f08_high_low_range_dynamics_trshock_30d_base_v103_signal": {"inputs": ["high", "low", "closeadj"], "func": f08hl_f08_high_low_range_dynamics_trshock_30d_base_v103_signal},
    "f08hl_f08_high_low_range_dynamics_rnghigh_30d_base_v104_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rnghigh_30d_base_v104_signal},
    "f08hl_f08_high_low_range_dynamics_rnglow_30d_base_v105_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rnglow_30d_base_v105_signal},
    "f08hl_f08_high_low_range_dynamics_emarng_20d_base_v106_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_emarng_20d_base_v106_signal},
    "f08hl_f08_high_low_range_dynamics_rngwinsor_40d_base_v107_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngwinsor_40d_base_v107_signal},
    "f08hl_f08_high_low_range_dynamics_rngfromtmin_60d_base_v108_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngfromtmin_60d_base_v108_signal},
    "f08hl_f08_high_low_range_dynamics_rngfromtmax_60d_base_v109_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngfromtmax_60d_base_v109_signal},
    "f08hl_f08_high_low_range_dynamics_rngbo_20d_base_v110_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngbo_20d_base_v110_signal},
    "f08hl_f08_high_low_range_dynamics_rngbocnt_50d_base_v111_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngbocnt_50d_base_v111_signal},
    "f08hl_f08_high_low_range_dynamics_rnggini_30d_base_v112_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rnggini_30d_base_v112_signal},
    "f08hl_f08_high_low_range_dynamics_rngzigzag_30d_base_v113_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngzigzag_30d_base_v113_signal},
    "f08hl_f08_high_low_range_dynamics_hivspc_20d_base_v114_signal": {"inputs": ["high", "low", "close"], "func": f08hl_f08_high_low_range_dynamics_hivspc_20d_base_v114_signal},
    "f08hl_f08_high_low_range_dynamics_lovspc_20d_base_v115_signal": {"inputs": ["high", "low", "close"], "func": f08hl_f08_high_low_range_dynamics_lovspc_20d_base_v115_signal},
    "f08hl_f08_high_low_range_dynamics_rngnetexp_50d_base_v116_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngnetexp_50d_base_v116_signal},
    "f08hl_f08_high_low_range_dynamics_atr14sma14_base_v117_signal": {"inputs": ["high", "low", "close"], "func": f08hl_f08_high_low_range_dynamics_atr14sma14_base_v117_signal},
    "f08hl_f08_high_low_range_dynamics_rngfourier_60d_base_v118_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngfourier_60d_base_v118_signal},
    "f08hl_f08_high_low_range_dynamics_rngtrcl_30d_base_v119_signal": {"inputs": ["high", "low", "close"], "func": f08hl_f08_high_low_range_dynamics_rngtrcl_30d_base_v119_signal},
    "f08hl_f08_high_low_range_dynamics_trrngrat_30d_base_v120_signal": {"inputs": ["high", "low", "close"], "func": f08hl_f08_high_low_range_dynamics_trrngrat_30d_base_v120_signal},
    "f08hl_f08_high_low_range_dynamics_donchwid_50d_base_v121_signal": {"inputs": ["high", "low", "closeadj"], "func": f08hl_f08_high_low_range_dynamics_donchwid_50d_base_v121_signal},
    "f08hl_f08_high_low_range_dynamics_parkvol_20d_base_v124_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_parkvol_20d_base_v124_signal},
    "f08hl_f08_high_low_range_dynamics_parkvolratio_50d_base_v125_signal": {"inputs": ["high", "low", "closeadj"], "func": f08hl_f08_high_low_range_dynamics_parkvolratio_50d_base_v125_signal},
    "f08hl_f08_high_low_range_dynamics_gkvol_30d_base_v126_signal": {"inputs": ["open", "high", "low", "close"], "func": f08hl_f08_high_low_range_dynamics_gkvol_30d_base_v126_signal},
    "f08hl_f08_high_low_range_dynamics_insouttrend_60d_base_v127_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_insouttrend_60d_base_v127_signal},
    "f08hl_f08_high_low_range_dynamics_rngslowcyc_60d_base_v128_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngslowcyc_60d_base_v128_signal},
    "f08hl_f08_high_low_range_dynamics_rngslope_100d_base_v129_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngslope_100d_base_v129_signal},
    "f08hl_f08_high_low_range_dynamics_rngslope_5d_base_v130_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngslope_5d_base_v130_signal},
    "f08hl_f08_high_low_range_dynamics_trupcomp_30d_base_v131_signal": {"inputs": ["high", "low", "closeadj"], "func": f08hl_f08_high_low_range_dynamics_trupcomp_30d_base_v131_signal},
    "f08hl_f08_high_low_range_dynamics_trdncomp_30d_base_v132_signal": {"inputs": ["high", "low", "closeadj"], "func": f08hl_f08_high_low_range_dynamics_trdncomp_30d_base_v132_signal},
    "f08hl_f08_high_low_range_dynamics_newhi_20d_base_v133_signal": {"inputs": ["high"], "func": f08hl_f08_high_low_range_dynamics_newhi_20d_base_v133_signal},
    "f08hl_f08_high_low_range_dynamics_newlo_20d_base_v134_signal": {"inputs": ["low"], "func": f08hl_f08_high_low_range_dynamics_newlo_20d_base_v134_signal},
    "f08hl_f08_high_low_range_dynamics_rngratlog_25d_base_v135_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngratlog_25d_base_v135_signal},
    "f08hl_f08_high_low_range_dynamics_rngratlog_long_base_v136_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngratlog_long_base_v136_signal},
    "f08hl_f08_high_low_range_dynamics_rngq90q10_50d_base_v137_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngq90q10_50d_base_v137_signal},
    "f08hl_f08_high_low_range_dynamics_hlratio_50d_base_v138_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_hlratio_50d_base_v138_signal},
    "f08hl_f08_high_low_range_dynamics_rngtailcnt_60d_base_v139_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngtailcnt_60d_base_v139_signal},
    "f08hl_f08_high_low_range_dynamics_parkvscclvol_60d_base_v140_signal": {"inputs": ["high", "low", "closeadj"], "func": f08hl_f08_high_low_range_dynamics_parkvscclvol_60d_base_v140_signal},
    "f08hl_f08_high_low_range_dynamics_rngnegcorr_40d_base_v141_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngnegcorr_40d_base_v141_signal},
    "f08hl_f08_high_low_range_dynamics_rng3of5_base_v142_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rng3of5_base_v142_signal},
    "f08hl_f08_high_low_range_dynamics_closecov_40d_base_v143_signal": {"inputs": ["open", "high", "low", "close"], "func": f08hl_f08_high_low_range_dynamics_closecov_40d_base_v143_signal},
    "f08hl_f08_high_low_range_dynamics_hiltrkurt_30d_base_v144_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_hiltrkurt_30d_base_v144_signal},
    "f08hl_f08_high_low_range_dynamics_atrnormdev_50d_base_v145_signal": {"inputs": ["high", "low", "closeadj"], "func": f08hl_f08_high_low_range_dynamics_atrnormdev_50d_base_v145_signal},
    "f08hl_f08_high_low_range_dynamics_logrngwid_60d_base_v146_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_logrngwid_60d_base_v146_signal},
    "f08hl_f08_high_low_range_dynamics_rngclasif_30d_base_v147_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngclasif_30d_base_v147_signal},
    "f08hl_f08_high_low_range_dynamics_rngacrng_30d_base_v148_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngacrng_30d_base_v148_signal},
    "f08hl_f08_high_low_range_dynamics_rngslpsig_50d_base_v149_signal": {"inputs": ["high", "low", "closeadj"], "func": f08hl_f08_high_low_range_dynamics_rngslpsig_50d_base_v149_signal},
    "f08hl_f08_high_low_range_dynamics_rngfractal_60d_base_v150_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngfractal_60d_base_v150_signal},
}


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------


def _synthetic_inputs(n: int = 800, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    seg = n // 4
    rest = n - 3 * seg
    ret = np.concatenate([
        rng.normal(0.0012, 0.011, seg),
        rng.normal(-0.0005, 0.018, seg),
        rng.normal(-0.0010, 0.014, seg),
        rng.normal(0.0008, 0.012, rest),
    ])
    close = 50.0 * np.exp(np.cumsum(ret))
    adj_drift = rng.normal(0.0, 0.0003, size=n).cumsum()
    closeadj = close * np.exp(adj_drift)
    intraday = rng.normal(0.0, 0.008, size=n)
    open_ = close * np.exp(-intraday * 0.5)
    high = np.maximum(close, open_) * np.exp(np.abs(rng.normal(0.0, 0.006, size=n)))
    low = np.minimum(close, open_) * np.exp(-np.abs(rng.normal(0.0, 0.006, size=n)))
    volume = rng.lognormal(mean=13.0, sigma=0.6, size=n)
    idx = pd.RangeIndex(n)
    return pd.DataFrame({
        "open": pd.Series(open_, index=idx, dtype=float),
        "high": pd.Series(high, index=idx, dtype=float),
        "low": pd.Series(low, index=idx, dtype=float),
        "close": pd.Series(close, index=idx, dtype=float),
        "closeadj": pd.Series(closeadj, index=idx, dtype=float),
        "volume": pd.Series(volume, index=idx, dtype=float),
    })


def _self_test() -> None:
    df = _synthetic_inputs(n=800, seed=42)
    results: dict[str, pd.Series] = {}
    for name, entry in f08_high_low_range_dynamics_base_076_150_REGISTRY.items():
        args = [df[col] for col in entry["inputs"]]
        out = entry["func"](*args)
        assert isinstance(out, pd.Series), f"{name}: not a Series"
        assert len(out) == len(df), f"{name}: length mismatch"
        clean = out.dropna()
        assert len(clean) > 0, f"{name}: all NaN"
        assert float(clean.std()) > 0.0 or clean.nunique() > 1, f"{name}: constant/all-zero"
        results[name] = out

    warm = 252
    coverage_ok = sum(1 for s in results.values() if s.iloc[warm:].isna().mean() < 0.5)
    frac = coverage_ok / len(results)
    assert frac >= 0.80, f"NaN-coverage too low: {frac:.2%} have <50% NaN after warm-up"

    aligned = pd.concat({n: results[n] for n in results}, axis=1).iloc[warm:]
    aligned = aligned.replace([np.inf, -np.inf], np.nan)
    corr = aligned.corr(min_periods=50).abs()
    np.fill_diagonal(corr.values, 0.0)
    max_corr = float(corr.max().max())
    if max_corr > 0.95:
        print(f"FAILING max |corr| = {max_corr:.4f}. Top pairs:")
        for i, a in enumerate(corr.columns):
            for j, b in enumerate(corr.columns):
                if j > i and corr.iloc[i, j] > 0.94:
                    print(f"  {a}  vs  {b}  ->  {corr.iloc[i, j]:.4f}")
    assert max_corr <= 0.95 + 1e-9, f"max pairwise |corr|={max_corr:.4f} exceeds 0.95"
    print(f"OK base_076_150: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
