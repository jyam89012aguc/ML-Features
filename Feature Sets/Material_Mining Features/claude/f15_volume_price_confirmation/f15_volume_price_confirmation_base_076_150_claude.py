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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rsum(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _slope(s, w):
    def _f(a):
        m = len(a)
        idx = np.arange(m, dtype=float)
        idx = idx - idx.mean()
        denom = float((idx * idx).sum())
        if denom == 0.0:
            return np.nan
        return float((idx * (a - a.mean())).sum()) / denom
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_f, raw=True)


def _rank(s, w):
    return s.rolling(w, min_periods=max(2, w // 4)).rank(pct=True) - 0.5


# ===== folder domain primitives (volume-price confirmation) =====
def _f15_obv(close, volume):
    direction = np.sign(close.diff())
    return (direction * volume).fillna(0.0).cumsum()


def _f15_clv(high, low, close):
    rng = (high - low).replace(0, np.nan)
    return ((close - low) - (high - close)) / rng


def _f15_ad_line(high, low, close, volume):
    mfv = _f15_clv(high, low, close) * volume
    return mfv.fillna(0.0).cumsum()


def _f15_cmf(high, low, close, volume, w):
    mfv = _f15_clv(high, low, close) * volume
    return _rsum(mfv, w) / _rsum(volume, w).replace(0, np.nan)


def _f15_typical(high, low, close):
    return (high + low + close) / 3.0


def _f15_mfi(high, low, close, volume, w):
    tp = _f15_typical(high, low, close)
    rmf = tp * volume
    up = tp.diff()
    pos = rmf.where(up > 0, 0.0)
    neg = rmf.where(up < 0, 0.0)
    pos_s = _rsum(pos, w)
    neg_s = _rsum(neg, w).replace(0, np.nan)
    mr = pos_s / neg_s
    return 100.0 - 100.0 / (1.0 + mr)


def _f15_force(close, volume):
    return close.diff() * volume


def _f15_vpt(closeadj, volume):
    return (closeadj.pct_change() * volume).fillna(0.0).cumsum()


# ============================================================
# OBV slope over a year, normalized by typical volume (long-horizon accumulation trend)
def f15vc_f15_volume_price_confirmation_obvslope_252d_base_v076_signal(close, volume):
    obv = _f15_obv(close, volume)
    b = _slope(obv, 252) / _mean(volume, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV momentum over a half-year scaled by half-year volume (net accumulation share)
def f15vc_f15_volume_price_confirmation_obvmom_126d_base_v077_signal(close, volume):
    obv = _f15_obv(close, volume)
    b = obv.diff(126) / _rsum(volume, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV slope short-minus-long spread (accumulation term structure)
def f15vc_f15_volume_price_confirmation_obvslopespr_base_v078_signal(close, volume):
    obv = _f15_obv(close, volume)
    s_short = _slope(obv, 21) / _mean(volume, 21).replace(0, np.nan)
    s_long = _slope(obv, 126) / _mean(volume, 126).replace(0, np.nan)
    b = s_short - s_long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV z-score vs 252d history (year-scale accumulation extremity)
def f15vc_f15_volume_price_confirmation_obvz_252d_base_v079_signal(close, volume):
    obv = _f15_obv(close, volume)
    b = _z(obv, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV range position over a half-year (where OBV sits within its own band)
def f15vc_f15_volume_price_confirmation_obvrngpos_126d_base_v080_signal(close, volume):
    obv = _f15_obv(close, volume)
    hi = obv.rolling(126, min_periods=63).max()
    lo = obv.rolling(126, min_periods=63).min()
    b = (obv - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV new-low frequency over a quarter (steady distribution / outflow)
def f15vc_f15_volume_price_confirmation_obvnewlo_63d_base_v081_signal(close, volume):
    obv = _f15_obv(close, volume)
    roll_lo = obv.rolling(63, min_periods=21).min()
    roll_hi = obv.rolling(63, min_periods=21).max()
    is_lo = (obv <= roll_lo * 1.00001).astype(float)
    depth = (obv - roll_lo) / (roll_hi - roll_lo).replace(0, np.nan)
    b = is_lo.rolling(63, min_periods=21).mean() - 0.25 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV-momentum acceleration: change in 21d OBV momentum over a month (flow turning)
def f15vc_f15_volume_price_confirmation_obvaccel_21d_base_v082_signal(close, volume):
    obv = _f15_obv(close, volume)
    mom = obv.diff(21) / _rsum(volume, 21).replace(0, np.nan)
    b = mom - mom.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV slope sign agreement with price slope over a half-year (long confirmation regime)
def f15vc_f15_volume_price_confirmation_obvconf_126d_base_v083_signal(close, volume):
    obv = _f15_obv(close, volume)
    osl = _slope(obv, 126)
    psl = _slope(close, 126)
    conf = np.sign(osl) * np.sign(psl)
    b = conf.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV-price divergence over a half-year (hidden long-horizon accumulation)
def f15vc_f15_volume_price_confirmation_obvdiv_126d_base_v084_signal(close, volume):
    obv = _f15_obv(close, volume)
    b = _rank(obv.diff(126), 252) - _rank(close.diff(126), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# A/D line slope over a year, normalized (long-horizon distribution trend)
def f15vc_f15_volume_price_confirmation_adslope_252d_base_v085_signal(high, low, close, volume):
    ad = _f15_ad_line(high, low, close, volume)
    b = _slope(ad, 252) / _mean(volume, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# A/D z-score vs 252d history (year-scale distribution extremity)
def f15vc_f15_volume_price_confirmation_adz_252d_base_v086_signal(high, low, close, volume):
    ad = _f15_ad_line(high, low, close, volume)
    b = _z(ad, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# A/D distance below its 63d high relative to its 63d range (distribution off peak)
def f15vc_f15_volume_price_confirmation_adnewhi_63d_base_v087_signal(high, low, close, volume):
    ad = _f15_ad_line(high, low, close, volume)
    roll_hi = ad.rolling(63, min_periods=21).max()
    roll_lo = ad.rolling(63, min_periods=21).min()
    b = (ad - roll_hi) / (roll_hi - roll_lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# A/D-line rising-day persistence over a quarter blended with CLV depth
def f15vc_f15_volume_price_confirmation_adrise_63d_base_v088_signal(high, low, close, volume):
    ad = _f15_ad_line(high, low, close, volume)
    rising = (ad.diff() > 0).astype(float)
    clv = _f15_clv(high, low, close)
    b = (rising.rolling(63, min_periods=21).mean() - 0.5) + 0.25 * clv.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Chaikin Money Flow over a year (long-horizon money-flow level)
def f15vc_f15_volume_price_confirmation_cmf_252d_base_v089_signal(high, low, close, volume):
    b = _f15_cmf(high, low, close, volume, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CMF slope over a quarter (money-flow trend, not level)
def f15vc_f15_volume_price_confirmation_cmfslope_63d_base_v090_signal(high, low, close, volume):
    cmf = _f15_cmf(high, low, close, volume, 21)
    b = _slope(cmf, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CMF percentile rank vs its own year history (relative money-flow position)
def f15vc_f15_volume_price_confirmation_cmfrank_63d_base_v091_signal(high, low, close, volume):
    cmf = _f15_cmf(high, low, close, volume, 63)
    b = _rank(cmf, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CMF mid vs long spread (63d vs 252d money-flow term structure)
def f15vc_f15_volume_price_confirmation_cmfspr_63v252_base_v092_signal(high, low, close, volume):
    b = _f15_cmf(high, low, close, volume, 63) - _f15_cmf(high, low, close, volume, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CMF dispersion over a quarter (money-flow choppiness vs steady accumulation)
def f15vc_f15_volume_price_confirmation_cmfdisp_63d_base_v093_signal(high, low, close, volume):
    cmf = _f15_cmf(high, low, close, volume, 21)
    b = cmf.rolling(63, min_periods=21).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# negative-CMF time over a half-year (sustained distribution regime, count-friendly)
def f15vc_f15_volume_price_confirmation_cmfnegtime_126d_base_v094_signal(high, low, close, volume):
    cmf = _f15_cmf(high, low, close, volume, 21)
    neg = (cmf < 0).astype(float)
    b = neg.rolling(126, min_periods=63).mean() - 0.5 - cmf
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Money Flow Index over a half-year (long-horizon volume-weighted RSI)
def f15vc_f15_volume_price_confirmation_mfi_126d_base_v095_signal(high, low, close, volume):
    b = _f15_mfi(high, low, close, volume, 126) / 100.0 - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MFI slope over a quarter (money-flow-index trend)
def f15vc_f15_volume_price_confirmation_mfislope_63d_base_v096_signal(high, low, close, volume):
    mfi = _f15_mfi(high, low, close, volume, 21)
    b = _slope(mfi, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MFI overbought-streak persistence over a quarter (distribution-at-top warning)
def f15vc_f15_volume_price_confirmation_mfiob_63d_base_v097_signal(high, low, close, volume):
    mfi = _f15_mfi(high, low, close, volume, 14)
    ob = (mfi >= 80.0).astype(float)
    b = ob.rolling(63, min_periods=21).mean() + 0.01 * (mfi - 50.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MFI vs OBV-rank divergence over a half-year (twin-indicator disagreement)
def f15vc_f15_volume_price_confirmation_mfiobvdiv_126d_base_v098_signal(high, low, close, volume):
    mfi = _f15_mfi(high, low, close, volume, 21) / 100.0 - 0.5
    obv = _f15_obv(close, volume)
    b = _rank(mfi, 252) - _rank(obv.diff(63), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MFI 14d short-window classic, change over a week (fast money-flow swing)
def f15vc_f15_volume_price_confirmation_mfifast_14d_base_v099_signal(high, low, close, volume):
    mfi = _f15_mfi(high, low, close, volume, 14) / 100.0 - 0.5
    b = mfi - mfi.shift(5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Force Index smoothed over a half-year, normalized (long buying/selling pressure)
def f15vc_f15_volume_price_confirmation_force_126d_base_v100_signal(close, volume):
    fi = _f15_force(close, volume)
    fie = fi.ewm(span=126, min_periods=63).mean()
    b = fie / (_mean(close, 126) * _mean(volume, 126)).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Force Index slope over a quarter (acceleration of net force)
def f15vc_f15_volume_price_confirmation_forceslope_63d_base_v101_signal(close, volume):
    fi = _f15_force(close, volume).ewm(span=13, min_periods=7).mean()
    norm = fi / (_mean(close, 21) * _mean(volume, 21)).replace(0, np.nan)
    b = _slope(norm, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Force Index percentile rank vs year history (relative force position)
def f15vc_f15_volume_price_confirmation_forcerank_63d_base_v102_signal(close, volume):
    fi = _f15_force(close, volume).ewm(span=13, min_periods=7).mean()
    norm = fi / (_mean(close, 21) * _mean(volume, 21)).replace(0, np.nan)
    b = _rank(norm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Force Index sign-change frequency over a quarter (force regime instability)
def f15vc_f15_volume_price_confirmation_forcechop_63d_base_v103_signal(close, volume):
    fi = _f15_force(close, volume).ewm(span=13, min_periods=7).mean()
    norm = fi / (_mean(close, 21) * _mean(volume, 21)).replace(0, np.nan)
    flip = (np.sign(fi) != np.sign(fi.shift(1))).astype(float)
    b = flip.rolling(63, min_periods=21).mean() + 0.1 * norm.rolling(21, min_periods=10).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# raw 2-day force index z (Elder's short force), extreme-pressure detector
def f15vc_f15_volume_price_confirmation_force2d_base_v104_signal(close, volume):
    fi = _f15_force(close, volume).rolling(2, min_periods=1).mean()
    norm = fi / (_mean(close, 21) * _mean(volume, 21)).replace(0, np.nan)
    b = _z(norm, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# VPT slope over a half-year (long volume-price-trend direction)
def f15vc_f15_volume_price_confirmation_vptslope_126d_base_v105_signal(closeadj, volume):
    vpt = _f15_vpt(closeadj, volume)
    b = _slope(vpt, 126) / _mean(volume, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# VPT vs its own EMA displacement (volume-price-trend stretch)
def f15vc_f15_volume_price_confirmation_vptdisp_63d_base_v106_signal(closeadj, volume):
    vpt = _f15_vpt(closeadj, volume)
    ema = vpt.ewm(span=63, min_periods=21).mean()
    b = (vpt - ema) / _mean(volume, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# VPT range position over a quarter (where volume-price-trend sits in its own band)
def f15vc_f15_volume_price_confirmation_vptnewhi_63d_base_v107_signal(closeadj, volume):
    vpt = _f15_vpt(closeadj, volume)
    roll_hi = vpt.rolling(63, min_periods=21).max()
    roll_lo = vpt.rolling(63, min_periods=21).min()
    b = (vpt - roll_lo) / (roll_hi - roll_lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Chaikin oscillator z-scored vs its own 126d history
def f15vc_f15_volume_price_confirmation_chaikinoscz_base_v108_signal(high, low, close, volume):
    ad = _f15_ad_line(high, low, close, volume)
    osc = ad.ewm(span=3, min_periods=2).mean() - ad.ewm(span=10, min_periods=5).mean()
    norm = osc / _mean(volume, 21).replace(0, np.nan)
    b = _z(norm, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Chaikin oscillator sign-persistence over a quarter (money-flow momentum regime)
def f15vc_f15_volume_price_confirmation_chaikinoscpersist_base_v109_signal(high, low, close, volume):
    ad = _f15_ad_line(high, low, close, volume)
    osc = ad.ewm(span=3, min_periods=2).mean() - ad.ewm(span=10, min_periods=5).mean()
    pos = (osc > 0).astype(float)
    b = pos.rolling(63, min_periods=21).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume-weighted return divergence vs price over a quarter (>21d -> closeadj)
def f15vc_f15_volume_price_confirmation_dvwret_63d_base_v110_signal(closeadj, volume):
    dv = closeadj * volume
    ret = closeadj.pct_change()
    flow = _rsum(ret * dv, 63) / _rsum(dv, 63).replace(0, np.nan)
    b = flow - ret.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed dollar-volume imbalance over a quarter (>21d -> closeadj): net $ accumulation
def f15vc_f15_volume_price_confirmation_sdvimbal_63d_base_v111_signal(closeadj, volume):
    dv = closeadj * volume
    up = np.sign(closeadj.diff())
    b = _rsum(up * dv, 63) / _rsum(dv, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume trend confirmation: does rising $-vol coincide with rising price (half-year)
def f15vc_f15_volume_price_confirmation_dvconf_126d_base_v112_signal(closeadj, volume):
    dv = closeadj * volume
    b = _slope(dv, 126).pipe(np.sign) * np.sign(_slope(closeadj, 126))
    b = b.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price-volume correlation over a year (long-horizon confirmation regime)
def f15vc_f15_volume_price_confirmation_pvcorr_252d_base_v113_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = volume.diff()
    b = ret.rolling(252, min_periods=126).corr(dv)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# absolute-return-to-volume correlation over a quarter (volume confirms big moves?)
def f15vc_f15_volume_price_confirmation_absrvolcorr_63d_base_v114_signal(closeadj, volume):
    absret = closeadj.pct_change().abs()
    b = absret.rolling(63, min_periods=21).corr(volume)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price-volume correlation change over a quarter (shift in confirmation regime)
def f15vc_f15_volume_price_confirmation_pvcorrchg_63d_base_v115_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = volume.diff()
    c = ret.rolling(63, min_periods=21).corr(dv)
    b = c - c.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up-day vs down-day volume ratio over a year (long directional volume balance)
def f15vc_f15_volume_price_confirmation_updownvol_252d_base_v116_signal(close, volume):
    up = np.sign(close.diff())
    upv = volume.where(up > 0, 0.0)
    dnv = volume.where(up < 0, 0.0)
    b = (_rsum(upv, 252) - _rsum(dnv, 252)) / _rsum(volume, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation-day vs distribution-day net count over a year (count-friendly regime)
def f15vc_f15_volume_price_confirmation_accdist_252d_base_v117_signal(high, low, close):
    clv = _f15_clv(high, low, close)
    acc = (clv > 0.3).astype(float)
    dist = (clv < -0.3).astype(float)
    b = (acc - dist).rolling(252, min_periods=126).sum() / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-weighted CLV over a half-year (long intraday accumulation footprint)
def f15vc_f15_volume_price_confirmation_clvwgt_126d_base_v118_signal(high, low, close, volume):
    clv = _f15_clv(high, low, close)
    b = _rsum(clv * volume, 126) / _rsum(volume, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CLV slope over a quarter (trend in where closes land within range)
def f15vc_f15_volume_price_confirmation_clvslope_63d_base_v119_signal(high, low, close):
    clv = _f15_clv(high, low, close).rolling(5, min_periods=2).mean()
    b = _slope(clv, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CLV z-scored over a half-year (intraday close-position extremity)
def f15vc_f15_volume_price_confirmation_clvz_63d_base_v120_signal(high, low, close):
    clv = _f15_clv(high, low, close).rolling(5, min_periods=2).mean()
    b = _z(clv, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Ease of Movement slope over a quarter (trend in low-volume drift)
def f15vc_f15_volume_price_confirmation_emvslope_63d_base_v121_signal(high, low, volume):
    mid = (high + low) / 2.0
    box = volume / (high - low).replace(0, np.nan)
    emv = (mid.diff() / box.replace(0, np.nan)).rolling(5, min_periods=2).mean()
    b = _slope(emv, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Ease of Movement sign-persistence over a quarter (drift regime, count-friendly)
def f15vc_f15_volume_price_confirmation_emvpersist_63d_base_v122_signal(high, low, volume):
    mid = (high + low) / 2.0
    box = volume / (high - low).replace(0, np.nan)
    emv = (mid.diff() / box.replace(0, np.nan)).rolling(5, min_periods=2).mean()
    pos = (emv > 0).astype(float)
    b = pos.rolling(63, min_periods=21).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV efficiency over a half-year (net change vs total path: smooth vs choppy accum)
def f15vc_f15_volume_price_confirmation_obveff_126d_base_v123_signal(close, volume):
    obv = _f15_obv(close, volume)
    net = obv.diff(126).abs()
    path = obv.diff().abs().rolling(126, min_periods=63).sum()
    b = net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# A/D efficiency over a quarter (net flow vs path: trend purity of accumulation)
def f15vc_f15_volume_price_confirmation_adeff_63d_base_v124_signal(high, low, close, volume):
    ad = _f15_ad_line(high, low, close, volume)
    net = ad.diff(63).abs()
    path = ad.diff().abs().rolling(63, min_periods=21).sum()
    b = net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed-flow concentration over a half-year (one-day dominance of net flow)
def f15vc_f15_volume_price_confirmation_flowconc_126d_base_v125_signal(close, volume):
    sv = np.sign(close.diff()) * volume
    net = sv.rolling(126, min_periods=63).sum().abs()
    mx = sv.abs().rolling(126, min_periods=63).max()
    b = mx / net.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# money-flow-volume skewness over a quarter (asymmetry of accumulation pressure)
def f15vc_f15_volume_price_confirmation_mfvskew_63d_base_v126_signal(high, low, close, volume):
    mfv = (_f15_clv(high, low, close) * volume) / _mean(volume, 21).replace(0, np.nan)
    b = mfv.rolling(63, min_periods=21).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV-to-price elasticity over a half-year (volume response per price move)
def f15vc_f15_volume_price_confirmation_obvelast_126d_base_v127_signal(closeadj, close, volume):
    obv = _f15_obv(close, volume)
    dobv = obv.diff(63) / _mean(volume, 63).replace(0, np.nan)
    dpr = closeadj.pct_change(63)
    b = (dobv / dpr.replace(0, np.nan)).clip(-50, 50)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation-into-weakness over a half-year (smart-money buying multi-month dips)
def f15vc_f15_volume_price_confirmation_accweak_126d_base_v128_signal(high, low, close, volume, closeadj):
    mfv = _f15_clv(high, low, close) * volume
    flow = mfv.rolling(63, min_periods=21).mean()
    flowz = _z(flow, 252)
    drawdown = closeadj / _rmax(closeadj, 504).replace(0, np.nan) - 1.0
    b = flowz * (-drawdown)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CMF gated by drawdown (money flowing in while price is bombed out, cycle-bottom accum)
def f15vc_f15_volume_price_confirmation_cmfbottom_base_v129_signal(high, low, close, volume, closeadj):
    cmf = _f15_cmf(high, low, close, volume, 63)
    dd = closeadj / _rmax(closeadj, 252).replace(0, np.nan) - 1.0
    b = cmf * (-dd)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV slope gated by price near 252d low (accumulation at the lows)
def f15vc_f15_volume_price_confirmation_obvlowaccum_base_v130_signal(close, volume, closeadj):
    obv = _f15_obv(close, volume)
    osl = _slope(obv, 63) / _mean(volume, 63).replace(0, np.nan)
    rngpos = (closeadj - _rmin(closeadj, 252)) / (_rmax(closeadj, 252) - _rmin(closeadj, 252)).replace(0, np.nan)
    b = osl * (1.0 - rngpos)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distribution-at-highs: A/D falling while price near 252d high (smart-money exit)
def f15vc_f15_volume_price_confirmation_addisthi_base_v131_signal(high, low, close, volume, closeadj):
    ad = _f15_ad_line(high, low, close, volume)
    asl = _slope(ad, 63) / _mean(volume, 63).replace(0, np.nan)
    rngpos = (closeadj - _rmin(closeadj, 252)) / (_rmax(closeadj, 252) - _rmin(closeadj, 252)).replace(0, np.nan)
    b = -asl * rngpos
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# triple-confirmation regime: OBV-up & CMF-up & price-up agreement over a quarter
def f15vc_f15_volume_price_confirmation_tripleconf_base_v132_signal(high, low, close, volume, closeadj):
    obv_up = (_f15_obv(close, volume).diff(21) > 0).astype(float)
    cmf_up = (_f15_cmf(high, low, close, volume, 21) > 0).astype(float)
    pr_up = (closeadj.diff(21) > 0).astype(float)
    agree = obv_up + cmf_up + pr_up
    b = agree.rolling(63, min_periods=21).mean() / 3.0 - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-confirmed breakout: price 63d-high coinciding with high CMF (real breakout)
def f15vc_f15_volume_price_confirmation_volbreakout_base_v133_signal(high, low, close, volume, closeadj):
    near_hi = (closeadj >= _rmax(closeadj, 63) * 0.98).astype(float)
    cmf = _f15_cmf(high, low, close, volume, 21)
    b = (near_hi * cmf).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Twiggs money flow z over a year (true-range money flow extremity)
def f15vc_f15_volume_price_confirmation_twiggsz_base_v134_signal(high, low, close, volume):
    prev_close = close.shift(1)
    th = pd.concat([high, prev_close], axis=1).max(axis=1)
    tl = pd.concat([low, prev_close], axis=1).min(axis=1)
    tr = (th - tl).replace(0, np.nan)
    clv = ((close - tl) - (th - close)) / tr
    tmf = (clv * volume).ewm(span=21, min_periods=10).mean() / volume.ewm(span=21, min_periods=10).mean().replace(0, np.nan)
    b = _z(tmf, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-volume-flow rank over a year (relative accumulation position, percentile)
def f15vc_f15_volume_price_confirmation_netflowrank_base_v135_signal(close, volume):
    sv = (np.sign(close.diff()) * volume).fillna(0.0)
    netflow = _rsum(sv, 63) / _rsum(volume, 63).replace(0, np.nan)
    b = _rank(netflow, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# money-flow persistence index: fraction of quarter with positive force AND positive CMF
def f15vc_f15_volume_price_confirmation_mfpersist_base_v136_signal(high, low, close, volume):
    force_pos = (_f15_force(close, volume).ewm(span=13, min_periods=7).mean() > 0).astype(float)
    cmf_pos = (_f15_cmf(high, low, close, volume, 21) > 0).astype(float)
    both = force_pos * cmf_pos
    b = both.rolling(63, min_periods=21).mean() - 0.25
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV divergence streak: consecutive days OBV-rank exceeds price-rank (sustained hidden buy)
def f15vc_f15_volume_price_confirmation_obvdivstreak_base_v137_signal(close, volume):
    obv = _f15_obv(close, volume)
    sig = np.sign(_rank(obv.diff(21), 126) - _rank(close.diff(21), 126)).fillna(0.0)
    grp = (sig != sig.shift(1)).cumsum()
    streak = sig.groupby(grp).cumcount() + 1
    b = (streak * sig) / 63.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-weighted price vs simple price gap over a quarter (>21d -> closeadj, VWAP premium)
def f15vc_f15_volume_price_confirmation_vwapgap_63d_base_v138_signal(closeadj, volume):
    vwap = _rsum(closeadj * volume, 63) / _rsum(volume, 63).replace(0, np.nan)
    b = closeadj / vwap.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# VWAP gap over a half-year (long-horizon position vs volume-weighted cost basis)
def f15vc_f15_volume_price_confirmation_vwapgap_126d_base_v139_signal(closeadj, volume):
    vwap = _rsum(closeadj * volume, 126) / _rsum(volume, 126).replace(0, np.nan)
    b = closeadj / vwap.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# above-VWAP time over a half-year (fraction of days trading above accumulation cost)
def f15vc_f15_volume_price_confirmation_abovevwap_126d_base_v140_signal(closeadj, volume):
    vwap = _rsum(closeadj * volume, 63) / _rsum(volume, 63).replace(0, np.nan)
    above = (closeadj > vwap).astype(float)
    b = above.rolling(126, min_periods=63).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# money-flow-index minus price-RSI proxy (volume-weighting premium over a quarter)
def f15vc_f15_volume_price_confirmation_mfirsigap_base_v141_signal(high, low, close, volume, closeadj):
    mfi = _f15_mfi(high, low, close, volume, 21) / 100.0
    delta = closeadj.diff()
    up = delta.clip(lower=0).rolling(21, min_periods=10).mean()
    dn = (-delta).clip(lower=0).rolling(21, min_periods=10).mean()
    rsi = up / (up + dn).replace(0, np.nan)
    b = mfi - rsi
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CMF acceleration over a half-year basis (slow money-flow turning point)
def f15vc_f15_volume_price_confirmation_cmfaccel_63d_base_v142_signal(high, low, close, volume):
    cmf = _f15_cmf(high, low, close, volume, 63)
    b = cmf - cmf.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# A/D-line second-difference: curvature of accumulation over a quarter
def f15vc_f15_volume_price_confirmation_adcurv_63d_base_v143_signal(high, low, close, volume):
    ad = _f15_ad_line(high, low, close, volume)
    mom = ad.diff(21) / _rsum(volume, 21).replace(0, np.nan)
    b = mom.diff(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# downside-volume capture: avg volume z on down-days vs up-days (panic-volume tilt)
def f15vc_f15_volume_price_confirmation_downvolcap_63d_base_v144_signal(close, volume):
    volz = _z(volume, 63)
    dn = (close.diff() < 0).astype(float)
    up = (close.diff() > 0).astype(float)
    dn_v = (volz * dn).rolling(63, min_periods=21).sum() / dn.rolling(63, min_periods=21).sum().replace(0, np.nan)
    up_v = (volz * up).rolling(63, min_periods=21).sum() / up.rolling(63, min_periods=21).sum().replace(0, np.nan)
    b = dn_v - up_v
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Klinger-style volume oscillator proxy: signed-volume fast vs slow EMA over a quarter
def f15vc_f15_volume_price_confirmation_klinger_base_v145_signal(high, low, close, volume):
    tp = _f15_typical(high, low, close)
    trend = np.sign(tp.diff())
    sv = trend * volume
    osc = sv.ewm(span=34, min_periods=17).mean() - sv.ewm(span=55, min_periods=27).mean()
    b = osc / _mean(volume, 55).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Klinger oscillator signal-line displacement (momentum of volume oscillator)
def f15vc_f15_volume_price_confirmation_klingersig_base_v146_signal(high, low, close, volume):
    tp = _f15_typical(high, low, close)
    trend = np.sign(tp.diff())
    sv = trend * volume
    osc = sv.ewm(span=34, min_periods=17).mean() - sv.ewm(span=55, min_periods=27).mean()
    sig = osc.ewm(span=13, min_periods=7).mean()
    b = (osc - sig) / _mean(volume, 55).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-price-confirmation composite z over a half-year (OBV-z + CMF-z + force-z)
def f15vc_f15_volume_price_confirmation_compositez_base_v147_signal(high, low, close, volume):
    obvz = _z(_f15_obv(close, volume), 126)
    cmfz = _z(_f15_cmf(high, low, close, volume, 21), 126)
    forcez = _z(_f15_force(close, volume).ewm(span=13, min_periods=7).mean(), 126)
    b = (obvz + cmfz + forcez) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CMF sign-streak length over a half-year basis (duration of one-sided money-flow regime)
def f15vc_f15_volume_price_confirmation_regimedist_126d_base_v148_signal(high, low, close, volume):
    cmf = _f15_cmf(high, low, close, volume, 63)
    sgn = np.sign(cmf).fillna(0.0)
    grp = (sgn != sgn.shift(1)).cumsum()
    streak = sgn.groupby(grp).cumcount() + 1
    b = (streak * sgn) / 126.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-weighted momentum: 63d return scaled by volume-trend confirmation
def f15vc_f15_volume_price_confirmation_volwgtmom_base_v149_signal(closeadj, volume):
    mom = closeadj.pct_change(63)
    voltrend = _slope(volume, 63) / _mean(volume, 63).replace(0, np.nan)
    b = mom * np.tanh(voltrend * 63.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV-slope vs A/D-slope term shift: short close-flow vs long intraday-flow disagreement
def f15vc_f15_volume_price_confirmation_flowtermshift_base_v150_signal(high, low, close, volume):
    obv = _f15_obv(close, volume)
    ad = _f15_ad_line(high, low, close, volume)
    obv_sl = _slope(obv, 63) / _mean(volume, 63).replace(0, np.nan)
    ad_sl = _slope(ad, 252) / _mean(volume, 252).replace(0, np.nan)
    b = _rank(obv_sl, 252) - _rank(ad_sl, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f15vc_f15_volume_price_confirmation_obvslope_252d_base_v076_signal,
    f15vc_f15_volume_price_confirmation_obvmom_126d_base_v077_signal,
    f15vc_f15_volume_price_confirmation_obvslopespr_base_v078_signal,
    f15vc_f15_volume_price_confirmation_obvz_252d_base_v079_signal,
    f15vc_f15_volume_price_confirmation_obvrngpos_126d_base_v080_signal,
    f15vc_f15_volume_price_confirmation_obvnewlo_63d_base_v081_signal,
    f15vc_f15_volume_price_confirmation_obvaccel_21d_base_v082_signal,
    f15vc_f15_volume_price_confirmation_obvconf_126d_base_v083_signal,
    f15vc_f15_volume_price_confirmation_obvdiv_126d_base_v084_signal,
    f15vc_f15_volume_price_confirmation_adslope_252d_base_v085_signal,
    f15vc_f15_volume_price_confirmation_adz_252d_base_v086_signal,
    f15vc_f15_volume_price_confirmation_adnewhi_63d_base_v087_signal,
    f15vc_f15_volume_price_confirmation_adrise_63d_base_v088_signal,
    f15vc_f15_volume_price_confirmation_cmf_252d_base_v089_signal,
    f15vc_f15_volume_price_confirmation_cmfslope_63d_base_v090_signal,
    f15vc_f15_volume_price_confirmation_cmfrank_63d_base_v091_signal,
    f15vc_f15_volume_price_confirmation_cmfspr_63v252_base_v092_signal,
    f15vc_f15_volume_price_confirmation_cmfdisp_63d_base_v093_signal,
    f15vc_f15_volume_price_confirmation_cmfnegtime_126d_base_v094_signal,
    f15vc_f15_volume_price_confirmation_mfi_126d_base_v095_signal,
    f15vc_f15_volume_price_confirmation_mfislope_63d_base_v096_signal,
    f15vc_f15_volume_price_confirmation_mfiob_63d_base_v097_signal,
    f15vc_f15_volume_price_confirmation_mfiobvdiv_126d_base_v098_signal,
    f15vc_f15_volume_price_confirmation_mfifast_14d_base_v099_signal,
    f15vc_f15_volume_price_confirmation_force_126d_base_v100_signal,
    f15vc_f15_volume_price_confirmation_forceslope_63d_base_v101_signal,
    f15vc_f15_volume_price_confirmation_forcerank_63d_base_v102_signal,
    f15vc_f15_volume_price_confirmation_forcechop_63d_base_v103_signal,
    f15vc_f15_volume_price_confirmation_force2d_base_v104_signal,
    f15vc_f15_volume_price_confirmation_vptslope_126d_base_v105_signal,
    f15vc_f15_volume_price_confirmation_vptdisp_63d_base_v106_signal,
    f15vc_f15_volume_price_confirmation_vptnewhi_63d_base_v107_signal,
    f15vc_f15_volume_price_confirmation_chaikinoscz_base_v108_signal,
    f15vc_f15_volume_price_confirmation_chaikinoscpersist_base_v109_signal,
    f15vc_f15_volume_price_confirmation_dvwret_63d_base_v110_signal,
    f15vc_f15_volume_price_confirmation_sdvimbal_63d_base_v111_signal,
    f15vc_f15_volume_price_confirmation_dvconf_126d_base_v112_signal,
    f15vc_f15_volume_price_confirmation_pvcorr_252d_base_v113_signal,
    f15vc_f15_volume_price_confirmation_absrvolcorr_63d_base_v114_signal,
    f15vc_f15_volume_price_confirmation_pvcorrchg_63d_base_v115_signal,
    f15vc_f15_volume_price_confirmation_updownvol_252d_base_v116_signal,
    f15vc_f15_volume_price_confirmation_accdist_252d_base_v117_signal,
    f15vc_f15_volume_price_confirmation_clvwgt_126d_base_v118_signal,
    f15vc_f15_volume_price_confirmation_clvslope_63d_base_v119_signal,
    f15vc_f15_volume_price_confirmation_clvz_63d_base_v120_signal,
    f15vc_f15_volume_price_confirmation_emvslope_63d_base_v121_signal,
    f15vc_f15_volume_price_confirmation_emvpersist_63d_base_v122_signal,
    f15vc_f15_volume_price_confirmation_obveff_126d_base_v123_signal,
    f15vc_f15_volume_price_confirmation_adeff_63d_base_v124_signal,
    f15vc_f15_volume_price_confirmation_flowconc_126d_base_v125_signal,
    f15vc_f15_volume_price_confirmation_mfvskew_63d_base_v126_signal,
    f15vc_f15_volume_price_confirmation_obvelast_126d_base_v127_signal,
    f15vc_f15_volume_price_confirmation_accweak_126d_base_v128_signal,
    f15vc_f15_volume_price_confirmation_cmfbottom_base_v129_signal,
    f15vc_f15_volume_price_confirmation_obvlowaccum_base_v130_signal,
    f15vc_f15_volume_price_confirmation_addisthi_base_v131_signal,
    f15vc_f15_volume_price_confirmation_tripleconf_base_v132_signal,
    f15vc_f15_volume_price_confirmation_volbreakout_base_v133_signal,
    f15vc_f15_volume_price_confirmation_twiggsz_base_v134_signal,
    f15vc_f15_volume_price_confirmation_netflowrank_base_v135_signal,
    f15vc_f15_volume_price_confirmation_mfpersist_base_v136_signal,
    f15vc_f15_volume_price_confirmation_obvdivstreak_base_v137_signal,
    f15vc_f15_volume_price_confirmation_vwapgap_63d_base_v138_signal,
    f15vc_f15_volume_price_confirmation_vwapgap_126d_base_v139_signal,
    f15vc_f15_volume_price_confirmation_abovevwap_126d_base_v140_signal,
    f15vc_f15_volume_price_confirmation_mfirsigap_base_v141_signal,
    f15vc_f15_volume_price_confirmation_cmfaccel_63d_base_v142_signal,
    f15vc_f15_volume_price_confirmation_adcurv_63d_base_v143_signal,
    f15vc_f15_volume_price_confirmation_downvolcap_63d_base_v144_signal,
    f15vc_f15_volume_price_confirmation_klinger_base_v145_signal,
    f15vc_f15_volume_price_confirmation_klingersig_base_v146_signal,
    f15vc_f15_volume_price_confirmation_compositez_base_v147_signal,
    f15vc_f15_volume_price_confirmation_regimedist_126d_base_v148_signal,
    f15vc_f15_volume_price_confirmation_volwgtmom_base_v149_signal,
    f15vc_f15_volume_price_confirmation_flowtermshift_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F15_VOLUME_PRICE_CONFIRMATION_REGISTRY_076_150 = REGISTRY


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

    print("OK f15_volume_price_confirmation_base_076_150_claude: %d features pass" % n_features)
