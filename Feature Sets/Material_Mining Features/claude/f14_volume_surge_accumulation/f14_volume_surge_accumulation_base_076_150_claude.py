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


# ============================================================
# volume surge z over 21d (short, fast surge framing)
def f14vs_f14_volume_surge_accumulation_volz_21d_base_v076_signal(volume):
    b = _f14_vol_z(volume, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 5d-mean volume vs 21d-mean volume (very-short surge ramp)
def f14vs_f14_volume_surge_accumulation_surge_5v21_base_v077_signal(volume):
    short = volume.rolling(5, min_periods=3).mean()
    long = volume.rolling(21, min_periods=10).mean()
    b = short / long.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 21d-mean vs 252d-mean volume (monthly surge vs annual base)
def f14vs_f14_volume_surge_accumulation_surge_21v252_base_v078_signal(volume):
    short = volume.rolling(21, min_periods=10).mean()
    long = volume.rolling(252, min_periods=126).mean()
    b = np.log(short.replace(0, np.nan) / long.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 63d-mean vs 252d-mean volume (quarterly elevation vs annual)
def f14vs_f14_volume_surge_accumulation_surge_63v252_base_v079_signal(volume):
    short = volume.rolling(63, min_periods=21).mean()
    long = volume.rolling(252, min_periods=126).mean()
    b = np.log(short.replace(0, np.nan) / long.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up/down volume share over 5d (very-short accumulation pressure)
def f14vs_f14_volume_surge_accumulation_updn_5d_base_v080_signal(closeadj, volume):
    b = _f14_updown_vol(closeadj, volume, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up/down volume share over 252d (annual accumulation bias)
def f14vs_f14_volume_surge_accumulation_updn_252d_base_v081_signal(closeadj, volume):
    b = _f14_updown_vol(closeadj, volume, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net signed-volume slope: change in 63d signed-volume share over a month
def f14vs_f14_volume_surge_accumulation_accslope_63d_base_v082_signal(closeadj, volume):
    ret = closeadj.pct_change()
    signed = np.sign(ret) * volume
    s = signed.rolling(63, min_periods=21).sum()
    t = volume.rolling(63, min_periods=21).sum()
    share = s / t.replace(0, np.nan)
    b = share - share.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume level: log of 63d-mean dollar-volume (size/liquidity scale)
def f14vs_f14_volume_surge_accumulation_dvlevel_63d_base_v083_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume).rolling(63, min_periods=21).mean()
    b = np.log(dv.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume surge breadth: count of days dollar-vol above its own 126d 80th pctile
def f14vs_f14_volume_surge_accumulation_dvsurge_126d_base_v084_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    thr = dv.rolling(126, min_periods=63).quantile(0.80)
    cnt = (dv > thr).astype(float).rolling(63, min_periods=21).sum()
    depth = (dv / thr.replace(0, np.nan) - 1.0).clip(lower=0).where(dv > thr, 0.0).rolling(63, min_periods=21).sum()
    b = cnt + depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume trend over a quarter, z-scored vs 252d (relative liquidity momentum)
def f14vs_f14_volume_surge_accumulation_dvtrendz_63d_base_v085_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume).rolling(21, min_periods=10).mean()
    tr = np.log(dv.replace(0, np.nan) / dv.shift(63).replace(0, np.nan))
    b = _z(tr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# move-confirmed accumulation: return magnitude weighted by volume share, signed, 126d
def f14vs_f14_volume_surge_accumulation_accconfirm_63d_base_v086_signal(closeadj, volume):
    ret = closeadj.pct_change()
    w = volume / volume.rolling(126, min_periods=63).sum().replace(0, np.nan)
    b = (ret * w).rolling(126, min_periods=63).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# news-day volume premium: avg volume on big-move days vs quiet days over 63d
def f14vs_f14_volume_surge_accumulation_newsvolprem_63d_base_v087_signal(closeadj, volume):
    aret = closeadj.pct_change().abs()
    thr = aret.rolling(63, min_periods=21).median()
    lv = np.log(volume.clip(lower=1.0))
    big = lv.where(aret > thr, np.nan).rolling(63, min_periods=21).mean()
    quiet = lv.where(aret <= thr, np.nan).rolling(63, min_periods=21).mean()
    b = big - quiet
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-return rank correlation proxy: covariance of vol-rank and |ret|-rank, 63d
def f14vs_f14_volume_surge_accumulation_volretcorr_63d_base_v088_signal(closeadj, volume):
    aret = closeadj.pct_change().abs()
    rv = volume.rolling(63, min_periods=21).rank(pct=True)
    rr = aret.rolling(63, min_periods=21).rank(pct=True)
    b = ((rv - 0.5) * (rr - 0.5)).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Herfindahl of volume over 252d (annual concentration of activity)
def f14vs_f14_volume_surge_accumulation_herf_252d_base_v089_signal(volume):
    b = _f14_herfindahl(volume, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# top-3-day volume share within 21d (acute burst concentration)
def f14vs_f14_volume_surge_accumulation_top3share_21d_base_v090_signal(volume):
    def _top3(a):
        s = np.sort(a)[-3:].sum()
        tot = a.sum()
        if tot <= 0:
            return np.nan
        return s / tot
    b = volume.rolling(21, min_periods=10).apply(_top3, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge-day count vs own-volume 80th pctile over 63d, magnitude-weighted
def f14vs_f14_volume_surge_accumulation_scount80_63d_base_v091_signal(volume):
    thr = volume.rolling(252, min_periods=126).quantile(0.80)
    avg = volume.rolling(63, min_periods=21).mean()
    ratio = volume / avg.replace(0, np.nan)
    cnt = (volume > thr).astype(float).rolling(63, min_periods=21).sum()
    depth = (ratio - 1.0).clip(lower=0).where(volume > thr, 0.0).rolling(63, min_periods=21).sum()
    b = cnt + depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# extreme surge count vs own 95th pctile over 252d, magnitude-weighted
def f14vs_f14_volume_surge_accumulation_scount95_252d_base_v092_signal(volume):
    thr = volume.rolling(252, min_periods=126).quantile(0.95)
    avg = volume.rolling(126, min_periods=63).mean()
    ratio = volume / avg.replace(0, np.nan)
    cnt = (volume > thr).astype(float).rolling(252, min_periods=126).sum()
    depth = (ratio - 1.0).clip(lower=0).where(volume > thr, 0.0).rolling(252, min_periods=126).sum()
    b = cnt + depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of 126d in upper tercile of volume, overshoot-tilted (sustained-high regime)
def f14vs_f14_volume_surge_accumulation_uppertile_126d_base_v093_signal(volume):
    q = volume.rolling(252, min_periods=126).quantile(0.6667)
    above = (volume > q).astype(float)
    frac = above.rolling(126, min_periods=63).mean()
    overshoot = (volume / q.replace(0, np.nan) - 1.0).clip(lower=0).rolling(126, min_periods=63).mean()
    b = frac + overshoot
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume z-score over 252d (annual dollar-liquidity extremity)
def f14vs_f14_volume_surge_accumulation_dvz_252d_base_v094_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    b = _z(np.log(dv.clip(lower=1.0)), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume EWMA crossover: fast EWMA vs slow EWMA of log-volume (trend surge)
def f14vs_f14_volume_surge_accumulation_volxover_base_v095_signal(volume):
    lv = np.log(volume.clip(lower=1.0))
    fast = lv.ewm(span=10, min_periods=5).mean()
    slow = lv.ewm(span=63, min_periods=21).mean()
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume MACD-style histogram change (acceleration of EWMA crossover)
def f14vs_f14_volume_surge_accumulation_volmacd_base_v096_signal(volume):
    lv = np.log(volume.clip(lower=1.0))
    macd = lv.ewm(span=12, min_periods=6).mean() - lv.ewm(span=26, min_periods=13).mean()
    sig = macd.ewm(span=9, min_periods=5).mean()
    b = macd - sig
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net dollar-flow share over 126d (dollar-weighted accumulation balance)
def f14vs_f14_volume_surge_accumulation_dvflow_126d_base_v097_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f14_dollar_vol(closeadj, volume)
    up = dv.where(ret > 0, 0.0).rolling(126, min_periods=63).sum()
    dn = dv.where(ret < 0, 0.0).rolling(126, min_periods=63).sum()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return weighted by volume rank, summed over 63d (rank-flow accumulation)
def f14vs_f14_volume_surge_accumulation_rankflow_63d_base_v098_signal(closeadj, volume):
    ret = closeadj.pct_change()
    rv = volume.rolling(63, min_periods=21).rank(pct=True)
    b = (np.sign(ret) * rv).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume trend slope via OLS over 63d (linear log-volume drift)
def f14vs_f14_volume_surge_accumulation_volols_63d_base_v099_signal(volume):
    lv = np.log(volume.clip(lower=1.0))
    x = np.arange(63, dtype=float)
    xm = x.mean()
    den = ((x - xm) ** 2).sum()

    def _slope(a):
        return ((x - xm) * (a - a.mean())).sum() / den
    b = lv.rolling(63, min_periods=63).apply(_slope, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume trend slope via OLS over 126d
def f14vs_f14_volume_surge_accumulation_dvols_126d_base_v100_signal(closeadj, volume):
    ldv = np.log(_f14_dollar_vol(closeadj, volume).clip(lower=1.0))
    x = np.arange(126, dtype=float)
    xm = x.mean()
    den = ((x - xm) ** 2).sum()

    def _slope(a):
        return ((x - xm) * (a - a.mean())).sum() / den
    b = ldv.rolling(126, min_periods=126).apply(_slope, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume Bollinger position: where vol sits in its 63d mean +/- 2std band
def f14vs_f14_volume_surge_accumulation_volboll_63d_base_v101_signal(volume):
    m = volume.rolling(63, min_periods=21).mean()
    sd = volume.rolling(63, min_periods=21).std()
    b = (volume - m) / (2.0 * sd).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation persistence: EWMA of signed-volume-share, then its 63d-min floor distance
def f14vs_f14_volume_surge_accumulation_accpersist_63d_base_v102_signal(closeadj, volume):
    ret = closeadj.pct_change()
    avg = volume.rolling(63, min_periods=21).mean()
    pressure = np.sign(ret) * (volume / avg.replace(0, np.nan))
    smooth = pressure.ewm(span=21, min_periods=10).mean()
    b = smooth - smooth.rolling(63, min_periods=21).min()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-of-volume ratio: 21d log-vol std vs 126d log-vol std (spikiness regime shift)
def f14vs_f14_volume_surge_accumulation_vovratio_base_v103_signal(volume):
    lv = np.log(volume.clip(lower=1.0))
    short = lv.rolling(21, min_periods=10).std()
    long = lv.rolling(126, min_periods=63).std()
    b = short / long.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# largest single-day dollar-volume share within 63d (whale-trade concentration)
def f14vs_f14_volume_surge_accumulation_dvmaxshare_63d_base_v104_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    mx = dv.rolling(63, min_periods=21).max()
    tot = dv.rolling(63, min_periods=21).sum()
    b = mx / tot.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge ratio sign-magnitude over 21d (bounded compression of surge intensity)
def f14vs_f14_volume_surge_accumulation_surgesm_21d_base_v105_signal(volume):
    sr = _f14_surge_ratio(volume, 21) - 1.0
    sm = np.sign(sr) * (sr.abs() ** 0.5)
    b = sm.rolling(5, min_periods=3).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up-volume minus down-volume momentum imbalance over 126d, smoothed
def f14vs_f14_volume_surge_accumulation_imbal_126d_base_v106_signal(closeadj, volume):
    ud = _f14_updown_vol(closeadj, volume, 126)
    b = (ud - 0.5).ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume surge over a quarter ranked vs 504d (long-horizon relative surge)
def f14vs_f14_volume_surge_accumulation_surgerank_504d_base_v107_signal(volume):
    sm = volume.rolling(63, min_periods=21).mean()
    b = _rank(sm, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume drawdown over 504d (long liquidity-fade from peak)
def f14vs_f14_volume_surge_accumulation_dvdd_504d_base_v108_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume).rolling(21, min_periods=10).mean()
    peak = dv.rolling(504, min_periods=252).max()
    b = dv / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-weighted average up-move minus vol-weighted average down-move (63d)
def f14vs_f14_volume_surge_accumulation_vwmove_63d_base_v109_signal(closeadj, volume):
    ret = closeadj.pct_change()
    upw = (ret.clip(lower=0) * volume).rolling(63, min_periods=21).sum()
    dnw = (ret.clip(upper=0).abs() * volume).rolling(63, min_periods=21).sum()
    b = (upw - dnw) / (upw + dnw).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume regime streak: signed run-length of above/below 63d-avg, normalized
def f14vs_f14_volume_surge_accumulation_volstreak_63d_base_v110_signal(volume):
    avg = volume.rolling(63, min_periods=21).mean()
    above = (volume > avg).astype(float)
    persist = above.rolling(10, min_periods=5).mean()
    b = (persist - 0.5) * (volume / avg.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume acceleration: change in 63d OLS dollar-vol slope over a quarter
def f14vs_f14_volume_surge_accumulation_dvslopechg_base_v111_signal(closeadj, volume):
    ldv = np.log(_f14_dollar_vol(closeadj, volume).clip(lower=1.0)).rolling(21, min_periods=10).mean()
    t = np.log(ldv.replace(0, np.nan))
    slope = ldv - ldv.shift(63)
    b = slope - slope.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge breadth: count distinct local-peak volume days over 63d, depth-weighted
def f14vs_f14_volume_surge_accumulation_localpeaks_63d_base_v112_signal(volume):
    is_peak = ((volume > volume.shift(1)) & (volume > volume.shift(-1))).astype(float)
    avg = volume.rolling(63, min_periods=21).mean()
    depth = (volume / avg.replace(0, np.nan)).where(is_peak > 0, 0.0)
    b = depth.rolling(63, min_periods=21).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation on news rank: signed-vol share ranked vs 252d (relative accumulation)
def f14vs_f14_volume_surge_accumulation_accrank_252d_base_v113_signal(closeadj, volume):
    ret = closeadj.pct_change()
    signed = np.sign(ret) * volume
    share = signed.rolling(63, min_periods=21).sum() / volume.rolling(63, min_periods=21).sum().replace(0, np.nan)
    b = _rank(share, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume z impulse over 21d (medium-horizon surge onset)
def f14vs_f14_volume_surge_accumulation_volzimp_21d_base_v114_signal(volume):
    vz = _f14_vol_z(volume, 126)
    b = vz - vz.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Herfindahl ratio: 63d concentration vs 252d concentration (clustering intensification)
def f14vs_f14_volume_surge_accumulation_herfratio_base_v115_signal(volume):
    h63 = _f14_herfindahl(volume, 63)
    h252 = _f14_herfindahl(volume, 252)
    b = h63 / h252.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume surge percentile over 504d, smoothed (long relative liquidity spike)
def f14vs_f14_volume_surge_accumulation_dvsurgerank_504d_base_v116_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume).rolling(5, min_periods=3).mean()
    b = _rank(dv, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-buying acceleration: signed-vol share change quarter-over-quarter
def f14vs_f14_volume_surge_accumulation_accaccel_base_v117_signal(closeadj, volume):
    ret = closeadj.pct_change()
    signed = np.sign(ret) * volume
    share = signed.rolling(63, min_periods=21).sum() / volume.rolling(63, min_periods=21).sum().replace(0, np.nan)
    b = (share - share.shift(63)) - (share.shift(63) - share.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume skew over 126d (long-horizon spike asymmetry)
def f14vs_f14_volume_surge_accumulation_volskew_126d_base_v118_signal(volume):
    lv = np.log(volume.clip(lower=1.0))
    b = lv.rolling(126, min_periods=63).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume entropy proxy: normalized inverse Herfindahl effective days over 126d
def f14vs_f14_volume_surge_accumulation_effdays_126d_base_v119_signal(volume):
    h = _f14_herfindahl(volume, 126)
    b = 1.0 - (1.0 / h.replace(0, np.nan)) / 126.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# climactic-volume flag intensity: vol z x absolute return, smoothed 21d
def f14vs_f14_volume_surge_accumulation_climax_21d_base_v120_signal(closeadj, volume):
    vz = _f14_vol_z(volume, 63).clip(lower=0)
    aret = closeadj.pct_change().abs()
    b = (vz * aret).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume vol-of-vol: std of log dollar-volume over 63d (liquidity instability)
def f14vs_f14_volume_surge_accumulation_dvvov_63d_base_v121_signal(closeadj, volume):
    ldv = np.log(_f14_dollar_vol(closeadj, volume).clip(lower=1.0))
    b = ldv.rolling(63, min_periods=21).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge-then-fade: 5d surge ratio minus its value 5d ago (impulse onset/decay)
def f14vs_f14_volume_surge_accumulation_surgeimp_5d_base_v122_signal(volume):
    sr = volume.rolling(5, min_periods=3).mean() / volume.rolling(63, min_periods=21).mean().replace(0, np.nan)
    b = sr - sr.shift(5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distribution intensity: down-day surge excess vs up-day surge excess over 63d (selling on volume)
def f14vs_f14_volume_surge_accumulation_distrib_63d_base_v123_signal(closeadj, volume):
    ret = closeadj.pct_change()
    avg = volume.rolling(63, min_periods=21).mean()
    excess = (volume / avg.replace(0, np.nan) - 1.0).clip(lower=0)
    dn = excess.where(ret < 0, 0.0).rolling(63, min_periods=21).mean()
    up = excess.where(ret > 0, 0.0).rolling(63, min_periods=21).mean()
    b = dn - up
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume momentum vs price momentum divergence over 63d (vol leading/lagging price)
def f14vs_f14_volume_surge_accumulation_vpdiverge_63d_base_v124_signal(closeadj, volume):
    vm = np.log(volume.rolling(21, min_periods=10).mean().replace(0, np.nan)
                / volume.rolling(21, min_periods=10).mean().shift(63).replace(0, np.nan))
    pm = np.log(closeadj.replace(0, np.nan) / closeadj.shift(63).replace(0, np.nan))
    b = vm - pm
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# concentration of up-volume: Herfindahl of up-day volumes over 63d
def f14vs_f14_volume_surge_accumulation_upherf_63d_base_v125_signal(closeadj, volume):
    ret = closeadj.pct_change()
    uv = volume.where(ret > 0, 0.0)
    tot = uv.rolling(63, min_periods=21).sum()
    sq = (uv * uv).rolling(63, min_periods=21).sum()
    b = sq / (tot * tot).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume momentum z over 126d (relative dollar-liquidity acceleration)
def f14vs_f14_volume_surge_accumulation_dvmomz_126d_base_v126_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume).rolling(21, min_periods=10).mean()
    mom = np.log(dv.replace(0, np.nan) / dv.shift(21).replace(0, np.nan))
    b = _z(mom, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of 63d that volume is rising day-over-day, tilted by magnitude
def f14vs_f14_volume_surge_accumulation_volrise_63d_base_v127_signal(volume):
    rising = (volume > volume.shift(1)).astype(float)
    frac = rising.rolling(63, min_periods=21).mean()
    mag = (volume / volume.shift(1).replace(0, np.nan) - 1.0).clip(-2, 2).rolling(63, min_periods=21).mean()
    b = (frac - 0.5) + mag
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# structural-interest growth: 504d log-vol OLS slope (multi-year drift in activity)
def f14vs_f14_volume_surge_accumulation_growth_504d_base_v128_signal(volume):
    lv = np.log(volume.clip(lower=1.0)).rolling(21, min_periods=10).mean()
    b = lv - lv.shift(504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net accumulation index slope over 504d (long-horizon cumulative signed-vol trend)
def f14vs_f14_volume_surge_accumulation_accindex_504d_base_v129_signal(closeadj, volume):
    ret = closeadj.pct_change()
    signed = np.sign(ret) * volume
    cum = signed.rolling(504, min_periods=252).sum()
    tot = volume.rolling(504, min_periods=252).sum()
    b = cum / tot.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume kurtosis over 63d (short-horizon fat-tail spike detector)
def f14vs_f14_volume_surge_accumulation_volkurt_63d_base_v130_signal(volume):
    lv = np.log(volume.clip(lower=1.0))
    b = lv.rolling(63, min_periods=21).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge-confirmed price thrust: 5d return when 5d volume is elevated (news thrust)
def f14vs_f14_volume_surge_accumulation_thrust_5d_base_v131_signal(closeadj, volume):
    r5 = np.log(closeadj.replace(0, np.nan) / closeadj.shift(5).replace(0, np.nan))
    vr = volume.rolling(5, min_periods=3).mean() / volume.rolling(63, min_periods=21).mean().replace(0, np.nan)
    b = r5 * (vr - 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume Herfindahl over 126d (dollar-weighted concentration)
def f14vs_f14_volume_surge_accumulation_dvherf_126d_base_v132_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    b = _f14_herfindahl(dv, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume range expansion: 63d log-vol range minus its 252d typical range
def f14vs_f14_volume_surge_accumulation_volrangeexp_base_v133_signal(volume):
    lv = np.log(volume.clip(lower=1.0))
    rng63 = lv.rolling(63, min_periods=21).max() - lv.rolling(63, min_periods=21).min()
    rng252 = (lv.rolling(63, min_periods=21).max() - lv.rolling(63, min_periods=21).min()).rolling(252, min_periods=126).mean()
    b = rng63 - rng252
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation quality: up-vol share x positive trend (confirmed accumulation)
def f14vs_f14_volume_surge_accumulation_accquality_63d_base_v134_signal(closeadj, volume):
    ud = _f14_updown_vol(closeadj, volume, 63)
    trend = np.log(closeadj.replace(0, np.nan) / closeadj.shift(63).replace(0, np.nan))
    b = (ud - 0.5) * np.sign(trend) * (trend.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume z conditioned on direction: signed mean volume z over 21d
def f14vs_f14_volume_surge_accumulation_signedvolz_21d_base_v135_signal(closeadj, volume):
    ret = closeadj.pct_change()
    vz = _f14_vol_z(volume, 63)
    b = (np.sign(ret) * vz).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume trend vs price trend ratio over 126d (liquidity vs price coupling)
def f14vs_f14_volume_surge_accumulation_dvprice_126d_base_v136_signal(closeadj, volume):
    dvt = np.log(_f14_dollar_vol(closeadj, volume).rolling(21, min_periods=10).mean().replace(0, np.nan)
                 / _f14_dollar_vol(closeadj, volume).rolling(21, min_periods=10).mean().shift(126).replace(0, np.nan))
    pt = np.log(closeadj.replace(0, np.nan) / closeadj.shift(126).replace(0, np.nan))
    b = dvt - 2.0 * pt
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# proportion of total 126d volume in the heaviest 21d window (burst window share)
def f14vs_f14_volume_surge_accumulation_burstwin_126d_base_v137_signal(volume):
    w21 = volume.rolling(21, min_periods=10).sum()
    mx = w21.rolling(126, min_periods=63).max()
    tot = volume.rolling(126, min_periods=63).sum()
    b = mx / tot.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume autocorrelation lag-5 over 126d (weekly persistence of activity)
def f14vs_f14_volume_surge_accumulation_volac5_126d_base_v138_signal(volume):
    lv = np.log(volume.clip(lower=1.0))
    b = lv.rolling(126, min_periods=63).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=False)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge sustainability: how many of next-vs-now... (5d surge minus its own 63d max-surge)
def f14vs_f14_volume_surge_accumulation_surgesust_63d_base_v139_signal(volume):
    sr = volume.rolling(5, min_periods=3).mean() / volume.rolling(63, min_periods=21).mean().replace(0, np.nan)
    b = sr / sr.rolling(63, min_periods=21).max().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume net-flow sign-magnitude over 126d (dollar accumulation, compressed)
def f14vs_f14_volume_surge_accumulation_dvflowsm_126d_base_v140_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f14_dollar_vol(closeadj, volume)
    up = dv.where(ret > 0, 0.0).rolling(126, min_periods=63).sum()
    dn = dv.where(ret < 0, 0.0).rolling(126, min_periods=63).sum()
    bal = (up - dn) / (up + dn).replace(0, np.nan)
    b = np.sign(bal) * (bal.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume z above price-move expectation: vol z minus |ret| z over 63d (excess interest)
def f14vs_f14_volume_surge_accumulation_excessvol_63d_base_v141_signal(closeadj, volume):
    vz = _f14_vol_z(volume, 63)
    rz = _z(closeadj.pct_change().abs(), 63)
    b = vz - rz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of 252d in bottom-tercile volume (illiquidity/dry regime), depth-tilted
def f14vs_f14_volume_surge_accumulation_lowtile_252d_base_v142_signal(volume):
    q = volume.rolling(252, min_periods=126).quantile(0.3333)
    below = (volume < q).astype(float)
    frac = below.rolling(252, min_periods=126).mean()
    depth = (1.0 - volume / q.replace(0, np.nan)).clip(lower=0).rolling(252, min_periods=126).mean()
    b = frac + depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation breadth: net up-day count weighted by surge over 252d
def f14vs_f14_volume_surge_accumulation_accbreadth_252d_base_v143_signal(closeadj, volume):
    ret = closeadj.pct_change()
    avg = volume.rolling(63, min_periods=21).mean()
    excess = (volume / avg.replace(0, np.nan) - 1.0).clip(lower=0)
    w = np.sign(ret) * excess
    b = w.rolling(252, min_periods=126).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume mean-reversion z: today's vol vs 5d-ago vol normalized by 63d std
def f14vs_f14_volume_surge_accumulation_volmrz_base_v144_signal(volume):
    diff = volume - volume.shift(5)
    sd = volume.rolling(63, min_periods=21).std()
    b = diff / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume tail-spread P95/P50 over 126d (dollar upper-tail heaviness)
def f14vs_f14_volume_surge_accumulation_dvtail_126d_base_v145_signal(closeadj, volume):
    dv = _f14_dollar_vol(closeadj, volume)
    p95 = dv.rolling(126, min_periods=63).quantile(0.95)
    p50 = dv.rolling(126, min_periods=63).quantile(0.50)
    b = p95 / p50.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume trend consistency: sign-agreement of 21d and 63d log-vol momentum
def f14vs_f14_volume_surge_accumulation_trendcons_base_v146_signal(volume):
    lv = np.log(volume.clip(lower=1.0))
    m21 = lv.rolling(21, min_periods=10).mean() - lv.rolling(21, min_periods=10).mean().shift(21)
    m63 = lv.rolling(63, min_periods=21).mean() - lv.rolling(63, min_periods=21).mean().shift(63)
    b = np.sign(m21) * np.sign(m63) * (m21.abs() + m63.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge clustering ratio: top-3-day vol share over 63d vs 252d (intensifying concentration)
def f14vs_f14_volume_surge_accumulation_clustratio_base_v147_signal(volume):
    def _top3(a):
        s = np.sort(a)[-3:].sum()
        tot = a.sum()
        if tot <= 0:
            return np.nan
        return s / tot
    c63 = volume.rolling(63, min_periods=21).apply(_top3, raw=True)
    base = c63.rolling(252, min_periods=126).mean()
    b = c63 - base
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net dollar-flow momentum: change in 126d dollar-flow share over a quarter
def f14vs_f14_volume_surge_accumulation_dvflowmom_base_v148_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f14_dollar_vol(closeadj, volume)
    up = dv.where(ret > 0, 0.0).rolling(126, min_periods=63).sum()
    dn = dv.where(ret < 0, 0.0).rolling(126, min_periods=63).sum()
    share = (up - dn) / (up + dn).replace(0, np.nan)
    b = share - share.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume z dispersion across windows: std of 21/63/126 log-vol z (multi-scale disagreement)
def f14vs_f14_volume_surge_accumulation_volzdisp_multi_base_v149_signal(volume):
    z1 = _f14_vol_z(volume, 21)
    z2 = _f14_vol_z(volume, 63)
    z3 = _f14_vol_z(volume, 126)
    b = pd.concat([z1, z2, z3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation regime distance: 63d up/down share minus its 252d median share
def f14vs_f14_volume_surge_accumulation_accregdist_base_v150_signal(closeadj, volume):
    ud = _f14_updown_vol(closeadj, volume, 63)
    med = ud.rolling(252, min_periods=126).median()
    b = ud - med
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f14vs_f14_volume_surge_accumulation_volz_21d_base_v076_signal,
    f14vs_f14_volume_surge_accumulation_surge_5v21_base_v077_signal,
    f14vs_f14_volume_surge_accumulation_surge_21v252_base_v078_signal,
    f14vs_f14_volume_surge_accumulation_surge_63v252_base_v079_signal,
    f14vs_f14_volume_surge_accumulation_updn_5d_base_v080_signal,
    f14vs_f14_volume_surge_accumulation_updn_252d_base_v081_signal,
    f14vs_f14_volume_surge_accumulation_accslope_63d_base_v082_signal,
    f14vs_f14_volume_surge_accumulation_dvlevel_63d_base_v083_signal,
    f14vs_f14_volume_surge_accumulation_dvsurge_126d_base_v084_signal,
    f14vs_f14_volume_surge_accumulation_dvtrendz_63d_base_v085_signal,
    f14vs_f14_volume_surge_accumulation_accconfirm_63d_base_v086_signal,
    f14vs_f14_volume_surge_accumulation_newsvolprem_63d_base_v087_signal,
    f14vs_f14_volume_surge_accumulation_volretcorr_63d_base_v088_signal,
    f14vs_f14_volume_surge_accumulation_herf_252d_base_v089_signal,
    f14vs_f14_volume_surge_accumulation_top3share_21d_base_v090_signal,
    f14vs_f14_volume_surge_accumulation_scount80_63d_base_v091_signal,
    f14vs_f14_volume_surge_accumulation_scount95_252d_base_v092_signal,
    f14vs_f14_volume_surge_accumulation_uppertile_126d_base_v093_signal,
    f14vs_f14_volume_surge_accumulation_dvz_252d_base_v094_signal,
    f14vs_f14_volume_surge_accumulation_volxover_base_v095_signal,
    f14vs_f14_volume_surge_accumulation_volmacd_base_v096_signal,
    f14vs_f14_volume_surge_accumulation_dvflow_126d_base_v097_signal,
    f14vs_f14_volume_surge_accumulation_rankflow_63d_base_v098_signal,
    f14vs_f14_volume_surge_accumulation_volols_63d_base_v099_signal,
    f14vs_f14_volume_surge_accumulation_dvols_126d_base_v100_signal,
    f14vs_f14_volume_surge_accumulation_volboll_63d_base_v101_signal,
    f14vs_f14_volume_surge_accumulation_accpersist_63d_base_v102_signal,
    f14vs_f14_volume_surge_accumulation_vovratio_base_v103_signal,
    f14vs_f14_volume_surge_accumulation_dvmaxshare_63d_base_v104_signal,
    f14vs_f14_volume_surge_accumulation_surgesm_21d_base_v105_signal,
    f14vs_f14_volume_surge_accumulation_imbal_126d_base_v106_signal,
    f14vs_f14_volume_surge_accumulation_surgerank_504d_base_v107_signal,
    f14vs_f14_volume_surge_accumulation_dvdd_504d_base_v108_signal,
    f14vs_f14_volume_surge_accumulation_vwmove_63d_base_v109_signal,
    f14vs_f14_volume_surge_accumulation_volstreak_63d_base_v110_signal,
    f14vs_f14_volume_surge_accumulation_dvslopechg_base_v111_signal,
    f14vs_f14_volume_surge_accumulation_localpeaks_63d_base_v112_signal,
    f14vs_f14_volume_surge_accumulation_accrank_252d_base_v113_signal,
    f14vs_f14_volume_surge_accumulation_volzimp_21d_base_v114_signal,
    f14vs_f14_volume_surge_accumulation_herfratio_base_v115_signal,
    f14vs_f14_volume_surge_accumulation_dvsurgerank_504d_base_v116_signal,
    f14vs_f14_volume_surge_accumulation_accaccel_base_v117_signal,
    f14vs_f14_volume_surge_accumulation_volskew_126d_base_v118_signal,
    f14vs_f14_volume_surge_accumulation_effdays_126d_base_v119_signal,
    f14vs_f14_volume_surge_accumulation_climax_21d_base_v120_signal,
    f14vs_f14_volume_surge_accumulation_dvvov_63d_base_v121_signal,
    f14vs_f14_volume_surge_accumulation_surgeimp_5d_base_v122_signal,
    f14vs_f14_volume_surge_accumulation_distrib_63d_base_v123_signal,
    f14vs_f14_volume_surge_accumulation_vpdiverge_63d_base_v124_signal,
    f14vs_f14_volume_surge_accumulation_upherf_63d_base_v125_signal,
    f14vs_f14_volume_surge_accumulation_dvmomz_126d_base_v126_signal,
    f14vs_f14_volume_surge_accumulation_volrise_63d_base_v127_signal,
    f14vs_f14_volume_surge_accumulation_growth_504d_base_v128_signal,
    f14vs_f14_volume_surge_accumulation_accindex_504d_base_v129_signal,
    f14vs_f14_volume_surge_accumulation_volkurt_63d_base_v130_signal,
    f14vs_f14_volume_surge_accumulation_thrust_5d_base_v131_signal,
    f14vs_f14_volume_surge_accumulation_dvherf_126d_base_v132_signal,
    f14vs_f14_volume_surge_accumulation_volrangeexp_base_v133_signal,
    f14vs_f14_volume_surge_accumulation_accquality_63d_base_v134_signal,
    f14vs_f14_volume_surge_accumulation_signedvolz_21d_base_v135_signal,
    f14vs_f14_volume_surge_accumulation_dvprice_126d_base_v136_signal,
    f14vs_f14_volume_surge_accumulation_burstwin_126d_base_v137_signal,
    f14vs_f14_volume_surge_accumulation_volac5_126d_base_v138_signal,
    f14vs_f14_volume_surge_accumulation_surgesust_63d_base_v139_signal,
    f14vs_f14_volume_surge_accumulation_dvflowsm_126d_base_v140_signal,
    f14vs_f14_volume_surge_accumulation_excessvol_63d_base_v141_signal,
    f14vs_f14_volume_surge_accumulation_lowtile_252d_base_v142_signal,
    f14vs_f14_volume_surge_accumulation_accbreadth_252d_base_v143_signal,
    f14vs_f14_volume_surge_accumulation_volmrz_base_v144_signal,
    f14vs_f14_volume_surge_accumulation_dvtail_126d_base_v145_signal,
    f14vs_f14_volume_surge_accumulation_trendcons_base_v146_signal,
    f14vs_f14_volume_surge_accumulation_clustratio_base_v147_signal,
    f14vs_f14_volume_surge_accumulation_dvflowmom_base_v148_signal,
    f14vs_f14_volume_surge_accumulation_volzdisp_multi_base_v149_signal,
    f14vs_f14_volume_surge_accumulation_accregdist_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F14_VOLUME_SURGE_ACCUMULATION_REGISTRY_076_150 = REGISTRY


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

    print("OK f14_volume_surge_accumulation_base_076_150_claude: %d features pass" % n_features)
