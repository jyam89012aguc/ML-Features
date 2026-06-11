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
    return closeadj * volume


def _f17_logdv(closeadj, volume):
    return np.log((closeadj * volume).replace(0, np.nan))


def _f17_dv_mean(closeadj, volume, w):
    dv = closeadj * volume
    return dv.rolling(w, min_periods=max(1, w // 2)).mean()


def _f17_dv_med(closeadj, volume, w):
    dv = closeadj * volume
    return dv.rolling(w, min_periods=max(1, w // 2)).median()


def _f17_size_tier(closeadj, volume, w):
    ldv = np.log((closeadj * volume).replace(0, np.nan))
    return ldv.rolling(w, min_periods=max(1, w // 2)).mean()


def _f17_streak_sign(sm, ref):
    sign = np.sign(sm - ref)
    grp = (sign != sign.shift(1)).cumsum()
    run = sign.groupby(grp).cumcount() + 1
    return sign * run


# ============================================================
# --- LEVEL / LOG / SMOOTHED (longer & mixed horizons) ---

# log dollar-volume level smoothed over a half-year (medium-horizon size tier)
def f17dv_f17_dollar_volume_dynamics_logdvlvl_126d_base_v076_signal(closeadj, volume):
    b = _f17_size_tier(closeadj, volume, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# two-year smoothed log-DV (very durable size class)
def f17dv_f17_dollar_volume_dynamics_logdvlvl_504d_base_v077_signal(closeadj, volume):
    b = _f17_size_tier(closeadj, volume, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA log-DV with fast span (responsive level)
def f17dv_f17_dollar_volume_dynamics_emadv_fast_base_v078_signal(closeadj, volume):
    ldv = _f17_logdv(closeadj, volume)
    b = ldv.ewm(span=10, min_periods=5).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weekly mean DV (very short magnitude) z-scored vs quarter
def f17dv_f17_dollar_volume_dynamics_wkdvz_5v63_base_v079_signal(closeadj, volume):
    wk = _f17_dv_mean(closeadj, volume, 5)
    lwk = np.log(wk.replace(0, np.nan))
    b = _z(lwk, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative-notional growth: log-ratio of trailing-quarter total DV to the prior quarter total
def f17dv_f17_dollar_volume_dynamics_dvtotgrow_63d_base_v080_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    tot = _rsum(dv, 63)
    b = np.log(tot.replace(0, np.nan) / tot.shift(63).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- TREND / EXPANSION (more horizons / EMA crosses) ---

# log-DV fast EMA minus slow EMA (MACD-style activity expansion)
def f17dv_f17_dollar_volume_dynamics_dvmacd_base_v081_signal(closeadj, volume):
    ldv = _f17_logdv(closeadj, volume)
    b = ldv.ewm(span=12, min_periods=6).mean() - ldv.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of log dollar-volume over a year (long-run liquidity drift)
def f17dv_f17_dollar_volume_dynamics_dvtrend_252d_base_v082_signal(closeadj, volume):
    ldv = _f17_logdv(closeadj, volume)
    b = _slope(ldv.rolling(5, min_periods=2).mean(), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# month-over-month DV step: log-ratio of last 21d mean to prior 21d mean
def f17dv_f17_dollar_volume_dynamics_dvstep_21d_base_v083_signal(closeadj, volume):
    m = _f17_dv_mean(closeadj, volume, 21)
    b = np.log(m.replace(0, np.nan) / m.shift(21).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short impulse expansion: 5d mean DV vs 21d mean DV (weekly-vs-monthly burst)
def f17dv_f17_dollar_volume_dynamics_dvexp_5v21_base_v084_signal(closeadj, volume):
    s = _f17_dv_mean(closeadj, volume, 5)
    l = _f17_dv_mean(closeadj, volume, 21)
    b = np.log(s.replace(0, np.nan) / l.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slow-regime convexity: (63v252 expansion) minus (126v504 expansion) (drift acceleration)
def f17dv_f17_dollar_volume_dynamics_dvexpconv_base_v085_signal(closeadj, volume):
    e1 = np.log(_f17_dv_mean(closeadj, volume, 63).replace(0, np.nan)
                / _f17_dv_mean(closeadj, volume, 252).replace(0, np.nan))
    e2 = np.log(_f17_dv_mean(closeadj, volume, 126).replace(0, np.nan)
                / _f17_dv_mean(closeadj, volume, 504).replace(0, np.nan))
    b = e1 - e2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Z / RANK (other horizons & robust variants) ---

# log-DV z vs half-year history
def f17dv_f17_dollar_volume_dynamics_logdvz_126d_base_v086_signal(closeadj, volume):
    ldv = _f17_logdv(closeadj, volume)
    b = _z(ldv, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# robust z of log-DV using median & MAD over a year (outlier-resistant extremity)
def f17dv_f17_dollar_volume_dynamics_robz_252d_base_v087_signal(closeadj, volume):
    ldv = _f17_logdv(closeadj, volume)
    med = ldv.rolling(252, min_periods=63).median()
    mad = (ldv - med).abs().rolling(252, min_periods=63).median()
    b = (ldv - med) / (1.4826 * mad).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# percentile rank of smoothed log-DV within a half-year window
def f17dv_f17_dollar_volume_dynamics_dvrank_126d_base_v088_signal(closeadj, volume):
    lvl = _f17_size_tier(closeadj, volume, 5)
    b = lvl.rolling(126, min_periods=42).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# z of quarter-total DV vs its own year history (cumulative-notional extremity)
def f17dv_f17_dollar_volume_dynamics_totz_63v252_base_v089_signal(closeadj, volume):
    tot = _rsum(_f17_dv(closeadj, volume), 63)
    b = _z(np.log(tot.replace(0, np.nan)), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weekly DV rank vs two-year history (short magnitude in long context)
def f17dv_f17_dollar_volume_dynamics_wkrank_504d_base_v090_signal(closeadj, volume):
    wk = _f17_dv_mean(closeadj, volume, 5)
    lwk = np.log(wk.replace(0, np.nan))
    b = lwk.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- REGIME (other reference levels / durations) ---

# regime distance vs two-year median (multi-year liquidity regime gap)
def f17dv_f17_dollar_volume_dynamics_regdist_504d_base_v091_signal(closeadj, volume):
    ldv = _f17_logdv(closeadj, volume)
    lvl = ldv.rolling(21, min_periods=10).mean()
    med = ldv.rolling(504, min_periods=126).median()
    b = lvl - med
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# staleness of elevated liquidity: fraction of trailing quarter since DV last exceeded year-75th-pct
def f17dv_f17_dollar_volume_dynamics_elevstale_63d_base_v092_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    q75 = dv.rolling(252, min_periods=63).quantile(0.75)
    hot = (dv > q75).astype(float)

    def _f(a):
        # fraction of window since the most recent "hot" day; 1.0 if none in window
        nz = np.nonzero(a)[0]
        if len(nz) == 0:
            return 1.0
        return (len(a) - 1 - nz[-1]) / float(len(a))
    b = hot.rolling(63, min_periods=21).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed streak of smoothed DV vs its 126d mean (regime persistence, half-year ref)
def f17dv_f17_dollar_volume_dynamics_regstreak_126d_base_v093_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    sm = dv.rolling(10, min_periods=4).mean()
    ref = dv.rolling(126, min_periods=42).mean()
    b = _f17_streak_sign(sm, ref) / 21.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# regime transition count above/below year-25th-pct over a year (low-liq toggling)
def f17dv_f17_dollar_volume_dynamics_lowtoggle_252d_base_v094_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    q25 = dv.rolling(252, min_periods=63).quantile(0.25)
    below = (dv < q25).astype(float)
    cross = (below != below.shift(1)).astype(float)
    b = cross.rolling(252, min_periods=63).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# regime amplitude vs year-quartiles: log(q75/q25) of DV over a year (regime span)
def f17dv_f17_dollar_volume_dynamics_regspan_252d_base_v095_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    q75 = dv.rolling(252, min_periods=63).quantile(0.75)
    q25 = dv.rolling(252, min_periods=63).quantile(0.25)
    b = np.log(q75.replace(0, np.nan) / q25.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- SIZE-TIER DISTANCE (other anchors) ---

# tier distance vs half-year tier (medium-term size migration)
def f17dv_f17_dollar_volume_dynamics_tierstep_126d_base_v096_signal(closeadj, volume):
    lvl = _f17_size_tier(closeadj, volume, 21)
    base = _f17_size_tier(closeadj, volume, 126)
    b = lvl - base
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tier position within two-year tier range (long-horizon size standing)
def f17dv_f17_dollar_volume_dynamics_tierpos_504d_base_v097_signal(closeadj, volume):
    lvl = _f17_size_tier(closeadj, volume, 21)
    hi = lvl.rolling(504, min_periods=126).max()
    lo = lvl.rolling(504, min_periods=126).min()
    b = (lvl - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance to two-year tier floor (lift above multi-year liquidity floor)
def f17dv_f17_dollar_volume_dynamics_tierfloor_504d_base_v098_signal(closeadj, volume):
    lvl = _f17_size_tier(closeadj, volume, 21)
    lo = lvl.rolling(504, min_periods=126).min()
    b = lvl - lo
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tier-range width: two-year tier high minus low (how wide the size class has swung)
def f17dv_f17_dollar_volume_dynamics_tierwidth_504d_base_v099_signal(closeadj, volume):
    lvl = _f17_size_tier(closeadj, volume, 21)
    hi = lvl.rolling(504, min_periods=126).max()
    lo = lvl.rolling(504, min_periods=126).min()
    b = hi - lo
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tier migration over a year (smoothed level now vs one year ago)
def f17dv_f17_dollar_volume_dynamics_tieryoy_252d_base_v100_signal(closeadj, volume):
    lvl = _f17_size_tier(closeadj, volume, 21)
    b = lvl - lvl.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- DRAWDOWN / RECOVERY (other horizons) ---

# DV drawdown vs half-year peak (medium-term dry-up depth)
def f17dv_f17_dollar_volume_dynamics_dvdd_126d_base_v101_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    sm = dv.rolling(10, min_periods=4).mean()
    peak = sm.rolling(126, min_periods=42).max()
    b = sm / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DV drawdown vs two-year peak (multi-year liquidity erosion)
def f17dv_f17_dollar_volume_dynamics_dvdd_504d_base_v102_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    sm = dv.rolling(21, min_periods=10).mean()
    peak = sm.rolling(504, min_periods=126).max()
    b = sm / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# average DV drawdown over a year (liquidity pain index)
def f17dv_f17_dollar_volume_dynamics_dvpain_252d_base_v103_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    sm = dv.rolling(10, min_periods=4).mean()
    peak = sm.rolling(252, min_periods=63).max()
    dd = sm / peak.replace(0, np.nan) - 1.0
    b = dd.rolling(252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days since the two-year DV peak (staleness of multi-year liquidity high)
def f17dv_f17_dollar_volume_dynamics_dsdvpeak_504d_base_v104_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    sm = dv.rolling(10, min_periods=4).mean()

    def _f(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    b = sm.rolling(504, min_periods=126).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DV drawdown recovery rate off year peak: how much of the dry-up has been retraced
def f17dv_f17_dollar_volume_dynamics_ddretrace_252d_base_v105_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    sm = dv.rolling(10, min_periods=4).mean()
    peak = sm.rolling(252, min_periods=63).max()
    trough = sm.rolling(63, min_periods=21).min()
    b = (sm - trough) / (peak - trough).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- SPIKE (other definitions) ---

# spike magnitude vs year median (long-context burst size)
def f17dv_f17_dollar_volume_dynamics_spikemag_252d_base_v106_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    med = dv.rolling(252, min_periods=63).median()
    r = np.log(dv.replace(0, np.nan) / med.replace(0, np.nan))
    b = r.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# extreme-spike excess sum over a quarter (>4x year median) (rare-event intensity)
def f17dv_f17_dollar_volume_dynamics_extspike_63d_base_v107_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    med = dv.rolling(252, min_periods=63).median()
    ratio = dv / med.replace(0, np.nan)
    excess = (ratio - 4.0).clip(lower=0)
    b = excess.rolling(63, min_periods=21).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spike asymmetry: max-day vs min-day DV multiple over a quarter (one-sided burstiness)
def f17dv_f17_dollar_volume_dynamics_spikeasym_63d_base_v108_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    med = dv.rolling(63, min_periods=21).median()
    ratio = dv / med.replace(0, np.nan)
    hi = ratio.rolling(63, min_periods=21).max()
    lo = ratio.rolling(63, min_periods=21).min()
    b = np.log(hi.replace(0, np.nan)) + np.log(lo.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# post-spike persistence: mean DV multiple in the 3 days after the quarter's biggest spike-ish day
def f17dv_f17_dollar_volume_dynamics_spikefollow_21d_base_v109_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    med = dv.rolling(63, min_periods=21).median()
    ratio = dv / med.replace(0, np.nan)
    # average of next-day ratio when today is a spike (>2x): persistence proxy
    spike = ratio.shift(1) > 2.0
    follow = ratio.where(spike, np.nan)
    b = follow.rolling(21, min_periods=5).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spike frequency-weighted magnitude: sum of (ratio-1)+ over a month (total positive surprise)
def f17dv_f17_dollar_volume_dynamics_surprisemag_21d_base_v110_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    med = dv.rolling(63, min_periods=21).median()
    ratio = dv / med.replace(0, np.nan)
    pos = (ratio - 1.0).clip(lower=0)
    b = pos.rolling(21, min_periods=10).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- CONCENTRATION (other windows / definitions) ---

# top-day share of half-year dollar-volume (medium-window event crowding)
def f17dv_f17_dollar_volume_dynamics_dvconc_126d_base_v111_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    mx = dv.rolling(126, min_periods=42).max()
    tot = _rsum(dv, 126)
    b = mx / tot.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Herfindahl of DV shares over a year (long-window activity concentration)
def f17dv_f17_dollar_volume_dynamics_dvhhi_252d_base_v112_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    tot = _rsum(dv, 252)
    sq = _rsum(dv * dv, 252)
    b = sq / (tot * tot).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# top-3-day share of quarter dollar-volume (short-burst concentration)
def f17dv_f17_dollar_volume_dynamics_top3share_63d_base_v113_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)

    def _f(a):
        s = np.sort(a)[-3:].sum()
        tot = a.sum()
        return s / tot if tot > 0 else np.nan
    b = dv.rolling(63, min_periods=21).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# effective number of active days = 1/HHI over a quarter (breadth of activity)
def f17dv_f17_dollar_volume_dynamics_effdays_63d_base_v114_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    tot = _rsum(dv, 63)
    sq = _rsum(dv * dv, 63)
    hhi = sq / (tot * tot).replace(0, np.nan)
    b = 1.0 / hhi.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# temporal tilt of DV over a quarter: recent-half share minus older-half share (front/back loading)
def f17dv_f17_dollar_volume_dynamics_dvtilt_63d_base_v115_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    recent = _rsum(dv, 21)
    older = _rsum(dv.shift(42), 21)
    b = (recent - older) / (recent + older).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- DISPERSION / TAILS (other windows) ---

# dispersion of daily log-DV changes over a month (short-term turbulence)
def f17dv_f17_dollar_volume_dynamics_dvturb_21d_base_v116_signal(closeadj, volume):
    ldv = _f17_logdv(closeadj, volume)
    chg = ldv.diff()
    b = _std(chg, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turbulence ratio: short vs long log-DV-change dispersion (turbulence expansion)
def f17dv_f17_dollar_volume_dynamics_turbratio_base_v117_signal(closeadj, volume):
    ldv = _f17_logdv(closeadj, volume)
    chg = ldv.diff()
    s = _std(chg, 21)
    l = _std(chg, 126)
    b = np.log(s.replace(0, np.nan) / l.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upper-tail spread of log-DV over a quarter (99th vs 50th pct, short-window tail)
def f17dv_f17_dollar_volume_dynamics_tailspread_63d_base_v118_signal(closeadj, volume):
    ldv = _f17_logdv(closeadj, volume)
    q90 = ldv.rolling(63, min_periods=21).quantile(0.90)
    q50 = ldv.rolling(63, min_periods=21).quantile(0.50)
    b = q90 - q50
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tail asymmetry of log-DV over a year: (q90-q50) minus (q50-q10) (skew of activity)
def f17dv_f17_dollar_volume_dynamics_tailskew_252d_base_v119_signal(closeadj, volume):
    ldv = _f17_logdv(closeadj, volume)
    q90 = ldv.rolling(252, min_periods=63).quantile(0.90)
    q50 = ldv.rolling(252, min_periods=63).quantile(0.50)
    q10 = ldv.rolling(252, min_periods=63).quantile(0.10)
    b = (q90 - q50) - (q50 - q10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rolling kurtosis of daily log-DV changes over a quarter (fat-tail burst risk)
def f17dv_f17_dollar_volume_dynamics_dvkurt_63d_base_v120_signal(closeadj, volume):
    ldv = _f17_logdv(closeadj, volume)
    chg = ldv.diff()
    b = chg.rolling(63, min_periods=21).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- DIRECTIONAL / FLOW MAGNITUDE ---

# up-day DV share over a month (short-window accumulation magnitude)
def f17dv_f17_dollar_volume_dynamics_updvshare_21d_base_v121_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    ret = closeadj.pct_change()
    up = dv.where(ret > 0, 0.0)
    b = up.rolling(21, min_periods=10).sum() / _rsum(dv, 21).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return-weighted dollar-volume over a quarter (signed money-flow magnitude, normalized)
def f17dv_f17_dollar_volume_dynamics_signedflow_63d_base_v122_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    ret = closeadj.pct_change()
    flow = (ret * dv).rolling(63, min_periods=21).sum()
    norm = _rsum(dv, 63)
    b = flow / norm.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DV-weighted average return over a quarter minus simple average return (flow tilt)
def f17dv_f17_dollar_volume_dynamics_flowtilt_63d_base_v123_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    ret = closeadj.pct_change()
    wavg = (ret * dv).rolling(63, min_periods=21).sum() / _rsum(dv, 63).replace(0, np.nan)
    savg = ret.rolling(63, min_periods=21).mean()
    b = wavg - savg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up vs down DV imbalance over a year (long-horizon directional activity magnitude)
def f17dv_f17_dollar_volume_dynamics_dvimbal_252d_base_v124_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    ret = closeadj.pct_change()
    up = dv.where(ret > 0, 0.0).rolling(252, min_periods=63).sum()
    dn = dv.where(ret < 0, 0.0).rolling(252, min_periods=63).sum()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# imbalance momentum: change in quarter DV up/down imbalance over a month
def f17dv_f17_dollar_volume_dynamics_imbalmom_63d_base_v125_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    ret = closeadj.pct_change()
    up = dv.where(ret > 0, 0.0).rolling(63, min_periods=21).sum()
    dn = dv.where(ret < 0, 0.0).rolling(63, min_periods=21).sum()
    imb = (up - dn) / (up + dn).replace(0, np.nan)
    b = imb - imb.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- RANGE / DEPTH (using high, low) ---

# market-depth level: log (dollar-volume / intraday-range) over a quarter
def f17dv_f17_dollar_volume_dynamics_depthlvl_63d_base_v126_signal(closeadj, volume, high, low):
    dv = _f17_dv(closeadj, volume)
    span = (high - low)
    depth = dv / span.replace(0, np.nan)
    b = np.log(depth.rolling(63, min_periods=21).mean().replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# depth z-score vs year (standardized capital-per-range extremity)
def f17dv_f17_dollar_volume_dynamics_depthz_252d_base_v127_signal(closeadj, volume, high, low):
    dv = _f17_dv(closeadj, volume)
    span = (high - low)
    depth = dv / span.replace(0, np.nan)
    ldepth = np.log(depth.replace(0, np.nan)).rolling(5, min_periods=2).mean()
    b = _z(ldepth, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-adjusted DV burst: today's depth over its 63d median (depth spike)
def f17dv_f17_dollar_volume_dynamics_depthspike_63d_base_v128_signal(closeadj, volume, high, low):
    dv = _f17_dv(closeadj, volume)
    span = (high - low)
    depth = dv / span.replace(0, np.nan)
    med = depth.rolling(63, min_periods=21).median()
    r = np.log(depth.replace(0, np.nan) / med.replace(0, np.nan))
    b = r.rolling(10, min_periods=4).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DV per fractional range (notional traded per 1% range) regime vs year
def f17dv_f17_dollar_volume_dynamics_dvperpct_252d_base_v129_signal(closeadj, volume, high, low):
    dv = _f17_dv(closeadj, volume)
    pctrng = (high - low) / closeadj.replace(0, np.nan)
    dpp = dv / pctrng.replace(0, np.nan)
    sm = np.log(dpp.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    med = np.log(dpp.replace(0, np.nan)).rolling(252, min_periods=63).median()
    b = sm - med
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# co-movement of dollar-volume with intraday range over a quarter (range-driven activity)
def f17dv_f17_dollar_volume_dynamics_dvrangecorr_63d_base_v130_signal(closeadj, volume, high, low):
    ldv = _f17_logdv(closeadj, volume)
    lrng = np.log((high - low).replace(0, np.nan))
    md = ldv.rolling(63, min_periods=21).mean()
    mr = lrng.rolling(63, min_periods=21).mean()
    cov = (ldv * lrng).rolling(63, min_periods=21).mean() - md * mr
    vd = ldv.rolling(63, min_periods=21).var()
    vr = lrng.rolling(63, min_periods=21).var()
    b = cov / (np.sqrt(vd * vr)).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- MISC FACETS / INTERACTIONS ---

# DV trend curvature: difference of quarter slope now vs a quarter ago (acceleration-as-level)
def f17dv_f17_dollar_volume_dynamics_trendcurv_63d_base_v131_signal(closeadj, volume):
    ldv = _f17_logdv(closeadj, volume)
    sl = _slope(ldv.rolling(5, min_periods=2).mean(), 63)
    b = sl - sl.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# year-over-year change in DV dispersion: is daily-activity turbulence rising vs a year ago
def f17dv_f17_dollar_volume_dynamics_dispyoy_252d_base_v132_signal(closeadj, volume):
    ldv = _f17_logdv(closeadj, volume)
    disp = ldv.diff().rolling(63, min_periods=21).std()
    b = disp - disp.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign-magnitude of regime distance: sqrt-scaled signed gap to year median (compressed tails)
def f17dv_f17_dollar_volume_dynamics_regsignmag_252d_base_v133_signal(closeadj, volume):
    ldv = _f17_logdv(closeadj, volume)
    lvl = ldv.rolling(21, min_periods=10).mean()
    med = ldv.rolling(252, min_periods=63).median()
    g = lvl - med
    b = np.sign(g) * (g.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# interaction: size-tier level times DV trend (big AND growing liquidity)
def f17dv_f17_dollar_volume_dynamics_sizegrow_base_v134_signal(closeadj, volume):
    lvl = _f17_size_tier(closeadj, volume, 63)
    lvlz = _z(lvl, 252)
    ldv = _f17_logdv(closeadj, volume)
    tr = _slope(ldv.rolling(5, min_periods=2).mean(), 63)
    b = lvlz * np.tanh(50.0 * tr)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion of monthly DV levels over a year (instability of the size tier)
def f17dv_f17_dollar_volume_dynamics_tierinstab_252d_base_v135_signal(closeadj, volume):
    lvl = _f17_size_tier(closeadj, volume, 21)
    b = _std(lvl, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DV variance ratio: var of 5d-summed DV vs 5x var of daily DV (clustering of activity)
def f17dv_f17_dollar_volume_dynamics_dvvr_63d_base_v136_signal(closeadj, volume):
    ldv = _f17_logdv(closeadj, volume)
    chg1 = ldv.diff()
    chg5 = ldv.diff(5)
    v1 = chg1.rolling(63, min_periods=21).var()
    v5 = chg5.rolling(63, min_periods=21).var()
    b = v5 / (5.0 * v1).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency ratio of log-DV path over a quarter (net drift vs total path of activity)
def f17dv_f17_dollar_volume_dynamics_dveff_63d_base_v137_signal(closeadj, volume):
    ldv = _f17_logdv(closeadj, volume).rolling(5, min_periods=2).mean()
    net = (ldv - ldv.shift(63)).abs()
    path = ldv.diff().abs().rolling(63, min_periods=21).sum()
    b = net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net up-vs-down magnitude of smoothed-DV daily changes over a quarter (signed trend pressure)
def f17dv_f17_dollar_volume_dynamics_risepress_63d_base_v138_signal(closeadj, volume):
    lvl = _f17_size_tier(closeadj, volume, 10)
    d = lvl.diff()
    up = d.where(d > 0, 0.0).rolling(63, min_periods=21).sum()
    dn = (-d.where(d < 0, 0.0)).rolling(63, min_periods=21).sum()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DV level relative to its own 252d EWMA, sqrt-sign compressed (durable displacement)
def f17dv_f17_dollar_volume_dynamics_emadisp_252d_base_v139_signal(closeadj, volume):
    ldv = _f17_logdv(closeadj, volume)
    disp = ldv.ewm(span=21, min_periods=10).mean() - ldv.ewm(span=252, min_periods=63).mean()
    b = np.sign(disp) * (disp.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# month-total DV vs the busiest 21d-total of the trailing year (distance below peak month)
def f17dv_f17_dollar_volume_dynamics_monthvspeak_base_v140_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    m21 = _rsum(dv, 21)
    peak = m21.rolling(252, min_periods=63).max()
    b = np.log(m21.replace(0, np.nan) / peak.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration of the dry-up: change in 126d DV drawdown over a quarter
def f17dv_f17_dollar_volume_dynamics_ddaccel_126d_base_v141_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    sm = dv.rolling(10, min_periods=4).mean()
    peak = sm.rolling(126, min_periods=42).max()
    dd = sm / peak.replace(0, np.nan) - 1.0
    b = dd - dd.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# thin-floor cushion: smoothed log-DV distance above its year 10th-percentile (liquidity floor lift)
def f17dv_f17_dollar_volume_dynamics_floorcushion_252d_base_v142_signal(closeadj, volume):
    ldv = _f17_logdv(closeadj, volume)
    lvl = ldv.rolling(21, min_periods=10).mean()
    q10 = ldv.rolling(252, min_periods=63).quantile(0.10)
    b = lvl - q10
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DV momentum consistency: mean weekly log-DV change divided by its dispersion (info-ratio of activity drift)
def f17dv_f17_dollar_volume_dynamics_momcons_63d_base_v143_signal(closeadj, volume):
    lvl = _f17_size_tier(closeadj, volume, 5)
    chg = lvl - lvl.shift(5)
    m = chg.rolling(63, min_periods=21).mean()
    sd = chg.rolling(63, min_periods=21).std()
    b = m / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DV toggling frequency: rate at which daily DV crosses its 21d median over a quarter (choppiness)
def f17dv_f17_dollar_volume_dynamics_dvtoggle_63d_base_v144_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    med = dv.rolling(21, min_periods=10).median()
    above = (dv > med).astype(float)
    cross = (above != above.shift(1)).astype(float)
    b = cross.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# two-year tier rank: where current smoothed DV sits in its two-year distribution
def f17dv_f17_dollar_volume_dynamics_tierrank_504d_base_v145_signal(closeadj, volume):
    lvl = _f17_size_tier(closeadj, volume, 10)
    b = lvl.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spike clustering at year scale: serial correlation of high-DV indicator over a year
def f17dv_f17_dollar_volume_dynamics_spikeclust_252d_base_v146_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    med = dv.rolling(252, min_periods=63).median()
    ind = (dv > 1.5 * med).astype(float)
    pair = ind * ind.shift(1)
    b = pair.rolling(252, min_periods=63).mean() - ind.rolling(252, min_periods=63).mean() ** 2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DV recovery breadth: fraction of quarter spent within 80% of the year DV peak
def f17dv_f17_dollar_volume_dynamics_nearpeakfrac_252d_base_v147_signal(closeadj, volume):
    dv = _f17_dv(closeadj, volume)
    sm = dv.rolling(10, min_periods=4).mean()
    peak = sm.rolling(252, min_periods=63).max()
    near = (sm >= 0.8 * peak).astype(float)
    deep = (sm / peak.replace(0, np.nan)).clip(0, 1)
    b = near.rolling(63, min_periods=21).mean() + 0.5 * deep
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-weighted DV concentration: top-day share where DV weighted by intraday range
def f17dv_f17_dollar_volume_dynamics_rwconc_63d_base_v148_signal(closeadj, volume, high, low):
    rng = (high - low) / low.replace(0, np.nan)
    rdv = (closeadj * volume) * rng
    mx = rdv.rolling(63, min_periods=21).max()
    tot = _rsum(rdv, 63)
    b = mx / tot.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration of size migration: tier-step now vs tier-step a quarter ago
def f17dv_f17_dollar_volume_dynamics_migaccel_base_v149_signal(closeadj, volume):
    lvl = _f17_size_tier(closeadj, volume, 21)
    base = _f17_size_tier(closeadj, volume, 252)
    step = lvl - base
    b = step - step.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite liquidity health: blend of year-rank, dry-up depth, and rising-fraction
def f17dv_f17_dollar_volume_dynamics_liqhealth_252d_base_v150_signal(closeadj, volume):
    ldv = _f17_logdv(closeadj, volume)
    lvl = ldv.rolling(21, min_periods=10).mean()
    rnk = lvl.rolling(252, min_periods=63).rank(pct=True) - 0.5
    dv = _f17_dv(closeadj, volume)
    sm = dv.rolling(10, min_periods=4).mean()
    peak = sm.rolling(252, min_periods=63).max()
    dd = sm / peak.replace(0, np.nan) - 1.0
    b = rnk + 0.5 * dd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f17dv_f17_dollar_volume_dynamics_logdvlvl_126d_base_v076_signal,
    f17dv_f17_dollar_volume_dynamics_logdvlvl_504d_base_v077_signal,
    f17dv_f17_dollar_volume_dynamics_emadv_fast_base_v078_signal,
    f17dv_f17_dollar_volume_dynamics_wkdvz_5v63_base_v079_signal,
    f17dv_f17_dollar_volume_dynamics_dvtotgrow_63d_base_v080_signal,
    f17dv_f17_dollar_volume_dynamics_dvmacd_base_v081_signal,
    f17dv_f17_dollar_volume_dynamics_dvtrend_252d_base_v082_signal,
    f17dv_f17_dollar_volume_dynamics_dvstep_21d_base_v083_signal,
    f17dv_f17_dollar_volume_dynamics_dvexp_5v21_base_v084_signal,
    f17dv_f17_dollar_volume_dynamics_dvexpconv_base_v085_signal,
    f17dv_f17_dollar_volume_dynamics_logdvz_126d_base_v086_signal,
    f17dv_f17_dollar_volume_dynamics_robz_252d_base_v087_signal,
    f17dv_f17_dollar_volume_dynamics_dvrank_126d_base_v088_signal,
    f17dv_f17_dollar_volume_dynamics_totz_63v252_base_v089_signal,
    f17dv_f17_dollar_volume_dynamics_wkrank_504d_base_v090_signal,
    f17dv_f17_dollar_volume_dynamics_regdist_504d_base_v091_signal,
    f17dv_f17_dollar_volume_dynamics_elevstale_63d_base_v092_signal,
    f17dv_f17_dollar_volume_dynamics_regstreak_126d_base_v093_signal,
    f17dv_f17_dollar_volume_dynamics_lowtoggle_252d_base_v094_signal,
    f17dv_f17_dollar_volume_dynamics_regspan_252d_base_v095_signal,
    f17dv_f17_dollar_volume_dynamics_tierstep_126d_base_v096_signal,
    f17dv_f17_dollar_volume_dynamics_tierpos_504d_base_v097_signal,
    f17dv_f17_dollar_volume_dynamics_tierfloor_504d_base_v098_signal,
    f17dv_f17_dollar_volume_dynamics_tierwidth_504d_base_v099_signal,
    f17dv_f17_dollar_volume_dynamics_tieryoy_252d_base_v100_signal,
    f17dv_f17_dollar_volume_dynamics_dvdd_126d_base_v101_signal,
    f17dv_f17_dollar_volume_dynamics_dvdd_504d_base_v102_signal,
    f17dv_f17_dollar_volume_dynamics_dvpain_252d_base_v103_signal,
    f17dv_f17_dollar_volume_dynamics_dsdvpeak_504d_base_v104_signal,
    f17dv_f17_dollar_volume_dynamics_ddretrace_252d_base_v105_signal,
    f17dv_f17_dollar_volume_dynamics_spikemag_252d_base_v106_signal,
    f17dv_f17_dollar_volume_dynamics_extspike_63d_base_v107_signal,
    f17dv_f17_dollar_volume_dynamics_spikeasym_63d_base_v108_signal,
    f17dv_f17_dollar_volume_dynamics_spikefollow_21d_base_v109_signal,
    f17dv_f17_dollar_volume_dynamics_surprisemag_21d_base_v110_signal,
    f17dv_f17_dollar_volume_dynamics_dvconc_126d_base_v111_signal,
    f17dv_f17_dollar_volume_dynamics_dvhhi_252d_base_v112_signal,
    f17dv_f17_dollar_volume_dynamics_top3share_63d_base_v113_signal,
    f17dv_f17_dollar_volume_dynamics_effdays_63d_base_v114_signal,
    f17dv_f17_dollar_volume_dynamics_dvtilt_63d_base_v115_signal,
    f17dv_f17_dollar_volume_dynamics_dvturb_21d_base_v116_signal,
    f17dv_f17_dollar_volume_dynamics_turbratio_base_v117_signal,
    f17dv_f17_dollar_volume_dynamics_tailspread_63d_base_v118_signal,
    f17dv_f17_dollar_volume_dynamics_tailskew_252d_base_v119_signal,
    f17dv_f17_dollar_volume_dynamics_dvkurt_63d_base_v120_signal,
    f17dv_f17_dollar_volume_dynamics_updvshare_21d_base_v121_signal,
    f17dv_f17_dollar_volume_dynamics_signedflow_63d_base_v122_signal,
    f17dv_f17_dollar_volume_dynamics_flowtilt_63d_base_v123_signal,
    f17dv_f17_dollar_volume_dynamics_dvimbal_252d_base_v124_signal,
    f17dv_f17_dollar_volume_dynamics_imbalmom_63d_base_v125_signal,
    f17dv_f17_dollar_volume_dynamics_depthlvl_63d_base_v126_signal,
    f17dv_f17_dollar_volume_dynamics_depthz_252d_base_v127_signal,
    f17dv_f17_dollar_volume_dynamics_depthspike_63d_base_v128_signal,
    f17dv_f17_dollar_volume_dynamics_dvperpct_252d_base_v129_signal,
    f17dv_f17_dollar_volume_dynamics_dvrangecorr_63d_base_v130_signal,
    f17dv_f17_dollar_volume_dynamics_trendcurv_63d_base_v131_signal,
    f17dv_f17_dollar_volume_dynamics_dispyoy_252d_base_v132_signal,
    f17dv_f17_dollar_volume_dynamics_regsignmag_252d_base_v133_signal,
    f17dv_f17_dollar_volume_dynamics_sizegrow_base_v134_signal,
    f17dv_f17_dollar_volume_dynamics_tierinstab_252d_base_v135_signal,
    f17dv_f17_dollar_volume_dynamics_dvvr_63d_base_v136_signal,
    f17dv_f17_dollar_volume_dynamics_dveff_63d_base_v137_signal,
    f17dv_f17_dollar_volume_dynamics_risepress_63d_base_v138_signal,
    f17dv_f17_dollar_volume_dynamics_emadisp_252d_base_v139_signal,
    f17dv_f17_dollar_volume_dynamics_monthvspeak_base_v140_signal,
    f17dv_f17_dollar_volume_dynamics_ddaccel_126d_base_v141_signal,
    f17dv_f17_dollar_volume_dynamics_floorcushion_252d_base_v142_signal,
    f17dv_f17_dollar_volume_dynamics_momcons_63d_base_v143_signal,
    f17dv_f17_dollar_volume_dynamics_dvtoggle_63d_base_v144_signal,
    f17dv_f17_dollar_volume_dynamics_tierrank_504d_base_v145_signal,
    f17dv_f17_dollar_volume_dynamics_spikeclust_252d_base_v146_signal,
    f17dv_f17_dollar_volume_dynamics_nearpeakfrac_252d_base_v147_signal,
    f17dv_f17_dollar_volume_dynamics_rwconc_63d_base_v148_signal,
    f17dv_f17_dollar_volume_dynamics_migaccel_base_v149_signal,
    f17dv_f17_dollar_volume_dynamics_liqhealth_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F17_DOLLAR_VOLUME_DYNAMICS_REGISTRY_076_150 = REGISTRY


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

    print("OK f17_dollar_volume_dynamics_base_076_150_claude: %d features pass" % n_features)
