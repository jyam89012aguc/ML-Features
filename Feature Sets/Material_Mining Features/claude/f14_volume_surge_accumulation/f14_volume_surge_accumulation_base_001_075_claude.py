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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


# ===== folder domain primitives (volume surge / accumulation) =====
def _f14_vol_z(volume, w):
    # log-volume z-score: spike detector robust to junior thin/spiky volume
    lv = np.log(volume.clip(lower=1.0))
    return _z(lv, w)


def _f14_surge_ratio(volume, w_long):
    # current volume vs its trailing long-window average (surge ratio)
    avg = volume.rolling(w_long, min_periods=max(5, w_long // 2)).mean()
    return volume / avg.replace(0, np.nan)


def _f14_dollar_vol(closeadj, volume):
    # dollar-volume; closeadj used because it's a >21d notional level
    return (closeadj * volume).clip(lower=0.0)


def _f14_updown_vol(closeadj, volume, w):
    # up-volume vs down-volume ratio over window (accumulation pressure)
    ret = closeadj.pct_change()
    up = volume.where(ret > 0, 0.0)
    dn = volume.where(ret < 0, 0.0)
    ups = up.rolling(w, min_periods=max(3, w // 2)).sum()
    dns = dn.rolling(w, min_periods=max(3, w // 2)).sum()
    return ups / (ups + dns).replace(0, np.nan)


def _f14_herfindahl(volume, w):
    # volume concentration: Herfindahl of volume shares within the window
    tot = volume.rolling(w, min_periods=max(3, w // 2)).sum()
    sq = (volume * volume).rolling(w, min_periods=max(3, w // 2)).sum()
    return sq / (tot * tot).replace(0, np.nan)


def _f14_surge_count(volume, w_base, w_count, mult):
    # count of surge days (volume > mult * trailing base avg) within w_count
    avg = volume.rolling(w_base, min_periods=max(5, w_base // 2)).mean()
    surge = (volume > mult * avg).astype(float)
    return surge.rolling(w_count, min_periods=max(3, w_count // 2)).sum()


# ============================================================
# raw log-volume z-score over 63d (surge detector)
def f14vs_f14_volume_surge_accumulation_volz_63d_base_v001_signal(volume):
    b = _f14_vol_z(volume, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed-volume z: 21d-mean log-volume z-scored over 126d (sustained elevation, not single spikes)
def f14vs_f14_volume_surge_accumulation_volz_126d_base_v002_signal(volume):
    lv = np.log(volume.clip(lower=1.0)).rolling(21, min_periods=10).mean()
    b = _z(lv, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# annual elevation: 63d-mean volume percentile-ranked vs its 252d distribution (sustained-high regime)
def f14vs_f14_volume_surge_accumulation_volz_252d_base_v003_signal(volume):
    sm = volume.rolling(63, min_periods=21).mean()
    b = sm.rolling(252, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge ratio: today's volume vs trailing 63d average
def f14vs_f14_volume_surge_accumulation_surge_63d_base_v004_signal(volume):
    b = _f14_surge_ratio(volume, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge ratio: 5d average volume vs 63d average (short surge vs base)
def f14vs_f14_volume_surge_accumulation_surge_5v63_base_v005_signal(volume):
    short = volume.rolling(5, min_periods=3).mean()
    long = volume.rolling(63, min_periods=21).mean()
    b = short / long.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge ratio: 21d average vs 126d average (monthly surge vs half-year base)
def f14vs_f14_volume_surge_accumulation_surge_21v126_base_v006_signal(volume):
    short = volume.rolling(21, min_periods=10).mean()
    long = volume.rolling(126, min_periods=63).mean()
    b = short / long.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# annual surge skew: 21d mean-volume vs 252d median-volume (sustained elevation vs typical)
def f14vs_f14_volume_surge_accumulation_surge_252d_base_v007_signal(volume):
    short = volume.rolling(21, min_periods=10).mean()
    med = volume.rolling(252, min_periods=126).median()
    b = np.log(short.replace(0, np.nan) / med.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up/down volume ratio over 21d (accumulation pressure, monthly)
def f14vs_f14_volume_surge_accumulation_updn_21d_base_v008_signal(closeadj, volume):
    b = _f14_updown_vol(closeadj, volume, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up/down volume ratio over 63d (accumulation pressure, quarterly)
def f14vs_f14_volume_surge_accumulation_updn_63d_base_v009_signal(closeadj, volume):
    b = _f14_updown_vol(closeadj, volume, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up/down volume ratio over 126d (accumulation pressure, half-year)
def f14vs_f14_volume_surge_accumulation_updn_126d_base_v010_signal(closeadj, volume):
    b = _f14_updown_vol(closeadj, volume, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume trend: log-slope of 21d dollar-volume over a quarter
def f14vs_f14_volume_surge_accumulation_dvtrend_63d_base_v011_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume).rolling(21, min_periods=10).mean()
    b = np.log(dv.replace(0, np.nan) / dv.shift(63).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume trend over a half-year
def f14vs_f14_volume_surge_accumulation_dvtrend_126d_base_v012_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume).rolling(21, min_periods=10).mean()
    b = np.log(dv.replace(0, np.nan) / dv.shift(126).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume z-score over 126d (log dollar-vol level extremity)
def f14vs_f14_volume_surge_accumulation_dvz_126d_base_v013_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    b = _z(np.log(dv.clip(lower=1.0)), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation-on-news: volume z weighted by signed return (smart-money on moves)
def f14vs_f14_volume_surge_accumulation_accnews_63d_base_v014_signal(closeadj, volume):
    vz = _f14_vol_z(volume, 63)
    ret = closeadj.pct_change()
    signed = np.sign(ret) * vz.clip(lower=0)
    b = signed.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume concentration / Herfindahl over 63d (lumpiness of volume)
def f14vs_f14_volume_surge_accumulation_herf_63d_base_v015_signal(volume):
    b = _f14_herfindahl(volume, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume concentration / Herfindahl over 126d
def f14vs_f14_volume_surge_accumulation_herf_126d_base_v016_signal(volume):
    b = _f14_herfindahl(volume, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of surge days (>2x of 63d avg) within 63d, plus surge-depth magnitude
def f14vs_f14_volume_surge_accumulation_scount_63d_base_v017_signal(volume):
    avg = volume.rolling(63, min_periods=21).mean()
    ratio = volume / avg.replace(0, np.nan)
    cnt = (ratio > 2.0).astype(float).rolling(63, min_periods=21).sum()
    depth = (ratio - 2.0).clip(lower=0).rolling(63, min_periods=21).mean()
    b = cnt + depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of surge days (>2x of 63d avg) within trailing 126d, depth-weighted
def f14vs_f14_volume_surge_accumulation_scount_126d_base_v018_signal(volume):
    avg = volume.rolling(63, min_periods=21).mean()
    ratio = volume / avg.replace(0, np.nan)
    cnt = (ratio > 2.0).astype(float).rolling(126, min_periods=63).sum()
    depth = (ratio - 2.0).clip(lower=0).rolling(126, min_periods=63).mean()
    b = cnt + 2.0 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# big-surge frequency over 252d: count above 90th-pctile of own 252d volume, magnitude-weighted
def f14vs_f14_volume_surge_accumulation_scount_252d_base_v019_signal(volume):
    thr = volume.rolling(252, min_periods=126).quantile(0.90)
    avg = volume.rolling(126, min_periods=63).mean()
    ratio = volume / avg.replace(0, np.nan)
    cnt = (volume > thr).astype(float).rolling(252, min_periods=126).sum()
    depth = (ratio - 1.0).clip(lower=0).where(volume > thr, 0.0).rolling(252, min_periods=126).sum()
    b = cnt + depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# elevated-volume regime over 63d: fraction above 63d median, tilted by mean overshoot
def f14vs_f14_volume_surge_accumulation_elevfrac_63d_base_v020_signal(volume):
    med = volume.rolling(63, min_periods=21).median()
    above = (volume > med).astype(float)
    frac = above.rolling(63, min_periods=21).mean()
    overshoot = (volume / med.replace(0, np.nan) - 1.0).rolling(63, min_periods=21).mean()
    b = frac + 0.5 * overshoot
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed-volume percentile rank: 21d-mean volume ranked vs its own 252d history
def f14vs_f14_volume_surge_accumulation_surgerank_252d_base_v021_signal(volume):
    sm = volume.rolling(21, min_periods=10).mean()
    b = _rank(sm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume term-structure: 5d log-vol std vs 63d log-vol std (short vs long spikiness)
def f14vs_f14_volume_surge_accumulation_volzdisp_63d_base_v022_signal(volume):
    lv = np.log(volume.clip(lower=1.0))
    short = lv.rolling(5, min_periods=3).std()
    long = lv.rolling(63, min_periods=21).std()
    b = short / long.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up-volume share minus 0.5, smoothed (net accumulation bias)
def f14vs_f14_volume_surge_accumulation_accbias_63d_base_v023_signal(closeadj, volume):
    ud = _f14_updown_vol(closeadj, volume, 63)
    b = (ud - 0.5).ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume surge: 5d dollar-vol vs 63d dollar-vol average
def f14vs_f14_volume_surge_accumulation_dvsurge_5v63_base_v024_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    short = dv.rolling(5, min_periods=3).mean()
    long = dv.rolling(63, min_periods=21).mean()
    b = short / long.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume vol-of-vol: std of log-volume over 63d (spikiness regime)
def f14vs_f14_volume_surge_accumulation_volvov_63d_base_v025_signal(volume):
    lv = np.log(volume.clip(lower=1.0))
    b = lv.rolling(63, min_periods=21).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in volume vol-of-vol over a quarter (spikiness expanding/contracting)
def f14vs_f14_volume_surge_accumulation_volvovchg_63d_base_v026_signal(volume):
    lv = np.log(volume.clip(lower=1.0))
    vov = lv.rolling(63, min_periods=21).std()
    b = vov - vov.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# max single-day volume share within trailing 63d (peak concentration)
def f14vs_f14_volume_surge_accumulation_maxshare_63d_base_v027_signal(volume):
    tot = volume.rolling(63, min_periods=21).sum()
    mx = volume.rolling(63, min_periods=21).max()
    b = mx / tot.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation on big-move days: correlation of |ret| and volume over 126d (news-volume coupling)
def f14vs_f14_volume_surge_accumulation_accnews_126d_base_v028_signal(closeadj, volume):
    aret = closeadj.pct_change().abs()
    lv = np.log(volume.clip(lower=1.0))
    mr = aret.rolling(126, min_periods=63).mean()
    mv = lv.rolling(126, min_periods=63).mean()
    cov = (aret * lv).rolling(126, min_periods=63).mean() - mr * mv
    sr = aret.rolling(126, min_periods=63).std()
    sv = lv.rolling(126, min_periods=63).std()
    b = cov / (sr * sv).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge persistence: 5d-summed positive log-surge vs 63d base (clustered elevation)
def f14vs_f14_volume_surge_accumulation_surgelog_63d_base_v029_signal(volume):
    avg = volume.rolling(63, min_periods=21).mean()
    ls = np.log(volume.clip(lower=1.0) / avg.replace(0, np.nan))
    b = ls.clip(lower=0).rolling(5, min_periods=3).sum() - ls.clip(upper=0).abs().rolling(5, min_periods=3).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dry-up days (volume < 0.5x of 63d avg) within 63d, plus shortfall depth
def f14vs_f14_volume_surge_accumulation_drycount_63d_base_v030_signal(volume):
    avg = volume.rolling(63, min_periods=21).mean()
    ratio = volume / avg.replace(0, np.nan)
    cnt = (ratio < 0.5).astype(float).rolling(63, min_periods=21).sum()
    depth = (0.5 - ratio).clip(lower=0).rolling(63, min_periods=21).mean()
    b = cnt + 20.0 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net surge-minus-dry activity over 126d (depth-weighted activity balance)
def f14vs_f14_volume_surge_accumulation_netactiv_126d_base_v031_signal(volume):
    avg = volume.rolling(63, min_periods=21).mean()
    ratio = volume / avg.replace(0, np.nan)
    surge = (ratio > 2.0).astype(float).rolling(126, min_periods=63).sum()
    dry = (ratio < 0.5).astype(float).rolling(126, min_periods=63).sum()
    tilt = (ratio - 1.0).clip(-1.0, 3.0).rolling(126, min_periods=63).mean()
    b = (surge - dry) + 5.0 * tilt
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume drawdown: current 21d dollar-vol vs its 252d peak (liquidity fade)
def f14vs_f14_volume_surge_accumulation_dvdd_252d_base_v032_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume).rolling(21, min_periods=10).mean()
    peak = dv.rolling(252, min_periods=126).max()
    b = dv / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-flow trend: change in 21d-summed signed dollar-volume over a quarter (accel of accumulation)
def f14vs_f14_volume_surge_accumulation_dvupdn_63d_base_v033_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f14_dollar_vol(closeadj, volume)
    flow = (np.sign(ret) * dv).rolling(21, min_periods=10).sum()
    base = dv.rolling(63, min_periods=21).mean() * 21.0
    norm = flow / base.replace(0, np.nan)
    b = norm - norm.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume trend: log-slope of 5d volume average over a month
def f14vs_f14_volume_surge_accumulation_voltrend_21d_base_v034_signal(volume):
    va = volume.rolling(5, min_periods=3).mean()
    b = np.log(va.replace(0, np.nan) / va.shift(21).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume trend: log-slope of 21d volume average over a quarter
def f14vs_f14_volume_surge_accumulation_voltrend_63d_base_v035_signal(volume):
    va = volume.rolling(21, min_periods=10).mean()
    b = np.log(va.replace(0, np.nan) / va.shift(63).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Herfindahl change over a quarter (concentration building/dispersing)
def f14vs_f14_volume_surge_accumulation_herfchg_63d_base_v036_signal(volume):
    h = _f14_herfindahl(volume, 63)
    b = h - h.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# proximity to recent peak volume: today's volume vs trailing 63d max (near-record activity)
def f14vs_f14_volume_surge_accumulation_surgez_126d_base_v037_signal(volume):
    mx = volume.rolling(63, min_periods=21).max()
    b = volume / mx.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation streak: up-and-heavy day count over 21d, weighted by heaviness
def f14vs_f14_volume_surge_accumulation_accstreak_21d_base_v038_signal(closeadj, volume):
    ret = closeadj.pct_change()
    med = volume.rolling(21, min_periods=10).median()
    heavy = (volume / med.replace(0, np.nan)).where(ret > 0, 0.0)
    b = heavy.rolling(21, min_periods=10).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume spike recency: time since last >3x surge, normalized over 63d
def f14vs_f14_volume_surge_accumulation_spikerecency_63d_base_v039_signal(volume):
    avg = volume.rolling(63, min_periods=21).mean()
    surge = (volume > 3.0 * avg).astype(float)

    def _last(a):
        idx = np.where(a > 0)[0]
        if len(idx) == 0:
            return 1.0
        return (len(a) - 1 - idx[-1]) / float(len(a))
    b = surge.rolling(63, min_periods=21).apply(_last, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume z relative to volume z (price-amplified surge vs raw surge)
def f14vs_f14_volume_surge_accumulation_dvampl_63d_base_v040_signal(closeadj, volume):
    dvz = _z(np.log(_f14_dollar_vol(closeadj, volume).clip(lower=1.0)), 63)
    vz = _f14_vol_z(volume, 63)
    b = dvz - vz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# top-quartile activity over 63d: fraction above 252d Q3, tilted by overshoot depth
def f14vs_f14_volume_surge_accumulation_topqfrac_63d_base_v041_signal(volume):
    q3 = volume.rolling(252, min_periods=63).quantile(0.75)
    above = (volume > q3).astype(float)
    frac = above.rolling(63, min_periods=21).mean()
    overshoot = (volume / q3.replace(0, np.nan) - 1.0).clip(lower=0).rolling(63, min_periods=21).mean()
    b = frac + overshoot
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume surge ratio short vs long spread (5v63 minus 21v126)
def f14vs_f14_volume_surge_accumulation_surgespr_base_v042_signal(volume):
    a = volume.rolling(5, min_periods=3).mean() / volume.rolling(63, min_periods=21).mean().replace(0, np.nan)
    c = volume.rolling(21, min_periods=10).mean() / volume.rolling(126, min_periods=63).mean().replace(0, np.nan)
    b = a - c
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation/distribution proxy: signed-return-weighted volume sum normalized (63d)
def f14vs_f14_volume_surge_accumulation_addist_63d_base_v043_signal(closeadj, volume):
    ret = closeadj.pct_change()
    signed = ret.clip(-0.5, 0.5) * volume
    s = signed.rolling(63, min_periods=21).sum()
    t = volume.rolling(63, min_periods=21).sum()
    b = s / t.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume skewness over 63d (spike-tilted distribution detector)
def f14vs_f14_volume_surge_accumulation_volskew_63d_base_v044_signal(volume):
    lv = np.log(volume.clip(lower=1.0))
    b = lv.rolling(63, min_periods=21).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume kurtosis over 126d (fat-tail spike regime)
def f14vs_f14_volume_surge_accumulation_volkurt_126d_base_v045_signal(volume):
    lv = np.log(volume.clip(lower=1.0))
    b = lv.rolling(126, min_periods=63).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# largest 5-day cluster volume share within 63d (burst clustering)
def f14vs_f14_volume_surge_accumulation_burst_63d_base_v046_signal(volume):
    five = volume.rolling(5, min_periods=3).sum()
    mx5 = five.rolling(63, min_periods=21).max()
    tot = volume.rolling(63, min_periods=21).sum()
    b = mx5 / tot.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume trend ranked vs 252d history (relative liquidity momentum)
def f14vs_f14_volume_surge_accumulation_dvtrendrank_base_v047_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume).rolling(21, min_periods=10).mean()
    tr = np.log(dv.replace(0, np.nan) / dv.shift(63).replace(0, np.nan))
    b = _rank(tr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation term-spread: 21d up/down volume share minus 126d up/down share (short vs long pressure)
def f14vs_f14_volume_surge_accumulation_accmom_63d_base_v048_signal(closeadj, volume):
    short = _f14_updown_vol(closeadj, volume, 21)
    long = _f14_updown_vol(closeadj, volume, 126)
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume regime shift: 63d mean log-vol vs 252d mean log-vol (regime up/down trend)
def f14vs_f14_volume_surge_accumulation_regdist_252d_base_v049_signal(volume):
    lv = np.log(volume.clip(lower=1.0))
    short = lv.rolling(63, min_periods=21).mean()
    long = lv.rolling(252, min_periods=126).mean()
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge intensity: average excess over 2x threshold among surge days (63d)
def f14vs_f14_volume_surge_accumulation_surgeint_63d_base_v050_signal(volume):
    avg = volume.rolling(63, min_periods=21).mean()
    ratio = volume / avg.replace(0, np.nan)
    excess = (ratio - 2.0).clip(lower=0)
    b = excess.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net dollar-flow sign-magnitude: signed sqrt of accumulation balance (63d)
def f14vs_f14_volume_surge_accumulation_dvflowsm_63d_base_v051_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f14_dollar_vol(closeadj, volume)
    up = dv.where(ret > 0, 0.0).rolling(63, min_periods=21).sum()
    dn = dv.where(ret < 0, 0.0).rolling(63, min_periods=21).sum()
    bal = (up - dn) / (up + dn).replace(0, np.nan)
    b = np.sign(bal) * (bal.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume tail-spread: 90th vs 50th percentile volume ratio over 63d (upper-tail heaviness)
def f14vs_f14_volume_surge_accumulation_voldisp_63d_base_v052_signal(volume):
    p90 = volume.rolling(63, min_periods=21).quantile(0.90)
    p50 = volume.rolling(63, min_periods=21).quantile(0.50)
    b = p90 / p50.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# z-magnitude-weighted surge count over 126d (intensity-weighted tally)
def f14vs_f14_volume_surge_accumulation_wscount_126d_base_v053_signal(volume):
    vz = _f14_vol_z(volume, 63)
    w = vz.clip(lower=0)
    b = w.rolling(126, min_periods=63).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed volume surge (bounded spike intensity)
def f14vs_f14_volume_surge_accumulation_surgetanh_63d_base_v054_signal(volume):
    vz = _f14_vol_z(volume, 63)
    b = np.tanh(0.7 * vz)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume acceleration: 63d trend minus 126d trend
def f14vs_f14_volume_surge_accumulation_dvaccel_base_v055_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume).rolling(21, min_periods=10).mean()
    t63 = np.log(dv.replace(0, np.nan) / dv.shift(63).replace(0, np.nan))
    t126 = np.log(dv.replace(0, np.nan) / dv.shift(126).replace(0, np.nan)) / 2.0
    b = t63 - t126
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up-and-surge over 126d, weighted by surge-volume excess (informed buying)
def f14vs_f14_volume_surge_accumulation_upsurge_126d_base_v056_signal(closeadj, volume):
    ret = closeadj.pct_change()
    avg = volume.rolling(63, min_periods=21).mean()
    excess = (volume / avg.replace(0, np.nan) - 1.5).clip(lower=0)
    wgt = excess.where(ret > 0, 0.0)
    b = wgt.rolling(126, min_periods=63).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# down-and-surge over 126d, weighted by surge-volume excess (informed selling)
def f14vs_f14_volume_surge_accumulation_dnsurge_126d_base_v057_signal(closeadj, volume):
    ret = closeadj.pct_change()
    avg = volume.rolling(63, min_periods=21).mean()
    excess = (volume / avg.replace(0, np.nan) - 1.5).clip(lower=0)
    wgt = excess.where(ret < 0, 0.0)
    b = wgt.rolling(126, min_periods=63).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge-day directional bias over 126d (up-surge minus down-surge, excess-weighted)
def f14vs_f14_volume_surge_accumulation_surgebias_126d_base_v058_signal(closeadj, volume):
    ret = closeadj.pct_change()
    avg = volume.rolling(63, min_periods=21).mean()
    excess = (volume / avg.replace(0, np.nan) - 1.5).clip(lower=0)
    up = excess.where(ret > 0, 0.0)
    dn = excess.where(ret < 0, 0.0)
    b = (up - dn).rolling(126, min_periods=63).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume consistency: signed 21d fraction above 63d avg, tilted by mean ratio
def f14vs_f14_volume_surge_accumulation_volcons_21d_base_v059_signal(volume):
    avg = volume.rolling(63, min_periods=21).mean()
    above = (volume > avg).astype(float)
    frac = above.rolling(21, min_periods=10).mean()
    tilt = (volume / avg.replace(0, np.nan) - 1.0).rolling(21, min_periods=10).mean()
    b = (2.0 * frac - 1.0) + tilt
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log dollar-volume slope over 252d (annual liquidity growth)
def f14vs_f14_volume_surge_accumulation_dvtrend_252d_base_v060_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume).rolling(21, min_periods=10).mean()
    b = np.log(dv.replace(0, np.nan) / dv.shift(252).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume range compression: (max-min)/mean of log-volume over 63d
def f14vs_f14_volume_surge_accumulation_volrange_63d_base_v061_signal(volume):
    lv = np.log(volume.clip(lower=1.0))
    rng = lv.rolling(63, min_periods=21).max() - lv.rolling(63, min_periods=21).min()
    mn = lv.rolling(63, min_periods=21).mean()
    b = rng / mn.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation-news interaction: signed return x excess surge ratio, 21d sum
def f14vs_f14_volume_surge_accumulation_newsint_21d_base_v062_signal(closeadj, volume):
    ret = closeadj.pct_change()
    sr = _f14_surge_ratio(volume, 63)
    inter = ret * (sr - 1.0)
    b = inter.rolling(21, min_periods=10).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# concentration of dollar-volume (Herfindahl on dollar-vol) over 63d
def f14vs_f14_volume_surge_accumulation_dvherf_63d_base_v063_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    b = _f14_herfindahl(dv, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume z change over a week (impulse onset / spike acceleration)
def f14vs_f14_volume_surge_accumulation_volzimp_5d_base_v064_signal(volume):
    vz = _f14_vol_z(volume, 63)
    b = vz - vz.shift(5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# extreme upper-tail mass over 252d: summed positive z-excess above 1 (spike severity)
def f14vs_f14_volume_surge_accumulation_extspike_252d_base_v065_signal(volume):
    vz = _f14_vol_z(volume, 126)
    cnt = (vz > 1.0).astype(float).rolling(252, min_periods=126).sum()
    mag = (vz - 1.0).clip(lower=0).rolling(252, min_periods=126).sum()
    b = cnt + mag
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# proportion of total quarterly volume on the single biggest up-day (63d)
def f14vs_f14_volume_surge_accumulation_bigupday_63d_base_v066_signal(closeadj, volume):
    ret = closeadj.pct_change()
    upvol = volume.where(ret > 0, 0.0)
    mx = upvol.rolling(63, min_periods=21).max()
    tot = volume.rolling(63, min_periods=21).sum()
    b = mx / tot.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume autocorrelation lag-1 over 63d (persistent vs spiky activity)
def f14vs_f14_volume_surge_accumulation_volac1_63d_base_v067_signal(volume):
    lv = np.log(volume.clip(lower=1.0))
    b = lv.rolling(63, min_periods=21).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=False)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume surge percentile vs 252d (relative liquidity spike)
def f14vs_f14_volume_surge_accumulation_dvsurgerank_base_v068_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    sr = dv / dv.rolling(63, min_periods=21).mean().replace(0, np.nan)
    b = _rank(sr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation balance smoothed and z-scored (persistent net buying extremity)
def f14vs_f14_volume_surge_accumulation_accbalz_126d_base_v069_signal(closeadj, volume):
    ud = _f14_updown_vol(closeadj, volume, 21)
    sm = ud.ewm(span=21, min_periods=10).mean()
    b = _z(sm, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spike fade: distance of today's volume below the trailing 21d peak volume (post-spike cooldown)
def f14vs_f14_volume_surge_accumulation_surgefade_63d_base_v070_signal(volume):
    pk = volume.rolling(21, min_periods=10).max()
    b = np.log(volume.clip(lower=1.0) / pk.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-activity regime over 126d: fraction above 126d median, tilted by overshoot
def f14vs_f14_volume_surge_accumulation_dvelevfrac_126d_base_v071_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    med = dv.rolling(126, min_periods=63).median()
    above = (dv > med).astype(float)
    frac = above.rolling(126, min_periods=63).mean()
    overshoot = (dv / med.replace(0, np.nan) - 1.0).rolling(126, min_periods=63).mean()
    b = frac + 0.3 * overshoot
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net signed-volume accumulation index over 252d (cumulative net buying share)
def f14vs_f14_volume_surge_accumulation_accindex_252d_base_v072_signal(closeadj, volume):
    ret = closeadj.pct_change()
    signed = np.sign(ret) * volume
    cum = signed.rolling(252, min_periods=126).sum()
    tot = volume.rolling(252, min_periods=126).sum()
    b = cum / tot.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge clustering: recent vs prior 21d surge-excess (depth-weighted clustering)
def f14vs_f14_volume_surge_accumulation_surgeclust_base_v073_signal(volume):
    avg = volume.rolling(63, min_periods=21).mean()
    excess = (volume / avg.replace(0, np.nan) - 2.0).clip(lower=0)
    recent = excess.rolling(21, min_periods=10).sum()
    prior = excess.shift(21).rolling(21, min_periods=10).sum()
    b = recent - prior
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# event intensity: |ret| weighted by volume share, summed over 63d
def f14vs_f14_volume_surge_accumulation_eventint_63d_base_v074_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    w = volume / volume.rolling(63, min_periods=21).sum().replace(0, np.nan)
    b = (ret * w).rolling(63, min_periods=21).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume z minus 21d-lagged dollar-volume z (liquidity surge onset)
def f14vs_f14_volume_surge_accumulation_dvzonset_21d_base_v075_signal(closeadj, volume):
    dvz = _z(np.log(_f14_dollar_vol(closeadj, volume).clip(lower=1.0)), 126)
    b = dvz - dvz.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f14vs_f14_volume_surge_accumulation_volz_63d_base_v001_signal,
    f14vs_f14_volume_surge_accumulation_volz_126d_base_v002_signal,
    f14vs_f14_volume_surge_accumulation_volz_252d_base_v003_signal,
    f14vs_f14_volume_surge_accumulation_surge_63d_base_v004_signal,
    f14vs_f14_volume_surge_accumulation_surge_5v63_base_v005_signal,
    f14vs_f14_volume_surge_accumulation_surge_21v126_base_v006_signal,
    f14vs_f14_volume_surge_accumulation_surge_252d_base_v007_signal,
    f14vs_f14_volume_surge_accumulation_updn_21d_base_v008_signal,
    f14vs_f14_volume_surge_accumulation_updn_63d_base_v009_signal,
    f14vs_f14_volume_surge_accumulation_updn_126d_base_v010_signal,
    f14vs_f14_volume_surge_accumulation_dvtrend_63d_base_v011_signal,
    f14vs_f14_volume_surge_accumulation_dvtrend_126d_base_v012_signal,
    f14vs_f14_volume_surge_accumulation_dvz_126d_base_v013_signal,
    f14vs_f14_volume_surge_accumulation_accnews_63d_base_v014_signal,
    f14vs_f14_volume_surge_accumulation_herf_63d_base_v015_signal,
    f14vs_f14_volume_surge_accumulation_herf_126d_base_v016_signal,
    f14vs_f14_volume_surge_accumulation_scount_63d_base_v017_signal,
    f14vs_f14_volume_surge_accumulation_scount_126d_base_v018_signal,
    f14vs_f14_volume_surge_accumulation_scount_252d_base_v019_signal,
    f14vs_f14_volume_surge_accumulation_elevfrac_63d_base_v020_signal,
    f14vs_f14_volume_surge_accumulation_surgerank_252d_base_v021_signal,
    f14vs_f14_volume_surge_accumulation_volzdisp_63d_base_v022_signal,
    f14vs_f14_volume_surge_accumulation_accbias_63d_base_v023_signal,
    f14vs_f14_volume_surge_accumulation_dvsurge_5v63_base_v024_signal,
    f14vs_f14_volume_surge_accumulation_volvov_63d_base_v025_signal,
    f14vs_f14_volume_surge_accumulation_volvovchg_63d_base_v026_signal,
    f14vs_f14_volume_surge_accumulation_maxshare_63d_base_v027_signal,
    f14vs_f14_volume_surge_accumulation_accnews_126d_base_v028_signal,
    f14vs_f14_volume_surge_accumulation_surgelog_63d_base_v029_signal,
    f14vs_f14_volume_surge_accumulation_drycount_63d_base_v030_signal,
    f14vs_f14_volume_surge_accumulation_netactiv_126d_base_v031_signal,
    f14vs_f14_volume_surge_accumulation_dvdd_252d_base_v032_signal,
    f14vs_f14_volume_surge_accumulation_dvupdn_63d_base_v033_signal,
    f14vs_f14_volume_surge_accumulation_voltrend_21d_base_v034_signal,
    f14vs_f14_volume_surge_accumulation_voltrend_63d_base_v035_signal,
    f14vs_f14_volume_surge_accumulation_herfchg_63d_base_v036_signal,
    f14vs_f14_volume_surge_accumulation_surgez_126d_base_v037_signal,
    f14vs_f14_volume_surge_accumulation_accstreak_21d_base_v038_signal,
    f14vs_f14_volume_surge_accumulation_spikerecency_63d_base_v039_signal,
    f14vs_f14_volume_surge_accumulation_dvampl_63d_base_v040_signal,
    f14vs_f14_volume_surge_accumulation_topqfrac_63d_base_v041_signal,
    f14vs_f14_volume_surge_accumulation_surgespr_base_v042_signal,
    f14vs_f14_volume_surge_accumulation_addist_63d_base_v043_signal,
    f14vs_f14_volume_surge_accumulation_volskew_63d_base_v044_signal,
    f14vs_f14_volume_surge_accumulation_volkurt_126d_base_v045_signal,
    f14vs_f14_volume_surge_accumulation_burst_63d_base_v046_signal,
    f14vs_f14_volume_surge_accumulation_dvtrendrank_base_v047_signal,
    f14vs_f14_volume_surge_accumulation_accmom_63d_base_v048_signal,
    f14vs_f14_volume_surge_accumulation_regdist_252d_base_v049_signal,
    f14vs_f14_volume_surge_accumulation_surgeint_63d_base_v050_signal,
    f14vs_f14_volume_surge_accumulation_dvflowsm_63d_base_v051_signal,
    f14vs_f14_volume_surge_accumulation_voldisp_63d_base_v052_signal,
    f14vs_f14_volume_surge_accumulation_wscount_126d_base_v053_signal,
    f14vs_f14_volume_surge_accumulation_surgetanh_63d_base_v054_signal,
    f14vs_f14_volume_surge_accumulation_dvaccel_base_v055_signal,
    f14vs_f14_volume_surge_accumulation_upsurge_126d_base_v056_signal,
    f14vs_f14_volume_surge_accumulation_dnsurge_126d_base_v057_signal,
    f14vs_f14_volume_surge_accumulation_surgebias_126d_base_v058_signal,
    f14vs_f14_volume_surge_accumulation_volcons_21d_base_v059_signal,
    f14vs_f14_volume_surge_accumulation_dvtrend_252d_base_v060_signal,
    f14vs_f14_volume_surge_accumulation_volrange_63d_base_v061_signal,
    f14vs_f14_volume_surge_accumulation_newsint_21d_base_v062_signal,
    f14vs_f14_volume_surge_accumulation_dvherf_63d_base_v063_signal,
    f14vs_f14_volume_surge_accumulation_volzimp_5d_base_v064_signal,
    f14vs_f14_volume_surge_accumulation_extspike_252d_base_v065_signal,
    f14vs_f14_volume_surge_accumulation_bigupday_63d_base_v066_signal,
    f14vs_f14_volume_surge_accumulation_volac1_63d_base_v067_signal,
    f14vs_f14_volume_surge_accumulation_dvsurgerank_base_v068_signal,
    f14vs_f14_volume_surge_accumulation_accbalz_126d_base_v069_signal,
    f14vs_f14_volume_surge_accumulation_surgefade_63d_base_v070_signal,
    f14vs_f14_volume_surge_accumulation_dvelevfrac_126d_base_v071_signal,
    f14vs_f14_volume_surge_accumulation_accindex_252d_base_v072_signal,
    f14vs_f14_volume_surge_accumulation_surgeclust_base_v073_signal,
    f14vs_f14_volume_surge_accumulation_eventint_63d_base_v074_signal,
    f14vs_f14_volume_surge_accumulation_dvzonset_21d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F14_VOLUME_SURGE_ACCUMULATION_REGISTRY_001_075 = REGISTRY


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

    print("OK f14_volume_surge_accumulation_base_001_075_claude: %d features pass" % n_features)
