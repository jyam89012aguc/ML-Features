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


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


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


# 5d slope of 21d obv
def f06va_f06_volume_accumulation_obv_21d_slope_v001_signal(closeadj, volume):
    base = _f06_accumulation_obv(closeadj, volume, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d obv
def f06va_f06_volume_accumulation_obv_21d_slope_v002_signal(closeadj, volume):
    base = _f06_accumulation_obv(closeadj, volume, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d obv
def f06va_f06_volume_accumulation_obv_63d_slope_v003_signal(closeadj, volume):
    base = _f06_accumulation_obv(closeadj, volume, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d obv
def f06va_f06_volume_accumulation_obv_63d_slope_v004_signal(closeadj, volume):
    base = _f06_accumulation_obv(closeadj, volume, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d obv
def f06va_f06_volume_accumulation_obv_63d_slope_v005_signal(closeadj, volume):
    base = _f06_accumulation_obv(closeadj, volume, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d obv
def f06va_f06_volume_accumulation_obv_126d_slope_v006_signal(closeadj, volume):
    base = _f06_accumulation_obv(closeadj, volume, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d obv
def f06va_f06_volume_accumulation_obv_126d_slope_v007_signal(closeadj, volume):
    base = _f06_accumulation_obv(closeadj, volume, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d obv
def f06va_f06_volume_accumulation_obv_252d_slope_v008_signal(closeadj, volume):
    base = _f06_accumulation_obv(closeadj, volume, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d obv
def f06va_f06_volume_accumulation_obv_252d_slope_v009_signal(closeadj, volume):
    base = _f06_accumulation_obv(closeadj, volume, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d obv
def f06va_f06_volume_accumulation_obv_504d_slope_v010_signal(closeadj, volume):
    base = _f06_accumulation_obv(closeadj, volume, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d obv
def f06va_f06_volume_accumulation_obv_504d_slope_v011_signal(closeadj, volume):
    base = _f06_accumulation_obv(closeadj, volume, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 5d obv
def f06va_f06_volume_accumulation_obv_5d_slope_v012_signal(closeadj, volume):
    base = _f06_accumulation_obv(closeadj, volume, 5) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 10d obv
def f06va_f06_volume_accumulation_obv_10d_slope_v013_signal(closeadj, volume):
    base = _f06_accumulation_obv(closeadj, volume, 10) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 42d obv
def f06va_f06_volume_accumulation_obv_42d_slope_v014_signal(closeadj, volume):
    base = _f06_accumulation_obv(closeadj, volume, 42) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 189d obv
def f06va_f06_volume_accumulation_obv_189d_slope_v015_signal(closeadj, volume):
    base = _f06_accumulation_obv(closeadj, volume, 189) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 378d obv
def f06va_f06_volume_accumulation_obv_378d_slope_v016_signal(closeadj, volume):
    base = _f06_accumulation_obv(closeadj, volume, 378) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d obv EMA
def f06va_f06_volume_accumulation_obvema_21d_slope_v017_signal(closeadj, volume):
    o = _f06_accumulation_obv(closeadj, volume, 21)
    base = o.ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d obv EMA
def f06va_f06_volume_accumulation_obvema_63d_slope_v018_signal(closeadj, volume):
    o = _f06_accumulation_obv(closeadj, volume, 63)
    base = o.ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d obv EMA
def f06va_f06_volume_accumulation_obvema_252d_slope_v019_signal(closeadj, volume):
    o = _f06_accumulation_obv(closeadj, volume, 252)
    base = o.ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d obv z
def f06va_f06_volume_accumulation_obvz_21d_slope_v020_signal(closeadj, volume):
    base = _z(_f06_accumulation_obv(closeadj, volume, 21), 252)
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d obv z
def f06va_f06_volume_accumulation_obvz_63d_slope_v021_signal(closeadj, volume):
    base = _z(_f06_accumulation_obv(closeadj, volume, 63), 252)
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d obv z
def f06va_f06_volume_accumulation_obvz_252d_slope_v022_signal(closeadj, volume):
    base = _z(_f06_accumulation_obv(closeadj, volume, 252), 504)
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d obv std
def f06va_f06_volume_accumulation_obvstd_21d_slope_v023_signal(closeadj, volume):
    base = _std(_f06_accumulation_obv(closeadj, volume, 21), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d obv std
def f06va_f06_volume_accumulation_obvstd_63d_slope_v024_signal(closeadj, volume):
    base = _std(_f06_accumulation_obv(closeadj, volume, 63), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d obv std
def f06va_f06_volume_accumulation_obvstd_252d_slope_v025_signal(closeadj, volume):
    base = _std(_f06_accumulation_obv(closeadj, volume, 252), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of obv diff (21-63)
def f06va_f06_volume_accumulation_obvdiff_21m63_slope_v026_signal(closeadj, volume):
    base = (_f06_accumulation_obv(closeadj, volume, 21) - _f06_accumulation_obv(closeadj, volume, 63)) * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of obv diff (63-252)
def f06va_f06_volume_accumulation_obvdiff_63m252_slope_v027_signal(closeadj, volume):
    base = (_f06_accumulation_obv(closeadj, volume, 63) - _f06_accumulation_obv(closeadj, volume, 252)) * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of obv diff (252-504)
def f06va_f06_volume_accumulation_obvdiff_252m504_slope_v028_signal(closeadj, volume):
    base = (_f06_accumulation_obv(closeadj, volume, 252) - _f06_accumulation_obv(closeadj, volume, 504)) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of obv ratio 21v63
def f06va_f06_volume_accumulation_obvratio_21v63_slope_v029_signal(closeadj, volume):
    a = _f06_accumulation_obv(closeadj, volume, 21)
    b = _f06_accumulation_obv(closeadj, volume, 63).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of obv ratio 63v252
def f06va_f06_volume_accumulation_obvratio_63v252_slope_v030_signal(closeadj, volume):
    a = _f06_accumulation_obv(closeadj, volume, 63)
    b = _f06_accumulation_obv(closeadj, volume, 252).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d MFI
def f06va_f06_volume_accumulation_mfi_21d_slope_v031_signal(closeadj, volume, high, low):
    base = _f06_money_flow(closeadj, high, low, volume, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d MFI
def f06va_f06_volume_accumulation_mfi_21d_slope_v032_signal(closeadj, volume, high, low):
    base = _f06_money_flow(closeadj, high, low, volume, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d MFI
def f06va_f06_volume_accumulation_mfi_63d_slope_v033_signal(closeadj, volume, high, low):
    base = _f06_money_flow(closeadj, high, low, volume, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d MFI
def f06va_f06_volume_accumulation_mfi_63d_slope_v034_signal(closeadj, volume, high, low):
    base = _f06_money_flow(closeadj, high, low, volume, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d MFI
def f06va_f06_volume_accumulation_mfi_126d_slope_v035_signal(closeadj, volume, high, low):
    base = _f06_money_flow(closeadj, high, low, volume, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d MFI
def f06va_f06_volume_accumulation_mfi_252d_slope_v036_signal(closeadj, volume, high, low):
    base = _f06_money_flow(closeadj, high, low, volume, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d MFI
def f06va_f06_volume_accumulation_mfi_504d_slope_v037_signal(closeadj, volume, high, low):
    base = _f06_money_flow(closeadj, high, low, volume, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 5d MFI
def f06va_f06_volume_accumulation_mfi_5d_slope_v038_signal(closeadj, volume, high, low):
    base = _f06_money_flow(closeadj, high, low, volume, 5) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 10d MFI
def f06va_f06_volume_accumulation_mfi_10d_slope_v039_signal(closeadj, volume, high, low):
    base = _f06_money_flow(closeadj, high, low, volume, 10) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 42d MFI
def f06va_f06_volume_accumulation_mfi_42d_slope_v040_signal(closeadj, volume, high, low):
    base = _f06_money_flow(closeadj, high, low, volume, 42) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 189d MFI
def f06va_f06_volume_accumulation_mfi_189d_slope_v041_signal(closeadj, volume, high, low):
    base = _f06_money_flow(closeadj, high, low, volume, 189) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 378d MFI
def f06va_f06_volume_accumulation_mfi_378d_slope_v042_signal(closeadj, volume, high, low):
    base = _f06_money_flow(closeadj, high, low, volume, 378) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d MFI EMA
def f06va_f06_volume_accumulation_mfiema_21d_slope_v043_signal(closeadj, volume, high, low):
    m = _f06_money_flow(closeadj, high, low, volume, 21)
    base = m.ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d MFI EMA
def f06va_f06_volume_accumulation_mfiema_63d_slope_v044_signal(closeadj, volume, high, low):
    m = _f06_money_flow(closeadj, high, low, volume, 63)
    base = m.ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d MFI EMA
def f06va_f06_volume_accumulation_mfiema_252d_slope_v045_signal(closeadj, volume, high, low):
    m = _f06_money_flow(closeadj, high, low, volume, 252)
    base = m.ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d MFI z
def f06va_f06_volume_accumulation_mfiz_21d_slope_v046_signal(closeadj, volume, high, low):
    base = _z(_f06_money_flow(closeadj, high, low, volume, 21), 252)
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d MFI z
def f06va_f06_volume_accumulation_mfiz_63d_slope_v047_signal(closeadj, volume, high, low):
    base = _z(_f06_money_flow(closeadj, high, low, volume, 63), 252)
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d MFI z
def f06va_f06_volume_accumulation_mfiz_252d_slope_v048_signal(closeadj, volume, high, low):
    base = _z(_f06_money_flow(closeadj, high, low, volume, 252), 504)
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of MFI diff (21-63)
def f06va_f06_volume_accumulation_mfidiff_21m63_slope_v049_signal(closeadj, volume, high, low):
    base = (_f06_money_flow(closeadj, high, low, volume, 21) - _f06_money_flow(closeadj, high, low, volume, 63)) * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of MFI diff (63-252)
def f06va_f06_volume_accumulation_mfidiff_63m252_slope_v050_signal(closeadj, volume, high, low):
    base = (_f06_money_flow(closeadj, high, low, volume, 63) - _f06_money_flow(closeadj, high, low, volume, 252)) * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of MFI diff (252-504)
def f06va_f06_volume_accumulation_mfidiff_252m504_slope_v051_signal(closeadj, volume, high, low):
    base = (_f06_money_flow(closeadj, high, low, volume, 252) - _f06_money_flow(closeadj, high, low, volume, 504)) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of MFI ratio 21v63
def f06va_f06_volume_accumulation_mfiratio_21v63_slope_v052_signal(closeadj, volume, high, low):
    a = _f06_money_flow(closeadj, high, low, volume, 21)
    b = _f06_money_flow(closeadj, high, low, volume, 63).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of MFI ratio 63v252
def f06va_f06_volume_accumulation_mfiratio_63v252_slope_v053_signal(closeadj, volume, high, low):
    a = _f06_money_flow(closeadj, high, low, volume, 63)
    b = _f06_money_flow(closeadj, high, low, volume, 252).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d A/D
def f06va_f06_volume_accumulation_ad_21d_slope_v054_signal(closeadj, volume, high, low):
    base = _f06_accumulation_ad(closeadj, high, low, volume, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d A/D
def f06va_f06_volume_accumulation_ad_63d_slope_v055_signal(closeadj, volume, high, low):
    base = _f06_accumulation_ad(closeadj, high, low, volume, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d A/D
def f06va_f06_volume_accumulation_ad_126d_slope_v056_signal(closeadj, volume, high, low):
    base = _f06_accumulation_ad(closeadj, high, low, volume, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d A/D
def f06va_f06_volume_accumulation_ad_252d_slope_v057_signal(closeadj, volume, high, low):
    base = _f06_accumulation_ad(closeadj, high, low, volume, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d A/D
def f06va_f06_volume_accumulation_ad_504d_slope_v058_signal(closeadj, volume, high, low):
    base = _f06_accumulation_ad(closeadj, high, low, volume, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d A/D EMA
def f06va_f06_volume_accumulation_adema_21d_slope_v059_signal(closeadj, volume, high, low):
    a = _f06_accumulation_ad(closeadj, high, low, volume, 21)
    base = a.ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d A/D EMA
def f06va_f06_volume_accumulation_adema_63d_slope_v060_signal(closeadj, volume, high, low):
    a = _f06_accumulation_ad(closeadj, high, low, volume, 63)
    base = a.ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d A/D EMA
def f06va_f06_volume_accumulation_adema_252d_slope_v061_signal(closeadj, volume, high, low):
    a = _f06_accumulation_ad(closeadj, high, low, volume, 252)
    base = a.ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d A/D z
def f06va_f06_volume_accumulation_adz_21d_slope_v062_signal(closeadj, volume, high, low):
    base = _z(_f06_accumulation_ad(closeadj, high, low, volume, 21), 252)
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d A/D z
def f06va_f06_volume_accumulation_adz_63d_slope_v063_signal(closeadj, volume, high, low):
    base = _z(_f06_accumulation_ad(closeadj, high, low, volume, 63), 252)
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d A/D z
def f06va_f06_volume_accumulation_adz_252d_slope_v064_signal(closeadj, volume, high, low):
    base = _z(_f06_accumulation_ad(closeadj, high, low, volume, 252), 504)
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of A/D diff (21-63)
def f06va_f06_volume_accumulation_addiff_21m63_slope_v065_signal(closeadj, volume, high, low):
    base = (_f06_accumulation_ad(closeadj, high, low, volume, 21) - _f06_accumulation_ad(closeadj, high, low, volume, 63)) * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of A/D diff (63-252)
def f06va_f06_volume_accumulation_addiff_63m252_slope_v066_signal(closeadj, volume, high, low):
    base = (_f06_accumulation_ad(closeadj, high, low, volume, 63) - _f06_accumulation_ad(closeadj, high, low, volume, 252)) * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of A/D diff (252-504)
def f06va_f06_volume_accumulation_addiff_252m504_slope_v067_signal(closeadj, volume, high, low):
    base = (_f06_accumulation_ad(closeadj, high, low, volume, 252) - _f06_accumulation_ad(closeadj, high, low, volume, 504)) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d obv × dollar volume
def f06va_f06_volume_accumulation_obvxdv_21d_slope_v068_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f06_accumulation_obv(closeadj, volume, 21) * _mean(dv, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d obv × dv
def f06va_f06_volume_accumulation_obvxdv_63d_slope_v069_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f06_accumulation_obv(closeadj, volume, 63) * _mean(dv, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d obv × dv
def f06va_f06_volume_accumulation_obvxdv_252d_slope_v070_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f06_accumulation_obv(closeadj, volume, 252) * _mean(dv, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d obv × volume z
def f06va_f06_volume_accumulation_obvxvolz_21d_slope_v071_signal(closeadj, volume):
    base = _f06_accumulation_obv(closeadj, volume, 21) * _z(volume, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d obv × volume z
def f06va_f06_volume_accumulation_obvxvolz_63d_slope_v072_signal(closeadj, volume):
    base = _f06_accumulation_obv(closeadj, volume, 63) * _z(volume, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d obv × volume z
def f06va_f06_volume_accumulation_obvxvolz_252d_slope_v073_signal(closeadj, volume):
    base = _f06_accumulation_obv(closeadj, volume, 252) * _z(volume, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d MFI × volume z
def f06va_f06_volume_accumulation_mfixvolz_21d_slope_v074_signal(closeadj, volume, high, low):
    base = _f06_money_flow(closeadj, high, low, volume, 21) * _z(volume, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d MFI × volume z
def f06va_f06_volume_accumulation_mfixvolz_63d_slope_v075_signal(closeadj, volume, high, low):
    base = _f06_money_flow(closeadj, high, low, volume, 63) * _z(volume, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d MFI × dv
def f06va_f06_volume_accumulation_mfixdv_252d_slope_v076_signal(closeadj, volume, high, low):
    dv = closeadj * volume
    base = _f06_money_flow(closeadj, high, low, volume, 252) * _mean(dv, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d A/D × volume z
def f06va_f06_volume_accumulation_adxvolz_21d_slope_v077_signal(closeadj, volume, high, low):
    base = _f06_accumulation_ad(closeadj, high, low, volume, 21) * _z(volume, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d A/D × volume z
def f06va_f06_volume_accumulation_adxvolz_63d_slope_v078_signal(closeadj, volume, high, low):
    base = _f06_accumulation_ad(closeadj, high, low, volume, 63) * _z(volume, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d obv × ret
def f06va_f06_volume_accumulation_obvxret_21d_slope_v079_signal(closeadj, volume):
    r21 = closeadj.pct_change(21)
    base = _f06_accumulation_obv(closeadj, volume, 21) * r21 * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d obv × ret
def f06va_f06_volume_accumulation_obvxret_63d_slope_v080_signal(closeadj, volume):
    r63 = closeadj.pct_change(63)
    base = _f06_accumulation_obv(closeadj, volume, 63) * r63 * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d obv × ret
def f06va_f06_volume_accumulation_obvxret_252d_slope_v081_signal(closeadj, volume):
    r252 = closeadj.pct_change(252)
    base = _f06_accumulation_obv(closeadj, volume, 252) * r252 * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d composite acc
def f06va_f06_volume_accumulation_acccomp_21d_slope_v082_signal(closeadj, volume, high, low):
    base = (_f06_accumulation_obv(closeadj, volume, 21) + _f06_money_flow(closeadj, high, low, volume, 21) + _f06_accumulation_ad(closeadj, high, low, volume, 21)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d composite acc
def f06va_f06_volume_accumulation_acccomp_252d_slope_v083_signal(closeadj, volume, high, low):
    base = (_f06_accumulation_obv(closeadj, volume, 252) + _f06_money_flow(closeadj, high, low, volume, 252) + _f06_accumulation_ad(closeadj, high, low, volume, 252)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d obv × rv
def f06va_f06_volume_accumulation_obvxrv_21d_slope_v084_signal(closeadj, volume):
    rv = _std(closeadj.pct_change(), 21)
    base = _f06_accumulation_obv(closeadj, volume, 21) * rv * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d obv × rv
def f06va_f06_volume_accumulation_obvxrv_63d_slope_v085_signal(closeadj, volume):
    rv = _std(closeadj.pct_change(), 63)
    base = _f06_accumulation_obv(closeadj, volume, 63) * rv * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d obv × rv
def f06va_f06_volume_accumulation_obvxrv_252d_slope_v086_signal(closeadj, volume):
    rv = _std(closeadj.pct_change(), 63)
    base = _f06_accumulation_obv(closeadj, volume, 252) * rv * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d obv / rv
def f06va_f06_volume_accumulation_obvdivrv_21d_slope_v087_signal(closeadj, volume):
    rv = _std(closeadj.pct_change(), 21).replace(0, np.nan)
    base = (_f06_accumulation_obv(closeadj, volume, 21) / rv) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d obv / rv
def f06va_f06_volume_accumulation_obvdivrv_63d_slope_v088_signal(closeadj, volume):
    rv = _std(closeadj.pct_change(), 63).replace(0, np.nan)
    base = (_f06_accumulation_obv(closeadj, volume, 63) / rv) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d obv / rv
def f06va_f06_volume_accumulation_obvdivrv_252d_slope_v089_signal(closeadj, volume):
    rv = _std(closeadj.pct_change(), 63).replace(0, np.nan)
    base = (_f06_accumulation_obv(closeadj, volume, 252) / rv) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d MFI × rv
def f06va_f06_volume_accumulation_mfixrv_21d_slope_v090_signal(closeadj, volume, high, low):
    rv = _std(closeadj.pct_change(), 21)
    base = _f06_money_flow(closeadj, high, low, volume, 21) * rv * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d MFI × rv
def f06va_f06_volume_accumulation_mfixrv_63d_slope_v091_signal(closeadj, volume, high, low):
    rv = _std(closeadj.pct_change(), 63)
    base = _f06_money_flow(closeadj, high, low, volume, 63) * rv * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d MFI × rv
def f06va_f06_volume_accumulation_mfixrv_252d_slope_v092_signal(closeadj, volume, high, low):
    rv = _std(closeadj.pct_change(), 63)
    base = _f06_money_flow(closeadj, high, low, volume, 252) * rv * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d obv × log
def f06va_f06_volume_accumulation_obvxlog_21d_slope_v093_signal(closeadj, volume):
    lg = np.log(closeadj.replace(0, np.nan).abs())
    base = _f06_accumulation_obv(closeadj, volume, 21) * lg * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d obv × log
def f06va_f06_volume_accumulation_obvxlog_63d_slope_v094_signal(closeadj, volume):
    lg = np.log(closeadj.replace(0, np.nan).abs())
    base = _f06_accumulation_obv(closeadj, volume, 63) * lg * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d obv × log
def f06va_f06_volume_accumulation_obvxlog_252d_slope_v095_signal(closeadj, volume):
    lg = np.log(closeadj.replace(0, np.nan).abs())
    base = _f06_accumulation_obv(closeadj, volume, 252) * lg * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d MFI × log
def f06va_f06_volume_accumulation_mfixlog_21d_slope_v096_signal(closeadj, volume, high, low):
    lg = np.log(closeadj.replace(0, np.nan).abs())
    base = _f06_money_flow(closeadj, high, low, volume, 21) * lg * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d MFI × log
def f06va_f06_volume_accumulation_mfixlog_63d_slope_v097_signal(closeadj, volume, high, low):
    lg = np.log(closeadj.replace(0, np.nan).abs())
    base = _f06_money_flow(closeadj, high, low, volume, 63) * lg * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d A/D × log
def f06va_f06_volume_accumulation_adxlog_21d_slope_v098_signal(closeadj, volume, high, low):
    lg = np.log(closeadj.replace(0, np.nan).abs())
    base = _f06_accumulation_ad(closeadj, high, low, volume, 21) * lg * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d A/D × log
def f06va_f06_volume_accumulation_adxlog_63d_slope_v099_signal(closeadj, volume, high, low):
    lg = np.log(closeadj.replace(0, np.nan).abs())
    base = _f06_accumulation_ad(closeadj, high, low, volume, 63) * lg * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d obv × ATR
def f06va_f06_volume_accumulation_obvxatr_21d_slope_v100_signal(closeadj, volume, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = _f06_accumulation_obv(closeadj, volume, 21) * atr
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d obv × ATR
def f06va_f06_volume_accumulation_obvxatr_63d_slope_v101_signal(closeadj, volume, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    base = _f06_accumulation_obv(closeadj, volume, 63) * atr
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d obv × ATR
def f06va_f06_volume_accumulation_obvxatr_252d_slope_v102_signal(closeadj, volume, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    base = _f06_accumulation_obv(closeadj, volume, 252) * atr
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d MFI × ATR
def f06va_f06_volume_accumulation_mfixatr_21d_slope_v103_signal(closeadj, volume, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = _f06_money_flow(closeadj, high, low, volume, 21) * atr
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d MFI × ATR
def f06va_f06_volume_accumulation_mfixatr_63d_slope_v104_signal(closeadj, volume, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    base = _f06_money_flow(closeadj, high, low, volume, 63) * atr
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d MFI × ATR
def f06va_f06_volume_accumulation_mfixatr_252d_slope_v105_signal(closeadj, volume, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    base = _f06_money_flow(closeadj, high, low, volume, 252) * atr
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d A/D × ATR
def f06va_f06_volume_accumulation_adxatr_21d_slope_v106_signal(closeadj, volume, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = _f06_accumulation_ad(closeadj, high, low, volume, 21) * atr
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d A/D × ATR
def f06va_f06_volume_accumulation_adxatr_63d_slope_v107_signal(closeadj, volume, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    base = _f06_accumulation_ad(closeadj, high, low, volume, 63) * atr
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d obv × MFI
def f06va_f06_volume_accumulation_obvxmfi_21d_slope_v108_signal(closeadj, volume, high, low):
    base = _f06_accumulation_obv(closeadj, volume, 21) * _f06_money_flow(closeadj, high, low, volume, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d obv × MFI
def f06va_f06_volume_accumulation_obvxmfi_63d_slope_v109_signal(closeadj, volume, high, low):
    base = _f06_accumulation_obv(closeadj, volume, 63) * _f06_money_flow(closeadj, high, low, volume, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d obv × MFI
def f06va_f06_volume_accumulation_obvxmfi_252d_slope_v110_signal(closeadj, volume, high, low):
    base = _f06_accumulation_obv(closeadj, volume, 252) * _f06_money_flow(closeadj, high, low, volume, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d obv × A/D
def f06va_f06_volume_accumulation_obvxad_21d_slope_v111_signal(closeadj, volume, high, low):
    base = _f06_accumulation_obv(closeadj, volume, 21) * _f06_accumulation_ad(closeadj, high, low, volume, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d obv × A/D
def f06va_f06_volume_accumulation_obvxad_63d_slope_v112_signal(closeadj, volume, high, low):
    base = _f06_accumulation_obv(closeadj, volume, 63) * _f06_accumulation_ad(closeadj, high, low, volume, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d obv × A/D
def f06va_f06_volume_accumulation_obvxad_252d_slope_v113_signal(closeadj, volume, high, low):
    base = _f06_accumulation_obv(closeadj, volume, 252) * _f06_accumulation_ad(closeadj, high, low, volume, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d MFI × A/D
def f06va_f06_volume_accumulation_mfixad_21d_slope_v114_signal(closeadj, volume, high, low):
    base = _f06_money_flow(closeadj, high, low, volume, 21) * _f06_accumulation_ad(closeadj, high, low, volume, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d MFI × A/D
def f06va_f06_volume_accumulation_mfixad_63d_slope_v115_signal(closeadj, volume, high, low):
    base = _f06_money_flow(closeadj, high, low, volume, 63) * _f06_accumulation_ad(closeadj, high, low, volume, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d MFI × A/D
def f06va_f06_volume_accumulation_mfixad_252d_slope_v116_signal(closeadj, volume, high, low):
    base = _f06_money_flow(closeadj, high, low, volume, 252) * _f06_accumulation_ad(closeadj, high, low, volume, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d A/D × dv
def f06va_f06_volume_accumulation_adxdv_21d_slope_v117_signal(closeadj, volume, high, low):
    dv = closeadj * volume
    base = _f06_accumulation_ad(closeadj, high, low, volume, 21) * dv
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d A/D × dv
def f06va_f06_volume_accumulation_adxdv_63d_slope_v118_signal(closeadj, volume, high, low):
    dv = closeadj * volume
    base = _f06_accumulation_ad(closeadj, high, low, volume, 63) * dv
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d A/D × dv
def f06va_f06_volume_accumulation_adxdv_252d_slope_v119_signal(closeadj, volume, high, low):
    dv = closeadj * volume
    base = _f06_accumulation_ad(closeadj, high, low, volume, 252) * _mean(dv, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d MFI × ret
def f06va_f06_volume_accumulation_mfixret_21d_slope_v120_signal(closeadj, volume, high, low):
    r21 = closeadj.pct_change(21)
    base = _f06_money_flow(closeadj, high, low, volume, 21) * r21 * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d MFI × ret
def f06va_f06_volume_accumulation_mfixret_63d_slope_v121_signal(closeadj, volume, high, low):
    r63 = closeadj.pct_change(63)
    base = _f06_money_flow(closeadj, high, low, volume, 63) * r63 * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d MFI × ret
def f06va_f06_volume_accumulation_mfixret_252d_slope_v122_signal(closeadj, volume, high, low):
    r252 = closeadj.pct_change(252)
    base = _f06_money_flow(closeadj, high, low, volume, 252) * r252 * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d A/D × ret
def f06va_f06_volume_accumulation_adxret_21d_slope_v123_signal(closeadj, volume, high, low):
    r21 = closeadj.pct_change(21)
    base = _f06_accumulation_ad(closeadj, high, low, volume, 21) * r21 * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d A/D × ret
def f06va_f06_volume_accumulation_adxret_63d_slope_v124_signal(closeadj, volume, high, low):
    r63 = closeadj.pct_change(63)
    base = _f06_accumulation_ad(closeadj, high, low, volume, 63) * r63 * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d A/D × ret
def f06va_f06_volume_accumulation_adxret_252d_slope_v125_signal(closeadj, volume, high, low):
    r252 = closeadj.pct_change(252)
    base = _f06_accumulation_ad(closeadj, high, low, volume, 252) * r252 * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d obv × skew
def f06va_f06_volume_accumulation_obvxskew_63d_slope_v126_signal(closeadj, volume):
    sk = closeadj.pct_change().rolling(63, min_periods=21).skew()
    base = _f06_accumulation_obv(closeadj, volume, 21) * sk * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d obv × kurt
def f06va_f06_volume_accumulation_obvxkurt_252d_slope_v127_signal(closeadj, volume):
    kt = closeadj.pct_change().rolling(252, min_periods=63).kurt()
    base = _f06_accumulation_obv(closeadj, volume, 63) * kt * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d MFI × skew
def f06va_f06_volume_accumulation_mfixskew_63d_slope_v128_signal(closeadj, volume, high, low):
    sk = closeadj.pct_change().rolling(63, min_periods=21).skew()
    base = _f06_money_flow(closeadj, high, low, volume, 21) * sk * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d obv anom
def f06va_f06_volume_accumulation_obvanom_21d_slope_v129_signal(closeadj, volume):
    o = _f06_accumulation_obv(closeadj, volume, 21)
    base = (o - _mean(o, 252)) * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d obv anom
def f06va_f06_volume_accumulation_obvanom_63d_slope_v130_signal(closeadj, volume):
    o = _f06_accumulation_obv(closeadj, volume, 63)
    base = (o - _mean(o, 252)) * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d obv anom
def f06va_f06_volume_accumulation_obvanom_252d_slope_v131_signal(closeadj, volume):
    o = _f06_accumulation_obv(closeadj, volume, 252)
    base = (o - _mean(o, 504)) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d MFI anom
def f06va_f06_volume_accumulation_mfianom_21d_slope_v132_signal(closeadj, volume, high, low):
    m = _f06_money_flow(closeadj, high, low, volume, 21)
    base = (m - _mean(m, 252)) * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d A/D anom
def f06va_f06_volume_accumulation_adanom_21d_slope_v133_signal(closeadj, volume, high, low):
    a = _f06_accumulation_ad(closeadj, high, low, volume, 21)
    base = (a - _mean(a, 252)) * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d obv × abs ret
def f06va_f06_volume_accumulation_obvxabsret_21d_slope_v134_signal(closeadj, volume):
    ar = closeadj.pct_change().abs().rolling(21, min_periods=5).mean()
    base = _f06_accumulation_obv(closeadj, volume, 21) * ar * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d obv × abs ret
def f06va_f06_volume_accumulation_obvxabsret_63d_slope_v135_signal(closeadj, volume):
    ar = closeadj.pct_change().abs().rolling(63, min_periods=21).mean()
    base = _f06_accumulation_obv(closeadj, volume, 63) * ar * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d MFI × abs ret
def f06va_f06_volume_accumulation_mfixabsret_21d_slope_v136_signal(closeadj, volume, high, low):
    ar = closeadj.pct_change().abs().rolling(21, min_periods=5).mean()
    base = _f06_money_flow(closeadj, high, low, volume, 21) * ar * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d composite acc × dv
def f06va_f06_volume_accumulation_acccompxdv_21d_slope_v137_signal(closeadj, volume, high, low):
    dv = closeadj * volume
    comp = _f06_accumulation_obv(closeadj, volume, 21) + _f06_money_flow(closeadj, high, low, volume, 21) + _f06_accumulation_ad(closeadj, high, low, volume, 21)
    base = comp * dv
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d composite acc × dv
def f06va_f06_volume_accumulation_acccompxdv_252d_slope_v138_signal(closeadj, volume, high, low):
    dv = closeadj * volume
    comp = _f06_accumulation_obv(closeadj, volume, 252) + _f06_money_flow(closeadj, high, low, volume, 252) + _f06_accumulation_ad(closeadj, high, low, volume, 252)
    base = comp * _mean(dv, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d obv sum
def f06va_f06_volume_accumulation_obvsum_63d_slope_v139_signal(closeadj, volume):
    o = _f06_accumulation_obv(closeadj, volume, 21)
    base = o.rolling(63, min_periods=21).sum() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d obv sum
def f06va_f06_volume_accumulation_obvsum_252d_slope_v140_signal(closeadj, volume):
    o = _f06_accumulation_obv(closeadj, volume, 63)
    base = o.rolling(252, min_periods=63).sum() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d MFI sum
def f06va_f06_volume_accumulation_mfisum_63d_slope_v141_signal(closeadj, volume, high, low):
    m = _f06_money_flow(closeadj, high, low, volume, 21)
    base = m.rolling(63, min_periods=21).sum() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d A/D sum
def f06va_f06_volume_accumulation_adsum_63d_slope_v142_signal(closeadj, volume, high, low):
    a = _f06_accumulation_ad(closeadj, high, low, volume, 21)
    base = a.rolling(63, min_periods=21).sum() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d obv max
def f06va_f06_volume_accumulation_obvmax_63d_slope_v143_signal(closeadj, volume):
    o = _f06_accumulation_obv(closeadj, volume, 21)
    base = o.rolling(63, min_periods=21).max() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d obv squared
def f06va_f06_volume_accumulation_obvsq_21d_slope_v144_signal(closeadj, volume):
    o = _f06_accumulation_obv(closeadj, volume, 21)
    base = o * o.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d obv squared
def f06va_f06_volume_accumulation_obvsq_63d_slope_v145_signal(closeadj, volume):
    o = _f06_accumulation_obv(closeadj, volume, 63)
    base = o * o.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d MFI squared
def f06va_f06_volume_accumulation_mfisq_21d_slope_v146_signal(closeadj, volume, high, low):
    m = _f06_money_flow(closeadj, high, low, volume, 21)
    base = m * m.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d obv × volume ratio
def f06va_f06_volume_accumulation_obvxvolratio_21d_slope_v147_signal(closeadj, volume):
    vmean = _mean(volume, 21).replace(0, np.nan)
    base = _f06_accumulation_obv(closeadj, volume, 21) * (volume / vmean) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d MFI × volume ratio
def f06va_f06_volume_accumulation_mfixvolratio_252d_slope_v148_signal(closeadj, volume, high, low):
    vmean = _mean(volume, 252).replace(0, np.nan)
    base = _f06_money_flow(closeadj, high, low, volume, 252) * (volume / vmean) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d obv × hl spread
def f06va_f06_volume_accumulation_obvxhlspread_21d_slope_v149_signal(closeadj, volume, high, low):
    sp = (high - low) / closeadj.replace(0, np.nan)
    base = _f06_accumulation_obv(closeadj, volume, 21) * sp * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d MFI EMA × volume z
def f06va_f06_volume_accumulation_mfiemaxvolz_21d_slope_v150_signal(closeadj, volume, high, low):
    m = _f06_money_flow(closeadj, high, low, volume, 21)
    e = m.ewm(span=21, adjust=False).mean()
    base = e * _z(volume, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f06va_f06_volume_accumulation_obv_21d_slope_v001_signal,
    f06va_f06_volume_accumulation_obv_21d_slope_v002_signal,
    f06va_f06_volume_accumulation_obv_63d_slope_v003_signal,
    f06va_f06_volume_accumulation_obv_63d_slope_v004_signal,
    f06va_f06_volume_accumulation_obv_63d_slope_v005_signal,
    f06va_f06_volume_accumulation_obv_126d_slope_v006_signal,
    f06va_f06_volume_accumulation_obv_126d_slope_v007_signal,
    f06va_f06_volume_accumulation_obv_252d_slope_v008_signal,
    f06va_f06_volume_accumulation_obv_252d_slope_v009_signal,
    f06va_f06_volume_accumulation_obv_504d_slope_v010_signal,
    f06va_f06_volume_accumulation_obv_504d_slope_v011_signal,
    f06va_f06_volume_accumulation_obv_5d_slope_v012_signal,
    f06va_f06_volume_accumulation_obv_10d_slope_v013_signal,
    f06va_f06_volume_accumulation_obv_42d_slope_v014_signal,
    f06va_f06_volume_accumulation_obv_189d_slope_v015_signal,
    f06va_f06_volume_accumulation_obv_378d_slope_v016_signal,
    f06va_f06_volume_accumulation_obvema_21d_slope_v017_signal,
    f06va_f06_volume_accumulation_obvema_63d_slope_v018_signal,
    f06va_f06_volume_accumulation_obvema_252d_slope_v019_signal,
    f06va_f06_volume_accumulation_obvz_21d_slope_v020_signal,
    f06va_f06_volume_accumulation_obvz_63d_slope_v021_signal,
    f06va_f06_volume_accumulation_obvz_252d_slope_v022_signal,
    f06va_f06_volume_accumulation_obvstd_21d_slope_v023_signal,
    f06va_f06_volume_accumulation_obvstd_63d_slope_v024_signal,
    f06va_f06_volume_accumulation_obvstd_252d_slope_v025_signal,
    f06va_f06_volume_accumulation_obvdiff_21m63_slope_v026_signal,
    f06va_f06_volume_accumulation_obvdiff_63m252_slope_v027_signal,
    f06va_f06_volume_accumulation_obvdiff_252m504_slope_v028_signal,
    f06va_f06_volume_accumulation_obvratio_21v63_slope_v029_signal,
    f06va_f06_volume_accumulation_obvratio_63v252_slope_v030_signal,
    f06va_f06_volume_accumulation_mfi_21d_slope_v031_signal,
    f06va_f06_volume_accumulation_mfi_21d_slope_v032_signal,
    f06va_f06_volume_accumulation_mfi_63d_slope_v033_signal,
    f06va_f06_volume_accumulation_mfi_63d_slope_v034_signal,
    f06va_f06_volume_accumulation_mfi_126d_slope_v035_signal,
    f06va_f06_volume_accumulation_mfi_252d_slope_v036_signal,
    f06va_f06_volume_accumulation_mfi_504d_slope_v037_signal,
    f06va_f06_volume_accumulation_mfi_5d_slope_v038_signal,
    f06va_f06_volume_accumulation_mfi_10d_slope_v039_signal,
    f06va_f06_volume_accumulation_mfi_42d_slope_v040_signal,
    f06va_f06_volume_accumulation_mfi_189d_slope_v041_signal,
    f06va_f06_volume_accumulation_mfi_378d_slope_v042_signal,
    f06va_f06_volume_accumulation_mfiema_21d_slope_v043_signal,
    f06va_f06_volume_accumulation_mfiema_63d_slope_v044_signal,
    f06va_f06_volume_accumulation_mfiema_252d_slope_v045_signal,
    f06va_f06_volume_accumulation_mfiz_21d_slope_v046_signal,
    f06va_f06_volume_accumulation_mfiz_63d_slope_v047_signal,
    f06va_f06_volume_accumulation_mfiz_252d_slope_v048_signal,
    f06va_f06_volume_accumulation_mfidiff_21m63_slope_v049_signal,
    f06va_f06_volume_accumulation_mfidiff_63m252_slope_v050_signal,
    f06va_f06_volume_accumulation_mfidiff_252m504_slope_v051_signal,
    f06va_f06_volume_accumulation_mfiratio_21v63_slope_v052_signal,
    f06va_f06_volume_accumulation_mfiratio_63v252_slope_v053_signal,
    f06va_f06_volume_accumulation_ad_21d_slope_v054_signal,
    f06va_f06_volume_accumulation_ad_63d_slope_v055_signal,
    f06va_f06_volume_accumulation_ad_126d_slope_v056_signal,
    f06va_f06_volume_accumulation_ad_252d_slope_v057_signal,
    f06va_f06_volume_accumulation_ad_504d_slope_v058_signal,
    f06va_f06_volume_accumulation_adema_21d_slope_v059_signal,
    f06va_f06_volume_accumulation_adema_63d_slope_v060_signal,
    f06va_f06_volume_accumulation_adema_252d_slope_v061_signal,
    f06va_f06_volume_accumulation_adz_21d_slope_v062_signal,
    f06va_f06_volume_accumulation_adz_63d_slope_v063_signal,
    f06va_f06_volume_accumulation_adz_252d_slope_v064_signal,
    f06va_f06_volume_accumulation_addiff_21m63_slope_v065_signal,
    f06va_f06_volume_accumulation_addiff_63m252_slope_v066_signal,
    f06va_f06_volume_accumulation_addiff_252m504_slope_v067_signal,
    f06va_f06_volume_accumulation_obvxdv_21d_slope_v068_signal,
    f06va_f06_volume_accumulation_obvxdv_63d_slope_v069_signal,
    f06va_f06_volume_accumulation_obvxdv_252d_slope_v070_signal,
    f06va_f06_volume_accumulation_obvxvolz_21d_slope_v071_signal,
    f06va_f06_volume_accumulation_obvxvolz_63d_slope_v072_signal,
    f06va_f06_volume_accumulation_obvxvolz_252d_slope_v073_signal,
    f06va_f06_volume_accumulation_mfixvolz_21d_slope_v074_signal,
    f06va_f06_volume_accumulation_mfixvolz_63d_slope_v075_signal,
    f06va_f06_volume_accumulation_mfixdv_252d_slope_v076_signal,
    f06va_f06_volume_accumulation_adxvolz_21d_slope_v077_signal,
    f06va_f06_volume_accumulation_adxvolz_63d_slope_v078_signal,
    f06va_f06_volume_accumulation_obvxret_21d_slope_v079_signal,
    f06va_f06_volume_accumulation_obvxret_63d_slope_v080_signal,
    f06va_f06_volume_accumulation_obvxret_252d_slope_v081_signal,
    f06va_f06_volume_accumulation_acccomp_21d_slope_v082_signal,
    f06va_f06_volume_accumulation_acccomp_252d_slope_v083_signal,
    f06va_f06_volume_accumulation_obvxrv_21d_slope_v084_signal,
    f06va_f06_volume_accumulation_obvxrv_63d_slope_v085_signal,
    f06va_f06_volume_accumulation_obvxrv_252d_slope_v086_signal,
    f06va_f06_volume_accumulation_obvdivrv_21d_slope_v087_signal,
    f06va_f06_volume_accumulation_obvdivrv_63d_slope_v088_signal,
    f06va_f06_volume_accumulation_obvdivrv_252d_slope_v089_signal,
    f06va_f06_volume_accumulation_mfixrv_21d_slope_v090_signal,
    f06va_f06_volume_accumulation_mfixrv_63d_slope_v091_signal,
    f06va_f06_volume_accumulation_mfixrv_252d_slope_v092_signal,
    f06va_f06_volume_accumulation_obvxlog_21d_slope_v093_signal,
    f06va_f06_volume_accumulation_obvxlog_63d_slope_v094_signal,
    f06va_f06_volume_accumulation_obvxlog_252d_slope_v095_signal,
    f06va_f06_volume_accumulation_mfixlog_21d_slope_v096_signal,
    f06va_f06_volume_accumulation_mfixlog_63d_slope_v097_signal,
    f06va_f06_volume_accumulation_adxlog_21d_slope_v098_signal,
    f06va_f06_volume_accumulation_adxlog_63d_slope_v099_signal,
    f06va_f06_volume_accumulation_obvxatr_21d_slope_v100_signal,
    f06va_f06_volume_accumulation_obvxatr_63d_slope_v101_signal,
    f06va_f06_volume_accumulation_obvxatr_252d_slope_v102_signal,
    f06va_f06_volume_accumulation_mfixatr_21d_slope_v103_signal,
    f06va_f06_volume_accumulation_mfixatr_63d_slope_v104_signal,
    f06va_f06_volume_accumulation_mfixatr_252d_slope_v105_signal,
    f06va_f06_volume_accumulation_adxatr_21d_slope_v106_signal,
    f06va_f06_volume_accumulation_adxatr_63d_slope_v107_signal,
    f06va_f06_volume_accumulation_obvxmfi_21d_slope_v108_signal,
    f06va_f06_volume_accumulation_obvxmfi_63d_slope_v109_signal,
    f06va_f06_volume_accumulation_obvxmfi_252d_slope_v110_signal,
    f06va_f06_volume_accumulation_obvxad_21d_slope_v111_signal,
    f06va_f06_volume_accumulation_obvxad_63d_slope_v112_signal,
    f06va_f06_volume_accumulation_obvxad_252d_slope_v113_signal,
    f06va_f06_volume_accumulation_mfixad_21d_slope_v114_signal,
    f06va_f06_volume_accumulation_mfixad_63d_slope_v115_signal,
    f06va_f06_volume_accumulation_mfixad_252d_slope_v116_signal,
    f06va_f06_volume_accumulation_adxdv_21d_slope_v117_signal,
    f06va_f06_volume_accumulation_adxdv_63d_slope_v118_signal,
    f06va_f06_volume_accumulation_adxdv_252d_slope_v119_signal,
    f06va_f06_volume_accumulation_mfixret_21d_slope_v120_signal,
    f06va_f06_volume_accumulation_mfixret_63d_slope_v121_signal,
    f06va_f06_volume_accumulation_mfixret_252d_slope_v122_signal,
    f06va_f06_volume_accumulation_adxret_21d_slope_v123_signal,
    f06va_f06_volume_accumulation_adxret_63d_slope_v124_signal,
    f06va_f06_volume_accumulation_adxret_252d_slope_v125_signal,
    f06va_f06_volume_accumulation_obvxskew_63d_slope_v126_signal,
    f06va_f06_volume_accumulation_obvxkurt_252d_slope_v127_signal,
    f06va_f06_volume_accumulation_mfixskew_63d_slope_v128_signal,
    f06va_f06_volume_accumulation_obvanom_21d_slope_v129_signal,
    f06va_f06_volume_accumulation_obvanom_63d_slope_v130_signal,
    f06va_f06_volume_accumulation_obvanom_252d_slope_v131_signal,
    f06va_f06_volume_accumulation_mfianom_21d_slope_v132_signal,
    f06va_f06_volume_accumulation_adanom_21d_slope_v133_signal,
    f06va_f06_volume_accumulation_obvxabsret_21d_slope_v134_signal,
    f06va_f06_volume_accumulation_obvxabsret_63d_slope_v135_signal,
    f06va_f06_volume_accumulation_mfixabsret_21d_slope_v136_signal,
    f06va_f06_volume_accumulation_acccompxdv_21d_slope_v137_signal,
    f06va_f06_volume_accumulation_acccompxdv_252d_slope_v138_signal,
    f06va_f06_volume_accumulation_obvsum_63d_slope_v139_signal,
    f06va_f06_volume_accumulation_obvsum_252d_slope_v140_signal,
    f06va_f06_volume_accumulation_mfisum_63d_slope_v141_signal,
    f06va_f06_volume_accumulation_adsum_63d_slope_v142_signal,
    f06va_f06_volume_accumulation_obvmax_63d_slope_v143_signal,
    f06va_f06_volume_accumulation_obvsq_21d_slope_v144_signal,
    f06va_f06_volume_accumulation_obvsq_63d_slope_v145_signal,
    f06va_f06_volume_accumulation_mfisq_21d_slope_v146_signal,
    f06va_f06_volume_accumulation_obvxvolratio_21d_slope_v147_signal,
    f06va_f06_volume_accumulation_mfixvolratio_252d_slope_v148_signal,
    f06va_f06_volume_accumulation_obvxhlspread_21d_slope_v149_signal,
    f06va_f06_volume_accumulation_mfiemaxvolz_21d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F06_VOLUME_ACCUMULATION_REGISTRY_SLOPE = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f06_volume_accumulation_2nd_derivatives_001_150_claude: {n_features} features pass")
