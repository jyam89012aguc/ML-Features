"""f09_close_position_within_range base features 001-075.

Domain: close-position-within-(single-bar)-range. Core quantity is
close_pos = (close - low) / (high - low), the intra-bar location of
the close on the [0,1] segment between low and high. Every feature
references this single-bar position or aggregations of it; no rolling
high-low channels (that is f02 territory) and no body-vs-range candle
ratios (f06 territory).

NaN policy: never `fillna(<value>)` inside any rolling computation;
only `replace([inf,-inf], nan)` at each function's final return.
Windows > 21 use `closeadj` where relevant; windows <= 21 use `close`.
Single-bar high/low/close/open are always the unadjusted intraday
OHLC. Each feature is a fully expanded `def` block — no `_core()`
factory, no `formulas[i]` indexing.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Features 001-075. Each function spells the full close-position formula
# inline. The base quantity reappears in many forms (raw, transformed,
# windowed, signed, ranked, weighted) but every feature is structurally
# distinct from the next.
# ---------------------------------------------------------------------------


# --- Group A: raw and transformed single-bar close-positions (5) ----------


def f09cp_f09_close_position_within_range_cp_1d_base_v001_signal(close, high, low):
    """Raw intra-bar close-position: (c - l) / (h - l). The fundamental
    close-position quantity in [0, 1]."""
    rng = (high - low).replace(0.0, np.nan)
    out = (close - low) / rng
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpdisp_1d_base_v002_signal(close, high, low):
    """(2*close_pos - 1)^2: range-dispersion (concavity). Zero at the
    midpoint, 1 at either extreme. Bounded, NON-MONOTONE in cp so it
    is structurally orthogonal to cp itself."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = (2.0 * cp - 1.0) ** 2
    return out.replace([np.inf, -np.inf], np.nan)




def f09cp_f09_close_position_within_range_cpprior_1d_base_v004_signal(close, high, low):
    """close_pos minus close_pos.shift(3) — three-bar change in
    close-position. Cancels the level component of cp, captures
    multi-bar position drift."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = cp - cp.shift(3)
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_logodds_1d_base_v005_signal(close, high, low):
    """Log-odds of close_pos: log((c-l+eps)/(h-c+eps)). On the
    synthetic data this is very similar to cp; the structurally
    distinct feature here is its difference from a 5d EW of itself."""
    rng = (high - low).replace(0.0, np.nan)
    eps = rng * 0.001 + 1e-9
    lo = np.log((close - low) + eps) - np.log((high - close) + eps)
    out = lo - lo.ewm(span=5, adjust=False, min_periods=5).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group B: close_pos vs open_pos / intra-bar drift (5) -----------------


def f09cp_f09_close_position_within_range_cpop_1d_base_v006_signal(close, open, high, low):
    """close_pos - open_pos = (c - o)/(h - l). Net intra-bar
    drift expressed in fractions of the bar's range."""
    rng = (high - low).replace(0.0, np.nan)
    out = (close - open) / rng
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_op_1d_base_v007_signal(open, high, low):
    """Open-position only: (o - l)/(h - l). Where the bar started in
    its eventual high-low range — control variable for v006."""
    rng = (high - low).replace(0.0, np.nan)
    out = (open - low) / rng
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpopabs_5d_base_v008_signal(close, open, high, low):
    """5d mean of |close_pos - open_pos|. Average intra-bar drift
    magnitude regardless of direction."""
    rng = (high - low).replace(0.0, np.nan)
    d = ((close - open) / rng).abs()
    out = d.rolling(5, min_periods=5).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpopsgn_10d_base_v009_signal(close, open, high, low):
    """10d net count of bars where close_pos > open_pos (up-drift
    bars) minus where close_pos < open_pos (down-drift), divided by 10."""
    drift = close - open
    pos = (drift > 0).astype(float)
    neg = (drift < 0).astype(float)
    eq = (drift == 0).astype(float)
    pos = pos.where(~(high - low).eq(0.0), np.nan)
    neg = neg.where(~(high - low).eq(0.0), np.nan)
    out = (pos - neg).rolling(10, min_periods=10).sum() / 10.0
    # blank the bars with no range so the warm-up reflects valid data only
    _ = eq  # not used directly but kept for clarity
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_oppos_21d_base_v010_signal(open, high, low):
    """21d mean of (o - l)/(h - l). Where bars TYPICALLY open in their
    range over a month — distinct from close_pos."""
    rng = (high - low).replace(0.0, np.nan)
    op = (open - low) / rng
    out = op.rolling(21, min_periods=21).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group C: rolling stats of close_pos (10) -----------------------------


def f09cp_f09_close_position_within_range_cpmean_5d_base_v011_signal(close, high, low):
    """5d mean of close_pos. Short-term average finishing strength."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = cp.rolling(5, min_periods=5).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpmean_21d_base_v012_signal(close, high, low):
    """21d mean of close_pos."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = cp.rolling(21, min_periods=21).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpmed_63d_base_v013_signal(closeadj, close, high, low):
    """63d median of close_pos. Robust to outlier huge-range bars.
    closeadj listed in inputs for window>21 rule even though the bar
    quantity itself uses close (intra-bar)."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = cp.rolling(63, min_periods=63).median()
    # closeadj parameter is intentionally accepted but not used in the
    # numerator (close_pos is single-bar); accept it for input-policy.
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpstd_21d_base_v014_signal(close, high, low):
    """21d std of close_pos: how consistent the close placement is."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = cp.rolling(21, min_periods=21).std()
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpstd_63d_base_v015_signal(closeadj, close, high, low):
    """63d std of close_pos."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = cp.rolling(63, min_periods=63).std()
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpskew_42d_base_v016_signal(closeadj, close, high, low):
    """42d skew of close_pos — symmetry of the close-position
    distribution: negative = many low closes, positive tail."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = cp.rolling(42, min_periods=42).skew()
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpkurt_50d_base_v017_signal(closeadj, close, high, low):
    """50d kurtosis of close_pos. Tail-heaviness of the close placement."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = cp.rolling(50, min_periods=50).kurt()
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpmax_15d_base_v018_signal(close, high, low):
    """15d max of close_pos — best (most bullish) finishing position
    in the trailing window."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = cp.rolling(15, min_periods=15).max()
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpmin_30d_base_v019_signal(closeadj, close, high, low):
    """30d min of close_pos — most bearish finishing in the window."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = cp.rolling(30, min_periods=30).min()
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cprange_45d_base_v020_signal(closeadj, close, high, low):
    """45d (max - min) of close_pos. Width of the close-position
    distribution; distinct from std."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = cp.rolling(45, min_periods=45).max() - cp.rolling(45, min_periods=45).min()
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group D: bull/bear bucket counts (8) ----------------------------------


def f09cp_f09_close_position_within_range_hicnt_20d_base_v021_signal(close, high, low):
    """Count of bars in trailing 20 where close_pos > 0.7
    (close-near-high bar). Normalized to a fraction in [0,1]."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    hi = (cp > 0.7).astype(float)
    hi = hi.where(cp.notna(), np.nan)
    out = hi.rolling(20, min_periods=20).sum() / 20.0
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_locnt_30d_base_v022_signal(closeadj, close, high, low):
    """30d fraction of bars with close_pos < 0.3 (close-near-low)."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    lo = (cp < 0.3).astype(float)
    lo = lo.where(cp.notna(), np.nan)
    out = lo.rolling(30, min_periods=30).sum() / 30.0
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_hilodif_40d_base_v023_signal(closeadj, close, high, low):
    """40d (hi-bars - lo-bars) using 0.7/0.3 thresholds. Sign-aware
    bullish/bearish dominance."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    hi = (cp > 0.7).astype(float).where(cp.notna(), np.nan)
    lo = (cp < 0.3).astype(float).where(cp.notna(), np.nan)
    out = (hi - lo).rolling(40, min_periods=40).sum() / 40.0
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_extrhi_50d_base_v024_signal(closeadj, close, high, low):
    """50d count of close_pos > 0.9 (extreme top closes)."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    flag = (cp > 0.9).astype(float).where(cp.notna(), np.nan)
    out = flag.rolling(50, min_periods=50).sum() / 50.0
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_extrlo_50d_base_v025_signal(closeadj, close, high, low):
    """50d count of close_pos < 0.1 (extreme bottom closes)."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    flag = (cp < 0.1).astype(float).where(cp.notna(), np.nan)
    out = flag.rolling(50, min_periods=50).sum() / 50.0
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_midcnt_60d_base_v026_signal(closeadj, close, high, low):
    """60d fraction of bars with 0.4 <= close_pos <= 0.6 (mid-range
    closes — indecisive bars)."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    flag = ((cp >= 0.4) & (cp <= 0.6)).astype(float).where(cp.notna(), np.nan)
    out = flag.rolling(60, min_periods=60).sum() / 60.0
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_hilorat_30d_base_v027_signal(closeadj, close, high, low):
    """30d ratio (hi-bars)/(lo-bars+1) where hi=cp>0.6, lo=cp<0.4.
    Heavy-tailed asymmetry measure."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    hi = (cp > 0.6).astype(float).where(cp.notna(), np.nan)
    lo = (cp < 0.4).astype(float).where(cp.notna(), np.nan)
    hs = hi.rolling(30, min_periods=30).sum()
    ls = lo.rolling(30, min_periods=30).sum()
    out = (hs - ls) / (hs + ls + 1.0)
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_consechi_10d_base_v028_signal(close, high, low):
    """10d count of cases where cp_t > 0.7 AND cp_{t-1} > 0.7 (back-
    to-back bullish closes)."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    pair = ((cp > 0.7) & (cp.shift(1) > 0.7)).astype(float).where(cp.notna() & cp.shift(1).notna(), np.nan)
    out = pair.rolling(10, min_periods=10).sum() / 10.0
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group E: streaks and timing (6) --------------------------------------


def f09cp_f09_close_position_within_range_streakhi_15d_base_v029_signal(close, high, low):
    """Length of the current run (capped at 15) of consecutive bars
    where close_pos > 0.5. Resets to 0 on a bar with cp <= 0.5."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    above = (cp > 0.5).astype(float).where(cp.notna(), np.nan)
    streak = above.copy()
    prev = 0.0
    out_vals = np.full(len(close), np.nan)
    for i in range(len(close)):
        v = above.iloc[i]
        if np.isnan(v):
            prev = 0.0
            out_vals[i] = np.nan
            continue
        if v > 0.5:
            prev = prev + 1.0
        else:
            prev = 0.0
        out_vals[i] = min(prev, 15.0)
    _ = streak
    out = pd.Series(out_vals, index=close.index)
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_streaklo_15d_base_v030_signal(close, high, low):
    """Current run length (capped 15) of consecutive cp < 0.5 bars."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    below = (cp < 0.5).astype(float).where(cp.notna(), np.nan)
    out_vals = np.full(len(close), np.nan)
    prev = 0.0
    for i in range(len(close)):
        v = below.iloc[i]
        if np.isnan(v):
            prev = 0.0
            out_vals[i] = np.nan
            continue
        if v > 0.5:
            prev = prev + 1.0
        else:
            prev = 0.0
        out_vals[i] = min(prev, 15.0)
    out = pd.Series(out_vals, index=close.index)
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_dayssincehi_50d_base_v031_signal(closeadj, close, high, low):
    """Days since last bar with close_pos > 0.9 (capped at 50)."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    flag = (cp > 0.9).astype(float).where(cp.notna(), np.nan)
    out_vals = np.full(len(close), np.nan)
    days = np.nan
    for i in range(len(close)):
        v = flag.iloc[i]
        if np.isnan(v):
            out_vals[i] = np.nan
            continue
        if v > 0.5:
            days = 0.0
        elif np.isnan(days):
            days = np.nan
        else:
            days = days + 1.0
        out_vals[i] = min(days, 50.0) if not np.isnan(days) else np.nan
    out = pd.Series(out_vals, index=close.index)
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_dayssincelo_50d_base_v032_signal(closeadj, close, high, low):
    """Days since last bar with close_pos < 0.1 (capped 50)."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    flag = (cp < 0.1).astype(float).where(cp.notna(), np.nan)
    out_vals = np.full(len(close), np.nan)
    days = np.nan
    for i in range(len(close)):
        v = flag.iloc[i]
        if np.isnan(v):
            out_vals[i] = np.nan
            continue
        if v > 0.5:
            days = 0.0
        elif np.isnan(days):
            days = np.nan
        else:
            days = days + 1.0
        out_vals[i] = min(days, 50.0) if not np.isnan(days) else np.nan
    out = pd.Series(out_vals, index=close.index)
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_midstreak_15d_base_v033_signal(close, high, low):
    """Streak length (capped 15) where the sign of (cp - 0.5) is
    persistent — counts contiguous bars on the SAME side of midpoint."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    sign = np.sign(cp - 0.5).where(cp.notna(), np.nan)
    out_vals = np.full(len(close), np.nan)
    prev_sign = 0.0
    cnt = 0.0
    for i in range(len(close)):
        v = sign.iloc[i]
        if np.isnan(v):
            prev_sign = 0.0
            cnt = 0.0
            out_vals[i] = np.nan
            continue
        if v == prev_sign and v != 0.0:
            cnt = cnt + 1.0
        else:
            cnt = 1.0
        prev_sign = v
        out_vals[i] = min(cnt, 15.0) * v
    out = pd.Series(out_vals, index=close.index)
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_flipfreq_30d_base_v034_signal(closeadj, close, high, low):
    """30d count of midpoint flips: cases where sign(cp_t - 0.5) !=
    sign(cp_{t-1} - 0.5). Normalized to [0,1]."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    side = np.sign(cp - 0.5)
    flip = (side != side.shift(1)).astype(float).where(side.notna() & side.shift(1).notna(), np.nan)
    out = flip.rolling(30, min_periods=30).sum() / 30.0
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group F: position momentum / change (6) ------------------------------


def f09cp_f09_close_position_within_range_cpdiff_1d_base_v035_signal(close, high, low):
    """One-bar change in close_pos: cp.diff(1). Position momentum."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = cp.diff(1)
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpdiff_5d_base_v036_signal(close, high, low):
    """5-bar change in close_pos: cp - cp.shift(5)."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = cp - cp.shift(5)
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpchgabs_10d_base_v037_signal(close, high, low):
    """10d mean of |cp.diff(1)|. Average position-volatility."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = cp.diff(1).abs().rolling(10, min_periods=10).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpchgsgn_20d_base_v038_signal(close, high, low):
    """20d sum of sign(cp.diff(1)) divided by 20: net direction of
    position change over a month."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    s = np.sign(cp.diff(1))
    out = s.rolling(20, min_periods=20).sum() / 20.0
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpaccdir_15d_base_v039_signal(close, high, low):
    """15d count of consecutive same-sign cp.diff(1). Captures
    persistence of position drift."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    d = cp.diff(1)
    s = np.sign(d)
    same = (s == s.shift(1)).astype(float).where(s.notna() & s.shift(1).notna(), np.nan)
    out = same.rolling(15, min_periods=15).sum() / 15.0
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpslope_30d_base_v040_signal(closeadj, close, high, low):
    """30d slope of cp via diff of means: mean(cp,5) - mean(cp,30)."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = cp.rolling(5, min_periods=5).mean() - cp.rolling(30, min_periods=30).mean()
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group G: weighted aggregates (6) -------------------------------------


def f09cp_f09_close_position_within_range_volwcp_21d_base_v041_signal(close, high, low, volume):
    """Volume-weighted 21d mean of close_pos."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    num = (cp * volume).rolling(21, min_periods=21).sum()
    den = volume.rolling(21, min_periods=21).sum().replace(0.0, np.nan)
    out = num / den
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_rngwcp_30d_base_v042_signal(closeadj, close, high, low):
    """Range-weighted 30d mean of close_pos: longer bars count more."""
    rngraw = high - low
    rng = rngraw.replace(0.0, np.nan)
    cp = (close - low) / rng
    num = (cp * rngraw).rolling(30, min_periods=30).sum()
    den = rngraw.rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    out = num / den
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_dollwcp_40d_base_v043_signal(closeadj, close, high, low, volume):
    """Dollar-volume weighted 40d mean of close_pos (close*volume)."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    dv = close * volume
    num = (cp * dv).rolling(40, min_periods=40).sum()
    den = dv.rolling(40, min_periods=40).sum().replace(0.0, np.nan)
    out = num / den
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_expwcp_10d_base_v044_signal(close, high, low):
    """Exponentially-weighted (span=10) mean of close_pos."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = cp.ewm(span=10, adjust=False, min_periods=10).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_expwcp_50d_base_v045_signal(closeadj, close, high, low):
    """EW(50) mean of close_pos minus EW(10): long-vs-short EW
    position differential — drift-cancelling."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = cp.ewm(span=50, adjust=False, min_periods=50).mean() - cp.ewm(span=10, adjust=False, min_periods=10).mean()
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_trimcp_30d_base_v046_signal(closeadj, close, high, low):
    """30d trimmed mean of close_pos: drop top/bottom 10% (3 of 30)
    by index of rolling quantile. Approximated by mean of values
    between the 10th and 90th rolling percentile of cp."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    q10 = cp.rolling(30, min_periods=30).quantile(0.10)
    q90 = cp.rolling(30, min_periods=30).quantile(0.90)
    mid = cp.where((cp >= q10) & (cp <= q90))
    out = mid.rolling(30, min_periods=15).mean()
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group H: ranks and z-scores (6) --------------------------------------


def f09cp_f09_close_position_within_range_disprk_60d_base_v047_signal(closeadj, close, high, low):
    """60d percentile rank of (2*cp - 1)^2 (cp dispersion). Centered.
    Captures regime of close-position conviction rather than direction."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    disp = (2.0 * cp - 1.0) ** 2
    out = disp.rolling(60, min_periods=30).rank(pct=True) - 0.5
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpabsdrk_120d_base_v048_signal(closeadj, close, high, low):
    """120d percentile rank of |close_pos.diff(1)|. Rank of position
    CHANGE MAGNITUDE — non-monotone in signed change, so structurally
    distinct from cpdiff."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    d = cp.diff(1).abs()
    out = d.rolling(120, min_periods=60).rank(pct=True) - 0.5
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpmidvol_30d_base_v049_signal(closeadj, close, high, low):
    """30d std of (cp - 0.5). Volatility of distance-from-midpoint."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = (cp - 0.5).rolling(30, min_periods=30).std()
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpd10zsc_90d_base_v050_signal(closeadj, close, high, low):
    """90d z-score of close_pos.diff(10). Standardized 10-bar
    position drift — slower than v073's 1-bar variant."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    d = cp.diff(10)
    m = d.rolling(90, min_periods=45).mean()
    sd = d.rolling(90, min_periods=45).std().replace(0.0, np.nan)
    out = (d - m) / sd
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpiqr_50d_base_v051_signal(closeadj, close, high, low):
    """50d inter-quartile range of close_pos: Q3 - Q1. Robust spread."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    q3 = cp.rolling(50, min_periods=25).quantile(0.75)
    q1 = cp.rolling(50, min_periods=25).quantile(0.25)
    out = q3 - q1
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpquint_30d_base_v052_signal(closeadj, close, high, low):
    """30d quintile bucket index of close_pos (1..5 minus 3 centered).
    Discrete signal, no constant value over warm-up."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    q20 = cp.rolling(30, min_periods=15).quantile(0.20)
    q40 = cp.rolling(30, min_periods=15).quantile(0.40)
    q60 = cp.rolling(30, min_periods=15).quantile(0.60)
    q80 = cp.rolling(30, min_periods=15).quantile(0.80)
    bucket = pd.Series(np.nan, index=cp.index, dtype=float)
    bucket = bucket.where(cp.isna(), 3.0)
    bucket = bucket.where(cp.isna() | (cp > q20), 1.0)
    bucket = bucket.where(cp.isna() | (cp <= q20) | (cp > q40), 2.0)
    bucket = bucket.where(cp.isna() | (cp <= q60) | (cp > q80), 4.0)
    bucket = bucket.where(cp.isna() | (cp <= q80), 5.0)
    out = bucket - 3.0
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group I: midpoint / extreme proximity (6) ----------------------------


def f09cp_f09_close_position_within_range_midabs_5d_base_v053_signal(close, high, low):
    """5d mean of |close_pos - 0.5|. Distance from midpoint magnitude."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = (cp - 0.5).abs().rolling(5, min_periods=5).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_midabs_50d_base_v054_signal(closeadj, close, high, low):
    """50d mean of |close_pos - 0.5|. Long-horizon midpoint distance."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = (cp - 0.5).abs().rolling(50, min_periods=50).mean()
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_asymabs_20d_base_v055_signal(close, high, low):
    """20d mean of |asymmetry| = |h+l-2c|/(h-l). Distance-from-mid
    magnitude per bar averaged over a month."""
    rng = (high - low).replace(0.0, np.nan)
    asym = (high + low - 2.0 * close).abs() / rng
    out = asym.rolling(20, min_periods=20).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_tdvol_30d_base_v056_signal(closeadj, close, high, low):
    """30d corr between (h-c)/(h-l) and volume. Bearish-finish bars
    on heavy volume produce positive corr; light-volume bearish
    bars produce small corr. Structural form: corr, not aggregate."""
    rng = (high - low).replace(0.0, np.nan)
    td = (high - close) / rng
    vol = (np.log(close.replace(0.0, np.nan)) - np.log(close.shift(1).replace(0.0, np.nan))).abs()
    out = td.rolling(30, min_periods=15).corr(vol)
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_topdistabs_45d_base_v057_signal(closeadj, close, high, low):
    """45d mean of (h-c)*(c-l)/(h-l)^2 — a triangular bar conviction
    score peaked at cp=0.5 and zero at the extremes. Reversed-shape
    relative to cp."""
    rng = (high - low).replace(0.0, np.nan)
    tri = (high - close) * (close - low) / (rng * rng)
    out = tri.rolling(45, min_periods=45).mean()
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_extrabs_30d_base_v058_signal(closeadj, close, high, low):
    """30d fraction of bars where |cp - 0.5| > 0.4 (extreme on either
    side). Range pinning / bar conviction count."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    flag = ((cp - 0.5).abs() > 0.4).astype(float).where(cp.notna(), np.nan)
    out = flag.rolling(30, min_periods=30).sum() / 30.0
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group J: position-volatility interactions (5) ------------------------


def f09cp_f09_close_position_within_range_cpxabsret_15d_base_v059_signal(close, high, low):
    """15d mean of close_pos × |daily return| — bullish-finish bars
    receive more weight when the return is large."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    r = close.pct_change()
    out = (cp * r.abs()).rolling(15, min_periods=15).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpxret_25d_base_v060_signal(closeadj, close, high, low):
    """25d mean of (close_pos - 0.5) × return — signed: high-close
    days that are up days dominate, mid-close days vanish."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    r = close.pct_change()
    out = ((cp - 0.5) * r).rolling(25, min_periods=25).mean()
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cphighrng_20d_base_v061_signal(close, high, low):
    """20d mean of close_pos restricted to high-range bars
    (range > rolling-median range). Captures cp behavior on big bars."""
    rngraw = high - low
    rng = rngraw.replace(0.0, np.nan)
    cp = (close - low) / rng
    med = rngraw.rolling(20, min_periods=20).median()
    big = cp.where(rngraw > med)
    out = big.rolling(20, min_periods=10).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cplowrng_20d_base_v062_signal(close, high, low):
    """20d mean of close_pos restricted to low-range bars. Mean cp
    on quiet days."""
    rngraw = high - low
    rng = rngraw.replace(0.0, np.nan)
    cp = (close - low) / rng
    med = rngraw.rolling(20, min_periods=20).median()
    small = cp.where(rngraw <= med)
    out = small.rolling(20, min_periods=10).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpcondvol_30d_base_v063_signal(closeadj, close, high, low):
    """Difference: mean(cp | big-range bar) - mean(cp | small-range bar),
    over 30d. State-conditioned cp signal."""
    rngraw = high - low
    rng = rngraw.replace(0.0, np.nan)
    cp = (close - low) / rng
    med = rngraw.rolling(30, min_periods=30).median()
    big = cp.where(rngraw > med).rolling(30, min_periods=15).mean()
    small = cp.where(rngraw <= med).rolling(30, min_periods=15).mean()
    out = big - small
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group K: cross-bar consistency and patterns (8) ----------------------


def f09cp_f09_close_position_within_range_cpac1_60d_base_v064_signal(closeadj, close, high, low):
    """60d autocorrelation of close_pos at lag 1."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = cp.rolling(60, min_periods=30).corr(cp.shift(1))
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpac5_80d_base_v065_signal(closeadj, close, high, low):
    """80d autocorrelation of close_pos at lag 5."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = cp.rolling(80, min_periods=40).corr(cp.shift(5))
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_three_hi_25d_base_v066_signal(closeadj, close, high, low):
    """25d fraction of windows where cp_t > 0.7 for 3 bars in a row."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    a = (cp > 0.7).astype(float).where(cp.notna(), np.nan)
    triple = (a * a.shift(1) * a.shift(2)).where(
        a.notna() & a.shift(1).notna() & a.shift(2).notna(), np.nan
    )
    out = triple.rolling(25, min_periods=25).sum() / 25.0
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_three_lo_25d_base_v067_signal(closeadj, close, high, low):
    """25d fraction of windows where cp_t < 0.3 for 3 bars in a row."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    a = (cp < 0.3).astype(float).where(cp.notna(), np.nan)
    triple = (a * a.shift(1) * a.shift(2)).where(
        a.notna() & a.shift(1).notna() & a.shift(2).notna(), np.nan
    )
    out = triple.rolling(25, min_periods=25).sum() / 25.0
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)




def f09cp_f09_close_position_within_range_cpspan_5d_base_v069_signal(close, high, low):
    """5d (max(cp) - min(cp)). Span of close-position across a week."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = cp.rolling(5, min_periods=5).max() - cp.rolling(5, min_periods=5).min()
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpcormid_40d_base_v070_signal(closeadj, close, high, low):
    """40d correlation between cp and the bar's range (h-l). Are
    bullish closes associated with bigger bars?"""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    rngraw = high - low
    out = cp.rolling(40, min_periods=20).corr(rngraw)
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_revpat_30d_base_v071_signal(closeadj, close, high, low):
    """30d count of pattern: cp_{t-1} > 0.7 AND cp_t < 0.3 (top-then-
    bottom reversal). Normalized."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    pat = ((cp.shift(1) > 0.7) & (cp < 0.3)).astype(float).where(
        cp.notna() & cp.shift(1).notna(), np.nan
    )
    out = pat.rolling(30, min_periods=30).sum() / 30.0
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group L: smooth-vs-spot anchored signals (4) -------------------------


def f09cp_f09_close_position_within_range_dispsma_25d_base_v072_signal(closeadj, close, high, low):
    """25d mean of (2*cp - 1)^2 — average bar-conviction strength.
    High when closes consistently finish near an extreme, low when
    consistently midrange."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = ((2.0 * cp - 1.0) ** 2).rolling(25, min_periods=25).mean()
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpvolvscp_45d_base_v073_signal(closeadj, close, high, low):
    """45d corr between close_pos and (high - low) / close (range
    magnitude). Captures whether high closes happen on wide-range or
    narrow-range bars."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    relrng = (high - low) / close.replace(0.0, np.nan)
    out = cp.rolling(45, min_periods=22).corr(relrng)
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpregr_50d_base_v074_signal(closeadj, close, high, low):
    """50d OLS slope of close_pos against time (t=0..49). Captures
    drift in finishing-position over the window."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng

    def _slope(x: np.ndarray) -> float:
        if np.isnan(x).any():
            return np.nan
        n = len(x)
        t = np.arange(n, dtype=float)
        tm = t.mean()
        xm = x.mean()
        num = np.sum((t - tm) * (x - xm))
        den = np.sum((t - tm) ** 2)
        return float(num / den) if den != 0.0 else np.nan

    out = cp.rolling(50, min_periods=50).apply(_slope, raw=True)
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpmad_35d_base_v075_signal(closeadj, close, high, low):
    """35d mean-absolute-deviation of close_pos from its median.
    Robust spread measure distinct from std/IQR."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    med = cp.rolling(35, min_periods=35).median()
    out = (cp - med).abs().rolling(35, min_periods=35).mean()
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


def _e(fn, *inputs):
    return fn.__name__, {"inputs": list(inputs), "func": fn}


f09_close_position_within_range_base_001_075_REGISTRY = dict([
    _e(f09cp_f09_close_position_within_range_cp_1d_base_v001_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpdisp_1d_base_v002_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpprior_1d_base_v004_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_logodds_1d_base_v005_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpop_1d_base_v006_signal, "close", "open", "high", "low"),
    _e(f09cp_f09_close_position_within_range_op_1d_base_v007_signal, "open", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpopabs_5d_base_v008_signal, "close", "open", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpopsgn_10d_base_v009_signal, "close", "open", "high", "low"),
    _e(f09cp_f09_close_position_within_range_oppos_21d_base_v010_signal, "open", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpmean_5d_base_v011_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpmean_21d_base_v012_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpmed_63d_base_v013_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpstd_21d_base_v014_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpstd_63d_base_v015_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpskew_42d_base_v016_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpkurt_50d_base_v017_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpmax_15d_base_v018_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpmin_30d_base_v019_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cprange_45d_base_v020_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_hicnt_20d_base_v021_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_locnt_30d_base_v022_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_hilodif_40d_base_v023_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_extrhi_50d_base_v024_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_extrlo_50d_base_v025_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_midcnt_60d_base_v026_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_hilorat_30d_base_v027_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_consechi_10d_base_v028_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_streakhi_15d_base_v029_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_streaklo_15d_base_v030_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_dayssincehi_50d_base_v031_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_dayssincelo_50d_base_v032_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_midstreak_15d_base_v033_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_flipfreq_30d_base_v034_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpdiff_1d_base_v035_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpdiff_5d_base_v036_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpchgabs_10d_base_v037_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpchgsgn_20d_base_v038_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpaccdir_15d_base_v039_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpslope_30d_base_v040_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_volwcp_21d_base_v041_signal, "close", "high", "low", "volume"),
    _e(f09cp_f09_close_position_within_range_rngwcp_30d_base_v042_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_dollwcp_40d_base_v043_signal, "closeadj", "close", "high", "low", "volume"),
    _e(f09cp_f09_close_position_within_range_expwcp_10d_base_v044_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_expwcp_50d_base_v045_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_trimcp_30d_base_v046_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_disprk_60d_base_v047_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpabsdrk_120d_base_v048_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpmidvol_30d_base_v049_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpd10zsc_90d_base_v050_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpiqr_50d_base_v051_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpquint_30d_base_v052_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_midabs_5d_base_v053_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_midabs_50d_base_v054_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_asymabs_20d_base_v055_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_tdvol_30d_base_v056_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_topdistabs_45d_base_v057_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_extrabs_30d_base_v058_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpxabsret_15d_base_v059_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpxret_25d_base_v060_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cphighrng_20d_base_v061_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cplowrng_20d_base_v062_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpcondvol_30d_base_v063_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpac1_60d_base_v064_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpac5_80d_base_v065_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_three_hi_25d_base_v066_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_three_lo_25d_base_v067_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpspan_5d_base_v069_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpcormid_40d_base_v070_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_revpat_30d_base_v071_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_dispsma_25d_base_v072_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpvolvscp_45d_base_v073_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpregr_50d_base_v074_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpmad_35d_base_v075_signal, "closeadj", "close", "high", "low"),
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
    for name, entry in f09_close_position_within_range_base_001_075_REGISTRY.items():
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
    print(f"OK base_001_075: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
