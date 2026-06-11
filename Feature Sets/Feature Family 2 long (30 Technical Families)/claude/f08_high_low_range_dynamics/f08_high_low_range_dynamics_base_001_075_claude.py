"""f08_high_low_range_dynamics base features 001-075.

Domain: how the bar range (high - low) and true range evolve over time.
Every feature references `high`, `low`, and possibly `close.shift(1)`.

Core quantities:
  range = high - low
  true range = max(high - low, |high - close.shift(1)|, |low - close.shift(1)|)
  relative range = (high - low) / close
  log range = log(high) - log(low)

NOT MA features, NOT channel position, NOT candle body ratios. The
features focus on dynamics of range itself: levels, expansion, contraction,
distribution shape, percentile rank, regimes, and discrete patterns
(inside/outside, NR4/NR7, WR4/WR7).

NaN policy: never fillna(0); only replace([inf,-inf], nan) at return.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Helpers used by features (each feature still inlines its own formula).
# ---------------------------------------------------------------------------


def _tr(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    pc = close.shift(1)
    a = (high - low).abs()
    b = (high - pc).abs()
    c = (low - pc).abs()
    return pd.concat([a, b, c], axis=1).max(axis=1)


def _wilder(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()


# ---------------------------------------------------------------------------
# Features 001-075
# ---------------------------------------------------------------------------


# --- Group A: relative range levels (few, widely spaced) -------------------


def f08hl_f08_high_low_range_dynamics_relrng_1d_base_v001_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-bar mean of (high-low)/close. Smoothed short-horizon relative range."""
    rr = (high - low) / close.replace(0.0, np.nan)
    out = rr.rolling(5, min_periods=5).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_relrngmean_21d_base_v002_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-bar mean of (high-low)/close."""
    r = (high - low) / close.replace(0.0, np.nan)
    out = r.rolling(21, min_periods=21).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_relrngmean_100d_base_v003_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """100-bar mean of (high-low)/closeadj. Long-horizon range level."""
    r = (high - low) / closeadj.replace(0.0, np.nan)
    out = r.rolling(100, min_periods=100).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group B: log range ----------------------------------------------------


def f08hl_f08_high_low_range_dynamics_logrng_1d_base_v004_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """log(high) - log(low). Per-bar log range."""
    out = np.log(high.replace(0.0, np.nan)) - np.log(low.replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_logrngmean_50d_base_v005_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """50-bar mean of log(high)-log(low)."""
    lr = np.log(high.replace(0.0, np.nan)) - np.log(low.replace(0.0, np.nan))
    out = lr.rolling(50, min_periods=50).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group C: ATR / true range ---------------------------------------------


def f08hl_f08_high_low_range_dynamics_atrwild_14d_base_v006_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Wilder ATR(14) normalized by close. Classic volatility measure."""
    pc = close.shift(1)
    a = (high - low).abs(); b = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, b, c], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    out = atr / close.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_atrsma_50d_base_v007_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """SMA-based ATR(50)/closeadj. Smoother long-horizon true range level."""
    pc = closeadj.shift(1)
    a = (high - low).abs(); b = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, b, c], axis=1).max(axis=1)
    atr = tr.rolling(50, min_periods=50).mean()
    out = atr / closeadj.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_atrrng_30d_base_v008_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """SMA(range,5) / Wilder ATR(30). Smoothed range vs smoothed ATR.
    Tells how recent 5-bar avg compares to slow ATR baseline."""
    pc = closeadj.shift(1)
    a = (high - low).abs(); b = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, b, c], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 30.0, adjust=False, min_periods=30).mean()
    rng5 = (high - low).rolling(5, min_periods=5).mean()
    out = rng5 / atr.replace(0.0, np.nan)
    return np.log(out).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_normrng_20d_base_v009_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """SMA(range,3) / SMA(range,80). Smoothed-bar 3 vs long-baseline 80
    range ratio. Wide-window normalization breaks correlation with single-
    bar features."""
    rng = high - low
    s3 = rng.rolling(3, min_periods=3).mean()
    s80 = rng.rolling(80, min_periods=80).mean()
    out = s3 / s80.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_trrngrat_1d_base_v010_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """TR / range = how much of true range is overnight gap component."""
    pc = close.shift(1)
    a = (high - low).abs(); b = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, b, c], axis=1).max(axis=1)
    rng = (high - low).replace(0.0, np.nan)
    out = tr / rng
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group D: range dynamics (expansion vs contraction) --------------------


def f08hl_f08_high_low_range_dynamics_rngexp_10d_base_v011_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """log(range / SMA(range, 10)). Symmetric expansion/contraction."""
    rng = (high - low).replace(0.0, np.nan)
    sma = rng.rolling(10, min_periods=10).mean()
    out = np.log(rng / sma.replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngslope_20d_base_v012_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """SMA(range,20).diff(5) / SMA(range,20). Slope of mean range path."""
    rng = high - low
    sma = rng.rolling(20, min_periods=20).mean()
    out = sma.diff(5) / sma.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngcurv_30d_base_v013_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Curvature of SMA(range,30): r - 2*r.shift(5) + r.shift(10) all /r."""
    rng = high - low
    sma = rng.rolling(30, min_periods=30).mean()
    cur = sma - 2.0 * sma.shift(5) + sma.shift(10)
    out = cur / sma.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_volofrng_30d_base_v014_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """std(range, 30) / mean(range, 30). Vol-of-vol of range."""
    rng = high - low
    m = rng.rolling(30, min_periods=30).mean()
    s = rng.rolling(30, min_periods=30).std()
    out = s / m.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngac_30d_base_v015_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """30-bar autocorr of range at lag 1. Persistence of range."""
    rng = (high - low).replace(0.0, np.nan)
    lr = np.log(rng)
    out = lr.rolling(30, min_periods=30).corr(lr.shift(1))
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group E: range distribution (rank / z / shape) ------------------------


def f08hl_f08_high_low_range_dynamics_rngrnk_63d_base_v016_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of SMA(range, 21) in trailing 63 bars. Smoothed range
    rank — distinct from raw-bar rank by averaging out single-bar spikes."""
    rng = high - low
    sm = rng.rolling(21, min_periods=21).mean()
    out = sm.rolling(63, min_periods=40).rank(pct=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngzs_40d_base_v017_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """corr of log(range) with log(closeadj) over 40 bars. Tells whether
    range expands as price goes up (linear regime) or compresses (range
    decoupled from level)."""
    rng = (high - low).replace(0.0, np.nan)
    lr = np.log(rng)
    lc = np.log(closeadj.replace(0.0, np.nan))
    out = lr.rolling(40, min_periods=40).corr(lc)
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngsk_60d_base_v018_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Skewness of range distribution over trailing 60 bars."""
    rng = high - low
    out = rng.rolling(60, min_periods=60).skew()
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngkur_60d_base_v019_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Kurtosis of range distribution over trailing 60 bars."""
    rng = high - low
    out = rng.rolling(60, min_periods=60).kurt()
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngmadr_30d_base_v020_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """MAD/std ratio for range in 30-bar window. Tail-fatness proxy."""
    rng = high - low
    m = rng.rolling(30, min_periods=30).mean()
    mad = (rng - m).abs().rolling(30, min_periods=30).mean()
    sd = rng.rolling(30, min_periods=30).std()
    out = mad / sd.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group F: TR-specific features -----------------------------------------


def f08hl_f08_high_low_range_dynamics_trrnk_50d_base_v021_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """TR percentile rank in trailing 50 bars."""
    pc = closeadj.shift(1)
    a = (high - low).abs(); b = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, b, c], axis=1).max(axis=1)
    out = tr.rolling(50, min_periods=30).rank(pct=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_trzs_30d_base_v022_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """log(TR) - log(range) — per-bar gap-component magnitude on log scale.
    Distinct from gapcontr's 30-bar mean by being un-smoothed and bar-level."""
    pc = closeadj.shift(1)
    a = (high - low).abs(); b = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, b, c], axis=1).max(axis=1).replace(0.0, np.nan)
    rng = (high - low).replace(0.0, np.nan)
    out = np.log(tr) - np.log(rng)
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_wildvssma_30d_base_v023_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """log(Wilder ATR(14)) - log(SMA(TR, 30)). Lag differential between
    smoothers — reveals momentum of true range."""
    pc = closeadj.shift(1)
    a = (high - low).abs(); b = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, b, c], axis=1).max(axis=1)
    w = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    s = tr.rolling(30, min_periods=30).mean()
    out = np.log(w.replace(0.0, np.nan)) - np.log(s.replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group G: current vs prior bar / trailing max --------------------------


def f08hl_f08_high_low_range_dynamics_rngprior_1d_base_v024_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """log(range / range.shift(1)). Current vs prior bar range ratio."""
    rng = (high - low).replace(0.0, np.nan)
    out = np.log(rng / rng.shift(1).replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngtmax_20d_base_v025_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """range / max(range, 20).shift(1). > 1 means breaking out of recent
    high-vol cluster."""
    rng = high - low
    mx = rng.rolling(20, min_periods=20).max().shift(1)
    out = rng / mx.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngtmin_20d_base_v026_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """range / min(range, 20).shift(1). Compression breakout proxy."""
    rng = (high - low).replace(0.0, np.nan)
    mn = rng.rolling(20, min_periods=20).min().shift(1)
    out = rng / mn.replace(0.0, np.nan)
    out = np.log(out)
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngstrkabv_30d_base_v027_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Running streak: # consecutive bars with range > SMA(range, 30)."""
    rng = high - low
    sma = rng.rolling(30, min_periods=30).mean()
    above = (rng > sma).astype(float).where(~sma.isna())
    grp = (above != above.shift()).cumsum()
    streak = above.groupby(grp).cumcount() + 1
    out = (streak * above).where(~sma.isna())
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group H: discrete bar patterns (inside / outside / NR / WR) -----------


def f08hl_f08_high_low_range_dynamics_insidebr_1d_base_v028_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Inside bar: high<high.shift(1) AND low>low.shift(1). 1/0 indicator."""
    flag = (high < high.shift(1)) & (low > low.shift(1))
    out = flag.astype(float).where(~high.shift(1).isna() & ~low.shift(1).isna())
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_outsidebr_1d_base_v029_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Outside bar: high>high.shift(1) AND low<low.shift(1). 1/0 indicator."""
    flag = (high > high.shift(1)) & (low < low.shift(1))
    out = flag.astype(float).where(~high.shift(1).isna() & ~low.shift(1).isna())
    return out.replace([np.inf, -np.inf], np.nan)






def f08hl_f08_high_low_range_dynamics_wr4_1d_base_v032_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """WR4: widest range of last 4. 1/0."""
    rng = high - low
    mxrng = rng.rolling(4, min_periods=4).max()
    flag = (rng >= mxrng - 1e-12).astype(float).where(~mxrng.isna())
    return flag.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_wr7_1d_base_v033_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """WR7: widest range of last 7. 1/0."""
    rng = high - low
    mxrng = rng.rolling(7, min_periods=7).max()
    flag = (rng >= mxrng - 1e-12).astype(float).where(~mxrng.isna())
    return flag.replace([np.inf, -np.inf], np.nan)






def f08hl_f08_high_low_range_dynamics_nr7cnt_50d_base_v036_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of NR7 bars in trailing 50."""
    rng = high - low
    minrng = rng.rolling(7, min_periods=7).min()
    flag = (rng <= minrng + 1e-12).astype(float).where(~minrng.isna())
    out = flag.rolling(50, min_periods=30).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_wr7cnt_50d_base_v037_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of WR7 bars in trailing 50."""
    rng = high - low
    mxrng = rng.rolling(7, min_periods=7).max()
    flag = (rng >= mxrng - 1e-12).astype(float).where(~mxrng.isna())
    out = flag.rolling(50, min_periods=30).sum()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group I: range squeeze / expansion regimes ----------------------------


def f08hl_f08_high_low_range_dynamics_sqz_60d_base_v038_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Squeeze indicator: 1 if SMA(range,10) in bottom decile of trailing 60.
    Continuous: percentile rank of SMA(range,10) within 60."""
    rng = high - low
    sma = rng.rolling(10, min_periods=10).mean()
    out = sma.rolling(60, min_periods=40).rank(pct=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_xpan_40d_base_v039_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Slope-of-vol-of-range: std(range,10).diff(5) / std(range,10).
    Captures whether range volatility itself is rising or falling."""
    rng = high - low
    s10 = rng.rolling(10, min_periods=10).std()
    out = s10.diff(5) / s10.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group J: cross-window range comparisons -------------------------------


def f08hl_f08_high_low_range_dynamics_rngrat_short_base_v040_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """log(SMA(range,5)) - log(SMA(range,21)). Differential level
    (short over mid). Nulls absolute range drift."""
    rng = (high - low).replace(0.0, np.nan)
    s5 = rng.rolling(5, min_periods=5).mean()
    s21 = rng.rolling(21, min_periods=21).mean()
    out = np.log(s5.replace(0.0, np.nan)) - np.log(s21.replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngrat_long_base_v041_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """log(SMA(range,21)) - log(SMA(range,100)). Mid vs long differential."""
    rng = (high - low).replace(0.0, np.nan)
    s21 = rng.rolling(21, min_periods=21).mean()
    s100 = rng.rolling(100, min_periods=100).mean()
    out = np.log(s21.replace(0.0, np.nan)) - np.log(s100.replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngslpdiff_30d_base_v042_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Short slope - long slope: slope(SMA(range,10),3)/.. - slope(SMA(range,30),10)/..
    Captures whether range path is accelerating."""
    rng = high - low
    s10 = rng.rolling(10, min_periods=10).mean()
    s30 = rng.rolling(30, min_periods=30).mean()
    short_slp = s10.diff(3) / s10.replace(0.0, np.nan)
    long_slp = s30.diff(10) / s30.replace(0.0, np.nan)
    out = short_slp - long_slp
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group K: sum / cumulative / correlation -------------------------------


def f08hl_f08_high_low_range_dynamics_rngsum_30d_base_v043_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Sum of ranges in 30 bars / closeadj. Total range over horizon."""
    rng = high - low
    s = rng.rolling(30, min_periods=30).sum()
    out = s / closeadj.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngabsret_30d_base_v044_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Correlation of range with abs(return) over 30 bars. Tests whether
    range and absolute moves are in phase."""
    rng = (high - low) / closeadj.replace(0.0, np.nan)
    absret = closeadj.pct_change().abs()
    out = rng.rolling(30, min_periods=30).corr(absret)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group L: bounded transforms -------------------------------------------


def f08hl_f08_high_low_range_dynamics_arcrng_30d_base_v045_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """arctan slope: arctan(SMA(range,30).diff(10) / std(range,30)). Bounded
    range-trend rate measure with no level component."""
    rng = high - low
    sma = rng.rolling(30, min_periods=30).mean()
    sd = rng.rolling(30, min_periods=30).std()
    x = sma.diff(10) / sd.replace(0.0, np.nan)
    out = np.arctan(x)
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_tanhrng_50d_base_v046_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """tanh of z-score of range *change* (not level) in trailing 50."""
    rng = high - low
    d = rng.diff(1)
    m = d.rolling(50, min_periods=50).mean()
    s = d.rolling(50, min_periods=50).std()
    z = (d - m) / s.replace(0.0, np.nan)
    out = np.tanh(z)
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_pctb_rng_30d_base_v047_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Stochastic position of SMA(range,5) within trailing 60 bars:
    (s5 - rmin)/(rmax - rmin). Smoothed, so distinct from per-bar rank."""
    rng = high - low
    s5 = rng.rolling(5, min_periods=5).mean()
    mn = s5.rolling(60, min_periods=40).min()
    mx = s5.rolling(60, min_periods=40).max()
    out = (s5 - mn) / (mx - mn).replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group M: range vs body / wick (still range-focused) -------------------


def f08hl_f08_high_low_range_dynamics_rngbody_10d_base_v048_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """SMA over 10 bars of range / max(|close-open|, eps). Measures how
    much beyond the body the range extended — focuses on range size
    relative to directional move."""
    rng = high - low
    body = (close - open).abs()
    r = rng / body.replace(0.0, np.nan)
    rcl = r.clip(upper=20.0)
    out = rcl.rolling(10, min_periods=10).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_uprngfrac_15d_base_v049_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """SMA over 15 of (high - max(o,c)) / (high - low). Upper-range fraction
    averaged — measures persistence of upper-wick dominance in range."""
    upper = high - np.maximum(open, close)
    rng = (high - low).replace(0.0, np.nan)
    r = upper / rng
    out = r.rolling(15, min_periods=15).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_lorngfrac_15d_base_v050_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """SMA over 15 of (min(o,c) - low) / (high - low). Lower-range fraction."""
    lower = np.minimum(open, close) - low
    rng = (high - low).replace(0.0, np.nan)
    r = lower / rng
    out = r.rolling(15, min_periods=15).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group N: discrete bucket / state --------------------------------------


def f08hl_f08_high_low_range_dynamics_rngbuc_60d_base_v051_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Range vs close-vol differential: log(SMA(range,30)/closeadj) -
    log(rolling 30-bar std of closeadj returns). Tests whether intra-bar
    range exceeds inter-bar variability."""
    rng = (high - low) / closeadj.replace(0.0, np.nan)
    ret = closeadj.pct_change()
    rstd = ret.rolling(30, min_periods=30).std()
    rngm = rng.rolling(30, min_periods=30).mean()
    out = np.log(rngm.replace(0.0, np.nan)) - np.log(rstd.replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_sqzcnt_50d_base_v052_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of bars where range is in bottom quartile of trailing 60,
    summed over trailing 50."""
    rng = high - low
    p = rng.rolling(60, min_periods=40).rank(pct=True)
    flag = (p <= 0.25).astype(float).where(~p.isna())
    out = flag.rolling(50, min_periods=30).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_xpancnt_50d_base_v053_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of bars where range is in top quartile of trailing 60,
    summed over trailing 50."""
    rng = high - low
    p = rng.rolling(60, min_periods=40).rank(pct=True)
    flag = (p >= 0.75).astype(float).where(~p.isna())
    out = flag.rolling(50, min_periods=30).sum()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group O: range slope variations / direction signs --------------------


def f08hl_f08_high_low_range_dynamics_rngsign_21d_base_v054_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Sign of SMA(range,21).diff(5). +1/0/-1 — bare direction of range."""
    rng = high - low
    sma = rng.rolling(21, min_periods=21).mean()
    d = sma.diff(5)
    out = pd.Series(np.sign(d.values), index=d.index, dtype=float).where(~d.isna())
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngupcnt_50d_base_v055_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Number of bars in trailing 50 where range increased vs prior bar."""
    rng = high - low
    upd = (rng.diff() > 0.0).astype(float).where(~rng.diff().isna())
    out = upd.rolling(50, min_periods=30).sum()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group P: log-range autocorr at lag 5 / cross-lag correlation ---------


def f08hl_f08_high_low_range_dynamics_rngac5_60d_base_v056_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Autocorr of log range at lag 5 over 60 bars."""
    rng = (high - low).replace(0.0, np.nan)
    lr = np.log(rng)
    out = lr.rolling(60, min_periods=60).corr(lr.shift(5))
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngcumchg_60d_base_v057_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """log(SMA(range,5).shift(0) / SMA(range,5).shift(60)).
    60-bar log change in 5-day range level."""
    rng = high - low
    s = rng.rolling(5, min_periods=5).mean()
    out = np.log(s / s.shift(60).replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group Q: range Hurst-like persistence ---------------------------------


def f08hl_f08_high_low_range_dynamics_rngrs_60d_base_v058_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Range R/S persistence proxy over 60 bars:
    std(log range) * 60 / (max - min cumdev of log range)."""
    rng = (high - low).replace(0.0, np.nan)
    lr = np.log(rng)

    def _hurst(window: np.ndarray) -> float:
        x = window - np.mean(window)
        cum = np.cumsum(x)
        rng_cum = float(np.max(cum) - np.min(cum))
        sd = float(np.std(window, ddof=0))
        if sd == 0.0 or rng_cum == 0.0:
            return np.nan
        return float(np.log(rng_cum / sd) / np.log(len(window)))

    out = lr.rolling(60, min_periods=60).apply(_hurst, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group R: gap vs intraday breakdown of TR ------------------------------


def f08hl_f08_high_low_range_dynamics_gapcontr_30d_base_v059_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Avg over 30 bars of (TR - range)/TR. The fraction of true range
    attributable to overnight gaps."""
    pc = closeadj.shift(1)
    a = (high - low).abs(); b = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, b, c], axis=1).max(axis=1).replace(0.0, np.nan)
    frac = (tr - (high - low)) / tr
    out = frac.rolling(30, min_periods=30).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group S: range volatility regimes -------------------------------------


def f08hl_f08_high_low_range_dynamics_rngvolratio_30d_base_v060_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """std(range,10) / std(range,30). Short vs long vol of range."""
    rng = high - low
    s10 = rng.rolling(10, min_periods=10).std()
    s30 = rng.rolling(30, min_periods=30).std()
    out = s10 / s30.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group T: relationship between high and low diffs (separate H, L) -----


def f08hl_f08_high_low_range_dynamics_hidiff_5d_base_v061_signal(high: pd.Series) -> pd.Series:
    """SMA over 5 of high.diff(1)/high. Mean intraday upward push level."""
    r = high.diff(1) / high.shift(1).replace(0.0, np.nan)
    out = r.rolling(5, min_periods=5).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_lodiff_5d_base_v062_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Asymmetric range-push: SMA(high.diff,5)/SMA(|low.diff|,5).
    Ratio of upward extension to downward extension. > 1 = highs leading."""
    hd = high.diff(1)
    ld = low.diff(1).abs()
    hm = hd.rolling(5, min_periods=5).mean()
    lm = ld.rolling(5, min_periods=5).mean()
    out = hm / lm.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_himhdif_20d_base_v063_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """corr(high diff, low diff, 20). Tells whether highs and lows
    co-move (trending) or diverge (range expansion)."""
    hd = high.diff(1)
    ld = low.diff(1)
    out = hd.rolling(20, min_periods=20).corr(ld)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group U: inside/outside streaks and run lengths -----------------------


def f08hl_f08_high_low_range_dynamics_insstrk_15d_base_v064_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """corr(range, high) - corr(range, low) over 30 bars. Tells whether
    range expansion is driven more by upside or downside extension."""
    rng = high - low
    cu = rng.rolling(30, min_periods=30).corr(high)
    cd = rng.rolling(30, min_periods=30).corr(low)
    out = cu - cd
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_daysnr7_40d_base_v065_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Days since last NR7 bar, capped at 40."""
    rng = high - low
    minrng = rng.rolling(7, min_periods=7).min()
    flag = (rng <= minrng + 1e-12).where(~minrng.isna())

    def _since(x: np.ndarray) -> float:
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return float(len(x))
        return float(len(x) - 1 - idx[-1])

    out = flag.rolling(40, min_periods=20).apply(_since, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group V: range curvature variants -------------------------------------


def f08hl_f08_high_low_range_dynamics_rngcurvlog_60d_base_v066_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Curvature of log-range mean(50): l - 2*l.shift(10) + l.shift(20)."""
    rng = (high - low).replace(0.0, np.nan)
    lr = np.log(rng)
    sma = lr.rolling(50, min_periods=50).mean()
    out = sma - 2.0 * sma.shift(10) + sma.shift(20)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group W: range entropy proxy ------------------------------------------


def f08hl_f08_high_low_range_dynamics_rngdispiqr_30d_base_v067_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """IQR of log range over trailing 30 bars / median(log range, 30).
    Distribution-width measure of range variability."""
    rng = (high - low).replace(0.0, np.nan)
    lr = np.log(rng)
    q1 = lr.rolling(30, min_periods=30).quantile(0.25)
    q3 = lr.rolling(30, min_periods=30).quantile(0.75)
    med = lr.rolling(30, min_periods=30).median()
    out = (q3 - q1) / med.abs().replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group X: trough / peak of range path ---------------------------------


def f08hl_f08_high_low_range_dynamics_rngfromtmin_30d_base_v068_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars since trailing 30-day min of range, scaled to [0,1]."""
    rng = high - low
    win = 30

    def _argmin_age(x: np.ndarray) -> float:
        i = int(np.argmin(x))
        return float(len(x) - 1 - i) / float(len(x) - 1)

    out = rng.rolling(win, min_periods=win).apply(_argmin_age, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngfromtmax_30d_base_v069_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars since trailing 30-day max of range, scaled to [0,1]."""
    rng = high - low
    win = 30

    def _argmax_age(x: np.ndarray) -> float:
        i = int(np.argmax(x))
        return float(len(x) - 1 - i) / float(len(x) - 1)

    out = rng.rolling(win, min_periods=win).apply(_argmax_age, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group Y: range trend persistence / MAD --------------------------------


def f08hl_f08_high_low_range_dynamics_rngmad_50d_base_v070_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Mean absolute deviation of relative range over 50 bars."""
    r = (high - low) / closeadj.replace(0.0, np.nan)
    m = r.rolling(50, min_periods=50).mean()
    out = (r - m).abs().rolling(50, min_periods=50).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngavgcv_30d_base_v071_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Range autocorr at lag 10 over 30 bars. Distinct from lag-1 and lag-5
    autocorrelations elsewhere — captures medium-cycle persistence."""
    rng = (high - low).replace(0.0, np.nan)
    lr = np.log(rng)
    out = lr.rolling(30, min_periods=30).corr(lr.shift(10))
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group Z: 3-bar inside / outside patterns ------------------------------


def f08hl_f08_high_low_range_dynamics_ins3_1d_base_v072_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """3-bar inside: current is inside vs shift(1) AND shift(1) is inside
    vs shift(2). 1/0 indicator."""
    cur_in = (high < high.shift(1)) & (low > low.shift(1))
    prev_in = (high.shift(1) < high.shift(2)) & (low.shift(1) > low.shift(2))
    flag = cur_in & prev_in
    out = flag.astype(float).where(~high.shift(2).isna() & ~low.shift(2).isna())
    return out.replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_out3_1d_base_v073_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """3-bar outside: current outside vs shift(1) AND shift(1) outside vs
    shift(2). 1/0."""
    cur_out = (high > high.shift(1)) & (low < low.shift(1))
    prev_out = (high.shift(1) > high.shift(2)) & (low.shift(1) < low.shift(2))
    flag = cur_out & prev_out
    out = flag.astype(float).where(~high.shift(2).isna() & ~low.shift(2).isna())
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group AA: range entropy / Hill estimator-like -----------------------


def f08hl_f08_high_low_range_dynamics_rngtopfrac_30d_base_v074_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """In trailing 30 bars, fraction of total summed range contributed by
    top-3 largest bars. Concentration of range mass."""
    rng = high - low

    def _topfrac(x: np.ndarray) -> float:
        s = np.sort(x)[::-1]
        tot = float(np.sum(s))
        if tot == 0.0:
            return np.nan
        return float(np.sum(s[:3]) / tot)

    out = rng.rolling(30, min_periods=30).apply(_topfrac, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group AB: range cross-correlation with prior shift --------------------


def f08hl_f08_high_low_range_dynamics_rngshiftcorr_40d_base_v075_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """corr(log range, log range.shift(3)) over 40 bars. Cross-lag-3
    persistence of range variation."""
    rng = (high - low).replace(0.0, np.nan)
    lr = np.log(rng)
    out = lr.rolling(40, min_periods=40).corr(lr.shift(3))
    return out.replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f08_high_low_range_dynamics_base_001_075_REGISTRY = {
    "f08hl_f08_high_low_range_dynamics_relrng_1d_base_v001_signal": {"inputs": ["high", "low", "close"], "func": f08hl_f08_high_low_range_dynamics_relrng_1d_base_v001_signal},
    "f08hl_f08_high_low_range_dynamics_relrngmean_21d_base_v002_signal": {"inputs": ["high", "low", "close"], "func": f08hl_f08_high_low_range_dynamics_relrngmean_21d_base_v002_signal},
    "f08hl_f08_high_low_range_dynamics_relrngmean_100d_base_v003_signal": {"inputs": ["high", "low", "closeadj"], "func": f08hl_f08_high_low_range_dynamics_relrngmean_100d_base_v003_signal},
    "f08hl_f08_high_low_range_dynamics_logrng_1d_base_v004_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_logrng_1d_base_v004_signal},
    "f08hl_f08_high_low_range_dynamics_logrngmean_50d_base_v005_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_logrngmean_50d_base_v005_signal},
    "f08hl_f08_high_low_range_dynamics_atrwild_14d_base_v006_signal": {"inputs": ["high", "low", "close"], "func": f08hl_f08_high_low_range_dynamics_atrwild_14d_base_v006_signal},
    "f08hl_f08_high_low_range_dynamics_atrsma_50d_base_v007_signal": {"inputs": ["high", "low", "closeadj"], "func": f08hl_f08_high_low_range_dynamics_atrsma_50d_base_v007_signal},
    "f08hl_f08_high_low_range_dynamics_atrrng_30d_base_v008_signal": {"inputs": ["high", "low", "closeadj"], "func": f08hl_f08_high_low_range_dynamics_atrrng_30d_base_v008_signal},
    "f08hl_f08_high_low_range_dynamics_normrng_20d_base_v009_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_normrng_20d_base_v009_signal},
    "f08hl_f08_high_low_range_dynamics_trrngrat_1d_base_v010_signal": {"inputs": ["high", "low", "close"], "func": f08hl_f08_high_low_range_dynamics_trrngrat_1d_base_v010_signal},
    "f08hl_f08_high_low_range_dynamics_rngexp_10d_base_v011_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngexp_10d_base_v011_signal},
    "f08hl_f08_high_low_range_dynamics_rngslope_20d_base_v012_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngslope_20d_base_v012_signal},
    "f08hl_f08_high_low_range_dynamics_rngcurv_30d_base_v013_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngcurv_30d_base_v013_signal},
    "f08hl_f08_high_low_range_dynamics_volofrng_30d_base_v014_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_volofrng_30d_base_v014_signal},
    "f08hl_f08_high_low_range_dynamics_rngac_30d_base_v015_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngac_30d_base_v015_signal},
    "f08hl_f08_high_low_range_dynamics_rngrnk_63d_base_v016_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngrnk_63d_base_v016_signal},
    "f08hl_f08_high_low_range_dynamics_rngzs_40d_base_v017_signal": {"inputs": ["high", "low", "closeadj"], "func": f08hl_f08_high_low_range_dynamics_rngzs_40d_base_v017_signal},
    "f08hl_f08_high_low_range_dynamics_rngsk_60d_base_v018_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngsk_60d_base_v018_signal},
    "f08hl_f08_high_low_range_dynamics_rngkur_60d_base_v019_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngkur_60d_base_v019_signal},
    "f08hl_f08_high_low_range_dynamics_rngmadr_30d_base_v020_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngmadr_30d_base_v020_signal},
    "f08hl_f08_high_low_range_dynamics_trrnk_50d_base_v021_signal": {"inputs": ["high", "low", "closeadj"], "func": f08hl_f08_high_low_range_dynamics_trrnk_50d_base_v021_signal},
    "f08hl_f08_high_low_range_dynamics_trzs_30d_base_v022_signal": {"inputs": ["high", "low", "closeadj"], "func": f08hl_f08_high_low_range_dynamics_trzs_30d_base_v022_signal},
    "f08hl_f08_high_low_range_dynamics_wildvssma_30d_base_v023_signal": {"inputs": ["high", "low", "closeadj"], "func": f08hl_f08_high_low_range_dynamics_wildvssma_30d_base_v023_signal},
    "f08hl_f08_high_low_range_dynamics_rngprior_1d_base_v024_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngprior_1d_base_v024_signal},
    "f08hl_f08_high_low_range_dynamics_rngtmax_20d_base_v025_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngtmax_20d_base_v025_signal},
    "f08hl_f08_high_low_range_dynamics_rngtmin_20d_base_v026_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngtmin_20d_base_v026_signal},
    "f08hl_f08_high_low_range_dynamics_rngstrkabv_30d_base_v027_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngstrkabv_30d_base_v027_signal},
    "f08hl_f08_high_low_range_dynamics_insidebr_1d_base_v028_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_insidebr_1d_base_v028_signal},
    "f08hl_f08_high_low_range_dynamics_outsidebr_1d_base_v029_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_outsidebr_1d_base_v029_signal},
    "f08hl_f08_high_low_range_dynamics_wr4_1d_base_v032_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_wr4_1d_base_v032_signal},
    "f08hl_f08_high_low_range_dynamics_wr7_1d_base_v033_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_wr7_1d_base_v033_signal},
    "f08hl_f08_high_low_range_dynamics_nr7cnt_50d_base_v036_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_nr7cnt_50d_base_v036_signal},
    "f08hl_f08_high_low_range_dynamics_wr7cnt_50d_base_v037_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_wr7cnt_50d_base_v037_signal},
    "f08hl_f08_high_low_range_dynamics_sqz_60d_base_v038_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_sqz_60d_base_v038_signal},
    "f08hl_f08_high_low_range_dynamics_xpan_40d_base_v039_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_xpan_40d_base_v039_signal},
    "f08hl_f08_high_low_range_dynamics_rngrat_short_base_v040_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngrat_short_base_v040_signal},
    "f08hl_f08_high_low_range_dynamics_rngrat_long_base_v041_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngrat_long_base_v041_signal},
    "f08hl_f08_high_low_range_dynamics_rngslpdiff_30d_base_v042_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngslpdiff_30d_base_v042_signal},
    "f08hl_f08_high_low_range_dynamics_rngsum_30d_base_v043_signal": {"inputs": ["high", "low", "closeadj"], "func": f08hl_f08_high_low_range_dynamics_rngsum_30d_base_v043_signal},
    "f08hl_f08_high_low_range_dynamics_rngabsret_30d_base_v044_signal": {"inputs": ["high", "low", "closeadj"], "func": f08hl_f08_high_low_range_dynamics_rngabsret_30d_base_v044_signal},
    "f08hl_f08_high_low_range_dynamics_arcrng_30d_base_v045_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_arcrng_30d_base_v045_signal},
    "f08hl_f08_high_low_range_dynamics_tanhrng_50d_base_v046_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_tanhrng_50d_base_v046_signal},
    "f08hl_f08_high_low_range_dynamics_pctb_rng_30d_base_v047_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_pctb_rng_30d_base_v047_signal},
    "f08hl_f08_high_low_range_dynamics_rngbody_10d_base_v048_signal": {"inputs": ["open", "high", "low", "close"], "func": f08hl_f08_high_low_range_dynamics_rngbody_10d_base_v048_signal},
    "f08hl_f08_high_low_range_dynamics_uprngfrac_15d_base_v049_signal": {"inputs": ["open", "high", "low", "close"], "func": f08hl_f08_high_low_range_dynamics_uprngfrac_15d_base_v049_signal},
    "f08hl_f08_high_low_range_dynamics_lorngfrac_15d_base_v050_signal": {"inputs": ["open", "high", "low", "close"], "func": f08hl_f08_high_low_range_dynamics_lorngfrac_15d_base_v050_signal},
    "f08hl_f08_high_low_range_dynamics_rngbuc_60d_base_v051_signal": {"inputs": ["high", "low", "closeadj"], "func": f08hl_f08_high_low_range_dynamics_rngbuc_60d_base_v051_signal},
    "f08hl_f08_high_low_range_dynamics_sqzcnt_50d_base_v052_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_sqzcnt_50d_base_v052_signal},
    "f08hl_f08_high_low_range_dynamics_xpancnt_50d_base_v053_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_xpancnt_50d_base_v053_signal},
    "f08hl_f08_high_low_range_dynamics_rngsign_21d_base_v054_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngsign_21d_base_v054_signal},
    "f08hl_f08_high_low_range_dynamics_rngupcnt_50d_base_v055_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngupcnt_50d_base_v055_signal},
    "f08hl_f08_high_low_range_dynamics_rngac5_60d_base_v056_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngac5_60d_base_v056_signal},
    "f08hl_f08_high_low_range_dynamics_rngcumchg_60d_base_v057_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngcumchg_60d_base_v057_signal},
    "f08hl_f08_high_low_range_dynamics_rngrs_60d_base_v058_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngrs_60d_base_v058_signal},
    "f08hl_f08_high_low_range_dynamics_gapcontr_30d_base_v059_signal": {"inputs": ["high", "low", "closeadj"], "func": f08hl_f08_high_low_range_dynamics_gapcontr_30d_base_v059_signal},
    "f08hl_f08_high_low_range_dynamics_rngvolratio_30d_base_v060_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngvolratio_30d_base_v060_signal},
    "f08hl_f08_high_low_range_dynamics_hidiff_5d_base_v061_signal": {"inputs": ["high"], "func": f08hl_f08_high_low_range_dynamics_hidiff_5d_base_v061_signal},
    "f08hl_f08_high_low_range_dynamics_lodiff_5d_base_v062_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_lodiff_5d_base_v062_signal},
    "f08hl_f08_high_low_range_dynamics_himhdif_20d_base_v063_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_himhdif_20d_base_v063_signal},
    "f08hl_f08_high_low_range_dynamics_insstrk_15d_base_v064_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_insstrk_15d_base_v064_signal},
    "f08hl_f08_high_low_range_dynamics_daysnr7_40d_base_v065_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_daysnr7_40d_base_v065_signal},
    "f08hl_f08_high_low_range_dynamics_rngcurvlog_60d_base_v066_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngcurvlog_60d_base_v066_signal},
    "f08hl_f08_high_low_range_dynamics_rngdispiqr_30d_base_v067_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngdispiqr_30d_base_v067_signal},
    "f08hl_f08_high_low_range_dynamics_rngfromtmin_30d_base_v068_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngfromtmin_30d_base_v068_signal},
    "f08hl_f08_high_low_range_dynamics_rngfromtmax_30d_base_v069_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngfromtmax_30d_base_v069_signal},
    "f08hl_f08_high_low_range_dynamics_rngmad_50d_base_v070_signal": {"inputs": ["high", "low", "closeadj"], "func": f08hl_f08_high_low_range_dynamics_rngmad_50d_base_v070_signal},
    "f08hl_f08_high_low_range_dynamics_rngavgcv_30d_base_v071_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngavgcv_30d_base_v071_signal},
    "f08hl_f08_high_low_range_dynamics_ins3_1d_base_v072_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_ins3_1d_base_v072_signal},
    "f08hl_f08_high_low_range_dynamics_out3_1d_base_v073_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_out3_1d_base_v073_signal},
    "f08hl_f08_high_low_range_dynamics_rngtopfrac_30d_base_v074_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngtopfrac_30d_base_v074_signal},
    "f08hl_f08_high_low_range_dynamics_rngshiftcorr_40d_base_v075_signal": {"inputs": ["high", "low"], "func": f08hl_f08_high_low_range_dynamics_rngshiftcorr_40d_base_v075_signal},
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
    for name, entry in f08_high_low_range_dynamics_base_001_075_REGISTRY.items():
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
