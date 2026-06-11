import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
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


def _ema(s, span):
    return s.ewm(span=span, min_periods=max(2, span // 2)).mean()


# ===== folder domain primitives (hype / blowoff / overextension) =====
def _f05hb_atr(high, low, closeadj, w):
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low),
                    (high - pc).abs(),
                    (low - pc).abs()], axis=1).max(axis=1)
    return tr.rolling(w, min_periods=max(2, w // 2)).mean()


def _f05hb_stretch_atr(high, low, closeadj, maw, atrw):
    ma = closeadj.rolling(maw, min_periods=max(2, maw // 2)).mean()
    atr = _f05hb_atr(high, low, closeadj, atrw)
    return (closeadj - ma) / atr.replace(0, np.nan)


def _f05hb_dist_ma(closeadj, maw):
    ma = closeadj.rolling(maw, min_periods=max(2, maw // 2)).mean()
    return closeadj / ma.replace(0, np.nan) - 1.0


def _f05hb_run_slope(closeadj, w):
    return np.log(closeadj.replace(0, np.nan) / closeadj.shift(w).replace(0, np.nan)) / float(w)


def _f05hb_volspike(volume, w):
    return volume / volume.rolling(w, min_periods=max(2, w // 2)).mean().replace(0, np.nan)


def _f05hb_rsi(closeadj, w):
    d = closeadj.diff()
    up = d.clip(lower=0.0)
    dn = (-d).clip(lower=0.0)
    au = up.rolling(w, min_periods=max(2, w // 2)).mean()
    ad = dn.rolling(w, min_periods=max(2, w // 2)).mean()
    rs = au / ad.replace(0, np.nan)
    return 100.0 - 100.0 / (1.0 + rs)

def f05hb_f05_hype_blowoff_stretch5_5d_jerk_v001_signal(closeadj, high, low):
    ma = closeadj.rolling(5, min_periods=3).mean()
    atr = _f05hb_atr(high, low, closeadj, 14)
    bse = (closeadj - ma) / atr.replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(5) + bse.shift(10)) / float(5 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_stretch5_8d_jerk_v002_signal(closeadj, high, low):
    ma = closeadj.rolling(5, min_periods=3).mean()
    atr = _f05hb_atr(high, low, closeadj, 14)
    bse = (closeadj - ma) / atr.replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(8) + bse.shift(16)) / float(8 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_stretch5_12d_jerk_v003_signal(closeadj, high, low):
    ma = closeadj.rolling(5, min_periods=3).mean()
    atr = _f05hb_atr(high, low, closeadj, 14)
    bse = (closeadj - ma) / atr.replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(12) + bse.shift(24)) / float(12 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_stretch10_5d_jerk_v004_signal(closeadj, high, low):
    ma = closeadj.rolling(10, min_periods=5).mean()
    atr = _f05hb_atr(high, low, closeadj, 14)
    bse = (closeadj - ma) / atr.replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(5) + bse.shift(10)) / float(5 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_stretch10_8d_jerk_v005_signal(closeadj, high, low):
    ma = closeadj.rolling(10, min_periods=5).mean()
    atr = _f05hb_atr(high, low, closeadj, 14)
    bse = (closeadj - ma) / atr.replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(8) + bse.shift(16)) / float(8 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_stretch10_12d_jerk_v006_signal(closeadj, high, low):
    ma = closeadj.rolling(10, min_periods=5).mean()
    atr = _f05hb_atr(high, low, closeadj, 14)
    bse = (closeadj - ma) / atr.replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(12) + bse.shift(24)) / float(12 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_stretch21_10d_jerk_v007_signal(closeadj, high, low):
    ma = closeadj.rolling(21, min_periods=10).mean()
    atr = _f05hb_atr(high, low, closeadj, 21)
    bse = (closeadj - ma) / atr.replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(10) + bse.shift(20)) / float(10 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_stretch21_16d_jerk_v008_signal(closeadj, high, low):
    ma = closeadj.rolling(21, min_periods=10).mean()
    atr = _f05hb_atr(high, low, closeadj, 21)
    bse = (closeadj - ma) / atr.replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(16) + bse.shift(32)) / float(16 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_stretch21_24d_jerk_v009_signal(closeadj, high, low):
    ma = closeadj.rolling(21, min_periods=10).mean()
    atr = _f05hb_atr(high, low, closeadj, 21)
    bse = (closeadj - ma) / atr.replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(24) + bse.shift(48)) / float(24 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_distma21_5d_jerk_v010_signal(closeadj):
    ma = closeadj.rolling(21, min_periods=10).mean()
    bse = closeadj / ma.replace(0, np.nan) - 1.0
    d2 = (bse - 2.0 * bse.shift(5) + bse.shift(10)) / float(5 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_distma21_8d_jerk_v011_signal(closeadj):
    ma = closeadj.rolling(21, min_periods=10).mean()
    bse = closeadj / ma.replace(0, np.nan) - 1.0
    d2 = (bse - 2.0 * bse.shift(8) + bse.shift(16)) / float(8 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_distma21_12d_jerk_v012_signal(closeadj):
    ma = closeadj.rolling(21, min_periods=10).mean()
    bse = closeadj / ma.replace(0, np.nan) - 1.0
    d2 = (bse - 2.0 * bse.shift(12) + bse.shift(24)) / float(12 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_distma63_10d_jerk_v013_signal(closeadj):
    ma = closeadj.rolling(63, min_periods=21).mean()
    bse = closeadj / ma.replace(0, np.nan) - 1.0
    d2 = (bse - 2.0 * bse.shift(10) + bse.shift(20)) / float(10 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_distma63_16d_jerk_v014_signal(closeadj):
    ma = closeadj.rolling(63, min_periods=21).mean()
    bse = closeadj / ma.replace(0, np.nan) - 1.0
    d2 = (bse - 2.0 * bse.shift(16) + bse.shift(32)) / float(16 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_distma63_24d_jerk_v015_signal(closeadj):
    ma = closeadj.rolling(63, min_periods=21).mean()
    bse = closeadj / ma.replace(0, np.nan) - 1.0
    d2 = (bse - 2.0 * bse.shift(24) + bse.shift(48)) / float(24 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_bandwidth_5d_jerk_v016_signal(closeadj):
    ma = closeadj.rolling(21, min_periods=10).mean()
    sd = closeadj.rolling(21, min_periods=10).std()
    bse = (4.0 * sd) / ma.replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(5) + bse.shift(10)) / float(5 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_bandwidth_8d_jerk_v017_signal(closeadj):
    ma = closeadj.rolling(21, min_periods=10).mean()
    sd = closeadj.rolling(21, min_periods=10).std()
    bse = (4.0 * sd) / ma.replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(8) + bse.shift(16)) / float(8 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_bandwidth_12d_jerk_v018_signal(closeadj):
    ma = closeadj.rolling(21, min_periods=10).mean()
    sd = closeadj.rolling(21, min_periods=10).std()
    bse = (4.0 * sd) / ma.replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(12) + bse.shift(24)) / float(12 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_effratio_5d_jerk_v019_signal(closeadj):
    net = (closeadj - closeadj.shift(10)).abs()
    path = closeadj.diff().abs().rolling(10, min_periods=5).sum()
    bse = net / path.replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(5) + bse.shift(10)) / float(5 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_effratio_8d_jerk_v020_signal(closeadj):
    net = (closeadj - closeadj.shift(10)).abs()
    path = closeadj.diff().abs().rolling(10, min_periods=5).sum()
    bse = net / path.replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(8) + bse.shift(16)) / float(8 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_effratio_12d_jerk_v021_signal(closeadj):
    net = (closeadj - closeadj.shift(10)).abs()
    path = closeadj.diff().abs().rolling(10, min_periods=5).sum()
    bse = net / path.replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(12) + bse.shift(24)) / float(12 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_runslope5_5d_jerk_v022_signal(closeadj):
    bse = _f05hb_run_slope(closeadj, 5)
    d2 = (bse - 2.0 * bse.shift(5) + bse.shift(10)) / float(5 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_runslope5_8d_jerk_v023_signal(closeadj):
    bse = _f05hb_run_slope(closeadj, 5)
    d2 = (bse - 2.0 * bse.shift(8) + bse.shift(16)) / float(8 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_runslope5_12d_jerk_v024_signal(closeadj):
    bse = _f05hb_run_slope(closeadj, 5)
    d2 = (bse - 2.0 * bse.shift(12) + bse.shift(24)) / float(12 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_runslope10_5d_jerk_v025_signal(closeadj):
    bse = _f05hb_run_slope(closeadj, 10)
    d2 = (bse - 2.0 * bse.shift(5) + bse.shift(10)) / float(5 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_runslope10_8d_jerk_v026_signal(closeadj):
    bse = _f05hb_run_slope(closeadj, 10)
    d2 = (bse - 2.0 * bse.shift(8) + bse.shift(16)) / float(8 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_runslope10_12d_jerk_v027_signal(closeadj):
    bse = _f05hb_run_slope(closeadj, 10)
    d2 = (bse - 2.0 * bse.shift(12) + bse.shift(24)) / float(12 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_runslope21_10d_jerk_v028_signal(closeadj):
    bse = _f05hb_run_slope(closeadj, 21)
    d2 = (bse - 2.0 * bse.shift(10) + bse.shift(20)) / float(10 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_runslope21_16d_jerk_v029_signal(closeadj):
    bse = _f05hb_run_slope(closeadj, 21)
    d2 = (bse - 2.0 * bse.shift(16) + bse.shift(32)) / float(16 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_runslope21_24d_jerk_v030_signal(closeadj):
    bse = _f05hb_run_slope(closeadj, 21)
    d2 = (bse - 2.0 * bse.shift(24) + bse.shift(48)) / float(24 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_rsi14_5d_jerk_v031_signal(closeadj):
    bse = _f05hb_rsi(closeadj, 14) - 50.0
    d2 = (bse - 2.0 * bse.shift(5) + bse.shift(10)) / float(5 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_rsi14_8d_jerk_v032_signal(closeadj):
    bse = _f05hb_rsi(closeadj, 14) - 50.0
    d2 = (bse - 2.0 * bse.shift(8) + bse.shift(16)) / float(8 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_rsi14_12d_jerk_v033_signal(closeadj):
    bse = _f05hb_rsi(closeadj, 14) - 50.0
    d2 = (bse - 2.0 * bse.shift(12) + bse.shift(24)) / float(12 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_rsi7_3d_jerk_v034_signal(closeadj):
    bse = _f05hb_rsi(closeadj, 7) - 50.0
    d2 = (bse - 2.0 * bse.shift(3) + bse.shift(6)) / float(3 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_rsi7_5d_jerk_v035_signal(closeadj):
    bse = _f05hb_rsi(closeadj, 7) - 50.0
    d2 = (bse - 2.0 * bse.shift(5) + bse.shift(10)) / float(5 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_rsi7_7d_jerk_v036_signal(closeadj):
    bse = _f05hb_rsi(closeadj, 7) - 50.0
    d2 = (bse - 2.0 * bse.shift(7) + bse.shift(14)) / float(7 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_tailasym_10d_jerk_v037_signal(closeadj):
    r = closeadj.pct_change()
    mu = r.rolling(21, min_periods=10).max()
    md = (-r).rolling(21, min_periods=10).max()
    bse = (mu - md) / (mu + md).replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(10) + bse.shift(20)) / float(10 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_tailasym_16d_jerk_v038_signal(closeadj):
    r = closeadj.pct_change()
    mu = r.rolling(21, min_periods=10).max()
    md = (-r).rolling(21, min_periods=10).max()
    bse = (mu - md) / (mu + md).replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(16) + bse.shift(32)) / float(16 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_tailasym_24d_jerk_v039_signal(closeadj):
    r = closeadj.pct_change()
    mu = r.rolling(21, min_periods=10).max()
    md = (-r).rolling(21, min_periods=10).max()
    bse = (mu - md) / (mu + md).replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(24) + bse.shift(48)) / float(24 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_volspike21_5d_jerk_v040_signal(volume):
    bse = _f05hb_volspike(volume, 21)
    d2 = (bse - 2.0 * bse.shift(5) + bse.shift(10)) / float(5 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_volspike21_8d_jerk_v041_signal(volume):
    bse = _f05hb_volspike(volume, 21)
    d2 = (bse - 2.0 * bse.shift(8) + bse.shift(16)) / float(8 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_volspike21_12d_jerk_v042_signal(volume):
    bse = _f05hb_volspike(volume, 21)
    d2 = (bse - 2.0 * bse.shift(12) + bse.shift(24)) / float(12 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_volspike63_10d_jerk_v043_signal(volume):
    bse = _f05hb_volspike(volume, 63)
    d2 = (bse - 2.0 * bse.shift(10) + bse.shift(20)) / float(10 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_volspike63_16d_jerk_v044_signal(volume):
    bse = _f05hb_volspike(volume, 63)
    d2 = (bse - 2.0 * bse.shift(16) + bse.shift(32)) / float(16 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_volspike63_24d_jerk_v045_signal(volume):
    bse = _f05hb_volspike(volume, 63)
    d2 = (bse - 2.0 * bse.shift(24) + bse.shift(48)) / float(24 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_volz63_5d_jerk_v046_signal(volume):
    bse = _z(np.log(volume.replace(0, np.nan)), 63)
    d2 = (bse - 2.0 * bse.shift(5) + bse.shift(10)) / float(5 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_volz63_8d_jerk_v047_signal(volume):
    bse = _z(np.log(volume.replace(0, np.nan)), 63)
    d2 = (bse - 2.0 * bse.shift(8) + bse.shift(16)) / float(8 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_volz63_12d_jerk_v048_signal(volume):
    bse = _z(np.log(volume.replace(0, np.nan)), 63)
    d2 = (bse - 2.0 * bse.shift(12) + bse.shift(24)) / float(12 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_crowdbuild_5d_jerk_v049_signal(volume):
    short = volume.rolling(5, min_periods=3).mean()
    long = volume.rolling(63, min_periods=21).mean()
    bse = short / long.replace(0, np.nan) - 1.0
    d2 = (bse - 2.0 * bse.shift(5) + bse.shift(10)) / float(5 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_crowdbuild_8d_jerk_v050_signal(volume):
    short = volume.rolling(5, min_periods=3).mean()
    long = volume.rolling(63, min_periods=21).mean()
    bse = short / long.replace(0, np.nan) - 1.0
    d2 = (bse - 2.0 * bse.shift(8) + bse.shift(16)) / float(8 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_crowdbuild_12d_jerk_v051_signal(volume):
    short = volume.rolling(5, min_periods=3).mean()
    long = volume.rolling(63, min_periods=21).mean()
    bse = short / long.replace(0, np.nan) - 1.0
    d2 = (bse - 2.0 * bse.shift(12) + bse.shift(24)) / float(12 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_stoch21_5d_jerk_v052_signal(closeadj, high, low):
    hh = high.rolling(21, min_periods=10).max()
    ll = low.rolling(21, min_periods=10).min()
    bse = (closeadj - ll) / (hh - ll).replace(0, np.nan) - 0.5
    d2 = (bse - 2.0 * bse.shift(5) + bse.shift(10)) / float(5 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_stoch21_8d_jerk_v053_signal(closeadj, high, low):
    hh = high.rolling(21, min_periods=10).max()
    ll = low.rolling(21, min_periods=10).min()
    bse = (closeadj - ll) / (hh - ll).replace(0, np.nan) - 0.5
    d2 = (bse - 2.0 * bse.shift(8) + bse.shift(16)) / float(8 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_stoch21_12d_jerk_v054_signal(closeadj, high, low):
    hh = high.rolling(21, min_periods=10).max()
    ll = low.rolling(21, min_periods=10).min()
    bse = (closeadj - ll) / (hh - ll).replace(0, np.nan) - 0.5
    d2 = (bse - 2.0 * bse.shift(12) + bse.shift(24)) / float(12 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_willr10_5d_jerk_v055_signal(closeadj, high, low):
    hh = high.rolling(10, min_periods=5).max()
    ll = low.rolling(10, min_periods=5).min()
    bse = (hh - closeadj) / (hh - ll).replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(5) + bse.shift(10)) / float(5 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_willr10_8d_jerk_v056_signal(closeadj, high, low):
    hh = high.rolling(10, min_periods=5).max()
    ll = low.rolling(10, min_periods=5).min()
    bse = (hh - closeadj) / (hh - ll).replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(8) + bse.shift(16)) / float(8 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_willr10_12d_jerk_v057_signal(closeadj, high, low):
    hh = high.rolling(10, min_periods=5).max()
    ll = low.rolling(10, min_periods=5).min()
    bse = (hh - closeadj) / (hh - ll).replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(12) + bse.shift(24)) / float(12 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_pctb21_5d_jerk_v058_signal(closeadj):
    ma = closeadj.rolling(21, min_periods=10).mean()
    sd = closeadj.rolling(21, min_periods=10).std()
    bse = (closeadj - ma) / (2.0 * sd).replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(5) + bse.shift(10)) / float(5 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_pctb21_8d_jerk_v059_signal(closeadj):
    ma = closeadj.rolling(21, min_periods=10).mean()
    sd = closeadj.rolling(21, min_periods=10).std()
    bse = (closeadj - ma) / (2.0 * sd).replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(8) + bse.shift(16)) / float(8 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_pctb21_12d_jerk_v060_signal(closeadj):
    ma = closeadj.rolling(21, min_periods=10).mean()
    sd = closeadj.rolling(21, min_periods=10).std()
    bse = (closeadj - ma) / (2.0 * sd).replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(12) + bse.shift(24)) / float(12 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_lowgapatr_5d_jerk_v061_signal(closeadj, high, low):
    ll = low.rolling(21, min_periods=10).min()
    atr = _f05hb_atr(high, low, closeadj, 21)
    bse = (closeadj - ll) / atr.replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(5) + bse.shift(10)) / float(5 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_lowgapatr_8d_jerk_v062_signal(closeadj, high, low):
    ll = low.rolling(21, min_periods=10).min()
    atr = _f05hb_atr(high, low, closeadj, 21)
    bse = (closeadj - ll) / atr.replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(8) + bse.shift(16)) / float(8 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_lowgapatr_12d_jerk_v063_signal(closeadj, high, low):
    ll = low.rolling(21, min_periods=10).min()
    atr = _f05hb_atr(high, low, closeadj, 21)
    bse = (closeadj - ll) / atr.replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(12) + bse.shift(24)) / float(12 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_cci_5d_jerk_v064_signal(closeadj, high, low):
    tp = (high + low + closeadj) / 3.0
    ma = tp.rolling(21, min_periods=10).mean()
    md = (tp - ma).abs().rolling(21, min_periods=10).mean()
    bse = (tp - ma) / (0.015 * md).replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(5) + bse.shift(10)) / float(5 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_cci_8d_jerk_v065_signal(closeadj, high, low):
    tp = (high + low + closeadj) / 3.0
    ma = tp.rolling(21, min_periods=10).mean()
    md = (tp - ma).abs().rolling(21, min_periods=10).mean()
    bse = (tp - ma) / (0.015 * md).replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(8) + bse.shift(16)) / float(8 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_cci_12d_jerk_v066_signal(closeadj, high, low):
    tp = (high + low + closeadj) / 3.0
    ma = tp.rolling(21, min_periods=10).mean()
    md = (tp - ma).abs().rolling(21, min_periods=10).mean()
    bse = (tp - ma) / (0.015 * md).replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(12) + bse.shift(24)) / float(12 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_atrratio_5d_jerk_v067_signal(closeadj, high, low):
    a5 = _f05hb_atr(high, low, closeadj, 5)
    a21 = _f05hb_atr(high, low, closeadj, 21)
    bse = a5 / a21.replace(0, np.nan) - 1.0
    d2 = (bse - 2.0 * bse.shift(5) + bse.shift(10)) / float(5 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_atrratio_8d_jerk_v068_signal(closeadj, high, low):
    a5 = _f05hb_atr(high, low, closeadj, 5)
    a21 = _f05hb_atr(high, low, closeadj, 21)
    bse = a5 / a21.replace(0, np.nan) - 1.0
    d2 = (bse - 2.0 * bse.shift(8) + bse.shift(16)) / float(8 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_atrratio_12d_jerk_v069_signal(closeadj, high, low):
    a5 = _f05hb_atr(high, low, closeadj, 5)
    a21 = _f05hb_atr(high, low, closeadj, 21)
    bse = a5 / a21.replace(0, np.nan) - 1.0
    d2 = (bse - 2.0 * bse.shift(12) + bse.shift(24)) / float(12 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_rangez_5d_jerk_v070_signal(closeadj, high, low):
    rng = (high - low) / closeadj.replace(0, np.nan)
    bse = _z(rng, 63)
    d2 = (bse - 2.0 * bse.shift(5) + bse.shift(10)) / float(5 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_rangez_8d_jerk_v071_signal(closeadj, high, low):
    rng = (high - low) / closeadj.replace(0, np.nan)
    bse = _z(rng, 63)
    d2 = (bse - 2.0 * bse.shift(8) + bse.shift(16)) / float(8 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_rangez_12d_jerk_v072_signal(closeadj, high, low):
    rng = (high - low) / closeadj.replace(0, np.nan)
    bse = _z(rng, 63)
    d2 = (bse - 2.0 * bse.shift(12) + bse.shift(24)) / float(12 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_rvol21_5d_jerk_v073_signal(closeadj):
    r = closeadj.pct_change()
    bse = r.rolling(21, min_periods=10).std()
    d2 = (bse - 2.0 * bse.shift(5) + bse.shift(10)) / float(5 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_rvol21_8d_jerk_v074_signal(closeadj):
    r = closeadj.pct_change()
    bse = r.rolling(21, min_periods=10).std()
    d2 = (bse - 2.0 * bse.shift(8) + bse.shift(16)) / float(8 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_rvol21_12d_jerk_v075_signal(closeadj):
    r = closeadj.pct_change()
    bse = r.rolling(21, min_periods=10).std()
    d2 = (bse - 2.0 * bse.shift(12) + bse.shift(24)) / float(12 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_mafanout_5d_jerk_v076_signal(closeadj):
    d21 = _f05hb_dist_ma(closeadj, 21)
    d63 = _f05hb_dist_ma(closeadj, 63)
    bse = d21 - d63
    d2 = (bse - 2.0 * bse.shift(5) + bse.shift(10)) / float(5 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_mafanout_8d_jerk_v077_signal(closeadj):
    d21 = _f05hb_dist_ma(closeadj, 21)
    d63 = _f05hb_dist_ma(closeadj, 63)
    bse = d21 - d63
    d2 = (bse - 2.0 * bse.shift(8) + bse.shift(16)) / float(8 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_mafanout_12d_jerk_v078_signal(closeadj):
    d21 = _f05hb_dist_ma(closeadj, 21)
    d63 = _f05hb_dist_ma(closeadj, 63)
    bse = d21 - d63
    d2 = (bse - 2.0 * bse.shift(12) + bse.shift(24)) / float(12 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_moveconc_5d_jerk_v079_signal(closeadj):
    g10 = np.log(closeadj.replace(0, np.nan) / closeadj.shift(10).replace(0, np.nan))
    g63 = np.log(closeadj.replace(0, np.nan) / closeadj.shift(63).replace(0, np.nan))
    bse = g10 / (g63.abs() + 0.05)
    d2 = (bse - 2.0 * bse.shift(5) + bse.shift(10)) / float(5 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_moveconc_8d_jerk_v080_signal(closeadj):
    g10 = np.log(closeadj.replace(0, np.nan) / closeadj.shift(10).replace(0, np.nan))
    g63 = np.log(closeadj.replace(0, np.nan) / closeadj.shift(63).replace(0, np.nan))
    bse = g10 / (g63.abs() + 0.05)
    d2 = (bse - 2.0 * bse.shift(8) + bse.shift(16)) / float(8 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_moveconc_12d_jerk_v081_signal(closeadj):
    g10 = np.log(closeadj.replace(0, np.nan) / closeadj.shift(10).replace(0, np.nan))
    g63 = np.log(closeadj.replace(0, np.nan) / closeadj.shift(63).replace(0, np.nan))
    bse = g10 / (g63.abs() + 0.05)
    d2 = (bse - 2.0 * bse.shift(12) + bse.shift(24)) / float(12 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_volaccel_5d_jerk_v082_signal(volume):
    av = volume.rolling(5, min_periods=3).mean()
    bse = av / av.shift(5).replace(0, np.nan) - 1.0
    d2 = (bse - 2.0 * bse.shift(5) + bse.shift(10)) / float(5 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_volaccel_8d_jerk_v083_signal(volume):
    av = volume.rolling(5, min_periods=3).mean()
    bse = av / av.shift(5).replace(0, np.nan) - 1.0
    d2 = (bse - 2.0 * bse.shift(8) + bse.shift(16)) / float(8 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_volaccel_12d_jerk_v084_signal(volume):
    av = volume.rolling(5, min_periods=3).mean()
    bse = av / av.shift(5).replace(0, np.nan) - 1.0
    d2 = (bse - 2.0 * bse.shift(12) + bse.shift(24)) / float(12 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_revfromhi_5d_jerk_v085_signal(closeadj):
    hi = closeadj.rolling(21, min_periods=10).max()
    bse = closeadj / hi.replace(0, np.nan) - 1.0
    d2 = (bse - 2.0 * bse.shift(5) + bse.shift(10)) / float(5 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_revfromhi_8d_jerk_v086_signal(closeadj):
    hi = closeadj.rolling(21, min_periods=10).max()
    bse = closeadj / hi.replace(0, np.nan) - 1.0
    d2 = (bse - 2.0 * bse.shift(8) + bse.shift(16)) / float(8 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_revfromhi_12d_jerk_v087_signal(closeadj):
    hi = closeadj.rolling(21, min_periods=10).max()
    bse = closeadj / hi.replace(0, np.nan) - 1.0
    d2 = (bse - 2.0 * bse.shift(12) + bse.shift(24)) / float(12 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_upshare_5d_jerk_v088_signal(closeadj):
    r = closeadj.pct_change()
    uv = (r.clip(lower=0) ** 2).rolling(21, min_periods=10).mean()
    tv = (r ** 2).rolling(21, min_periods=10).mean()
    bse = uv / tv.replace(0, np.nan) - 0.5
    d2 = (bse - 2.0 * bse.shift(5) + bse.shift(10)) / float(5 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_upshare_8d_jerk_v089_signal(closeadj):
    r = closeadj.pct_change()
    uv = (r.clip(lower=0) ** 2).rolling(21, min_periods=10).mean()
    tv = (r ** 2).rolling(21, min_periods=10).mean()
    bse = uv / tv.replace(0, np.nan) - 0.5
    d2 = (bse - 2.0 * bse.shift(8) + bse.shift(16)) / float(8 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_upshare_12d_jerk_v090_signal(closeadj):
    r = closeadj.pct_change()
    uv = (r.clip(lower=0) ** 2).rolling(21, min_periods=10).mean()
    tv = (r ** 2).rolling(21, min_periods=10).mean()
    bse = uv / tv.replace(0, np.nan) - 0.5
    d2 = (bse - 2.0 * bse.shift(12) + bse.shift(24)) / float(12 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_riskrun63_10d_jerk_v091_signal(closeadj):
    g = np.log(closeadj.replace(0, np.nan) / closeadj.shift(63).replace(0, np.nan))
    vol = closeadj.pct_change().rolling(63, min_periods=21).std() * np.sqrt(63.0)
    bse = g / vol.replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(10) + bse.shift(20)) / float(10 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_riskrun63_16d_jerk_v092_signal(closeadj):
    g = np.log(closeadj.replace(0, np.nan) / closeadj.shift(63).replace(0, np.nan))
    vol = closeadj.pct_change().rolling(63, min_periods=21).std() * np.sqrt(63.0)
    bse = g / vol.replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(16) + bse.shift(32)) / float(16 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_riskrun63_24d_jerk_v093_signal(closeadj):
    g = np.log(closeadj.replace(0, np.nan) / closeadj.shift(63).replace(0, np.nan))
    vol = closeadj.pct_change().rolling(63, min_periods=21).std() * np.sqrt(63.0)
    bse = g / vol.replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(24) + bse.shift(48)) / float(24 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_dvoltrend_5d_jerk_v094_signal(closeadj, volume):
    dv = np.log((closeadj * volume).replace(0, np.nan))
    bse = (dv - dv.shift(21)) / 21.0
    d2 = (bse - 2.0 * bse.shift(5) + bse.shift(10)) / float(5 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_dvoltrend_8d_jerk_v095_signal(closeadj, volume):
    dv = np.log((closeadj * volume).replace(0, np.nan))
    bse = (dv - dv.shift(21)) / 21.0
    d2 = (bse - 2.0 * bse.shift(8) + bse.shift(16)) / float(8 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_dvoltrend_12d_jerk_v096_signal(closeadj, volume):
    dv = np.log((closeadj * volume).replace(0, np.nan))
    bse = (dv - dv.shift(21)) / 21.0
    d2 = (bse - 2.0 * bse.shift(12) + bse.shift(24)) / float(12 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_rngpos63_10d_jerk_v097_signal(closeadj, high, low):
    hh = high.rolling(63, min_periods=21).max()
    ll = low.rolling(63, min_periods=21).min()
    pos = (closeadj - ll) / (hh - ll).replace(0, np.nan)
    bse = pos - 0.5
    d2 = (bse - 2.0 * bse.shift(10) + bse.shift(20)) / float(10 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_rngpos63_16d_jerk_v098_signal(closeadj, high, low):
    hh = high.rolling(63, min_periods=21).max()
    ll = low.rolling(63, min_periods=21).min()
    pos = (closeadj - ll) / (hh - ll).replace(0, np.nan)
    bse = pos - 0.5
    d2 = (bse - 2.0 * bse.shift(16) + bse.shift(32)) / float(16 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_rngpos63_24d_jerk_v099_signal(closeadj, high, low):
    hh = high.rolling(63, min_periods=21).max()
    ll = low.rolling(63, min_periods=21).min()
    pos = (closeadj - ll) / (hh - ll).replace(0, np.nan)
    bse = pos - 0.5
    d2 = (bse - 2.0 * bse.shift(24) + bse.shift(48)) / float(24 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_donchext_5d_jerk_v100_signal(closeadj, high, low):
    hh = high.rolling(21, min_periods=10).max()
    ll = low.rolling(21, min_periods=10).min()
    mid = (hh + ll) / 2.0
    atr = _f05hb_atr(high, low, closeadj, 21)
    bse = (closeadj - mid) / atr.replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(5) + bse.shift(10)) / float(5 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_donchext_8d_jerk_v101_signal(closeadj, high, low):
    hh = high.rolling(21, min_periods=10).max()
    ll = low.rolling(21, min_periods=10).min()
    mid = (hh + ll) / 2.0
    atr = _f05hb_atr(high, low, closeadj, 21)
    bse = (closeadj - mid) / atr.replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(8) + bse.shift(16)) / float(8 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_donchext_12d_jerk_v102_signal(closeadj, high, low):
    hh = high.rolling(21, min_periods=10).max()
    ll = low.rolling(21, min_periods=10).min()
    mid = (hh + ll) / 2.0
    atr = _f05hb_atr(high, low, closeadj, 21)
    bse = (closeadj - mid) / atr.replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(12) + bse.shift(24)) / float(12 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_upwick_5d_jerk_v103_signal(closeadj, high, low):
    uw = (high - closeadj).clip(lower=0)
    rng = (high - low).replace(0, np.nan)
    bse = (uw / rng).rolling(5, min_periods=3).mean()
    d2 = (bse - 2.0 * bse.shift(5) + bse.shift(10)) / float(5 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_upwick_8d_jerk_v104_signal(closeadj, high, low):
    uw = (high - closeadj).clip(lower=0)
    rng = (high - low).replace(0, np.nan)
    bse = (uw / rng).rolling(5, min_periods=3).mean()
    d2 = (bse - 2.0 * bse.shift(8) + bse.shift(16)) / float(8 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_upwick_12d_jerk_v105_signal(closeadj, high, low):
    uw = (high - closeadj).clip(lower=0)
    rng = (high - low).replace(0, np.nan)
    bse = (uw / rng).rolling(5, min_periods=3).mean()
    d2 = (bse - 2.0 * bse.shift(12) + bse.shift(24)) / float(12 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_maxjumpatr_5d_jerk_v106_signal(closeadj, high, low):
    atr = _f05hb_atr(high, low, closeadj, 21)
    jump = (closeadj - closeadj.shift(1)) / atr.replace(0, np.nan)
    bse = jump.rolling(10, min_periods=5).max()
    d2 = (bse - 2.0 * bse.shift(5) + bse.shift(10)) / float(5 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_maxjumpatr_8d_jerk_v107_signal(closeadj, high, low):
    atr = _f05hb_atr(high, low, closeadj, 21)
    jump = (closeadj - closeadj.shift(1)) / atr.replace(0, np.nan)
    bse = jump.rolling(10, min_periods=5).max()
    d2 = (bse - 2.0 * bse.shift(8) + bse.shift(16)) / float(8 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_maxjumpatr_12d_jerk_v108_signal(closeadj, high, low):
    atr = _f05hb_atr(high, low, closeadj, 21)
    jump = (closeadj - closeadj.shift(1)) / atr.replace(0, np.nan)
    bse = jump.rolling(10, min_periods=5).max()
    d2 = (bse - 2.0 * bse.shift(12) + bse.shift(24)) / float(12 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_stretchema_5d_jerk_v109_signal(closeadj, high, low):
    st = _f05hb_stretch_atr(high, low, closeadj, 5, 14)
    bse = _ema(st, 10)
    d2 = (bse - 2.0 * bse.shift(5) + bse.shift(10)) / float(5 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_stretchema_8d_jerk_v110_signal(closeadj, high, low):
    st = _f05hb_stretch_atr(high, low, closeadj, 5, 14)
    bse = _ema(st, 10)
    d2 = (bse - 2.0 * bse.shift(8) + bse.shift(16)) / float(8 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_stretchema_12d_jerk_v111_signal(closeadj, high, low):
    st = _f05hb_stretch_atr(high, low, closeadj, 5, 14)
    bse = _ema(st, 10)
    d2 = (bse - 2.0 * bse.shift(12) + bse.shift(24)) / float(12 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_distma126_21d_jerk_v112_signal(closeadj):
    ma = closeadj.rolling(126, min_periods=42).mean()
    bse = closeadj / ma.replace(0, np.nan) - 1.0
    d2 = (bse - 2.0 * bse.shift(21) + bse.shift(42)) / float(21 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_distma126_34d_jerk_v113_signal(closeadj):
    ma = closeadj.rolling(126, min_periods=42).mean()
    bse = closeadj / ma.replace(0, np.nan) - 1.0
    d2 = (bse - 2.0 * bse.shift(34) + bse.shift(68)) / float(34 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_distma126_50d_jerk_v114_signal(closeadj):
    ma = closeadj.rolling(126, min_periods=42).mean()
    bse = closeadj / ma.replace(0, np.nan) - 1.0
    d2 = (bse - 2.0 * bse.shift(50) + bse.shift(100)) / float(50 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_volconc_5d_jerk_v115_signal(volume):
    tot = volume.rolling(21, min_periods=10).sum()
    mx = volume.rolling(21, min_periods=10).max()
    bse = mx / tot.replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(5) + bse.shift(10)) / float(5 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_volconc_8d_jerk_v116_signal(volume):
    tot = volume.rolling(21, min_periods=10).sum()
    mx = volume.rolling(21, min_periods=10).max()
    bse = mx / tot.replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(8) + bse.shift(16)) / float(8 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_volconc_12d_jerk_v117_signal(volume):
    tot = volume.rolling(21, min_periods=10).sum()
    mx = volume.rolling(21, min_periods=10).max()
    bse = mx / tot.replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(12) + bse.shift(24)) / float(12 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_obenergy_5d_jerk_v118_signal(closeadj):
    rsi = _f05hb_rsi(closeadj, 14)
    bse = (rsi - 50.0).clip(lower=0).rolling(10, min_periods=5).sum()
    d2 = (bse - 2.0 * bse.shift(5) + bse.shift(10)) / float(5 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_obenergy_8d_jerk_v119_signal(closeadj):
    rsi = _f05hb_rsi(closeadj, 14)
    bse = (rsi - 50.0).clip(lower=0).rolling(10, min_periods=5).sum()
    d2 = (bse - 2.0 * bse.shift(8) + bse.shift(16)) / float(8 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_obenergy_12d_jerk_v120_signal(closeadj):
    rsi = _f05hb_rsi(closeadj, 14)
    bse = (rsi - 50.0).clip(lower=0).rolling(10, min_periods=5).sum()
    d2 = (bse - 2.0 * bse.shift(12) + bse.shift(24)) / float(12 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_emadiff_5d_jerk_v121_signal(closeadj):
    bse = _ema(closeadj, 8) / _ema(closeadj, 21).replace(0, np.nan) - 1.0
    d2 = (bse - 2.0 * bse.shift(5) + bse.shift(10)) / float(5 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_emadiff_8d_jerk_v122_signal(closeadj):
    bse = _ema(closeadj, 8) / _ema(closeadj, 21).replace(0, np.nan) - 1.0
    d2 = (bse - 2.0 * bse.shift(8) + bse.shift(16)) / float(8 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_emadiff_12d_jerk_v123_signal(closeadj):
    bse = _ema(closeadj, 8) / _ema(closeadj, 21).replace(0, np.nan) - 1.0
    d2 = (bse - 2.0 * bse.shift(12) + bse.shift(24)) / float(12 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_hiextend_10d_jerk_v124_signal(closeadj):
    hi = closeadj.rolling(21, min_periods=10).max()
    ma = closeadj.rolling(21, min_periods=10).mean()
    bse = (hi - ma) / ma.replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(10) + bse.shift(20)) / float(10 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_hiextend_16d_jerk_v125_signal(closeadj):
    hi = closeadj.rolling(21, min_periods=10).max()
    ma = closeadj.rolling(21, min_periods=10).mean()
    bse = (hi - ma) / ma.replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(16) + bse.shift(32)) / float(16 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_hiextend_24d_jerk_v126_signal(closeadj):
    hi = closeadj.rolling(21, min_periods=10).max()
    ma = closeadj.rolling(21, min_periods=10).mean()
    bse = (hi - ma) / ma.replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(24) + bse.shift(48)) / float(24 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_amplitude_5d_jerk_v127_signal(closeadj):
    hi = closeadj.rolling(21, min_periods=10).max()
    lo = closeadj.rolling(21, min_periods=10).min()
    bse = (hi - lo) / closeadj.replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(5) + bse.shift(10)) / float(5 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_amplitude_8d_jerk_v128_signal(closeadj):
    hi = closeadj.rolling(21, min_periods=10).max()
    lo = closeadj.rolling(21, min_periods=10).min()
    bse = (hi - lo) / closeadj.replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(8) + bse.shift(16)) / float(8 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_amplitude_12d_jerk_v129_signal(closeadj):
    hi = closeadj.rolling(21, min_periods=10).max()
    lo = closeadj.rolling(21, min_periods=10).min()
    bse = (hi - lo) / closeadj.replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(12) + bse.shift(24)) / float(12 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_park21_5d_jerk_v130_signal(high, low):
    hl = np.log(high.replace(0, np.nan) / low.replace(0, np.nan)) ** 2
    bse = np.sqrt(hl.rolling(21, min_periods=10).mean() / (4.0 * np.log(2.0)))
    d2 = (bse - 2.0 * bse.shift(5) + bse.shift(10)) / float(5 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_park21_8d_jerk_v131_signal(high, low):
    hl = np.log(high.replace(0, np.nan) / low.replace(0, np.nan)) ** 2
    bse = np.sqrt(hl.rolling(21, min_periods=10).mean() / (4.0 * np.log(2.0)))
    d2 = (bse - 2.0 * bse.shift(8) + bse.shift(16)) / float(8 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_park21_12d_jerk_v132_signal(high, low):
    hl = np.log(high.replace(0, np.nan) / low.replace(0, np.nan)) ** 2
    bse = np.sqrt(hl.rolling(21, min_periods=10).mean() / (4.0 * np.log(2.0)))
    d2 = (bse - 2.0 * bse.shift(12) + bse.shift(24)) / float(12 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_bubble_10d_jerk_v133_signal(closeadj):
    g = np.log(closeadj.replace(0, np.nan) / closeadj.shift(63).replace(0, np.nan))
    ob = _f05hb_rsi(closeadj, 14) / 100.0
    bse = g.clip(lower=0) * ob
    d2 = (bse - 2.0 * bse.shift(10) + bse.shift(20)) / float(10 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_bubble_16d_jerk_v134_signal(closeadj):
    g = np.log(closeadj.replace(0, np.nan) / closeadj.shift(63).replace(0, np.nan))
    ob = _f05hb_rsi(closeadj, 14) / 100.0
    bse = g.clip(lower=0) * ob
    d2 = (bse - 2.0 * bse.shift(16) + bse.shift(32)) / float(16 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_bubble_24d_jerk_v135_signal(closeadj):
    g = np.log(closeadj.replace(0, np.nan) / closeadj.shift(63).replace(0, np.nan))
    ob = _f05hb_rsi(closeadj, 14) / 100.0
    bse = g.clip(lower=0) * ob
    d2 = (bse - 2.0 * bse.shift(24) + bse.shift(48)) / float(24 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_vwext_5d_jerk_v136_signal(closeadj, volume):
    d = _f05hb_dist_ma(closeadj, 21)
    dv = closeadj * volume
    vw = dv / dv.rolling(21, min_periods=10).sum().replace(0, np.nan) * 21.0
    bse = d * vw
    d2 = (bse - 2.0 * bse.shift(5) + bse.shift(10)) / float(5 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_vwext_8d_jerk_v137_signal(closeadj, volume):
    d = _f05hb_dist_ma(closeadj, 21)
    dv = closeadj * volume
    vw = dv / dv.rolling(21, min_periods=10).sum().replace(0, np.nan) * 21.0
    bse = d * vw
    d2 = (bse - 2.0 * bse.shift(8) + bse.shift(16)) / float(8 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_vwext_12d_jerk_v138_signal(closeadj, volume):
    d = _f05hb_dist_ma(closeadj, 21)
    dv = closeadj * volume
    vw = dv / dv.rolling(21, min_periods=10).sum().replace(0, np.nan) * 21.0
    bse = d * vw
    d2 = (bse - 2.0 * bse.shift(12) + bse.shift(24)) / float(12 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_rsirank_5d_jerk_v139_signal(closeadj):
    rsi = _f05hb_rsi(closeadj, 14)
    bse = rsi.rolling(63, min_periods=21).rank(pct=True) - 0.5
    d2 = (bse - 2.0 * bse.shift(5) + bse.shift(10)) / float(5 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_rsirank_8d_jerk_v140_signal(closeadj):
    rsi = _f05hb_rsi(closeadj, 14)
    bse = rsi.rolling(63, min_periods=21).rank(pct=True) - 0.5
    d2 = (bse - 2.0 * bse.shift(8) + bse.shift(16)) / float(8 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_rsirank_12d_jerk_v141_signal(closeadj):
    rsi = _f05hb_rsi(closeadj, 14)
    bse = rsi.rolling(63, min_periods=21).rank(pct=True) - 0.5
    d2 = (bse - 2.0 * bse.shift(12) + bse.shift(24)) / float(12 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_trendeff_10d_jerk_v142_signal(closeadj):
    net = (closeadj - closeadj.shift(21)).abs()
    path = closeadj.diff().abs().rolling(21, min_periods=10).sum()
    bse = net / path.replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(10) + bse.shift(20)) / float(10 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_trendeff_16d_jerk_v143_signal(closeadj):
    net = (closeadj - closeadj.shift(21)).abs()
    path = closeadj.diff().abs().rolling(21, min_periods=10).sum()
    bse = net / path.replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(16) + bse.shift(32)) / float(16 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_trendeff_24d_jerk_v144_signal(closeadj):
    net = (closeadj - closeadj.shift(21)).abs()
    path = closeadj.diff().abs().rolling(21, min_periods=10).sum()
    bse = net / path.replace(0, np.nan)
    d2 = (bse - 2.0 * bse.shift(24) + bse.shift(48)) / float(24 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_signmag_5d_jerk_v145_signal(closeadj, high, low):
    st = _f05hb_stretch_atr(high, low, closeadj, 5, 14)
    bse = np.sign(st) * np.sqrt(st.abs())
    d2 = (bse - 2.0 * bse.shift(5) + bse.shift(10)) / float(5 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_signmag_8d_jerk_v146_signal(closeadj, high, low):
    st = _f05hb_stretch_atr(high, low, closeadj, 5, 14)
    bse = np.sign(st) * np.sqrt(st.abs())
    d2 = (bse - 2.0 * bse.shift(8) + bse.shift(16)) / float(8 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_signmag_12d_jerk_v147_signal(closeadj, high, low):
    st = _f05hb_stretch_atr(high, low, closeadj, 5, 14)
    bse = np.sign(st) * np.sqrt(st.abs())
    d2 = (bse - 2.0 * bse.shift(12) + bse.shift(24)) / float(12 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_compz_5d_jerk_v148_signal(closeadj, high, low, volume):
    st = _z(_f05hb_stretch_atr(high, low, closeadj, 10, 14), 63)
    vz = _z(np.log(volume.replace(0, np.nan)), 63)
    bse = (st + vz) / 2.0
    d2 = (bse - 2.0 * bse.shift(5) + bse.shift(10)) / float(5 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_compz_8d_jerk_v149_signal(closeadj, high, low, volume):
    st = _z(_f05hb_stretch_atr(high, low, closeadj, 10, 14), 63)
    vz = _z(np.log(volume.replace(0, np.nan)), 63)
    bse = (st + vz) / 2.0
    d2 = (bse - 2.0 * bse.shift(8) + bse.shift(16)) / float(8 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f05hb_f05_hype_blowoff_compz_12d_jerk_v150_signal(closeadj, high, low, volume):
    st = _z(_f05hb_stretch_atr(high, low, closeadj, 10, 14), 63)
    vz = _z(np.log(volume.replace(0, np.nan)), 63)
    bse = (st + vz) / 2.0
    d2 = (bse - 2.0 * bse.shift(12) + bse.shift(24)) / float(12 ** 2)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f05hb_f05_hype_blowoff_stretch5_5d_jerk_v001_signal,
    f05hb_f05_hype_blowoff_stretch5_8d_jerk_v002_signal,
    f05hb_f05_hype_blowoff_stretch5_12d_jerk_v003_signal,
    f05hb_f05_hype_blowoff_stretch10_5d_jerk_v004_signal,
    f05hb_f05_hype_blowoff_stretch10_8d_jerk_v005_signal,
    f05hb_f05_hype_blowoff_stretch10_12d_jerk_v006_signal,
    f05hb_f05_hype_blowoff_stretch21_10d_jerk_v007_signal,
    f05hb_f05_hype_blowoff_stretch21_16d_jerk_v008_signal,
    f05hb_f05_hype_blowoff_stretch21_24d_jerk_v009_signal,
    f05hb_f05_hype_blowoff_distma21_5d_jerk_v010_signal,
    f05hb_f05_hype_blowoff_distma21_8d_jerk_v011_signal,
    f05hb_f05_hype_blowoff_distma21_12d_jerk_v012_signal,
    f05hb_f05_hype_blowoff_distma63_10d_jerk_v013_signal,
    f05hb_f05_hype_blowoff_distma63_16d_jerk_v014_signal,
    f05hb_f05_hype_blowoff_distma63_24d_jerk_v015_signal,
    f05hb_f05_hype_blowoff_bandwidth_5d_jerk_v016_signal,
    f05hb_f05_hype_blowoff_bandwidth_8d_jerk_v017_signal,
    f05hb_f05_hype_blowoff_bandwidth_12d_jerk_v018_signal,
    f05hb_f05_hype_blowoff_effratio_5d_jerk_v019_signal,
    f05hb_f05_hype_blowoff_effratio_8d_jerk_v020_signal,
    f05hb_f05_hype_blowoff_effratio_12d_jerk_v021_signal,
    f05hb_f05_hype_blowoff_runslope5_5d_jerk_v022_signal,
    f05hb_f05_hype_blowoff_runslope5_8d_jerk_v023_signal,
    f05hb_f05_hype_blowoff_runslope5_12d_jerk_v024_signal,
    f05hb_f05_hype_blowoff_runslope10_5d_jerk_v025_signal,
    f05hb_f05_hype_blowoff_runslope10_8d_jerk_v026_signal,
    f05hb_f05_hype_blowoff_runslope10_12d_jerk_v027_signal,
    f05hb_f05_hype_blowoff_runslope21_10d_jerk_v028_signal,
    f05hb_f05_hype_blowoff_runslope21_16d_jerk_v029_signal,
    f05hb_f05_hype_blowoff_runslope21_24d_jerk_v030_signal,
    f05hb_f05_hype_blowoff_rsi14_5d_jerk_v031_signal,
    f05hb_f05_hype_blowoff_rsi14_8d_jerk_v032_signal,
    f05hb_f05_hype_blowoff_rsi14_12d_jerk_v033_signal,
    f05hb_f05_hype_blowoff_rsi7_3d_jerk_v034_signal,
    f05hb_f05_hype_blowoff_rsi7_5d_jerk_v035_signal,
    f05hb_f05_hype_blowoff_rsi7_7d_jerk_v036_signal,
    f05hb_f05_hype_blowoff_tailasym_10d_jerk_v037_signal,
    f05hb_f05_hype_blowoff_tailasym_16d_jerk_v038_signal,
    f05hb_f05_hype_blowoff_tailasym_24d_jerk_v039_signal,
    f05hb_f05_hype_blowoff_volspike21_5d_jerk_v040_signal,
    f05hb_f05_hype_blowoff_volspike21_8d_jerk_v041_signal,
    f05hb_f05_hype_blowoff_volspike21_12d_jerk_v042_signal,
    f05hb_f05_hype_blowoff_volspike63_10d_jerk_v043_signal,
    f05hb_f05_hype_blowoff_volspike63_16d_jerk_v044_signal,
    f05hb_f05_hype_blowoff_volspike63_24d_jerk_v045_signal,
    f05hb_f05_hype_blowoff_volz63_5d_jerk_v046_signal,
    f05hb_f05_hype_blowoff_volz63_8d_jerk_v047_signal,
    f05hb_f05_hype_blowoff_volz63_12d_jerk_v048_signal,
    f05hb_f05_hype_blowoff_crowdbuild_5d_jerk_v049_signal,
    f05hb_f05_hype_blowoff_crowdbuild_8d_jerk_v050_signal,
    f05hb_f05_hype_blowoff_crowdbuild_12d_jerk_v051_signal,
    f05hb_f05_hype_blowoff_stoch21_5d_jerk_v052_signal,
    f05hb_f05_hype_blowoff_stoch21_8d_jerk_v053_signal,
    f05hb_f05_hype_blowoff_stoch21_12d_jerk_v054_signal,
    f05hb_f05_hype_blowoff_willr10_5d_jerk_v055_signal,
    f05hb_f05_hype_blowoff_willr10_8d_jerk_v056_signal,
    f05hb_f05_hype_blowoff_willr10_12d_jerk_v057_signal,
    f05hb_f05_hype_blowoff_pctb21_5d_jerk_v058_signal,
    f05hb_f05_hype_blowoff_pctb21_8d_jerk_v059_signal,
    f05hb_f05_hype_blowoff_pctb21_12d_jerk_v060_signal,
    f05hb_f05_hype_blowoff_lowgapatr_5d_jerk_v061_signal,
    f05hb_f05_hype_blowoff_lowgapatr_8d_jerk_v062_signal,
    f05hb_f05_hype_blowoff_lowgapatr_12d_jerk_v063_signal,
    f05hb_f05_hype_blowoff_cci_5d_jerk_v064_signal,
    f05hb_f05_hype_blowoff_cci_8d_jerk_v065_signal,
    f05hb_f05_hype_blowoff_cci_12d_jerk_v066_signal,
    f05hb_f05_hype_blowoff_atrratio_5d_jerk_v067_signal,
    f05hb_f05_hype_blowoff_atrratio_8d_jerk_v068_signal,
    f05hb_f05_hype_blowoff_atrratio_12d_jerk_v069_signal,
    f05hb_f05_hype_blowoff_rangez_5d_jerk_v070_signal,
    f05hb_f05_hype_blowoff_rangez_8d_jerk_v071_signal,
    f05hb_f05_hype_blowoff_rangez_12d_jerk_v072_signal,
    f05hb_f05_hype_blowoff_rvol21_5d_jerk_v073_signal,
    f05hb_f05_hype_blowoff_rvol21_8d_jerk_v074_signal,
    f05hb_f05_hype_blowoff_rvol21_12d_jerk_v075_signal,
    f05hb_f05_hype_blowoff_mafanout_5d_jerk_v076_signal,
    f05hb_f05_hype_blowoff_mafanout_8d_jerk_v077_signal,
    f05hb_f05_hype_blowoff_mafanout_12d_jerk_v078_signal,
    f05hb_f05_hype_blowoff_moveconc_5d_jerk_v079_signal,
    f05hb_f05_hype_blowoff_moveconc_8d_jerk_v080_signal,
    f05hb_f05_hype_blowoff_moveconc_12d_jerk_v081_signal,
    f05hb_f05_hype_blowoff_volaccel_5d_jerk_v082_signal,
    f05hb_f05_hype_blowoff_volaccel_8d_jerk_v083_signal,
    f05hb_f05_hype_blowoff_volaccel_12d_jerk_v084_signal,
    f05hb_f05_hype_blowoff_revfromhi_5d_jerk_v085_signal,
    f05hb_f05_hype_blowoff_revfromhi_8d_jerk_v086_signal,
    f05hb_f05_hype_blowoff_revfromhi_12d_jerk_v087_signal,
    f05hb_f05_hype_blowoff_upshare_5d_jerk_v088_signal,
    f05hb_f05_hype_blowoff_upshare_8d_jerk_v089_signal,
    f05hb_f05_hype_blowoff_upshare_12d_jerk_v090_signal,
    f05hb_f05_hype_blowoff_riskrun63_10d_jerk_v091_signal,
    f05hb_f05_hype_blowoff_riskrun63_16d_jerk_v092_signal,
    f05hb_f05_hype_blowoff_riskrun63_24d_jerk_v093_signal,
    f05hb_f05_hype_blowoff_dvoltrend_5d_jerk_v094_signal,
    f05hb_f05_hype_blowoff_dvoltrend_8d_jerk_v095_signal,
    f05hb_f05_hype_blowoff_dvoltrend_12d_jerk_v096_signal,
    f05hb_f05_hype_blowoff_rngpos63_10d_jerk_v097_signal,
    f05hb_f05_hype_blowoff_rngpos63_16d_jerk_v098_signal,
    f05hb_f05_hype_blowoff_rngpos63_24d_jerk_v099_signal,
    f05hb_f05_hype_blowoff_donchext_5d_jerk_v100_signal,
    f05hb_f05_hype_blowoff_donchext_8d_jerk_v101_signal,
    f05hb_f05_hype_blowoff_donchext_12d_jerk_v102_signal,
    f05hb_f05_hype_blowoff_upwick_5d_jerk_v103_signal,
    f05hb_f05_hype_blowoff_upwick_8d_jerk_v104_signal,
    f05hb_f05_hype_blowoff_upwick_12d_jerk_v105_signal,
    f05hb_f05_hype_blowoff_maxjumpatr_5d_jerk_v106_signal,
    f05hb_f05_hype_blowoff_maxjumpatr_8d_jerk_v107_signal,
    f05hb_f05_hype_blowoff_maxjumpatr_12d_jerk_v108_signal,
    f05hb_f05_hype_blowoff_stretchema_5d_jerk_v109_signal,
    f05hb_f05_hype_blowoff_stretchema_8d_jerk_v110_signal,
    f05hb_f05_hype_blowoff_stretchema_12d_jerk_v111_signal,
    f05hb_f05_hype_blowoff_distma126_21d_jerk_v112_signal,
    f05hb_f05_hype_blowoff_distma126_34d_jerk_v113_signal,
    f05hb_f05_hype_blowoff_distma126_50d_jerk_v114_signal,
    f05hb_f05_hype_blowoff_volconc_5d_jerk_v115_signal,
    f05hb_f05_hype_blowoff_volconc_8d_jerk_v116_signal,
    f05hb_f05_hype_blowoff_volconc_12d_jerk_v117_signal,
    f05hb_f05_hype_blowoff_obenergy_5d_jerk_v118_signal,
    f05hb_f05_hype_blowoff_obenergy_8d_jerk_v119_signal,
    f05hb_f05_hype_blowoff_obenergy_12d_jerk_v120_signal,
    f05hb_f05_hype_blowoff_emadiff_5d_jerk_v121_signal,
    f05hb_f05_hype_blowoff_emadiff_8d_jerk_v122_signal,
    f05hb_f05_hype_blowoff_emadiff_12d_jerk_v123_signal,
    f05hb_f05_hype_blowoff_hiextend_10d_jerk_v124_signal,
    f05hb_f05_hype_blowoff_hiextend_16d_jerk_v125_signal,
    f05hb_f05_hype_blowoff_hiextend_24d_jerk_v126_signal,
    f05hb_f05_hype_blowoff_amplitude_5d_jerk_v127_signal,
    f05hb_f05_hype_blowoff_amplitude_8d_jerk_v128_signal,
    f05hb_f05_hype_blowoff_amplitude_12d_jerk_v129_signal,
    f05hb_f05_hype_blowoff_park21_5d_jerk_v130_signal,
    f05hb_f05_hype_blowoff_park21_8d_jerk_v131_signal,
    f05hb_f05_hype_blowoff_park21_12d_jerk_v132_signal,
    f05hb_f05_hype_blowoff_bubble_10d_jerk_v133_signal,
    f05hb_f05_hype_blowoff_bubble_16d_jerk_v134_signal,
    f05hb_f05_hype_blowoff_bubble_24d_jerk_v135_signal,
    f05hb_f05_hype_blowoff_vwext_5d_jerk_v136_signal,
    f05hb_f05_hype_blowoff_vwext_8d_jerk_v137_signal,
    f05hb_f05_hype_blowoff_vwext_12d_jerk_v138_signal,
    f05hb_f05_hype_blowoff_rsirank_5d_jerk_v139_signal,
    f05hb_f05_hype_blowoff_rsirank_8d_jerk_v140_signal,
    f05hb_f05_hype_blowoff_rsirank_12d_jerk_v141_signal,
    f05hb_f05_hype_blowoff_trendeff_10d_jerk_v142_signal,
    f05hb_f05_hype_blowoff_trendeff_16d_jerk_v143_signal,
    f05hb_f05_hype_blowoff_trendeff_24d_jerk_v144_signal,
    f05hb_f05_hype_blowoff_signmag_5d_jerk_v145_signal,
    f05hb_f05_hype_blowoff_signmag_8d_jerk_v146_signal,
    f05hb_f05_hype_blowoff_signmag_12d_jerk_v147_signal,
    f05hb_f05_hype_blowoff_compz_5d_jerk_v148_signal,
    f05hb_f05_hype_blowoff_compz_8d_jerk_v149_signal,
    f05hb_f05_hype_blowoff_compz_12d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F05_HYPE_BLOWOFF_REGISTRY_001_150 = REGISTRY


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

    print("OK f05_hype_blowoff_3rd_derivatives_001_150_claude: %d features pass" % n_features)
