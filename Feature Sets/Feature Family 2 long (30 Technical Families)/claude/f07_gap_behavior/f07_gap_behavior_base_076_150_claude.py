"""f07_gap_behavior base features 076-150.

Domain: overnight gap behavior. Continuation of the v001-075 file with
75 additional, structurally distinct features. All features reference
the open vs prior-close gap construct in some form:
  gap   = (open - close.shift(1)) / close.shift(1)
  sgap  = open - close.shift(1)
  lgap  = log(open / close.shift(1))

Each function is a fully expanded def: formula inline, no _core()
factory, no parametric reuse. NaN policy: never fillna(0); only
replace([inf,-inf], nan) at the final return.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Features 076-150
# ---------------------------------------------------------------------------


# --- Group A: gap classification distributions ------------------------------


def f07gb_f07_gap_behavior_smallcnt_50d_base_v076_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """50-bar count of small gaps (|gap| in (0.1%, 0.5%])."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    sm = ((g.abs() > 0.001) & (g.abs() <= 0.005)).astype(float).where(~g.isna())
    out = sm.rolling(50, min_periods=50).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_medcnt_50d_base_v077_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """50-bar count of medium gaps (|gap| in (0.5%, 1.5%])."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    md = ((g.abs() > 0.005) & (g.abs() <= 0.015)).astype(float).where(~g.isna())
    out = md.rolling(50, min_periods=50).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_lrgcnt_80d_base_v078_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """80-bar count of large gaps (|gap| > 1.5%)."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    lg = (g.abs() > 0.015).astype(float).where(~g.isna())
    out = lg.rolling(80, min_periods=80).sum()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group B: gap quantile bands -------------------------------------------


def f07gb_f07_gap_behavior_gapq90_80d_base_v079_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """80-bar 90th-percentile of gap pct."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    out = g.rolling(80, min_periods=80).quantile(0.90)
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapq10_80d_base_v080_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """80-bar 10th-percentile of gap pct."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    out = g.rolling(80, min_periods=80).quantile(0.10)
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapsymq_60d_base_v081_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """60-bar (q90+q10) of gap pct -- gap-distribution asymmetry indicator."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    q9 = g.rolling(60, min_periods=60).quantile(0.90)
    q1 = g.rolling(60, min_periods=60).quantile(0.10)
    out = q9 + q1
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group C: cross-correlations between gap and other quantities -----------


def f07gb_f07_gap_behavior_gapvsvol_50d_base_v082_signal(open: pd.Series, closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """50-bar correlation between |gap| and log volume. Big gaps on heavy volume?"""
    pc = closeadj.shift(1)
    g = ((open - pc) / pc.replace(0.0, np.nan)).abs()
    lv = np.log(volume.replace(0.0, np.nan))
    out = g.rolling(50, min_periods=50).corr(lv)
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapvslag_40d_base_v083_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """40-bar correlation between current gap and gap 2 days ago.
    Tests medium-lag autocorrelation."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    out = g.rolling(40, min_periods=40).corr(g.shift(2))
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapvsrange_40d_base_v084_signal(open: pd.Series, high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """40-bar correlation between |gap| and intraday range. Co-volatility test."""
    pc = closeadj.shift(1)
    g = ((open - pc) / pc.replace(0.0, np.nan)).abs()
    rng = (high - low) / closeadj.replace(0.0, np.nan)
    out = g.rolling(40, min_periods=40).corr(rng)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group D: gap-relative-to-volatility regimes ----------------------------


def f07gb_f07_gap_behavior_gapsdr_30d_base_v085_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """30-bar std(gap) / 30-bar mean(|return|): how volatile are gaps relative
    to typical daily move."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    r = closeadj.pct_change(1).abs()
    gsd = g.rolling(30, min_periods=30).std(ddof=1)
    rmu = r.rolling(30, min_periods=30).mean()
    out = gsd / rmu.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapmaxnrm_60d_base_v086_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """60-bar max(|gap|) / 60-bar mean(|gap|). Spike-y gap regime indicator."""
    pc = closeadj.shift(1)
    g = ((open - pc) / pc.replace(0.0, np.nan)).abs()
    mx = g.rolling(60, min_periods=60).max()
    mu = g.rolling(60, min_periods=60).mean()
    out = mx / mu.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group E: time-decay / EWMA -based gap signals --------------------------


def f07gb_f07_gap_behavior_gapdiffstd_20d_base_v087_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """20-bar std of (gap_t - gap_{t-1}): volatility of gap-changes (jerk-like
    variability proxy). Distinct from per-bar gap level."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    dg = g - g.shift(1)
    out = dg.rolling(20, min_periods=20).std(ddof=1)
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapcounttrend_80d_base_v088_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """80-bar count of non-trivial gaps (|gap|>0.2%) divided by 40-bar count.
    Indicator of regime change in gap frequency."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    has = (g.abs() > 0.002).astype(float).where(~g.isna())
    c80 = has.rolling(80, min_periods=80).sum()
    c40 = has.rolling(40, min_periods=40).sum()
    out = c80 / c40.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group F: cumulative / drift features -----------------------------------


def f07gb_f07_gap_behavior_gapcummean_200d_base_v089_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """200-bar mean of gap pct -- long-horizon overnight bias."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    out = g.rolling(200, min_periods=200).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapcumabs_200d_base_v090_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """200-bar mean of |gap| -- long-horizon overnight magnitude."""
    pc = closeadj.shift(1)
    g = ((open - pc) / pc.replace(0.0, np.nan)).abs()
    out = g.rolling(200, min_periods=200).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group G: gap-return interaction --------------------------------------


def f07gb_f07_gap_behavior_overnightfrac_60d_base_v091_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """60-bar (sum overnight returns) / (sum close-to-close returns).
    Fraction of total drift coming from overnight moves."""
    pc = closeadj.shift(1)
    on = np.log(open / pc.replace(0.0, np.nan))
    c2c = np.log(closeadj / pc.replace(0.0, np.nan))
    out = on.rolling(60, min_periods=60).sum() / c2c.rolling(60, min_periods=60).sum().replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_intradayfrac_60d_base_v092_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """60-bar (sum intraday returns log(close/open)) / sum |log(open/prev_close)|.
    Intraday move vs overnight magnitude."""
    pc = closeadj.shift(1)
    intra = np.log(closeadj / open.replace(0.0, np.nan))
    on_abs = np.log(open / pc.replace(0.0, np.nan)).abs()
    out = intra.rolling(60, min_periods=60).sum() / on_abs.rolling(60, min_periods=60).sum().replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group H: gap-volume scaled signals -------------------------------------


def f07gb_f07_gap_behavior_gapwdvol_30d_base_v093_signal(open: pd.Series, closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """30-bar volume-weighted gap: sum(gap*volume)/sum(volume). Big-volume gaps
    weighted more heavily."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    gv = (g * volume).rolling(30, min_periods=30).sum()
    v = volume.rolling(30, min_periods=30).sum()
    out = gv / v.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gaplvolz_50d_base_v094_signal(open: pd.Series, closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """50-bar mean of (|gap| * z-score(volume)). Captures co-occurrence of big
    gaps and unusual volume."""
    pc = closeadj.shift(1)
    g = ((open - pc) / pc.replace(0.0, np.nan)).abs()
    lv = np.log(volume.replace(0.0, np.nan))
    mu = lv.rolling(50, min_periods=50).mean()
    sd = lv.rolling(50, min_periods=50).std(ddof=1)
    z = (lv - mu) / sd.replace(0.0, np.nan)
    out = (g * z).rolling(50, min_periods=50).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group I: gap-streak max windows ---------------------------------------


def f07gb_f07_gap_behavior_maxupstrk_60d_base_v095_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """60-bar longest consecutive up-gap run."""
    pc = closeadj.shift(1)
    g = open - pc
    up = (g > 0).astype(float).where(~g.isna())
    def _longest(x):
        x = np.asarray(x, dtype=float)
        if np.any(~np.isfinite(x)):
            return np.nan
        best = 0; cur = 0
        for v in x:
            if v > 0.5:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return float(best)
    out = up.rolling(60, min_periods=60).apply(_longest, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_maxdnstrk_60d_base_v096_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """60-bar longest consecutive down-gap run."""
    pc = closeadj.shift(1)
    g = open - pc
    dn = (g < 0).astype(float).where(~g.isna())
    def _longest(x):
        x = np.asarray(x, dtype=float)
        if np.any(~np.isfinite(x)):
            return np.nan
        best = 0; cur = 0
        for v in x:
            if v > 0.5:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return float(best)
    out = dn.rolling(60, min_periods=60).apply(_longest, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group J: gap-distribution shape ---------------------------------------


def f07gb_f07_gap_behavior_gapdownsskew_80d_base_v097_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """80-bar downside skewness of gaps: cube-mean of negative-only gaps
    divided by their std^3. Captures heavy-down-tail asymmetry."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    neg = g.where(g < 0)
    sd = neg.rolling(80, min_periods=10).std(ddof=1)
    mu = neg.rolling(80, min_periods=10).mean()
    m3 = ((neg - mu) ** 3).rolling(80, min_periods=10).mean()
    out = m3 / (sd ** 3).replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gaptaildiff_80d_base_v098_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """80-bar (q95 - q5) / (q75 - q25) of gap: tail vs body width ratio."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    q95 = g.rolling(80, min_periods=80).quantile(0.95)
    q05 = g.rolling(80, min_periods=80).quantile(0.05)
    q75 = g.rolling(80, min_periods=80).quantile(0.75)
    q25 = g.rolling(80, min_periods=80).quantile(0.25)
    out = (q95 - q05) / (q75 - q25).replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group K: directionally-conditional aggregates -------------------------


def f07gb_f07_gap_behavior_avgupgap_60d_base_v099_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """60-bar mean of positive gaps only (NaN if none)."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    pos = g.where(g > 0)
    out = pos.rolling(60, min_periods=10).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_avgdngap_60d_base_v100_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """60-bar mean of |negative gaps| only."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    neg = (-g).where(g < 0)
    out = neg.rolling(60, min_periods=10).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group L: gap-vs-prior-bar-features (positions) -----------------------


def f07gb_f07_gap_behavior_gapatop_1d_base_v101_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Did the gap open in the upper third of prior range?
    z = (open - prior_low) / (prior_high - prior_low) -- only when there is a gap."""
    pc = close.shift(1)
    g = open - pc
    span = (high.shift(1) - low.shift(1)).replace(0.0, np.nan)
    pos = (open - low.shift(1)) / span
    out = pos.where(g != 0.0)
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapatopmean_30d_base_v102_signal(open: pd.Series, high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """30-bar mean of (open - prior_low)/(prior_high - prior_low) on gap bars."""
    pc = closeadj.shift(1)
    g = open - pc
    span = (high.shift(1) - low.shift(1)).replace(0.0, np.nan)
    pos = (open - low.shift(1)) / span
    pos = pos.where(g != 0.0)
    out = pos.rolling(30, min_periods=15).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group M: smoothed gap-fill metrics ------------------------------------


def f07gb_f07_gap_behavior_fillewm_50d_base_v103_signal(open: pd.Series, high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """EWM-50 of gap-fill binary."""
    pc = closeadj.shift(1)
    g = open - pc
    up_fill = (low <= pc) & (g > 0)
    dn_fill = (high >= pc) & (g < 0)
    filled = (up_fill | dn_fill).astype(float).where(g != 0.0)
    out = filled.ewm(span=50, adjust=False, min_periods=20).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_fillpart_80d_base_v104_signal(open: pd.Series, high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """80-bar mean of partial-fill ratio, sub-window median smoothed."""
    pc = closeadj.shift(1)
    g = open - pc
    up_amt = (open - low) / g.where(g > 0, np.nan)
    dn_amt = (high - open) / (-g).where(g < 0, np.nan)
    raw = up_amt.combine_first(dn_amt).clip(lower=0.0, upper=1.0)
    out = raw.rolling(80, min_periods=20).median()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group N: relative bar-position after gap ------------------------------


def f07gb_f07_gap_behavior_postgaprng_1d_base_v105_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """How much the bar moves after the gap-open relative to gap magnitude.
    For up gap: (high - open)/(open - prev_close); for down gap: (open - low)/(prev_close - open)."""
    pc = close.shift(1)
    g = open - pc
    up_mv = (high - open) / g.where(g > 0, np.nan)
    dn_mv = (open - low) / (-g).where(g < 0, np.nan)
    raw = up_mv.combine_first(dn_mv)
    out = raw.clip(lower=0.0, upper=10.0)
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_postgapbeta_50d_base_v106_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """50-bar OLS beta: intraday_return = a + beta * gap. Negative beta = mean
    revert; positive = continuation. Distinct from sd-ratio aggregates."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    intra = (closeadj - open) / open.replace(0.0, np.nan)
    cov = g.rolling(50, min_periods=50).cov(intra)
    var = g.rolling(50, min_periods=50).var(ddof=1)
    out = cov / var.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group O: cross-window differential aggregates -------------------------


def f07gb_f07_gap_behavior_gapsdratio_60d_base_v107_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """60-bar std(gap) / 200-bar std(gap). >1 = recent gaps are unusually volatile."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    s60 = g.rolling(60, min_periods=60).std(ddof=1)
    s200 = g.rolling(200, min_periods=200).std(ddof=1)
    out = s60 / s200.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapmagchg_30d_base_v108_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """log(mean(|gap|, 30) / mean(|gap|, 90)): magnitude-regime shift."""
    pc = closeadj.shift(1)
    g = ((open - pc) / pc.replace(0.0, np.nan)).abs()
    m30 = g.rolling(30, min_periods=30).mean()
    m90 = g.rolling(90, min_periods=90).mean()
    out = np.log(m30.replace(0.0, np.nan) / m90.replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group P: gap-EWM crossovers (sign signals) -----------------------------


def f07gb_f07_gap_behavior_gapewmx_60d_base_v109_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """sign(EWM(gap,10) - EWM(gap,40)): sign of gap-trend MA crossover."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    fast = g.ewm(span=10, adjust=False, min_periods=10).mean()
    slow = g.ewm(span=40, adjust=False, min_periods=40).mean()
    s = np.sign(fast - slow)
    out = s.where(~fast.isna() & ~slow.isna())
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapewmspr_60d_base_v110_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """EWM(gap,15) - EWM(gap,60): the gap-trend MA spread itself."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    f15 = g.ewm(span=15, adjust=False, min_periods=15).mean()
    s60 = g.ewm(span=60, adjust=False, min_periods=60).mean()
    out = f15 - s60
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group Q: gap and intraday relation -----------------------------------


def f07gb_f07_gap_behavior_gapintsgn_30d_base_v111_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """30-bar mean of sign(gap) - sign(close-open).
    +2 = gaps up but day closes down (heavy reversal), 0 = matched, -2 = gap dn day rallies."""
    pc = closeadj.shift(1)
    g = open - pc
    intra = closeadj - open
    s_g = np.sign(g).where(~g.isna())
    s_i = np.sign(intra).where(~intra.isna())
    raw = s_g - s_i
    out = raw.rolling(30, min_periods=15).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapfaderate_50d_base_v112_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """50-bar fraction of gap-bars where intraday move opposed the gap.
    (gap*intraday < 0)"""
    pc = closeadj.shift(1)
    g = open - pc
    intra = closeadj - open
    fade = ((g * intra) < 0).astype(float).where(~g.isna() & ~intra.isna() & (g != 0.0))
    out = fade.rolling(50, min_periods=25).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group R: gap timing / clustering --------------------------------------


def f07gb_f07_gap_behavior_gaprecencysum_30d_base_v113_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """30-bar exponentially-decayed (alpha=0.1) sum of |gap| -- weighting
    recent gaps more strongly than distant ones."""
    pc = closeadj.shift(1)
    g = ((open - pc) / pc.replace(0.0, np.nan)).abs()
    out = g.ewm(alpha=0.1, adjust=False, min_periods=30).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapdensity_60d_base_v114_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """60-bar fraction of bars that had any non-trivial gap (|gap|>0.05%)."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    has = (g.abs() > 0.0005).astype(float).where(~g.isna())
    out = has.rolling(60, min_periods=60).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group S: gap and prior-day-direction interactions ---------------------


def f07gb_f07_gap_behavior_gapcondup_50d_base_v115_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """50-bar mean gap pct conditional on prior day's close > prior-prior day's close."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    prev_up = (closeadj.shift(1) > closeadj.shift(2)).astype(float)
    cond = g.where(prev_up > 0.5)
    out = cond.rolling(50, min_periods=10).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapconddn_50d_base_v116_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """50-bar mean gap pct conditional on prior day's close < prior-prior day's close."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    prev_dn = (closeadj.shift(1) < closeadj.shift(2)).astype(float)
    cond = g.where(prev_dn > 0.5)
    out = cond.rolling(50, min_periods=10).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group T: gap and high/low extension ----------------------------------


def f07gb_f07_gap_behavior_gapnew_high_30d_base_v117_signal(open: pd.Series, high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """30-bar count of (up gap & high > prior_high) -- breakaway up gaps."""
    pc = closeadj.shift(1)
    g = open - pc
    cond = ((g > 0) & (high > high.shift(1))).astype(float).where(~g.isna())
    out = cond.rolling(30, min_periods=30).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapnew_low_30d_base_v118_signal(open: pd.Series, high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """30-bar count of (down gap & low < prior_low) -- breakaway down gaps."""
    pc = closeadj.shift(1)
    g = open - pc
    cond = ((g < 0) & (low < low.shift(1))).astype(float).where(~g.isna())
    out = cond.rolling(30, min_periods=30).sum()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group U: gap-bar position metrics ------------------------------------


def f07gb_f07_gap_behavior_gappxpos_50d_base_v119_signal(open: pd.Series, high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """50-bar mean of |gap| / 50-bar (max(high) - min(low)). Gap as fraction of
    long-window price-range."""
    pc = closeadj.shift(1)
    g = (open - pc).abs()
    rng = high.rolling(50, min_periods=50).max() - low.rolling(50, min_periods=50).min()
    r = g / rng.replace(0.0, np.nan)
    out = r.rolling(50, min_periods=50).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapboxpos_30d_base_v120_signal(open: pd.Series, high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """30-bar (open - max(prev_30 high)) on up-gaps relative to box-top. Indicates
    breakout strength. NaN on non-up-gap bars."""
    pc = closeadj.shift(1)
    g = open - pc
    box_top = high.shift(1).rolling(30, min_periods=30).max()
    diff = (open - box_top) / closeadj.replace(0.0, np.nan)
    out = diff.where(g > 0)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group V: gap-relative-to-close direction matching ---------------------


def f07gb_f07_gap_behavior_gapprodint_20d_base_v121_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """20-bar mean of gap * (close-open) -- average product of gap direction and
    same-bar intraday move. Direction-confirmation aggregate."""
    pc = close.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    intra = (close - open) / open.replace(0.0, np.nan)
    out = (g * intra).rolling(20, min_periods=20).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapsignsumlng_120d_base_v122_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """120-bar sum of sign(gap): net polarity over long window."""
    pc = closeadj.shift(1)
    g = open - pc
    s = np.sign(g).where(~g.isna())
    out = s.rolling(120, min_periods=120).sum()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group W: gap entropy / variability indicators -------------------------


def f07gb_f07_gap_behavior_gapcv_60d_base_v123_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """60-bar std(gap) / mean(|gap|): coefficient of variation for gaps."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    sd = g.rolling(60, min_periods=60).std(ddof=1)
    mu = g.abs().rolling(60, min_periods=60).mean()
    out = sd / mu.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gappnratio_30d_base_v124_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """30-bar count(positive gap) / count(negative gap). >1 = up-bias."""
    pc = closeadj.shift(1)
    g = open - pc
    up = (g > 0).astype(float).where(~g.isna())
    dn = (g < 0).astype(float).where(~g.isna())
    su = up.rolling(30, min_periods=30).sum()
    sd = dn.rolling(30, min_periods=30).sum()
    out = su / sd.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group X: gap-direction prediction / momentum -------------------------


def f07gb_f07_gap_behavior_gapmom_5d_base_v125_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """5-bar sum of gap pct -- short overnight momentum."""
    pc = close.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    out = g.rolling(5, min_periods=5).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapmomlong_90d_base_v126_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """90-bar sum of gap pct -- long overnight momentum."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    out = g.rolling(90, min_periods=90).sum()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group Y: gap regression (slope of gap vs time within window) ---------


def f07gb_f07_gap_behavior_gapregslp_60d_base_v127_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """60-bar OLS slope of gap pct vs time index. Captures trend in gap level."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    n = 60
    t = np.arange(n, dtype=float)
    tmean = t.mean()
    tvar = ((t - tmean) ** 2).sum()
    def _slp(x):
        if not np.all(np.isfinite(x)):
            return np.nan
        xm = x.mean()
        return float(((t - tmean) * (x - xm)).sum() / tvar)
    out = g.rolling(n, min_periods=n).apply(_slp, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapabsregslp_80d_base_v128_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """80-bar OLS slope of |gap| vs time. Captures gap-volatility trend."""
    pc = closeadj.shift(1)
    g = ((open - pc) / pc.replace(0.0, np.nan)).abs()
    n = 80
    t = np.arange(n, dtype=float)
    tmean = t.mean()
    tvar = ((t - tmean) ** 2).sum()
    def _slp(x):
        if not np.all(np.isfinite(x)):
            return np.nan
        xm = x.mean()
        return float(((t - tmean) * (x - xm)).sum() / tvar)
    out = g.rolling(n, min_periods=n).apply(_slp, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group Z: gap-by-segment indicators -----------------------------------


def f07gb_f07_gap_behavior_gaphvol_40d_base_v129_signal(open: pd.Series, closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """40-bar mean |gap| in top-quartile-volume bars only.
    Captures whether gap-magnitude regime under heavy volume differs."""
    pc = closeadj.shift(1)
    g = ((open - pc) / pc.replace(0.0, np.nan)).abs()
    lv = np.log(volume.replace(0.0, np.nan))
    q75 = lv.rolling(40, min_periods=40).quantile(0.75)
    big = (lv >= q75)
    cond = g.where(big)
    out = cond.rolling(40, min_periods=10).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gaplvol_40d_base_v130_signal(open: pd.Series, closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """40-bar mean |gap| in bottom-quartile-volume bars only."""
    pc = closeadj.shift(1)
    g = ((open - pc) / pc.replace(0.0, np.nan)).abs()
    lv = np.log(volume.replace(0.0, np.nan))
    q25 = lv.rolling(40, min_periods=40).quantile(0.25)
    sm = (lv <= q25)
    cond = g.where(sm)
    out = cond.rolling(40, min_periods=10).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group AA: combined gap composites ------------------------------------


def f07gb_f07_gap_behavior_gapatropmean_30d_base_v131_signal(open: pd.Series, high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """30-bar mean of (|gap| - ATR_14) / ATR_14: how much typical gaps exceed
    typical bar TR -- a magnitude-vs-typical-range residual."""
    pc = closeadj.shift(1)
    g = (open - pc).abs()
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    raw = (g - atr) / atr.replace(0.0, np.nan)
    out = raw.rolling(30, min_periods=15).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapcrosssym_60d_base_v132_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """60-bar (gap_skew * gap_kurt): combined shape signal."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    sk = g.rolling(60, min_periods=60).skew()
    kt = g.rolling(60, min_periods=60).kurt()
    out = sk * kt
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group AB: gap-rank vs absolute-rank -----------------------------------


def f07gb_f07_gap_behavior_gapabsrnk_30d_base_v133_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """30-bar pct-rank of current |gap| in trailing 30 -- smoothed by 5-mean."""
    pc = closeadj.shift(1)
    g = ((open - pc) / pc.replace(0.0, np.nan)).abs()
    pr = g.rolling(30, min_periods=30).rank(pct=True)
    out = pr.rolling(5, min_periods=5).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gaplargefr_60d_base_v134_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """60-bar fraction of total |gap| concentrated in top-5 largest gaps.
    Captures sparseness vs density of gap energy."""
    pc = closeadj.shift(1)
    g = ((open - pc) / pc.replace(0.0, np.nan)).abs()
    def _topfr(x):
        x = np.asarray(x, dtype=float)
        if not np.all(np.isfinite(x)) or x.sum() <= 0.0:
            return np.nan
        top = np.sort(x)[-5:].sum()
        return float(top / x.sum())
    out = g.rolling(60, min_periods=60).apply(_topfr, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group AC: gap unfilled-stack tracking --------------------------------


def f07gb_f07_gap_behavior_unfildur_60d_base_v135_signal(open: pd.Series, high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Bars since last unfilled gap, capped at 60. Tracks how recently a
    gap remained open through the day."""
    pc = closeadj.shift(1)
    g = open - pc
    up_unf = ((g > 0) & (low > pc)).astype(float)
    dn_unf = ((g < 0) & (high < pc)).astype(float)
    unf = (up_unf + dn_unf).where(~g.isna())
    n = 60
    def _last_one(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return float(n)
        return float(len(x) - 1 - idx[-1])
    out = unf.rolling(n, min_periods=n).apply(_last_one, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_unfilbias_50d_base_v136_signal(open: pd.Series, high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """50-bar (up_unfilled - dn_unfilled) / total bars. Sign = which direction
    has more unfilled gaps."""
    pc = closeadj.shift(1)
    g = open - pc
    up_unf = ((g > 0) & (low > pc)).astype(float)
    dn_unf = ((g < 0) & (high < pc)).astype(float)
    u = up_unf.rolling(50, min_periods=50).sum()
    d = dn_unf.rolling(50, min_periods=50).sum()
    out = (u - d) / 50.0
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group AD: gap-relative-to-MA -----------------------------------------


def f07gb_f07_gap_behavior_gapvssma_50d_base_v137_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """50-bar mean gap pct - 50-bar (open/SMA50 - 1). Disentangles overnight
    drift from spot-vs-MA position."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    s50 = closeadj.rolling(50, min_periods=50).mean()
    rel = (open - s50) / s50.replace(0.0, np.nan)
    gmu = g.rolling(50, min_periods=50).mean()
    rmu = rel.rolling(50, min_periods=50).mean()
    out = gmu - rmu
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapvsema_60d_base_v138_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """sign(gap) where current open vs EMA60 is on the same side. Captures
    gap-direction agreeing with trend."""
    pc = closeadj.shift(1)
    g = open - pc
    ema = closeadj.ewm(span=60, adjust=False, min_periods=60).mean()
    trend = open - ema
    raw = np.sign(g) * np.sign(trend)
    out = raw.rolling(40, min_periods=20).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group AE: gap-volume features (composite) ----------------------------


def f07gb_f07_gap_behavior_gapvolblend_30d_base_v139_signal(open: pd.Series, closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """30-bar mean of (signed-gap * sign(volume - vol_ma_30)).
    Captures whether big gaps come with above-average volume confirmation."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    vma = volume.rolling(30, min_periods=30).mean()
    vsig = np.sign(volume - vma)
    out = (g * vsig).rolling(30, min_periods=30).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group AF: gap-zscore-extreme detection -------------------------------


def f07gb_f07_gap_behavior_gapextfrac_120d_base_v140_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """120-bar fraction of bars where gap exceeds 2x trailing 120-bar std(gap)."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    sd = g.rolling(120, min_periods=120).std(ddof=1)
    ext = (g.abs() > 2.0 * sd).astype(float).where(~g.isna() & ~sd.isna())
    out = ext.rolling(120, min_periods=120).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group AG: gap-fill-time / fade window --------------------------------


def f07gb_f07_gap_behavior_gapfadewin_60d_base_v141_signal(open: pd.Series, high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """60-bar fraction where gap fully faded (closed below prior close on up gap
    or above prior close on down gap)."""
    pc = closeadj.shift(1)
    g = open - pc
    fade_up = ((g > 0) & (closeadj < pc)).astype(float)
    fade_dn = ((g < 0) & (closeadj > pc)).astype(float)
    fade = (fade_up + fade_dn).where(~g.isna() & (g != 0.0))
    out = fade.rolling(60, min_periods=30).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group AH: relative gap on prior gap conditional ----------------------


def f07gb_f07_gap_behavior_postupgapret_40d_base_v142_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """40-bar mean of next-day return after up-gap days.
    Tests reversion vs continuation of up-gap moves."""
    pc = closeadj.shift(1)
    g = open - pc
    next_ret = closeadj.pct_change(1).shift(-1)
    up_day = (g > 0).astype(float)
    cond = next_ret.where(up_day > 0.5)
    out = cond.rolling(40, min_periods=10).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_postdngapret_40d_base_v143_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """40-bar mean of next-day return after down-gap days."""
    pc = closeadj.shift(1)
    g = open - pc
    next_ret = closeadj.pct_change(1).shift(-1)
    dn_day = (g < 0).astype(float)
    cond = next_ret.where(dn_day > 0.5)
    out = cond.rolling(40, min_periods=10).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group AI: gap-vs-VWAP-like proxy --------------------------------------


def f07gb_f07_gap_behavior_gapvssvap_50d_base_v144_signal(open: pd.Series, high: pd.Series, low: pd.Series, closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Open relative to 50-bar volume-weighted close minus open-vs-prev-close.
    Composite of gap vs vwap-position."""
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    vw = (closeadj * volume).rolling(50, min_periods=50).sum() / volume.rolling(50, min_periods=50).sum().replace(0.0, np.nan)
    rel = (open - vw) / vw.replace(0.0, np.nan)
    out = g - rel
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group AJ: gap-direction stability ------------------------------------


def f07gb_f07_gap_behavior_gapsignstab_30d_base_v145_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """30-bar (|sum sign(gap)|) / 30 -- magnitude of net direction, range [0,1]."""
    pc = closeadj.shift(1)
    g = open - pc
    s = np.sign(g).where(~g.isna())
    out = s.rolling(30, min_periods=30).sum().abs() / 30.0
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapscaledabs_40d_base_v146_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """40-bar mean of |gap| scaled by 40-bar realized vol of close-to-close returns.
    Z-like indicator of gap magnitude regime."""
    pc = closeadj.shift(1)
    g = ((open - pc) / pc.replace(0.0, np.nan)).abs()
    r = closeadj.pct_change(1)
    rv = r.rolling(40, min_periods=40).std(ddof=1)
    s = g / rv.replace(0.0, np.nan)
    out = s.rolling(40, min_periods=40).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group AK: gap and HL relative to prior-bar OHLC ----------------------


def f07gb_f07_gap_behavior_gapinbar_60d_base_v147_signal(open: pd.Series, high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """60-bar fraction of bars where open is between prev_low and prev_high
    (no true gap relative to prior bar's range)."""
    pc = closeadj.shift(1)
    g = open - pc
    inside = ((open >= low.shift(1)) & (open <= high.shift(1))).astype(float).where(~g.isna())
    out = inside.rolling(60, min_periods=60).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapoutbar_60d_base_v148_signal(open: pd.Series, high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """60-bar fraction of bars where open > prev_high (true breakout gap up)
    minus fraction where open < prev_low (true breakout gap down)."""
    pc = closeadj.shift(1)
    g = open - pc
    up = (open > high.shift(1)).astype(float).where(~g.isna())
    dn = (open < low.shift(1)).astype(float).where(~g.isna())
    out = up.rolling(60, min_periods=60).mean() - dn.rolling(60, min_periods=60).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group AL: final gap variants -----------------------------------------


def f07gb_f07_gap_behavior_gapsharpeabs_60d_base_v149_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """60-bar median(|gap|) / median absolute deviation of |gap|: robust scaled
    magnitude. Distinct from sum or mean-based aggregates."""
    pc = closeadj.shift(1)
    g = ((open - pc) / pc.replace(0.0, np.nan)).abs()
    med = g.rolling(60, min_periods=60).median()
    def _mad(x):
        x = np.asarray(x, dtype=float)
        if not np.all(np.isfinite(x)):
            return np.nan
        m = np.median(x)
        return float(np.median(np.abs(x - m)))
    mad = g.rolling(60, min_periods=60).apply(_mad, raw=True)
    out = med / mad.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapnegac_60d_base_v150_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """60-bar lag-3 partial autocorrelation of |gap| -- magnitude-clustering signal
    at lag 3 (distinct from lag-1/lag-2 on signed gaps)."""
    pc = closeadj.shift(1)
    g = ((open - pc) / pc.replace(0.0, np.nan)).abs()
    def _ac3(x):
        x = np.asarray(x, dtype=float)
        if not np.all(np.isfinite(x)):
            return np.nan
        x0 = x[:-3]; x1 = x[3:]
        m0 = x0.mean(); m1 = x1.mean()
        v0 = x0.std(ddof=1); v1 = x1.std(ddof=1)
        if v0 <= 0.0 or v1 <= 0.0:
            return np.nan
        return float(((x0 - m0) * (x1 - m1)).mean() / (v0 * v1))
    out = g.rolling(60, min_periods=60).apply(_ac3, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


def _e(fn, *inputs):
    return fn.__name__, {"inputs": list(inputs), "func": fn}


f07_gap_behavior_base_076_150_REGISTRY = dict([
    _e(f07gb_f07_gap_behavior_smallcnt_50d_base_v076_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_medcnt_50d_base_v077_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_lrgcnt_80d_base_v078_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapq90_80d_base_v079_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapq10_80d_base_v080_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapsymq_60d_base_v081_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapvsvol_50d_base_v082_signal, "open", "closeadj", "volume"),
    _e(f07gb_f07_gap_behavior_gapvslag_40d_base_v083_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapvsrange_40d_base_v084_signal, "open", "high", "low", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapsdr_30d_base_v085_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapmaxnrm_60d_base_v086_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapdiffstd_20d_base_v087_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapcounttrend_80d_base_v088_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapcummean_200d_base_v089_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapcumabs_200d_base_v090_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_overnightfrac_60d_base_v091_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_intradayfrac_60d_base_v092_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapwdvol_30d_base_v093_signal, "open", "closeadj", "volume"),
    _e(f07gb_f07_gap_behavior_gaplvolz_50d_base_v094_signal, "open", "closeadj", "volume"),
    _e(f07gb_f07_gap_behavior_maxupstrk_60d_base_v095_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_maxdnstrk_60d_base_v096_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapdownsskew_80d_base_v097_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gaptaildiff_80d_base_v098_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_avgupgap_60d_base_v099_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_avgdngap_60d_base_v100_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapatop_1d_base_v101_signal, "open", "high", "low", "close"),
    _e(f07gb_f07_gap_behavior_gapatopmean_30d_base_v102_signal, "open", "high", "low", "closeadj"),
    _e(f07gb_f07_gap_behavior_fillewm_50d_base_v103_signal, "open", "high", "low", "closeadj"),
    _e(f07gb_f07_gap_behavior_fillpart_80d_base_v104_signal, "open", "high", "low", "closeadj"),
    _e(f07gb_f07_gap_behavior_postgaprng_1d_base_v105_signal, "open", "high", "low", "close"),
    _e(f07gb_f07_gap_behavior_postgapbeta_50d_base_v106_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapsdratio_60d_base_v107_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapmagchg_30d_base_v108_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapewmx_60d_base_v109_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapewmspr_60d_base_v110_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapintsgn_30d_base_v111_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapfaderate_50d_base_v112_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gaprecencysum_30d_base_v113_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapdensity_60d_base_v114_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapcondup_50d_base_v115_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapconddn_50d_base_v116_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapnew_high_30d_base_v117_signal, "open", "high", "low", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapnew_low_30d_base_v118_signal, "open", "high", "low", "closeadj"),
    _e(f07gb_f07_gap_behavior_gappxpos_50d_base_v119_signal, "open", "high", "low", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapboxpos_30d_base_v120_signal, "open", "high", "low", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapprodint_20d_base_v121_signal, "open", "close"),
    _e(f07gb_f07_gap_behavior_gapsignsumlng_120d_base_v122_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapcv_60d_base_v123_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gappnratio_30d_base_v124_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapmom_5d_base_v125_signal, "open", "close"),
    _e(f07gb_f07_gap_behavior_gapmomlong_90d_base_v126_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapregslp_60d_base_v127_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapabsregslp_80d_base_v128_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gaphvol_40d_base_v129_signal, "open", "closeadj", "volume"),
    _e(f07gb_f07_gap_behavior_gaplvol_40d_base_v130_signal, "open", "closeadj", "volume"),
    _e(f07gb_f07_gap_behavior_gapatropmean_30d_base_v131_signal, "open", "high", "low", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapcrosssym_60d_base_v132_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapabsrnk_30d_base_v133_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gaplargefr_60d_base_v134_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_unfildur_60d_base_v135_signal, "open", "high", "low", "closeadj"),
    _e(f07gb_f07_gap_behavior_unfilbias_50d_base_v136_signal, "open", "high", "low", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapvssma_50d_base_v137_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapvsema_60d_base_v138_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapvolblend_30d_base_v139_signal, "open", "closeadj", "volume"),
    _e(f07gb_f07_gap_behavior_gapextfrac_120d_base_v140_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapfadewin_60d_base_v141_signal, "open", "high", "low", "closeadj"),
    _e(f07gb_f07_gap_behavior_postupgapret_40d_base_v142_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_postdngapret_40d_base_v143_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapvssvap_50d_base_v144_signal, "open", "high", "low", "closeadj", "volume"),
    _e(f07gb_f07_gap_behavior_gapsignstab_30d_base_v145_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapscaledabs_40d_base_v146_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapinbar_60d_base_v147_signal, "open", "high", "low", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapoutbar_60d_base_v148_signal, "open", "high", "low", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapsharpeabs_60d_base_v149_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapnegac_60d_base_v150_signal, "open", "closeadj"),
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
    for name, entry in f07_gap_behavior_base_076_150_REGISTRY.items():
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
