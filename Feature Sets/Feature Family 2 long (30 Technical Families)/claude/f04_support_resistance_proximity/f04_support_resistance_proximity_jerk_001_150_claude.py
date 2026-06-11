"""f04_support_resistance_proximity jerk features 001-150 (2nd deriv)."""

import numpy as np
import pandas as pd

def _bars_since_true(mask, cap):
    out = pd.Series(np.nan, index=mask.index, dtype=float)
    last = np.nan
    for i in range(len(mask)):
        v = mask.iloc[i]
        if isinstance(v, (bool, np.bool_)) and bool(v):
            last = i
        if not np.isnan(last):
            out.iloc[i] = float(min(i - last, cap))
    return out

def _streak_above(cond):
    out = pd.Series(np.nan, index=cond.index, dtype=float)
    run = 0
    started = False
    for i in range(len(cond)):
        v = cond.iloc[i]
        if isinstance(v, float) and np.isnan(v):
            continue
        started = True
        if bool(v):
            run += 1
        else:
            run = 0
        out.iloc[i] = float(run)
    if not started:
        return out
    return out

def _true_range(high, low, close):
    pc = close.shift(1)
    a = (high - low).abs()
    bb = (high - pc).abs()
    c = (low - pc).abs()
    return pd.concat([a, bb, c], axis=1).max(axis=1)

def f04sr_f04_support_resistance_proximity_dhi_8d_jerk_v001_signal(close, high):
    h8 = high.rolling(8,8).max()
    b = (close - h8) / close.replace(0.0, np.nan)
    return (b - 2.0*b.shift(5) + b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dhi_21d_jerk_v002_signal(close, high):
    h21 = high.rolling(21,21).max()
    b = (close - h21) / close.replace(0.0, np.nan)
    return (b - 2.0*b.shift(10) + b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dlo_50d_jerk_v003_signal(closeadj):
    l50 = closeadj.rolling(50,50).min()
    b = (closeadj - l50) / closeadj.replace(0.0, np.nan)
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dhi_252d_jerk_v004_signal(closeadj):
    h252 = closeadj.rolling(252,200).max()
    b = np.log(closeadj / h252.replace(0.0, np.nan))
    return (b - 2.0*b.shift(63) + b.shift(126)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dlo_252d_jerk_v005_signal(closeadj):
    l252 = closeadj.rolling(252,200).min()
    b = np.log(closeadj / l252.replace(0.0, np.nan))
    return (b - 2.0*b.shift(63) + b.shift(126)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dshi_21d_jerk_v006_signal(high):
    b = high.rolling(21,21).apply(lambda x: float(np.argmax(x[::-1])), raw=True)
    return (b - 2.0*b.shift(5) + b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dslo_63d_jerk_v007_signal(closeadj):
    b = closeadj.rolling(63,63).apply(lambda x: float(np.argmin(x[::-1])), raw=True)
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dshi_252d_jerk_v008_signal(closeadj):
    b = closeadj.rolling(252,200).apply(lambda x: float(np.argmax(x[::-1])), raw=True)
    return (b - 2.0*b.shift(63) + b.shift(126)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dslo_252d_jerk_v009_signal(closeadj):
    b = closeadj.rolling(252,200).apply(lambda x: float(np.argmin(x[::-1])), raw=True)
    return (b - 2.0*b.shift(63) + b.shift(126)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dshi_50d_jerk_v010_signal(closeadj):
    b = closeadj.rolling(50,50).apply(lambda x: float(np.argmax(x[::-1])), raw=True)
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dslo_100d_jerk_v011_signal(closeadj):
    b = closeadj.rolling(100,100).apply(lambda x: float(np.argmin(x[::-1])), raw=True)
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_ddh_252d_jerk_v012_signal(closeadj):
    log_c = np.log(closeadj.replace(0.0, np.nan))
    def _decay(x):
        if np.all(np.isnan(x)):
            return np.nan
        n = len(x)
        ref = x[-1]
        if not np.isfinite(ref):
            return np.nan
        ages = np.arange(n - 1, -1, -1, dtype=float)
        w = np.exp(-ages / 63.0)
        diff = x - ref
        return float(np.nanmax(w * diff))
    b = log_c.rolling(252,60).apply(_decay, raw=True)
    return (b - 2.0*b.shift(63) + b.shift(126)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dul_252d_jerk_v013_signal(closeadj):
    h252 = closeadj.rolling(252,200).max()
    l252 = closeadj.rolling(252,200).min()
    b = np.log(h252.replace(0.0, np.nan) / l252.replace(0.0, np.nan))
    return (b - 2.0*b.shift(63) + b.shift(126)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_ddh_100d_jerk_v014_signal(closeadj):
    h100 = closeadj.rolling(100,100).max()
    b = closeadj / h100.replace(0.0, np.nan) - 1.0
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dul_63d_jerk_v015_signal(closeadj):
    h63 = closeadj.rolling(63,63).max()
    l63 = closeadj.rolling(63,63).min()
    rng = (h63 - l63).replace(0.0, np.nan)
    b = (closeadj - l63) / rng
    return (b - 2.0*b.shift(10) + b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dpiv_1d_jerk_v016_signal(close, high, low):
    h5 = high.shift(1).rolling(5,5).mean()
    l5 = low.shift(1).rolling(5,5).mean()
    c5 = close.shift(1).rolling(5,5).mean()
    pivot_w = (h5 + l5 + c5) / 3.0
    inst = (close - pivot_w) / close.replace(0.0, np.nan)
    b = inst.rolling(21,10).mean()
    return (b - 2.0*b.shift(5) + b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dr1_1d_jerk_v017_signal(close, high, low):
    pivot = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    r1 = 2.0 * pivot - low.shift(1)
    b = (close - r1) / close.replace(0.0, np.nan)
    return (b - 2.0*b.shift(5) + b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_ds1_1d_jerk_v018_signal(close, high, low):
    pivot = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    s1 = 2.0 * pivot - high.shift(1)
    b = (close - s1) / close.replace(0.0, np.nan)
    return (b - 2.0*b.shift(5) + b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dr2_1d_jerk_v019_signal(close, high, low):
    pivot = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    r2 = pivot + (high.shift(1) - low.shift(1))
    cond = (close > r2).astype(float)
    b = cond.rolling(20,5).mean()
    return (b - 2.0*b.shift(5) + b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_ds2_1d_jerk_v020_signal(close, high, low):
    pivot = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    s2 = pivot - (high.shift(1) - low.shift(1))
    cond = (close < s2).astype(float)
    b = cond.rolling(20,5).mean()
    return (b - 2.0*b.shift(5) + b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dcamr3_1d_jerk_v021_signal(close, high, low):
    rng = high.shift(1) - low.shift(1)
    r3 = close.shift(1) + rng * 1.1 / 4.0
    cond = (close > r3).astype(float)
    grp = (cond != cond.shift(1)).cumsum()
    b = cond.groupby(grp).cumsum() * cond
    return (b - 2.0*b.shift(5) + b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dcams3_1d_jerk_v022_signal(close, high, low):
    rng = high.shift(1) - low.shift(1)
    s3 = close.shift(1) - rng * 1.1 / 4.0
    cond = (close < s3).astype(float)
    grp = (cond != cond.shift(1)).cumsum()
    b = cond.groupby(grp).cumsum() * cond
    return (b - 2.0*b.shift(5) + b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dfibr1_1d_jerk_v023_signal(close, high, low):
    rng = high.shift(1) - low.shift(1)
    fib_38 = low.shift(1) + 0.382 * rng
    fib_62 = low.shift(1) + 0.618 * rng
    inside = ((close >= fib_38) & (close <= fib_62)).astype(float)
    b = inside.rolling(10,3).mean()
    return (b - 2.0*b.shift(5) + b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dfrhi_30d_jerk_v024_signal(high, close):
    is_frac = (high.shift(2) > high.shift(3)) & (high.shift(2) > high.shift(4)) & (high.shift(2) > high.shift(1)) & (high.shift(2) > high)
    level = high.shift(2).where(is_frac).ffill(limit=30)
    b = (close - level) / close.replace(0.0, np.nan)
    return (b - 2.0*b.shift(10) + b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dfrlo_50d_jerk_v025_signal(low, closeadj, close):
    is_frac = (low.shift(2) < low.shift(3)) & (low.shift(2) < low.shift(4)) & (low.shift(2) < low.shift(1)) & (low.shift(2) < low)
    level = low.shift(2).where(is_frac).ffill(limit=50)
    b = (close - level) / close.replace(0.0, np.nan)
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_nfrhi_30d_jerk_v026_signal(high):
    is_frac = (high.shift(2) > high.shift(3)) & (high.shift(2) > high.shift(4)) & (high.shift(2) > high.shift(1)) & (high.shift(2) > high)
    b = is_frac.astype(float).rolling(30,10).sum()
    return (b - 2.0*b.shift(10) + b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_nfrlo_50d_jerk_v027_signal(low):
    is_frac = (low.shift(2) < low.shift(3)) & (low.shift(2) < low.shift(4)) & (low.shift(2) < low.shift(1)) & (low.shift(2) < low)
    b = is_frac.astype(float).rolling(50,10).sum()
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_afrhi_30d_jerk_v028_signal(high):
    is_frac = (high.shift(2) > high.shift(3)) & (high.shift(2) > high.shift(4)) & (high.shift(2) > high.shift(1)) & (high.shift(2) > high)
    b = _bars_since_true(is_frac.fillna(False), 30)
    return (b - 2.0*b.shift(10) + b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_afrlo_50d_jerk_v029_signal(low):
    is_frac = (low.shift(2) < low.shift(3)) & (low.shift(2) < low.shift(4)) & (low.shift(2) < low.shift(1)) & (low.shift(2) < low)
    b = _bars_since_true(is_frac.fillna(False), 50)
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dr10_1d_jerk_v030_signal(close):
    nearest = (close / 10.0).round() * 10.0
    b = (close - nearest) / close.replace(0.0, np.nan)
    return (b - 2.0*b.shift(5) + b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dr5_1d_jerk_v031_signal(close):
    nearest = (close / 5.0).round() * 5.0
    b = (close - nearest) / close.replace(0.0, np.nan)
    return (b - 2.0*b.shift(5) + b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_pr10_1d_jerk_v032_signal(close):
    b = (close / 10.0) - np.floor(close / 10.0)
    return (b - 2.0*b.shift(5) + b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_drone_1d_jerk_v033_signal(close):
    nearest = (close / 1.0).round() * 1.0
    b = (close - nearest) / close.replace(0.0, np.nan)
    return (b - 2.0*b.shift(5) + b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dr100_1d_jerk_v034_signal(close):
    nearest = (close / 100.0).round() * 100.0
    b = (close - nearest) / close.replace(0.0, np.nan)
    return (b - 2.0*b.shift(5) + b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_thi_30d_jerk_v035_signal(high):
    h30 = high.rolling(30,15).max()
    touched = (high >= 0.995 * h30) & (h30.notna())
    b = touched.astype(float).rolling(30,15).sum()
    return (b - 2.0*b.shift(10) + b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_thi_60d_jerk_v036_signal(high, closeadj):
    h60 = high.rolling(60,30).max()
    touched = (high >= 0.99 * h60) & (h60.notna())
    b = touched.astype(float).rolling(60,30).sum()
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_tlo_30d_jerk_v037_signal(low):
    l30 = low.rolling(30,15).min()
    touched = (low <= 1.005 * l30) & (l30.notna())
    b = touched.astype(float).rolling(30,15).sum()
    return (b - 2.0*b.shift(10) + b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_tlo_60d_jerk_v038_signal(low):
    l60 = low.rolling(60,30).min()
    touched = (low <= 1.01 * l60) & (l60.notna())
    b = touched.astype(float).rolling(60,30).sum()
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_tmaxhi_100d_jerk_v039_signal(high):
    def _f(x):
        if len(x) < 30:
            return np.nan
        ref = float(x[-1])
        if not np.isfinite(ref) or ref <= 0:
            return np.nan
        bins = np.round(np.log(x / ref) / np.log(1.005))
        vals, cnts = np.unique(bins, return_counts=True)
        return float(cnts.max())
    b = high.rolling(100,30).apply(_f, raw=True)
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_sigbd_20d_jerk_v041_signal(close, low):
    prior_lo = low.shift(1).rolling(20,20).min()
    b = np.sign(prior_lo - close)
    return (b - 2.0*b.shift(5) + b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_sigbo_50d_jerk_v042_signal(closeadj):
    prior_hi = closeadj.shift(1).rolling(50,50).max()
    b = np.sign(closeadj - prior_hi)
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_sigbd_50d_jerk_v043_signal(closeadj):
    prior_lo = closeadj.shift(1).rolling(50,50).min()
    b = np.sign(prior_lo - closeadj)
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_skbo_20d_jerk_v044_signal(close, high):
    prior_hi = high.shift(1).rolling(20,20).max()
    cond = (close > prior_hi)
    b = _streak_above(cond)
    return (b - 2.0*b.shift(5) + b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_skbd_20d_jerk_v045_signal(close, low):
    prior_lo = low.shift(1).rolling(20,20).min()
    cond = (close < prior_lo)
    b = _streak_above(cond)
    return (b - 2.0*b.shift(5) + b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_skbo_63d_jerk_v046_signal(closeadj):
    prior_hi = closeadj.shift(1).rolling(63,63).max()
    cond = (closeadj > prior_hi)
    b = _streak_above(cond)
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_fbo_30d_jerk_v047_signal(close, high):
    prior_hi = high.shift(1).rolling(20,20).max()
    broke_above = (close > prior_hi)
    came_back = (close < prior_hi)
    failed = pd.Series(False, index=close.index)
    for j in range(1, 6):
        failed = failed | (broke_above.shift(j).fillna(False) & came_back)
    b = failed.astype(float).rolling(30,15).sum()
    return (b - 2.0*b.shift(10) + b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_mbo_20d_jerk_v048_signal(close, high):
    prior_hi = high.shift(1).rolling(20,20).max()
    log_hi = np.log(prior_hi.replace(0.0, np.nan))
    def _nu(x):
        if np.all(np.isnan(x)):
            return np.nan
        x = x[~np.isnan(x)]
        if len(x) == 0:
            return np.nan
        bins = np.round(x / np.log(1.01))
        return float(len(np.unique(bins)))
    b = log_hi.rolling(60,20).apply(_nu, raw=True)
    return (b - 2.0*b.shift(5) + b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_mbo_50d_jerk_v049_signal(closeadj):
    prior_hi = closeadj.shift(1).rolling(50,50).max()
    b = (closeadj - prior_hi) / closeadj.replace(0.0, np.nan)
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_mbd_20d_jerk_v050_signal(close, low):
    prior_lo = low.shift(1).rolling(20,20).min()
    b = (prior_lo - close) / close.replace(0.0, np.nan)
    return (b - 2.0*b.shift(5) + b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_mbo_252d_jerk_v051_signal(closeadj):
    prior_hi = closeadj.shift(1).rolling(252,200).max()
    is_break = (closeadj > prior_hi).astype(float)
    b = is_break.rolling(252,200).sum()
    return (b - 2.0*b.shift(63) + b.shift(126)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dlmx_21d_jerk_v052_signal(close, high):
    h21 = high.rolling(21,21).max()
    l21 = high.rolling(21,21).min()
    mid = (h21 + l21) / 2.0
    b = (close - mid) / close.replace(0.0, np.nan)
    return (b - 2.0*b.shift(10) + b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dlmn_63d_jerk_v053_signal(closeadj):
    l63 = closeadj.rolling(63,63).min()
    diff = closeadj - l63
    b = diff.rolling(63,30).std() / closeadj.replace(0.0, np.nan)
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dlmx_8d_jerk_v054_signal(close, high):
    h8 = high.rolling(8,8).max()
    l8 = high.rolling(8,8).min()
    mh = high.rolling(8,8).mean().replace(0.0, np.nan)
    b = (h8 - l8) / mh
    return (b - 2.0*b.shift(5) + b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dlmn_100d_jerk_v055_signal(closeadj):
    l100 = closeadj.rolling(100,100).min()
    m100 = closeadj.rolling(100,100).mean()
    b = (m100 - l100) / closeadj.replace(0.0, np.nan)
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_alm_21d_jerk_v056_signal(high):
    h21 = high.rolling(21,21).max()
    l21 = high.rolling(21,21).min()
    rng = (h21 - l21).replace(0.0, np.nan)
    b = (high - l21) / rng
    return (b - 2.0*b.shift(10) + b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_nphi_100d_jerk_v057_signal(closeadj, high):
    is_frac = (high.shift(2) > high.shift(3)) & (high.shift(2) > high.shift(4)) & (high.shift(2) > high.shift(1)) & (high.shift(2) > high)
    levels = high.shift(2).where(is_frac)
    ratio = (levels / closeadj - 1.0)
    def _cnt(x):
        if np.all(np.isnan(x)):
            return np.nan
        x = x[~np.isnan(x)]
        return float((np.abs(x) <= 0.02).sum())
    b = ratio.rolling(100,10).apply(_cnt, raw=True)
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_nplo_100d_jerk_v058_signal(closeadj, low):
    is_frac = (low.shift(2) < low.shift(3)) & (low.shift(2) < low.shift(4)) & (low.shift(2) < low.shift(1)) & (low.shift(2) < low)
    levels = low.shift(2).where(is_frac)
    ratio = (levels / closeadj - 1.0)
    def _cnt(x):
        if np.all(np.isnan(x)):
            return np.nan
        x = x[~np.isnan(x)]
        return float((np.abs(x) <= 0.02).sum())
    b = ratio.rolling(100,10).apply(_cnt, raw=True)
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_denhi_252d_jerk_v059_signal(closeadj, high):
    rel = (high / closeadj - 1.0)
    in_band = (rel.abs() <= 0.02).astype(float)
    b = in_band.rolling(252,100).mean()
    return (b - 2.0*b.shift(63) + b.shift(126)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_denlo_252d_jerk_v060_signal(closeadj, low):
    is_piv = (low.shift(2) < low.shift(4)) & (low.shift(2) < low.shift(3)) & (low.shift(2) < low.shift(1)) & (low.shift(2) < low)
    levels = low.shift(2).where(is_piv)
    log_levels = np.log(levels.replace(0.0, np.nan))
    n = len(log_levels)
    arr = log_levels.to_numpy()
    base_arr = np.full(n, np.nan, dtype=float)
    for t in range(252, n):
        window = arr[t-251:t+1]
        m = ~np.isnan(window)
        if m.sum() < 5:
            continue
        base_arr[t] = float(np.std(window[m], ddof=1)) if m.sum() > 1 else 0.0
    b = pd.Series(base_arr, index=closeadj.index)
    return (b - 2.0*b.shift(63) + b.shift(126)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_rkhi_60d_jerk_v061_signal(closeadj):
    h252 = closeadj.rolling(252,200).max()
    d = np.log(closeadj / h252.replace(0.0, np.nan))
    b = d.rolling(60,20).rank(pct=True)
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_rklo_60d_jerk_v062_signal(closeadj):
    l252 = closeadj.rolling(252,200).min()
    d = closeadj / l252.replace(0.0, np.nan) - 1.0
    b = d.rolling(60,20).rank(pct=True)
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_rkfr_30d_jerk_v063_signal(closeadj, high):
    is_frac = (high.shift(2) > high.shift(3)) & (high.shift(2) > high.shift(4)) & (high.shift(2) > high.shift(1)) & (high.shift(2) > high)
    level = high.shift(2).where(is_frac).ffill(limit=60)
    d = (closeadj - level) / closeadj.replace(0.0, np.nan)
    b = d.rolling(30,10).rank(pct=True)
    return (b - 2.0*b.shift(10) + b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_rec_30d_jerk_v064_signal(close, high):
    prior_hi = high.shift(1).rolling(20,20).max()
    cond = (close > prior_hi)
    b = _bars_since_true(cond.fillna(False), 30)
    return (b - 2.0*b.shift(10) + b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_redr_30d_jerk_v065_signal(close, high):
    prior_hi = high.shift(1).rolling(20,20).max()
    broke = (close > prior_hi)
    lvl_at_break = prior_hi.where(broke).ffill(limit=30)
    came_back = (close < lvl_at_break)
    magnitude = (lvl_at_break - close) / close.replace(0.0, np.nan)
    b = magnitude.where(came_back)
    return (b - 2.0*b.shift(10) + b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_netbo_60d_jerk_v066_signal(close, high, low):
    prior_hi = high.shift(1).rolling(20,20).max()
    prior_lo = low.shift(1).rolling(20,20).min()
    up = (close > prior_hi).astype(float)
    dn = (close < prior_lo).astype(float)
    b = up.rolling(60,30).sum() - dn.rolling(60,30).sum()
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_ddmpv_1d_jerk_v067_signal(close, high, low):
    rng = (high.shift(1) - low.shift(1)).replace(0.0, np.nan)
    b = (close - low.shift(1)) / rng
    return (b - 2.0*b.shift(5) + b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dwdr1_1d_jerk_v068_signal(close, high, low):
    body_top = pd.concat([close.shift(1), low.shift(1)], axis=1).max(axis=1)
    rejection = (high.shift(1) - body_top) / high.shift(1).replace(0.0, np.nan)
    is_rej = (rejection > 0.005).astype(float)
    b = is_rej.rolling(10,3).sum()
    return (b - 2.0*b.shift(5) + b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dwds1_1d_jerk_v069_signal(close, high, low):
    body_bot = pd.concat([close.shift(1), high.shift(1)], axis=1).min(axis=1)
    rejection = (body_bot - low.shift(1)) / low.shift(1).replace(0.0, np.nan)
    is_rej = (rejection > 0.005).astype(float)
    b = is_rej.rolling(10,3).sum()
    return (b - 2.0*b.shift(5) + b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dath_all_jerk_v070_signal(closeadj):
    ath = closeadj.expanding(min_periods=30).max()
    b = np.log(closeadj / ath.replace(0.0, np.nan))
    return (b - 2.0*b.shift(63) + b.shift(126)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_kelb_252d_jerk_v071_signal(closeadj):
    h252 = closeadj.rolling(252,200).max()
    l252 = closeadj.rolling(252,200).min()
    near_hi = np.log(closeadj / h252.replace(0.0, np.nan)).abs()
    near_lo = np.log(closeadj / l252.replace(0.0, np.nan)).abs()
    b = np.sign(near_lo - near_hi)
    return (b - 2.0*b.shift(63) + b.shift(126)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_mxh_21d_jerk_v072_signal(closeadj):
    h252 = closeadj.rolling(252,200).max()
    d = np.log(closeadj / h252.replace(0.0, np.nan))
    b = d.rolling(21,10).max() - d.rolling(21,10).min()
    return (b - 2.0*b.shift(10) + b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_nh_252d_jerk_v073_signal(closeadj):
    prior_hi = closeadj.shift(1).rolling(252,200).max()
    b = pd.Series(np.where(closeadj > prior_hi, 1.0, -1.0), index=closeadj.index, dtype=float).where(prior_hi.notna())
    return (b - 2.0*b.shift(63) + b.shift(126)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_nl_252d_jerk_v074_signal(closeadj):
    prior_lo = closeadj.shift(1).rolling(252,200).min()
    b = pd.Series(np.where(closeadj < prior_lo, 1.0, -1.0), index=closeadj.index, dtype=float).where(prior_lo.notna())
    return (b - 2.0*b.shift(63) + b.shift(126)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_nhl_60d_jerk_v075_signal(closeadj):
    prior_hi = closeadj.shift(1).rolling(60,60).max()
    prior_lo = closeadj.shift(1).rolling(60,60).min()
    up = (closeadj > prior_hi).astype(float)
    dn = (closeadj < prior_lo).astype(float)
    b = up.rolling(60,30).sum() - dn.rolling(60,30).sum()
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dmpv_21d_jerk_v076_signal(closeadj, high, low):
    h21 = high.rolling(21,21).max().shift(1)
    l21 = low.rolling(21,21).min().shift(1)
    b = (h21 - l21) / closeadj.replace(0.0, np.nan)
    return (b - 2.0*b.shift(10) + b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dwpv_5d_jerk_v077_signal(close, high, low):
    h5 = high.rolling(5,5).max().shift(1)
    l5 = low.rolling(5,5).min().shift(1)
    c1 = close.shift(1)
    pivot = (h5 + l5 + c1) / 3.0
    b = (close - pivot) / close.replace(0.0, np.nan)
    return (b - 2.0*b.shift(5) + b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dpsh_21d_jerk_v078_signal(close, high):
    lvl = high.shift(21)
    b = (close - lvl) / close.replace(0.0, np.nan)
    return (b - 2.0*b.shift(10) + b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dpsl_21d_jerk_v079_signal(close, low):
    diff = low.shift(21) - low
    is_above = (diff > 0).astype(float)
    b = is_above.rolling(21,10).sum()
    return (b - 2.0*b.shift(10) + b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_drx_10d_jerk_v080_signal(close, high):
    lvl = high.shift(5).rolling(6,6).max()
    b = (close - lvl) / close.replace(0.0, np.nan)
    return (b - 2.0*b.shift(5) + b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dvc_30d_jerk_v081_signal(closeadj, volume, close):
    out = pd.Series(np.nan, index=closeadj.index, dtype=float)
    ca_arr = closeadj.to_numpy()
    v_arr = volume.to_numpy()
    n = len(closeadj)
    for i in range(29, n):
        wc = ca_arr[i - 29:i + 1]
        wv = v_arr[i - 29:i + 1]
        if np.all(np.isnan(wv)) or np.all(np.isnan(wc)):
            continue
        idx = int(np.nanargmax(wv))
        lvl = float(wc[idx])
        if lvl > 0 and np.isfinite(ca_arr[i]):
            out.iloc[i] = (ca_arr[i] - lvl) / ca_arr[i]
    b = out
    return (b - 2.0*b.shift(10) + b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dvh_60d_jerk_v082_signal(closeadj, volume, high):
    out = pd.Series(np.nan, index=closeadj.index, dtype=float)
    ca_arr = closeadj.to_numpy()
    v_arr = volume.to_numpy()
    h_arr = high.to_numpy()
    n = len(closeadj)
    for i in range(59, n):
        wv = v_arr[i - 59:i + 1]
        wh = h_arr[i - 59:i + 1]
        if np.all(np.isnan(wv)) or np.all(np.isnan(wh)):
            continue
        idx = int(np.nanargmax(wv))
        lvl = float(wh[idx])
        if lvl > 0 and np.isfinite(ca_arr[i]):
            out.iloc[i] = (ca_arr[i] - lvl) / ca_arr[i]
    b = out
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dvl_60d_jerk_v083_signal(closeadj, volume, low):
    out = pd.Series(np.nan, index=closeadj.index, dtype=float)
    v_arr = volume.to_numpy()
    n = len(closeadj)
    for i in range(59, n):
        wv = v_arr[i - 59:i + 1]
        if np.all(np.isnan(wv)):
            continue
        idx = int(np.nanargmax(wv))
        out.iloc[i] = float(59 - idx)
    b = out
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dvh_50d_jerk_v084_signal(closeadj, volume, high):
    w = volume.replace(0.0, np.nan)
    q90 = high.rolling(50,30).quantile(0.9)
    is_upper = (high >= q90).astype(float)
    num = (is_upper * w).rolling(50,30).sum()
    den = w.rolling(50,30).sum()
    b = num / den.replace(0.0, np.nan)
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dvl_50d_jerk_v085_signal(closeadj, volume, low):
    w = volume.to_numpy()
    l_arr = low.to_numpy()
    n = len(low)
    out_arr = np.full(n, np.nan, dtype=float)
    for i in range(49, n):
        wv = w[i - 49:i + 1]
        wl = l_arr[i - 49:i + 1]
        if np.all(np.isnan(wv)) or np.all(np.isnan(wl)):
            continue
        thr = np.nanquantile(wv, 0.7)
        m = wv >= thr
        if m.sum() < 5:
            continue
        ls = wl[m]
        out_arr[i] = float(np.nanmax(ls) - np.nanmin(ls)) / float(closeadj.iloc[i]) if closeadj.iloc[i] > 0 else np.nan
    b = pd.Series(out_arr, index=closeadj.index)
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dcamr1_1d_jerk_v086_signal(close, high, low):
    rng = high.shift(1) - low.shift(1)
    r1 = close.shift(1) + rng * 1.1 / 12.0
    cond = (close > r1).astype(float)
    b = cond.rolling(10,3).sum()
    return (b - 2.0*b.shift(5) + b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dcams1_1d_jerk_v087_signal(close, high, low):
    rng = high.shift(1) - low.shift(1)
    s1 = close.shift(1) - rng * 1.1 / 12.0
    cond = (close < s1).astype(float)
    b = cond.rolling(20,5).mean()
    return (b - 2.0*b.shift(5) + b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dcamr2_1d_jerk_v088_signal(close, high, low):
    rng = high.shift(1) - low.shift(1)
    r2 = close.shift(1) + rng * 1.1 / 6.0
    cond = (close > r2).astype(float)
    b = cond.rolling(30,10).sum()
    return (b - 2.0*b.shift(5) + b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dcams2_1d_jerk_v089_signal(close, high, low):
    rng = high.shift(1) - low.shift(1)
    s2 = close.shift(1) - rng * 1.1 / 6.0
    cond = (close < s2).astype(float)
    b = cond.rolling(20,5).sum()
    return (b - 2.0*b.shift(5) + b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dfibr2_1d_jerk_v090_signal(close, high, low):
    pivot = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    rng = high.shift(1) - low.shift(1)
    r2 = pivot + 0.618 * rng
    cond = (close > r2).astype(float)
    grp = (cond != cond.shift(1)).cumsum()
    b = cond.groupby(grp).cumsum() * cond
    return (b - 2.0*b.shift(5) + b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dfibs1_1d_jerk_v091_signal(close, high, low):
    pivot = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    rng = high.shift(1) - low.shift(1)
    r236 = pivot + 0.236 * rng
    r382 = pivot + 0.382 * rng
    r618 = pivot + 0.618 * rng
    cond = ((close > r236) & (close > r382) & (close > r618)).astype(float)
    b = cond.rolling(20,5).mean()
    return (b - 2.0*b.shift(5) + b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dfibs2_1d_jerk_v092_signal(close, high, low):
    pivot = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    rng = high.shift(1) - low.shift(1)
    s2 = pivot - 0.618 * rng
    cond = (close < s2).astype(float)
    b = cond.rolling(10,3).sum()
    return (b - 2.0*b.shift(5) + b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_nhh_21d_jerk_v093_signal(high):
    is_frac = (high.shift(2) > high.shift(3)) & (high.shift(2) > high.shift(4)) & (high.shift(2) > high.shift(1)) & (high.shift(2) > high)
    levels = high.shift(2).where(is_frac).ffill(limit=40)
    prev_levels = levels.shift(1).ffill(limit=40)
    hh = is_frac & (high.shift(2) > prev_levels)
    b = hh.astype(float).rolling(21,10).sum()
    return (b - 2.0*b.shift(10) + b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_nll_21d_jerk_v094_signal(low):
    is_frac = (low.shift(2) < low.shift(3)) & (low.shift(2) < low.shift(4)) & (low.shift(2) < low.shift(1)) & (low.shift(2) < low)
    levels = low.shift(2).where(is_frac).ffill(limit=40)
    prev_levels = levels.shift(1).ffill(limit=40)
    ll = is_frac & (low.shift(2) < prev_levels)
    b = ll.astype(float).rolling(21,10).sum()
    return (b - 2.0*b.shift(10) + b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_nhl_30d_jerk_v095_signal(low):
    is_frac = (low.shift(2) < low.shift(3)) & (low.shift(2) < low.shift(4)) & (low.shift(2) < low.shift(1)) & (low.shift(2) < low)
    levels = low.shift(2).where(is_frac).ffill(limit=40)
    prev_levels = levels.shift(1).ffill(limit=40)
    hl = is_frac & (low.shift(2) > prev_levels)
    b = hl.astype(float).rolling(30,15).sum()
    return (b - 2.0*b.shift(10) + b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_nlh_30d_jerk_v096_signal(high):
    is_frac = (high.shift(2) > high.shift(3)) & (high.shift(2) > high.shift(4)) & (high.shift(2) > high.shift(1)) & (high.shift(2) > high)
    levels = high.shift(2).where(is_frac).ffill(limit=40)
    prev_levels = levels.shift(1).ffill(limit=40)
    lh = is_frac & (high.shift(2) < prev_levels)
    b = lh.astype(float).rolling(30,15).sum()
    return (b - 2.0*b.shift(10) + b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_nwave_30d_jerk_v097_signal(high, low):
    is_fh = (high.shift(2) > high.shift(3)) & (high.shift(2) > high.shift(4)) & (high.shift(2) > high.shift(1)) & (high.shift(2) > high)
    is_fl = (low.shift(2) < low.shift(3)) & (low.shift(2) < low.shift(4)) & (low.shift(2) < low.shift(1)) & (low.shift(2) < low)
    fh_lvl = high.shift(2).where(is_fh).ffill(limit=40)
    fl_lvl = low.shift(2).where(is_fl).ffill(limit=40)
    fh_prev = fh_lvl.shift(1).ffill(limit=40)
    fl_prev = fl_lvl.shift(1).ffill(limit=40)
    hh = (is_fh & (high.shift(2) > fh_prev)).astype(float)
    lh = (is_fh & (high.shift(2) < fh_prev)).astype(float)
    ll = (is_fl & (low.shift(2) < fl_prev)).astype(float)
    hl = (is_fl & (low.shift(2) > fl_prev)).astype(float)
    b = (hh + hl - ll - lh).rolling(30,15).sum()
    return (b - 2.0*b.shift(10) + b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dfr3h_30d_jerk_v098_signal(high, close):
    is_frac = (high.shift(1) > high.shift(2)) & (high.shift(1) > high)
    level = high.shift(1).where(is_frac).ffill(limit=30)
    b = (close - level) / close.replace(0.0, np.nan)
    return (b - 2.0*b.shift(10) + b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dfr3l_30d_jerk_v099_signal(low, close):
    is_frac = (low.shift(1) < low.shift(2)) & (low.shift(1) < low)
    level = low.shift(1).where(is_frac).ffill(limit=30)
    b = (close - level) / close.replace(0.0, np.nan)
    return (b - 2.0*b.shift(10) + b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dfr7h_50d_jerk_v100_signal(high, closeadj):
    h = high
    cond = (h.shift(3) > h.shift(1)) & (h.shift(3) > h.shift(2)) & (h.shift(3) > h.shift(4)) & (h.shift(3) > h.shift(5)) & (h.shift(3) > h.shift(6)) & (h.shift(3) > h)
    level = h.shift(3).where(cond).ffill(limit=50)
    b = (closeadj - level) / closeadj.replace(0.0, np.nan)
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dfr7l_50d_jerk_v101_signal(low, closeadj):
    ll = low
    cond = (ll.shift(3) < ll.shift(1)) & (ll.shift(3) < ll.shift(2)) & (ll.shift(3) < ll.shift(4)) & (ll.shift(3) < ll.shift(5)) & (ll.shift(3) < ll.shift(6)) & (ll.shift(3) < ll)
    level = ll.shift(3).where(cond).ffill(limit=50)
    b = (closeadj - level) / closeadj.replace(0.0, np.nan)
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dfr9h_80d_jerk_v102_signal(high, closeadj):
    h = high
    cond = (h.shift(4) > h.shift(1)) & (h.shift(4) > h.shift(2)) & (h.shift(4) > h.shift(3)) & (h.shift(4) > h.shift(5)) & (h.shift(4) > h.shift(6)) & (h.shift(4) > h.shift(7)) & (h.shift(4) > h.shift(8)) & (h.shift(4) > h)
    level = h.shift(4).where(cond).ffill(limit=80)
    b = (closeadj - level) / closeadj.replace(0.0, np.nan)
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_tsfb_30d_jerk_v103_signal(close, high):
    prior_hi = high.shift(1).rolling(20,20).max()
    broke = (close > prior_hi)
    came_back = (close < prior_hi)
    failed = pd.Series(False, index=close.index)
    for j in range(1, 6):
        failed = failed | (broke.shift(j).fillna(False) & came_back)
    b = _bars_since_true(failed.fillna(False), 30)
    return (b - 2.0*b.shift(10) + b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_tsfd_30d_jerk_v104_signal(close, low):
    prior_lo = low.shift(1).rolling(20,20).min()
    broke = (close < prior_lo)
    came_back = (close > prior_lo)
    failed = pd.Series(False, index=close.index)
    for j in range(1, 6):
        failed = failed | (broke.shift(j).fillna(False) & came_back)
    b = _bars_since_true(failed.fillna(False), 30)
    return (b - 2.0*b.shift(10) + b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_bfn_60d_jerk_v105_signal(close, high, low):
    prior_hi = high.shift(1).rolling(20,20).max()
    prior_lo = low.shift(1).rolling(20,20).min()
    above = (close > prior_hi)
    below = (close < prior_lo)
    succ_up = above & above.shift(5).fillna(False)
    succ_dn = below & below.shift(5).fillna(False)
    b = succ_up.astype(float).rolling(60,30).sum() - succ_dn.astype(float).rolling(60,30).sum()
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_nh20_60d_jerk_v106_signal(closeadj):
    prior_hi = closeadj.shift(1).rolling(20,20).max()
    nh = (closeadj > prior_hi).astype(float)
    b = nh.rolling(60,30).sum()
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_nl20_60d_jerk_v107_signal(closeadj):
    prior_lo = closeadj.shift(1).rolling(20,20).min()
    nl = (closeadj < prior_lo).astype(float)
    b = nl.rolling(60,30).sum()
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_skr10_1d_jerk_v108_signal(close):
    bucket = np.floor(close / 10.0)
    changed = (bucket != bucket.shift(1))
    streak = pd.Series(np.nan, index=close.index, dtype=float)
    run = 0
    for i in range(len(close)):
        v = changed.iloc[i]
        if isinstance(v, float) and np.isnan(v):
            continue
        if bool(v):
            run = 0
        run += 1
        streak.iloc[i] = float(run)
    b = streak
    return (b - 2.0*b.shift(5) + b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_skr100_1d_jerk_v109_signal(close):
    # 2nd-derivative of the fractional position of close within its
    # nearest $100 bucket: (close mod 100) / 100. Replaces a degenerate
    # bars-since-cross streak that monotonically increments (and thus
    # has zero 2nd derivative) on synthetic data whose close stays
    # inside a single $100 bucket.
    pos = (close - np.floor(close / 100.0) * 100.0) / 100.0
    b = pos
    return (b - 2.0*b.shift(5) + b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_asr5_1d_jerk_v110_signal(close):
    bucket = np.floor(close / 5.0)
    changed = (bucket != bucket.shift(1))
    b = _bars_since_true(changed.fillna(False), 60)
    return (b - 2.0*b.shift(5) + b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_ncr10_60d_jerk_v111_signal(close):
    bucket = np.floor(close / 10.0)
    diff = bucket.diff()
    up = (diff > 0).astype(float)
    dn = (diff < 0).astype(float)
    b = up.rolling(60,30).sum() - dn.rolling(60,30).sum()
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_davwap_50d_jerk_v112_signal(closeadj, volume, high, low):
    tp = (high + low + closeadj) / 3.0
    w = volume.replace(0.0, np.nan)
    num = (tp * w).rolling(50,30).sum()
    den = w.rolling(50,30).sum()
    avwap = num / den.replace(0.0, np.nan)
    b = (closeadj - avwap) / closeadj.replace(0.0, np.nan)
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_davwap_100d_jerk_v113_signal(closeadj, volume, high, low):
    # 2nd derivative of an INDICATOR: close > 100d AVWAP, smoothed over
    # 20 bars. Discrete-frequency feature distinct from a continuous
    # distance-to-AVWAP and not collinear with v112's distance.
    tp = (high + low + closeadj) / 3.0
    w = volume.replace(0.0, np.nan)
    num = (tp * w).rolling(100,60).sum()
    den = w.rolling(100,60).sum()
    avwap = num / den.replace(0.0, np.nan)
    cond = (closeadj > avwap).astype(float)
    b = cond.rolling(20,5).mean()
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_davwap_21d_jerk_v114_signal(close, volume):
    w = volume.replace(0.0, np.nan)
    num = (close * w).rolling(21,15).sum()
    den = w.rolling(21,15).sum()
    avwap = num / den.replace(0.0, np.nan)
    cond = (close > avwap).astype(float)
    b = cond.rolling(10,3).mean()
    return (b - 2.0*b.shift(10) + b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dnpv_1d_jerk_v115_signal(close, high, low):
    pivot = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    rng = high.shift(1) - low.shift(1)
    r1 = 2.0 * pivot - low.shift(1)
    s1 = 2.0 * pivot - high.shift(1)
    r2 = pivot + rng
    s2 = pivot - rng
    r3 = high.shift(1) + 2.0 * (pivot - low.shift(1))
    s3 = low.shift(1) - 2.0 * (high.shift(1) - pivot)
    levels = pd.concat({"r1": r1, "r2": r2, "r3": r3, "p": pivot, "s1": s1, "s2": s2, "s3": s3}, axis=1)
    diffs = levels.sub(close, axis=0).mul(-1.0)
    abs_d = diffs.abs()
    idxmin = abs_d.idxmin(axis=1)
    out = pd.Series(np.nan, index=close.index, dtype=float)
    for i in range(len(close)):
        k = idxmin.iloc[i]
        if isinstance(k, str):
            v = diffs.loc[diffs.index[i], k]
            c = close.iloc[i]
            if np.isfinite(v) and np.isfinite(c) and c > 0:
                out.iloc[i] = float(v / c)
    b = out
    return (b - 2.0*b.shift(5) + b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dnfr_30d_jerk_v116_signal(close, high, low):
    is_fh = (high.shift(2) > high.shift(3)) & (high.shift(2) > high.shift(4)) & (high.shift(2) > high.shift(1)) & (high.shift(2) > high)
    is_fl = (low.shift(2) < low.shift(3)) & (low.shift(2) < low.shift(4)) & (low.shift(2) < low.shift(1)) & (low.shift(2) < low)
    fh = high.shift(2).where(is_fh).ffill(limit=30)
    fl = low.shift(2).where(is_fl).ffill(limit=30)
    dh = (close - fh) / close.replace(0.0, np.nan)
    dl = (close - fl) / close.replace(0.0, np.nan)
    use_h = dh.abs() < dl.abs()
    b = dh.where(use_h, dl)
    return (b - 2.0*b.shift(10) + b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dmid_252d_jerk_v117_signal(closeadj):
    h = closeadj.rolling(252,200).max()
    l = closeadj.rolling(252,200).min()
    mid = (h + l) / 2.0
    b = np.log(mid / mid.shift(63).replace(0.0, np.nan))
    return (b - 2.0*b.shift(63) + b.shift(126)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dsmh_21d_jerk_v118_signal(close, high):
    h21 = high.rolling(21,21).max()
    is_new_high = (high >= h21 - 1e-12).astype(float)
    b = is_new_high.rolling(21,10).sum()
    return (b - 2.0*b.shift(10) + b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dsml_21d_jerk_v119_signal(close, low):
    sd_l = low.rolling(21,21).std()
    b = sd_l / close.replace(0.0, np.nan)
    return (b - 2.0*b.shift(10) + b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_datl_all_jerk_v120_signal(closeadj):
    atl = closeadj.expanding(min_periods=1).min()
    is_new = (closeadj <= atl + 1e-12)
    arr = is_new.fillna(False).to_numpy()
    n = len(arr)
    age_arr = np.full(n, np.nan, dtype=float)
    last = -1
    for i in range(n):
        if arr[i]:
            last = i
        if last >= 0:
            age_arr[i] = float(i - last)
    age = pd.Series(age_arr, index=closeadj.index)
    age.iloc[:30] = np.nan
    log_ratio = np.log(closeadj / atl.replace(0.0, np.nan))
    b = age * log_ratio
    return (b - 2.0*b.shift(63) + b.shift(126)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_tama_100d_jerk_v121_signal(closeadj):
    h = closeadj.rolling(252,200).max()
    l = closeadj.rolling(252,200).min()
    mid = (h + l) / 2.0
    above = (closeadj > mid).astype(float)
    b = above.rolling(100,60).mean()
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_tnhi_100d_jerk_v122_signal(closeadj):
    h = closeadj.rolling(252,200).max()
    near = (closeadj / h.replace(0.0, np.nan) >= 0.99)
    arr = near.fillna(False).to_numpy()
    n = len(arr)
    out_arr = np.full(n, np.nan, dtype=float)
    last = -1
    for i in range(n):
        if arr[i]:
            last = i
        if last >= 0:
            out_arr[i] = float(min(i - last, 100))
    b = pd.Series(out_arr, index=closeadj.index)
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dhatr_252d_jerk_v123_signal(closeadj, high, low, close):
    tr = _true_range(high, low, close)
    atr = tr.rolling(14,14).mean()
    h252 = closeadj.rolling(252,200).max()
    b = (closeadj - h252) / atr.replace(0.0, np.nan)
    return (b - 2.0*b.shift(63) + b.shift(126)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dlatr_252d_jerk_v124_signal(closeadj, high, low, close):
    l252 = closeadj.rolling(252,200).min()
    b = np.log(l252 / l252.shift(63).replace(0.0, np.nan))
    return (b - 2.0*b.shift(63) + b.shift(126)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dhatr_20d_jerk_v125_signal(close, high, low):
    tr = _true_range(high, low, close)
    atr = tr.rolling(14,14).mean()
    b = (atr / close.replace(0.0, np.nan)).rolling(20,10).mean()
    return (b - 2.0*b.shift(10) + b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dlatr_20d_jerk_v126_signal(close, high, low):
    tr = _true_range(high, low, close)
    atr = tr.rolling(14,14).mean()
    l20 = low.rolling(20,20).min()
    b = (close - l20) / atr.replace(0.0, np.nan)
    return (b - 2.0*b.shift(10) + b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dzfh_60d_jerk_v127_signal(high, closeadj):
    is_fh = (high.shift(2) > high.shift(3)) & (high.shift(2) > high.shift(4)) & (high.shift(2) > high.shift(1)) & (high.shift(2) > high)
    levels = high.shift(2).where(is_fh)
    b = levels.rolling(60,3).std() / closeadj.replace(0.0, np.nan)
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dzfl_60d_jerk_v128_signal(low, closeadj):
    is_fl = (low.shift(2) < low.shift(3)) & (low.shift(2) < low.shift(4)) & (low.shift(2) < low.shift(1)) & (low.shift(2) < low)
    levels = low.shift(2).where(is_fl)
    b = levels.rolling(60,3).std() / closeadj.replace(0.0, np.nan)
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_wfh_60d_jerk_v129_signal(high):
    is_fh = (high.shift(2) > high.shift(3)) & (high.shift(2) > high.shift(4)) & (high.shift(2) > high.shift(1)) & (high.shift(2) > high)
    levels = high.shift(2).where(is_fh)
    mx = levels.rolling(60,3).max()
    mn = levels.rolling(60,3).min()
    mean = levels.rolling(60,3).mean()
    b = (mx - mn) / mean.replace(0.0, np.nan)
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_wfl_60d_jerk_v130_signal(low):
    is_fl = (low.shift(2) < low.shift(3)) & (low.shift(2) < low.shift(4)) & (low.shift(2) < low.shift(1)) & (low.shift(2) < low)
    levels = low.shift(2).where(is_fl)
    mx = levels.rolling(60,3).max()
    mn = levels.rolling(60,3).min()
    mean = levels.rolling(60,3).mean()
    b = (mx - mn) / mean.replace(0.0, np.nan)
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_zh_30d_jerk_v131_signal(close, high):
    mu = high.rolling(30,15).mean()
    sd = high.rolling(30,15).std()
    b = (close - mu) / sd.replace(0.0, np.nan)
    return (b - 2.0*b.shift(10) + b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_zl_30d_jerk_v132_signal(close, low):
    mu = low.rolling(30,15).mean()
    sd = low.rolling(30,15).std()
    b = sd / mu.replace(0.0, np.nan)
    return (b - 2.0*b.shift(10) + b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_skfh_100d_jerk_v133_signal(high, closeadj):
    is_fh = (high.shift(2) > high.shift(3)) & (high.shift(2) > high.shift(4)) & (high.shift(2) > high.shift(1)) & (high.shift(2) > high)
    levels = high.shift(2).where(is_fh)
    rel = (closeadj - levels) / closeadj.replace(0.0, np.nan)
    b = rel.rolling(100,5).skew()
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_skfl_100d_jerk_v134_signal(low, closeadj):
    is_fl = (low.shift(2) < low.shift(3)) & (low.shift(2) < low.shift(4)) & (low.shift(2) < low.shift(1)) & (low.shift(2) < low)
    levels = low.shift(2).where(is_fl)
    rel = (closeadj - levels) / closeadj.replace(0.0, np.nan)
    b = rel.rolling(100,5).skew()
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_kufh_60d_jerk_v135_signal(closeadj, high):
    rel = (closeadj - high) / closeadj.replace(0.0, np.nan)
    b = rel.rolling(60,20).kurt()
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_cbo20_3d_jerk_v136_signal(close, high):
    prior_hi = high.shift(1).rolling(20,20).max()
    above = (close > prior_hi)
    confirmed = above & above.shift(1).fillna(False) & above.shift(2).fillna(False)
    b = confirmed.astype(float).where(prior_hi.notna())
    return (b - 2.0*b.shift(5) + b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_cbo50_5d_jerk_v137_signal(closeadj):
    prior_hi = closeadj.shift(1).rolling(50,50).max()
    above = (closeadj > prior_hi)
    confirmed = above & above.shift(1).fillna(False) & above.shift(2).fillna(False) & above.shift(3).fillna(False) & above.shift(4).fillna(False)
    b = confirmed.astype(float).where(prior_hi.notna())
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_cbd20_3d_jerk_v138_signal(close, low):
    prior_lo = low.shift(1).rolling(20,20).min()
    below = (close < prior_lo)
    confirmed = below & below.shift(1).fillna(False) & below.shift(2).fillna(False)
    b = confirmed.astype(float).where(prior_lo.notna())
    return (b - 2.0*b.shift(5) + b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_pull_50d_jerk_v139_signal(closeadj):
    prior_hi = closeadj.shift(1).rolling(50,50).max()
    broke = (closeadj > prior_hi)
    lvl_at_break = closeadj.where(broke).ffill(limit=60)
    min_post = closeadj.rolling(60,10).min()
    b = (min_post / lvl_at_break - 1.0)
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_bounce_50d_jerk_v140_signal(closeadj):
    prior_lo = closeadj.shift(1).rolling(50,50).min()
    is_break = (closeadj < prior_lo).astype(float)
    b = is_break.rolling(60,20).sum()
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_holdup_50d_jerk_v141_signal(closeadj):
    prior_hi = closeadj.shift(1).rolling(50,50).max()
    above = (closeadj > prior_hi).astype(int)
    grp = (above != above.shift(1)).cumsum()
    cur_streak = above.groupby(grp).cumsum() * above
    b = cur_streak.rolling(60,30).max().astype(float)
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_sgpv_1d_jerk_v142_signal(close, high, low):
    pivot = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    b = np.sign(close - pivot)
    return (b - 2.0*b.shift(5) + b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_sgwp_5d_jerk_v143_signal(close, high, low):
    h5 = high.rolling(5,5).max().shift(1)
    l5 = low.rolling(5,5).min().shift(1)
    c1 = close.shift(1)
    pivot = (h5 + l5 + c1) / 3.0
    b = np.sign(close - pivot)
    return (b - 2.0*b.shift(5) + b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_pvz_1d_jerk_v144_signal(close, high, low):
    pivot = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    r1 = 2.0 * pivot - low.shift(1)
    s1 = 2.0 * pivot - high.shift(1)
    inside = ((close >= s1) & (close <= r1)).astype(float)
    b = inside.rolling(10,3).mean()
    return (b - 2.0*b.shift(5) + b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_pvrng_1d_jerk_v145_signal(close, high, low):
    rng = (high.shift(1) - low.shift(1))
    b = rng / close.replace(0.0, np.nan)
    return (b - 2.0*b.shift(5) + b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_slh_60d_jerk_v146_signal(closeadj):
    h60 = closeadj.rolling(60,60).max()
    b = np.log(h60 / h60.shift(21).replace(0.0, np.nan))
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_sll_60d_jerk_v147_signal(closeadj):
    l60 = closeadj.rolling(60,60).min()
    b = np.log(l60 / l60.shift(21).replace(0.0, np.nan))
    return (b - 2.0*b.shift(21) + b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_rexp_252d_jerk_v148_signal(closeadj):
    h = closeadj.rolling(252,200).max()
    l = closeadj.rolling(252,200).min()
    rng = (h - l).replace(0.0, np.nan)
    b = np.log(rng / rng.shift(63).replace(0.0, np.nan))
    return (b - 2.0*b.shift(63) + b.shift(126)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_dya_252d_jerk_v149_signal(closeadj):
    b = np.log(closeadj / closeadj.shift(252).replace(0.0, np.nan))
    return (b - 2.0*b.shift(63) + b.shift(126)).replace([np.inf,-np.inf],np.nan)

def f04sr_f04_support_resistance_proximity_pvw_1d_jerk_v150_signal(close, high, low):
    rng_frac = (high - low) / close.replace(0.0, np.nan)
    b = rng_frac.rolling(20,10).mean()
    return (b - 2.0*b.shift(5) + b.shift(10)).replace([np.inf,-np.inf],np.nan)

# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------

def _e(fn, *inputs):
    return fn.__name__, {"inputs": list(inputs), "func": fn}

f04_support_resistance_proximity_jerk_001_150_REGISTRY = dict([
    _e(f04sr_f04_support_resistance_proximity_dhi_8d_jerk_v001_signal, "close", "high"),
    _e(f04sr_f04_support_resistance_proximity_dhi_21d_jerk_v002_signal, "close", "high"),
    _e(f04sr_f04_support_resistance_proximity_dlo_50d_jerk_v003_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_dhi_252d_jerk_v004_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_dlo_252d_jerk_v005_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_dshi_21d_jerk_v006_signal, "high"),
    _e(f04sr_f04_support_resistance_proximity_dslo_63d_jerk_v007_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_dshi_252d_jerk_v008_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_dslo_252d_jerk_v009_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_dshi_50d_jerk_v010_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_dslo_100d_jerk_v011_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_ddh_252d_jerk_v012_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_dul_252d_jerk_v013_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_ddh_100d_jerk_v014_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_dul_63d_jerk_v015_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_dpiv_1d_jerk_v016_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_dr1_1d_jerk_v017_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_ds1_1d_jerk_v018_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_dr2_1d_jerk_v019_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_ds2_1d_jerk_v020_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_dcamr3_1d_jerk_v021_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_dcams3_1d_jerk_v022_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_dfibr1_1d_jerk_v023_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_dfrhi_30d_jerk_v024_signal, "high", "close"),
    _e(f04sr_f04_support_resistance_proximity_dfrlo_50d_jerk_v025_signal, "low", "closeadj", "close"),
    _e(f04sr_f04_support_resistance_proximity_nfrhi_30d_jerk_v026_signal, "high"),
    _e(f04sr_f04_support_resistance_proximity_nfrlo_50d_jerk_v027_signal, "low"),
    _e(f04sr_f04_support_resistance_proximity_afrhi_30d_jerk_v028_signal, "high"),
    _e(f04sr_f04_support_resistance_proximity_afrlo_50d_jerk_v029_signal, "low"),
    _e(f04sr_f04_support_resistance_proximity_dr10_1d_jerk_v030_signal, "close"),
    _e(f04sr_f04_support_resistance_proximity_dr5_1d_jerk_v031_signal, "close"),
    _e(f04sr_f04_support_resistance_proximity_pr10_1d_jerk_v032_signal, "close"),
    _e(f04sr_f04_support_resistance_proximity_drone_1d_jerk_v033_signal, "close"),
    _e(f04sr_f04_support_resistance_proximity_dr100_1d_jerk_v034_signal, "close"),
    _e(f04sr_f04_support_resistance_proximity_thi_30d_jerk_v035_signal, "high"),
    _e(f04sr_f04_support_resistance_proximity_thi_60d_jerk_v036_signal, "high", "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_tlo_30d_jerk_v037_signal, "low"),
    _e(f04sr_f04_support_resistance_proximity_tlo_60d_jerk_v038_signal, "low"),
    _e(f04sr_f04_support_resistance_proximity_tmaxhi_100d_jerk_v039_signal, "high"),
    _e(f04sr_f04_support_resistance_proximity_sigbd_20d_jerk_v041_signal, "close", "low"),
    _e(f04sr_f04_support_resistance_proximity_sigbo_50d_jerk_v042_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_sigbd_50d_jerk_v043_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_skbo_20d_jerk_v044_signal, "close", "high"),
    _e(f04sr_f04_support_resistance_proximity_skbd_20d_jerk_v045_signal, "close", "low"),
    _e(f04sr_f04_support_resistance_proximity_skbo_63d_jerk_v046_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_fbo_30d_jerk_v047_signal, "close", "high"),
    _e(f04sr_f04_support_resistance_proximity_mbo_20d_jerk_v048_signal, "close", "high"),
    _e(f04sr_f04_support_resistance_proximity_mbo_50d_jerk_v049_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_mbd_20d_jerk_v050_signal, "close", "low"),
    _e(f04sr_f04_support_resistance_proximity_mbo_252d_jerk_v051_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_dlmx_21d_jerk_v052_signal, "close", "high"),
    _e(f04sr_f04_support_resistance_proximity_dlmn_63d_jerk_v053_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_dlmx_8d_jerk_v054_signal, "close", "high"),
    _e(f04sr_f04_support_resistance_proximity_dlmn_100d_jerk_v055_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_alm_21d_jerk_v056_signal, "high"),
    _e(f04sr_f04_support_resistance_proximity_nphi_100d_jerk_v057_signal, "closeadj", "high"),
    _e(f04sr_f04_support_resistance_proximity_nplo_100d_jerk_v058_signal, "closeadj", "low"),
    _e(f04sr_f04_support_resistance_proximity_denhi_252d_jerk_v059_signal, "closeadj", "high"),
    _e(f04sr_f04_support_resistance_proximity_denlo_252d_jerk_v060_signal, "closeadj", "low"),
    _e(f04sr_f04_support_resistance_proximity_rkhi_60d_jerk_v061_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_rklo_60d_jerk_v062_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_rkfr_30d_jerk_v063_signal, "closeadj", "high"),
    _e(f04sr_f04_support_resistance_proximity_rec_30d_jerk_v064_signal, "close", "high"),
    _e(f04sr_f04_support_resistance_proximity_redr_30d_jerk_v065_signal, "close", "high"),
    _e(f04sr_f04_support_resistance_proximity_netbo_60d_jerk_v066_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_ddmpv_1d_jerk_v067_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_dwdr1_1d_jerk_v068_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_dwds1_1d_jerk_v069_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_dath_all_jerk_v070_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_kelb_252d_jerk_v071_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_mxh_21d_jerk_v072_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_nh_252d_jerk_v073_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_nl_252d_jerk_v074_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_nhl_60d_jerk_v075_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_dmpv_21d_jerk_v076_signal, "closeadj", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_dwpv_5d_jerk_v077_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_dpsh_21d_jerk_v078_signal, "close", "high"),
    _e(f04sr_f04_support_resistance_proximity_dpsl_21d_jerk_v079_signal, "close", "low"),
    _e(f04sr_f04_support_resistance_proximity_drx_10d_jerk_v080_signal, "close", "high"),
    _e(f04sr_f04_support_resistance_proximity_dvc_30d_jerk_v081_signal, "closeadj", "volume", "close"),
    _e(f04sr_f04_support_resistance_proximity_dvh_60d_jerk_v082_signal, "closeadj", "volume", "high"),
    _e(f04sr_f04_support_resistance_proximity_dvl_60d_jerk_v083_signal, "closeadj", "volume", "low"),
    _e(f04sr_f04_support_resistance_proximity_dvh_50d_jerk_v084_signal, "closeadj", "volume", "high"),
    _e(f04sr_f04_support_resistance_proximity_dvl_50d_jerk_v085_signal, "closeadj", "volume", "low"),
    _e(f04sr_f04_support_resistance_proximity_dcamr1_1d_jerk_v086_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_dcams1_1d_jerk_v087_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_dcamr2_1d_jerk_v088_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_dcams2_1d_jerk_v089_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_dfibr2_1d_jerk_v090_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_dfibs1_1d_jerk_v091_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_dfibs2_1d_jerk_v092_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_nhh_21d_jerk_v093_signal, "high"),
    _e(f04sr_f04_support_resistance_proximity_nll_21d_jerk_v094_signal, "low"),
    _e(f04sr_f04_support_resistance_proximity_nhl_30d_jerk_v095_signal, "low"),
    _e(f04sr_f04_support_resistance_proximity_nlh_30d_jerk_v096_signal, "high"),
    _e(f04sr_f04_support_resistance_proximity_nwave_30d_jerk_v097_signal, "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_dfr3h_30d_jerk_v098_signal, "high", "close"),
    _e(f04sr_f04_support_resistance_proximity_dfr3l_30d_jerk_v099_signal, "low", "close"),
    _e(f04sr_f04_support_resistance_proximity_dfr7h_50d_jerk_v100_signal, "high", "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_dfr7l_50d_jerk_v101_signal, "low", "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_dfr9h_80d_jerk_v102_signal, "high", "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_tsfb_30d_jerk_v103_signal, "close", "high"),
    _e(f04sr_f04_support_resistance_proximity_tsfd_30d_jerk_v104_signal, "close", "low"),
    _e(f04sr_f04_support_resistance_proximity_bfn_60d_jerk_v105_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_nh20_60d_jerk_v106_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_nl20_60d_jerk_v107_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_skr10_1d_jerk_v108_signal, "close"),
    _e(f04sr_f04_support_resistance_proximity_skr100_1d_jerk_v109_signal, "close"),
    _e(f04sr_f04_support_resistance_proximity_asr5_1d_jerk_v110_signal, "close"),
    _e(f04sr_f04_support_resistance_proximity_ncr10_60d_jerk_v111_signal, "close"),
    _e(f04sr_f04_support_resistance_proximity_davwap_50d_jerk_v112_signal, "closeadj", "volume", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_davwap_100d_jerk_v113_signal, "closeadj", "volume", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_davwap_21d_jerk_v114_signal, "close", "volume"),
    _e(f04sr_f04_support_resistance_proximity_dnpv_1d_jerk_v115_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_dnfr_30d_jerk_v116_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_dmid_252d_jerk_v117_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_dsmh_21d_jerk_v118_signal, "close", "high"),
    _e(f04sr_f04_support_resistance_proximity_dsml_21d_jerk_v119_signal, "close", "low"),
    _e(f04sr_f04_support_resistance_proximity_datl_all_jerk_v120_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_tama_100d_jerk_v121_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_tnhi_100d_jerk_v122_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_dhatr_252d_jerk_v123_signal, "closeadj", "high", "low", "close"),
    _e(f04sr_f04_support_resistance_proximity_dlatr_252d_jerk_v124_signal, "closeadj", "high", "low", "close"),
    _e(f04sr_f04_support_resistance_proximity_dhatr_20d_jerk_v125_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_dlatr_20d_jerk_v126_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_dzfh_60d_jerk_v127_signal, "high", "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_dzfl_60d_jerk_v128_signal, "low", "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_wfh_60d_jerk_v129_signal, "high"),
    _e(f04sr_f04_support_resistance_proximity_wfl_60d_jerk_v130_signal, "low"),
    _e(f04sr_f04_support_resistance_proximity_zh_30d_jerk_v131_signal, "close", "high"),
    _e(f04sr_f04_support_resistance_proximity_zl_30d_jerk_v132_signal, "close", "low"),
    _e(f04sr_f04_support_resistance_proximity_skfh_100d_jerk_v133_signal, "high", "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_skfl_100d_jerk_v134_signal, "low", "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_kufh_60d_jerk_v135_signal, "closeadj", "high"),
    _e(f04sr_f04_support_resistance_proximity_cbo20_3d_jerk_v136_signal, "close", "high"),
    _e(f04sr_f04_support_resistance_proximity_cbo50_5d_jerk_v137_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_cbd20_3d_jerk_v138_signal, "close", "low"),
    _e(f04sr_f04_support_resistance_proximity_pull_50d_jerk_v139_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_bounce_50d_jerk_v140_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_holdup_50d_jerk_v141_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_sgpv_1d_jerk_v142_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_sgwp_5d_jerk_v143_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_pvz_1d_jerk_v144_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_pvrng_1d_jerk_v145_signal, "close", "high", "low"),
    _e(f04sr_f04_support_resistance_proximity_slh_60d_jerk_v146_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_sll_60d_jerk_v147_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_rexp_252d_jerk_v148_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_dya_252d_jerk_v149_signal, "closeadj"),
    _e(f04sr_f04_support_resistance_proximity_pvw_1d_jerk_v150_signal, "close", "high", "low"),
])

def _synthetic_inputs(n: int = 800, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    seg = n // 4
    rest = n - 3 * seg
    ret = np.concatenate([
        rng.normal(0.0012, 0.011, seg),
        rng.normal(-0.0005, 0.018, seg),
        rng.normal(-0.0010, 0.014, seg),
        rng.normal(0.0008, 0.012, rest),
    ])
    close = 50.0 * np.exp(np.cumsum(ret))
    adj_drift = rng.normal(0.0, 0.0003, size=n).cumsum()
    closeadj = close * np.exp(adj_drift)
    intraday = rng.normal(0.0, 0.008, size=n)
    open_ = close * np.exp(-intraday * 0.5)
    high = np.maximum(close, open_) * np.exp(np.abs(rng.normal(0.0, 0.006, size=n)))
    low = np.minimum(close, open_) * np.exp(-np.abs(rng.normal(0.0, 0.006, size=n)))
    volume = rng.lognormal(mean=13.0, sigma=0.6, size=n)
    idx = pd.RangeIndex(n)
    return pd.DataFrame({
        "open": pd.Series(open_, index=idx, dtype=float),
        "high": pd.Series(high, index=idx, dtype=float),
        "low": pd.Series(low, index=idx, dtype=float),
        "close": pd.Series(close, index=idx, dtype=float),
        "closeadj": pd.Series(closeadj, index=idx, dtype=float),
        "volume": pd.Series(volume, index=idx, dtype=float),
    })

def _self_test() -> None:
    df = _synthetic_inputs(n=800, seed=42)
    results: dict[str, pd.Series] = {}
    for name, entry in f04_support_resistance_proximity_jerk_001_150_REGISTRY.items():
        args = [df[col] for col in entry["inputs"]]
        out = entry["func"](*args)
        assert isinstance(out, pd.Series), f"{name}: not a Series"
        assert len(out) == len(df), f"{name}: length mismatch"
        clean = out.dropna()
        assert len(clean) > 0, f"{name}: all NaN"
        assert float(clean.std()) > 0.0 or clean.nunique() > 1, f"{name}: constant/all-zero"
        results[name] = out

    warm = 252
    coverage_ok = 0
    for ser in results.values():
        if ser.iloc[warm:].isna().mean() < 0.5:
            coverage_ok += 1
    frac = coverage_ok / len(results)
    assert frac >= 0.80, f"NaN-coverage too low: {frac:.2%} have <50% NaN after warm-up"

    aligned = pd.concat({n: results[n] for n in results}, axis=1).iloc[warm:]
    aligned = aligned.replace([np.inf,-np.inf],np.nan)
    corr = aligned.corr(min_periods=50).abs()
    np.fill_diagonal(corr.values, 0.0)
    max_corr = float(corr.max().max())
    if max_corr > 0.95 + 1e-9:
        s = corr.unstack().sort_values(ascending=False)
        s = s[s > 0.90].head(40)
        print("Top |corr| pairs > 0.90:")
        seen = set()
        for (a, b), v in s.items():
            if a < b and (a, b) not in seen:
                seen.add((a, b))
                print(f"  {a}  vs  {b}  ->  {v:.4f}")
    assert max_corr <= 0.95 + 1e-9, f"max pairwise |corr|={max_corr:.4f} exceeds 0.95"
    print(f"OK jerk_001_150: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")

if __name__ == "__main__":
    _self_test()
