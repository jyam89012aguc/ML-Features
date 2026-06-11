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


def _rsum(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(2, w // 4)).rank(pct=True) - 0.5


# ===== folder domain primitives (volume-price confirmation) =====
def _obv(close, volume):
    direction = np.sign(close.diff())
    return (direction * volume).fillna(0.0).cumsum()


def _clv(high, low, close):
    rng = (high - low).replace(0, np.nan)
    return ((close - low) - (high - close)) / rng


def _ad_line(high, low, close, volume):
    mfv = _clv(high, low, close) * volume
    return mfv.fillna(0.0).cumsum()


def _cmf(high, low, close, volume, w):
    mfv = _clv(high, low, close) * volume
    return _rsum(mfv, w) / _rsum(volume, w).replace(0, np.nan)


def _typical(high, low, close):
    return (high + low + close) / 3.0


def _mfi(high, low, close, volume, w):
    tp = _typical(high, low, close)
    rmf = tp * volume
    up = tp.diff()
    pos = _rsum(rmf.where(up > 0, 0.0), w)
    neg = _rsum(rmf.where(up < 0, 0.0), w).replace(0, np.nan)
    return 100.0 - 100.0 / (1.0 + pos / neg)


def _force(close, volume):
    return close.diff() * volume


def _vpt(closeadj, volume):
    return (closeadj.pct_change() * volume).fillna(0.0).cumsum()


def _force_ema(close, volume, span):
    fi = _force(close, volume)
    return fi.ewm(span=span, min_periods=max(2, span // 2)).mean() / (
        _mean(close, 21) * _mean(volume, 21)).replace(0, np.nan)


# obv momentum normalized
def _obv_mom(close, volume, w):
    return _obv(close, volume).diff(w) / _rsum(volume, w).replace(0, np.nan)


# ad-line drawdown from its own rolling high (distinct from CMF, which equals diff/volsum)
def _ad_mom(close, high, low, volume, w):
    ad = _ad_line(high, low, close, volume)
    hi = ad.rolling(w, min_periods=max(2, w // 2)).max()
    return (ad - hi) / _rsum(volume, w).replace(0, np.nan)


def _vwap_gap(closeadj, volume, w):
    vwap = _rsum(closeadj * volume, w) / _rsum(volume, w).replace(0, np.nan)
    return closeadj / vwap.replace(0, np.nan) - 1.0


def _updown_bal(close, volume, w):
    # average volume on up-days vs down-days (asymmetry), distinct from OBV momentum
    up = np.sign(close.diff())
    upv = volume.where(up > 0, np.nan)
    dnv = volume.where(up < 0, np.nan)
    avg_up = upv.rolling(w, min_periods=max(2, w // 4)).mean()
    avg_dn = dnv.rolling(w, min_periods=max(2, w // 4)).mean()
    return (avg_up - avg_dn) / (avg_up + avg_dn).replace(0, np.nan)


def _pvcorr(closeadj, volume, w):
    return closeadj.pct_change().rolling(w, min_periods=max(5, w // 2)).corr(volume.diff())


def _emv(high, low, volume, w):
    mid = (high + low) / 2.0
    box = volume / (high - low).replace(0, np.nan)
    return (mid.diff() / box.replace(0, np.nan)).rolling(w, min_periods=max(2, w // 2)).mean()


# ============================================================
# slope (1st derivative) of OBV-momentum 21d, ROC=5d
def f15vc_f15_volume_price_confirmation_obvmom21_5d_slope_v001_signal(close, volume):
    base = _obv_mom(close, volume, 21)
    d = base.diff(5) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of OBV-momentum 21d, ROC=21d
def f15vc_f15_volume_price_confirmation_obvmom21_21d_slope_v002_signal(close, volume):
    base = _obv_mom(close, volume, 21)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of OBV-momentum 63d, ROC=21d
def f15vc_f15_volume_price_confirmation_obvmom63_21d_slope_v003_signal(close, volume):
    base = _obv_mom(close, volume, 63)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of OBV-momentum 63d, ROC=63d
def f15vc_f15_volume_price_confirmation_obvmom63_63d_slope_v004_signal(close, volume):
    base = _obv_mom(close, volume, 63)
    d = base.diff(63) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of OBV z-score 63d, ROC=21d
def f15vc_f15_volume_price_confirmation_obvz63_21d_slope_v005_signal(close, volume):
    base = _z(_obv(close, volume), 63)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of OBV z-score 252d, ROC=63d
def f15vc_f15_volume_price_confirmation_obvz252_63d_slope_v006_signal(close, volume):
    base = _z(_obv(close, volume), 252)
    d = base.diff(63) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of OBV efficiency 63d, ROC=21d
def f15vc_f15_volume_price_confirmation_obveff63_21d_slope_v007_signal(close, volume):
    obv = _obv(close, volume)
    net = obv.diff(63).abs()
    path = obv.diff().abs().rolling(63, min_periods=21).sum()
    base = net / path.replace(0, np.nan)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of A/D-momentum 21d, ROC=5d
def f15vc_f15_volume_price_confirmation_admom21_5d_slope_v008_signal(high, low, close, volume):
    base = _ad_mom(close, high, low, volume, 21)
    d = base.diff(5) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of A/D-momentum 21d, ROC=21d
def f15vc_f15_volume_price_confirmation_admom21_21d_slope_v009_signal(high, low, close, volume):
    base = _ad_mom(close, high, low, volume, 21)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of A/D-momentum 63d, ROC=21d
def f15vc_f15_volume_price_confirmation_admom63_21d_slope_v010_signal(high, low, close, volume):
    base = _ad_mom(close, high, low, volume, 63)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of A/D-momentum 63d, ROC=63d
def f15vc_f15_volume_price_confirmation_admom63_63d_slope_v011_signal(high, low, close, volume):
    base = _ad_mom(close, high, low, volume, 63)
    d = base.diff(63) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of A/D z-score 63d, ROC=21d
def f15vc_f15_volume_price_confirmation_adz63_21d_slope_v012_signal(high, low, close, volume):
    base = _z(_ad_line(high, low, close, volume), 63)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of A/D z-score 252d, ROC=63d
def f15vc_f15_volume_price_confirmation_adz252_63d_slope_v013_signal(high, low, close, volume):
    base = _z(_ad_line(high, low, close, volume), 252)
    d = base.diff(63) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CMF 21d, ROC=5d
def f15vc_f15_volume_price_confirmation_cmf21_5d_slope_v014_signal(high, low, close, volume):
    base = _cmf(high, low, close, volume, 21)
    d = base.diff(5) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CMF 21d, ROC=21d
def f15vc_f15_volume_price_confirmation_cmf21_21d_slope_v015_signal(high, low, close, volume):
    base = _cmf(high, low, close, volume, 21)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CMF 63d, ROC=21d
def f15vc_f15_volume_price_confirmation_cmf63_21d_slope_v016_signal(high, low, close, volume):
    base = _cmf(high, low, close, volume, 63)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CMF 63d, ROC=63d
def f15vc_f15_volume_price_confirmation_cmf63_63d_slope_v017_signal(high, low, close, volume):
    base = _cmf(high, low, close, volume, 63)
    d = base.diff(63) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CMF 126d, ROC=21d
def f15vc_f15_volume_price_confirmation_cmf126_21d_slope_v018_signal(high, low, close, volume):
    base = _cmf(high, low, close, volume, 126)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CMF 126d, ROC=63d
def f15vc_f15_volume_price_confirmation_cmf126_63d_slope_v019_signal(high, low, close, volume):
    base = _cmf(high, low, close, volume, 126)
    d = base.diff(63) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CMF short-long spread (z21 vs z126), ROC=21d (de-scaled term structure)
def f15vc_f15_volume_price_confirmation_cmfspr_21d_slope_v020_signal(high, low, close, volume):
    z21 = _z(_cmf(high, low, close, volume, 21), 126)
    z126 = _z(_cmf(high, low, close, volume, 126), 252)
    base = z21 - z126
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of MFI 21d, ROC=5d
def f15vc_f15_volume_price_confirmation_mfi21_5d_slope_v021_signal(high, low, close, volume):
    base = _mfi(high, low, close, volume, 21) / 100.0
    d = base.diff(5) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of MFI 21d, ROC=21d
def f15vc_f15_volume_price_confirmation_mfi21_21d_slope_v022_signal(high, low, close, volume):
    base = _mfi(high, low, close, volume, 21) / 100.0
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of MFI 63d, ROC=21d
def f15vc_f15_volume_price_confirmation_mfi63_21d_slope_v023_signal(high, low, close, volume):
    base = _mfi(high, low, close, volume, 63) / 100.0
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of MFI 63d, ROC=63d
def f15vc_f15_volume_price_confirmation_mfi63_63d_slope_v024_signal(high, low, close, volume):
    base = _mfi(high, low, close, volume, 63) / 100.0
    d = base.diff(63) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of MFI 126d, ROC=63d
def f15vc_f15_volume_price_confirmation_mfi126_63d_slope_v025_signal(high, low, close, volume):
    base = _mfi(high, low, close, volume, 126) / 100.0
    d = base.diff(63) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of force-index 13d EMA, ROC=5d
def f15vc_f15_volume_price_confirmation_force13_5d_slope_v026_signal(close, volume):
    base = _force_ema(close, volume, 13)
    d = base.diff(5) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of force-index 13d EMA, ROC=21d
def f15vc_f15_volume_price_confirmation_force13_21d_slope_v027_signal(close, volume):
    base = _force_ema(close, volume, 13)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of force-index 63d EMA, ROC=21d
def f15vc_f15_volume_price_confirmation_force63_21d_slope_v028_signal(close, volume):
    base = _force_ema(close, volume, 63)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of force-index 63d EMA, ROC=63d
def f15vc_f15_volume_price_confirmation_force63_63d_slope_v029_signal(close, volume):
    base = _force_ema(close, volume, 63)
    d = base.diff(63) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of force-index 126d EMA, ROC=63d
def f15vc_f15_volume_price_confirmation_force126_63d_slope_v030_signal(close, volume):
    base = _force_ema(close, volume, 126)
    d = base.diff(63) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of VPT range-position 126d, ROC=21d (where volume-price-trend sits in its band)
def f15vc_f15_volume_price_confirmation_vptdisp_21d_slope_v031_signal(closeadj, volume):
    vpt = _vpt(closeadj, volume)
    hi = vpt.rolling(126, min_periods=63).max()
    lo = vpt.rolling(126, min_periods=63).min()
    base = (vpt - lo) / (hi - lo).replace(0, np.nan)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of VPT z-score 126d, ROC=21d
def f15vc_f15_volume_price_confirmation_vptz_21d_slope_v032_signal(closeadj, volume):
    base = _z(_vpt(closeadj, volume), 126)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of VPT z-score 126d, ROC=63d
def f15vc_f15_volume_price_confirmation_vptz_63d_slope_v033_signal(closeadj, volume):
    base = _z(_vpt(closeadj, volume), 126)
    d = base.diff(63) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of up-down volume balance 21d, ROC=5d
def f15vc_f15_volume_price_confirmation_udvol21_5d_slope_v034_signal(close, volume):
    base = _updown_bal(close, volume, 21)
    d = base.diff(5) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of up-down volume balance 63d, ROC=21d
def f15vc_f15_volume_price_confirmation_udvol63_21d_slope_v035_signal(close, volume):
    base = _updown_bal(close, volume, 63)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of up-down volume balance 252d, ROC=63d
def f15vc_f15_volume_price_confirmation_udvol252_63d_slope_v036_signal(close, volume):
    base = _updown_bal(close, volume, 252)
    d = base.diff(63) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of price-volume correlation 63d, ROC=21d
def f15vc_f15_volume_price_confirmation_pvcorr63_21d_slope_v037_signal(closeadj, volume):
    base = _pvcorr(closeadj, volume, 63)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of price-volume correlation 126d, ROC=21d
def f15vc_f15_volume_price_confirmation_pvcorr126_21d_slope_v038_signal(closeadj, volume):
    base = _pvcorr(closeadj, volume, 126)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of price-volume correlation 126d, ROC=63d
def f15vc_f15_volume_price_confirmation_pvcorr126_63d_slope_v039_signal(closeadj, volume):
    base = _pvcorr(closeadj, volume, 126)
    d = base.diff(63) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of Ease-of-Movement 21d, ROC=5d
def f15vc_f15_volume_price_confirmation_emv21_5d_slope_v040_signal(high, low, volume):
    base = _emv(high, low, volume, 21)
    d = base.diff(5) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of Ease-of-Movement 21d, ROC=21d
def f15vc_f15_volume_price_confirmation_emv21_21d_slope_v041_signal(high, low, volume):
    base = _emv(high, low, volume, 21)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CLV-average 21d, ROC=5d
def f15vc_f15_volume_price_confirmation_clv21_5d_slope_v042_signal(high, low, close):
    base = _clv(high, low, close).rolling(21, min_periods=10).mean()
    d = base.diff(5) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CLV-average 63d, ROC=21d
def f15vc_f15_volume_price_confirmation_clv63_21d_slope_v043_signal(high, low, close):
    base = _clv(high, low, close).rolling(63, min_periods=21).mean()
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of volume-weighted minus equal-weighted CLV 63d, ROC=21d (big-day accumulation tilt)
def f15vc_f15_volume_price_confirmation_clvwgt63_21d_slope_v044_signal(high, low, close, volume):
    clv = _clv(high, low, close)
    vw = _rsum(clv * volume, 63) / _rsum(volume, 63).replace(0, np.nan)
    ew = clv.rolling(63, min_periods=21).mean()
    base = vw - ew
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of Chaikin oscillator (3/10), ROC=5d
def f15vc_f15_volume_price_confirmation_chosc_5d_slope_v045_signal(high, low, close, volume):
    ad = _ad_line(high, low, close, volume)
    base = (ad.ewm(span=3, min_periods=2).mean() - ad.ewm(span=10, min_periods=5).mean()) / _mean(volume, 21).replace(0, np.nan)
    d = base.diff(5) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of Chaikin oscillator (3/10), ROC=21d
def f15vc_f15_volume_price_confirmation_chosc_21d_slope_v046_signal(high, low, close, volume):
    ad = _ad_line(high, low, close, volume)
    base = (ad.ewm(span=3, min_periods=2).mean() - ad.ewm(span=10, min_periods=5).mean()) / _mean(volume, 21).replace(0, np.nan)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of slow Chaikin oscillator (21/63), ROC=21d
def f15vc_f15_volume_price_confirmation_choscslow_21d_slope_v047_signal(high, low, close, volume):
    ad = _ad_line(high, low, close, volume)
    base = (ad.ewm(span=21, min_periods=10).mean() - ad.ewm(span=63, min_periods=21).mean()) / _mean(volume, 63).replace(0, np.nan)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of VWAP gap 63d, ROC=5d
def f15vc_f15_volume_price_confirmation_vwap63_5d_slope_v048_signal(closeadj, volume):
    base = _vwap_gap(closeadj, volume, 63)
    d = base.diff(5) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of VWAP gap 63d, ROC=21d
def f15vc_f15_volume_price_confirmation_vwap63_21d_slope_v049_signal(closeadj, volume):
    base = _vwap_gap(closeadj, volume, 63)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of VWAP gap 126d, ROC=21d
def f15vc_f15_volume_price_confirmation_vwap126_21d_slope_v050_signal(closeadj, volume):
    base = _vwap_gap(closeadj, volume, 126)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of MFI-minus-price-rank divergence 63d, ROC=21d (volume-flow leading price)
def f15vc_f15_volume_price_confirmation_mfratio63_21d_slope_v051_signal(high, low, close, volume, closeadj):
    mfi = _mfi(high, low, close, volume, 63) / 100.0 - 0.5
    base = _rank(mfi, 252) - _rank(closeadj.diff(21), 252)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of OBV-price-confirmation regime 63d, ROC=21d
def f15vc_f15_volume_price_confirmation_obvconf63_21d_slope_v052_signal(close, volume):
    obv = _obv(close, volume)

    def _sl(s, w):
        def _f(a):
            m = len(a)
            idx = np.arange(m, dtype=float) - (m - 1) / 2.0
            den = float((idx * idx).sum())
            return float((idx * (a - a.mean())).sum()) / den if den else np.nan
        return s.rolling(w, min_periods=max(2, w // 2)).apply(_f, raw=True)
    conf = (np.sign(_sl(obv, 63)) * np.sign(_sl(close, 63))).rolling(63, min_periods=21).mean()
    d = conf.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net-flow rank 63d, ROC=21d
def f15vc_f15_volume_price_confirmation_netflowrank_21d_slope_v053_signal(close, volume):
    sv = (np.sign(close.diff()) * volume).fillna(0.0)
    netflow = _rsum(sv, 63) / _rsum(volume, 63).replace(0, np.nan)
    base = _rank(netflow, 252)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of accumulation-into-weakness 63d, ROC=21d
def f15vc_f15_volume_price_confirmation_accweak_21d_slope_v054_signal(high, low, close, volume, closeadj):
    mfv = _clv(high, low, close) * volume
    flowz = _z(mfv.rolling(21, min_periods=10).mean(), 126)
    dd = closeadj / _rmax(closeadj, 252).replace(0, np.nan) - 1.0
    base = flowz * (-dd)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CMF-rank 63d, ROC=21d
def f15vc_f15_volume_price_confirmation_cmfrank_21d_slope_v055_signal(high, low, close, volume):
    base = _rank(_cmf(high, low, close, volume, 63), 252)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of force-index rank 63d, ROC=21d
def f15vc_f15_volume_price_confirmation_forcerank_21d_slope_v056_signal(close, volume):
    base = _rank(_force_ema(close, volume, 13), 252)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume vs price-level correlation 63d, ROC=21d
def f15vc_f15_volume_price_confirmation_sdvimbal_21d_slope_v057_signal(closeadj, volume):
    dv = closeadj * volume
    base = closeadj.rolling(63, min_periods=21).corr(dv)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of above-VWAP time 126d, ROC=21d
def f15vc_f15_volume_price_confirmation_abovevwap_21d_slope_v058_signal(closeadj, volume):
    vwap = _rsum(closeadj * volume, 63) / _rsum(volume, 63).replace(0, np.nan)
    above = (closeadj > vwap).astype(float)
    base = above.rolling(126, min_periods=63).mean()
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of Klinger oscillator, ROC=21d
def f15vc_f15_volume_price_confirmation_klinger_21d_slope_v059_signal(high, low, close, volume):
    trend = np.sign(_typical(high, low, close).diff())
    sv = trend * volume
    base = (sv.ewm(span=34, min_periods=17).mean() - sv.ewm(span=55, min_periods=27).mean()) / _mean(volume, 55).replace(0, np.nan)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of money-flow-persistence (force+CMF both positive) 63d, ROC=21d
def f15vc_f15_volume_price_confirmation_mfpersist_21d_slope_v060_signal(high, low, close, volume):
    fp = (_force_ema(close, volume, 13) > 0).astype(float)
    cp = (_cmf(high, low, close, volume, 21) > 0).astype(float)
    base = (fp * cp).rolling(63, min_periods=21).mean()
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of OBV-momentum 126d, ROC=21d
def f15vc_f15_volume_price_confirmation_obvmom126_21d_slope_v061_signal(close, volume):
    base = _obv_mom(close, volume, 126)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of OBV-momentum 126d, ROC=63d
def f15vc_f15_volume_price_confirmation_obvmom126_63d_slope_v062_signal(close, volume):
    base = _obv_mom(close, volume, 126)
    d = base.diff(63) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of A/D-momentum 126d, ROC=21d
def f15vc_f15_volume_price_confirmation_admom126_21d_slope_v063_signal(high, low, close, volume):
    base = _ad_mom(close, high, low, volume, 126)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of A/D-momentum 126d, ROC=63d
def f15vc_f15_volume_price_confirmation_admom126_63d_slope_v064_signal(high, low, close, volume):
    base = _ad_mom(close, high, low, volume, 126)
    d = base.diff(63) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CMF 252d, ROC=63d
def f15vc_f15_volume_price_confirmation_cmf252_63d_slope_v065_signal(high, low, close, volume):
    base = _cmf(high, low, close, volume, 252)
    d = base.diff(63) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of MFI 14d (fast classic), ROC=5d
def f15vc_f15_volume_price_confirmation_mfi14_5d_slope_v066_signal(high, low, close, volume):
    base = _mfi(high, low, close, volume, 14) / 100.0
    d = base.diff(5) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of force-index 2d (Elder short), ROC=5d
def f15vc_f15_volume_price_confirmation_force2_5d_slope_v067_signal(close, volume):
    base = _force_ema(close, volume, 2)
    d = base.diff(5) / 5.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of VPT efficiency 126d, ROC=63d (trend-purity of volume-price advance)
def f15vc_f15_volume_price_confirmation_vptdisp_63d_slope_v068_signal(closeadj, volume):
    vpt = _vpt(closeadj, volume)
    net = vpt.diff(126).abs()
    path = vpt.diff().abs().rolling(126, min_periods=63).sum()
    base = net / path.replace(0, np.nan)
    d = base.diff(63) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of pvcorr 252d, ROC=63d
def f15vc_f15_volume_price_confirmation_pvcorr252_63d_slope_v069_signal(closeadj, volume):
    base = _pvcorr(closeadj, volume, 252)
    d = base.diff(63) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of abs-return-volume correlation 63d, ROC=21d
def f15vc_f15_volume_price_confirmation_absrvol63_21d_slope_v070_signal(closeadj, volume):
    base = closeadj.pct_change().abs().rolling(63, min_periods=21).corr(volume)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of volume-weighted-CLV rank 63d, ROC=21d (relative intraday accumulation footprint)
def f15vc_f15_volume_price_confirmation_clvz63_21d_slope_v071_signal(high, low, close, volume):
    clv = _clv(high, low, close)
    vw = _rsum(clv * volume, 21) / _rsum(volume, 21).replace(0, np.nan)
    base = _rank(vw, 252)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EMV 63d, ROC=21d
def f15vc_f15_volume_price_confirmation_emv63_21d_slope_v072_signal(high, low, volume):
    base = _emv(high, low, volume, 63)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of VWAP gap 126d, ROC=63d
def f15vc_f15_volume_price_confirmation_vwap126_63d_slope_v073_signal(closeadj, volume):
    base = _vwap_gap(closeadj, volume, 126)
    d = base.diff(63) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of A/D-line range position 126d, ROC=21d
def f15vc_f15_volume_price_confirmation_adrngpos_21d_slope_v074_signal(high, low, close, volume):
    ad = _ad_line(high, low, close, volume)
    hi = ad.rolling(126, min_periods=63).max()
    lo = ad.rolling(126, min_periods=63).min()
    base = (ad - lo) / (hi - lo).replace(0, np.nan)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of OBV range position 126d, ROC=21d
def f15vc_f15_volume_price_confirmation_obvrngpos_21d_slope_v075_signal(close, volume):
    obv = _obv(close, volume)
    hi = obv.rolling(126, min_periods=63).max()
    lo = obv.rolling(126, min_periods=63).min()
    base = (obv - lo) / (hi - lo).replace(0, np.nan)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of twin-confirmation (MFI x OBV sign) 63d, ROC=21d
def f15vc_f15_volume_price_confirmation_twinconf_21d_slope_v076_signal(high, low, close, volume):
    mfi = _mfi(high, low, close, volume, 21) / 100.0 - 0.5
    obvm = _obv_mom(close, volume, 21)
    base = (np.sign(mfi) * np.sign(obvm)).rolling(63, min_periods=21).mean()
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume-weighted return divergence 63d, ROC=21d
def f15vc_f15_volume_price_confirmation_dvwret_21d_slope_v077_signal(closeadj, volume):
    dv = closeadj * volume
    ret = closeadj.pct_change()
    base = _rsum(ret * dv, 63) / _rsum(dv, 63).replace(0, np.nan) - ret.rolling(63, min_periods=21).mean()
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of force up/down asymmetry 63d, ROC=21d
def f15vc_f15_volume_price_confirmation_forceasym_21d_slope_v078_signal(close, volume):
    fi = _force(close, volume)
    pos = _rsum(fi.clip(lower=0), 63)
    neg = _rsum((-fi).clip(lower=0), 63)
    base = (pos - neg) / (pos + neg).replace(0, np.nan)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of Twiggs money flow 63d, ROC=21d
def f15vc_f15_volume_price_confirmation_twiggs_21d_slope_v079_signal(high, low, close, volume):
    prev_close = close.shift(1)
    th = pd.concat([high, prev_close], axis=1).max(axis=1)
    tl = pd.concat([low, prev_close], axis=1).min(axis=1)
    tr = (th - tl).replace(0, np.nan)
    clv = ((close - tl) - (th - close)) / tr
    base = (clv * volume).ewm(span=63, min_periods=21).mean() / volume.ewm(span=63, min_periods=21).mean().replace(0, np.nan)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of OBV-momentum 21d, ROC=10d (intermediate)
def f15vc_f15_volume_price_confirmation_obvmom21_10d_slope_v080_signal(close, volume):
    base = _obv_mom(close, volume, 21)
    d = base.diff(10) / 10.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CMF 21d, ROC=10d
def f15vc_f15_volume_price_confirmation_cmf21_10d_slope_v081_signal(high, low, close, volume):
    base = _cmf(high, low, close, volume, 21)
    d = base.diff(10) / 10.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of MFI 21d, ROC=10d
def f15vc_f15_volume_price_confirmation_mfi21_10d_slope_v082_signal(high, low, close, volume):
    base = _mfi(high, low, close, volume, 21) / 100.0
    d = base.diff(10) / 10.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of force-index 13d EMA, ROC=10d
def f15vc_f15_volume_price_confirmation_force13_10d_slope_v083_signal(close, volume):
    base = _force_ema(close, volume, 13)
    d = base.diff(10) / 10.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of A/D-momentum 21d, ROC=10d
def f15vc_f15_volume_price_confirmation_admom21_10d_slope_v084_signal(high, low, close, volume):
    base = _ad_mom(close, high, low, volume, 21)
    d = base.diff(10) / 10.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of up-down balance 21d, ROC=10d
def f15vc_f15_volume_price_confirmation_udvol21_10d_slope_v085_signal(close, volume):
    base = _updown_bal(close, volume, 21)
    d = base.diff(10) / 10.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CMF spread (z63 vs z252), ROC=21d (de-scaled long term structure)
def f15vc_f15_volume_price_confirmation_cmfspr63_21d_slope_v086_signal(high, low, close, volume):
    z63 = _z(_cmf(high, low, close, volume, 63), 126)
    z252 = _z(_cmf(high, low, close, volume, 252), 504)
    base = z63 - z252
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of OBV-slope-spread (z21 vs z126), ROC=21d (de-scaled term-structure)
def f15vc_f15_volume_price_confirmation_obvslopespr_21d_slope_v087_signal(close, volume):
    s21 = _z(_obv_mom(close, volume, 21), 126)
    s126 = _z(_obv_mom(close, volume, 126), 252)
    base = s21 - s126
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of MFI-RSI gap 21d, ROC=21d
def f15vc_f15_volume_price_confirmation_mfirsigap_21d_slope_v088_signal(high, low, close, volume, closeadj):
    mfi = _mfi(high, low, close, volume, 21) / 100.0
    delta = closeadj.diff()
    up = delta.clip(lower=0).rolling(21, min_periods=10).mean()
    dn = (-delta).clip(lower=0).rolling(21, min_periods=10).mean()
    rsi = up / (up + dn).replace(0, np.nan)
    base = mfi - rsi
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of volume-weighted minus equal-weighted CLV 126d, ROC=21d
def f15vc_f15_volume_price_confirmation_clvwgt126_21d_slope_v089_signal(high, low, close, volume):
    clv = _clv(high, low, close)
    vw = _rsum(clv * volume, 126) / _rsum(volume, 126).replace(0, np.nan)
    ew = clv.rolling(126, min_periods=63).mean()
    base = vw - ew
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of down-day-volume share of total volume 63d, ROC=21d (panic-volume tilt)
def f15vc_f15_volume_price_confirmation_downvolcap_21d_slope_v090_signal(close, volume):
    dn = (close.diff() < 0).astype(float)
    dn_share = _rsum(dn * volume, 63) / _rsum(volume, 63).replace(0, np.nan)
    base = _z(dn_share, 252)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of effort-vs-result 21d, ROC=21d
def f15vc_f15_volume_price_confirmation_effres_21d_slope_v091_signal(closeadj, volume):
    base = _z(volume, 63) - _z(closeadj.pct_change().abs(), 63)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of VPT z-score 252d, ROC=63d
def f15vc_f15_volume_price_confirmation_vptz252_63d_slope_v092_signal(closeadj, volume):
    base = _z(_vpt(closeadj, volume), 252)
    d = base.diff(63) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of Klinger signal-line displacement, ROC=21d
def f15vc_f15_volume_price_confirmation_klingersig_21d_slope_v093_signal(high, low, close, volume):
    trend = np.sign(_typical(high, low, close).diff())
    sv = trend * volume
    osc = (sv.ewm(span=34, min_periods=17).mean() - sv.ewm(span=55, min_periods=27).mean())
    base = (osc - osc.ewm(span=13, min_periods=7).mean()) / _mean(volume, 55).replace(0, np.nan)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of money-flow-volume skew 63d, ROC=21d
def f15vc_f15_volume_price_confirmation_mfvskew_21d_slope_v094_signal(high, low, close, volume):
    mfv = (_clv(high, low, close) * volume) / _mean(volume, 21).replace(0, np.nan)
    base = mfv.rolling(63, min_periods=21).skew()
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of composite-z (OBV+CMF+force) 126d, ROC=21d
def f15vc_f15_volume_price_confirmation_compz_21d_slope_v095_signal(high, low, close, volume):
    obvz = _z(_obv(close, volume), 126)
    cmfz = _z(_cmf(high, low, close, volume, 21), 126)
    forcez = _z(_force(close, volume).ewm(span=13, min_periods=7).mean(), 126)
    base = (obvz + cmfz + forcez) / 3.0
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CMF-dispersion 63d, ROC=21d
def f15vc_f15_volume_price_confirmation_cmfdisp_21d_slope_v096_signal(high, low, close, volume):
    base = _cmf(high, low, close, volume, 21).rolling(63, min_periods=21).std()
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of OBV-elasticity 63d, ROC=21d
def f15vc_f15_volume_price_confirmation_obvelast_21d_slope_v097_signal(closeadj, close, volume):
    obv = _obv(close, volume)
    dobv = obv.diff(21) / _mean(volume, 21).replace(0, np.nan)
    base = (dobv / closeadj.pct_change(21).replace(0, np.nan)).clip(-50, 50)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of flow-concentration 63d, ROC=21d
def f15vc_f15_volume_price_confirmation_flowconc_21d_slope_v098_signal(close, volume):
    sv = np.sign(close.diff()) * volume
    net = sv.rolling(63, min_periods=21).sum().abs()
    mx = sv.abs().rolling(63, min_periods=21).max()
    base = mx / net.replace(0, np.nan)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of A/D-efficiency 63d, ROC=21d
def f15vc_f15_volume_price_confirmation_adeff_21d_slope_v099_signal(high, low, close, volume):
    ad = _ad_line(high, low, close, volume)
    net = ad.diff(63).abs()
    path = ad.diff().abs().rolling(63, min_periods=21).sum()
    base = net / path.replace(0, np.nan)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CMF 21d, ROC=42d
def f15vc_f15_volume_price_confirmation_cmf21_42d_slope_v100_signal(high, low, close, volume):
    base = _cmf(high, low, close, volume, 21)
    d = base.diff(42) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of OBV-momentum 63d, ROC=42d
def f15vc_f15_volume_price_confirmation_obvmom63_42d_slope_v101_signal(close, volume):
    base = _obv_mom(close, volume, 63)
    d = base.diff(42) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of MFI 63d, ROC=42d
def f15vc_f15_volume_price_confirmation_mfi63_42d_slope_v102_signal(high, low, close, volume):
    base = _mfi(high, low, close, volume, 63) / 100.0
    d = base.diff(42) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of A/D-momentum 63d, ROC=42d
def f15vc_f15_volume_price_confirmation_admom63_42d_slope_v103_signal(high, low, close, volume):
    base = _ad_mom(close, high, low, volume, 63)
    d = base.diff(42) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of force-index 63d EMA, ROC=42d
def f15vc_f15_volume_price_confirmation_force63_42d_slope_v104_signal(close, volume):
    base = _force_ema(close, volume, 63)
    d = base.diff(42) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of VWAP gap 63d, ROC=42d
def f15vc_f15_volume_price_confirmation_vwap63_42d_slope_v105_signal(closeadj, volume):
    base = _vwap_gap(closeadj, volume, 63)
    d = base.diff(42) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of up-down balance 63d, ROC=42d
def f15vc_f15_volume_price_confirmation_udvol63_42d_slope_v106_signal(close, volume):
    base = _updown_bal(close, volume, 63)
    d = base.diff(42) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of pvcorr 63d, ROC=42d
def f15vc_f15_volume_price_confirmation_pvcorr63_42d_slope_v107_signal(closeadj, volume):
    base = _pvcorr(closeadj, volume, 63)
    d = base.diff(42) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CLV-average 63d, ROC=42d
def f15vc_f15_volume_price_confirmation_clv63_42d_slope_v108_signal(high, low, close):
    base = _clv(high, low, close).rolling(63, min_periods=21).mean()
    d = base.diff(42) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CMF-z 63d, ROC=21d
def f15vc_f15_volume_price_confirmation_cmfz63_21d_slope_v109_signal(high, low, close, volume):
    base = _z(_cmf(high, low, close, volume, 63), 126)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of force-index-z 21d, ROC=21d
def f15vc_f15_volume_price_confirmation_forcez21_21d_slope_v110_signal(close, volume):
    fi = _force(close, volume).rolling(21, min_periods=10).mean()
    base = _z(fi, 126)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of MFI-z 21d, ROC=21d
def f15vc_f15_volume_price_confirmation_mfiz21_21d_slope_v111_signal(high, low, close, volume):
    base = _z(_mfi(high, low, close, volume, 21), 126)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of triple-confirmation 63d, ROC=21d
def f15vc_f15_volume_price_confirmation_tripleconf_21d_slope_v112_signal(high, low, close, volume, closeadj):
    obv_up = (_obv(close, volume).diff(21) > 0).astype(float)
    cmf_up = (_cmf(high, low, close, volume, 21) > 0).astype(float)
    pr_up = (closeadj.diff(21) > 0).astype(float)
    base = (obv_up + cmf_up + pr_up).rolling(63, min_periods=21).mean() / 3.0
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of accumulation-at-lows (OBV slope x (1-rngpos)), ROC=21d
def f15vc_f15_volume_price_confirmation_obvlowaccum_21d_slope_v113_signal(close, volume, closeadj):
    osl = _obv_mom(close, volume, 63)
    rngpos = (closeadj - _rmin(closeadj, 252)) / (_rmax(closeadj, 252) - _rmin(closeadj, 252)).replace(0, np.nan)
    base = osl * (1.0 - rngpos)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of distribution-at-highs, ROC=21d
def f15vc_f15_volume_price_confirmation_addisthi_21d_slope_v114_signal(high, low, close, volume, closeadj):
    asl = _ad_mom(close, high, low, volume, 63)
    rngpos = (closeadj - _rmin(closeadj, 252)) / (_rmax(closeadj, 252) - _rmin(closeadj, 252)).replace(0, np.nan)
    base = -asl * rngpos
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CMF-bottom (cmf x -drawdown), ROC=21d
def f15vc_f15_volume_price_confirmation_cmfbottom_21d_slope_v115_signal(high, low, close, volume, closeadj):
    cmf = _cmf(high, low, close, volume, 63)
    dd = closeadj / _rmax(closeadj, 252).replace(0, np.nan) - 1.0
    base = cmf * (-dd)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of VWAP gap 126d, ROC=42d
def f15vc_f15_volume_price_confirmation_vwap126_42d_slope_v116_signal(closeadj, volume):
    base = _vwap_gap(closeadj, volume, 126)
    d = base.diff(42) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EMV 21d, ROC=10d
def f15vc_f15_volume_price_confirmation_emv21_10d_slope_v117_signal(high, low, volume):
    base = _emv(high, low, volume, 21)
    d = base.diff(10) / 10.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of OBV-z 126d, ROC=21d
def f15vc_f15_volume_price_confirmation_obvz126_21d_slope_v118_signal(close, volume):
    base = _z(_obv(close, volume), 126)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of A/D-z 126d, ROC=21d
def f15vc_f15_volume_price_confirmation_adz126_21d_slope_v119_signal(high, low, close, volume):
    base = _z(_ad_line(high, low, close, volume), 126)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of force-asymmetry 63d, ROC=42d
def f15vc_f15_volume_price_confirmation_forceasym_42d_slope_v120_signal(close, volume):
    fi = _force(close, volume)
    pos = _rsum(fi.clip(lower=0), 63)
    neg = _rsum((-fi).clip(lower=0), 63)
    base = (pos - neg) / (pos + neg).replace(0, np.nan)
    d = base.diff(42) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net-flow rank 63d, ROC=42d
def f15vc_f15_volume_price_confirmation_netflowrank_42d_slope_v121_signal(close, volume):
    sv = (np.sign(close.diff()) * volume).fillna(0.0)
    netflow = _rsum(sv, 63) / _rsum(volume, 63).replace(0, np.nan)
    base = _rank(netflow, 252)
    d = base.diff(42) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CMF 126d, ROC=42d
def f15vc_f15_volume_price_confirmation_cmf126_42d_slope_v122_signal(high, low, close, volume):
    base = _cmf(high, low, close, volume, 126)
    d = base.diff(42) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of MFI 126d, ROC=42d
def f15vc_f15_volume_price_confirmation_mfi126_42d_slope_v123_signal(high, low, close, volume):
    base = _mfi(high, low, close, volume, 126) / 100.0
    d = base.diff(42) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of OBV-momentum 126d, ROC=42d
def f15vc_f15_volume_price_confirmation_obvmom126_42d_slope_v124_signal(close, volume):
    base = _obv_mom(close, volume, 126)
    d = base.diff(42) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of A/D-momentum 126d, ROC=42d
def f15vc_f15_volume_price_confirmation_admom126_42d_slope_v125_signal(high, low, close, volume):
    base = _ad_mom(close, high, low, volume, 126)
    d = base.diff(42) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of volume-weighted minus equal-weighted CLV 63d, ROC=42d
def f15vc_f15_volume_price_confirmation_clvwgt63_42d_slope_v126_signal(high, low, close, volume):
    clv = _clv(high, low, close)
    vw = _rsum(clv * volume, 63) / _rsum(volume, 63).replace(0, np.nan)
    ew = clv.rolling(63, min_periods=21).mean()
    base = vw - ew
    d = base.diff(42) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume-weighted return divergence 126d, ROC=42d
def f15vc_f15_volume_price_confirmation_sdvimbal_42d_slope_v127_signal(closeadj, volume):
    dv = closeadj * volume
    ret = closeadj.pct_change()
    base = _rsum(ret * dv, 126) / _rsum(dv, 126).replace(0, np.nan) - ret.rolling(126, min_periods=63).mean()
    d = base.diff(42) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of pvcorr 126d, ROC=42d
def f15vc_f15_volume_price_confirmation_pvcorr126_42d_slope_v128_signal(closeadj, volume):
    base = _pvcorr(closeadj, volume, 126)
    d = base.diff(42) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CMF-rank 63d, ROC=42d
def f15vc_f15_volume_price_confirmation_cmfrank_42d_slope_v129_signal(high, low, close, volume):
    base = _rank(_cmf(high, low, close, volume, 63), 252)
    d = base.diff(42) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of force-rank 63d, ROC=42d
def f15vc_f15_volume_price_confirmation_forcerank_42d_slope_v130_signal(close, volume):
    base = _rank(_force_ema(close, volume, 13), 252)
    d = base.diff(42) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of above-VWAP time 126d, ROC=42d
def f15vc_f15_volume_price_confirmation_abovevwap_42d_slope_v131_signal(closeadj, volume):
    vwap = _rsum(closeadj * volume, 63) / _rsum(volume, 63).replace(0, np.nan)
    above = (closeadj > vwap).astype(float)
    base = above.rolling(126, min_periods=63).mean()
    d = base.diff(42) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of MFI-OBV divergence 126d, ROC=21d
def f15vc_f15_volume_price_confirmation_mfiobvdiv_21d_slope_v132_signal(high, low, close, volume):
    mfi = _mfi(high, low, close, volume, 21) / 100.0 - 0.5
    obv = _obv(close, volume)
    base = _rank(mfi, 252) - _rank(obv.diff(63), 252)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of Klinger oscillator, ROC=42d
def f15vc_f15_volume_price_confirmation_klinger_42d_slope_v133_signal(high, low, close, volume):
    trend = np.sign(_typical(high, low, close).diff())
    sv = trend * volume
    base = (sv.ewm(span=34, min_periods=17).mean() - sv.ewm(span=55, min_periods=27).mean()) / _mean(volume, 55).replace(0, np.nan)
    d = base.diff(42) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of money-flow-ratio z-score 63d, ROC=42d (de-trended flow-ratio extremity)
def f15vc_f15_volume_price_confirmation_mfratio_42d_slope_v134_signal(high, low, close, volume):
    tp = _typical(high, low, close)
    rmf = tp * volume
    up = tp.diff()
    pos = _rsum(rmf.where(up > 0, 0.0), 63)
    neg = _rsum(rmf.where(up < 0, 0.0), 63).replace(0, np.nan)
    ratio = np.log(pos.replace(0, np.nan) / neg)
    base = _z(ratio, 252)
    d = base.diff(42) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of Chaikin-osc positive-time fraction 63d, ROC=21d (money-flow regime)
def f15vc_f15_volume_price_confirmation_choscz_21d_slope_v135_signal(high, low, close, volume):
    ad = _ad_line(high, low, close, volume)
    osc = ad.ewm(span=3, min_periods=2).mean() - ad.ewm(span=10, min_periods=5).mean()
    base = (osc > 0).astype(float).rolling(63, min_periods=21).mean() + 0.0001 * osc / _mean(volume, 21).replace(0, np.nan)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CLV dispersion 63d, ROC=42d (intraday close-position choppiness)
def f15vc_f15_volume_price_confirmation_clvz63_42d_slope_v136_signal(high, low, close):
    base = _clv(high, low, close).rolling(63, min_periods=21).std()
    d = base.diff(42) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of volume-weighted momentum, ROC=21d
def f15vc_f15_volume_price_confirmation_volwgtmom_21d_slope_v137_signal(closeadj, volume):
    def _sl(s, w):
        def _f(a):
            m = len(a)
            idx = np.arange(m, dtype=float) - (m - 1) / 2.0
            den = float((idx * idx).sum())
            return float((idx * (a - a.mean())).sum()) / den if den else np.nan
        return s.rolling(w, min_periods=max(2, w // 2)).apply(_f, raw=True)
    mom = closeadj.pct_change(63)
    voltrend = _sl(volume, 63) / _mean(volume, 63).replace(0, np.nan)
    base = mom * np.tanh(voltrend * 63.0)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EMV-persistence 63d, ROC=21d
def f15vc_f15_volume_price_confirmation_emvpersist_21d_slope_v138_signal(high, low, volume):
    emv = _emv(high, low, volume, 5)
    base = (emv > 0).astype(float).rolling(63, min_periods=21).mean() + 100.0 * emv.rolling(21, min_periods=10).mean()
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of force-chop 63d, ROC=21d
def f15vc_f15_volume_price_confirmation_forcechop_21d_slope_v139_signal(close, volume):
    fi = _force(close, volume).ewm(span=13, min_periods=7).mean()
    norm = fi / (_mean(close, 21) * _mean(volume, 21)).replace(0, np.nan)
    flip = (np.sign(fi) != np.sign(fi.shift(1))).astype(float)
    base = flip.rolling(63, min_periods=21).mean() + 0.1 * norm.rolling(21, min_periods=10).std()
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of volume-confirmed breakout, ROC=21d
def f15vc_f15_volume_price_confirmation_volbreakout_21d_slope_v140_signal(high, low, close, volume, closeadj):
    near_hi = (closeadj >= _rmax(closeadj, 63) * 0.98).astype(float)
    cmf = _cmf(high, low, close, volume, 21)
    base = (near_hi * cmf).rolling(21, min_periods=10).mean()
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of OBV-efficiency 126d, ROC=21d (trend-purity acceleration of accumulation)
def f15vc_f15_volume_price_confirmation_obvmom21_63d_slope_v141_signal(close, volume):
    obv = _obv(close, volume)
    net = obv.diff(126).abs()
    path = obv.diff().abs().rolling(126, min_periods=63).sum()
    base = net / path.replace(0, np.nan)
    d = base.diff(21) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of CMF 63d, ROC=42d
def f15vc_f15_volume_price_confirmation_cmf63_42d_slope_v142_signal(high, low, close, volume):
    base = _cmf(high, low, close, volume, 63)
    d = base.diff(42) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of A/D-z 63d, ROC=42d
def f15vc_f15_volume_price_confirmation_adz63_42d_slope_v143_signal(high, low, close, volume):
    base = _z(_ad_line(high, low, close, volume), 63)
    d = base.diff(42) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of OBV-z 63d, ROC=42d
def f15vc_f15_volume_price_confirmation_obvz63_42d_slope_v144_signal(close, volume):
    base = _z(_obv(close, volume), 63)
    d = base.diff(42) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dollar-volume return divergence 63d, ROC=42d
def f15vc_f15_volume_price_confirmation_dvwret_42d_slope_v145_signal(closeadj, volume):
    dv = closeadj * volume
    ret = closeadj.pct_change()
    base = _rsum(ret * dv, 63) / _rsum(dv, 63).replace(0, np.nan) - ret.rolling(63, min_periods=21).mean()
    d = base.diff(42) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of twin-confirmation 63d, ROC=42d
def f15vc_f15_volume_price_confirmation_twinconf_42d_slope_v146_signal(high, low, close, volume):
    mfi = _mfi(high, low, close, volume, 21) / 100.0 - 0.5
    obvm = _obv_mom(close, volume, 21)
    base = (np.sign(mfi) * np.sign(obvm)).rolling(63, min_periods=21).mean()
    d = base.diff(42) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of MFI-RSI gap 21d, ROC=42d
def f15vc_f15_volume_price_confirmation_mfirsigap_42d_slope_v147_signal(high, low, close, volume, closeadj):
    mfi = _mfi(high, low, close, volume, 21) / 100.0
    delta = closeadj.diff()
    up = delta.clip(lower=0).rolling(21, min_periods=10).mean()
    dn = (-delta).clip(lower=0).rolling(21, min_periods=10).mean()
    rsi = up / (up + dn).replace(0, np.nan)
    base = mfi - rsi
    d = base.diff(42) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of VWAP gap 63d, ROC=63d
def f15vc_f15_volume_price_confirmation_vwap63_63d_slope_v148_signal(closeadj, volume):
    base = _vwap_gap(closeadj, volume, 63)
    d = base.diff(63) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of force-index 13d EMA, ROC=42d
def f15vc_f15_volume_price_confirmation_force13_42d_slope_v149_signal(close, volume):
    base = _force_ema(close, volume, 13)
    d = base.diff(42) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope of composite-z 126d, ROC=42d
def f15vc_f15_volume_price_confirmation_compz_42d_slope_v150_signal(high, low, close, volume):
    obvz = _z(_obv(close, volume), 126)
    cmfz = _z(_cmf(high, low, close, volume, 21), 126)
    forcez = _z(_force(close, volume).ewm(span=13, min_periods=7).mean(), 126)
    base = (obvz + cmfz + forcez) / 3.0
    d = base.diff(42) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f15vc_f15_volume_price_confirmation_obvmom21_5d_slope_v001_signal,
    f15vc_f15_volume_price_confirmation_obvmom21_21d_slope_v002_signal,
    f15vc_f15_volume_price_confirmation_obvmom63_21d_slope_v003_signal,
    f15vc_f15_volume_price_confirmation_obvmom63_63d_slope_v004_signal,
    f15vc_f15_volume_price_confirmation_obvz63_21d_slope_v005_signal,
    f15vc_f15_volume_price_confirmation_obvz252_63d_slope_v006_signal,
    f15vc_f15_volume_price_confirmation_obveff63_21d_slope_v007_signal,
    f15vc_f15_volume_price_confirmation_admom21_5d_slope_v008_signal,
    f15vc_f15_volume_price_confirmation_admom21_21d_slope_v009_signal,
    f15vc_f15_volume_price_confirmation_admom63_21d_slope_v010_signal,
    f15vc_f15_volume_price_confirmation_admom63_63d_slope_v011_signal,
    f15vc_f15_volume_price_confirmation_adz63_21d_slope_v012_signal,
    f15vc_f15_volume_price_confirmation_adz252_63d_slope_v013_signal,
    f15vc_f15_volume_price_confirmation_cmf21_5d_slope_v014_signal,
    f15vc_f15_volume_price_confirmation_cmf21_21d_slope_v015_signal,
    f15vc_f15_volume_price_confirmation_cmf63_21d_slope_v016_signal,
    f15vc_f15_volume_price_confirmation_cmf63_63d_slope_v017_signal,
    f15vc_f15_volume_price_confirmation_cmf126_21d_slope_v018_signal,
    f15vc_f15_volume_price_confirmation_cmf126_63d_slope_v019_signal,
    f15vc_f15_volume_price_confirmation_cmfspr_21d_slope_v020_signal,
    f15vc_f15_volume_price_confirmation_mfi21_5d_slope_v021_signal,
    f15vc_f15_volume_price_confirmation_mfi21_21d_slope_v022_signal,
    f15vc_f15_volume_price_confirmation_mfi63_21d_slope_v023_signal,
    f15vc_f15_volume_price_confirmation_mfi63_63d_slope_v024_signal,
    f15vc_f15_volume_price_confirmation_mfi126_63d_slope_v025_signal,
    f15vc_f15_volume_price_confirmation_force13_5d_slope_v026_signal,
    f15vc_f15_volume_price_confirmation_force13_21d_slope_v027_signal,
    f15vc_f15_volume_price_confirmation_force63_21d_slope_v028_signal,
    f15vc_f15_volume_price_confirmation_force63_63d_slope_v029_signal,
    f15vc_f15_volume_price_confirmation_force126_63d_slope_v030_signal,
    f15vc_f15_volume_price_confirmation_vptdisp_21d_slope_v031_signal,
    f15vc_f15_volume_price_confirmation_vptz_21d_slope_v032_signal,
    f15vc_f15_volume_price_confirmation_vptz_63d_slope_v033_signal,
    f15vc_f15_volume_price_confirmation_udvol21_5d_slope_v034_signal,
    f15vc_f15_volume_price_confirmation_udvol63_21d_slope_v035_signal,
    f15vc_f15_volume_price_confirmation_udvol252_63d_slope_v036_signal,
    f15vc_f15_volume_price_confirmation_pvcorr63_21d_slope_v037_signal,
    f15vc_f15_volume_price_confirmation_pvcorr126_21d_slope_v038_signal,
    f15vc_f15_volume_price_confirmation_pvcorr126_63d_slope_v039_signal,
    f15vc_f15_volume_price_confirmation_emv21_5d_slope_v040_signal,
    f15vc_f15_volume_price_confirmation_emv21_21d_slope_v041_signal,
    f15vc_f15_volume_price_confirmation_clv21_5d_slope_v042_signal,
    f15vc_f15_volume_price_confirmation_clv63_21d_slope_v043_signal,
    f15vc_f15_volume_price_confirmation_clvwgt63_21d_slope_v044_signal,
    f15vc_f15_volume_price_confirmation_chosc_5d_slope_v045_signal,
    f15vc_f15_volume_price_confirmation_chosc_21d_slope_v046_signal,
    f15vc_f15_volume_price_confirmation_choscslow_21d_slope_v047_signal,
    f15vc_f15_volume_price_confirmation_vwap63_5d_slope_v048_signal,
    f15vc_f15_volume_price_confirmation_vwap63_21d_slope_v049_signal,
    f15vc_f15_volume_price_confirmation_vwap126_21d_slope_v050_signal,
    f15vc_f15_volume_price_confirmation_mfratio63_21d_slope_v051_signal,
    f15vc_f15_volume_price_confirmation_obvconf63_21d_slope_v052_signal,
    f15vc_f15_volume_price_confirmation_netflowrank_21d_slope_v053_signal,
    f15vc_f15_volume_price_confirmation_accweak_21d_slope_v054_signal,
    f15vc_f15_volume_price_confirmation_cmfrank_21d_slope_v055_signal,
    f15vc_f15_volume_price_confirmation_forcerank_21d_slope_v056_signal,
    f15vc_f15_volume_price_confirmation_sdvimbal_21d_slope_v057_signal,
    f15vc_f15_volume_price_confirmation_abovevwap_21d_slope_v058_signal,
    f15vc_f15_volume_price_confirmation_klinger_21d_slope_v059_signal,
    f15vc_f15_volume_price_confirmation_mfpersist_21d_slope_v060_signal,
    f15vc_f15_volume_price_confirmation_obvmom126_21d_slope_v061_signal,
    f15vc_f15_volume_price_confirmation_obvmom126_63d_slope_v062_signal,
    f15vc_f15_volume_price_confirmation_admom126_21d_slope_v063_signal,
    f15vc_f15_volume_price_confirmation_admom126_63d_slope_v064_signal,
    f15vc_f15_volume_price_confirmation_cmf252_63d_slope_v065_signal,
    f15vc_f15_volume_price_confirmation_mfi14_5d_slope_v066_signal,
    f15vc_f15_volume_price_confirmation_force2_5d_slope_v067_signal,
    f15vc_f15_volume_price_confirmation_vptdisp_63d_slope_v068_signal,
    f15vc_f15_volume_price_confirmation_pvcorr252_63d_slope_v069_signal,
    f15vc_f15_volume_price_confirmation_absrvol63_21d_slope_v070_signal,
    f15vc_f15_volume_price_confirmation_clvz63_21d_slope_v071_signal,
    f15vc_f15_volume_price_confirmation_emv63_21d_slope_v072_signal,
    f15vc_f15_volume_price_confirmation_vwap126_63d_slope_v073_signal,
    f15vc_f15_volume_price_confirmation_adrngpos_21d_slope_v074_signal,
    f15vc_f15_volume_price_confirmation_obvrngpos_21d_slope_v075_signal,
    f15vc_f15_volume_price_confirmation_twinconf_21d_slope_v076_signal,
    f15vc_f15_volume_price_confirmation_dvwret_21d_slope_v077_signal,
    f15vc_f15_volume_price_confirmation_forceasym_21d_slope_v078_signal,
    f15vc_f15_volume_price_confirmation_twiggs_21d_slope_v079_signal,
    f15vc_f15_volume_price_confirmation_obvmom21_10d_slope_v080_signal,
    f15vc_f15_volume_price_confirmation_cmf21_10d_slope_v081_signal,
    f15vc_f15_volume_price_confirmation_mfi21_10d_slope_v082_signal,
    f15vc_f15_volume_price_confirmation_force13_10d_slope_v083_signal,
    f15vc_f15_volume_price_confirmation_admom21_10d_slope_v084_signal,
    f15vc_f15_volume_price_confirmation_udvol21_10d_slope_v085_signal,
    f15vc_f15_volume_price_confirmation_cmfspr63_21d_slope_v086_signal,
    f15vc_f15_volume_price_confirmation_obvslopespr_21d_slope_v087_signal,
    f15vc_f15_volume_price_confirmation_mfirsigap_21d_slope_v088_signal,
    f15vc_f15_volume_price_confirmation_clvwgt126_21d_slope_v089_signal,
    f15vc_f15_volume_price_confirmation_downvolcap_21d_slope_v090_signal,
    f15vc_f15_volume_price_confirmation_effres_21d_slope_v091_signal,
    f15vc_f15_volume_price_confirmation_vptz252_63d_slope_v092_signal,
    f15vc_f15_volume_price_confirmation_klingersig_21d_slope_v093_signal,
    f15vc_f15_volume_price_confirmation_mfvskew_21d_slope_v094_signal,
    f15vc_f15_volume_price_confirmation_compz_21d_slope_v095_signal,
    f15vc_f15_volume_price_confirmation_cmfdisp_21d_slope_v096_signal,
    f15vc_f15_volume_price_confirmation_obvelast_21d_slope_v097_signal,
    f15vc_f15_volume_price_confirmation_flowconc_21d_slope_v098_signal,
    f15vc_f15_volume_price_confirmation_adeff_21d_slope_v099_signal,
    f15vc_f15_volume_price_confirmation_cmf21_42d_slope_v100_signal,
    f15vc_f15_volume_price_confirmation_obvmom63_42d_slope_v101_signal,
    f15vc_f15_volume_price_confirmation_mfi63_42d_slope_v102_signal,
    f15vc_f15_volume_price_confirmation_admom63_42d_slope_v103_signal,
    f15vc_f15_volume_price_confirmation_force63_42d_slope_v104_signal,
    f15vc_f15_volume_price_confirmation_vwap63_42d_slope_v105_signal,
    f15vc_f15_volume_price_confirmation_udvol63_42d_slope_v106_signal,
    f15vc_f15_volume_price_confirmation_pvcorr63_42d_slope_v107_signal,
    f15vc_f15_volume_price_confirmation_clv63_42d_slope_v108_signal,
    f15vc_f15_volume_price_confirmation_cmfz63_21d_slope_v109_signal,
    f15vc_f15_volume_price_confirmation_forcez21_21d_slope_v110_signal,
    f15vc_f15_volume_price_confirmation_mfiz21_21d_slope_v111_signal,
    f15vc_f15_volume_price_confirmation_tripleconf_21d_slope_v112_signal,
    f15vc_f15_volume_price_confirmation_obvlowaccum_21d_slope_v113_signal,
    f15vc_f15_volume_price_confirmation_addisthi_21d_slope_v114_signal,
    f15vc_f15_volume_price_confirmation_cmfbottom_21d_slope_v115_signal,
    f15vc_f15_volume_price_confirmation_vwap126_42d_slope_v116_signal,
    f15vc_f15_volume_price_confirmation_emv21_10d_slope_v117_signal,
    f15vc_f15_volume_price_confirmation_obvz126_21d_slope_v118_signal,
    f15vc_f15_volume_price_confirmation_adz126_21d_slope_v119_signal,
    f15vc_f15_volume_price_confirmation_forceasym_42d_slope_v120_signal,
    f15vc_f15_volume_price_confirmation_netflowrank_42d_slope_v121_signal,
    f15vc_f15_volume_price_confirmation_cmf126_42d_slope_v122_signal,
    f15vc_f15_volume_price_confirmation_mfi126_42d_slope_v123_signal,
    f15vc_f15_volume_price_confirmation_obvmom126_42d_slope_v124_signal,
    f15vc_f15_volume_price_confirmation_admom126_42d_slope_v125_signal,
    f15vc_f15_volume_price_confirmation_clvwgt63_42d_slope_v126_signal,
    f15vc_f15_volume_price_confirmation_sdvimbal_42d_slope_v127_signal,
    f15vc_f15_volume_price_confirmation_pvcorr126_42d_slope_v128_signal,
    f15vc_f15_volume_price_confirmation_cmfrank_42d_slope_v129_signal,
    f15vc_f15_volume_price_confirmation_forcerank_42d_slope_v130_signal,
    f15vc_f15_volume_price_confirmation_abovevwap_42d_slope_v131_signal,
    f15vc_f15_volume_price_confirmation_mfiobvdiv_21d_slope_v132_signal,
    f15vc_f15_volume_price_confirmation_klinger_42d_slope_v133_signal,
    f15vc_f15_volume_price_confirmation_mfratio_42d_slope_v134_signal,
    f15vc_f15_volume_price_confirmation_choscz_21d_slope_v135_signal,
    f15vc_f15_volume_price_confirmation_clvz63_42d_slope_v136_signal,
    f15vc_f15_volume_price_confirmation_volwgtmom_21d_slope_v137_signal,
    f15vc_f15_volume_price_confirmation_emvpersist_21d_slope_v138_signal,
    f15vc_f15_volume_price_confirmation_forcechop_21d_slope_v139_signal,
    f15vc_f15_volume_price_confirmation_volbreakout_21d_slope_v140_signal,
    f15vc_f15_volume_price_confirmation_obvmom21_63d_slope_v141_signal,
    f15vc_f15_volume_price_confirmation_cmf63_42d_slope_v142_signal,
    f15vc_f15_volume_price_confirmation_adz63_42d_slope_v143_signal,
    f15vc_f15_volume_price_confirmation_obvz63_42d_slope_v144_signal,
    f15vc_f15_volume_price_confirmation_dvwret_42d_slope_v145_signal,
    f15vc_f15_volume_price_confirmation_twinconf_42d_slope_v146_signal,
    f15vc_f15_volume_price_confirmation_mfirsigap_42d_slope_v147_signal,
    f15vc_f15_volume_price_confirmation_vwap63_63d_slope_v148_signal,
    f15vc_f15_volume_price_confirmation_force13_42d_slope_v149_signal,
    f15vc_f15_volume_price_confirmation_compz_42d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F15_VOLUME_PRICE_CONFIRMATION_REGISTRY_001_150 = REGISTRY


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
            idx = ai.index.intersection(aj.index)
            if len(idx) < 30:
                continue
            c = ai.loc[idx].corr(aj.loc[idx])
            if c is None or np.isnan(c):
                continue
            assert abs(c) <= 0.97, "CORR %s vs %s = %.4f" % (ni, nj, c)

    print("OK f15_volume_price_confirmation_2nd_derivatives_001_150_claude: %d features pass" % n_features)
