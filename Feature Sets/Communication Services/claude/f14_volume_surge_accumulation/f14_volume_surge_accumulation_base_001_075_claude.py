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
# NOTE: dollar-volume (closeadj*volume) belongs to f17 and is NEVER computed here.
# Turnover / Amihud belong to f16 and are NEVER computed here.
# closeadj is used ONLY to obtain the SIGN of the daily return for up/down
# classification of RAW volume. It is NEVER used as a price/dollar multiplier.
def _f14_ret_sign(closeadj):
    return np.sign(closeadj.pct_change())


def _f14_surge_ratio(volume, w):
    # current RAW volume vs its own rolling-mean baseline (surge multiple)
    base = volume.rolling(w, min_periods=max(2, w // 2)).mean()
    return volume / base.replace(0, np.nan)


def _f14_surge_excess(volume, w, k):
    # standardized RAW-volume excess above k sd of its own window baseline
    base = volume.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = volume.rolling(w, min_periods=max(2, w // 2)).std()
    return ((volume - base) / sd.replace(0, np.nan) - k).clip(lower=0)


def _f14_signed_vol_norm(closeadj, volume, w):
    # accumulation primitive: sign(return) * baseline-normalized RAW volume
    nvol = volume / _mean(volume, w).replace(0, np.nan)
    return _f14_ret_sign(closeadj) * nvol


def _f14_signed_surgez(closeadj, volume, w):
    # spike-weighted accumulation primitive: sign(return) * standardized RAW-volume z.
    # Heavily weights surge days, decoupling the cumulative line from plain up/down share.
    vz = _z(volume, w)
    return _f14_ret_sign(closeadj) * vz


# ============================================================
# --- SURGE MAGNITUDE (raw volume vs its own baseline) ---

# fast-vs-slow RAW-volume EMA surge oscillator (MACD-style, baseline-relative)
def f14vs_f14_volume_surge_accumulation_surgeosc_21d_base_v001_signal(volume):
    fast = volume.ewm(span=5, min_periods=3).mean()
    slow = volume.ewm(span=21, min_periods=10).mean()
    b = (fast - slow) / slow.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# robust surge multiple: today's volume over its 63d MEDIAN baseline (outlier-resistant)
def f14vs_f14_volume_surge_accumulation_surgemed_63d_base_v002_signal(volume):
    med = _med(volume, 63)
    b = volume / med.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slow participation-baseline drift: 126d median volume vs 252d median (regime, not spike)
def f14vs_f14_volume_surge_accumulation_basedrift_126d_base_v003_signal(volume):
    med126 = _med(volume, 126)
    med252 = _med(volume, 252)
    b = np.log(med126.replace(0, np.nan) / med252.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# excess-breach energy: summed log(volume/q90) on days breaching the 126d 90th-pct, minus chance level
def f14vs_f14_volume_surge_accumulation_q90excess_126d_base_v004_signal(volume):
    q90 = volume.rolling(126, min_periods=63).quantile(0.90)
    over = np.log(volume / q90.replace(0, np.nan)).clip(lower=0)
    energy = over.rolling(63, min_periods=32).sum()
    cnt = (volume > q90).astype(float).rolling(63, min_periods=32).sum()
    b = energy - 0.05 * cnt
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sustained surge anomaly: EMA(10) volume vs 63d mean, de-meaned by its own 126d level
def f14vs_f14_volume_surge_accumulation_surgeanom_63d_base_v005_signal(volume):
    fast = volume.ewm(span=10, min_periods=5).mean()
    ratio = fast / _mean(volume, 63).replace(0, np.nan)
    b = ratio - ratio.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge IMPULSE: today's 21d surge ratio minus its level a week ago (rate of surge onset)
def f14vs_f14_volume_surge_accumulation_surgeimp_21d_base_v006_signal(volume):
    sr = _f14_surge_ratio(volume, 21)
    b = sr - sr.shift(5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# peak surge magnitude: loudest single day in last 21d vs its 63d mean baseline (blowoff scale)
def f14vs_f14_volume_surge_accumulation_peaksurge_21d_base_v007_signal(volume):
    peak = _rmax(volume, 21)
    base = _mean(volume, 63)
    b = peak / base.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quiet-then-loud: recent 21d-mean volume vs the calmest 21d-mean over the prior half-year
def f14vs_f14_volume_surge_accumulation_quietloud_base_v008_signal(volume):
    base = _mean(volume, 21)
    quiet = _rmin(base, 126)
    b = np.log(base.replace(0, np.nan) / quiet.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blowoff prominence vs history: 63d-max/63d-median now, standardized by its own 252d history
def f14vs_f14_volume_surge_accumulation_blowoff_63d_base_v009_signal(volume):
    prom = _rmax(volume, 63) / _med(volume, 63).replace(0, np.nan)
    b = _z(prom, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- UP/DOWN VOLUME PRESSURE (sign from return, magnitude from RAW volume) ---

# up vs down RAW-volume net pressure over 21d, z-scored vs its own 252d history (tilt extremity)
def f14vs_f14_volume_surge_accumulation_updown_21d_base_v010_signal(closeadj, volume):
    ret = closeadj.pct_change()
    up = volume.where(ret > 0, 0.0).rolling(21, min_periods=10).sum()
    dn = volume.where(ret < 0, 0.0).rolling(21, min_periods=10).sum()
    bal = (up - dn) / (up + dn).replace(0, np.nan)
    b = _z(bal, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up vs down RAW-volume net pressure over 63d, displaced by its own slow 126d EMA (de-trended tilt)
def f14vs_f14_volume_surge_accumulation_updown_63d_base_v011_signal(closeadj, volume):
    ret = closeadj.pct_change()
    up = volume.where(ret > 0, 0.0).rolling(63, min_periods=32).sum()
    dn = volume.where(ret < 0, 0.0).rolling(63, min_periods=32).sum()
    bal = (up - dn) / (up + dn).replace(0, np.nan)
    b = bal - bal.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up vs down net pressure CHANGE over 126d (slow accumulation regime shift, not level)
def f14vs_f14_volume_surge_accumulation_updownchg_126d_base_v012_signal(closeadj, volume):
    ret = closeadj.pct_change()
    up = volume.where(ret > 0, 0.0).rolling(126, min_periods=63).sum()
    dn = volume.where(ret < 0, 0.0).rolling(126, min_periods=63).sum()
    bal = (up - dn) / (up + dn).replace(0, np.nan)
    b = bal - bal.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# avg RAW volume on down-days vs up-days (selling-pressure intensity ratio, log) 126d, de-trended
def f14vs_f14_volume_surge_accumulation_dnintensity_63d_base_v013_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dn = volume.where(ret < 0, np.nan).rolling(126, min_periods=40).mean()
    up = volume.where(ret > 0, np.nan).rolling(126, min_periods=40).mean()
    r = np.log(dn / up.replace(0, np.nan))
    b = r - r.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up-volume thrust restricted to TOP-QUARTILE volume days only (big-day buying bias) 21d
def f14vs_f14_volume_surge_accumulation_bigupbias_21d_base_v014_signal(closeadj, volume):
    ret = closeadj.pct_change()
    thr = volume.rolling(63, min_periods=32).quantile(0.75)
    big = volume.where(volume >= thr, 0.0)
    bigup = big.where(ret > 0, 0.0)
    su = bigup.rolling(21, min_periods=10).sum()
    tot = big.rolling(21, min_periods=10).sum()
    b = su / tot.replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net sign of returns on the LOUDEST 63d volume days, weighted by RAW volume (event flow)
def f14vs_f14_volume_surge_accumulation_loudflow_63d_base_v015_signal(closeadj, volume):
    ret = closeadj.pct_change()
    thr = volume.rolling(63, min_periods=32).quantile(0.80)
    big = volume >= thr
    signed = (np.sign(ret) * volume).where(big, 0.0)
    net = signed.rolling(63, min_periods=32).sum()
    gross = volume.where(big, 0.0).rolling(63, min_periods=32).sum()
    b = net / gross.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up/down RAW-volume log-ratio over 126d z-scored vs its own 252d history (flow extremity)
def f14vs_f14_volume_surge_accumulation_udratioz_21d_base_v016_signal(closeadj, volume):
    ret = closeadj.pct_change()
    up = volume.where(ret > 0, 0.0).rolling(126, min_periods=63).sum()
    dn = volume.where(ret < 0, 0.0).rolling(126, min_periods=63).sum()
    r = np.log((up + 1.0) / (dn + 1.0))
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# proportion of RAW volume on up-closes over 252d, centered (long accumulation share)
def f14vs_f14_volume_surge_accumulation_upshare_252d_base_v017_signal(closeadj, volume):
    ret = closeadj.pct_change()
    up = volume.where(ret > 0, 0.0).rolling(252, min_periods=126).sum()
    tot = volume.rolling(252, min_periods=126).sum()
    b = up / tot.replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# extreme single-day surge asymmetry: loudest up-day volume vs loudest down-day volume (log) 63d
def f14vs_f14_volume_surge_accumulation_surgeasymmag_63d_base_v018_signal(closeadj, volume):
    ret = closeadj.pct_change()
    up = volume.where(ret > 0, np.nan).rolling(63, min_periods=20).max()
    dn = volume.where(ret < 0, np.nan).rolling(63, min_periods=20).max()
    b = np.log(up / dn.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- SURGE / BURST / CLIMAX COUNTS (raw volume) ---

# magnitude-weighted surge-day tally over 63d (sum of excess sd-units beyond 2 sd)
def f14vs_f14_volume_surge_accumulation_surgecnt_63d_base_v019_signal(volume):
    b = _f14_surge_excess(volume, 63, 2.0).rolling(63, min_periods=32).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# magnitude-weighted surge-day tally over 126d (excess beyond 1.5 sd)
def f14vs_f14_volume_surge_accumulation_surgecnt_126d_base_v020_signal(volume):
    b = _f14_surge_excess(volume, 126, 1.5).rolling(126, min_periods=63).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-window burst tally over 21d (excess beyond 1.5 sd of 63d baseline)
def f14vs_f14_volume_surge_accumulation_burstcnt_21d_base_v021_signal(volume):
    base = _mean(volume, 63)
    sd = _std(volume, 63)
    burst = ((volume - base) / sd.replace(0, np.nan) - 1.5).clip(lower=0)
    b = burst.rolling(21, min_periods=10).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# climactic-volume intensity: summed (volume/21d-mean - 1.6)+ over last 63d (blowoff days)
def f14vs_f14_volume_surge_accumulation_climax_63d_base_v022_signal(volume):
    m = _mean(volume, 21)
    climax = (volume / m.replace(0, np.nan) - 1.6).clip(lower=0)
    b = climax.rolling(63, min_periods=32).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge persistence: fraction-weighted hot share where 63d surge ratio exceeds 1.5
def f14vs_f14_volume_surge_accumulation_surgepersist_63d_base_v023_signal(volume):
    sr = _f14_surge_ratio(volume, 63)
    hot = (sr - 1.5).clip(lower=0)
    b = hot.rolling(63, min_periods=32).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge-day CLUSTERING: summed product of consecutive standardized excesses over 63d
def f14vs_f14_volume_surge_accumulation_surgeclust_63d_base_v024_signal(volume):
    base = _mean(volume, 63)
    sd = _std(volume, 63)
    exc = ((volume - base) / sd.replace(0, np.nan)).clip(lower=0)
    consec = exc * exc.shift(1)
    b = consec.rolling(63, min_periods=32).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge asymmetry: up-surge excess count minus down-surge excess count over 63d
def f14vs_f14_volume_surge_accumulation_surgeasym_63d_base_v025_signal(closeadj, volume):
    ret = closeadj.pct_change()
    exc = _f14_surge_excess(volume, 63, 1.5)
    up = exc.where(ret > 0, 0.0).rolling(63, min_periods=32).sum()
    dn = exc.where(ret < 0, 0.0).rolling(63, min_periods=32).sum()
    b = up - dn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge-day frequency TREND: 63d excess count now minus its value a quarter ago
def f14vs_f14_volume_surge_accumulation_surgefreqtr_base_v026_signal(volume):
    cnt = _f14_surge_excess(volume, 63, 1.5).rolling(63, min_periods=32).sum()
    b = cnt - cnt.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recency-weighted spike intensity over 63d (recent excesses weighted more heavily)
def f14vs_f14_volume_surge_accumulation_recspikes_63d_base_v027_signal(volume):
    exc = _f14_surge_excess(volume, 63, 1.5)

    def _wsum(a):
        return float((a * np.linspace(0.5, 1.5, len(a))).sum())
    b = exc.rolling(63, min_periods=32).apply(_wsum, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# new-volume-high frequency: mag-weighted count of 63d-volume-high days within last 21d
def f14vs_f14_volume_surge_accumulation_newvolhi_21d_base_v028_signal(volume):
    rollmax = _rmax(volume, 63)
    isnew = (volume >= rollmax * 0.99999).astype(float)
    mag = volume / _mean(volume, 63).replace(0, np.nan)
    b = (isnew * mag).rolling(21, min_periods=10).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- SURGE TIMING / RECENCY / STREAKS ---

# surge recency: fractional days since the 63d-volume max (fresh vs stale spike)
def f14vs_f14_volume_surge_accumulation_surgerecency_63d_base_v029_signal(volume):
    def _f(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    b = volume.rolling(63, min_periods=32).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inter-surge spacing: mean days-since-last 2-sd surge over 126d (rare vs frequent spikes)
def f14vs_f14_volume_surge_accumulation_surgespace_126d_base_v030_signal(volume):
    base = _mean(volume, 63)
    sd = _std(volume, 63)
    surge = (volume > base + 2.0 * sd).astype(float)
    cum = surge.cumsum()
    since = cum.groupby(cum).cumcount().astype(float)
    b = since.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# high-volume-day streak: consecutive days volume exceeds its 21d mean, scaled by surge magnitude
def f14vs_f14_volume_surge_accumulation_hotstreak_base_v031_signal(volume):
    hot = (volume > _mean(volume, 21)).astype(float)
    grp = (hot != hot.shift(1)).cumsum()
    run = hot.groupby(grp).cumcount() + 1
    streak = run * hot
    mag = volume / _mean(volume, 21).replace(0, np.nan)
    b = streak * mag
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# longest above-mean-volume run within last 63d, scaled by recent-vs-long participation
def f14vs_f14_volume_surge_accumulation_maxrun_63d_base_v032_signal(volume):
    hot = (volume > _mean(volume, 21)).astype(float)
    grp = (hot != hot.shift(1)).cumsum()
    run = (hot.groupby(grp).cumcount() + 1) * hot
    b = _rmax(run, 63) * (_mean(volume, 21) / _mean(volume, 126).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation streak: signed consecutive up/down-close run, scaled by surge magnitude
def f14vs_f14_volume_surge_accumulation_accstreak_base_v033_signal(closeadj, volume):
    sign = _f14_ret_sign(closeadj).fillna(0.0)
    grp = (sign != sign.shift(1)).cumsum()
    run = sign.groupby(grp).cumcount() + 1
    b = (run * sign) * (volume / _mean(volume, 21).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap from latest 63d surge peak to current surge: how far volume has retreated off its peak
def f14vs_f14_volume_surge_accumulation_topfrac_21d_base_v034_signal(volume):
    sr = _f14_surge_ratio(volume, 63)
    peak = _rmax(sr, 21)
    b = (sr - peak) / peak.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- SIGNED RAW-VOLUME ACCUMULATION (sign of return x normalized RAW volume) ---

# accumulation oscillator: fast(10) minus slow(40) EMA of signed normalized RAW volume
def f14vs_f14_volume_surge_accumulation_accflow_21d_base_v035_signal(closeadj, volume):
    sv = _f14_signed_vol_norm(closeadj, volume, 63)
    fast = sv.ewm(span=10, min_periods=5).mean()
    slow = sv.ewm(span=40, min_periods=20).mean()
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation flow ACCELERATION: 21d signed-volume tilt minus its value a month ago
def f14vs_f14_volume_surge_accumulation_accaccel_21d_base_v036_signal(closeadj, volume):
    ret = closeadj.pct_change()
    flow = (np.sign(ret) * volume).rolling(21, min_periods=10).sum()
    tot = volume.rolling(21, min_periods=10).sum()
    tilt = flow / tot.replace(0, np.nan)
    b = tilt - tilt.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation directedness: |21d net signed-volume| / total signed path, scaled by loudness
def f14vs_f14_volume_surge_accumulation_acceff_21d_base_v037_signal(closeadj, volume):
    ret = closeadj.pct_change()
    signed = np.sign(ret) * volume
    net = signed.rolling(21, min_periods=10).sum().abs()
    path = signed.abs().rolling(21, min_periods=10).sum()
    eff = net / path.replace(0, np.nan)
    loud = _mean(volume, 21) / _mean(volume, 126).replace(0, np.nan)
    b = eff * loud
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation-line distance: spike-weighted signed-surge cumsum vs its 63d mean
def f14vs_f14_volume_surge_accumulation_accdist_63d_base_v038_signal(closeadj, volume):
    line = _f14_signed_surgez(closeadj, volume, 63).cumsum()
    b = (line - _mean(line, 63)) / _std(line, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spike-weighted accumulation-line slope over 21d (short surge-flow trend)
def f14vs_f14_volume_surge_accumulation_accslope_21d_base_v039_signal(closeadj, volume):
    line = _f14_signed_surgez(closeadj, volume, 63).cumsum()
    b = (line - line.shift(21)) / 21.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spike-weighted accumulation-line slope over 63d (medium surge-flow trend)
def f14vs_f14_volume_surge_accumulation_accslope_63d_base_v040_signal(closeadj, volume):
    line = _f14_signed_surgez(closeadj, volume, 63).cumsum()
    b = (line - line.shift(63)) / 63.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spike-weighted accumulation-line curvature: recent 21d slope minus prior 105d slope (flow accel)
def f14vs_f14_volume_surge_accumulation_acccurv_126d_base_v041_signal(closeadj, volume):
    line = _f14_signed_surgez(closeadj, volume, 126).cumsum()
    recent = (line - line.shift(21)) / 21.0
    prior = (line.shift(21) - line.shift(126)) / 105.0
    b = recent - prior
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spike-weighted accumulation-line drawdown: distance below its 126d peak, range-normalized
def f14vs_f14_volume_surge_accumulation_accstall_126d_base_v042_signal(closeadj, volume):
    line = _f14_signed_surgez(closeadj, volume, 63).cumsum()
    peak = _rmax(line, 126)
    span = (_rmax(line, 126) - _rmin(line, 126)).replace(0, np.nan)
    b = (line - peak) / span
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spike-weighted accumulation-line recency: fractional days since the 126d peak
def f14vs_f14_volume_surge_accumulation_accgap_126d_base_v043_signal(closeadj, volume):
    line = _f14_signed_surgez(closeadj, volume, 63).cumsum()

    def _f(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    b = line.rolling(126, min_periods=63).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation conviction streak: signed run of accumulation-line up-days, surge-mag weighted
def f14vs_f14_volume_surge_accumulation_accrun_base_v044_signal(closeadj, volume):
    line = _f14_signed_surgez(closeadj, volume, 63).cumsum()
    up = (line.diff() > 0).astype(float)
    grp = (up != up.shift(1)).cumsum()
    run = (up.groupby(grp).cumcount() + 1)
    signed = run * (2 * up - 1)
    b = signed * (volume / _mean(volume, 63).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation momentum: 63d net signed-volume rank now minus its rank a quarter ago
def f14vs_f14_volume_surge_accumulation_accmom_63d_base_v045_signal(closeadj, volume):
    ret = closeadj.pct_change()
    net = (np.sign(ret) * volume).rolling(63, min_periods=32).sum()
    b = net.rank(pct=True) - net.shift(63).rank(pct=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable accumulation regime: 252d up-tilt intensity minus down-tilt intensity (mag-weighted)
def f14vs_f14_volume_surge_accumulation_duracc_252d_base_v046_signal(closeadj, volume):
    tilt = _f14_signed_vol_norm(closeadj, volume, 126).rolling(21, min_periods=10).mean()
    up = tilt.clip(lower=0).rolling(252, min_periods=126).mean()
    dn = (-tilt).clip(lower=0).rolling(252, min_periods=126).mean()
    b = up - dn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation breadth DISPERSION: variability of daily signed-surge contributions over 21d
def f14vs_f14_volume_surge_accumulation_accbreadth_21d_base_v047_signal(closeadj, volume):
    contrib = _f14_signed_vol_norm(closeadj, volume, 63)
    b = contrib.rolling(21, min_periods=10).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation over distribution episodes: net surge-day direction over 126d (big days only)
def f14vs_f14_volume_surge_accumulation_episode_126d_base_v048_signal(closeadj, volume):
    ret = closeadj.pct_change()
    sr = _f14_surge_ratio(volume, 63)
    big = (sr - 1.5).clip(lower=0)
    net = (np.sign(ret) * big).rolling(126, min_periods=63).sum()
    gross = big.rolling(126, min_periods=63).sum()
    b = net / gross.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- SURGE TREND / EXPANSION (raw volume baselines, log-space) ---

# log-volume baseline expansion: 21d log-mean minus 63d log-mean (short-vs-medium drift)
def f14vs_f14_volume_surge_accumulation_logexp_21v63_base_v049_signal(volume):
    lv = np.log(volume.clip(lower=1.0))
    b = _mean(lv, 21) - _mean(lv, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume expansion: 21d mean now vs 21d mean a quarter ago, percent (participation pickup)
def f14vs_f14_volume_surge_accumulation_volexpand_21d_base_v050_signal(volume):
    m = _mean(volume, 21)
    b = (m - m.shift(63)) / m.shift(63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume floor lift: 63d-min volume rising year-on-quarter (rising base of participation)
def f14vs_f14_volume_surge_accumulation_volfloor_63d_base_v051_signal(volume):
    fl = _rmin(volume, 63)
    b = np.log(fl.replace(0, np.nan) / fl.shift(63).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# robust regime drift: 63d-median distance from 252d-median in MAD units (level, not spike)
def f14vs_f14_volume_surge_accumulation_madregime_252d_base_v052_signal(volume):
    med63 = _med(volume, 63)
    med252 = _med(volume, 252)
    mad252 = (volume - med252).abs().rolling(252, min_periods=126).median()
    b = (med63 - med252) / (1.4826 * mad252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge-multiple RANGE over 21d: spread between loudest & quietest 63d surge ratio (regime width)
def f14vs_f14_volume_surge_accumulation_surgewidth_base_v053_signal(volume):
    sr = _f14_surge_ratio(volume, 63)
    b = _rmax(sr, 21) - _rmin(sr, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge-ratio dispersion across windows (5/21/63 disagreement of surge multiple)
def f14vs_f14_volume_surge_accumulation_surgedisp_base_v054_signal(volume):
    s1 = _f14_surge_ratio(volume, 5)
    s2 = _f14_surge_ratio(volume, 21)
    s3 = _f14_surge_ratio(volume, 63)
    b = pd.concat([s1, s2, s3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weekly-aggregated surge: 5d-summed volume vs its 13-week baseline (weekly burst level)
def f14vs_f14_volume_surge_accumulation_wksurge_base_v055_signal(volume):
    wk = volume.rolling(5).sum()
    base = _mean(wk, 63)
    b = wk / base.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge-ratio MEMORY: halflife-10 decayed surge ratio minus the slow 63d-mean surge (after-glow level)
def f14vs_f14_volume_surge_accumulation_afterglow_base_v056_signal(volume):
    sr = _f14_surge_ratio(volume, 63)
    decayed = sr.ewm(halflife=10, min_periods=5).mean()
    slow = sr.rolling(63, min_periods=32).mean()
    b = decayed - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# post-spike follow-through: avg next-day surge multiple after a top-decile spike (21d)
def f14vs_f14_volume_surge_accumulation_followthru_base_v057_signal(volume):
    thr = volume.rolling(126, min_periods=63).quantile(0.85)
    spike = (volume.shift(1) >= thr.shift(1))
    nextvol = (volume / _mean(volume, 63).replace(0, np.nan)).where(spike, np.nan)
    b = nextvol.rolling(126, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# burst decay: today's volume vs the max of the prior 5 days, z-scored (post-spike fade)
def f14vs_f14_volume_surge_accumulation_burstdecay_base_v058_signal(volume):
    prior5 = volume.shift(1).rolling(5, min_periods=3).max()
    ratio = volume / prior5.replace(0, np.nan)
    b = _z(ratio, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- SURGE-CONDITIONED PRICE INTERACTION (effort vs result; sign only) ---

# surge-day return reaction: avg return on top-decile volume days vs all days over 126d
def f14vs_f14_volume_surge_accumulation_surgereact_126d_base_v059_signal(closeadj, volume):
    ret = closeadj.pct_change()
    thr = volume.rolling(126, min_periods=63).quantile(0.85)
    bigret = ret.where(volume >= thr, np.nan)
    bigmean = bigret.rolling(126, min_periods=10).mean()
    allmean = ret.rolling(126, min_periods=63).mean()
    b = bigmean - allmean
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# climactic-reversal: large surge on a reversal day over 21d (exhaustion proxy)
def f14vs_f14_volume_surge_accumulation_climaxrev_base_v060_signal(closeadj, volume):
    ret = closeadj.pct_change()
    prior = closeadj.shift(1) / closeadj.shift(6) - 1.0
    sr = _f14_surge_ratio(volume, 63)
    reversal = -np.sign(ret) * np.sign(prior) * (sr - 1.0).clip(lower=0)
    b = reversal.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return-on-surge efficiency: 63d price ROC per unit of average surge ratio (move per crowd)
def f14vs_f14_volume_surge_accumulation_roveff_63d_base_v061_signal(closeadj, volume):
    roc = closeadj / closeadj.shift(63) - 1.0
    avgsurge = _mean(_f14_surge_ratio(volume, 63), 63)
    b = roc / avgsurge.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-vs-|return| co-movement over 21d: rolling correlation of surge ratio with |return| (effort-result link)
def f14vs_f14_volume_surge_accumulation_vwret_21d_base_v062_signal(closeadj, volume):
    ar = closeadj.pct_change().abs()
    sr = _f14_surge_ratio(volume, 63)
    b = sr.rolling(21, min_periods=10).corr(ar)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# silent-surge fraction over 63d: share of volume spikes occurring on near-flat price days (no |ret| spike)
def f14vs_f14_volume_surge_accumulation_thrust_21d_base_v063_signal(closeadj, volume):
    ar = closeadj.pct_change().abs()
    volspike = (volume > volume.rolling(63, min_periods=32).quantile(0.85)).astype(float)
    quiet = (ar < ar.rolling(63, min_periods=32).quantile(0.50)).astype(float)
    silent = (volspike * quiet).rolling(63, min_periods=32).sum()
    base = volspike.rolling(63, min_periods=32).sum()
    b = silent / base.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# flow-vs-price divergence: 63d signed-volume tilt minus tanh of 63d price ROC (effort vs result)
def f14vs_f14_volume_surge_accumulation_flowdiv_63d_base_v064_signal(closeadj, volume):
    ret = closeadj.pct_change()
    flow = (np.sign(ret) * volume).rolling(63, min_periods=32).sum()
    flow_n = flow / volume.rolling(63, min_periods=32).sum().replace(0, np.nan)
    price = closeadj / closeadj.shift(63) - 1.0
    b = flow_n - np.tanh(price)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge on up-days only: surge ratio conditioned on a positive close (buying-surge intensity)
def f14vs_f14_volume_surge_accumulation_upsurge_63d_base_v065_signal(closeadj, volume):
    ret = closeadj.pct_change()
    sr = _f14_surge_ratio(volume, 63) - 1.0
    b = sr.where(ret > 0, 0.0)
    b = b.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge on down-days only: surge ratio conditioned on a negative close (distribution intensity)
def f14vs_f14_volume_surge_accumulation_dnsurge_63d_base_v066_signal(closeadj, volume):
    ret = closeadj.pct_change()
    sr = _f14_surge_ratio(volume, 63) - 1.0
    b = sr.where(ret < 0, 0.0)
    b = b.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up-surge vs down-surge BALANCE on big days: net direction of top-quartile surge days over 63d
def f14vs_f14_volume_surge_accumulation_signsurge_21d_base_v067_signal(closeadj, volume):
    ret = closeadj.pct_change()
    sr = _f14_surge_ratio(volume, 63)
    big = (sr >= sr.rolling(63, min_periods=32).quantile(0.75))
    upbig = (big & (ret > 0)).astype(float).rolling(63, min_periods=32).sum()
    dnbig = (big & (ret < 0)).astype(float).rolling(63, min_periods=32).sum()
    b = (upbig - dnbig) / (upbig + dnbig).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- SURGE REGIME POSITION / RANK / VOL-OF-SURGE ---

# participation regime rank: 21d-mean volume percentile vs its own 252d history (smoothed)
def f14vs_f14_volume_surge_accumulation_volrank_252d_base_v068_signal(volume):
    base = _mean(volume, 21)
    b = base.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge-rank momentum: smoothed surge percentile now minus its level 21d ago (ramping crowd)
def f14vs_f14_volume_surge_accumulation_surgerank_252d_base_v069_signal(volume):
    sr = _mean(_f14_surge_ratio(volume, 63), 5)
    rk = sr.rolling(252, min_periods=63).rank(pct=True)
    b = rk - rk.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# regime position: 21d-mean volume within its 252d min-max band (where in the range)
def f14vs_f14_volume_surge_accumulation_volregpos_252d_base_v070_signal(volume):
    base = _mean(volume, 21)
    hi = _rmax(base, 252)
    lo = _rmin(base, 252)
    b = (base - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-of-surge: standard deviation of the 63d surge ratio over 63d (unstable participation)
def f14vs_f14_volume_surge_accumulation_surgevol_63d_base_v071_signal(volume):
    sr = _f14_surge_ratio(volume, 63)
    b = sr.rolling(63, min_periods=32).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge-ratio momentum z: standardized change of the 21d surge ratio (de-trended onset)
def f14vs_f14_volume_surge_accumulation_surgemomz_base_v072_signal(volume):
    sr = _f14_surge_ratio(volume, 21)
    chg = sr - sr.shift(10)
    b = _z(chg, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-trend consistency: fraction of last 63d above the 63d mean, centered (steady surge)
def f14vs_f14_volume_surge_accumulation_voltrendcon_63d_base_v073_signal(volume):
    m = _mean(volume, 63)
    above = (volume > m).astype(float)
    b = above.rolling(63, min_periods=32).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration of participation: 21d-mean ratio change (rate of crowd pickup)
def f14vs_f14_volume_surge_accumulation_volaccel_21d_base_v074_signal(volume):
    m = _mean(volume, 21)
    r = m / m.shift(21).replace(0, np.nan)
    b = r - r.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# long-regime heat: fraction of last 63d that volume exceeded its slow EMA200 baseline, centered
def f14vs_f14_volume_surge_accumulation_volstretch_base_v075_signal(volume):
    slow = volume.ewm(span=200, min_periods=100).mean()
    above = (volume > slow).astype(float)
    b = above.rolling(63, min_periods=32).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f14vs_f14_volume_surge_accumulation_surgeosc_21d_base_v001_signal,
    f14vs_f14_volume_surge_accumulation_surgemed_63d_base_v002_signal,
    f14vs_f14_volume_surge_accumulation_basedrift_126d_base_v003_signal,
    f14vs_f14_volume_surge_accumulation_q90excess_126d_base_v004_signal,
    f14vs_f14_volume_surge_accumulation_surgeanom_63d_base_v005_signal,
    f14vs_f14_volume_surge_accumulation_surgeimp_21d_base_v006_signal,
    f14vs_f14_volume_surge_accumulation_peaksurge_21d_base_v007_signal,
    f14vs_f14_volume_surge_accumulation_quietloud_base_v008_signal,
    f14vs_f14_volume_surge_accumulation_blowoff_63d_base_v009_signal,
    f14vs_f14_volume_surge_accumulation_updown_21d_base_v010_signal,
    f14vs_f14_volume_surge_accumulation_updown_63d_base_v011_signal,
    f14vs_f14_volume_surge_accumulation_updownchg_126d_base_v012_signal,
    f14vs_f14_volume_surge_accumulation_dnintensity_63d_base_v013_signal,
    f14vs_f14_volume_surge_accumulation_bigupbias_21d_base_v014_signal,
    f14vs_f14_volume_surge_accumulation_loudflow_63d_base_v015_signal,
    f14vs_f14_volume_surge_accumulation_udratioz_21d_base_v016_signal,
    f14vs_f14_volume_surge_accumulation_upshare_252d_base_v017_signal,
    f14vs_f14_volume_surge_accumulation_surgeasymmag_63d_base_v018_signal,
    f14vs_f14_volume_surge_accumulation_surgecnt_63d_base_v019_signal,
    f14vs_f14_volume_surge_accumulation_surgecnt_126d_base_v020_signal,
    f14vs_f14_volume_surge_accumulation_burstcnt_21d_base_v021_signal,
    f14vs_f14_volume_surge_accumulation_climax_63d_base_v022_signal,
    f14vs_f14_volume_surge_accumulation_surgepersist_63d_base_v023_signal,
    f14vs_f14_volume_surge_accumulation_surgeclust_63d_base_v024_signal,
    f14vs_f14_volume_surge_accumulation_surgeasym_63d_base_v025_signal,
    f14vs_f14_volume_surge_accumulation_surgefreqtr_base_v026_signal,
    f14vs_f14_volume_surge_accumulation_recspikes_63d_base_v027_signal,
    f14vs_f14_volume_surge_accumulation_newvolhi_21d_base_v028_signal,
    f14vs_f14_volume_surge_accumulation_surgerecency_63d_base_v029_signal,
    f14vs_f14_volume_surge_accumulation_surgespace_126d_base_v030_signal,
    f14vs_f14_volume_surge_accumulation_hotstreak_base_v031_signal,
    f14vs_f14_volume_surge_accumulation_maxrun_63d_base_v032_signal,
    f14vs_f14_volume_surge_accumulation_accstreak_base_v033_signal,
    f14vs_f14_volume_surge_accumulation_topfrac_21d_base_v034_signal,
    f14vs_f14_volume_surge_accumulation_accflow_21d_base_v035_signal,
    f14vs_f14_volume_surge_accumulation_accaccel_21d_base_v036_signal,
    f14vs_f14_volume_surge_accumulation_acceff_21d_base_v037_signal,
    f14vs_f14_volume_surge_accumulation_accdist_63d_base_v038_signal,
    f14vs_f14_volume_surge_accumulation_accslope_21d_base_v039_signal,
    f14vs_f14_volume_surge_accumulation_accslope_63d_base_v040_signal,
    f14vs_f14_volume_surge_accumulation_acccurv_126d_base_v041_signal,
    f14vs_f14_volume_surge_accumulation_accstall_126d_base_v042_signal,
    f14vs_f14_volume_surge_accumulation_accgap_126d_base_v043_signal,
    f14vs_f14_volume_surge_accumulation_accrun_base_v044_signal,
    f14vs_f14_volume_surge_accumulation_accmom_63d_base_v045_signal,
    f14vs_f14_volume_surge_accumulation_duracc_252d_base_v046_signal,
    f14vs_f14_volume_surge_accumulation_accbreadth_21d_base_v047_signal,
    f14vs_f14_volume_surge_accumulation_episode_126d_base_v048_signal,
    f14vs_f14_volume_surge_accumulation_logexp_21v63_base_v049_signal,
    f14vs_f14_volume_surge_accumulation_volexpand_21d_base_v050_signal,
    f14vs_f14_volume_surge_accumulation_volfloor_63d_base_v051_signal,
    f14vs_f14_volume_surge_accumulation_madregime_252d_base_v052_signal,
    f14vs_f14_volume_surge_accumulation_surgewidth_base_v053_signal,
    f14vs_f14_volume_surge_accumulation_surgedisp_base_v054_signal,
    f14vs_f14_volume_surge_accumulation_wksurge_base_v055_signal,
    f14vs_f14_volume_surge_accumulation_afterglow_base_v056_signal,
    f14vs_f14_volume_surge_accumulation_followthru_base_v057_signal,
    f14vs_f14_volume_surge_accumulation_burstdecay_base_v058_signal,
    f14vs_f14_volume_surge_accumulation_surgereact_126d_base_v059_signal,
    f14vs_f14_volume_surge_accumulation_climaxrev_base_v060_signal,
    f14vs_f14_volume_surge_accumulation_roveff_63d_base_v061_signal,
    f14vs_f14_volume_surge_accumulation_vwret_21d_base_v062_signal,
    f14vs_f14_volume_surge_accumulation_thrust_21d_base_v063_signal,
    f14vs_f14_volume_surge_accumulation_flowdiv_63d_base_v064_signal,
    f14vs_f14_volume_surge_accumulation_upsurge_63d_base_v065_signal,
    f14vs_f14_volume_surge_accumulation_dnsurge_63d_base_v066_signal,
    f14vs_f14_volume_surge_accumulation_signsurge_21d_base_v067_signal,
    f14vs_f14_volume_surge_accumulation_volrank_252d_base_v068_signal,
    f14vs_f14_volume_surge_accumulation_surgerank_252d_base_v069_signal,
    f14vs_f14_volume_surge_accumulation_volregpos_252d_base_v070_signal,
    f14vs_f14_volume_surge_accumulation_surgevol_63d_base_v071_signal,
    f14vs_f14_volume_surge_accumulation_surgemomz_base_v072_signal,
    f14vs_f14_volume_surge_accumulation_voltrendcon_63d_base_v073_signal,
    f14vs_f14_volume_surge_accumulation_volaccel_21d_base_v074_signal,
    f14vs_f14_volume_surge_accumulation_volstretch_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F14_VOLUME_SURGE_ACCUMULATION_REGISTRY_001_075 = REGISTRY


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
