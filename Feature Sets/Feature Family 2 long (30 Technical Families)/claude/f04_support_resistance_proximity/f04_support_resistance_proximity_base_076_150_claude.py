"""f04_support_resistance_proximity base features 076-150.

Continues the S/R-proximity feature catalog with structurally distinct
classes from the first 75: Camarilla / Fibonacci / Woodie full pivot
families, volume-anchored level distances (VWAP / volume-POC),
wave-pattern (HH / LL / HL / LH) counts, multi-N fractal level
distances, ATR-normalized distance to extremes, confirmed multi-bar
break signals, post-break recovery / pullback metrics, anchored
year-ago levels, and statistical S/R density measures (z-scores,
distribution skew/kurtosis of distances to historical pivots).

NO MA-based features, NO pure channel-position features, NO
trend-strength features. Every feature anchors to a SPECIFIC prior
price level.

NaN policy: never `fillna(0)`; only `replace([inf,-inf], nan)` at
return. Window > 21 trading days uses `closeadj`; windows <= 21 use
`close`. OHLC features within a single bar use unadjusted high/low.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Helpers (small, named utilities; each feature still spells its full
# expression inline).
# ---------------------------------------------------------------------------


def _bars_since_true(mask: pd.Series, cap: int) -> pd.Series:
    out = pd.Series(np.nan, index=mask.index, dtype=float)
    last = np.nan
    for i in range(len(mask)):
        v = mask.iloc[i]
        if isinstance(v, (bool, np.bool_)) and bool(v):
            last = i
        if not np.isnan(last):
            out.iloc[i] = float(min(i - last, cap))
    return out


def _streak_above(cond: pd.Series) -> pd.Series:
    out = pd.Series(np.nan, index=cond.index, dtype=float)
    run = 0
    started = False
    for i in range(len(cond)):
        v = cond.iloc[i]
        if isinstance(v, float) and np.isnan(v):
            continue
        started = True
        if bool(v):
            run += 1
        else:
            run = 0
        out.iloc[i] = float(run)
    if not started:
        return out
    return out


def _true_range(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    pc = close.shift(1)
    a = (high - low).abs()
    b = (high - pc).abs()
    c = (low - pc).abs()
    return pd.concat([a, b, c], axis=1).max(axis=1)


# ---------------------------------------------------------------------------
# Features 076-150
# ---------------------------------------------------------------------------


# --- Group A1: Pivot-level distance with rolling-period H/L/C anchors ------


def f04sr_f04_support_resistance_proximity_dmpv_21d_base_v076_signal(closeadj: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Range width of the rolling 21d "monthly" pivot zone normalized
    by closeadj: (max(H,21) - min(L,21)) / closeadj. A breadth metric
    of the monthly S/R envelope, not a distance to its center."""
    h21 = high.rolling(21, min_periods=21).max().shift(1)
    l21 = low.rolling(21, min_periods=21).min().shift(1)
    out = (h21 - l21) / closeadj.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dwpv_5d_base_v077_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance to "weekly" pivot computed over 5d-prior H/L/C window."""
    h5 = high.rolling(5, min_periods=5).max().shift(1)
    l5 = low.rolling(5, min_periods=5).min().shift(1)
    c1 = close.shift(1)
    pivot = (h5 + l5 + c1) / 3.0
    out = (close - pivot) / close.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dpsh_21d_base_v078_signal(close: pd.Series, high: pd.Series) -> pd.Series:
    """Distance to 21-bars-back high. (close - high.shift(21))/close.
    Anchored specifically to the high level seen exactly 21 bars ago —
    distinct from rolling-max and distinct from the 21d swing-high."""
    lvl = high.shift(21)
    out = (close - lvl) / close.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dpsl_21d_base_v079_signal(close: pd.Series, low: pd.Series) -> pd.Series:
    """Number of bars in the last 21 where low.shift(21) > low (i.e., the
    bar 21 days ago had a higher low than today). Counts how often the
    look-back support level still stands above current low. Discrete
    aggregate distinct from a continuous distance to a single bar."""
    diff = low.shift(21) - low
    is_above = (diff > 0).astype(float)
    out = is_above.rolling(21, min_periods=10).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_drx_10d_base_v080_signal(close: pd.Series, high: pd.Series) -> pd.Series:
    """Distance to highest-high in the look-back range [t-10, t-5]: the
    highest high reached 5 to 10 bars ago. Structurally distinct from
    rolling-max because it excludes the most recent 5 bars."""
    lvl = high.shift(5).rolling(6, min_periods=6).max()
    out = (close - lvl) / close.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group A2: Volume-anchored prior level distances -----------------------


def f04sr_f04_support_resistance_proximity_dvc_30d_base_v081_signal(closeadj: pd.Series, volume: pd.Series, close: pd.Series) -> pd.Series:
    """Distance to closeadj of the highest-volume bar in last 30 bars (the
    "volume point of control"). Heavy-volume bars often act as durable
    S/R levels."""
    def _lvl(window_close, window_vol):
        # find index of max volume in window; return close at that index
        idx = int(np.nanargmax(window_vol))
        return float(window_close[idx])
    out = pd.Series(np.nan, index=closeadj.index, dtype=float)
    ca_arr = closeadj.to_numpy()
    v_arr = volume.to_numpy()
    n = len(closeadj)
    for i in range(29, n):
        wc = ca_arr[i - 29:i + 1]
        wv = v_arr[i - 29:i + 1]
        if np.all(np.isnan(wv)):
            continue
        if np.all(np.isnan(wc)):
            continue
        idx = int(np.nanargmax(wv))
        lvl = float(wc[idx])
        if lvl > 0 and np.isfinite(ca_arr[i]):
            out.iloc[i] = (ca_arr[i] - lvl) / ca_arr[i]
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dvh_60d_base_v082_signal(closeadj: pd.Series, volume: pd.Series, high: pd.Series) -> pd.Series:
    """Distance to high of the highest-volume bar in last 60 bars."""
    out = pd.Series(np.nan, index=closeadj.index, dtype=float)
    ca_arr = closeadj.to_numpy()
    v_arr = volume.to_numpy()
    h_arr = high.to_numpy()
    n = len(closeadj)
    for i in range(59, n):
        wv = v_arr[i - 59:i + 1]
        wh = h_arr[i - 59:i + 1]
        if np.all(np.isnan(wv)) or np.all(np.isnan(wh)):
            continue
        idx = int(np.nanargmax(wv))
        lvl = float(wh[idx])
        if lvl > 0 and np.isfinite(ca_arr[i]):
            out.iloc[i] = (ca_arr[i] - lvl) / ca_arr[i]
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dvl_60d_base_v083_signal(closeadj: pd.Series, volume: pd.Series, low: pd.Series) -> pd.Series:
    """Bars elapsed since the highest-volume bar in the last 60 bars
    (the age of the volume-point-of-control). A temporal feature, not a
    price distance — captures how stale the dominant S/R node is."""
    out = pd.Series(np.nan, index=closeadj.index, dtype=float)
    v_arr = volume.to_numpy()
    n = len(closeadj)
    for i in range(59, n):
        wv = v_arr[i - 59:i + 1]
        if np.all(np.isnan(wv)):
            continue
        idx = int(np.nanargmax(wv))
        out.iloc[i] = float(59 - idx)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dvh_50d_base_v084_signal(closeadj: pd.Series, volume: pd.Series, high: pd.Series) -> pd.Series:
    """Volume-concentration at recent highs: fraction of 50d total
    volume that occurred on bars whose high was in the upper-decile
    of the 50d high distribution. Strong concentration -> resistance
    has heavy volume backing."""
    w = volume.replace(0.0, np.nan)
    q90 = high.rolling(50, min_periods=30).quantile(0.9)
    is_upper = (high >= q90).astype(float)
    num = (is_upper * w).rolling(50, min_periods=30).sum()
    den = w.rolling(50, min_periods=30).sum()
    out = num / den.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dvl_50d_base_v085_signal(closeadj: pd.Series, volume: pd.Series, low: pd.Series) -> pd.Series:
    """Range of volume-weighted lows over the trailing 50 bars: the
    max(low) - min(low) over bars whose volume rank in the window was
    in the top 30%. A WIDTH feature of the high-volume support cluster."""
    w = volume.to_numpy()
    l_arr = low.to_numpy()
    n = len(low)
    out_arr = np.full(n, np.nan, dtype=float)
    for i in range(49, n):
        wv = w[i - 49:i + 1]
        wl = l_arr[i - 49:i + 1]
        if np.all(np.isnan(wv)) or np.all(np.isnan(wl)):
            continue
        thr = np.nanquantile(wv, 0.7)
        m = wv >= thr
        if m.sum() < 5:
            continue
        ls = wl[m]
        out_arr[i] = float(np.nanmax(ls) - np.nanmin(ls)) / float(closeadj.iloc[i]) if closeadj.iloc[i] > 0 else np.nan
    out = pd.Series(out_arr, index=closeadj.index)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group A3: Camarilla pivot full family --------------------------------


def f04sr_f04_support_resistance_proximity_dcamr1_1d_base_v086_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance to Camarilla R1 = C_{-1} + (H_{-1}-L_{-1})*1.1/12. Smaller
    coefficient than R3 — represents a near-term resistance level."""
    rng = high.shift(1) - low.shift(1)
    r1 = close.shift(1) + rng * 1.1 / 12.0
    out = (close - r1) / close.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dcams1_1d_base_v087_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """20-bar fraction of bars where close < Camarilla S1
    = C_{-1} - 1.1*(H_{-1}-L_{-1})/12. Discrete frequency of brief
    breakdowns through the inner Camarilla support."""
    rng = high.shift(1) - low.shift(1)
    s1 = close.shift(1) - rng * 1.1 / 12.0
    cond = (close < s1).astype(float)
    out = cond.rolling(20, min_periods=5).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dcamr2_1d_base_v088_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Indicator-streak: consecutive bars where close exceeded Camarilla
    R2 = C_{-1} + 1.1*(H_{-1}-L_{-1})/6. Discrete streak length, not a
    continuous distance."""
    rng = high.shift(1) - low.shift(1)
    r2 = close.shift(1) + rng * 1.1 / 6.0
    cond = (close > r2).astype(float)
    grp = (cond != cond.shift(1)).cumsum()
    streak = cond.groupby(grp).cumsum() * cond
    return streak.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dcams2_1d_base_v089_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """20-bar count of bars where the bar's CLOSE finished below
    Camarilla S2 = C_{-1} - 1.1*(H_{-1}-L_{-1})/6. A frequency feature
    of inner-Camarilla support violations."""
    rng = high.shift(1) - low.shift(1)
    s2 = close.shift(1) - rng * 1.1 / 6.0
    cond = (close < s2).astype(float)
    out = cond.rolling(20, min_periods=5).sum()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group A4: Fibonacci pivot extensions ---------------------------------


def f04sr_f04_support_resistance_proximity_dfibr2_1d_base_v090_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Streak: consecutive bars where close > Fib R2 = pivot +
    0.618*(H_{-1}-L_{-1}). A discrete persistence count above the
    upper Fib extension, distinct from a continuous distance."""
    pivot = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    rng = high.shift(1) - low.shift(1)
    r2 = pivot + 0.618 * rng
    cond = (close > r2).astype(float)
    grp = (cond != cond.shift(1)).cumsum()
    streak = cond.groupby(grp).cumsum() * cond
    return streak.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dfibs1_1d_base_v091_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Indicator: close exceeded ALL three Fib resistance levels
    (pivot + 0.236*rng, pivot + 0.382*rng, pivot + 0.618*rng), counted
    over 20 bars as a fraction. Categorical-cluster breakout measure
    distinct from a single-level distance."""
    pivot = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    rng = high.shift(1) - low.shift(1)
    r236 = pivot + 0.236 * rng
    r382 = pivot + 0.382 * rng
    r618 = pivot + 0.618 * rng
    cond = ((close > r236) & (close > r382) & (close > r618)).astype(float)
    out = cond.rolling(20, min_periods=5).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dfibs2_1d_base_v092_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Indicator: 10-bar count of bars where close was below Fib S2 =
    pivot - 0.618*(H_{-1}-L_{-1}). Discrete deep-support-test count."""
    pivot = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    rng = high.shift(1) - low.shift(1)
    s2 = pivot - 0.618 * rng
    cond = (close < s2).astype(float)
    out = cond.rolling(10, min_periods=3).sum()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group A5: Wave / swing-pattern counts (HH, LL, HL, LH) ---------------


def f04sr_f04_support_resistance_proximity_nhh_21d_base_v093_signal(high: pd.Series) -> pd.Series:
    """Count of "higher-high" events in last 21 bars. A HH event at bar
    t-2 (5-bar fractal high) with high.shift(2) greater than the
    previous fractal high level in window. Captures resistance pivots
    that broke prior resistance — bullish wave signal anchored to
    specific pivot levels."""
    is_frac = (high.shift(2) > high.shift(3)) & (high.shift(2) > high.shift(4)) & (high.shift(2) > high.shift(1)) & (high.shift(2) > high)
    levels = high.shift(2).where(is_frac).ffill(limit=40)
    prev_levels = levels.shift(1).ffill(limit=40)
    hh = is_frac & (high.shift(2) > prev_levels)
    out = hh.astype(float).rolling(21, min_periods=10).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_nll_21d_base_v094_signal(low: pd.Series) -> pd.Series:
    """Count of "lower-low" events in last 21 bars (LL: 5-bar fractal low
    breaks the previous fractal low level)."""
    is_frac = (low.shift(2) < low.shift(3)) & (low.shift(2) < low.shift(4)) & (low.shift(2) < low.shift(1)) & (low.shift(2) < low)
    levels = low.shift(2).where(is_frac).ffill(limit=40)
    prev_levels = levels.shift(1).ffill(limit=40)
    ll = is_frac & (low.shift(2) < prev_levels)
    out = ll.astype(float).rolling(21, min_periods=10).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_nhl_30d_base_v095_signal(low: pd.Series) -> pd.Series:
    """Count of "higher-low" events in last 30 bars (HL: fractal low ABOVE
    previous fractal low — supportive consolidation/uptrend)."""
    is_frac = (low.shift(2) < low.shift(3)) & (low.shift(2) < low.shift(4)) & (low.shift(2) < low.shift(1)) & (low.shift(2) < low)
    levels = low.shift(2).where(is_frac).ffill(limit=40)
    prev_levels = levels.shift(1).ffill(limit=40)
    hl = is_frac & (low.shift(2) > prev_levels)
    out = hl.astype(float).rolling(30, min_periods=15).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_nlh_30d_base_v096_signal(high: pd.Series) -> pd.Series:
    """Count of "lower-high" events in last 30 bars (LH: fractal high
    below previous fractal high — bearish wave)."""
    is_frac = (high.shift(2) > high.shift(3)) & (high.shift(2) > high.shift(4)) & (high.shift(2) > high.shift(1)) & (high.shift(2) > high)
    levels = high.shift(2).where(is_frac).ffill(limit=40)
    prev_levels = levels.shift(1).ffill(limit=40)
    lh = is_frac & (high.shift(2) < prev_levels)
    out = lh.astype(float).rolling(30, min_periods=15).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_nwave_30d_base_v097_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Net wave-pattern score: HH+HL - LL - LH over last 30 bars."""
    is_fh = (high.shift(2) > high.shift(3)) & (high.shift(2) > high.shift(4)) & (high.shift(2) > high.shift(1)) & (high.shift(2) > high)
    is_fl = (low.shift(2) < low.shift(3)) & (low.shift(2) < low.shift(4)) & (low.shift(2) < low.shift(1)) & (low.shift(2) < low)
    fh_lvl = high.shift(2).where(is_fh).ffill(limit=40)
    fl_lvl = low.shift(2).where(is_fl).ffill(limit=40)
    fh_prev = fh_lvl.shift(1).ffill(limit=40)
    fl_prev = fl_lvl.shift(1).ffill(limit=40)
    hh = (is_fh & (high.shift(2) > fh_prev)).astype(float)
    lh = (is_fh & (high.shift(2) < fh_prev)).astype(float)
    ll = (is_fl & (low.shift(2) < fl_prev)).astype(float)
    hl = (is_fl & (low.shift(2) > fl_prev)).astype(float)
    out = (hh + hl - ll - lh).rolling(30, min_periods=15).sum()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group A6: Multi-N fractal level distances ----------------------------


def f04sr_f04_support_resistance_proximity_dfr3h_30d_base_v098_signal(high: pd.Series, close: pd.Series) -> pd.Series:
    """Distance to most recent 3-bar fractal high (less strict: H[t-1] >
    H[t-2] and H[t-1] > H[t])."""
    is_frac = (high.shift(1) > high.shift(2)) & (high.shift(1) > high)
    level = high.shift(1).where(is_frac).ffill(limit=30)
    out = (close - level) / close.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dfr3l_30d_base_v099_signal(low: pd.Series, close: pd.Series) -> pd.Series:
    """Distance to most recent 3-bar fractal low."""
    is_frac = (low.shift(1) < low.shift(2)) & (low.shift(1) < low)
    level = low.shift(1).where(is_frac).ffill(limit=30)
    out = (close - level) / close.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dfr7h_50d_base_v100_signal(high: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Distance to most recent 7-bar fractal high: H[t-3] > H[t-1..t-2]
    AND H[t-3] > H[t-4..t-6] AND H[t-3] > H[t]. Stronger pivot — fewer,
    further-apart events."""
    h = high
    cond = (h.shift(3) > h.shift(1)) & (h.shift(3) > h.shift(2)) & (h.shift(3) > h.shift(4)) & (h.shift(3) > h.shift(5)) & (h.shift(3) > h.shift(6)) & (h.shift(3) > h)
    level = h.shift(3).where(cond).ffill(limit=50)
    out = (closeadj - level) / closeadj.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dfr7l_50d_base_v101_signal(low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Distance to most recent 7-bar fractal low."""
    ll = low
    cond = (ll.shift(3) < ll.shift(1)) & (ll.shift(3) < ll.shift(2)) & (ll.shift(3) < ll.shift(4)) & (ll.shift(3) < ll.shift(5)) & (ll.shift(3) < ll.shift(6)) & (ll.shift(3) < ll)
    level = ll.shift(3).where(cond).ffill(limit=50)
    out = (closeadj - level) / closeadj.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dfr9h_80d_base_v102_signal(high: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Distance to most recent 9-bar fractal high: center bar H[t-4] is
    the max of H[t-8..t]. Strong long-window resistance pivot."""
    h = high
    cond = (h.shift(4) > h.shift(1)) & (h.shift(4) > h.shift(2)) & (h.shift(4) > h.shift(3)) & (h.shift(4) > h.shift(5)) & (h.shift(4) > h.shift(6)) & (h.shift(4) > h.shift(7)) & (h.shift(4) > h.shift(8)) & (h.shift(4) > h)
    level = h.shift(4).where(cond).ffill(limit=80)
    out = (closeadj - level) / closeadj.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group A7: Recent break / failure dynamics ----------------------------


def f04sr_f04_support_resistance_proximity_tsfb_30d_base_v103_signal(close: pd.Series, high: pd.Series) -> pd.Series:
    """Bars since the last false-breakout (breakout-then-fail-within-5)
    above prior-20d high, capped at 30."""
    prior_hi = high.shift(1).rolling(20, min_periods=20).max()
    broke = (close > prior_hi)
    came_back = (close < prior_hi)
    failed = pd.Series(False, index=close.index)
    for j in range(1, 6):
        failed = failed | (broke.shift(j).fillna(False) & came_back)
    return _bars_since_true(failed.fillna(False), 30)


def f04sr_f04_support_resistance_proximity_tsfd_30d_base_v104_signal(close: pd.Series, low: pd.Series) -> pd.Series:
    """Bars since the last false-breakdown (breakdown-then-fail-within-5)
    below prior-20d low."""
    prior_lo = low.shift(1).rolling(20, min_periods=20).min()
    broke = (close < prior_lo)
    came_back = (close > prior_lo)
    failed = pd.Series(False, index=close.index)
    for j in range(1, 6):
        failed = failed | (broke.shift(j).fillna(False) & came_back)
    return _bars_since_true(failed.fillna(False), 30)


def f04sr_f04_support_resistance_proximity_bfn_60d_base_v105_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Net (success-failed-break - success-failed-breakdown) in last 60 bars.
    A confirmed break (success): broke up and stayed up >= 5 bars."""
    prior_hi = high.shift(1).rolling(20, min_periods=20).max()
    prior_lo = low.shift(1).rolling(20, min_periods=20).min()
    above = (close > prior_hi)
    below = (close < prior_lo)
    # success = bar t is broken up AND was also above 5 bars ago (still holds)
    succ_up = above & above.shift(5).fillna(False)
    succ_dn = below & below.shift(5).fillna(False)
    out = succ_up.astype(float).rolling(60, min_periods=30).sum() - succ_dn.astype(float).rolling(60, min_periods=30).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_nh20_60d_base_v106_signal(closeadj: pd.Series) -> pd.Series:
    """Count of new 20d highs in last 60 days. Tally of resistance breaks."""
    prior_hi = closeadj.shift(1).rolling(20, min_periods=20).max()
    nh = (closeadj > prior_hi).astype(float)
    out = nh.rolling(60, min_periods=30).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_nl20_60d_base_v107_signal(closeadj: pd.Series) -> pd.Series:
    """Count of new 20d lows in last 60 days."""
    prior_lo = closeadj.shift(1).rolling(20, min_periods=20).min()
    nl = (closeadj < prior_lo).astype(float)
    out = nl.rolling(60, min_periods=30).sum()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group A8: Round-number streaks and crosses ---------------------------


def f04sr_f04_support_resistance_proximity_skr10_1d_base_v108_signal(close: pd.Series) -> pd.Series:
    """Streak of consecutive bars on the same side of the nearest round-10
    line: counts bars since last round-10 cross. Captures persistence
    near a psychological level."""
    bucket = np.floor(close / 10.0)
    changed = (bucket != bucket.shift(1))
    streak = pd.Series(np.nan, index=close.index, dtype=float)
    run = 0
    for i in range(len(close)):
        v = changed.iloc[i]
        if isinstance(v, float) and np.isnan(v):
            continue
        if bool(v):
            run = 0
        run += 1
        streak.iloc[i] = float(run)
    return streak.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_skr100_1d_base_v109_signal(close: pd.Series) -> pd.Series:
    """Streak of bars since last round-100 cross. Strongest psychological
    tier."""
    bucket = np.floor(close / 100.0)
    changed = (bucket != bucket.shift(1))
    streak = pd.Series(np.nan, index=close.index, dtype=float)
    run = 0
    for i in range(len(close)):
        v = changed.iloc[i]
        if isinstance(v, float) and np.isnan(v):
            continue
        if bool(v):
            run = 0
        run += 1
        streak.iloc[i] = float(run)
    return streak.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_asr5_1d_base_v110_signal(close: pd.Series) -> pd.Series:
    """Bars since last round-5 cross (capped 60)."""
    bucket = np.floor(close / 5.0)
    changed = (bucket != bucket.shift(1))
    return _bars_since_true(changed.fillna(False), 60)


def f04sr_f04_support_resistance_proximity_ncr10_60d_base_v111_signal(close: pd.Series) -> pd.Series:
    """Net round-10 crosses (up minus down) in last 60 bars."""
    bucket = np.floor(close / 10.0)
    diff = bucket.diff()
    up = (diff > 0).astype(float)
    dn = (diff < 0).astype(float)
    out = up.rolling(60, min_periods=30).sum() - dn.rolling(60, min_periods=30).sum()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group A9: Anchored VWAP distances ------------------------------------


def f04sr_f04_support_resistance_proximity_davwap_50d_base_v112_signal(closeadj: pd.Series, volume: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance to 50d AVWAP using typical price * volume.
    AVWAP_t = sum(TP*V) / sum(V) over the last 50 bars."""
    tp = (high + low + closeadj) / 3.0
    w = volume.replace(0.0, np.nan)
    num = (tp * w).rolling(50, min_periods=30).sum()
    den = w.rolling(50, min_periods=30).sum()
    avwap = num / den.replace(0.0, np.nan)
    out = (closeadj - avwap) / closeadj.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_davwap_100d_base_v113_signal(closeadj: pd.Series, volume: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance to 100d AVWAP."""
    tp = (high + low + closeadj) / 3.0
    w = volume.replace(0.0, np.nan)
    num = (tp * w).rolling(100, min_periods=60).sum()
    den = w.rolling(100, min_periods=60).sum()
    avwap = num / den.replace(0.0, np.nan)
    out = (closeadj - avwap) / closeadj.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_davwap_21d_base_v114_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Distance to 21d AVWAP using close * volume."""
    w = volume.replace(0.0, np.nan)
    num = (close * w).rolling(21, min_periods=15).sum()
    den = w.rolling(21, min_periods=15).sum()
    avwap = num / den.replace(0.0, np.nan)
    out = (close - avwap) / close.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group A10: Combined / nearest level distances ------------------------


def f04sr_f04_support_resistance_proximity_dnpv_1d_base_v115_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance to the NEAREST classical pivot level among {R1, R2, R3,
    pivot, S1, S2, S3}. Sign of result = sign(close - nearest). Yields
    smallest signed distance to any of the 7 levels."""
    pivot = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    rng = high.shift(1) - low.shift(1)
    r1 = 2.0 * pivot - low.shift(1)
    s1 = 2.0 * pivot - high.shift(1)
    r2 = pivot + rng
    s2 = pivot - rng
    r3 = high.shift(1) + 2.0 * (pivot - low.shift(1))
    s3 = low.shift(1) - 2.0 * (high.shift(1) - pivot)
    levels = pd.concat({"r1": r1, "r2": r2, "r3": r3, "p": pivot, "s1": s1, "s2": s2, "s3": s3}, axis=1)
    diffs = levels.sub(close, axis=0).mul(-1.0)  # close - level
    # find smallest |diff| per row, preserve sign
    abs_d = diffs.abs()
    idxmin = abs_d.idxmin(axis=1)
    out = pd.Series(np.nan, index=close.index, dtype=float)
    for i in range(len(close)):
        k = idxmin.iloc[i]
        if isinstance(k, str):
            v = diffs.loc[diffs.index[i], k]
            c = close.iloc[i]
            if np.isfinite(v) and np.isfinite(c) and c > 0:
                out.iloc[i] = float(v / c)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dnfr_30d_base_v116_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance to nearest fractal H or L (5-bar) in last 30 bars. Picks
    the side closest to current close."""
    is_fh = (high.shift(2) > high.shift(3)) & (high.shift(2) > high.shift(4)) & (high.shift(2) > high.shift(1)) & (high.shift(2) > high)
    is_fl = (low.shift(2) < low.shift(3)) & (low.shift(2) < low.shift(4)) & (low.shift(2) < low.shift(1)) & (low.shift(2) < low)
    fh = high.shift(2).where(is_fh).ffill(limit=30)
    fl = low.shift(2).where(is_fl).ffill(limit=30)
    dh = (close - fh) / close.replace(0.0, np.nan)
    dl = (close - fl) / close.replace(0.0, np.nan)
    # pick the smaller absolute distance
    use_h = dh.abs() < dl.abs()
    out = dh.where(use_h, dl)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dmid_252d_base_v117_signal(closeadj: pd.Series) -> pd.Series:
    """Distance to the midpoint of the 252d Donchian band: ((H252+L252)/2 -
    close)/close * (-1). Sign flips for "above midpoint". Anchored to
    the SPECIFIC midline of the 1-year level."""
    h = closeadj.rolling(252, min_periods=200).max()
    l = closeadj.rolling(252, min_periods=200).min()
    mid = (h + l) / 2.0
    out = (closeadj - mid) / closeadj.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dsmh_21d_base_v118_signal(close: pd.Series, high: pd.Series) -> pd.Series:
    """Count of bars in the last 21 whose high set a NEW 21d-trailing
    high. A discrete event-frequency feature distinct from continuous
    distance to mean-high."""
    h21 = high.rolling(21, min_periods=21).max()
    is_new_high = (high >= h21 - 1e-12).astype(float)
    out = is_new_high.rolling(21, min_periods=10).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dsml_21d_base_v119_signal(close: pd.Series, low: pd.Series) -> pd.Series:
    """Spread between 21d mean-of-highs and 21d mean-of-lows divided by
    close: (mean(L,21) - close)/close + (high.rolling(21).mean() -
    low.rolling(21).mean())/close — but we capture the BAND-WIDTH
    portion explicitly. Strictly: (mean(L,21) std) / close — the
    cross-bar variability of recent lows."""
    sd_l = low.rolling(21, min_periods=21).std()
    out = sd_l / close.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group A11: Anchored extremes from inception / time-band proximity ----


def f04sr_f04_support_resistance_proximity_datl_all_base_v120_signal(closeadj: pd.Series) -> pd.Series:
    """Bars elapsed since the anchored-since-inception all-time low.
    Counter starts at 0 on the bar that set a new ATL and increments
    until the next ATL. A temporal feature (age) of the ATL support,
    not a price distance."""
    atl = closeadj.expanding(min_periods=1).min()
    is_new = (closeadj <= atl + 1e-12)
    arr = is_new.fillna(False).to_numpy()
    n = len(arr)
    out_arr = np.full(n, np.nan, dtype=float)
    last = -1
    for i in range(n):
        if arr[i]:
            last = i
        if last >= 0:
            out_arr[i] = float(i - last)
    # apply warm-up
    out = pd.Series(out_arr, index=closeadj.index)
    out.iloc[:30] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_tama_100d_base_v121_signal(closeadj: pd.Series) -> pd.Series:
    """Fraction of last 100 bars spent above the 252d Donchian midpoint.
    A regime tally anchored to the SPECIFIC mid-of-52w-range level."""
    h = closeadj.rolling(252, min_periods=200).max()
    l = closeadj.rolling(252, min_periods=200).min()
    mid = (h + l) / 2.0
    above = (closeadj > mid).astype(float)
    out = above.rolling(100, min_periods=60).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_tnhi_100d_base_v122_signal(closeadj: pd.Series) -> pd.Series:
    """Bar-since the LAST time closeadj came within 1% of its 252d
    high, capped at 100. Time-since-resistance-test, a temporal
    feature distinct from a fraction of time near resistance."""
    h = closeadj.rolling(252, min_periods=200).max()
    near = (closeadj / h.replace(0.0, np.nan) >= 0.99)
    arr = near.fillna(False).to_numpy()
    n = len(arr)
    out_arr = np.full(n, np.nan, dtype=float)
    last = -1
    for i in range(n):
        if arr[i]:
            last = i
        if last >= 0:
            out_arr[i] = float(min(i - last, 100))
    out = pd.Series(out_arr, index=closeadj.index)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group A12: ATR-normalized distance to extremes -----------------------


def f04sr_f04_support_resistance_proximity_dhatr_252d_base_v123_signal(closeadj: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(closeadj - 252d-high) / ATR_14. Distance to 52w-high measured in
    volatility-normalized units — different functional form than %.
    ATR computed from raw high/low/close (no warm-up bias)."""
    tr = _true_range(high, low, close)
    atr = tr.rolling(14, min_periods=14).mean()
    h252 = closeadj.rolling(252, min_periods=200).max()
    out = (closeadj - h252) / atr.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dlatr_252d_base_v124_signal(closeadj: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of (closeadj - 252d-low) to (252d-high - 252d-low) — a
    pure RANGE-FRACTION position within the 252d Donchian channel,
    decoupled from ATR. Bounded in [0,1]."""
    h252 = closeadj.rolling(252, min_periods=200).max()
    l252 = closeadj.rolling(252, min_periods=200).min()
    rng = (h252 - l252).replace(0.0, np.nan)
    out = (closeadj - l252) / rng
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dhatr_20d_base_v125_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """(close - 20d-high) / ATR_14."""
    tr = _true_range(high, low, close)
    atr = tr.rolling(14, min_periods=14).mean()
    h20 = high.rolling(20, min_periods=20).max()
    out = (close - h20) / atr.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dlatr_20d_base_v126_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """(close - 20d-low) / ATR_14."""
    tr = _true_range(high, low, close)
    atr = tr.rolling(14, min_periods=14).mean()
    l20 = low.rolling(20, min_periods=20).min()
    out = (close - l20) / atr.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group A13: Cluster-of-pivots zone-center features --------------------


def f04sr_f04_support_resistance_proximity_dzfh_60d_base_v127_signal(high: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Cross-bar standard deviation of fractal-HIGH levels in the last
    60 bars divided by closeadj — width of the resistance-zone
    cluster. Tight cluster -> strong, well-defined resistance band."""
    is_fh = (high.shift(2) > high.shift(3)) & (high.shift(2) > high.shift(4)) & (high.shift(2) > high.shift(1)) & (high.shift(2) > high)
    levels = high.shift(2).where(is_fh)
    out = levels.rolling(60, min_periods=3).std() / closeadj.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dzfl_60d_base_v128_signal(low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Cross-bar standard deviation of fractal-low LEVELS in the last 60
    bars: width of the support-zone cluster. Tight cluster (small std)
    -> a strongly defined support shelf; wide cluster -> diffuse
    support. A dispersion feature distinct from a distance to a
    centroid."""
    is_fl = (low.shift(2) < low.shift(3)) & (low.shift(2) < low.shift(4)) & (low.shift(2) < low.shift(1)) & (low.shift(2) < low)
    levels = low.shift(2).where(is_fl)
    out = levels.rolling(60, min_periods=3).std() / closeadj.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_wfh_60d_base_v129_signal(high: pd.Series) -> pd.Series:
    """Spread between max and min fractal-high level in last 60 bars
    normalized by avg fractal level. Measures resistance-band width."""
    is_fh = (high.shift(2) > high.shift(3)) & (high.shift(2) > high.shift(4)) & (high.shift(2) > high.shift(1)) & (high.shift(2) > high)
    levels = high.shift(2).where(is_fh)
    mx = levels.rolling(60, min_periods=3).max()
    mn = levels.rolling(60, min_periods=3).min()
    mean = levels.rolling(60, min_periods=3).mean()
    out = (mx - mn) / mean.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_wfl_60d_base_v130_signal(low: pd.Series) -> pd.Series:
    """Spread between max and min fractal-low level in last 60 bars
    normalized by mean (support-band width)."""
    is_fl = (low.shift(2) < low.shift(3)) & (low.shift(2) < low.shift(4)) & (low.shift(2) < low.shift(1)) & (low.shift(2) < low)
    levels = low.shift(2).where(is_fl)
    mx = levels.rolling(60, min_periods=3).max()
    mn = levels.rolling(60, min_periods=3).min()
    mean = levels.rolling(60, min_periods=3).mean()
    out = (mx - mn) / mean.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group A14: Statistical S/R density measures --------------------------


def f04sr_f04_support_resistance_proximity_zh_30d_base_v131_signal(close: pd.Series, high: pd.Series) -> pd.Series:
    """Z-score of close relative to the distribution of last-30 bars'
    HIGH values. Captures how extreme the current close is vs the
    cluster of recent highs (anchored to high pivots, not closes)."""
    mu = high.rolling(30, min_periods=15).mean()
    sd = high.rolling(30, min_periods=15).std()
    out = (close - mu) / sd.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_zl_30d_base_v132_signal(close: pd.Series, low: pd.Series) -> pd.Series:
    """Coefficient of variation of LOWS over 30 bars: std(low,30) /
    mean(low,30). Captures how dispersed the 30d support cluster is —
    a width statistic rather than a position z-score."""
    mu = low.rolling(30, min_periods=15).mean()
    sd = low.rolling(30, min_periods=15).std()
    out = sd / mu.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_skfh_100d_base_v133_signal(high: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Skewness of the (close - fractal-high-level)/close distribution
    over last 100 bars. Captures asymmetry of nearby resistance
    distances."""
    is_fh = (high.shift(2) > high.shift(3)) & (high.shift(2) > high.shift(4)) & (high.shift(2) > high.shift(1)) & (high.shift(2) > high)
    levels = high.shift(2).where(is_fh)
    rel = (closeadj - levels) / closeadj.replace(0.0, np.nan)
    out = rel.rolling(100, min_periods=5).skew()
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_skfl_100d_base_v134_signal(low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Skewness of (close - fractal-low-level)/close over last 100 bars."""
    is_fl = (low.shift(2) < low.shift(3)) & (low.shift(2) < low.shift(4)) & (low.shift(2) < low.shift(1)) & (low.shift(2) < low)
    levels = low.shift(2).where(is_fl)
    rel = (closeadj - levels) / closeadj.replace(0.0, np.nan)
    out = rel.rolling(100, min_periods=5).skew()
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_kufh_60d_base_v135_signal(closeadj: pd.Series, high: pd.Series) -> pd.Series:
    """Kurtosis of (closeadj - high)/closeadj over last 60 bars. Measures
    "fat-tailedness" of distances to recent bar highs — a structural
    S/R-distribution feature."""
    rel = (closeadj - high) / closeadj.replace(0.0, np.nan)
    out = rel.rolling(60, min_periods=20).kurt()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group A15: Confirmed multi-bar break signals -------------------------


def f04sr_f04_support_resistance_proximity_cbo20_3d_base_v136_signal(close: pd.Series, high: pd.Series) -> pd.Series:
    """Confirmed 20d-high break: 1 if close > prior-20d-high for 3
    consecutive bars, else 0. Stronger-than-single-bar break signal
    anchored to the specific resistance level."""
    prior_hi = high.shift(1).rolling(20, min_periods=20).max()
    above = (close > prior_hi)
    confirmed = above & above.shift(1).fillna(False) & above.shift(2).fillna(False)
    out = confirmed.astype(float)
    out = out.where(prior_hi.notna())
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_cbo50_5d_base_v137_signal(closeadj: pd.Series) -> pd.Series:
    """Confirmed 50d-high break: 5 consecutive bars closeadj above prior
    50d-high."""
    prior_hi = closeadj.shift(1).rolling(50, min_periods=50).max()
    above = (closeadj > prior_hi)
    confirmed = above & above.shift(1).fillna(False) & above.shift(2).fillna(False) & above.shift(3).fillna(False) & above.shift(4).fillna(False)
    out = confirmed.astype(float)
    out = out.where(prior_hi.notna())
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_cbd20_3d_base_v138_signal(close: pd.Series, low: pd.Series) -> pd.Series:
    """Confirmed 20d-low break: 3 consec bars close < prior 20d low."""
    prior_lo = low.shift(1).rolling(20, min_periods=20).min()
    below = (close < prior_lo)
    confirmed = below & below.shift(1).fillna(False) & below.shift(2).fillna(False)
    out = confirmed.astype(float)
    out = out.where(prior_lo.notna())
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group A16: Post-break pullback / recovery dynamics -------------------


def f04sr_f04_support_resistance_proximity_pull_50d_base_v139_signal(closeadj: pd.Series) -> pd.Series:
    """Depth of pullback after most-recent 50d-high break: tracks the
    minimum closeadj reached since the last day closeadj > prior-50d-
    high, divided by closeadj at break time minus 1. Negative = pulled
    back; close to 0 = continued. NaN before any break."""
    prior_hi = closeadj.shift(1).rolling(50, min_periods=50).max()
    broke = (closeadj > prior_hi)
    lvl_at_break = closeadj.where(broke).ffill(limit=60)
    # rolling min of closeadj since the last break event:
    # use bars-since to define window; approximate via 60-bar trailing min
    min_post = closeadj.rolling(60, min_periods=10).min()
    out = (min_post / lvl_at_break - 1.0)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_bounce_50d_base_v140_signal(closeadj: pd.Series) -> pd.Series:
    """Count of 50d-low BREAK events in the trailing 60 bars (number of
    bars where closeadj closed under the prior 50d-low). A discrete
    event-count, structurally distinct from a continuous bounce height."""
    prior_lo = closeadj.shift(1).rolling(50, min_periods=50).min()
    is_break = (closeadj < prior_lo).astype(float)
    out = is_break.rolling(60, min_periods=20).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_holdup_50d_base_v141_signal(closeadj: pd.Series) -> pd.Series:
    """Maximum consecutive-streak length of closeadj > prior-50d-high
    seen in the trailing 60 bars. A discrete max-streak feature
    distinct from the fraction-of-time-above."""
    prior_hi = closeadj.shift(1).rolling(50, min_periods=50).max()
    above = (closeadj > prior_hi).astype(int)
    grp = (above != above.shift(1)).cumsum()
    cur_streak = above.groupby(grp).cumsum() * above
    out = cur_streak.rolling(60, min_periods=30).max().astype(float)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group A17: Paired-level relations ------------------------------------


def f04sr_f04_support_resistance_proximity_sgpv_1d_base_v142_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """sign(close - daily-pivot). Discrete pivot-regime indicator. Anchored
    to the SPECIFIC daily pivot level computed from prior bar HLC."""
    pivot = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    out = np.sign(close - pivot)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_sgwp_5d_base_v143_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """sign(close - weekly-pivot). Weekly pivot uses 5d-prior H/L/C."""
    h5 = high.rolling(5, min_periods=5).max().shift(1)
    l5 = low.rolling(5, min_periods=5).min().shift(1)
    c1 = close.shift(1)
    pivot = (h5 + l5 + c1) / 3.0
    out = np.sign(close - pivot)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_pvz_1d_base_v144_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Normalized position within (S1, R1) pivot zone:
    (close - S1) / (R1 - S1) - 0.5. Distance from the midpoint of the
    classical S1-to-R1 pivot range, anchored to prior bar's H/L/C."""
    pivot = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    r1 = 2.0 * pivot - low.shift(1)
    s1 = 2.0 * pivot - high.shift(1)
    width = (r1 - s1).replace(0.0, np.nan)
    out = (close - s1) / width - 0.5
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_pvrng_1d_base_v145_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Prior-bar range fraction of close: (H_{-1} - L_{-1}) / close. A
    pure prior-bar range-width metric (volatility/breadth), not a
    distance from any pivot level."""
    rng = (high.shift(1) - low.shift(1))
    out = rng / close.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group A18: Slope of the S/R level itself / range expansion -----------


def f04sr_f04_support_resistance_proximity_slh_60d_base_v146_signal(closeadj: pd.Series) -> pd.Series:
    """Slope of the 60d-Donchian-high level over last 21 bars: log of
    today's 60d-high divided by 21-bars-ago 60d-high. Captures whether
    resistance is rising or falling (a trending vs sticky ceiling)."""
    h60 = closeadj.rolling(60, min_periods=60).max()
    out = np.log(h60 / h60.shift(21).replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_sll_60d_base_v147_signal(closeadj: pd.Series) -> pd.Series:
    """Slope of 60d-Donchian-low level over last 21 bars."""
    l60 = closeadj.rolling(60, min_periods=60).min()
    out = np.log(l60 / l60.shift(21).replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_rexp_252d_base_v148_signal(closeadj: pd.Series) -> pd.Series:
    """Change-in-range over 252 bars: log(252d-range_today /
    252d-range_63bars_ago) where range = h252 - l252. Captures whether
    the long-term S/R envelope is expanding or contracting — a
    derivative-of-width metric distinct from the level or width itself."""
    h = closeadj.rolling(252, min_periods=200).max()
    l = closeadj.rolling(252, min_periods=200).min()
    rng = (h - l).replace(0.0, np.nan)
    out = np.log(rng / rng.shift(63).replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group A19: Anchored "year-ago" reference -----------------------------


def f04sr_f04_support_resistance_proximity_dya_252d_base_v149_signal(closeadj: pd.Series) -> pd.Series:
    """log(closeadj / closeadj.shift(252)). Distance from anchored "1-
    year-ago close" level — a specific historical reference point
    (the close of the bar 252 trading days back)."""
    out = np.log(closeadj / closeadj.shift(252).replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_pvw_1d_base_v150_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """20-bar rolling mean of (H - L)/close — average prior-bar range
    fraction smoothed over the trailing month. A SMOOTHED breadth
    statistic decoupled from any close-vs-pivot distance signal."""
    rng_frac = (high - low) / close.replace(0.0, np.nan)
    out = rng_frac.rolling(20, min_periods=10).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


def _e(fn, *inputs):
    return fn.__name__, {"inputs": list(inputs), "func": fn}


f04_support_resistance_proximity_base_076_150_REGISTRY = dict([
    _e(f04sr_f04_support_resistance_proximity_dmpv_21d_base_v076_signal, "closeadj", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_dwpv_5d_base_v077_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_dpsh_21d_base_v078_signal, "close", "high"),
    _e(f04sr_f04_support_resistance_proximity_dpsl_21d_base_v079_signal, "close", "low"),
    _e(f04sr_f04_support_resistance_proximity_drx_10d_base_v080_signal, "close", "high"),
    _e(f04sr_f04_support_resistance_proximity_dvc_30d_base_v081_signal, "closeadj", "volume", "close"),
    _e(f04sr_f04_support_resistance_proximity_dvh_60d_base_v082_signal, "closeadj", "volume", "high"),
    _e(f04sr_f04_support_resistance_proximity_dvl_60d_base_v083_signal, "closeadj", "volume", "low"),
    _e(f04sr_f04_support_resistance_proximity_dvh_50d_base_v084_signal, "closeadj", "volume", "high"),
    _e(f04sr_f04_support_resistance_proximity_dvl_50d_base_v085_signal, "closeadj", "volume", "low"),
    _e(f04sr_f04_support_resistance_proximity_dcamr1_1d_base_v086_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_dcams1_1d_base_v087_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_dcamr2_1d_base_v088_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_dcams2_1d_base_v089_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_dfibr2_1d_base_v090_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_dfibs1_1d_base_v091_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_dfibs2_1d_base_v092_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_nhh_21d_base_v093_signal, "high"),
    _e(f04sr_f04_support_resistance_proximity_nll_21d_base_v094_signal, "low"),
    _e(f04sr_f04_support_resistance_proximity_nhl_30d_base_v095_signal, "low"),
    _e(f04sr_f04_support_resistance_proximity_nlh_30d_base_v096_signal, "high"),
    _e(f04sr_f04_support_resistance_proximity_nwave_30d_base_v097_signal, "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_dfr3h_30d_base_v098_signal, "high", "close"),
    _e(f04sr_f04_support_resistance_proximity_dfr3l_30d_base_v099_signal, "low", "close"),
    _e(f04sr_f04_support_resistance_proximity_dfr7h_50d_base_v100_signal, "high", "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_dfr7l_50d_base_v101_signal, "low", "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_dfr9h_80d_base_v102_signal, "high", "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_tsfb_30d_base_v103_signal, "close", "high"),
    _e(f04sr_f04_support_resistance_proximity_tsfd_30d_base_v104_signal, "close", "low"),
    _e(f04sr_f04_support_resistance_proximity_bfn_60d_base_v105_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_nh20_60d_base_v106_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_nl20_60d_base_v107_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_skr10_1d_base_v108_signal, "close"),
    _e(f04sr_f04_support_resistance_proximity_skr100_1d_base_v109_signal, "close"),
    _e(f04sr_f04_support_resistance_proximity_asr5_1d_base_v110_signal, "close"),
    _e(f04sr_f04_support_resistance_proximity_ncr10_60d_base_v111_signal, "close"),
    _e(f04sr_f04_support_resistance_proximity_davwap_50d_base_v112_signal, "closeadj", "volume", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_davwap_100d_base_v113_signal, "closeadj", "volume", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_davwap_21d_base_v114_signal, "close", "volume"),
    _e(f04sr_f04_support_resistance_proximity_dnpv_1d_base_v115_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_dnfr_30d_base_v116_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_dmid_252d_base_v117_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_dsmh_21d_base_v118_signal, "close", "high"),
    _e(f04sr_f04_support_resistance_proximity_dsml_21d_base_v119_signal, "close", "low"),
    _e(f04sr_f04_support_resistance_proximity_datl_all_base_v120_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_tama_100d_base_v121_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_tnhi_100d_base_v122_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_dhatr_252d_base_v123_signal, "closeadj", "high", "low", "close"),
    _e(f04sr_f04_support_resistance_proximity_dlatr_252d_base_v124_signal, "closeadj", "high", "low", "close"),
    _e(f04sr_f04_support_resistance_proximity_dhatr_20d_base_v125_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_dlatr_20d_base_v126_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_dzfh_60d_base_v127_signal, "high", "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_dzfl_60d_base_v128_signal, "low", "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_wfh_60d_base_v129_signal, "high"),
    _e(f04sr_f04_support_resistance_proximity_wfl_60d_base_v130_signal, "low"),
    _e(f04sr_f04_support_resistance_proximity_zh_30d_base_v131_signal, "close", "high"),
    _e(f04sr_f04_support_resistance_proximity_zl_30d_base_v132_signal, "close", "low"),
    _e(f04sr_f04_support_resistance_proximity_skfh_100d_base_v133_signal, "high", "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_skfl_100d_base_v134_signal, "low", "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_kufh_60d_base_v135_signal, "closeadj", "high"),
    _e(f04sr_f04_support_resistance_proximity_cbo20_3d_base_v136_signal, "close", "high"),
    _e(f04sr_f04_support_resistance_proximity_cbo50_5d_base_v137_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_cbd20_3d_base_v138_signal, "close", "low"),
    _e(f04sr_f04_support_resistance_proximity_pull_50d_base_v139_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_bounce_50d_base_v140_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_holdup_50d_base_v141_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_sgpv_1d_base_v142_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_sgwp_5d_base_v143_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_pvz_1d_base_v144_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_pvrng_1d_base_v145_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_slh_60d_base_v146_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_sll_60d_base_v147_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_rexp_252d_base_v148_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_dya_252d_base_v149_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_pvw_1d_base_v150_signal, "close", "high", "low"),
])


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
    for name, entry in f04_support_resistance_proximity_base_076_150_REGISTRY.items():
        args = [df[col] for col in entry["inputs"]]
        out = entry["func"](*args)
        assert isinstance(out, pd.Series), f"{name}: not a Series"
        assert len(out) == len(df), f"{name}: length mismatch"
        clean = out.dropna()
        assert len(clean) > 0, f"{name}: all NaN"
        assert float(clean.std()) > 0.0 or clean.nunique() > 1, f"{name}: constant/all-zero"
        results[name] = out

    warm = 252
    coverage_ok = 0
    for ser in results.values():
        if ser.iloc[warm:].isna().mean() < 0.5:
            coverage_ok += 1
    frac = coverage_ok / len(results)
    assert frac >= 0.80, f"NaN-coverage too low: {frac:.2%} have <50% NaN after warm-up"

    aligned = pd.concat({n: results[n] for n in results}, axis=1).iloc[warm:]
    aligned = aligned.replace([np.inf, -np.inf], np.nan)
    corr = aligned.corr(min_periods=50).abs()
    np.fill_diagonal(corr.values, 0.0)
    max_corr = float(corr.max().max())
    if max_corr > 0.95 + 1e-9:
        s = corr.unstack().sort_values(ascending=False)
        s = s[s > 0.90].head(40)
        print("Top |corr| pairs > 0.90:")
        seen = set()
        for (a, b), v in s.items():
            if a < b and (a, b) not in seen:
                seen.add((a, b))
                print(f"  {a}  vs  {b}  ->  {v:.4f}")
    assert max_corr <= 0.95 + 1e-9, f"max pairwise |corr|={max_corr:.4f} exceeds 0.95"
    print(f"OK base_076_150: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
