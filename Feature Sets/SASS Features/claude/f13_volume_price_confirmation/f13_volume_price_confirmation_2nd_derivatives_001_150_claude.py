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


def _sum(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _roc(s, w):
    # 1st math derivative: rate of change of a feature over window w (per-day slope)
    return (s - s.shift(w)) / float(w)


def _slope(s, w):
    idx = np.arange(w, dtype=float)
    idx = idx - idx.mean()
    denom = (idx ** 2).sum()

    def _f(a):
        if np.isnan(a).any():
            return np.nan
        return float((idx * (a - a.mean())).sum() / denom)
    return s.rolling(w, min_periods=w).apply(_f, raw=True)


# ===== folder domain primitives (volume-price confirmation) =====
def _f13_obv(close, volume):
    direction = np.sign(close.diff())
    return (direction * volume).fillna(0.0).cumsum()


def _f13_clv(close, high, low):
    rng = (high - low).replace(0, np.nan)
    return ((close - low) - (high - close)) / rng


def _f13_ad_line(close, high, low, volume):
    mfv = _f13_clv(close, high, low) * volume
    return mfv.fillna(0.0).cumsum()


def _f13_cmf(close, high, low, volume, w):
    mfv = _f13_clv(close, high, low) * volume
    return _sum(mfv, w) / _sum(volume, w).replace(0, np.nan)


def _f13_typical(close, high, low):
    return (high + low + close) / 3.0


def _f13_mfi(close, high, low, volume, w):
    tp = _f13_typical(close, high, low)
    rmf = tp * volume
    up = rmf.where(tp.diff() > 0, 0.0)
    dn = rmf.where(tp.diff() < 0, 0.0)
    pmf = _sum(up, w)
    nmf = _sum(dn, w)
    ratio = pmf / nmf.replace(0, np.nan)
    return 100.0 - (100.0 / (1.0 + ratio))


def _f13_force(close, volume, w):
    raw = close.diff() * volume
    return raw.ewm(span=w, min_periods=max(1, w // 2)).mean()


def _f13_eom(high, low, volume, w):
    mid = (high + low) / 2.0
    dist = mid.diff()
    box = volume / (high - low).replace(0, np.nan)
    raw = dist / box.replace(0, np.nan)
    return _mean(raw, w)


def _f13_pvt(close, volume):
    return (close.pct_change() * volume).fillna(0.0).cumsum()


# ============================================================
# Each feature = SLOPE (1st math derivative / ROC) of a volume-price-confirmation base.
# ROC window scaled to the base window (short base -> short ROC; long base -> longer ROC).

# slope of OBV-slope(63d) over 21d
def f13vc_f13_volume_price_confirmation_obvslope_63d_slope_v001_signal(close, volume):
    obv = _f13_obv(close, volume)
    base = _slope(obv, 63) / _mean(volume, 63).replace(0, np.nan)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of OBV-slope(21d) over 5d
def f13vc_f13_volume_price_confirmation_obvslope_21d_slope_v002_signal(close, volume):
    obv = _f13_obv(close, volume)
    base = _slope(obv, 21) / _mean(volume, 21).replace(0, np.nan)
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of OBV-price 21d correlation over 5d
def f13vc_f13_volume_price_confirmation_obvcorr_21d_slope_v003_signal(closeadj, close, volume):
    obv = _f13_obv(close, volume)
    base = obv.rolling(21, min_periods=10).corr(closeadj)
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of OBV 63d-vs-21d momentum spread over 21d
def f13vc_f13_volume_price_confirmation_obvmomspr_63d_slope_v004_signal(close, volume):
    obv = _f13_obv(close, volume)
    long_m = (obv - obv.shift(63)) / _sum(volume, 63).replace(0, np.nan)
    short_m = (obv - obv.shift(21)) / _sum(volume, 21).replace(0, np.nan)
    base = long_m - short_m
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of OBV displacement(vs 63d EMA) over 21d
def f13vc_f13_volume_price_confirmation_obvdisp_63d_slope_v005_signal(close, volume):
    obv = _f13_obv(close, volume)
    ema = obv.ewm(span=63, min_periods=21).mean()
    base = (obv - ema) / _sum(volume, 63).replace(0, np.nan)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of z-scored OBV 21d-momentum over 21d
def f13vc_f13_volume_price_confirmation_obvmomz_126d_slope_v006_signal(close, volume):
    obv = _f13_obv(close, volume)
    mom = (obv - obv.shift(21)) / _sum(volume, 21).replace(0, np.nan)
    base = _z(mom, 126)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of OBV efficiency(63d) over 21d
def f13vc_f13_volume_price_confirmation_obveff_63d_slope_v007_signal(close, volume):
    obv = _f13_obv(close, volume)
    net = (obv - obv.shift(63)).abs()
    base = net / _sum(volume, 63).replace(0, np.nan)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of OBV oscillator(21d) over 5d
def f13vc_f13_volume_price_confirmation_obvosc_21d_slope_v008_signal(close, volume):
    obv = _f13_obv(close, volume)
    osc = obv - _mean(obv, 21)
    base = osc / _sum(volume, 21).replace(0, np.nan)
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of OBV drawdown(126d) over 21d
def f13vc_f13_volume_price_confirmation_obvdd_126d_slope_v009_signal(close, volume):
    obv = _f13_obv(close, volume)
    peak = obv.rolling(126, min_periods=63).max()
    base = (obv - peak) / _sum(volume, 126).replace(0, np.nan)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of OBV-lead-over-price(126d) over 21d
def f13vc_f13_volume_price_confirmation_obvlead_126d_slope_v010_signal(closeadj, close, volume):
    obv = _f13_obv(close, volume)
    obvsl = _slope(obv, 126) / _mean(volume, 126).replace(0, np.nan)
    pxsl = _slope(np.log(closeadj.replace(0, np.nan)), 126) * 100.0
    base = obvsl - pxsl
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of A/D-slope(63d) over 21d
def f13vc_f13_volume_price_confirmation_adslope_63d_slope_v011_signal(close, high, low, volume):
    ad = _f13_ad_line(close, high, low, volume)
    base = _slope(ad, 63) / _mean(volume, 63).replace(0, np.nan)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of A/D-price 63d correlation over 21d
def f13vc_f13_volume_price_confirmation_adcorr_63d_slope_v012_signal(closeadj, close, high, low, volume):
    ad = _f13_ad_line(close, high, low, volume)
    base = ad.rolling(63, min_periods=21).corr(closeadj)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of A/D displacement(vs 42d EMA) over 21d
def f13vc_f13_volume_price_confirmation_addisp_42d_slope_v013_signal(close, high, low, volume):
    ad = _f13_ad_line(close, high, low, volume)
    ema = ad.ewm(span=42, min_periods=21).mean()
    base = (ad - ema) / _sum(volume, 42).replace(0, np.nan)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of Chaikin oscillator over 5d
def f13vc_f13_volume_price_confirmation_chaikinosc_slope_v014_signal(close, high, low, volume):
    ad = _f13_ad_line(close, high, low, volume)
    osc = ad.ewm(span=3, min_periods=2).mean() - ad.ewm(span=10, min_periods=5).mean()
    base = osc / _mean(volume, 21).replace(0, np.nan)
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of A/D efficiency(63d) over 21d
def f13vc_f13_volume_price_confirmation_adeff_63d_slope_v015_signal(close, high, low, volume):
    mfv = _f13_clv(close, high, low) * volume
    net = _sum(mfv, 63).abs()
    gross = _sum(mfv.abs(), 63)
    base = net / gross.replace(0, np.nan)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of A/D drawdown(126d) over 21d
def f13vc_f13_volume_price_confirmation_addd_126d_slope_v016_signal(close, high, low, volume):
    ad = _f13_ad_line(close, high, low, volume)
    peak = ad.rolling(126, min_periods=63).max()
    base = (ad - peak) / _sum(volume, 126).replace(0, np.nan)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of A/D-line efficiency (net travel / gross |MFV|, 126d) over 21d
def f13vc_f13_volume_price_confirmation_adslopera_63d_slope_v017_signal(close, high, low, volume):
    mfv = _f13_clv(close, high, low) * volume
    net = _sum(mfv, 126).abs()
    gross = _sum(mfv.abs(), 126)
    base = net / gross.replace(0, np.nan)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CMF(21d) over 5d
def f13vc_f13_volume_price_confirmation_cmf_21d_slope_v018_signal(close, high, low, volume):
    base = _f13_cmf(close, high, low, volume, 21)
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CMF(63d) over 21d
def f13vc_f13_volume_price_confirmation_cmf_63d_slope_v019_signal(close, high, low, volume):
    base = _f13_cmf(close, high, low, volume, 63)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CMF(126d) over 21d
def f13vc_f13_volume_price_confirmation_cmf_126d_slope_v020_signal(close, high, low, volume):
    base = _f13_cmf(close, high, low, volume, 126)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CMF 21v63 spread over 5d
def f13vc_f13_volume_price_confirmation_cmfspr_21v63_slope_v021_signal(close, high, low, volume):
    s = _f13_cmf(close, high, low, volume, 21)
    l = _f13_cmf(close, high, low, volume, 63)
    base = s - l
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CMF21 z-scored(252d) over 21d
def f13vc_f13_volume_price_confirmation_cmfz_252d_slope_v022_signal(close, high, low, volume):
    c = _f13_cmf(close, high, low, volume, 21)
    base = _z(c, 252)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CMF amplitude(63d) over 21d
def f13vc_f13_volume_price_confirmation_cmfamp_63d_slope_v023_signal(close, high, low, volume):
    c = _f13_cmf(close, high, low, volume, 21)
    hi = c.rolling(63, min_periods=21).max()
    lo = c.rolling(63, min_periods=21).min()
    base = hi - lo
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CMF-price confirmation(63d) over 21d
def f13vc_f13_volume_price_confirmation_cmfpxconf_63d_slope_v024_signal(closeadj, close, high, low, volume):
    c = _f13_cmf(close, high, low, volume, 63)
    pxm = np.sign(closeadj / closeadj.shift(63) - 1.0)
    base = c * pxm
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CMF21 std(63d) over 21d
def f13vc_f13_volume_price_confirmation_cmfstd_63d_slope_v025_signal(close, high, low, volume):
    c = _f13_cmf(close, high, low, volume, 21)
    base = _std(c, 63)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of MFI(14d) centered over 5d
def f13vc_f13_volume_price_confirmation_mfi_14d_slope_v026_signal(close, high, low, volume):
    base = _f13_mfi(close, high, low, volume, 14) - 50.0
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of MFI(21d) centered over 5d
def f13vc_f13_volume_price_confirmation_mfi_21d_slope_v027_signal(close, high, low, volume):
    base = _f13_mfi(close, high, low, volume, 21) - 50.0
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of MFI(63d) centered over 21d
def f13vc_f13_volume_price_confirmation_mfi_63d_slope_v028_signal(close, high, low, volume):
    base = _f13_mfi(close, high, low, volume, 63) - 50.0
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of MFI-minus-CMF (two money-flow gauges, 14d) over 5d
def f13vc_f13_volume_price_confirmation_mfispr_14v63_slope_v029_signal(close, high, low, volume):
    m = (_f13_mfi(close, high, low, volume, 14) - 50.0) / 50.0
    c = _f13_cmf(close, high, low, volume, 14)
    base = m - c
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of MFI21 rank(252d) over 21d
def f13vc_f13_volume_price_confirmation_mfirank_252d_slope_v030_signal(close, high, low, volume):
    m = _f13_mfi(close, high, low, volume, 21)
    base = m.rolling(252, min_periods=126).rank(pct=True) - 0.5
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of MFI dispersion(63d) over 21d
def f13vc_f13_volume_price_confirmation_mfidisp_63d_slope_v031_signal(close, high, low, volume):
    m = _f13_mfi(close, high, low, volume, 14)
    base = _std(m, 63)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of MFI overbought-pressure(63d) over 21d
def f13vc_f13_volume_price_confirmation_mfiob_63d_slope_v032_signal(close, high, low, volume):
    m = _f13_mfi(close, high, low, volume, 14)
    base = _mean((m - 50.0).clip(lower=0), 63)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of MFI smoothing displacement over 5d
def f13vc_f13_volume_price_confirmation_mfidisp14_slope_v033_signal(close, high, low, volume):
    m = _f13_mfi(close, high, low, volume, 14)
    base = m - m.ewm(span=21, min_periods=10).mean()
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of force index(13d normalized) over 5d
def f13vc_f13_volume_price_confirmation_force_13d_slope_v034_signal(close, volume):
    f = _f13_force(close, volume, 13)
    base = f / (_mean(volume, 63) * _mean(close.abs(), 63)).replace(0, np.nan)
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of force-index sign-confirmation with price (13d) over 5d
def f13vc_f13_volume_price_confirmation_forcets_slope_v035_signal(closeadj, close, volume):
    nrm = (_mean(volume, 63) * _mean(close.abs(), 63)).replace(0, np.nan)
    fn = _f13_force(close, volume, 13) / nrm
    pxm = np.sign(closeadj / closeadj.shift(13) - 1.0)
    base = fn * pxm
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of force sign-persistence(63d) over 21d
def f13vc_f13_volume_price_confirmation_forcepersist_63d_slope_v036_signal(close, volume):
    f = _f13_force(close, volume, 13)
    base = np.sign(f).rolling(63, min_periods=21).mean()
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of force z-score(126d) over 21d
def f13vc_f13_volume_price_confirmation_forcez_126d_slope_v037_signal(close, volume):
    f = _f13_force(close, volume, 13)
    base = _z(f, 126)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of force asymmetry(63d) over 21d
def f13vc_f13_volume_price_confirmation_forceasym_63d_slope_v038_signal(close, volume):
    raw = close.diff() * volume
    nrm = (_mean(volume, 63) * _mean(close.abs(), 63)).replace(0, np.nan)
    rn = raw / nrm
    pos = _mean(rn.clip(lower=0), 63)
    neg = _mean((-rn).clip(lower=0), 63)
    base = (pos - neg) / (pos + neg).replace(0, np.nan)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of force efficiency(63d) over 21d
def f13vc_f13_volume_price_confirmation_forceeff_63d_slope_v039_signal(close, volume):
    raw = close.diff() * volume
    net = _sum(raw, 63).abs()
    gross = _sum(raw.abs(), 63)
    base = net / gross.replace(0, np.nan)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EOM(14d) over 5d
def f13vc_f13_volume_price_confirmation_eom_14d_slope_v040_signal(high, low, volume):
    base = _f13_eom(high, low, volume, 14) * 1e6
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EOM(21d) over 5d
def f13vc_f13_volume_price_confirmation_eom_21d_slope_v041_signal(high, low, volume):
    base = _f13_eom(high, low, volume, 21) * 1e6
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EOM z-score(126d) over 21d
def f13vc_f13_volume_price_confirmation_eomz_126d_slope_v042_signal(high, low, volume):
    e = _f13_eom(high, low, volume, 14)
    base = _z(e, 126)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EOM sign-persistence(63d) over 21d
def f13vc_f13_volume_price_confirmation_eompersist_63d_slope_v043_signal(high, low, volume):
    e = _f13_eom(high, low, volume, 14)
    base = np.sign(e).rolling(63, min_periods=21).mean()
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EOM dispersion(63d) over 21d
def f13vc_f13_volume_price_confirmation_eomdisp_63d_slope_v044_signal(high, low, volume):
    e = _f13_eom(high, low, volume, 14) * 1e6
    base = _std(e, 63)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of price-volume correlation(21d) over 5d
def f13vc_f13_volume_price_confirmation_pvcorr_21d_slope_v045_signal(closeadj, volume):
    pc = closeadj.pct_change()
    vc = volume.pct_change()
    base = pc.rolling(21, min_periods=10).corr(vc)
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of price-volume correlation(63d) over 21d
def f13vc_f13_volume_price_confirmation_pvcorr_63d_slope_v046_signal(closeadj, volume):
    pc = closeadj.pct_change()
    vc = volume.pct_change()
    base = pc.rolling(63, min_periods=21).corr(vc)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of up/down volume balance(21d) over 5d
def f13vc_f13_volume_price_confirmation_updnvol_21d_slope_v047_signal(closeadj, volume):
    up = volume.where(closeadj.diff() > 0, 0.0)
    dn = volume.where(closeadj.diff() < 0, 0.0)
    base = (_sum(up, 21) - _sum(dn, 21)) / _sum(volume, 21).replace(0, np.nan)
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of up/down volume balance(63d) over 21d
def f13vc_f13_volume_price_confirmation_updnvol_63d_slope_v048_signal(closeadj, volume):
    up = volume.where(closeadj.diff() > 0, 0.0)
    dn = volume.where(closeadj.diff() < 0, 0.0)
    base = (_sum(up, 63) - _sum(dn, 63)) / _sum(volume, 63).replace(0, np.nan)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of volume-weighted return(21d) over 5d
def f13vc_f13_volume_price_confirmation_vwret_21d_slope_v049_signal(closeadj, volume):
    ret = closeadj.pct_change()
    base = (ret * volume).rolling(21, min_periods=10).sum() / _sum(volume, 21).replace(0, np.nan)
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of PVT-slope(63d) over 21d
def f13vc_f13_volume_price_confirmation_pvtslope_63d_slope_v050_signal(closeadj, volume):
    pvt = _f13_pvt(closeadj, volume)
    base = _slope(pvt, 63) / _mean(volume, 63).replace(0, np.nan)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of PVT-price correlation(63d) over 21d
def f13vc_f13_volume_price_confirmation_pvtcorr_63d_slope_v051_signal(closeadj, volume):
    pvt = _f13_pvt(closeadj, volume)
    base = pvt.rolling(63, min_periods=21).corr(closeadj)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of PVT displacement(42d) over 21d
def f13vc_f13_volume_price_confirmation_pvtdisp_42d_slope_v052_signal(closeadj, volume):
    pvt = _f13_pvt(closeadj, volume)
    ema = pvt.ewm(span=42, min_periods=21).mean()
    base = (pvt - ema) / _sum(volume, 42).replace(0, np.nan)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of OBV-to-price level rolling correlation (accumulation tracking price, 63d) over 21d
def f13vc_f13_volume_price_confirmation_dvobvslope_63d_slope_v053_signal(closeadj, close, volume):
    obv = _f13_obv(close, volume)
    base = obv.rolling(63, min_periods=21).corr(np.log(closeadj.replace(0, np.nan)))
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-CMF percentile-rank vs 252d (value-weighted money-flow extremity) over 21d
def f13vc_f13_volume_price_confirmation_dvcmf_63d_slope_v054_signal(closeadj, close, high, low, volume):
    clv = _f13_clv(close, high, low)
    dv = closeadj * volume
    dvcmf = _sum(clv * dv, 63) / _sum(dv, 63).replace(0, np.nan)
    base = dvcmf.rolling(252, min_periods=126).rank(pct=True) - 0.5
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of NVI proxy(21d) over 5d
def f13vc_f13_volume_price_confirmation_nvi_21d_slope_v055_signal(closeadj, volume):
    quiet = (volume < volume.shift(1)).astype(float)
    contrib = closeadj.pct_change() * quiet
    base = _sum(contrib, 21)
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of PVI proxy(21d) over 5d
def f13vc_f13_volume_price_confirmation_pvi_21d_slope_v056_signal(closeadj, volume):
    loud = (volume > volume.shift(1)).astype(float)
    contrib = closeadj.pct_change() * loud
    base = _sum(contrib, 21)
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of PVI-NVI spread(63d) over 21d
def f13vc_f13_volume_price_confirmation_pvinvispr_63d_slope_v057_signal(closeadj, volume):
    loud = (volume > volume.shift(1)).astype(float)
    quiet = 1.0 - loud
    ret = closeadj.pct_change()
    base = _sum(ret * loud, 63) - _sum(ret * quiet, 63)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of volume concentration on the 5 largest up-days vs down-days (63d) over 21d
def f13vc_f13_volume_price_confirmation_upvolshare_63d_slope_v058_signal(closeadj, volume):
    ret = closeadj.pct_change()
    rank = ret.rolling(63, min_periods=21).rank(pct=True)
    top = (rank > 0.92).astype(float)
    bot = (rank < 0.08).astype(float)
    base = (_sum(top * volume, 63) - _sum(bot * volume, 63)) / _sum(volume, 63).replace(0, np.nan)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of volume thrust(21d) over 5d
def f13vc_f13_volume_price_confirmation_volthrust_21d_slope_v059_signal(closeadj, volume):
    relv = volume / _mean(volume, 63).replace(0, np.nan)
    up = relv.where(closeadj.diff() > 0)
    dn = relv.where(closeadj.diff() < 0)
    base = _mean(up, 21) - _mean(dn, 21)
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of stealth accumulation(63d) over 21d
def f13vc_f13_volume_price_confirmation_stealth_63d_slope_v060_signal(close, high, low, volume):
    clv = _f13_clv(close, high, low)
    quiet = (volume < _mean(volume, 63)).astype(float)
    base = _sum(clv * quiet, 63) / _sum(quiet, 63).replace(0, np.nan)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of stealth-minus-loud spread(63d) over 21d
def f13vc_f13_volume_price_confirmation_stealthspr_63d_slope_v061_signal(close, high, low, volume):
    clv = _f13_clv(close, high, low)
    quiet = (volume < _mean(volume, 63)).astype(float)
    loud = (volume >= _mean(volume, 63)).astype(float)
    qa = _sum(clv * quiet, 63) / _sum(quiet, 63).replace(0, np.nan)
    la = _sum(clv * loud, 63) / _sum(loud, 63).replace(0, np.nan)
    base = qa - la
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net accumulation-distribution(63d) over 21d
def f13vc_f13_volume_price_confirmation_netaccdist_63d_slope_v062_signal(closeadj, close, high, low, volume):
    relv = volume / _mean(volume, 63).replace(0, np.nan)
    clv = _f13_clv(close, high, low)
    acc = ((closeadj.diff() > 0) & (relv > 1.0) & (clv > 0)).astype(float) * relv
    dist = ((closeadj.diff() < 0) & (relv > 1.0) & (clv < 0)).astype(float) * relv
    base = (_sum(acc, 63) - _sum(dist, 63)) / 63.0
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CLV decisiveness(63d) over 21d
def f13vc_f13_volume_price_confirmation_clvabs_63d_slope_v063_signal(close, high, low):
    clv = _f13_clv(close, high, low)
    base = _mean(clv.abs(), 63)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CLV skew(63d) over 21d
def f13vc_f13_volume_price_confirmation_clvskew_63d_slope_v064_signal(close, high, low):
    clv = _f13_clv(close, high, low)
    base = clv.rolling(63, min_periods=21).skew()
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of MFI-CMF disagreement (two money-flow gauges, 21d) over 5d
def f13vc_f13_volume_price_confirmation_cmfvolint_21d_slope_v065_signal(close, high, low, volume):
    c = _f13_cmf(close, high, low, volume, 21)
    m = (_f13_mfi(close, high, low, volume, 14) - 50.0) / 50.0
    base = c - m
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of MFI(21d) rank vs 126d history (relative money-flow extremity) over 5d
def f13vc_f13_volume_price_confirmation_mfratio_21d_slope_v066_signal(close, high, low, volume):
    m = _f13_mfi(close, high, low, volume, 21)
    base = m.rolling(126, min_periods=63).rank(pct=True) - 0.5
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CMF crossing/indecision(63d) over 21d
def f13vc_f13_volume_price_confirmation_cmfcross_63d_slope_v067_signal(close, high, low, volume):
    c = _f13_cmf(close, high, low, volume, 21)
    flip = (np.sign(c) != np.sign(c.shift(1))).astype(float)
    base = _mean(flip, 63) - _mean(c.abs(), 63)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of MFV breadth(63d) over 21d
def f13vc_f13_volume_price_confirmation_mfvbreadth_63d_slope_v068_signal(close, high, low):
    clv = _f13_clv(close, high, low)
    pos = _sum(clv.clip(lower=0), 63)
    neg = _sum((-clv).clip(lower=0), 63)
    base = (pos - neg) / (pos + neg).replace(0, np.nan)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of force-index dispersion (std of normalized raw force, 63d) over 21d
def f13vc_f13_volume_price_confirmation_force_21d_slope_v069_signal(close, volume):
    raw = close.diff() * volume
    nrm = (_mean(volume, 63) * _mean(close.abs(), 63)).replace(0, np.nan)
    base = _std(raw / nrm, 63)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-force drawdown(126d) over 21d
def f13vc_f13_volume_price_confirmation_dvforcedd_126d_slope_v070_signal(closeadj, volume):
    raw = closeadj.diff() * volume
    f = raw.ewm(span=21, min_periods=10).mean()
    fn = f / _mean(closeadj * volume, 126).replace(0, np.nan)
    peak = fn.rolling(126, min_periods=63).max()
    base = fn - peak
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of typical-price OBV slope(63d) over 21d
def f13vc_f13_volume_price_confirmation_tpobvslope_63d_slope_v071_signal(close, high, low, volume):
    tp = _f13_typical(close, high, low)
    direction = np.sign(tp.diff())
    tpobv = (direction * volume).fillna(0.0).cumsum()
    base = _slope(tpobv, 63) / _mean(volume, 63).replace(0, np.nan)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CMF reversal(63d) over 21d
def f13vc_f13_volume_price_confirmation_cmfreversal_63d_slope_v072_signal(close, high, low, volume):
    c = _f13_cmf(close, high, low, volume, 21)
    base = c - c.shift(63)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of volume-confirmed momentum quality(63d) over 21d
def f13vc_f13_volume_price_confirmation_momquality_63d_slope_v073_signal(closeadj, volume):
    ret = np.tanh((closeadj / closeadj.shift(63) - 1.0) * 3.0)
    voltrend = _slope(np.log(volume.replace(0, np.nan)), 63)
    voltrend_n = np.tanh(voltrend * 200.0)
    base = ret * (1.0 + voltrend_n) / 2.0
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of signed price impact(21d) over 5d
def f13vc_f13_volume_price_confirmation_signedimpact_21d_slope_v074_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = closeadj * volume
    impact = ret / dv.replace(0, np.nan)
    base = _mean(impact, 21) * 1e12
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of price elasticity(21d) over 5d
def f13vc_f13_volume_price_confirmation_priceelast_21d_slope_v075_signal(closeadj, volume):
    move = (closeadj / closeadj.shift(21) - 1.0).abs()
    relv = _mean(volume, 21) / _mean(volume, 252).replace(0, np.nan)
    base = move / relv.replace(0, np.nan)
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of weak-rally warning(21d) over 5d
def f13vc_f13_volume_price_confirmation_weakrally_21d_slope_v076_signal(closeadj, volume):
    px_up = (closeadj.diff() > 0).astype(float)
    vol_dn = (volume.diff() < 0).astype(float)
    weak = px_up * vol_dn * closeadj.pct_change().abs()
    base = _mean(weak, 21) * 100.0
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capitulation(21d) over 5d
def f13vc_f13_volume_price_confirmation_capit_21d_slope_v077_signal(closeadj, volume):
    px_dn = (closeadj.diff() < 0).astype(float)
    vol_up = (volume.diff() > 0).astype(float)
    relv = volume / _mean(volume, 63).replace(0, np.nan)
    cap = px_dn * vol_up * relv
    base = _mean(cap, 21)
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of OBV beta to price(63d) over 21d
def f13vc_f13_volume_price_confirmation_obvbeta_63d_slope_v078_signal(closeadj, close, volume):
    obv = _f13_obv(close, volume)
    cov = obv.rolling(63, min_periods=21).cov(np.log(closeadj.replace(0, np.nan)))
    var = np.log(closeadj.replace(0, np.nan)).rolling(63, min_periods=21).var()
    base = cov / var.replace(0, np.nan) / _mean(volume, 63).replace(0, np.nan)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of A/D beta to price(126d) over 21d
def f13vc_f13_volume_price_confirmation_adbeta_126d_slope_v079_signal(closeadj, close, high, low, volume):
    ad = _f13_ad_line(close, high, low, volume)
    cov = ad.rolling(126, min_periods=63).cov(np.log(closeadj.replace(0, np.nan)))
    var = np.log(closeadj.replace(0, np.nan)).rolling(126, min_periods=63).var()
    base = cov / var.replace(0, np.nan) / _mean(volume, 126).replace(0, np.nan)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of chaikin oscillator z-score(126d) over 21d
def f13vc_f13_volume_price_confirmation_chaikinoscz_126d_slope_v080_signal(close, high, low, volume):
    ad = _f13_ad_line(close, high, low, volume)
    osc = ad.ewm(span=3, min_periods=2).mean() - ad.ewm(span=10, min_periods=5).mean()
    oscn = osc / _mean(volume, 21).replace(0, np.nan)
    base = _z(oscn, 126)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CMF acceleration over 21d
def f13vc_f13_volume_price_confirmation_cmfaccel_slope_v081_signal(close, high, low, volume):
    c21 = _f13_cmf(close, high, low, volume, 21)
    c63 = _f13_cmf(close, high, low, volume, 63)
    base = (c21 - c21.shift(21)) - (c63 - c63.shift(21))
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of MFI-price divergence(21d) over 5d
def f13vc_f13_volume_price_confirmation_mfidiv_21d_slope_v082_signal(closeadj, close, high, low, volume):
    mfi = _f13_mfi(close, high, low, volume, 21) - 50.0
    pxm = np.sign(closeadj / closeadj.shift(21) - 1.0)
    base = mfi - pxm * mfi.abs()
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of MFI slope(63d) over 21d
def f13vc_f13_volume_price_confirmation_mfislope_63d_slope_v083_signal(close, high, low, volume):
    m = _f13_mfi(close, high, low, volume, 14)
    base = _slope(m, 63)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of force-index raw rank(252d) over 21d
def f13vc_f13_volume_price_confirmation_forceraw_252d_slope_v084_signal(close, volume):
    raw = close.diff() * volume
    nrm = (_mean(volume, 63) * _mean(close.abs(), 63)).replace(0, np.nan)
    base = (raw / nrm).rolling(252, min_periods=126).rank(pct=True) - 0.5
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EOM slope(63d) over 21d
def f13vc_f13_volume_price_confirmation_eomslope_63d_slope_v085_signal(high, low, volume):
    e = _f13_eom(high, low, volume, 14) * 1e6
    base = _slope(e, 63)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EOM rank(252d) over 21d
def f13vc_f13_volume_price_confirmation_eomrank_252d_slope_v086_signal(high, low, volume):
    e = _f13_eom(high, low, volume, 14)
    base = e.rolling(252, min_periods=126).rank(pct=True) - 0.5
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of price-volume rank correlation(63d) over 21d
def f13vc_f13_volume_price_confirmation_pvrankcorr_63d_slope_v087_signal(closeadj, volume):
    pr = closeadj.pct_change().rolling(63, min_periods=21).rank(pct=True)
    vr = volume.rolling(63, min_periods=21).rank(pct=True)
    base = pr.rolling(63, min_periods=21).corr(vr)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of volume-trend confirmation(63d) over 21d
def f13vc_f13_volume_price_confirmation_voltrendconf_63d_slope_v088_signal(closeadj, volume):
    pxdir = np.sign(closeadj / closeadj.shift(63) - 1.0)
    voltrend = _slope(np.log(volume.replace(0, np.nan)), 63)
    base = pxdir * voltrend
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of distribution days(21d) over 5d
def f13vc_f13_volume_price_confirmation_distdays_21d_slope_v089_signal(closeadj, close, high, low, volume):
    relv = volume / _mean(volume, 63).replace(0, np.nan)
    clv = _f13_clv(close, high, low)
    dist = ((closeadj.diff() < 0) & (relv > 1.2) & (clv < 0)).astype(float) * relv
    base = _sum(dist, 21)
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of accumulation days(21d) over 5d
def f13vc_f13_volume_price_confirmation_accdays_21d_slope_v090_signal(closeadj, close, high, low, volume):
    relv = volume / _mean(volume, 63).replace(0, np.nan)
    clv = _f13_clv(close, high, low)
    acc = ((closeadj.diff() > 0) & (relv > 1.2) & (clv > 0)).astype(float) * relv
    base = _sum(acc, 21)
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of MFI-OBV agreement(63d) over 21d
def f13vc_f13_volume_price_confirmation_mfiobvagree_63d_slope_v091_signal(close, high, low, volume):
    mfi = _f13_mfi(close, high, low, volume, 21) - 50.0
    obv = _f13_obv(close, volume)
    obvm = (obv - obv.shift(63))
    agree = np.sign(mfi) * np.sign(obvm) * mfi.abs()
    base = _mean(agree, 63)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of volume-acceleration force(21d) over 5d
def f13vc_f13_volume_price_confirmation_volaccel_21d_slope_v092_signal(close, volume):
    accel = close.diff().diff()
    raw = accel * volume
    f = raw.ewm(span=21, min_periods=10).mean()
    base = f / (_mean(volume, 63) * _mean(close.abs(), 63)).replace(0, np.nan)
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CMF rising drift(126d) over 21d
def f13vc_f13_volume_price_confirmation_cmfrising_126d_slope_v093_signal(close, high, low, volume):
    c = _f13_cmf(close, high, low, volume, 63)
    up = _sum(c.diff().clip(lower=0), 126)
    dn = _sum((-c.diff()).clip(lower=0), 126)
    base = (up - dn) / (up + dn).replace(0, np.nan)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of A/D oscillator divergence(63d) over 21d
def f13vc_f13_volume_price_confirmation_adoscdiv_63d_slope_v094_signal(closeadj, close, high, low, volume):
    ad = _f13_ad_line(close, high, low, volume)
    osc = ad.ewm(span=3, min_periods=2).mean() - ad.ewm(span=10, min_periods=5).mean()
    oscn = osc / _mean(volume, 21).replace(0, np.nan)
    pxm = np.sign(closeadj / closeadj.shift(63) - 1.0)
    base = oscn - pxm * oscn.abs()
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EOM-force composite(21d) over 5d
def f13vc_f13_volume_price_confirmation_eomforce_21d_slope_v095_signal(close, high, low, volume):
    e = _f13_eom(high, low, volume, 14) * 1e6
    f = _f13_force(close, volume, 13)
    fn = f / (_mean(volume, 63) * _mean(close.abs(), 63)).replace(0, np.nan)
    base = np.sign(e) * np.sign(fn) * (e.abs() ** 0.5)
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of OBV-PVT divergence(63d) over 21d
def f13vc_f13_volume_price_confirmation_obvpvtdiv_63d_slope_v096_signal(closeadj, close, volume):
    obv = _f13_obv(close, volume)
    pvt = _f13_pvt(closeadj, volume)
    obvn = (obv - obv.shift(63)) / _sum(volume, 63).replace(0, np.nan)
    pvtn = (pvt - pvt.shift(63)) / _sum(volume, 63).replace(0, np.nan)
    base = obvn - pvtn * 50.0
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of money-flow vs OBV spread(63d) over 21d
def f13vc_f13_volume_price_confirmation_mfobvspr_63d_slope_v097_signal(close, high, low, volume):
    cmf = _f13_cmf(close, high, low, volume, 63)
    obv = _f13_obv(close, volume)
    obvn = (obv - obv.shift(63)) / _sum(volume, 63).replace(0, np.nan)
    base = cmf - obvn
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of breakout-volume confirmation(21d) over 5d
def f13vc_f13_volume_price_confirmation_breakvol_21d_slope_v098_signal(closeadj, volume):
    hi = closeadj.shift(1).rolling(21, min_periods=10).max()
    brk = (closeadj / hi.replace(0, np.nan) - 1.0).clip(lower=0)
    relv = volume / _mean(volume, 63).replace(0, np.nan)
    base = _mean(brk * relv, 21) * 100.0
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CLV-weighted return(21d) over 5d
def f13vc_f13_volume_price_confirmation_clvret_21d_slope_v099_signal(closeadj, close, high, low):
    clv = _f13_clv(close, high, low)
    base = _mean(clv * closeadj.pct_change(), 21) * 100.0
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of volume concentration on big-move days(63d) over 21d
def f13vc_f13_volume_price_confirmation_volconc_63d_slope_v100_signal(closeadj, volume):
    absret = closeadj.pct_change().abs()
    rank = absret.rolling(63, min_periods=21).rank(pct=True)
    big = (rank > 0.92).astype(float)
    base = _sum(big * volume, 63) / _sum(volume, 63).replace(0, np.nan)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of NVI proxy(63d) over 21d
def f13vc_f13_volume_price_confirmation_nvi_63d_slope_v101_signal(closeadj, volume):
    quiet = (volume < volume.shift(1)).astype(float)
    contrib = closeadj.pct_change() * quiet
    base = _sum(contrib, 63)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of PVI proxy(63d) over 21d
def f13vc_f13_volume_price_confirmation_pvi_63d_slope_v102_signal(closeadj, volume):
    loud = (volume > volume.shift(1)).astype(float)
    contrib = closeadj.pct_change() * loud
    base = _sum(contrib, 63)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of volume thrust(63d) over 21d
def f13vc_f13_volume_price_confirmation_volthrust_63d_slope_v103_signal(closeadj, volume):
    relv = volume / _mean(volume, 126).replace(0, np.nan)
    up = relv.where(closeadj.diff() > 0)
    dn = relv.where(closeadj.diff() < 0)
    base = _mean(up, 63) - _mean(dn, 63)
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of loud distribution(63d) over 21d
def f13vc_f13_volume_price_confirmation_loud_63d_slope_v104_signal(close, high, low, volume):
    clv = _f13_clv(close, high, low)
    loud = (volume > _mean(volume, 63)).astype(float)
    base = -_sum(clv * loud, 63) / _sum(loud, 63).replace(0, np.nan)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CMF-momentum-price confirmation(21d) over 5d
def f13vc_f13_volume_price_confirmation_cmfmompx_21d_slope_v105_signal(closeadj, close, high, low, volume):
    c = _f13_cmf(close, high, low, volume, 21)
    cmom = c - c.shift(21)
    pxm = np.sign(closeadj / closeadj.shift(21) - 1.0)
    base = cmom * pxm
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of OBV new-high rate(63d) over 21d
def f13vc_f13_volume_price_confirmation_obvnewhi_63d_slope_v106_signal(close, volume):
    obv = _f13_obv(close, volume)
    roll_hi = obv.rolling(126, min_periods=63).max()
    is_hi = (obv >= roll_hi - 1e-9).astype(float)
    freq = _mean(is_hi, 63)
    depth = (obv - obv.rolling(126, min_periods=63).min()) / _sum(volume, 126).replace(0, np.nan)
    base = freq + 0.1 * depth
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of chaikin oscillator momentum(21d) over 5d
def f13vc_f13_volume_price_confirmation_chaikmom_21d_slope_v107_signal(close, high, low, volume):
    ad = _f13_ad_line(close, high, low, volume)
    osc = ad.ewm(span=3, min_periods=2).mean() - ad.ewm(span=10, min_periods=5).mean()
    oscn = osc / _mean(volume, 21).replace(0, np.nan)
    base = oscn - oscn.shift(21)
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CMF stability(126d) over 21d
def f13vc_f13_volume_price_confirmation_cmfstab_126d_slope_v108_signal(close, high, low, volume):
    c = _f13_cmf(close, high, low, volume, 21)
    sw = c.rolling(126, min_periods=63).max() - c.rolling(126, min_periods=63).min()
    lvl = _mean(c, 126).abs()
    base = lvl / sw.replace(0, np.nan)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of effort-result divergence(63d) over 21d
def f13vc_f13_volume_price_confirmation_effdiv_63d_slope_v109_signal(closeadj, volume):
    up = volume.where(closeadj.diff() > 0, 0.0)
    dn = volume.where(closeadj.diff() < 0, 0.0)
    bal = (_sum(up, 63) - _sum(dn, 63)) / _sum(volume, 63).replace(0, np.nan)
    pxret = np.tanh((closeadj / closeadj.shift(63) - 1.0) * 5.0)
    base = bal - pxret
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of up/down volume momentum(21d) over 5d
def f13vc_f13_volume_price_confirmation_updnmom_21d_slope_v110_signal(closeadj, volume):
    up = volume.where(closeadj.diff() > 0, 0.0)
    dn = volume.where(closeadj.diff() < 0, 0.0)
    bal = (_sum(up, 21) - _sum(dn, 21)) / _sum(volume, 21).replace(0, np.nan)
    base = bal - bal.shift(21)
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CMF persistence(63d) over 21d
def f13vc_f13_volume_price_confirmation_cmfpersist_63d_slope_v111_signal(close, high, low, volume):
    c = _f13_cmf(close, high, low, volume, 21)
    base = (c > 0).astype(float).rolling(63, min_periods=21).mean() - 0.5
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CMF rank(252d) over 21d
def f13vc_f13_volume_price_confirmation_cmfrank_252d_slope_v112_signal(close, high, low, volume):
    c = _f13_cmf(close, high, low, volume, 21)
    base = c.rolling(252, min_periods=126).rank(pct=True) - 0.5
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of MFI oversold pressure(63d) over 21d
def f13vc_f13_volume_price_confirmation_mfios_63d_slope_v113_signal(close, high, low, volume):
    m = _f13_mfi(close, high, low, volume, 14)
    base = _mean((50.0 - m).clip(lower=0), 63)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of MFI momentum(14d) over 5d
def f13vc_f13_volume_price_confirmation_mfimom_14d_slope_v114_signal(close, high, low, volume):
    m = _f13_mfi(close, high, low, volume, 14)
    base = m - m.shift(21)
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of MFI(21d) acceleration (21d momentum minus prior) over 21d
def f13vc_f13_volume_price_confirmation_mfiz_252d_slope_v115_signal(close, high, low, volume):
    m = _f13_mfi(close, high, low, volume, 21)
    mom = m - m.shift(21)
    base = mom - mom.shift(21)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of force momentum(13d) over 5d
def f13vc_f13_volume_price_confirmation_forcemom_13d_slope_v116_signal(close, volume):
    f = _f13_force(close, volume, 13)
    nrm = (_mean(volume, 63) * _mean(close.abs(), 63)).replace(0, np.nan)
    fn = f / nrm
    base = fn - fn.shift(21)
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of force z-score(126d, 21d-force) over 21d
def f13vc_f13_volume_price_confirmation_forcez21_126d_slope_v117_signal(close, volume):
    nrm = (_mean(volume, 63) * _mean(close.abs(), 63)).replace(0, np.nan)
    f = _f13_force(close, volume, 21) / nrm
    base = _z(f, 126)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EOM momentum(21d) over 5d
def f13vc_f13_volume_price_confirmation_eommom_21d_slope_v118_signal(high, low, volume):
    e = _f13_eom(high, low, volume, 21) * 1e6
    base = e - e.shift(21)
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of OBV efficiency-momentum risk-adjusted(126d) over 21d
def f13vc_f13_volume_price_confirmation_obvmomra_126d_slope_v119_signal(close, volume):
    obv = _f13_obv(close, volume)
    chg = obv - obv.shift(126)
    vol = _std(obv.diff(), 126) * np.sqrt(126.0)
    base = chg / vol.replace(0, np.nan)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of A/D-line slope acceleration(63d) over 21d
def f13vc_f13_volume_price_confirmation_adslopechg_63d_slope_v120_signal(close, high, low, volume):
    ad = _f13_ad_line(close, high, low, volume)
    sl = _slope(ad, 63) / _mean(volume, 63).replace(0, np.nan)
    base = sl - sl.shift(21)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of chaikin persistence(63d) over 21d
def f13vc_f13_volume_price_confirmation_chaikpersist_63d_slope_v121_signal(close, high, low, volume):
    ad = _f13_ad_line(close, high, low, volume)
    osc = ad.ewm(span=3, min_periods=2).mean() - ad.ewm(span=10, min_periods=5).mean()
    base = np.sign(osc).rolling(63, min_periods=21).mean()
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of money-flow trend(126d) over 21d
def f13vc_f13_volume_price_confirmation_cmftrend_126d_slope_v122_signal(close, high, low, volume):
    c = _f13_cmf(close, high, low, volume, 63)
    base = _slope(c, 126)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CLV lag-1 autocorrelation (intrabar-strength persistence, 63d) over 21d
def f13vc_f13_volume_price_confirmation_clvmean_63d_slope_v123_signal(close, high, low):
    clv = _f13_clv(close, high, low)
    base = clv.rolling(63, min_periods=32).apply(
        lambda a: pd.Series(a).autocorr(lag=1) if np.std(a) > 0 else np.nan, raw=True)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of relative-volume distribution skew (participation asymmetry, 21d) over 5d
def f13vc_f13_volume_price_confirmation_relvolasym_21d_slope_v124_signal(volume):
    relv = volume / _mean(volume, 63).replace(0, np.nan)
    base = relv.rolling(21, min_periods=12).skew()
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of MFI(63d)-vs-price divergence over 21d
def f13vc_f13_volume_price_confirmation_mfratio_63d_slope_v125_signal(closeadj, close, high, low, volume):
    m = _f13_mfi(close, high, low, volume, 63) - 50.0
    pxm = np.sign(closeadj / closeadj.shift(63) - 1.0)
    base = m - pxm * m.abs()
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of OBV oscillator (OBV minus 42d mean, 21d) over 5d
def f13vc_f13_volume_price_confirmation_obvmomn_21d_slope_v126_signal(close, volume):
    obv = _f13_obv(close, volume)
    base = (obv - _mean(obv, 42)) / _sum(volume, 42).replace(0, np.nan)
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of A/D-vs-price divergence(63d) over 21d
def f13vc_f13_volume_price_confirmation_admomn_63d_slope_v127_signal(closeadj, close, high, low, volume):
    ad = _f13_ad_line(close, high, low, volume)
    adn = (ad - ad.shift(63)) / _sum(volume, 63).replace(0, np.nan)
    pxm = np.sign(closeadj / closeadj.shift(63) - 1.0)
    base = adn - pxm * adn.abs()
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CMF63 displacement from its 126d EMA (de-meaned pressure) over 21d
def f13vc_f13_volume_price_confirmation_cmfregime_slope_v128_signal(close, high, low, volume):
    c = _f13_cmf(close, high, low, volume, 63)
    base = c - c.ewm(span=126, min_periods=42).mean()
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of force cumulative-efficiency vs longer base (63d eff) over 21d, alt window
def f13vc_f13_volume_price_confirmation_forceeff126_slope_v129_signal(close, volume):
    raw = close.diff() * volume
    net = _sum(raw, 126).abs()
    gross = _sum(raw.abs(), 126)
    base = net / gross.replace(0, np.nan)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume CLV price-tilt(63d) over 21d
def f13vc_f13_volume_price_confirmation_dvclvtilt_63d_slope_v130_signal(closeadj, close, high, low, volume):
    clv = _f13_clv(close, high, low)
    dv = closeadj * volume
    dollar_w = _sum(clv * dv, 63) / _sum(dv, 63).replace(0, np.nan)
    vol_w = _sum(clv * volume, 63) / _sum(volume, 63).replace(0, np.nan)
    base = (dollar_w - vol_w) * 100.0
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of MFI(14) over 21d (longer-horizon money-flow drift)
def f13vc_f13_volume_price_confirmation_mfi14_21d_slope_v131_signal(close, high, low, volume):
    base = _f13_mfi(close, high, low, volume, 14) - 50.0
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of OBV-price 21d rolling beta (volume sensitivity to price) over 5d
def f13vc_f13_volume_price_confirmation_obvslopepv_21d_slope_v132_signal(closeadj, close, volume):
    obv = _f13_obv(close, volume)
    lp = np.log(closeadj.replace(0, np.nan))
    cov = obv.rolling(21, min_periods=10).cov(lp)
    var = lp.rolling(21, min_periods=10).var()
    base = cov / var.replace(0, np.nan) / _mean(volume, 21).replace(0, np.nan)
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of money-flow conviction (mean / dispersion of CMF21, 63d) over 21d
def f13vc_f13_volume_price_confirmation_accconv_63d_slope_v133_signal(close, high, low, volume):
    c = _f13_cmf(close, high, low, volume, 21)
    base = _mean(c, 63) / _std(c, 63).replace(0, np.nan)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of volume-weighted CLV concentration gap(21d) over 5d
def f13vc_f13_volume_price_confirmation_wclvgap_21d_slope_v134_signal(close, high, low, volume):
    clv = _f13_clv(close, high, low)
    vw = _sum(clv * volume, 21) / _sum(volume, 21).replace(0, np.nan)
    ew = _mean(clv, 21)
    base = vw - ew
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CMF-vs-MFI confirmation composite (both gauges agree, 21d) over 5d
def f13vc_f13_volume_price_confirmation_dvcmfdt_63d_slope_v135_signal(close, high, low, volume):
    c = _f13_cmf(close, high, low, volume, 21)
    m = (_f13_mfi(close, high, low, volume, 14) - 50.0) / 50.0
    base = np.sign(c) * np.sign(m) * (c.abs() + m.abs())
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of force sign-weighted return confirmation(21d) over 5d
def f13vc_f13_volume_price_confirmation_forceconf_21d_slope_v136_signal(closeadj, close, volume):
    f = _f13_force(close, volume, 13)
    fn = f / (_mean(volume, 63) * _mean(close.abs(), 63)).replace(0, np.nan)
    pxm = np.sign(closeadj / closeadj.shift(21) - 1.0)
    base = fn * pxm
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of money-flow breadth weighted by volume(63d) over 21d
def f13vc_f13_volume_price_confirmation_mfbreadthv_63d_slope_v137_signal(close, high, low, volume):
    clv = _f13_clv(close, high, low)
    pos = (clv > 0).astype(float) * volume
    base = _sum(pos, 63) / _sum(volume, 63).replace(0, np.nan) - 0.5
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of distribution-warning intensity(21d) over 5d
def f13vc_f13_volume_price_confirmation_distwarn_21d_slope_v138_signal(closeadj, volume):
    relv = volume / _mean(volume, 63).replace(0, np.nan)
    heavy_dn = ((closeadj.diff() < 0) & (relv > 1.0)).astype(float) * relv
    base = _sum(heavy_dn, 21) / 21.0
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of OBV-vs-price agreement(63d) over 21d
def f13vc_f13_volume_price_confirmation_obvpxagree_63d_slope_v139_signal(closeadj, close, volume):
    obv = _f13_obv(close, volume)
    obvsl = _slope(obv, 63) / _mean(volume, 63).replace(0, np.nan)
    pxsl = _slope(np.log(closeadj.replace(0, np.nan)), 63)
    base = np.tanh(obvsl) * np.sign(pxsl)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EOM-return confirmation(21d) over 5d
def f13vc_f13_volume_price_confirmation_eomret_21d_slope_v140_signal(closeadj, high, low, volume):
    e = _f13_eom(high, low, volume, 14)
    ret = closeadj / closeadj.shift(21) - 1.0
    base = np.sign(e) * (e.abs() ** 0.5) * 1e3 * np.sign(ret)
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of volume-price elasticity dispersion(63d) over 21d
def f13vc_f13_volume_price_confirmation_vpelastdisp_63d_slope_v141_signal(closeadj, volume):
    relv = volume / _mean(volume, 63).replace(0, np.nan)
    impact = closeadj.pct_change().abs() / relv.replace(0, np.nan)
    base = _std(impact, 63)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of A/D acceleration over 21d
def f13vc_f13_volume_price_confirmation_adaccel_slope_v142_signal(close, high, low, volume):
    ad = _f13_ad_line(close, high, low, volume)
    flow = (ad - ad.shift(21)) / _sum(volume, 21).replace(0, np.nan)
    base = flow - 2.0 * flow.shift(21) + flow.shift(42)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of money-flow vs OBV scale spread alt(126d) over 21d
def f13vc_f13_volume_price_confirmation_mfobvspr_126d_slope_v143_signal(close, high, low, volume):
    cmf = _f13_cmf(close, high, low, volume, 126)
    obv = _f13_obv(close, volume)
    obvn = (obv - obv.shift(126)) / _sum(volume, 126).replace(0, np.nan)
    base = cmf - obvn
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of trend efficiency-ratio weighted by volume confirmation (21d) over 5d
def f13vc_f13_volume_price_confirmation_effortres_21d_slope_v144_signal(closeadj, volume):
    net = (closeadj - closeadj.shift(21)).abs()
    path = closeadj.diff().abs().rolling(21, min_periods=10).sum()
    er = net / path.replace(0, np.nan)
    relv = _mean(volume, 21) / _mean(volume, 252).replace(0, np.nan)
    base = er * relv
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CMF21-vs-CMF126 ratio (short/long money-flow alignment, 63d) over 21d
def f13vc_f13_volume_price_confirmation_cmf21slope_63d_slope_v145_signal(close, high, low, volume):
    s = _f13_cmf(close, high, low, volume, 21)
    l = _f13_cmf(close, high, low, volume, 126)
    base = np.sign(s) * np.sign(l) * (s.abs() + l.abs())
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of OBV-EOM agreement (accumulation confirmed by ease-of-movement, 63d) over 21d
def f13vc_f13_volume_price_confirmation_dvobvmom_63d_slope_v146_signal(close, high, low, volume):
    obv = _f13_obv(close, volume)
    obvm = (obv - obv.shift(63)) / _sum(volume, 63).replace(0, np.nan)
    e = _f13_eom(high, low, volume, 21) * 1e6
    base = np.sign(obvm) * np.sign(e) * obvm.abs()
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of MFI smoothing displacement(14d) over 21d
def f13vc_f13_volume_price_confirmation_mfismdisp_21d_slope_v147_signal(close, high, low, volume):
    m = _f13_mfi(close, high, low, volume, 14)
    base = m - m.ewm(span=21, min_periods=10).mean()
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of accumulation-day net pressure(126d) over 21d
def f13vc_f13_volume_price_confirmation_netaccdist_126d_slope_v148_signal(closeadj, close, high, low, volume):
    relv = volume / _mean(volume, 126).replace(0, np.nan)
    clv = _f13_clv(close, high, low)
    acc = ((closeadj.diff() > 0) & (relv > 1.0) & (clv > 0)).astype(float) * relv
    dist = ((closeadj.diff() < 0) & (relv > 1.0) & (clv < 0)).astype(float) * relv
    base = (_sum(acc, 126) - _sum(dist, 126)) / 126.0
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CMF-volume balance composite(21d) over 5d
def f13vc_f13_volume_price_confirmation_cmfvolbal_21d_slope_v149_signal(close, high, low, volume):
    cmf = _f13_cmf(close, high, low, volume, 21)
    up = volume.where(close.diff() > 0, 0.0)
    dn = volume.where(close.diff() < 0, 0.0)
    bal = (_sum(up, 21) - _sum(dn, 21)) / _sum(volume, 21).replace(0, np.nan)
    base = cmf * np.sign(bal) * (bal.abs() ** 0.5)
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of typical-price OBV momentum normalized(126d) over 21d
def f13vc_f13_volume_price_confirmation_tpobvmom_126d_slope_v150_signal(close, high, low, volume):
    tp = _f13_typical(close, high, low)
    direction = np.sign(tp.diff())
    tpobv = (direction * volume).fillna(0.0).cumsum()
    base = (tpobv - tpobv.shift(126)) / _sum(volume, 126).replace(0, np.nan)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f13vc_f13_volume_price_confirmation_obvslope_63d_slope_v001_signal,
    f13vc_f13_volume_price_confirmation_obvslope_21d_slope_v002_signal,
    f13vc_f13_volume_price_confirmation_obvcorr_21d_slope_v003_signal,
    f13vc_f13_volume_price_confirmation_obvmomspr_63d_slope_v004_signal,
    f13vc_f13_volume_price_confirmation_obvdisp_63d_slope_v005_signal,
    f13vc_f13_volume_price_confirmation_obvmomz_126d_slope_v006_signal,
    f13vc_f13_volume_price_confirmation_obveff_63d_slope_v007_signal,
    f13vc_f13_volume_price_confirmation_obvosc_21d_slope_v008_signal,
    f13vc_f13_volume_price_confirmation_obvdd_126d_slope_v009_signal,
    f13vc_f13_volume_price_confirmation_obvlead_126d_slope_v010_signal,
    f13vc_f13_volume_price_confirmation_adslope_63d_slope_v011_signal,
    f13vc_f13_volume_price_confirmation_adcorr_63d_slope_v012_signal,
    f13vc_f13_volume_price_confirmation_addisp_42d_slope_v013_signal,
    f13vc_f13_volume_price_confirmation_chaikinosc_slope_v014_signal,
    f13vc_f13_volume_price_confirmation_adeff_63d_slope_v015_signal,
    f13vc_f13_volume_price_confirmation_addd_126d_slope_v016_signal,
    f13vc_f13_volume_price_confirmation_adslopera_63d_slope_v017_signal,
    f13vc_f13_volume_price_confirmation_cmf_21d_slope_v018_signal,
    f13vc_f13_volume_price_confirmation_cmf_63d_slope_v019_signal,
    f13vc_f13_volume_price_confirmation_cmf_126d_slope_v020_signal,
    f13vc_f13_volume_price_confirmation_cmfspr_21v63_slope_v021_signal,
    f13vc_f13_volume_price_confirmation_cmfz_252d_slope_v022_signal,
    f13vc_f13_volume_price_confirmation_cmfamp_63d_slope_v023_signal,
    f13vc_f13_volume_price_confirmation_cmfpxconf_63d_slope_v024_signal,
    f13vc_f13_volume_price_confirmation_cmfstd_63d_slope_v025_signal,
    f13vc_f13_volume_price_confirmation_mfi_14d_slope_v026_signal,
    f13vc_f13_volume_price_confirmation_mfi_21d_slope_v027_signal,
    f13vc_f13_volume_price_confirmation_mfi_63d_slope_v028_signal,
    f13vc_f13_volume_price_confirmation_mfispr_14v63_slope_v029_signal,
    f13vc_f13_volume_price_confirmation_mfirank_252d_slope_v030_signal,
    f13vc_f13_volume_price_confirmation_mfidisp_63d_slope_v031_signal,
    f13vc_f13_volume_price_confirmation_mfiob_63d_slope_v032_signal,
    f13vc_f13_volume_price_confirmation_mfidisp14_slope_v033_signal,
    f13vc_f13_volume_price_confirmation_force_13d_slope_v034_signal,
    f13vc_f13_volume_price_confirmation_forcets_slope_v035_signal,
    f13vc_f13_volume_price_confirmation_forcepersist_63d_slope_v036_signal,
    f13vc_f13_volume_price_confirmation_forcez_126d_slope_v037_signal,
    f13vc_f13_volume_price_confirmation_forceasym_63d_slope_v038_signal,
    f13vc_f13_volume_price_confirmation_forceeff_63d_slope_v039_signal,
    f13vc_f13_volume_price_confirmation_eom_14d_slope_v040_signal,
    f13vc_f13_volume_price_confirmation_eom_21d_slope_v041_signal,
    f13vc_f13_volume_price_confirmation_eomz_126d_slope_v042_signal,
    f13vc_f13_volume_price_confirmation_eompersist_63d_slope_v043_signal,
    f13vc_f13_volume_price_confirmation_eomdisp_63d_slope_v044_signal,
    f13vc_f13_volume_price_confirmation_pvcorr_21d_slope_v045_signal,
    f13vc_f13_volume_price_confirmation_pvcorr_63d_slope_v046_signal,
    f13vc_f13_volume_price_confirmation_updnvol_21d_slope_v047_signal,
    f13vc_f13_volume_price_confirmation_updnvol_63d_slope_v048_signal,
    f13vc_f13_volume_price_confirmation_vwret_21d_slope_v049_signal,
    f13vc_f13_volume_price_confirmation_pvtslope_63d_slope_v050_signal,
    f13vc_f13_volume_price_confirmation_pvtcorr_63d_slope_v051_signal,
    f13vc_f13_volume_price_confirmation_pvtdisp_42d_slope_v052_signal,
    f13vc_f13_volume_price_confirmation_dvobvslope_63d_slope_v053_signal,
    f13vc_f13_volume_price_confirmation_dvcmf_63d_slope_v054_signal,
    f13vc_f13_volume_price_confirmation_nvi_21d_slope_v055_signal,
    f13vc_f13_volume_price_confirmation_pvi_21d_slope_v056_signal,
    f13vc_f13_volume_price_confirmation_pvinvispr_63d_slope_v057_signal,
    f13vc_f13_volume_price_confirmation_upvolshare_63d_slope_v058_signal,
    f13vc_f13_volume_price_confirmation_volthrust_21d_slope_v059_signal,
    f13vc_f13_volume_price_confirmation_stealth_63d_slope_v060_signal,
    f13vc_f13_volume_price_confirmation_stealthspr_63d_slope_v061_signal,
    f13vc_f13_volume_price_confirmation_netaccdist_63d_slope_v062_signal,
    f13vc_f13_volume_price_confirmation_clvabs_63d_slope_v063_signal,
    f13vc_f13_volume_price_confirmation_clvskew_63d_slope_v064_signal,
    f13vc_f13_volume_price_confirmation_cmfvolint_21d_slope_v065_signal,
    f13vc_f13_volume_price_confirmation_mfratio_21d_slope_v066_signal,
    f13vc_f13_volume_price_confirmation_cmfcross_63d_slope_v067_signal,
    f13vc_f13_volume_price_confirmation_mfvbreadth_63d_slope_v068_signal,
    f13vc_f13_volume_price_confirmation_force_21d_slope_v069_signal,
    f13vc_f13_volume_price_confirmation_dvforcedd_126d_slope_v070_signal,
    f13vc_f13_volume_price_confirmation_tpobvslope_63d_slope_v071_signal,
    f13vc_f13_volume_price_confirmation_cmfreversal_63d_slope_v072_signal,
    f13vc_f13_volume_price_confirmation_momquality_63d_slope_v073_signal,
    f13vc_f13_volume_price_confirmation_signedimpact_21d_slope_v074_signal,
    f13vc_f13_volume_price_confirmation_priceelast_21d_slope_v075_signal,
    f13vc_f13_volume_price_confirmation_weakrally_21d_slope_v076_signal,
    f13vc_f13_volume_price_confirmation_capit_21d_slope_v077_signal,
    f13vc_f13_volume_price_confirmation_obvbeta_63d_slope_v078_signal,
    f13vc_f13_volume_price_confirmation_adbeta_126d_slope_v079_signal,
    f13vc_f13_volume_price_confirmation_chaikinoscz_126d_slope_v080_signal,
    f13vc_f13_volume_price_confirmation_cmfaccel_slope_v081_signal,
    f13vc_f13_volume_price_confirmation_mfidiv_21d_slope_v082_signal,
    f13vc_f13_volume_price_confirmation_mfislope_63d_slope_v083_signal,
    f13vc_f13_volume_price_confirmation_forceraw_252d_slope_v084_signal,
    f13vc_f13_volume_price_confirmation_eomslope_63d_slope_v085_signal,
    f13vc_f13_volume_price_confirmation_eomrank_252d_slope_v086_signal,
    f13vc_f13_volume_price_confirmation_pvrankcorr_63d_slope_v087_signal,
    f13vc_f13_volume_price_confirmation_voltrendconf_63d_slope_v088_signal,
    f13vc_f13_volume_price_confirmation_distdays_21d_slope_v089_signal,
    f13vc_f13_volume_price_confirmation_accdays_21d_slope_v090_signal,
    f13vc_f13_volume_price_confirmation_mfiobvagree_63d_slope_v091_signal,
    f13vc_f13_volume_price_confirmation_volaccel_21d_slope_v092_signal,
    f13vc_f13_volume_price_confirmation_cmfrising_126d_slope_v093_signal,
    f13vc_f13_volume_price_confirmation_adoscdiv_63d_slope_v094_signal,
    f13vc_f13_volume_price_confirmation_eomforce_21d_slope_v095_signal,
    f13vc_f13_volume_price_confirmation_obvpvtdiv_63d_slope_v096_signal,
    f13vc_f13_volume_price_confirmation_mfobvspr_63d_slope_v097_signal,
    f13vc_f13_volume_price_confirmation_breakvol_21d_slope_v098_signal,
    f13vc_f13_volume_price_confirmation_clvret_21d_slope_v099_signal,
    f13vc_f13_volume_price_confirmation_volconc_63d_slope_v100_signal,
    f13vc_f13_volume_price_confirmation_nvi_63d_slope_v101_signal,
    f13vc_f13_volume_price_confirmation_pvi_63d_slope_v102_signal,
    f13vc_f13_volume_price_confirmation_volthrust_63d_slope_v103_signal,
    f13vc_f13_volume_price_confirmation_loud_63d_slope_v104_signal,
    f13vc_f13_volume_price_confirmation_cmfmompx_21d_slope_v105_signal,
    f13vc_f13_volume_price_confirmation_obvnewhi_63d_slope_v106_signal,
    f13vc_f13_volume_price_confirmation_chaikmom_21d_slope_v107_signal,
    f13vc_f13_volume_price_confirmation_cmfstab_126d_slope_v108_signal,
    f13vc_f13_volume_price_confirmation_effdiv_63d_slope_v109_signal,
    f13vc_f13_volume_price_confirmation_updnmom_21d_slope_v110_signal,
    f13vc_f13_volume_price_confirmation_cmfpersist_63d_slope_v111_signal,
    f13vc_f13_volume_price_confirmation_cmfrank_252d_slope_v112_signal,
    f13vc_f13_volume_price_confirmation_mfios_63d_slope_v113_signal,
    f13vc_f13_volume_price_confirmation_mfimom_14d_slope_v114_signal,
    f13vc_f13_volume_price_confirmation_mfiz_252d_slope_v115_signal,
    f13vc_f13_volume_price_confirmation_forcemom_13d_slope_v116_signal,
    f13vc_f13_volume_price_confirmation_forcez21_126d_slope_v117_signal,
    f13vc_f13_volume_price_confirmation_eommom_21d_slope_v118_signal,
    f13vc_f13_volume_price_confirmation_obvmomra_126d_slope_v119_signal,
    f13vc_f13_volume_price_confirmation_adslopechg_63d_slope_v120_signal,
    f13vc_f13_volume_price_confirmation_chaikpersist_63d_slope_v121_signal,
    f13vc_f13_volume_price_confirmation_cmftrend_126d_slope_v122_signal,
    f13vc_f13_volume_price_confirmation_clvmean_63d_slope_v123_signal,
    f13vc_f13_volume_price_confirmation_relvolasym_21d_slope_v124_signal,
    f13vc_f13_volume_price_confirmation_mfratio_63d_slope_v125_signal,
    f13vc_f13_volume_price_confirmation_obvmomn_21d_slope_v126_signal,
    f13vc_f13_volume_price_confirmation_admomn_63d_slope_v127_signal,
    f13vc_f13_volume_price_confirmation_cmfregime_slope_v128_signal,
    f13vc_f13_volume_price_confirmation_forceeff126_slope_v129_signal,
    f13vc_f13_volume_price_confirmation_dvclvtilt_63d_slope_v130_signal,
    f13vc_f13_volume_price_confirmation_mfi14_21d_slope_v131_signal,
    f13vc_f13_volume_price_confirmation_obvslopepv_21d_slope_v132_signal,
    f13vc_f13_volume_price_confirmation_accconv_63d_slope_v133_signal,
    f13vc_f13_volume_price_confirmation_wclvgap_21d_slope_v134_signal,
    f13vc_f13_volume_price_confirmation_dvcmfdt_63d_slope_v135_signal,
    f13vc_f13_volume_price_confirmation_forceconf_21d_slope_v136_signal,
    f13vc_f13_volume_price_confirmation_mfbreadthv_63d_slope_v137_signal,
    f13vc_f13_volume_price_confirmation_distwarn_21d_slope_v138_signal,
    f13vc_f13_volume_price_confirmation_obvpxagree_63d_slope_v139_signal,
    f13vc_f13_volume_price_confirmation_eomret_21d_slope_v140_signal,
    f13vc_f13_volume_price_confirmation_vpelastdisp_63d_slope_v141_signal,
    f13vc_f13_volume_price_confirmation_adaccel_slope_v142_signal,
    f13vc_f13_volume_price_confirmation_mfobvspr_126d_slope_v143_signal,
    f13vc_f13_volume_price_confirmation_effortres_21d_slope_v144_signal,
    f13vc_f13_volume_price_confirmation_cmf21slope_63d_slope_v145_signal,
    f13vc_f13_volume_price_confirmation_dvobvmom_63d_slope_v146_signal,
    f13vc_f13_volume_price_confirmation_mfismdisp_21d_slope_v147_signal,
    f13vc_f13_volume_price_confirmation_netaccdist_126d_slope_v148_signal,
    f13vc_f13_volume_price_confirmation_cmfvolbal_21d_slope_v149_signal,
    f13vc_f13_volume_price_confirmation_tpobvmom_126d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F13_VOLUME_PRICE_CONFIRMATION_REGISTRY_SLOPE_001_150 = REGISTRY


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

    print("OK f13_volume_price_confirmation_2nd_derivatives_001_150_claude: %d features pass" % n_features)
