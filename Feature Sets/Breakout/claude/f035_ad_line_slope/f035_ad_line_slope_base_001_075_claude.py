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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f035_ad_line(high, low, closeadj, volume):
    rng = (high - low).replace(0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    return (clv.fillna(0.0) * volume).cumsum()


def _f035_ad_slope(high, low, closeadj, volume, w):
    rng = (high - low).replace(0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv.fillna(0.0) * volume).cumsum()
    return ad.diff(w) / ad.abs().replace(0, np.nan)


def _f035_chaikin_trend(high, low, closeadj, volume, w):
    rng = (high - low).replace(0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv.fillna(0.0) * volume).cumsum()
    fast = ad.ewm(span=max(3, w // 4), adjust=False).mean()
    slow = ad.ewm(span=w, adjust=False).mean()
    return (fast - slow) / ad.abs().replace(0, np.nan).rolling(w, min_periods=max(1, w // 2)).mean()


def f035ads_f035_ad_line_slope_adslope_5d_base_v001_signal(high, low, closeadj, volume):
    result = _f035_ad_slope(high, low, closeadj, volume, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adslope_10d_base_v002_signal(high, low, closeadj, volume):
    result = _f035_ad_slope(high, low, closeadj, volume, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adslope_21d_base_v003_signal(high, low, closeadj, volume):
    result = _f035_ad_slope(high, low, closeadj, volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adslope_42d_base_v004_signal(high, low, closeadj, volume):
    result = _f035_ad_slope(high, low, closeadj, volume, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adslope_63d_base_v005_signal(high, low, closeadj, volume):
    result = _f035_ad_slope(high, low, closeadj, volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adslope_126d_base_v006_signal(high, low, closeadj, volume):
    result = _f035_ad_slope(high, low, closeadj, volume, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adslope_189d_base_v007_signal(high, low, closeadj, volume):
    result = _f035_ad_slope(high, low, closeadj, volume, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adslope_252d_base_v008_signal(high, low, closeadj, volume):
    result = _f035_ad_slope(high, low, closeadj, volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adslope_378d_base_v009_signal(high, low, closeadj, volume):
    result = _f035_ad_slope(high, low, closeadj, volume, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adslope_504d_base_v010_signal(high, low, closeadj, volume):
    result = _f035_ad_slope(high, low, closeadj, volume, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_chaikin_5d_base_v011_signal(high, low, closeadj, volume):
    result = _f035_chaikin_trend(high, low, closeadj, volume, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_chaikin_10d_base_v012_signal(high, low, closeadj, volume):
    result = _f035_chaikin_trend(high, low, closeadj, volume, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_chaikin_21d_base_v013_signal(high, low, closeadj, volume):
    result = _f035_chaikin_trend(high, low, closeadj, volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_chaikin_42d_base_v014_signal(high, low, closeadj, volume):
    result = _f035_chaikin_trend(high, low, closeadj, volume, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_chaikin_63d_base_v015_signal(high, low, closeadj, volume):
    result = _f035_chaikin_trend(high, low, closeadj, volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_chaikin_126d_base_v016_signal(high, low, closeadj, volume):
    result = _f035_chaikin_trend(high, low, closeadj, volume, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_chaikin_189d_base_v017_signal(high, low, closeadj, volume):
    result = _f035_chaikin_trend(high, low, closeadj, volume, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_chaikin_252d_base_v018_signal(high, low, closeadj, volume):
    result = _f035_chaikin_trend(high, low, closeadj, volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_chaikin_378d_base_v019_signal(high, low, closeadj, volume):
    result = _f035_chaikin_trend(high, low, closeadj, volume, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_chaikin_504d_base_v020_signal(high, low, closeadj, volume):
    result = _f035_chaikin_trend(high, low, closeadj, volume, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adlinez_5d_base_v021_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    result = _z(ad, 21) * closeadj * np.log(5 + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adlinez_10d_base_v022_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    result = _z(ad, 21) * closeadj * np.log(10 + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adlinez_21d_base_v023_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    result = _z(ad, 21) * closeadj * np.log(21 + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adlinez_42d_base_v024_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    result = _z(ad, 63) * closeadj * np.log(42 + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adlinez_63d_base_v025_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    result = _z(ad, 63) * closeadj * np.log(63 + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adlinez_126d_base_v026_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    result = _z(ad, 126) * closeadj * np.log(126 + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adlinez_189d_base_v027_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    result = _z(ad, 252) * closeadj * np.log(189 + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adlinez_252d_base_v028_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    result = _z(ad, 252) * closeadj * np.log(252 + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adlinez_378d_base_v029_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    result = _z(ad, 504) * closeadj * np.log(378 + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adlinez_504d_base_v030_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    result = _z(ad, 504) * closeadj * np.log(504 + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_smadslope_5d_base_v031_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 5)
    result = _mean(sl, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_smadslope_10d_base_v032_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 10)
    result = _mean(sl, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_smadslope_21d_base_v033_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 21)
    result = _mean(sl, 7) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_smadslope_42d_base_v034_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 42)
    result = _mean(sl, 14) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_smadslope_63d_base_v035_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 63)
    result = _mean(sl, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_smadslope_126d_base_v036_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 126)
    result = _mean(sl, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_smadslope_189d_base_v037_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 189)
    result = _mean(sl, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_smadslope_252d_base_v038_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 252)
    result = _mean(sl, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_smadslope_378d_base_v039_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 378)
    result = _mean(sl, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_smadslope_504d_base_v040_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 504)
    result = _mean(sl, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_zadslope_5d_base_v041_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 5)
    result = _z(sl, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_zadslope_10d_base_v042_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 10)
    result = _z(sl, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_zadslope_21d_base_v043_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 21)
    result = _z(sl, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_zadslope_42d_base_v044_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 42)
    result = _z(sl, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_zadslope_63d_base_v045_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 63)
    result = _z(sl, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_zadslope_126d_base_v046_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 126)
    result = _z(sl, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_zadslope_189d_base_v047_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 189)
    result = _z(sl, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_zadslope_252d_base_v048_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 252)
    result = _z(sl, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_zadslope_378d_base_v049_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 378)
    result = _z(sl, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_zadslope_504d_base_v050_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 504)
    result = _z(sl, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_stdadslope_5d_base_v051_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 5)
    result = _std(sl, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_stdadslope_10d_base_v052_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 10)
    result = _std(sl, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_stdadslope_21d_base_v053_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 21)
    result = _std(sl, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_stdadslope_42d_base_v054_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 42)
    result = _std(sl, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_stdadslope_63d_base_v055_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 63)
    result = _std(sl, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_stdadslope_126d_base_v056_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 126)
    result = _std(sl, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_stdadslope_189d_base_v057_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 189)
    result = _std(sl, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_stdadslope_252d_base_v058_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 252)
    result = _std(sl, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_stdadslope_378d_base_v059_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 378)
    result = _std(sl, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_stdadslope_504d_base_v060_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 504)
    result = _std(sl, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_smchaikin_5d_base_v061_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 5)
    result = _mean(c, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_smchaikin_10d_base_v062_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 10)
    result = _mean(c, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_smchaikin_21d_base_v063_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 21)
    result = _mean(c, 7) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_smchaikin_42d_base_v064_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 42)
    result = _mean(c, 14) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_smchaikin_63d_base_v065_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 63)
    result = _mean(c, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_smchaikin_126d_base_v066_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 126)
    result = _mean(c, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_smchaikin_189d_base_v067_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 189)
    result = _mean(c, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_smchaikin_252d_base_v068_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 252)
    result = _mean(c, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_smchaikin_378d_base_v069_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 378)
    result = _mean(c, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_smchaikin_504d_base_v070_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 504)
    result = _mean(c, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_zchaikin_5d_base_v071_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 5)
    result = _z(c, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_zchaikin_10d_base_v072_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 10)
    result = _z(c, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_zchaikin_21d_base_v073_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 21)
    result = _z(c, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_zchaikin_42d_base_v074_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 42)
    result = _z(c, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_zchaikin_63d_base_v075_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 63)
    result = _z(c, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f035ads_f035_ad_line_slope_adslope_5d_base_v001_signal,
    f035ads_f035_ad_line_slope_adslope_10d_base_v002_signal,
    f035ads_f035_ad_line_slope_adslope_21d_base_v003_signal,
    f035ads_f035_ad_line_slope_adslope_42d_base_v004_signal,
    f035ads_f035_ad_line_slope_adslope_63d_base_v005_signal,
    f035ads_f035_ad_line_slope_adslope_126d_base_v006_signal,
    f035ads_f035_ad_line_slope_adslope_189d_base_v007_signal,
    f035ads_f035_ad_line_slope_adslope_252d_base_v008_signal,
    f035ads_f035_ad_line_slope_adslope_378d_base_v009_signal,
    f035ads_f035_ad_line_slope_adslope_504d_base_v010_signal,
    f035ads_f035_ad_line_slope_chaikin_5d_base_v011_signal,
    f035ads_f035_ad_line_slope_chaikin_10d_base_v012_signal,
    f035ads_f035_ad_line_slope_chaikin_21d_base_v013_signal,
    f035ads_f035_ad_line_slope_chaikin_42d_base_v014_signal,
    f035ads_f035_ad_line_slope_chaikin_63d_base_v015_signal,
    f035ads_f035_ad_line_slope_chaikin_126d_base_v016_signal,
    f035ads_f035_ad_line_slope_chaikin_189d_base_v017_signal,
    f035ads_f035_ad_line_slope_chaikin_252d_base_v018_signal,
    f035ads_f035_ad_line_slope_chaikin_378d_base_v019_signal,
    f035ads_f035_ad_line_slope_chaikin_504d_base_v020_signal,
    f035ads_f035_ad_line_slope_adlinez_5d_base_v021_signal,
    f035ads_f035_ad_line_slope_adlinez_10d_base_v022_signal,
    f035ads_f035_ad_line_slope_adlinez_21d_base_v023_signal,
    f035ads_f035_ad_line_slope_adlinez_42d_base_v024_signal,
    f035ads_f035_ad_line_slope_adlinez_63d_base_v025_signal,
    f035ads_f035_ad_line_slope_adlinez_126d_base_v026_signal,
    f035ads_f035_ad_line_slope_adlinez_189d_base_v027_signal,
    f035ads_f035_ad_line_slope_adlinez_252d_base_v028_signal,
    f035ads_f035_ad_line_slope_adlinez_378d_base_v029_signal,
    f035ads_f035_ad_line_slope_adlinez_504d_base_v030_signal,
    f035ads_f035_ad_line_slope_smadslope_5d_base_v031_signal,
    f035ads_f035_ad_line_slope_smadslope_10d_base_v032_signal,
    f035ads_f035_ad_line_slope_smadslope_21d_base_v033_signal,
    f035ads_f035_ad_line_slope_smadslope_42d_base_v034_signal,
    f035ads_f035_ad_line_slope_smadslope_63d_base_v035_signal,
    f035ads_f035_ad_line_slope_smadslope_126d_base_v036_signal,
    f035ads_f035_ad_line_slope_smadslope_189d_base_v037_signal,
    f035ads_f035_ad_line_slope_smadslope_252d_base_v038_signal,
    f035ads_f035_ad_line_slope_smadslope_378d_base_v039_signal,
    f035ads_f035_ad_line_slope_smadslope_504d_base_v040_signal,
    f035ads_f035_ad_line_slope_zadslope_5d_base_v041_signal,
    f035ads_f035_ad_line_slope_zadslope_10d_base_v042_signal,
    f035ads_f035_ad_line_slope_zadslope_21d_base_v043_signal,
    f035ads_f035_ad_line_slope_zadslope_42d_base_v044_signal,
    f035ads_f035_ad_line_slope_zadslope_63d_base_v045_signal,
    f035ads_f035_ad_line_slope_zadslope_126d_base_v046_signal,
    f035ads_f035_ad_line_slope_zadslope_189d_base_v047_signal,
    f035ads_f035_ad_line_slope_zadslope_252d_base_v048_signal,
    f035ads_f035_ad_line_slope_zadslope_378d_base_v049_signal,
    f035ads_f035_ad_line_slope_zadslope_504d_base_v050_signal,
    f035ads_f035_ad_line_slope_stdadslope_5d_base_v051_signal,
    f035ads_f035_ad_line_slope_stdadslope_10d_base_v052_signal,
    f035ads_f035_ad_line_slope_stdadslope_21d_base_v053_signal,
    f035ads_f035_ad_line_slope_stdadslope_42d_base_v054_signal,
    f035ads_f035_ad_line_slope_stdadslope_63d_base_v055_signal,
    f035ads_f035_ad_line_slope_stdadslope_126d_base_v056_signal,
    f035ads_f035_ad_line_slope_stdadslope_189d_base_v057_signal,
    f035ads_f035_ad_line_slope_stdadslope_252d_base_v058_signal,
    f035ads_f035_ad_line_slope_stdadslope_378d_base_v059_signal,
    f035ads_f035_ad_line_slope_stdadslope_504d_base_v060_signal,
    f035ads_f035_ad_line_slope_smchaikin_5d_base_v061_signal,
    f035ads_f035_ad_line_slope_smchaikin_10d_base_v062_signal,
    f035ads_f035_ad_line_slope_smchaikin_21d_base_v063_signal,
    f035ads_f035_ad_line_slope_smchaikin_42d_base_v064_signal,
    f035ads_f035_ad_line_slope_smchaikin_63d_base_v065_signal,
    f035ads_f035_ad_line_slope_smchaikin_126d_base_v066_signal,
    f035ads_f035_ad_line_slope_smchaikin_189d_base_v067_signal,
    f035ads_f035_ad_line_slope_smchaikin_252d_base_v068_signal,
    f035ads_f035_ad_line_slope_smchaikin_378d_base_v069_signal,
    f035ads_f035_ad_line_slope_smchaikin_504d_base_v070_signal,
    f035ads_f035_ad_line_slope_zchaikin_5d_base_v071_signal,
    f035ads_f035_ad_line_slope_zchaikin_10d_base_v072_signal,
    f035ads_f035_ad_line_slope_zchaikin_21d_base_v073_signal,
    f035ads_f035_ad_line_slope_zchaikin_42d_base_v074_signal,
    f035ads_f035_ad_line_slope_zchaikin_63d_base_v075_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F035_AD_LINE_SLOPE_REGISTRY_001_075 = REGISTRY


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
    domain_primitives = ('_f035_ad_line', '_f035_ad_slope', '_f035_chaikin_trend')
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
    print(f"OK f035_ad_line_slope_base_001_075_claude: {n_features} features pass")
