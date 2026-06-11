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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 3)).rank(pct=True) - 0.5


def _f13_range(high, low):
    return (high - low)


def _f13_body_abs(open_, close):
    return (close - open_).abs()


def _f13_body_ratio(open_, high, low, close):
    rng = (high - low).replace(0, np.nan)
    return (close - open_).abs() / rng


def _f13_close_in_range(high, low, close):
    rng = (high - low).replace(0, np.nan)
    return (close - low) / rng


def _f13_upper_ratio(open_, high, low, close):
    rng = (high - low).replace(0, np.nan)
    return (high - np.maximum(open_, close)) / rng


def _f13_lower_ratio(open_, high, low, close):
    rng = (high - low).replace(0, np.nan)
    return (np.minimum(open_, close) - low) / rng


def _f13_upper_wick(open_, high, close):
    return (high - np.maximum(open_, close))


def _f13_lower_wick(open_, low, close):
    return (np.minimum(open_, close) - low)


def f13cr_f13_candle_range_structure_bodyratio_5d_jerk_v001_signal(open, high, low, close):
    base = _mean(_f13_body_ratio(open, high, low, close), 5)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_cir_5d_jerk_v002_signal(high, low, close):
    base = _mean(_f13_close_in_range(high, low, close), 5) - 0.5
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_uwick_5d_jerk_v003_signal(open, high, low, close):
    base = _mean(_f13_upper_ratio(open, high, low, close), 5)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_lwick_5d_jerk_v004_signal(open, high, low, close):
    base = _mean(_f13_lower_ratio(open, high, low, close), 5)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_wickskew_5d_jerk_v005_signal(open, high, low, close):
    lw = _f13_lower_ratio(open, high, low, close)
    uw = _f13_upper_ratio(open, high, low, close)
    base = _mean(lw - uw, 5)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_rngexp_5d_jerk_v006_signal(high, low):
    rng = _f13_range(high, low)
    base = _mean(rng, 5) / _mean(rng, 63).replace(0, np.nan)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_atrpct_5d_jerk_v007_signal(high, low, close):
    tr = _f13_range(high, low) / close.replace(0, np.nan)
    base = _mean(tr, 5)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_thrust_5d_jerk_v008_signal(open, high, low, close):
    rng = _f13_range(high, low).replace(0, np.nan)
    base = _mean((close - open) / rng, 5)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_gapfade_5d_jerk_v009_signal(open, close):
    gap = open / close.shift(1).replace(0, np.nan) - 1.0
    intraday = close / open.replace(0, np.nan) - 1.0
    base = _mean(-np.sign(gap) * intraday, 5)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_rngconc_5d_jerk_v010_signal(high, low):
    rng = _f13_range(high, low)
    mx = rng.rolling(63, min_periods=max(1,63//2)).max()
    tot = rng.rolling(63, min_periods=max(1,63//2)).sum().replace(0, np.nan)
    base = mx / tot
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_cirema_5d_jerk_v011_signal(high, low, close):
    cir = _f13_close_in_range(high, low, close)
    base = cir.ewm(span=5, min_periods=max(5, 5//2)).mean() - 0.5
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_rngvsbody_5d_jerk_v012_signal(open, high, low, close):
    rng = _f13_range(high, low)
    body = _f13_body_abs(open, close)
    base = _mean((rng / body.replace(0, np.nan)).clip(upper=20.0), 5)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_decisive_5d_jerk_v013_signal(high, low, close):
    cir = _f13_close_in_range(high, low, close)
    base = _mean((cir - 0.5).abs(), 5)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_rngcv_5d_jerk_v014_signal(high, low, close):
    tr = _f13_range(high, low) / close.replace(0, np.nan)
    base = _std(tr, 5) / _mean(tr, 5).replace(0, np.nan)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_bodyskew_5d_jerk_v015_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close)
    base = br.rolling(63, min_periods=max(1,63//2)).skew()
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_varratio_5d_jerk_v016_signal(high, low, close):
    cc = close.pct_change()
    ccv = _mean(cc ** 2, 5)
    lr = np.log(high.replace(0, np.nan) / low.replace(0, np.nan)) ** 2
    pkv = _mean(lr, 5) / (4.0 * np.log(2.0))
    base = ccv / pkv.replace(0, np.nan)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_vwcir_5d_jerk_v017_signal(high, low, close, volume):
    cir = _f13_close_in_range(high, low, close)
    num = (cir * volume).rolling(5, min_periods=max(1,5//2)).sum()
    den = volume.rolling(5, min_periods=max(1,5//2)).sum().replace(0, np.nan)
    base = num / den - 0.5
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_bodydom_5d_jerk_v018_signal(open, close):
    body = (close - open)
    net = body.rolling(5, min_periods=max(1,5//2)).sum()
    gross = body.abs().rolling(5, min_periods=max(1,5//2)).sum().replace(0, np.nan)
    base = net / gross
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_wickshare_5d_jerk_v019_signal(open, high, low, close):
    uw = _f13_upper_wick(open, high, close)
    lw = _f13_lower_wick(open, low, close)
    rng = _f13_range(high, low)
    wsum = (uw + lw).rolling(5, min_periods=max(1,5//2)).sum()
    rsum = rng.rolling(5, min_periods=max(1,5//2)).sum().replace(0, np.nan)
    base = wsum / rsum
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_strongbody_5d_jerk_v020_signal(open, high, low, close):
    cir = _f13_close_in_range(high, low, close)
    br = _f13_body_ratio(open, high, low, close)
    base = _mean((cir - 0.5) * br, 5)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_maxshock_5d_jerk_v021_signal(high, low, close):
    rng = _f13_range(high, low)
    base = rng.rolling(5, min_periods=max(1,5//2)).max() / close.replace(0, np.nan)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_rngeffic_5d_jerk_v022_signal(high, low, close):
    net = (close - close.shift(5)).abs()
    path = _f13_range(high, low).rolling(5, min_periods=max(1,5//2)).sum().replace(0, np.nan)
    base = net / path
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_rngmedmean_5d_jerk_v023_signal(high, low, close):
    tr = _f13_range(high, low) / close.replace(0, np.nan)
    med = tr.rolling(63, min_periods=max(1,63//2)).median()
    mn = _mean(tr, 63)
    base = (mn - med) / mn.replace(0, np.nan)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_conviction_5d_jerk_v024_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close)
    maru = (br - 0.6).clip(lower=0)
    doji = (0.2 - br).clip(lower=0)
    base = _mean(maru - doji, 5)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_cirskew_5d_jerk_v025_signal(high, low, close):
    cir = _f13_close_in_range(high, low, close)
    base = cir.rolling(63, min_periods=max(1,63//2)).skew()
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_uwickdom_5d_jerk_v026_signal(open, high, low, close):
    uw = _f13_upper_ratio(open, high, low, close)
    lw = _f13_lower_ratio(open, high, low, close)
    base = _mean((uw - lw).clip(lower=0), 5)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_lwickdom_5d_jerk_v027_signal(open, high, low, close):
    uw = _f13_upper_ratio(open, high, low, close)
    lw = _f13_lower_ratio(open, high, low, close)
    base = _mean((lw - uw).clip(lower=0), 5)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_vwbody_5d_jerk_v028_signal(open, high, low, close, volume):
    br = _f13_body_ratio(open, high, low, close)
    num = (br * volume).rolling(5, min_periods=max(1,5//2)).sum()
    den = volume.rolling(5, min_periods=max(1,5//2)).sum().replace(0, np.nan)
    base = num / den
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_climaxz_5d_jerk_v029_signal(high, low, volume):
    rng = _f13_range(high, low)
    base = _mean(_z(rng, 63).clip(lower=0) * _z(volume, 63).clip(lower=0), 5)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_gapdom_5d_jerk_v030_signal(open, high, low, close):
    gap = (open - close.shift(1)).abs()
    intr = _f13_range(high, low)
    base = _mean(gap / (gap + intr).replace(0, np.nan), 5)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_widerev_5d_jerk_v031_signal(high, low, close):
    rng = _f13_range(high, low)
    rz = _z(rng, 63).clip(lower=0)
    cir = _f13_close_in_range(high, low, close)
    base = _mean(rz * (1.0 - (cir - 0.5).abs() * 2.0), 5)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_squeezemin_5d_jerk_v032_signal(high, low):
    rng = _f13_range(high, low)
    mn = rng.rolling(63, min_periods=max(1,63//2)).min()
    base = mn / _mean(rng, 63).replace(0, np.nan)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_garmanklass_5d_jerk_v033_signal(open, high, low, close):
    hl = np.log(high.replace(0, np.nan) / low.replace(0, np.nan)) ** 2
    co = np.log(close.replace(0, np.nan) / open.replace(0, np.nan)) ** 2
    gk = 0.5 * hl - (2.0 * np.log(2.0) - 1.0) * co
    base = np.sqrt(_mean(gk, 5).clip(lower=0))
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_composite_5d_jerk_v034_signal(open, high, low, close, volume):
    br = _f13_body_ratio(open, high, low, close)
    cir = _f13_close_in_range(high, low, close)
    vz = _z(volume, 63)
    base = _mean(br * (cir - 0.5) * np.tanh(vz), 5)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_effortresult_5d_jerk_v035_signal(high, low, close, volume):
    rng = _f13_range(high, low) / close.replace(0, np.nan)
    eff = volume / rng.replace(0, np.nan)
    base = _z(_mean(eff, 5), 252)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_closeoverrng_5d_jerk_v036_signal(high, low, close):
    chg = close.diff()
    rng = _f13_range(high, low).replace(0, np.nan)
    base = _mean(chg / rng, 5)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_gapmag_5d_jerk_v037_signal(open, close):
    gap = (open - close.shift(1)).abs() / close.shift(1).replace(0, np.nan)
    base = _z(_mean(gap, 5), 252)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_ovnratio_5d_jerk_v038_signal(high, low, close):
    cc = close.pct_change().abs()
    rng = _f13_range(high, low) / close.replace(0, np.nan)
    base = _mean(cc, 5) / _mean(rng, 5).replace(0, np.nan)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_wicklograt_5d_jerk_v039_signal(open, high, low, close):
    uw = _f13_upper_wick(open, high, close)
    lw = _f13_lower_wick(open, low, close)
    base = _mean(np.log((lw + 1e-6) / (uw + 1e-6)), 5)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_rngbodydiverge_5d_jerk_v040_signal(open, high, low, close):
    rng = _f13_range(high, low)
    body = _f13_body_abs(open, close)
    rex = _mean(rng, 5) / _mean(rng, 252).replace(0, np.nan)
    bex = _mean(body, 5) / _mean(body, 252).replace(0, np.nan)
    base = rex - bex
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_climaxbias_5d_jerk_v041_signal(open, high, low, close):
    rng = _f13_range(high, low)
    rz = _z(rng, 63).clip(lower=0)
    cir = _f13_close_in_range(high, low, close)
    up = (rz * cir).where(close > open, 0.0)
    dn = (rz * (1.0 - cir)).where(close < open, 0.0)
    base = _mean(up - dn, 5)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_capitdepth_5d_jerk_v042_signal(open, high, low, close):
    rng = _f13_range(high, low)
    cir = _f13_close_in_range(high, low, close)
    cap = (rng * (1.0 - cir)).where(close < open, 0.0)
    base = _z(_mean(cap, 5), 252)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_blowoff_5d_jerk_v043_signal(open, high, low, close):
    rng = _f13_range(high, low)
    cir = _f13_close_in_range(high, low, close)
    bo = (rng * cir).where(close > open, 0.0)
    base = _z(_mean(bo, 5), 252)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_rngskew_5d_jerk_v044_signal(high, low, close):
    tr = _f13_range(high, low) / close.replace(0, np.nan)
    base = tr.rolling(63, min_periods=max(1,63//2)).skew()
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_insidebar_5d_jerk_v045_signal(high, low):
    rng = (high - low)
    prng = (high.shift(1) - low.shift(1)).replace(0, np.nan)
    inside = ((high < high.shift(1)) & (low > low.shift(1)))
    shrink = (1.0 - rng / prng).clip(lower=0).where(inside, 0.0)
    base = _mean(shrink, 5)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_wickvol_5d_jerk_v046_signal(open, high, low, close, volume):
    lw = _f13_lower_ratio(open, high, low, close)
    uw = _f13_upper_ratio(open, high, low, close)
    vz = _z(volume, 63)
    base = _mean((lw - uw) * vz, 5)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_bodyvolconf_5d_jerk_v047_signal(open, high, low, close, volume):
    br = _f13_body_ratio(open, high, low, close)
    vz = _z(volume, 63)
    base = _mean(br * vz, 5)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_voldirgap_5d_jerk_v048_signal(high, low, close):
    rng = _f13_range(high, low) / close.replace(0, np.nan)
    mv = close.pct_change().abs()
    base = _z(_mean(rng, 5), 252) - _z(_mean(mv, 5), 252)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_tightdepth_5d_jerk_v049_signal(high, low, close):
    tr = _f13_range(high, low) / close.replace(0, np.nan)
    med = tr.rolling(63, min_periods=max(1,63//2)).median().replace(0, np.nan)
    base = _mean((0.6 - tr / med).clip(lower=0), 5)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_wideover_5d_jerk_v050_signal(high, low, close):
    tr = _f13_range(high, low) / close.replace(0, np.nan)
    med = tr.rolling(63, min_periods=max(1,63//2)).median().replace(0, np.nan)
    base = _mean((tr / med - 2.0).clip(lower=0), 5)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_bodyratio_21d_jerk_v051_signal(open, high, low, close):
    base = _mean(_f13_body_ratio(open, high, low, close), 21)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_cir_21d_jerk_v052_signal(high, low, close):
    base = _mean(_f13_close_in_range(high, low, close), 21) - 0.5
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_uwick_21d_jerk_v053_signal(open, high, low, close):
    base = _mean(_f13_upper_ratio(open, high, low, close), 21)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_lwick_21d_jerk_v054_signal(open, high, low, close):
    base = _mean(_f13_lower_ratio(open, high, low, close), 21)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_wickskew_21d_jerk_v055_signal(open, high, low, close):
    lw = _f13_lower_ratio(open, high, low, close)
    uw = _f13_upper_ratio(open, high, low, close)
    base = _mean(lw - uw, 21)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_rngexp_21d_jerk_v056_signal(high, low):
    rng = _f13_range(high, low)
    base = _mean(rng, 21) / _mean(rng, 63).replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_atrpct_21d_jerk_v057_signal(high, low, close):
    tr = _f13_range(high, low) / close.replace(0, np.nan)
    base = _mean(tr, 21)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_thrust_21d_jerk_v058_signal(open, high, low, close):
    rng = _f13_range(high, low).replace(0, np.nan)
    base = _mean((close - open) / rng, 21)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_gapfade_21d_jerk_v059_signal(open, close):
    gap = open / close.shift(1).replace(0, np.nan) - 1.0
    intraday = close / open.replace(0, np.nan) - 1.0
    base = _mean(-np.sign(gap) * intraday, 21)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_rngconc_21d_jerk_v060_signal(high, low):
    rng = _f13_range(high, low)
    mx = rng.rolling(63, min_periods=max(1,63//2)).max()
    tot = rng.rolling(63, min_periods=max(1,63//2)).sum().replace(0, np.nan)
    base = mx / tot
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_cirema_21d_jerk_v061_signal(high, low, close):
    cir = _f13_close_in_range(high, low, close)
    base = cir.ewm(span=21, min_periods=max(5, 21//2)).mean() - 0.5
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_rngvsbody_21d_jerk_v062_signal(open, high, low, close):
    rng = _f13_range(high, low)
    body = _f13_body_abs(open, close)
    base = _mean((rng / body.replace(0, np.nan)).clip(upper=20.0), 21)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_decisive_21d_jerk_v063_signal(high, low, close):
    cir = _f13_close_in_range(high, low, close)
    base = _mean((cir - 0.5).abs(), 21)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_rngcv_21d_jerk_v064_signal(high, low, close):
    tr = _f13_range(high, low) / close.replace(0, np.nan)
    base = _std(tr, 21) / _mean(tr, 21).replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_bodyskew_21d_jerk_v065_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close)
    base = br.rolling(63, min_periods=max(1,63//2)).skew()
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_varratio_21d_jerk_v066_signal(high, low, close):
    cc = close.pct_change()
    ccv = _mean(cc ** 2, 21)
    lr = np.log(high.replace(0, np.nan) / low.replace(0, np.nan)) ** 2
    pkv = _mean(lr, 21) / (4.0 * np.log(2.0))
    base = ccv / pkv.replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_vwcir_21d_jerk_v067_signal(high, low, close, volume):
    cir = _f13_close_in_range(high, low, close)
    num = (cir * volume).rolling(21, min_periods=max(1,21//2)).sum()
    den = volume.rolling(21, min_periods=max(1,21//2)).sum().replace(0, np.nan)
    base = num / den - 0.5
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_bodydom_21d_jerk_v068_signal(open, close):
    body = (close - open)
    net = body.rolling(21, min_periods=max(1,21//2)).sum()
    gross = body.abs().rolling(21, min_periods=max(1,21//2)).sum().replace(0, np.nan)
    base = net / gross
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_wickshare_21d_jerk_v069_signal(open, high, low, close):
    uw = _f13_upper_wick(open, high, close)
    lw = _f13_lower_wick(open, low, close)
    rng = _f13_range(high, low)
    wsum = (uw + lw).rolling(21, min_periods=max(1,21//2)).sum()
    rsum = rng.rolling(21, min_periods=max(1,21//2)).sum().replace(0, np.nan)
    base = wsum / rsum
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_strongbody_21d_jerk_v070_signal(open, high, low, close):
    cir = _f13_close_in_range(high, low, close)
    br = _f13_body_ratio(open, high, low, close)
    base = _mean((cir - 0.5) * br, 21)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_maxshock_21d_jerk_v071_signal(high, low, close):
    rng = _f13_range(high, low)
    base = rng.rolling(21, min_periods=max(1,21//2)).max() / close.replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_rngeffic_21d_jerk_v072_signal(high, low, close):
    net = (close - close.shift(21)).abs()
    path = _f13_range(high, low).rolling(21, min_periods=max(1,21//2)).sum().replace(0, np.nan)
    base = net / path
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_rngmedmean_21d_jerk_v073_signal(high, low, close):
    tr = _f13_range(high, low) / close.replace(0, np.nan)
    med = tr.rolling(63, min_periods=max(1,63//2)).median()
    mn = _mean(tr, 63)
    base = (mn - med) / mn.replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_conviction_21d_jerk_v074_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close)
    maru = (br - 0.6).clip(lower=0)
    doji = (0.2 - br).clip(lower=0)
    base = _mean(maru - doji, 21)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_cirskew_21d_jerk_v075_signal(high, low, close):
    cir = _f13_close_in_range(high, low, close)
    base = cir.rolling(63, min_periods=max(1,63//2)).skew()
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_uwickdom_21d_jerk_v076_signal(open, high, low, close):
    uw = _f13_upper_ratio(open, high, low, close)
    lw = _f13_lower_ratio(open, high, low, close)
    base = _mean((uw - lw).clip(lower=0), 21)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_lwickdom_21d_jerk_v077_signal(open, high, low, close):
    uw = _f13_upper_ratio(open, high, low, close)
    lw = _f13_lower_ratio(open, high, low, close)
    base = _mean((lw - uw).clip(lower=0), 21)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_vwbody_21d_jerk_v078_signal(open, high, low, close, volume):
    br = _f13_body_ratio(open, high, low, close)
    num = (br * volume).rolling(21, min_periods=max(1,21//2)).sum()
    den = volume.rolling(21, min_periods=max(1,21//2)).sum().replace(0, np.nan)
    base = num / den
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_climaxz_21d_jerk_v079_signal(high, low, volume):
    rng = _f13_range(high, low)
    base = _mean(_z(rng, 63).clip(lower=0) * _z(volume, 63).clip(lower=0), 21)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_gapdom_21d_jerk_v080_signal(open, high, low, close):
    gap = (open - close.shift(1)).abs()
    intr = _f13_range(high, low)
    base = _mean(gap / (gap + intr).replace(0, np.nan), 21)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_widerev_21d_jerk_v081_signal(high, low, close):
    rng = _f13_range(high, low)
    rz = _z(rng, 63).clip(lower=0)
    cir = _f13_close_in_range(high, low, close)
    base = _mean(rz * (1.0 - (cir - 0.5).abs() * 2.0), 21)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_squeezemin_21d_jerk_v082_signal(high, low):
    rng = _f13_range(high, low)
    mn = rng.rolling(63, min_periods=max(1,63//2)).min()
    base = mn / _mean(rng, 63).replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_garmanklass_21d_jerk_v083_signal(open, high, low, close):
    hl = np.log(high.replace(0, np.nan) / low.replace(0, np.nan)) ** 2
    co = np.log(close.replace(0, np.nan) / open.replace(0, np.nan)) ** 2
    gk = 0.5 * hl - (2.0 * np.log(2.0) - 1.0) * co
    base = np.sqrt(_mean(gk, 21).clip(lower=0))
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_composite_21d_jerk_v084_signal(open, high, low, close, volume):
    br = _f13_body_ratio(open, high, low, close)
    cir = _f13_close_in_range(high, low, close)
    vz = _z(volume, 63)
    base = _mean(br * (cir - 0.5) * np.tanh(vz), 21)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_effortresult_21d_jerk_v085_signal(high, low, close, volume):
    rng = _f13_range(high, low) / close.replace(0, np.nan)
    eff = volume / rng.replace(0, np.nan)
    base = _z(_mean(eff, 21), 252)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_closeoverrng_21d_jerk_v086_signal(high, low, close):
    chg = close.diff()
    rng = _f13_range(high, low).replace(0, np.nan)
    base = _mean(chg / rng, 21)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_gapmag_21d_jerk_v087_signal(open, close):
    gap = (open - close.shift(1)).abs() / close.shift(1).replace(0, np.nan)
    base = _z(_mean(gap, 21), 252)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_ovnratio_21d_jerk_v088_signal(high, low, close):
    cc = close.pct_change().abs()
    rng = _f13_range(high, low) / close.replace(0, np.nan)
    base = _mean(cc, 21) / _mean(rng, 21).replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_wicklograt_21d_jerk_v089_signal(open, high, low, close):
    uw = _f13_upper_wick(open, high, close)
    lw = _f13_lower_wick(open, low, close)
    base = _mean(np.log((lw + 1e-6) / (uw + 1e-6)), 21)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_rngbodydiverge_21d_jerk_v090_signal(open, high, low, close):
    rng = _f13_range(high, low)
    body = _f13_body_abs(open, close)
    rex = _mean(rng, 21) / _mean(rng, 252).replace(0, np.nan)
    bex = _mean(body, 21) / _mean(body, 252).replace(0, np.nan)
    base = rex - bex
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_climaxbias_21d_jerk_v091_signal(open, high, low, close):
    rng = _f13_range(high, low)
    rz = _z(rng, 63).clip(lower=0)
    cir = _f13_close_in_range(high, low, close)
    up = (rz * cir).where(close > open, 0.0)
    dn = (rz * (1.0 - cir)).where(close < open, 0.0)
    base = _mean(up - dn, 21)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_capitdepth_21d_jerk_v092_signal(open, high, low, close):
    rng = _f13_range(high, low)
    cir = _f13_close_in_range(high, low, close)
    cap = (rng * (1.0 - cir)).where(close < open, 0.0)
    base = _z(_mean(cap, 21), 252)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_blowoff_21d_jerk_v093_signal(open, high, low, close):
    rng = _f13_range(high, low)
    cir = _f13_close_in_range(high, low, close)
    bo = (rng * cir).where(close > open, 0.0)
    base = _z(_mean(bo, 21), 252)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_rngskew_21d_jerk_v094_signal(high, low, close):
    tr = _f13_range(high, low) / close.replace(0, np.nan)
    base = tr.rolling(63, min_periods=max(1,63//2)).skew()
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_insidebar_21d_jerk_v095_signal(high, low):
    rng = (high - low)
    prng = (high.shift(1) - low.shift(1)).replace(0, np.nan)
    inside = ((high < high.shift(1)) & (low > low.shift(1)))
    shrink = (1.0 - rng / prng).clip(lower=0).where(inside, 0.0)
    base = _mean(shrink, 21)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_wickvol_21d_jerk_v096_signal(open, high, low, close, volume):
    lw = _f13_lower_ratio(open, high, low, close)
    uw = _f13_upper_ratio(open, high, low, close)
    vz = _z(volume, 63)
    base = _mean((lw - uw) * vz, 21)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_bodyvolconf_21d_jerk_v097_signal(open, high, low, close, volume):
    br = _f13_body_ratio(open, high, low, close)
    vz = _z(volume, 63)
    base = _mean(br * vz, 21)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_voldirgap_21d_jerk_v098_signal(high, low, close):
    rng = _f13_range(high, low) / close.replace(0, np.nan)
    mv = close.pct_change().abs()
    base = _z(_mean(rng, 21), 252) - _z(_mean(mv, 21), 252)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_tightdepth_21d_jerk_v099_signal(high, low, close):
    tr = _f13_range(high, low) / close.replace(0, np.nan)
    med = tr.rolling(63, min_periods=max(1,63//2)).median().replace(0, np.nan)
    base = _mean((0.6 - tr / med).clip(lower=0), 21)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_wideover_21d_jerk_v100_signal(high, low, close):
    tr = _f13_range(high, low) / close.replace(0, np.nan)
    med = tr.rolling(63, min_periods=max(1,63//2)).median().replace(0, np.nan)
    base = _mean((tr / med - 2.0).clip(lower=0), 21)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_bodyratio_63d_jerk_v101_signal(open, high, low, close):
    base = _mean(_f13_body_ratio(open, high, low, close), 63)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_cir_63d_jerk_v102_signal(high, low, close):
    base = _mean(_f13_close_in_range(high, low, close), 63) - 0.5
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_uwick_63d_jerk_v103_signal(open, high, low, close):
    base = _mean(_f13_upper_ratio(open, high, low, close), 63)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_lwick_63d_jerk_v104_signal(open, high, low, close):
    base = _mean(_f13_lower_ratio(open, high, low, close), 63)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_wickskew_63d_jerk_v105_signal(open, high, low, close):
    lw = _f13_lower_ratio(open, high, low, close)
    uw = _f13_upper_ratio(open, high, low, close)
    base = _mean(lw - uw, 63)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_rngexp_63d_jerk_v106_signal(high, low):
    rng = _f13_range(high, low)
    base = _mean(rng, 63) / _mean(rng, 126).replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_atrpct_63d_jerk_v107_signal(high, low, close):
    tr = _f13_range(high, low) / close.replace(0, np.nan)
    base = _mean(tr, 63)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_thrust_63d_jerk_v108_signal(open, high, low, close):
    rng = _f13_range(high, low).replace(0, np.nan)
    base = _mean((close - open) / rng, 63)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_gapfade_63d_jerk_v109_signal(open, close):
    gap = open / close.shift(1).replace(0, np.nan) - 1.0
    intraday = close / open.replace(0, np.nan) - 1.0
    base = _mean(-np.sign(gap) * intraday, 63)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_rngconc_63d_jerk_v110_signal(high, low):
    rng = _f13_range(high, low)
    mx = rng.rolling(126, min_periods=max(1,126//2)).max()
    tot = rng.rolling(126, min_periods=max(1,126//2)).sum().replace(0, np.nan)
    base = mx / tot
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_cirema_63d_jerk_v111_signal(high, low, close):
    cir = _f13_close_in_range(high, low, close)
    base = cir.ewm(span=63, min_periods=max(5, 63//2)).mean() - 0.5
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_rngvsbody_63d_jerk_v112_signal(open, high, low, close):
    rng = _f13_range(high, low)
    body = _f13_body_abs(open, close)
    base = _mean((rng / body.replace(0, np.nan)).clip(upper=20.0), 63)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_decisive_63d_jerk_v113_signal(high, low, close):
    cir = _f13_close_in_range(high, low, close)
    base = _mean((cir - 0.5).abs(), 63)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_rngcv_63d_jerk_v114_signal(high, low, close):
    tr = _f13_range(high, low) / close.replace(0, np.nan)
    base = _std(tr, 63) / _mean(tr, 63).replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_bodyskew_63d_jerk_v115_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close)
    base = br.rolling(126, min_periods=max(1,126//2)).skew()
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_varratio_63d_jerk_v116_signal(high, low, close):
    cc = close.pct_change()
    ccv = _mean(cc ** 2, 63)
    lr = np.log(high.replace(0, np.nan) / low.replace(0, np.nan)) ** 2
    pkv = _mean(lr, 63) / (4.0 * np.log(2.0))
    base = ccv / pkv.replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_vwcir_63d_jerk_v117_signal(high, low, close, volume):
    cir = _f13_close_in_range(high, low, close)
    num = (cir * volume).rolling(63, min_periods=max(1,63//2)).sum()
    den = volume.rolling(63, min_periods=max(1,63//2)).sum().replace(0, np.nan)
    base = num / den - 0.5
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_bodydom_63d_jerk_v118_signal(open, close):
    body = (close - open)
    net = body.rolling(63, min_periods=max(1,63//2)).sum()
    gross = body.abs().rolling(63, min_periods=max(1,63//2)).sum().replace(0, np.nan)
    base = net / gross
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_wickshare_63d_jerk_v119_signal(open, high, low, close):
    uw = _f13_upper_wick(open, high, close)
    lw = _f13_lower_wick(open, low, close)
    rng = _f13_range(high, low)
    wsum = (uw + lw).rolling(63, min_periods=max(1,63//2)).sum()
    rsum = rng.rolling(63, min_periods=max(1,63//2)).sum().replace(0, np.nan)
    base = wsum / rsum
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_strongbody_63d_jerk_v120_signal(open, high, low, close):
    cir = _f13_close_in_range(high, low, close)
    br = _f13_body_ratio(open, high, low, close)
    base = _mean((cir - 0.5) * br, 63)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_maxshock_63d_jerk_v121_signal(high, low, close):
    rng = _f13_range(high, low)
    base = rng.rolling(63, min_periods=max(1,63//2)).max() / close.replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_rngeffic_63d_jerk_v122_signal(high, low, close):
    net = (close - close.shift(63)).abs()
    path = _f13_range(high, low).rolling(63, min_periods=max(1,63//2)).sum().replace(0, np.nan)
    base = net / path
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_rngmedmean_63d_jerk_v123_signal(high, low, close):
    tr = _f13_range(high, low) / close.replace(0, np.nan)
    med = tr.rolling(126, min_periods=max(1,126//2)).median()
    mn = _mean(tr, 126)
    base = (mn - med) / mn.replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_conviction_63d_jerk_v124_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close)
    maru = (br - 0.6).clip(lower=0)
    doji = (0.2 - br).clip(lower=0)
    base = _mean(maru - doji, 63)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_cirskew_63d_jerk_v125_signal(high, low, close):
    cir = _f13_close_in_range(high, low, close)
    base = cir.rolling(126, min_periods=max(1,126//2)).skew()
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_uwickdom_63d_jerk_v126_signal(open, high, low, close):
    uw = _f13_upper_ratio(open, high, low, close)
    lw = _f13_lower_ratio(open, high, low, close)
    base = _mean((uw - lw).clip(lower=0), 63)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_lwickdom_63d_jerk_v127_signal(open, high, low, close):
    uw = _f13_upper_ratio(open, high, low, close)
    lw = _f13_lower_ratio(open, high, low, close)
    base = _mean((lw - uw).clip(lower=0), 63)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_vwbody_63d_jerk_v128_signal(open, high, low, close, volume):
    br = _f13_body_ratio(open, high, low, close)
    num = (br * volume).rolling(63, min_periods=max(1,63//2)).sum()
    den = volume.rolling(63, min_periods=max(1,63//2)).sum().replace(0, np.nan)
    base = num / den
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_climaxz_63d_jerk_v129_signal(high, low, volume):
    rng = _f13_range(high, low)
    base = _mean(_z(rng, 126).clip(lower=0) * _z(volume, 126).clip(lower=0), 63)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_gapdom_63d_jerk_v130_signal(open, high, low, close):
    gap = (open - close.shift(1)).abs()
    intr = _f13_range(high, low)
    base = _mean(gap / (gap + intr).replace(0, np.nan), 63)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_widerev_63d_jerk_v131_signal(high, low, close):
    rng = _f13_range(high, low)
    rz = _z(rng, 126).clip(lower=0)
    cir = _f13_close_in_range(high, low, close)
    base = _mean(rz * (1.0 - (cir - 0.5).abs() * 2.0), 63)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_squeezemin_63d_jerk_v132_signal(high, low):
    rng = _f13_range(high, low)
    mn = rng.rolling(126, min_periods=max(1,126//2)).min()
    base = mn / _mean(rng, 126).replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_garmanklass_63d_jerk_v133_signal(open, high, low, close):
    hl = np.log(high.replace(0, np.nan) / low.replace(0, np.nan)) ** 2
    co = np.log(close.replace(0, np.nan) / open.replace(0, np.nan)) ** 2
    gk = 0.5 * hl - (2.0 * np.log(2.0) - 1.0) * co
    base = np.sqrt(_mean(gk, 63).clip(lower=0))
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_composite_63d_jerk_v134_signal(open, high, low, close, volume):
    br = _f13_body_ratio(open, high, low, close)
    cir = _f13_close_in_range(high, low, close)
    vz = _z(volume, 126)
    base = _mean(br * (cir - 0.5) * np.tanh(vz), 63)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_effortresult_63d_jerk_v135_signal(high, low, close, volume):
    rng = _f13_range(high, low) / close.replace(0, np.nan)
    eff = volume / rng.replace(0, np.nan)
    base = _z(_mean(eff, 63), 504)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_closeoverrng_63d_jerk_v136_signal(high, low, close):
    chg = close.diff()
    rng = _f13_range(high, low).replace(0, np.nan)
    base = _mean(chg / rng, 63)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_gapmag_63d_jerk_v137_signal(open, close):
    gap = (open - close.shift(1)).abs() / close.shift(1).replace(0, np.nan)
    base = _z(_mean(gap, 63), 504)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_ovnratio_63d_jerk_v138_signal(high, low, close):
    cc = close.pct_change().abs()
    rng = _f13_range(high, low) / close.replace(0, np.nan)
    base = _mean(cc, 63) / _mean(rng, 63).replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_wicklograt_63d_jerk_v139_signal(open, high, low, close):
    uw = _f13_upper_wick(open, high, close)
    lw = _f13_lower_wick(open, low, close)
    base = _mean(np.log((lw + 1e-6) / (uw + 1e-6)), 63)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_rngbodydiverge_63d_jerk_v140_signal(open, high, low, close):
    rng = _f13_range(high, low)
    body = _f13_body_abs(open, close)
    rex = _mean(rng, 63) / _mean(rng, 504).replace(0, np.nan)
    bex = _mean(body, 63) / _mean(body, 504).replace(0, np.nan)
    base = rex - bex
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_climaxbias_63d_jerk_v141_signal(open, high, low, close):
    rng = _f13_range(high, low)
    rz = _z(rng, 126).clip(lower=0)
    cir = _f13_close_in_range(high, low, close)
    up = (rz * cir).where(close > open, 0.0)
    dn = (rz * (1.0 - cir)).where(close < open, 0.0)
    base = _mean(up - dn, 63)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_capitdepth_63d_jerk_v142_signal(open, high, low, close):
    rng = _f13_range(high, low)
    cir = _f13_close_in_range(high, low, close)
    cap = (rng * (1.0 - cir)).where(close < open, 0.0)
    base = _z(_mean(cap, 63), 504)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_blowoff_63d_jerk_v143_signal(open, high, low, close):
    rng = _f13_range(high, low)
    cir = _f13_close_in_range(high, low, close)
    bo = (rng * cir).where(close > open, 0.0)
    base = _z(_mean(bo, 63), 504)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_rngskew_63d_jerk_v144_signal(high, low, close):
    tr = _f13_range(high, low) / close.replace(0, np.nan)
    base = tr.rolling(126, min_periods=max(1,126//2)).skew()
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_insidebar_63d_jerk_v145_signal(high, low):
    rng = (high - low)
    prng = (high.shift(1) - low.shift(1)).replace(0, np.nan)
    inside = ((high < high.shift(1)) & (low > low.shift(1)))
    shrink = (1.0 - rng / prng).clip(lower=0).where(inside, 0.0)
    base = _mean(shrink, 63)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_wickvol_63d_jerk_v146_signal(open, high, low, close, volume):
    lw = _f13_lower_ratio(open, high, low, close)
    uw = _f13_upper_ratio(open, high, low, close)
    vz = _z(volume, 126)
    base = _mean((lw - uw) * vz, 63)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_bodyvolconf_63d_jerk_v147_signal(open, high, low, close, volume):
    br = _f13_body_ratio(open, high, low, close)
    vz = _z(volume, 126)
    base = _mean(br * vz, 63)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_voldirgap_63d_jerk_v148_signal(high, low, close):
    rng = _f13_range(high, low) / close.replace(0, np.nan)
    mv = close.pct_change().abs()
    base = _z(_mean(rng, 63), 504) - _z(_mean(mv, 63), 504)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_tightdepth_63d_jerk_v149_signal(high, low, close):
    tr = _f13_range(high, low) / close.replace(0, np.nan)
    med = tr.rolling(126, min_periods=max(1,126//2)).median().replace(0, np.nan)
    base = _mean((0.6 - tr / med).clip(lower=0), 63)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f13cr_f13_candle_range_structure_wideover_63d_jerk_v150_signal(high, low, close):
    tr = _f13_range(high, low) / close.replace(0, np.nan)
    med = tr.rolling(126, min_periods=max(1,126//2)).median().replace(0, np.nan)
    base = _mean((tr / med - 2.0).clip(lower=0), 63)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f13cr_f13_candle_range_structure_bodyratio_5d_jerk_v001_signal,
    f13cr_f13_candle_range_structure_cir_5d_jerk_v002_signal,
    f13cr_f13_candle_range_structure_uwick_5d_jerk_v003_signal,
    f13cr_f13_candle_range_structure_lwick_5d_jerk_v004_signal,
    f13cr_f13_candle_range_structure_wickskew_5d_jerk_v005_signal,
    f13cr_f13_candle_range_structure_rngexp_5d_jerk_v006_signal,
    f13cr_f13_candle_range_structure_atrpct_5d_jerk_v007_signal,
    f13cr_f13_candle_range_structure_thrust_5d_jerk_v008_signal,
    f13cr_f13_candle_range_structure_gapfade_5d_jerk_v009_signal,
    f13cr_f13_candle_range_structure_rngconc_5d_jerk_v010_signal,
    f13cr_f13_candle_range_structure_cirema_5d_jerk_v011_signal,
    f13cr_f13_candle_range_structure_rngvsbody_5d_jerk_v012_signal,
    f13cr_f13_candle_range_structure_decisive_5d_jerk_v013_signal,
    f13cr_f13_candle_range_structure_rngcv_5d_jerk_v014_signal,
    f13cr_f13_candle_range_structure_bodyskew_5d_jerk_v015_signal,
    f13cr_f13_candle_range_structure_varratio_5d_jerk_v016_signal,
    f13cr_f13_candle_range_structure_vwcir_5d_jerk_v017_signal,
    f13cr_f13_candle_range_structure_bodydom_5d_jerk_v018_signal,
    f13cr_f13_candle_range_structure_wickshare_5d_jerk_v019_signal,
    f13cr_f13_candle_range_structure_strongbody_5d_jerk_v020_signal,
    f13cr_f13_candle_range_structure_maxshock_5d_jerk_v021_signal,
    f13cr_f13_candle_range_structure_rngeffic_5d_jerk_v022_signal,
    f13cr_f13_candle_range_structure_rngmedmean_5d_jerk_v023_signal,
    f13cr_f13_candle_range_structure_conviction_5d_jerk_v024_signal,
    f13cr_f13_candle_range_structure_cirskew_5d_jerk_v025_signal,
    f13cr_f13_candle_range_structure_uwickdom_5d_jerk_v026_signal,
    f13cr_f13_candle_range_structure_lwickdom_5d_jerk_v027_signal,
    f13cr_f13_candle_range_structure_vwbody_5d_jerk_v028_signal,
    f13cr_f13_candle_range_structure_climaxz_5d_jerk_v029_signal,
    f13cr_f13_candle_range_structure_gapdom_5d_jerk_v030_signal,
    f13cr_f13_candle_range_structure_widerev_5d_jerk_v031_signal,
    f13cr_f13_candle_range_structure_squeezemin_5d_jerk_v032_signal,
    f13cr_f13_candle_range_structure_garmanklass_5d_jerk_v033_signal,
    f13cr_f13_candle_range_structure_composite_5d_jerk_v034_signal,
    f13cr_f13_candle_range_structure_effortresult_5d_jerk_v035_signal,
    f13cr_f13_candle_range_structure_closeoverrng_5d_jerk_v036_signal,
    f13cr_f13_candle_range_structure_gapmag_5d_jerk_v037_signal,
    f13cr_f13_candle_range_structure_ovnratio_5d_jerk_v038_signal,
    f13cr_f13_candle_range_structure_wicklograt_5d_jerk_v039_signal,
    f13cr_f13_candle_range_structure_rngbodydiverge_5d_jerk_v040_signal,
    f13cr_f13_candle_range_structure_climaxbias_5d_jerk_v041_signal,
    f13cr_f13_candle_range_structure_capitdepth_5d_jerk_v042_signal,
    f13cr_f13_candle_range_structure_blowoff_5d_jerk_v043_signal,
    f13cr_f13_candle_range_structure_rngskew_5d_jerk_v044_signal,
    f13cr_f13_candle_range_structure_insidebar_5d_jerk_v045_signal,
    f13cr_f13_candle_range_structure_wickvol_5d_jerk_v046_signal,
    f13cr_f13_candle_range_structure_bodyvolconf_5d_jerk_v047_signal,
    f13cr_f13_candle_range_structure_voldirgap_5d_jerk_v048_signal,
    f13cr_f13_candle_range_structure_tightdepth_5d_jerk_v049_signal,
    f13cr_f13_candle_range_structure_wideover_5d_jerk_v050_signal,
    f13cr_f13_candle_range_structure_bodyratio_21d_jerk_v051_signal,
    f13cr_f13_candle_range_structure_cir_21d_jerk_v052_signal,
    f13cr_f13_candle_range_structure_uwick_21d_jerk_v053_signal,
    f13cr_f13_candle_range_structure_lwick_21d_jerk_v054_signal,
    f13cr_f13_candle_range_structure_wickskew_21d_jerk_v055_signal,
    f13cr_f13_candle_range_structure_rngexp_21d_jerk_v056_signal,
    f13cr_f13_candle_range_structure_atrpct_21d_jerk_v057_signal,
    f13cr_f13_candle_range_structure_thrust_21d_jerk_v058_signal,
    f13cr_f13_candle_range_structure_gapfade_21d_jerk_v059_signal,
    f13cr_f13_candle_range_structure_rngconc_21d_jerk_v060_signal,
    f13cr_f13_candle_range_structure_cirema_21d_jerk_v061_signal,
    f13cr_f13_candle_range_structure_rngvsbody_21d_jerk_v062_signal,
    f13cr_f13_candle_range_structure_decisive_21d_jerk_v063_signal,
    f13cr_f13_candle_range_structure_rngcv_21d_jerk_v064_signal,
    f13cr_f13_candle_range_structure_bodyskew_21d_jerk_v065_signal,
    f13cr_f13_candle_range_structure_varratio_21d_jerk_v066_signal,
    f13cr_f13_candle_range_structure_vwcir_21d_jerk_v067_signal,
    f13cr_f13_candle_range_structure_bodydom_21d_jerk_v068_signal,
    f13cr_f13_candle_range_structure_wickshare_21d_jerk_v069_signal,
    f13cr_f13_candle_range_structure_strongbody_21d_jerk_v070_signal,
    f13cr_f13_candle_range_structure_maxshock_21d_jerk_v071_signal,
    f13cr_f13_candle_range_structure_rngeffic_21d_jerk_v072_signal,
    f13cr_f13_candle_range_structure_rngmedmean_21d_jerk_v073_signal,
    f13cr_f13_candle_range_structure_conviction_21d_jerk_v074_signal,
    f13cr_f13_candle_range_structure_cirskew_21d_jerk_v075_signal,
    f13cr_f13_candle_range_structure_uwickdom_21d_jerk_v076_signal,
    f13cr_f13_candle_range_structure_lwickdom_21d_jerk_v077_signal,
    f13cr_f13_candle_range_structure_vwbody_21d_jerk_v078_signal,
    f13cr_f13_candle_range_structure_climaxz_21d_jerk_v079_signal,
    f13cr_f13_candle_range_structure_gapdom_21d_jerk_v080_signal,
    f13cr_f13_candle_range_structure_widerev_21d_jerk_v081_signal,
    f13cr_f13_candle_range_structure_squeezemin_21d_jerk_v082_signal,
    f13cr_f13_candle_range_structure_garmanklass_21d_jerk_v083_signal,
    f13cr_f13_candle_range_structure_composite_21d_jerk_v084_signal,
    f13cr_f13_candle_range_structure_effortresult_21d_jerk_v085_signal,
    f13cr_f13_candle_range_structure_closeoverrng_21d_jerk_v086_signal,
    f13cr_f13_candle_range_structure_gapmag_21d_jerk_v087_signal,
    f13cr_f13_candle_range_structure_ovnratio_21d_jerk_v088_signal,
    f13cr_f13_candle_range_structure_wicklograt_21d_jerk_v089_signal,
    f13cr_f13_candle_range_structure_rngbodydiverge_21d_jerk_v090_signal,
    f13cr_f13_candle_range_structure_climaxbias_21d_jerk_v091_signal,
    f13cr_f13_candle_range_structure_capitdepth_21d_jerk_v092_signal,
    f13cr_f13_candle_range_structure_blowoff_21d_jerk_v093_signal,
    f13cr_f13_candle_range_structure_rngskew_21d_jerk_v094_signal,
    f13cr_f13_candle_range_structure_insidebar_21d_jerk_v095_signal,
    f13cr_f13_candle_range_structure_wickvol_21d_jerk_v096_signal,
    f13cr_f13_candle_range_structure_bodyvolconf_21d_jerk_v097_signal,
    f13cr_f13_candle_range_structure_voldirgap_21d_jerk_v098_signal,
    f13cr_f13_candle_range_structure_tightdepth_21d_jerk_v099_signal,
    f13cr_f13_candle_range_structure_wideover_21d_jerk_v100_signal,
    f13cr_f13_candle_range_structure_bodyratio_63d_jerk_v101_signal,
    f13cr_f13_candle_range_structure_cir_63d_jerk_v102_signal,
    f13cr_f13_candle_range_structure_uwick_63d_jerk_v103_signal,
    f13cr_f13_candle_range_structure_lwick_63d_jerk_v104_signal,
    f13cr_f13_candle_range_structure_wickskew_63d_jerk_v105_signal,
    f13cr_f13_candle_range_structure_rngexp_63d_jerk_v106_signal,
    f13cr_f13_candle_range_structure_atrpct_63d_jerk_v107_signal,
    f13cr_f13_candle_range_structure_thrust_63d_jerk_v108_signal,
    f13cr_f13_candle_range_structure_gapfade_63d_jerk_v109_signal,
    f13cr_f13_candle_range_structure_rngconc_63d_jerk_v110_signal,
    f13cr_f13_candle_range_structure_cirema_63d_jerk_v111_signal,
    f13cr_f13_candle_range_structure_rngvsbody_63d_jerk_v112_signal,
    f13cr_f13_candle_range_structure_decisive_63d_jerk_v113_signal,
    f13cr_f13_candle_range_structure_rngcv_63d_jerk_v114_signal,
    f13cr_f13_candle_range_structure_bodyskew_63d_jerk_v115_signal,
    f13cr_f13_candle_range_structure_varratio_63d_jerk_v116_signal,
    f13cr_f13_candle_range_structure_vwcir_63d_jerk_v117_signal,
    f13cr_f13_candle_range_structure_bodydom_63d_jerk_v118_signal,
    f13cr_f13_candle_range_structure_wickshare_63d_jerk_v119_signal,
    f13cr_f13_candle_range_structure_strongbody_63d_jerk_v120_signal,
    f13cr_f13_candle_range_structure_maxshock_63d_jerk_v121_signal,
    f13cr_f13_candle_range_structure_rngeffic_63d_jerk_v122_signal,
    f13cr_f13_candle_range_structure_rngmedmean_63d_jerk_v123_signal,
    f13cr_f13_candle_range_structure_conviction_63d_jerk_v124_signal,
    f13cr_f13_candle_range_structure_cirskew_63d_jerk_v125_signal,
    f13cr_f13_candle_range_structure_uwickdom_63d_jerk_v126_signal,
    f13cr_f13_candle_range_structure_lwickdom_63d_jerk_v127_signal,
    f13cr_f13_candle_range_structure_vwbody_63d_jerk_v128_signal,
    f13cr_f13_candle_range_structure_climaxz_63d_jerk_v129_signal,
    f13cr_f13_candle_range_structure_gapdom_63d_jerk_v130_signal,
    f13cr_f13_candle_range_structure_widerev_63d_jerk_v131_signal,
    f13cr_f13_candle_range_structure_squeezemin_63d_jerk_v132_signal,
    f13cr_f13_candle_range_structure_garmanklass_63d_jerk_v133_signal,
    f13cr_f13_candle_range_structure_composite_63d_jerk_v134_signal,
    f13cr_f13_candle_range_structure_effortresult_63d_jerk_v135_signal,
    f13cr_f13_candle_range_structure_closeoverrng_63d_jerk_v136_signal,
    f13cr_f13_candle_range_structure_gapmag_63d_jerk_v137_signal,
    f13cr_f13_candle_range_structure_ovnratio_63d_jerk_v138_signal,
    f13cr_f13_candle_range_structure_wicklograt_63d_jerk_v139_signal,
    f13cr_f13_candle_range_structure_rngbodydiverge_63d_jerk_v140_signal,
    f13cr_f13_candle_range_structure_climaxbias_63d_jerk_v141_signal,
    f13cr_f13_candle_range_structure_capitdepth_63d_jerk_v142_signal,
    f13cr_f13_candle_range_structure_blowoff_63d_jerk_v143_signal,
    f13cr_f13_candle_range_structure_rngskew_63d_jerk_v144_signal,
    f13cr_f13_candle_range_structure_insidebar_63d_jerk_v145_signal,
    f13cr_f13_candle_range_structure_wickvol_63d_jerk_v146_signal,
    f13cr_f13_candle_range_structure_bodyvolconf_63d_jerk_v147_signal,
    f13cr_f13_candle_range_structure_voldirgap_63d_jerk_v148_signal,
    f13cr_f13_candle_range_structure_tightdepth_63d_jerk_v149_signal,
    f13cr_f13_candle_range_structure_wideover_63d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F13_CANDLE_RANGE_STRUCTURE_REGISTRY_001_150 = REGISTRY


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

    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), "nan_ok=%d/%d" % (nan_ok, n_features)

    items = list(results.items())
    for i in range(len(items)):
        ni, si = items[i]
        ai = si.dropna()
        for j in range(i + 1, len(items)):
            nj, sj = items[j]
            aj = sj.dropna()
            ix = ai.index.intersection(aj.index)
            if len(ix) < 30:
                continue
            c = ai.loc[ix].corr(aj.loc[ix])
            if c is None or np.isnan(c):
                continue
            assert abs(c) <= 0.97, "CORR %s vs %s = %.4f" % (ni, nj, c)

    print("OK f13_candle_range_structure_3rd_derivatives_001_150_claude: %d features pass" % n_features)
