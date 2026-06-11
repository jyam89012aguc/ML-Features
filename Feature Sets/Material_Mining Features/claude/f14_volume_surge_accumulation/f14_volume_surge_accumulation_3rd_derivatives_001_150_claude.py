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


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _f14_vol_z(volume, w):
    lv = np.log(volume.clip(lower=1.0))
    return _z(lv, w)


def _f14_surge_ratio(volume, w_long):
    avg = volume.rolling(w_long, min_periods=max(5, w_long // 2)).mean()
    return volume / avg.replace(0, np.nan)


def _f14_dollar_vol(closeadj, volume):
    return (closeadj * volume).clip(lower=0.0)


def _f14_updown_vol(closeadj, volume, w):
    ret = closeadj.pct_change()
    up = volume.where(ret > 0, 0.0)
    dn = volume.where(ret < 0, 0.0)
    ups = up.rolling(w, min_periods=max(3, w // 2)).sum()
    dns = dn.rolling(w, min_periods=max(3, w // 2)).sum()
    return ups / (ups + dns).replace(0, np.nan)


def _f14_herfindahl(volume, w):
    tot = volume.rolling(w, min_periods=max(3, w // 2)).sum()
    sq = (volume * volume).rolling(w, min_periods=max(3, w // 2)).sum()
    return sq / (tot * tot).replace(0, np.nan)


def f14vs_f14_volume_surge_accumulation_volz_63d_jerk_v001_signal(volume):
    b = _f14_vol_z(volume, 63)
    result = (b.shift(-21) - 2.0 * b + b.shift(21)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_volz_126d_jerk_v002_signal(volume):
    lv = np.log(volume.clip(lower=1.0)).rolling(21, min_periods=10).mean()
    b = _z(lv, 126)
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_volz_252d_jerk_v003_signal(volume):
    sm = volume.rolling(63, min_periods=21).mean()
    b = sm.rolling(252, min_periods=126).rank(pct=True) - 0.5
    result = ((b - b.shift(63)) - (b.shift(63) - b.shift(94))) / float(1953)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_surge_63d_jerk_v004_signal(volume):
    b = _f14_surge_ratio(volume, 63)
    sm = b.ewm(span=21, min_periods=2).mean()
    result = (sm - 2.0 * sm.shift(21) + sm.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_surge_5v63_jerk_v005_signal(volume):
    short = volume.rolling(5, min_periods=3).mean()
    long = volume.rolling(63, min_periods=21).mean()
    b = short / long.replace(0, np.nan)
    sc = b.rolling(63, min_periods=21).std().replace(0, np.nan)
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / (sc * float(21))
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_surge_21v126_jerk_v006_signal(volume):
    short = volume.rolling(21, min_periods=10).mean()
    long = volume.rolling(126, min_periods=63).mean()
    b = short / long.replace(0, np.nan)
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_surge_252d_jerk_v007_signal(volume):
    short = volume.rolling(21, min_periods=10).mean()
    med = volume.rolling(252, min_periods=126).median()
    b = np.log(short.replace(0, np.nan) / med.replace(0, np.nan))
    result = (b.shift(-63) - 2.0 * b + b.shift(63)) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_updn_21d_jerk_v008_signal(closeadj, volume):
    b = _f14_updown_vol(closeadj, volume, 21)
    result = (b - 2.0 * b.shift(3) + b.shift(6)) / float(9)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_updn_63d_jerk_v009_signal(closeadj, volume):
    b = _f14_updown_vol(closeadj, volume, 63)
    result = ((b - b.shift(21)) - (b.shift(21) - b.shift(31))) / float(210)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_updn_126d_jerk_v010_signal(closeadj, volume):
    b = _f14_updown_vol(closeadj, volume, 126)
    sm = b.ewm(span=21, min_periods=2).mean()
    result = (sm - 2.0 * sm.shift(21) + sm.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_dvtrend_63d_jerk_v011_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume).rolling(21, min_periods=10).mean()
    b = np.log(dv.replace(0, np.nan) / dv.shift(63).replace(0, np.nan))
    sc = b.rolling(63, min_periods=21).std().replace(0, np.nan)
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / (sc * float(21))
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_dvtrend_126d_jerk_v012_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume).rolling(21, min_periods=10).mean()
    b = np.log(dv.replace(0, np.nan) / dv.shift(126).replace(0, np.nan))
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_dvz_126d_jerk_v013_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    b = _z(np.log(dv.clip(lower=1.0)), 126)
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_accnews_63d_jerk_v014_signal(closeadj, volume):
    vz = _f14_vol_z(volume, 63)
    ret = closeadj.pct_change()
    signed = np.sign(ret) * vz.clip(lower=0)
    b = signed.rolling(21, min_periods=10).mean()
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_herf_63d_jerk_v015_signal(volume):
    b = _f14_herfindahl(volume, 63)
    result = ((b - b.shift(21)) - (b.shift(21) - b.shift(31))) / float(210)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_herf_126d_jerk_v016_signal(volume):
    b = _f14_herfindahl(volume, 126)
    sm = b.ewm(span=21, min_periods=2).mean()
    result = (sm - 2.0 * sm.shift(21) + sm.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_scount_63d_jerk_v017_signal(volume):
    avg = volume.rolling(63, min_periods=21).mean()
    ratio = volume / avg.replace(0, np.nan)
    cnt = (ratio > 2.0).astype(float).rolling(63, min_periods=21).sum()
    depth = (ratio - 2.0).clip(lower=0).rolling(63, min_periods=21).mean()
    b = cnt + depth
    sc = b.rolling(63, min_periods=21).std().replace(0, np.nan)
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / (sc * float(21))
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_scount_126d_jerk_v018_signal(volume):
    avg = volume.rolling(63, min_periods=21).mean()
    ratio = volume / avg.replace(0, np.nan)
    cnt = (ratio > 2.0).astype(float).rolling(126, min_periods=63).sum()
    depth = (ratio - 2.0).clip(lower=0).rolling(126, min_periods=63).mean()
    b = cnt + 2.0 * depth
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_scount_252d_jerk_v019_signal(volume):
    thr = volume.rolling(252, min_periods=126).quantile(0.90)
    avg = volume.rolling(126, min_periods=63).mean()
    ratio = volume / avg.replace(0, np.nan)
    cnt = (volume > thr).astype(float).rolling(252, min_periods=126).sum()
    depth = (ratio - 1.0).clip(lower=0).where(volume > thr, 0.0).rolling(252, min_periods=126).sum()
    b = cnt + depth
    result = (b.shift(-63) - 2.0 * b + b.shift(63)) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_elevfrac_63d_jerk_v020_signal(volume):
    med = volume.rolling(63, min_periods=21).median()
    above = (volume > med).astype(float)
    frac = above.rolling(63, min_periods=21).mean()
    overshoot = (volume / med.replace(0, np.nan) - 1.0).rolling(63, min_periods=21).mean()
    b = frac + 0.5 * overshoot
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_surgerank_252d_jerk_v021_signal(volume):
    sm = volume.rolling(21, min_periods=10).mean()
    b = _rank(sm, 252)
    result = ((b - b.shift(63)) - (b.shift(63) - b.shift(94))) / float(1953)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_volzdisp_63d_jerk_v022_signal(volume):
    lv = np.log(volume.clip(lower=1.0))
    short = lv.rolling(5, min_periods=3).std()
    long = lv.rolling(63, min_periods=21).std()
    b = short / long.replace(0, np.nan)
    sm = b.ewm(span=21, min_periods=2).mean()
    result = (sm - 2.0 * sm.shift(21) + sm.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_accbias_63d_jerk_v023_signal(closeadj, volume):
    ud = _f14_updown_vol(closeadj, volume, 63)
    b = (ud - 0.5).ewm(span=21, min_periods=10).mean()
    sc = b.rolling(63, min_periods=21).std().replace(0, np.nan)
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / (sc * float(21))
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_dvsurge_5v63_jerk_v024_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    short = dv.rolling(5, min_periods=3).mean()
    long = dv.rolling(63, min_periods=21).mean()
    b = short / long.replace(0, np.nan)
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_volvov_63d_jerk_v025_signal(volume):
    lv = np.log(volume.clip(lower=1.0))
    b = lv.rolling(63, min_periods=21).std()
    result = (b.shift(-21) - 2.0 * b + b.shift(21)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_volvovchg_63d_jerk_v026_signal(volume):
    lv = np.log(volume.clip(lower=1.0))
    vov = lv.rolling(63, min_periods=21).std()
    b = vov - vov.shift(63)
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_maxshare_63d_jerk_v027_signal(volume):
    tot = volume.rolling(63, min_periods=21).sum()
    mx = volume.rolling(63, min_periods=21).max()
    b = mx / tot.replace(0, np.nan)
    result = ((b - b.shift(21)) - (b.shift(21) - b.shift(31))) / float(210)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_accnews_126d_jerk_v028_signal(closeadj, volume):
    aret = closeadj.pct_change().abs()
    lv = np.log(volume.clip(lower=1.0))
    mr = aret.rolling(126, min_periods=63).mean()
    mv = lv.rolling(126, min_periods=63).mean()
    cov = (aret * lv).rolling(126, min_periods=63).mean() - mr * mv
    sr = aret.rolling(126, min_periods=63).std()
    sv = lv.rolling(126, min_periods=63).std()
    b = cov / (sr * sv).replace(0, np.nan)
    sm = b.ewm(span=21, min_periods=2).mean()
    result = (sm - 2.0 * sm.shift(21) + sm.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_surgelog_63d_jerk_v029_signal(volume):
    avg = volume.rolling(63, min_periods=21).mean()
    ls = np.log(volume.clip(lower=1.0) / avg.replace(0, np.nan))
    b = ls.clip(lower=0).rolling(5, min_periods=3).sum() - ls.clip(upper=0).abs().rolling(5, min_periods=3).sum()
    sc = b.rolling(63, min_periods=21).std().replace(0, np.nan)
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / (sc * float(21))
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_drycount_63d_jerk_v030_signal(volume):
    avg = volume.rolling(63, min_periods=21).mean()
    ratio = volume / avg.replace(0, np.nan)
    cnt = (ratio < 0.5).astype(float).rolling(63, min_periods=21).sum()
    depth = (0.5 - ratio).clip(lower=0).rolling(63, min_periods=21).mean()
    b = cnt + 20.0 * depth
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_netactiv_126d_jerk_v031_signal(volume):
    avg = volume.rolling(63, min_periods=21).mean()
    ratio = volume / avg.replace(0, np.nan)
    surge = (ratio > 2.0).astype(float).rolling(126, min_periods=63).sum()
    dry = (ratio < 0.5).astype(float).rolling(126, min_periods=63).sum()
    tilt = (ratio - 1.0).clip(-1.0, 3.0).rolling(126, min_periods=63).mean()
    b = (surge - dry) + 5.0 * tilt
    result = (b.shift(-21) - 2.0 * b + b.shift(21)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_dvdd_252d_jerk_v032_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume).rolling(21, min_periods=10).mean()
    peak = dv.rolling(252, min_periods=126).max()
    b = dv / peak.replace(0, np.nan) - 1.0
    result = (b - 2.0 * b.shift(31) + b.shift(62)) / float(961)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_dvupdn_63d_jerk_v033_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f14_dollar_vol(closeadj, volume)
    flow = (np.sign(ret) * dv).rolling(21, min_periods=10).sum()
    base = dv.rolling(63, min_periods=21).mean() * 21.0
    norm = flow / base.replace(0, np.nan)
    b = norm - norm.shift(63)
    result = ((b - b.shift(21)) - (b.shift(21) - b.shift(31))) / float(210)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_voltrend_21d_jerk_v034_signal(volume):
    va = volume.rolling(5, min_periods=3).mean()
    b = np.log(va.replace(0, np.nan) / va.shift(21).replace(0, np.nan))
    sm = b.ewm(span=5, min_periods=2).mean()
    result = (sm - 2.0 * sm.shift(5) + sm.shift(10)) / float(25)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_voltrend_63d_jerk_v035_signal(volume):
    va = volume.rolling(21, min_periods=10).mean()
    b = np.log(va.replace(0, np.nan) / va.shift(63).replace(0, np.nan))
    sc = b.rolling(63, min_periods=21).std().replace(0, np.nan)
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / (sc * float(21))
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_herfchg_63d_jerk_v036_signal(volume):
    h = _f14_herfindahl(volume, 63)
    b = h - h.shift(63)
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_surgez_126d_jerk_v037_signal(volume):
    mx = volume.rolling(63, min_periods=21).max()
    b = volume / mx.replace(0, np.nan)
    result = (b.shift(-21) - 2.0 * b + b.shift(21)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_accstreak_21d_jerk_v038_signal(closeadj, volume):
    ret = closeadj.pct_change()
    med = volume.rolling(21, min_periods=10).median()
    heavy = (volume / med.replace(0, np.nan)).where(ret > 0, 0.0)
    b = heavy.rolling(21, min_periods=10).sum()
    result = (b - 2.0 * b.shift(3) + b.shift(6)) / float(9)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_spikerecency_63d_jerk_v039_signal(volume):
    avg = volume.rolling(63, min_periods=21).mean()
    surge = (volume > 3.0 * avg).astype(float)

    def _last(a):
        idx = np.where(a > 0)[0]
        if len(idx) == 0:
            return 1.0
        return (len(a) - 1 - idx[-1]) / float(len(a))
    b = surge.rolling(63, min_periods=21).apply(_last, raw=True)
    result = ((b - b.shift(21)) - (b.shift(21) - b.shift(31))) / float(210)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_dvampl_63d_jerk_v040_signal(closeadj, volume):
    dvz = _z(np.log(_f14_dollar_vol(closeadj, volume).clip(lower=1.0)), 63)
    vz = _f14_vol_z(volume, 63)
    b = dvz - vz
    sm = b.ewm(span=21, min_periods=2).mean()
    result = (sm - 2.0 * sm.shift(21) + sm.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_topqfrac_63d_jerk_v041_signal(volume):
    q3 = volume.rolling(252, min_periods=63).quantile(0.75)
    above = (volume > q3).astype(float)
    frac = above.rolling(63, min_periods=21).mean()
    overshoot = (volume / q3.replace(0, np.nan) - 1.0).clip(lower=0).rolling(63, min_periods=21).mean()
    b = frac + overshoot
    sc = b.rolling(63, min_periods=21).std().replace(0, np.nan)
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / (sc * float(21))
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_surgespr_jerk_v042_signal(volume):
    a = volume.rolling(5, min_periods=3).mean() / volume.rolling(63, min_periods=21).mean().replace(0, np.nan)
    c = volume.rolling(21, min_periods=10).mean() / volume.rolling(126, min_periods=63).mean().replace(0, np.nan)
    b = a - c
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_addist_63d_jerk_v043_signal(closeadj, volume):
    ret = closeadj.pct_change()
    signed = ret.clip(-0.5, 0.5) * volume
    s = signed.rolling(63, min_periods=21).sum()
    t = volume.rolling(63, min_periods=21).sum()
    b = s / t.replace(0, np.nan)
    result = (b.shift(-21) - 2.0 * b + b.shift(21)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_volskew_63d_jerk_v044_signal(volume):
    lv = np.log(volume.clip(lower=1.0))
    b = lv.rolling(63, min_periods=21).skew()
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_volkurt_126d_jerk_v045_signal(volume):
    lv = np.log(volume.clip(lower=1.0))
    b = lv.rolling(126, min_periods=63).kurt()
    result = ((b - b.shift(21)) - (b.shift(21) - b.shift(31))) / float(210)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_burst_63d_jerk_v046_signal(volume):
    five = volume.rolling(5, min_periods=3).sum()
    mx5 = five.rolling(63, min_periods=21).max()
    tot = volume.rolling(63, min_periods=21).sum()
    b = mx5 / tot.replace(0, np.nan)
    sm = b.ewm(span=21, min_periods=2).mean()
    result = (sm - 2.0 * sm.shift(21) + sm.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_dvtrendrank_jerk_v047_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume).rolling(21, min_periods=10).mean()
    tr = np.log(dv.replace(0, np.nan) / dv.shift(63).replace(0, np.nan))
    b = _rank(tr, 252)
    sc = b.rolling(63, min_periods=21).std().replace(0, np.nan)
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / (sc * float(21))
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_accmom_63d_jerk_v048_signal(closeadj, volume):
    short = _f14_updown_vol(closeadj, volume, 21)
    long = _f14_updown_vol(closeadj, volume, 126)
    b = short - long
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_regdist_252d_jerk_v049_signal(volume):
    lv = np.log(volume.clip(lower=1.0))
    short = lv.rolling(63, min_periods=21).mean()
    long = lv.rolling(252, min_periods=126).mean()
    b = short - long
    result = (b.shift(-63) - 2.0 * b + b.shift(63)) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_surgeint_63d_jerk_v050_signal(volume):
    avg = volume.rolling(63, min_periods=21).mean()
    ratio = volume / avg.replace(0, np.nan)
    excess = (ratio - 2.0).clip(lower=0)
    b = excess.rolling(63, min_periods=21).mean()
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_dvflowsm_63d_jerk_v051_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f14_dollar_vol(closeadj, volume)
    up = dv.where(ret > 0, 0.0).rolling(63, min_periods=21).sum()
    dn = dv.where(ret < 0, 0.0).rolling(63, min_periods=21).sum()
    bal = (up - dn) / (up + dn).replace(0, np.nan)
    b = np.sign(bal) * (bal.abs() ** 0.5)
    result = ((b - b.shift(21)) - (b.shift(21) - b.shift(31))) / float(210)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_voldisp_63d_jerk_v052_signal(volume):
    p90 = volume.rolling(63, min_periods=21).quantile(0.90)
    p50 = volume.rolling(63, min_periods=21).quantile(0.50)
    b = p90 / p50.replace(0, np.nan)
    sm = b.ewm(span=21, min_periods=2).mean()
    result = (sm - 2.0 * sm.shift(21) + sm.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_wscount_126d_jerk_v053_signal(volume):
    vz = _f14_vol_z(volume, 63)
    w = vz.clip(lower=0)
    b = w.rolling(126, min_periods=63).sum()
    sc = b.rolling(63, min_periods=21).std().replace(0, np.nan)
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / (sc * float(21))
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_surgetanh_63d_jerk_v054_signal(volume):
    vz = _f14_vol_z(volume, 63)
    b = np.tanh(0.7 * vz)
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_dvaccel_jerk_v055_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume).rolling(21, min_periods=10).mean()
    t63 = np.log(dv.replace(0, np.nan) / dv.shift(63).replace(0, np.nan))
    t126 = np.log(dv.replace(0, np.nan) / dv.shift(126).replace(0, np.nan)) / 2.0
    b = t63 - t126
    result = (b.shift(-21) - 2.0 * b + b.shift(21)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_upsurge_126d_jerk_v056_signal(closeadj, volume):
    ret = closeadj.pct_change()
    avg = volume.rolling(63, min_periods=21).mean()
    excess = (volume / avg.replace(0, np.nan) - 1.5).clip(lower=0)
    wgt = excess.where(ret > 0, 0.0)
    b = wgt.rolling(126, min_periods=63).sum()
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_dnsurge_126d_jerk_v057_signal(closeadj, volume):
    ret = closeadj.pct_change()
    avg = volume.rolling(63, min_periods=21).mean()
    excess = (volume / avg.replace(0, np.nan) - 1.5).clip(lower=0)
    wgt = excess.where(ret < 0, 0.0)
    b = wgt.rolling(126, min_periods=63).sum()
    result = ((b - b.shift(21)) - (b.shift(21) - b.shift(31))) / float(210)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_surgebias_126d_jerk_v058_signal(closeadj, volume):
    ret = closeadj.pct_change()
    avg = volume.rolling(63, min_periods=21).mean()
    excess = (volume / avg.replace(0, np.nan) - 1.5).clip(lower=0)
    up = excess.where(ret > 0, 0.0)
    dn = excess.where(ret < 0, 0.0)
    b = (up - dn).rolling(126, min_periods=63).sum()
    sm = b.ewm(span=21, min_periods=2).mean()
    result = (sm - 2.0 * sm.shift(21) + sm.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_volcons_21d_jerk_v059_signal(volume):
    avg = volume.rolling(63, min_periods=21).mean()
    above = (volume > avg).astype(float)
    frac = above.rolling(21, min_periods=10).mean()
    tilt = (volume / avg.replace(0, np.nan) - 1.0).rolling(21, min_periods=10).mean()
    b = (2.0 * frac - 1.0) + tilt
    sc = b.rolling(15, min_periods=5).std().replace(0, np.nan)
    result = (b - 2.0 * b.shift(5) + b.shift(10)) / (sc * float(5))
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_dvtrend_252d_jerk_v060_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume).rolling(21, min_periods=10).mean()
    b = np.log(dv.replace(0, np.nan) / dv.shift(252).replace(0, np.nan))
    result = (b - 2.0 * b.shift(63) + b.shift(126)) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_volrange_63d_jerk_v061_signal(volume):
    lv = np.log(volume.clip(lower=1.0))
    rng = lv.rolling(63, min_periods=21).max() - lv.rolling(63, min_periods=21).min()
    mn = lv.rolling(63, min_periods=21).mean()
    b = rng / mn.replace(0, np.nan)
    result = (b.shift(-21) - 2.0 * b + b.shift(21)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_newsint_21d_jerk_v062_signal(closeadj, volume):
    ret = closeadj.pct_change()
    sr = _f14_surge_ratio(volume, 63)
    inter = ret * (sr - 1.0)
    b = inter.rolling(21, min_periods=10).sum()
    result = (b - 2.0 * b.shift(3) + b.shift(6)) / float(9)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_dvherf_63d_jerk_v063_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    b = _f14_herfindahl(dv, 63)
    result = ((b - b.shift(21)) - (b.shift(21) - b.shift(31))) / float(210)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_volzimp_5d_jerk_v064_signal(volume):
    vz = _f14_vol_z(volume, 63)
    b = vz - vz.shift(5)
    sm = b.ewm(span=5, min_periods=2).mean()
    result = (sm - 2.0 * sm.shift(5) + sm.shift(10)) / float(25)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_extspike_252d_jerk_v065_signal(volume):
    vz = _f14_vol_z(volume, 126)
    cnt = (vz > 1.0).astype(float).rolling(252, min_periods=126).sum()
    mag = (vz - 1.0).clip(lower=0).rolling(252, min_periods=126).sum()
    b = cnt + mag
    sc = b.rolling(189, min_periods=63).std().replace(0, np.nan)
    result = (b - 2.0 * b.shift(63) + b.shift(126)) / (sc * float(63))
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_bigupday_63d_jerk_v066_signal(closeadj, volume):
    ret = closeadj.pct_change()
    upvol = volume.where(ret > 0, 0.0)
    mx = upvol.rolling(63, min_periods=21).max()
    tot = volume.rolling(63, min_periods=21).sum()
    b = mx / tot.replace(0, np.nan)
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_volac1_63d_jerk_v067_signal(volume):
    lv = np.log(volume.clip(lower=1.0))
    b = lv.rolling(63, min_periods=21).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=False)
    result = (b.shift(-21) - 2.0 * b + b.shift(21)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_dvsurgerank_jerk_v068_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    sr = dv / dv.rolling(63, min_periods=21).mean().replace(0, np.nan)
    b = _rank(sr, 252)
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_accbalz_126d_jerk_v069_signal(closeadj, volume):
    ud = _f14_updown_vol(closeadj, volume, 21)
    sm = ud.ewm(span=21, min_periods=10).mean()
    b = _z(sm, 126)
    result = ((b - b.shift(21)) - (b.shift(21) - b.shift(31))) / float(210)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_surgefade_63d_jerk_v070_signal(volume):
    pk = volume.rolling(21, min_periods=10).max()
    b = np.log(volume.clip(lower=1.0) / pk.replace(0, np.nan))
    sm = b.ewm(span=21, min_periods=2).mean()
    result = (sm - 2.0 * sm.shift(21) + sm.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_dvelevfrac_126d_jerk_v071_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    med = dv.rolling(126, min_periods=63).median()
    above = (dv > med).astype(float)
    frac = above.rolling(126, min_periods=63).mean()
    overshoot = (dv / med.replace(0, np.nan) - 1.0).rolling(126, min_periods=63).mean()
    b = frac + 0.3 * overshoot
    sc = b.rolling(63, min_periods=21).std().replace(0, np.nan)
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / (sc * float(21))
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_accindex_252d_jerk_v072_signal(closeadj, volume):
    ret = closeadj.pct_change()
    signed = np.sign(ret) * volume
    cum = signed.rolling(252, min_periods=126).sum()
    tot = volume.rolling(252, min_periods=126).sum()
    b = cum / tot.replace(0, np.nan)
    result = (b - 2.0 * b.shift(63) + b.shift(126)) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_surgeclust_jerk_v073_signal(volume):
    avg = volume.rolling(63, min_periods=21).mean()
    excess = (volume / avg.replace(0, np.nan) - 2.0).clip(lower=0)
    recent = excess.rolling(21, min_periods=10).sum()
    prior = excess.shift(21).rolling(21, min_periods=10).sum()
    b = recent - prior
    result = (b.shift(-21) - 2.0 * b + b.shift(21)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_eventint_63d_jerk_v074_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    w = volume / volume.rolling(63, min_periods=21).sum().replace(0, np.nan)
    b = (ret * w).rolling(63, min_periods=21).sum()
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_dvzonset_21d_jerk_v075_signal(closeadj, volume):
    dvz = _z(np.log(_f14_dollar_vol(closeadj, volume).clip(lower=1.0)), 126)
    b = dvz - dvz.shift(21)
    result = ((b - b.shift(5)) - (b.shift(5) - b.shift(8))) / float(15)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_volz_21d_jerk_v076_signal(volume):
    b = _f14_vol_z(volume, 21)
    sm = b.ewm(span=5, min_periods=2).mean()
    result = (sm - 2.0 * sm.shift(5) + sm.shift(10)) / float(25)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_surge_5v21_jerk_v077_signal(volume):
    short = volume.rolling(5, min_periods=3).mean()
    long = volume.rolling(21, min_periods=10).mean()
    b = short / long.replace(0, np.nan)
    sc = b.rolling(63, min_periods=21).std().replace(0, np.nan)
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / (sc * float(21))
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_surge_21v252_jerk_v078_signal(volume):
    short = volume.rolling(21, min_periods=10).mean()
    long = volume.rolling(252, min_periods=126).mean()
    b = np.log(short.replace(0, np.nan) / long.replace(0, np.nan))
    result = ((b - b.shift(21)) - (b.shift(21) - b.shift(31))) / float(210)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_surge_63v252_jerk_v079_signal(volume):
    short = volume.rolling(63, min_periods=21).mean()
    long = volume.rolling(252, min_periods=126).mean()
    b = np.log(short.replace(0, np.nan) / long.replace(0, np.nan))
    result = (b.shift(-21) - 2.0 * b + b.shift(21)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_updn_5d_jerk_v080_signal(closeadj, volume):
    b = _f14_updown_vol(closeadj, volume, 5)
    result = (b - 2.0 * b.shift(3) + b.shift(6)) / float(9)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_updn_252d_jerk_v081_signal(closeadj, volume):
    b = _f14_updown_vol(closeadj, volume, 252)
    result = ((b - b.shift(63)) - (b.shift(63) - b.shift(94))) / float(1953)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_accslope_63d_jerk_v082_signal(closeadj, volume):
    ret = closeadj.pct_change()
    signed = np.sign(ret) * volume
    s = signed.rolling(63, min_periods=21).sum()
    t = volume.rolling(63, min_periods=21).sum()
    share = s / t.replace(0, np.nan)
    b = share - share.shift(21)
    sm = b.ewm(span=21, min_periods=2).mean()
    result = (sm - 2.0 * sm.shift(21) + sm.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_dvlevel_63d_jerk_v083_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume).rolling(63, min_periods=21).mean()
    b = np.log(dv.replace(0, np.nan))
    sc = b.rolling(63, min_periods=21).std().replace(0, np.nan)
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / (sc * float(21))
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_dvsurge_126d_jerk_v084_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    thr = dv.rolling(126, min_periods=63).quantile(0.80)
    cnt = (dv > thr).astype(float).rolling(63, min_periods=21).sum()
    depth = (dv / thr.replace(0, np.nan) - 1.0).clip(lower=0).where(dv > thr, 0.0).rolling(63, min_periods=21).sum()
    b = cnt + depth
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_dvtrendz_63d_jerk_v085_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume).rolling(21, min_periods=10).mean()
    tr = np.log(dv.replace(0, np.nan) / dv.shift(63).replace(0, np.nan))
    b = _z(tr, 252)
    result = (b.shift(-21) - 2.0 * b + b.shift(21)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_accconfirm_63d_jerk_v086_signal(closeadj, volume):
    ret = closeadj.pct_change()
    w = volume / volume.rolling(126, min_periods=63).sum().replace(0, np.nan)
    b = (ret * w).rolling(126, min_periods=63).sum()
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_newsvolprem_63d_jerk_v087_signal(closeadj, volume):
    aret = closeadj.pct_change().abs()
    thr = aret.rolling(63, min_periods=21).median()
    lv = np.log(volume.clip(lower=1.0))
    big = lv.where(aret > thr, np.nan).rolling(63, min_periods=21).mean()
    quiet = lv.where(aret <= thr, np.nan).rolling(63, min_periods=21).mean()
    b = big - quiet
    result = ((b - b.shift(21)) - (b.shift(21) - b.shift(31))) / float(210)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_volretcorr_63d_jerk_v088_signal(closeadj, volume):
    aret = closeadj.pct_change().abs()
    rv = volume.rolling(63, min_periods=21).rank(pct=True)
    rr = aret.rolling(63, min_periods=21).rank(pct=True)
    b = ((rv - 0.5) * (rr - 0.5)).rolling(63, min_periods=21).mean()
    sm = b.ewm(span=21, min_periods=2).mean()
    result = (sm - 2.0 * sm.shift(21) + sm.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_herf_252d_jerk_v089_signal(volume):
    b = _f14_herfindahl(volume, 252)
    sc = b.rolling(189, min_periods=63).std().replace(0, np.nan)
    result = (b - 2.0 * b.shift(63) + b.shift(126)) / (sc * float(63))
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_top3share_21d_jerk_v090_signal(volume):
    def _top3(a):
        s = np.sort(a)[-3:].sum()
        tot = a.sum()
        if tot <= 0:
            return np.nan
        return s / tot
    b = volume.rolling(21, min_periods=10).apply(_top3, raw=True)
    result = (b - 2.0 * b.shift(5) + b.shift(10)) / float(25)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_scount80_63d_jerk_v091_signal(volume):
    thr = volume.rolling(252, min_periods=126).quantile(0.80)
    avg = volume.rolling(63, min_periods=21).mean()
    ratio = volume / avg.replace(0, np.nan)
    cnt = (volume > thr).astype(float).rolling(63, min_periods=21).sum()
    depth = (ratio - 1.0).clip(lower=0).where(volume > thr, 0.0).rolling(63, min_periods=21).sum()
    b = cnt + depth
    result = (b.shift(-21) - 2.0 * b + b.shift(21)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_scount95_252d_jerk_v092_signal(volume):
    thr = volume.rolling(252, min_periods=126).quantile(0.95)
    avg = volume.rolling(126, min_periods=63).mean()
    ratio = volume / avg.replace(0, np.nan)
    cnt = (volume > thr).astype(float).rolling(252, min_periods=126).sum()
    depth = (ratio - 1.0).clip(lower=0).where(volume > thr, 0.0).rolling(252, min_periods=126).sum()
    b = cnt + depth
    result = (b - 2.0 * b.shift(31) + b.shift(62)) / float(961)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_uppertile_126d_jerk_v093_signal(volume):
    q = volume.rolling(252, min_periods=126).quantile(0.6667)
    above = (volume > q).astype(float)
    frac = above.rolling(126, min_periods=63).mean()
    overshoot = (volume / q.replace(0, np.nan) - 1.0).clip(lower=0).rolling(126, min_periods=63).mean()
    b = frac + overshoot
    result = ((b - b.shift(21)) - (b.shift(21) - b.shift(31))) / float(210)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_dvz_252d_jerk_v094_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    b = _z(np.log(dv.clip(lower=1.0)), 252)
    sm = b.ewm(span=63, min_periods=2).mean()
    result = (sm - 2.0 * sm.shift(63) + sm.shift(126)) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_volxover_jerk_v095_signal(volume):
    lv = np.log(volume.clip(lower=1.0))
    fast = lv.ewm(span=10, min_periods=5).mean()
    slow = lv.ewm(span=63, min_periods=21).mean()
    b = fast - slow
    sc = b.rolling(63, min_periods=21).std().replace(0, np.nan)
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / (sc * float(21))
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_volmacd_jerk_v096_signal(volume):
    lv = np.log(volume.clip(lower=1.0))
    macd = lv.ewm(span=12, min_periods=6).mean() - lv.ewm(span=26, min_periods=13).mean()
    sig = macd.ewm(span=9, min_periods=5).mean()
    b = macd - sig
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_dvflow_126d_jerk_v097_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f14_dollar_vol(closeadj, volume)
    up = dv.where(ret > 0, 0.0).rolling(126, min_periods=63).sum()
    dn = dv.where(ret < 0, 0.0).rolling(126, min_periods=63).sum()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = (b.shift(-21) - 2.0 * b + b.shift(21)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_rankflow_63d_jerk_v098_signal(closeadj, volume):
    ret = closeadj.pct_change()
    rv = volume.rolling(63, min_periods=21).rank(pct=True)
    b = (np.sign(ret) * rv).rolling(63, min_periods=21).mean()
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_volols_63d_jerk_v099_signal(volume):
    lv = np.log(volume.clip(lower=1.0))
    x = np.arange(63, dtype=float)
    xm = x.mean()
    den = ((x - xm) ** 2).sum()

    def _slope(a):
        return ((x - xm) * (a - a.mean())).sum() / den
    b = lv.rolling(63, min_periods=63).apply(_slope, raw=True)
    result = ((b - b.shift(21)) - (b.shift(21) - b.shift(31))) / float(210)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_dvols_126d_jerk_v100_signal(closeadj, volume):
    ldv = np.log(_f14_dollar_vol(closeadj, volume).clip(lower=1.0))
    x = np.arange(126, dtype=float)
    xm = x.mean()
    den = ((x - xm) ** 2).sum()

    def _slope(a):
        return ((x - xm) * (a - a.mean())).sum() / den
    b = ldv.rolling(126, min_periods=126).apply(_slope, raw=True)
    sm = b.ewm(span=21, min_periods=2).mean()
    result = (sm - 2.0 * sm.shift(21) + sm.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_volboll_63d_jerk_v101_signal(volume):
    m = volume.rolling(63, min_periods=21).mean()
    sd = volume.rolling(63, min_periods=21).std()
    b = (volume - m) / (2.0 * sd).replace(0, np.nan)
    sc = b.rolling(63, min_periods=21).std().replace(0, np.nan)
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / (sc * float(21))
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_accpersist_63d_jerk_v102_signal(closeadj, volume):
    ret = closeadj.pct_change()
    avg = volume.rolling(63, min_periods=21).mean()
    pressure = np.sign(ret) * (volume / avg.replace(0, np.nan))
    smooth = pressure.ewm(span=21, min_periods=10).mean()
    b = smooth - smooth.rolling(63, min_periods=21).min()
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_vovratio_jerk_v103_signal(volume):
    lv = np.log(volume.clip(lower=1.0))
    short = lv.rolling(21, min_periods=10).std()
    long = lv.rolling(126, min_periods=63).std()
    b = short / long.replace(0, np.nan)
    result = (b.shift(-21) - 2.0 * b + b.shift(21)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_dvmaxshare_63d_jerk_v104_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    mx = dv.rolling(63, min_periods=21).max()
    tot = dv.rolling(63, min_periods=21).sum()
    b = mx / tot.replace(0, np.nan)
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_surgesm_21d_jerk_v105_signal(volume):
    sr = _f14_surge_ratio(volume, 21) - 1.0
    sm = np.sign(sr) * (sr.abs() ** 0.5)
    b = sm.rolling(5, min_periods=3).mean()
    result = ((b - b.shift(5)) - (b.shift(5) - b.shift(8))) / float(15)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_imbal_126d_jerk_v106_signal(closeadj, volume):
    ud = _f14_updown_vol(closeadj, volume, 126)
    b = (ud - 0.5).ewm(span=42, min_periods=21).mean()
    sm = b.ewm(span=21, min_periods=2).mean()
    result = (sm - 2.0 * sm.shift(21) + sm.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_surgerank_504d_jerk_v107_signal(volume):
    sm = volume.rolling(63, min_periods=21).mean()
    b = _rank(sm, 504)
    sc = b.rolling(189, min_periods=63).std().replace(0, np.nan)
    result = (b - 2.0 * b.shift(63) + b.shift(126)) / (sc * float(63))
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_dvdd_504d_jerk_v108_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume).rolling(21, min_periods=10).mean()
    peak = dv.rolling(504, min_periods=252).max()
    b = dv / peak.replace(0, np.nan) - 1.0
    result = (b - 2.0 * b.shift(63) + b.shift(126)) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_vwmove_63d_jerk_v109_signal(closeadj, volume):
    ret = closeadj.pct_change()
    upw = (ret.clip(lower=0) * volume).rolling(63, min_periods=21).sum()
    dnw = (ret.clip(upper=0).abs() * volume).rolling(63, min_periods=21).sum()
    b = (upw - dnw) / (upw + dnw).replace(0, np.nan)
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_volstreak_63d_jerk_v110_signal(volume):
    avg = volume.rolling(63, min_periods=21).mean()
    above = (volume > avg).astype(float)
    persist = above.rolling(10, min_periods=5).mean()
    b = (persist - 0.5) * (volume / avg.replace(0, np.nan))
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_dvslopechg_jerk_v111_signal(closeadj, volume):
    ldv = np.log(_f14_dollar_vol(closeadj, volume).clip(lower=1.0)).rolling(21, min_periods=10).mean()
    t = np.log(ldv.replace(0, np.nan))
    slope = ldv - ldv.shift(63)
    b = slope - slope.shift(63)
    result = ((b - b.shift(21)) - (b.shift(21) - b.shift(31))) / float(210)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_localpeaks_63d_jerk_v112_signal(volume):
    is_peak = ((volume > volume.shift(1)) & (volume > volume.shift(-1))).astype(float)
    avg = volume.rolling(63, min_periods=21).mean()
    depth = (volume / avg.replace(0, np.nan)).where(is_peak > 0, 0.0)
    b = depth.rolling(63, min_periods=21).sum()
    sm = b.ewm(span=21, min_periods=2).mean()
    result = (sm - 2.0 * sm.shift(21) + sm.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_accrank_252d_jerk_v113_signal(closeadj, volume):
    ret = closeadj.pct_change()
    signed = np.sign(ret) * volume
    share = signed.rolling(63, min_periods=21).sum() / volume.rolling(63, min_periods=21).sum().replace(0, np.nan)
    b = _rank(share, 252)
    sc = b.rolling(189, min_periods=63).std().replace(0, np.nan)
    result = (b - 2.0 * b.shift(63) + b.shift(126)) / (sc * float(63))
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_volzimp_21d_jerk_v114_signal(volume):
    vz = _f14_vol_z(volume, 126)
    b = vz - vz.shift(21)
    result = (b - 2.0 * b.shift(5) + b.shift(10)) / float(25)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_herfratio_jerk_v115_signal(volume):
    h63 = _f14_herfindahl(volume, 63)
    h252 = _f14_herfindahl(volume, 252)
    b = h63 / h252.replace(0, np.nan)
    result = (b.shift(-21) - 2.0 * b + b.shift(21)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_dvsurgerank_504d_jerk_v116_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume).rolling(5, min_periods=3).mean()
    b = _rank(dv, 504)
    result = (b - 2.0 * b.shift(31) + b.shift(62)) / float(961)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_accaccel_jerk_v117_signal(closeadj, volume):
    ret = closeadj.pct_change()
    signed = np.sign(ret) * volume
    share = signed.rolling(63, min_periods=21).sum() / volume.rolling(63, min_periods=21).sum().replace(0, np.nan)
    b = (share - share.shift(63)) - (share.shift(63) - share.shift(126))
    result = ((b - b.shift(21)) - (b.shift(21) - b.shift(31))) / float(210)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_volskew_126d_jerk_v118_signal(volume):
    lv = np.log(volume.clip(lower=1.0))
    b = lv.rolling(126, min_periods=63).skew()
    sm = b.ewm(span=21, min_periods=2).mean()
    result = (sm - 2.0 * sm.shift(21) + sm.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_effdays_126d_jerk_v119_signal(volume):
    h = _f14_herfindahl(volume, 126)
    b = 1.0 - (1.0 / h.replace(0, np.nan)) / 126.0
    sc = b.rolling(63, min_periods=21).std().replace(0, np.nan)
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / (sc * float(21))
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_climax_21d_jerk_v120_signal(closeadj, volume):
    vz = _f14_vol_z(volume, 63).clip(lower=0)
    aret = closeadj.pct_change().abs()
    b = (vz * aret).rolling(21, min_periods=10).mean()
    result = (b - 2.0 * b.shift(5) + b.shift(10)) / float(25)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_dvvov_63d_jerk_v121_signal(closeadj, volume):
    ldv = np.log(_f14_dollar_vol(closeadj, volume).clip(lower=1.0))
    b = ldv.rolling(63, min_periods=21).std()
    result = ((b - b.shift(21)) - (b.shift(21) - b.shift(31))) / float(210)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_surgeimp_5d_jerk_v122_signal(volume):
    sr = volume.rolling(5, min_periods=3).mean() / volume.rolling(63, min_periods=21).mean().replace(0, np.nan)
    b = sr - sr.shift(5)
    result = (b - 2.0 * b.shift(3) + b.shift(6)) / float(9)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_distrib_63d_jerk_v123_signal(closeadj, volume):
    ret = closeadj.pct_change()
    avg = volume.rolling(63, min_periods=21).mean()
    excess = (volume / avg.replace(0, np.nan) - 1.0).clip(lower=0)
    dn = excess.where(ret < 0, 0.0).rolling(63, min_periods=21).mean()
    up = excess.where(ret > 0, 0.0).rolling(63, min_periods=21).mean()
    b = dn - up
    result = ((b - b.shift(21)) - (b.shift(21) - b.shift(31))) / float(210)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_vpdiverge_63d_jerk_v124_signal(closeadj, volume):
    vm = np.log(volume.rolling(21, min_periods=10).mean().replace(0, np.nan)
                / volume.rolling(21, min_periods=10).mean().shift(63).replace(0, np.nan))
    pm = np.log(closeadj.replace(0, np.nan) / closeadj.shift(63).replace(0, np.nan))
    b = vm - pm
    sm = b.ewm(span=21, min_periods=2).mean()
    result = (sm - 2.0 * sm.shift(21) + sm.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_upherf_63d_jerk_v125_signal(closeadj, volume):
    ret = closeadj.pct_change()
    uv = volume.where(ret > 0, 0.0)
    tot = uv.rolling(63, min_periods=21).sum()
    sq = (uv * uv).rolling(63, min_periods=21).sum()
    b = sq / (tot * tot).replace(0, np.nan)
    sc = b.rolling(63, min_periods=21).std().replace(0, np.nan)
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / (sc * float(21))
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_dvmomz_126d_jerk_v126_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume).rolling(21, min_periods=10).mean()
    mom = np.log(dv.replace(0, np.nan) / dv.shift(21).replace(0, np.nan))
    b = _z(mom, 126)
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_volrise_63d_jerk_v127_signal(volume):
    rising = (volume > volume.shift(1)).astype(float)
    frac = rising.rolling(63, min_periods=21).mean()
    mag = (volume / volume.shift(1).replace(0, np.nan) - 1.0).clip(-2, 2).rolling(63, min_periods=21).mean()
    b = (frac - 0.5) + mag
    result = (b.shift(-21) - 2.0 * b + b.shift(21)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_growth_504d_jerk_v128_signal(volume):
    lv = np.log(volume.clip(lower=1.0)).rolling(21, min_periods=10).mean()
    b = lv - lv.shift(504)
    result = (b - 2.0 * b.shift(31) + b.shift(62)) / float(961)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_accindex_504d_jerk_v129_signal(closeadj, volume):
    ret = closeadj.pct_change()
    signed = np.sign(ret) * volume
    cum = signed.rolling(504, min_periods=252).sum()
    tot = volume.rolling(504, min_periods=252).sum()
    b = cum / tot.replace(0, np.nan)
    result = ((b - b.shift(63)) - (b.shift(63) - b.shift(94))) / float(1953)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_volkurt_63d_jerk_v130_signal(volume):
    lv = np.log(volume.clip(lower=1.0))
    b = lv.rolling(63, min_periods=21).kurt()
    sm = b.ewm(span=21, min_periods=2).mean()
    result = (sm - 2.0 * sm.shift(21) + sm.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_thrust_5d_jerk_v131_signal(closeadj, volume):
    r5 = np.log(closeadj.replace(0, np.nan) / closeadj.shift(5).replace(0, np.nan))
    vr = volume.rolling(5, min_periods=3).mean() / volume.rolling(63, min_periods=21).mean().replace(0, np.nan)
    b = r5 * (vr - 1.0)
    sc = b.rolling(15, min_periods=5).std().replace(0, np.nan)
    result = (b - 2.0 * b.shift(5) + b.shift(10)) / (sc * float(5))
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_dvherf_126d_jerk_v132_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    b = _f14_herfindahl(dv, 126)
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_volrangeexp_jerk_v133_signal(volume):
    lv = np.log(volume.clip(lower=1.0))
    rng63 = lv.rolling(63, min_periods=21).max() - lv.rolling(63, min_periods=21).min()
    rng252 = (lv.rolling(63, min_periods=21).max() - lv.rolling(63, min_periods=21).min()).rolling(252, min_periods=126).mean()
    b = rng63 - rng252
    result = ((b - b.shift(21)) - (b.shift(21) - b.shift(31))) / float(210)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_accquality_63d_jerk_v134_signal(closeadj, volume):
    ud = _f14_updown_vol(closeadj, volume, 63)
    trend = np.log(closeadj.replace(0, np.nan) / closeadj.shift(63).replace(0, np.nan))
    b = (ud - 0.5) * np.sign(trend) * (trend.abs() ** 0.5)
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_signedvolz_21d_jerk_v135_signal(closeadj, volume):
    ret = closeadj.pct_change()
    vz = _f14_vol_z(volume, 63)
    b = (np.sign(ret) * vz).rolling(21, min_periods=10).mean()
    result = ((b - b.shift(5)) - (b.shift(5) - b.shift(8))) / float(15)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_dvprice_126d_jerk_v136_signal(closeadj, volume):
    dvt = np.log(_f14_dollar_vol(closeadj, volume).rolling(21, min_periods=10).mean().replace(0, np.nan)
                 / _f14_dollar_vol(closeadj, volume).rolling(21, min_periods=10).mean().shift(126).replace(0, np.nan))
    pt = np.log(closeadj.replace(0, np.nan) / closeadj.shift(126).replace(0, np.nan))
    b = dvt - 2.0 * pt
    sm = b.ewm(span=21, min_periods=2).mean()
    result = (sm - 2.0 * sm.shift(21) + sm.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_burstwin_126d_jerk_v137_signal(volume):
    w21 = volume.rolling(21, min_periods=10).sum()
    mx = w21.rolling(126, min_periods=63).max()
    tot = volume.rolling(126, min_periods=63).sum()
    b = mx / tot.replace(0, np.nan)
    sc = b.rolling(63, min_periods=21).std().replace(0, np.nan)
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / (sc * float(21))
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_volac5_126d_jerk_v138_signal(volume):
    lv = np.log(volume.clip(lower=1.0))
    b = lv.rolling(126, min_periods=63).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=False)
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_surgesust_63d_jerk_v139_signal(volume):
    sr = volume.rolling(5, min_periods=3).mean() / volume.rolling(63, min_periods=21).mean().replace(0, np.nan)
    b = sr / sr.rolling(63, min_periods=21).max().replace(0, np.nan)
    result = (b.shift(-21) - 2.0 * b + b.shift(21)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_dvflowsm_126d_jerk_v140_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f14_dollar_vol(closeadj, volume)
    up = dv.where(ret > 0, 0.0).rolling(126, min_periods=63).sum()
    dn = dv.where(ret < 0, 0.0).rolling(126, min_periods=63).sum()
    bal = (up - dn) / (up + dn).replace(0, np.nan)
    b = np.sign(bal) * (bal.abs() ** 0.5)
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_excessvol_63d_jerk_v141_signal(closeadj, volume):
    vz = _f14_vol_z(volume, 63)
    rz = _z(closeadj.pct_change().abs(), 63)
    b = vz - rz
    result = ((b - b.shift(21)) - (b.shift(21) - b.shift(31))) / float(210)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_lowtile_252d_jerk_v142_signal(volume):
    q = volume.rolling(252, min_periods=126).quantile(0.3333)
    below = (volume < q).astype(float)
    frac = below.rolling(252, min_periods=126).mean()
    depth = (1.0 - volume / q.replace(0, np.nan)).clip(lower=0).rolling(252, min_periods=126).mean()
    b = frac + depth
    sm = b.ewm(span=63, min_periods=2).mean()
    result = (sm - 2.0 * sm.shift(63) + sm.shift(126)) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_accbreadth_252d_jerk_v143_signal(closeadj, volume):
    ret = closeadj.pct_change()
    avg = volume.rolling(63, min_periods=21).mean()
    excess = (volume / avg.replace(0, np.nan) - 1.0).clip(lower=0)
    w = np.sign(ret) * excess
    b = w.rolling(252, min_periods=126).sum()
    sc = b.rolling(189, min_periods=63).std().replace(0, np.nan)
    result = (b - 2.0 * b.shift(63) + b.shift(126)) / (sc * float(63))
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_volmrz_jerk_v144_signal(volume):
    diff = volume - volume.shift(5)
    sd = volume.rolling(63, min_periods=21).std()
    b = diff / sd.replace(0, np.nan)
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_dvtail_126d_jerk_v145_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    p95 = dv.rolling(126, min_periods=63).quantile(0.95)
    p50 = dv.rolling(126, min_periods=63).quantile(0.50)
    b = p95 / p50.replace(0, np.nan)
    result = (b.shift(-21) - 2.0 * b + b.shift(21)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_trendcons_jerk_v146_signal(volume):
    lv = np.log(volume.clip(lower=1.0))
    m21 = lv.rolling(21, min_periods=10).mean() - lv.rolling(21, min_periods=10).mean().shift(21)
    m63 = lv.rolling(63, min_periods=21).mean() - lv.rolling(63, min_periods=21).mean().shift(63)
    b = np.sign(m21) * np.sign(m63) * (m21.abs() + m63.abs())
    result = (b - 2.0 * b.shift(10) + b.shift(20)) / float(100)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_clustratio_jerk_v147_signal(volume):
    def _top3(a):
        s = np.sort(a)[-3:].sum()
        tot = a.sum()
        if tot <= 0:
            return np.nan
        return s / tot
    c63 = volume.rolling(63, min_periods=21).apply(_top3, raw=True)
    base = c63.rolling(252, min_periods=126).mean()
    b = c63 - base
    result = ((b - b.shift(21)) - (b.shift(21) - b.shift(31))) / float(210)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_dvflowmom_jerk_v148_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f14_dollar_vol(closeadj, volume)
    up = dv.where(ret > 0, 0.0).rolling(126, min_periods=63).sum()
    dn = dv.where(ret < 0, 0.0).rolling(126, min_periods=63).sum()
    share = (up - dn) / (up + dn).replace(0, np.nan)
    b = share - share.shift(63)
    sm = b.ewm(span=21, min_periods=2).mean()
    result = (sm - 2.0 * sm.shift(21) + sm.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_volzdisp_multi_jerk_v149_signal(volume):
    z1 = _f14_vol_z(volume, 21)
    z2 = _f14_vol_z(volume, 63)
    z3 = _f14_vol_z(volume, 126)
    b = pd.concat([z1, z2, z3], axis=1).std(axis=1)
    sc = b.rolling(63, min_periods=21).std().replace(0, np.nan)
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / (sc * float(21))
    return result.replace([np.inf, -np.inf], np.nan)
def f14vs_f14_volume_surge_accumulation_accregdist_jerk_v150_signal(closeadj, volume):
    ud = _f14_updown_vol(closeadj, volume, 63)
    med = ud.rolling(252, min_periods=126).median()
    b = ud - med
    result = (b - 2.0 * b.shift(21) + b.shift(42)) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f14vs_f14_volume_surge_accumulation_volz_63d_jerk_v001_signal,
    f14vs_f14_volume_surge_accumulation_volz_126d_jerk_v002_signal,
    f14vs_f14_volume_surge_accumulation_volz_252d_jerk_v003_signal,
    f14vs_f14_volume_surge_accumulation_surge_63d_jerk_v004_signal,
    f14vs_f14_volume_surge_accumulation_surge_5v63_jerk_v005_signal,
    f14vs_f14_volume_surge_accumulation_surge_21v126_jerk_v006_signal,
    f14vs_f14_volume_surge_accumulation_surge_252d_jerk_v007_signal,
    f14vs_f14_volume_surge_accumulation_updn_21d_jerk_v008_signal,
    f14vs_f14_volume_surge_accumulation_updn_63d_jerk_v009_signal,
    f14vs_f14_volume_surge_accumulation_updn_126d_jerk_v010_signal,
    f14vs_f14_volume_surge_accumulation_dvtrend_63d_jerk_v011_signal,
    f14vs_f14_volume_surge_accumulation_dvtrend_126d_jerk_v012_signal,
    f14vs_f14_volume_surge_accumulation_dvz_126d_jerk_v013_signal,
    f14vs_f14_volume_surge_accumulation_accnews_63d_jerk_v014_signal,
    f14vs_f14_volume_surge_accumulation_herf_63d_jerk_v015_signal,
    f14vs_f14_volume_surge_accumulation_herf_126d_jerk_v016_signal,
    f14vs_f14_volume_surge_accumulation_scount_63d_jerk_v017_signal,
    f14vs_f14_volume_surge_accumulation_scount_126d_jerk_v018_signal,
    f14vs_f14_volume_surge_accumulation_scount_252d_jerk_v019_signal,
    f14vs_f14_volume_surge_accumulation_elevfrac_63d_jerk_v020_signal,
    f14vs_f14_volume_surge_accumulation_surgerank_252d_jerk_v021_signal,
    f14vs_f14_volume_surge_accumulation_volzdisp_63d_jerk_v022_signal,
    f14vs_f14_volume_surge_accumulation_accbias_63d_jerk_v023_signal,
    f14vs_f14_volume_surge_accumulation_dvsurge_5v63_jerk_v024_signal,
    f14vs_f14_volume_surge_accumulation_volvov_63d_jerk_v025_signal,
    f14vs_f14_volume_surge_accumulation_volvovchg_63d_jerk_v026_signal,
    f14vs_f14_volume_surge_accumulation_maxshare_63d_jerk_v027_signal,
    f14vs_f14_volume_surge_accumulation_accnews_126d_jerk_v028_signal,
    f14vs_f14_volume_surge_accumulation_surgelog_63d_jerk_v029_signal,
    f14vs_f14_volume_surge_accumulation_drycount_63d_jerk_v030_signal,
    f14vs_f14_volume_surge_accumulation_netactiv_126d_jerk_v031_signal,
    f14vs_f14_volume_surge_accumulation_dvdd_252d_jerk_v032_signal,
    f14vs_f14_volume_surge_accumulation_dvupdn_63d_jerk_v033_signal,
    f14vs_f14_volume_surge_accumulation_voltrend_21d_jerk_v034_signal,
    f14vs_f14_volume_surge_accumulation_voltrend_63d_jerk_v035_signal,
    f14vs_f14_volume_surge_accumulation_herfchg_63d_jerk_v036_signal,
    f14vs_f14_volume_surge_accumulation_surgez_126d_jerk_v037_signal,
    f14vs_f14_volume_surge_accumulation_accstreak_21d_jerk_v038_signal,
    f14vs_f14_volume_surge_accumulation_spikerecency_63d_jerk_v039_signal,
    f14vs_f14_volume_surge_accumulation_dvampl_63d_jerk_v040_signal,
    f14vs_f14_volume_surge_accumulation_topqfrac_63d_jerk_v041_signal,
    f14vs_f14_volume_surge_accumulation_surgespr_jerk_v042_signal,
    f14vs_f14_volume_surge_accumulation_addist_63d_jerk_v043_signal,
    f14vs_f14_volume_surge_accumulation_volskew_63d_jerk_v044_signal,
    f14vs_f14_volume_surge_accumulation_volkurt_126d_jerk_v045_signal,
    f14vs_f14_volume_surge_accumulation_burst_63d_jerk_v046_signal,
    f14vs_f14_volume_surge_accumulation_dvtrendrank_jerk_v047_signal,
    f14vs_f14_volume_surge_accumulation_accmom_63d_jerk_v048_signal,
    f14vs_f14_volume_surge_accumulation_regdist_252d_jerk_v049_signal,
    f14vs_f14_volume_surge_accumulation_surgeint_63d_jerk_v050_signal,
    f14vs_f14_volume_surge_accumulation_dvflowsm_63d_jerk_v051_signal,
    f14vs_f14_volume_surge_accumulation_voldisp_63d_jerk_v052_signal,
    f14vs_f14_volume_surge_accumulation_wscount_126d_jerk_v053_signal,
    f14vs_f14_volume_surge_accumulation_surgetanh_63d_jerk_v054_signal,
    f14vs_f14_volume_surge_accumulation_dvaccel_jerk_v055_signal,
    f14vs_f14_volume_surge_accumulation_upsurge_126d_jerk_v056_signal,
    f14vs_f14_volume_surge_accumulation_dnsurge_126d_jerk_v057_signal,
    f14vs_f14_volume_surge_accumulation_surgebias_126d_jerk_v058_signal,
    f14vs_f14_volume_surge_accumulation_volcons_21d_jerk_v059_signal,
    f14vs_f14_volume_surge_accumulation_dvtrend_252d_jerk_v060_signal,
    f14vs_f14_volume_surge_accumulation_volrange_63d_jerk_v061_signal,
    f14vs_f14_volume_surge_accumulation_newsint_21d_jerk_v062_signal,
    f14vs_f14_volume_surge_accumulation_dvherf_63d_jerk_v063_signal,
    f14vs_f14_volume_surge_accumulation_volzimp_5d_jerk_v064_signal,
    f14vs_f14_volume_surge_accumulation_extspike_252d_jerk_v065_signal,
    f14vs_f14_volume_surge_accumulation_bigupday_63d_jerk_v066_signal,
    f14vs_f14_volume_surge_accumulation_volac1_63d_jerk_v067_signal,
    f14vs_f14_volume_surge_accumulation_dvsurgerank_jerk_v068_signal,
    f14vs_f14_volume_surge_accumulation_accbalz_126d_jerk_v069_signal,
    f14vs_f14_volume_surge_accumulation_surgefade_63d_jerk_v070_signal,
    f14vs_f14_volume_surge_accumulation_dvelevfrac_126d_jerk_v071_signal,
    f14vs_f14_volume_surge_accumulation_accindex_252d_jerk_v072_signal,
    f14vs_f14_volume_surge_accumulation_surgeclust_jerk_v073_signal,
    f14vs_f14_volume_surge_accumulation_eventint_63d_jerk_v074_signal,
    f14vs_f14_volume_surge_accumulation_dvzonset_21d_jerk_v075_signal,
    f14vs_f14_volume_surge_accumulation_volz_21d_jerk_v076_signal,
    f14vs_f14_volume_surge_accumulation_surge_5v21_jerk_v077_signal,
    f14vs_f14_volume_surge_accumulation_surge_21v252_jerk_v078_signal,
    f14vs_f14_volume_surge_accumulation_surge_63v252_jerk_v079_signal,
    f14vs_f14_volume_surge_accumulation_updn_5d_jerk_v080_signal,
    f14vs_f14_volume_surge_accumulation_updn_252d_jerk_v081_signal,
    f14vs_f14_volume_surge_accumulation_accslope_63d_jerk_v082_signal,
    f14vs_f14_volume_surge_accumulation_dvlevel_63d_jerk_v083_signal,
    f14vs_f14_volume_surge_accumulation_dvsurge_126d_jerk_v084_signal,
    f14vs_f14_volume_surge_accumulation_dvtrendz_63d_jerk_v085_signal,
    f14vs_f14_volume_surge_accumulation_accconfirm_63d_jerk_v086_signal,
    f14vs_f14_volume_surge_accumulation_newsvolprem_63d_jerk_v087_signal,
    f14vs_f14_volume_surge_accumulation_volretcorr_63d_jerk_v088_signal,
    f14vs_f14_volume_surge_accumulation_herf_252d_jerk_v089_signal,
    f14vs_f14_volume_surge_accumulation_top3share_21d_jerk_v090_signal,
    f14vs_f14_volume_surge_accumulation_scount80_63d_jerk_v091_signal,
    f14vs_f14_volume_surge_accumulation_scount95_252d_jerk_v092_signal,
    f14vs_f14_volume_surge_accumulation_uppertile_126d_jerk_v093_signal,
    f14vs_f14_volume_surge_accumulation_dvz_252d_jerk_v094_signal,
    f14vs_f14_volume_surge_accumulation_volxover_jerk_v095_signal,
    f14vs_f14_volume_surge_accumulation_volmacd_jerk_v096_signal,
    f14vs_f14_volume_surge_accumulation_dvflow_126d_jerk_v097_signal,
    f14vs_f14_volume_surge_accumulation_rankflow_63d_jerk_v098_signal,
    f14vs_f14_volume_surge_accumulation_volols_63d_jerk_v099_signal,
    f14vs_f14_volume_surge_accumulation_dvols_126d_jerk_v100_signal,
    f14vs_f14_volume_surge_accumulation_volboll_63d_jerk_v101_signal,
    f14vs_f14_volume_surge_accumulation_accpersist_63d_jerk_v102_signal,
    f14vs_f14_volume_surge_accumulation_vovratio_jerk_v103_signal,
    f14vs_f14_volume_surge_accumulation_dvmaxshare_63d_jerk_v104_signal,
    f14vs_f14_volume_surge_accumulation_surgesm_21d_jerk_v105_signal,
    f14vs_f14_volume_surge_accumulation_imbal_126d_jerk_v106_signal,
    f14vs_f14_volume_surge_accumulation_surgerank_504d_jerk_v107_signal,
    f14vs_f14_volume_surge_accumulation_dvdd_504d_jerk_v108_signal,
    f14vs_f14_volume_surge_accumulation_vwmove_63d_jerk_v109_signal,
    f14vs_f14_volume_surge_accumulation_volstreak_63d_jerk_v110_signal,
    f14vs_f14_volume_surge_accumulation_dvslopechg_jerk_v111_signal,
    f14vs_f14_volume_surge_accumulation_localpeaks_63d_jerk_v112_signal,
    f14vs_f14_volume_surge_accumulation_accrank_252d_jerk_v113_signal,
    f14vs_f14_volume_surge_accumulation_volzimp_21d_jerk_v114_signal,
    f14vs_f14_volume_surge_accumulation_herfratio_jerk_v115_signal,
    f14vs_f14_volume_surge_accumulation_dvsurgerank_504d_jerk_v116_signal,
    f14vs_f14_volume_surge_accumulation_accaccel_jerk_v117_signal,
    f14vs_f14_volume_surge_accumulation_volskew_126d_jerk_v118_signal,
    f14vs_f14_volume_surge_accumulation_effdays_126d_jerk_v119_signal,
    f14vs_f14_volume_surge_accumulation_climax_21d_jerk_v120_signal,
    f14vs_f14_volume_surge_accumulation_dvvov_63d_jerk_v121_signal,
    f14vs_f14_volume_surge_accumulation_surgeimp_5d_jerk_v122_signal,
    f14vs_f14_volume_surge_accumulation_distrib_63d_jerk_v123_signal,
    f14vs_f14_volume_surge_accumulation_vpdiverge_63d_jerk_v124_signal,
    f14vs_f14_volume_surge_accumulation_upherf_63d_jerk_v125_signal,
    f14vs_f14_volume_surge_accumulation_dvmomz_126d_jerk_v126_signal,
    f14vs_f14_volume_surge_accumulation_volrise_63d_jerk_v127_signal,
    f14vs_f14_volume_surge_accumulation_growth_504d_jerk_v128_signal,
    f14vs_f14_volume_surge_accumulation_accindex_504d_jerk_v129_signal,
    f14vs_f14_volume_surge_accumulation_volkurt_63d_jerk_v130_signal,
    f14vs_f14_volume_surge_accumulation_thrust_5d_jerk_v131_signal,
    f14vs_f14_volume_surge_accumulation_dvherf_126d_jerk_v132_signal,
    f14vs_f14_volume_surge_accumulation_volrangeexp_jerk_v133_signal,
    f14vs_f14_volume_surge_accumulation_accquality_63d_jerk_v134_signal,
    f14vs_f14_volume_surge_accumulation_signedvolz_21d_jerk_v135_signal,
    f14vs_f14_volume_surge_accumulation_dvprice_126d_jerk_v136_signal,
    f14vs_f14_volume_surge_accumulation_burstwin_126d_jerk_v137_signal,
    f14vs_f14_volume_surge_accumulation_volac5_126d_jerk_v138_signal,
    f14vs_f14_volume_surge_accumulation_surgesust_63d_jerk_v139_signal,
    f14vs_f14_volume_surge_accumulation_dvflowsm_126d_jerk_v140_signal,
    f14vs_f14_volume_surge_accumulation_excessvol_63d_jerk_v141_signal,
    f14vs_f14_volume_surge_accumulation_lowtile_252d_jerk_v142_signal,
    f14vs_f14_volume_surge_accumulation_accbreadth_252d_jerk_v143_signal,
    f14vs_f14_volume_surge_accumulation_volmrz_jerk_v144_signal,
    f14vs_f14_volume_surge_accumulation_dvtail_126d_jerk_v145_signal,
    f14vs_f14_volume_surge_accumulation_trendcons_jerk_v146_signal,
    f14vs_f14_volume_surge_accumulation_clustratio_jerk_v147_signal,
    f14vs_f14_volume_surge_accumulation_dvflowmom_jerk_v148_signal,
    f14vs_f14_volume_surge_accumulation_volzdisp_multi_jerk_v149_signal,
    f14vs_f14_volume_surge_accumulation_accregdist_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F14_VOLUME_SURGE_ACCUMULATION_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0003, 0.035, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(8e5, 5e5, n)) + 1e4, name="volume")

    cols = {"closeadj": closeadj, "volume": volume}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        args = [cols[c] for c in meta["inputs"]]
        y1 = meta["func"](*args)
        pd.testing.assert_series_equal(y1, meta["func"](*args))
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 20, "%s nunique=%d" % (name, q.nunique())
        assert q.std() > 0, name
        assert not q.isna().all(), name
        if y1.iloc[504:].isna().mean() < 0.5:
            nan_ok += 1
        results[name] = y1.iloc[504:]
        n_features += 1

    assert n_features == 150, n_features
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

    print("OK f14_volume_surge_accumulation_3rd_derivatives_001_150_claude: %d features pass" % n_features)
