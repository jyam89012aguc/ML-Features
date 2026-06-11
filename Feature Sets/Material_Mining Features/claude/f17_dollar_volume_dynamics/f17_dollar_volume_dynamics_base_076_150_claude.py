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
# Same domain + same de-overlap discipline as base_001_075: NOT Amihud/|ret|/dv/turnover (f16),
# NOT plain volume z / surge (f14). Bounded / count / regime / de-leveled forms dominate.
_DV_TIERS = [1.0e4, 3.0e4, 1.0e5, 3.0e5, 1.0e6, 3.0e6,
             1.0e7, 3.0e7, 1.0e8, 3.0e8, 1.0e9]
_DV_LADDER = np.log10(np.array(_DV_TIERS, dtype="float64"))


def _f17_dv(closeadj, volume):
    return (closeadj * volume).clip(lower=0.0)


def _f17_dv_smooth(closeadj, volume, w):
    return _f17_dv(closeadj, volume).rolling(w, min_periods=max(2, w // 2)).mean()


def _f17_tier_ord(dv_sm):
    # pure ordinal fixed-$ rung count
    idx = pd.Series(0.0, index=dv_sm.index)
    for t in _DV_TIERS:
        idx = idx + (dv_sm >= t).astype(float)
    return idx.where(dv_sm.notna(), np.nan)


def _f17_tier_index(dv_sm):
    # continuous absolute size-tier position on the fixed half-decade $ ladder (de-leveled use only)
    ld = np.log10(dv_sm.replace(0, np.nan))
    lo = float(_DV_LADDER[0])
    step = float(_DV_LADDER[1] - _DV_LADDER[0])
    pos = (ld - lo) / step
    return pos.clip(lower=0.0, upper=float(len(_DV_LADDER) - 1)).where(dv_sm.notna(), np.nan)


def _f17_within_rung(dv_sm):
    # fractional position WITHIN the current fixed $ rung (sawtooth -> non-monotone in level)
    ld = np.log10(dv_sm.replace(0, np.nan))
    step = float(_DV_LADDER[1] - _DV_LADDER[0])
    frac = ((ld - float(_DV_LADDER[0])) / step) % 1.0
    return frac.where(dv_sm.notna(), np.nan)


def _f17_rung_q(dv, q, step_up):
    # fixed-$ reference rung snapped from a long-run quantile of traded value (see base_001_075)
    lvl = dv.rolling(504, min_periods=126).quantile(q)
    llvl = np.log10(lvl.replace(0, np.nan))
    step = float(_DV_LADDER[1] - _DV_LADDER[0])
    k = ((llvl - float(_DV_LADDER[0])) / step).round() + step_up
    k = k.clip(lower=0, upper=len(_DV_LADDER) - 1)
    rung_log = float(_DV_LADDER[0]) + k * step
    return np.power(10.0, rung_log)


def _f17_rung(dv, step_up):
    return _f17_rung_q(dv, 0.5, step_up)


def _f17_frac_above_rung(dv, step_up, w):
    ref = _f17_rung(dv, step_up)
    above = (dv >= ref).astype(float).where(dv.notna() & ref.notna(), np.nan)
    return above.rolling(w, min_periods=max(2, w // 2)).mean()


def _f17_gini(dv, w):
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
    tot = dv.rolling(w, min_periods=max(3, w // 2)).sum()
    topk = dv.rolling(w, min_periods=max(3, w // 2)).apply(
        lambda a: np.sort(a[np.isfinite(a)])[-k:].sum() if np.isfinite(a).sum() >= k else np.nan,
        raw=True)
    return topk / tot.replace(0, np.nan)


# ============================================================
# ---- tier migration velocity / acceleration (de-leveled) ----

# size-tier choppiness over a quarter: std of daily continuous-tier first differences (how noisily
# the name's tradeable size class jitters day to day, regardless of net direction) — a dispersion of
# rung motion, distinct from a net tier drift / dollar-volume trend
def f17dv_f17_dollar_volume_dynamics_tierchop_63d_base_v076_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 5)
    tier = _f17_tier_index(dv)
    d = tier - tier.shift(1)
    b = d.rolling(63, min_periods=21).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration of the size tier: quarterly migration now minus migration a quarter ago
def f17dv_f17_dollar_volume_dynamics_tieraccel_63d_base_v077_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    tier = _f17_tier_index(dv)
    mig = tier - tier.shift(63)
    b = mig - mig.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tier disagreement across smoothing horizons: 21d tier minus 126d tier (short vs structural size)
def f17dv_f17_dollar_volume_dynamics_tierdisagree_base_v078_signal(closeadj, volume):
    t21 = _f17_tier_index(_f17_dv_smooth(closeadj, volume, 21))
    t126 = _f17_tier_index(_f17_dv_smooth(closeadj, volume, 126))
    b = t21 - t126
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tier dispersion across 21/63/252 smoothing horizons (multi-horizon size-class scatter)
def f17dv_f17_dollar_volume_dynamics_tierdisp_base_v079_signal(closeadj, volume):
    t1 = _f17_tier_index(_f17_dv_smooth(closeadj, volume, 21))
    t2 = _f17_tier_index(_f17_dv_smooth(closeadj, volume, 63))
    t3 = _f17_tier_index(_f17_dv_smooth(closeadj, volume, 252))
    b = pd.concat([t1, t2, t3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- within-rung dynamics ----

# within-rung position minus its own slow EMA (rung-internal displacement)
def f17dv_f17_dollar_volume_dynamics_wrdisp_63d_base_v080_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    wr = _f17_within_rung(dv)
    b = wr - wr.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last quarter the 21d dv sat in the upper half of its current fixed rung
def f17dv_f17_dollar_volume_dynamics_wruptime_63d_base_v081_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    wr = _f17_within_rung(dv)
    up = (wr >= 0.5).astype(float).where(wr.notna(), np.nan)
    b = up.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- absolute-rung tradeability at other rungs / windows ----

# fraction of last half-year daily dv cleared the anchor rung (medium-window tradeability)
def f17dv_f17_dollar_volume_dynamics_fracanchor_126d_base_v082_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    b = _f17_frac_above_rung(dv, 0, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year daily dv cleared two rungs above anchor (durable step-up size)
def f17dv_f17_dollar_volume_dynamics_fracup2_252d_base_v083_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    b = _f17_frac_above_rung(dv, 2, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# longest spell (fraction of year) dv held continuously above its anchor rung (sticky tradeability)
def f17dv_f17_dollar_volume_dynamics_anchorspell_252d_base_v084_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    ref = _f17_rung(dv, 0)
    above = (dv >= ref).astype(float).where(dv.notna() & ref.notna(), np.nan)

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


# count of down-crossings of the anchor rung over the year (tradeability loss events)
def f17dv_f17_dollar_volume_dynamics_downcross_252d_base_v085_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    ref = _f17_rung(dv, 0)
    above = (dv >= ref).astype(float)
    down = ((above == 0) & (above.shift(1) == 1)).astype(float).where(dv.notna() & ref.notna(), np.nan)
    b = down.rolling(252, min_periods=126).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- dollar-liquidity drawdown / recovery on alternate windows ----

# multi-year dollar-liquidity rebuild progress: fraction of the 504d log-span the current level
# has climbed back from its trough (bounded 0..1 position-in-span; not a raw log distance, so it
# does not track the 504d span amplitude itself)
def f17dv_f17_dollar_volume_dynamics_dvrebuild_504d_base_v086_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    ldv = np.log(dv.replace(0, np.nan))
    hi = _rmax(ldv, 504)
    lo = _rmin(ldv, 504)
    pos = (ldv - lo) / (hi - lo).replace(0, np.nan)
    # blend with how long it has held above the span midpoint (rebuild durability)
    held = (pos >= 0.5).astype(float).where(pos.notna(), np.nan).rolling(63, min_periods=21).mean()
    b = pos - 0.5 * held
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-liquidity drawdown off 126d peak (medium-horizon liquidity fade, log)
def f17dv_f17_dollar_volume_dynamics_dvdd_126d_base_v087_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    peak = _rmax(dv, 126)
    b = np.log(dv.replace(0, np.nan) / peak.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# time since the 504d traded-value peak (staleness of best multi-year liquidity, 0..1)
def f17dv_f17_dollar_volume_dynamics_dvpeakage_504d_base_v088_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)

    def _age(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    b = dv.rolling(504, min_periods=252).apply(_age, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-position of dv within its 126d band, change over a month (medium-phase momentum)
def f17dv_f17_dollar_volume_dynamics_dvrngposchg_126d_base_v089_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    hi = _rmax(dv, 126)
    lo = _rmin(dv, 126)
    pos = (dv - lo) / (hi - lo).replace(0, np.nan)
    b = pos - pos.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log span of the 504d dollar-liquidity range (multi-year peak-to-trough amplitude)
def f17dv_f17_dollar_volume_dynamics_dvspan_504d_base_v090_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    hi = _rmax(dv, 504)
    lo = _rmin(dv, 504)
    b = np.log(hi.replace(0, np.nan) / lo.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-liquidity recovery slope: 21d-change in log distance above the trailing 252d trough
# (how fast liquidity is rebuilding off its dry low, de-leveled and momentum-flavoured)
def f17dv_f17_dollar_volume_dynamics_offtrough_252d_base_v091_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    trough = _rmin(dv, 252)
    above = np.log(dv.replace(0, np.nan) / trough.replace(0, np.nan))
    b = above - above.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- regime: percentile / position on alternate windows ----

# percentile rank of dv vs its own 126d distribution (medium-horizon liquidity phase)
def f17dv_f17_dollar_volume_dynamics_dvpct_126d_base_v092_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    b = _rank(dv, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in 252d dv percentile over a half-year (slow regime drift, de-leveled)
def f17dv_f17_dollar_volume_dynamics_dvpctchg_126d_base_v093_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    pct = _rank(dv, 252)
    b = pct - pct.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion of the 252d dv percentile over the last quarter (regime instability)
def f17dv_f17_dollar_volume_dynamics_dvpctvol_63d_base_v094_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    pct = _rank(dv, 252)
    b = pct.rolling(63, min_periods=21).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year dv ranked in the top quintile of its own 252d history (high-liquidity time)
def f17dv_f17_dollar_volume_dynamics_topquint_252d_base_v095_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    pct = dv.rolling(252, min_periods=126).rank(pct=True)
    top = (pct >= 0.8).astype(float).where(pct.notna(), np.nan)
    b = top.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- concentration: alternate estimators / windows ----

# Gini concentration of daily traded VALUE over a year (annual lumpiness)
def f17dv_f17_dollar_volume_dynamics_dvgini_252d_base_v096_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    b = _f17_gini(dv, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# busy-day value mass: share of total quarterly traded VALUE delivered on days whose value exceeded
# 2x the window median (how much of the quarter's liquidity arrives on the busy days, by VALUE mass
# above a robust threshold — distinct from top-k-rank share or volume CV/dispersion)
def f17dv_f17_dollar_volume_dynamics_dvbusymass_63d_base_v097_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)

    def _mass(a):
        a = a[np.isfinite(a)]
        if a.size < 21 or a.sum() <= 0:
            return np.nan
        thr = 2.0 * np.median(a)
        return a[a > thr].sum() / a.sum()
    b = dv.rolling(63, min_periods=21).apply(_mass, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# top-20-day dollar-value share over a year (chunkiness of the annual liquidity profile)
def f17dv_f17_dollar_volume_dynamics_dvtop20_252d_base_v098_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    b = _f17_topk_share(dv, 252, 20)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ratio of the busiest single day to the median day in dollar value over a quarter (peak/typical)
def f17dv_f17_dollar_volume_dynamics_dvpeakmed_63d_base_v099_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    mx = _rmax(dv, 63)
    md = _median(dv, 63)
    b = np.log(mx.replace(0, np.nan) / md.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# concentration drift: quarterly Gini minus its own 252d average (lumpiness anomaly)
def f17dv_f17_dollar_volume_dynamics_dvginianom_63d_base_v100_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    g = _f17_gini(dv, 63)
    b = g - g.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- spike magnitude / cadence (level-excess over robust within-window bars) ----

# count of half-year days above the 95th-pctile dollar-value bar (rare-event tally)
def f17dv_f17_dollar_volume_dynamics_dvp95cnt_126d_base_v101_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    bar = dv.rolling(126, min_periods=63).quantile(0.95)
    over = (dv > bar).astype(float).where(dv.notna() & bar.notna(), np.nan)
    b = over.rolling(126, min_periods=63).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# largest single-day dollar value vs its 63d mean, log (short-horizon peak event magnitude)
def f17dv_f17_dollar_volume_dynamics_dvmaxmean_63d_base_v102_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    mn = _mean(dv, 63)
    b = np.log(_rmax(dv, 63).replace(0, np.nan) / mn.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spike-onset: today's dv vs the max of the prior 20 days (fresh single-day value breakout)
def f17dv_f17_dollar_volume_dynamics_dvonset_21d_base_v103_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    prior = dv.shift(1).rolling(20, min_periods=10).max()
    b = np.tanh(np.log(dv.replace(0, np.nan) / prior.replace(0, np.nan)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# burstiness of value spikes: spike rate last 21d minus last 252d (news-cadence change)
def f17dv_f17_dollar_volume_dynamics_dvburst_252d_base_v104_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    bar = dv.rolling(252, min_periods=126).quantile(0.90)
    spike = (dv > bar).astype(float).where(dv.notna() & bar.notna(), np.nan)
    near = spike.rolling(21, min_periods=10).mean()
    far = spike.rolling(252, min_periods=126).mean()
    b = near - far
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last quarter within 5d of a top-decile value day (post-event echo)
def f17dv_f17_dollar_volume_dynamics_dvecho_63d_base_v105_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    bar = dv.rolling(126, min_periods=63).quantile(0.90)
    spike = (dv > bar).astype(float).where(dv.notna() & bar.notna(), 0.0)
    recent = spike.rolling(5, min_periods=1).max()
    b = recent.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- dispersion / stability of traded value (de-leveled) ----

# coefficient of quartile variation of dv over a quarter ((q75-q25)/(q75+q25), scale-free)
def f17dv_f17_dollar_volume_dynamics_dvcqv_63d_base_v106_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    q75 = dv.rolling(63, min_periods=21).quantile(0.75)
    q25 = dv.rolling(63, min_periods=21).quantile(0.25)
    b = (q75 - q25) / (q75 + q25).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stability of log-dv: negative std of log dv over a quarter (smooth-liquidity proxy)
def f17dv_f17_dollar_volume_dynamics_dvstability_63d_base_v107_signal(closeadj, volume):
    ldv = np.log(_f17_dv(closeadj, volume).replace(0, np.nan))
    b = -ldv.rolling(63, min_periods=21).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log-dv range over a month normalized by its 126d typical range (relative monthly scatter)
def f17dv_f17_dollar_volume_dynamics_dvrelrange_21d_base_v108_signal(closeadj, volume):
    ldv = np.log(_f17_dv(closeadj, volume).replace(0, np.nan))
    rng = _rmax(ldv, 21) - _rmin(ldv, 21)
    typ = (_rmax(ldv, 126) - _rmin(ldv, 126)).replace(0, np.nan)
    b = rng / typ
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# autocorrelation(1) of log-dv over a quarter (liquidity persistence vs choppiness)
def f17dv_f17_dollar_volume_dynamics_dvautocorr_63d_base_v109_signal(closeadj, volume):
    ldv = np.log(_f17_dv(closeadj, volume).replace(0, np.nan))

    def _ac(a):
        a = a[np.isfinite(a)]
        if a.size < 20:
            return np.nan
        x = a[:-1]
        y = a[1:]
        if x.std() == 0 or y.std() == 0:
            return np.nan
        return np.corrcoef(x, y)[0, 1]
    b = ldv.rolling(63, min_periods=30).apply(_ac, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- drought / build balance, alternate windows ----

# dollar-liquidity build vs drought balance over 126d (medium-horizon asymmetry)
def f17dv_f17_dollar_volume_dynamics_dvbuildbal_126d_base_v110_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    chg = np.log(dv.replace(0, np.nan) / dv.shift(10).replace(0, np.nan))
    up = chg.clip(lower=0).rolling(126, min_periods=63).sum()
    dn = (-chg.clip(upper=0)).rolling(126, min_periods=63).sum()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# step-direction balance of dv over a year: net fraction of days the 21d-smoothed traded value
# rose vs fell day-over-day (a path/direction regime, independent of level-vs-threshold occupancy)
def f17dv_f17_dollar_volume_dynamics_dvstepbal_252d_base_v111_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    step = np.sign(dv - dv.shift(1)).where(dv.notna() & dv.shift(1).notna(), np.nan)
    b = step.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# longest dry spell (fraction of year) dv stayed below its 252d median (sustained drought)
def f17dv_f17_dollar_volume_dynamics_dvdryspell_252d_base_v112_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    med = _median(dv, 252)
    below = (dv < med).astype(float).where(dv.notna() & med.notna(), np.nan)

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
    b = below.rolling(252, min_periods=126).apply(_maxrun, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- short vs long liquidity-base ratios (de-leveled) ----

# 5d-mean vs 63d-mean dollar value (very-short vs quarter liquidity base)
def f17dv_f17_dollar_volume_dynamics_dv5v63_base_v113_signal(closeadj, volume):
    short = _f17_dv_smooth(closeadj, volume, 5)
    long = _f17_dv_smooth(closeadj, volume, 63)
    b = np.log(short.replace(0, np.nan) / long.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 126d-mean vs 504d-mean dollar value (half-year vs two-year structural liquidity)
def f17dv_f17_dollar_volume_dynamics_dv126v504_base_v114_signal(closeadj, volume):
    short = _f17_dv_smooth(closeadj, volume, 126)
    long = _f17_dv_smooth(closeadj, volume, 504)
    b = np.log(short.replace(0, np.nan) / long.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# curvature of the liquidity-base term structure: 21v63 ratio minus 63v252 ratio
def f17dv_f17_dollar_volume_dynamics_dvtermcurv_base_v115_signal(closeadj, volume):
    a = np.log(_f17_dv_smooth(closeadj, volume, 21).replace(0, np.nan)
               / _f17_dv_smooth(closeadj, volume, 63).replace(0, np.nan))
    c = np.log(_f17_dv_smooth(closeadj, volume, 63).replace(0, np.nan)
               / _f17_dv_smooth(closeadj, volume, 252).replace(0, np.nan))
    b = a - c
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- intraday hi/lo dollar tiers & value-vs-price size ----

# spread between intraday-high and intraday-low traded-value tiers, averaged 63d (intraday band)
def f17dv_f17_dollar_volume_dynamics_hilotiergap_63d_base_v116_signal(high, low, volume):
    th = _f17_tier_index((high * volume).clip(lower=0.0))
    tl = _f17_tier_index((low * volume).clip(lower=0.0))
    b = (th - tl).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year the intraday-high traded value cleared one rung above the close anchor
def f17dv_f17_dollar_volume_dynamics_hifracup_252d_base_v117_signal(closeadj, high, volume):
    dvh = (high * volume).clip(lower=0.0)
    dvc = _f17_dv(closeadj, volume)
    ref = _f17_rung(dvc, 1)
    above = (dvh >= ref).astype(float).where(dvh.notna() & ref.notna(), np.nan)
    b = above.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-flow steadiness: negative std of log(value-per-price) over a quarter (how smooth vs erratic
# the underlying share-flow component of traded value is) — a dispersion/stability of the size proxy,
# not a directional trend in volume or dollar value
def f17dv_f17_dollar_volume_dynamics_shareflowsteady_63d_base_v118_signal(closeadj, volume):
    per = _f17_dv_smooth(closeadj, volume, 5) / closeadj.replace(0, np.nan)
    lper = np.log(per.replace(0, np.nan))
    b = -lper.rolling(63, min_periods=21).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar value vs intraday-range value: fraction of value beyond the mid-range traverse (63d)
def f17dv_f17_dollar_volume_dynamics_dvbeyondrange_63d_base_v119_signal(closeadj, volume, high, low):
    mid = (high + low) / 2.0
    rngval = (mid * volume).clip(lower=0.0)
    dv = _f17_dv(closeadj, volume)
    gap = (dv - rngval) / dv.replace(0, np.nan)
    b = gap.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- additional regime / tier variety ----

# within-rung position percentile-ranked vs its own 252d history (rung-internal regime)
def f17dv_f17_dollar_volume_dynamics_wrrank_252d_base_v120_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    wr = _f17_within_rung(dv)
    b = _rank(wr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year the ordinal tier exceeded its own 252d median tier (above-typical size)
def f17dv_f17_dollar_volume_dynamics_tierabovemed_252d_base_v121_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    tier = _f17_tier_ord(dv)
    med = tier.rolling(252, min_periods=126).median()
    above = (tier > med).astype(float).where(tier.notna() & med.notna(), np.nan)
    b = above.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net ordinal-tier change over a quarter (integer rung hops, blended with continuous travel)
def f17dv_f17_dollar_volume_dynamics_tierhop_63d_base_v122_signal(closeadj, volume):
    dvs = _f17_dv_smooth(closeadj, volume, 21)
    ord_now = _f17_tier_ord(dvs)
    hop = ord_now - ord_now.shift(63)
    cont = _f17_tier_index(dvs)
    b = hop + 0.5 * (cont - cont.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# time since the size tier last changed (rung dwell time, normalized over a year)
def f17dv_f17_dollar_volume_dynamics_tierdwell_252d_base_v123_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    tier = _f17_tier_ord(dv)
    changed = (tier != tier.shift(1)).astype(float).where(tier.notna(), np.nan)

    def _since(a):
        idx = np.where(a[::-1] > 0.5)[0]
        return (idx[0] / float(len(a))) if idx.size else 1.0
    b = changed.rolling(252, min_periods=126).apply(_since, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- multi-horizon regime spreads ----

# spread between 63d and 252d dv percentile (short vs long liquidity-phase disagreement)
def f17dv_f17_dollar_volume_dynamics_pctspread_base_v124_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    p63 = dv.rolling(63, min_periods=21).rank(pct=True) - 0.5
    p252 = _rank(dv, 252)
    b = p63 - p252
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-position spread: 126d band position minus 504d band position (phase disagreement)
def f17dv_f17_dollar_volume_dynamics_rngposspread_base_v125_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    p126 = (dv - _rmin(dv, 126)) / (_rmax(dv, 126) - _rmin(dv, 126)).replace(0, np.nan)
    p504 = (dv - _rmin(dv, 504)) / (_rmax(dv, 504) - _rmin(dv, 504)).replace(0, np.nan)
    b = p126 - p504
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- recovery rate / momentum (de-leveled) ----

# dollar-liquidity recovery off 126d trough scaled by time since that trough (recovery rate)
def f17dv_f17_dollar_volume_dynamics_dvrecovrate_126d_base_v126_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    trough = _rmin(dv, 126)
    rec = np.log(dv.replace(0, np.nan) / trough.replace(0, np.nan))

    def _age(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    age = dv.rolling(126, min_periods=63).apply(_age, raw=True)
    b = rec / (age * 126.0 + 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-liquidity recovery momentum: 252d recovery now minus a quarter ago (de-leveled)
def f17dv_f17_dollar_volume_dynamics_dvrecovmom_252d_base_v127_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    trough = _rmin(dv, 252)
    rec = np.log(dv.replace(0, np.nan) / trough.replace(0, np.nan))
    b = rec - rec.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- value spike intensity / clustering, alternate ----

# average over-bar excess on top-decile days over a half-year (event-size intensity)
def f17dv_f17_dollar_volume_dynamics_dvexcint_126d_base_v128_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    bar = dv.rolling(126, min_periods=63).quantile(0.90)
    exc = (dv / bar.replace(0, np.nan) - 1.0).clip(lower=0)
    b = exc.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days since the last top-decile value day, normalized over a half-year (event recency)
def f17dv_f17_dollar_volume_dynamics_dveventage_126d_base_v129_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    bar = dv.rolling(126, min_periods=63).quantile(0.90)
    spike = (dv > bar).astype(float).where(dv.notna() & bar.notna(), np.nan)

    def _since(a):
        idx = np.where(a[::-1] > 0.5)[0]
        return (idx[0] / float(len(a))) if idx.size else 1.0
    b = spike.rolling(126, min_periods=63).apply(_since, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Gini of traded value computed on the 21d-smoothed series over a year (smoothed lumpiness)
def f17dv_f17_dollar_volume_dynamics_dvsmgini_252d_base_v130_signal(closeadj, volume):
    dvs = _f17_dv_smooth(closeadj, volume, 21)
    b = _f17_gini(dvs, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- more tradeability / band features ----

# presence in the basic-liquidity band: fraction of last quarter dv sat between rungs -1 and +1
def f17dv_f17_dollar_volume_dynamics_fracdn1_63d_base_v131_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    lo = _f17_rung(dv, -1)
    hi = _f17_rung(dv, 1)
    inband = ((dv >= lo) & (dv < hi)).astype(float).where(dv.notna() & lo.notna(), np.nan)
    frac = inband.rolling(63, min_periods=21).mean()
    # add within-rung position so the score has fine resolution (not a coarse 0/1 fraction)
    wr = _f17_within_rung(_f17_dv_smooth(closeadj, volume, 21))
    b = frac + 0.3 * (wr - 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tradeability breadth: sum across rungs (-1..+2) of the fraction-of-quarter each was cleared
# (continuous depth-weighted count of how many size rungs the name reliably trades at)
def f17dv_f17_dollar_volume_dynamics_tradebreadth_63d_base_v132_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    tot = pd.Series(0.0, index=dv.index)
    for s in (-1, 0, 1, 2):
        tot = tot + _f17_frac_above_rung(dv, s, 63)
    b = tot.where(dv.notna(), np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change over a quarter in fraction-above-anchor (rung-tradeability momentum, half-year window)
def f17dv_f17_dollar_volume_dynamics_fracanchorchg_126d_base_v133_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    fa = _f17_frac_above_rung(dv, 0, 126)
    b = fa - fa.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- intraday range-value share & typical-value tier ----

# typical-price traded-value tier de-rated by its own 252d peak tier (typical-size headroom)
def f17dv_f17_dollar_volume_dynamics_typtierderate_252d_base_v134_signal(closeadj, volume, high, low):
    typ = ((high + low + closeadj) / 3.0 * volume).clip(lower=0.0)
    tier = _f17_tier_index(typ)
    b = (tier - tier.rolling(252, min_periods=126).max()).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share of traded value attributable to intraday range (mid*vol / close*vol), 126d (structure)
def f17dv_f17_dollar_volume_dynamics_dvrangefrac_126d_base_v135_signal(closeadj, volume, high, low):
    mid = (high + low) / 2.0
    rngval = (mid * volume).clip(lower=0.0)
    dv = _f17_dv(closeadj, volume)
    ratio = rngval / dv.replace(0, np.nan)
    b = ratio.rolling(126, min_periods=63).mean() - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- additional de-leveled regime to reach 150 ----

# EWMA-smoothed within-rung position centred (persistent rung-internal bias)
def f17dv_f17_dollar_volume_dynamics_wrema_base_v136_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    wr = _f17_within_rung(dv)
    b = wr.ewm(span=63, min_periods=21).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# percentile of the 63d dv range-amplitude vs its 252d history (liquidity-volatility regime)
def f17dv_f17_dollar_volume_dynamics_amplrank_252d_base_v137_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 5)
    ampl = (_rmax(dv, 63) - _rmin(dv, 63)) / _median(dv, 63).replace(0, np.nan)
    b = _rank(ampl, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year dv exceeded 5x its own 252d minimum (well above the dry floor)
def f17dv_f17_dollar_volume_dynamics_above5xmin_252d_base_v138_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    mn = _rmin(dv, 252)
    well = (dv > 5.0 * mn).astype(float).where(dv.notna() & mn.notna(), np.nan)
    b = well.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log gap between the 252d dv peak and the 252d dv median (peak-vs-typical liquidity spread)
def f17dv_f17_dollar_volume_dynamics_peakmedgap_252d_base_v139_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    peak = _rmax(dv, 252)
    med = _median(dv, 252)
    b = np.log(peak.replace(0, np.nan) / med.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log gap between the 252d dv median and the 252d dv trough (typical-vs-trough liquidity floor)
def f17dv_f17_dollar_volume_dynamics_medtroughgap_252d_base_v140_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    med = _median(dv, 252)
    trough = _rmin(dv, 252)
    b = np.log(med.replace(0, np.nan) / trough.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# within-rung occupancy skew: mean within-rung position over a year minus 0.5 (do days cluster
# near rung floors or ceilings — a fine-grained size-pinning signal independent of the band level)
def f17dv_f17_dollar_volume_dynamics_bandskew_252d_base_v141_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 5)
    wr = _f17_within_rung(dv)
    b = wr.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# band-position churn: flip count (cross 0.5) blended with band-position dispersion over a year
def f17dv_f17_dollar_volume_dynamics_bandflip_252d_base_v142_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    pos = (dv - _rmin(dv, 252)) / (_rmax(dv, 252) - _rmin(dv, 252)).replace(0, np.nan)
    hi = (pos >= 0.5).astype(float)
    flip = (hi != hi.shift(1)).astype(float).where(pos.notna(), np.nan)
    cnt = flip.rolling(252, min_periods=126).sum()
    disp = pos.rolling(252, min_periods=126).std()
    b = cnt + 20.0 * disp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# within-rung travel: mean absolute daily within-rung changes over a quarter (rung churn)
def f17dv_f17_dollar_volume_dynamics_wrtravel_63d_base_v143_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 5)
    wr = _f17_within_rung(dv)
    d = (wr - wr.shift(1)).abs()
    # ignore rung wraps (|delta| near 1) so travel reflects within-rung motion only
    d = d.where(d < 0.5, np.nan)
    b = d.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-liquidity drawdown velocity: 126d drawdown now minus a month ago (deepening speed)
def f17dv_f17_dollar_volume_dynamics_dvddvel_126d_base_v144_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    peak = _rmax(dv, 126)
    dd = np.log(dv.replace(0, np.nan) / peak.replace(0, np.nan))
    b = dd - dd.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last half-year dv was within 20% of its trailing 126d peak (near-peak liquidity)
def f17dv_f17_dollar_volume_dynamics_nearpeak_126d_base_v145_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    peak = _rmax(dv, 126)
    near = (dv >= 0.8 * peak).astype(float).where(dv.notna() & peak.notna(), np.nan)
    b = near.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-window value spikiness: log ratio of the busiest single day to the median day over the last
# month (peak-to-typical traded-VALUE amplitude — a magnitude spread, distinct from top-k share)
def f17dv_f17_dollar_volume_dynamics_dvspikymonth_21d_base_v146_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    mx = _rmax(dv, 21)
    md = _median(dv, 21)
    b = np.log(mx.replace(0, np.nan) / md.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# half-year size-class breadth: ordinal-tier span blended with continuous tier span (fine res)
def f17dv_f17_dollar_volume_dynamics_tierspan_126d_base_v147_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    tier = _f17_tier_ord(dv)
    ospan = tier.rolling(126, min_periods=63).max() - tier.rolling(126, min_periods=63).min()
    ct = _f17_tier_index(_f17_dv_smooth(closeadj, volume, 21))
    cspan = ct.rolling(126, min_periods=63).max() - ct.rolling(126, min_periods=63).min()
    b = ospan + cspan
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread between value-per-price rank and dollar-value rank (size driven by shares vs price)
def f17dv_f17_dollar_volume_dynamics_sizeshape_252d_base_v148_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    per = dv / closeadj.replace(0, np.nan)
    b = _rank(per, 252) - _rank(dv, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-year size-class de-rating: how far below its 1260d peak continuous $ size-tier the name sits
# now, damped by how long ago that multi-year peak occurred (recently-de-rated large names score
# most negative; a continuous magnitude-x-recency form, distinct from the 1260d range position)
def f17dv_f17_dollar_volume_dynamics_tierderate_1260d_base_v149_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    tier = _f17_tier_index(dv)
    peak = tier.rolling(1260, min_periods=504).max()

    def _age(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    age = tier.rolling(1260, min_periods=504).apply(_age, raw=True)
    b = (tier - peak) * (1.0 - age)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-year band position: where dv sits within its 1260d min-max range (cyclical phase)
def f17dv_f17_dollar_volume_dynamics_dvrngpos_1260d_base_v150_signal(closeadj, volume):
    dv = _f17_dv_smooth(closeadj, volume, 21)
    hi = _rmax(dv, 1260)
    lo = _rmin(dv, 1260)
    b = (dv - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f17dv_f17_dollar_volume_dynamics_tierchop_63d_base_v076_signal,
    f17dv_f17_dollar_volume_dynamics_tieraccel_63d_base_v077_signal,
    f17dv_f17_dollar_volume_dynamics_tierdisagree_base_v078_signal,
    f17dv_f17_dollar_volume_dynamics_tierdisp_base_v079_signal,
    f17dv_f17_dollar_volume_dynamics_wrdisp_63d_base_v080_signal,
    f17dv_f17_dollar_volume_dynamics_wruptime_63d_base_v081_signal,
    f17dv_f17_dollar_volume_dynamics_fracanchor_126d_base_v082_signal,
    f17dv_f17_dollar_volume_dynamics_fracup2_252d_base_v083_signal,
    f17dv_f17_dollar_volume_dynamics_anchorspell_252d_base_v084_signal,
    f17dv_f17_dollar_volume_dynamics_downcross_252d_base_v085_signal,
    f17dv_f17_dollar_volume_dynamics_dvrebuild_504d_base_v086_signal,
    f17dv_f17_dollar_volume_dynamics_dvdd_126d_base_v087_signal,
    f17dv_f17_dollar_volume_dynamics_dvpeakage_504d_base_v088_signal,
    f17dv_f17_dollar_volume_dynamics_dvrngposchg_126d_base_v089_signal,
    f17dv_f17_dollar_volume_dynamics_dvspan_504d_base_v090_signal,
    f17dv_f17_dollar_volume_dynamics_offtrough_252d_base_v091_signal,
    f17dv_f17_dollar_volume_dynamics_dvpct_126d_base_v092_signal,
    f17dv_f17_dollar_volume_dynamics_dvpctchg_126d_base_v093_signal,
    f17dv_f17_dollar_volume_dynamics_dvpctvol_63d_base_v094_signal,
    f17dv_f17_dollar_volume_dynamics_topquint_252d_base_v095_signal,
    f17dv_f17_dollar_volume_dynamics_dvgini_252d_base_v096_signal,
    f17dv_f17_dollar_volume_dynamics_dvbusymass_63d_base_v097_signal,
    f17dv_f17_dollar_volume_dynamics_dvtop20_252d_base_v098_signal,
    f17dv_f17_dollar_volume_dynamics_dvpeakmed_63d_base_v099_signal,
    f17dv_f17_dollar_volume_dynamics_dvginianom_63d_base_v100_signal,
    f17dv_f17_dollar_volume_dynamics_dvp95cnt_126d_base_v101_signal,
    f17dv_f17_dollar_volume_dynamics_dvmaxmean_63d_base_v102_signal,
    f17dv_f17_dollar_volume_dynamics_dvonset_21d_base_v103_signal,
    f17dv_f17_dollar_volume_dynamics_dvburst_252d_base_v104_signal,
    f17dv_f17_dollar_volume_dynamics_dvecho_63d_base_v105_signal,
    f17dv_f17_dollar_volume_dynamics_dvcqv_63d_base_v106_signal,
    f17dv_f17_dollar_volume_dynamics_dvstability_63d_base_v107_signal,
    f17dv_f17_dollar_volume_dynamics_dvrelrange_21d_base_v108_signal,
    f17dv_f17_dollar_volume_dynamics_dvautocorr_63d_base_v109_signal,
    f17dv_f17_dollar_volume_dynamics_dvbuildbal_126d_base_v110_signal,
    f17dv_f17_dollar_volume_dynamics_dvstepbal_252d_base_v111_signal,
    f17dv_f17_dollar_volume_dynamics_dvdryspell_252d_base_v112_signal,
    f17dv_f17_dollar_volume_dynamics_dv5v63_base_v113_signal,
    f17dv_f17_dollar_volume_dynamics_dv126v504_base_v114_signal,
    f17dv_f17_dollar_volume_dynamics_dvtermcurv_base_v115_signal,
    f17dv_f17_dollar_volume_dynamics_hilotiergap_63d_base_v116_signal,
    f17dv_f17_dollar_volume_dynamics_hifracup_252d_base_v117_signal,
    f17dv_f17_dollar_volume_dynamics_shareflowsteady_63d_base_v118_signal,
    f17dv_f17_dollar_volume_dynamics_dvbeyondrange_63d_base_v119_signal,
    f17dv_f17_dollar_volume_dynamics_wrrank_252d_base_v120_signal,
    f17dv_f17_dollar_volume_dynamics_tierabovemed_252d_base_v121_signal,
    f17dv_f17_dollar_volume_dynamics_tierhop_63d_base_v122_signal,
    f17dv_f17_dollar_volume_dynamics_tierdwell_252d_base_v123_signal,
    f17dv_f17_dollar_volume_dynamics_pctspread_base_v124_signal,
    f17dv_f17_dollar_volume_dynamics_rngposspread_base_v125_signal,
    f17dv_f17_dollar_volume_dynamics_dvrecovrate_126d_base_v126_signal,
    f17dv_f17_dollar_volume_dynamics_dvrecovmom_252d_base_v127_signal,
    f17dv_f17_dollar_volume_dynamics_dvexcint_126d_base_v128_signal,
    f17dv_f17_dollar_volume_dynamics_dveventage_126d_base_v129_signal,
    f17dv_f17_dollar_volume_dynamics_dvsmgini_252d_base_v130_signal,
    f17dv_f17_dollar_volume_dynamics_fracdn1_63d_base_v131_signal,
    f17dv_f17_dollar_volume_dynamics_tradebreadth_63d_base_v132_signal,
    f17dv_f17_dollar_volume_dynamics_fracanchorchg_126d_base_v133_signal,
    f17dv_f17_dollar_volume_dynamics_typtierderate_252d_base_v134_signal,
    f17dv_f17_dollar_volume_dynamics_dvrangefrac_126d_base_v135_signal,
    f17dv_f17_dollar_volume_dynamics_wrema_base_v136_signal,
    f17dv_f17_dollar_volume_dynamics_amplrank_252d_base_v137_signal,
    f17dv_f17_dollar_volume_dynamics_above5xmin_252d_base_v138_signal,
    f17dv_f17_dollar_volume_dynamics_peakmedgap_252d_base_v139_signal,
    f17dv_f17_dollar_volume_dynamics_medtroughgap_252d_base_v140_signal,
    f17dv_f17_dollar_volume_dynamics_bandskew_252d_base_v141_signal,
    f17dv_f17_dollar_volume_dynamics_bandflip_252d_base_v142_signal,
    f17dv_f17_dollar_volume_dynamics_wrtravel_63d_base_v143_signal,
    f17dv_f17_dollar_volume_dynamics_dvddvel_126d_base_v144_signal,
    f17dv_f17_dollar_volume_dynamics_nearpeak_126d_base_v145_signal,
    f17dv_f17_dollar_volume_dynamics_dvspikymonth_21d_base_v146_signal,
    f17dv_f17_dollar_volume_dynamics_tierspan_126d_base_v147_signal,
    f17dv_f17_dollar_volume_dynamics_sizeshape_252d_base_v148_signal,
    f17dv_f17_dollar_volume_dynamics_tierderate_1260d_base_v149_signal,
    f17dv_f17_dollar_volume_dynamics_dvrngpos_1260d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F17_DOLLAR_VOLUME_DYNAMICS_REGISTRY_076_150 = REGISTRY


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

    print("OK f17_dollar_volume_dynamics_base_076_150_claude: %d features pass" % n_features)
