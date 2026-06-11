import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
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


def _diff(s, n):
    return s.diff(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f06_accumulation_obv(close, volume, w):
    r = close.pct_change()
    sign = np.sign(r).fillna(0.0)
    obv = (sign * volume).rolling(w, min_periods=max(1, w // 2)).sum()
    return obv / volume.rolling(w, min_periods=max(1, w // 2)).sum().replace(0, np.nan)


def _f06_money_flow(close, high, low, volume, w):
    tp = (high + low + close) / 3.0
    mf = tp * volume
    pos = mf * (close > close.shift(1)).astype(float)
    neg = mf * (close < close.shift(1)).astype(float)
    pos_s = pos.rolling(w, min_periods=max(1, w // 2)).sum()
    neg_s = neg.rolling(w, min_periods=max(1, w // 2)).sum()
    return (pos_s - neg_s) / (pos_s + neg_s).replace(0, np.nan)


def _f06_accumulation_ad(close, high, low, volume, w):
    rng = (high - low).replace(0, np.nan)
    clv = ((close - low) - (high - close)) / rng
    ad = (clv * volume).rolling(w, min_periods=max(1, w // 2)).sum()
    return ad / volume.rolling(w, min_periods=max(1, w // 2)).sum().replace(0, np.nan)


# 21d on-balance volume normalized
def f06va_f06_volume_accumulation_obv_21d_base_v001_signal(closeadj, volume):
    result = _f06_accumulation_obv(closeadj, volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d on-balance volume normalized
def f06va_f06_volume_accumulation_obv_63d_base_v002_signal(closeadj, volume):
    result = _f06_accumulation_obv(closeadj, volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d obv normalized
def f06va_f06_volume_accumulation_obv_126d_base_v003_signal(closeadj, volume):
    result = _f06_accumulation_obv(closeadj, volume, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d obv normalized
def f06va_f06_volume_accumulation_obv_252d_base_v004_signal(closeadj, volume):
    result = _f06_accumulation_obv(closeadj, volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d obv normalized
def f06va_f06_volume_accumulation_obv_504d_base_v005_signal(closeadj, volume):
    result = _f06_accumulation_obv(closeadj, volume, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d obv normalized
def f06va_f06_volume_accumulation_obv_5d_base_v006_signal(closeadj, volume):
    result = _f06_accumulation_obv(closeadj, volume, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d obv normalized
def f06va_f06_volume_accumulation_obv_10d_base_v007_signal(closeadj, volume):
    result = _f06_accumulation_obv(closeadj, volume, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d obv normalized
def f06va_f06_volume_accumulation_obv_42d_base_v008_signal(closeadj, volume):
    result = _f06_accumulation_obv(closeadj, volume, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d obv normalized
def f06va_f06_volume_accumulation_obv_189d_base_v009_signal(closeadj, volume):
    result = _f06_accumulation_obv(closeadj, volume, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d obv normalized
def f06va_f06_volume_accumulation_obv_378d_base_v010_signal(closeadj, volume):
    result = _f06_accumulation_obv(closeadj, volume, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA of obv
def f06va_f06_volume_accumulation_obvema_21d_base_v011_signal(closeadj, volume):
    o = _f06_accumulation_obv(closeadj, volume, 21)
    result = o.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of obv
def f06va_f06_volume_accumulation_obvema_63d_base_v012_signal(closeadj, volume):
    o = _f06_accumulation_obv(closeadj, volume, 63)
    result = o.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of obv
def f06va_f06_volume_accumulation_obvema_252d_base_v013_signal(closeadj, volume):
    o = _f06_accumulation_obv(closeadj, volume, 252)
    result = o.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d zscore of obv (252d window)
def f06va_f06_volume_accumulation_obvz_21d_base_v014_signal(closeadj, volume):
    result = _z(_f06_accumulation_obv(closeadj, volume, 21), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of obv
def f06va_f06_volume_accumulation_obvz_63d_base_v015_signal(closeadj, volume):
    result = _z(_f06_accumulation_obv(closeadj, volume, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of obv (504d window)
def f06va_f06_volume_accumulation_obvz_252d_base_v016_signal(closeadj, volume):
    result = _z(_f06_accumulation_obv(closeadj, volume, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of obv
def f06va_f06_volume_accumulation_obvstd_21d_base_v017_signal(closeadj, volume):
    result = _std(_f06_accumulation_obv(closeadj, volume, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of obv
def f06va_f06_volume_accumulation_obvstd_63d_base_v018_signal(closeadj, volume):
    result = _std(_f06_accumulation_obv(closeadj, volume, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of obv
def f06va_f06_volume_accumulation_obvstd_252d_base_v019_signal(closeadj, volume):
    result = _std(_f06_accumulation_obv(closeadj, volume, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d obv minus 63d obv (acceleration)
def f06va_f06_volume_accumulation_obvdiff_21m63_base_v020_signal(closeadj, volume):
    result = (_f06_accumulation_obv(closeadj, volume, 21) - _f06_accumulation_obv(closeadj, volume, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d obv minus 252d obv
def f06va_f06_volume_accumulation_obvdiff_63m252_base_v021_signal(closeadj, volume):
    result = (_f06_accumulation_obv(closeadj, volume, 63) - _f06_accumulation_obv(closeadj, volume, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d obv minus 504d obv
def f06va_f06_volume_accumulation_obvdiff_252m504_base_v022_signal(closeadj, volume):
    result = (_f06_accumulation_obv(closeadj, volume, 252) - _f06_accumulation_obv(closeadj, volume, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d obv ratio over 63d
def f06va_f06_volume_accumulation_obvratio_21v63_base_v023_signal(closeadj, volume):
    a = _f06_accumulation_obv(closeadj, volume, 21)
    b = _f06_accumulation_obv(closeadj, volume, 63).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d obv ratio over 252d
def f06va_f06_volume_accumulation_obvratio_63v252_base_v024_signal(closeadj, volume):
    a = _f06_accumulation_obv(closeadj, volume, 63)
    b = _f06_accumulation_obv(closeadj, volume, 252).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d money flow index (MFI-style)
def f06va_f06_volume_accumulation_mfi_21d_base_v025_signal(closeadj, volume, high, low):
    result = _f06_money_flow(closeadj, high, low, volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d money flow
def f06va_f06_volume_accumulation_mfi_63d_base_v026_signal(closeadj, volume, high, low):
    result = _f06_money_flow(closeadj, high, low, volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d money flow
def f06va_f06_volume_accumulation_mfi_126d_base_v027_signal(closeadj, volume, high, low):
    result = _f06_money_flow(closeadj, high, low, volume, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d money flow
def f06va_f06_volume_accumulation_mfi_252d_base_v028_signal(closeadj, volume, high, low):
    result = _f06_money_flow(closeadj, high, low, volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d money flow
def f06va_f06_volume_accumulation_mfi_504d_base_v029_signal(closeadj, volume, high, low):
    result = _f06_money_flow(closeadj, high, low, volume, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d money flow
def f06va_f06_volume_accumulation_mfi_5d_base_v030_signal(closeadj, volume, high, low):
    result = _f06_money_flow(closeadj, high, low, volume, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d money flow
def f06va_f06_volume_accumulation_mfi_10d_base_v031_signal(closeadj, volume, high, low):
    result = _f06_money_flow(closeadj, high, low, volume, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d money flow
def f06va_f06_volume_accumulation_mfi_42d_base_v032_signal(closeadj, volume, high, low):
    result = _f06_money_flow(closeadj, high, low, volume, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d money flow
def f06va_f06_volume_accumulation_mfi_189d_base_v033_signal(closeadj, volume, high, low):
    result = _f06_money_flow(closeadj, high, low, volume, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d money flow
def f06va_f06_volume_accumulation_mfi_378d_base_v034_signal(closeadj, volume, high, low):
    result = _f06_money_flow(closeadj, high, low, volume, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA of money flow
def f06va_f06_volume_accumulation_mfiema_21d_base_v035_signal(closeadj, volume, high, low):
    m = _f06_money_flow(closeadj, high, low, volume, 21)
    result = m.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of money flow
def f06va_f06_volume_accumulation_mfiema_63d_base_v036_signal(closeadj, volume, high, low):
    m = _f06_money_flow(closeadj, high, low, volume, 63)
    result = m.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of money flow
def f06va_f06_volume_accumulation_mfiema_252d_base_v037_signal(closeadj, volume, high, low):
    m = _f06_money_flow(closeadj, high, low, volume, 252)
    result = m.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d zscore of money flow
def f06va_f06_volume_accumulation_mfiz_21d_base_v038_signal(closeadj, volume, high, low):
    result = _z(_f06_money_flow(closeadj, high, low, volume, 21), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of money flow
def f06va_f06_volume_accumulation_mfiz_63d_base_v039_signal(closeadj, volume, high, low):
    result = _z(_f06_money_flow(closeadj, high, low, volume, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of money flow
def f06va_f06_volume_accumulation_mfiz_252d_base_v040_signal(closeadj, volume, high, low):
    result = _z(_f06_money_flow(closeadj, high, low, volume, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d money flow minus 63d money flow
def f06va_f06_volume_accumulation_mfidiff_21m63_base_v041_signal(closeadj, volume, high, low):
    result = (_f06_money_flow(closeadj, high, low, volume, 21) - _f06_money_flow(closeadj, high, low, volume, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d MFI minus 252d MFI
def f06va_f06_volume_accumulation_mfidiff_63m252_base_v042_signal(closeadj, volume, high, low):
    result = (_f06_money_flow(closeadj, high, low, volume, 63) - _f06_money_flow(closeadj, high, low, volume, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d MFI minus 504d MFI
def f06va_f06_volume_accumulation_mfidiff_252m504_base_v043_signal(closeadj, volume, high, low):
    result = (_f06_money_flow(closeadj, high, low, volume, 252) - _f06_money_flow(closeadj, high, low, volume, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d MFI ratio over 63d
def f06va_f06_volume_accumulation_mfiratio_21v63_base_v044_signal(closeadj, volume, high, low):
    a = _f06_money_flow(closeadj, high, low, volume, 21)
    b = _f06_money_flow(closeadj, high, low, volume, 63).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d MFI ratio over 252d
def f06va_f06_volume_accumulation_mfiratio_63v252_base_v045_signal(closeadj, volume, high, low):
    a = _f06_money_flow(closeadj, high, low, volume, 63)
    b = _f06_money_flow(closeadj, high, low, volume, 252).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accumulation/distribution line (CLV-weighted volume)
def f06va_f06_volume_accumulation_ad_21d_base_v046_signal(closeadj, volume, high, low):
    result = _f06_accumulation_ad(closeadj, high, low, volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d A/D line
def f06va_f06_volume_accumulation_ad_63d_base_v047_signal(closeadj, volume, high, low):
    result = _f06_accumulation_ad(closeadj, high, low, volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d A/D line
def f06va_f06_volume_accumulation_ad_126d_base_v048_signal(closeadj, volume, high, low):
    result = _f06_accumulation_ad(closeadj, high, low, volume, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d A/D line
def f06va_f06_volume_accumulation_ad_252d_base_v049_signal(closeadj, volume, high, low):
    result = _f06_accumulation_ad(closeadj, high, low, volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d A/D line
def f06va_f06_volume_accumulation_ad_504d_base_v050_signal(closeadj, volume, high, low):
    result = _f06_accumulation_ad(closeadj, high, low, volume, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA of A/D
def f06va_f06_volume_accumulation_adema_21d_base_v051_signal(closeadj, volume, high, low):
    a = _f06_accumulation_ad(closeadj, high, low, volume, 21)
    result = a.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of A/D
def f06va_f06_volume_accumulation_adema_63d_base_v052_signal(closeadj, volume, high, low):
    a = _f06_accumulation_ad(closeadj, high, low, volume, 63)
    result = a.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of A/D
def f06va_f06_volume_accumulation_adema_252d_base_v053_signal(closeadj, volume, high, low):
    a = _f06_accumulation_ad(closeadj, high, low, volume, 252)
    result = a.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d zscore of A/D
def f06va_f06_volume_accumulation_adz_21d_base_v054_signal(closeadj, volume, high, low):
    result = _z(_f06_accumulation_ad(closeadj, high, low, volume, 21), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of A/D
def f06va_f06_volume_accumulation_adz_63d_base_v055_signal(closeadj, volume, high, low):
    result = _z(_f06_accumulation_ad(closeadj, high, low, volume, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of A/D
def f06va_f06_volume_accumulation_adz_252d_base_v056_signal(closeadj, volume, high, low):
    result = _z(_f06_accumulation_ad(closeadj, high, low, volume, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d A/D minus 63d A/D
def f06va_f06_volume_accumulation_addiff_21m63_base_v057_signal(closeadj, volume, high, low):
    result = (_f06_accumulation_ad(closeadj, high, low, volume, 21) - _f06_accumulation_ad(closeadj, high, low, volume, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d A/D minus 252d A/D
def f06va_f06_volume_accumulation_addiff_63m252_base_v058_signal(closeadj, volume, high, low):
    result = (_f06_accumulation_ad(closeadj, high, low, volume, 63) - _f06_accumulation_ad(closeadj, high, low, volume, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d A/D minus 504d A/D
def f06va_f06_volume_accumulation_addiff_252m504_base_v059_signal(closeadj, volume, high, low):
    result = (_f06_accumulation_ad(closeadj, high, low, volume, 252) - _f06_accumulation_ad(closeadj, high, low, volume, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d obv × dollar volume mean
def f06va_f06_volume_accumulation_obvxdv_21d_base_v060_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f06_accumulation_obv(closeadj, volume, 21) * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d obv × dollar volume mean
def f06va_f06_volume_accumulation_obvxdv_63d_base_v061_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f06_accumulation_obv(closeadj, volume, 63) * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d obv × dollar volume mean
def f06va_f06_volume_accumulation_obvxdv_252d_base_v062_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f06_accumulation_obv(closeadj, volume, 252) * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d obv × volume zscore
def f06va_f06_volume_accumulation_obvxvolz_21d_base_v063_signal(closeadj, volume):
    result = _f06_accumulation_obv(closeadj, volume, 21) * _z(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d obv × volume zscore
def f06va_f06_volume_accumulation_obvxvolz_63d_base_v064_signal(closeadj, volume):
    result = _f06_accumulation_obv(closeadj, volume, 63) * _z(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d obv × 252d volume zscore
def f06va_f06_volume_accumulation_obvxvolz_252d_base_v065_signal(closeadj, volume):
    result = _f06_accumulation_obv(closeadj, volume, 252) * _z(volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d MFI × volume zscore
def f06va_f06_volume_accumulation_mfixvolz_21d_base_v066_signal(closeadj, volume, high, low):
    result = _f06_money_flow(closeadj, high, low, volume, 21) * _z(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d MFI × volume zscore
def f06va_f06_volume_accumulation_mfixvolz_63d_base_v067_signal(closeadj, volume, high, low):
    result = _f06_money_flow(closeadj, high, low, volume, 63) * _z(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d MFI × dollar volume mean
def f06va_f06_volume_accumulation_mfixdv_252d_base_v068_signal(closeadj, volume, high, low):
    dv = closeadj * volume
    result = _f06_money_flow(closeadj, high, low, volume, 252) * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d A/D × volume zscore
def f06va_f06_volume_accumulation_adxvolz_21d_base_v069_signal(closeadj, volume, high, low):
    result = _f06_accumulation_ad(closeadj, high, low, volume, 21) * _z(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d A/D × volume zscore
def f06va_f06_volume_accumulation_adxvolz_63d_base_v070_signal(closeadj, volume, high, low):
    result = _f06_accumulation_ad(closeadj, high, low, volume, 63) * _z(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d obv × 21d return
def f06va_f06_volume_accumulation_obvxret_21d_base_v071_signal(closeadj, volume):
    r21 = closeadj.pct_change(21)
    result = _f06_accumulation_obv(closeadj, volume, 21) * r21 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d obv × 63d return
def f06va_f06_volume_accumulation_obvxret_63d_base_v072_signal(closeadj, volume):
    r63 = closeadj.pct_change(63)
    result = _f06_accumulation_obv(closeadj, volume, 63) * r63 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d obv × 252d return
def f06va_f06_volume_accumulation_obvxret_252d_base_v073_signal(closeadj, volume):
    r252 = closeadj.pct_change(252)
    result = _f06_accumulation_obv(closeadj, volume, 252) * r252 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d composite accumulation: obv + mfi + ad
def f06va_f06_volume_accumulation_acccomp_21d_base_v074_signal(closeadj, volume, high, low):
    result = (_f06_accumulation_obv(closeadj, volume, 21) + _f06_money_flow(closeadj, high, low, volume, 21) + _f06_accumulation_ad(closeadj, high, low, volume, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite accumulation
def f06va_f06_volume_accumulation_acccomp_252d_base_v075_signal(closeadj, volume, high, low):
    result = (_f06_accumulation_obv(closeadj, volume, 252) + _f06_money_flow(closeadj, high, low, volume, 252) + _f06_accumulation_ad(closeadj, high, low, volume, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f06va_f06_volume_accumulation_obv_21d_base_v001_signal,
    f06va_f06_volume_accumulation_obv_63d_base_v002_signal,
    f06va_f06_volume_accumulation_obv_126d_base_v003_signal,
    f06va_f06_volume_accumulation_obv_252d_base_v004_signal,
    f06va_f06_volume_accumulation_obv_504d_base_v005_signal,
    f06va_f06_volume_accumulation_obv_5d_base_v006_signal,
    f06va_f06_volume_accumulation_obv_10d_base_v007_signal,
    f06va_f06_volume_accumulation_obv_42d_base_v008_signal,
    f06va_f06_volume_accumulation_obv_189d_base_v009_signal,
    f06va_f06_volume_accumulation_obv_378d_base_v010_signal,
    f06va_f06_volume_accumulation_obvema_21d_base_v011_signal,
    f06va_f06_volume_accumulation_obvema_63d_base_v012_signal,
    f06va_f06_volume_accumulation_obvema_252d_base_v013_signal,
    f06va_f06_volume_accumulation_obvz_21d_base_v014_signal,
    f06va_f06_volume_accumulation_obvz_63d_base_v015_signal,
    f06va_f06_volume_accumulation_obvz_252d_base_v016_signal,
    f06va_f06_volume_accumulation_obvstd_21d_base_v017_signal,
    f06va_f06_volume_accumulation_obvstd_63d_base_v018_signal,
    f06va_f06_volume_accumulation_obvstd_252d_base_v019_signal,
    f06va_f06_volume_accumulation_obvdiff_21m63_base_v020_signal,
    f06va_f06_volume_accumulation_obvdiff_63m252_base_v021_signal,
    f06va_f06_volume_accumulation_obvdiff_252m504_base_v022_signal,
    f06va_f06_volume_accumulation_obvratio_21v63_base_v023_signal,
    f06va_f06_volume_accumulation_obvratio_63v252_base_v024_signal,
    f06va_f06_volume_accumulation_mfi_21d_base_v025_signal,
    f06va_f06_volume_accumulation_mfi_63d_base_v026_signal,
    f06va_f06_volume_accumulation_mfi_126d_base_v027_signal,
    f06va_f06_volume_accumulation_mfi_252d_base_v028_signal,
    f06va_f06_volume_accumulation_mfi_504d_base_v029_signal,
    f06va_f06_volume_accumulation_mfi_5d_base_v030_signal,
    f06va_f06_volume_accumulation_mfi_10d_base_v031_signal,
    f06va_f06_volume_accumulation_mfi_42d_base_v032_signal,
    f06va_f06_volume_accumulation_mfi_189d_base_v033_signal,
    f06va_f06_volume_accumulation_mfi_378d_base_v034_signal,
    f06va_f06_volume_accumulation_mfiema_21d_base_v035_signal,
    f06va_f06_volume_accumulation_mfiema_63d_base_v036_signal,
    f06va_f06_volume_accumulation_mfiema_252d_base_v037_signal,
    f06va_f06_volume_accumulation_mfiz_21d_base_v038_signal,
    f06va_f06_volume_accumulation_mfiz_63d_base_v039_signal,
    f06va_f06_volume_accumulation_mfiz_252d_base_v040_signal,
    f06va_f06_volume_accumulation_mfidiff_21m63_base_v041_signal,
    f06va_f06_volume_accumulation_mfidiff_63m252_base_v042_signal,
    f06va_f06_volume_accumulation_mfidiff_252m504_base_v043_signal,
    f06va_f06_volume_accumulation_mfiratio_21v63_base_v044_signal,
    f06va_f06_volume_accumulation_mfiratio_63v252_base_v045_signal,
    f06va_f06_volume_accumulation_ad_21d_base_v046_signal,
    f06va_f06_volume_accumulation_ad_63d_base_v047_signal,
    f06va_f06_volume_accumulation_ad_126d_base_v048_signal,
    f06va_f06_volume_accumulation_ad_252d_base_v049_signal,
    f06va_f06_volume_accumulation_ad_504d_base_v050_signal,
    f06va_f06_volume_accumulation_adema_21d_base_v051_signal,
    f06va_f06_volume_accumulation_adema_63d_base_v052_signal,
    f06va_f06_volume_accumulation_adema_252d_base_v053_signal,
    f06va_f06_volume_accumulation_adz_21d_base_v054_signal,
    f06va_f06_volume_accumulation_adz_63d_base_v055_signal,
    f06va_f06_volume_accumulation_adz_252d_base_v056_signal,
    f06va_f06_volume_accumulation_addiff_21m63_base_v057_signal,
    f06va_f06_volume_accumulation_addiff_63m252_base_v058_signal,
    f06va_f06_volume_accumulation_addiff_252m504_base_v059_signal,
    f06va_f06_volume_accumulation_obvxdv_21d_base_v060_signal,
    f06va_f06_volume_accumulation_obvxdv_63d_base_v061_signal,
    f06va_f06_volume_accumulation_obvxdv_252d_base_v062_signal,
    f06va_f06_volume_accumulation_obvxvolz_21d_base_v063_signal,
    f06va_f06_volume_accumulation_obvxvolz_63d_base_v064_signal,
    f06va_f06_volume_accumulation_obvxvolz_252d_base_v065_signal,
    f06va_f06_volume_accumulation_mfixvolz_21d_base_v066_signal,
    f06va_f06_volume_accumulation_mfixvolz_63d_base_v067_signal,
    f06va_f06_volume_accumulation_mfixdv_252d_base_v068_signal,
    f06va_f06_volume_accumulation_adxvolz_21d_base_v069_signal,
    f06va_f06_volume_accumulation_adxvolz_63d_base_v070_signal,
    f06va_f06_volume_accumulation_obvxret_21d_base_v071_signal,
    f06va_f06_volume_accumulation_obvxret_63d_base_v072_signal,
    f06va_f06_volume_accumulation_obvxret_252d_base_v073_signal,
    f06va_f06_volume_accumulation_acccomp_21d_base_v074_signal,
    f06va_f06_volume_accumulation_acccomp_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F06_VOLUME_ACCUMULATION_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    cols = {"closeadj": closeadj, "high": high, "low": low, "volume": volume}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f06_accumulation_obv", "_f06_money_flow", "_f06_accumulation_ad")
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f06_volume_accumulation_base_001_075_claude: {n_features} features pass")
