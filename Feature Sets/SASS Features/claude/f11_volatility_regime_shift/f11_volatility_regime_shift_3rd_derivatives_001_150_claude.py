import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _f11_ret(closeadj):
    return np.log(closeadj.replace(0, np.nan)).diff()


def _f11_vol(closeadj, w):
    r = _f11_ret(closeadj)
    return r.rolling(w, min_periods=max(2, w // 2)).std()


def _f11_bbwidth(closeadj, w):
    m = closeadj.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = closeadj.rolling(w, min_periods=max(2, w // 2)).std()
    return (4.0 * sd) / m.replace(0, np.nan)


def _f11_compress_ratio(closeadj, ws, wl):
    vs = _f11_vol(closeadj, ws)
    vl = _f11_vol(closeadj, wl)
    return vs / vl.replace(0, np.nan)


def _f11_volofvol(closeadj, wv, ws):
    v = _f11_vol(closeadj, wv)
    return v.rolling(ws, min_periods=max(2, ws // 2)).std() / v.rolling(ws, min_periods=max(2, ws // 2)).mean().replace(0, np.nan)


def _f11_truerange(high, low, closeadj):
    pc = closeadj.shift(1)
    a = (high - low)
    b = (high - pc).abs()
    c = (low - pc).abs()
    return pd.concat([a, b, c], axis=1).max(axis=1)


def _f11_atr(high, low, closeadj, w):
    tr = _f11_truerange(high, low, closeadj)
    return tr.rolling(w, min_periods=max(2, w // 2)).mean()


def _f11_parkinson(high, low, w):
    hl = np.log(high.replace(0, np.nan) / low.replace(0, np.nan)) ** 2
    return (hl.rolling(w, min_periods=max(2, w // 2)).mean() / (4.0 * np.log(2.0))) ** 0.5



def f11vr_f11_volatility_regime_shift_compr563_63d_jerk_v001_signal(closeadj):
    bse = _f11_compress_ratio(closeadj, 5, 63)
    f1 = bse.shift(5)
    f2 = bse.shift(10)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_compr2112_126d_jerk_v002_signal(closeadj):
    bse = _f11_compress_ratio(closeadj, 21, 126)
    f1 = bse.shift(21)
    f2 = bse.shift(42)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_pctbpos_21d_jerk_v003_signal(closeadj):
    m = _mean(closeadj, 21)
    sd = _std(closeadj, 21).replace(0, np.nan)
    bse = (closeadj - m) / (2.0 * sd)
    f1 = bse.shift(5)
    f2 = bse.shift(10)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_compr1012_126d_jerk_v004_signal(closeadj):
    bse = _f11_compress_ratio(closeadj, 10, 126)
    f1 = bse.shift(10)
    f2 = bse.shift(20)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_rngeff21_21d_jerk_v005_signal(high, low, closeadj):
    net = (closeadj - closeadj.shift(21)).abs()
    path = _f11_truerange(high, low, closeadj).rolling(21, min_periods=10).sum()
    bse = net / path.replace(0, np.nan)
    f1 = bse.shift(5)
    f2 = bse.shift(10)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_bbw21_21d_jerk_v006_signal(closeadj):
    bse = _f11_bbwidth(closeadj, 21)
    f1 = bse.shift(5)
    f2 = bse.shift(10)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_bbw63_63d_jerk_v007_signal(closeadj):
    bse = _f11_bbwidth(closeadj, 63)
    f1 = bse.shift(21)
    f2 = bse.shift(42)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_bbw126_126d_jerk_v008_signal(closeadj):
    bse = _f11_bbwidth(closeadj, 126)
    f1 = bse.shift(21)
    f2 = bse.shift(42)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_volacf_63d_jerk_v009_signal(closeadj):
    v = _f11_vol(closeadj, 10)
    dv = v - v.rolling(63, min_periods=21).mean()
    num = (dv * dv.shift(10)).rolling(63, min_periods=21).mean()
    den = (dv * dv).rolling(63, min_periods=21).mean()
    bse = num / den.replace(0, np.nan)
    f1 = bse.shift(21)
    f2 = bse.shift(42)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_bbwratio_63d_jerk_v010_signal(closeadj):
    bw = _f11_bbwidth(closeadj, 21)
    bse = bw / bw.rolling(63, min_periods=21).mean().replace(0, np.nan)
    f1 = bse.shift(10)
    f2 = bse.shift(20)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_vov63_63d_jerk_v011_signal(closeadj):
    bse = _f11_volofvol(closeadj, 21, 63)
    f1 = bse.shift(21)
    f2 = bse.shift(42)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_vov126_126d_jerk_v012_signal(closeadj):
    bse = _f11_volofvol(closeadj, 21, 126)
    f1 = bse.shift(21)
    f2 = bse.shift(42)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_vovshort_21d_jerk_v013_signal(closeadj):
    bse = _f11_volofvol(closeadj, 5, 21)
    f1 = bse.shift(5)
    f2 = bse.shift(10)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_voltermcurv_63d_jerk_v014_signal(closeadj):
    p5 = _rank(_f11_vol(closeadj, 5), 252)
    p21 = _rank(_f11_vol(closeadj, 21), 252)
    p63 = _rank(_f11_vol(closeadj, 63), 252)
    bse = p5 + p63 - 2.0 * p21
    f1 = bse.shift(21)
    f2 = bse.shift(42)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_volz504_504d_jerk_v015_signal(closeadj):
    bse = _z(_f11_vol(closeadj, 63), 504)
    f1 = bse.shift(63)
    f2 = bse.shift(126)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_rangeff63_63d_jerk_v016_signal(high, low, closeadj):
    trp = (_f11_truerange(high, low, closeadj) / closeadj.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    bse = trp.rolling(63, min_periods=21).max() / trp.rolling(63, min_periods=21).min().replace(0, np.nan)
    f1 = bse.shift(21)
    f2 = bse.shift(42)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_squeeze21_21d_jerk_v017_signal(closeadj):
    bse = _f11_bbwidth(closeadj, 21).rolling(252, min_periods=63).rank(pct=True) - 0.5
    f1 = bse.shift(10)
    f2 = bse.shift(20)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_squeeze63_63d_jerk_v018_signal(closeadj):
    bse = _f11_bbwidth(closeadj, 63).rolling(252, min_periods=63).rank(pct=True) - 0.5
    f1 = bse.shift(21)
    f2 = bse.shift(42)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_vol21_21d_jerk_v019_signal(closeadj):
    bse = _f11_vol(closeadj, 21)
    f1 = bse.shift(5)
    f2 = bse.shift(10)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_vol63_63d_jerk_v020_signal(closeadj):
    bse = _f11_vol(closeadj, 63)
    f1 = bse.shift(21)
    f2 = bse.shift(42)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_bandtag_63d_jerk_v021_signal(closeadj):
    m = _mean(closeadj, 21)
    sd = _std(closeadj, 21).replace(0, np.nan)
    pctb = (closeadj - m) / (2.0 * sd)
    bse = (pctb.abs() - 1.0).clip(lower=0).rolling(63, min_periods=21).mean()
    f1 = bse.shift(21)
    f2 = bse.shift(42)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_vol126_126d_jerk_v022_signal(closeadj):
    bse = _f11_vol(closeadj, 126)
    f1 = bse.shift(21)
    f2 = bse.shift(42)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_atrp21_21d_jerk_v023_signal(high, low, closeadj):
    bse = _f11_atr(high, low, closeadj, 21) / closeadj.replace(0, np.nan)
    f1 = bse.shift(5)
    f2 = bse.shift(10)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_atrp63_63d_jerk_v024_signal(high, low, closeadj):
    bse = _f11_atr(high, low, closeadj, 63) / closeadj.replace(0, np.nan)
    f1 = bse.shift(21)
    f2 = bse.shift(42)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_atrcompr_63d_jerk_v025_signal(high, low, closeadj):
    a_s = _f11_atr(high, low, closeadj, 5)
    a_l = _f11_atr(high, low, closeadj, 63)
    bse = a_s / a_l.replace(0, np.nan)
    f1 = bse.shift(5)
    f2 = bse.shift(10)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_pk21_21d_jerk_v026_signal(high, low):
    bse = _f11_parkinson(high, low, 21)
    f1 = bse.shift(5)
    f2 = bse.shift(10)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_pk63_63d_jerk_v027_signal(high, low):
    bse = _f11_parkinson(high, low, 63)
    f1 = bse.shift(21)
    f2 = bse.shift(42)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_pkz_252d_jerk_v028_signal(high, low):
    bse = _z(_f11_parkinson(high, low, 21), 252)
    f1 = bse.shift(21)
    f2 = bse.shift(42)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_bbwz_504d_jerk_v029_signal(closeadj):
    bse = _z(_f11_bbwidth(closeadj, 63), 504)
    f1 = bse.shift(63)
    f2 = bse.shift(126)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_atrz_252d_jerk_v030_signal(high, low, closeadj):
    bse = _z(_f11_atr(high, low, closeadj, 21) / closeadj.replace(0, np.nan), 252)
    f1 = bse.shift(21)
    f2 = bse.shift(42)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_bbwenergy_63d_jerk_v031_signal(closeadj):
    bw = _f11_bbwidth(closeadj, 21)
    vs = bw.rolling(21, min_periods=10).var()
    vl = bw.rolling(126, min_periods=42).var()
    bse = vs / vl.replace(0, np.nan)
    f1 = bse.shift(21)
    f2 = bse.shift(42)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_volcurv_63d_jerk_v032_signal(closeadj):
    v5 = _f11_vol(closeadj, 5)
    v21 = _f11_vol(closeadj, 21)
    v63 = _f11_vol(closeadj, 63)
    bse = (v5 - 2.0 * v21 + v63) / v21.replace(0, np.nan)
    f1 = bse.shift(10)
    f2 = bse.shift(20)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_volasym_63d_jerk_v033_signal(closeadj):
    r = _f11_ret(closeadj)
    uv = r.where(r > 0).rolling(63, min_periods=21).std()
    dv = r.where(r < 0).rolling(63, min_periods=21).std()
    bse = (uv - dv) / (uv + dv).replace(0, np.nan)
    f1 = bse.shift(21)
    f2 = bse.shift(42)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_rngexp_63d_jerk_v034_signal(closeadj):
    rng5 = (_rmax(closeadj, 5) - _rmin(closeadj, 5)) / closeadj.replace(0, np.nan)
    bse = rng5 / rng5.rolling(63, min_periods=21).mean().replace(0, np.nan)
    f1 = bse.shift(5)
    f2 = bse.shift(10)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_bbwfrommax_252d_jerk_v035_signal(closeadj):
    bw = _f11_bbwidth(closeadj, 21)
    bse = bw / bw.rolling(252, min_periods=63).max().replace(0, np.nan)
    f1 = bse.shift(21)
    f2 = bse.shift(42)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_volhyst_252d_jerk_v036_signal(closeadj):
    pf = _rank(_f11_vol(closeadj, 10), 252)
    ps = _rank(_f11_vol(closeadj, 63), 252)
    bse = pf - ps
    f1 = bse.shift(21)
    f2 = bse.shift(42)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_pctbdisp_63d_jerk_v037_signal(closeadj):
    m = _mean(closeadj, 21)
    sd = _std(closeadj, 21).replace(0, np.nan)
    pctb = (closeadj - m) / (2.0 * sd)
    bse = pctb.rolling(63, min_periods=21).std()
    f1 = bse.shift(21)
    f2 = bse.shift(42)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_voltilt_252d_jerk_v038_signal(closeadj):
    v63 = _f11_vol(closeadj, 63)
    bse = v63.rolling(252, min_periods=63).rank(pct=True) - v63.rolling(504, min_periods=126).rank(pct=True)
    f1 = bse.shift(21)
    f2 = bse.shift(42)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_bbwspread_63d_jerk_v039_signal(closeadj):
    b21 = _f11_bbwidth(closeadj, 21)
    b63 = _f11_bbwidth(closeadj, 63)
    bse = (b21 - b63) / b63.replace(0, np.nan)
    f1 = bse.shift(10)
    f2 = bse.shift(20)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_pkrvgap_21d_jerk_v040_signal(high, low, closeadj):
    bse = _f11_parkinson(high, low, 21) - _f11_vol(closeadj, 21)
    f1 = bse.shift(5)
    f2 = bse.shift(10)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_downvol_21d_jerk_v041_signal(closeadj):
    r = _f11_ret(closeadj)
    bse = r.where(r < 0).rolling(21, min_periods=8).std()
    f1 = bse.shift(5)
    f2 = bse.shift(10)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_upvol_21d_jerk_v042_signal(closeadj):
    r = _f11_ret(closeadj)
    bse = r.where(r > 0).rolling(21, min_periods=8).std()
    f1 = bse.shift(5)
    f2 = bse.shift(10)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_bbwdonch_21d_jerk_v043_signal(closeadj):
    bw = _f11_bbwidth(closeadj, 21)
    donch = (_rmax(closeadj, 21) - _rmin(closeadj, 21)) / _mean(closeadj, 21).replace(0, np.nan)
    bse = bw / donch.replace(0, np.nan)
    f1 = bse.shift(10)
    f2 = bse.shift(20)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_trp_21d_jerk_v044_signal(high, low, closeadj):
    bse = (_f11_truerange(high, low, closeadj) / closeadj.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    f1 = bse.shift(5)
    f2 = bse.shift(10)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_rsest_21d_jerk_v045_signal(high, low, closeadj):
    hc = np.log(high.replace(0, np.nan) / closeadj.replace(0, np.nan))
    lc = np.log(low.replace(0, np.nan) / closeadj.replace(0, np.nan))
    ho = np.log(high.replace(0, np.nan) / closeadj.shift(1).replace(0, np.nan))
    lo = np.log(low.replace(0, np.nan) / closeadj.shift(1).replace(0, np.nan))
    bse = (hc * ho + lc * lo).rolling(21, min_periods=10).mean().clip(lower=0) ** 0.5
    f1 = bse.shift(5)
    f2 = bse.shift(10)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_volregslope_63d_jerk_v046_signal(closeadj):
    v = _f11_vol(closeadj, 21)
    x = pd.Series(np.arange(len(v)), index=v.index, dtype=float)
    mx = x.rolling(63, min_periods=21).mean()
    my = v.rolling(63, min_periods=21).mean()
    cov = (x * v).rolling(63, min_periods=21).mean() - mx * my
    varx = (x * x).rolling(63, min_periods=21).mean() - mx * mx
    bse = (cov / varx.replace(0, np.nan)) / my.replace(0, np.nan)
    f1 = bse.shift(21)
    f2 = bse.shift(42)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_volscale_63d_jerk_v047_signal(closeadj):
    r1 = _f11_ret(closeadj)
    r5 = np.log(closeadj.replace(0, np.nan)).diff(5)
    v1 = r1.rolling(63, min_periods=21).std() * np.sqrt(5.0)
    v5 = r5.rolling(63, min_periods=21).std()
    bse = v5 / v1.replace(0, np.nan)
    f1 = bse.shift(21)
    f2 = bse.shift(42)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_bbwjump_21d_jerk_v048_signal(closeadj):
    bw = _f11_bbwidth(closeadj, 21)
    jump = bw.diff() / bw.shift(1).replace(0, np.nan)
    bse = jump.rolling(21, min_periods=10).max()
    f1 = bse.shift(5)
    f2 = bse.shift(10)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_downratio_126d_jerk_v049_signal(closeadj):
    r = _f11_ret(closeadj)
    dn = r.where(r < 0)
    ds = dn.rolling(21, min_periods=8).std()
    dl = dn.rolling(126, min_periods=42).std()
    bse = ds / dl.replace(0, np.nan)
    f1 = bse.shift(21)
    f2 = bse.shift(42)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_volamp_252d_jerk_v050_signal(closeadj):
    v = _f11_vol(closeadj, 21)
    amp = (v.rolling(252, min_periods=63).max() - v.rolling(252, min_periods=63).min())
    bse = amp / v.rolling(252, min_periods=63).mean().replace(0, np.nan)
    f1 = bse.shift(21)
    f2 = bse.shift(42)
    jrk = bse - 2.0 * f1 + f2
    sc = (bse.abs() + 2.0 * f1.abs() + f2.abs()).replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_compr563_63d_jerk_v051_signal(closeadj):
    bse = _f11_compress_ratio(closeadj, 5, 63)
    der = bse.diff(5)
    jrk = der.diff(5)
    result = _z(jrk, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_compr2112_126d_jerk_v052_signal(closeadj):
    bse = _f11_compress_ratio(closeadj, 21, 126)
    der = bse.diff(21)
    jrk = der.diff(21)
    result = _z(jrk, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_pctbpos_21d_jerk_v053_signal(closeadj):
    m = _mean(closeadj, 21)
    sd = _std(closeadj, 21).replace(0, np.nan)
    bse = (closeadj - m) / (2.0 * sd)
    der = bse.diff(5)
    jrk = der.diff(5)
    result = _z(jrk, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_compr1012_126d_jerk_v054_signal(closeadj):
    bse = _f11_compress_ratio(closeadj, 10, 126)
    der = bse.diff(10)
    jrk = der.diff(10)
    result = _z(jrk, 20)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_rngeff21_21d_jerk_v055_signal(high, low, closeadj):
    net = (closeadj - closeadj.shift(21)).abs()
    path = _f11_truerange(high, low, closeadj).rolling(21, min_periods=10).sum()
    bse = net / path.replace(0, np.nan)
    der = bse.diff(5)
    jrk = der.diff(5)
    result = _z(jrk, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_bbw21_21d_jerk_v056_signal(closeadj):
    bse = _f11_bbwidth(closeadj, 21)
    der = bse.diff(5)
    jrk = der.diff(5)
    result = _z(jrk, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_bbw63_63d_jerk_v057_signal(closeadj):
    bse = _f11_bbwidth(closeadj, 63)
    der = bse.diff(21)
    jrk = der.diff(21)
    result = _z(jrk, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_bbw126_126d_jerk_v058_signal(closeadj):
    bse = _f11_bbwidth(closeadj, 126)
    der = bse.diff(21)
    jrk = der.diff(21)
    result = _z(jrk, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_volacf_63d_jerk_v059_signal(closeadj):
    v = _f11_vol(closeadj, 10)
    dv = v - v.rolling(63, min_periods=21).mean()
    num = (dv * dv.shift(10)).rolling(63, min_periods=21).mean()
    den = (dv * dv).rolling(63, min_periods=21).mean()
    bse = num / den.replace(0, np.nan)
    der = bse.diff(21)
    jrk = der.diff(21)
    result = _z(jrk, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_bbwratio_63d_jerk_v060_signal(closeadj):
    bw = _f11_bbwidth(closeadj, 21)
    bse = bw / bw.rolling(63, min_periods=21).mean().replace(0, np.nan)
    der = bse.diff(10)
    jrk = der.diff(10)
    result = _z(jrk, 20)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_vov63_63d_jerk_v061_signal(closeadj):
    bse = _f11_volofvol(closeadj, 21, 63)
    der = bse.diff(21)
    jrk = der.diff(21)
    result = _z(jrk, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_vov126_126d_jerk_v062_signal(closeadj):
    bse = _f11_volofvol(closeadj, 21, 126)
    der = bse.diff(21)
    jrk = der.diff(21)
    result = _z(jrk, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_vovshort_21d_jerk_v063_signal(closeadj):
    bse = _f11_volofvol(closeadj, 5, 21)
    der = bse.diff(5)
    jrk = der.diff(5)
    result = _z(jrk, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_voltermcurv_63d_jerk_v064_signal(closeadj):
    p5 = _rank(_f11_vol(closeadj, 5), 252)
    p21 = _rank(_f11_vol(closeadj, 21), 252)
    p63 = _rank(_f11_vol(closeadj, 63), 252)
    bse = p5 + p63 - 2.0 * p21
    der = bse.diff(21)
    jrk = der.diff(21)
    result = _z(jrk, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_volz504_504d_jerk_v065_signal(closeadj):
    bse = _z(_f11_vol(closeadj, 63), 504)
    der = bse.diff(63)
    jrk = der.diff(63)
    result = _z(jrk, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_rangeff63_63d_jerk_v066_signal(high, low, closeadj):
    trp = (_f11_truerange(high, low, closeadj) / closeadj.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    bse = trp.rolling(63, min_periods=21).max() / trp.rolling(63, min_periods=21).min().replace(0, np.nan)
    der = bse.diff(21)
    jrk = der.diff(21)
    result = _z(jrk, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_squeeze21_21d_jerk_v067_signal(closeadj):
    bse = _f11_bbwidth(closeadj, 21).rolling(252, min_periods=63).rank(pct=True) - 0.5
    der = bse.diff(10)
    jrk = der.diff(10)
    result = _z(jrk, 20)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_squeeze63_63d_jerk_v068_signal(closeadj):
    bse = _f11_bbwidth(closeadj, 63).rolling(252, min_periods=63).rank(pct=True) - 0.5
    der = bse.diff(21)
    jrk = der.diff(21)
    result = _z(jrk, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_vol21_21d_jerk_v069_signal(closeadj):
    bse = _f11_vol(closeadj, 21)
    der = bse.diff(5)
    jrk = der.diff(5)
    result = _z(jrk, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_vol63_63d_jerk_v070_signal(closeadj):
    bse = _f11_vol(closeadj, 63)
    der = bse.diff(21)
    jrk = der.diff(21)
    result = _z(jrk, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_bandtag_63d_jerk_v071_signal(closeadj):
    m = _mean(closeadj, 21)
    sd = _std(closeadj, 21).replace(0, np.nan)
    pctb = (closeadj - m) / (2.0 * sd)
    bse = (pctb.abs() - 1.0).clip(lower=0).rolling(63, min_periods=21).mean()
    der = bse.diff(21)
    jrk = der.diff(21)
    result = _z(jrk, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_vol126_126d_jerk_v072_signal(closeadj):
    bse = _f11_vol(closeadj, 126)
    der = bse.diff(21)
    jrk = der.diff(21)
    result = _z(jrk, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_atrp21_21d_jerk_v073_signal(high, low, closeadj):
    bse = _f11_atr(high, low, closeadj, 21) / closeadj.replace(0, np.nan)
    der = bse.diff(5)
    jrk = der.diff(5)
    result = _z(jrk, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_atrp63_63d_jerk_v074_signal(high, low, closeadj):
    bse = _f11_atr(high, low, closeadj, 63) / closeadj.replace(0, np.nan)
    der = bse.diff(21)
    jrk = der.diff(21)
    result = _z(jrk, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_atrcompr_63d_jerk_v075_signal(high, low, closeadj):
    a_s = _f11_atr(high, low, closeadj, 5)
    a_l = _f11_atr(high, low, closeadj, 63)
    bse = a_s / a_l.replace(0, np.nan)
    der = bse.diff(5)
    jrk = der.diff(5)
    result = _z(jrk, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_pk21_21d_jerk_v076_signal(high, low):
    bse = _f11_parkinson(high, low, 21)
    der = bse.diff(5)
    jrk = der.diff(5)
    result = _z(jrk, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_pk63_63d_jerk_v077_signal(high, low):
    bse = _f11_parkinson(high, low, 63)
    der = bse.diff(21)
    jrk = der.diff(21)
    result = _z(jrk, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_pkz_252d_jerk_v078_signal(high, low):
    bse = _z(_f11_parkinson(high, low, 21), 252)
    der = bse.diff(21)
    jrk = der.diff(21)
    result = _z(jrk, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_bbwz_504d_jerk_v079_signal(closeadj):
    bse = _z(_f11_bbwidth(closeadj, 63), 504)
    der = bse.diff(63)
    jrk = der.diff(63)
    result = _z(jrk, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_atrz_252d_jerk_v080_signal(high, low, closeadj):
    bse = _z(_f11_atr(high, low, closeadj, 21) / closeadj.replace(0, np.nan), 252)
    der = bse.diff(21)
    jrk = der.diff(21)
    result = _z(jrk, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_bbwenergy_63d_jerk_v081_signal(closeadj):
    bw = _f11_bbwidth(closeadj, 21)
    vs = bw.rolling(21, min_periods=10).var()
    vl = bw.rolling(126, min_periods=42).var()
    bse = vs / vl.replace(0, np.nan)
    der = bse.diff(21)
    jrk = der.diff(21)
    result = _z(jrk, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_volcurv_63d_jerk_v082_signal(closeadj):
    v5 = _f11_vol(closeadj, 5)
    v21 = _f11_vol(closeadj, 21)
    v63 = _f11_vol(closeadj, 63)
    bse = (v5 - 2.0 * v21 + v63) / v21.replace(0, np.nan)
    der = bse.diff(10)
    jrk = der.diff(10)
    result = _z(jrk, 20)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_volasym_63d_jerk_v083_signal(closeadj):
    r = _f11_ret(closeadj)
    uv = r.where(r > 0).rolling(63, min_periods=21).std()
    dv = r.where(r < 0).rolling(63, min_periods=21).std()
    bse = (uv - dv) / (uv + dv).replace(0, np.nan)
    der = bse.diff(21)
    jrk = der.diff(21)
    result = _z(jrk, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_rngexp_63d_jerk_v084_signal(closeadj):
    rng5 = (_rmax(closeadj, 5) - _rmin(closeadj, 5)) / closeadj.replace(0, np.nan)
    bse = rng5 / rng5.rolling(63, min_periods=21).mean().replace(0, np.nan)
    der = bse.diff(5)
    jrk = der.diff(5)
    result = _z(jrk, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_bbwfrommax_252d_jerk_v085_signal(closeadj):
    bw = _f11_bbwidth(closeadj, 21)
    bse = bw / bw.rolling(252, min_periods=63).max().replace(0, np.nan)
    der = bse.diff(21)
    jrk = der.diff(21)
    result = _z(jrk, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_volhyst_252d_jerk_v086_signal(closeadj):
    pf = _rank(_f11_vol(closeadj, 10), 252)
    ps = _rank(_f11_vol(closeadj, 63), 252)
    bse = pf - ps
    der = bse.diff(21)
    jrk = der.diff(21)
    result = _z(jrk, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_pctbdisp_63d_jerk_v087_signal(closeadj):
    m = _mean(closeadj, 21)
    sd = _std(closeadj, 21).replace(0, np.nan)
    pctb = (closeadj - m) / (2.0 * sd)
    bse = pctb.rolling(63, min_periods=21).std()
    der = bse.diff(21)
    jrk = der.diff(21)
    result = _z(jrk, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_voltilt_252d_jerk_v088_signal(closeadj):
    v63 = _f11_vol(closeadj, 63)
    bse = v63.rolling(252, min_periods=63).rank(pct=True) - v63.rolling(504, min_periods=126).rank(pct=True)
    der = bse.diff(21)
    jrk = der.diff(21)
    result = _z(jrk, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_bbwspread_63d_jerk_v089_signal(closeadj):
    b21 = _f11_bbwidth(closeadj, 21)
    b63 = _f11_bbwidth(closeadj, 63)
    bse = (b21 - b63) / b63.replace(0, np.nan)
    der = bse.diff(10)
    jrk = der.diff(10)
    result = _z(jrk, 20)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_pkrvgap_21d_jerk_v090_signal(high, low, closeadj):
    bse = _f11_parkinson(high, low, 21) - _f11_vol(closeadj, 21)
    der = bse.diff(5)
    jrk = der.diff(5)
    result = _z(jrk, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_downvol_21d_jerk_v091_signal(closeadj):
    r = _f11_ret(closeadj)
    bse = r.where(r < 0).rolling(21, min_periods=8).std()
    der = bse.diff(5)
    jrk = der.diff(5)
    result = _z(jrk, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_upvol_21d_jerk_v092_signal(closeadj):
    r = _f11_ret(closeadj)
    bse = r.where(r > 0).rolling(21, min_periods=8).std()
    der = bse.diff(5)
    jrk = der.diff(5)
    result = _z(jrk, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_bbwdonch_21d_jerk_v093_signal(closeadj):
    bw = _f11_bbwidth(closeadj, 21)
    donch = (_rmax(closeadj, 21) - _rmin(closeadj, 21)) / _mean(closeadj, 21).replace(0, np.nan)
    bse = bw / donch.replace(0, np.nan)
    der = bse.diff(10)
    jrk = der.diff(10)
    result = _z(jrk, 20)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_trp_21d_jerk_v094_signal(high, low, closeadj):
    bse = (_f11_truerange(high, low, closeadj) / closeadj.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    der = bse.diff(5)
    jrk = der.diff(5)
    result = _z(jrk, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_rsest_21d_jerk_v095_signal(high, low, closeadj):
    hc = np.log(high.replace(0, np.nan) / closeadj.replace(0, np.nan))
    lc = np.log(low.replace(0, np.nan) / closeadj.replace(0, np.nan))
    ho = np.log(high.replace(0, np.nan) / closeadj.shift(1).replace(0, np.nan))
    lo = np.log(low.replace(0, np.nan) / closeadj.shift(1).replace(0, np.nan))
    bse = (hc * ho + lc * lo).rolling(21, min_periods=10).mean().clip(lower=0) ** 0.5
    der = bse.diff(5)
    jrk = der.diff(5)
    result = _z(jrk, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_volregslope_63d_jerk_v096_signal(closeadj):
    v = _f11_vol(closeadj, 21)
    x = pd.Series(np.arange(len(v)), index=v.index, dtype=float)
    mx = x.rolling(63, min_periods=21).mean()
    my = v.rolling(63, min_periods=21).mean()
    cov = (x * v).rolling(63, min_periods=21).mean() - mx * my
    varx = (x * x).rolling(63, min_periods=21).mean() - mx * mx
    bse = (cov / varx.replace(0, np.nan)) / my.replace(0, np.nan)
    der = bse.diff(21)
    jrk = der.diff(21)
    result = _z(jrk, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_volscale_63d_jerk_v097_signal(closeadj):
    r1 = _f11_ret(closeadj)
    r5 = np.log(closeadj.replace(0, np.nan)).diff(5)
    v1 = r1.rolling(63, min_periods=21).std() * np.sqrt(5.0)
    v5 = r5.rolling(63, min_periods=21).std()
    bse = v5 / v1.replace(0, np.nan)
    der = bse.diff(21)
    jrk = der.diff(21)
    result = _z(jrk, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_bbwjump_21d_jerk_v098_signal(closeadj):
    bw = _f11_bbwidth(closeadj, 21)
    jump = bw.diff() / bw.shift(1).replace(0, np.nan)
    bse = jump.rolling(21, min_periods=10).max()
    der = bse.diff(5)
    jrk = der.diff(5)
    result = _z(jrk, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_downratio_126d_jerk_v099_signal(closeadj):
    r = _f11_ret(closeadj)
    dn = r.where(r < 0)
    ds = dn.rolling(21, min_periods=8).std()
    dl = dn.rolling(126, min_periods=42).std()
    bse = ds / dl.replace(0, np.nan)
    der = bse.diff(21)
    jrk = der.diff(21)
    result = _z(jrk, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_volamp_252d_jerk_v100_signal(closeadj):
    v = _f11_vol(closeadj, 21)
    amp = (v.rolling(252, min_periods=63).max() - v.rolling(252, min_periods=63).min())
    bse = amp / v.rolling(252, min_periods=63).mean().replace(0, np.nan)
    der = bse.diff(21)
    jrk = der.diff(21)
    result = _z(jrk, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_compr563_63d_jerk_v101_signal(closeadj):
    bse = _f11_compress_ratio(closeadj, 5, 63)
    vel = bse.ewm(span=5, min_periods=2).mean() - bse.ewm(span=15, min_periods=7).mean()
    jrk = vel - vel.shift(5)
    sc = bse.rolling(21, min_periods=10).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_compr2112_126d_jerk_v102_signal(closeadj):
    bse = _f11_compress_ratio(closeadj, 21, 126)
    vel = bse.ewm(span=21, min_periods=10).mean() - bse.ewm(span=63, min_periods=31).mean()
    jrk = vel - vel.shift(21)
    sc = bse.rolling(84, min_periods=42).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_pctbpos_21d_jerk_v103_signal(closeadj):
    m = _mean(closeadj, 21)
    sd = _std(closeadj, 21).replace(0, np.nan)
    bse = (closeadj - m) / (2.0 * sd)
    vel = bse.ewm(span=5, min_periods=2).mean() - bse.ewm(span=15, min_periods=7).mean()
    jrk = vel - vel.shift(5)
    sc = bse.rolling(21, min_periods=10).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_compr1012_126d_jerk_v104_signal(closeadj):
    bse = _f11_compress_ratio(closeadj, 10, 126)
    vel = bse.ewm(span=10, min_periods=5).mean() - bse.ewm(span=30, min_periods=15).mean()
    jrk = vel - vel.shift(10)
    sc = bse.rolling(40, min_periods=20).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_rngeff21_21d_jerk_v105_signal(high, low, closeadj):
    net = (closeadj - closeadj.shift(21)).abs()
    path = _f11_truerange(high, low, closeadj).rolling(21, min_periods=10).sum()
    bse = net / path.replace(0, np.nan)
    vel = bse.ewm(span=5, min_periods=2).mean() - bse.ewm(span=15, min_periods=7).mean()
    jrk = vel - vel.shift(5)
    sc = bse.rolling(21, min_periods=10).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_bbw21_21d_jerk_v106_signal(closeadj):
    bse = _f11_bbwidth(closeadj, 21)
    vel = bse.ewm(span=5, min_periods=2).mean() - bse.ewm(span=15, min_periods=7).mean()
    jrk = vel - vel.shift(5)
    sc = bse.rolling(21, min_periods=10).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_bbw63_63d_jerk_v107_signal(closeadj):
    bse = _f11_bbwidth(closeadj, 63)
    vel = bse.ewm(span=21, min_periods=10).mean() - bse.ewm(span=63, min_periods=31).mean()
    jrk = vel - vel.shift(21)
    sc = bse.rolling(84, min_periods=42).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_bbw126_126d_jerk_v108_signal(closeadj):
    bse = _f11_bbwidth(closeadj, 126)
    vel = bse.ewm(span=21, min_periods=10).mean() - bse.ewm(span=63, min_periods=31).mean()
    jrk = vel - vel.shift(21)
    sc = bse.rolling(84, min_periods=42).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_volacf_63d_jerk_v109_signal(closeadj):
    v = _f11_vol(closeadj, 10)
    dv = v - v.rolling(63, min_periods=21).mean()
    num = (dv * dv.shift(10)).rolling(63, min_periods=21).mean()
    den = (dv * dv).rolling(63, min_periods=21).mean()
    bse = num / den.replace(0, np.nan)
    vel = bse.ewm(span=21, min_periods=10).mean() - bse.ewm(span=63, min_periods=31).mean()
    jrk = vel - vel.shift(21)
    sc = bse.rolling(84, min_periods=42).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_bbwratio_63d_jerk_v110_signal(closeadj):
    bw = _f11_bbwidth(closeadj, 21)
    bse = bw / bw.rolling(63, min_periods=21).mean().replace(0, np.nan)
    vel = bse.ewm(span=10, min_periods=5).mean() - bse.ewm(span=30, min_periods=15).mean()
    jrk = vel - vel.shift(10)
    sc = bse.rolling(40, min_periods=20).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_vov63_63d_jerk_v111_signal(closeadj):
    bse = _f11_volofvol(closeadj, 21, 63)
    vel = bse.ewm(span=21, min_periods=10).mean() - bse.ewm(span=63, min_periods=31).mean()
    jrk = vel - vel.shift(21)
    sc = bse.rolling(84, min_periods=42).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_vov126_126d_jerk_v112_signal(closeadj):
    bse = _f11_volofvol(closeadj, 21, 126)
    vel = bse.ewm(span=21, min_periods=10).mean() - bse.ewm(span=63, min_periods=31).mean()
    jrk = vel - vel.shift(21)
    sc = bse.rolling(84, min_periods=42).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_vovshort_21d_jerk_v113_signal(closeadj):
    bse = _f11_volofvol(closeadj, 5, 21)
    vel = bse.ewm(span=5, min_periods=2).mean() - bse.ewm(span=15, min_periods=7).mean()
    jrk = vel - vel.shift(5)
    sc = bse.rolling(21, min_periods=10).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_voltermcurv_63d_jerk_v114_signal(closeadj):
    p5 = _rank(_f11_vol(closeadj, 5), 252)
    p21 = _rank(_f11_vol(closeadj, 21), 252)
    p63 = _rank(_f11_vol(closeadj, 63), 252)
    bse = p5 + p63 - 2.0 * p21
    vel = bse.ewm(span=21, min_periods=10).mean() - bse.ewm(span=63, min_periods=31).mean()
    jrk = vel - vel.shift(21)
    sc = bse.rolling(84, min_periods=42).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_volz504_504d_jerk_v115_signal(closeadj):
    bse = _z(_f11_vol(closeadj, 63), 504)
    vel = bse.ewm(span=63, min_periods=31).mean() - bse.ewm(span=189, min_periods=94).mean()
    jrk = vel - vel.shift(63)
    sc = bse.rolling(252, min_periods=126).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_rangeff63_63d_jerk_v116_signal(high, low, closeadj):
    trp = (_f11_truerange(high, low, closeadj) / closeadj.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    bse = trp.rolling(63, min_periods=21).max() / trp.rolling(63, min_periods=21).min().replace(0, np.nan)
    vel = bse.ewm(span=21, min_periods=10).mean() - bse.ewm(span=63, min_periods=31).mean()
    jrk = vel - vel.shift(21)
    sc = bse.rolling(84, min_periods=42).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_squeeze21_21d_jerk_v117_signal(closeadj):
    bse = _f11_bbwidth(closeadj, 21).rolling(252, min_periods=63).rank(pct=True) - 0.5
    vel = bse.ewm(span=10, min_periods=5).mean() - bse.ewm(span=30, min_periods=15).mean()
    jrk = vel - vel.shift(10)
    sc = bse.rolling(40, min_periods=20).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_squeeze63_63d_jerk_v118_signal(closeadj):
    bse = _f11_bbwidth(closeadj, 63).rolling(252, min_periods=63).rank(pct=True) - 0.5
    vel = bse.ewm(span=21, min_periods=10).mean() - bse.ewm(span=63, min_periods=31).mean()
    jrk = vel - vel.shift(21)
    sc = bse.rolling(84, min_periods=42).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_vol21_21d_jerk_v119_signal(closeadj):
    bse = _f11_vol(closeadj, 21)
    vel = bse.ewm(span=5, min_periods=2).mean() - bse.ewm(span=15, min_periods=7).mean()
    jrk = vel - vel.shift(5)
    sc = bse.rolling(21, min_periods=10).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_vol63_63d_jerk_v120_signal(closeadj):
    bse = _f11_vol(closeadj, 63)
    vel = bse.ewm(span=21, min_periods=10).mean() - bse.ewm(span=63, min_periods=31).mean()
    jrk = vel - vel.shift(21)
    sc = bse.rolling(84, min_periods=42).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_bandtag_63d_jerk_v121_signal(closeadj):
    m = _mean(closeadj, 21)
    sd = _std(closeadj, 21).replace(0, np.nan)
    pctb = (closeadj - m) / (2.0 * sd)
    bse = (pctb.abs() - 1.0).clip(lower=0).rolling(63, min_periods=21).mean()
    vel = bse.ewm(span=21, min_periods=10).mean() - bse.ewm(span=63, min_periods=31).mean()
    jrk = vel - vel.shift(21)
    sc = bse.rolling(84, min_periods=42).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_vol126_126d_jerk_v122_signal(closeadj):
    bse = _f11_vol(closeadj, 126)
    vel = bse.ewm(span=21, min_periods=10).mean() - bse.ewm(span=63, min_periods=31).mean()
    jrk = vel - vel.shift(21)
    sc = bse.rolling(84, min_periods=42).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_atrp21_21d_jerk_v123_signal(high, low, closeadj):
    bse = _f11_atr(high, low, closeadj, 21) / closeadj.replace(0, np.nan)
    vel = bse.ewm(span=5, min_periods=2).mean() - bse.ewm(span=15, min_periods=7).mean()
    jrk = vel - vel.shift(5)
    sc = bse.rolling(21, min_periods=10).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_atrp63_63d_jerk_v124_signal(high, low, closeadj):
    bse = _f11_atr(high, low, closeadj, 63) / closeadj.replace(0, np.nan)
    vel = bse.ewm(span=21, min_periods=10).mean() - bse.ewm(span=63, min_periods=31).mean()
    jrk = vel - vel.shift(21)
    sc = bse.rolling(84, min_periods=42).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_atrcompr_63d_jerk_v125_signal(high, low, closeadj):
    a_s = _f11_atr(high, low, closeadj, 5)
    a_l = _f11_atr(high, low, closeadj, 63)
    bse = a_s / a_l.replace(0, np.nan)
    vel = bse.ewm(span=5, min_periods=2).mean() - bse.ewm(span=15, min_periods=7).mean()
    jrk = vel - vel.shift(5)
    sc = bse.rolling(21, min_periods=10).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_pk21_21d_jerk_v126_signal(high, low):
    bse = _f11_parkinson(high, low, 21)
    vel = bse.ewm(span=5, min_periods=2).mean() - bse.ewm(span=15, min_periods=7).mean()
    jrk = vel - vel.shift(5)
    sc = bse.rolling(21, min_periods=10).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_pk63_63d_jerk_v127_signal(high, low):
    bse = _f11_parkinson(high, low, 63)
    vel = bse.ewm(span=21, min_periods=10).mean() - bse.ewm(span=63, min_periods=31).mean()
    jrk = vel - vel.shift(21)
    sc = bse.rolling(84, min_periods=42).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_pkz_252d_jerk_v128_signal(high, low):
    bse = _z(_f11_parkinson(high, low, 21), 252)
    vel = bse.ewm(span=21, min_periods=10).mean() - bse.ewm(span=63, min_periods=31).mean()
    jrk = vel - vel.shift(21)
    sc = bse.rolling(84, min_periods=42).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_bbwz_504d_jerk_v129_signal(closeadj):
    bse = _z(_f11_bbwidth(closeadj, 63), 504)
    vel = bse.ewm(span=63, min_periods=31).mean() - bse.ewm(span=189, min_periods=94).mean()
    jrk = vel - vel.shift(63)
    sc = bse.rolling(252, min_periods=126).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_atrz_252d_jerk_v130_signal(high, low, closeadj):
    bse = _z(_f11_atr(high, low, closeadj, 21) / closeadj.replace(0, np.nan), 252)
    vel = bse.ewm(span=21, min_periods=10).mean() - bse.ewm(span=63, min_periods=31).mean()
    jrk = vel - vel.shift(21)
    sc = bse.rolling(84, min_periods=42).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_bbwenergy_63d_jerk_v131_signal(closeadj):
    bw = _f11_bbwidth(closeadj, 21)
    vs = bw.rolling(21, min_periods=10).var()
    vl = bw.rolling(126, min_periods=42).var()
    bse = vs / vl.replace(0, np.nan)
    vel = bse.ewm(span=21, min_periods=10).mean() - bse.ewm(span=63, min_periods=31).mean()
    jrk = vel - vel.shift(21)
    sc = bse.rolling(84, min_periods=42).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_volcurv_63d_jerk_v132_signal(closeadj):
    v5 = _f11_vol(closeadj, 5)
    v21 = _f11_vol(closeadj, 21)
    v63 = _f11_vol(closeadj, 63)
    bse = (v5 - 2.0 * v21 + v63) / v21.replace(0, np.nan)
    vel = bse.ewm(span=10, min_periods=5).mean() - bse.ewm(span=30, min_periods=15).mean()
    jrk = vel - vel.shift(10)
    sc = bse.rolling(40, min_periods=20).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_volasym_63d_jerk_v133_signal(closeadj):
    r = _f11_ret(closeadj)
    uv = r.where(r > 0).rolling(63, min_periods=21).std()
    dv = r.where(r < 0).rolling(63, min_periods=21).std()
    bse = (uv - dv) / (uv + dv).replace(0, np.nan)
    vel = bse.ewm(span=21, min_periods=10).mean() - bse.ewm(span=63, min_periods=31).mean()
    jrk = vel - vel.shift(21)
    sc = bse.rolling(84, min_periods=42).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_rngexp_63d_jerk_v134_signal(closeadj):
    rng5 = (_rmax(closeadj, 5) - _rmin(closeadj, 5)) / closeadj.replace(0, np.nan)
    bse = rng5 / rng5.rolling(63, min_periods=21).mean().replace(0, np.nan)
    vel = bse.ewm(span=5, min_periods=2).mean() - bse.ewm(span=15, min_periods=7).mean()
    jrk = vel - vel.shift(5)
    sc = bse.rolling(21, min_periods=10).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_bbwfrommax_252d_jerk_v135_signal(closeadj):
    bw = _f11_bbwidth(closeadj, 21)
    bse = bw / bw.rolling(252, min_periods=63).max().replace(0, np.nan)
    vel = bse.ewm(span=21, min_periods=10).mean() - bse.ewm(span=63, min_periods=31).mean()
    jrk = vel - vel.shift(21)
    sc = bse.rolling(84, min_periods=42).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_volhyst_252d_jerk_v136_signal(closeadj):
    pf = _rank(_f11_vol(closeadj, 10), 252)
    ps = _rank(_f11_vol(closeadj, 63), 252)
    bse = pf - ps
    vel = bse.ewm(span=21, min_periods=10).mean() - bse.ewm(span=63, min_periods=31).mean()
    jrk = vel - vel.shift(21)
    sc = bse.rolling(84, min_periods=42).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_pctbdisp_63d_jerk_v137_signal(closeadj):
    m = _mean(closeadj, 21)
    sd = _std(closeadj, 21).replace(0, np.nan)
    pctb = (closeadj - m) / (2.0 * sd)
    bse = pctb.rolling(63, min_periods=21).std()
    vel = bse.ewm(span=21, min_periods=10).mean() - bse.ewm(span=63, min_periods=31).mean()
    jrk = vel - vel.shift(21)
    sc = bse.rolling(84, min_periods=42).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_voltilt_252d_jerk_v138_signal(closeadj):
    v63 = _f11_vol(closeadj, 63)
    bse = v63.rolling(252, min_periods=63).rank(pct=True) - v63.rolling(504, min_periods=126).rank(pct=True)
    vel = bse.ewm(span=21, min_periods=10).mean() - bse.ewm(span=63, min_periods=31).mean()
    jrk = vel - vel.shift(21)
    sc = bse.rolling(84, min_periods=42).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_bbwspread_63d_jerk_v139_signal(closeadj):
    b21 = _f11_bbwidth(closeadj, 21)
    b63 = _f11_bbwidth(closeadj, 63)
    bse = (b21 - b63) / b63.replace(0, np.nan)
    vel = bse.ewm(span=10, min_periods=5).mean() - bse.ewm(span=30, min_periods=15).mean()
    jrk = vel - vel.shift(10)
    sc = bse.rolling(40, min_periods=20).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_pkrvgap_21d_jerk_v140_signal(high, low, closeadj):
    bse = _f11_parkinson(high, low, 21) - _f11_vol(closeadj, 21)
    vel = bse.ewm(span=5, min_periods=2).mean() - bse.ewm(span=15, min_periods=7).mean()
    jrk = vel - vel.shift(5)
    sc = bse.rolling(21, min_periods=10).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_downvol_21d_jerk_v141_signal(closeadj):
    r = _f11_ret(closeadj)
    bse = r.where(r < 0).rolling(21, min_periods=8).std()
    vel = bse.ewm(span=5, min_periods=2).mean() - bse.ewm(span=15, min_periods=7).mean()
    jrk = vel - vel.shift(5)
    sc = bse.rolling(21, min_periods=10).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_upvol_21d_jerk_v142_signal(closeadj):
    r = _f11_ret(closeadj)
    bse = r.where(r > 0).rolling(21, min_periods=8).std()
    vel = bse.ewm(span=5, min_periods=2).mean() - bse.ewm(span=15, min_periods=7).mean()
    jrk = vel - vel.shift(5)
    sc = bse.rolling(21, min_periods=10).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_bbwdonch_21d_jerk_v143_signal(closeadj):
    bw = _f11_bbwidth(closeadj, 21)
    donch = (_rmax(closeadj, 21) - _rmin(closeadj, 21)) / _mean(closeadj, 21).replace(0, np.nan)
    bse = bw / donch.replace(0, np.nan)
    vel = bse.ewm(span=10, min_periods=5).mean() - bse.ewm(span=30, min_periods=15).mean()
    jrk = vel - vel.shift(10)
    sc = bse.rolling(40, min_periods=20).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_trp_21d_jerk_v144_signal(high, low, closeadj):
    bse = (_f11_truerange(high, low, closeadj) / closeadj.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    vel = bse.ewm(span=5, min_periods=2).mean() - bse.ewm(span=15, min_periods=7).mean()
    jrk = vel - vel.shift(5)
    sc = bse.rolling(21, min_periods=10).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_rsest_21d_jerk_v145_signal(high, low, closeadj):
    hc = np.log(high.replace(0, np.nan) / closeadj.replace(0, np.nan))
    lc = np.log(low.replace(0, np.nan) / closeadj.replace(0, np.nan))
    ho = np.log(high.replace(0, np.nan) / closeadj.shift(1).replace(0, np.nan))
    lo = np.log(low.replace(0, np.nan) / closeadj.shift(1).replace(0, np.nan))
    bse = (hc * ho + lc * lo).rolling(21, min_periods=10).mean().clip(lower=0) ** 0.5
    vel = bse.ewm(span=5, min_periods=2).mean() - bse.ewm(span=15, min_periods=7).mean()
    jrk = vel - vel.shift(5)
    sc = bse.rolling(21, min_periods=10).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_volregslope_63d_jerk_v146_signal(closeadj):
    v = _f11_vol(closeadj, 21)
    x = pd.Series(np.arange(len(v)), index=v.index, dtype=float)
    mx = x.rolling(63, min_periods=21).mean()
    my = v.rolling(63, min_periods=21).mean()
    cov = (x * v).rolling(63, min_periods=21).mean() - mx * my
    varx = (x * x).rolling(63, min_periods=21).mean() - mx * mx
    bse = (cov / varx.replace(0, np.nan)) / my.replace(0, np.nan)
    vel = bse.ewm(span=21, min_periods=10).mean() - bse.ewm(span=63, min_periods=31).mean()
    jrk = vel - vel.shift(21)
    sc = bse.rolling(84, min_periods=42).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_volscale_63d_jerk_v147_signal(closeadj):
    r1 = _f11_ret(closeadj)
    r5 = np.log(closeadj.replace(0, np.nan)).diff(5)
    v1 = r1.rolling(63, min_periods=21).std() * np.sqrt(5.0)
    v5 = r5.rolling(63, min_periods=21).std()
    bse = v5 / v1.replace(0, np.nan)
    vel = bse.ewm(span=21, min_periods=10).mean() - bse.ewm(span=63, min_periods=31).mean()
    jrk = vel - vel.shift(21)
    sc = bse.rolling(84, min_periods=42).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_bbwjump_21d_jerk_v148_signal(closeadj):
    bw = _f11_bbwidth(closeadj, 21)
    jump = bw.diff() / bw.shift(1).replace(0, np.nan)
    bse = jump.rolling(21, min_periods=10).max()
    vel = bse.ewm(span=5, min_periods=2).mean() - bse.ewm(span=15, min_periods=7).mean()
    jrk = vel - vel.shift(5)
    sc = bse.rolling(21, min_periods=10).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_downratio_126d_jerk_v149_signal(closeadj):
    r = _f11_ret(closeadj)
    dn = r.where(r < 0)
    ds = dn.rolling(21, min_periods=8).std()
    dl = dn.rolling(126, min_periods=42).std()
    bse = ds / dl.replace(0, np.nan)
    vel = bse.ewm(span=21, min_periods=10).mean() - bse.ewm(span=63, min_periods=31).mean()
    jrk = vel - vel.shift(21)
    sc = bse.rolling(84, min_periods=42).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)

def f11vr_f11_volatility_regime_shift_volamp_252d_jerk_v150_signal(closeadj):
    v = _f11_vol(closeadj, 21)
    amp = (v.rolling(252, min_periods=63).max() - v.rolling(252, min_periods=63).min())
    bse = amp / v.rolling(252, min_periods=63).mean().replace(0, np.nan)
    vel = bse.ewm(span=21, min_periods=10).mean() - bse.ewm(span=63, min_periods=31).mean()
    jrk = vel - vel.shift(21)
    sc = bse.rolling(84, min_periods=42).std().replace(0, np.nan)
    result = jrk / sc
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f11vr_f11_volatility_regime_shift_compr563_63d_jerk_v001_signal,
    f11vr_f11_volatility_regime_shift_compr2112_126d_jerk_v002_signal,
    f11vr_f11_volatility_regime_shift_pctbpos_21d_jerk_v003_signal,
    f11vr_f11_volatility_regime_shift_compr1012_126d_jerk_v004_signal,
    f11vr_f11_volatility_regime_shift_rngeff21_21d_jerk_v005_signal,
    f11vr_f11_volatility_regime_shift_bbw21_21d_jerk_v006_signal,
    f11vr_f11_volatility_regime_shift_bbw63_63d_jerk_v007_signal,
    f11vr_f11_volatility_regime_shift_bbw126_126d_jerk_v008_signal,
    f11vr_f11_volatility_regime_shift_volacf_63d_jerk_v009_signal,
    f11vr_f11_volatility_regime_shift_bbwratio_63d_jerk_v010_signal,
    f11vr_f11_volatility_regime_shift_vov63_63d_jerk_v011_signal,
    f11vr_f11_volatility_regime_shift_vov126_126d_jerk_v012_signal,
    f11vr_f11_volatility_regime_shift_vovshort_21d_jerk_v013_signal,
    f11vr_f11_volatility_regime_shift_voltermcurv_63d_jerk_v014_signal,
    f11vr_f11_volatility_regime_shift_volz504_504d_jerk_v015_signal,
    f11vr_f11_volatility_regime_shift_rangeff63_63d_jerk_v016_signal,
    f11vr_f11_volatility_regime_shift_squeeze21_21d_jerk_v017_signal,
    f11vr_f11_volatility_regime_shift_squeeze63_63d_jerk_v018_signal,
    f11vr_f11_volatility_regime_shift_vol21_21d_jerk_v019_signal,
    f11vr_f11_volatility_regime_shift_vol63_63d_jerk_v020_signal,
    f11vr_f11_volatility_regime_shift_bandtag_63d_jerk_v021_signal,
    f11vr_f11_volatility_regime_shift_vol126_126d_jerk_v022_signal,
    f11vr_f11_volatility_regime_shift_atrp21_21d_jerk_v023_signal,
    f11vr_f11_volatility_regime_shift_atrp63_63d_jerk_v024_signal,
    f11vr_f11_volatility_regime_shift_atrcompr_63d_jerk_v025_signal,
    f11vr_f11_volatility_regime_shift_pk21_21d_jerk_v026_signal,
    f11vr_f11_volatility_regime_shift_pk63_63d_jerk_v027_signal,
    f11vr_f11_volatility_regime_shift_pkz_252d_jerk_v028_signal,
    f11vr_f11_volatility_regime_shift_bbwz_504d_jerk_v029_signal,
    f11vr_f11_volatility_regime_shift_atrz_252d_jerk_v030_signal,
    f11vr_f11_volatility_regime_shift_bbwenergy_63d_jerk_v031_signal,
    f11vr_f11_volatility_regime_shift_volcurv_63d_jerk_v032_signal,
    f11vr_f11_volatility_regime_shift_volasym_63d_jerk_v033_signal,
    f11vr_f11_volatility_regime_shift_rngexp_63d_jerk_v034_signal,
    f11vr_f11_volatility_regime_shift_bbwfrommax_252d_jerk_v035_signal,
    f11vr_f11_volatility_regime_shift_volhyst_252d_jerk_v036_signal,
    f11vr_f11_volatility_regime_shift_pctbdisp_63d_jerk_v037_signal,
    f11vr_f11_volatility_regime_shift_voltilt_252d_jerk_v038_signal,
    f11vr_f11_volatility_regime_shift_bbwspread_63d_jerk_v039_signal,
    f11vr_f11_volatility_regime_shift_pkrvgap_21d_jerk_v040_signal,
    f11vr_f11_volatility_regime_shift_downvol_21d_jerk_v041_signal,
    f11vr_f11_volatility_regime_shift_upvol_21d_jerk_v042_signal,
    f11vr_f11_volatility_regime_shift_bbwdonch_21d_jerk_v043_signal,
    f11vr_f11_volatility_regime_shift_trp_21d_jerk_v044_signal,
    f11vr_f11_volatility_regime_shift_rsest_21d_jerk_v045_signal,
    f11vr_f11_volatility_regime_shift_volregslope_63d_jerk_v046_signal,
    f11vr_f11_volatility_regime_shift_volscale_63d_jerk_v047_signal,
    f11vr_f11_volatility_regime_shift_bbwjump_21d_jerk_v048_signal,
    f11vr_f11_volatility_regime_shift_downratio_126d_jerk_v049_signal,
    f11vr_f11_volatility_regime_shift_volamp_252d_jerk_v050_signal,
    f11vr_f11_volatility_regime_shift_compr563_63d_jerk_v051_signal,
    f11vr_f11_volatility_regime_shift_compr2112_126d_jerk_v052_signal,
    f11vr_f11_volatility_regime_shift_pctbpos_21d_jerk_v053_signal,
    f11vr_f11_volatility_regime_shift_compr1012_126d_jerk_v054_signal,
    f11vr_f11_volatility_regime_shift_rngeff21_21d_jerk_v055_signal,
    f11vr_f11_volatility_regime_shift_bbw21_21d_jerk_v056_signal,
    f11vr_f11_volatility_regime_shift_bbw63_63d_jerk_v057_signal,
    f11vr_f11_volatility_regime_shift_bbw126_126d_jerk_v058_signal,
    f11vr_f11_volatility_regime_shift_volacf_63d_jerk_v059_signal,
    f11vr_f11_volatility_regime_shift_bbwratio_63d_jerk_v060_signal,
    f11vr_f11_volatility_regime_shift_vov63_63d_jerk_v061_signal,
    f11vr_f11_volatility_regime_shift_vov126_126d_jerk_v062_signal,
    f11vr_f11_volatility_regime_shift_vovshort_21d_jerk_v063_signal,
    f11vr_f11_volatility_regime_shift_voltermcurv_63d_jerk_v064_signal,
    f11vr_f11_volatility_regime_shift_volz504_504d_jerk_v065_signal,
    f11vr_f11_volatility_regime_shift_rangeff63_63d_jerk_v066_signal,
    f11vr_f11_volatility_regime_shift_squeeze21_21d_jerk_v067_signal,
    f11vr_f11_volatility_regime_shift_squeeze63_63d_jerk_v068_signal,
    f11vr_f11_volatility_regime_shift_vol21_21d_jerk_v069_signal,
    f11vr_f11_volatility_regime_shift_vol63_63d_jerk_v070_signal,
    f11vr_f11_volatility_regime_shift_bandtag_63d_jerk_v071_signal,
    f11vr_f11_volatility_regime_shift_vol126_126d_jerk_v072_signal,
    f11vr_f11_volatility_regime_shift_atrp21_21d_jerk_v073_signal,
    f11vr_f11_volatility_regime_shift_atrp63_63d_jerk_v074_signal,
    f11vr_f11_volatility_regime_shift_atrcompr_63d_jerk_v075_signal,
    f11vr_f11_volatility_regime_shift_pk21_21d_jerk_v076_signal,
    f11vr_f11_volatility_regime_shift_pk63_63d_jerk_v077_signal,
    f11vr_f11_volatility_regime_shift_pkz_252d_jerk_v078_signal,
    f11vr_f11_volatility_regime_shift_bbwz_504d_jerk_v079_signal,
    f11vr_f11_volatility_regime_shift_atrz_252d_jerk_v080_signal,
    f11vr_f11_volatility_regime_shift_bbwenergy_63d_jerk_v081_signal,
    f11vr_f11_volatility_regime_shift_volcurv_63d_jerk_v082_signal,
    f11vr_f11_volatility_regime_shift_volasym_63d_jerk_v083_signal,
    f11vr_f11_volatility_regime_shift_rngexp_63d_jerk_v084_signal,
    f11vr_f11_volatility_regime_shift_bbwfrommax_252d_jerk_v085_signal,
    f11vr_f11_volatility_regime_shift_volhyst_252d_jerk_v086_signal,
    f11vr_f11_volatility_regime_shift_pctbdisp_63d_jerk_v087_signal,
    f11vr_f11_volatility_regime_shift_voltilt_252d_jerk_v088_signal,
    f11vr_f11_volatility_regime_shift_bbwspread_63d_jerk_v089_signal,
    f11vr_f11_volatility_regime_shift_pkrvgap_21d_jerk_v090_signal,
    f11vr_f11_volatility_regime_shift_downvol_21d_jerk_v091_signal,
    f11vr_f11_volatility_regime_shift_upvol_21d_jerk_v092_signal,
    f11vr_f11_volatility_regime_shift_bbwdonch_21d_jerk_v093_signal,
    f11vr_f11_volatility_regime_shift_trp_21d_jerk_v094_signal,
    f11vr_f11_volatility_regime_shift_rsest_21d_jerk_v095_signal,
    f11vr_f11_volatility_regime_shift_volregslope_63d_jerk_v096_signal,
    f11vr_f11_volatility_regime_shift_volscale_63d_jerk_v097_signal,
    f11vr_f11_volatility_regime_shift_bbwjump_21d_jerk_v098_signal,
    f11vr_f11_volatility_regime_shift_downratio_126d_jerk_v099_signal,
    f11vr_f11_volatility_regime_shift_volamp_252d_jerk_v100_signal,
    f11vr_f11_volatility_regime_shift_compr563_63d_jerk_v101_signal,
    f11vr_f11_volatility_regime_shift_compr2112_126d_jerk_v102_signal,
    f11vr_f11_volatility_regime_shift_pctbpos_21d_jerk_v103_signal,
    f11vr_f11_volatility_regime_shift_compr1012_126d_jerk_v104_signal,
    f11vr_f11_volatility_regime_shift_rngeff21_21d_jerk_v105_signal,
    f11vr_f11_volatility_regime_shift_bbw21_21d_jerk_v106_signal,
    f11vr_f11_volatility_regime_shift_bbw63_63d_jerk_v107_signal,
    f11vr_f11_volatility_regime_shift_bbw126_126d_jerk_v108_signal,
    f11vr_f11_volatility_regime_shift_volacf_63d_jerk_v109_signal,
    f11vr_f11_volatility_regime_shift_bbwratio_63d_jerk_v110_signal,
    f11vr_f11_volatility_regime_shift_vov63_63d_jerk_v111_signal,
    f11vr_f11_volatility_regime_shift_vov126_126d_jerk_v112_signal,
    f11vr_f11_volatility_regime_shift_vovshort_21d_jerk_v113_signal,
    f11vr_f11_volatility_regime_shift_voltermcurv_63d_jerk_v114_signal,
    f11vr_f11_volatility_regime_shift_volz504_504d_jerk_v115_signal,
    f11vr_f11_volatility_regime_shift_rangeff63_63d_jerk_v116_signal,
    f11vr_f11_volatility_regime_shift_squeeze21_21d_jerk_v117_signal,
    f11vr_f11_volatility_regime_shift_squeeze63_63d_jerk_v118_signal,
    f11vr_f11_volatility_regime_shift_vol21_21d_jerk_v119_signal,
    f11vr_f11_volatility_regime_shift_vol63_63d_jerk_v120_signal,
    f11vr_f11_volatility_regime_shift_bandtag_63d_jerk_v121_signal,
    f11vr_f11_volatility_regime_shift_vol126_126d_jerk_v122_signal,
    f11vr_f11_volatility_regime_shift_atrp21_21d_jerk_v123_signal,
    f11vr_f11_volatility_regime_shift_atrp63_63d_jerk_v124_signal,
    f11vr_f11_volatility_regime_shift_atrcompr_63d_jerk_v125_signal,
    f11vr_f11_volatility_regime_shift_pk21_21d_jerk_v126_signal,
    f11vr_f11_volatility_regime_shift_pk63_63d_jerk_v127_signal,
    f11vr_f11_volatility_regime_shift_pkz_252d_jerk_v128_signal,
    f11vr_f11_volatility_regime_shift_bbwz_504d_jerk_v129_signal,
    f11vr_f11_volatility_regime_shift_atrz_252d_jerk_v130_signal,
    f11vr_f11_volatility_regime_shift_bbwenergy_63d_jerk_v131_signal,
    f11vr_f11_volatility_regime_shift_volcurv_63d_jerk_v132_signal,
    f11vr_f11_volatility_regime_shift_volasym_63d_jerk_v133_signal,
    f11vr_f11_volatility_regime_shift_rngexp_63d_jerk_v134_signal,
    f11vr_f11_volatility_regime_shift_bbwfrommax_252d_jerk_v135_signal,
    f11vr_f11_volatility_regime_shift_volhyst_252d_jerk_v136_signal,
    f11vr_f11_volatility_regime_shift_pctbdisp_63d_jerk_v137_signal,
    f11vr_f11_volatility_regime_shift_voltilt_252d_jerk_v138_signal,
    f11vr_f11_volatility_regime_shift_bbwspread_63d_jerk_v139_signal,
    f11vr_f11_volatility_regime_shift_pkrvgap_21d_jerk_v140_signal,
    f11vr_f11_volatility_regime_shift_downvol_21d_jerk_v141_signal,
    f11vr_f11_volatility_regime_shift_upvol_21d_jerk_v142_signal,
    f11vr_f11_volatility_regime_shift_bbwdonch_21d_jerk_v143_signal,
    f11vr_f11_volatility_regime_shift_trp_21d_jerk_v144_signal,
    f11vr_f11_volatility_regime_shift_rsest_21d_jerk_v145_signal,
    f11vr_f11_volatility_regime_shift_volregslope_63d_jerk_v146_signal,
    f11vr_f11_volatility_regime_shift_volscale_63d_jerk_v147_signal,
    f11vr_f11_volatility_regime_shift_bbwjump_21d_jerk_v148_signal,
    f11vr_f11_volatility_regime_shift_downratio_126d_jerk_v149_signal,
    f11vr_f11_volatility_regime_shift_volamp_252d_jerk_v150_signal,
]




def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F11_VOLATILITY_REGIME_SHIFT_REGISTRY_001_150 = REGISTRY


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

    print("OK f11_volatility_regime_shift_3rd_derivatives_001_150_claude: %d features pass" % n_features)
