"""f08_high_low_range_dynamics jerk features 001-150 (2nd derivative).
Each jerk = base - 2*base.shift(k) + base.shift(2k) where k follows the
ROC bracket of the base's primary window, varied within bracket. Base
formula re-inlined per feature. NaN policy: replace([inf,-inf], nan) at
the final return only. No helper for the second-difference operator.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# --- v001-v075 mirror base_001_075 ----------------------------------------


def f08hl_f08_high_low_range_dynamics_relrng_1d_jerk_v001_signal(high, low, close):
    rr = (high - low) / close.replace(0.0, np.nan)
    b = rr.rolling(5, min_periods=5).mean()
    return (b - 2.0 * b.shift(5) + b.shift(10)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_relrngmean_21d_jerk_v002_signal(high, low, close):
    r = (high - low) / close.replace(0.0, np.nan)
    b = r.rolling(21, min_periods=21).mean()
    return (b - 2.0 * b.shift(5) + b.shift(10)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_relrngmean_100d_jerk_v003_signal(high, low, closeadj):
    r = (high - low) / closeadj.replace(0.0, np.nan)
    b = r.rolling(100, min_periods=100).mean()
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_logrng_1d_jerk_v004_signal(high, low):
    b = np.log(high.replace(0.0, np.nan)) - np.log(low.replace(0.0, np.nan))
    return (b - 2.0 * b.shift(5) + b.shift(10)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_logrngmean_50d_jerk_v005_signal(high, low):
    lr = np.log(high.replace(0.0, np.nan)) - np.log(low.replace(0.0, np.nan))
    b = lr.rolling(50, min_periods=50).mean()
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_atrwild_14d_jerk_v006_signal(high, low, close):
    pc = close.shift(1)
    a = (high - low).abs(); bb = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, bb, c], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    b = atr / close.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(5) + b.shift(10)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_atrsma_50d_jerk_v007_signal(high, low, closeadj):
    pc = closeadj.shift(1)
    a = (high - low).abs(); bb = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, bb, c], axis=1).max(axis=1)
    atr = tr.rolling(50, min_periods=50).mean()
    b = atr / closeadj.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_atrrng_30d_jerk_v008_signal(high, low, closeadj):
    pc = closeadj.shift(1)
    a = (high - low).abs(); bb = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, bb, c], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 30.0, adjust=False, min_periods=30).mean()
    rng5 = (high - low).rolling(5, min_periods=5).mean()
    b = np.log(rng5 / atr.replace(0.0, np.nan))
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_normrng_20d_jerk_v009_signal(high, low):
    rng = high - low
    s3 = rng.rolling(3, min_periods=3).mean()
    s80 = rng.rolling(80, min_periods=80).mean()
    b = s3 / s80.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_trrngrat_1d_jerk_v010_signal(high, low, close):
    pc = close.shift(1)
    a = (high - low).abs(); bb = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, bb, c], axis=1).max(axis=1)
    rng = (high - low).replace(0.0, np.nan)
    b = tr / rng
    return (b - 2.0 * b.shift(5) + b.shift(10)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngexp_10d_jerk_v011_signal(high, low):
    rng = (high - low).replace(0.0, np.nan)
    sma = rng.rolling(10, min_periods=10).mean()
    b = np.log(rng / sma.replace(0.0, np.nan))
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngslope_20d_jerk_v012_signal(high, low):
    rng = high - low
    sma = rng.rolling(20, min_periods=20).mean()
    b = sma.diff(5) / sma.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(5) + b.shift(10)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngcurv_30d_jerk_v013_signal(high, low):
    rng = high - low
    sma = rng.rolling(30, min_periods=30).mean()
    cur = sma - 2.0 * sma.shift(5) + sma.shift(10)
    b = cur / sma.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_volofrng_30d_jerk_v014_signal(high, low):
    rng = high - low
    m = rng.rolling(30, min_periods=30).mean()
    s = rng.rolling(30, min_periods=30).std()
    b = s / m.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngac_30d_jerk_v015_signal(high, low):
    rng = (high - low).replace(0.0, np.nan)
    lr = np.log(rng)
    b = lr.rolling(30, min_periods=30).corr(lr.shift(1))
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngrnk_63d_jerk_v016_signal(high, low):
    rng = high - low
    sm = rng.rolling(21, min_periods=21).mean()
    b = sm.rolling(63, min_periods=40).rank(pct=True)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngzs_40d_jerk_v017_signal(high, low, closeadj):
    rng = (high - low).replace(0.0, np.nan)
    lr = np.log(rng)
    lc = np.log(closeadj.replace(0.0, np.nan))
    b = lr.rolling(40, min_periods=40).corr(lc)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngsk_60d_jerk_v018_signal(high, low):
    rng = high - low
    b = rng.rolling(60, min_periods=60).skew()
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngkur_60d_jerk_v019_signal(high, low):
    rng = high - low
    b = rng.rolling(60, min_periods=60).kurt()
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngmadr_30d_jerk_v020_signal(high, low):
    rng = high - low
    m = rng.rolling(30, min_periods=30).mean()
    mad = (rng - m).abs().rolling(30, min_periods=30).mean()
    sd = rng.rolling(30, min_periods=30).std()
    b = mad / sd.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_trrnk_50d_jerk_v021_signal(high, low, closeadj):
    pc = closeadj.shift(1)
    a = (high - low).abs(); bb = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, bb, c], axis=1).max(axis=1)
    b = tr.rolling(50, min_periods=30).rank(pct=True)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_trzs_30d_jerk_v022_signal(high, low, closeadj):
    pc = closeadj.shift(1)
    a = (high - low).abs(); bb = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, bb, c], axis=1).max(axis=1).replace(0.0, np.nan)
    rng = (high - low).replace(0.0, np.nan)
    b = np.log(tr) - np.log(rng)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_wildvssma_30d_jerk_v023_signal(high, low, closeadj):
    pc = closeadj.shift(1)
    a = (high - low).abs(); bb = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, bb, c], axis=1).max(axis=1)
    w = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    s = tr.rolling(30, min_periods=30).mean()
    b = np.log(w.replace(0.0, np.nan)) - np.log(s.replace(0.0, np.nan))
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngprior_1d_jerk_v024_signal(high, low):
    rng = (high - low).replace(0.0, np.nan)
    b = np.log(rng / rng.shift(1).replace(0.0, np.nan))
    return (b - 2.0 * b.shift(5) + b.shift(10)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngtmax_20d_jerk_v025_signal(high, low):
    rng = high - low
    mx = rng.rolling(20, min_periods=20).max().shift(1)
    b = rng / mx.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngtmin_20d_jerk_v026_signal(high, low):
    rng = (high - low).replace(0.0, np.nan)
    mn = rng.rolling(20, min_periods=20).min().shift(1)
    b = np.log(rng / mn.replace(0.0, np.nan))
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngstrkabv_30d_jerk_v027_signal(high, low):
    rng = high - low
    sma = rng.rolling(30, min_periods=30).mean()
    above = (rng > sma).astype(float).where(~sma.isna())
    grp = (above != above.shift()).cumsum()
    streak = above.groupby(grp).cumcount() + 1
    b = (streak * above).where(~sma.isna())
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_insidebr_1d_jerk_v028_signal(high, low):
    flag = (high < high.shift(1)) & (low > low.shift(1))
    b = flag.astype(float).where(~high.shift(1).isna() & ~low.shift(1).isna())
    return (b - 2.0 * b.shift(5) + b.shift(10)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_outsidebr_1d_jerk_v029_signal(high, low):
    flag = (high > high.shift(1)) & (low < low.shift(1))
    b = flag.astype(float).where(~high.shift(1).isna() & ~low.shift(1).isna())
    return (b - 2.0 * b.shift(5) + b.shift(10)).replace([np.inf, -np.inf], np.nan)






def f08hl_f08_high_low_range_dynamics_wr4_1d_jerk_v032_signal(high, low):
    rng = high - low
    mxrng = rng.rolling(4, min_periods=4).max()
    b = (rng >= mxrng - 1e-12).astype(float).where(~mxrng.isna())
    return (b - 2.0 * b.shift(5) + b.shift(10)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_wr7_1d_jerk_v033_signal(high, low):
    rng = high - low
    mxrng = rng.rolling(7, min_periods=7).max()
    b = (rng >= mxrng - 1e-12).astype(float).where(~mxrng.isna())
    return (b - 2.0 * b.shift(5) + b.shift(10)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_insidecnt_30d_jerk_v034_signal(high, low):
    flag = ((high < high.shift(1)) & (low > low.shift(1))).astype(float)
    b = flag.rolling(30, min_periods=30).sum()
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_outsidecnt_30d_jerk_v035_signal(high, low):
    flag = ((high > high.shift(1)) & (low < low.shift(1))).astype(float)
    b = flag.rolling(30, min_periods=30).sum()
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_nr7cnt_50d_jerk_v036_signal(high, low):
    rng = high - low
    minrng = rng.rolling(7, min_periods=7).min()
    flag = (rng <= minrng + 1e-12).astype(float).where(~minrng.isna())
    b = flag.rolling(50, min_periods=30).sum()
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_wr7cnt_50d_jerk_v037_signal(high, low):
    rng = high - low
    mxrng = rng.rolling(7, min_periods=7).max()
    flag = (rng >= mxrng - 1e-12).astype(float).where(~mxrng.isna())
    b = flag.rolling(50, min_periods=30).sum()
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_sqz_60d_jerk_v038_signal(high, low):
    rng = high - low
    sma = rng.rolling(10, min_periods=10).mean()
    b = sma.rolling(60, min_periods=40).rank(pct=True)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_xpan_40d_jerk_v039_signal(high, low):
    rng = high - low
    s10 = rng.rolling(10, min_periods=10).std()
    b = s10.diff(5) / s10.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngrat_short_jerk_v040_signal(high, low):
    rng = (high - low).replace(0.0, np.nan)
    s5 = rng.rolling(5, min_periods=5).mean()
    s21 = rng.rolling(21, min_periods=21).mean()
    bsig = np.log(s5.replace(0.0, np.nan)) - np.log(s21.replace(0.0, np.nan))
    b = bsig / bsig.abs().rolling(10, min_periods=10).mean().replace(0.0, np.nan)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngrat_long_jerk_v041_signal(high, low):
    rng = (high - low).replace(0.0, np.nan)
    s21 = rng.rolling(21, min_periods=21).mean()
    s100 = rng.rolling(100, min_periods=100).mean()
    b = np.log(s21.replace(0.0, np.nan)) - np.log(s100.replace(0.0, np.nan))
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngslpdiff_30d_jerk_v042_signal(high, low):
    rng = high - low
    s10 = rng.rolling(10, min_periods=10).mean()
    s30 = rng.rolling(30, min_periods=30).mean()
    short_slp = s10.diff(3) / s10.replace(0.0, np.nan)
    long_slp = s30.diff(10) / s30.replace(0.0, np.nan)
    b = short_slp - long_slp
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngsum_30d_jerk_v043_signal(high, low, closeadj):
    rng = high - low
    s = rng.rolling(30, min_periods=30).sum()
    b = s / closeadj.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngabsret_30d_jerk_v044_signal(high, low, closeadj):
    rng = (high - low) / closeadj.replace(0.0, np.nan)
    absret = closeadj.pct_change().abs()
    b = rng.rolling(30, min_periods=30).corr(absret)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_arcrng_30d_jerk_v045_signal(high, low):
    rng = high - low
    sma = rng.rolling(30, min_periods=30).mean()
    sd = rng.rolling(30, min_periods=30).std()
    x = sma.diff(10) / sd.replace(0.0, np.nan)
    b = np.arctan(x)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_tanhrng_50d_jerk_v046_signal(high, low):
    rng = high - low
    d = rng.diff(1)
    m = d.rolling(50, min_periods=50).mean()
    s = d.rolling(50, min_periods=50).std()
    z = (d - m) / s.replace(0.0, np.nan)
    b = np.tanh(z)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_pctb_rng_30d_jerk_v047_signal(high, low):
    rng = high - low
    s5 = rng.rolling(5, min_periods=5).mean()
    mn = s5.rolling(60, min_periods=40).min()
    mx = s5.rolling(60, min_periods=40).max()
    b = (s5 - mn) / (mx - mn).replace(0.0, np.nan)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngbody_10d_jerk_v048_signal(open, high, low, close):
    rng = high - low
    body = (close - open).abs()
    r = rng / body.replace(0.0, np.nan)
    rcl = r.clip(upper=20.0)
    b = rcl.rolling(10, min_periods=10).mean()
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_uprngfrac_15d_jerk_v049_signal(open, high, low, close):
    upper = high - np.maximum(open, close)
    rng = (high - low).replace(0.0, np.nan)
    r = upper / rng
    b = r.rolling(15, min_periods=15).mean()
    return (b - 2.0 * b.shift(5) + b.shift(10)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_lorngfrac_15d_jerk_v050_signal(open, high, low, close):
    lower = np.minimum(open, close) - low
    rng = (high - low).replace(0.0, np.nan)
    r = lower / rng
    b = r.rolling(15, min_periods=15).mean()
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngbuc_60d_jerk_v051_signal(high, low, closeadj):
    rng = (high - low) / closeadj.replace(0.0, np.nan)
    ret = closeadj.pct_change()
    rstd = ret.rolling(30, min_periods=30).std()
    rngm = rng.rolling(30, min_periods=30).mean()
    b = np.log(rngm.replace(0.0, np.nan)) - np.log(rstd.replace(0.0, np.nan))
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_sqzcnt_50d_jerk_v052_signal(high, low):
    rng = high - low
    p = rng.rolling(60, min_periods=40).rank(pct=True)
    flag = (p <= 0.25).astype(float).where(~p.isna())
    b = flag.rolling(50, min_periods=30).sum()
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_xpancnt_50d_jerk_v053_signal(high, low):
    rng = high - low
    p = rng.rolling(60, min_periods=40).rank(pct=True)
    flag = (p >= 0.75).astype(float).where(~p.isna())
    b = flag.rolling(50, min_periods=30).sum()
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngsign_21d_jerk_v054_signal(high, low):
    rng = high - low
    sma = rng.rolling(21, min_periods=21).mean()
    d = sma.diff(5)
    b = pd.Series(np.sign(d.values), index=d.index, dtype=float).where(~d.isna())
    return (b - 2.0 * b.shift(5) + b.shift(10)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngupcnt_50d_jerk_v055_signal(high, low):
    rng = high - low
    upd = (rng.diff() > 0.0).astype(float).where(~rng.diff().isna())
    b = upd.rolling(50, min_periods=30).sum()
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngac5_60d_jerk_v056_signal(high, low):
    rng = (high - low).replace(0.0, np.nan)
    lr = np.log(rng)
    b = lr.rolling(60, min_periods=60).corr(lr.shift(5))
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngcumchg_60d_jerk_v057_signal(high, low):
    rng = high - low
    s = rng.rolling(5, min_periods=5).mean()
    b = np.log(s / s.shift(60).replace(0.0, np.nan))
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngrs_60d_jerk_v058_signal(high, low):
    rng = (high - low).replace(0.0, np.nan)
    lr = np.log(rng)

    def _hurst(window):
        x = window - np.mean(window)
        cum = np.cumsum(x)
        rng_cum = float(np.max(cum) - np.min(cum))
        sd = float(np.std(window, ddof=0))
        if sd == 0.0 or rng_cum == 0.0:
            return np.nan
        return float(np.log(rng_cum / sd) / np.log(len(window)))

    b = lr.rolling(60, min_periods=60).apply(_hurst, raw=True)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_gapcontr_30d_jerk_v059_signal(high, low, closeadj):
    pc = closeadj.shift(1)
    a = (high - low).abs(); bb = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, bb, c], axis=1).max(axis=1).replace(0.0, np.nan)
    frac = (tr - (high - low)) / tr
    b = frac.rolling(30, min_periods=30).mean()
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngvolratio_30d_jerk_v060_signal(high, low):
    rng = high - low
    s10 = rng.rolling(10, min_periods=10).std()
    s30 = rng.rolling(30, min_periods=30).std()
    b = s10 / s30.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_hidiff_5d_jerk_v061_signal(high):
    r = high.diff(1) / high.shift(1).replace(0.0, np.nan)
    b = r.rolling(5, min_periods=5).mean()
    return (b - 2.0 * b.shift(5) + b.shift(10)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_lodiff_5d_jerk_v062_signal(high, low):
    hd = high.diff(1)
    ld = low.diff(1).abs()
    hm = hd.rolling(5, min_periods=5).mean()
    lm = ld.rolling(5, min_periods=5).mean()
    b = hm / lm.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(5) + b.shift(10)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_himhdif_20d_jerk_v063_signal(high, low):
    hd = high.diff(1)
    ld = low.diff(1)
    b = hd.rolling(20, min_periods=20).corr(ld)
    return (b - 2.0 * b.shift(5) + b.shift(10)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_insstrk_15d_jerk_v064_signal(high, low):
    rng = high - low
    cu = rng.rolling(30, min_periods=30).corr(high)
    cd = rng.rolling(30, min_periods=30).corr(low)
    b = cu - cd
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_daysnr7_40d_jerk_v065_signal(high, low):
    rng = high - low
    minrng = rng.rolling(7, min_periods=7).min()
    flag = (rng <= minrng + 1e-12).where(~minrng.isna())

    def _since(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return float(len(x))
        return float(len(x) - 1 - idx[-1])

    b = flag.rolling(40, min_periods=20).apply(_since, raw=True)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngcurvlog_60d_jerk_v066_signal(high, low):
    rng = (high - low).replace(0.0, np.nan)
    lr = np.log(rng)
    sma = lr.rolling(50, min_periods=50).mean()
    b = sma - 2.0 * sma.shift(10) + sma.shift(20)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngdispiqr_30d_jerk_v067_signal(high, low):
    rng = (high - low).replace(0.0, np.nan)
    lr = np.log(rng)
    q1 = lr.rolling(30, min_periods=30).quantile(0.25)
    q3 = lr.rolling(30, min_periods=30).quantile(0.75)
    med = lr.rolling(30, min_periods=30).median()
    b = (q3 - q1) / med.abs().replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngfromtmin_30d_jerk_v068_signal(high, low):
    rng = high - low
    win = 30

    def _argmin_age(x):
        i = int(np.argmin(x))
        return float(len(x) - 1 - i) / float(len(x) - 1)

    b = rng.rolling(win, min_periods=win).apply(_argmin_age, raw=True)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngfromtmax_30d_jerk_v069_signal(high, low):
    rng = high - low
    win = 30

    def _argmax_age(x):
        i = int(np.argmax(x))
        return float(len(x) - 1 - i) / float(len(x) - 1)

    b = rng.rolling(win, min_periods=win).apply(_argmax_age, raw=True)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngmad_50d_jerk_v070_signal(high, low, closeadj):
    r = (high - low) / closeadj.replace(0.0, np.nan)
    m = r.rolling(50, min_periods=50).mean()
    b = (r - m).abs().rolling(50, min_periods=50).mean()
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngavgcv_30d_jerk_v071_signal(high, low):
    rng = (high - low).replace(0.0, np.nan)
    lr = np.log(rng)
    b = lr.rolling(30, min_periods=30).corr(lr.shift(10))
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_ins3_1d_jerk_v072_signal(high, low):
    cur_in = (high < high.shift(1)) & (low > low.shift(1))
    prev_in = (high.shift(1) < high.shift(2)) & (low.shift(1) > low.shift(2))
    flag = cur_in & prev_in
    b = flag.astype(float).where(~high.shift(2).isna() & ~low.shift(2).isna())
    return (b - 2.0 * b.shift(5) + b.shift(10)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_out3_1d_jerk_v073_signal(high, low):
    cur_out = (high > high.shift(1)) & (low < low.shift(1))
    prev_out = (high.shift(1) > high.shift(2)) & (low.shift(1) < low.shift(2))
    flag = cur_out & prev_out
    b = flag.astype(float).where(~high.shift(2).isna() & ~low.shift(2).isna())
    return (b - 2.0 * b.shift(5) + b.shift(10)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngtopfrac_30d_jerk_v074_signal(high, low):
    rng = high - low

    def _topfrac(x):
        s = np.sort(x)[::-1]
        tot = float(np.sum(s))
        if tot == 0.0:
            return np.nan
        return float(np.sum(s[:3]) / tot)

    b = rng.rolling(30, min_periods=30).apply(_topfrac, raw=True)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngshiftcorr_40d_jerk_v075_signal(high, low):
    rng = (high - low).replace(0.0, np.nan)
    lr = np.log(rng)
    b = lr.rolling(40, min_periods=40).corr(lr.shift(3))
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


# --- v076-v150 mirror base_076_150 ----------------------------------------


def f08hl_f08_high_low_range_dynamics_atrwild_5d_jerk_v076_signal(high, low, close):
    pc = close.shift(1)
    a = (high - low).abs(); bb = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, bb, c], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 5.0, adjust=False, min_periods=5).mean()
    b = atr / close.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(5) + b.shift(10)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_atrlog_100d_jerk_v077_signal(high, low, closeadj):
    pc = closeadj.shift(1)
    a = (high - low).abs(); bb = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, bb, c], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 100.0, adjust=False, min_periods=100).mean()
    b = np.log(atr / closeadj.replace(0.0, np.nan))
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_atrshort_long_jerk_v078_signal(high, low, closeadj):
    pc = closeadj.shift(1)
    a = (high - low).abs(); bb = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, bb, c], axis=1).max(axis=1)
    a7 = tr.ewm(alpha=1.0 / 7.0, adjust=False, min_periods=7).mean()
    a50 = tr.ewm(alpha=1.0 / 50.0, adjust=False, min_periods=50).mean()
    b = np.log(a7.replace(0.0, np.nan)) - np.log(a50.replace(0.0, np.nan))
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_atrslope_30d_jerk_v079_signal(high, low, closeadj):
    pc = closeadj.shift(1)
    a = (high - low).abs(); bb = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, bb, c], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 30.0, adjust=False, min_periods=30).mean()
    b = atr.diff(10) / atr.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_atrcurv_50d_jerk_v080_signal(high, low, closeadj):
    pc = closeadj.shift(1)
    a = (high - low).abs(); bb = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, bb, c], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 50.0, adjust=False, min_periods=50).mean()
    la = np.log(atr.replace(0.0, np.nan))
    b = la - 2.0 * la.shift(10) + la.shift(20)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_trsk_60d_jerk_v081_signal(high, low, closeadj):
    pc = closeadj.shift(1)
    a = (high - low).abs(); bb = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, bb, c], axis=1).max(axis=1)
    b = tr.rolling(60, min_periods=60).skew()
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_trkur_60d_jerk_v082_signal(high, low, closeadj):
    pc = closeadj.shift(1)
    a = (high - low).abs(); bb = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, bb, c], axis=1).max(axis=1)
    md = tr.rolling(60, min_periods=60).median()
    mn = tr.rolling(60, min_periods=60).mean()
    b = md / mn.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_trmadr_40d_jerk_v083_signal(high, low, closeadj):
    pc = closeadj.shift(1)
    a = (high - low).abs(); bb = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, bb, c], axis=1).max(axis=1)
    m = tr.rolling(40, min_periods=40).mean()
    mad = (tr - m).abs().rolling(40, min_periods=40).mean()
    sd = tr.rolling(40, min_periods=40).std()
    b = mad / sd.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngdowncnt_50d_jerk_v084_signal(high, low):
    rng = high - low
    down = (rng.diff() < 0.0).astype(float).where(~rng.diff().isna())
    bsum = down.rolling(50, min_periods=30).sum()
    b = np.log1p(bsum) - np.log1p(50.0 - bsum)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngconseccnt_30d_jerk_v085_signal(high, low):
    rng = high - low
    d = rng.diff()
    cur = (d > 0.0).astype(float)
    prv = (d.shift(1) > 0.0).astype(float)
    pair = cur * prv
    b = pair.rolling(30, min_periods=30).sum()
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngent_60d_jerk_v086_signal(high, low):
    rng = (high - low).replace(0.0, np.nan)
    lr = np.log(rng)

    def _ent(x):
        if np.isnan(x).any():
            return np.nan
        lo = float(np.min(x)); hi = float(np.max(x))
        if hi - lo == 0.0:
            return np.nan
        edges = np.linspace(lo, hi, 9)
        bb = np.digitize(x, edges[1:-1])
        c = np.bincount(bb, minlength=8).astype(float)
        c = c[c > 0]
        p = c / c.sum()
        return float(-np.sum(p * np.log(p)))

    b = lr.rolling(60, min_periods=60).apply(_ent, raw=True)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngmom_10d_jerk_v087_signal(high, low):
    rng = (high - low).replace(0.0, np.nan)
    b = np.log(rng / rng.shift(10).replace(0.0, np.nan))
    return (b - 2.0 * b.shift(5) + b.shift(10)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngmom_50d_jerk_v088_signal(high, low, closeadj):
    rng = high - low
    sm = rng.rolling(10, min_periods=10).mean()
    b = np.log(sm.replace(0.0, np.nan) / sm.shift(50).replace(0.0, np.nan))
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_overlap_15d_jerk_v089_signal(high, low):
    h_prev = high.shift(1); l_prev = low.shift(1)
    overlap_top = np.minimum(high, h_prev)
    overlap_bot = np.maximum(low, l_prev)
    overlap = (overlap_top - overlap_bot).clip(lower=0.0)
    r = overlap / (high - low).replace(0.0, np.nan)
    b = r.rolling(15, min_periods=15).mean()
    return (b - 2.0 * b.shift(5) + b.shift(10)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_overlapstd_30d_jerk_v090_signal(high, low):
    h_prev = high.shift(1); l_prev = low.shift(1)
    overlap_top = np.minimum(high, h_prev)
    overlap_bot = np.maximum(low, l_prev)
    overlap = (overlap_top - overlap_bot).clip(lower=0.0)
    r = overlap / (high - low).replace(0.0, np.nan)
    b = r.rolling(30, min_periods=30).std()
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_hihigher_30d_jerk_v091_signal(high):
    flag = (high > high.shift(1)).astype(float).where(~high.shift(1).isna())
    b = flag.rolling(30, min_periods=30).mean()
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_lolower_30d_jerk_v092_signal(low):
    flag = (low < low.shift(1)).astype(float).where(~low.shift(1).isna())
    b = flag.rolling(30, min_periods=30).mean()
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_hhll_diff_30d_jerk_v093_signal(high, low):
    both = ((high > high.shift(1)) & (low > low.shift(1))).astype(float).where(~high.shift(1).isna())
    b = both.rolling(30, min_periods=30).sum()
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_trextqt_50d_jerk_v094_signal(high, low, closeadj):
    pc = closeadj.shift(1)
    a = (high - low).abs(); bb = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, bb, c], axis=1).max(axis=1)
    p90 = tr.rolling(50, min_periods=50).quantile(0.90)
    flag = (tr > p90).astype(float).where(~p90.isna())
    b = flag.rolling(50, min_periods=30).mean()
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngratrng_30d_jerk_v095_signal(high, low):
    rng = (high - low).replace(0.0, np.nan)
    r = np.log(rng / rng.shift(1).replace(0.0, np.nan))
    b = r.rolling(30, min_periods=30).mean()
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngenrm_30d_jerk_v096_signal(high, low):
    rng = high - low
    s1 = rng.rolling(30, min_periods=30).sum()
    s2 = (rng ** 2).rolling(30, min_periods=30).sum()
    b = (30.0 * s2) / (s1 ** 2).replace(0.0, np.nan)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngabsretr_30d_jerk_v097_signal(high, low, closeadj):
    rng = high - low
    aret = closeadj.diff().abs()
    r = rng / aret.replace(0.0, np.nan)
    rcl = r.clip(upper=20.0)
    b = rcl.rolling(30, min_periods=30).mean()
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_trrnk100_jerk_v098_signal(high, low, closeadj):
    pc = closeadj.shift(1)
    a = (high - low).abs(); bb = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, bb, c], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 20.0, adjust=False, min_periods=20).mean()
    b = atr.rolling(100, min_periods=60).rank(pct=True)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngsum_100d_jerk_v099_signal(high, low, closeadj):
    rng = high - low
    s = rng.rolling(100, min_periods=100).sum()
    b = np.log(s / (100.0 * closeadj.replace(0.0, np.nan)))
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngreg_50d_jerk_v100_signal(high, low):
    rng = (high - low).replace(0.0, np.nan)
    lr = np.log(rng)
    n = 50
    x = np.arange(n, dtype=float)
    x_mean = float(x.mean())
    xx = float(((x - x_mean) ** 2).sum())

    def _slp(y):
        if np.isnan(y).any():
            return np.nan
        y_mean = float(np.mean(y))
        s = float(np.sum((x - x_mean) * (y - y_mean))) / xx
        return s

    slope = lr.rolling(n, min_periods=n).apply(_slp, raw=True)
    basev = lr.rolling(n, min_periods=n).mean().abs().replace(0.0, np.nan)
    b = slope / basev
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngabvavg_60d_jerk_v101_signal(high, low):
    rng = high - low
    med = rng.rolling(60, min_periods=60).median()
    below = (rng < med).where(~med.isna())

    def _since(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return float(len(x))
        return float(len(x) - 1 - idx[-1])

    b = below.rolling(60, min_periods=60).apply(_since, raw=True)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngblwavg_60d_jerk_v102_signal(high, low):
    rng = high - low
    med = rng.rolling(60, min_periods=60).median()
    above = (rng > med).where(~med.isna())

    def _since(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return float(len(x))
        return float(len(x) - 1 - idx[-1])

    b = above.rolling(60, min_periods=60).apply(_since, raw=True)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_trshock_30d_jerk_v103_signal(high, low, closeadj):
    pc = closeadj.shift(1)
    a = (high - low).abs(); bb = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, bb, c], axis=1).max(axis=1).replace(0.0, np.nan)
    sm = tr.rolling(30, min_periods=30).mean()
    b = np.log(tr / sm.replace(0.0, np.nan))
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rnghigh_30d_jerk_v104_signal(high, low):
    rng = high - low
    b = rng.rolling(30, min_periods=30).corr(high)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rnglow_30d_jerk_v105_signal(high, low):
    rng = high - low
    b = rng.rolling(30, min_periods=30).corr(low)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_emarng_20d_jerk_v106_signal(high, low):
    rng = high - low
    e20 = rng.ewm(span=20, adjust=False, min_periods=20).mean()
    e50 = rng.ewm(span=50, adjust=False, min_periods=50).mean()
    b = (e20 / e50.replace(0.0, np.nan)) - 1.0
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngwinsor_40d_jerk_v107_signal(high, low):
    rng = high - low
    m = rng.rolling(40, min_periods=40).mean()
    md = rng.rolling(40, min_periods=40).median()
    b = m / md.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngfromtmin_60d_jerk_v108_signal(high, low):
    rng = (high - low).replace(0.0, np.nan)
    mn = rng.rolling(60, min_periods=40).min()
    b = np.log(rng / mn.replace(0.0, np.nan))
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngfromtmax_60d_jerk_v109_signal(high, low):
    rng = (high - low).replace(0.0, np.nan)
    mx = rng.rolling(60, min_periods=40).max()
    b = np.log(rng / mx.replace(0.0, np.nan))
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngbo_20d_jerk_v110_signal(high, low):
    rng = high - low
    mx = rng.rolling(20, min_periods=20).max().shift(1)
    b = (rng > mx).astype(float).where(~mx.isna())
    return (b - 2.0 * b.shift(5) + b.shift(10)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngbocnt_50d_jerk_v111_signal(high, low):
    rng = high - low
    mx = rng.rolling(20, min_periods=20).max().shift(1)
    bo = (rng > mx).astype(float).where(~mx.isna())
    b = bo.rolling(50, min_periods=30).sum()
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rnggini_30d_jerk_v112_signal(high, low):
    rng = high - low

    def _gini(x):
        m = float(np.median(x))
        mn = float(np.mean(x))
        if mn == 0.0:
            return np.nan
        return float(np.mean(np.abs(x - m)) / mn)

    b = rng.rolling(30, min_periods=30).apply(_gini, raw=True)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngzigzag_30d_jerk_v113_signal(high, low):
    rng = high - low
    d = rng.diff()
    s = np.sign(d)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    b = flip.rolling(30, min_periods=30).mean()
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_hivspc_20d_jerk_v114_signal(high, low, close):
    pc = close.shift(1)
    r = (high - pc) / pc.replace(0.0, np.nan)
    b = r.rolling(20, min_periods=20).mean()
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_lovspc_20d_jerk_v115_signal(high, low, close):
    pc = close.shift(1)
    r = (pc - low) / pc.replace(0.0, np.nan)
    b = r.rolling(20, min_periods=20).mean()
    return (b - 2.0 * b.shift(5) + b.shift(10)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngnetexp_50d_jerk_v116_signal(high, low):
    rng = (high - low).replace(0.0, np.nan)
    r = np.log(rng / rng.shift(1).replace(0.0, np.nan))
    b = r.rolling(50, min_periods=30).sum()
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_atr14sma14_jerk_v117_signal(high, low, close):
    pc = close.shift(1)
    a = (high - low).abs(); bb = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, bb, c], axis=1).max(axis=1)
    w = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    s = tr.rolling(14, min_periods=14).mean()
    b = np.log(w.replace(0.0, np.nan)) - np.log(s.replace(0.0, np.nan))
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngfourier_60d_jerk_v118_signal(high, low):
    rng = (high - low).replace(0.0, np.nan)
    lr = np.log(rng)

    def _f(x):
        if np.isnan(x).any():
            return np.nan
        x = x - x.mean()
        f = np.fft.rfft(x)
        p = np.abs(f) ** 2
        if p.sum() == 0.0:
            return np.nan
        return float(p[1] / p.sum())

    b = lr.rolling(60, min_periods=60).apply(_f, raw=True)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngtrcl_30d_jerk_v119_signal(high, low, close):
    rng = high - low
    cd = close.diff(1).abs()
    b = rng.rolling(30, min_periods=30).corr(cd)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_trrngrat_30d_jerk_v120_signal(high, low, close):
    pc = close.shift(1)
    a = (high - low).abs(); bb = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, bb, c], axis=1).max(axis=1)
    rng = (high - low).replace(0.0, np.nan)
    r = tr / rng
    b = r.rolling(30, min_periods=30).mean()
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_donchwid_50d_jerk_v121_signal(high, low, closeadj):
    hh = high.rolling(50, min_periods=50).max()
    ll = low.rolling(50, min_periods=50).min()
    b = (hh - ll) / closeadj.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)




def f08hl_f08_high_low_range_dynamics_rngdonchrat_30d_jerk_v123_signal(high, low):
    rng = (high - low).rolling(30, min_periods=30).mean()
    hh = high.rolling(30, min_periods=30).max()
    ll = low.rolling(30, min_periods=30).min()
    b = rng / (hh - ll).replace(0.0, np.nan)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_parkvol_20d_jerk_v124_signal(high, low):
    lr2 = (np.log(high.replace(0.0, np.nan)) - np.log(low.replace(0.0, np.nan))) ** 2
    b = np.sqrt(lr2.rolling(20, min_periods=20).mean() / (4.0 * np.log(2.0)))
    return (b - 2.0 * b.shift(5) + b.shift(10)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_parkvolratio_50d_jerk_v125_signal(high, low, closeadj):
    lr2 = (np.log(high.replace(0.0, np.nan)) - np.log(low.replace(0.0, np.nan))) ** 2
    p20 = np.sqrt(lr2.rolling(20, min_periods=20).mean() / (4.0 * np.log(2.0)))
    p50 = np.sqrt(lr2.rolling(50, min_periods=50).mean() / (4.0 * np.log(2.0)))
    b = np.log(p20.replace(0.0, np.nan) / p50.replace(0.0, np.nan))
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_gkvol_30d_jerk_v126_signal(open, high, low, close):
    lhl2 = (np.log(high.replace(0.0, np.nan)) - np.log(low.replace(0.0, np.nan))) ** 2
    lco2 = (np.log(close.replace(0.0, np.nan)) - np.log(open.replace(0.0, np.nan))) ** 2
    gk = 0.5 * lhl2 - (2.0 * np.log(2.0) - 1.0) * lco2
    gk_pos = gk.where(gk >= 0.0)
    b = np.sqrt(gk_pos.rolling(30, min_periods=30).mean())
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_insouttrend_60d_jerk_v127_signal(high, low):
    ins = ((high < high.shift(1)) & (low > low.shift(1))).astype(float)
    out_b = ((high > high.shift(1)) & (low < low.shift(1))).astype(float)
    b = ins.rolling(60, min_periods=40).mean() - out_b.rolling(60, min_periods=40).mean()
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngslowcyc_60d_jerk_v128_signal(high, low):
    rng = (high - low).replace(0.0, np.nan)
    lr = np.log(rng)

    def _se(x):
        if np.isnan(x).any():
            return np.nan
        x = x - x.mean()
        f = np.fft.rfft(x)
        p = np.abs(f) ** 2
        s = p.sum()
        if s == 0.0:
            return np.nan
        pn = p / s
        pn = pn[pn > 0]
        return float(-np.sum(pn * np.log(pn)))

    b = lr.rolling(60, min_periods=60).apply(_se, raw=True)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngslope_100d_jerk_v129_signal(high, low):
    rng = high - low
    sma = rng.rolling(100, min_periods=100).mean()
    b = sma.diff(21) / sma.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngslope_5d_jerk_v130_signal(high, low):
    rng = high - low
    sma = rng.rolling(5, min_periods=5).mean()
    b = sma.diff(3) / sma.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(5) + b.shift(10)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_trupcomp_30d_jerk_v131_signal(high, low, closeadj):
    pc = closeadj.shift(1)
    a = (high - low).abs(); bb = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, bb, c], axis=1).max(axis=1).replace(0.0, np.nan)
    upcomp = (high - pc).clip(lower=0.0)
    r = upcomp / tr
    b = r.rolling(30, min_periods=30).mean()
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_trdncomp_30d_jerk_v132_signal(high, low, closeadj):
    pc = closeadj.shift(1)
    a = (high - low).abs(); bb = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, bb, c], axis=1).max(axis=1).replace(0.0, np.nan)
    asym = ((high - pc).clip(lower=0.0) - (pc - low).clip(lower=0.0)) / tr
    b = asym.rolling(30, min_periods=30).std()
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_newhi_20d_jerk_v133_signal(high):
    win = 20
    mx = high.rolling(win, min_periods=win).max()
    flag = (high >= mx).where(~mx.isna())

    def _since(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return float(len(x))
        return float(len(x) - 1 - idx[-1])

    b = flag.rolling(win, min_periods=win).apply(_since, raw=True)
    return (b - 2.0 * b.shift(5) + b.shift(10)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_newlo_20d_jerk_v134_signal(low):
    win = 20
    mn = low.rolling(win, min_periods=win).min()
    flag = (low <= mn).where(~mn.isna())

    def _since(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return float(len(x))
        return float(len(x) - 1 - idx[-1])

    b = flag.rolling(win, min_periods=win).apply(_since, raw=True)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngratlog_25d_jerk_v135_signal(high, low):
    rng = (high - low).replace(0.0, np.nan)
    s10 = rng.rolling(10, min_periods=10).mean()
    s25 = rng.rolling(25, min_periods=25).mean()
    b = np.log(s10.replace(0.0, np.nan)) - np.log(s25.replace(0.0, np.nan))
    return (b - 2.0 * b.shift(5) + b.shift(10)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngratlog_long_jerk_v136_signal(high, low):
    rng = (high - low).replace(0.0, np.nan)
    s50 = rng.rolling(50, min_periods=50).mean()
    s200 = rng.rolling(200, min_periods=200).mean()
    b = np.log(s50.replace(0.0, np.nan)) - np.log(s200.replace(0.0, np.nan))
    return (b - 2.0 * b.shift(63) + b.shift(126)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngq90q10_50d_jerk_v137_signal(high, low):
    rng = (high - low).replace(0.0, np.nan)
    lr = np.log(rng)
    q90 = lr.rolling(50, min_periods=50).quantile(0.90)
    q10 = lr.rolling(50, min_periods=50).quantile(0.10)
    b = q90 - q10
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_hlratio_50d_jerk_v138_signal(high, low):
    r = (high / low.replace(0.0, np.nan)) - 1.0
    b = r.rolling(50, min_periods=50).mean()
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngtailcnt_60d_jerk_v139_signal(high, low):
    rng = (high - low).replace(0.0, np.nan)
    lr = np.log(rng)
    md = lr.rolling(60, min_periods=60).median()
    sd = lr.rolling(60, min_periods=60).std()
    thresh = md + sd
    flag = (lr > thresh).astype(float).where(~thresh.isna())
    b = flag.rolling(60, min_periods=40).sum()
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_parkvscclvol_60d_jerk_v140_signal(high, low, closeadj):
    lr2 = (np.log(high.replace(0.0, np.nan)) - np.log(low.replace(0.0, np.nan))) ** 2
    pv = np.sqrt(lr2.rolling(20, min_periods=20).mean() / (4.0 * np.log(2.0)))
    cret = np.log(closeadj.replace(0.0, np.nan)).diff()
    cv = cret.rolling(20, min_periods=20).std()
    b = pv / cv.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngnegcorr_40d_jerk_v141_signal(high, low):
    rng = (high - low).replace(0.0, np.nan)
    lr = np.log(rng)
    b = lr.rolling(40, min_periods=40).corr(lr.shift(20))
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rng3of5_jerk_v142_signal(high, low):
    rng = high - low
    flag = (rng > rng.shift(1)).astype(float).where(~rng.shift(1).isna())
    b = flag.rolling(5, min_periods=5).sum()
    return (b - 2.0 * b.shift(5) + b.shift(10)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_closecov_40d_jerk_v143_signal(open, high, low, close):
    pc = close.shift(1)
    rng = high - low
    nc = (close - pc).abs().replace(0.0, np.nan)
    r = (rng / nc).clip(upper=50.0)
    b = r.rolling(40, min_periods=40).mean()
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_hiltrkurt_30d_jerk_v144_signal(high, low):
    lr = np.log((high - low).replace(0.0, np.nan))
    sk = lr.rolling(30, min_periods=30).skew()
    kt = lr.rolling(30, min_periods=30).kurt()
    b = sk - kt / 3.0
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_atrnormdev_50d_jerk_v145_signal(high, low, closeadj):
    pc = closeadj.shift(1)
    a = (high - low).abs(); bb = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, bb, c], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 20.0, adjust=False, min_periods=20).mean()
    dev = (tr - atr) / atr.replace(0.0, np.nan)
    b = dev.rolling(5, min_periods=5).mean()
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_logrngwid_60d_jerk_v146_signal(high, low):
    rng = (high - low).replace(0.0, np.nan)
    lr = np.log(rng)
    b = lr.rolling(60, min_periods=60).max() - lr.rolling(60, min_periods=60).min()
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngclasif_30d_jerk_v147_signal(high, low):
    rng = high - low
    s7 = rng.rolling(7, min_periods=7).mean()
    s30 = rng.rolling(30, min_periods=30).mean()
    d = s7 - s30
    b = pd.Series(np.sign(d.values), index=d.index, dtype=float).where(~d.isna())
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngacrng_30d_jerk_v148_signal(high, low):
    rng = (high - low).replace(0.0, np.nan)
    lr = np.log(rng)
    b = lr.rolling(30, min_periods=30).corr(lr.shift(2))
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngslpsig_50d_jerk_v149_signal(high, low, closeadj):
    rng = high - low
    sma = rng.rolling(10, min_periods=10).mean()
    pos = (sma.diff(3) > 0.0).astype(float).where(~sma.diff(3).isna())
    b = pos.rolling(50, min_periods=30).mean()
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f08hl_f08_high_low_range_dynamics_rngfractal_60d_jerk_v150_signal(high, low):
    rng = high - low
    pl = rng.diff().abs().rolling(60, min_periods=60).sum()
    chord = rng.rolling(60, min_periods=60).max() - rng.rolling(60, min_periods=60).min()
    b = pl / chord.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


_FUNCS_JERK = [
    (f08hl_f08_high_low_range_dynamics_relrng_1d_jerk_v001_signal, ["high", "low", "close"]),
    (f08hl_f08_high_low_range_dynamics_relrngmean_21d_jerk_v002_signal, ["high", "low", "close"]),
    (f08hl_f08_high_low_range_dynamics_relrngmean_100d_jerk_v003_signal, ["high", "low", "closeadj"]),
    (f08hl_f08_high_low_range_dynamics_logrng_1d_jerk_v004_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_logrngmean_50d_jerk_v005_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_atrwild_14d_jerk_v006_signal, ["high", "low", "close"]),
    (f08hl_f08_high_low_range_dynamics_atrsma_50d_jerk_v007_signal, ["high", "low", "closeadj"]),
    (f08hl_f08_high_low_range_dynamics_atrrng_30d_jerk_v008_signal, ["high", "low", "closeadj"]),
    (f08hl_f08_high_low_range_dynamics_normrng_20d_jerk_v009_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_trrngrat_1d_jerk_v010_signal, ["high", "low", "close"]),
    (f08hl_f08_high_low_range_dynamics_rngexp_10d_jerk_v011_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngslope_20d_jerk_v012_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngcurv_30d_jerk_v013_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_volofrng_30d_jerk_v014_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngac_30d_jerk_v015_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngrnk_63d_jerk_v016_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngzs_40d_jerk_v017_signal, ["high", "low", "closeadj"]),
    (f08hl_f08_high_low_range_dynamics_rngsk_60d_jerk_v018_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngkur_60d_jerk_v019_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngmadr_30d_jerk_v020_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_trrnk_50d_jerk_v021_signal, ["high", "low", "closeadj"]),
    (f08hl_f08_high_low_range_dynamics_trzs_30d_jerk_v022_signal, ["high", "low", "closeadj"]),
    (f08hl_f08_high_low_range_dynamics_wildvssma_30d_jerk_v023_signal, ["high", "low", "closeadj"]),
    (f08hl_f08_high_low_range_dynamics_rngprior_1d_jerk_v024_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngtmax_20d_jerk_v025_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngtmin_20d_jerk_v026_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngstrkabv_30d_jerk_v027_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_insidebr_1d_jerk_v028_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_outsidebr_1d_jerk_v029_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_wr4_1d_jerk_v032_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_wr7_1d_jerk_v033_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_insidecnt_30d_jerk_v034_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_outsidecnt_30d_jerk_v035_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_nr7cnt_50d_jerk_v036_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_wr7cnt_50d_jerk_v037_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_sqz_60d_jerk_v038_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_xpan_40d_jerk_v039_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngrat_short_jerk_v040_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngrat_long_jerk_v041_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngslpdiff_30d_jerk_v042_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngsum_30d_jerk_v043_signal, ["high", "low", "closeadj"]),
    (f08hl_f08_high_low_range_dynamics_rngabsret_30d_jerk_v044_signal, ["high", "low", "closeadj"]),
    (f08hl_f08_high_low_range_dynamics_arcrng_30d_jerk_v045_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_tanhrng_50d_jerk_v046_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_pctb_rng_30d_jerk_v047_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngbody_10d_jerk_v048_signal, ["open", "high", "low", "close"]),
    (f08hl_f08_high_low_range_dynamics_uprngfrac_15d_jerk_v049_signal, ["open", "high", "low", "close"]),
    (f08hl_f08_high_low_range_dynamics_lorngfrac_15d_jerk_v050_signal, ["open", "high", "low", "close"]),
    (f08hl_f08_high_low_range_dynamics_rngbuc_60d_jerk_v051_signal, ["high", "low", "closeadj"]),
    (f08hl_f08_high_low_range_dynamics_sqzcnt_50d_jerk_v052_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_xpancnt_50d_jerk_v053_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngsign_21d_jerk_v054_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngupcnt_50d_jerk_v055_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngac5_60d_jerk_v056_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngcumchg_60d_jerk_v057_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngrs_60d_jerk_v058_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_gapcontr_30d_jerk_v059_signal, ["high", "low", "closeadj"]),
    (f08hl_f08_high_low_range_dynamics_rngvolratio_30d_jerk_v060_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_hidiff_5d_jerk_v061_signal, ["high"]),
    (f08hl_f08_high_low_range_dynamics_lodiff_5d_jerk_v062_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_himhdif_20d_jerk_v063_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_insstrk_15d_jerk_v064_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_daysnr7_40d_jerk_v065_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngcurvlog_60d_jerk_v066_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngdispiqr_30d_jerk_v067_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngfromtmin_30d_jerk_v068_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngfromtmax_30d_jerk_v069_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngmad_50d_jerk_v070_signal, ["high", "low", "closeadj"]),
    (f08hl_f08_high_low_range_dynamics_rngavgcv_30d_jerk_v071_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_ins3_1d_jerk_v072_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_out3_1d_jerk_v073_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngtopfrac_30d_jerk_v074_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngshiftcorr_40d_jerk_v075_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_atrwild_5d_jerk_v076_signal, ["high", "low", "close"]),
    (f08hl_f08_high_low_range_dynamics_atrlog_100d_jerk_v077_signal, ["high", "low", "closeadj"]),
    (f08hl_f08_high_low_range_dynamics_atrshort_long_jerk_v078_signal, ["high", "low", "closeadj"]),
    (f08hl_f08_high_low_range_dynamics_atrslope_30d_jerk_v079_signal, ["high", "low", "closeadj"]),
    (f08hl_f08_high_low_range_dynamics_atrcurv_50d_jerk_v080_signal, ["high", "low", "closeadj"]),
    (f08hl_f08_high_low_range_dynamics_trsk_60d_jerk_v081_signal, ["high", "low", "closeadj"]),
    (f08hl_f08_high_low_range_dynamics_trkur_60d_jerk_v082_signal, ["high", "low", "closeadj"]),
    (f08hl_f08_high_low_range_dynamics_trmadr_40d_jerk_v083_signal, ["high", "low", "closeadj"]),
    (f08hl_f08_high_low_range_dynamics_rngdowncnt_50d_jerk_v084_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngconseccnt_30d_jerk_v085_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngent_60d_jerk_v086_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngmom_10d_jerk_v087_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngmom_50d_jerk_v088_signal, ["high", "low", "closeadj"]),
    (f08hl_f08_high_low_range_dynamics_overlap_15d_jerk_v089_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_overlapstd_30d_jerk_v090_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_hihigher_30d_jerk_v091_signal, ["high"]),
    (f08hl_f08_high_low_range_dynamics_lolower_30d_jerk_v092_signal, ["low"]),
    (f08hl_f08_high_low_range_dynamics_hhll_diff_30d_jerk_v093_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_trextqt_50d_jerk_v094_signal, ["high", "low", "closeadj"]),
    (f08hl_f08_high_low_range_dynamics_rngratrng_30d_jerk_v095_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngenrm_30d_jerk_v096_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngabsretr_30d_jerk_v097_signal, ["high", "low", "closeadj"]),
    (f08hl_f08_high_low_range_dynamics_trrnk100_jerk_v098_signal, ["high", "low", "closeadj"]),
    (f08hl_f08_high_low_range_dynamics_rngsum_100d_jerk_v099_signal, ["high", "low", "closeadj"]),
    (f08hl_f08_high_low_range_dynamics_rngreg_50d_jerk_v100_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngabvavg_60d_jerk_v101_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngblwavg_60d_jerk_v102_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_trshock_30d_jerk_v103_signal, ["high", "low", "closeadj"]),
    (f08hl_f08_high_low_range_dynamics_rnghigh_30d_jerk_v104_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rnglow_30d_jerk_v105_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_emarng_20d_jerk_v106_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngwinsor_40d_jerk_v107_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngfromtmin_60d_jerk_v108_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngfromtmax_60d_jerk_v109_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngbo_20d_jerk_v110_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngbocnt_50d_jerk_v111_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rnggini_30d_jerk_v112_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngzigzag_30d_jerk_v113_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_hivspc_20d_jerk_v114_signal, ["high", "low", "close"]),
    (f08hl_f08_high_low_range_dynamics_lovspc_20d_jerk_v115_signal, ["high", "low", "close"]),
    (f08hl_f08_high_low_range_dynamics_rngnetexp_50d_jerk_v116_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_atr14sma14_jerk_v117_signal, ["high", "low", "close"]),
    (f08hl_f08_high_low_range_dynamics_rngfourier_60d_jerk_v118_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngtrcl_30d_jerk_v119_signal, ["high", "low", "close"]),
    (f08hl_f08_high_low_range_dynamics_trrngrat_30d_jerk_v120_signal, ["high", "low", "close"]),
    (f08hl_f08_high_low_range_dynamics_donchwid_50d_jerk_v121_signal, ["high", "low", "closeadj"]),
    (f08hl_f08_high_low_range_dynamics_rngdonchrat_30d_jerk_v123_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_parkvol_20d_jerk_v124_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_parkvolratio_50d_jerk_v125_signal, ["high", "low", "closeadj"]),
    (f08hl_f08_high_low_range_dynamics_gkvol_30d_jerk_v126_signal, ["open", "high", "low", "close"]),
    (f08hl_f08_high_low_range_dynamics_insouttrend_60d_jerk_v127_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngslowcyc_60d_jerk_v128_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngslope_100d_jerk_v129_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngslope_5d_jerk_v130_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_trupcomp_30d_jerk_v131_signal, ["high", "low", "closeadj"]),
    (f08hl_f08_high_low_range_dynamics_trdncomp_30d_jerk_v132_signal, ["high", "low", "closeadj"]),
    (f08hl_f08_high_low_range_dynamics_newhi_20d_jerk_v133_signal, ["high"]),
    (f08hl_f08_high_low_range_dynamics_newlo_20d_jerk_v134_signal, ["low"]),
    (f08hl_f08_high_low_range_dynamics_rngratlog_25d_jerk_v135_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngratlog_long_jerk_v136_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngq90q10_50d_jerk_v137_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_hlratio_50d_jerk_v138_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngtailcnt_60d_jerk_v139_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_parkvscclvol_60d_jerk_v140_signal, ["high", "low", "closeadj"]),
    (f08hl_f08_high_low_range_dynamics_rngnegcorr_40d_jerk_v141_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rng3of5_jerk_v142_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_closecov_40d_jerk_v143_signal, ["open", "high", "low", "close"]),
    (f08hl_f08_high_low_range_dynamics_hiltrkurt_30d_jerk_v144_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_atrnormdev_50d_jerk_v145_signal, ["high", "low", "closeadj"]),
    (f08hl_f08_high_low_range_dynamics_logrngwid_60d_jerk_v146_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngclasif_30d_jerk_v147_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngacrng_30d_jerk_v148_signal, ["high", "low"]),
    (f08hl_f08_high_low_range_dynamics_rngslpsig_50d_jerk_v149_signal, ["high", "low", "closeadj"]),
    (f08hl_f08_high_low_range_dynamics_rngfractal_60d_jerk_v150_signal, ["high", "low"]),
]


f08_high_low_range_dynamics_jerk_001_150_REGISTRY = {
    fn.__name__: {"inputs": inputs, "func": fn} for (fn, inputs) in _FUNCS_JERK
}


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------


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
    for name, entry in f08_high_low_range_dynamics_jerk_001_150_REGISTRY.items():
        args = [df[col] for col in entry["inputs"]]
        out = entry["func"](*args)
        assert isinstance(out, pd.Series), f"{name}: not a Series"
        assert len(out) == len(df), f"{name}: length mismatch"
        clean = out.dropna()
        assert len(clean) > 0, f"{name}: all NaN"
        assert float(clean.std()) > 0.0 or clean.nunique() > 1, f"{name}: constant/all-zero"
        results[name] = out

    warm = 252
    coverage_ok = sum(1 for s in results.values() if s.iloc[warm:].isna().mean() < 0.5)
    frac = coverage_ok / len(results)
    assert frac >= 0.80, f"NaN-coverage too low: {frac:.2%} have <50% NaN after warm-up"

    aligned = pd.concat({n: results[n] for n in results}, axis=1).iloc[warm:]
    aligned = aligned.replace([np.inf, -np.inf], np.nan)
    corr = aligned.corr(min_periods=50).abs()
    np.fill_diagonal(corr.values, 0.0)
    max_corr = float(corr.max().max())
    if max_corr > 0.95:
        print(f"FAILING max |corr| = {max_corr:.4f}. Top pairs:")
        for i, a in enumerate(corr.columns):
            for j, b in enumerate(corr.columns):
                if j > i and corr.iloc[i, j] > 0.94:
                    print(f"  {a}  vs  {b}  ->  {corr.iloc[i, j]:.4f}")
    assert max_corr <= 0.95 + 1e-9, f"max pairwise |corr|={max_corr:.4f} exceeds 0.95"
    print(f"OK jerk_001_150: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
