import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_FIVEYEAR = 1260
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _sum(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _median(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


# ===== folder domain primitives (dollar-volume VALUE magnitude / regime / size-tier) =====
# Domain: dollar-traded-VALUE (closeadj*volume) magnitude, fixed size-tier membership,
# regime/percentile, dollar-liquidity drawdown/recovery, concentration of traded VALUE,
# value-spike magnitude/persistence. NOT Amihud / |ret|/dv / turnover (f16); NOT plain
# volume z / surge (f14). Most features are BOUNDED / COUNT / REGIME forms so they do not
# collapse onto raw log-dollar-volume level (which is ~ -Amihud and ~ f14's dv-level/z/trend).

# Fixed absolute dollar-volume size tiers (USD/day) — the economic anchor unique to f17.
# Junior miners live in the $10k-$50M traded-value band; these fixed half-decade rungs
# (10k,30k,100k,300k,1M,3M,10M,30M,100M,300M,1B) measure whether the name is a tradeable
# size in ABSOLUTE terms, not self-relative percentiles. The named economic lines used by
# the tradeability features ($50k floor, $250k thin, $1M tradeable, $5M instit., $25M large)
# are applied directly inside those features.
_DV_TIERS = [1.0e4, 3.0e4, 1.0e5, 3.0e5, 1.0e6, 3.0e6,
             1.0e7, 3.0e7, 1.0e8, 3.0e8, 1.0e9]
_DV_LADDER = np.log10(np.array(_DV_TIERS, dtype="float64"))


def _f17_dv(closeadj, volume):
    # dollar-volume = closeadj * volume (traded VALUE). closeadj per >21d notional rule.
    return (closeadj * volume).clip(lower=0.0)


def _f17_dv_smooth(closeadj, volume, w):
    # smoothed dollar-volume LEVEL (stable traded-value scale)
    return _f17_dv(closeadj, volume).rolling(w, min_periods=max(2, w // 2)).mean()


def _f17_tier_ord(dv_sm):
    # PURE ordinal absolute size-tier index 0..len(ladder): how many fixed half-decade $ rungs
    # the traded-value level clears. Used where an integer rung count is wanted (crossings,
    # distinct-tiers, streaks-of-rung-membership). Coarse by construction.
    idx = pd.Series(0.0, index=dv_sm.index)
    for t in _DV_TIERS:
        idx = idx + (dv_sm >= t).astype(float)
    return idx.where(dv_sm.notna(), np.nan)


def _f17_tier_index(dv_sm):
    # CONTINUOUS absolute size-tier position on the fixed half-decade $ ladder: integer part =
    # ordinal rung count; fractional part = log-position within the current rung toward the next.
    # Anchored to absolute dollars (rungs are fixed $ amounts), not a self-relative percentile.
    # Only used inside DE-LEVELED forms (migration / excess vs typical / derate / span), so a raw
    # level (~ -Amihud, which is f16; ~ f14 dv-level) never appears as a standalone feature.
    ld = np.log10(dv_sm.replace(0, np.nan))
    lo = float(_DV_LADDER[0])
    step = float(_DV_LADDER[1] - _DV_LADDER[0])
    pos = (ld - lo) / step
    return pos.clip(lower=0.0, upper=float(len(_DV_LADDER) - 1)).where(dv_sm.notna(), np.nan)


def _f17_rung_q(dv, q, step_up):
    # Fixed-dollar reference rung for this name: snap a long-run (504d) quantile of its traded
    # value to the nearest fixed half-decade ladder rung, then step `step_up` fixed rungs up/down.
    # The result is ALWAYS one of the fixed $ rungs (a constant dollar amount), so threshold
    # features stay in absolute-dollar terms yet sit inside the name's own size range. Using a low
    # quantile (q<0.5) anchors "thin / floor" lines where the series actually visits.
    lvl = dv.rolling(504, min_periods=126).quantile(q)
    llvl = np.log10(lvl.replace(0, np.nan))
    step = float(_DV_LADDER[1] - _DV_LADDER[0])
    k = ((llvl - float(_DV_LADDER[0])) / step).round() + step_up
    k = k.clip(lower=0, upper=len(_DV_LADDER) - 1)
    rung_log = float(_DV_LADDER[0]) + k * step
    return np.power(10.0, rung_log)


def _f17_rung(dv, step_up):
    # median-anchored fixed rung (q=0.5) — see _f17_rung_q.
    return _f17_rung_q(dv, 0.5, step_up)


def _f17_frac_above(dv, t, w):
    # fraction of last w days the (daily) dollar-volume cleared fixed $ tier t (bounded 0..1)
    above = (dv >= t).astype(float).where(dv.notna(), np.nan)
    return above.rolling(w, min_periods=max(2, w // 2)).mean()


def _f17_frac_above_rung(dv, step_up, w):
    # fraction of last w days dv cleared a fixed $ rung `step_up` rungs above the name's anchor rung
    ref = _f17_rung(dv, step_up)
    above = (dv >= ref).astype(float).where(dv.notna() & ref.notna(), np.nan)
    return above.rolling(w, min_periods=max(2, w // 2)).mean()


def _f17_within_rung(dv_sm):
    # fractional position WITHIN the current fixed half-decade $ rung (0 at the rung floor, ->1
    # approaching the next rung). Sawtooth in log-dv -> deliberately NON-monotone in the level, so
    # it does not collapse onto raw log-dollar-volume (~ -Amihud=f16, ~ f14 dv-level). Absolute:
    # the rung edges are fixed dollar amounts.
    ld = np.log10(dv_sm.replace(0, np.nan))
    step = float(_DV_LADDER[1] - _DV_LADDER[0])
    frac = ((ld - float(_DV_LADDER[0])) / step) % 1.0
    return frac.where(dv_sm.notna(), np.nan)


def _f17_gini(dv, w):
    # Gini concentration of traded VALUE across the window (0 even, ->1 lumpy/news-driven)
    def _g(a):
        a = a[np.isfinite(a)]
        if a.size < 3:
            return np.nan
        s = np.sort(a)
        nn = s.size
        tot = s.sum()
        if tot <= 0:
            return np.nan
        cum = np.cumsum(s)
        return (nn + 1 - 2.0 * (cum.sum() / tot)) / nn
    return dv.rolling(w, min_periods=max(3, w // 2)).apply(_g, raw=True)


def _f17_topk_share(dv, w, k):
    # share of total window dollar-volume contributed by its k single biggest days
    tot = dv.rolling(w, min_periods=max(3, w // 2)).sum()
    topk = dv.rolling(w, min_periods=max(3, w // 2)).apply(
        lambda a: np.sort(a[np.isfinite(a)])[-k:].sum() if np.isfinite(a).sum() >= k else np.nan,
        raw=True)
    return topk / tot.replace(0, np.nan)


def _f17_streak_above(dv, t, w):
    # current consecutive-day run of dollar-volume above fixed $ tier t (capped by w)
    above = (dv >= t).astype(float).where(dv.notna(), np.nan)

    def _run(a):
        c = 0
        for x in a[::-1]:
            if x > 0.5:
                c += 1
            else:
                break
        return c
    return above.rolling(w, min_periods=max(2, w // 2)).apply(_run, raw=True)


# ============================================================
# ---- absolute size-tier membership / migration (unique f17 economic hook) ----

# how many fixed $ rungs the 21d traded value sits above its 252d-typical rung (tier excess)
def f17dv_f17_dollar_volume_dynamics_tierexcess_63d_base_v001_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    tier = _f17_tier_index(dv)
    typ = _f17_tier_index(_f17_dv_smooth(closeadj, volume, 252))
    b = tier - typ
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread between the daily-high tier and daily-low tier reached over 63d (intraday size band)
def f17dv_f17_dollar_volume_dynamics_tierhilospread_63d_base_v002_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    tier = _f17_tier_index(dv)
    hi = tier.rolling(63, min_periods=21).max()
    lo = tier.rolling(63, min_periods=21).min()
    b = hi - lo
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bounded distance of 21d traded-value level to the $1M tradeable rung (tanh log-ratio)
def f17dv_f17_dollar_volume_dynamics_tierdist1m_21d_base_v003_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    b = _f17_within_rung(dv)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# within-rung position of the 63d traded-value level (how far into its fixed $ rung), centred
def f17dv_f17_dollar_volume_dynamics_tierdist250k_63d_base_v004_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 63)
    b = _f17_within_rung(dv) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in within-rung position over a quarter (climbing toward / slipping from next rung)
def f17dv_f17_dollar_volume_dynamics_tierdist5m_126d_base_v005_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 126)
    wr = _f17_within_rung(dv)
    b = wr - wr.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last quarter the daily traded value cleared its anchor tradeable rung (+0 steps)
def f17dv_f17_dollar_volume_dynamics_fracabove1m_63d_base_v006_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    b = _f17_frac_above_rung(dv, 0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year the daily traded value cleared one fixed rung below anchor (thin line)
def f17dv_f17_dollar_volume_dynamics_fracabove250k_252d_base_v007_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    b = _f17_frac_above_rung(dv, -1, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year the daily traded value cleared one fixed rung above anchor (step-up size)
def f17dv_f17_dollar_volume_dynamics_fracabove5m_252d_base_v008_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    b = _f17_frac_above_rung(dv, 1, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last quarter daily traded value sat below the fixed dry-floor rung (q25-anchored)
def f17dv_f17_dollar_volume_dynamics_fracbelow50k_63d_base_v009_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    ref = _f17_rung_q(dv, 0.25, 0)
    below = (dv < ref).astype(float).where(dv.notna() & ref.notna(), np.nan)
    b = below.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current consecutive-day streak with traded value above the anchor tradeable rung
def f17dv_f17_dollar_volume_dynamics_streak1m_63d_base_v010_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    ref = _f17_rung(dv, 0)
    above = (dv >= ref).astype(float).where(dv.notna() & ref.notna(), np.nan)

    def _run(a):
        c = 0
        for x in a[::-1]:
            if x > 0.5:
                c += 1
            else:
                break
        return c
    b = above.rolling(63, min_periods=21).apply(_run, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current consecutive-day streak with traded value below the thin rung (q25-anchored)
def f17dv_f17_dollar_volume_dynamics_thinstreak250k_126d_base_v011_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    ref = _f17_rung_q(dv, 0.25, 0)
    below = (dv < ref).astype(float).where(dv.notna() & ref.notna(), np.nan)

    def _run(a):
        c = 0
        for x in a[::-1]:
            if x > 0.5:
                c += 1
            else:
                break
        return c
    streak = below.rolling(126, min_periods=42).apply(_run, raw=True)
    # blend with how depressed traded value is below the thin rung (avg log shortfall, 63d)
    short = np.log(dv.replace(0, np.nan) / ref.replace(0, np.nan)).clip(upper=0)
    depth = short.rolling(63, min_periods=21).mean()
    b = streak - 30.0 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of up-crossings of the anchor tradeable rung over the last year (size-tier churn)
def f17dv_f17_dollar_volume_dynamics_tiercross1m_252d_base_v012_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    ref = _f17_rung(dv, 0)
    above = (dv >= ref).astype(float)
    up = ((above == 1) & (above.shift(1) == 0)).astype(float).where(dv.notna() & ref.notna(), np.nan)
    b = up.rolling(252, min_periods=126).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tier headroom: how many fixed $ rungs below its own 252d peak rung the dv sits now,
# scaled by how long ago that peak rung occurred (de-rated-and-stale size class)
def f17dv_f17_dollar_volume_dynamics_tierstale_252d_base_v013_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    tier = _f17_tier_index(dv)
    peak = tier.rolling(252, min_periods=126).max()

    def _age(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    age = tier.rolling(252, min_periods=126).apply(_age, raw=True)
    b = (tier - peak) * (1.0 - age)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how far the current size tier sits below its own 252d peak tier (de-rated size class)
def f17dv_f17_dollar_volume_dynamics_tierderate_252d_base_v014_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    tier = _f17_tier_index(dv)
    b = tier - tier.rolling(252, min_periods=126).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth of size tiers visited over the last year (tier range = max-min, regime instability)
def f17dv_f17_dollar_volume_dynamics_tierspan_252d_base_v015_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    tier = _f17_tier_index(dv)
    b = tier.rolling(252, min_periods=126).max() - tier.rolling(252, min_periods=126).min()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- dollar-liquidity drawdown / recovery (de-leveled ratios off own peak/trough) ----

# dollar-liquidity rebuild durability off the 126d dry low: fraction of the last quarter the
# smoothed traded value held at least 50% (log) of the way up from its trailing 126d trough toward
# its 126d peak (a bounded occupancy/regime count, not the raw log distance above the trough)
def f17dv_f17_dollar_volume_dynamics_dvrebuildtime_126d_base_v016_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    ldv = np.log(dv.replace(0, np.nan))
    hi = _rmax(ldv, 126)
    lo = _rmin(ldv, 126)
    pos = (ldv - lo) / (hi - lo).replace(0, np.nan)
    up = (pos >= 0.5).astype(float).where(pos.notna(), np.nan)
    b = up.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year dollar-liquidity sat >50% below its trailing 252d peak (deep dry-up)
def f17dv_f17_dollar_volume_dynamics_dvunderwater_252d_base_v017_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    peak = _rmax(dv, 252)
    under = (dv / peak.replace(0, np.nan)) - 1.0
    deep = (under <= -0.5).astype(float).where(under.notna(), np.nan)
    b = deep.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# time since the 252d traded-value peak (staleness of best-liquidity, normalized 0..1)
def f17dv_f17_dollar_volume_dynamics_dvpeakage_252d_base_v018_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)

    def _age(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    b = dv.rolling(252, min_periods=126).apply(_age, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# time since the 252d traded-value trough (how long since the driest point, 0..1)
def f17dv_f17_dollar_volume_dynamics_dvtroughage_252d_base_v019_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)

    def _age(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    b = dv.rolling(252, min_periods=126).apply(_age, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-liquidity drawdown-episode rate blended with average underwater depth over the year
def f17dv_f17_dollar_volume_dynamics_dvddfreq_252d_base_v020_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    peak = _rmax(dv, 63)
    under = (dv / peak.replace(0, np.nan)) - 1.0
    in_dd = (under <= -0.25).astype(float)
    entries = ((in_dd == 1) & (in_dd.shift(1) == 0)).astype(float).where(under.notna(), np.nan)
    rate = entries.rolling(252, min_periods=126).sum()
    depth = under.clip(upper=0).rolling(252, min_periods=126).mean()
    b = rate + 5.0 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-liquidity recovery slope off its 252d trough scaled by time since that trough
def f17dv_f17_dollar_volume_dynamics_dvrecovrate_252d_base_v021_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    trough = _rmin(dv, 252)
    rec = np.log(dv.replace(0, np.nan) / trough.replace(0, np.nan))

    def _age(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    age = dv.rolling(252, min_periods=126).apply(_age, raw=True)
    b = rec / (age * 252.0 + 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-position of current dollar-liquidity within its 252d min-max band (bounded regime)
def f17dv_f17_dollar_volume_dynamics_dvrngpos_252d_base_v022_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    hi = _rmax(dv, 252)
    lo = _rmin(dv, 252)
    b = (dv - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in 504d range-position over a quarter (multi-year liquidity phase momentum, de-leveled)
def f17dv_f17_dollar_volume_dynamics_dvrngpos_504d_base_v023_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    hi = _rmax(dv, 504)
    lo = _rmin(dv, 504)
    pos = (dv - lo) / (hi - lo).replace(0, np.nan)
    b = pos - pos.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log span of the 252d dollar-liquidity range (peak-to-trough amplitude, scale-free)
def f17dv_f17_dollar_volume_dynamics_dvspan_252d_base_v024_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    hi = _rmax(dv, 252)
    lo = _rmin(dv, 252)
    b = np.log(hi.replace(0, np.nan) / lo.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- dollar-liquidity regime: percentile of LEVEL (bounded, de-monotonized) ----

# percentile rank of current dollar-liquidity vs its own 252d distribution (liquidity phase)
def f17dv_f17_dollar_volume_dynamics_dvpct_252d_base_v025_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    b = _rank(dv, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-year size-tier regime distance: the current continuous absolute $ size-tier minus its own
# 504d mean tier, expressed in 504d-tier-std units (how unusually large/small the name's tradeable
# size is right now vs its two-year norm — anchored to fixed $ rungs, not a raw self-percentile)
def f17dv_f17_dollar_volume_dynamics_tierregdist_504d_base_v026_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    tier = _f17_tier_index(dv)
    m = tier.rolling(504, min_periods=252).mean()
    sd = tier.rolling(504, min_periods=252).std().replace(0, np.nan)
    b = (tier - m) / sd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year dollar-liquidity stayed in the top third of its own 252d band
def f17dv_f17_dollar_volume_dynamics_dvhitime_252d_base_v027_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    hi = _rmax(dv, 252)
    lo = _rmin(dv, 252)
    pos = (dv - lo) / (hi - lo).replace(0, np.nan)
    upper = (pos >= 0.6667).astype(float).where(pos.notna(), np.nan)
    b = upper.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of distinct drought entries (drops into the bottom third of the 252d band) over a year
def f17dv_f17_dollar_volume_dynamics_dvlotime_252d_base_v028_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    hi = _rmax(dv, 252)
    lo = _rmin(dv, 252)
    pos = (dv - lo) / (hi - lo).replace(0, np.nan)
    inlo = (pos <= 0.3333).astype(float)
    entries = ((inlo == 1) & (inlo.shift(1) == 0)).astype(float).where(pos.notna(), np.nan)
    rate = entries.rolling(252, min_periods=126).sum()
    depth = (0.3333 - pos).clip(lower=0).rolling(63, min_periods=21).mean()
    b = rate + 20.0 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- dollar-VALUE concentration (Gini / top-k share / entropy — NOT Herfindahl/skew/cv) ----

# Gini concentration of daily traded VALUE over a quarter (news-lumpy vs even liquidity)
def f17dv_f17_dollar_volume_dynamics_dvgini_63d_base_v029_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    b = _f17_gini(dv, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Gini concentration of daily traded VALUE over a half-year (structural lumpiness)
def f17dv_f17_dollar_volume_dynamics_dvgini_126d_base_v030_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    b = _f17_gini(dv, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# temporal value clustering: share of the quarter's traded VALUE delivered in its single busiest
# rolling 5-day week vs the 5/63 even-split expectation (does the dollar flow arrive in one tight
# burst-week or spread evenly — a TIME-clustering measure, distinct from magnitude Gini/top-k share)
def f17dv_f17_dollar_volume_dynamics_dvweekburst_63d_base_v031_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    wk = dv.rolling(5, min_periods=5).sum()
    tot = dv.rolling(63, min_periods=40).sum()
    busiest = wk.rolling(63, min_periods=40).max()
    b = busiest / tot.replace(0, np.nan) - (5.0 / 63.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upper-vs-lower decile ratio of daily traded VALUE over a quarter, in log units: how many times
# bigger a top-decile day is than a bottom-decile day (spread-based lumpiness, distinct from share)
def f17dv_f17_dollar_volume_dynamics_dvdecileratio_63d_base_v032_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    q90 = dv.rolling(63, min_periods=21).quantile(0.90)
    q10 = dv.rolling(63, min_periods=21).quantile(0.10)
    b = np.log(q90.replace(0, np.nan) / q10.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share of half-year traded VALUE in its 10 biggest days (chunky-liquidity profile)
def f17dv_f17_dollar_volume_dynamics_dvtop10_126d_base_v033_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    b = _f17_topk_share(dv, 126, 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# thin-day starvation: share of total quarterly traded VALUE delivered on the lowest-decile
# (driest) days vs the even-split expectation (lower-tail mass; how little trades on quiet days)
def f17dv_f17_dollar_volume_dynamics_dveffdays_63d_base_v034_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)

    def _ltail(a):
        a = a[np.isfinite(a)]
        if a.size < 10 or a.sum() <= 0:
            return np.nan
        thr = np.quantile(a, 0.10)
        lower = a[a <= thr].sum() / a.sum()
        return 0.10 - lower
    b = dv.rolling(63, min_periods=30).apply(_ltail, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- dollar-VALUE spike magnitude & persistence (level-excess over median, NOT surge-ratio) ----

# count of dollar-VALUE spike days (above the trailing 126d 90th-pctile bar) over a quarter,
# blended with their average over-bar excess (event tally weighted by event size)
def f17dv_f17_dollar_volume_dynamics_dvspikecnt_63d_base_v035_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    bar = dv.rolling(126, min_periods=63).quantile(0.90)
    over = (dv > bar).astype(float).where(dv.notna() & bar.notna(), np.nan)
    cnt = over.rolling(63, min_periods=21).sum()
    exc = (dv / bar.replace(0, np.nan) - 1.0).clip(lower=0).rolling(63, min_periods=21).mean()
    b = cnt + 3.0 * exc
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# largest single-day dollar-VALUE spike vs its trailing 126d median (peak event magnitude)
def f17dv_f17_dollar_volume_dynamics_dvmaxspike_126d_base_v036_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    med = _median(dv, 126)
    ratio = dv / med.replace(0, np.nan)
    b = np.log(_rmax(ratio, 126).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday single-day rung-jump magnitude: average over a quarter of the absolute change in the
# continuous fixed-$ size-tier from one day to the next (how violently the name's tradeable size
# class hops between days — measured in absolute $ ladder rungs, not a self-relative surge ratio)
def f17dv_f17_dollar_volume_dynamics_dvrungjump_63d_base_v037_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    tier = _f17_tier_index(dv)
    jump = (tier - tier.shift(1)).abs().where(tier.notna() & tier.shift(1).notna(), np.nan)
    b = jump.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days since the last big dollar-VALUE spike (>5x 63d median), normalized over a quarter
def f17dv_f17_dollar_volume_dynamics_dvspikeage_63d_base_v038_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    med = _median(dv, 63)
    spike = (dv > 5.0 * med).astype(float).where(dv.notna() & med.notna(), np.nan)

    def _since(a):
        idx = np.where(a[::-1] > 0.5)[0]
        return (idx[0] / float(len(a))) if idx.size else 1.0
    b = spike.rolling(63, min_periods=21).apply(_since, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spike persistence: fraction of the last 42d the dollar-VALUE held above 1.5x its 63d median
def f17dv_f17_dollar_volume_dynamics_dvspikepersist_21d_base_v039_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    med = _median(dv, 63)
    hot = (dv > 1.5 * med).astype(float).where(dv.notna() & med.notna(), np.nan)
    b = hot.rolling(42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# excess of today's dollar value over its 21d median, squashed (bounded spike magnitude)
def f17dv_f17_dollar_volume_dynamics_dvexcess_21d_base_v040_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    med = _median(dv, 21)
    b = np.tanh(np.log(dv.replace(0, np.nan) / med.replace(0, np.nan)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- size-vs-price / value-per-price shape (size proxy, de-leveled) ----

# price-tier vs value-tier divergence: how much of the name's traded-value size tier is carried by
# its price level vs its share flow. log(closeadj) and log(dv/closeadj) each mapped onto the fixed
# half-decade ladder step, then differenced and smoothed (is its tradeable size a high-price/low-
# share name or a low-price/high-share name — a size-shape signal, not a volume rank/trend)
def f17dv_f17_dollar_volume_dynamics_pricesharetilt_252d_base_v041_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    step = float(_DV_LADDER[1] - _DV_LADDER[0])
    price_rung = np.log10(closeadj.replace(0, np.nan)) / step
    share_rung = np.log10((dv / closeadj.replace(0, np.nan)).replace(0, np.nan)) / step
    b = (price_rung - share_rung).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# is the dollar-liquidity regime rising or falling: sign-balance of dv vs its 63d median (63d)
def f17dv_f17_dollar_volume_dynamics_dvsignbal_63d_base_v042_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    med = _median(dv, 63)
    above = np.sign(dv - med)
    b = above.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity-regime occupancy: fraction of the last quarter the 21d traded-value mean sat ABOVE its
# 126d mean (how persistently short-run liquidity has run hot vs its structural base — a bounded
# regime count, distinct from the continuous short/long expansion ratio used elsewhere/in f16)
def f17dv_f17_dollar_volume_dynamics_hotregime_63d_base_v043_signal(closeadj, volume):
    short = _f17_dv_smooth(closeadj, volume, 21)
    long = _f17_dv_smooth(closeadj, volume, 126)
    hot = (short > long).astype(float).where(short.notna() & long.notna(), np.nan)
    b = hot.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ratio of 63d-mean to 252d-mean dollar value (quarterly vs annual liquidity base)
def f17dv_f17_dollar_volume_dynamics_dvqtryr_base_v044_signal(closeadj, volume):
    short = _f17_dv_smooth(closeadj, volume, 63)
    long = _f17_dv_smooth(closeadj, volume, 252)
    b = np.log(short.replace(0, np.nan) / long.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- intraday dollar-RANGE value (uses high/low; distinct from close*volume) ----

# intraday range-VALUE drawdown: the daily high-low dollar span (range*volume), smoothed, vs its own
# trailing 252d peak in log terms (how far the dollar value churned across the intraday range has
# faded from its best — a de-leveled liquidity-fade on the intraday-range dollar series)
def f17dv_f17_dollar_volume_dynamics_rangevaldd_252d_base_v045_signal(closeadj, volume, high, low):
    spanval = ((high - low).clip(lower=0.0) * volume).clip(lower=0.0)
    sm = spanval.rolling(21, min_periods=10).mean()
    peak = _rmax(sm, 252)
    b = np.log(sm.replace(0, np.nan) / peak.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday-high vs close tier gap: rungs the daily-high traded value clears beyond the close
# traded value, averaged over 63d (best-case-vs-realized tradeable size lift, de-leveled)
def f17dv_f17_dollar_volume_dynamics_hitiergap_63d_base_v046_signal(closeadj, high, volume):
    th = _f17_tier_index((high * volume).clip(lower=0.0))
    tc = _f17_tier_index((closeadj * volume).clip(lower=0.0))
    b = (th - tc).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday-low tier floor: ordinal fixed-$ tier of the intraday-low traded value, de-rated by
# its own 252d max tier (worst-case tradeable size vs best, over a quarter average)
def f17dv_f17_dollar_volume_dynamics_lofrac250k_63d_base_v047_signal(low, volume):
    dvl = (low * volume).clip(lower=0.0)
    tier = _f17_tier_index(dvl)
    derate = (tier - tier.rolling(252, min_periods=126).max())
    b = derate.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- additional tier / regime variety to reach 75 ----

# within-rung position of the 252d traded-value level, smoothed (long-horizon rung phase)
def f17dv_f17_dollar_volume_dynamics_tierdist25m_252d_base_v048_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 252)
    b = _f17_within_rung(dv).ewm(span=42, min_periods=21).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year the 21d traded value sat in the lower half of its current fixed rung
def f17dv_f17_dollar_volume_dynamics_tierdist50k_21d_base_v049_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    wr = _f17_within_rung(dv)
    lower = (wr < 0.5).astype(float).where(wr.notna(), np.nan)
    b = lower.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net tier migration over the last half-year (current tier minus tier 126d ago)
def f17dv_f17_dollar_volume_dynamics_tierpatheff_126d_base_v050_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    tier = _f17_tier_index(dv)
    net = (tier - tier.shift(126)).abs()
    step = (tier - tier.shift(1)).abs()
    gross = step.rolling(126, min_periods=63).sum()
    b = net / gross.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# annual size-class directedness: signed net continuous-tier change over the year divided by the
# total absolute distance the tier travelled (a directional-efficiency ratio in [-1,1]: was the size
# drift purposeful or churny). Path-shape, distinct from a raw tier drift / dollar-volume trend.
def f17dv_f17_dollar_volume_dynamics_tierdirected_252d_base_v051_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    tier = _f17_tier_index(dv)
    net = tier - tier.shift(252)
    gross = (tier - tier.shift(1)).abs().rolling(252, min_periods=126).sum()
    b = net / gross.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# size-class wandering: count of distinct fixed $ tiers occupied over the last year, blended
# with the continuous tier span (so it captures both rung-hops and within-rung travel)
def f17dv_f17_dollar_volume_dynamics_tiernunique_252d_base_v052_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    tier = _f17_tier_ord(dv)
    ndist = tier.rolling(252, min_periods=126).apply(
        lambda a: len(np.unique(a[np.isfinite(a)])) if np.isfinite(a).any() else np.nan, raw=True)
    ctier = _f17_tier_index(_f17_dv_smooth(closeadj, volume, 21))
    span = ctier.rolling(252, min_periods=126).max() - ctier.rolling(252, min_periods=126).min()
    b = ndist + span
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year spent at-or-above the modal (most-common) size tier
def f17dv_f17_dollar_volume_dynamics_tierabovemode_252d_base_v053_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    tier = _f17_tier_ord(dv)

    def _frac(a):
        a = a[np.isfinite(a)]
        if a.size < 60:
            return np.nan
        vals, cnts = np.unique(a, return_counts=True)
        mode = vals[np.argmax(cnts)]
        return (a >= mode).mean()
    b = tier.rolling(252, min_periods=126).apply(_frac, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stability of the size tier: fraction of last quarter the tier equalled today's tier
def f17dv_f17_dollar_volume_dynamics_tierstable_63d_base_v054_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    tier = _f17_tier_ord(dv)

    def _stab(a):
        a = a[np.isfinite(a)]
        if a.size < 21:
            return np.nan
        return (a == a[-1]).mean()
    b = tier.rolling(63, min_periods=21).apply(_stab, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- dollar-liquidity dispersion / stability (de-leveled scatter, not CV/skew) ----

# log-range of daily dollar value over a quarter normalized by its median (relative scatter)
def f17dv_f17_dollar_volume_dynamics_dvlogscatter_63d_base_v055_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    hi = _rmax(dv, 63)
    lo = _rmin(dv, 63)
    med = _median(dv, 63)
    b = (hi - lo) / med.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inter-quartile dispersion of daily dollar value over 126d, scaled by median (robust spread)
def f17dv_f17_dollar_volume_dynamics_dviqr_126d_base_v056_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    q75 = dv.rolling(126, min_periods=63).quantile(0.75)
    q25 = dv.rolling(126, min_periods=63).quantile(0.25)
    med = _median(dv, 126)
    b = (q75 - q25) / med.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log-value MAD: mean abs deviation of log dollar value over a quarter (multiplicative scatter)
def f17dv_f17_dollar_volume_dynamics_dvlogmad_63d_base_v057_signal(closeadj, volume):
    ldv = np.log(_f17_dv(closeadj, volume).replace(0, np.nan))
    m = _mean(ldv, 63)
    b = (ldv - m).abs().rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of days dollar value exceeds twice the window mean (right-skew incidence, 126d)
def f17dv_f17_dollar_volume_dynamics_dvfatright_126d_base_v058_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    m = _mean(dv, 126)
    fat = (dv > 2.0 * m).astype(float).where(dv.notna() & m.notna(), np.nan)
    b = fat.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- recovery / drought balance, multi-year ----

# dollar-liquidity drought-depth dispersion: std of the log-shortfall-below-252d-peak over a
# year (volatility of the underwater path, distinct from average depth or time-in-band)
def f17dv_f17_dollar_volume_dynamics_dvdroughtdepth_252d_base_v059_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    peak = _rmax(dv, 252)
    short = np.log(dv.replace(0, np.nan) / peak.replace(0, np.nan)).clip(upper=0)
    b = short.rolling(252, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-liquidity build vs drought balance over 252d (asymmetry of up vs down moves)
def f17dv_f17_dollar_volume_dynamics_dvbuildbal_252d_base_v060_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    chg = np.log(dv.replace(0, np.nan) / dv.shift(21).replace(0, np.nan))
    up = chg.clip(lower=0).rolling(252, min_periods=126).sum()
    dn = (-chg.clip(upper=0)).rolling(252, min_periods=126).sum()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# longest unbroken stretch (fraction of year) dollar-liquidity held above its 252d median level
def f17dv_f17_dollar_volume_dynamics_dvabovemed_252d_base_v061_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    med = _median(dv, 252)
    above = (dv > med).astype(float).where(dv.notna() & med.notna(), np.nan)

    def _maxrun(a):
        best = 0
        cur = 0
        for x in a:
            if x > 0.5:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return best / float(len(a))
    b = above.rolling(252, min_periods=126).apply(_maxrun, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- spike clustering / news-cadence ----

# clustering of dollar-VALUE spikes: spike rate last 21d vs last 126d (burstiness)
def f17dv_f17_dollar_volume_dynamics_dvburst_base_v062_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    med = _median(dv, 126)
    spike = (dv > 3.0 * med).astype(float).where(dv.notna() & med.notna(), np.nan)
    near = spike.rolling(21, min_periods=10).mean()
    far = spike.rolling(126, min_periods=63).mean()
    b = near - far
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# longest spike-free stretch within the last quarter (calm-liquidity span, normalized)
def f17dv_f17_dollar_volume_dynamics_dvcalmspan_63d_base_v063_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    med = _median(dv, 63)
    spike = (dv > 3.0 * med).astype(float).where(dv.notna() & med.notna(), np.nan)

    def _gap(a):
        best = 0
        cur = 0
        for x in a:
            if x > 0.5:
                cur = 0
            else:
                cur += 1
                if cur > best:
                    best = cur
        return best / float(len(a))
    b = spike.rolling(63, min_periods=21).apply(_gap, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- absolute-size composites ----

# blended tradeability: avg fraction-above across rungs -1/0/+1 around the anchor (63d)
def f17dv_f17_dollar_volume_dynamics_tradeblend_63d_base_v064_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    f1 = _f17_frac_above_rung(dv, -1, 63)
    f2 = _f17_frac_above_rung(dv, 0, 63)
    f3 = _f17_frac_above_rung(dv, 1, 63)
    b = (f1 + f2 + f3) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tradeability momentum: net change in the blended rung-tradeability score over a quarter
def f17dv_f17_dollar_volume_dynamics_tradechg_63d_base_v065_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    f1 = _f17_frac_above_rung(dv, -1, 63)
    f2 = _f17_frac_above_rung(dv, 0, 63)
    f3 = _f17_frac_above_rung(dv, 1, 63)
    blend = (f1 + f2 + f3) / 3.0
    b = blend - blend.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tier-occupancy entropy: how evenly the last year's days spread across the fixed $ tiers
# (low = pinned to one size class; high = wandering across many tiers)
def f17dv_f17_dollar_volume_dynamics_bandtime_252d_base_v066_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    tier = _f17_tier_ord(dv)

    def _ent(a):
        a = a[np.isfinite(a)]
        if a.size < 60:
            return np.nan
        _, cnts = np.unique(a, return_counts=True)
        p = cnts / cnts.sum()
        return -(p * np.log(p)).sum()
    b = tier.rolling(252, min_periods=126).apply(_ent, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- dollar-liquidity acceleration of regime (de-leveled second differences) ----

# change in dollar-liquidity percentile over a quarter (regime shift, bounded inputs)
def f17dv_f17_dollar_volume_dynamics_dvpctchg_252d_base_v067_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    pct = _rank(dv, 252)
    b = pct - pct.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in fraction-above-anchor-rung over a quarter (tradeability improving/eroding)
def f17dv_f17_dollar_volume_dynamics_fracchg1m_63d_base_v068_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    fa = _f17_frac_above_rung(dv, 0, 63)
    b = fa - fa.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in Gini concentration of traded value over a half-year (lumpiness drift)
def f17dv_f17_dollar_volume_dynamics_ginichg_126d_base_v069_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    g = _f17_gini(dv, 126)
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- more bounded regime to round out 75 ----

# range-position of dollar-liquidity within its 126d band (medium-horizon phase)
def f17dv_f17_dollar_volume_dynamics_dvrngpos_126d_base_v070_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    hi = _rmax(dv, 126)
    lo = _rmin(dv, 126)
    b = (dv - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tier-occupancy Herfindahl over a half-year: sum of squared shares of days spent at each fixed $
# size rung (1/#rungs even .. 1 pinned to one rung) — a size-CLASS concentration anchored to the
# absolute ladder, structurally distinct from value-share concentration or volume dispersion/CV
def f17dv_f17_dollar_volume_dynamics_tierherf_126d_base_v071_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    tier = _f17_tier_ord(dv)

    def _herf(a):
        a = a[np.isfinite(a)]
        if a.size < 40:
            return np.nan
        _, cnts = np.unique(a, return_counts=True)
        p = cnts / cnts.sum()
        return float((p * p).sum())
    b = tier.rolling(126, min_periods=63).apply(_herf, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last quarter daily traded value cleared two rungs above anchor (step-up size)
def f17dv_f17_dollar_volume_dynamics_fracabove5m_63d_base_v072_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    b = _f17_frac_above_rung(dv, 2, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-liquidity recovery off 252d trough (log multiple, multi-year rebuild magnitude)
def f17dv_f17_dollar_volume_dynamics_dvrecov_252d_base_v073_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    trough = _rmin(dv, 252)
    b = np.log(dv.replace(0, np.nan) / trough.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of half-year days whose traded value reached the top quintile of its own 126d range
# (big-event tally via a robust within-window bar, varies on smooth and lumpy series alike)
def f17dv_f17_dollar_volume_dynamics_dvbigspike_126d_base_v074_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    q80 = dv.rolling(126, min_periods=63).quantile(0.80)
    big = (dv > q80).astype(float).where(dv.notna() & q80.notna(), np.nan)
    b = big.rolling(126, min_periods=63).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last half-year the intraday-typical traded value cleared the anchor rung
def f17dv_f17_dollar_volume_dynamics_typfrac1m_126d_base_v075_signal(closeadj, volume, high, low):
    typ = ((high + low + closeadj) / 3.0 * volume).clip(lower=0.0)
    b = _f17_frac_above_rung(typ, 0, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f17dv_f17_dollar_volume_dynamics_tierexcess_63d_base_v001_signal,
    f17dv_f17_dollar_volume_dynamics_tierhilospread_63d_base_v002_signal,
    f17dv_f17_dollar_volume_dynamics_tierdist1m_21d_base_v003_signal,
    f17dv_f17_dollar_volume_dynamics_tierdist250k_63d_base_v004_signal,
    f17dv_f17_dollar_volume_dynamics_tierdist5m_126d_base_v005_signal,
    f17dv_f17_dollar_volume_dynamics_fracabove1m_63d_base_v006_signal,
    f17dv_f17_dollar_volume_dynamics_fracabove250k_252d_base_v007_signal,
    f17dv_f17_dollar_volume_dynamics_fracabove5m_252d_base_v008_signal,
    f17dv_f17_dollar_volume_dynamics_fracbelow50k_63d_base_v009_signal,
    f17dv_f17_dollar_volume_dynamics_streak1m_63d_base_v010_signal,
    f17dv_f17_dollar_volume_dynamics_thinstreak250k_126d_base_v011_signal,
    f17dv_f17_dollar_volume_dynamics_tiercross1m_252d_base_v012_signal,
    f17dv_f17_dollar_volume_dynamics_tierstale_252d_base_v013_signal,
    f17dv_f17_dollar_volume_dynamics_tierderate_252d_base_v014_signal,
    f17dv_f17_dollar_volume_dynamics_tierspan_252d_base_v015_signal,
    f17dv_f17_dollar_volume_dynamics_dvrebuildtime_126d_base_v016_signal,
    f17dv_f17_dollar_volume_dynamics_dvunderwater_252d_base_v017_signal,
    f17dv_f17_dollar_volume_dynamics_dvpeakage_252d_base_v018_signal,
    f17dv_f17_dollar_volume_dynamics_dvtroughage_252d_base_v019_signal,
    f17dv_f17_dollar_volume_dynamics_dvddfreq_252d_base_v020_signal,
    f17dv_f17_dollar_volume_dynamics_dvrecovrate_252d_base_v021_signal,
    f17dv_f17_dollar_volume_dynamics_dvrngpos_252d_base_v022_signal,
    f17dv_f17_dollar_volume_dynamics_dvrngpos_504d_base_v023_signal,
    f17dv_f17_dollar_volume_dynamics_dvspan_252d_base_v024_signal,
    f17dv_f17_dollar_volume_dynamics_dvpct_252d_base_v025_signal,
    f17dv_f17_dollar_volume_dynamics_tierregdist_504d_base_v026_signal,
    f17dv_f17_dollar_volume_dynamics_dvhitime_252d_base_v027_signal,
    f17dv_f17_dollar_volume_dynamics_dvlotime_252d_base_v028_signal,
    f17dv_f17_dollar_volume_dynamics_dvgini_63d_base_v029_signal,
    f17dv_f17_dollar_volume_dynamics_dvgini_126d_base_v030_signal,
    f17dv_f17_dollar_volume_dynamics_dvweekburst_63d_base_v031_signal,
    f17dv_f17_dollar_volume_dynamics_dvdecileratio_63d_base_v032_signal,
    f17dv_f17_dollar_volume_dynamics_dvtop10_126d_base_v033_signal,
    f17dv_f17_dollar_volume_dynamics_dveffdays_63d_base_v034_signal,
    f17dv_f17_dollar_volume_dynamics_dvspikecnt_63d_base_v035_signal,
    f17dv_f17_dollar_volume_dynamics_dvmaxspike_126d_base_v036_signal,
    f17dv_f17_dollar_volume_dynamics_dvrungjump_63d_base_v037_signal,
    f17dv_f17_dollar_volume_dynamics_dvspikeage_63d_base_v038_signal,
    f17dv_f17_dollar_volume_dynamics_dvspikepersist_21d_base_v039_signal,
    f17dv_f17_dollar_volume_dynamics_dvexcess_21d_base_v040_signal,
    f17dv_f17_dollar_volume_dynamics_pricesharetilt_252d_base_v041_signal,
    f17dv_f17_dollar_volume_dynamics_dvsignbal_63d_base_v042_signal,
    f17dv_f17_dollar_volume_dynamics_hotregime_63d_base_v043_signal,
    f17dv_f17_dollar_volume_dynamics_dvqtryr_base_v044_signal,
    f17dv_f17_dollar_volume_dynamics_rangevaldd_252d_base_v045_signal,
    f17dv_f17_dollar_volume_dynamics_hitiergap_63d_base_v046_signal,
    f17dv_f17_dollar_volume_dynamics_lofrac250k_63d_base_v047_signal,
    f17dv_f17_dollar_volume_dynamics_tierdist25m_252d_base_v048_signal,
    f17dv_f17_dollar_volume_dynamics_tierdist50k_21d_base_v049_signal,
    f17dv_f17_dollar_volume_dynamics_tierpatheff_126d_base_v050_signal,
    f17dv_f17_dollar_volume_dynamics_tierdirected_252d_base_v051_signal,
    f17dv_f17_dollar_volume_dynamics_tiernunique_252d_base_v052_signal,
    f17dv_f17_dollar_volume_dynamics_tierabovemode_252d_base_v053_signal,
    f17dv_f17_dollar_volume_dynamics_tierstable_63d_base_v054_signal,
    f17dv_f17_dollar_volume_dynamics_dvlogscatter_63d_base_v055_signal,
    f17dv_f17_dollar_volume_dynamics_dviqr_126d_base_v056_signal,
    f17dv_f17_dollar_volume_dynamics_dvlogmad_63d_base_v057_signal,
    f17dv_f17_dollar_volume_dynamics_dvfatright_126d_base_v058_signal,
    f17dv_f17_dollar_volume_dynamics_dvdroughtdepth_252d_base_v059_signal,
    f17dv_f17_dollar_volume_dynamics_dvbuildbal_252d_base_v060_signal,
    f17dv_f17_dollar_volume_dynamics_dvabovemed_252d_base_v061_signal,
    f17dv_f17_dollar_volume_dynamics_dvburst_base_v062_signal,
    f17dv_f17_dollar_volume_dynamics_dvcalmspan_63d_base_v063_signal,
    f17dv_f17_dollar_volume_dynamics_tradeblend_63d_base_v064_signal,
    f17dv_f17_dollar_volume_dynamics_tradechg_63d_base_v065_signal,
    f17dv_f17_dollar_volume_dynamics_bandtime_252d_base_v066_signal,
    f17dv_f17_dollar_volume_dynamics_dvpctchg_252d_base_v067_signal,
    f17dv_f17_dollar_volume_dynamics_fracchg1m_63d_base_v068_signal,
    f17dv_f17_dollar_volume_dynamics_ginichg_126d_base_v069_signal,
    f17dv_f17_dollar_volume_dynamics_dvrngpos_126d_base_v070_signal,
    f17dv_f17_dollar_volume_dynamics_tierherf_126d_base_v071_signal,
    f17dv_f17_dollar_volume_dynamics_fracabove5m_63d_base_v072_signal,
    f17dv_f17_dollar_volume_dynamics_dvrecov_252d_base_v073_signal,
    f17dv_f17_dollar_volume_dynamics_dvbigspike_126d_base_v074_signal,
    f17dv_f17_dollar_volume_dynamics_typfrac1m_126d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F17_DOLLAR_VOLUME_DYNAMICS_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0003, 0.035, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.01, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.02, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.02, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(8e5, 5e5, n)) + 1e4, name="volume")

    cols = {"closeadj": closeadj, "close": close, "open": openp,
            "high": high, "low": low, "volume": volume}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 20, "%s nunique=%d" % (name, q.nunique())
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        results[name] = y1.iloc[504:]
        n_features += 1

    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), "nan_ok=%d/%d" % (nan_ok, n_features)

    items = list(results.items())
    for i in range(len(items)):
        ni, si = items[i]
        ai = si.dropna()
        for j in range(i + 1, len(items)):
            nj, sj = items[j]
            aj = sj.dropna()
            idx = ai.index.intersection(aj.index)
            if len(idx) < 30:
                continue
            c = ai.loc[idx].corr(aj.loc[idx])
            if c is None or np.isnan(c):
                continue
            assert abs(c) <= 0.97, "CORR %s vs %s = %.4f" % (ni, nj, c)

    print("OK f17_dollar_volume_dynamics_base_001_075_claude: %d features pass" % n_features)
