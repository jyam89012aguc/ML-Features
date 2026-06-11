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


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


def _corr(a, b, w):
    return a.rolling(w, min_periods=max(2, w // 2)).corr(b)


# ===== folder domain primitives (volume-price confirmation) =====
def _f15_obv(close, volume):
    # On-balance volume: signed cumulative volume by price direction.
    direction = np.sign(close.diff())
    return (direction * volume).fillna(0.0).cumsum()


def _f15_signed_dollar(closeadj, volume):
    # Signed dollar-volume flow by price direction (closeadj for >21d aggregation).
    direction = np.sign(closeadj.diff())
    return (direction * closeadj * volume).fillna(0.0).cumsum()


def _f15_clv(close, high, low):
    # Close location value within the bar's range (-1..+1).
    rng = (high - low).replace(0, np.nan)
    return ((close - low) - (high - close)) / rng


def _f15_adline(close, high, low, volume):
    # Accumulation/Distribution line: cumulative money-flow volume.
    mfv = _f15_clv(close, high, low) * volume
    return mfv.fillna(0.0).cumsum()


def _f15_cmf(close, high, low, volume, w):
    # Chaikin money flow: w-day money-flow volume / total volume.
    mfv = _f15_clv(close, high, low) * volume
    num = mfv.rolling(w, min_periods=max(2, w // 2)).sum()
    den = volume.rolling(w, min_periods=max(2, w // 2)).sum().replace(0, np.nan)
    return num / den


def _f15_typ(close, high, low):
    return (high + low + close) / 3.0


def _f15_mfi(close, high, low, volume, w):
    # Money-flow index: RSI of typical-price-weighted dollar volume.
    tp = _f15_typ(close, high, low)
    rmf = tp * volume
    up = rmf.where(tp.diff() > 0, 0.0)
    dn = rmf.where(tp.diff() < 0, 0.0)
    pos = up.rolling(w, min_periods=max(2, w // 2)).sum()
    neg = dn.rolling(w, min_periods=max(2, w // 2)).sum().replace(0, np.nan)
    ratio = pos / neg
    return 100.0 - 100.0 / (1.0 + ratio)


def _f15_force(closeadj, volume, w):
    # Elder force index: price change * volume, EMA-smoothed.
    fi = closeadj.diff() * volume
    return fi.ewm(span=w, min_periods=max(2, w // 2)).mean()


def _f15_updownvol(close, volume, w):
    # Up-volume minus down-volume share over window.
    up = volume.where(close.diff() > 0, 0.0)
    dn = volume.where(close.diff() < 0, 0.0)
    su = up.rolling(w, min_periods=max(2, w // 2)).sum()
    sd = dn.rolling(w, min_periods=max(2, w // 2)).sum()
    tot = (su + sd).replace(0, np.nan)
    return (su - sd) / tot


def _f15_pvt(closeadj, volume):
    # Price-volume trend: cumulative volume weighted by pct return.
    return (closeadj.pct_change() * volume).fillna(0.0).cumsum()


def _f15_eom(closeadj, high, low, volume, w):
    # Ease of movement: price midpoint move per unit dollar volume.
    mid = (high + low) / 2.0
    box = volume / (high - low).replace(0, np.nan)
    raw = mid.diff() / box.replace(0, np.nan)
    return raw.rolling(w, min_periods=max(2, w // 2)).mean()


def _f15_slope(s, w):
    # Normalized log-slope of a cumulative line over w days.
    return (s - s.shift(w)) / (s.abs().rolling(w, min_periods=max(2, w // 2)).mean().replace(0, np.nan) * w)


# ============================================================
# OBV slope over a quarter, normalized by typical OBV magnitude
def f15vc_f15_volume_price_confirmation_obvslope_63d_base_v001_signal(close, volume):
    obv = _f15_obv(close, volume)
    b = _f15_slope(obv, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV slope over a half-year
def f15vc_f15_volume_price_confirmation_obvslope_126d_base_v002_signal(close, volume):
    obv = _f15_obv(close, volume)
    b = _f15_slope(obv, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV z-score vs its own 126d history (accumulation extremity)
def f15vc_f15_volume_price_confirmation_obvz_126d_base_v003_signal(close, volume):
    obv = _f15_obv(close, volume)
    b = _z(obv, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV detrended: OBV minus its 63d mean, scaled by 63d vol
def f15vc_f15_volume_price_confirmation_obvdetr_63d_base_v004_signal(close, volume):
    obv = _f15_obv(close, volume)
    b = (obv - _mean(obv, 63)) / _std(obv, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV momentum: 21d change minus 63d change (short vs long accumulation)
def f15vc_f15_volume_price_confirmation_obvmom_base_v005_signal(close, volume):
    obv = _f15_obv(close, volume)
    short = (obv - obv.shift(21)) / 21.0
    long = (obv - obv.shift(63)) / 63.0
    scale = obv.abs().rolling(63, min_periods=21).mean().replace(0, np.nan)
    b = (short - long) / scale
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV slope per unit price slope (volume confirmation of trend)
def f15vc_f15_volume_price_confirmation_obvconf_63d_base_v006_signal(close, closeadj, volume):
    obv = _f15_obv(close, volume)
    obv_sl = _f15_slope(obv, 63)
    px_sl = (closeadj - closeadj.shift(63)) / (closeadj.rolling(63, min_periods=21).mean().replace(0, np.nan) * 63)
    b = obv_sl - px_sl
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV-price divergence: sign disagreement of OBV slope vs price slope, magnitude-weighted
def f15vc_f15_volume_price_confirmation_obvdiv_63d_base_v007_signal(close, closeadj, volume):
    obv = _f15_obv(close, volume)
    obv_sl = _z(_f15_slope(obv, 63), 126)
    px_sl = _z((closeadj - closeadj.shift(63)) / 63.0, 126)
    b = px_sl - obv_sl
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rank of OBV slope vs its own 252d history
def f15vc_f15_volume_price_confirmation_obvslrank_63d_base_v008_signal(close, volume):
    obv = _f15_obv(close, volume)
    sl = _f15_slope(obv, 63)
    b = _rank(sl, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV new-high persistence: fraction of last quarter OBV set a 126d high
def f15vc_f15_volume_price_confirmation_obvnewhi_base_v009_signal(close, volume):
    obv = _f15_obv(close, volume)
    hi = obv.rolling(126, min_periods=63).max()
    is_hi = (obv >= hi * 0.99999).astype(float)
    b = is_hi.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# A/D line slope over a quarter
def f15vc_f15_volume_price_confirmation_adslope_63d_base_v010_signal(close, high, low, volume):
    ad = _f15_adline(close, high, low, volume)
    b = _f15_slope(ad, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# A/D line slope over a half-year
def f15vc_f15_volume_price_confirmation_adslope_126d_base_v011_signal(close, high, low, volume):
    ad = _f15_adline(close, high, low, volume)
    b = _f15_slope(ad, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# A/D line z-score vs 126d history
def f15vc_f15_volume_price_confirmation_adz_126d_base_v012_signal(close, high, low, volume):
    ad = _f15_adline(close, high, low, volume)
    b = _z(ad, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# A/D detrended vs 63d mean scaled by vol
def f15vc_f15_volume_price_confirmation_addetr_63d_base_v013_signal(close, high, low, volume):
    ad = _f15_adline(close, high, low, volume)
    b = (ad - _mean(ad, 63)) / _std(ad, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# A/D line vs price divergence (A/D slope minus price slope, z-scored)
def f15vc_f15_volume_price_confirmation_addiv_63d_base_v014_signal(close, high, low, closeadj, volume):
    ad = _f15_adline(close, high, low, volume)
    ad_sl = _z(_f15_slope(ad, 63), 126)
    px_sl = _z((closeadj - closeadj.shift(63)) / 63.0, 126)
    b = ad_sl - px_sl
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# A/D momentum: 21d vs 63d change spread
def f15vc_f15_volume_price_confirmation_admom_base_v015_signal(close, high, low, volume):
    ad = _f15_adline(close, high, low, volume)
    short = (ad - ad.shift(21)) / 21.0
    long = (ad - ad.shift(63)) / 63.0
    scale = ad.abs().rolling(63, min_periods=21).mean().replace(0, np.nan)
    b = (short - long) / scale
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# A/D slope rank vs 252d history
def f15vc_f15_volume_price_confirmation_adslrank_base_v016_signal(close, high, low, volume):
    ad = _f15_adline(close, high, low, volume)
    b = _rank(_f15_slope(ad, 63), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Close location value smoothed over a month (intra-bar accumulation bias)
def f15vc_f15_volume_price_confirmation_clv_21d_base_v017_signal(close, high, low):
    clv = _f15_clv(close, high, low)
    b = clv.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CLV positive-bar fraction minus volume-weighted bias (where does flow concentrate)
def f15vc_f15_volume_price_confirmation_clvskew_63d_base_v018_signal(close, high, low, volume):
    clv = _f15_clv(close, high, low)
    unweighted = clv.rolling(63, min_periods=21).mean()
    num = (clv * volume).rolling(63, min_periods=21).sum()
    den = volume.rolling(63, min_periods=21).sum().replace(0, np.nan)
    weighted = num / den
    b = weighted - unweighted
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Chaikin money flow 21d
def f15vc_f15_volume_price_confirmation_cmf_21d_base_v019_signal(close, high, low, volume):
    b = _f15_cmf(close, high, low, volume, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Chaikin money flow 63d
def f15vc_f15_volume_price_confirmation_cmf_63d_base_v020_signal(close, high, low, volume):
    b = _f15_cmf(close, high, low, volume, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Chaikin money flow 126d
def f15vc_f15_volume_price_confirmation_cmf_126d_base_v021_signal(close, high, low, volume):
    b = _f15_cmf(close, high, low, volume, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CMF term-structure spread: 21d minus 63d (short vs long money flow)
def f15vc_f15_volume_price_confirmation_cmfspr_base_v022_signal(close, high, low, volume):
    b = _f15_cmf(close, high, low, volume, 21) - _f15_cmf(close, high, low, volume, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CMF z-score vs 252d history
def f15vc_f15_volume_price_confirmation_cmfz_63d_base_v023_signal(close, high, low, volume):
    cmf = _f15_cmf(close, high, low, volume, 63)
    b = _z(cmf, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CMF rank minus price-momentum rank (money-flow leads/lags price percentile)
def f15vc_f15_volume_price_confirmation_cmfpxrank_63d_base_v024_signal(close, high, low, closeadj, volume):
    cmf_r = _rank(_f15_cmf(close, high, low, volume, 63), 252)
    px_r = _rank(closeadj / closeadj.shift(63) - 1.0, 252)
    b = cmf_r - px_r
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CMF persistence: fraction of last quarter CMF stayed positive
def f15vc_f15_volume_price_confirmation_cmfpersist_base_v025_signal(close, high, low, volume):
    cmf = _f15_cmf(close, high, low, volume, 21)
    pos = (cmf > 0).astype(float)
    b = pos.rolling(63, min_periods=21).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Money-flow index 14d (classic)
def f15vc_f15_volume_price_confirmation_mfi_14d_base_v026_signal(close, high, low, volume):
    b = _f15_mfi(close, high, low, volume, 14)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Money-flow index 21d
def f15vc_f15_volume_price_confirmation_mfi_21d_base_v027_signal(close, high, low, volume):
    b = _f15_mfi(close, high, low, volume, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Money-flow index 63d
def f15vc_f15_volume_price_confirmation_mfi_63d_base_v028_signal(close, high, low, volume):
    b = _f15_mfi(close, high, low, volume, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MFI momentum: 21d change of the 14d money-flow index (flow acceleration)
def f15vc_f15_volume_price_confirmation_mfimom_21d_base_v029_signal(close, high, low, volume):
    mfi = _f15_mfi(close, high, low, volume, 14)
    b = (mfi - mfi.shift(21)) / 21.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MFI term spread: 14d minus 63d
def f15vc_f15_volume_price_confirmation_mfispr_base_v030_signal(close, high, low, volume):
    b = _f15_mfi(close, high, low, volume, 14) - _f15_mfi(close, high, low, volume, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MFI z-score vs 252d history
def f15vc_f15_volume_price_confirmation_mfiz_21d_base_v031_signal(close, high, low, volume):
    mfi = _f15_mfi(close, high, low, volume, 21)
    b = _z(mfi, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MFI extreme-day frequency (>80 or <20) over a quarter, signed
def f15vc_f15_volume_price_confirmation_mfiextr_base_v032_signal(close, high, low, volume):
    mfi = _f15_mfi(close, high, low, volume, 14)
    hot = (mfi > 80).astype(float)
    cold = (mfi < 20).astype(float)
    b = (hot - cold).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Force index 2d (raw single-bar pressure) percentile-ranked vs 252d history
def f15vc_f15_volume_price_confirmation_forcerank2_base_v033_signal(closeadj, volume):
    fi = _f15_force(closeadj, volume, 2)
    b = _rank(fi, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Force index EMA 21d, z-scored vs 126d history
def f15vc_f15_volume_price_confirmation_forcez_21d_base_v034_signal(closeadj, volume):
    fi = _f15_force(closeadj, volume, 21)
    b = _z(fi, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Force index EMA 63d, z-scored vs 252d history (slow money pressure)
def f15vc_f15_volume_price_confirmation_forcez_63d_base_v035_signal(closeadj, volume):
    fi = _f15_force(closeadj, volume, 63)
    b = _z(fi, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Force index sign persistence over a quarter
def f15vc_f15_volume_price_confirmation_forcepersist_base_v036_signal(closeadj, volume):
    fi = _f15_force(closeadj, volume, 13)
    pos = np.sign(fi)
    b = pos.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Force index rank vs 252d history
def f15vc_f15_volume_price_confirmation_forcerank_base_v037_signal(closeadj, volume):
    fi = _f15_force(closeadj, volume, 21)
    b = _rank(fi, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Up/down volume share over 21d
def f15vc_f15_volume_price_confirmation_udvol_21d_base_v038_signal(close, volume):
    b = _f15_updownvol(close, volume, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Up/down volume share over 63d
def f15vc_f15_volume_price_confirmation_udvol_63d_base_v039_signal(close, volume):
    b = _f15_updownvol(close, volume, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Up/down volume share term spread (21d vs 63d)
def f15vc_f15_volume_price_confirmation_udvolspr_base_v040_signal(close, volume):
    b = _f15_updownvol(close, volume, 21) - _f15_updownvol(close, volume, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Up/down volume share z-score vs 252d history
def f15vc_f15_volume_price_confirmation_udvolz_63d_base_v041_signal(close, volume):
    ud = _f15_updownvol(close, volume, 63)
    b = _z(ud, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Price-volume trend slope over a quarter
def f15vc_f15_volume_price_confirmation_pvtslope_63d_base_v042_signal(closeadj, volume):
    pvt = _f15_pvt(closeadj, volume)
    b = _f15_slope(pvt, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Price-volume trend z-score vs 126d history
def f15vc_f15_volume_price_confirmation_pvtz_126d_base_v043_signal(closeadj, volume):
    pvt = _f15_pvt(closeadj, volume)
    b = _z(pvt, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# PVT vs price divergence (PVT slope minus price slope)
def f15vc_f15_volume_price_confirmation_pvtdiv_63d_base_v044_signal(closeadj, volume):
    pvt = _f15_pvt(closeadj, volume)
    pvt_sl = _z(_f15_slope(pvt, 63), 126)
    px_sl = _z((closeadj - closeadj.shift(63)) / 63.0, 126)
    b = pvt_sl - px_sl
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Signed dollar-volume flow slope (closeadj*volume direction) over a quarter
def f15vc_f15_volume_price_confirmation_sdvslope_63d_base_v045_signal(closeadj, volume):
    sdv = _f15_signed_dollar(closeadj, volume)
    b = _f15_slope(sdv, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Dollar-vs-share flow disagreement: signed dollar-flow slope minus OBV slope
def f15vc_f15_volume_price_confirmation_sdvobvspr_63d_base_v046_signal(close, closeadj, volume):
    sdv_sl = _z(_f15_slope(_f15_signed_dollar(closeadj, volume), 63), 126)
    obv_sl = _z(_f15_slope(_f15_obv(close, volume), 63), 126)
    b = sdv_sl - obv_sl
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Ease of movement 21d (price progress per dollar volume)
def f15vc_f15_volume_price_confirmation_eom_21d_base_v047_signal(closeadj, high, low, volume):
    b = _f15_eom(closeadj, high, low, volume, 21)
    result = b.replace([np.inf, -np.inf], np.nan)
    return _z(result, 126)


# Ease of movement 63d, z-scored
def f15vc_f15_volume_price_confirmation_eomz_63d_base_v048_signal(closeadj, high, low, volume):
    eom = _f15_eom(closeadj, high, low, volume, 63)
    b = _z(eom, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Volume-price correlation over a quarter (confirmation strength)
def f15vc_f15_volume_price_confirmation_vpcorr_63d_base_v049_signal(closeadj, volume):
    ret = closeadj.pct_change()
    vchg = volume.pct_change()
    b = _corr(ret, vchg, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Volume-return correlation: signed return vs volume level over 63d
def f15vc_f15_volume_price_confirmation_vrcorr_63d_base_v050_signal(closeadj, volume):
    ret = closeadj.pct_change()
    logv = np.log(volume.replace(0, np.nan))
    b = _corr(ret, logv, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CMF * price-trend interaction (money flow aligned with trend)
def f15vc_f15_volume_price_confirmation_cmftrend_63d_base_v051_signal(close, high, low, closeadj, volume):
    cmf = _f15_cmf(close, high, low, volume, 63)
    px_sl = np.sign(closeadj - closeadj.shift(63))
    b = cmf * px_sl
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV-to-price ratio trend: OBV growth minus price growth (cumulative confirmation)
def f15vc_f15_volume_price_confirmation_obvpxratio_126d_base_v052_signal(close, closeadj, volume):
    obv = _f15_obv(close, volume)
    obv_g = obv / obv.shift(126).replace(0, np.nan) - 1.0
    px_g = closeadj / closeadj.shift(126).replace(0, np.nan) - 1.0
    b = np.tanh(obv_g - px_g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Conviction accumulation: return-magnitude-weighted up vs down volume over 21d
def f15vc_f15_volume_price_confirmation_convaccum_21d_base_v053_signal(close, closeadj, volume):
    w = closeadj.pct_change().abs() * volume
    up = w.where(close.diff() > 0, 0.0)
    dn = w.where(close.diff() < 0, 0.0)
    su = up.rolling(21, min_periods=10).sum()
    sd = dn.rolling(21, min_periods=10).sum()
    tot = (su + sd).replace(0, np.nan)
    b = (su - sd) / tot
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# A/D line acceleration-as-level: 63d change minus 126d change normalized
def f15vc_f15_volume_price_confirmation_adaccel_base_v054_signal(close, high, low, volume):
    ad = _f15_adline(close, high, low, volume)
    c63 = ad - ad.shift(63)
    c126 = (ad - ad.shift(126)) * 0.5
    scale = ad.abs().rolling(126, min_periods=63).mean().replace(0, np.nan)
    b = (c63 - c126) / scale
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CMF dispersion over a quarter (instability of money flow)
def f15vc_f15_volume_price_confirmation_cmfdisp_base_v055_signal(close, high, low, volume):
    cmf = _f15_cmf(close, high, low, volume, 21)
    b = _std(cmf, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Force index dispersion (volatility of money pressure) over a quarter
def f15vc_f15_volume_price_confirmation_forcedisp_base_v056_signal(closeadj, volume):
    fi = _f15_force(closeadj, volume, 13)
    b = _std(fi, 63) / fi.abs().rolling(63, min_periods=21).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MFI-price divergence: MFI change vs price change disagreement
def f15vc_f15_volume_price_confirmation_mfidiv_63d_base_v057_signal(close, high, low, closeadj, volume):
    mfi = _f15_mfi(close, high, low, volume, 21)
    mfi_chg = _z(mfi - mfi.shift(63), 126)
    px_chg = _z(closeadj - closeadj.shift(63), 126)
    b = px_chg - mfi_chg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Volume-weighted return tilt: mean of return*volume share over 21d
def f15vc_f15_volume_price_confirmation_vwret_21d_base_v058_signal(closeadj, volume):
    ret = closeadj.pct_change()
    num = (ret * volume).rolling(21, min_periods=10).sum()
    den = volume.rolling(21, min_periods=10).sum().replace(0, np.nan)
    b = num / den
    result = b.replace([np.inf, -np.inf], np.nan)
    return _z(b, 126)


# Effort-vs-result: volume z minus absolute return z (churn without progress)
def f15vc_f15_volume_price_confirmation_effres_63d_base_v059_signal(closeadj, volume):
    volz = _z(volume, 63)
    retz = _z(closeadj.pct_change().abs(), 63)
    b = volz - retz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Negative-volume signal: A/D contribution on down-days only over 63d
def f15vc_f15_volume_price_confirmation_distrib_63d_base_v060_signal(close, high, low, volume):
    mfv = _f15_clv(close, high, low) * volume
    dn = mfv.where(close.diff() < 0, 0.0)
    num = dn.rolling(63, min_periods=21).sum()
    den = volume.rolling(63, min_periods=21).sum().replace(0, np.nan)
    b = num / den
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV smoothed slope vs its EMA (OBV momentum oscillator)
def f15vc_f15_volume_price_confirmation_obvosc_base_v061_signal(close, volume):
    obv = _f15_obv(close, volume)
    fast = obv.ewm(span=21, min_periods=10).mean()
    slow = obv.ewm(span=63, min_periods=21).mean()
    scale = obv.abs().rolling(63, min_periods=21).mean().replace(0, np.nan)
    b = (fast - slow) / scale
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CMF accumulation streak: consecutive positive-CMF run length (signed)
def f15vc_f15_volume_price_confirmation_cmfstreak_base_v062_signal(close, high, low, volume):
    cmf = _f15_cmf(close, high, low, volume, 21)
    sign = np.sign(cmf).fillna(0.0)
    grp = (sign != sign.shift()).cumsum()
    streak = sign.groupby(grp).cumcount() + 1
    b = (streak * sign) / 63.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Price up but money-flow down regime: count over a quarter (false rallies)
def f15vc_f15_volume_price_confirmation_falserally_base_v063_signal(close, high, low, closeadj, volume):
    cmf = _f15_cmf(close, high, low, volume, 21)
    px_up = (closeadj.diff(21) > 0)
    flow_dn = (cmf < 0)
    flag = (px_up & flow_dn).astype(float)
    b = flag.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Force-index vs price divergence: cumulative force slope minus price slope (63d)
def f15vc_f15_volume_price_confirmation_forcediv_63d_base_v064_signal(closeadj, volume):
    cumforce = (closeadj.diff() * volume).fillna(0.0).cumsum()
    f_sl = _z(_f15_slope(cumforce, 63), 126)
    px_sl = _z((closeadj - closeadj.shift(63)) / 63.0, 126)
    b = f_sl - px_sl
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# A/D-OBV agreement: correlation of the two cumulative flow lines over 63d
def f15vc_f15_volume_price_confirmation_adobvagr_base_v065_signal(close, high, low, volume):
    ad = _f15_adline(close, high, low, volume).diff()
    obv = _f15_obv(close, volume).diff()
    b = _corr(ad, obv, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Money-flow volume share on highest-volume days over 63d (climactic flow)
def f15vc_f15_volume_price_confirmation_climflow_base_v066_signal(close, high, low, volume):
    clv = _f15_clv(close, high, low)
    volrank = volume.rolling(63, min_periods=21).rank(pct=True)
    heavy = clv.where(volrank > 0.8, np.nan)
    b = heavy.rolling(63, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CMF-MFI composite confirmation (average of two normalized money-flow gauges)
def f15vc_f15_volume_price_confirmation_mfcomposite_base_v067_signal(close, high, low, volume):
    cmf = _z(_f15_cmf(close, high, low, volume, 21), 126)
    mfi = _z(_f15_mfi(close, high, low, volume, 21) - 50.0, 126)
    b = (cmf + mfi) / 2.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Volume-confirmed momentum: 63d return * up-down volume share
def f15vc_f15_volume_price_confirmation_volmom_63d_base_v068_signal(close, closeadj, volume):
    ret = closeadj / closeadj.shift(63) - 1.0
    ud = _f15_updownvol(close, volume, 63)
    b = np.tanh(3.0 * ret) * ud
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV range position: where OBV sits within its own 126d high-low range
def f15vc_f15_volume_price_confirmation_obvrngpos_base_v069_signal(close, volume):
    obv = _f15_obv(close, volume)
    hi = obv.rolling(126, min_periods=63).max()
    lo = obv.rolling(126, min_periods=63).min()
    b = (obv - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Accumulation regime: fraction of last year 21d-CMF stayed above +0.05 minus below -0.05
def f15vc_f15_volume_price_confirmation_cmfregime_base_v070_signal(close, high, low, volume):
    cmf = _f15_cmf(close, high, low, volume, 21)
    acc = (cmf > 0.05).astype(float)
    dist = (cmf < -0.05).astype(float)
    b = (acc - dist).rolling(252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EOM sign persistence (smooth-advance days) over a quarter
def f15vc_f15_volume_price_confirmation_eompersist_base_v071_signal(closeadj, high, low, volume):
    eom = _f15_eom(closeadj, high, low, volume, 5)
    b = np.sign(eom).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Force index year-over-quarter momentum: 63d force vs 126d force, z-scored
def f15vc_f15_volume_price_confirmation_forcemom_base_v072_signal(closeadj, volume):
    fast = _f15_force(closeadj, volume, 21)
    slow = _f15_force(closeadj, volume, 63)
    b = _z(fast - slow, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Up-volume vs down-volume magnitude asymmetry (avg up-day vol / avg down-day vol)
def f15vc_f15_volume_price_confirmation_volasym_63d_base_v073_signal(close, volume):
    up = volume.where(close.diff() > 0, np.nan)
    dn = volume.where(close.diff() < 0, np.nan)
    au = up.rolling(63, min_periods=15).mean()
    ad = dn.rolling(63, min_periods=15).mean().replace(0, np.nan)
    b = np.log(au / ad)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Divergence breadth: signed disagreement between A/D, OBV, CMF trends (composite)
def f15vc_f15_volume_price_confirmation_divbreadth_base_v074_signal(close, high, low, closeadj, volume):
    px = np.sign(closeadj.diff(63))
    z_ad = _z(_f15_adline(close, high, low, volume).diff(63), 126)
    z_obv = _z(_f15_obv(close, volume).diff(63), 126)
    z_cmf = _z(_f15_cmf(close, high, low, volume, 63), 126)
    b = px * (z_ad + z_obv + z_cmf) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Volume-price trend confirmation rank: PVT slope ranked, signed by price direction
def f15vc_f15_volume_price_confirmation_pvtconf_base_v075_signal(closeadj, volume):
    pvt = _f15_pvt(closeadj, volume)
    sl = _f15_slope(pvt, 63)
    rank = _rank(sl, 252)
    b = rank * np.sign(closeadj.diff(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f15vc_f15_volume_price_confirmation_obvslope_63d_base_v001_signal,
    f15vc_f15_volume_price_confirmation_obvslope_126d_base_v002_signal,
    f15vc_f15_volume_price_confirmation_obvz_126d_base_v003_signal,
    f15vc_f15_volume_price_confirmation_obvdetr_63d_base_v004_signal,
    f15vc_f15_volume_price_confirmation_obvmom_base_v005_signal,
    f15vc_f15_volume_price_confirmation_obvconf_63d_base_v006_signal,
    f15vc_f15_volume_price_confirmation_obvdiv_63d_base_v007_signal,
    f15vc_f15_volume_price_confirmation_obvslrank_63d_base_v008_signal,
    f15vc_f15_volume_price_confirmation_obvnewhi_base_v009_signal,
    f15vc_f15_volume_price_confirmation_adslope_63d_base_v010_signal,
    f15vc_f15_volume_price_confirmation_adslope_126d_base_v011_signal,
    f15vc_f15_volume_price_confirmation_adz_126d_base_v012_signal,
    f15vc_f15_volume_price_confirmation_addetr_63d_base_v013_signal,
    f15vc_f15_volume_price_confirmation_addiv_63d_base_v014_signal,
    f15vc_f15_volume_price_confirmation_admom_base_v015_signal,
    f15vc_f15_volume_price_confirmation_adslrank_base_v016_signal,
    f15vc_f15_volume_price_confirmation_clv_21d_base_v017_signal,
    f15vc_f15_volume_price_confirmation_clvskew_63d_base_v018_signal,
    f15vc_f15_volume_price_confirmation_cmf_21d_base_v019_signal,
    f15vc_f15_volume_price_confirmation_cmf_63d_base_v020_signal,
    f15vc_f15_volume_price_confirmation_cmf_126d_base_v021_signal,
    f15vc_f15_volume_price_confirmation_cmfspr_base_v022_signal,
    f15vc_f15_volume_price_confirmation_cmfz_63d_base_v023_signal,
    f15vc_f15_volume_price_confirmation_cmfpxrank_63d_base_v024_signal,
    f15vc_f15_volume_price_confirmation_cmfpersist_base_v025_signal,
    f15vc_f15_volume_price_confirmation_mfi_14d_base_v026_signal,
    f15vc_f15_volume_price_confirmation_mfi_21d_base_v027_signal,
    f15vc_f15_volume_price_confirmation_mfi_63d_base_v028_signal,
    f15vc_f15_volume_price_confirmation_mfimom_21d_base_v029_signal,
    f15vc_f15_volume_price_confirmation_mfispr_base_v030_signal,
    f15vc_f15_volume_price_confirmation_mfiz_21d_base_v031_signal,
    f15vc_f15_volume_price_confirmation_mfiextr_base_v032_signal,
    f15vc_f15_volume_price_confirmation_forcerank2_base_v033_signal,
    f15vc_f15_volume_price_confirmation_forcez_21d_base_v034_signal,
    f15vc_f15_volume_price_confirmation_forcez_63d_base_v035_signal,
    f15vc_f15_volume_price_confirmation_forcepersist_base_v036_signal,
    f15vc_f15_volume_price_confirmation_forcerank_base_v037_signal,
    f15vc_f15_volume_price_confirmation_udvol_21d_base_v038_signal,
    f15vc_f15_volume_price_confirmation_udvol_63d_base_v039_signal,
    f15vc_f15_volume_price_confirmation_udvolspr_base_v040_signal,
    f15vc_f15_volume_price_confirmation_udvolz_63d_base_v041_signal,
    f15vc_f15_volume_price_confirmation_pvtslope_63d_base_v042_signal,
    f15vc_f15_volume_price_confirmation_pvtz_126d_base_v043_signal,
    f15vc_f15_volume_price_confirmation_pvtdiv_63d_base_v044_signal,
    f15vc_f15_volume_price_confirmation_sdvslope_63d_base_v045_signal,
    f15vc_f15_volume_price_confirmation_sdvobvspr_63d_base_v046_signal,
    f15vc_f15_volume_price_confirmation_eom_21d_base_v047_signal,
    f15vc_f15_volume_price_confirmation_eomz_63d_base_v048_signal,
    f15vc_f15_volume_price_confirmation_vpcorr_63d_base_v049_signal,
    f15vc_f15_volume_price_confirmation_vrcorr_63d_base_v050_signal,
    f15vc_f15_volume_price_confirmation_cmftrend_63d_base_v051_signal,
    f15vc_f15_volume_price_confirmation_obvpxratio_126d_base_v052_signal,
    f15vc_f15_volume_price_confirmation_convaccum_21d_base_v053_signal,
    f15vc_f15_volume_price_confirmation_adaccel_base_v054_signal,
    f15vc_f15_volume_price_confirmation_cmfdisp_base_v055_signal,
    f15vc_f15_volume_price_confirmation_forcedisp_base_v056_signal,
    f15vc_f15_volume_price_confirmation_mfidiv_63d_base_v057_signal,
    f15vc_f15_volume_price_confirmation_vwret_21d_base_v058_signal,
    f15vc_f15_volume_price_confirmation_effres_63d_base_v059_signal,
    f15vc_f15_volume_price_confirmation_distrib_63d_base_v060_signal,
    f15vc_f15_volume_price_confirmation_obvosc_base_v061_signal,
    f15vc_f15_volume_price_confirmation_cmfstreak_base_v062_signal,
    f15vc_f15_volume_price_confirmation_falserally_base_v063_signal,
    f15vc_f15_volume_price_confirmation_forcediv_63d_base_v064_signal,
    f15vc_f15_volume_price_confirmation_adobvagr_base_v065_signal,
    f15vc_f15_volume_price_confirmation_climflow_base_v066_signal,
    f15vc_f15_volume_price_confirmation_mfcomposite_base_v067_signal,
    f15vc_f15_volume_price_confirmation_volmom_63d_base_v068_signal,
    f15vc_f15_volume_price_confirmation_obvrngpos_base_v069_signal,
    f15vc_f15_volume_price_confirmation_cmfregime_base_v070_signal,
    f15vc_f15_volume_price_confirmation_eompersist_base_v071_signal,
    f15vc_f15_volume_price_confirmation_forcemom_base_v072_signal,
    f15vc_f15_volume_price_confirmation_volasym_63d_base_v073_signal,
    f15vc_f15_volume_price_confirmation_divbreadth_base_v074_signal,
    f15vc_f15_volume_price_confirmation_pvtconf_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F15_VOLUME_PRICE_CONFIRMATION_REGISTRY_001_075 = REGISTRY


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

    print("OK f15_volume_price_confirmation_base_001_075_claude: %d features pass" % n_features)
