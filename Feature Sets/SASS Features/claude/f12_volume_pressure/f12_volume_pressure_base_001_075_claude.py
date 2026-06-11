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
    # OLS slope of s on time over window w (per-step)
    idx = np.arange(w, dtype=float)
    idx = idx - idx.mean()
    denom = float((idx ** 2).sum())

    def _f(a):
        if np.any(np.isnan(a)):
            return np.nan
        return float(np.dot(idx, a) / denom)
    return s.rolling(w, min_periods=w).apply(_f, raw=True)


# ===== folder domain primitives (volume pressure) =====
def _f12_dollar_vol(closeadj, volume):
    # dollar-volume; use closeadj*volume for windows > 21d
    return closeadj * volume


def _f12_vol_z(volume, w):
    return _z(volume, w)


def _f12_rel_vol(volume, w):
    # current volume vs its trailing w-day average
    return volume / _mean(volume, w).replace(0, np.nan)


def _f12_surge(volume, wshort, wlong):
    # short-window avg volume vs long-window avg volume
    return _mean(volume, wshort) / _mean(volume, wlong).replace(0, np.nan)


def _f12_updown_ratio(closeadj, volume, w):
    # up-day volume vs down-day volume over w
    ret = closeadj.pct_change()
    up = volume.where(ret > 0, 0.0)
    dn = volume.where(ret < 0, 0.0)
    return _rsum(up, w) / _rsum(dn, w).replace(0, np.nan)


def _f12_concentration(volume, w):
    # Herfindahl-like concentration of volume within the window
    sm = _rsum(volume, w)
    sq = _rsum(volume ** 2, w)
    return sq / (sm ** 2).replace(0, np.nan)


# ============================================================
# --- volume z-score family ---
def f12vp_f12_volume_pressure_volz_21d_base_v001_signal(volume):
    b = _f12_vol_z(volume, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f12vp_f12_volume_pressure_volz_63d_base_v002_signal(volume):
    # abnormal-volume momentum: change in the 63d volume z-score over a month
    zz = _z(volume, 63)
    b = zz - zz.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f12vp_f12_volume_pressure_volz_126d_base_v003_signal(volume):
    # abnormal-volume persistence: fraction of 126d window with |z(21d)| elevated,
    # signed by the mean z (continuous, distribution-shape driven)
    zz = _z(volume, 21)
    elevated = (zz.abs() > 1.0).astype(float)
    frac = elevated.rolling(126, min_periods=63).mean()
    b = frac * np.sign(zz.rolling(126, min_periods=63).mean()) + zz / 10.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log-volume z-score (heavy-tail tamed)
def f12vp_f12_volume_pressure_logvolz_63d_base_v004_signal(volume):
    # asymmetry of abnormal volume: avg positive log-vol z minus avg negative,
    # over a quarter (are surges bigger than droughts?)
    lv = np.log(volume.replace(0, np.nan))
    zz = _z(lv, 63)
    pos = zz.clip(lower=0).rolling(63, min_periods=21).mean()
    neg = (-zz.clip(upper=0)).rolling(63, min_periods=21).mean()
    b = pos - neg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# robust volume z: deviation from median scaled by MAD
def f12vp_f12_volume_pressure_volmadz_63d_base_v005_signal(volume):
    # mean-vs-median gap of volume (distribution skew proxy), scaled by MAD
    med = volume.rolling(63, min_periods=21).median()
    mn = _mean(volume, 63)
    mad = (volume - med).abs().rolling(63, min_periods=21).median()
    b = (mn - med) / (1.4826 * mad).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- relative volume vs 63d average (the headline RVOL) ---
def f12vp_f12_volume_pressure_relvol_63d_base_v006_signal(volume):
    # sustained relative volume: 21d-average volume vs the trailing 63d median
    # (slow RVOL regime, distinct autocorrelation from single-day measures)
    av = _mean(volume, 21)
    med = volume.rolling(63, min_periods=21).median()
    b = av / med.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f12vp_f12_volume_pressure_relvol_21d_base_v007_signal(closeadj, volume):
    # 21d relative volume modulated by the magnitude of the day's price move
    ret = closeadj.pct_change()
    rv = _f12_rel_vol(volume, 21)
    b = rv * ret.abs().rolling(5, min_periods=2).mean() * 100.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f12vp_f12_volume_pressure_relvol_252d_base_v008_signal(volume):
    # single-day volume vs annual baseline, log-scaled (long-horizon RVOL)
    b = np.log(volume.replace(0, np.nan) / _mean(volume, 252).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 5-day avg relative volume (smoothed RVOL vs 63d)
def f12vp_f12_volume_pressure_relvolsm_63d_base_v009_signal(volume):
    # medium-term volume tide: 21d EWMA vs 126d EWMA (slow surge gauge)
    fast = volume.ewm(span=21, min_periods=10).mean()
    slow = volume.ewm(span=126, min_periods=42).mean()
    b = fast / slow.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log relative volume centered at 0
def f12vp_f12_volume_pressure_logrelvol_63d_base_v010_signal(closeadj, volume):
    # return-signed log relative-volume: today's surprise volume, signed by the move
    ret = closeadj.pct_change()
    lr = np.log(volume.replace(0, np.nan) / _mean(volume, 63).replace(0, np.nan))
    b = np.sign(ret) * lr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- volume surge ratios (short vs long average) ---
def f12vp_f12_volume_pressure_surge_5v63_base_v011_signal(volume):
    b = _f12_surge(volume, 5, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f12vp_f12_volume_pressure_surge_21v126_base_v012_signal(volume):
    b = _f12_surge(volume, 21, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f12vp_f12_volume_pressure_surge_5v21_base_v013_signal(volume):
    b = _f12_surge(volume, 5, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f12vp_f12_volume_pressure_surge_21v252_base_v014_signal(volume):
    # quarterly tide vs annual baseline (slow structural volume shift)
    b = _f12_surge(volume, 63, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spike ratio: today's volume vs trailing max over a quarter
def f12vp_f12_volume_pressure_spikemax_63d_base_v015_signal(volume):
    b = volume / _rmax(volume.shift(1), 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- up/down volume ratio family ---
def f12vp_f12_volume_pressure_udvol_21d_base_v016_signal(closeadj, volume):
    b = np.log(_f12_updown_ratio(closeadj, volume, 21))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f12vp_f12_volume_pressure_udvol_63d_base_v017_signal(closeadj, volume):
    b = np.log(_f12_updown_ratio(closeadj, volume, 63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f12vp_f12_volume_pressure_udvol_126d_base_v018_signal(closeadj, volume):
    b = np.log(_f12_updown_ratio(closeadj, volume, 126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up-volume share: up-day volume / total volume over a month
def f12vp_f12_volume_pressure_upvolshare_21d_base_v019_signal(closeadj, volume):
    # up-day volume concentration: Herfindahl of up-day volumes over a month
    ret = closeadj.pct_change()
    up = volume.where(ret > 0, 0.0)
    sm = _rsum(up, 21)
    sq = _rsum(up ** 2, 21)
    b = sq / (sm ** 2).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# down-volume share over a quarter
def f12vp_f12_volume_pressure_dnvolshare_63d_base_v020_signal(closeadj, volume):
    # down-day volume concentration: Herfindahl of down-day volumes over a quarter
    ret = closeadj.pct_change()
    dn = volume.where(ret < 0, 0.0)
    sm = _rsum(dn, 63)
    sq = _rsum(dn ** 2, 63)
    b = sq / (sm ** 2).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed-volume pressure: sum(sign(ret)*volume)/sum(volume)
def f12vp_f12_volume_pressure_signvolpr_21d_base_v021_signal(closeadj, volume):
    # volume-weighted move asymmetry: do the highest-volume days lean up or down?
    # correlation of daily return sign with the volume rank within the month
    ret = closeadj.pct_change()
    vr = volume.rolling(21, min_periods=10).rank(pct=True) - 0.5
    b = _rsum(np.sign(ret) * vr, 21) / 21.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f12vp_f12_volume_pressure_signvolpr_63d_base_v022_signal(closeadj, volume):
    # net signed-volume pressure (quarter) MINUS its own monthly value (pressure shift)
    ret = closeadj.pct_change()
    signed = np.sign(ret) * volume
    q = _rsum(signed, 63) / _rsum(volume, 63).replace(0, np.nan)
    mo = _rsum(signed, 21) / _rsum(volume, 21).replace(0, np.nan)
    b = mo - q
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- volume trend slope (math slope of volume level) ---
def f12vp_f12_volume_pressure_volslope_21d_base_v023_signal(volume):
    b = _slope(volume, 21) / _mean(volume, 21).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f12vp_f12_volume_pressure_volslope_63d_base_v024_signal(volume):
    b = _slope(volume, 63) / _mean(volume, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of log-volume (compounded volume growth rate)
def f12vp_f12_volume_pressure_logvolslope_63d_base_v025_signal(volume):
    # R-squared-like trendiness of log-volume: how monotone is the 63d volume trend
    lv = np.log(volume.replace(0, np.nan))
    net = lv - lv.shift(62)
    path = lv.diff().abs().rolling(63, min_periods=21).sum()
    b = net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- dollar-volume (closeadj*volume) trend; windows > 21d ---
def f12vp_f12_volume_pressure_dvolz_63d_base_v026_signal(closeadj, volume):
    dv = _f12_dollar_vol(closeadj, volume)
    b = _z(np.log(dv.replace(0, np.nan)), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f12vp_f12_volume_pressure_dvolz_126d_base_v027_signal(closeadj, volume):
    # dollar-volume tide: log-DV cross-horizon gap (21d z minus 126d z)
    dv = np.log(_f12_dollar_vol(closeadj, volume).replace(0, np.nan))
    b = _z(dv, 21) - _z(dv, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume relative to its 63d average
def f12vp_f12_volume_pressure_dvolrel_63d_base_v028_signal(closeadj, volume):
    dv = _f12_dollar_vol(closeadj, volume)
    b = dv / _mean(dv, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume surge: 21d avg vs 126d avg
def f12vp_f12_volume_pressure_dvolsurge_21v126_base_v029_signal(closeadj, volume):
    dv = _f12_dollar_vol(closeadj, volume)
    b = _mean(dv, 21) / _mean(dv, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume trend slope normalized (log-DV slope over a quarter)
def f12vp_f12_volume_pressure_dvolslope_63d_base_v030_signal(closeadj, volume):
    dv = _f12_dollar_vol(closeadj, volume)
    b = _slope(np.log(dv.replace(0, np.nan)), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume year-over-year log growth
def f12vp_f12_volume_pressure_dvolyoy_252d_base_v031_signal(closeadj, volume):
    dv = _f12_dollar_vol(closeadj, volume)
    a = _mean(dv, 63)
    b = np.log(a.replace(0, np.nan) / a.shift(252).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- volume concentration / clustering ---
def f12vp_f12_volume_pressure_conc_21d_base_v032_signal(volume):
    b = _f12_concentration(volume, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f12vp_f12_volume_pressure_conc_63d_base_v033_signal(volume):
    b = _f12_concentration(volume, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coefficient of variation of volume (dispersion of activity)
def f12vp_f12_volume_pressure_volcv_63d_base_v034_signal(volume):
    # inter-quantile spread of volume: (Q90 - Q10) / median over a quarter
    q90 = volume.rolling(63, min_periods=21).quantile(0.9)
    q10 = volume.rolling(63, min_periods=21).quantile(0.1)
    med = volume.rolling(63, min_periods=21).median()
    b = (q90 - q10) / med.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of the quarter's volume done in its single biggest day
def f12vp_f12_volume_pressure_topday_63d_base_v035_signal(volume):
    b = _rmax(volume, 63) / _rsum(volume, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- volume surge frequency / hit-rate of high-volume days ---
def f12vp_f12_volume_pressure_surgefreq_63d_base_v036_signal(volume):
    avg = _mean(volume, 63)
    hi = (volume > 1.5 * avg).astype(float)
    freq = hi.rolling(63, min_periods=21).mean()
    depth = (volume / avg.replace(0, np.nan) - 1.5).clip(lower=0).rolling(21, min_periods=10).mean()
    b = freq + depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quiet-day frequency: fraction of days well below average volume
def f12vp_f12_volume_pressure_quietfreq_63d_base_v037_signal(volume):
    avg = _mean(volume, 63)
    lo = (volume < 0.5 * avg).astype(float)
    freq = lo.rolling(63, min_periods=21).mean()
    depth = (0.5 - volume / avg.replace(0, np.nan)).clip(lower=0).rolling(21, min_periods=10).mean()
    b = freq + depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- volume percentile rank vs own history ---
def f12vp_f12_volume_pressure_volrank_126d_base_v038_signal(volume):
    # percentile rank of current volume vs its own 126d history, de-meaned by the
    # rank of the 21d-average (level rank net of trend rank)
    rk = volume.rolling(126, min_periods=63).rank(pct=True)
    rkav = _mean(volume, 21).rolling(126, min_periods=63).rank(pct=True)
    b = rk - rkav
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f12vp_f12_volume_pressure_volrank_252d_base_v039_signal(volume):
    b = volume.rolling(252, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# percentile rank of 5d avg volume vs its 252d history
def f12vp_f12_volume_pressure_avgvolrank_252d_base_v040_signal(volume):
    # average trailing-252d percentile rank of volume over the last quarter
    # (smooth measure of how elevated activity has been vs the year)
    rk = volume.rolling(252, min_periods=126).rank(pct=True)
    b = rk.rolling(63, min_periods=21).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ratio/spread interactions across windows ---
def f12vp_f12_volume_pressure_volzspr_21v63_base_v041_signal(volume):
    b = _z(volume, 21) - _z(volume, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# relative-volume spread: short RVOL minus long RVOL
def f12vp_f12_volume_pressure_relvolspr_21v126_base_v042_signal(volume):
    b = _f12_rel_vol(volume, 21) - _f12_rel_vol(volume, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge ratio momentum: change in the 5v63 surge over a week
def f12vp_f12_volume_pressure_surgemom_5v63_base_v043_signal(volume):
    # surge ACCELERATION: change in the 21v126 surge ratio over a month (2nd-order)
    s = _f12_surge(volume, 21, 126)
    b = (s - s.shift(21)) - (s.shift(21) - s.shift(42))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- volume-weighted by return magnitude (pressure intensity) ---
def f12vp_f12_volume_pressure_intensity_21d_base_v044_signal(closeadj, volume):
    ret = closeadj.pct_change()
    pr = (ret.abs() * volume)
    b = _rsum(pr, 21) / _rsum(volume, 21).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net signed dollar-volume pressure over a quarter
def f12vp_f12_volume_pressure_signdvol_63d_base_v045_signal(closeadj, volume):
    # share of quarterly dollar-volume transacted on UP days minus share on big-up days
    ret = closeadj.pct_change()
    dv = _f12_dollar_vol(closeadj, volume)
    updv = dv.where(ret > 0, 0.0)
    bigup = dv.where(ret > ret.rolling(63, min_periods=21).std(), 0.0)
    b = _rsum(updv, 63) / _rsum(dv, 63).replace(0, np.nan) \
        - _rsum(bigup, 63) / _rsum(dv, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- relative volume on up days vs down days (asymmetry of participation) ---
def f12vp_f12_volume_pressure_udasym_63d_base_v046_signal(closeadj, volume):
    ret = closeadj.pct_change()
    up = volume.where(ret > 0, np.nan)
    dn = volume.where(ret < 0, np.nan)
    ub = up.rolling(63, min_periods=10).mean()
    db = dn.rolling(63, min_periods=10).mean()
    b = (ub - db) / (ub + db).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-weighted return sign over a month (does volume back the move?)
def f12vp_f12_volume_pressure_volweightret_21d_base_v047_signal(closeadj, volume):
    ret = closeadj.pct_change()
    b = _rsum(ret * volume, 21) / _rsum(volume, 21).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- volume acceleration as level (current avg vs avg one month ago) ---
def f12vp_f12_volume_pressure_volaccel_63d_base_v048_signal(volume):
    a = _mean(volume, 21)
    b = a / a.shift(21).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log-volume distance from its slow EMA (displacement)
def f12vp_f12_volume_pressure_voldisp_63d_base_v049_signal(volume):
    # acceleration of log-volume: change in the 5d log-volume momentum (2nd diff level)
    lv = np.log(volume.replace(0, np.nan))
    mom = lv.rolling(5, min_periods=3).mean() - lv.rolling(5, min_periods=3).mean().shift(5)
    b = mom - mom.shift(5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA volume ratio (fast/slow exponential averages)
def f12vp_f12_volume_pressure_volewmratio_base_v050_signal(volume):
    fast = volume.ewm(span=10, min_periods=5).mean()
    slow = volume.ewm(span=63, min_periods=21).mean()
    b = fast / slow.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- relative dollar-volume rank (liquidity-scaled activity percentile) ---
def f12vp_f12_volume_pressure_dvolrank_252d_base_v051_signal(closeadj, volume):
    dv = _f12_dollar_vol(closeadj, volume)
    b = dv.rolling(252, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed log relative-volume (bounded surge intensity)
def f12vp_f12_volume_pressure_relvoltanh_63d_base_v052_signal(volume):
    # bounded surge MOMENTUM: tanh of the change in 5d-avg relative volume over a week
    rv = _mean(volume, 5) / _mean(volume, 63).replace(0, np.nan)
    b = np.tanh(rv - rv.shift(5))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- up/down volume ratio change (pressure rotation) ---
def f12vp_f12_volume_pressure_udmom_63d_base_v053_signal(closeadj, volume):
    r = np.log(_f12_updown_ratio(closeadj, volume, 63))
    b = r - r.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# concentration change over a month (clustering rotation)
def f12vp_f12_volume_pressure_concmom_63d_base_v054_signal(volume):
    c = _f12_concentration(volume, 63)
    b = c - c.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume z-score smoothed by EWMA (persistent abnormal volume)
def f12vp_f12_volume_pressure_volzema_63d_base_v055_signal(volume):
    # persistence of the abnormal-volume SIGN: EWMA of sign(z), a smooth regime gauge
    zz = _z(volume, 63)
    b = np.sign(zz).ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- streak of consecutive above-average-volume days ---
def f12vp_f12_volume_pressure_surgestreak_63d_base_v056_signal(volume):
    avg = _mean(volume, 63)
    above = (volume > avg).astype(float)
    grp = (above == 0).cumsum()
    streak = above.groupby(grp).cumsum()
    # weight streak by current magnitude so it is continuous-valued
    b = streak * (volume / avg.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of quarter with rising volume (5d avg increasing)
def f12vp_f12_volume_pressure_risingfrac_63d_base_v057_signal(volume):
    av = _mean(volume, 5)
    chg = (av - av.shift(1)) / av.shift(1).replace(0, np.nan)
    rising = (av > av.shift(1)).astype(float)
    frac = rising.rolling(63, min_periods=21).mean()
    b = frac + chg.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- dollar-volume concentration (where big-money days cluster) ---
def f12vp_f12_volume_pressure_dvolconc_63d_base_v058_signal(closeadj, volume):
    dv = _f12_dollar_vol(closeadj, volume)
    b = _f12_concentration(dv, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume coefficient of variation
def f12vp_f12_volume_pressure_dvolcv_126d_base_v059_signal(closeadj, volume):
    dv = _f12_dollar_vol(closeadj, volume)
    b = _std(dv, 126) / _mean(dv, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- relative volume z-scored vs its own distribution (de-trended RVOL) ---
def f12vp_f12_volume_pressure_relvolz_63d_base_v060_signal(volume):
    # how extreme is current relvol vs the running max relvol of the past quarter
    rv = _f12_rel_vol(volume, 63)
    b = rv / _rmax(rv, 63).replace(0, np.nan) - _mean((rv > 1.0).astype(float), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume z capped & signed: extreme-volume indicator with direction
def f12vp_f12_volume_pressure_volzext_63d_base_v061_signal(closeadj, volume):
    zz = _z(volume, 63)
    ret = closeadj.pct_change()
    b = zz.clip(-3, 3) * np.sign(ret)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- volume entropy-like dispersion within window (evenness) ---
def f12vp_f12_volume_pressure_volentropy_21d_base_v062_signal(volume):
    sm = _rsum(volume, 21)
    p = volume / sm.replace(0, np.nan)
    contrib = -(p * np.log(p.replace(0, np.nan)))
    b = contrib.rolling(21, min_periods=10).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- surge magnitude when it surges (avg excess on high days) ---
def f12vp_f12_volume_pressure_surgemag_63d_base_v063_signal(volume):
    avg = _mean(volume, 63)
    excess = (volume / avg.replace(0, np.nan) - 1.0).clip(lower=0)
    b = excess.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- volume slope sign persistence (trend direction agreement) ---
def f12vp_f12_volume_pressure_slopesign_63d_base_v064_signal(volume):
    av = _mean(volume, 5)
    d = np.sign(av - av.shift(5))
    persist = d.rolling(63, min_periods=21).mean()
    mag = ((av - av.shift(5)) / av.shift(5).replace(0, np.nan)).rolling(21, min_periods=10).mean()
    b = persist + mag
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- abnormal-volume on big-return days (event participation) ---
def f12vp_f12_volume_pressure_eventvol_63d_base_v065_signal(closeadj, volume):
    ret = closeadj.pct_change()
    big = (ret.abs() > ret.abs().rolling(63, min_periods=21).mean() * 2.0)
    rv = _f12_rel_vol(volume, 63)
    ev = rv.where(big, np.nan)
    b = ev.rolling(63, min_periods=5).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- relative volume asymmetry around the median (skew of activity) ---
def f12vp_f12_volume_pressure_volskew_63d_base_v066_signal(volume):
    lv = np.log(volume.replace(0, np.nan))
    b = lv.rolling(63, min_periods=21).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- kurtosis of volume (spikiness of activity) ---
def f12vp_f12_volume_pressure_volkurt_126d_base_v067_signal(volume):
    lv = np.log(volume.replace(0, np.nan))
    b = lv.rolling(126, min_periods=63).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- dollar-volume vs raw-volume divergence (price-mix effect) ---
def f12vp_f12_volume_pressure_dvmix_63d_base_v068_signal(closeadj, volume):
    dv = _f12_dollar_vol(closeadj, volume)
    rdv = dv / _mean(dv, 63).replace(0, np.nan)
    rv = volume / _mean(volume, 63).replace(0, np.nan)
    b = np.log(rdv.replace(0, np.nan)) - np.log(rv.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- volume pressure index: signed log-relvol weighted by return sign ---
def f12vp_f12_volume_pressure_pressidx_21d_base_v069_signal(closeadj, volume):
    ret = closeadj.pct_change()
    lr = np.log(volume.replace(0, np.nan) / _mean(volume, 63).replace(0, np.nan))
    b = _rsum(np.sign(ret) * lr, 21) / 21.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- accumulation pressure: up-vol minus down-vol normalized, smoothed ---
def f12vp_f12_volume_pressure_accpress_63d_base_v070_signal(closeadj, volume):
    ret = closeadj.pct_change()
    up = volume.where(ret > 0, 0.0)
    dn = volume.where(ret < 0, 0.0)
    net = (_rsum(up, 63) - _rsum(dn, 63)) / _rsum(volume, 63).replace(0, np.nan)
    b = net.ewm(span=10, min_periods=5).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- relative volume regime: current 21d avg vs 252d percentile band ---
def f12vp_f12_volume_pressure_volregime_252d_base_v071_signal(volume):
    av = _mean(volume, 21)
    hi = _rmax(volume, 252)
    lo = _rmin(volume, 252)
    b = (av - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- volume "thrust": one-day spike relative to 5d baseline ---
def f12vp_f12_volume_pressure_thrust_5d_base_v072_signal(volume):
    base = _mean(volume.shift(1), 5)
    b = volume / base.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- net buying pressure dollar-weighted, ranked ---
def f12vp_f12_volume_pressure_netpressrank_126d_base_v073_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f12_dollar_vol(closeadj, volume)
    net = _rsum(np.sign(ret) * dv, 21) / _rsum(dv, 21).replace(0, np.nan)
    b = net.rolling(126, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- volume trend vs price trend agreement (does vol confirm direction sign) ---
def f12vp_f12_volume_pressure_voltrendconf_63d_base_v074_signal(closeadj, volume):
    vsl = _slope(np.log(volume.replace(0, np.nan)), 63)
    psl = _slope(np.log(closeadj.replace(0, np.nan)), 63)
    b = vsl * np.sign(psl)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- relative volume dispersion across 5/21/63 windows (regime breadth) ---
def f12vp_f12_volume_pressure_relvoldisp_multi_base_v075_signal(volume):
    r1 = _f12_rel_vol(volume, 5)
    r2 = _f12_rel_vol(volume, 21)
    r3 = _f12_rel_vol(volume, 63)
    b = pd.concat([r1, r2, r3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f12vp_f12_volume_pressure_volz_21d_base_v001_signal,
    f12vp_f12_volume_pressure_volz_63d_base_v002_signal,
    f12vp_f12_volume_pressure_volz_126d_base_v003_signal,
    f12vp_f12_volume_pressure_logvolz_63d_base_v004_signal,
    f12vp_f12_volume_pressure_volmadz_63d_base_v005_signal,
    f12vp_f12_volume_pressure_relvol_63d_base_v006_signal,
    f12vp_f12_volume_pressure_relvol_21d_base_v007_signal,
    f12vp_f12_volume_pressure_relvol_252d_base_v008_signal,
    f12vp_f12_volume_pressure_relvolsm_63d_base_v009_signal,
    f12vp_f12_volume_pressure_logrelvol_63d_base_v010_signal,
    f12vp_f12_volume_pressure_surge_5v63_base_v011_signal,
    f12vp_f12_volume_pressure_surge_21v126_base_v012_signal,
    f12vp_f12_volume_pressure_surge_5v21_base_v013_signal,
    f12vp_f12_volume_pressure_surge_21v252_base_v014_signal,
    f12vp_f12_volume_pressure_spikemax_63d_base_v015_signal,
    f12vp_f12_volume_pressure_udvol_21d_base_v016_signal,
    f12vp_f12_volume_pressure_udvol_63d_base_v017_signal,
    f12vp_f12_volume_pressure_udvol_126d_base_v018_signal,
    f12vp_f12_volume_pressure_upvolshare_21d_base_v019_signal,
    f12vp_f12_volume_pressure_dnvolshare_63d_base_v020_signal,
    f12vp_f12_volume_pressure_signvolpr_21d_base_v021_signal,
    f12vp_f12_volume_pressure_signvolpr_63d_base_v022_signal,
    f12vp_f12_volume_pressure_volslope_21d_base_v023_signal,
    f12vp_f12_volume_pressure_volslope_63d_base_v024_signal,
    f12vp_f12_volume_pressure_logvolslope_63d_base_v025_signal,
    f12vp_f12_volume_pressure_dvolz_63d_base_v026_signal,
    f12vp_f12_volume_pressure_dvolz_126d_base_v027_signal,
    f12vp_f12_volume_pressure_dvolrel_63d_base_v028_signal,
    f12vp_f12_volume_pressure_dvolsurge_21v126_base_v029_signal,
    f12vp_f12_volume_pressure_dvolslope_63d_base_v030_signal,
    f12vp_f12_volume_pressure_dvolyoy_252d_base_v031_signal,
    f12vp_f12_volume_pressure_conc_21d_base_v032_signal,
    f12vp_f12_volume_pressure_conc_63d_base_v033_signal,
    f12vp_f12_volume_pressure_volcv_63d_base_v034_signal,
    f12vp_f12_volume_pressure_topday_63d_base_v035_signal,
    f12vp_f12_volume_pressure_surgefreq_63d_base_v036_signal,
    f12vp_f12_volume_pressure_quietfreq_63d_base_v037_signal,
    f12vp_f12_volume_pressure_volrank_126d_base_v038_signal,
    f12vp_f12_volume_pressure_volrank_252d_base_v039_signal,
    f12vp_f12_volume_pressure_avgvolrank_252d_base_v040_signal,
    f12vp_f12_volume_pressure_volzspr_21v63_base_v041_signal,
    f12vp_f12_volume_pressure_relvolspr_21v126_base_v042_signal,
    f12vp_f12_volume_pressure_surgemom_5v63_base_v043_signal,
    f12vp_f12_volume_pressure_intensity_21d_base_v044_signal,
    f12vp_f12_volume_pressure_signdvol_63d_base_v045_signal,
    f12vp_f12_volume_pressure_udasym_63d_base_v046_signal,
    f12vp_f12_volume_pressure_volweightret_21d_base_v047_signal,
    f12vp_f12_volume_pressure_volaccel_63d_base_v048_signal,
    f12vp_f12_volume_pressure_voldisp_63d_base_v049_signal,
    f12vp_f12_volume_pressure_volewmratio_base_v050_signal,
    f12vp_f12_volume_pressure_dvolrank_252d_base_v051_signal,
    f12vp_f12_volume_pressure_relvoltanh_63d_base_v052_signal,
    f12vp_f12_volume_pressure_udmom_63d_base_v053_signal,
    f12vp_f12_volume_pressure_concmom_63d_base_v054_signal,
    f12vp_f12_volume_pressure_volzema_63d_base_v055_signal,
    f12vp_f12_volume_pressure_surgestreak_63d_base_v056_signal,
    f12vp_f12_volume_pressure_risingfrac_63d_base_v057_signal,
    f12vp_f12_volume_pressure_dvolconc_63d_base_v058_signal,
    f12vp_f12_volume_pressure_dvolcv_126d_base_v059_signal,
    f12vp_f12_volume_pressure_relvolz_63d_base_v060_signal,
    f12vp_f12_volume_pressure_volzext_63d_base_v061_signal,
    f12vp_f12_volume_pressure_volentropy_21d_base_v062_signal,
    f12vp_f12_volume_pressure_surgemag_63d_base_v063_signal,
    f12vp_f12_volume_pressure_slopesign_63d_base_v064_signal,
    f12vp_f12_volume_pressure_eventvol_63d_base_v065_signal,
    f12vp_f12_volume_pressure_volskew_63d_base_v066_signal,
    f12vp_f12_volume_pressure_volkurt_126d_base_v067_signal,
    f12vp_f12_volume_pressure_dvmix_63d_base_v068_signal,
    f12vp_f12_volume_pressure_pressidx_21d_base_v069_signal,
    f12vp_f12_volume_pressure_accpress_63d_base_v070_signal,
    f12vp_f12_volume_pressure_volregime_252d_base_v071_signal,
    f12vp_f12_volume_pressure_thrust_5d_base_v072_signal,
    f12vp_f12_volume_pressure_netpressrank_126d_base_v073_signal,
    f12vp_f12_volume_pressure_voltrendconf_63d_base_v074_signal,
    f12vp_f12_volume_pressure_relvoldisp_multi_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F12_VOLUME_PRESSURE_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.005, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.01, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.01, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)) + 1e5, name="volume")

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
        assert q.nunique() > 50, "%s nunique=%d" % (name, q.nunique())
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

    print("OK f12_volume_pressure_base_001_075_claude: %d features pass" % n_features)
