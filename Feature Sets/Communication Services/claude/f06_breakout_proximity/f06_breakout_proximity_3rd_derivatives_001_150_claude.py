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


def _slope(s, w):
    # rolling OLS slope over a window of length w (per-step first derivative)
    n = w
    x = np.arange(n, dtype=float)
    xm = x.mean()
    xc = x - xm
    denom = (xc ** 2).sum()

    def _f(a):
        am = a.mean()
        return float((xc * (a - am)).sum() / denom)

    return s.rolling(n, min_periods=max(2, n // 2)).apply(_f, raw=True)


def _diff_slope(s, w):
    # simple per-step first derivative: change over w steps divided by w
    return (s - s.shift(w)) / float(w)


def _jerk(s, w):
    # second derivative proxy: difference of the w-step slope, over w steps
    sl = (s - s.shift(w)) / float(w)
    return (sl - sl.shift(w)) / float(w)


# ===== folder domain primitives (breakout proximity / Donchian) =====
def _f06_donch_pos(price, w):
    hi = price.rolling(w, min_periods=max(1, w // 2)).max()
    lo = price.rolling(w, min_periods=max(1, w // 2)).min()
    return (price - lo) / (hi - lo).replace(0, np.nan)


def _f06_dist_high(price, w):
    hi = price.rolling(w, min_periods=max(1, w // 2)).max()
    return price / hi.replace(0, np.nan) - 1.0


def _f06_dist_low(price, w):
    lo = price.rolling(w, min_periods=max(1, w // 2)).min()
    return price / lo.replace(0, np.nan) - 1.0


def _f06_prior_high(price, w):
    return price.shift(1).rolling(w, min_periods=max(1, w // 2)).max()


def _f06_prior_low(price, w):
    return price.shift(1).rolling(w, min_periods=max(1, w // 2)).min()


def _f06_atr(high, low, w):
    return (high - low).rolling(w, min_periods=max(1, w // 2)).mean()


def _f06_band_width(price, w):
    hi = price.rolling(w, min_periods=max(1, w // 2)).max()
    lo = price.rolling(w, min_periods=max(1, w // 2)).min()
    return (hi - lo) / price.replace(0, np.nan)

def f06bp_f06_breakout_proximity_donchpos_21_10d_jerk_v001_signal(close):
    base = _f06_donch_pos(close, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_donchpos_63_21d_jerk_v002_signal(closeadj):
    base = _f06_donch_pos(closeadj, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_donchpos_126_21d_jerk_v003_signal(closeadj):
    base = _f06_donch_pos(closeadj, 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_donchpos_252_42d_jerk_v004_signal(closeadj):
    base = _f06_donch_pos(closeadj, 252)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_disthi_21_10d_jerk_v005_signal(close):
    base = _f06_dist_high(close, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_disthi_63_21d_jerk_v006_signal(closeadj):
    base = _f06_dist_high(closeadj, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_disthi_126_21d_jerk_v007_signal(closeadj):
    base = _f06_dist_high(closeadj, 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_disthi_252_42d_jerk_v008_signal(closeadj):
    base = _f06_dist_high(closeadj, 252)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_distlo_21_10d_jerk_v009_signal(close):
    base = _f06_dist_low(close, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_distlo_63_21d_jerk_v010_signal(closeadj):
    base = _f06_dist_low(closeadj, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_distlo_126_21d_jerk_v011_signal(closeadj):
    base = _f06_dist_low(closeadj, 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_distlo_252_42d_jerk_v012_signal(closeadj):
    base = _f06_dist_low(closeadj, 252)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_gaptohi_63_13d_jerk_v013_signal(closeadj):
    hi = _rmax(closeadj, 63)
    base = np.log(hi.replace(0, np.nan) / closeadj.replace(0, np.nan))
    result = _jerk(base, 13)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_rngexpand_126_21d_jerk_v014_signal(closeadj):
    bw_s = _f06_band_width(closeadj, 21)
    bw_l = _f06_band_width(closeadj, 126)
    base = bw_s / bw_l.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_bandwidth_21_10d_jerk_v015_signal(closeadj):
    base = _f06_band_width(closeadj, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_bandwidth_63_21d_jerk_v016_signal(closeadj):
    base = _f06_band_width(closeadj, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_bandwidth_126_21d_jerk_v017_signal(closeadj):
    base = _f06_band_width(closeadj, 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_brkup_21_10d_jerk_v018_signal(close):
    ph = _f06_prior_high(close, 21)
    base = (close / ph.replace(0, np.nan) - 1.0).clip(lower=0)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_brkup_63_21d_jerk_v019_signal(closeadj):
    ph = _f06_prior_high(closeadj, 63)
    base = (closeadj / ph.replace(0, np.nan) - 1.0).clip(lower=0)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_brkup_126_21d_jerk_v020_signal(closeadj):
    ph = _f06_prior_high(closeadj, 126)
    base = (closeadj / ph.replace(0, np.nan) - 1.0).clip(lower=0)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_brkdn_21_10d_jerk_v021_signal(close):
    pl = _f06_prior_low(close, 21)
    base = (close / pl.replace(0, np.nan) - 1.0).clip(upper=0)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_brkdn_63_21d_jerk_v022_signal(closeadj):
    pl = _f06_prior_low(closeadj, 63)
    base = (closeadj / pl.replace(0, np.nan) - 1.0).clip(upper=0)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_disthiatr_63_21d_jerk_v023_signal(closeadj, high, low):
    hi = _rmax(closeadj, 63)
    atr = _f06_atr(high, low, 21)
    base = (closeadj - hi) / atr.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_distloatr_63_21d_jerk_v024_signal(closeadj, high, low):
    lo = _rmin(closeadj, 63)
    atr = _f06_atr(high, low, 21)
    base = (closeadj - lo) / atr.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_disthiatr_126_21d_jerk_v025_signal(closeadj, high, low):
    hi = _rmax(closeadj, 126)
    atr = _f06_atr(high, low, 21)
    base = (closeadj - hi) / atr.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_hlrngwidth_21_10d_jerk_v026_signal(close, high, low):
    hi = _rmax(high, 21)
    lo = _rmin(low, 21)
    base = (hi - lo) / close.replace(0, np.nan)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_hldonch_63_13d_jerk_v027_signal(closeadj, high, low):
    hi = _rmax(high, 63)
    lo = _rmin(low, 63)
    base = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    result = _jerk(base, 13)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_hldonch_126_13d_jerk_v028_signal(closeadj, high, low):
    hi = _rmax(high, 126)
    lo = _rmin(low, 126)
    base = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    result = _jerk(base, 13)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_clv_21_10d_jerk_v029_signal(close, high, low):
    clv = (2.0 * close - high - low) / (high - low).replace(0, np.nan)
    base = clv.rolling(21, min_periods=10).mean()
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_headwidth_126_34d_jerk_v030_signal(closeadj):
    hi = _rmax(closeadj, 126)
    lo = _rmin(closeadj, 126)
    base = (hi - closeadj) / (hi - lo).replace(0, np.nan)
    result = _jerk(base, 34)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_headwidth_252_34d_jerk_v031_signal(closeadj):
    hi = _rmax(closeadj, 252)
    lo = _rmin(closeadj, 252)
    base = (hi - closeadj) / (hi - lo).replace(0, np.nan)
    result = _jerk(base, 34)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_squeeze_21_21d_jerk_v032_signal(closeadj):
    bw = _f06_band_width(closeadj, 21)
    med = bw.rolling(126, min_periods=63).median()
    base = bw / med.replace(0, np.nan) - 1.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_squeezedepth_63_13d_jerk_v033_signal(closeadj):
    bw = _f06_band_width(closeadj, 63)
    bwmax = bw.rolling(252, min_periods=126).max()
    base = bw / bwmax.replace(0, np.nan)
    result = _jerk(base, 13)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_upperhug_63_21d_jerk_v034_signal(closeadj):
    p = _f06_donch_pos(closeadj, 63)
    base = (p >= 0.9).astype(float).rolling(63, min_periods=21).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_lowerhug_63_21d_jerk_v035_signal(closeadj):
    p = _f06_donch_pos(closeadj, 63)
    base = (p <= 0.1).astype(float).rolling(63, min_periods=21).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_brkvol_21_10d_jerk_v036_signal(close, volume):
    ph = _f06_prior_high(close, 21)
    head = (close / ph.replace(0, np.nan) - 1.0).clip(lower=0)
    vsurge = volume / _mean(volume, 21).replace(0, np.nan)
    base = head * vsurge
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_brkvol_63_21d_jerk_v037_signal(closeadj, volume):
    ph = _f06_prior_high(closeadj, 63)
    head = (closeadj / ph.replace(0, np.nan) - 1.0).clip(lower=0)
    vsurge = volume / _mean(volume, 63).replace(0, np.nan)
    base = head * vsurge
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_dvbrk_63_13d_jerk_v038_signal(closeadj, volume):
    ph = _f06_prior_high(closeadj, 63)
    head = (closeadj / ph.replace(0, np.nan) - 1.0).clip(lower=0)
    dv = closeadj * volume
    dvsurge = dv / _mean(dv, 63).replace(0, np.nan)
    base = head * dvsurge
    result = _jerk(base, 13)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_volconfpos_63_21d_jerk_v039_signal(closeadj, volume):
    pos = _f06_donch_pos(closeadj, 63)
    vtrend = _mean(volume, 21) / _mean(volume, 63).replace(0, np.nan)
    pos_r = pos.rolling(63, min_periods=21).rank(pct=True)
    vol_r = vtrend.rolling(63, min_periods=21).rank(pct=True)
    base = pos_r - vol_r
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_netbreak_63_21d_jerk_v040_signal(closeadj):
    ph = _f06_prior_high(closeadj, 21)
    pl = _f06_prior_low(closeadj, 21)
    up = (closeadj > ph).astype(float)
    dn = (closeadj < pl).astype(float)
    base = (up - dn).rolling(63, min_periods=21).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_newhifreq_21_21d_jerk_v041_signal(close):
    ph = _f06_prior_high(close, 21)
    base = (close > ph).astype(float).rolling(63, min_periods=21).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_posskew_63_21d_jerk_v042_signal(closeadj):
    p = _f06_donch_pos(closeadj, 63)
    base = (p - 0.5).rolling(63, min_periods=21).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_posdisp_63_21d_jerk_v043_signal(closeadj):
    p = _f06_donch_pos(closeadj, 63)
    base = p.rolling(63, min_periods=21).std()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_middistatr_63_21d_jerk_v044_signal(closeadj, high, low):
    hi = _rmax(closeadj, 63)
    lo = _rmin(closeadj, 63)
    mid = (hi + lo) / 2.0
    atr = _f06_atr(high, low, 21)
    base = (closeadj - mid) / atr.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_brkupvol_21_10d_jerk_v045_signal(close, volume):
    pos = _f06_donch_pos(close, 21)
    up = close > close.shift(1)
    upvol = volume.where(up, 0.0).rolling(21, min_periods=10).sum()
    dnvol = volume.where(~up, 0.0).rolling(21, min_periods=10).sum()
    ratio = upvol / (upvol + dnvol).replace(0, np.nan)
    base = pos * (ratio - 0.5)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_thrust_63_21d_jerk_v046_signal(closeadj):
    ph = _f06_prior_high(closeadj, 63)
    at_high = (closeadj >= ph).astype(float)
    ret21 = closeadj / closeadj.shift(21).replace(0, np.nan) - 1.0
    base = at_high.rolling(21, min_periods=10).mean() * ret21
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_brktanh_63_21d_jerk_v047_signal(closeadj):
    ph = _f06_prior_high(closeadj, 63)
    head = closeadj / ph.replace(0, np.nan) - 1.0
    base = np.tanh(15.0 * head)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_convex_63_21d_jerk_v048_signal(close, closeadj):
    p_s = _f06_donch_pos(close, 21)
    p_m = _f06_donch_pos(closeadj, 63)
    p_l = _f06_donch_pos(closeadj, 126)
    base = p_m - 0.5 * (p_s + p_l)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_disthispr_21v126_21d_jerk_v049_signal(close, closeadj):
    s = _f06_dist_high(close, 21)
    l = _f06_dist_high(closeadj, 126)
    base = s - l
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_donchspr_21v252_21d_jerk_v050_signal(close, closeadj):
    s = _f06_donch_pos(close, 21)
    l = _f06_donch_pos(closeadj, 252)
    base = s - l
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_truepremium_63_21d_jerk_v051_signal(closeadj, high):
    hi_true = _rmax(high, 63)
    hi_close = _rmax(closeadj, 63)
    base = hi_true / hi_close.replace(0, np.nan) - 1.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_freshhi_126_21d_jerk_v052_signal(closeadj):
    def _dsh(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    dsh = closeadj.rolling(126, min_periods=63).apply(_dsh, raw=True)
    pos = _f06_donch_pos(closeadj, 126)
    base = (1.0 - dsh) * pos
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_comprpos_70_21d_jerk_v053_signal(closeadj):
    bw = _f06_band_width(closeadj, 21)
    pos = _f06_donch_pos(closeadj, 63) - 0.5
    base = pos / bw.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_squeezedist_63_34d_jerk_v054_signal(closeadj):
    bw = _f06_band_width(closeadj, 63)
    bwmin = bw.rolling(252, min_periods=126).min()
    base = bw / bwmin.replace(0, np.nan) - 1.0
    result = _jerk(base, 34)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_poscentered_252_34d_jerk_v055_signal(closeadj):
    p = _f06_donch_pos(closeadj, 63)
    med = p.rolling(252, min_periods=126).median()
    base = p - med
    result = _jerk(base, 34)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_topdvshare_63_21d_jerk_v056_signal(closeadj, volume):
    pos = _f06_donch_pos(closeadj, 63)
    dv = closeadj * volume
    top_dv = dv.where(pos >= 0.75, 0.0).rolling(63, min_periods=21).sum()
    all_dv = dv.rolling(63, min_periods=21).sum()
    base = top_dv / all_dv.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_clean_63_21d_jerk_v057_signal(closeadj):
    disp = (closeadj - closeadj.shift(63)).abs()
    path = closeadj.diff().abs().rolling(63, min_periods=21).sum()
    eff = disp / path.replace(0, np.nan)
    pos = _f06_donch_pos(closeadj, 63) - 0.5
    base = eff * np.sign(pos)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_brkdnvol_21_10d_jerk_v058_signal(close, volume):
    pl = _f06_prior_low(close, 21)
    depth = (close / pl.replace(0, np.nan) - 1.0).clip(upper=0)
    vsurge = volume / _mean(volume, 21).replace(0, np.nan)
    base = depth * vsurge
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_multiagree_42d_jerk_v059_signal(close, closeadj):
    p1 = _f06_donch_pos(close, 21)
    p2 = _f06_donch_pos(closeadj, 63)
    p3 = _f06_donch_pos(closeadj, 126)
    p4 = _f06_donch_pos(closeadj, 252)
    base = pd.concat([p1, p2, p3, p4], axis=1).mean(axis=1)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_multidisp_42d_jerk_v060_signal(close, closeadj):
    p1 = _f06_donch_pos(close, 21)
    p2 = _f06_donch_pos(closeadj, 63)
    p3 = _f06_donch_pos(closeadj, 126)
    p4 = _f06_donch_pos(closeadj, 252)
    base = pd.concat([p1, p2, p3, p4], axis=1).std(axis=1)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_widthtrend_63_21d_jerk_v061_signal(closeadj):
    bw = _f06_band_width(closeadj, 63)
    base = bw / bw.shift(21).replace(0, np.nan) - 1.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_brkhold_63_21d_jerk_v062_signal(closeadj):
    ph = _f06_prior_high(closeadj, 63).shift(21)
    base = (closeadj >= ph).astype(float).rolling(21, min_periods=10).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_brkfail_63_21d_jerk_v063_signal(closeadj):
    p = _f06_donch_pos(closeadj, 63)
    recent_top = p.rolling(21, min_periods=10).max()
    base = recent_top - p
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_disthi_504_63d_jerk_v064_signal(closeadj):
    d = _f06_dist_high(closeadj, 504)
    base = _z(d, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_donchpos_504_63d_jerk_v065_signal(closeadj):
    base = _f06_donch_pos(closeadj, 504)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_volathigh_63_21d_jerk_v066_signal(closeadj, volume):
    pos = _f06_donch_pos(closeadj, 63)
    near = (pos >= 0.85).astype(float)
    vz = _z(volume, 63)
    base = (near * vz).rolling(21, min_periods=10).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_distrlo_63_21d_jerk_v067_signal(closeadj, volume):
    pos = _f06_donch_pos(closeadj, 63)
    near_low = (pos <= 0.15).astype(float)
    vz = _z(volume, 63)
    base = (near_low * vz).rolling(21, min_periods=10).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_middist_126atr_21d_jerk_v068_signal(closeadj, high, low):
    hi = _rmax(closeadj, 126)
    lo = _rmin(closeadj, 126)
    mid = (hi + lo) / 2.0
    atr = _f06_atr(high, low, 21)
    base = (closeadj - mid) / atr.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_postlow_126_21d_jerk_v069_signal(closeadj):
    def _dsl(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    dsl = closeadj.rolling(126, min_periods=63).apply(_dsl, raw=True)
    pos = _f06_donch_pos(closeadj, 126)
    base = (1.0 - pos) * np.exp(-2.0 * dsl)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_posture_126_13d_jerk_v070_signal(closeadj):
    def _dsh(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    dsh = closeadj.rolling(126, min_periods=63).apply(_dsh, raw=True)
    pos = _f06_donch_pos(closeadj, 126)
    base = pos * np.exp(-2.0 * dsh)
    result = _jerk(base, 13)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_donchmom_63_21d_jerk_v071_signal(closeadj):
    p = _f06_donch_pos(closeadj, 63)
    base = p - p.shift(21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_squeezehead_21_21d_jerk_v072_signal(close):
    bw = _f06_band_width(close, 21)
    tight = (1.0 - bw.rolling(126, min_periods=63).rank(pct=True)).shift(5)
    ph = _f06_prior_high(close, 21)
    head = (close / ph.replace(0, np.nan) - 1.0).clip(lower=0)
    base = tight * head
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_brkup_252_42d_jerk_v073_signal(closeadj):
    ph = _f06_prior_high(closeadj, 252)
    base = (closeadj / ph.replace(0, np.nan) - 1.0).clip(lower=0)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_dshvsdsl_63_21d_jerk_v074_signal(closeadj):
    def _dsh(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    def _dsl(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    dsh = closeadj.rolling(63, min_periods=21).apply(_dsh, raw=True)
    dsl = closeadj.rolling(63, min_periods=21).apply(_dsl, raw=True)
    base = dsl - dsh
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_truedistloatr_126_21d_jerk_v075_signal(closeadj, high, low):
    lo = _rmin(low, 126)
    atr = _f06_atr(high, low, 21)
    base = (closeadj - lo) / atr.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_donchpos_5_5d_jerk_v076_signal(close):
    base = _f06_donch_pos(close, 5)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_donchpos_42_21d_jerk_v077_signal(closeadj):
    base = _f06_donch_pos(closeadj, 42)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_disthi_42_21d_jerk_v078_signal(closeadj):
    base = _f06_dist_high(closeadj, 42)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_distlo_42_21d_jerk_v079_signal(closeadj):
    base = _f06_dist_low(closeadj, 42)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_brkup_42_21d_jerk_v080_signal(closeadj):
    ph = _f06_prior_high(closeadj, 42)
    base = (closeadj / ph.replace(0, np.nan) - 1.0).clip(lower=0)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_brkdn_42_21d_jerk_v081_signal(closeadj):
    pl = _f06_prior_low(closeadj, 42)
    base = (closeadj / pl.replace(0, np.nan) - 1.0).clip(upper=0)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_brkdn_126_21d_jerk_v082_signal(closeadj):
    pl = _f06_prior_low(closeadj, 126)
    base = (closeadj / pl.replace(0, np.nan) - 1.0).clip(upper=0)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_bandwidth_252_42d_jerk_v083_signal(closeadj):
    base = _f06_band_width(closeadj, 252)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_hilogap_252_63d_jerk_v084_signal(closeadj):
    hi = _rmax(closeadj, 252)
    lo = _rmin(closeadj, 252)
    gh = np.log(hi.replace(0, np.nan) / closeadj.replace(0, np.nan))
    gl = np.log(closeadj.replace(0, np.nan) / lo.replace(0, np.nan))
    base = (gl - gh) / (gl + gh).replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_disthi_5_5d_jerk_v085_signal(close):
    base = _f06_dist_high(close, 5)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_distloatr_126_13d_jerk_v086_signal(closeadj, high, low):
    lo = _rmin(closeadj, 126)
    atr = _f06_atr(high, low, 21)
    base = (closeadj - lo) / atr.replace(0, np.nan)
    result = _jerk(base, 13)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_disthiatr_252_42d_jerk_v087_signal(closeadj, high, low):
    hi = _rmax(closeadj, 252)
    atr = _f06_atr(high, low, 63)
    base = (closeadj - hi) / atr.replace(0, np.nan)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_clv_63_21d_jerk_v088_signal(closeadj, high, low):
    clv = (2.0 * closeadj - high - low) / (high - low).replace(0, np.nan)
    base = clv.rolling(63, min_periods=21).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_hldonch_252_21d_jerk_v089_signal(closeadj, high, low):
    hi = _rmax(high, 252)
    lo = _rmin(low, 252)
    base = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_squeeze_63_42d_jerk_v090_signal(closeadj):
    bw = _f06_band_width(closeadj, 63)
    med = bw.rolling(252, min_periods=126).median()
    base = bw / med.replace(0, np.nan) - 1.0
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_squeezedepth_126_21d_jerk_v091_signal(closeadj):
    bw = _f06_band_width(closeadj, 126)
    bwmax = bw.rolling(504, min_periods=252).max()
    base = bw / bwmax.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_upperhug_126_21d_jerk_v092_signal(closeadj):
    p = _f06_donch_pos(closeadj, 126)
    base = (p >= 0.9).astype(float).rolling(126, min_periods=63).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_lowerhug_126_21d_jerk_v093_signal(closeadj):
    p = _f06_donch_pos(closeadj, 126)
    base = (p <= 0.1).astype(float).rolling(126, min_periods=63).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_brkvol_126_21d_jerk_v094_signal(closeadj, volume):
    ph = _f06_prior_high(closeadj, 126)
    head = (closeadj / ph.replace(0, np.nan) - 1.0).clip(lower=0)
    vsurge = volume / _mean(volume, 126).replace(0, np.nan)
    base = head * vsurge
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_brkdnvol_63_21d_jerk_v095_signal(closeadj, volume):
    pl = _f06_prior_low(closeadj, 63)
    depth = (closeadj / pl.replace(0, np.nan) - 1.0).clip(upper=0)
    vsurge = volume / _mean(volume, 63).replace(0, np.nan)
    base = depth * vsurge
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_dvbrk_21_10d_jerk_v096_signal(close, closeadj, volume):
    ph = _f06_prior_high(close, 21)
    head = (close / ph.replace(0, np.nan) - 1.0).clip(lower=0)
    dv = closeadj * volume
    dvz = _z(dv, 63)
    base = head * dvz
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_volconfpos_126_21d_jerk_v097_signal(closeadj, volume):
    pos = _f06_donch_pos(closeadj, 126)
    vtrend = _mean(volume, 63) / _mean(volume, 126).replace(0, np.nan)
    pos_r = pos.rolling(126, min_periods=63).rank(pct=True)
    vol_r = vtrend.rolling(126, min_periods=63).rank(pct=True)
    base = pos_r - vol_r
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_netbreak_126_21d_jerk_v098_signal(closeadj):
    ph = _f06_prior_high(closeadj, 63)
    pl = _f06_prior_low(closeadj, 63)
    up = (closeadj > ph).astype(float)
    dn = (closeadj < pl).astype(float)
    base = (up - dn).rolling(126, min_periods=63).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_newlofreq_21_21d_jerk_v099_signal(close):
    pl = _f06_prior_low(close, 21)
    freq = (close < pl).astype(float).rolling(63, min_periods=21).mean()
    depth = (pl / close.replace(0, np.nan) - 1.0).clip(lower=0).rolling(63, min_periods=21).mean()
    base = freq + 5.0 * depth
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_posskew_126_21d_jerk_v100_signal(closeadj):
    p = _f06_donch_pos(closeadj, 126)
    base = (p - 0.5).rolling(126, min_periods=63).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_posdisp_126_21d_jerk_v101_signal(closeadj):
    p = _f06_donch_pos(closeadj, 126)
    base = p.rolling(126, min_periods=63).std()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_brkupvol_63_21d_jerk_v102_signal(closeadj, volume):
    pos = _f06_donch_pos(closeadj, 63)
    up = closeadj > closeadj.shift(1)
    upvol = volume.where(up, 0.0).rolling(63, min_periods=21).sum()
    dnvol = volume.where(~up, 0.0).rolling(63, min_periods=21).sum()
    ratio = upvol / (upvol + dnvol).replace(0, np.nan)
    base = pos * (ratio - 0.5)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_thrust_126_21d_jerk_v103_signal(closeadj):
    ph = _f06_prior_high(closeadj, 126)
    at_high = (closeadj >= ph).astype(float)
    ret63 = closeadj / closeadj.shift(63).replace(0, np.nan) - 1.0
    base = at_high.rolling(63, min_periods=21).mean() * ret63
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_brktanh_126_21d_jerk_v104_signal(closeadj):
    ph = _f06_prior_high(closeadj, 126)
    head = closeadj / ph.replace(0, np.nan) - 1.0
    base = np.tanh(12.0 * head)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_convex_252_42d_jerk_v105_signal(closeadj):
    p_s = _f06_donch_pos(closeadj, 63)
    p_m = _f06_donch_pos(closeadj, 126)
    p_l = _f06_donch_pos(closeadj, 252)
    base = p_m - 0.5 * (p_s + p_l)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_disthispr_5v63_21d_jerk_v106_signal(close, closeadj):
    s = _f06_dist_high(close, 5)
    l = _f06_dist_high(closeadj, 63)
    base = s - l
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_donchspr_63v252_21d_jerk_v107_signal(closeadj):
    s = _f06_donch_pos(closeadj, 63)
    l = _f06_donch_pos(closeadj, 252)
    base = s - l
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_truepremium_126_21d_jerk_v108_signal(closeadj, high):
    hi_true = _rmax(high, 126)
    hi_close = _rmax(closeadj, 126)
    base = hi_true / hi_close.replace(0, np.nan) - 1.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_truediscount_126_21d_jerk_v109_signal(closeadj, low):
    lo_true = _rmin(low, 126)
    lo_close = _rmin(closeadj, 126)
    base = lo_close / lo_true.replace(0, np.nan) - 1.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_freshlo_252_42d_jerk_v110_signal(closeadj):
    def _dsl(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    dsl = closeadj.rolling(252, min_periods=126).apply(_dsl, raw=True)
    pos = _f06_donch_pos(closeadj, 252)
    base = (1.0 - dsl) * (1.0 - pos)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_squeezedist_126_13d_jerk_v111_signal(closeadj):
    bw = _f06_band_width(closeadj, 126)
    bwmin = bw.rolling(504, min_periods=252).min()
    base = bw / bwmin.replace(0, np.nan) - 1.0
    result = _jerk(base, 13)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_poscentered_126_42d_jerk_v112_signal(closeadj):
    p = _f06_donch_pos(closeadj, 126)
    med = p.rolling(252, min_periods=126).median()
    base = p - med
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_clean_126_21d_jerk_v113_signal(closeadj):
    disp = (closeadj - closeadj.shift(126)).abs()
    path = closeadj.diff().abs().rolling(126, min_periods=63).sum()
    eff = disp / path.replace(0, np.nan)
    pos = _f06_donch_pos(closeadj, 126) - 0.5
    base = eff * np.sign(pos)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_widthtrend_126_21d_jerk_v114_signal(closeadj):
    bw = _f06_band_width(closeadj, 126)
    base = bw / bw.shift(63).replace(0, np.nan) - 1.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_brkhold_126_21d_jerk_v115_signal(closeadj):
    ph = _f06_prior_high(closeadj, 126).shift(63)
    base = (closeadj >= ph).astype(float).rolling(63, min_periods=21).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_brkfail_126_21d_jerk_v116_signal(closeadj):
    p = _f06_donch_pos(closeadj, 126)
    recent_top = p.rolling(42, min_periods=21).max()
    base = recent_top - p
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_donchmom_126_21d_jerk_v117_signal(closeadj):
    p = _f06_donch_pos(closeadj, 126)
    base = p - p.shift(63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_middist_252atr_42d_jerk_v118_signal(closeadj, high, low):
    hi = _rmax(closeadj, 252)
    lo = _rmin(closeadj, 252)
    mid = (hi + lo) / 2.0
    atr = _f06_atr(high, low, 63)
    base = (closeadj - mid) / atr.replace(0, np.nan)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_dshvsdsl_126_21d_jerk_v119_signal(closeadj):
    def _dsh(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    def _dsl(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    dsh = closeadj.rolling(126, min_periods=63).apply(_dsh, raw=True)
    dsl = closeadj.rolling(126, min_periods=63).apply(_dsl, raw=True)
    base = dsl - dsh
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_dshdecay_126_21d_jerk_v120_signal(closeadj):
    def _dsh(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    dsh = closeadj.rolling(126, min_periods=63).apply(_dsh, raw=True)
    base = np.exp(-3.0 * dsh)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_pushstreak_63_21d_jerk_v121_signal(closeadj):
    p = _f06_donch_pos(closeadj, 63)
    up = (p >= 0.75).astype(float)
    grp = (up == 0).cumsum()
    base = up.groupby(grp).cumsum() / 21.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_slidestreak_63_21d_jerk_v122_signal(closeadj):
    p = _f06_donch_pos(closeadj, 63)
    dn = (p <= 0.25).astype(float)
    grp = (dn == 0).cumsum()
    base = dn.groupby(grp).cumsum() / 21.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_contractstreak_21d_jerk_v123_signal(high, low):
    rng = (high - low).rolling(21, min_periods=10).mean()
    ref = (high - low).rolling(63, min_periods=21).mean()
    tight = (rng < ref).astype(float)
    grp = (tight == 0).cumsum()
    base = tight.groupby(grp).cumsum() / 21.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_brkupyoy_252_63d_jerk_v124_signal(closeadj):
    ph = _f06_prior_high(closeadj, 252)
    head = closeadj / ph.replace(0, np.nan) - 1.0
    base = head - head.shift(252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_disthiyoy_252_42d_jerk_v125_signal(closeadj):
    d = _f06_dist_high(closeadj, 252)
    base = d - d.shift(252)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_brkmagsum_63_21d_jerk_v126_signal(closeadj):
    ph = _f06_prior_high(closeadj, 21)
    head = (closeadj / ph.replace(0, np.nan) - 1.0).clip(lower=0)
    base = head.rolling(63, min_periods=21).sum()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_brkdnmagasym_63_21d_jerk_v127_signal(closeadj):
    ph = _f06_prior_high(closeadj, 21)
    pl = _f06_prior_low(closeadj, 21)
    up = (closeadj / ph.replace(0, np.nan) - 1.0).clip(lower=0).rolling(63, min_periods=21).sum()
    dn = (1.0 - closeadj / pl.replace(0, np.nan)).clip(lower=0).rolling(63, min_periods=21).sum()
    base = (up - dn) / (up + dn).replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_topaccel_63_21d_jerk_v128_signal(closeadj):
    p = _f06_donch_pos(closeadj, 63)
    top = (p >= 0.8).astype(float).rolling(21, min_periods=10).mean()
    base = top - top.shift(21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_squeezetrig_21d_jerk_v129_signal(closeadj):
    bw = _f06_band_width(closeadj, 21)
    prior_low = bw.rolling(126, min_periods=63).min().shift(5)
    expand = bw / prior_low.replace(0, np.nan) - 1.0
    pos = _f06_donch_pos(closeadj, 63) - 0.5
    base = expand * np.sign(pos)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_calmbreak_63_21d_jerk_v130_signal(closeadj):
    vol = closeadj.pct_change().rolling(21, min_periods=10).std()
    vol_rank = vol.rolling(252, min_periods=126).rank(pct=True)
    calm = (1.0 - vol_rank)
    ph = _f06_prior_high(closeadj, 63)
    head = (closeadj / ph.replace(0, np.nan) - 1.0).clip(lower=0)
    base = calm * head
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_brkvoladj_63_21d_jerk_v131_signal(closeadj):
    ph = _f06_prior_high(closeadj, 63)
    head = closeadj / ph.replace(0, np.nan) - 1.0
    vol = closeadj.pct_change().rolling(21, min_periods=10).std()
    ratio = head / vol.replace(0, np.nan)
    base = ratio.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_disthirank_spr_21d_jerk_v132_signal(closeadj):
    d63 = _f06_dist_high(closeadj, 63)
    d252 = _f06_dist_high(closeadj, 252)
    base = d63 - d252
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_multiagreeshort_21d_jerk_v133_signal(close, closeadj):
    p1 = _f06_donch_pos(close, 5)
    p2 = _f06_donch_pos(close, 21)
    p3 = _f06_donch_pos(closeadj, 63)
    p4 = _f06_donch_pos(closeadj, 126)
    base = pd.concat([p1, p2, p3, p4], axis=1).mean(axis=1)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_disthidisp_42d_jerk_v134_signal(close, closeadj):
    d1 = _f06_dist_high(close, 21)
    d2 = _f06_dist_high(closeadj, 63)
    d3 = _f06_dist_high(closeadj, 126)
    d4 = _f06_dist_high(closeadj, 252)
    base = pd.concat([d1, d2, d3, d4], axis=1).std(axis=1)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_donchmom_5_5d_jerk_v135_signal(close):
    p = _f06_donch_pos(close, 21)
    base = p - p.shift(5)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_donchapproach_126_13d_jerk_v136_signal(closeadj):
    p = _f06_donch_pos(closeadj, 126)
    base = p - p.shift(63)
    result = _jerk(base, 13)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_disthimom_126_21d_jerk_v137_signal(closeadj):
    d = _f06_dist_high(closeadj, 126)
    base = d - d.shift(21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_distlomom_126_21d_jerk_v138_signal(closeadj):
    d = _f06_dist_low(closeadj, 126)
    base = d - d.shift(21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_donchposema_63_21d_jerk_v139_signal(closeadj):
    p = _f06_donch_pos(closeadj, 63)
    base = p.ewm(span=21, min_periods=10).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_donchdisp_63_21d_jerk_v140_signal(closeadj):
    p = _f06_donch_pos(closeadj, 63)
    base = p - p.ewm(span=42, min_periods=21).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_squeezerelease_63_21d_jerk_v141_signal(closeadj):
    bw = _f06_band_width(closeadj, 21)
    med = bw.rolling(126, min_periods=63).median()
    compr = (med / bw.replace(0, np.nan)).shift(5)
    pos = _f06_donch_pos(closeadj, 21) - 0.5
    base = compr * pos
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_squeezestreak_21d_jerk_v142_signal(closeadj):
    bw = _f06_band_width(closeadj, 21)
    med = bw.rolling(126, min_periods=63).median()
    tight = (bw < med).astype(float)
    grp = (tight == 0).cumsum()
    base = tight.groupby(grp).cumsum() / 21.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_comprpos_signed_13d_jerk_v143_signal(closeadj):
    bw = _f06_band_width(closeadj, 21)
    pos = _f06_donch_pos(closeadj, 63) - 0.5
    base = pos / bw.replace(0, np.nan)
    result = _jerk(base, 13)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_posaccel_252_42d_jerk_v144_signal(closeadj):
    p = _f06_donch_pos(closeadj, 252)
    base = (p - p.shift(63)) - (p.shift(63) - p.shift(126))
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_truedisthi_63_13d_jerk_v145_signal(closeadj, high):
    hi_true = _rmax(high, 63)
    hi_close = _rmax(closeadj, 63)
    base = hi_true / hi_close.replace(0, np.nan) - 1.0
    result = _jerk(base, 13)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_donchposrank_252_42d_jerk_v146_signal(closeadj):
    p = _f06_donch_pos(closeadj, 252)
    base = p.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_brkvolrank_21_21d_jerk_v147_signal(close, volume):
    ph = _f06_prior_high(close, 21)
    head = (close / ph.replace(0, np.nan) - 1.0).clip(lower=0)
    vsurge = volume / _mean(volume, 21).replace(0, np.nan)
    raw = head * vsurge
    base = raw.rolling(126, min_periods=63).rank(pct=True) - 0.5
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_dsh_126_21d_jerk_v148_signal(closeadj):
    def _dsh(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    base = closeadj.rolling(126, min_periods=63).apply(_dsh, raw=True)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_dsl_126_21d_jerk_v149_signal(closeadj):
    def _dsl(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    base = closeadj.rolling(126, min_periods=63).apply(_dsl, raw=True)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06bp_f06_breakout_proximity_failrate_126_21d_jerk_v150_signal(closeadj):
    ph = _f06_prior_high(closeadj, 21)
    is_high = (closeadj > ph)
    fade = (closeadj.shift(-5) < closeadj) & is_high
    fail = fade.astype(float)
    raw = fail.rolling(126, min_periods=63).sum()
    bcnt = is_high.astype(float).rolling(126, min_periods=63).sum()
    base = raw / bcnt.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f06bp_f06_breakout_proximity_donchpos_21_10d_jerk_v001_signal,
    f06bp_f06_breakout_proximity_donchpos_63_21d_jerk_v002_signal,
    f06bp_f06_breakout_proximity_donchpos_126_21d_jerk_v003_signal,
    f06bp_f06_breakout_proximity_donchpos_252_42d_jerk_v004_signal,
    f06bp_f06_breakout_proximity_disthi_21_10d_jerk_v005_signal,
    f06bp_f06_breakout_proximity_disthi_63_21d_jerk_v006_signal,
    f06bp_f06_breakout_proximity_disthi_126_21d_jerk_v007_signal,
    f06bp_f06_breakout_proximity_disthi_252_42d_jerk_v008_signal,
    f06bp_f06_breakout_proximity_distlo_21_10d_jerk_v009_signal,
    f06bp_f06_breakout_proximity_distlo_63_21d_jerk_v010_signal,
    f06bp_f06_breakout_proximity_distlo_126_21d_jerk_v011_signal,
    f06bp_f06_breakout_proximity_distlo_252_42d_jerk_v012_signal,
    f06bp_f06_breakout_proximity_gaptohi_63_13d_jerk_v013_signal,
    f06bp_f06_breakout_proximity_rngexpand_126_21d_jerk_v014_signal,
    f06bp_f06_breakout_proximity_bandwidth_21_10d_jerk_v015_signal,
    f06bp_f06_breakout_proximity_bandwidth_63_21d_jerk_v016_signal,
    f06bp_f06_breakout_proximity_bandwidth_126_21d_jerk_v017_signal,
    f06bp_f06_breakout_proximity_brkup_21_10d_jerk_v018_signal,
    f06bp_f06_breakout_proximity_brkup_63_21d_jerk_v019_signal,
    f06bp_f06_breakout_proximity_brkup_126_21d_jerk_v020_signal,
    f06bp_f06_breakout_proximity_brkdn_21_10d_jerk_v021_signal,
    f06bp_f06_breakout_proximity_brkdn_63_21d_jerk_v022_signal,
    f06bp_f06_breakout_proximity_disthiatr_63_21d_jerk_v023_signal,
    f06bp_f06_breakout_proximity_distloatr_63_21d_jerk_v024_signal,
    f06bp_f06_breakout_proximity_disthiatr_126_21d_jerk_v025_signal,
    f06bp_f06_breakout_proximity_hlrngwidth_21_10d_jerk_v026_signal,
    f06bp_f06_breakout_proximity_hldonch_63_13d_jerk_v027_signal,
    f06bp_f06_breakout_proximity_hldonch_126_13d_jerk_v028_signal,
    f06bp_f06_breakout_proximity_clv_21_10d_jerk_v029_signal,
    f06bp_f06_breakout_proximity_headwidth_126_34d_jerk_v030_signal,
    f06bp_f06_breakout_proximity_headwidth_252_34d_jerk_v031_signal,
    f06bp_f06_breakout_proximity_squeeze_21_21d_jerk_v032_signal,
    f06bp_f06_breakout_proximity_squeezedepth_63_13d_jerk_v033_signal,
    f06bp_f06_breakout_proximity_upperhug_63_21d_jerk_v034_signal,
    f06bp_f06_breakout_proximity_lowerhug_63_21d_jerk_v035_signal,
    f06bp_f06_breakout_proximity_brkvol_21_10d_jerk_v036_signal,
    f06bp_f06_breakout_proximity_brkvol_63_21d_jerk_v037_signal,
    f06bp_f06_breakout_proximity_dvbrk_63_13d_jerk_v038_signal,
    f06bp_f06_breakout_proximity_volconfpos_63_21d_jerk_v039_signal,
    f06bp_f06_breakout_proximity_netbreak_63_21d_jerk_v040_signal,
    f06bp_f06_breakout_proximity_newhifreq_21_21d_jerk_v041_signal,
    f06bp_f06_breakout_proximity_posskew_63_21d_jerk_v042_signal,
    f06bp_f06_breakout_proximity_posdisp_63_21d_jerk_v043_signal,
    f06bp_f06_breakout_proximity_middistatr_63_21d_jerk_v044_signal,
    f06bp_f06_breakout_proximity_brkupvol_21_10d_jerk_v045_signal,
    f06bp_f06_breakout_proximity_thrust_63_21d_jerk_v046_signal,
    f06bp_f06_breakout_proximity_brktanh_63_21d_jerk_v047_signal,
    f06bp_f06_breakout_proximity_convex_63_21d_jerk_v048_signal,
    f06bp_f06_breakout_proximity_disthispr_21v126_21d_jerk_v049_signal,
    f06bp_f06_breakout_proximity_donchspr_21v252_21d_jerk_v050_signal,
    f06bp_f06_breakout_proximity_truepremium_63_21d_jerk_v051_signal,
    f06bp_f06_breakout_proximity_freshhi_126_21d_jerk_v052_signal,
    f06bp_f06_breakout_proximity_comprpos_70_21d_jerk_v053_signal,
    f06bp_f06_breakout_proximity_squeezedist_63_34d_jerk_v054_signal,
    f06bp_f06_breakout_proximity_poscentered_252_34d_jerk_v055_signal,
    f06bp_f06_breakout_proximity_topdvshare_63_21d_jerk_v056_signal,
    f06bp_f06_breakout_proximity_clean_63_21d_jerk_v057_signal,
    f06bp_f06_breakout_proximity_brkdnvol_21_10d_jerk_v058_signal,
    f06bp_f06_breakout_proximity_multiagree_42d_jerk_v059_signal,
    f06bp_f06_breakout_proximity_multidisp_42d_jerk_v060_signal,
    f06bp_f06_breakout_proximity_widthtrend_63_21d_jerk_v061_signal,
    f06bp_f06_breakout_proximity_brkhold_63_21d_jerk_v062_signal,
    f06bp_f06_breakout_proximity_brkfail_63_21d_jerk_v063_signal,
    f06bp_f06_breakout_proximity_disthi_504_63d_jerk_v064_signal,
    f06bp_f06_breakout_proximity_donchpos_504_63d_jerk_v065_signal,
    f06bp_f06_breakout_proximity_volathigh_63_21d_jerk_v066_signal,
    f06bp_f06_breakout_proximity_distrlo_63_21d_jerk_v067_signal,
    f06bp_f06_breakout_proximity_middist_126atr_21d_jerk_v068_signal,
    f06bp_f06_breakout_proximity_postlow_126_21d_jerk_v069_signal,
    f06bp_f06_breakout_proximity_posture_126_13d_jerk_v070_signal,
    f06bp_f06_breakout_proximity_donchmom_63_21d_jerk_v071_signal,
    f06bp_f06_breakout_proximity_squeezehead_21_21d_jerk_v072_signal,
    f06bp_f06_breakout_proximity_brkup_252_42d_jerk_v073_signal,
    f06bp_f06_breakout_proximity_dshvsdsl_63_21d_jerk_v074_signal,
    f06bp_f06_breakout_proximity_truedistloatr_126_21d_jerk_v075_signal,
    f06bp_f06_breakout_proximity_donchpos_5_5d_jerk_v076_signal,
    f06bp_f06_breakout_proximity_donchpos_42_21d_jerk_v077_signal,
    f06bp_f06_breakout_proximity_disthi_42_21d_jerk_v078_signal,
    f06bp_f06_breakout_proximity_distlo_42_21d_jerk_v079_signal,
    f06bp_f06_breakout_proximity_brkup_42_21d_jerk_v080_signal,
    f06bp_f06_breakout_proximity_brkdn_42_21d_jerk_v081_signal,
    f06bp_f06_breakout_proximity_brkdn_126_21d_jerk_v082_signal,
    f06bp_f06_breakout_proximity_bandwidth_252_42d_jerk_v083_signal,
    f06bp_f06_breakout_proximity_hilogap_252_63d_jerk_v084_signal,
    f06bp_f06_breakout_proximity_disthi_5_5d_jerk_v085_signal,
    f06bp_f06_breakout_proximity_distloatr_126_13d_jerk_v086_signal,
    f06bp_f06_breakout_proximity_disthiatr_252_42d_jerk_v087_signal,
    f06bp_f06_breakout_proximity_clv_63_21d_jerk_v088_signal,
    f06bp_f06_breakout_proximity_hldonch_252_21d_jerk_v089_signal,
    f06bp_f06_breakout_proximity_squeeze_63_42d_jerk_v090_signal,
    f06bp_f06_breakout_proximity_squeezedepth_126_21d_jerk_v091_signal,
    f06bp_f06_breakout_proximity_upperhug_126_21d_jerk_v092_signal,
    f06bp_f06_breakout_proximity_lowerhug_126_21d_jerk_v093_signal,
    f06bp_f06_breakout_proximity_brkvol_126_21d_jerk_v094_signal,
    f06bp_f06_breakout_proximity_brkdnvol_63_21d_jerk_v095_signal,
    f06bp_f06_breakout_proximity_dvbrk_21_10d_jerk_v096_signal,
    f06bp_f06_breakout_proximity_volconfpos_126_21d_jerk_v097_signal,
    f06bp_f06_breakout_proximity_netbreak_126_21d_jerk_v098_signal,
    f06bp_f06_breakout_proximity_newlofreq_21_21d_jerk_v099_signal,
    f06bp_f06_breakout_proximity_posskew_126_21d_jerk_v100_signal,
    f06bp_f06_breakout_proximity_posdisp_126_21d_jerk_v101_signal,
    f06bp_f06_breakout_proximity_brkupvol_63_21d_jerk_v102_signal,
    f06bp_f06_breakout_proximity_thrust_126_21d_jerk_v103_signal,
    f06bp_f06_breakout_proximity_brktanh_126_21d_jerk_v104_signal,
    f06bp_f06_breakout_proximity_convex_252_42d_jerk_v105_signal,
    f06bp_f06_breakout_proximity_disthispr_5v63_21d_jerk_v106_signal,
    f06bp_f06_breakout_proximity_donchspr_63v252_21d_jerk_v107_signal,
    f06bp_f06_breakout_proximity_truepremium_126_21d_jerk_v108_signal,
    f06bp_f06_breakout_proximity_truediscount_126_21d_jerk_v109_signal,
    f06bp_f06_breakout_proximity_freshlo_252_42d_jerk_v110_signal,
    f06bp_f06_breakout_proximity_squeezedist_126_13d_jerk_v111_signal,
    f06bp_f06_breakout_proximity_poscentered_126_42d_jerk_v112_signal,
    f06bp_f06_breakout_proximity_clean_126_21d_jerk_v113_signal,
    f06bp_f06_breakout_proximity_widthtrend_126_21d_jerk_v114_signal,
    f06bp_f06_breakout_proximity_brkhold_126_21d_jerk_v115_signal,
    f06bp_f06_breakout_proximity_brkfail_126_21d_jerk_v116_signal,
    f06bp_f06_breakout_proximity_donchmom_126_21d_jerk_v117_signal,
    f06bp_f06_breakout_proximity_middist_252atr_42d_jerk_v118_signal,
    f06bp_f06_breakout_proximity_dshvsdsl_126_21d_jerk_v119_signal,
    f06bp_f06_breakout_proximity_dshdecay_126_21d_jerk_v120_signal,
    f06bp_f06_breakout_proximity_pushstreak_63_21d_jerk_v121_signal,
    f06bp_f06_breakout_proximity_slidestreak_63_21d_jerk_v122_signal,
    f06bp_f06_breakout_proximity_contractstreak_21d_jerk_v123_signal,
    f06bp_f06_breakout_proximity_brkupyoy_252_63d_jerk_v124_signal,
    f06bp_f06_breakout_proximity_disthiyoy_252_42d_jerk_v125_signal,
    f06bp_f06_breakout_proximity_brkmagsum_63_21d_jerk_v126_signal,
    f06bp_f06_breakout_proximity_brkdnmagasym_63_21d_jerk_v127_signal,
    f06bp_f06_breakout_proximity_topaccel_63_21d_jerk_v128_signal,
    f06bp_f06_breakout_proximity_squeezetrig_21d_jerk_v129_signal,
    f06bp_f06_breakout_proximity_calmbreak_63_21d_jerk_v130_signal,
    f06bp_f06_breakout_proximity_brkvoladj_63_21d_jerk_v131_signal,
    f06bp_f06_breakout_proximity_disthirank_spr_21d_jerk_v132_signal,
    f06bp_f06_breakout_proximity_multiagreeshort_21d_jerk_v133_signal,
    f06bp_f06_breakout_proximity_disthidisp_42d_jerk_v134_signal,
    f06bp_f06_breakout_proximity_donchmom_5_5d_jerk_v135_signal,
    f06bp_f06_breakout_proximity_donchapproach_126_13d_jerk_v136_signal,
    f06bp_f06_breakout_proximity_disthimom_126_21d_jerk_v137_signal,
    f06bp_f06_breakout_proximity_distlomom_126_21d_jerk_v138_signal,
    f06bp_f06_breakout_proximity_donchposema_63_21d_jerk_v139_signal,
    f06bp_f06_breakout_proximity_donchdisp_63_21d_jerk_v140_signal,
    f06bp_f06_breakout_proximity_squeezerelease_63_21d_jerk_v141_signal,
    f06bp_f06_breakout_proximity_squeezestreak_21d_jerk_v142_signal,
    f06bp_f06_breakout_proximity_comprpos_signed_13d_jerk_v143_signal,
    f06bp_f06_breakout_proximity_posaccel_252_42d_jerk_v144_signal,
    f06bp_f06_breakout_proximity_truedisthi_63_13d_jerk_v145_signal,
    f06bp_f06_breakout_proximity_donchposrank_252_42d_jerk_v146_signal,
    f06bp_f06_breakout_proximity_brkvolrank_21_21d_jerk_v147_signal,
    f06bp_f06_breakout_proximity_dsh_126_21d_jerk_v148_signal,
    f06bp_f06_breakout_proximity_dsl_126_21d_jerk_v149_signal,
    f06bp_f06_breakout_proximity_failrate_126_21d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F06_BREAKOUT_PROXIMITY_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
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

    ALLOW = {"open", "high", "low", "close", "closeadj", "volume"}

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

    print("OK f06_breakout_proximity_3rd_derivatives_001_150_claude.py: %d features pass" % n_features)
