import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rsum(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _slope(s, w):
    # OLS slope of s on time index over window w (length-robust for partial windows)
    def _f(a):
        m = len(a)
        idx = np.arange(m, dtype=float)
        xm = idx.mean()
        xden = ((idx - xm) ** 2).sum()
        if xden == 0:
            return np.nan
        return ((idx - xm) * (a - a.mean())).sum() / xden
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_f, raw=True)


# ===== folder domain primitives: DOLLAR-VOLUME (closeadj*volume) =====
def _f17_dv(closeadj, volume):
    # dollar-volume level
    return closeadj * volume


def _f17_logdv(closeadj, volume):
    dv = closeadj * volume
    return np.log(dv.replace(0, np.nan))


def _f17_dv_mean(closeadj, volume, w):
    dv = closeadj * volume
    return dv.rolling(w, min_periods=max(1, w // 2)).mean()


def _f17_dv_med(closeadj, volume, w):
    dv = closeadj * volume
    return dv.rolling(w, min_periods=max(1, w // 2)).median()


def _f17_dv_z(closeadj, volume, w):
    dv = closeadj * volume
    return _z(dv, w)


def _f17_logdv_z(closeadj, volume, w):
    ldv = np.log((closeadj * volume).replace(0, np.nan))
    return _z(ldv, w)


def _f17_dd(closeadj, volume, w):
    # dollar-volume drawdown vs rolling peak
    dv = closeadj * volume
    peak = dv.rolling(w, min_periods=max(1, w // 2)).max()
    return dv / peak.replace(0, np.nan) - 1.0


def _f17_size_tier(closeadj, volume, w):
    # log dollar-volume level as a size-tier proxy (smoothed)
    ldv = np.log((closeadj * volume).replace(0, np.nan))
    return ldv.rolling(w, min_periods=max(1, w // 2)).mean()


# ============================================================
# --- LEVEL / LOG / SMOOTHED MAGNITUDE ---

# log dollar-volume level smoothed over a month (size magnitude)
def f17dv_f17_dollar_volume_dynamics_logdvlvl_21d_base_v001_signal(closeadj, volume):
    b = _f17_size_tier(closeadj, volume, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# persistence of log-DV: lag-1 autocorrelation of daily log dollar-volume over a quarter
def f17dv_f17_dollar_volume_dynamics_dvpersist_63d_base_v002_signal(closeadj, volume):
    ldv = _f17_logdv(closeadj, volume)
    lag = ldv.shift(1)
    # rolling lag-1 autocorr via covariance / variances
    m = ldv.rolling(63, min_periods=21).mean()
    ml = lag.rolling(63, min_periods=21).mean()
    cov = (ldv * lag).rolling(63, min_periods=21).mean() - m * ml
    v0 = ldv.rolling(63, min_periods=21).var()
    v1 = lag.rolling(63, min_periods=21).var()
    b = cov / (np.sqrt(v0 * v1)).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log dollar-volume level smoothed over a year (durable size tier)
def f17dv_f17_dollar_volume_dynamics_logdvlvl_252d_base_v003_signal(closeadj, volume):
    b = _f17_size_tier(closeadj, volume, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# median-DV shift: log-ratio of quarter median DV to year median DV (robust regime shift)
def f17dv_f17_dollar_volume_dynamics_medshift_63v252_base_v004_signal(closeadj, volume):
    sq = _f17_dv_med(closeadj, volume, 63)
    lq = _f17_dv_med(closeadj, volume, 252)
    b = np.log(sq.replace(0, np.nan) / lq.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# mean-to-median dollar-volume ratio (right-skew of activity)
def f17dv_f17_dollar_volume_dynamics_skewdv_63d_base_v005_signal(closeadj, volume):
    mean = _f17_dv_mean(closeadj, volume, 63)
    med = _f17_dv_med(closeadj, volume, 63)
    b = mean / med.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- TREND / SLOPE OF DOLLAR VOLUME ---

# slope of log dollar-volume over a quarter (liquidity growth)
def f17dv_f17_dollar_volume_dynamics_dvtrend_63d_base_v006_signal(closeadj, volume):
    ldv = _f17_logdv(closeadj, volume)
    b = _slope(ldv, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of log dollar-volume over a half-year
def f17dv_f17_dollar_volume_dynamics_dvtrend_126d_base_v007_signal(closeadj, volume):
    ldv = _f17_logdv(closeadj, volume)
    b = _slope(ldv, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log-ratio of short to long dollar-volume average (activity expansion)
def f17dv_f17_dollar_volume_dynamics_dvexp_21v126_base_v008_signal(closeadj, volume):
    s = _f17_dv_mean(closeadj, volume, 21)
    l = _f17_dv_mean(closeadj, volume, 126)
    b = np.log(s.replace(0, np.nan) / l.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log-ratio of quarter to year dollar-volume average (medium-term regime shift)
def f17dv_f17_dollar_volume_dynamics_dvexp_63v252_base_v009_signal(closeadj, volume):
    s = _f17_dv_mean(closeadj, volume, 63)
    l = _f17_dv_mean(closeadj, volume, 252)
    b = np.log(s.replace(0, np.nan) / l.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# year-over-year change in smoothed log dollar-volume (annual liquidity growth)
def f17dv_f17_dollar_volume_dynamics_dvyoy_252d_base_v010_signal(closeadj, volume):
    lvl = _f17_size_tier(closeadj, volume, 63)
    b = lvl - lvl.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Z-SCORE / STANDARDIZED MAGNITUDE ---

# log dollar-volume z-scored vs its own quarter history
def f17dv_f17_dollar_volume_dynamics_logdvz_63d_base_v011_signal(closeadj, volume):
    b = _f17_logdv_z(closeadj, volume, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log dollar-volume z-scored vs its own year history
def f17dv_f17_dollar_volume_dynamics_logdvz_252d_base_v012_signal(closeadj, volume):
    b = _f17_logdv_z(closeadj, volume, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# raw dollar-volume z vs quarter (untransformed magnitude extremity)
def f17dv_f17_dollar_volume_dynamics_dvz_63d_base_v013_signal(closeadj, volume):
    b = _f17_dv_z(closeadj, volume, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed-monthly log dollar-volume z vs year (persistent regime z)
def f17dv_f17_dollar_volume_dynamics_smdvz_252d_base_v014_signal(closeadj, volume):
    lvl = _f17_size_tier(closeadj, volume, 21)
    b = _z(lvl, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# percentile rank of log dollar-volume within trailing year
def f17dv_f17_dollar_volume_dynamics_dvrank_252d_base_v015_signal(closeadj, volume):
    ldv = _f17_logdv(closeadj, volume)
    b = ldv.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- DOLLAR-LIQUIDITY REGIME (level vs thresholds / state fraction) ---

# fraction of quarter spent above the year-median dollar-volume (high-liquidity regime)
def f17dv_f17_dollar_volume_dynamics_hiliqfrac_63d_base_v016_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    med = dv.rolling(252, min_periods=63).median()
    above = (dv > med).astype(float)
    b = above.rolling(63, min_periods=21).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of quarter in a thin-liquidity regime (below 50% of year-median)
def f17dv_f17_dollar_volume_dynamics_thinfrac_63d_base_v017_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    med = dv.rolling(252, min_periods=63).median()
    # depth-weighted thinness: how far below the year median, averaged over a quarter
    shortfall = (1.0 - dv / med.replace(0, np.nan)).clip(lower=0)
    b = shortfall.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# regime distance: smoothed log dollar-volume minus its year median (level gap)
def f17dv_f17_dollar_volume_dynamics_regdist_252d_base_v018_signal(closeadj, volume):
    ldv = _f17_logdv(closeadj, volume)
    lvl = ldv.rolling(21, min_periods=10).mean()
    med = ldv.rolling(252, min_periods=63).median()
    b = lvl - med
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of regime crossings (above<->below year-median) over a quarter (instability)
def f17dv_f17_dollar_volume_dynamics_regcross_63d_base_v019_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    med = dv.rolling(252, min_periods=63).median()
    above = (dv > med).astype(float)
    cross = (above != above.shift(1)).astype(float)
    b = cross.rolling(63, min_periods=21).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity-regime amplitude: log-ratio of mean DV on above-median days to below-median days
def f17dv_f17_dollar_volume_dynamics_regamp_63d_base_v020_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    med = dv.rolling(252, min_periods=63).median()
    hi = dv.where(dv > med, np.nan)
    lo = dv.where(dv <= med, np.nan)
    him = hi.rolling(63, min_periods=15).mean()
    lom = lo.rolling(63, min_periods=15).mean()
    b = np.log(him.replace(0, np.nan) / lom.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- SIZE-TIER DISTANCE ---

# distance of current log-DV tier from its year-high tier (room below ceiling)
def f17dv_f17_dollar_volume_dynamics_tierhigap_252d_base_v021_signal(closeadj, volume):
    lvl = _f17_size_tier(closeadj, volume, 21)
    hi = lvl.rolling(252, min_periods=63).max()
    b = lvl - hi
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance of current log-DV tier above its year-low tier (lift off floor)
def f17dv_f17_dollar_volume_dynamics_tierlogap_252d_base_v022_signal(closeadj, volume):
    lvl = _f17_size_tier(closeadj, volume, 21)
    lo = lvl.rolling(252, min_periods=63).min()
    b = lvl - lo
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# position of log-DV tier within its trailing-year tier range (0..1, centered)
def f17dv_f17_dollar_volume_dynamics_tierpos_252d_base_v023_signal(closeadj, volume):
    lvl = _f17_size_tier(closeadj, volume, 21)
    hi = lvl.rolling(252, min_periods=63).max()
    lo = lvl.rolling(252, min_periods=63).min()
    b = (lvl - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# size-tier step vs two-year tier (multi-year size migration)
def f17dv_f17_dollar_volume_dynamics_tierstep_504d_base_v024_signal(closeadj, volume):
    lvl = _f17_size_tier(closeadj, volume, 63)
    base = _f17_size_tier(closeadj, volume, 504)
    b = lvl - base
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tier elevation vs prior-year tier ceiling, in tier-vol units (standardized size break-up)
def f17dv_f17_dollar_volume_dynamics_tierbreak_252d_base_v025_signal(closeadj, volume):
    lvl = _f17_size_tier(closeadj, volume, 21)
    prior_hi = lvl.shift(1).rolling(252, min_periods=63).max()
    raw = lvl - prior_hi
    b = _z(raw, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- DOLLAR-VOLUME DRAWDOWN / RECOVERY ---

# dollar-volume drawdown vs quarter peak (smoothed series to reduce noise)
def f17dv_f17_dollar_volume_dynamics_dvdd_63d_base_v026_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    sm = dv.rolling(5, min_periods=2).mean()
    peak = sm.rolling(63, min_periods=21).max()
    b = sm / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume drawdown vs year peak (liquidity dry-up depth)
def f17dv_f17_dollar_volume_dynamics_dvdd_252d_base_v027_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    sm = dv.rolling(21, min_periods=10).mean()
    peak = sm.rolling(252, min_periods=63).max()
    b = sm / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume recovery momentum: change in (DV vs year-trough lift) over a quarter
def f17dv_f17_dollar_volume_dynamics_dvrecovmom_252d_base_v028_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    sm = dv.rolling(21, min_periods=10).mean()
    trough = sm.rolling(252, min_periods=63).min()
    rec = np.log(sm.replace(0, np.nan) / trough.replace(0, np.nan))
    b = rec - rec.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year DV spent >30% below year peak (chronic dry-up)
def f17dv_f17_dollar_volume_dynamics_dryupfrac_252d_base_v029_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    sm = dv.rolling(5, min_periods=2).mean()
    peak = sm.rolling(252, min_periods=63).max()
    dd = sm / peak.replace(0, np.nan) - 1.0
    deep = (dd <= -0.30).astype(float)
    b = deep.rolling(252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days since the year dollar-volume peak (staleness of liquidity high)
def f17dv_f17_dollar_volume_dynamics_dsdvpeak_252d_base_v030_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    sm = dv.rolling(5, min_periods=2).mean()

    def _f(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    b = sm.rolling(252, min_periods=63).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- SPIKE MAGNITUDE & PERSISTENCE ---

# spike magnitude vs short prior baseline: today's DV over its prior 10-day median (burst jump)
def f17dv_f17_dollar_volume_dynamics_spikemag_63d_base_v031_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    base = dv.shift(1).rolling(10, min_periods=4).median()
    r = np.log(dv.replace(0, np.nan) / base.replace(0, np.nan))
    # average burst magnitude over the last quarter (persistent burstiness)
    b = r.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spike-excess intensity: summed (DV/median - 2.5) over days exceeding 2.5x, last month
def f17dv_f17_dollar_volume_dynamics_spikexs_21d_base_v032_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    med = dv.rolling(63, min_periods=21).median()
    ratio = dv / med.replace(0, np.nan)
    excess = (ratio - 2.5).clip(lower=0)
    b = excess.rolling(21, min_periods=10).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spike persistence: avg DV multiple on the 3 highest-DV days vs median (peak clustering)
def f17dv_f17_dollar_volume_dynamics_spikepersist_63d_base_v033_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    med = dv.rolling(63, min_periods=21).median()
    ratio = dv / med.replace(0, np.nan)
    b = ratio.rolling(21, min_periods=10).max() - ratio.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# largest single-day DV multiple over the trailing quarter (peak spike intensity)
def f17dv_f17_dollar_volume_dynamics_maxspike_63d_base_v034_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    med = dv.rolling(63, min_periods=21).median()
    ratio = dv / med.replace(0, np.nan)
    b = np.log(ratio.rolling(63, min_periods=21).max().replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spike decay: how fast a DV spike fades (today vs max of prior 5 days)
def f17dv_f17_dollar_volume_dynamics_spikedecay_21d_base_v035_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    prior_peak = dv.shift(1).rolling(5, min_periods=2).max()
    decay = dv / prior_peak.replace(0, np.nan)
    b = decay.rolling(21, min_periods=10).mean() - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- CONCENTRATION ---

# DV concentration: share of quarter dollar-volume on its single biggest day
def f17dv_f17_dollar_volume_dynamics_dvconc_63d_base_v036_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    mx = dv.rolling(63, min_periods=21).max()
    tot = _rsum(dv, 63)
    b = mx / tot.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DV concentration: share of month dollar-volume on top day (short-window crowding)
def f17dv_f17_dollar_volume_dynamics_dvconc_21d_base_v037_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    mx = dv.rolling(21, min_periods=10).max()
    tot = _rsum(dv, 21)
    b = mx / tot.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Herfindahl of dollar-volume shares over a quarter (activity concentration index)
def f17dv_f17_dollar_volume_dynamics_dvhhi_63d_base_v038_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    tot = _rsum(dv, 63)
    sq = _rsum(dv * dv, 63)
    b = sq / (tot * tot).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quartile coefficient of dispersion of dollar-volume over a quarter (robust spread)
def f17dv_f17_dollar_volume_dynamics_dvqcd_63d_base_v039_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    q75 = dv.rolling(63, min_periods=21).quantile(0.75)
    q25 = dv.rolling(63, min_periods=21).quantile(0.25)
    b = (q75 - q25) / (q75 + q25).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# top-5-day share of year dollar-volume (long-window event concentration)
def f17dv_f17_dollar_volume_dynamics_top5share_252d_base_v040_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)

    def _f(a):
        s = np.sort(a)[-5:].sum()
        tot = a.sum()
        return s / tot if tot > 0 else np.nan
    b = dv.rolling(252, min_periods=63).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ADDITIONAL FACETS (level interactions / dispersion / range-weighted) ---

# log dollar-volume vs its 252d EMA (slow trend displacement)
def f17dv_f17_dollar_volume_dynamics_dvdisp_252d_base_v041_signal(closeadj, volume):
    ldv = _f17_logdv(closeadj, volume)
    b = ldv.ewm(span=21, min_periods=10).mean() - ldv.ewm(span=252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-intensity of dollar-volume: month-avg fractional intraday range, z-scored
# (isolates the range multiplier of range-weighted DV from the DV level itself)
def f17dv_f17_dollar_volume_dynamics_rangedv_21d_base_v042_signal(closeadj, volume, high, low):
    rng = (high - low) / low.replace(0, np.nan)
    # weight each day's range by that day's share of month dollar-volume
    dv = closeadj * volume
    w = dv / dv.rolling(21, min_periods=10).sum().replace(0, np.nan)
    wr = (rng * w).rolling(21, min_periods=10).sum()
    b = _z(wr, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-weighted dollar-volume regime: rdv vs its own year median
def f17dv_f17_dollar_volume_dynamics_rangedvreg_252d_base_v043_signal(closeadj, volume, high, low):
    rng = (high - low) / low.replace(0, np.nan)
    rdv = (closeadj * volume) * rng
    sm = rdv.rolling(21, min_periods=10).mean()
    med = rdv.rolling(252, min_periods=63).median()
    b = np.log(sm.replace(0, np.nan) / med.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up-day vs down-day dollar-volume imbalance over a quarter (directional money flow magnitude)
def f17dv_f17_dollar_volume_dynamics_dvimbal_63d_base_v044_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    ret = closeadj.pct_change()
    up = dv.where(ret > 0, 0.0)
    dn = dv.where(ret < 0, 0.0)
    usum = up.rolling(63, min_periods=21).sum()
    dsum = dn.rolling(63, min_periods=21).sum()
    b = (usum - dsum) / (usum + dsum).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume momentum: change in smoothed log-DV over a quarter
def f17dv_f17_dollar_volume_dynamics_dvmom_63d_base_v045_signal(closeadj, volume):
    lvl = _f17_size_tier(closeadj, volume, 21)
    b = lvl - lvl.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration-as-level: short DV trend minus long DV trend (regime curvature)
def f17dv_f17_dollar_volume_dynamics_dvtrendspr_base_v046_signal(closeadj, volume):
    ldv = _f17_logdv(closeadj, volume)
    s = _slope(ldv, 21)
    l = _slope(ldv, 126)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion of daily log-DV changes over a quarter (activity turbulence)
def f17dv_f17_dollar_volume_dynamics_dvturb_63d_base_v047_signal(closeadj, volume):
    ldv = _f17_logdv(closeadj, volume)
    chg = ldv.diff()
    b = _std(chg, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ratio of recent DV peak to recent DV trough over a quarter (activity span)
def f17dv_f17_dollar_volume_dynamics_dvspan_63d_base_v048_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    sm = dv.rolling(5, min_periods=2).mean()
    hi = sm.rolling(63, min_periods=21).max()
    lo = sm.rolling(63, min_periods=21).min()
    b = np.log(hi.replace(0, np.nan) / lo.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tier acceleration: change in year-tier-position over a quarter
def f17dv_f17_dollar_volume_dynamics_tierposmom_252d_base_v049_signal(closeadj, volume):
    lvl = _f17_size_tier(closeadj, volume, 21)
    hi = lvl.rolling(252, min_periods=63).max()
    lo = lvl.rolling(252, min_periods=63).min()
    pos = (lvl - lo) / (hi - lo).replace(0, np.nan)
    b = pos - pos.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# headroom below recent DV high: avg log-gap of smoothed DV to its trailing 63d high
def f17dv_f17_dollar_volume_dynamics_dvheadroom_63d_base_v050_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    sm = dv.rolling(5, min_periods=2).mean()
    hi = sm.rolling(63, min_periods=21).max()
    gap = np.log(sm.replace(0, np.nan) / hi.replace(0, np.nan))
    b = gap.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DV level relative to high-low-range proxy of capital at risk (depth proxy)
def f17dv_f17_dollar_volume_dynamics_dvdepth_21d_base_v051_signal(closeadj, volume, high, low):
    dv = _f17_dv(closeadj, volume)
    span = (high - low)
    depth = dv / span.replace(0, np.nan)
    b = np.log(depth.rolling(21, min_periods=10).mean().replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# half-year vs year DV regime gap z-scored (slow regime extremity)
def f17dv_f17_dollar_volume_dynamics_regzgap_base_v052_signal(closeadj, volume):
    s = _f17_dv_mean(closeadj, volume, 126)
    l = _f17_dv_mean(closeadj, volume, 252)
    gap = np.log(s.replace(0, np.nan) / l.replace(0, np.nan))
    b = _z(gap, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# within-month DV asymmetry: mean of signed deviations from month-mean, scaled (upside skew)
def f17dv_f17_dollar_volume_dynamics_upbias_21d_base_v053_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    m = _mean(dv, 21)
    dev = (dv - m) / m.replace(0, np.nan)
    # mean of cubed deviations -> skew-like asymmetry of within-window activity
    b = (dev ** 3).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity-regime streak: signed consecutive-day run of smoothed-DV above/below year median
def f17dv_f17_dollar_volume_dynamics_regstreak_252d_base_v054_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    sm = dv.rolling(5, min_periods=2).mean()
    med = dv.rolling(252, min_periods=63).median()
    sign = np.sign(sm - med)
    # consecutive run length of the current sign
    grp = (sign != sign.shift(1)).cumsum()
    run = sign.groupby(grp).cumcount() + 1
    b = (sign * run) / 21.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DV drawdown velocity: change in 252d DV drawdown over a month (dry-up speed)
def f17dv_f17_dollar_volume_dynamics_ddvel_252d_base_v055_signal(closeadj, volume):
    dd = _f17_dd(closeadj * 1.0, volume, 252)
    # recompute on smoothed dv for stability
    dv = _f17_dv(closeadj, volume)
    sm = dv.rolling(21, min_periods=10).mean()
    peak = sm.rolling(252, min_periods=63).max()
    dd = sm / peak.replace(0, np.nan) - 1.0
    b = dd - dd.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spike imbalance: fraction of quarter days that are >2x median DV (event density)
def f17dv_f17_dollar_volume_dynamics_eventdens_63d_base_v056_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    med = dv.rolling(63, min_periods=21).median()
    ev = (dv > 2.0 * med).astype(float)
    b = ev.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# size-tier minus two-year tier, z-scored vs year history (durable migration extremity)
def f17dv_f17_dollar_volume_dynamics_tiermigz_504d_base_v057_signal(closeadj, volume):
    lvl = _f17_size_tier(closeadj, volume, 63)
    base = _f17_size_tier(closeadj, volume, 504)
    mig = lvl - base
    b = _z(mig, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log DV percentile rank vs two-year history (long-horizon magnitude rank)
def f17dv_f17_dollar_volume_dynamics_dvrank_504d_base_v058_signal(closeadj, volume):
    ldv = _f17_logdv(closeadj, volume)
    b = ldv.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-bounded log-DV spike magnitude (squashed extremity)
def f17dv_f17_dollar_volume_dynamics_spiketanh_63d_base_v059_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    med = dv.rolling(63, min_periods=21).median()
    r = np.log(dv.replace(0, np.nan) / med.replace(0, np.nan))
    b = np.tanh(r)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DV trough recovery rate: recovery off year trough divided by time since trough
def f17dv_f17_dollar_volume_dynamics_recovrate_252d_base_v060_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    sm = dv.rolling(21, min_periods=10).mean()
    trough = sm.rolling(252, min_periods=63).min()
    rec = np.log(sm.replace(0, np.nan) / trough.replace(0, np.nan))

    def _f(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    dst = sm.rolling(252, min_periods=63).apply(_f, raw=True).replace(0, np.nan)
    b = rec / dst
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# market-depth trend: slope of log (dollar-volume / intraday-range) over a quarter
def f17dv_f17_dollar_volume_dynamics_depthtrend_63d_base_v061_signal(closeadj, volume, high, low):
    dv = _f17_dv(closeadj, volume)
    span = (high - low)
    depth = dv / span.replace(0, np.nan)
    ldepth = np.log(depth.replace(0, np.nan))
    b = _slope(ldepth.rolling(5, min_periods=2).mean(), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quarter mean DV vs prior quarter mean DV (sequential activity step)
def f17dv_f17_dollar_volume_dynamics_seqstep_63d_base_v062_signal(closeadj, volume):
    m = _f17_dv_mean(closeadj, volume, 63)
    b = np.log(m.replace(0, np.nan) / m.shift(63).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upside semi-dispersion of log-DV changes (asymmetric activity bursts)
def f17dv_f17_dollar_volume_dynamics_updisp_63d_base_v063_signal(closeadj, volume):
    ldv = _f17_logdv(closeadj, volume)
    chg = ldv.diff()
    up = chg.where(chg > 0, np.nan)
    b = up.rolling(63, min_periods=15).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# downside semi-dispersion of log-DV changes (collapse turbulence)
def f17dv_f17_dollar_volume_dynamics_dndisp_63d_base_v064_signal(closeadj, volume):
    ldv = _f17_logdv(closeadj, volume)
    chg = ldv.diff()
    dn = chg.where(chg < 0, np.nan)
    b = dn.rolling(63, min_periods=15).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# semi-dispersion asymmetry: up minus down log-DV change dispersion
def f17dv_f17_dollar_volume_dynamics_dispasym_63d_base_v065_signal(closeadj, volume):
    ldv = _f17_logdv(closeadj, volume)
    chg = ldv.diff()
    up = chg.where(chg > 0, np.nan).rolling(63, min_periods=15).std()
    dn = chg.where(chg < 0, np.nan).rolling(63, min_periods=15).std()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DV at year-tier ceiling persistence: fraction of quarter within 90% of year DV high
def f17dv_f17_dollar_volume_dynamics_ceilhug_252d_base_v066_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    sm = dv.rolling(5, min_periods=2).mean()
    hi = sm.rolling(252, min_periods=63).max()
    near = (sm >= 0.9 * hi).astype(float)
    b = near.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log-DV kurtosis-like tail proxy: 95th vs 50th percentile spread over a year
def f17dv_f17_dollar_volume_dynamics_tailspread_252d_base_v067_signal(closeadj, volume):
    ldv = _f17_logdv(closeadj, volume)
    q95 = ldv.rolling(252, min_periods=63).quantile(0.95)
    q50 = ldv.rolling(252, min_periods=63).quantile(0.50)
    b = q95 - q50
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# low-tail spread: 50th vs 5th percentile of log-DV (thin-side spread)
def f17dv_f17_dollar_volume_dynamics_lowtail_252d_base_v068_signal(closeadj, volume):
    ldv = _f17_logdv(closeadj, volume)
    q50 = ldv.rolling(252, min_periods=63).quantile(0.50)
    q05 = ldv.rolling(252, min_periods=63).quantile(0.05)
    b = q50 - q05
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DV interquartile range over a year (spread of typical activity)
def f17dv_f17_dollar_volume_dynamics_dviqr_252d_base_v069_signal(closeadj, volume):
    ldv = _f17_logdv(closeadj, volume)
    q75 = ldv.rolling(252, min_periods=63).quantile(0.75)
    q25 = ldv.rolling(252, min_periods=63).quantile(0.25)
    b = q75 - q25
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tier-distance to two-year ceiling (room below multi-year liquidity peak)
def f17dv_f17_dollar_volume_dynamics_tierceil_504d_base_v070_signal(closeadj, volume):
    lvl = _f17_size_tier(closeadj, volume, 21)
    hi = lvl.rolling(504, min_periods=126).max()
    b = lvl - hi
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DV trend consistency: sign agreement of monthly log-DV changes over a year
def f17dv_f17_dollar_volume_dynamics_trendcons_252d_base_v071_signal(closeadj, volume):
    lvl = _f17_size_tier(closeadj, volume, 21)
    chg = lvl - lvl.shift(21)
    sgn = np.sign(chg)
    b = sgn.rolling(252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spike clustering: serial correlation of high-DV-day indicator over a quarter
def f17dv_f17_dollar_volume_dynamics_spikeclust_63d_base_v072_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    med = dv.rolling(63, min_periods=21).median()
    ind = (dv > 1.5 * med).astype(float)
    pair = ind * ind.shift(1)
    b = pair.rolling(63, min_periods=21).mean() - ind.rolling(63, min_periods=21).mean() ** 2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DV co-movement: rolling correlation of |daily return| with daily log-DV change over a quarter
# (does dollar-volume surge on big price moves -> event-driven activity signature)
def f17dv_f17_dollar_volume_dynamics_dvcomove_63d_base_v073_signal(closeadj, volume):
    aret = closeadj.pct_change().abs()
    dldv = _f17_logdv(closeadj, volume).diff()
    ma = aret.rolling(63, min_periods=21).mean()
    md = dldv.rolling(63, min_periods=21).mean()
    cov = (aret * dldv).rolling(63, min_periods=21).mean() - ma * md
    va = aret.rolling(63, min_periods=21).var()
    vd = dldv.rolling(63, min_periods=21).var()
    b = cov / (np.sqrt(va * vd)).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net DV regime score: standardized regime distance modulated by DV trend direction
# (high level AND rising = strong; high but fading = weaker) -> interaction composite
def f17dv_f17_dollar_volume_dynamics_regcomposite_252d_base_v074_signal(closeadj, volume):
    ldv = _f17_logdv(closeadj, volume)
    lvl = ldv.rolling(21, min_periods=10).mean()
    med = ldv.rolling(252, min_periods=63).median()
    sd = ldv.rolling(252, min_periods=63).std()
    rd = (lvl - med) / sd.replace(0, np.nan)
    trend = lvl - lvl.shift(63)
    b = np.tanh(rd) * np.tanh(8.0 * trend)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable thin-float flag magnitude: how far below year-25th-pct DV the smoothed level sits
def f17dv_f17_dollar_volume_dynamics_thindist_252d_base_v075_signal(closeadj, volume):
    ldv = _f17_logdv(closeadj, volume)
    lvl = ldv.rolling(21, min_periods=10).mean()
    q25 = ldv.rolling(252, min_periods=63).quantile(0.25)
    b = (q25 - lvl).clip(lower=0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f17dv_f17_dollar_volume_dynamics_logdvlvl_21d_base_v001_signal,
    f17dv_f17_dollar_volume_dynamics_dvpersist_63d_base_v002_signal,
    f17dv_f17_dollar_volume_dynamics_logdvlvl_252d_base_v003_signal,
    f17dv_f17_dollar_volume_dynamics_medshift_63v252_base_v004_signal,
    f17dv_f17_dollar_volume_dynamics_skewdv_63d_base_v005_signal,
    f17dv_f17_dollar_volume_dynamics_dvtrend_63d_base_v006_signal,
    f17dv_f17_dollar_volume_dynamics_dvtrend_126d_base_v007_signal,
    f17dv_f17_dollar_volume_dynamics_dvexp_21v126_base_v008_signal,
    f17dv_f17_dollar_volume_dynamics_dvexp_63v252_base_v009_signal,
    f17dv_f17_dollar_volume_dynamics_dvyoy_252d_base_v010_signal,
    f17dv_f17_dollar_volume_dynamics_logdvz_63d_base_v011_signal,
    f17dv_f17_dollar_volume_dynamics_logdvz_252d_base_v012_signal,
    f17dv_f17_dollar_volume_dynamics_dvz_63d_base_v013_signal,
    f17dv_f17_dollar_volume_dynamics_smdvz_252d_base_v014_signal,
    f17dv_f17_dollar_volume_dynamics_dvrank_252d_base_v015_signal,
    f17dv_f17_dollar_volume_dynamics_hiliqfrac_63d_base_v016_signal,
    f17dv_f17_dollar_volume_dynamics_thinfrac_63d_base_v017_signal,
    f17dv_f17_dollar_volume_dynamics_regdist_252d_base_v018_signal,
    f17dv_f17_dollar_volume_dynamics_regcross_63d_base_v019_signal,
    f17dv_f17_dollar_volume_dynamics_regamp_63d_base_v020_signal,
    f17dv_f17_dollar_volume_dynamics_tierhigap_252d_base_v021_signal,
    f17dv_f17_dollar_volume_dynamics_tierlogap_252d_base_v022_signal,
    f17dv_f17_dollar_volume_dynamics_tierpos_252d_base_v023_signal,
    f17dv_f17_dollar_volume_dynamics_tierstep_504d_base_v024_signal,
    f17dv_f17_dollar_volume_dynamics_tierbreak_252d_base_v025_signal,
    f17dv_f17_dollar_volume_dynamics_dvdd_63d_base_v026_signal,
    f17dv_f17_dollar_volume_dynamics_dvdd_252d_base_v027_signal,
    f17dv_f17_dollar_volume_dynamics_dvrecovmom_252d_base_v028_signal,
    f17dv_f17_dollar_volume_dynamics_dryupfrac_252d_base_v029_signal,
    f17dv_f17_dollar_volume_dynamics_dsdvpeak_252d_base_v030_signal,
    f17dv_f17_dollar_volume_dynamics_spikemag_63d_base_v031_signal,
    f17dv_f17_dollar_volume_dynamics_spikexs_21d_base_v032_signal,
    f17dv_f17_dollar_volume_dynamics_spikepersist_63d_base_v033_signal,
    f17dv_f17_dollar_volume_dynamics_maxspike_63d_base_v034_signal,
    f17dv_f17_dollar_volume_dynamics_spikedecay_21d_base_v035_signal,
    f17dv_f17_dollar_volume_dynamics_dvconc_63d_base_v036_signal,
    f17dv_f17_dollar_volume_dynamics_dvconc_21d_base_v037_signal,
    f17dv_f17_dollar_volume_dynamics_dvhhi_63d_base_v038_signal,
    f17dv_f17_dollar_volume_dynamics_dvqcd_63d_base_v039_signal,
    f17dv_f17_dollar_volume_dynamics_top5share_252d_base_v040_signal,
    f17dv_f17_dollar_volume_dynamics_dvdisp_252d_base_v041_signal,
    f17dv_f17_dollar_volume_dynamics_rangedv_21d_base_v042_signal,
    f17dv_f17_dollar_volume_dynamics_rangedvreg_252d_base_v043_signal,
    f17dv_f17_dollar_volume_dynamics_dvimbal_63d_base_v044_signal,
    f17dv_f17_dollar_volume_dynamics_dvmom_63d_base_v045_signal,
    f17dv_f17_dollar_volume_dynamics_dvtrendspr_base_v046_signal,
    f17dv_f17_dollar_volume_dynamics_dvturb_63d_base_v047_signal,
    f17dv_f17_dollar_volume_dynamics_dvspan_63d_base_v048_signal,
    f17dv_f17_dollar_volume_dynamics_tierposmom_252d_base_v049_signal,
    f17dv_f17_dollar_volume_dynamics_dvheadroom_63d_base_v050_signal,
    f17dv_f17_dollar_volume_dynamics_dvdepth_21d_base_v051_signal,
    f17dv_f17_dollar_volume_dynamics_regzgap_base_v052_signal,
    f17dv_f17_dollar_volume_dynamics_upbias_21d_base_v053_signal,
    f17dv_f17_dollar_volume_dynamics_regstreak_252d_base_v054_signal,
    f17dv_f17_dollar_volume_dynamics_ddvel_252d_base_v055_signal,
    f17dv_f17_dollar_volume_dynamics_eventdens_63d_base_v056_signal,
    f17dv_f17_dollar_volume_dynamics_tiermigz_504d_base_v057_signal,
    f17dv_f17_dollar_volume_dynamics_dvrank_504d_base_v058_signal,
    f17dv_f17_dollar_volume_dynamics_spiketanh_63d_base_v059_signal,
    f17dv_f17_dollar_volume_dynamics_recovrate_252d_base_v060_signal,
    f17dv_f17_dollar_volume_dynamics_depthtrend_63d_base_v061_signal,
    f17dv_f17_dollar_volume_dynamics_seqstep_63d_base_v062_signal,
    f17dv_f17_dollar_volume_dynamics_updisp_63d_base_v063_signal,
    f17dv_f17_dollar_volume_dynamics_dndisp_63d_base_v064_signal,
    f17dv_f17_dollar_volume_dynamics_dispasym_63d_base_v065_signal,
    f17dv_f17_dollar_volume_dynamics_ceilhug_252d_base_v066_signal,
    f17dv_f17_dollar_volume_dynamics_tailspread_252d_base_v067_signal,
    f17dv_f17_dollar_volume_dynamics_lowtail_252d_base_v068_signal,
    f17dv_f17_dollar_volume_dynamics_dviqr_252d_base_v069_signal,
    f17dv_f17_dollar_volume_dynamics_tierceil_504d_base_v070_signal,
    f17dv_f17_dollar_volume_dynamics_trendcons_252d_base_v071_signal,
    f17dv_f17_dollar_volume_dynamics_spikeclust_63d_base_v072_signal,
    f17dv_f17_dollar_volume_dynamics_dvcomove_63d_base_v073_signal,
    f17dv_f17_dollar_volume_dynamics_regcomposite_252d_base_v074_signal,
    f17dv_f17_dollar_volume_dynamics_thindist_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F17_DOLLAR_VOLUME_DYNAMICS_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    ALLOW = {"open", "high", "low", "close", "closeadj", "volume",
             "revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc", "opex",
             "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin", "netinc",
             "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps", "ncfo", "ncff", "ncfi",
             "ncfcommon", "ncfdebt", "ncfbus", "capex", "depamor", "sharesbas", "shareswa",
             "shareswadil", "assets", "assetsc", "tangibles", "intangibles", "ppnenet",
             "investments", "inventory", "receivables", "payables", "equity", "retearn",
             "workingcapital", "debt", "debtc", "debtnc", "liabilities", "liabilitiesc",
             "cashneq", "currentratio", "roic", "roe", "roa", "ros", "assetturnover", "invcap",
             "intexp", "taxexp", "ebt", "sps", "bvps", "de", "ncfdiv", "dps", "divyield",
             "payoutratio", "prefdivis", "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
             "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal", "fndholders",
             "undholders", "prfholders", "dbtholders", "putholders", "putvalue", "cllholders",
             "cllvalue", "wntholders", "wntvalue", "dbtvalue"}

    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0004, 0.032, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.012, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.02, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.02, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1.2e6, 7e5, n)) + 5e4, name="volume")

    cols = {"closeadj": closeadj, "close": close, "open": openp,
            "high": high, "low": low, "volume": volume}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs %s" % (name, meta["inputs"])
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
