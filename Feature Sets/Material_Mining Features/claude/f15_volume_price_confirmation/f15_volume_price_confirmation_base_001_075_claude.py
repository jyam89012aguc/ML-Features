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
    # OLS slope of s on a 0..len-1 time index, per rolling window (handles partial warm-up)
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
    # On-Balance Volume: signed cumulative volume by close direction
    direction = np.sign(close.diff())
    return (direction * volume).fillna(0.0).cumsum()


def _f15_clv(high, low, close):
    # Close Location Value (a/d multiplier): position of close within the day's range
    rng = (high - low).replace(0, np.nan)
    return ((close - low) - (high - close)) / rng


def _f15_ad_line(high, low, close, volume):
    # Accumulation/Distribution line: cumulative CLV * volume
    mfv = _f15_clv(high, low, close) * volume
    return mfv.fillna(0.0).cumsum()


def _f15_cmf(high, low, close, volume, w):
    # Chaikin Money Flow over window w
    mfv = _f15_clv(high, low, close) * volume
    return _rsum(mfv, w) / _rsum(volume, w).replace(0, np.nan)


def _f15_typical(high, low, close):
    return (high + low + close) / 3.0


def _f15_mfi(high, low, close, volume, w):
    # Money Flow Index over window w
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
    # Force Index: one-period price change * volume
    return close.diff() * volume


def _f15_signed_dollar_vol(closeadj, volume):
    # signed dollar volume by adjusted-close direction (>21d windows use closeadj)
    direction = np.sign(closeadj.diff())
    return direction * closeadj * volume


# ============================================================
# OBV slope over a month, normalized by typical volume (smart-money accumulation pace)
def f15vc_f15_volume_price_confirmation_obvslope_21d_base_v001_signal(close, volume):
    obv = _f15_obv(close, volume)
    b = _slope(obv, 21) / _mean(volume, 21).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV slope over a quarter, normalized by typical volume
def f15vc_f15_volume_price_confirmation_obvslope_63d_base_v002_signal(close, volume):
    obv = _f15_obv(close, volume)
    b = _slope(obv, 63) / _mean(volume, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV slope over a half-year, normalized by typical volume
def f15vc_f15_volume_price_confirmation_obvslope_126d_base_v003_signal(close, volume):
    obv = _f15_obv(close, volume)
    b = _slope(obv, 126) / _mean(volume, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV z-score vs its own 63d history (accumulation extremity)
def f15vc_f15_volume_price_confirmation_obvz_63d_base_v004_signal(close, volume):
    obv = _f15_obv(close, volume)
    b = _z(obv, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV momentum: change over a month divided by month's traded volume (net accum share)
def f15vc_f15_volume_price_confirmation_obvmom_21d_base_v005_signal(close, volume):
    obv = _f15_obv(close, volume)
    b = obv.diff(21) / _rsum(volume, 21).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV momentum over a quarter divided by quarter's volume
def f15vc_f15_volume_price_confirmation_obvmom_63d_base_v006_signal(close, volume):
    obv = _f15_obv(close, volume)
    b = obv.diff(63) / _rsum(volume, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV vs its own 21d EMA (short accumulation displacement)
def f15vc_f15_volume_price_confirmation_obvdisp_21d_base_v007_signal(close, volume):
    obv = _f15_obv(close, volume)
    ema = obv.ewm(span=21, min_periods=10).mean()
    b = (obv - ema) / _mean(volume, 21).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV slope sign agreement with price slope (confirmation regime over a quarter)
def f15vc_f15_volume_price_confirmation_obvpriceconf_63d_base_v008_signal(close, volume):
    obv = _f15_obv(close, volume)
    osl = _slope(obv, 63)
    psl = _slope(close, 63)
    conf = np.sign(osl) * np.sign(psl)
    b = conf.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV-price divergence: OBV-momentum rank minus price-momentum rank (hidden accumulation)
def f15vc_f15_volume_price_confirmation_obvdiv_63d_base_v009_signal(close, volume):
    obv = _f15_obv(close, volume)
    b = _rank(obv.diff(63), 252) - _rank(close.diff(63), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume vs price-level correlation over a quarter (>21d -> closeadj): rising $ at rising price
def f15vc_f15_volume_price_confirmation_sdvslope_63d_base_v010_signal(closeadj, volume):
    dv = closeadj * volume
    b = closeadj.rolling(63, min_periods=21).corr(dv)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume up/down imbalance z over a half-year (>21d -> closeadj)
def f15vc_f15_volume_price_confirmation_sdvslope_126d_base_v011_signal(closeadj, volume):
    sdv = _f15_signed_dollar_vol(closeadj, volume)
    imbalance = _rsum(sdv, 126) / _rsum(closeadj * volume, 126).replace(0, np.nan)
    b = _z(imbalance, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Accumulation/Distribution line slope over a month
def f15vc_f15_volume_price_confirmation_adslope_21d_base_v012_signal(high, low, close, volume):
    ad = _f15_ad_line(high, low, close, volume)
    b = _slope(ad, 21) / _mean(volume, 21).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# A/D line slope over a quarter
def f15vc_f15_volume_price_confirmation_adslope_63d_base_v013_signal(high, low, close, volume):
    ad = _f15_ad_line(high, low, close, volume)
    b = _slope(ad, 63) / _mean(volume, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# A/D line slope over a half-year
def f15vc_f15_volume_price_confirmation_adslope_126d_base_v014_signal(high, low, close, volume):
    ad = _f15_ad_line(high, low, close, volume)
    b = _slope(ad, 126) / _mean(volume, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# A/D line z-score vs its own 63d history
def f15vc_f15_volume_price_confirmation_adz_63d_base_v015_signal(high, low, close, volume):
    ad = _f15_ad_line(high, low, close, volume)
    b = _z(ad, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# A/D-line rising-day persistence blended with CLV depth over a month (accumulation footprint)
def f15vc_f15_volume_price_confirmation_admom_21d_base_v016_signal(high, low, close, volume):
    ad = _f15_ad_line(high, low, close, volume)
    rising = (ad.diff() > 0).astype(float)
    clv = _f15_clv(high, low, close)
    b = (rising.rolling(21, min_periods=10).mean() - 0.5) + 0.25 * clv.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# A/D-line drawdown from its own 63d high (distribution stress relative to peak accumulation)
def f15vc_f15_volume_price_confirmation_admom_63d_base_v017_signal(high, low, close, volume):
    ad = _f15_ad_line(high, low, close, volume)
    hi = ad.rolling(63, min_periods=21).max()
    b = (ad - hi) / _rsum(volume, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# A/D-price divergence: A/D-momentum rank minus price-momentum rank over a quarter
def f15vc_f15_volume_price_confirmation_addiv_63d_base_v018_signal(high, low, close, volume, closeadj):
    ad = _f15_ad_line(high, low, close, volume)
    b = _rank(ad.diff(63), 252) - _rank(closeadj.diff(63), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# A/D-line range position over a half-year (where current accumulation sits in its band)
def f15vc_f15_volume_price_confirmation_addisp_63d_base_v019_signal(high, low, close, volume):
    ad = _f15_ad_line(high, low, close, volume)
    hi = ad.rolling(126, min_periods=63).max()
    lo = ad.rolling(126, min_periods=63).min()
    b = (ad - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Chaikin Money Flow over a month (intraday accumulation pressure)
def f15vc_f15_volume_price_confirmation_cmf_21d_base_v020_signal(high, low, close, volume):
    b = _f15_cmf(high, low, close, volume, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Chaikin Money Flow over a quarter
def f15vc_f15_volume_price_confirmation_cmf_63d_base_v021_signal(high, low, close, volume):
    b = _f15_cmf(high, low, close, volume, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Chaikin Money Flow over a half-year
def f15vc_f15_volume_price_confirmation_cmf_126d_base_v022_signal(high, low, close, volume):
    b = _f15_cmf(high, low, close, volume, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CMF z-scored vs its own 126d history (extreme money flow)
def f15vc_f15_volume_price_confirmation_cmfz_63d_base_v023_signal(high, low, close, volume):
    cmf = _f15_cmf(high, low, close, volume, 63)
    b = _z(cmf, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CMF short-minus-long spread (money-flow term structure)
def f15vc_f15_volume_price_confirmation_cmfspr_21v126_base_v024_signal(high, low, close, volume):
    b = _f15_cmf(high, low, close, volume, 21) - _f15_cmf(high, low, close, volume, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CMF persistence: fraction of last quarter with positive 21d CMF (steady accumulation)
def f15vc_f15_volume_price_confirmation_cmfpersist_63d_base_v025_signal(high, low, close, volume):
    cmf = _f15_cmf(high, low, close, volume, 21)
    pos = (cmf > 0).astype(float)
    b = pos.rolling(63, min_periods=21).mean() + 0.5 * cmf
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Money Flow Index over a month (overbought/oversold via volume)
def f15vc_f15_volume_price_confirmation_mfi_21d_base_v026_signal(high, low, close, volume):
    b = _f15_mfi(high, low, close, volume, 21) / 100.0 - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Money Flow Index over a quarter
def f15vc_f15_volume_price_confirmation_mfi_63d_base_v027_signal(high, low, close, volume):
    b = _f15_mfi(high, low, close, volume, 63) / 100.0 - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MFI z-scored vs its own 126d history
def f15vc_f15_volume_price_confirmation_mfiz_21d_base_v028_signal(high, low, close, volume):
    mfi = _f15_mfi(high, low, close, volume, 21)
    b = _z(mfi, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MFI-price divergence: MFI minus price-position over a quarter (hidden flow)
def f15vc_f15_volume_price_confirmation_mfidiv_63d_base_v029_signal(high, low, close, volume, closeadj):
    mfi = _f15_mfi(high, low, close, volume, 21) / 100.0 - 0.5
    ppos = _rank(closeadj, 63)
    b = mfi - ppos
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MFI extreme-time spread: overbought-time minus oversold-time over a quarter
def f15vc_f15_volume_price_confirmation_mfilow_63d_base_v030_signal(high, low, close, volume):
    mfi = _f15_mfi(high, low, close, volume, 21)
    low_t = (mfi <= 20.0).astype(float)
    high_t = (mfi >= 80.0).astype(float)
    b = high_t.rolling(63, min_periods=21).mean() - low_t.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Force Index smoothed over 13d (classic Elder force), normalized
def f15vc_f15_volume_price_confirmation_force_13d_base_v031_signal(close, volume):
    fi = _f15_force(close, volume)
    fie = fi.ewm(span=13, min_periods=7).mean()
    b = fie / (_mean(close, 21) * _mean(volume, 21)).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Force Index smoothed over a quarter, normalized
def f15vc_f15_volume_price_confirmation_force_63d_base_v032_signal(close, volume):
    fi = _f15_force(close, volume)
    fie = fi.ewm(span=63, min_periods=21).mean()
    b = fie / (_mean(close, 63) * _mean(volume, 63)).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Force Index z-scored vs its 126d history
def f15vc_f15_volume_price_confirmation_forcez_21d_base_v033_signal(close, volume):
    fi = _f15_force(close, volume)
    fie = fi.rolling(21, min_periods=10).mean()
    b = _z(fie, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# force-index up vs down asymmetry over a quarter (selling force heavier than buying?)
def f15vc_f15_volume_price_confirmation_forceslope_63d_base_v034_signal(close, volume):
    fi = _f15_force(close, volume)
    pos = _rsum(fi.clip(lower=0), 63)
    neg = _rsum((-fi).clip(lower=0), 63)
    b = (pos - neg) / (pos + neg).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return-magnitude-weighted volume balance over a month (big up-moves on volume vs big down)
def f15vc_f15_volume_price_confirmation_updownvol_21d_base_v035_signal(close, volume):
    ret = close.pct_change()
    upw = (ret.clip(lower=0) * volume)
    dnw = ((-ret).clip(lower=0) * volume)
    b = (_rsum(upw, 21) - _rsum(dnw, 21)) / (_rsum(upw, 21) + _rsum(dnw, 21)).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# average volume on up-days vs down-days over a quarter (volume preference asymmetry)
def f15vc_f15_volume_price_confirmation_updownvol_63d_base_v036_signal(close, volume):
    up = np.sign(close.diff())
    upv = volume.where(up > 0, np.nan)
    dnv = volume.where(up < 0, np.nan)
    avg_up = upv.rolling(63, min_periods=10).mean()
    avg_dn = dnv.rolling(63, min_periods=10).mean()
    b = (avg_up - avg_dn) / (avg_up + avg_dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# concentration of returns in high-volume days vs low-volume days over a quarter
def f15vc_f15_volume_price_confirmation_volwgtret_63d_base_v037_signal(closeadj, volume):
    ret = closeadj.pct_change()
    hivol = (volume > _mean(volume, 63)).astype(float)
    ret_hi = (ret * hivol).rolling(63, min_periods=21).mean()
    ret_lo = (ret * (1 - hivol)).rolling(63, min_periods=21).mean()
    b = ret_hi - ret_lo
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# effort-vs-result: volume z minus absolute-return z (churn without price progress)
def f15vc_f15_volume_price_confirmation_effortresult_21d_base_v038_signal(closeadj, volume):
    volz = _z(volume, 63)
    absret = closeadj.pct_change().abs()
    rz = _z(absret, 63)
    b = volz - rz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price-volume correlation over a quarter (confirmation vs divergence)
def f15vc_f15_volume_price_confirmation_pvcorr_63d_base_v039_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = volume.diff()
    b = ret.rolling(63, min_periods=21).corr(dv)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price-volume correlation over a half-year
def f15vc_f15_volume_price_confirmation_pvcorr_126d_base_v040_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = volume.diff()
    b = ret.rolling(126, min_periods=63).corr(dv)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Chaikin oscillator: A/D fast EMA minus slow EMA (money-flow momentum)
def f15vc_f15_volume_price_confirmation_chaikinosc_base_v041_signal(high, low, close, volume):
    ad = _f15_ad_line(high, low, close, volume)
    osc = ad.ewm(span=3, min_periods=2).mean() - ad.ewm(span=10, min_periods=5).mean()
    b = osc / _mean(volume, 21).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Chaikin oscillator slower variant (21 vs 63)
def f15vc_f15_volume_price_confirmation_chaikinosc_slow_base_v042_signal(high, low, close, volume):
    ad = _f15_ad_line(high, low, close, volume)
    osc = ad.ewm(span=21, min_periods=10).mean() - ad.ewm(span=63, min_periods=21).mean()
    b = osc / _mean(volume, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV efficiency ratio: net OBV change vs total absolute OBV path over a quarter
def f15vc_f15_volume_price_confirmation_obveff_63d_base_v043_signal(close, volume):
    obv = _f15_obv(close, volume)
    net = obv.diff(63).abs()
    path = obv.diff().abs().rolling(63, min_periods=21).sum()
    b = net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation-day balance: net count of CLV>0 vs CLV<0 days over a quarter
def f15vc_f15_volume_price_confirmation_accdays_63d_base_v044_signal(high, low, close, volume):
    clv = _f15_clv(high, low, close)
    acc = (clv > 0).astype(float)
    dist = (clv < 0).astype(float)
    b = (acc - dist).rolling(63, min_periods=21).mean() + clv.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation-into-weakness: money-flow z while in drawdown (smart-money buying dips)
def f15vc_f15_volume_price_confirmation_accweak_63d_base_v045_signal(high, low, close, volume, closeadj):
    mfv = _f15_clv(high, low, close) * volume
    flow = mfv.rolling(21, min_periods=10).mean()
    flowz = _z(flow, 126)
    drawdown = closeadj / _rmax(closeadj, 252).replace(0, np.nan) - 1.0
    b = flowz * (-drawdown)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CMF acceleration: change in 21d CMF over a month
def f15vc_f15_volume_price_confirmation_cmfaccel_21d_base_v046_signal(high, low, close, volume):
    cmf = _f15_cmf(high, low, close, volume, 21)
    b = cmf - cmf.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV new-high frequency: fraction of last quarter OBV makes a new 63d high (steady accum)
def f15vc_f15_volume_price_confirmation_obvnewhi_63d_base_v047_signal(close, volume):
    obv = _f15_obv(close, volume)
    roll_hi = obv.rolling(63, min_periods=21).max()
    is_hi = (obv >= roll_hi * 0.99999).astype(float)
    b = is_hi.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# negative-volume-index proxy: cum return on volume-decline (quiet) days, slope over a quarter
def f15vc_f15_volume_price_confirmation_nvi_63d_base_v048_signal(closeadj, volume):
    ret = closeadj.pct_change()
    quiet = (volume.diff() < 0).astype(float)
    nvi = (ret * quiet).fillna(0.0).cumsum()
    b = _slope(nvi, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# positive-volume-index proxy: cum return on volume-increase (busy) days, slope over a quarter
def f15vc_f15_volume_price_confirmation_pvi_63d_base_v049_signal(closeadj, volume):
    ret = closeadj.pct_change()
    busy = (volume.diff() > 0).astype(float)
    pvi = (ret * busy).fillna(0.0).cumsum()
    b = _slope(pvi, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# twin-confirmation: MFI-sign and OBV-momentum-sign agreement over a quarter
def f15vc_f15_volume_price_confirmation_twinconf_63d_base_v050_signal(high, low, close, volume):
    mfi = _f15_mfi(high, low, close, volume, 21) / 100.0 - 0.5
    obv = _f15_obv(close, volume)
    obvm = obv.diff(21) / _rsum(volume, 21).replace(0, np.nan)
    agree = np.sign(mfi) * np.sign(obvm)
    b = agree.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Twiggs money flow proxy: true-range CLV with EMA smoothing over a quarter
def f15vc_f15_volume_price_confirmation_twiggs_63d_base_v051_signal(high, low, close, volume):
    prev_close = close.shift(1)
    th = pd.concat([high, prev_close], axis=1).max(axis=1)
    tl = pd.concat([low, prev_close], axis=1).min(axis=1)
    tr = (th - tl).replace(0, np.nan)
    clv = ((close - tl) - (th - close)) / tr
    mfv = clv * volume
    b = mfv.ewm(span=63, min_periods=21).mean() / volume.ewm(span=63, min_periods=21).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Volume-Price Trend (VPT) slope over a quarter
def f15vc_f15_volume_price_confirmation_vpt_63d_base_v052_signal(closeadj, volume):
    vpt = (closeadj.pct_change() * volume).fillna(0.0).cumsum()
    b = _slope(vpt, 63) / _mean(volume, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# VPT z-score vs 126d history
def f15vc_f15_volume_price_confirmation_vptz_63d_base_v053_signal(closeadj, volume):
    vpt = (closeadj.pct_change() * volume).fillna(0.0).cumsum()
    b = _z(vpt, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Ease of Movement over a month (price drift per unit of volume box)
def f15vc_f15_volume_price_confirmation_emv_21d_base_v054_signal(high, low, volume):
    mid = (high + low) / 2.0
    box = volume / (high - low).replace(0, np.nan)
    emv = mid.diff() / box.replace(0, np.nan)
    b = emv.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Ease of Movement z-scored over a quarter window
def f15vc_f15_volume_price_confirmation_emv_63d_base_v055_signal(high, low, volume):
    mid = (high + low) / 2.0
    box = volume / (high - low).replace(0, np.nan)
    emv = mid.diff() / box.replace(0, np.nan)
    b = _z(emv.rolling(21, min_periods=10).mean(), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV-slope rank minus volatility rank (accumulation that is NOT just a vol artifact)
def f15vc_f15_volume_price_confirmation_obvvol_63d_base_v056_signal(close, closeadj, volume):
    obv = _f15_obv(close, volume)
    osl = _slope(obv, 63) / _mean(volume, 63).replace(0, np.nan)
    vol = closeadj.pct_change().rolling(63, min_periods=21).std()
    b = _rank(osl, 252) - _rank(vol, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# A/D-slope rank minus volatility rank over a year (genuine accumulation vs vol artifact)
def f15vc_f15_volume_price_confirmation_advol_63d_base_v057_signal(high, low, close, closeadj, volume):
    ad = _f15_ad_line(high, low, close, volume)
    asl = _slope(ad, 63) / _mean(volume, 63).replace(0, np.nan)
    vol = closeadj.pct_change().rolling(63, min_periods=21).std()
    b = _rank(asl, 252) - _rank(vol, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed-flow concentration: biggest single-day net flow share over a quarter
def f15vc_f15_volume_price_confirmation_flowconc_63d_base_v058_signal(close, volume):
    sv = np.sign(close.diff()) * volume
    net = sv.rolling(63, min_periods=21).sum().abs()
    mx = sv.abs().rolling(63, min_periods=21).max()
    b = mx / net.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation breadth: net CLV-weighted volume share ranked vs history
def f15vc_f15_volume_price_confirmation_accbreadth_63d_base_v059_signal(high, low, close, volume):
    mfv = _f15_clv(high, low, close) * volume
    net = _rsum(mfv, 63) / _rsum(volume, 63).replace(0, np.nan)
    b = _rank(net, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CMF sign-streak length (consecutive days of one-sided money flow)
def f15vc_f15_volume_price_confirmation_cmfstreak_base_v060_signal(high, low, close, volume):
    cmf = _f15_cmf(high, low, close, volume, 21)
    sgn = np.sign(cmf).fillna(0.0)
    grp = (sgn != sgn.shift(1)).cumsum()
    streak = sgn.groupby(grp).cumcount() + 1
    b = (streak * sgn) / 63.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# divergence tally: bearish (price up / flow down) minus bullish (price down / flow up)
def f15vc_f15_volume_price_confirmation_beardiv_63d_base_v061_signal(high, low, close, volume, closeadj):
    pr_up = (closeadj.diff(21) > 0).astype(float)
    cmf = _f15_cmf(high, low, close, volume, 21)
    bear = pr_up * (cmf.diff(21) < 0).astype(float)
    bull = (1 - pr_up) * (cmf.diff(21) > 0).astype(float)
    b = bear.rolling(63, min_periods=21).mean() - bull.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# force-index sign persistence over a quarter (sustained buying/selling pressure)
def f15vc_f15_volume_price_confirmation_forcepersist_63d_base_v062_signal(close, volume):
    fi = _f15_force(close, volume).ewm(span=13, min_periods=7).mean()
    pos = (fi > 0).astype(float)
    b = pos.rolling(63, min_periods=21).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV-to-price elasticity: OBV change per percent price change over a month
def f15vc_f15_volume_price_confirmation_obvelast_63d_base_v063_signal(closeadj, close, volume):
    obv = _f15_obv(close, volume)
    dobv = obv.diff(21) / _mean(volume, 21).replace(0, np.nan)
    dpr = closeadj.pct_change(21)
    b = (dobv / dpr.replace(0, np.nan)).clip(-50, 50)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# money-flow-volume dispersion over a quarter (flow choppiness)
def f15vc_f15_volume_price_confirmation_flowdisp_63d_base_v064_signal(high, low, close, volume):
    mfv = _f15_clv(high, low, close) * volume
    norm = mfv / _mean(volume, 21).replace(0, np.nan)
    b = norm.rolling(63, min_periods=21).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CMF gated by a volume surge (accumulation confirmed by a spike)
def f15vc_f15_volume_price_confirmation_cmfsurge_base_v065_signal(high, low, close, volume):
    cmf = _f15_cmf(high, low, close, volume, 21)
    surge = volume / _mean(volume, 63).replace(0, np.nan)
    b = cmf * np.tanh(surge - 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# A/D slope short-minus-long spread (flow term structure)
def f15vc_f15_volume_price_confirmation_adslopespr_base_v066_signal(high, low, close, volume):
    ad = _f15_ad_line(high, low, close, volume)
    s_short = _slope(ad, 21) / _mean(volume, 21).replace(0, np.nan)
    s_long = _slope(ad, 126) / _mean(volume, 126).replace(0, np.nan)
    b = s_short - s_long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV drawdown: distance of OBV below its own 126d high (distribution stress)
def f15vc_f15_volume_price_confirmation_obvdd_126d_base_v067_signal(close, volume):
    obv = _f15_obv(close, volume)
    hi = obv.rolling(126, min_periods=63).max()
    b = (obv - hi) / _mean(volume, 126).replace(0, np.nan) / 126.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# money-flow-ratio momentum: quarter-over-quarter change in log positive/negative flow
def f15vc_f15_volume_price_confirmation_mfratio_63d_base_v068_signal(high, low, close, volume):
    tp = _f15_typical(high, low, close)
    rmf = tp * volume
    up = tp.diff()
    pos = _rsum(rmf.where(up > 0, 0.0), 63)
    neg = _rsum(rmf.where(up < 0, 0.0), 63).replace(0, np.nan)
    ratio = np.log(pos.replace(0, np.nan) / neg)
    b = ratio - ratio.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday close-location average over a month (where closes land in range)
def f15vc_f15_volume_price_confirmation_clvavg_21d_base_v069_signal(high, low, close):
    clv = _f15_clv(high, low, close)
    b = clv.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-weighted minus equal-weighted CLV over a quarter (do big days accumulate more?)
def f15vc_f15_volume_price_confirmation_clvwgt_63d_base_v070_signal(high, low, close, volume):
    clv = _f15_clv(high, low, close)
    vw = _rsum(clv * volume, 63) / _rsum(volume, 63).replace(0, np.nan)
    ew = clv.rolling(63, min_periods=21).mean()
    b = vw - ew
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV slope minus A/D slope (close-based vs intraday flow disagreement)
def f15vc_f15_volume_price_confirmation_obvaddisagree_63d_base_v071_signal(high, low, close, volume):
    obv = _f15_obv(close, volume)
    ad = _f15_ad_line(high, low, close, volume)
    so = _slope(obv, 63) / _mean(volume, 63).replace(0, np.nan)
    sa = _slope(ad, 63) / _mean(volume, 63).replace(0, np.nan)
    b = so - sa
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Force-Index divergence from price over a quarter (effort not yielding price)
def f15vc_f15_volume_price_confirmation_forcediv_63d_base_v072_signal(closeadj, close, volume):
    fi = _f15_force(close, volume).ewm(span=13, min_periods=7).mean()
    b = _rank(fi, 252) - _rank(closeadj.diff(21), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up-day volume share change over a month (flow regime shift)
def f15vc_f15_volume_price_confirmation_volshift_21d_base_v073_signal(close, volume):
    up = np.sign(close.diff())
    upv = volume.where(up > 0, 0.0)
    bal = _rsum(upv, 21) / _rsum(volume, 21).replace(0, np.nan)
    b = bal - bal.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Chaikin money flow tanh-squashed momentum (bounded flow acceleration)
def f15vc_f15_volume_price_confirmation_cmftanh_63d_base_v074_signal(high, low, close, volume):
    cmf = _f15_cmf(high, low, close, volume, 21)
    chg = cmf - cmf.shift(21)
    b = np.tanh(5.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite confirmation score: OBV-slope-sign + CMF-sign + force-sign + OBV-z tilt
def f15vc_f15_volume_price_confirmation_confscore_63d_base_v075_signal(high, low, close, volume):
    obv = _f15_obv(close, volume)
    so = np.sign(_slope(obv, 63))
    cmf = np.sign(_f15_cmf(high, low, close, volume, 63))
    fi = np.sign(_f15_force(close, volume).ewm(span=63, min_periods=21).mean())
    b = (so + cmf + fi) / 3.0 + 0.1 * _z(obv, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f15vc_f15_volume_price_confirmation_obvslope_21d_base_v001_signal,
    f15vc_f15_volume_price_confirmation_obvslope_63d_base_v002_signal,
    f15vc_f15_volume_price_confirmation_obvslope_126d_base_v003_signal,
    f15vc_f15_volume_price_confirmation_obvz_63d_base_v004_signal,
    f15vc_f15_volume_price_confirmation_obvmom_21d_base_v005_signal,
    f15vc_f15_volume_price_confirmation_obvmom_63d_base_v006_signal,
    f15vc_f15_volume_price_confirmation_obvdisp_21d_base_v007_signal,
    f15vc_f15_volume_price_confirmation_obvpriceconf_63d_base_v008_signal,
    f15vc_f15_volume_price_confirmation_obvdiv_63d_base_v009_signal,
    f15vc_f15_volume_price_confirmation_sdvslope_63d_base_v010_signal,
    f15vc_f15_volume_price_confirmation_sdvslope_126d_base_v011_signal,
    f15vc_f15_volume_price_confirmation_adslope_21d_base_v012_signal,
    f15vc_f15_volume_price_confirmation_adslope_63d_base_v013_signal,
    f15vc_f15_volume_price_confirmation_adslope_126d_base_v014_signal,
    f15vc_f15_volume_price_confirmation_adz_63d_base_v015_signal,
    f15vc_f15_volume_price_confirmation_admom_21d_base_v016_signal,
    f15vc_f15_volume_price_confirmation_admom_63d_base_v017_signal,
    f15vc_f15_volume_price_confirmation_addiv_63d_base_v018_signal,
    f15vc_f15_volume_price_confirmation_addisp_63d_base_v019_signal,
    f15vc_f15_volume_price_confirmation_cmf_21d_base_v020_signal,
    f15vc_f15_volume_price_confirmation_cmf_63d_base_v021_signal,
    f15vc_f15_volume_price_confirmation_cmf_126d_base_v022_signal,
    f15vc_f15_volume_price_confirmation_cmfz_63d_base_v023_signal,
    f15vc_f15_volume_price_confirmation_cmfspr_21v126_base_v024_signal,
    f15vc_f15_volume_price_confirmation_cmfpersist_63d_base_v025_signal,
    f15vc_f15_volume_price_confirmation_mfi_21d_base_v026_signal,
    f15vc_f15_volume_price_confirmation_mfi_63d_base_v027_signal,
    f15vc_f15_volume_price_confirmation_mfiz_21d_base_v028_signal,
    f15vc_f15_volume_price_confirmation_mfidiv_63d_base_v029_signal,
    f15vc_f15_volume_price_confirmation_mfilow_63d_base_v030_signal,
    f15vc_f15_volume_price_confirmation_force_13d_base_v031_signal,
    f15vc_f15_volume_price_confirmation_force_63d_base_v032_signal,
    f15vc_f15_volume_price_confirmation_forcez_21d_base_v033_signal,
    f15vc_f15_volume_price_confirmation_forceslope_63d_base_v034_signal,
    f15vc_f15_volume_price_confirmation_updownvol_21d_base_v035_signal,
    f15vc_f15_volume_price_confirmation_updownvol_63d_base_v036_signal,
    f15vc_f15_volume_price_confirmation_volwgtret_63d_base_v037_signal,
    f15vc_f15_volume_price_confirmation_effortresult_21d_base_v038_signal,
    f15vc_f15_volume_price_confirmation_pvcorr_63d_base_v039_signal,
    f15vc_f15_volume_price_confirmation_pvcorr_126d_base_v040_signal,
    f15vc_f15_volume_price_confirmation_chaikinosc_base_v041_signal,
    f15vc_f15_volume_price_confirmation_chaikinosc_slow_base_v042_signal,
    f15vc_f15_volume_price_confirmation_obveff_63d_base_v043_signal,
    f15vc_f15_volume_price_confirmation_accdays_63d_base_v044_signal,
    f15vc_f15_volume_price_confirmation_accweak_63d_base_v045_signal,
    f15vc_f15_volume_price_confirmation_cmfaccel_21d_base_v046_signal,
    f15vc_f15_volume_price_confirmation_obvnewhi_63d_base_v047_signal,
    f15vc_f15_volume_price_confirmation_nvi_63d_base_v048_signal,
    f15vc_f15_volume_price_confirmation_pvi_63d_base_v049_signal,
    f15vc_f15_volume_price_confirmation_twinconf_63d_base_v050_signal,
    f15vc_f15_volume_price_confirmation_twiggs_63d_base_v051_signal,
    f15vc_f15_volume_price_confirmation_vpt_63d_base_v052_signal,
    f15vc_f15_volume_price_confirmation_vptz_63d_base_v053_signal,
    f15vc_f15_volume_price_confirmation_emv_21d_base_v054_signal,
    f15vc_f15_volume_price_confirmation_emv_63d_base_v055_signal,
    f15vc_f15_volume_price_confirmation_obvvol_63d_base_v056_signal,
    f15vc_f15_volume_price_confirmation_advol_63d_base_v057_signal,
    f15vc_f15_volume_price_confirmation_flowconc_63d_base_v058_signal,
    f15vc_f15_volume_price_confirmation_accbreadth_63d_base_v059_signal,
    f15vc_f15_volume_price_confirmation_cmfstreak_base_v060_signal,
    f15vc_f15_volume_price_confirmation_beardiv_63d_base_v061_signal,
    f15vc_f15_volume_price_confirmation_forcepersist_63d_base_v062_signal,
    f15vc_f15_volume_price_confirmation_obvelast_63d_base_v063_signal,
    f15vc_f15_volume_price_confirmation_flowdisp_63d_base_v064_signal,
    f15vc_f15_volume_price_confirmation_cmfsurge_base_v065_signal,
    f15vc_f15_volume_price_confirmation_adslopespr_base_v066_signal,
    f15vc_f15_volume_price_confirmation_obvdd_126d_base_v067_signal,
    f15vc_f15_volume_price_confirmation_mfratio_63d_base_v068_signal,
    f15vc_f15_volume_price_confirmation_clvavg_21d_base_v069_signal,
    f15vc_f15_volume_price_confirmation_clvwgt_63d_base_v070_signal,
    f15vc_f15_volume_price_confirmation_obvaddisagree_63d_base_v071_signal,
    f15vc_f15_volume_price_confirmation_forcediv_63d_base_v072_signal,
    f15vc_f15_volume_price_confirmation_volshift_21d_base_v073_signal,
    f15vc_f15_volume_price_confirmation_cmftanh_63d_base_v074_signal,
    f15vc_f15_volume_price_confirmation_confscore_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F15_VOLUME_PRICE_CONFIRMATION_REGISTRY_001_075 = REGISTRY


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

    print("OK f15_volume_price_confirmation_base_001_075_claude: %d features pass" % n_features)
