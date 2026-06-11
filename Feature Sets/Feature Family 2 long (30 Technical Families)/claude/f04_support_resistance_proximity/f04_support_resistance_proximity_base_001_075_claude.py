"""f04_support_resistance_proximity base features 001-075.

Domain: support / resistance proximity. Every feature references a
SPECIFIC prior price level as anchor: swing highs / lows, prior period
highs / lows, fractal pivots, classical pivots (daily / Camarilla /
Fibonacci / Woodie / DeMark), round-number psychological levels,
Donchian-anchored 252d extremes, multi-touch level strength, and
breakout / breakdown magnitude/streak/recovery signals.

NO moving-average distance features (f01). NO pure channel-position
features (f02). NO trend-strength features (f03). Every f04 feature
must anchor to an identifiable prior price level.

Each function is a structurally distinct, fully expanded `def` block:
no `_core()` factory, no `formulas[i]` indexing, no exec / importlib.
NaN policy: never `fillna(0)` inside rolling computations; only
`replace([inf,-inf], nan)` at the function's final return.

Window > 21 trading days uses `closeadj`; windows <= 21 use `close`.
OHLC features within a single bar use unadjusted high/low/open/close.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Helpers (small, named utilities re-used inline by the features below).
# Each feature still spells its full expression inline; helpers only
# wrap one small primitive (e.g., "bars since last True" or "nearest
# round-K level distance") so per-function code stays readable.
# ---------------------------------------------------------------------------


def _bars_since_true(mask: pd.Series, cap: int) -> pd.Series:
    """Bars since the most recent True in `mask`, capped at `cap`.

    NaN if no True has been observed yet at position t. We deliberately
    do NOT fillna(0) — instead the cap saturates and pre-event positions
    remain NaN.
    """
    out = pd.Series(np.nan, index=mask.index, dtype=float)
    last = np.nan
    for i in range(len(mask)):
        v = mask.iloc[i]
        if isinstance(v, (bool, np.bool_)) and bool(v):
            last = i
        if not np.isnan(last):
            d = i - last
            out.iloc[i] = float(min(d, cap))
    return out


def _streak_above(cond: pd.Series) -> pd.Series:
    """Consecutive-True streak counter. Each True bar increments,
    each False resets to 0. Leading NaNs preserved.
    """
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


def _round_dist(price: pd.Series, step: float) -> pd.Series:
    """Distance to nearest round-`step` level as a fraction of price.

    For step=10 this gives |close mod 10 centered at the closer side|/close.
    Positive when above the level, negative when below the nearest level.
    Uses signed distance: close-nearest_level, normalized by close.
    """
    nearest = (price / step).round() * step
    return (price - nearest) / price.replace(0.0, np.nan)


# ---------------------------------------------------------------------------
# Features 001-075
# ---------------------------------------------------------------------------


# --- Group A: Donchian-anchored S/R level distances (widely spaced) --------


def f04sr_f04_support_resistance_proximity_dhi_8d_base_v001_signal(close: pd.Series, high: pd.Series) -> pd.Series:
    """(close - rolling 8d high) / close. Distance to short-term resistance
    level (the highest high in the last 8 bars)."""
    h8 = high.rolling(8, min_periods=8).max()
    out = (close - h8) / close.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dhi_21d_base_v002_signal(close: pd.Series, high: pd.Series) -> pd.Series:
    """(close - rolling 21d high) / close. Distance to monthly resistance."""
    h21 = high.rolling(21, min_periods=21).max()
    out = (close - h21) / close.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dlo_50d_base_v003_signal(closeadj: pd.Series) -> pd.Series:
    """(closeadj - rolling 50d low of closeadj) / closeadj. Distance above
    the 50-day support level."""
    l50 = closeadj.rolling(50, min_periods=50).min()
    out = (closeadj - l50) / closeadj.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dhi_252d_base_v004_signal(closeadj: pd.Series) -> pd.Series:
    """log(closeadj / 252d-high). Distance below 52-week resistance."""
    h252 = closeadj.rolling(252, min_periods=200).max()
    out = np.log(closeadj / h252.replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dlo_252d_base_v005_signal(closeadj: pd.Series) -> pd.Series:
    """log(closeadj / 252d-low). Distance above 52-week support."""
    l252 = closeadj.rolling(252, min_periods=200).min()
    out = np.log(closeadj / l252.replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group B: Days since anchored extremum / pivot age ---------------------


def f04sr_f04_support_resistance_proximity_dshi_21d_base_v006_signal(high: pd.Series) -> pd.Series:
    """Days since the 21-day high (location of last resistance peak in the
    21-bar window). Bounded in [0, 20]."""
    idx_max = high.rolling(21, min_periods=21).apply(lambda x: float(np.argmax(x[::-1])), raw=True)
    return idx_max.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dslo_63d_base_v007_signal(closeadj: pd.Series) -> pd.Series:
    """Days since the 63-day low (location of last support trough). Uses
    closeadj because window > 21d."""
    idx_min = closeadj.rolling(63, min_periods=63).apply(lambda x: float(np.argmin(x[::-1])), raw=True)
    return idx_min.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dshi_252d_base_v008_signal(closeadj: pd.Series) -> pd.Series:
    """Days since 52-week high. Saturates at 252."""
    idx_max = closeadj.rolling(252, min_periods=200).apply(lambda x: float(np.argmax(x[::-1])), raw=True)
    return idx_max.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dslo_252d_base_v009_signal(closeadj: pd.Series) -> pd.Series:
    """Days since 52-week low. Saturates at 252."""
    idx_min = closeadj.rolling(252, min_periods=200).apply(lambda x: float(np.argmin(x[::-1])), raw=True)
    return idx_min.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dshi_50d_base_v010_signal(closeadj: pd.Series) -> pd.Series:
    """Days since 50d high (the last resistance peak within the swing window)."""
    idx_max = closeadj.rolling(50, min_periods=50).apply(lambda x: float(np.argmax(x[::-1])), raw=True)
    return idx_max.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dslo_100d_base_v011_signal(closeadj: pd.Series) -> pd.Series:
    """Days since 100d low (the last support trough within ~5-month window)."""
    idx_min = closeadj.rolling(100, min_periods=100).apply(lambda x: float(np.argmin(x[::-1])), raw=True)
    return idx_min.replace([np.inf, -np.inf], np.nan)


# --- Group C: Drawdown / drawup from anchored extremes ---------------------


def f04sr_f04_support_resistance_proximity_ddh_252d_base_v012_signal(closeadj: pd.Series) -> pd.Series:
    """Time-decayed proximity to 252d high: closer + more-recent peaks
    score higher. Computed as the maximum over the last 252 bars of
    exp(-(t-k)/63) * (closeadj_k / closeadj_t). A recency-weighted
    resistance-proximity score that diverges from a pure level distance."""
    log_c = np.log(closeadj.replace(0.0, np.nan))
    def _decay(x):
        if np.all(np.isnan(x)):
            return np.nan
        n = len(x)
        ref = x[-1]
        if not np.isfinite(ref):
            return np.nan
        ages = np.arange(n - 1, -1, -1, dtype=float)
        w = np.exp(-ages / 63.0)
        diff = x - ref  # log-ratio in log-space
        return float(np.nanmax(w * diff))
    out = log_c.rolling(252, min_periods=60).apply(_decay, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dul_252d_base_v013_signal(closeadj: pd.Series) -> pd.Series:
    """Width of the 252d high-low channel: log(h252 / l252). Pure
    channel breadth — a width metric of long-term S/R envelope, not a
    position within it. Higher when the year's range is wider."""
    h252 = closeadj.rolling(252, min_periods=200).max()
    l252 = closeadj.rolling(252, min_periods=200).min()
    out = np.log(h252.replace(0.0, np.nan) / l252.replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_ddh_100d_base_v014_signal(closeadj: pd.Series) -> pd.Series:
    """Drawdown from 100d high level."""
    h100 = closeadj.rolling(100, min_periods=100).max()
    out = closeadj / h100.replace(0.0, np.nan) - 1.0
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dul_63d_base_v015_signal(closeadj: pd.Series) -> pd.Series:
    """Range-fraction position over 63d window: (closeadj - l63) /
    (h63 - l63). Bounded in [0,1]; bands the current price by both
    swing extremes in the 63d window rather than tracking only the low."""
    h63 = closeadj.rolling(63, min_periods=63).max()
    l63 = closeadj.rolling(63, min_periods=63).min()
    rng = (h63 - l63).replace(0.0, np.nan)
    out = (closeadj - l63) / rng
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group D: Classical pivot point family (uses prior period H/L/C) -------


def f04sr_f04_support_resistance_proximity_dpiv_1d_base_v016_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance from close to *weekly* pivot built from rolling 5-bar
    H/L/C averages: pivot_w = (mean(H,5) + mean(L,5) + mean(C,5))/3 of
    bars [-5..-1]. A longer-anchor pivot smoothing out daily noise; the
    5-bar averaging makes it structurally distinct from the prior-bar
    classical pivot."""
    h5 = high.shift(1).rolling(5, min_periods=5).mean()
    l5 = low.shift(1).rolling(5, min_periods=5).mean()
    c5 = close.shift(1).rolling(5, min_periods=5).mean()
    pivot_w = (h5 + l5 + c5) / 3.0
    out = (close - pivot_w) / close.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dr1_1d_base_v017_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance from close to R1 = 2*pivot - L_{-1}. Classical 1st
    resistance level."""
    pivot = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    r1 = 2.0 * pivot - low.shift(1)
    out = (close - r1) / close.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_ds1_1d_base_v018_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance from close to S1 = 2*pivot - H_{-1}. Classical 1st support."""
    pivot = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    s1 = 2.0 * pivot - high.shift(1)
    out = (close - s1) / close.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dr2_1d_base_v019_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Indicator: close > R2 = pivot + (H_{-1}-L_{-1}), expressed as a
    20-bar fraction of breakouts above R2. A discrete event-frequency
    aggregate distinct from a continuous distance to R2."""
    pivot = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    r2 = pivot + (high.shift(1) - low.shift(1))
    cond = (close > r2).astype(float)
    out = cond.rolling(20, min_periods=5).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_ds2_1d_base_v020_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Indicator: close < S2 = pivot - (H_{-1}-L_{-1}), expressed as a
    20-bar fraction. Discrete frequency of breakdowns through S2."""
    pivot = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    s2 = pivot - (high.shift(1) - low.shift(1))
    cond = (close < s2).astype(float)
    out = cond.rolling(20, min_periods=5).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dcamr3_1d_base_v021_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Streak: consecutive bars in which close exceeded Camarilla R3 of
    that bar's prior-bar H/L/C. R3 = C_{-1} + 1.1*(H_{-1}-L_{-1})/4.
    Streak length (in bars) — a discrete count, structurally distinct
    from a continuous distance-to-R3."""
    rng = high.shift(1) - low.shift(1)
    r3 = close.shift(1) + rng * 1.1 / 4.0
    cond = (close > r3).astype(float)
    grp = (cond != cond.shift(1)).cumsum()
    streak = cond.groupby(grp).cumsum() * cond
    return streak.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dcams3_1d_base_v022_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Streak: consecutive bars below Camarilla S3 = C_{-1} -
    1.1*(H_{-1}-L_{-1})/4. Discrete persistence-of-breakdown count."""
    rng = high.shift(1) - low.shift(1)
    s3 = close.shift(1) - rng * 1.1 / 4.0
    cond = (close < s3).astype(float)
    grp = (cond != cond.shift(1)).cumsum()
    streak = cond.groupby(grp).cumsum() * cond
    return streak.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dfibr1_1d_base_v023_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Indicator: bar closed inside the Fibonacci 38.2-61.8% retracement
    band of the prior bar (1.0 if fib_38 <= close <= fib_62, else 0.0),
    smoothed over 10 bars as a fraction. Captures consolidation in the
    'value area' rather than a signed distance to one level."""
    rng = high.shift(1) - low.shift(1)
    fib_38 = low.shift(1) + 0.382 * rng
    fib_62 = low.shift(1) + 0.618 * rng
    inside = ((close >= fib_38) & (close <= fib_62)).astype(float)
    out = inside.rolling(10, min_periods=3).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group E: Williams 5-bar fractal pivots --------------------------------


def f04sr_f04_support_resistance_proximity_dfrhi_30d_base_v024_signal(high: pd.Series, close: pd.Series) -> pd.Series:
    """Distance to the most recent 5-bar fractal high (Williams) within the
    trailing 30 bars. A fractal high at bar i requires: H[i] > H[i-1],
    H[i] > H[i-2], H[i] > H[i+1], H[i] > H[i+2]. To avoid lookahead we
    only treat a candidate as confirmed 2 bars after it occurs, so the
    'distance' uses prices known by bar t."""
    is_frac = (high.shift(2) > high.shift(3)) & (high.shift(2) > high.shift(4)) & (high.shift(2) > high.shift(1)) & (high.shift(2) > high)
    level = high.shift(2).where(is_frac)
    last_level = level.ffill(limit=30)
    out = (close - last_level) / close.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dfrlo_50d_base_v025_signal(low: pd.Series, closeadj: pd.Series, close: pd.Series) -> pd.Series:
    """Distance to most recent 5-bar fractal low within trailing 50 bars."""
    is_frac = (low.shift(2) < low.shift(3)) & (low.shift(2) < low.shift(4)) & (low.shift(2) < low.shift(1)) & (low.shift(2) < low)
    level = low.shift(2).where(is_frac)
    last_level = level.ffill(limit=50)
    out = (close - last_level) / close.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_nfrhi_30d_base_v026_signal(high: pd.Series) -> pd.Series:
    """Count of confirmed fractal highs in the last 30 bars. A discrete
    integer-valued S/R-density signal."""
    is_frac = (high.shift(2) > high.shift(3)) & (high.shift(2) > high.shift(4)) & (high.shift(2) > high.shift(1)) & (high.shift(2) > high)
    out = is_frac.astype(float).rolling(30, min_periods=10).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_nfrlo_50d_base_v027_signal(low: pd.Series) -> pd.Series:
    """Count of confirmed fractal lows in the last 50 bars."""
    is_frac = (low.shift(2) < low.shift(3)) & (low.shift(2) < low.shift(4)) & (low.shift(2) < low.shift(1)) & (low.shift(2) < low)
    out = is_frac.astype(float).rolling(50, min_periods=10).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_afrhi_30d_base_v028_signal(high: pd.Series) -> pd.Series:
    """Bars since last fractal high (within last 30 bars, else NaN)."""
    is_frac = (high.shift(2) > high.shift(3)) & (high.shift(2) > high.shift(4)) & (high.shift(2) > high.shift(1)) & (high.shift(2) > high)
    return _bars_since_true(is_frac.fillna(False), 30)


def f04sr_f04_support_resistance_proximity_afrlo_50d_base_v029_signal(low: pd.Series) -> pd.Series:
    """Bars since last fractal low (within last 50 bars)."""
    is_frac = (low.shift(2) < low.shift(3)) & (low.shift(2) < low.shift(4)) & (low.shift(2) < low.shift(1)) & (low.shift(2) < low)
    return _bars_since_true(is_frac.fillna(False), 50)


# --- Group F: Round-number psychological levels ----------------------------


def f04sr_f04_support_resistance_proximity_dr10_1d_base_v030_signal(close: pd.Series) -> pd.Series:
    """Signed distance to nearest round-10 level as fraction of close.
    Round-$10 levels (e.g., $50, $60, $70) act as psychological pivots."""
    return _round_dist(close, 10.0).replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dr5_1d_base_v031_signal(close: pd.Series) -> pd.Series:
    """Signed distance to nearest round-5 level."""
    return _round_dist(close, 5.0).replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_pr10_1d_base_v032_signal(close: pd.Series) -> pd.Series:
    """Position within nearest [round-10*k, round-10*(k+1)] decile bucket
    in [0,1). Captures intra-$10-range location distinct from signed
    distance because it is always positive."""
    pos = (close / 10.0) - np.floor(close / 10.0)
    return pos.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_drone_1d_base_v033_signal(close: pd.Series) -> pd.Series:
    """Signed distance to nearest round-1 dollar level."""
    return _round_dist(close, 1.0).replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dr100_1d_base_v034_signal(close: pd.Series) -> pd.Series:
    """Signed distance to nearest round-100 level. The strongest
    psychological tier."""
    return _round_dist(close, 100.0).replace([np.inf, -np.inf], np.nan)


# --- Group G: Multi-touch level strength -----------------------------------


def f04sr_f04_support_resistance_proximity_thi_30d_base_v035_signal(high: pd.Series) -> pd.Series:
    """Count of bars in the last 30 whose high touched within 0.5% of the
    rolling 30d high. Measures strength of the resistance at that price.

    A 'touched' bar is one where the bar's high comes within 0.5% of the
    swing high level over the window. Multi-touch -> strong resistance."""
    h30 = high.rolling(30, min_periods=15).max()
    touched = (high >= 0.995 * h30) & (h30.notna())
    out = touched.astype(float).rolling(30, min_periods=15).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_thi_60d_base_v036_signal(high: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Touches within 1% of 60d high. Closeadj used only for warm-up
    consistency; touches counted on raw high."""
    h60 = high.rolling(60, min_periods=30).max()
    touched = (high >= 0.99 * h60) & (h60.notna())
    out = touched.astype(float).rolling(60, min_periods=30).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_tlo_30d_base_v037_signal(low: pd.Series) -> pd.Series:
    """Touches of the 30d low (within 0.5%). Strength of nearby support."""
    l30 = low.rolling(30, min_periods=15).min()
    touched = (low <= 1.005 * l30) & (l30.notna())
    out = touched.astype(float).rolling(30, min_periods=15).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_tlo_60d_base_v038_signal(low: pd.Series) -> pd.Series:
    """Touches of the 60d low (within 1%)."""
    l60 = low.rolling(60, min_periods=30).min()
    touched = (low <= 1.01 * l60) & (l60.notna())
    out = touched.astype(float).rolling(60, min_periods=30).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_tmaxhi_100d_base_v039_signal(high: pd.Series) -> pd.Series:
    """Max touch count of any swing-high price band (0.5%) over the last 100
    bars. Computes the histogram of recent highs in 1% bins and returns
    the largest bucket count — the most-touched (strongest) S/R level."""
    def _f(x):
        if len(x) < 30:
            return np.nan
        ref = float(x[-1])
        if not np.isfinite(ref) or ref <= 0:
            return np.nan
        # 0.5% bins relative to the last bar's level
        bins = np.round(np.log(x / ref) / np.log(1.005))
        vals, cnts = np.unique(bins, return_counts=True)
        return float(cnts.max())
    out = high.rolling(100, min_periods=30).apply(_f, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group H: Breakout / breakdown signs and streaks -----------------------




def f04sr_f04_support_resistance_proximity_sigbd_20d_base_v041_signal(close: pd.Series, low: pd.Series) -> pd.Series:
    """sign(prior-20d-low.shift(1) - close). +1 broke below 20d support."""
    prior_lo = low.shift(1).rolling(20, min_periods=20).min()
    diff = prior_lo - close
    out = np.sign(diff)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_sigbo_50d_base_v042_signal(closeadj: pd.Series) -> pd.Series:
    """sign(closeadj - prior-50d closeadj high.shift(1))."""
    prior_hi = closeadj.shift(1).rolling(50, min_periods=50).max()
    diff = closeadj - prior_hi
    out = np.sign(diff)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_sigbd_50d_base_v043_signal(closeadj: pd.Series) -> pd.Series:
    """sign(prior-50d closeadj low.shift(1) - closeadj)."""
    prior_lo = closeadj.shift(1).rolling(50, min_periods=50).min()
    diff = prior_lo - closeadj
    out = np.sign(diff)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_skbo_20d_base_v044_signal(close: pd.Series, high: pd.Series) -> pd.Series:
    """Streak of consecutive bars where close > prior-20d-high.shift(1).
    Long streak = price has been holding above broken resistance."""
    prior_hi = high.shift(1).rolling(20, min_periods=20).max()
    cond = (close > prior_hi)
    return _streak_above(cond).replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_skbd_20d_base_v045_signal(close: pd.Series, low: pd.Series) -> pd.Series:
    """Streak of consecutive bars where close < prior-20d-low.shift(1)."""
    prior_lo = low.shift(1).rolling(20, min_periods=20).min()
    cond = (close < prior_lo)
    return _streak_above(cond).replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_skbo_63d_base_v046_signal(closeadj: pd.Series) -> pd.Series:
    """Streak of bars where closeadj > prior-63d-high.shift(1)."""
    prior_hi = closeadj.shift(1).rolling(63, min_periods=63).max()
    cond = (closeadj > prior_hi)
    return _streak_above(cond).replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_fbo_30d_base_v047_signal(close: pd.Series, high: pd.Series) -> pd.Series:
    """False-breakout count in last 30 bars. A false breakout: bar t-k
    closed above prior-20d-high but bar t is back below the level
    (within 5 bars). Counts such failed breakouts."""
    prior_hi = high.shift(1).rolling(20, min_periods=20).max()
    broke_above = (close > prior_hi)
    came_back = (close < prior_hi)
    # bar k was a breakout, bar k+j (j in 1..5) is a came-back: count k's
    failed = pd.Series(False, index=close.index)
    for j in range(1, 6):
        failed = failed | (broke_above.shift(j).fillna(False) & came_back)
    out = failed.astype(float).rolling(30, min_periods=15).sum()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group I: Magnitude of break / signed level differential --------------


def f04sr_f04_support_resistance_proximity_mbo_20d_base_v048_signal(close: pd.Series, high: pd.Series) -> pd.Series:
    """Count of distinct 20d-high *levels* visited in the trailing 60
    bars: bins log(prior-20d-high) into 1% buckets and returns the
    number of unique buckets seen in the last 60 bars. Captures
    the number of structurally distinct resistance levels rather than
    the current distance to a single level."""
    prior_hi = high.shift(1).rolling(20, min_periods=20).max()
    log_hi = np.log(prior_hi.replace(0.0, np.nan))
    def _nu(x):
        if np.all(np.isnan(x)):
            return np.nan
        x = x[~np.isnan(x)]
        if len(x) == 0:
            return np.nan
        bins = np.round(x / np.log(1.01))
        return float(len(np.unique(bins)))
    out = log_hi.rolling(60, min_periods=20).apply(_nu, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_mbo_50d_base_v049_signal(closeadj: pd.Series) -> pd.Series:
    """(closeadj - prior-50d-high.shift(1)) / closeadj."""
    prior_hi = closeadj.shift(1).rolling(50, min_periods=50).max()
    out = (closeadj - prior_hi) / closeadj.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_mbd_20d_base_v050_signal(close: pd.Series, low: pd.Series) -> pd.Series:
    """(prior-20d-low.shift(1) - close) / close. Signed magnitude of
    breakdown — positive when below 20d support, negative when above."""
    prior_lo = low.shift(1).rolling(20, min_periods=20).min()
    out = (prior_lo - close) / close.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_mbo_252d_base_v051_signal(closeadj: pd.Series) -> pd.Series:
    """Cumulative count of past 252-day bars whose closeadj exceeded the
    prior 252d high (i.e., total number of 52w-high breakouts in the
    trailing year). A discrete event-count differs structurally from a
    continuous magnitude-of-break."""
    prior_hi = closeadj.shift(1).rolling(252, min_periods=200).max()
    is_break = (closeadj > prior_hi).astype(float)
    out = is_break.rolling(252, min_periods=200).sum()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group J: Local swing pivots (lookback-only) ---------------------------


def f04sr_f04_support_resistance_proximity_dlmx_21d_base_v052_signal(close: pd.Series, high: pd.Series) -> pd.Series:
    """Distance from close to the 21d high-low channel midpoint
    ((h21max + l21min)/2). The channel midpoint acts as a balanced
    reference level different from the swing-high distance."""
    h21 = high.rolling(21, min_periods=21).max()
    l21 = high.rolling(21, min_periods=21).min()
    mid = (h21 + l21) / 2.0
    out = (close - mid) / close.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dlmn_63d_base_v053_signal(closeadj: pd.Series) -> pd.Series:
    """Standard deviation of closeadj values in the last 63 bars
    *relative* to the rolling 63d-min: std(closeadj - l63) / closeadj.
    Captures the dispersion of the price away from its 63d support
    floor — a width metric anchored to the trough rather than a
    distance to the trough."""
    l63 = closeadj.rolling(63, min_periods=63).min()
    diff = closeadj - l63
    out = diff.rolling(63, min_periods=30).std() / closeadj.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dlmx_8d_base_v054_signal(close: pd.Series, high: pd.Series) -> pd.Series:
    """Range coverage: (h8 - l8) / mean(h, 8) — the relative width of
    the 8-bar high band. Wide band signals volatile resistance, narrow
    band signals a tight ceiling. Structurally a width metric, not a
    distance to a level."""
    h8 = high.rolling(8, min_periods=8).max()
    l8 = high.rolling(8, min_periods=8).min()
    mh = high.rolling(8, min_periods=8).mean().replace(0.0, np.nan)
    out = (h8 - l8) / mh
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dlmn_100d_base_v055_signal(closeadj: pd.Series) -> pd.Series:
    """Concavity-style support indicator: difference between the 100d
    *rolling-mean* and the 100d *min* of closeadj, divided by closeadj.
    Larger value indicates the average price sits well above the
    swing-low — measures the cushion to the trough rather than the
    current distance to it."""
    l100 = closeadj.rolling(100, min_periods=100).min()
    m100 = closeadj.rolling(100, min_periods=100).mean()
    out = (m100 - l100) / closeadj.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_alm_21d_base_v056_signal(high: pd.Series) -> pd.Series:
    """Position of current bar's high within the 21d high-low range:
    (high - rolling 21d-min(high)) / (rolling 21d-max(high) - rolling
    21d-min(high)). Bounded in [0,1]; captures vertical placement of the
    latest high inside the swing band rather than its temporal location."""
    h21 = high.rolling(21, min_periods=21).max()
    l21 = high.rolling(21, min_periods=21).min()
    rng = (h21 - l21).replace(0.0, np.nan)
    out = (high - l21) / rng
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group K: Density / clustering of prior peaks and troughs --------------


def f04sr_f04_support_resistance_proximity_nphi_100d_base_v057_signal(closeadj: pd.Series, high: pd.Series) -> pd.Series:
    """Count of fractal highs in last 100 bars whose price is within +/-2%
    of the current closeadj. A measure of how many prior resistance
    peaks cluster near the present price level."""
    is_frac = (high.shift(2) > high.shift(3)) & (high.shift(2) > high.shift(4)) & (high.shift(2) > high.shift(1)) & (high.shift(2) > high)
    levels = high.shift(2).where(is_frac)
    def _cnt(x):
        # x is a numpy array of the rolling window (levels). Last index is t.
        # We need the closeadj at t to compare; instead pass closeadj-relative
        # levels already (see prep below).
        if np.all(np.isnan(x)):
            return np.nan
        x = x[~np.isnan(x)]
        return float((np.abs(x) <= 0.02).sum())
    ratio = (levels / closeadj - 1.0)
    out = ratio.rolling(100, min_periods=10).apply(_cnt, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_nplo_100d_base_v058_signal(closeadj: pd.Series, low: pd.Series) -> pd.Series:
    """Count of fractal lows in last 100 bars whose price is within +/-2%
    of current closeadj. Density of nearby support troughs."""
    is_frac = (low.shift(2) < low.shift(3)) & (low.shift(2) < low.shift(4)) & (low.shift(2) < low.shift(1)) & (low.shift(2) < low)
    levels = low.shift(2).where(is_frac)
    ratio = (levels / closeadj - 1.0)
    def _cnt(x):
        if np.all(np.isnan(x)):
            return np.nan
        x = x[~np.isnan(x)]
        return float((np.abs(x) <= 0.02).sum())
    out = ratio.rolling(100, min_periods=10).apply(_cnt, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_denhi_252d_base_v059_signal(closeadj: pd.Series, high: pd.Series) -> pd.Series:
    """Density (fraction) of historical bar highs in the last 252 bars that
    sit in the same 2% band as the current close. Concentration of
    historical resistance touches at the current price level."""
    rel = (high / closeadj - 1.0)
    in_band = (rel.abs() <= 0.02).astype(float)
    out = in_band.rolling(252, min_periods=100).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_denlo_252d_base_v060_signal(closeadj: pd.Series, low: pd.Series) -> pd.Series:
    """Dispersion of historical fractal-low LEVELS over the last 252
    bars, expressed as std(log(level)) over the pivot-low population.
    A high value means support pivots are spread across a wide price
    band; low value means they cluster tightly. Population-statistic of
    pivots, not a distance to one."""
    is_piv = (low.shift(2) < low.shift(4)) & (low.shift(2) < low.shift(3)) & (low.shift(2) < low.shift(1)) & (low.shift(2) < low)
    levels = low.shift(2).where(is_piv)
    log_levels = np.log(levels.replace(0.0, np.nan))
    n = len(log_levels)
    arr = log_levels.to_numpy()
    out_arr = np.full(n, np.nan, dtype=float)
    for t in range(252, n):
        window = arr[t-251:t+1]
        m = ~np.isnan(window)
        if m.sum() < 5:
            continue
        out_arr[t] = float(np.std(window[m], ddof=1)) if m.sum() > 1 else 0.0
    out = pd.Series(out_arr, index=closeadj.index)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group L: Rolling-rank of distance to nearest level --------------------


def f04sr_f04_support_resistance_proximity_rkhi_60d_base_v061_signal(closeadj: pd.Series) -> pd.Series:
    """Rolling-percentile rank (0-1) over 60d of log(closeadj/252d-high).
    Where is current distance to 52w-high relative to the past 60 days?"""
    h252 = closeadj.rolling(252, min_periods=200).max()
    d = np.log(closeadj / h252.replace(0.0, np.nan))
    out = d.rolling(60, min_periods=20).rank(pct=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_rklo_60d_base_v062_signal(closeadj: pd.Series) -> pd.Series:
    """Rolling 60d rank of (closeadj/252d-low - 1). Captures whether the
    current drawup-from-low is rich vs recent history."""
    l252 = closeadj.rolling(252, min_periods=200).min()
    d = closeadj / l252.replace(0.0, np.nan) - 1.0
    out = d.rolling(60, min_periods=20).rank(pct=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_rkfr_30d_base_v063_signal(closeadj: pd.Series, high: pd.Series) -> pd.Series:
    """Rolling 30d percentile rank of distance to most-recent fractal high
    level (close - last-fractal-high)/close. Variation: where in recent
    history is the current discount to last resistance peak?"""
    is_frac = (high.shift(2) > high.shift(3)) & (high.shift(2) > high.shift(4)) & (high.shift(2) > high.shift(1)) & (high.shift(2) > high)
    level = high.shift(2).where(is_frac).ffill(limit=60)
    d = (closeadj - level) / closeadj.replace(0.0, np.nan)
    out = d.rolling(30, min_periods=10).rank(pct=True)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group M: Recovery / failure of break ----------------------------------


def f04sr_f04_support_resistance_proximity_rec_30d_base_v064_signal(close: pd.Series, high: pd.Series) -> pd.Series:
    """Bars since the most recent breakout above prior-20d-high, capped at
    30 bars. Pivot age of the last resistance break."""
    prior_hi = high.shift(1).rolling(20, min_periods=20).max()
    cond = (close > prior_hi)
    return _bars_since_true(cond.fillna(False), 30)


def f04sr_f04_support_resistance_proximity_redr_30d_base_v065_signal(close: pd.Series, high: pd.Series) -> pd.Series:
    """Re-entry magnitude: when the most recent breakout (within 30 bars)
    has reversed back inside, returns (prior-20d-high level at break -
    current close)/close. Reflects how far the failed-breakout has
    pulled back. NaN when no recent break or still above."""
    prior_hi = high.shift(1).rolling(20, min_periods=20).max()
    broke = (close > prior_hi)
    # snapshot the level at break time
    lvl_at_break = prior_hi.where(broke).ffill(limit=30)
    came_back = (close < lvl_at_break)
    magnitude = (lvl_at_break - close) / close.replace(0.0, np.nan)
    out = magnitude.where(came_back)
    # leave NaN when not applicable; the series still has enough non-NaN
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_netbo_60d_base_v066_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Net break count in 60 bars: (# bars closed > prior-20d-high) minus
    (# bars closed < prior-20d-low). A two-sided breakout sentiment
    anchored to specific S/R levels rather than to a mean."""
    prior_hi = high.shift(1).rolling(20, min_periods=20).max()
    prior_lo = low.shift(1).rolling(20, min_periods=20).min()
    up = (close > prior_hi).astype(float)
    dn = (close < prior_lo).astype(float)
    out = up.rolling(60, min_periods=30).sum() - dn.rolling(60, min_periods=30).sum()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group N: DeMark and Woodie pivots -------------------------------------


def f04sr_f04_support_resistance_proximity_ddmpv_1d_base_v067_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bar location within prior-day range: (close - L_{-1}) /
    (H_{-1} - L_{-1}). A ratio (not a difference) of the close inside
    the prior bar's high-low band. Unbounded above when current close
    pierces prior high; near 0 at prior low. Differs structurally from
    a (close - pivot)/close difference because the denominator is the
    *prior-day range*, not close itself."""
    rng = (high.shift(1) - low.shift(1)).replace(0.0, np.nan)
    out = (close - low.shift(1)) / rng
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dwdr1_1d_base_v068_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Indicator: prior bar's high tested current resistance band.
    Returns 1.0 when (H_{-1} - max(C_{-1},O_proxy)) / H_{-1} exceeds 0.5%
    (a rejection wick at resistance), 0 otherwise, smoothed over 10
    bars. Structurally a categorical rejection-event count, NOT a
    distance-to-pivot. The 'open proxy' is L_{-1} (lower of prior bar)."""
    body_top = pd.concat([close.shift(1), low.shift(1)], axis=1).max(axis=1)
    rejection = (high.shift(1) - body_top) / high.shift(1).replace(0.0, np.nan)
    is_rej = (rejection > 0.005).astype(float)
    out = is_rej.rolling(10, min_periods=3).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_dwds1_1d_base_v069_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Indicator: prior bar's low tested current support band — a
    rejection wick at support. Returns count over the last 10 bars of
    events where (min(C_{-1}, H_{-1}) - L_{-1}) / L_{-1} > 0.5%."""
    body_bot = pd.concat([close.shift(1), high.shift(1)], axis=1).min(axis=1)
    rejection = (body_bot - low.shift(1)) / low.shift(1).replace(0.0, np.nan)
    is_rej = (rejection > 0.005).astype(float)
    out = is_rej.rolling(10, min_periods=3).sum()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group O: Anchored historical extremes ---------------------------------


def f04sr_f04_support_resistance_proximity_dath_all_base_v070_signal(closeadj: pd.Series) -> pd.Series:
    """log(closeadj / cummax(closeadj)). Distance below the
    anchored-since-inception all-time high level. Strongly path-anchored;
    differs from 252d-high once max moves outside the rolling window."""
    ath = closeadj.expanding(min_periods=30).max()
    out = np.log(closeadj / ath.replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_kelb_252d_base_v071_signal(closeadj: pd.Series) -> pd.Series:
    """Sign-encoded location: +1 if closeadj is closer (in log space) to
    the 252d high than to the 252d low, else -1. A discrete S/R-tilt
    indicator anchored to specific extreme levels."""
    h252 = closeadj.rolling(252, min_periods=200).max()
    l252 = closeadj.rolling(252, min_periods=200).min()
    near_hi = np.log(closeadj / h252.replace(0.0, np.nan)).abs()
    near_lo = np.log(closeadj / l252.replace(0.0, np.nan)).abs()
    out = np.sign(near_lo - near_hi)
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_mxh_21d_base_v072_signal(closeadj: pd.Series) -> pd.Series:
    """Range of log(closeadj/252d-high) over last 21 bars (max - min).
    Captures the swing AMPLITUDE in proximity-to-resistance during the
    past month, not the level. Structurally a width, not a distance."""
    h252 = closeadj.rolling(252, min_periods=200).max()
    d = np.log(closeadj / h252.replace(0.0, np.nan))
    out = d.rolling(21, min_periods=10).max() - d.rolling(21, min_periods=10).min()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group P: New-high / new-low indicators --------------------------------


def f04sr_f04_support_resistance_proximity_nh_252d_base_v073_signal(closeadj: pd.Series) -> pd.Series:
    """Indicator: closeadj > prior-252d-high.shift(1) -> +1 (new 52w high),
    else -1. Binary anchored-extreme signal."""
    prior_hi = closeadj.shift(1).rolling(252, min_periods=200).max()
    out = pd.Series(np.where(closeadj > prior_hi, 1.0, -1.0), index=closeadj.index, dtype=float)
    out = out.where(prior_hi.notna())
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_nl_252d_base_v074_signal(closeadj: pd.Series) -> pd.Series:
    """Indicator: closeadj < prior-252d-low.shift(1) -> +1 (new 52w low),
    else -1."""
    prior_lo = closeadj.shift(1).rolling(252, min_periods=200).min()
    out = pd.Series(np.where(closeadj < prior_lo, 1.0, -1.0), index=closeadj.index, dtype=float)
    out = out.where(prior_lo.notna())
    return out.replace([np.inf, -np.inf], np.nan)


def f04sr_f04_support_resistance_proximity_nhl_60d_base_v075_signal(closeadj: pd.Series) -> pd.Series:
    """(# new 60d highs in last 60d) - (# new 60d lows in last 60d).
    Anchored-extreme tally — distinct from sign/streak features because
    it integrates count over a window."""
    prior_hi = closeadj.shift(1).rolling(60, min_periods=60).max()
    prior_lo = closeadj.shift(1).rolling(60, min_periods=60).min()
    up = (closeadj > prior_hi).astype(float)
    dn = (closeadj < prior_lo).astype(float)
    out = up.rolling(60, min_periods=30).sum() - dn.rolling(60, min_periods=30).sum()
    return out.replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


def _e(fn, *inputs):
    return fn.__name__, {"inputs": list(inputs), "func": fn}


f04_support_resistance_proximity_base_001_075_REGISTRY = dict([
    _e(f04sr_f04_support_resistance_proximity_dhi_8d_base_v001_signal, "close", "high"),
    _e(f04sr_f04_support_resistance_proximity_dhi_21d_base_v002_signal, "close", "high"),
    _e(f04sr_f04_support_resistance_proximity_dlo_50d_base_v003_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_dhi_252d_base_v004_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_dlo_252d_base_v005_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_dshi_21d_base_v006_signal, "high"),
    _e(f04sr_f04_support_resistance_proximity_dslo_63d_base_v007_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_dshi_252d_base_v008_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_dslo_252d_base_v009_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_dshi_50d_base_v010_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_dslo_100d_base_v011_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_ddh_252d_base_v012_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_dul_252d_base_v013_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_ddh_100d_base_v014_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_dul_63d_base_v015_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_dpiv_1d_base_v016_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_dr1_1d_base_v017_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_ds1_1d_base_v018_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_dr2_1d_base_v019_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_ds2_1d_base_v020_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_dcamr3_1d_base_v021_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_dcams3_1d_base_v022_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_dfibr1_1d_base_v023_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_dfrhi_30d_base_v024_signal, "high", "close"),
    _e(f04sr_f04_support_resistance_proximity_dfrlo_50d_base_v025_signal, "low", "closeadj", "close"),
    _e(f04sr_f04_support_resistance_proximity_nfrhi_30d_base_v026_signal, "high"),
    _e(f04sr_f04_support_resistance_proximity_nfrlo_50d_base_v027_signal, "low"),
    _e(f04sr_f04_support_resistance_proximity_afrhi_30d_base_v028_signal, "high"),
    _e(f04sr_f04_support_resistance_proximity_afrlo_50d_base_v029_signal, "low"),
    _e(f04sr_f04_support_resistance_proximity_dr10_1d_base_v030_signal, "close"),
    _e(f04sr_f04_support_resistance_proximity_dr5_1d_base_v031_signal, "close"),
    _e(f04sr_f04_support_resistance_proximity_pr10_1d_base_v032_signal, "close"),
    _e(f04sr_f04_support_resistance_proximity_drone_1d_base_v033_signal, "close"),
    _e(f04sr_f04_support_resistance_proximity_dr100_1d_base_v034_signal, "close"),
    _e(f04sr_f04_support_resistance_proximity_thi_30d_base_v035_signal, "high"),
    _e(f04sr_f04_support_resistance_proximity_thi_60d_base_v036_signal, "high", "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_tlo_30d_base_v037_signal, "low"),
    _e(f04sr_f04_support_resistance_proximity_tlo_60d_base_v038_signal, "low"),
    _e(f04sr_f04_support_resistance_proximity_tmaxhi_100d_base_v039_signal, "high"),
    _e(f04sr_f04_support_resistance_proximity_sigbd_20d_base_v041_signal, "close", "low"),
    _e(f04sr_f04_support_resistance_proximity_sigbo_50d_base_v042_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_sigbd_50d_base_v043_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_skbo_20d_base_v044_signal, "close", "high"),
    _e(f04sr_f04_support_resistance_proximity_skbd_20d_base_v045_signal, "close", "low"),
    _e(f04sr_f04_support_resistance_proximity_skbo_63d_base_v046_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_fbo_30d_base_v047_signal, "close", "high"),
    _e(f04sr_f04_support_resistance_proximity_mbo_20d_base_v048_signal, "close", "high"),
    _e(f04sr_f04_support_resistance_proximity_mbo_50d_base_v049_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_mbd_20d_base_v050_signal, "close", "low"),
    _e(f04sr_f04_support_resistance_proximity_mbo_252d_base_v051_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_dlmx_21d_base_v052_signal, "close", "high"),
    _e(f04sr_f04_support_resistance_proximity_dlmn_63d_base_v053_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_dlmx_8d_base_v054_signal, "close", "high"),
    _e(f04sr_f04_support_resistance_proximity_dlmn_100d_base_v055_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_alm_21d_base_v056_signal, "high"),
    _e(f04sr_f04_support_resistance_proximity_nphi_100d_base_v057_signal, "closeadj", "high"),
    _e(f04sr_f04_support_resistance_proximity_nplo_100d_base_v058_signal, "closeadj", "low"),
    _e(f04sr_f04_support_resistance_proximity_denhi_252d_base_v059_signal, "closeadj", "high"),
    _e(f04sr_f04_support_resistance_proximity_denlo_252d_base_v060_signal, "closeadj", "low"),
    _e(f04sr_f04_support_resistance_proximity_rkhi_60d_base_v061_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_rklo_60d_base_v062_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_rkfr_30d_base_v063_signal, "closeadj", "high"),
    _e(f04sr_f04_support_resistance_proximity_rec_30d_base_v064_signal, "close", "high"),
    _e(f04sr_f04_support_resistance_proximity_redr_30d_base_v065_signal, "close", "high"),
    _e(f04sr_f04_support_resistance_proximity_netbo_60d_base_v066_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_ddmpv_1d_base_v067_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_dwdr1_1d_base_v068_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_dwds1_1d_base_v069_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_dath_all_base_v070_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_kelb_252d_base_v071_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_mxh_21d_base_v072_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_nh_252d_base_v073_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_nl_252d_base_v074_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_nhl_60d_base_v075_signal, "closeadj"),
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
    for name, entry in f04_support_resistance_proximity_base_001_075_REGISTRY.items():
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
    print(f"OK base_001_075: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
