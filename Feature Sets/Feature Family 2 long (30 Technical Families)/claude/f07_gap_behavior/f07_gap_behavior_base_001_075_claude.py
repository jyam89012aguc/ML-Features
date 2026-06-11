"""f07_gap_behavior base features 001-075.

Domain: overnight gap behavior. The core construct is the relationship
between today's `open` and the prior bar's `close` (close.shift(1)).
  gap   = (open - close.shift(1)) / close.shift(1)   (pct gap)
  sgap  = open - close.shift(1)                       (absolute gap)
  lgap  = log(open / close.shift(1))                  (log gap)

Every feature in this file references the gap construct in some form:
raw gap signals, gap-fill / no-fill diagnostics, gap streaks and
sequencing, gap magnitude statistics, gap-vs-range interactions, time
since features, statistical features on gaps, and discrete states.

Each function is a fully expanded def block: formula inline, no
_core() factory, no parametric reuse. NaN policy: never fillna(0)
inside rolling code; only replace([inf,-inf], nan) at final return.
Windows > 21 use closeadj, windows <= 21 use close (OHLC for the bar
itself is unadjusted, per the guide).
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Features 001-075
# ---------------------------------------------------------------------------


# --- Group A: raw gap level signals (small set, widely spaced) -------------


def f07gb_f07_gap_behavior_gappct_1d_base_v001_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Per-bar gap percentage: (open - prior close) / prior close."""
    pc = close.shift(1)
    out = (open - pc) / pc.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_lgapcumlong_120d_base_v002_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """120-bar cumulative log-gap drift. Distinct from per-bar gap because
    it aggregates ON a long window."""
    pc = closeadj.shift(1)
    lg = np.log(open / pc.replace(0.0, np.nan))
    out = lg.rolling(120, min_periods=120).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapabsnrm_5d_base_v003_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """|gap| normalized by 5-bar trailing mean of |gap| -- relative magnitude
    indicator (current gap unusual vs immediate recent gap regime)."""
    pc = close.shift(1)
    g = ((open - pc) / pc.replace(0.0, np.nan)).abs()
    mu = g.rolling(5, min_periods=5).mean()
    out = g / mu.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapsgn_1d_base_v004_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Per-bar sign of gap: +1 / 0 / -1."""
    pc = close.shift(1)
    g = open - pc
    out = np.sign(g).where(~g.isna())
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group B: rolling gap aggregates (mean/sum/median) ---------------------


def f07gb_f07_gap_behavior_gapmean_10d_base_v005_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """10-bar mean of per-bar gap pct."""
    pc = close.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    out = g.rolling(10, min_periods=10).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapsum_21d_base_v006_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """21-bar cumulative sum of gap pct -- net overnight drift."""
    pc = close.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    out = g.rolling(21, min_periods=21).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapmed_50d_base_v007_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """50-bar median gap pct -- robust mid-term overnight bias."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    out = g.rolling(50, min_periods=50).median()
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapsumabs_30d_base_v008_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """30-bar sum of |gap| -- total overnight energy."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    out = g.abs().rolling(30, min_periods=30).sum()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group C: gap variability (std / mad / range / iqr) --------------------


def f07gb_f07_gap_behavior_gapstd_20d_base_v009_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """20-bar std of gap pct -- gap volatility."""
    pc = close.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    out = g.rolling(20, min_periods=20).std(ddof=1)
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapmad_40d_base_v010_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """40-bar mean-abs-deviation of gap pct."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    mu = g.rolling(40, min_periods=40).mean()
    out = (g - mu).abs().rolling(40, min_periods=40).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gaprng_30d_base_v011_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """30-bar max(gap) - min(gap): gap spread."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    out = g.rolling(30, min_periods=30).max() - g.rolling(30, min_periods=30).min()
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapiqr_60d_base_v012_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """60-bar IQR of gap pct."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    q75 = g.rolling(60, min_periods=60).quantile(0.75)
    q25 = g.rolling(60, min_periods=60).quantile(0.25)
    out = q75 - q25
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group D: gap z-score / standardization --------------------------------


def f07gb_f07_gap_behavior_bigfrac_30d_base_v013_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """30-bar fraction of gaps that exceeded 0.5% in magnitude."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    big = (g.abs() > 0.005).astype(float).where(~g.isna())
    out = big.rolling(30, min_periods=30).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_posnegratio_120d_base_v014_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """120-bar mean(positive gap) / mean(|negative gap|). >1 = up-gap bias."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    pmean = g.where(g > 0).rolling(120, min_periods=30).mean()
    nmean = (-g).where(g < 0).rolling(120, min_periods=30).mean()
    out = pmean / nmean.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group E: gap rank / quantile / percentile -----------------------------


def f07gb_f07_gap_behavior_gaprnkmed_50d_base_v015_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """5-bar median of (50-bar percentile rank of gap) -- smoothed rank,
    less single-bar correlated to v001."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    pr = g.rolling(50, min_periods=30).rank(pct=True)
    out = pr.rolling(5, min_periods=5).median()
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gaprnkabs_80d_base_v016_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """80-bar percentile rank of |gap| -- rare-magnitude indicator."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    out = g.abs().rolling(80, min_periods=40).rank(pct=True)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group F: gap-fill diagnostics (current bar) ---------------------------


def f07gb_f07_gap_behavior_fillbin_1d_base_v017_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Binary: 1 if today's bar reaches back to prior close (gap fills).
    For up gap, low <= prior close; for down gap, high >= prior close.
    No gap -> NaN."""
    pc = close.shift(1)
    g = open - pc
    up_fill = (low <= pc) & (g > 0)
    dn_fill = (high >= pc) & (g < 0)
    filled = (up_fill | dn_fill).astype(float)
    out = filled.where(g != 0.0)
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_fillratio_1d_base_v018_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of gap retraced intraday. For up gap, (open-low)/gap clipped
    to [0,1]. For down gap, (high-open)/(-gap) clipped to [0,1]."""
    pc = close.shift(1)
    g = open - pc
    up_amt = (open - low) / g.where(g > 0, np.nan)
    dn_amt = (high - open) / (-g).where(g < 0, np.nan)
    raw = up_amt.combine_first(dn_amt)
    out = raw.clip(lower=0.0, upper=1.0)
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_fillrate_30d_base_v019_signal(open: pd.Series, high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """30-bar mean fill-rate fraction of gaps that filled within their day."""
    pc = closeadj.shift(1)
    g = open - pc
    up_fill = (low <= pc) & (g > 0)
    dn_fill = (high >= pc) & (g < 0)
    has_gap = (g != 0.0).astype(float)
    filled = (up_fill | dn_fill).astype(float).where(g != 0.0)
    s_filled = filled.rolling(30, min_periods=15).sum()
    s_total = has_gap.rolling(30, min_periods=15).sum()
    out = s_filled / s_total.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_partfillmean_20d_base_v020_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """20-bar mean partial-fill ratio (gap retracement)."""
    pc = close.shift(1)
    g = open - pc
    up_amt = (open - low) / g.where(g > 0, np.nan)
    dn_amt = (high - open) / (-g).where(g < 0, np.nan)
    raw = up_amt.combine_first(dn_amt).clip(lower=0.0, upper=1.0)
    out = raw.rolling(20, min_periods=10).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group G: gap-and-go vs gap-and-reverse --------------------------------


def f07gb_f07_gap_behavior_gapgo_1d_base_v021_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Gap-and-go: +1 if (gap up & close>open), -1 if (gap down & close<open),
    0 otherwise. Uses prior-close construct."""
    pc = close.shift(1)
    g = open - pc
    cls = (close - open)
    val = pd.Series(np.where((g > 0) & (cls > 0), 1.0,
                   np.where((g < 0) & (cls < 0), -1.0, 0.0)),
                    index=open.index, dtype=float)
    out = val.where(~g.isna())
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gaprev_1d_base_v022_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Gap-and-reverse: +1 if (gap up & close<open), -1 if (gap down & close>open),
    0 otherwise."""
    pc = close.shift(1)
    g = open - pc
    cls = close - open
    val = pd.Series(np.where((g > 0) & (cls < 0), 1.0,
                   np.where((g < 0) & (cls > 0), -1.0, 0.0)),
                    index=open.index, dtype=float)
    out = val.where(~g.isna())
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapgomean_40d_base_v023_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """40-bar mean gap-and-go score, using a continuous version:
    sign(gap) * sign(close-open). +1 confirm, -1 reversal, 0 inside."""
    pc = closeadj.shift(1)
    g = open - pc
    cls = closeadj - open
    raw = np.sign(g) * np.sign(cls)
    out = raw.rolling(40, min_periods=20).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapcontinue_30d_base_v024_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Continuation strength: 30-bar mean of gap_pct * (close-open)/open.
    Positive when gap direction matches intraday direction."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    intra = (closeadj - open) / open.replace(0.0, np.nan)
    raw = g * intra
    out = raw.rolling(30, min_periods=15).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group H: gap streaks / consecutive counts -----------------------------


def f07gb_f07_gap_behavior_upstrk_1d_base_v025_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Length of current run of consecutive up gaps (gap > 0)."""
    pc = close.shift(1)
    g = open - pc
    up = (g > 0).astype(float).where(~g.isna())
    grp = (up != up.shift(1)).cumsum()
    out = up.groupby(grp).cumsum() * up
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_dnstrk_1d_base_v026_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Length of current run of consecutive down gaps (gap < 0)."""
    pc = close.shift(1)
    g = open - pc
    dn = (g < 0).astype(float).where(~g.isna())
    grp = (dn != dn.shift(1)).cumsum()
    out = dn.groupby(grp).cumsum() * dn
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapsignstrk_1d_base_v027_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Signed gap-streak: positive run length for up gaps, negative for down."""
    pc = close.shift(1)
    g = open - pc
    up = (g > 0).astype(float).where(~g.isna())
    dn = (g < 0).astype(float).where(~g.isna())
    grp_u = (up != up.shift(1)).cumsum()
    grp_d = (dn != dn.shift(1)).cumsum()
    rl_u = up.groupby(grp_u).cumsum() * up
    rl_d = dn.groupby(grp_d).cumsum() * dn
    out = rl_u - rl_d
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group I: counts of gap events -----------------------------------------


def f07gb_f07_gap_behavior_upcnt_20d_base_v028_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """20-bar count of up gaps."""
    pc = close.shift(1)
    g = open - pc
    up = (g > 0).astype(float).where(~g.isna())
    out = up.rolling(20, min_periods=20).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_dncnt_40d_base_v029_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """40-bar count of down gaps."""
    pc = closeadj.shift(1)
    g = open - pc
    dn = (g < 0).astype(float).where(~g.isna())
    out = dn.rolling(40, min_periods=40).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_bigcnt_60d_base_v030_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """60-bar count of large gaps (|gap| > 1%)."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    big = (g.abs() > 0.01).astype(float).where(~g.isna())
    out = big.rolling(60, min_periods=60).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_sigcnt_50d_base_v031_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """50-bar count of gaps exceeding 1-std (per-rolling-window) magnitude."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    sd = g.rolling(50, min_periods=50).std(ddof=1)
    big = (g.abs() > sd).astype(float).where(~g.isna() & ~sd.isna())
    out = big.rolling(50, min_periods=50).sum()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group J: gap magnitudes (max/min/positive_mean/negative_mean) ---------


def f07gb_f07_gap_behavior_maxup_30d_base_v032_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """30-bar max up-gap (max of positive gap pct, NaN if none in window)."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    pos = g.where(g > 0)
    out = pos.rolling(30, min_periods=5).max()
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_maxdn_60d_base_v033_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """60-bar max down-gap magnitude (max of -gap when gap<0)."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    neg = (-g).where(g < 0)
    out = neg.rolling(60, min_periods=10).max()
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_posneg_30d_base_v034_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """30-bar mean(positive_gaps) - mean(|negative_gaps|): asymmetry of gap distribution."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    pmean = g.where(g > 0).rolling(30, min_periods=5).mean()
    nmean = (-g).where(g < 0).rolling(30, min_periods=5).mean()
    out = pmean - nmean
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_extrme_50d_base_v035_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """50-bar (max gap up + max gap dn magnitude): total gap extreme."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    out = g.rolling(50, min_periods=50).max() + g.abs().rolling(50, min_periods=50).max()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group K: gap-vs-range interactions ------------------------------------


def f07gb_f07_gap_behavior_grtorng_1d_base_v036_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """|gap| / today's (high - low). Gap as fraction of intraday range."""
    pc = close.shift(1)
    g = (open - pc).abs()
    rng = (high - low).replace(0.0, np.nan)
    out = g / rng
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_grtoprng_1d_base_v037_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """|gap| / prior day's range = |open - prev close| / (prev high - prev low)."""
    pc = close.shift(1)
    g = (open - pc).abs()
    prng = (high.shift(1) - low.shift(1)).replace(0.0, np.nan)
    out = g / prng
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_grtoatrmean_14d_base_v038_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """14-bar mean of |gap| / 14d ATR (Wilder). Smoothed gap-to-ATR ratio."""
    pc = close.shift(1)
    g = (open - pc).abs()
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    r = g / atr.replace(0.0, np.nan)
    out = r.rolling(14, min_periods=14).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_grbig_30d_base_v039_signal(open: pd.Series, high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """30-bar mean of (|gap| / today's range). Tracks how `gapy` recent bars are."""
    pc = closeadj.shift(1)
    g = (open - pc).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = g / rng
    out = r.rolling(30, min_periods=15).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group L: time-since gap features --------------------------------------


def f07gb_f07_gap_behavior_dayslast_60d_base_v040_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Bars since last large gap (|gap|>1%), capped at 60."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    big = (g.abs() > 0.01).astype(float).where(~g.isna())
    n = 60
    def _last_one(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return float(n)
        return float(len(x) - 1 - idx[-1])
    out = big.rolling(n, min_periods=n).apply(_last_one, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_dayslastup_40d_base_v041_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Bars since last up gap, capped at 40."""
    pc = closeadj.shift(1)
    g = open - pc
    up = (g > 0).astype(float).where(~g.isna())
    n = 40
    def _last_one(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return float(n)
        return float(len(x) - 1 - idx[-1])
    out = up.rolling(n, min_periods=n).apply(_last_one, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_dayslastdn_40d_base_v042_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Bars since last down gap, capped at 40."""
    pc = closeadj.shift(1)
    g = open - pc
    dn = (g < 0).astype(float).where(~g.isna())
    n = 40
    def _last_one(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return float(n)
        return float(len(x) - 1 - idx[-1])
    out = dn.rolling(n, min_periods=n).apply(_last_one, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group M: statistical (skew, kurt, autocorr) on gaps -------------------


def f07gb_f07_gap_behavior_gapskew_60d_base_v043_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """60-bar skewness of gap pct distribution."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    out = g.rolling(60, min_periods=60).skew()
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapkurt_80d_base_v044_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """80-bar kurtosis of gap pct distribution."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    out = g.rolling(80, min_periods=80).kurt()
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapac1_50d_base_v045_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """50-bar lag-1 autocorrelation of gap series."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    def _ac1(x):
        x = np.asarray(x, dtype=float)
        if not np.all(np.isfinite(x)):
            return np.nan
        x0 = x[:-1]; x1 = x[1:]
        m0 = x0.mean(); m1 = x1.mean()
        v0 = x0.std(ddof=1); v1 = x1.std(ddof=1)
        if v0 <= 0.0 or v1 <= 0.0:
            return np.nan
        return float(((x0 - m0) * (x1 - m1)).mean() / (v0 * v1))
    out = g.rolling(50, min_periods=50).apply(_ac1, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapac2_70d_base_v046_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """70-bar lag-2 autocorrelation of gap series."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    def _ac2(x):
        x = np.asarray(x, dtype=float)
        if not np.all(np.isfinite(x)):
            return np.nan
        x0 = x[:-2]; x1 = x[2:]
        m0 = x0.mean(); m1 = x1.mean()
        v0 = x0.std(ddof=1); v1 = x1.std(ddof=1)
        if v0 <= 0.0 or v1 <= 0.0:
            return np.nan
        return float(((x0 - m0) * (x1 - m1)).mean() / (v0 * v1))
    out = g.rolling(70, min_periods=70).apply(_ac2, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group N: gap-classification (discrete states) -------------------------


def f07gb_f07_gap_behavior_gapcls_1d_base_v047_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """5-state classification: 0 no gap (|gap|<0.1%), +1 small up (0.1-1%),
    +2 big up (>1%), -1 small dn, -2 big dn."""
    pc = close.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    val = pd.Series(np.where(g.abs() < 0.001, 0.0,
                   np.where((g > 0) & (g < 0.01), 1.0,
                   np.where(g >= 0.01, 2.0,
                   np.where((g < 0) & (g > -0.01), -1.0, -2.0)))),
                    index=open.index, dtype=float)
    out = val.where(~g.isna())
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapclsmean_30d_base_v048_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """30-bar mean of the gap-classification state."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    val = pd.Series(np.where(g.abs() < 0.001, 0.0,
                   np.where((g > 0) & (g < 0.01), 1.0,
                   np.where(g >= 0.01, 2.0,
                   np.where((g < 0) & (g > -0.01), -1.0, -2.0)))),
                    index=open.index, dtype=float)
    val = val.where(~g.isna())
    out = val.rolling(30, min_periods=30).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group O: log-gap aggregates and EWMs ----------------------------------


def f07gb_f07_gap_behavior_lgapsum_60d_base_v049_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """60-bar sum of log gaps -- net log overnight drift."""
    pc = closeadj.shift(1)
    lg = np.log(open / pc.replace(0.0, np.nan))
    out = lg.rolling(60, min_periods=60).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_lgapewm_30d_base_v050_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """EWM-30 of log gap (decaying mean of recent overnight drift)."""
    pc = closeadj.shift(1)
    lg = np.log(open / pc.replace(0.0, np.nan))
    out = lg.ewm(span=30, adjust=False, min_periods=30).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_lgapewmabs_50d_base_v051_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """EWM-50 of |log gap| -- gap-energy decay average."""
    pc = closeadj.shift(1)
    lg = np.log(open / pc.replace(0.0, np.nan)).abs()
    out = lg.ewm(span=50, adjust=False, min_periods=50).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group P: bounded transforms of gap signals ----------------------------


def f07gb_f07_gap_behavior_gapextrnk_30d_base_v052_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """30-bar percentile rank of the trailing-30 max(|gap|). Locates whether
    the current gap-extreme regime is rare vs history (longer-context rank)."""
    pc = closeadj.shift(1)
    g = ((open - pc) / pc.replace(0.0, np.nan)).abs()
    rmax = g.rolling(30, min_periods=30).max()
    out = rmax.rolling(120, min_periods=60).rank(pct=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapaccel_1d_base_v053_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Gap acceleration: gap_t - 2*gap_{t-1} + gap_{t-2} (discrete 2nd diff).
    Tracks gap-velocity changes at the bar level."""
    pc = close.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    out = g - 2.0 * g.shift(1) + g.shift(2)
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapsigmoid_30d_base_v054_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """30-bar mean of sigmoid(50*gap): bounded [0,1] gap intensity proxy."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    s = 1.0 / (1.0 + np.exp(-50.0 * g))
    out = s.rolling(30, min_periods=30).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group Q: gap-vs-prior-bar interactions --------------------------------


def f07gb_f07_gap_behavior_gapvsret_30d_base_v055_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """30-bar correlation between gap and prior day's intraday return.
    Tests if up days are followed by up gaps (continuation)."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    pret = closeadj.pct_change(1).shift(1)
    out = g.rolling(30, min_periods=30).corr(pret)
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapvsfwd_40d_base_v056_signal(open: pd.Series, high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """40-bar correlation between gap and same-day intraday return (open->close).
    Captures continuation vs fade tendency."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    intra = (closeadj - open) / open.replace(0.0, np.nan)
    out = g.rolling(40, min_periods=40).corr(intra)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group R: gap energy / vol --------------------------------------------


def f07gb_f07_gap_behavior_gapintravar_30d_base_v057_signal(open: pd.Series, high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """30-bar var(gap) / var(intraday_range_log). Gap-volatility relative to
    intraday range volatility. Structurally distinct from continuation
    correlations."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    rlog = np.log((high / low).replace(0.0, np.nan))
    gv = g.rolling(30, min_periods=30).var(ddof=1)
    rv = rlog.rolling(30, min_periods=30).var(ddof=1)
    out = gv / rv.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapvol_50d_base_v058_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """50-bar std(gap) / std(daily return) -- relative gap vol to total return vol."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    r = closeadj.pct_change(1)
    g_sd = g.rolling(50, min_periods=50).std(ddof=1)
    r_sd = r.rolling(50, min_periods=50).std(ddof=1)
    out = g_sd / r_sd.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group S: gap close-position diagnostics -------------------------------


def f07gb_f07_gap_behavior_closegap_1d_base_v059_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Close vs prior close, relative to gap: (close - prior_close)/(open - prior_close).
    >1 = continued past open, 0 = closed at prior close (full fill+revert),
    <0 = closed beyond fill direction."""
    pc = close.shift(1)
    g = open - pc
    out = (close - pc) / g.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_closegapmean_30d_base_v060_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """30-bar mean of close-vs-gap position ratio."""
    pc = closeadj.shift(1)
    g = open - pc
    ratio = (closeadj - pc) / g.replace(0.0, np.nan)
    ratio = ratio.clip(lower=-3.0, upper=3.0)
    out = ratio.rolling(30, min_periods=15).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group T: bracketed gap quantities -------------------------------------


def f07gb_f07_gap_behavior_uppct_60d_base_v061_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """60-bar fraction of bars with an up gap."""
    pc = closeadj.shift(1)
    g = open - pc
    up = (g > 0).astype(float).where(~g.isna())
    out = up.rolling(60, min_periods=60).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_dnpct_90d_base_v062_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """90-bar fraction of bars with a down gap."""
    pc = closeadj.shift(1)
    g = open - pc
    dn = (g < 0).astype(float).where(~g.isna())
    out = dn.rolling(90, min_periods=90).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group U: signed gap-vs-trend diagnostics ------------------------------


def f07gb_f07_gap_behavior_aligntrend_40d_base_v063_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """40-bar mean of sign(gap) * sign(20d trend in closeadj). Are gaps aligned
    with the existing trend?"""
    pc = closeadj.shift(1)
    g = open - pc
    trend = closeadj - closeadj.shift(20)
    raw = np.sign(g) * np.sign(trend)
    out = raw.rolling(40, min_periods=20).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_aligntrendlng_80d_base_v064_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """80-bar mean of sign(gap) * sign(60d trend in closeadj)."""
    pc = closeadj.shift(1)
    g = open - pc
    trend = closeadj - closeadj.shift(60)
    raw = np.sign(g) * np.sign(trend)
    out = raw.rolling(80, min_periods=40).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group V: gap density / clusters ---------------------------------------


def f07gb_f07_gap_behavior_gapclust_30d_base_v065_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """30-bar concentration index of large gaps: sum(gap^2) / (sum |gap|)^2.
    High when gaps are concentrated in few bars."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    sqs = (g * g).rolling(30, min_periods=30).sum()
    abs_sum = g.abs().rolling(30, min_periods=30).sum()
    out = sqs / (abs_sum * abs_sum).replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapcumabs_120d_base_v066_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """120-bar sum of |gap| / 120-bar sum of |return|. Fraction of total
    movement that occurs overnight."""
    pc = closeadj.shift(1)
    g = ((open - pc) / pc.replace(0.0, np.nan)).abs()
    r = closeadj.pct_change(1).abs()
    out = g.rolling(120, min_periods=120).sum() / r.rolling(120, min_periods=120).sum().replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group W: gap vs prior gap (lag-1 dependence) --------------------------


def f07gb_f07_gap_behavior_gappgap_1d_base_v067_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Today's gap minus yesterday's gap (lag-1 differenced gap)."""
    pc = close.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    out = g - g.shift(1)
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapfollow_40d_base_v068_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """40-bar count of bars where sign(gap_t) == sign(gap_{t-1}) (follow-through)."""
    pc = closeadj.shift(1)
    g = open - pc
    s = np.sign(g)
    same = (s == s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    out = same.rolling(40, min_periods=40).sum()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group X: gap-after-streak --------------------------------------------


def f07gb_f07_gap_behavior_gapafterup_50d_base_v069_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """50-bar mean gap pct on days that follow 3+ consecutive up closes."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    rsign = np.sign(closeadj.diff())
    up3 = ((rsign.shift(1) > 0) & (rsign.shift(2) > 0) & (rsign.shift(3) > 0)).astype(float)
    masked = g.where(up3 > 0.5)
    out = masked.rolling(50, min_periods=5).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapafterdn_50d_base_v070_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """50-bar mean gap pct on days that follow 3+ consecutive down closes."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    rsign = np.sign(closeadj.diff())
    dn3 = ((rsign.shift(1) < 0) & (rsign.shift(2) < 0) & (rsign.shift(3) < 0)).astype(float)
    masked = g.where(dn3 > 0.5)
    out = masked.rolling(50, min_periods=5).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group Y: gap fill probability and unfilled-stack ----------------------


def f07gb_f07_gap_behavior_unfilcnt_40d_base_v071_signal(open: pd.Series, high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """40-bar count of unfilled gaps (gap, low/high did not retrace to prev close)."""
    pc = closeadj.shift(1)
    g = open - pc
    up_unf = ((g > 0) & (low > pc)).astype(float)
    dn_unf = ((g < 0) & (high < pc)).astype(float)
    unf = (up_unf + dn_unf).where(~g.isna())
    out = unf.rolling(40, min_periods=40).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_unfilfrac_60d_base_v072_signal(open: pd.Series, high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """60-bar fraction of gap-bars that remained unfilled within their day."""
    pc = closeadj.shift(1)
    g = open - pc
    up_unf = ((g > 0) & (low > pc)).astype(float)
    dn_unf = ((g < 0) & (high < pc)).astype(float)
    unf = (up_unf + dn_unf).where(~g.isna())
    has_gap = (g != 0.0).astype(float).where(~g.isna())
    s_unf = unf.rolling(60, min_periods=30).sum()
    s_tot = has_gap.rolling(60, min_periods=30).sum()
    out = s_unf / s_tot.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group Z: cross-window differentials and slope-of-aggregates -----------


def f07gb_f07_gap_behavior_gapdiff_short_base_v073_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """mean(gap, 10) - mean(gap, 60): short-vs-long mean gap differential."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    m10 = g.rolling(10, min_periods=10).mean()
    m60 = g.rolling(60, min_periods=60).mean()
    out = m10 - m60
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapabsdiff_60d_base_v074_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """mean(|gap|, 20) - mean(|gap|, 60): short-vs-long gap magnitude differential."""
    pc = closeadj.shift(1)
    g = ((open - pc) / pc.replace(0.0, np.nan)).abs()
    m20 = g.rolling(20, min_periods=20).mean()
    m60 = g.rolling(60, min_periods=60).mean()
    out = m20 - m60
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapwgtdir_40d_base_v075_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """40-bar weighted sign-of-gap, weighted by |gap|: sum(sign(g)*|g|^2) /
    sum(|g|^2). Heavily-weighted by big gaps, ignores small gaps. Distinct
    from EWM/SMA aggregates."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    w = g * g
    sg = np.sign(g) * w
    num = sg.rolling(40, min_periods=40).sum()
    den = w.rolling(40, min_periods=40).sum()
    out = num / den.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


def _e(fn, *inputs):
    return fn.__name__, {"inputs": list(inputs), "func": fn}


f07_gap_behavior_base_001_075_REGISTRY = dict([
    _e(f07gb_f07_gap_behavior_gappct_1d_base_v001_signal, "open", "close"),
    _e(f07gb_f07_gap_behavior_lgapcumlong_120d_base_v002_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapabsnrm_5d_base_v003_signal, "open", "close"),
    _e(f07gb_f07_gap_behavior_gapsgn_1d_base_v004_signal, "open", "close"),
    _e(f07gb_f07_gap_behavior_gapmean_10d_base_v005_signal, "open", "close"),
    _e(f07gb_f07_gap_behavior_gapsum_21d_base_v006_signal, "open", "close"),
    _e(f07gb_f07_gap_behavior_gapmed_50d_base_v007_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapsumabs_30d_base_v008_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapstd_20d_base_v009_signal, "open", "close"),
    _e(f07gb_f07_gap_behavior_gapmad_40d_base_v010_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gaprng_30d_base_v011_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapiqr_60d_base_v012_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_bigfrac_30d_base_v013_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_posnegratio_120d_base_v014_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gaprnkmed_50d_base_v015_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gaprnkabs_80d_base_v016_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_fillbin_1d_base_v017_signal, "open", "high", "low", "close"),
    _e(f07gb_f07_gap_behavior_fillratio_1d_base_v018_signal, "open", "high", "low", "close"),
    _e(f07gb_f07_gap_behavior_fillrate_30d_base_v019_signal, "open", "high", "low", "closeadj"),
    _e(f07gb_f07_gap_behavior_partfillmean_20d_base_v020_signal, "open", "high", "low", "close"),
    _e(f07gb_f07_gap_behavior_gapgo_1d_base_v021_signal, "open", "close"),
    _e(f07gb_f07_gap_behavior_gaprev_1d_base_v022_signal, "open", "close"),
    _e(f07gb_f07_gap_behavior_gapgomean_40d_base_v023_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapcontinue_30d_base_v024_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_upstrk_1d_base_v025_signal, "open", "close"),
    _e(f07gb_f07_gap_behavior_dnstrk_1d_base_v026_signal, "open", "close"),
    _e(f07gb_f07_gap_behavior_gapsignstrk_1d_base_v027_signal, "open", "close"),
    _e(f07gb_f07_gap_behavior_upcnt_20d_base_v028_signal, "open", "close"),
    _e(f07gb_f07_gap_behavior_dncnt_40d_base_v029_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_bigcnt_60d_base_v030_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_sigcnt_50d_base_v031_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_maxup_30d_base_v032_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_maxdn_60d_base_v033_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_posneg_30d_base_v034_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_extrme_50d_base_v035_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_grtorng_1d_base_v036_signal, "open", "high", "low", "close"),
    _e(f07gb_f07_gap_behavior_grtoprng_1d_base_v037_signal, "open", "high", "low", "close"),
    _e(f07gb_f07_gap_behavior_grtoatrmean_14d_base_v038_signal, "open", "high", "low", "close"),
    _e(f07gb_f07_gap_behavior_grbig_30d_base_v039_signal, "open", "high", "low", "closeadj"),
    _e(f07gb_f07_gap_behavior_dayslast_60d_base_v040_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_dayslastup_40d_base_v041_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_dayslastdn_40d_base_v042_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapskew_60d_base_v043_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapkurt_80d_base_v044_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapac1_50d_base_v045_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapac2_70d_base_v046_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapcls_1d_base_v047_signal, "open", "close"),
    _e(f07gb_f07_gap_behavior_gapclsmean_30d_base_v048_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_lgapsum_60d_base_v049_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_lgapewm_30d_base_v050_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_lgapewmabs_50d_base_v051_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapextrnk_30d_base_v052_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapaccel_1d_base_v053_signal, "open", "close"),
    _e(f07gb_f07_gap_behavior_gapsigmoid_30d_base_v054_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapvsret_30d_base_v055_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapvsfwd_40d_base_v056_signal, "open", "high", "low", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapintravar_30d_base_v057_signal, "open", "high", "low", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapvol_50d_base_v058_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_closegap_1d_base_v059_signal, "open", "close"),
    _e(f07gb_f07_gap_behavior_closegapmean_30d_base_v060_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_uppct_60d_base_v061_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_dnpct_90d_base_v062_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_aligntrend_40d_base_v063_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_aligntrendlng_80d_base_v064_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapclust_30d_base_v065_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapcumabs_120d_base_v066_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gappgap_1d_base_v067_signal, "open", "close"),
    _e(f07gb_f07_gap_behavior_gapfollow_40d_base_v068_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapafterup_50d_base_v069_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapafterdn_50d_base_v070_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_unfilcnt_40d_base_v071_signal, "open", "high", "low", "closeadj"),
    _e(f07gb_f07_gap_behavior_unfilfrac_60d_base_v072_signal, "open", "high", "low", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapdiff_short_base_v073_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapabsdiff_60d_base_v074_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapwgtdir_40d_base_v075_signal, "open", "closeadj"),
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
    for name, entry in f07_gap_behavior_base_001_075_REGISTRY.items():
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
