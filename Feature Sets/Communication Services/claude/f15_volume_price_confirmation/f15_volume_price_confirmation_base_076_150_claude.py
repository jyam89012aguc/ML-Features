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
    direction = np.sign(close.diff())
    return (direction * volume).fillna(0.0).cumsum()


def _f15_signed_dollar(closeadj, volume):
    direction = np.sign(closeadj.diff())
    return (direction * closeadj * volume).fillna(0.0).cumsum()


def _f15_clv(close, high, low):
    rng = (high - low).replace(0, np.nan)
    return ((close - low) - (high - close)) / rng


def _f15_adline(close, high, low, volume):
    mfv = _f15_clv(close, high, low) * volume
    return mfv.fillna(0.0).cumsum()


def _f15_cmf(close, high, low, volume, w):
    mfv = _f15_clv(close, high, low) * volume
    num = mfv.rolling(w, min_periods=max(2, w // 2)).sum()
    den = volume.rolling(w, min_periods=max(2, w // 2)).sum().replace(0, np.nan)
    return num / den


def _f15_typ(close, high, low):
    return (high + low + close) / 3.0


def _f15_mfi(close, high, low, volume, w):
    tp = _f15_typ(close, high, low)
    rmf = tp * volume
    up = rmf.where(tp.diff() > 0, 0.0)
    dn = rmf.where(tp.diff() < 0, 0.0)
    pos = up.rolling(w, min_periods=max(2, w // 2)).sum()
    neg = dn.rolling(w, min_periods=max(2, w // 2)).sum().replace(0, np.nan)
    ratio = pos / neg
    return 100.0 - 100.0 / (1.0 + ratio)


def _f15_force(closeadj, volume, w):
    fi = closeadj.diff() * volume
    return fi.ewm(span=w, min_periods=max(2, w // 2)).mean()


def _f15_updownvol(close, volume, w):
    up = volume.where(close.diff() > 0, 0.0)
    dn = volume.where(close.diff() < 0, 0.0)
    su = up.rolling(w, min_periods=max(2, w // 2)).sum()
    sd = dn.rolling(w, min_periods=max(2, w // 2)).sum()
    tot = (su + sd).replace(0, np.nan)
    return (su - sd) / tot


def _f15_pvt(closeadj, volume):
    return (closeadj.pct_change() * volume).fillna(0.0).cumsum()


def _f15_eom(closeadj, high, low, volume, w):
    mid = (high + low) / 2.0
    box = volume / (high - low).replace(0, np.nan)
    raw = mid.diff() / box.replace(0, np.nan)
    return raw.rolling(w, min_periods=max(2, w // 2)).mean()


def _f15_slope(s, w):
    return (s - s.shift(w)) / (s.abs().rolling(w, min_periods=max(2, w // 2)).mean().replace(0, np.nan) * w)


def _f15_nvi(close, volume):
    # Negative volume index: cumulate return only on lower-volume days.
    ret = close.pct_change()
    quiet = (volume.diff() < 0)
    step = ret.where(quiet, 0.0).fillna(0.0)
    return (1.0 + step).cumprod()


def _f15_pvi(close, volume):
    # Positive volume index: cumulate return only on higher-volume days.
    ret = close.pct_change()
    loud = (volume.diff() > 0)
    step = ret.where(loud, 0.0).fillna(0.0)
    return (1.0 + step).cumprod()


# ============================================================
# Negative volume index slope (smart-money trend on quiet days)
def f15vc_f15_volume_price_confirmation_nvislope_63d_base_v076_signal(close, volume):
    nvi = _f15_nvi(close, volume)
    b = (nvi - nvi.shift(63)) / 63.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# NVI vs its own 255d EMA (NVI above trend = quiet accumulation)
def f15vc_f15_volume_price_confirmation_nvitrend_base_v077_signal(close, volume):
    nvi = _f15_nvi(close, volume)
    ema = nvi.ewm(span=126, min_periods=63).mean().replace(0, np.nan)
    b = nvi / ema - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Positive volume index slope (crowd trend on heavy days)
def f15vc_f15_volume_price_confirmation_pvislope_63d_base_v078_signal(close, volume):
    pvi = _f15_pvi(close, volume)
    b = (pvi - pvi.shift(63)) / 63.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# PVI vs NVI divergence (crowd vs smart-money disagreement)
def f15vc_f15_volume_price_confirmation_pvinvidiv_base_v079_signal(close, volume):
    pvi = _z(_f15_pvi(close, volume), 126)
    nvi = _z(_f15_nvi(close, volume), 126)
    b = pvi - nvi
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV slope per unit price slope over a half-year (long confirmation ratio)
def f15vc_f15_volume_price_confirmation_obvconf_126d_base_v080_signal(close, closeadj, volume):
    obv_sl = _f15_slope(_f15_obv(close, volume), 126)
    px_sl = (closeadj - closeadj.shift(126)) / (closeadj.rolling(126, min_periods=63).mean().replace(0, np.nan) * 126)
    b = obv_sl - px_sl
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV-price divergence over a half-year (slow distribution warning)
def f15vc_f15_volume_price_confirmation_obvdiv_126d_base_v081_signal(close, closeadj, volume):
    obv_sl = _z(_f15_slope(_f15_obv(close, volume), 126), 252)
    px_sl = _z((closeadj - closeadj.shift(126)) / 126.0, 252)
    b = px_sl - obv_sl
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# A/D-price divergence over a half-year
def f15vc_f15_volume_price_confirmation_addiv_126d_base_v082_signal(close, high, low, closeadj, volume):
    ad_sl = _z(_f15_slope(_f15_adline(close, high, low, volume), 126), 252)
    px_sl = _z((closeadj - closeadj.shift(126)) / 126.0, 252)
    b = ad_sl - px_sl
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# A/D line range position (where A/D sits in its 252d range)
def f15vc_f15_volume_price_confirmation_adrngpos_base_v083_signal(close, high, low, volume):
    ad = _f15_adline(close, high, low, volume)
    hi = ad.rolling(252, min_periods=63).max()
    lo = ad.rolling(252, min_periods=63).min()
    b = (ad - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CMF 21d minus 126d (short money flow vs durable money flow)
def f15vc_f15_volume_price_confirmation_cmfspr_21v126_base_v084_signal(close, high, low, volume):
    b = _f15_cmf(close, high, low, volume, 21) - _f15_cmf(close, high, low, volume, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CMF sign-change frequency over a half-year (money-flow instability)
def f15vc_f15_volume_price_confirmation_cmfflip_base_v085_signal(close, high, low, volume):
    cmf = _f15_cmf(close, high, low, volume, 21)
    flip = (np.sign(cmf) != np.sign(cmf.shift(1))).astype(float)
    b = flip.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MFI 21d minus its 63d average (overbought/oversold relative to own regime)
def f15vc_f15_volume_price_confirmation_mfidetr_base_v086_signal(close, high, low, volume):
    mfi = _f15_mfi(close, high, low, volume, 21)
    b = mfi - mfi.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MFI 63d rank vs 252d history
def f15vc_f15_volume_price_confirmation_mfirank_63d_base_v087_signal(close, high, low, volume):
    mfi = _f15_mfi(close, high, low, volume, 63)
    b = _rank(mfi, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Force index 13d EMA z-scored vs 252d (medium money pressure)
def f15vc_f15_volume_price_confirmation_forcez_13d_base_v088_signal(closeadj, volume):
    fi = _f15_force(closeadj, volume, 13)
    b = _z(fi, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Force index rank over a half-year window
def f15vc_f15_volume_price_confirmation_forcerank63_base_v089_signal(closeadj, volume):
    fi = _f15_force(closeadj, volume, 63)
    b = _rank(fi, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Up/down volume share over a half-year
def f15vc_f15_volume_price_confirmation_udvol_126d_base_v090_signal(close, volume):
    b = _f15_updownvol(close, volume, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Up-volume streak: consecutive up-volume-dominant 21d windows (signed)
def f15vc_f15_volume_price_confirmation_udvolstreak_base_v091_signal(close, volume):
    ud = _f15_updownvol(close, volume, 21)
    sign = np.sign(ud).fillna(0.0)
    grp = (sign != sign.shift()).cumsum()
    streak = sign.groupby(grp).cumcount() + 1
    b = (streak * sign) / 63.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# PVT slope over a half-year
def f15vc_f15_volume_price_confirmation_pvtslope_126d_base_v092_signal(closeadj, volume):
    pvt = _f15_pvt(closeadj, volume)
    b = _f15_slope(pvt, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# PVT momentum: 21d vs 63d change spread
def f15vc_f15_volume_price_confirmation_pvtmom_base_v093_signal(closeadj, volume):
    pvt = _f15_pvt(closeadj, volume)
    short = (pvt - pvt.shift(21)) / 21.0
    long = (pvt - pvt.shift(63)) / 63.0
    scale = pvt.abs().rolling(63, min_periods=21).mean().replace(0, np.nan)
    b = (short - long) / scale
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Signed dollar-volume flow slope over a half-year
def f15vc_f15_volume_price_confirmation_sdvslope_126d_base_v094_signal(closeadj, volume):
    sdv = _f15_signed_dollar(closeadj, volume)
    b = _f15_slope(sdv, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Ease of movement 63d sign persistence (smooth-advance regime)
def f15vc_f15_volume_price_confirmation_eompersist63_base_v095_signal(closeadj, high, low, volume):
    eom = _f15_eom(closeadj, high, low, volume, 21)
    b = np.sign(eom).rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Volume-price correlation over a half-year (slow confirmation)
def f15vc_f15_volume_price_confirmation_vpcorr_126d_base_v096_signal(closeadj, volume):
    ret = closeadj.pct_change()
    vchg = volume.pct_change()
    b = _corr(ret, vchg, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Sign of return * volume z-score, averaged (directional volume thrust) 21d
def f15vc_f15_volume_price_confirmation_volthrust_21d_base_v097_signal(closeadj, volume):
    volz = _z(volume, 63)
    b = (np.sign(closeadj.diff()) * volz).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CMF-confirmed breakout: 21d-CMF gated by a new-63d-high indicator (vol-confirmed break)
def f15vc_f15_volume_price_confirmation_cmfbreak_base_v098_signal(close, high, low, closeadj, volume):
    cmf = _f15_cmf(close, high, low, volume, 21)
    hi_prior = closeadj.shift(1).rolling(63, min_periods=21).max()
    is_break = (closeadj > hi_prior).astype(float)
    gate = is_break.rolling(21, min_periods=10).mean()
    b = cmf * gate
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV drawdown: OBV vs its 126d running max (accumulation pullback)
def f15vc_f15_volume_price_confirmation_obvdd_base_v099_signal(close, volume):
    obv = _f15_obv(close, volume)
    peak = obv.rolling(126, min_periods=63).max()
    scale = obv.abs().rolling(126, min_periods=63).mean().replace(0, np.nan)
    b = (obv - peak) / scale
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# A/D drawdown vs 126d running max
def f15vc_f15_volume_price_confirmation_addd_base_v100_signal(close, high, low, volume):
    ad = _f15_adline(close, high, low, volume)
    peak = ad.rolling(126, min_periods=63).max()
    scale = ad.abs().rolling(126, min_periods=63).mean().replace(0, np.nan)
    b = (ad - peak) / scale
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Distribution-day intensity: volume on bars that closed down AND in lower range half 126d
def f15vc_f15_volume_price_confirmation_distrib_126d_base_v101_signal(close, high, low, volume):
    weak = ((close.diff() < 0) & (_f15_clv(close, high, low) < 0))
    distvol = volume.where(weak, 0.0).rolling(126, min_periods=63).sum()
    tot = volume.rolling(126, min_periods=63).sum().replace(0, np.nan)
    b = distvol / tot - 0.25
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Volume on high-CLV bars vs low-CLV bars (where volume concentrates in range) 63d
def f15vc_f15_volume_price_confirmation_volclvconc_base_v102_signal(close, high, low, volume):
    clv = _f15_clv(close, high, low)
    topv = volume.where(clv > 0.5, 0.0).rolling(63, min_periods=21).sum()
    botv = volume.where(clv < -0.5, 0.0).rolling(63, min_periods=21).sum()
    tot = (topv + botv).replace(0, np.nan)
    b = (topv - botv) / tot
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Chaikin oscillator: A/D fast EMA minus slow EMA, normalized
def f15vc_f15_volume_price_confirmation_chaikinosc_base_v103_signal(close, high, low, volume):
    ad = _f15_adline(close, high, low, volume)
    fast = ad.ewm(span=21, min_periods=10).mean()
    slow = ad.ewm(span=63, min_periods=21).mean()
    scale = ad.abs().rolling(63, min_periods=21).mean().replace(0, np.nan)
    b = (fast - slow) / scale
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Volume-weighted price vs simple price gap (VWAP premium) over 21d
def f15vc_f15_volume_price_confirmation_vwapgap_21d_base_v104_signal(closeadj, volume):
    pv = (closeadj * volume).rolling(21, min_periods=10).sum()
    v = volume.rolling(21, min_periods=10).sum().replace(0, np.nan)
    vwap = pv / v
    b = closeadj / vwap - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# VWAP premium over 63d, z-scored
def f15vc_f15_volume_price_confirmation_vwapgapz_63d_base_v105_signal(closeadj, volume):
    pv = (closeadj * volume).rolling(63, min_periods=21).sum()
    v = volume.rolling(63, min_periods=21).sum().replace(0, np.nan)
    vwap = pv / v
    raw = closeadj / vwap - 1.0
    b = _z(raw, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CMF acceleration: 21d CMF change minus 63d CMF change
def f15vc_f15_volume_price_confirmation_cmfaccel_base_v106_signal(close, high, low, volume):
    cmf = _f15_cmf(close, high, low, volume, 21)
    c21 = cmf - cmf.shift(21)
    c63 = (cmf - cmf.shift(63)) / 3.0
    b = c21 - c63
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Force index minus EMA (force oscillator) over 21d
def f15vc_f15_volume_price_confirmation_forceosc_base_v107_signal(closeadj, volume):
    raw = closeadj.diff() * volume
    fast = raw.ewm(span=13, min_periods=7).mean()
    slow = raw.ewm(span=63, min_periods=21).mean()
    scale = raw.abs().ewm(span=63, min_periods=21).mean().replace(0, np.nan)
    b = (fast - slow) / scale
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Up-day return vs down-day return volume-weighted asymmetry over 63d
def f15vc_f15_volume_price_confirmation_retvolasym_base_v108_signal(closeadj, volume):
    ret = closeadj.pct_change()
    up = (ret.clip(lower=0) * volume).rolling(63, min_periods=21).sum()
    dn = (ret.clip(upper=0).abs() * volume).rolling(63, min_periods=21).sum()
    tot = (up + dn).replace(0, np.nan)
    b = (up - dn) / tot
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Volume concentration on biggest up-moves (greed concentration) 63d
def f15vc_f15_volume_price_confirmation_greedconc_base_v109_signal(closeadj, volume):
    ret = closeadj.pct_change()
    big_up = (ret > ret.rolling(63, min_periods=21).quantile(0.8))
    volz = _z(volume, 63)
    b = volz.where(big_up, np.nan).rolling(63, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Volume concentration on biggest down-moves (panic concentration) 63d
def f15vc_f15_volume_price_confirmation_panicconc_base_v110_signal(closeadj, volume):
    ret = closeadj.pct_change()
    big_dn = (ret < ret.rolling(63, min_periods=21).quantile(0.2))
    volz = _z(volume, 63)
    b = volz.where(big_dn, np.nan).rolling(63, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CMF * MFI agreement sign over a quarter (double-confirmation persistence)
def f15vc_f15_volume_price_confirmation_dualconf_base_v111_signal(close, high, low, volume):
    cmf = _f15_cmf(close, high, low, volume, 21)
    mfi = _f15_mfi(close, high, low, volume, 21) - 50.0
    agree = (np.sign(cmf) == np.sign(mfi)).astype(float) * np.sign(cmf)
    b = agree.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV slope minus A/D slope (share-count vs intrabar flow disagreement) 63d
def f15vc_f15_volume_price_confirmation_obvadspr_base_v112_signal(close, high, low, volume):
    obv_sl = _z(_f15_slope(_f15_obv(close, volume), 63), 126)
    ad_sl = _z(_f15_slope(_f15_adline(close, high, low, volume), 63), 126)
    b = obv_sl - ad_sl
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Money-flow volume z (raw A/D daily contribution z-score) 63d
def f15vc_f15_volume_price_confirmation_mfvz_base_v113_signal(close, high, low, volume):
    mfv = _f15_clv(close, high, low) * volume
    b = _z(mfv.rolling(21, min_periods=10).mean(), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Fraction of last quarter where OBV and price both rose (clean confirmation)
def f15vc_f15_volume_price_confirmation_cleanconf_base_v114_signal(close, closeadj, volume):
    obv_up = (_f15_obv(close, volume).diff(21) > 0)
    px_up = (closeadj.diff(21) > 0)
    both = (obv_up & px_up).astype(float)
    b = both.rolling(63, min_periods=21).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CMF trend slope over a quarter (money-flow direction change)
def f15vc_f15_volume_price_confirmation_cmfslope_base_v115_signal(close, high, low, volume):
    cmf = _f15_cmf(close, high, low, volume, 21)
    b = (cmf - cmf.shift(63)) / 63.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MFI band: distance outside the 20/80 band, signed (extreme money-flow pressure)
def f15vc_f15_volume_price_confirmation_mfiband_base_v116_signal(close, high, low, volume):
    mfi = _f15_mfi(close, high, low, volume, 14)
    over = (mfi - 80).clip(lower=0)
    under = (20 - mfi).clip(lower=0)
    b = (over - under).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Volume elasticity: regression beta of |return| on volume z over 63d
def f15vc_f15_volume_price_confirmation_volelast_base_v117_signal(closeadj, volume):
    absret = closeadj.pct_change().abs()
    volz = _z(volume, 63)
    cov = (absret * volz).rolling(63, min_periods=21).mean() - absret.rolling(63, min_periods=21).mean() * volz.rolling(63, min_periods=21).mean()
    var = volz.rolling(63, min_periods=21).var().replace(0, np.nan)
    b = cov / var
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV vs PVT divergence (share-direction vs return-magnitude flow) 63d
def f15vc_f15_volume_price_confirmation_obvpvtspr_base_v118_signal(close, closeadj, volume):
    obv_sl = _z(_f15_slope(_f15_obv(close, volume), 63), 126)
    pvt_sl = _z(_f15_slope(_f15_pvt(closeadj, volume), 63), 126)
    b = obv_sl - pvt_sl
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# A/D line year-over-quarter momentum (slow flow acceleration)
def f15vc_f15_volume_price_confirmation_admomslow_base_v119_signal(close, high, low, volume):
    ad = _f15_adline(close, high, low, volume)
    c126 = ad - ad.shift(126)
    c252 = (ad - ad.shift(252)) * 0.5
    scale = ad.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    b = (c126 - c252) / scale
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Chaikin money flow weighted by trend strength (confirmation in trending regime)
def f15vc_f15_volume_price_confirmation_cmftrendstr_base_v120_signal(close, high, low, closeadj, volume):
    cmf = _f15_cmf(close, high, low, volume, 21)
    er = (closeadj.diff(21).abs()) / closeadj.diff().abs().rolling(21, min_periods=10).sum().replace(0, np.nan)
    b = cmf * er
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Force index 63d vs 126d ratio (medium vs long money pressure)
def f15vc_f15_volume_price_confirmation_forceratio_base_v121_signal(closeadj, volume):
    f63 = _f15_force(closeadj, volume, 63)
    f126 = _f15_force(closeadj, volume, 126)
    scale = (closeadj.diff().abs() * volume).ewm(span=126, min_periods=63).mean().replace(0, np.nan)
    b = (f63 - f126) / scale
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Money-flow momentum: change in CMF rank over a quarter
def f15vc_f15_volume_price_confirmation_cmfrankmom_base_v122_signal(close, high, low, volume):
    cmf = _f15_cmf(close, high, low, volume, 21)
    rk = _rank(cmf, 252)
    b = rk - rk.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Down-day volume share rising while price flat/up (silent distribution) 63d
def f15vc_f15_volume_price_confirmation_silentdist_base_v123_signal(close, closeadj, volume):
    dn = volume.where(close.diff() < 0, 0.0).rolling(21, min_periods=10).sum()
    tot = volume.rolling(21, min_periods=10).sum().replace(0, np.nan)
    dn_share = dn / tot
    px_chg = closeadj.diff(63)
    b = (dn_share - 0.5) * np.sign(px_chg.clip(lower=0) + 1e-9)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV trend stability: 126d OBV slope divided by dispersion of its 21d slopes
def f15vc_f15_volume_price_confirmation_obvstab_base_v124_signal(close, volume):
    obv = _f15_obv(close, volume)
    sl = obv.diff(21)
    scale = obv.abs().rolling(126, min_periods=63).mean().replace(0, np.nan)
    mu = sl.rolling(126, min_periods=63).mean() / scale
    sd = (sl / scale).rolling(126, min_periods=63).std().replace(0, np.nan)
    b = mu / sd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CMF vs volume-surge interaction (money flow during heavy volume) 21d
def f15vc_f15_volume_price_confirmation_cmfsurge_base_v125_signal(close, high, low, volume):
    cmf = _f15_cmf(close, high, low, volume, 21)
    surge = _z(volume, 63).clip(lower=0)
    b = (cmf * surge).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Price-volume trend rank vs 252d history
def f15vc_f15_volume_price_confirmation_pvtrank_base_v126_signal(closeadj, volume):
    pvt = _f15_pvt(closeadj, volume)
    sl = _f15_slope(pvt, 63)
    b = _rank(sl, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# A/D line z over 252d (long-horizon accumulation extremity)
def f15vc_f15_volume_price_confirmation_adz_252d_base_v127_signal(close, high, low, volume):
    ad = _f15_adline(close, high, low, volume)
    b = _z(ad, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV z over 252d (long-horizon accumulation extremity)
def f15vc_f15_volume_price_confirmation_obvz_252d_base_v128_signal(close, volume):
    obv = _f15_obv(close, volume)
    b = _z(obv, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Intrabar buying-pressure breadth: fraction of last quarter closing in upper range third
def f15vc_f15_volume_price_confirmation_clvbreadth_base_v129_signal(close, high, low, volume):
    clv = _f15_clv(close, high, low)
    strong = (clv > 0.3334).astype(float)
    weak = (clv < -0.3334).astype(float)
    vw_strong = (strong * volume).rolling(63, min_periods=21).sum()
    vw_weak = (weak * volume).rolling(63, min_periods=21).sum()
    tot = (vw_strong + vw_weak).replace(0, np.nan)
    b = (vw_strong - vw_weak) / tot
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MFI divergence over a half-year (slow money-flow vs price)
def f15vc_f15_volume_price_confirmation_mfidiv_126d_base_v130_signal(close, high, low, closeadj, volume):
    mfi = _f15_mfi(close, high, low, volume, 63)
    mfi_chg = _z(mfi - mfi.shift(126), 252)
    px_chg = _z(closeadj - closeadj.shift(126), 252)
    b = px_chg - mfi_chg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Effort-vs-result over a quarter: volume trend vs |price| trend (churn) 63d
def f15vc_f15_volume_price_confirmation_churn_63d_base_v131_signal(closeadj, volume):
    voltr = _f15_slope(volume.cumsum(), 63)
    pxtr = (closeadj.diff(63).abs()) / (closeadj.rolling(63, min_periods=21).mean().replace(0, np.nan))
    b = _z(voltr, 126) - _z(pxtr, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Accumulation/distribution day count: net A/D-positive days over a quarter
def f15vc_f15_volume_price_confirmation_addaycount_base_v132_signal(close, high, low, volume):
    mfv = _f15_clv(close, high, low) * volume
    pos = (mfv > 0).astype(float)
    neg = (mfv < 0).astype(float)
    b = (pos - neg).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CMF stability: inverse dispersion of CMF over a quarter (durable money flow)
def f15vc_f15_volume_price_confirmation_cmfstable_base_v133_signal(close, high, low, volume):
    cmf = _f15_cmf(close, high, low, volume, 21)
    mu = cmf.rolling(63, min_periods=21).mean()
    sd = cmf.rolling(63, min_periods=21).std().replace(0, np.nan)
    b = mu / sd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# NVI vs price confirmation: NVI slope minus price slope (quiet-day divergence)
def f15vc_f15_volume_price_confirmation_nvidiv_base_v134_signal(close, closeadj, volume):
    nvi = _f15_nvi(close, volume)
    nvi_sl = _z((nvi - nvi.shift(63)) / 63.0, 126)
    px_sl = _z((closeadj - closeadj.shift(63)) / 63.0, 126)
    b = nvi_sl - px_sl
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Up-volume thrust: 21d up-volume share above its 126d norm (accumulation surge)
def f15vc_f15_volume_price_confirmation_upthrust_base_v135_signal(close, volume):
    up = volume.where(close.diff() > 0, 0.0)
    share = up.rolling(21, min_periods=10).sum() / volume.rolling(21, min_periods=10).sum().replace(0, np.nan)
    b = share - share.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Force index sign-flip frequency over a quarter (pressure instability)
def f15vc_f15_volume_price_confirmation_forceflip_base_v136_signal(closeadj, volume):
    fi = _f15_force(closeadj, volume, 13)
    flip = (np.sign(fi) != np.sign(fi.shift(1))).astype(float)
    rate = flip.rolling(63, min_periods=21).mean()
    mag = fi.abs().rolling(63, min_periods=21).mean()
    scale = fi.abs().rolling(252, min_periods=63).mean().replace(0, np.nan)
    b = rate - 0.5 + 0.25 * (mag / scale)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Chaikin oscillator z-scored vs 126d (normalized A/D momentum)
def f15vc_f15_volume_price_confirmation_chaikinz_base_v137_signal(close, high, low, volume):
    ad = _f15_adline(close, high, low, volume)
    osc = ad.ewm(span=21, min_periods=10).mean() - ad.ewm(span=63, min_periods=21).mean()
    b = _z(osc, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Money-flow concentration: top-volume days CMF contribution over a half-year
def f15vc_f15_volume_price_confirmation_mfconc_base_v138_signal(close, high, low, volume):
    clv = _f15_clv(close, high, low)
    volrank = volume.rolling(126, min_periods=63).rank(pct=True)
    heavy_flow = (clv * volume).where(volrank > 0.75, 0.0)
    num = heavy_flow.rolling(126, min_periods=63).sum()
    den = volume.where(volrank > 0.75, 0.0).rolling(126, min_periods=63).sum().replace(0, np.nan)
    b = num / den
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Volume-price rank correlation over a quarter (Spearman-style confirmation)
def f15vc_f15_volume_price_confirmation_vprankcorr_base_v139_signal(closeadj, volume):
    retr = closeadj.pct_change().rolling(63, min_periods=21).rank(pct=True)
    volr = volume.rolling(63, min_periods=21).rank(pct=True)
    b = _corr(retr, volr, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV momentum z-scored (normalized accumulation thrust) over a quarter
def f15vc_f15_volume_price_confirmation_obvmomz_base_v140_signal(close, volume):
    obv = _f15_obv(close, volume)
    mom = obv.diff(21)
    b = _z(mom, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# A/D minus OBV normalized spread level (intrabar vs close-direction flow)
def f15vc_f15_volume_price_confirmation_adobvlevel_base_v141_signal(close, high, low, volume):
    ad = _z(_f15_adline(close, high, low, volume), 126)
    obv = _z(_f15_obv(close, volume), 126)
    b = ad - obv
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Volume-confirmed drawdown: price drawdown weighted by down-volume share 63d
def f15vc_f15_volume_price_confirmation_voldd_base_v142_signal(close, closeadj, volume):
    peak = closeadj.rolling(63, min_periods=21).max()
    dd = closeadj / peak.replace(0, np.nan) - 1.0
    dn_share = _f15_updownvol(close, volume, 21).clip(upper=0).abs()
    b = dd * (1.0 + dn_share)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MFI-CMF spread (typical-price money flow vs CLV money flow disagreement)
def f15vc_f15_volume_price_confirmation_mficmfspr_base_v143_signal(close, high, low, volume):
    mfi = _z(_f15_mfi(close, high, low, volume, 21) - 50.0, 126)
    cmf = _z(_f15_cmf(close, high, low, volume, 21), 126)
    b = mfi - cmf
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Persistent accumulation: smoothed positive money-flow-volume ratio 126d
def f15vc_f15_volume_price_confirmation_persaccum_base_v144_signal(close, high, low, volume):
    mfv = _f15_clv(close, high, low) * volume
    pos = mfv.clip(lower=0).rolling(126, min_periods=63).sum()
    tot = mfv.abs().rolling(126, min_periods=63).sum().replace(0, np.nan)
    b = pos / tot - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Volume-weighted momentum: 63d return scaled by relative dollar-volume level
def f15vc_f15_volume_price_confirmation_dvmom_base_v145_signal(closeadj, volume):
    ret = closeadj / closeadj.shift(63) - 1.0
    dv = closeadj * volume
    dvrel = dv.rolling(21, min_periods=10).mean() / dv.rolling(126, min_periods=63).mean().replace(0, np.nan)
    b = np.tanh(3.0 * ret) * dvrel
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV-confirmed 52w-style strength: OBV near its own 252d high while price rising
def f15vc_f15_volume_price_confirmation_obvstrength_base_v146_signal(close, closeadj, volume):
    obv = _f15_obv(close, volume)
    hi = obv.rolling(252, min_periods=126).max()
    prox = obv / hi.replace(0, np.nan)
    b = prox.where(prox > 0, np.nan) * np.sign(closeadj.diff(63))
    result = b.replace([np.inf, -np.inf], np.nan)
    return _z(result, 126)


# Money-flow reversal pressure: CMF level relative to where it was at last sign flip
def f15vc_f15_volume_price_confirmation_cmfreversal_base_v147_signal(close, high, low, volume):
    cmf = _f15_cmf(close, high, low, volume, 21)
    sign = np.sign(cmf).fillna(0.0)
    grp = (sign != sign.shift()).cumsum()
    age = sign.groupby(grp).cumcount() + 1
    b = cmf * np.log1p(age) / np.log1p(63.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Volume thrust dispersion: variability of directional volume thrust 63d
def f15vc_f15_volume_price_confirmation_thrustdisp_base_v148_signal(close, volume):
    thrust = np.sign(close.diff()) * _z(volume, 63)
    b = thrust.rolling(63, min_periods=21).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Long-horizon money-flow confirmation: 126d CMF * sign of 126d price trend
def f15vc_f15_volume_price_confirmation_cmftrend_126d_base_v149_signal(close, high, low, closeadj, volume):
    cmf = _f15_cmf(close, high, low, volume, 126)
    b = cmf * np.sign(closeadj - closeadj.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Composite flow confirmation: average normalized OBV/AD/PVT slopes signed by price
def f15vc_f15_volume_price_confirmation_flowcomposite_base_v150_signal(close, high, low, closeadj, volume):
    obv = _z(_f15_slope(_f15_obv(close, volume), 63), 126)
    ad = _z(_f15_slope(_f15_adline(close, high, low, volume), 63), 126)
    pvt = _z(_f15_slope(_f15_pvt(closeadj, volume), 63), 126)
    b = (obv + ad + pvt) / 3.0 * np.sign(closeadj.diff(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f15vc_f15_volume_price_confirmation_nvislope_63d_base_v076_signal,
    f15vc_f15_volume_price_confirmation_nvitrend_base_v077_signal,
    f15vc_f15_volume_price_confirmation_pvislope_63d_base_v078_signal,
    f15vc_f15_volume_price_confirmation_pvinvidiv_base_v079_signal,
    f15vc_f15_volume_price_confirmation_obvconf_126d_base_v080_signal,
    f15vc_f15_volume_price_confirmation_obvdiv_126d_base_v081_signal,
    f15vc_f15_volume_price_confirmation_addiv_126d_base_v082_signal,
    f15vc_f15_volume_price_confirmation_adrngpos_base_v083_signal,
    f15vc_f15_volume_price_confirmation_cmfspr_21v126_base_v084_signal,
    f15vc_f15_volume_price_confirmation_cmfflip_base_v085_signal,
    f15vc_f15_volume_price_confirmation_mfidetr_base_v086_signal,
    f15vc_f15_volume_price_confirmation_mfirank_63d_base_v087_signal,
    f15vc_f15_volume_price_confirmation_forcez_13d_base_v088_signal,
    f15vc_f15_volume_price_confirmation_forcerank63_base_v089_signal,
    f15vc_f15_volume_price_confirmation_udvol_126d_base_v090_signal,
    f15vc_f15_volume_price_confirmation_udvolstreak_base_v091_signal,
    f15vc_f15_volume_price_confirmation_pvtslope_126d_base_v092_signal,
    f15vc_f15_volume_price_confirmation_pvtmom_base_v093_signal,
    f15vc_f15_volume_price_confirmation_sdvslope_126d_base_v094_signal,
    f15vc_f15_volume_price_confirmation_eompersist63_base_v095_signal,
    f15vc_f15_volume_price_confirmation_vpcorr_126d_base_v096_signal,
    f15vc_f15_volume_price_confirmation_volthrust_21d_base_v097_signal,
    f15vc_f15_volume_price_confirmation_cmfbreak_base_v098_signal,
    f15vc_f15_volume_price_confirmation_obvdd_base_v099_signal,
    f15vc_f15_volume_price_confirmation_addd_base_v100_signal,
    f15vc_f15_volume_price_confirmation_distrib_126d_base_v101_signal,
    f15vc_f15_volume_price_confirmation_volclvconc_base_v102_signal,
    f15vc_f15_volume_price_confirmation_chaikinosc_base_v103_signal,
    f15vc_f15_volume_price_confirmation_vwapgap_21d_base_v104_signal,
    f15vc_f15_volume_price_confirmation_vwapgapz_63d_base_v105_signal,
    f15vc_f15_volume_price_confirmation_cmfaccel_base_v106_signal,
    f15vc_f15_volume_price_confirmation_forceosc_base_v107_signal,
    f15vc_f15_volume_price_confirmation_retvolasym_base_v108_signal,
    f15vc_f15_volume_price_confirmation_greedconc_base_v109_signal,
    f15vc_f15_volume_price_confirmation_panicconc_base_v110_signal,
    f15vc_f15_volume_price_confirmation_dualconf_base_v111_signal,
    f15vc_f15_volume_price_confirmation_obvadspr_base_v112_signal,
    f15vc_f15_volume_price_confirmation_mfvz_base_v113_signal,
    f15vc_f15_volume_price_confirmation_cleanconf_base_v114_signal,
    f15vc_f15_volume_price_confirmation_cmfslope_base_v115_signal,
    f15vc_f15_volume_price_confirmation_mfiband_base_v116_signal,
    f15vc_f15_volume_price_confirmation_volelast_base_v117_signal,
    f15vc_f15_volume_price_confirmation_obvpvtspr_base_v118_signal,
    f15vc_f15_volume_price_confirmation_admomslow_base_v119_signal,
    f15vc_f15_volume_price_confirmation_cmftrendstr_base_v120_signal,
    f15vc_f15_volume_price_confirmation_forceratio_base_v121_signal,
    f15vc_f15_volume_price_confirmation_cmfrankmom_base_v122_signal,
    f15vc_f15_volume_price_confirmation_silentdist_base_v123_signal,
    f15vc_f15_volume_price_confirmation_obvstab_base_v124_signal,
    f15vc_f15_volume_price_confirmation_cmfsurge_base_v125_signal,
    f15vc_f15_volume_price_confirmation_pvtrank_base_v126_signal,
    f15vc_f15_volume_price_confirmation_adz_252d_base_v127_signal,
    f15vc_f15_volume_price_confirmation_obvz_252d_base_v128_signal,
    f15vc_f15_volume_price_confirmation_clvbreadth_base_v129_signal,
    f15vc_f15_volume_price_confirmation_mfidiv_126d_base_v130_signal,
    f15vc_f15_volume_price_confirmation_churn_63d_base_v131_signal,
    f15vc_f15_volume_price_confirmation_addaycount_base_v132_signal,
    f15vc_f15_volume_price_confirmation_cmfstable_base_v133_signal,
    f15vc_f15_volume_price_confirmation_nvidiv_base_v134_signal,
    f15vc_f15_volume_price_confirmation_upthrust_base_v135_signal,
    f15vc_f15_volume_price_confirmation_forceflip_base_v136_signal,
    f15vc_f15_volume_price_confirmation_chaikinz_base_v137_signal,
    f15vc_f15_volume_price_confirmation_mfconc_base_v138_signal,
    f15vc_f15_volume_price_confirmation_vprankcorr_base_v139_signal,
    f15vc_f15_volume_price_confirmation_obvmomz_base_v140_signal,
    f15vc_f15_volume_price_confirmation_adobvlevel_base_v141_signal,
    f15vc_f15_volume_price_confirmation_voldd_base_v142_signal,
    f15vc_f15_volume_price_confirmation_mficmfspr_base_v143_signal,
    f15vc_f15_volume_price_confirmation_persaccum_base_v144_signal,
    f15vc_f15_volume_price_confirmation_dvmom_base_v145_signal,
    f15vc_f15_volume_price_confirmation_obvstrength_base_v146_signal,
    f15vc_f15_volume_price_confirmation_cmfreversal_base_v147_signal,
    f15vc_f15_volume_price_confirmation_thrustdisp_base_v148_signal,
    f15vc_f15_volume_price_confirmation_cmftrend_126d_base_v149_signal,
    f15vc_f15_volume_price_confirmation_flowcomposite_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F15_VOLUME_PRICE_CONFIRMATION_REGISTRY_076_150 = REGISTRY


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

    print("OK f15_volume_price_confirmation_base_076_150_claude: %d features pass" % n_features)
