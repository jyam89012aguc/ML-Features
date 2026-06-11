"""f09_close_position_within_range base features 076-150.

Second half of the close-position-within-bar-range domain. Same
constraints as 001-075. Every feature references the single-bar
close_pos = (close - low) / (high - low) or close-position-derived
aggregates. NaN policy: never `fillna(<value>)` inside any rolling
computation; only `replace([inf,-inf], nan)` at each function's final
return. Windows > 21 use `closeadj` where relevant; the single-bar
quantity itself uses unadjusted OHLC. Each feature is fully expanded.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Features 076-150.
# ---------------------------------------------------------------------------


# --- Group AA: bounded transforms / direct functions of cp (5) -------------


def f09cp_f09_close_position_within_range_sinpi_1d_base_v076_signal(close, high, low):
    """sin(pi * close_pos) — non-monotone in cp; peaks at cp=0.5,
    zero at extremes. Triangular-ish bar conviction measure."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = np.sin(np.pi * cp)
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpsmallrng_1d_base_v077_signal(close, high, low):
    """cp scaled by relative range: cp / (1 + (high-low)/close). Drops
    cp contribution when the bar's range is unusually large (small-bar
    cp dominates). Structurally orthogonal to plain cp."""
    rngraw = high - low
    rng = rngraw.replace(0.0, np.nan)
    cp = (close - low) / rng
    relrng = rngraw / close.replace(0.0, np.nan)
    out = cp / (1.0 + 50.0 * relrng)
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cubed_1d_base_v078_signal(close, high, low):
    """(2*cp - 1)^3 — emphasizes extremes; signed cubic transform."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = (2.0 * cp - 1.0) ** 3
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_relu_top_1d_base_v079_signal(close, high, low):
    """max(0, cp - 0.5): positive only when bar closes in upper half;
    zero otherwise. ReLU-style discrete bullish indicator."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = (cp - 0.5).clip(lower=0.0)
    out = out.where(cp.notna(), np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_relu_bot_1d_base_v080_signal(close, high, low):
    """max(0, 0.5 - cp): positive only when bar closes in lower half."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = (0.5 - cp).clip(lower=0.0)
    out = out.where(cp.notna(), np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group BB: cp aggregated in different ways than base 1 (8) -------------


def f09cp_f09_close_position_within_range_cpwma_15d_base_v081_signal(close, high, low):
    """Linear-weight WMA(15) of close_pos: recent bars weigh more."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    n = 15
    w = np.arange(1, n + 1, dtype=float)
    w /= w.sum()
    out = cp.rolling(n, min_periods=n).apply(lambda x: float(np.dot(x, w)), raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpgeo_30d_base_v082_signal(closeadj, close, high, low):
    """30d geometric mean of (cp + 0.01) — compresses small-cp bars
    more than the arithmetic mean. log-domain aggregate."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    shifted = (cp + 0.01).replace(0.0, np.nan)
    lcp = np.log(shifted)
    out = np.exp(lcp.rolling(30, min_periods=30).mean()) - 0.01
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cphar_25d_base_v083_signal(closeadj, close, high, low):
    """25d harmonic mean of (cp + 0.01). Penalizes near-zero cp
    values more than geometric / arithmetic."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    inv = 1.0 / (cp + 0.01).replace(0.0, np.nan)
    out = 1.0 / inv.rolling(25, min_periods=25).mean() - 0.01
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpqr10_50d_base_v084_signal(closeadj, close, high, low):
    """50d 10th percentile of close_pos — lower-tail of position
    distribution. Reaches near 0 in bear regimes."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = cp.rolling(50, min_periods=25).quantile(0.10)
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpqr90_50d_base_v085_signal(closeadj, close, high, low):
    """50d 90th percentile of close_pos — upper-tail of position
    distribution."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = cp.rolling(50, min_periods=25).quantile(0.90)
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpq90mid_60d_base_v086_signal(closeadj, close, high, low):
    """(P90 - P10) ratio: cp 90th percentile minus 10th over a 60d
    window. Robust spread measure of the position distribution."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    q90 = cp.rolling(60, min_periods=30).quantile(0.90)
    q10 = cp.rolling(60, min_periods=30).quantile(0.10)
    out = q90 - q10
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpmedabs_45d_base_v087_signal(closeadj, close, high, low):
    """45d median of |cp - 0.5|. Robust mid-distance summary;
    distinct from the MEAN equivalent."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = (cp - 0.5).abs().rolling(45, min_periods=45).median()
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpentropy_60d_base_v088_signal(closeadj, close, high, low):
    """60d Shannon-like entropy of binned cp values (5 bins). High
    when cp is uniformly distributed; low when concentrated."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng

    def _ent(x: np.ndarray) -> float:
        x = x[~np.isnan(x)]
        if len(x) < 5:
            return np.nan
        h, _ = np.histogram(x, bins=5, range=(0.0, 1.0))
        p = h / h.sum() if h.sum() > 0 else h
        nz = p[p > 0]
        return float(-(nz * np.log(nz)).sum())

    out = cp.rolling(60, min_periods=30).apply(_ent, raw=True)
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group CC: counts and ratios using different thresholds (8) -----------


def f09cp_f09_close_position_within_range_q60cnt_30d_base_v089_signal(closeadj, close, high, low):
    """30d fraction of bars with cp > 0.6 (mildly bullish closes)."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    flag = (cp > 0.6).astype(float).where(cp.notna(), np.nan)
    out = flag.rolling(30, min_periods=30).sum() / 30.0
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_q40cnt_30d_base_v090_signal(closeadj, close, high, low):
    """30d fraction of bars with cp < 0.4 (mildly bearish)."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    flag = (cp < 0.4).astype(float).where(cp.notna(), np.nan)
    out = flag.rolling(30, min_periods=30).sum() / 30.0
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_q80cnt_60d_base_v091_signal(closeadj, close, high, low):
    """60d fraction of bars with cp > 0.8."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    flag = (cp > 0.8).astype(float).where(cp.notna(), np.nan)
    out = flag.rolling(60, min_periods=60).sum() / 60.0
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_q20cnt_60d_base_v092_signal(closeadj, close, high, low):
    """60d fraction of bars with cp < 0.2."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    flag = (cp < 0.2).astype(float).where(cp.notna(), np.nan)
    out = flag.rolling(60, min_periods=60).sum() / 60.0
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_topbal_40d_base_v093_signal(closeadj, close, high, low):
    """40d ratio (cp>0.8)/(cp<0.2) using counts. (- balance)."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    hi = (cp > 0.8).astype(float).where(cp.notna(), np.nan)
    lo = (cp < 0.2).astype(float).where(cp.notna(), np.nan)
    hs = hi.rolling(40, min_periods=40).sum()
    ls = lo.rolling(40, min_periods=40).sum()
    out = (hs - ls) / (hs + ls + 2.0)
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_extrhi_10d_base_v094_signal(close, high, low):
    """10d count of bars with cp > 0.95 (close at very top)."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    flag = (cp > 0.95).astype(float).where(cp.notna(), np.nan)
    out = flag.rolling(10, min_periods=10).sum() / 10.0
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_extrlo_10d_base_v095_signal(close, high, low):
    """10d count of bars with cp < 0.05 (close at very bottom)."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    flag = (cp < 0.05).astype(float).where(cp.notna(), np.nan)
    out = flag.rolling(10, min_periods=10).sum() / 10.0
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_inside_70d_base_v096_signal(closeadj, close, high, low):
    """70d fraction of bars with 0.2 <= cp <= 0.8 — bars NOT pinned
    to the extremes. Inverse of extreme conviction."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    flag = ((cp >= 0.2) & (cp <= 0.8)).astype(float).where(cp.notna(), np.nan)
    out = flag.rolling(70, min_periods=70).sum() / 70.0
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group DD: streaks / timing (5) ---------------------------------------


def f09cp_f09_close_position_within_range_streakextrhi_20d_base_v097_signal(close, high, low):
    """Current run length (capped 20) of consecutive bars with
    cp > 0.8. Counts only EXTREME-bullish bars."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    above = (cp > 0.8).astype(float).where(cp.notna(), np.nan)
    out_vals = np.full(len(close), np.nan)
    prev = 0.0
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
        out_vals[i] = min(prev, 20.0)
    out = pd.Series(out_vals, index=close.index)
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_dayslastflip_30d_base_v098_signal(closeadj, close, high, low):
    """Days since the most recent sign flip of (cp - 0.5), capped 30."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    side = np.sign(cp - 0.5)
    flip = (side != side.shift(1)) & side.notna() & side.shift(1).notna()
    out_vals = np.full(len(close), np.nan)
    days = np.nan
    for i in range(len(close)):
        v = flip.iloc[i]
        s = side.iloc[i]
        if np.isnan(s):
            out_vals[i] = np.nan
            continue
        if v:
            days = 0.0
        elif np.isnan(days):
            days = np.nan
        else:
            days = days + 1.0
        out_vals[i] = min(days, 30.0) if not np.isnan(days) else np.nan
    out = pd.Series(out_vals, index=close.index)
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_dayssincextrhi_100d_base_v099_signal(closeadj, close, high, low):
    """Days since cp > 0.8 (capped 100). Longer-horizon analogue of v031."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    flag = (cp > 0.8).astype(float).where(cp.notna(), np.nan)
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
        out_vals[i] = min(days, 100.0) if not np.isnan(days) else np.nan
    out = pd.Series(out_vals, index=close.index)
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_runlen_above_30d_base_v100_signal(closeadj, close, high, low):
    """30d MAX run length of cp > 0.5 (longest bullish streak within
    the trailing window). Caps at 30."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    above = (cp > 0.5).astype(int).where(cp.notna(), np.nan)
    # rolling max of streak
    streak_arr = np.full(len(close), np.nan)
    prev = 0
    streaks = []
    for i in range(len(close)):
        v = above.iloc[i]
        if np.isnan(v):
            streaks.append(np.nan)
            prev = 0
            continue
        if v >= 1:
            prev = prev + 1
        else:
            prev = 0
        streaks.append(prev)
    s = pd.Series(streaks, index=close.index, dtype=float)
    out = s.rolling(30, min_periods=15).max()
    _ = streak_arr
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_runlen_below_30d_base_v101_signal(closeadj, close, high, low):
    """30d max run length of cp < 0.5."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    below = (cp < 0.5).astype(int).where(cp.notna(), np.nan)
    streaks = []
    prev = 0
    for i in range(len(close)):
        v = below.iloc[i]
        if np.isnan(v):
            streaks.append(np.nan)
            prev = 0
            continue
        if v >= 1:
            prev = prev + 1
        else:
            prev = 0
        streaks.append(prev)
    s = pd.Series(streaks, index=close.index, dtype=float)
    out = s.rolling(30, min_periods=15).max()
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group EE: position momentum / velocity (7) ---------------------------


def f09cp_f09_close_position_within_range_cpmom_10d_base_v102_signal(close, high, low):
    """cp - cp.shift(10): 10-bar position momentum."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = cp - cp.shift(10)
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpmom_21d_base_v103_signal(close, high, low):
    """cp - cp.shift(21): 21-bar position momentum."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = cp - cp.shift(21)
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpaccdir_30d_base_v104_signal(closeadj, close, high, low):
    """30d count of bars where sign(cp.diff(1)) AGREES with the
    direction over the prior 5 (sign of cp.diff(5))."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    short_dir = np.sign(cp.diff(1))
    long_dir = np.sign(cp.diff(5))
    agree = (short_dir == long_dir).astype(float).where(
        short_dir.notna() & long_dir.notna() & (short_dir != 0) & (long_dir != 0), np.nan
    )
    out = agree.rolling(30, min_periods=30).sum() / 30.0 - 0.5
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpaccel_25d_base_v105_signal(closeadj, close, high, low):
    """25d mean of (cp - 2*cp.shift(5) + cp.shift(10)) — 2nd-diff
    structure averaged. Position acceleration."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    j = cp - 2.0 * cp.shift(5) + cp.shift(10)
    out = j.rolling(25, min_periods=25).mean()
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpup10_30d_base_v106_signal(closeadj, close, high, low):
    """30d count of bars where cp_t > cp_{t-1} (rising-position
    bars). Normalized to [0,1]."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    up = (cp > cp.shift(1)).astype(float).where(cp.notna() & cp.shift(1).notna(), np.nan)
    out = up.rolling(30, min_periods=30).sum() / 30.0
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpzigzag_45d_base_v107_signal(closeadj, close, high, low):
    """45d count of pattern: cp_{t-1} > cp_{t-2} AND cp_t < cp_{t-1}
    (peak), normalized — captures zigzag tops."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    pk = ((cp.shift(1) > cp.shift(2)) & (cp < cp.shift(1))).astype(float).where(
        cp.notna() & cp.shift(1).notna() & cp.shift(2).notna(), np.nan
    )
    out = pk.rolling(45, min_periods=45).sum() / 45.0
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpdrift_60d_base_v108_signal(closeadj, close, high, low):
    """60d (mean of cp.diff(1)) — average per-bar drift in close
    position over the trailing window."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = cp.diff(1).rolling(60, min_periods=60).mean()
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group FF: weighted/conditional aggregates (6) ------------------------


def f09cp_f09_close_position_within_range_voldot_30d_base_v109_signal(closeadj, close, high, low, volume):
    """30d rolling correlation of (cp - 0.5) with log-volume —
    captures volume-association with bullish/bearish bar finishes."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    lv = np.log(volume.replace(0.0, np.nan))
    out = (cp - 0.5).rolling(30, min_periods=15).corr(lv)
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cphivol_40d_base_v110_signal(closeadj, close, high, low, volume):
    """40d mean of cp restricted to high-volume bars (vol > rolling
    median). Captures cp behavior on heavy-volume bars."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    med = volume.rolling(40, min_periods=20).median()
    big = cp.where(volume > med)
    out = big.rolling(40, min_periods=15).mean()
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cplowvol_40d_base_v111_signal(closeadj, close, high, low, volume):
    """40d mean of cp on low-volume bars (vol < rolling median)."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    med = volume.rolling(40, min_periods=20).median()
    small = cp.where(volume <= med)
    out = small.rolling(40, min_periods=15).mean()
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpcondvret_50d_base_v112_signal(closeadj, close, high, low):
    """50d (mean(cp on up-day) - mean(cp on down-day)). State-
    conditioned position; captures cp asymmetry on rallies vs sells."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    r = close.pct_change()
    up = cp.where(r > 0)
    dn = cp.where(r < 0)
    out = up.rolling(50, min_periods=20).mean() - dn.rolling(50, min_periods=20).mean()
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpgap_30d_base_v113_signal(closeadj, close, high, low):
    """30d mean of cp on bars that gapped up vs gapped down.
    Difference: mean(cp | gap-up) - mean(cp | gap-down). Captures
    gap-related bar-finish behavior."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    gap = close.shift(0)  # placeholder
    _ = gap
    prev_c = close.shift(1)
    up_gap = cp.where(low > prev_c)
    dn_gap = cp.where(high < prev_c)
    out = up_gap.rolling(30, min_periods=10).mean() - dn_gap.rolling(30, min_periods=10).mean()
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpwgttd_50d_base_v114_signal(closeadj, close, high, low):
    """50d range-weighted mean of (cp - 0.5) — sign-aware aggregate
    where wide bars get more weight."""
    rngraw = high - low
    rng = rngraw.replace(0.0, np.nan)
    cp = (close - low) / rng
    num = ((cp - 0.5) * rngraw).rolling(50, min_periods=50).sum()
    den = rngraw.rolling(50, min_periods=50).sum().replace(0.0, np.nan)
    out = num / den
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group GG: spread / shape (6) -----------------------------------------


def f09cp_f09_close_position_within_range_cpvar_15d_base_v115_signal(close, high, low):
    """15d variance of close_pos. Shorter than v014 (21d)."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = cp.rolling(15, min_periods=15).var()
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpskewsg_30d_base_v116_signal(closeadj, close, high, low):
    """Sign of 30d skew of cp."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    sk = cp.rolling(30, min_periods=30).skew()
    out = np.sign(sk).where(sk.notna(), np.nan)
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpkurtsg_50d_base_v117_signal(closeadj, close, high, low):
    """Sign of (kurt - 3) of cp over 50d — heavy- or light-tailed
    indicator."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    k = cp.rolling(50, min_periods=50).kurt()
    out = np.sign(k).where(k.notna(), np.nan)
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpmadrel_40d_base_v118_signal(closeadj, close, high, low):
    """40d MAD/IQR ratio of cp. Distinct shape signal: ratio of
    different spread measures."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    med = cp.rolling(40, min_periods=40).median()
    mad = (cp - med).abs().rolling(40, min_periods=40).mean()
    iqr = (cp.rolling(40, min_periods=20).quantile(0.75) - cp.rolling(40, min_periods=20).quantile(0.25)).replace(0.0, np.nan)
    out = mad / iqr
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpcv_50d_base_v119_signal(closeadj, close, high, low):
    """50d coefficient of variation: std(cp)/mean(cp)."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    m = cp.rolling(50, min_periods=50).mean().replace(0.0, np.nan)
    sd = cp.rolling(50, min_periods=50).std()
    out = sd / m
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpoctile_75d_base_v120_signal(closeadj, close, high, low):
    """75d octile of close_pos as integer 1..8 minus 4.5 (centered).
    Discrete-bin rank signal."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    rk = cp.rolling(75, min_periods=38).rank(pct=True)
    oct_ = np.ceil(rk * 8.0).where(rk.notna(), np.nan)
    out = oct_ - 4.5
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group HH: cross-bar autocorr / patterns (6) --------------------------


def f09cp_f09_close_position_within_range_cpac3_70d_base_v121_signal(closeadj, close, high, low):
    """70d autocorrelation of cp at lag 3."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = cp.rolling(70, min_periods=35).corr(cp.shift(3))
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpac10_100d_base_v122_signal(closeadj, close, high, low):
    """100d autocorrelation of cp at lag 10."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = cp.rolling(100, min_periods=50).corr(cp.shift(10))
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_revpatlo_45d_base_v123_signal(closeadj, close, high, low):
    """45d count of pattern: cp_{t-1} < 0.3 AND cp_t > 0.7 (bottom-
    then-top reversal). Normalized."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    pat = ((cp.shift(1) < 0.3) & (cp > 0.7)).astype(float).where(
        cp.notna() & cp.shift(1).notna(), np.nan
    )
    out = pat.rolling(45, min_periods=45).sum() / 45.0
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_threein_40d_base_v124_signal(closeadj, close, high, low):
    """40d fraction of windows where 3 bars in a row are inside 0.4-
    0.6 (mid-range cluster)."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    flag = ((cp >= 0.4) & (cp <= 0.6)).astype(float).where(cp.notna(), np.nan)
    triple = (flag * flag.shift(1) * flag.shift(2)).where(
        flag.notna() & flag.shift(1).notna() & flag.shift(2).notna(), np.nan
    )
    out = triple.rolling(40, min_periods=40).sum() / 40.0
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpparity_30d_base_v125_signal(closeadj, close, high, low):
    """30d (mean(cp on even bars) - mean(cp on odd bars)). Tests
    pseudo-alternation in cp."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    idx = pd.Series(np.arange(len(cp)), index=cp.index, dtype=float)
    even = cp.where(idx % 2 == 0)
    odd = cp.where(idx % 2 == 1)
    out = even.rolling(30, min_periods=15).mean() - odd.rolling(30, min_periods=15).mean()
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpsd2bar_50d_base_v126_signal(closeadj, close, high, low):
    """50d std of 2-bar mean of cp ((cp_t + cp_{t-1})/2). Compared
    to v014 (std of single-bar cp), this smooths first."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    sm = (cp + cp.shift(1)) / 2.0
    out = sm.rolling(50, min_periods=50).std()
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group II: position vs prior-bar range / anchored (5) ----------------


def f09cp_f09_close_position_within_range_prevrngavg_20d_base_v127_signal(close, high, low):
    """20d mean of (close - low.shift(1)) / (high.shift(1) -
    low.shift(1)). Average position of today's close inside YESTERDAY's
    bar range — can exceed [0,1] on expansions."""
    prng = (high.shift(1) - low.shift(1)).replace(0.0, np.nan)
    p = (close - low.shift(1)) / prng
    out = p.rolling(20, min_periods=20).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_prevrngabv_30d_base_v128_signal(closeadj, close, high, low):
    """30d fraction of bars where close > high.shift(1) — close
    exceeded yesterday's high, an extreme up-position relative to
    prior bar."""
    above = (close > high.shift(1)).astype(float).where(close.shift(1).notna(), np.nan)
    out = above.rolling(30, min_periods=30).sum() / 30.0
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_prevrngblw_30d_base_v129_signal(closeadj, close, high, low):
    """30d fraction of bars where close < low.shift(1) — close
    below yesterday's low."""
    below = (close < low.shift(1)).astype(float).where(close.shift(1).notna(), np.nan)
    out = below.rolling(30, min_periods=30).sum() / 30.0
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_2barhilo_50d_base_v130_signal(closeadj, close, high, low):
    """50d mean of (close - 2-bar low) / (2-bar high - 2-bar low). A
    2-bar-windowed close-position; still single-bar-style aggregate
    but uses a 2-bar reference range."""
    h2 = high.rolling(2, min_periods=2).max()
    l2 = low.rolling(2, min_periods=2).min()
    pp = (close - l2) / (h2 - l2).replace(0.0, np.nan)
    out = pp.rolling(50, min_periods=50).mean()
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_3barhilo_30d_base_v131_signal(closeadj, close, high, low):
    """30d std of (close - 3-bar low)/(3-bar high - 3-bar low)."""
    h3 = high.rolling(3, min_periods=3).max()
    l3 = low.rolling(3, min_periods=3).min()
    pp = (close - l3) / (h3 - l3).replace(0.0, np.nan)
    out = pp.rolling(30, min_periods=30).std()
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group JJ: regression / anchored statistics (6) -----------------------


def f09cp_f09_close_position_within_range_cpregr_25d_base_v132_signal(close, high, low):
    """25d OLS slope of close_pos against time."""
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

    out = cp.rolling(25, min_periods=25).apply(_slope, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpr2_40d_base_v133_signal(closeadj, close, high, low):
    """40d R^2 of cp vs time. Strength of linear position trend."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng

    def _r2(x: np.ndarray) -> float:
        if np.isnan(x).any():
            return np.nan
        n = len(x)
        t = np.arange(n, dtype=float)
        tm = t.mean()
        xm = x.mean()
        num = np.sum((t - tm) * (x - xm))
        den_t = np.sum((t - tm) ** 2)
        den_x = np.sum((x - xm) ** 2)
        if den_t == 0.0 or den_x == 0.0:
            return np.nan
        r = num / np.sqrt(den_t * den_x)
        return float(r * r)

    out = cp.rolling(40, min_periods=40).apply(_r2, raw=True)
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cphurst_80d_base_v134_signal(closeadj, close, high, low):
    """Approximate Hurst exponent of cp over 80 bars via rescaled-
    range. Distinguishes mean-reverting vs trending close positions."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng

    def _h(x: np.ndarray) -> float:
        x = x[~np.isnan(x)]
        if len(x) < 30:
            return np.nan
        y = x - x.mean()
        z = y.cumsum()
        r = z.max() - z.min()
        s = x.std()
        if s == 0.0 or r == 0.0:
            return np.nan
        return float(np.log(r / s) / np.log(len(x)))

    out = cp.rolling(80, min_periods=40).apply(_h, raw=True)
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpdrawup_60d_base_v135_signal(closeadj, close, high, low):
    """60d max drawup of cumulative (cp - 0.5): how much positive bar-
    finishing has accumulated minus the running min, scaled by 60."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    cum = (cp - 0.5).cumsum()
    drawup = cum - cum.rolling(60, min_periods=60).min()
    out = drawup / 60.0
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpdrawdn_60d_base_v136_signal(closeadj, close, high, low):
    """60d max drawdown of cumulative (cp - 0.5)."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    cum = (cp - 0.5).cumsum()
    drawdn = cum.rolling(60, min_periods=60).max() - cum
    out = drawdn / 60.0
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpsharpe_45d_base_v137_signal(closeadj, close, high, low):
    """45d mean(cp - 0.5) / std(cp). Position 'Sharpe ratio' — how
    persistently and cleanly the bars finish on one side."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    m = (cp - 0.5).rolling(45, min_periods=45).mean()
    sd = cp.rolling(45, min_periods=45).std().replace(0.0, np.nan)
    out = m / sd
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group KK: cross-class composite / volatility (5) --------------------


def f09cp_f09_close_position_within_range_cpvxret_30d_base_v138_signal(closeadj, close, high, low):
    """30d corr between cp and same-bar return — does a high cp
    typically coincide with an up day?"""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    r = close.pct_change()
    out = cp.rolling(30, min_periods=15).corr(r)
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpvxnret_25d_base_v139_signal(closeadj, close, high, low):
    """25d corr between cp and NEXT-bar return (cp leads r). Tests
    forward predictive structure (synthetic data; small)."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    rfwd = close.pct_change().shift(-1)
    out = cp.rolling(25, min_periods=15).corr(rfwd)
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpemavar_40d_base_v140_signal(closeadj, close, high, low):
    """40d EW variance of cp (span=20). Smoother volatility."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = cp.ewm(span=20, adjust=False, min_periods=20).var()
    _ = closeadj
    # apply 40d rolling to bound vintage
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpsignmom_45d_base_v141_signal(closeadj, close, high, low):
    """45d mean of sign(cp - 0.5). Discrete sign-only aggregate; loses
    magnitude information so it is structurally distinct from mean(cp)
    or sharpe(cp)."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    s = np.sign(cp - 0.5).where(cp.notna(), np.nan)
    out = s.rolling(45, min_periods=45).mean()
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpvolclip_60d_base_v142_signal(closeadj, close, high, low):
    """60d mean of clip(cp - 0.5, -0.25, 0.25). Winsorized signed
    midpoint deviation — bounded aggregate distinct from raw mean."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    clipped = (cp - 0.5).clip(-0.25, 0.25)
    out = clipped.rolling(60, min_periods=60).mean()
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group LL: midpoint cross / extremes (4) ------------------------------


def f09cp_f09_close_position_within_range_midcross_50d_base_v143_signal(closeadj, close, high, low):
    """50d count of midpoint crossings: sign(cp-0.5) changes."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    s = np.sign(cp - 0.5)
    cross = (s != s.shift(1)).astype(float).where(s.notna() & s.shift(1).notna(), np.nan)
    out = cross.rolling(50, min_periods=50).sum() / 50.0
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_clipupsum_25d_base_v144_signal(close, high, low):
    """25d mean of max(0, cp - 0.7) (upper-tail clipped score)."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    score = (cp - 0.7).clip(lower=0.0).where(cp.notna(), np.nan)
    out = score.rolling(25, min_periods=25).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_clipdnsum_25d_base_v145_signal(close, high, low):
    """25d mean of max(0, 0.3 - cp) (lower-tail clipped score)."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    score = (0.3 - cp).clip(lower=0.0).where(cp.notna(), np.nan)
    out = score.rolling(25, min_periods=25).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_extremes_70d_base_v146_signal(closeadj, close, high, low):
    """70d (count of cp>0.9) - (count of cp<0.1), normalized. Pure
    extreme-conviction balance."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    hi = (cp > 0.9).astype(float).where(cp.notna(), np.nan)
    lo = (cp < 0.1).astype(float).where(cp.notna(), np.nan)
    out = (hi - lo).rolling(70, min_periods=70).sum() / 70.0
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group MM: closing-strength composites (4) ----------------------------


def f09cp_f09_close_position_within_range_csmix_30d_base_v147_signal(closeadj, close, high, low):
    """30d mean of [cp × (1 if return>0 else -1)] — signed bar
    finish strength scaled by daily direction."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    r = close.pct_change()
    s = np.sign(r)
    out = (cp * s).rolling(30, min_periods=30).mean()
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_csmix_lo_30d_base_v148_signal(closeadj, close, high, low):
    """30d mean of [(1-cp) × (1 if return<0 else 0)] — bear-bar
    bearish-finish strength."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    r = close.pct_change()
    mask = (r < 0).astype(float).where(r.notna(), np.nan)
    out = ((1.0 - cp) * mask).rolling(30, min_periods=30).mean()
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpprdsign_45d_base_v149_signal(closeadj, close, high, low):
    """45d count of bars where (close > open) AND cp > 0.6 (intra-bar
    rally that closes near the top). Normalized."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out_vals = ((close > close.shift(1)) & (cp > 0.6)).astype(float).where(cp.notna(), np.nan)
    out = out_vals.rolling(45, min_periods=45).sum() / 45.0
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


def f09cp_f09_close_position_within_range_cpcorrop_40d_base_v150_signal(closeadj, close, open, high, low):
    """40d corr between cp and open_pos. Does the open position
    predict the close position systematically?"""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    op = (open - low) / rng
    out = cp.rolling(40, min_periods=20).corr(op)
    _ = closeadj
    return out.replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


def _e(fn, *inputs):
    return fn.__name__, {"inputs": list(inputs), "func": fn}


f09_close_position_within_range_base_076_150_REGISTRY = dict([
    _e(f09cp_f09_close_position_within_range_sinpi_1d_base_v076_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpsmallrng_1d_base_v077_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cubed_1d_base_v078_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_relu_top_1d_base_v079_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_relu_bot_1d_base_v080_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpwma_15d_base_v081_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpgeo_30d_base_v082_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cphar_25d_base_v083_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpqr10_50d_base_v084_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpqr90_50d_base_v085_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpq90mid_60d_base_v086_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpmedabs_45d_base_v087_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpentropy_60d_base_v088_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_q60cnt_30d_base_v089_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_q40cnt_30d_base_v090_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_q80cnt_60d_base_v091_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_q20cnt_60d_base_v092_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_topbal_40d_base_v093_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_extrhi_10d_base_v094_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_extrlo_10d_base_v095_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_inside_70d_base_v096_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_streakextrhi_20d_base_v097_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_dayslastflip_30d_base_v098_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_dayssincextrhi_100d_base_v099_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_runlen_above_30d_base_v100_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_runlen_below_30d_base_v101_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpmom_10d_base_v102_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpmom_21d_base_v103_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpaccdir_30d_base_v104_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpaccel_25d_base_v105_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpup10_30d_base_v106_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpzigzag_45d_base_v107_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpdrift_60d_base_v108_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_voldot_30d_base_v109_signal, "closeadj", "close", "high", "low", "volume"),
    _e(f09cp_f09_close_position_within_range_cphivol_40d_base_v110_signal, "closeadj", "close", "high", "low", "volume"),
    _e(f09cp_f09_close_position_within_range_cplowvol_40d_base_v111_signal, "closeadj", "close", "high", "low", "volume"),
    _e(f09cp_f09_close_position_within_range_cpcondvret_50d_base_v112_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpgap_30d_base_v113_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpwgttd_50d_base_v114_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpvar_15d_base_v115_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpskewsg_30d_base_v116_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpkurtsg_50d_base_v117_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpmadrel_40d_base_v118_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpcv_50d_base_v119_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpoctile_75d_base_v120_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpac3_70d_base_v121_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpac10_100d_base_v122_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_revpatlo_45d_base_v123_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_threein_40d_base_v124_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpparity_30d_base_v125_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpsd2bar_50d_base_v126_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_prevrngavg_20d_base_v127_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_prevrngabv_30d_base_v128_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_prevrngblw_30d_base_v129_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_2barhilo_50d_base_v130_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_3barhilo_30d_base_v131_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpregr_25d_base_v132_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpr2_40d_base_v133_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cphurst_80d_base_v134_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpdrawup_60d_base_v135_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpdrawdn_60d_base_v136_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpsharpe_45d_base_v137_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpvxret_30d_base_v138_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpvxnret_25d_base_v139_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpemavar_40d_base_v140_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpsignmom_45d_base_v141_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpvolclip_60d_base_v142_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_midcross_50d_base_v143_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_clipupsum_25d_base_v144_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_clipdnsum_25d_base_v145_signal, "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_extremes_70d_base_v146_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_csmix_30d_base_v147_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_csmix_lo_30d_base_v148_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpprdsign_45d_base_v149_signal, "closeadj", "close", "high", "low"),
    _e(f09cp_f09_close_position_within_range_cpcorrop_40d_base_v150_signal, "closeadj", "close", "open", "high", "low"),
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
    for name, entry in f09_close_position_within_range_base_076_150_REGISTRY.items():
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
