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
    m = s.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(2, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rmax(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).min()


def _med(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).median()


# ===== folder domain primitives: RAW VOLUME SURGE / ACCUMULATION ONLY =====
# Dollar-volume (closeadj*volume) belongs to f17; turnover/Amihud belong to f16.
# closeadj is used ONLY for the SIGN of the daily return, never as a dollar multiplier.
def _f14_ret_sign(closeadj):
    return np.sign(closeadj.pct_change())


def _f14_surge_ratio(volume, w):
    base = volume.rolling(w, min_periods=max(2, w // 2)).mean()
    return volume / base.replace(0, np.nan)


def _f14_surge_excess(volume, w, k):
    base = volume.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = volume.rolling(w, min_periods=max(2, w // 2)).std()
    return ((volume - base) / sd.replace(0, np.nan) - k).clip(lower=0)


def _f14_signed_vol_norm(closeadj, volume, w):
    nvol = volume / _mean(volume, w).replace(0, np.nan)
    return _f14_ret_sign(closeadj) * nvol


def _f14_signed_surgez(closeadj, volume, w):
    vz = _z(volume, w)
    return _f14_ret_sign(closeadj) * vz


# ============================================================


def f14vs_f14_volume_surge_accumulation_surgeosc_21d_jerk_v001_signal(volume):
    fast = volume.ewm(span=5, min_periods=3).mean()
    slow = volume.ewm(span=21, min_periods=10).mean()
    b = (fast - slow) / slow.replace(0, np.nan)
    base = b
    result = base - 2.0 * base.shift(5) + base.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_surgemed_63d_jerk_v002_signal(volume):
    med = _med(volume, 63)
    b = volume / med.replace(0, np.nan) - 1.0
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_basedrift_126d_jerk_v003_signal(volume):
    med126 = _med(volume, 126)
    med252 = _med(volume, 252)
    b = np.log(med126.replace(0, np.nan) / med252.replace(0, np.nan))
    base = b
    result = base - 2.0 * base.shift(21) + base.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_q90excess_126d_jerk_v004_signal(volume):
    q90 = volume.rolling(126, min_periods=63).quantile(0.90)
    over = np.log(volume / q90.replace(0, np.nan)).clip(lower=0)
    energy = over.rolling(63, min_periods=32).sum()
    cnt = (volume > q90).astype(float).rolling(63, min_periods=32).sum()
    b = energy - 0.05 * cnt
    base = b
    result = base - 2.0 * base.shift(21) + base.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_surgeanom_63d_jerk_v005_signal(volume):
    fast = volume.ewm(span=10, min_periods=5).mean()
    ratio = fast / _mean(volume, 63).replace(0, np.nan)
    b = ratio - ratio.rolling(126, min_periods=63).mean()
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_surgeimp_21d_jerk_v006_signal(volume):
    sr = _f14_surge_ratio(volume, 21)
    b = sr - sr.shift(5)
    base = b
    result = base - 2.0 * base.shift(5) + base.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_peaksurge_21d_jerk_v007_signal(volume):
    peak = _rmax(volume, 21)
    base = _mean(volume, 63)
    b = peak / base.replace(0, np.nan)
    base = b
    result = base - 2.0 * base.shift(5) + base.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_quietloud_jerk_v008_signal(volume):
    base = _mean(volume, 21)
    quiet = _rmin(base, 126)
    b = np.log(base.replace(0, np.nan) / quiet.replace(0, np.nan))
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_blowoff_63d_jerk_v009_signal(volume):
    prom = _rmax(volume, 63) / _med(volume, 63).replace(0, np.nan)
    b = _z(prom, 252)
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_updown_21d_jerk_v010_signal(closeadj, volume):
    ret = closeadj.pct_change()
    up = volume.where(ret > 0, 0.0).rolling(21, min_periods=10).sum()
    dn = volume.where(ret < 0, 0.0).rolling(21, min_periods=10).sum()
    bal = (up - dn) / (up + dn).replace(0, np.nan)
    b = _z(bal, 252)
    base = b
    result = base - 2.0 * base.shift(5) + base.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_updown_63d_jerk_v011_signal(closeadj, volume):
    ret = closeadj.pct_change()
    up = volume.where(ret > 0, 0.0).rolling(63, min_periods=32).sum()
    dn = volume.where(ret < 0, 0.0).rolling(63, min_periods=32).sum()
    bal = (up - dn) / (up + dn).replace(0, np.nan)
    b = bal - bal.ewm(span=126, min_periods=63).mean()
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_updownchg_126d_jerk_v012_signal(closeadj, volume):
    ret = closeadj.pct_change()
    up = volume.where(ret > 0, 0.0).rolling(126, min_periods=63).sum()
    dn = volume.where(ret < 0, 0.0).rolling(126, min_periods=63).sum()
    bal = (up - dn) / (up + dn).replace(0, np.nan)
    b = bal - bal.shift(63)
    base = b
    result = base - 2.0 * base.shift(21) + base.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_dnintensity_63d_jerk_v013_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dn = volume.where(ret < 0, np.nan).rolling(126, min_periods=40).mean()
    up = volume.where(ret > 0, np.nan).rolling(126, min_periods=40).mean()
    r = np.log(dn / up.replace(0, np.nan))
    b = r - r.rolling(126, min_periods=63).mean()
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_bigupbias_21d_jerk_v014_signal(closeadj, volume):
    ret = closeadj.pct_change()
    thr = volume.rolling(63, min_periods=32).quantile(0.75)
    big = volume.where(volume >= thr, 0.0)
    bigup = big.where(ret > 0, 0.0)
    su = bigup.rolling(21, min_periods=10).sum()
    tot = big.rolling(21, min_periods=10).sum()
    b = su / tot.replace(0, np.nan) - 0.5
    base = b
    result = base - 2.0 * base.shift(5) + base.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_loudflow_63d_jerk_v015_signal(closeadj, volume):
    ret = closeadj.pct_change()
    thr = volume.rolling(63, min_periods=32).quantile(0.80)
    big = volume >= thr
    signed = (np.sign(ret) * volume).where(big, 0.0)
    net = signed.rolling(63, min_periods=32).sum()
    gross = volume.where(big, 0.0).rolling(63, min_periods=32).sum()
    b = net / gross.replace(0, np.nan)
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_udratioz_21d_jerk_v016_signal(closeadj, volume):
    ret = closeadj.pct_change()
    up = volume.where(ret > 0, 0.0).rolling(126, min_periods=63).sum()
    dn = volume.where(ret < 0, 0.0).rolling(126, min_periods=63).sum()
    r = np.log((up + 1.0) / (dn + 1.0))
    b = _z(r, 252)
    base = b
    result = base - 2.0 * base.shift(5) + base.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_upshare_252d_jerk_v017_signal(closeadj, volume):
    ret = closeadj.pct_change()
    up = volume.where(ret > 0, 0.0).rolling(252, min_periods=126).sum()
    tot = volume.rolling(252, min_periods=126).sum()
    b = up / tot.replace(0, np.nan) - 0.5
    base = b
    result = base - 2.0 * base.shift(21) + base.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_surgeasymmag_63d_jerk_v018_signal(closeadj, volume):
    ret = closeadj.pct_change()
    up = volume.where(ret > 0, np.nan).rolling(63, min_periods=20).max()
    dn = volume.where(ret < 0, np.nan).rolling(63, min_periods=20).max()
    b = np.log(up / dn.replace(0, np.nan))
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_surgecnt_63d_jerk_v019_signal(volume):
    b = _f14_surge_excess(volume, 63, 2.0).rolling(63, min_periods=32).sum()
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_surgecnt_126d_jerk_v020_signal(volume):
    b = _f14_surge_excess(volume, 126, 1.5).rolling(126, min_periods=63).sum()
    base = b
    result = base - 2.0 * base.shift(21) + base.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_burstcnt_21d_jerk_v021_signal(volume):
    base = _mean(volume, 63)
    sd = _std(volume, 63)
    burst = ((volume - base) / sd.replace(0, np.nan) - 1.5).clip(lower=0)
    b = burst.rolling(21, min_periods=10).sum()
    base = b
    result = base - 2.0 * base.shift(5) + base.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_climax_63d_jerk_v022_signal(volume):
    m = _mean(volume, 21)
    climax = (volume / m.replace(0, np.nan) - 1.6).clip(lower=0)
    b = climax.rolling(63, min_periods=32).sum()
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_surgepersist_63d_jerk_v023_signal(volume):
    sr = _f14_surge_ratio(volume, 63)
    hot = (sr - 1.5).clip(lower=0)
    b = hot.rolling(63, min_periods=32).mean()
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_surgeclust_63d_jerk_v024_signal(volume):
    base = _mean(volume, 63)
    sd = _std(volume, 63)
    exc = ((volume - base) / sd.replace(0, np.nan)).clip(lower=0)
    consec = exc * exc.shift(1)
    b = consec.rolling(63, min_periods=32).sum()
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_surgeasym_63d_jerk_v025_signal(closeadj, volume):
    ret = closeadj.pct_change()
    exc = _f14_surge_excess(volume, 63, 1.5)
    up = exc.where(ret > 0, 0.0).rolling(63, min_periods=32).sum()
    dn = exc.where(ret < 0, 0.0).rolling(63, min_periods=32).sum()
    b = up - dn
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_surgefreqtr_jerk_v026_signal(volume):
    cnt = _f14_surge_excess(volume, 63, 1.5).rolling(63, min_periods=32).sum()
    b = cnt - cnt.shift(63)
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_recspikes_63d_jerk_v027_signal(volume):
    exc = _f14_surge_excess(volume, 63, 1.5)
    def _wsum(a):
        return float((a * np.linspace(0.5, 1.5, len(a))).sum())
    b = exc.rolling(63, min_periods=32).apply(_wsum, raw=True)
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_newvolhi_21d_jerk_v028_signal(volume):
    rollmax = _rmax(volume, 63)
    isnew = (volume >= rollmax * 0.99999).astype(float)
    mag = volume / _mean(volume, 63).replace(0, np.nan)
    b = (isnew * mag).rolling(21, min_periods=10).sum()
    base = b
    result = base - 2.0 * base.shift(5) + base.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_surgerecency_63d_jerk_v029_signal(volume):
    def _f(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    b = volume.rolling(63, min_periods=32).apply(_f, raw=True)
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_surgespace_126d_jerk_v030_signal(volume):
    base = _mean(volume, 63)
    sd = _std(volume, 63)
    surge = (volume > base + 2.0 * sd).astype(float)
    cum = surge.cumsum()
    since = cum.groupby(cum).cumcount().astype(float)
    b = since.rolling(126, min_periods=63).mean()
    base = b
    result = base - 2.0 * base.shift(21) + base.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_hotstreak_jerk_v031_signal(volume):
    hot = (volume > _mean(volume, 21)).astype(float)
    grp = (hot != hot.shift(1)).cumsum()
    run = hot.groupby(grp).cumcount() + 1
    streak = run * hot
    mag = volume / _mean(volume, 21).replace(0, np.nan)
    b = streak * mag
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_maxrun_63d_jerk_v032_signal(volume):
    hot = (volume > _mean(volume, 21)).astype(float)
    grp = (hot != hot.shift(1)).cumsum()
    run = (hot.groupby(grp).cumcount() + 1) * hot
    b = _rmax(run, 63) * (_mean(volume, 21) / _mean(volume, 126).replace(0, np.nan))
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_accstreak_jerk_v033_signal(closeadj, volume):
    sign = _f14_ret_sign(closeadj).fillna(0.0)
    grp = (sign != sign.shift(1)).cumsum()
    run = sign.groupby(grp).cumcount() + 1
    b = (run * sign) * (volume / _mean(volume, 21).replace(0, np.nan))
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_topfrac_21d_jerk_v034_signal(volume):
    sr = _f14_surge_ratio(volume, 63)
    peak = _rmax(sr, 21)
    b = (sr - peak) / peak.replace(0, np.nan)
    base = b
    result = base - 2.0 * base.shift(5) + base.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_accflow_21d_jerk_v035_signal(closeadj, volume):
    sv = _f14_signed_vol_norm(closeadj, volume, 63)
    fast = sv.ewm(span=10, min_periods=5).mean()
    slow = sv.ewm(span=40, min_periods=20).mean()
    b = fast - slow
    base = b
    result = base - 2.0 * base.shift(5) + base.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_accaccel_21d_jerk_v036_signal(closeadj, volume):
    ret = closeadj.pct_change()
    flow = (np.sign(ret) * volume).rolling(21, min_periods=10).sum()
    tot = volume.rolling(21, min_periods=10).sum()
    tilt = flow / tot.replace(0, np.nan)
    b = tilt - tilt.shift(21)
    base = b
    result = base - 2.0 * base.shift(5) + base.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_acceff_21d_jerk_v037_signal(closeadj, volume):
    ret = closeadj.pct_change()
    signed = np.sign(ret) * volume
    net = signed.rolling(21, min_periods=10).sum().abs()
    path = signed.abs().rolling(21, min_periods=10).sum()
    eff = net / path.replace(0, np.nan)
    loud = _mean(volume, 21) / _mean(volume, 126).replace(0, np.nan)
    b = eff * loud
    base = b
    result = base - 2.0 * base.shift(5) + base.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_accdist_63d_jerk_v038_signal(closeadj, volume):
    line = _f14_signed_surgez(closeadj, volume, 63).cumsum()
    b = (line - _mean(line, 63)) / _std(line, 63).replace(0, np.nan)
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_accslope_21d_jerk_v039_signal(closeadj, volume):
    line = _f14_signed_surgez(closeadj, volume, 63).cumsum()
    b = (line - line.shift(21)) / 21.0
    base = b
    result = base - 2.0 * base.shift(5) + base.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_accslope_63d_jerk_v040_signal(closeadj, volume):
    line = _f14_signed_surgez(closeadj, volume, 63).cumsum()
    b = (line - line.shift(63)) / 63.0
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_acccurv_126d_jerk_v041_signal(closeadj, volume):
    line = _f14_signed_surgez(closeadj, volume, 126).cumsum()
    recent = (line - line.shift(21)) / 21.0
    prior = (line.shift(21) - line.shift(126)) / 105.0
    b = recent - prior
    base = b
    result = base - 2.0 * base.shift(21) + base.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_accstall_126d_jerk_v042_signal(closeadj, volume):
    line = _f14_signed_surgez(closeadj, volume, 63).cumsum()
    peak = _rmax(line, 126)
    span = (_rmax(line, 126) - _rmin(line, 126)).replace(0, np.nan)
    b = (line - peak) / span
    base = b
    result = base - 2.0 * base.shift(21) + base.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_accgap_126d_jerk_v043_signal(closeadj, volume):
    line = _f14_signed_surgez(closeadj, volume, 63).cumsum()
    def _f(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    b = line.rolling(126, min_periods=63).apply(_f, raw=True)
    base = b
    result = base - 2.0 * base.shift(21) + base.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_accrun_jerk_v044_signal(closeadj, volume):
    line = _f14_signed_surgez(closeadj, volume, 63).cumsum()
    up = (line.diff() > 0).astype(float)
    grp = (up != up.shift(1)).cumsum()
    run = (up.groupby(grp).cumcount() + 1)
    signed = run * (2 * up - 1)
    b = signed * (volume / _mean(volume, 63).replace(0, np.nan))
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_accmom_63d_jerk_v045_signal(closeadj, volume):
    ret = closeadj.pct_change()
    net = (np.sign(ret) * volume).rolling(63, min_periods=32).sum()
    b = net.rank(pct=True) - net.shift(63).rank(pct=True)
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_duracc_252d_jerk_v046_signal(closeadj, volume):
    tilt = _f14_signed_vol_norm(closeadj, volume, 126).rolling(21, min_periods=10).mean()
    up = tilt.clip(lower=0).rolling(252, min_periods=126).mean()
    dn = (-tilt).clip(lower=0).rolling(252, min_periods=126).mean()
    b = up - dn
    base = b
    result = base - 2.0 * base.shift(21) + base.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_accbreadth_21d_jerk_v047_signal(closeadj, volume):
    contrib = _f14_signed_vol_norm(closeadj, volume, 63)
    b = contrib.rolling(21, min_periods=10).std()
    base = b
    result = base - 2.0 * base.shift(5) + base.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_episode_126d_jerk_v048_signal(closeadj, volume):
    ret = closeadj.pct_change()
    sr = _f14_surge_ratio(volume, 63)
    big = (sr - 1.5).clip(lower=0)
    net = (np.sign(ret) * big).rolling(126, min_periods=63).sum()
    gross = big.rolling(126, min_periods=63).sum()
    b = net / gross.replace(0, np.nan)
    base = b
    result = base - 2.0 * base.shift(21) + base.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_logexp_21v63_jerk_v049_signal(volume):
    lv = np.log(volume.clip(lower=1.0))
    b = _mean(lv, 21) - _mean(lv, 63)
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_volexpand_21d_jerk_v050_signal(volume):
    m = _mean(volume, 21)
    b = (m - m.shift(63)) / m.shift(63).replace(0, np.nan)
    base = b
    result = base - 2.0 * base.shift(5) + base.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_volfloor_63d_jerk_v051_signal(volume):
    fl = _rmin(volume, 63)
    b = np.log(fl.replace(0, np.nan) / fl.shift(63).replace(0, np.nan))
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_madregime_252d_jerk_v052_signal(volume):
    med63 = _med(volume, 63)
    med252 = _med(volume, 252)
    mad252 = (volume - med252).abs().rolling(252, min_periods=126).median()
    b = (med63 - med252) / (1.4826 * mad252).replace(0, np.nan)
    base = b
    result = base - 2.0 * base.shift(21) + base.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_surgewidth_jerk_v053_signal(volume):
    sr = _f14_surge_ratio(volume, 63)
    b = _rmax(sr, 21) - _rmin(sr, 21)
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_surgedisp_jerk_v054_signal(volume):
    s1 = _f14_surge_ratio(volume, 5)
    s2 = _f14_surge_ratio(volume, 21)
    s3 = _f14_surge_ratio(volume, 63)
    b = pd.concat([s1, s2, s3], axis=1).std(axis=1)
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_wksurge_jerk_v055_signal(volume):
    wk = volume.rolling(5).sum()
    base = _mean(wk, 63)
    b = wk / base.replace(0, np.nan) - 1.0
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_afterglow_jerk_v056_signal(volume):
    sr = _f14_surge_ratio(volume, 63)
    decayed = sr.ewm(halflife=10, min_periods=5).mean()
    slow = sr.rolling(63, min_periods=32).mean()
    b = decayed - slow
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_followthru_jerk_v057_signal(volume):
    thr = volume.rolling(126, min_periods=63).quantile(0.85)
    spike = (volume.shift(1) >= thr.shift(1))
    nextvol = (volume / _mean(volume, 63).replace(0, np.nan)).where(spike, np.nan)
    b = nextvol.rolling(126, min_periods=10).mean()
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_burstdecay_jerk_v058_signal(volume):
    prior5 = volume.shift(1).rolling(5, min_periods=3).max()
    ratio = volume / prior5.replace(0, np.nan)
    b = _z(ratio, 63)
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_surgereact_126d_jerk_v059_signal(closeadj, volume):
    ret = closeadj.pct_change()
    thr = volume.rolling(126, min_periods=63).quantile(0.85)
    bigret = ret.where(volume >= thr, np.nan)
    bigmean = bigret.rolling(126, min_periods=10).mean()
    allmean = ret.rolling(126, min_periods=63).mean()
    b = bigmean - allmean
    base = b
    result = base - 2.0 * base.shift(21) + base.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_climaxrev_jerk_v060_signal(closeadj, volume):
    ret = closeadj.pct_change()
    prior = closeadj.shift(1) / closeadj.shift(6) - 1.0
    sr = _f14_surge_ratio(volume, 63)
    reversal = -np.sign(ret) * np.sign(prior) * (sr - 1.0).clip(lower=0)
    b = reversal.rolling(21, min_periods=10).mean()
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_roveff_63d_jerk_v061_signal(closeadj, volume):
    roc = closeadj / closeadj.shift(63) - 1.0
    avgsurge = _mean(_f14_surge_ratio(volume, 63), 63)
    b = roc / avgsurge.replace(0, np.nan)
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_vwret_21d_jerk_v062_signal(closeadj, volume):
    ar = closeadj.pct_change().abs()
    sr = _f14_surge_ratio(volume, 63)
    b = sr.rolling(21, min_periods=10).corr(ar)
    base = b
    result = base - 2.0 * base.shift(5) + base.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_thrust_21d_jerk_v063_signal(closeadj, volume):
    ar = closeadj.pct_change().abs()
    volspike = (volume > volume.rolling(63, min_periods=32).quantile(0.85)).astype(float)
    quiet = (ar < ar.rolling(63, min_periods=32).quantile(0.50)).astype(float)
    silent = (volspike * quiet).rolling(63, min_periods=32).sum()
    base = volspike.rolling(63, min_periods=32).sum()
    b = silent / base.replace(0, np.nan)
    base = b
    result = base - 2.0 * base.shift(5) + base.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_flowdiv_63d_jerk_v064_signal(closeadj, volume):
    ret = closeadj.pct_change()
    flow = (np.sign(ret) * volume).rolling(63, min_periods=32).sum()
    flow_n = flow / volume.rolling(63, min_periods=32).sum().replace(0, np.nan)
    price = closeadj / closeadj.shift(63) - 1.0
    b = flow_n - np.tanh(price)
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_upsurge_63d_jerk_v065_signal(closeadj, volume):
    ret = closeadj.pct_change()
    sr = _f14_surge_ratio(volume, 63) - 1.0
    b = sr.where(ret > 0, 0.0)
    b = b.rolling(21, min_periods=10).mean()
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_dnsurge_63d_jerk_v066_signal(closeadj, volume):
    ret = closeadj.pct_change()
    sr = _f14_surge_ratio(volume, 63) - 1.0
    b = sr.where(ret < 0, 0.0)
    b = b.rolling(21, min_periods=10).mean()
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_signsurge_21d_jerk_v067_signal(closeadj, volume):
    ret = closeadj.pct_change()
    sr = _f14_surge_ratio(volume, 63)
    big = (sr >= sr.rolling(63, min_periods=32).quantile(0.75))
    upbig = (big & (ret > 0)).astype(float).rolling(63, min_periods=32).sum()
    dnbig = (big & (ret < 0)).astype(float).rolling(63, min_periods=32).sum()
    b = (upbig - dnbig) / (upbig + dnbig).replace(0, np.nan)
    base = b
    result = base - 2.0 * base.shift(5) + base.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_volrank_252d_jerk_v068_signal(volume):
    base = _mean(volume, 21)
    b = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    base = b
    result = base - 2.0 * base.shift(21) + base.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_surgerank_252d_jerk_v069_signal(volume):
    sr = _mean(_f14_surge_ratio(volume, 63), 5)
    rk = sr.rolling(252, min_periods=63).rank(pct=True)
    b = rk - rk.shift(21)
    base = b
    result = base - 2.0 * base.shift(21) + base.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_volregpos_252d_jerk_v070_signal(volume):
    base = _mean(volume, 21)
    hi = _rmax(base, 252)
    lo = _rmin(base, 252)
    b = (base - lo) / (hi - lo).replace(0, np.nan)
    base = b
    result = base - 2.0 * base.shift(21) + base.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_surgevol_63d_jerk_v071_signal(volume):
    sr = _f14_surge_ratio(volume, 63)
    b = sr.rolling(63, min_periods=32).std()
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_surgemomz_jerk_v072_signal(volume):
    sr = _f14_surge_ratio(volume, 21)
    chg = sr - sr.shift(10)
    b = _z(chg, 126)
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_voltrendcon_63d_jerk_v073_signal(volume):
    m = _mean(volume, 63)
    above = (volume > m).astype(float)
    b = above.rolling(63, min_periods=32).mean() - 0.5
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_volaccel_21d_jerk_v074_signal(volume):
    m = _mean(volume, 21)
    r = m / m.shift(21).replace(0, np.nan)
    b = r - r.shift(21)
    base = b
    result = base - 2.0 * base.shift(5) + base.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_volstretch_jerk_v075_signal(volume):
    slow = volume.ewm(span=200, min_periods=100).mean()
    above = (volume > slow).astype(float)
    b = above.rolling(63, min_periods=32).mean() - 0.5
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_surgetanh_21d_jerk_v076_signal(volume):
    sr = _f14_surge_ratio(volume, 63)
    b = np.tanh(sr - 1.0).rolling(21, min_periods=10).mean()
    base = b
    result = base - 2.0 * base.shift(5) + base.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_logsurge_126d_jerk_v077_signal(volume):
    sr = _f14_surge_ratio(volume, 126)
    b = np.log(sr.replace(0, np.nan))
    base = b
    result = base - 2.0 * base.shift(21) + base.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_surgesqrt_63d_jerk_v078_signal(volume):
    sr = _f14_surge_ratio(volume, 126)
    typ = sr.rolling(126, min_periods=63).median()
    d = sr - typ
    b = np.sign(d) * d.abs() ** 0.5
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_surge5v63_jerk_v079_signal(volume):
    s10 = _mean(volume, 10)
    base = _mean(volume, 126)
    r = np.log(s10.replace(0, np.nan) / base.replace(0, np.nan))
    b = r - r.rolling(63, min_periods=32).mean()
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_surgeaccel_jerk_v080_signal(volume):
    sr = _f14_surge_ratio(volume, 63)
    slope = sr - sr.shift(21)
    b = slope - slope.shift(21)
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_meanexcess_63d_jerk_v081_signal(volume):
    base = _mean(volume, 63)
    sd = _std(volume, 63)
    z = (volume - base) / sd.replace(0, np.nan)
    pos = z.where(z > 0, np.nan)
    b = pos.rolling(63, min_periods=20).mean()
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_burstchg_21d_jerk_v082_signal(volume):
    cnt = _f14_surge_excess(volume, 63, 1.5).rolling(21, min_periods=10).sum()
    b = cnt - cnt.shift(63)
    base = b
    result = base - 2.0 * base.shift(5) + base.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_surgedrought_jerk_v083_signal(volume):
    base = _mean(volume, 63)
    sd = _std(volume, 63)
    calm = (volume <= base + 2.0 * sd).astype(float)
    grp = (calm != calm.shift(1)).cumsum()
    run = (calm.groupby(grp).cumcount() + 1) * calm
    floor = _rmin(_f14_surge_ratio(volume, 63), 21)
    b = _rmax(run, 126) * floor
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_broadheat_126d_jerk_v084_signal(volume):
    base = _mean(volume, 126)
    heat = (volume / base.replace(0, np.nan) - 1.0).clip(lower=0)
    b = heat.rolling(126, min_periods=63).mean()
    base = b
    result = base - 2.0 * base.shift(21) + base.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_spikefloor_21d_jerk_v085_signal(volume):
    hi = _rmax(volume, 21)
    lo = _rmin(volume, 21)
    b = np.log(hi.replace(0, np.nan) / lo.replace(0, np.nan))
    base = b
    result = base - 2.0 * base.shift(5) + base.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_dirspike_63d_jerk_v086_signal(closeadj, volume):
    ret = closeadj.pct_change()
    exc = _f14_surge_excess(volume, 63, 1.0)
    up = exc.where(ret > 0, 0.0).rolling(63, min_periods=32).sum()
    dn = exc.where(ret < 0, 0.0).rolling(63, min_periods=32).sum()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_wkflow_jerk_v087_signal(closeadj, volume):
    ret5 = closeadj / closeadj.shift(5) - 1.0
    wkvol = volume.rolling(5).sum()
    signed = np.sign(ret5) * wkvol
    net = signed.rolling(63, min_periods=32).sum()
    tot = wkvol.rolling(63, min_periods=32).sum()
    b = net / tot.replace(0, np.nan)
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_wkbreadth_jerk_v088_signal(closeadj, volume):
    ret5 = closeadj / closeadj.shift(5) - 1.0
    wkvol = volume.rolling(5).sum()
    nv = wkvol / _mean(wkvol, 63).replace(0, np.nan)
    contrib = np.sign(ret5) * nv
    b = contrib.rolling(126, min_periods=63).mean()
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_voldirpow_126d_jerk_v089_signal(closeadj, volume):
    ret = closeadj.pct_change()
    nv = volume / _mean(volume, 126).replace(0, np.nan)
    up = (nv.where(ret > 0, 0.0) ** 1.5).rolling(126, min_periods=63).mean()
    dn = (nv.where(ret < 0, 0.0) ** 1.5).rolling(126, min_periods=63).mean()
    b = up - dn
    base = b
    result = base - 2.0 * base.shift(21) + base.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_acceff_63d_jerk_v090_signal(closeadj, volume):
    line = _f14_signed_surgez(closeadj, volume, 63).cumsum()
    net = (line - line.shift(63)).abs()
    path = line.diff().abs().rolling(63, min_periods=32).sum()
    b = net / path.replace(0, np.nan)
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_flowspread_jerk_v091_signal(closeadj, volume):
    ret = closeadj.pct_change()
    sv = np.sign(ret) * volume
    t21 = sv.rolling(21, min_periods=10).sum() / volume.rolling(21, min_periods=10).sum().replace(0, np.nan)
    t63 = sv.rolling(63, min_periods=32).sum() / volume.rolling(63, min_periods=32).sum().replace(0, np.nan)
    b = t21 - t63
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_flowmom_jerk_v092_signal(closeadj, volume):
    ret = closeadj.pct_change()
    sv = np.sign(ret) * volume
    t21 = sv.rolling(21, min_periods=10).sum() / volume.rolling(21, min_periods=10).sum().replace(0, np.nan)
    t63 = sv.rolling(63, min_periods=32).sum() / volume.rolling(63, min_periods=32).sum().replace(0, np.nan)
    spread = t21 - t63
    b = spread - spread.shift(21)
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_distrwarn_jerk_v093_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dnvol = volume.where(ret < 0, np.nan).rolling(21, min_periods=8).mean()
    allvol = _mean(volume, 21)
    b = np.log(dnvol / allvol.replace(0, np.nan))
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_accpersist_252d_jerk_v094_signal(closeadj, volume):
    ret = closeadj.pct_change()
    tilt = (np.sign(ret) * volume).rolling(21, min_periods=10).sum() \
        / volume.rolling(21, min_periods=10).sum().replace(0, np.nan)
    pos = (tilt > 0).astype(float)
    b = pos.rolling(252, min_periods=126).mean() - 0.5
    base = b
    result = base - 2.0 * base.shift(21) + base.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_voleffort_63d_jerk_v095_signal(closeadj, volume):
    surge_rk = _mean(_f14_surge_ratio(volume, 63), 21).rolling(252, min_periods=63).rank(pct=True)
    move = (closeadj / closeadj.shift(63) - 1.0).abs()
    move_rk = move.rolling(252, min_periods=63).rank(pct=True)
    b = surge_rk - move_rk
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_exhaust_63d_jerk_v096_signal(closeadj, volume):
    ret = closeadj.pct_change()
    exc = _f14_surge_excess(volume, 63, 1.0)
    rev = (np.sign(ret) != np.sign(ret.shift(1))).astype(float)
    b = (exc * rev).rolling(63, min_periods=32).sum()
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_loudagree_63d_jerk_v097_signal(closeadj, volume):
    ret = closeadj.pct_change()
    thr = volume.rolling(63, min_periods=32).quantile(0.92)
    big = volume >= thr
    signs = (np.sign(ret) * big.astype(float))
    netsign = signs.rolling(63, min_periods=32).sum()
    count = big.astype(float).rolling(63, min_periods=32).sum()
    b = netsign / count.replace(0, np.nan)
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_movepersurge_jerk_v098_signal(closeadj, volume):
    ret = closeadj.pct_change()
    exc = (_f14_surge_ratio(volume, 63) - 1.0).clip(lower=0)
    upmove = (ret.where(ret > 0, 0.0) * exc).rolling(63, min_periods=32).sum()
    dnmove = (ret.where(ret < 0, 0.0).abs() * exc).rolling(63, min_periods=32).sum()
    b = (upmove - dnmove) / (upmove + dnmove).replace(0, np.nan)
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_surgestreak_jerk_v099_signal(volume):
    sr = _f14_surge_ratio(volume, 63)
    hot = (sr > 1.25).astype(float)
    grp = (hot != hot.shift(1)).cumsum()
    run = (hot.groupby(grp).cumcount() + 1) * hot
    b = run * sr
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_quietstreak_jerk_v100_signal(volume):
    m = _mean(volume, 21)
    cool = (volume < m).astype(float)
    grp = (cool != cool.shift(1)).cumsum()
    run = (cool.groupby(grp).cumcount() + 1) * cool
    depth = (m / volume.replace(0, np.nan)).clip(lower=1.0)
    b = run * depth
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_postpeak_jerk_v101_signal(volume):
    sr = _f14_surge_ratio(volume, 63)
    q75 = sr.rolling(63, min_periods=32).quantile(0.75)
    q25 = sr.rolling(63, min_periods=32).quantile(0.25)
    b = q75 - q25
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_presurgecalm_jerk_v102_signal(volume):
    sr = _f14_surge_ratio(volume, 63)
    b = _rmin(sr, 21)
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_surgedecay_jerk_v103_signal(volume):
    exc = _f14_surge_excess(volume, 63, 1.0)
    recent = exc.rolling(5, min_periods=3).sum()
    older = exc.shift(5).rolling(16, min_periods=8).sum()
    b = recent / (recent + older).replace(0, np.nan)
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_surgedrift_63d_jerk_v104_signal(volume):
    sr = _f14_surge_ratio(volume, 63)
    def _slope(a):
        x = np.arange(len(a), dtype=float)
        xc = x - x.mean()
        denom = (xc ** 2).sum()
        if denom == 0:
            return np.nan
        return float((xc * (a - a.mean())).sum() / denom)
    b = sr.rolling(63, min_periods=32).apply(_slope, raw=True)
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_expconvex_jerk_v105_signal(volume):
    a = np.log(_mean(volume, 5).replace(0, np.nan) / _mean(volume, 21).replace(0, np.nan))
    c = np.log(_mean(volume, 21).replace(0, np.nan) / _mean(volume, 63).replace(0, np.nan))
    b = a - c
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_volyoy_jerk_v106_signal(volume):
    m = _mean(volume, 63)
    b = np.log(m.replace(0, np.nan) / m.shift(252).replace(0, np.nan))
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_volmom_step_jerk_v107_signal(volume):
    m = _mean(volume, 21)
    step = np.log(m.replace(0, np.nan) / m.shift(21).replace(0, np.nan))
    b = step - step.shift(21)
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_surgepctl_252d_jerk_v108_signal(volume):
    sr = _mean(_f14_surge_ratio(volume, 21), 5)
    b = (sr.rolling(252, min_periods=63).rank(pct=True) - 0.5).abs()
    base = b
    result = base - 2.0 * base.shift(21) + base.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_surgejitter_21d_jerk_v109_signal(volume):
    sr = _f14_surge_ratio(volume, 63)
    b = sr.rolling(21, min_periods=10).std() / sr.rolling(21, min_periods=10).mean().replace(0, np.nan)
    base = b
    result = base - 2.0 * base.shift(5) + base.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_surgevolchg_jerk_v110_signal(volume):
    sr = _f14_surge_ratio(volume, 63)
    sv = sr.rolling(63, min_periods=32).std()
    b = sv - sv.shift(63)
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_surgeswing_63d_jerk_v111_signal(volume):
    sr = _f14_surge_ratio(volume, 63)
    peak = _rmax(sr, 63)
    med = sr.rolling(63, min_periods=32).median()
    b = peak / med.replace(0, np.nan)
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_surgeclump_jerk_v112_signal(volume):
    exc = _f14_surge_excess(volume, 63, 1.0)
    win5 = exc.rolling(5, min_periods=3).sum()
    top5 = _rmax(win5, 63)
    tot = exc.rolling(63, min_periods=32).sum()
    b = top5 / tot.replace(0, np.nan)
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_surgez_252d_jerk_v113_signal(volume):
    sr = _mean(_f14_surge_ratio(volume, 63), 21)
    b = _z(sr, 252)
    base = b
    result = base - 2.0 * base.shift(21) + base.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_volregpos_504d_jerk_v114_signal(volume):
    base = _mean(volume, 63)
    hi = _rmax(base, 504)
    lo = _rmin(base, 504)
    b = (base - lo) / (hi - lo).replace(0, np.nan)
    base = b
    result = base - 2.0 * base.shift(21) + base.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_floorlift_252d_jerk_v115_signal(volume):
    base = _mean(volume, 63)
    floor = _rmin(base, 252)
    b = np.log(base.replace(0, np.nan) / floor.replace(0, np.nan))
    base = b
    result = base - 2.0 * base.shift(21) + base.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_ceilroom_252d_jerk_v116_signal(volume):
    base = _mean(volume, 63)
    ceil = _rmax(base, 252)
    b = np.log(base.replace(0, np.nan) / ceil.replace(0, np.nan))
    base = b
    result = base - 2.0 * base.shift(21) + base.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_partfade_jerk_v117_signal(volume):
    base = _mean(volume, 63)
    dd = base / _rmax(base, 252).replace(0, np.nan) - 1.0
    b = dd - dd.shift(63)
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_netsurge_126d_jerk_v118_signal(closeadj, volume):
    sign = _f14_ret_sign(closeadj)
    exc = _f14_surge_excess(volume, 126, 1.0)
    b = (sign * exc).rolling(126, min_periods=63).sum()
    base = b
    result = base - 2.0 * base.shift(21) + base.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_surgemomflow_jerk_v119_signal(closeadj, volume):
    sign = _f14_ret_sign(closeadj)
    exc = _f14_surge_excess(volume, 63, 1.0)
    flow = (sign * exc).rolling(21, min_periods=10).sum()
    b = flow - flow.rolling(126, min_periods=63).mean()
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_buyshare_63d_jerk_v120_signal(closeadj, volume):
    ret = closeadj.pct_change()
    exc = _f14_surge_excess(volume, 63, 1.5)
    upenergy = (exc * volume).where(ret > 0, 0.0).rolling(63, min_periods=32).sum()
    totvol = volume.rolling(63, min_periods=32).sum()
    b = upenergy / totvol.replace(0, np.nan)
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_dirtiltmom_jerk_v121_signal(closeadj, volume):
    ret = closeadj.pct_change()
    exc = _f14_surge_excess(volume, 63, 1.0)
    up = exc.where(ret > 0, 0.0).rolling(63, min_periods=32).sum()
    dn = exc.where(ret < 0, 0.0).rolling(63, min_periods=32).sum()
    bal = (up - dn) / (up + dn).replace(0, np.nan)
    b = bal - bal.shift(63)
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_wksurgez_jerk_v122_signal(closeadj, volume):
    ret5 = closeadj / closeadj.shift(5) - 1.0
    wk = volume.rolling(5).sum()
    tilt = np.sign(ret5) * wk
    sm = tilt.rolling(21, min_periods=10).sum() / wk.rolling(21, min_periods=10).sum().replace(0, np.nan)
    b = _z(sm, 63)
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_wkaccel_jerk_v123_signal(volume):
    wk = volume.rolling(5).sum()
    r = np.log(wk.replace(0, np.nan) / wk.shift(5).replace(0, np.nan))
    b = r - r.shift(20)
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_dayspike_jerk_v124_signal(volume):
    daymax = _rmax(volume, 5)
    wk = volume.rolling(5, min_periods=3).sum()
    b = daymax / wk.replace(0, np.nan)
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_extspike_126d_jerk_v125_signal(volume):
    sr = _f14_surge_ratio(volume, 63)
    b = (sr - 1.8).clip(lower=0).rolling(126, min_periods=63).sum()
    base = b
    result = base - 2.0 * base.shift(21) + base.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_tailshape_126d_jerk_v126_signal(volume):
    base = _mean(volume, 126)
    sd = _std(volume, 126)
    z = (volume - base) / sd.replace(0, np.nan)
    c1 = (z > 1.0).astype(float).rolling(126, min_periods=63).sum()
    c2 = (z > 2.0).astype(float).rolling(126, min_periods=63).sum()
    b = c2 / (c1 + 1.0)
    base = b
    result = base - 2.0 * base.shift(21) + base.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_surgeyoy_jerk_v127_signal(volume):
    cnt = _f14_surge_excess(volume, 63, 1.5).rolling(63, min_periods=32).sum()
    b = cnt - cnt.shift(252)
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_hiregime_252d_jerk_v128_signal(volume):
    base = _mean(volume, 21)
    med = _med(base, 252)
    above = (base > med).astype(float)
    b = above.rolling(252, min_periods=126).mean() - 0.5
    base = b
    result = base - 2.0 * base.shift(21) + base.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_regcross_252d_jerk_v129_signal(volume):
    base = _mean(volume, 21)
    med = _med(base, 252)
    above = (base > med).astype(float)
    cross = (above != above.shift(1)).astype(float)
    b = cross.rolling(252, min_periods=126).sum()
    base = b
    result = base - 2.0 * base.shift(21) + base.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_accdist_252d_jerk_v130_signal(closeadj, volume):
    line = _f14_signed_surgez(closeadj, volume, 126).cumsum()
    b = (line - _mean(line, 252)) / _std(line, 252).replace(0, np.nan)
    base = b
    result = base - 2.0 * base.shift(21) + base.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_flowsignmag_jerk_v131_signal(closeadj, volume):
    ret = closeadj.pct_change()
    tilt = (np.sign(ret) * volume).rolling(63, min_periods=32).sum() \
        / volume.rolling(63, min_periods=32).sum().replace(0, np.nan)
    b = np.sign(tilt) * tilt.abs() ** 0.5
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_flowdisp_jerk_v132_signal(closeadj, volume):
    sv = _f14_signed_vol_norm(closeadj, volume, 63)
    tilt = sv.rolling(21, min_periods=10).mean()
    b = tilt - tilt.ewm(span=63, min_periods=21).mean()
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_accnewhi_252d_jerk_v133_signal(closeadj, volume):
    line = _f14_signed_surgez(closeadj, volume, 126).cumsum()
    def _f(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    b = line.rolling(252, min_periods=126).apply(_f, raw=True)
    base = b
    result = base - 2.0 * base.shift(21) + base.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_flowpricediv_jerk_v134_signal(closeadj, volume):
    ret = closeadj.pct_change()
    flow = (np.sign(ret) * volume).rolling(63, min_periods=32).sum() \
        / volume.rolling(63, min_periods=32).sum().replace(0, np.nan)
    flow_rk = flow.rolling(252, min_periods=63).rank(pct=True)
    roc = closeadj / closeadj.shift(63) - 1.0
    roc_rk = roc.rolling(252, min_periods=63).rank(pct=True)
    b = flow_rk - roc_rk
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_surgevoldiv_jerk_v135_signal(closeadj, volume):
    surge_rk = _mean(_f14_surge_ratio(volume, 63), 21).rolling(252, min_periods=63).rank(pct=True)
    rv = closeadj.pct_change().rolling(63, min_periods=32).std()
    rv_rk = rv.rolling(252, min_periods=63).rank(pct=True)
    b = surge_rk - rv_rk
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_vwret_63d_jerk_v136_signal(closeadj, volume):
    ret = closeadj.pct_change()
    thr = volume.rolling(126, min_periods=63).quantile(0.75)
    bigstd = ret.where(volume >= thr, np.nan).rolling(126, min_periods=20).std()
    allstd = ret.rolling(126, min_periods=63).std()
    b = bigstd / allstd.replace(0, np.nan) - 1.0
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_impactasym_jerk_v137_signal(closeadj, volume):
    ar = closeadj.pct_change().abs()
    thr = volume.rolling(126, min_periods=63).quantile(0.80)
    surge = ar.where(volume >= thr, np.nan).rolling(126, min_periods=20).mean()
    calm = ar.where(volume < thr, np.nan).rolling(126, min_periods=20).mean()
    b = np.log(surge / calm.replace(0, np.nan))
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_surgedispema_jerk_v138_signal(volume):
    lo21 = _rmin(volume, 21)
    lo63 = _rmin(volume, 63)
    b = np.log(lo21.replace(0, np.nan) / lo63.replace(0, np.nan))
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_surgeema_jerk_v139_signal(volume):
    sr = _f14_surge_ratio(volume, 63)
    b = sr.ewm(span=21, min_periods=10).mean() - 1.0
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_logvolstretch_jerk_v140_signal(volume):
    lv = np.log(volume.clip(lower=1.0))
    b = (lv - lv.ewm(span=63, min_periods=21).mean()).rolling(10, min_periods=5).mean()
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_q75frac_21d_jerk_v141_signal(volume):
    q75 = volume.rolling(63, min_periods=32).quantile(0.75)
    over = np.log(volume / q75.replace(0, np.nan)).clip(lower=0)
    energy = over.rolling(21, min_periods=10).sum()
    cnt = (volume > q75).astype(float).rolling(21, min_periods=10).sum()
    b = energy - 0.05 * cnt
    base = b
    result = base - 2.0 * base.shift(5) + base.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_medsym_63d_jerk_v142_signal(volume):
    med = _med(volume, 63)
    d = np.sign(volume - med) * np.log1p((volume - med).abs() / med.replace(0, np.nan))
    b = d.rolling(21, min_periods=10).mean()
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_surgehotcnt_63d_jerk_v143_signal(volume):
    sr = _f14_surge_ratio(volume, 63)
    b = sr.rolling(63, min_periods=32).mean() - sr.rolling(63, min_periods=32).median()
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_regimeratio_jerk_v144_signal(volume):
    s21 = _mean(_f14_surge_ratio(volume, 21), 21)
    s126 = _mean(_f14_surge_ratio(volume, 126), 21)
    b = s21 / s126.replace(0, np.nan)
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_accbaltrend_jerk_v145_signal(closeadj, volume):
    ret = closeadj.pct_change()
    up = volume.where(ret > 0, 0.0).rolling(21, min_periods=10).sum()
    dn = volume.where(ret < 0, 0.0).rolling(21, min_periods=10).sum()
    bal = (up - dn) / (up + dn).replace(0, np.nan)
    b = bal - bal.shift(63)
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_loudtilt_126d_jerk_v146_signal(closeadj, volume):
    ret = closeadj.pct_change()
    thr = volume.rolling(126, min_periods=63).quantile(0.92)
    big = volume >= thr
    netsign = (np.sign(ret) * big.astype(float)).rolling(126, min_periods=63).sum()
    cnt = big.astype(float).rolling(126, min_periods=63).sum()
    b = netsign / cnt.replace(0, np.nan)
    base = b
    result = base - 2.0 * base.shift(21) + base.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_peakgap_jerk_v147_signal(volume):
    sr = _f14_surge_ratio(volume, 21)
    peak = _rmax(sr, 63)
    b = sr / peak.replace(0, np.nan) - 1.0
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_acceff_126d_jerk_v148_signal(closeadj, volume):
    ret = closeadj.pct_change()
    signed = np.sign(ret) * volume
    net = signed.rolling(126, min_periods=63).sum().abs()
    path = signed.abs().rolling(126, min_periods=63).sum()
    eff = net / path.replace(0, np.nan)
    loud = _mean(volume, 126) / _mean(volume, 252).replace(0, np.nan)
    b = eff * loud
    base = b
    result = base - 2.0 * base.shift(21) + base.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_loudflowint_jerk_v149_signal(closeadj, volume):
    ret = closeadj.pct_change()
    surge_rk = _mean(_f14_surge_ratio(volume, 63), 21).rolling(252, min_periods=63).rank(pct=True) - 0.5
    tilt = (np.sign(ret) * volume).rolling(63, min_periods=32).sum() \
        / volume.rolling(63, min_periods=32).sum().replace(0, np.nan)
    b = surge_rk * tilt
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)

def f14vs_f14_volume_surge_accumulation_health_jerk_v150_signal(closeadj, volume):
    ret = closeadj.pct_change()
    surge_rk = _mean(_f14_surge_ratio(volume, 63), 21).rolling(252, min_periods=63).rank(pct=True) - 0.5
    up = volume.where(ret > 0, 0.0).rolling(63, min_periods=32).sum()
    tot = volume.rolling(63, min_periods=32).sum()
    tilt = up / tot.replace(0, np.nan) - 0.5
    rising = np.log(_mean(volume, 63).replace(0, np.nan) / _mean(volume, 252).replace(0, np.nan))
    b = surge_rk + tilt + np.tanh(rising)
    base = b
    result = base - 2.0 * base.shift(10) + base.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f14vs_f14_volume_surge_accumulation_surgeosc_21d_jerk_v001_signal,
    f14vs_f14_volume_surge_accumulation_surgemed_63d_jerk_v002_signal,
    f14vs_f14_volume_surge_accumulation_basedrift_126d_jerk_v003_signal,
    f14vs_f14_volume_surge_accumulation_q90excess_126d_jerk_v004_signal,
    f14vs_f14_volume_surge_accumulation_surgeanom_63d_jerk_v005_signal,
    f14vs_f14_volume_surge_accumulation_surgeimp_21d_jerk_v006_signal,
    f14vs_f14_volume_surge_accumulation_peaksurge_21d_jerk_v007_signal,
    f14vs_f14_volume_surge_accumulation_quietloud_jerk_v008_signal,
    f14vs_f14_volume_surge_accumulation_blowoff_63d_jerk_v009_signal,
    f14vs_f14_volume_surge_accumulation_updown_21d_jerk_v010_signal,
    f14vs_f14_volume_surge_accumulation_updown_63d_jerk_v011_signal,
    f14vs_f14_volume_surge_accumulation_updownchg_126d_jerk_v012_signal,
    f14vs_f14_volume_surge_accumulation_dnintensity_63d_jerk_v013_signal,
    f14vs_f14_volume_surge_accumulation_bigupbias_21d_jerk_v014_signal,
    f14vs_f14_volume_surge_accumulation_loudflow_63d_jerk_v015_signal,
    f14vs_f14_volume_surge_accumulation_udratioz_21d_jerk_v016_signal,
    f14vs_f14_volume_surge_accumulation_upshare_252d_jerk_v017_signal,
    f14vs_f14_volume_surge_accumulation_surgeasymmag_63d_jerk_v018_signal,
    f14vs_f14_volume_surge_accumulation_surgecnt_63d_jerk_v019_signal,
    f14vs_f14_volume_surge_accumulation_surgecnt_126d_jerk_v020_signal,
    f14vs_f14_volume_surge_accumulation_burstcnt_21d_jerk_v021_signal,
    f14vs_f14_volume_surge_accumulation_climax_63d_jerk_v022_signal,
    f14vs_f14_volume_surge_accumulation_surgepersist_63d_jerk_v023_signal,
    f14vs_f14_volume_surge_accumulation_surgeclust_63d_jerk_v024_signal,
    f14vs_f14_volume_surge_accumulation_surgeasym_63d_jerk_v025_signal,
    f14vs_f14_volume_surge_accumulation_surgefreqtr_jerk_v026_signal,
    f14vs_f14_volume_surge_accumulation_recspikes_63d_jerk_v027_signal,
    f14vs_f14_volume_surge_accumulation_newvolhi_21d_jerk_v028_signal,
    f14vs_f14_volume_surge_accumulation_surgerecency_63d_jerk_v029_signal,
    f14vs_f14_volume_surge_accumulation_surgespace_126d_jerk_v030_signal,
    f14vs_f14_volume_surge_accumulation_hotstreak_jerk_v031_signal,
    f14vs_f14_volume_surge_accumulation_maxrun_63d_jerk_v032_signal,
    f14vs_f14_volume_surge_accumulation_accstreak_jerk_v033_signal,
    f14vs_f14_volume_surge_accumulation_topfrac_21d_jerk_v034_signal,
    f14vs_f14_volume_surge_accumulation_accflow_21d_jerk_v035_signal,
    f14vs_f14_volume_surge_accumulation_accaccel_21d_jerk_v036_signal,
    f14vs_f14_volume_surge_accumulation_acceff_21d_jerk_v037_signal,
    f14vs_f14_volume_surge_accumulation_accdist_63d_jerk_v038_signal,
    f14vs_f14_volume_surge_accumulation_accslope_21d_jerk_v039_signal,
    f14vs_f14_volume_surge_accumulation_accslope_63d_jerk_v040_signal,
    f14vs_f14_volume_surge_accumulation_acccurv_126d_jerk_v041_signal,
    f14vs_f14_volume_surge_accumulation_accstall_126d_jerk_v042_signal,
    f14vs_f14_volume_surge_accumulation_accgap_126d_jerk_v043_signal,
    f14vs_f14_volume_surge_accumulation_accrun_jerk_v044_signal,
    f14vs_f14_volume_surge_accumulation_accmom_63d_jerk_v045_signal,
    f14vs_f14_volume_surge_accumulation_duracc_252d_jerk_v046_signal,
    f14vs_f14_volume_surge_accumulation_accbreadth_21d_jerk_v047_signal,
    f14vs_f14_volume_surge_accumulation_episode_126d_jerk_v048_signal,
    f14vs_f14_volume_surge_accumulation_logexp_21v63_jerk_v049_signal,
    f14vs_f14_volume_surge_accumulation_volexpand_21d_jerk_v050_signal,
    f14vs_f14_volume_surge_accumulation_volfloor_63d_jerk_v051_signal,
    f14vs_f14_volume_surge_accumulation_madregime_252d_jerk_v052_signal,
    f14vs_f14_volume_surge_accumulation_surgewidth_jerk_v053_signal,
    f14vs_f14_volume_surge_accumulation_surgedisp_jerk_v054_signal,
    f14vs_f14_volume_surge_accumulation_wksurge_jerk_v055_signal,
    f14vs_f14_volume_surge_accumulation_afterglow_jerk_v056_signal,
    f14vs_f14_volume_surge_accumulation_followthru_jerk_v057_signal,
    f14vs_f14_volume_surge_accumulation_burstdecay_jerk_v058_signal,
    f14vs_f14_volume_surge_accumulation_surgereact_126d_jerk_v059_signal,
    f14vs_f14_volume_surge_accumulation_climaxrev_jerk_v060_signal,
    f14vs_f14_volume_surge_accumulation_roveff_63d_jerk_v061_signal,
    f14vs_f14_volume_surge_accumulation_vwret_21d_jerk_v062_signal,
    f14vs_f14_volume_surge_accumulation_thrust_21d_jerk_v063_signal,
    f14vs_f14_volume_surge_accumulation_flowdiv_63d_jerk_v064_signal,
    f14vs_f14_volume_surge_accumulation_upsurge_63d_jerk_v065_signal,
    f14vs_f14_volume_surge_accumulation_dnsurge_63d_jerk_v066_signal,
    f14vs_f14_volume_surge_accumulation_signsurge_21d_jerk_v067_signal,
    f14vs_f14_volume_surge_accumulation_volrank_252d_jerk_v068_signal,
    f14vs_f14_volume_surge_accumulation_surgerank_252d_jerk_v069_signal,
    f14vs_f14_volume_surge_accumulation_volregpos_252d_jerk_v070_signal,
    f14vs_f14_volume_surge_accumulation_surgevol_63d_jerk_v071_signal,
    f14vs_f14_volume_surge_accumulation_surgemomz_jerk_v072_signal,
    f14vs_f14_volume_surge_accumulation_voltrendcon_63d_jerk_v073_signal,
    f14vs_f14_volume_surge_accumulation_volaccel_21d_jerk_v074_signal,
    f14vs_f14_volume_surge_accumulation_volstretch_jerk_v075_signal,
    f14vs_f14_volume_surge_accumulation_surgetanh_21d_jerk_v076_signal,
    f14vs_f14_volume_surge_accumulation_logsurge_126d_jerk_v077_signal,
    f14vs_f14_volume_surge_accumulation_surgesqrt_63d_jerk_v078_signal,
    f14vs_f14_volume_surge_accumulation_surge5v63_jerk_v079_signal,
    f14vs_f14_volume_surge_accumulation_surgeaccel_jerk_v080_signal,
    f14vs_f14_volume_surge_accumulation_meanexcess_63d_jerk_v081_signal,
    f14vs_f14_volume_surge_accumulation_burstchg_21d_jerk_v082_signal,
    f14vs_f14_volume_surge_accumulation_surgedrought_jerk_v083_signal,
    f14vs_f14_volume_surge_accumulation_broadheat_126d_jerk_v084_signal,
    f14vs_f14_volume_surge_accumulation_spikefloor_21d_jerk_v085_signal,
    f14vs_f14_volume_surge_accumulation_dirspike_63d_jerk_v086_signal,
    f14vs_f14_volume_surge_accumulation_wkflow_jerk_v087_signal,
    f14vs_f14_volume_surge_accumulation_wkbreadth_jerk_v088_signal,
    f14vs_f14_volume_surge_accumulation_voldirpow_126d_jerk_v089_signal,
    f14vs_f14_volume_surge_accumulation_acceff_63d_jerk_v090_signal,
    f14vs_f14_volume_surge_accumulation_flowspread_jerk_v091_signal,
    f14vs_f14_volume_surge_accumulation_flowmom_jerk_v092_signal,
    f14vs_f14_volume_surge_accumulation_distrwarn_jerk_v093_signal,
    f14vs_f14_volume_surge_accumulation_accpersist_252d_jerk_v094_signal,
    f14vs_f14_volume_surge_accumulation_voleffort_63d_jerk_v095_signal,
    f14vs_f14_volume_surge_accumulation_exhaust_63d_jerk_v096_signal,
    f14vs_f14_volume_surge_accumulation_loudagree_63d_jerk_v097_signal,
    f14vs_f14_volume_surge_accumulation_movepersurge_jerk_v098_signal,
    f14vs_f14_volume_surge_accumulation_surgestreak_jerk_v099_signal,
    f14vs_f14_volume_surge_accumulation_quietstreak_jerk_v100_signal,
    f14vs_f14_volume_surge_accumulation_postpeak_jerk_v101_signal,
    f14vs_f14_volume_surge_accumulation_presurgecalm_jerk_v102_signal,
    f14vs_f14_volume_surge_accumulation_surgedecay_jerk_v103_signal,
    f14vs_f14_volume_surge_accumulation_surgedrift_63d_jerk_v104_signal,
    f14vs_f14_volume_surge_accumulation_expconvex_jerk_v105_signal,
    f14vs_f14_volume_surge_accumulation_volyoy_jerk_v106_signal,
    f14vs_f14_volume_surge_accumulation_volmom_step_jerk_v107_signal,
    f14vs_f14_volume_surge_accumulation_surgepctl_252d_jerk_v108_signal,
    f14vs_f14_volume_surge_accumulation_surgejitter_21d_jerk_v109_signal,
    f14vs_f14_volume_surge_accumulation_surgevolchg_jerk_v110_signal,
    f14vs_f14_volume_surge_accumulation_surgeswing_63d_jerk_v111_signal,
    f14vs_f14_volume_surge_accumulation_surgeclump_jerk_v112_signal,
    f14vs_f14_volume_surge_accumulation_surgez_252d_jerk_v113_signal,
    f14vs_f14_volume_surge_accumulation_volregpos_504d_jerk_v114_signal,
    f14vs_f14_volume_surge_accumulation_floorlift_252d_jerk_v115_signal,
    f14vs_f14_volume_surge_accumulation_ceilroom_252d_jerk_v116_signal,
    f14vs_f14_volume_surge_accumulation_partfade_jerk_v117_signal,
    f14vs_f14_volume_surge_accumulation_netsurge_126d_jerk_v118_signal,
    f14vs_f14_volume_surge_accumulation_surgemomflow_jerk_v119_signal,
    f14vs_f14_volume_surge_accumulation_buyshare_63d_jerk_v120_signal,
    f14vs_f14_volume_surge_accumulation_dirtiltmom_jerk_v121_signal,
    f14vs_f14_volume_surge_accumulation_wksurgez_jerk_v122_signal,
    f14vs_f14_volume_surge_accumulation_wkaccel_jerk_v123_signal,
    f14vs_f14_volume_surge_accumulation_dayspike_jerk_v124_signal,
    f14vs_f14_volume_surge_accumulation_extspike_126d_jerk_v125_signal,
    f14vs_f14_volume_surge_accumulation_tailshape_126d_jerk_v126_signal,
    f14vs_f14_volume_surge_accumulation_surgeyoy_jerk_v127_signal,
    f14vs_f14_volume_surge_accumulation_hiregime_252d_jerk_v128_signal,
    f14vs_f14_volume_surge_accumulation_regcross_252d_jerk_v129_signal,
    f14vs_f14_volume_surge_accumulation_accdist_252d_jerk_v130_signal,
    f14vs_f14_volume_surge_accumulation_flowsignmag_jerk_v131_signal,
    f14vs_f14_volume_surge_accumulation_flowdisp_jerk_v132_signal,
    f14vs_f14_volume_surge_accumulation_accnewhi_252d_jerk_v133_signal,
    f14vs_f14_volume_surge_accumulation_flowpricediv_jerk_v134_signal,
    f14vs_f14_volume_surge_accumulation_surgevoldiv_jerk_v135_signal,
    f14vs_f14_volume_surge_accumulation_vwret_63d_jerk_v136_signal,
    f14vs_f14_volume_surge_accumulation_impactasym_jerk_v137_signal,
    f14vs_f14_volume_surge_accumulation_surgedispema_jerk_v138_signal,
    f14vs_f14_volume_surge_accumulation_surgeema_jerk_v139_signal,
    f14vs_f14_volume_surge_accumulation_logvolstretch_jerk_v140_signal,
    f14vs_f14_volume_surge_accumulation_q75frac_21d_jerk_v141_signal,
    f14vs_f14_volume_surge_accumulation_medsym_63d_jerk_v142_signal,
    f14vs_f14_volume_surge_accumulation_surgehotcnt_63d_jerk_v143_signal,
    f14vs_f14_volume_surge_accumulation_regimeratio_jerk_v144_signal,
    f14vs_f14_volume_surge_accumulation_accbaltrend_jerk_v145_signal,
    f14vs_f14_volume_surge_accumulation_loudtilt_126d_jerk_v146_signal,
    f14vs_f14_volume_surge_accumulation_peakgap_jerk_v147_signal,
    f14vs_f14_volume_surge_accumulation_acceff_126d_jerk_v148_signal,
    f14vs_f14_volume_surge_accumulation_loudflowint_jerk_v149_signal,
    f14vs_f14_volume_surge_accumulation_health_jerk_v150_signal
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F14_VOLUME_SURGE_ACCUMULATION_REGISTRY_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0004, 0.032, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1.2e6, 7e5, n)) + 5e4, name="volume")

    cols = {"closeadj": closeadj, "volume": volume}

    ALLOW = {
        "open", "high", "low", "close", "closeadj", "volume",
    }

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs=%s" % (name, meta["inputs"])
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
