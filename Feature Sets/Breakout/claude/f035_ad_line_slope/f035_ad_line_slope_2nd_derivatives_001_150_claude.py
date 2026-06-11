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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


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


def f035ads_f035_ad_line_slope_adslope_21d_slope_v001_signal(high, low, closeadj, volume):
    base = _f035_ad_slope(high, low, closeadj, volume, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adslope_21d_slope_v002_signal(high, low, closeadj, volume):
    base = _f035_ad_slope(high, low, closeadj, volume, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adslope_63d_slope_v003_signal(high, low, closeadj, volume):
    base = _f035_ad_slope(high, low, closeadj, volume, 63) * closeadj
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adslope_63d_slope_v004_signal(high, low, closeadj, volume):
    base = _f035_ad_slope(high, low, closeadj, volume, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adslope_126d_slope_v005_signal(high, low, closeadj, volume):
    base = _f035_ad_slope(high, low, closeadj, volume, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adslope_126d_slope_v006_signal(high, low, closeadj, volume):
    base = _f035_ad_slope(high, low, closeadj, volume, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adslope_252d_slope_v007_signal(high, low, closeadj, volume):
    base = _f035_ad_slope(high, low, closeadj, volume, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adslope_252d_slope_v008_signal(high, low, closeadj, volume):
    base = _f035_ad_slope(high, low, closeadj, volume, 252) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adslope_252d_slope_v009_signal(high, low, closeadj, volume):
    base = _f035_ad_slope(high, low, closeadj, volume, 252) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adslope_252d_slope_v010_signal(high, low, closeadj, volume):
    base = _f035_ad_slope(high, low, closeadj, volume, 252) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_chaikin_21d_slope_v011_signal(high, low, closeadj, volume):
    base = _f035_chaikin_trend(high, low, closeadj, volume, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_chaikin_21d_slope_v012_signal(high, low, closeadj, volume):
    base = _f035_chaikin_trend(high, low, closeadj, volume, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_chaikin_63d_slope_v013_signal(high, low, closeadj, volume):
    base = _f035_chaikin_trend(high, low, closeadj, volume, 63) * closeadj
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_chaikin_63d_slope_v014_signal(high, low, closeadj, volume):
    base = _f035_chaikin_trend(high, low, closeadj, volume, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_chaikin_126d_slope_v015_signal(high, low, closeadj, volume):
    base = _f035_chaikin_trend(high, low, closeadj, volume, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_chaikin_126d_slope_v016_signal(high, low, closeadj, volume):
    base = _f035_chaikin_trend(high, low, closeadj, volume, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_chaikin_252d_slope_v017_signal(high, low, closeadj, volume):
    base = _f035_chaikin_trend(high, low, closeadj, volume, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_chaikin_252d_slope_v018_signal(high, low, closeadj, volume):
    base = _f035_chaikin_trend(high, low, closeadj, volume, 252) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_chaikin_252d_slope_v019_signal(high, low, closeadj, volume):
    base = _f035_chaikin_trend(high, low, closeadj, volume, 252) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_chaikin_252d_slope_v020_signal(high, low, closeadj, volume):
    base = _f035_chaikin_trend(high, low, closeadj, volume, 252) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adlinez_21d_slope_v021_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    base = _z(ad, 21) * closeadj * np.log(21 + 1.0)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adlinez_21d_slope_v022_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    base = _z(ad, 21) * closeadj * np.log(21 + 1.0)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adlinez_63d_slope_v023_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    base = _z(ad, 63) * closeadj * np.log(63 + 1.0)
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adlinez_63d_slope_v024_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    base = _z(ad, 63) * closeadj * np.log(63 + 1.0)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adlinez_126d_slope_v025_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    base = _z(ad, 126) * closeadj * np.log(126 + 1.0)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adlinez_126d_slope_v026_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    base = _z(ad, 126) * closeadj * np.log(126 + 1.0)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adlinez_252d_slope_v027_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    base = _z(ad, 252) * closeadj * np.log(252 + 1.0)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adlinez_252d_slope_v028_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    base = _z(ad, 252) * closeadj * np.log(252 + 1.0)
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adlinez_252d_slope_v029_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    base = _z(ad, 252) * closeadj * np.log(252 + 1.0)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adlinez_252d_slope_v030_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    base = _z(ad, 252) * closeadj * np.log(252 + 1.0)
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_smadslope_21d_slope_v031_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 21)
    base = _mean(sl, 7) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_smadslope_21d_slope_v032_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 21)
    base = _mean(sl, 7) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_smadslope_63d_slope_v033_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 63)
    base = _mean(sl, 21) * closeadj
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_smadslope_63d_slope_v034_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 63)
    base = _mean(sl, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_smadslope_126d_slope_v035_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 126)
    base = _mean(sl, 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_smadslope_126d_slope_v036_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 126)
    base = _mean(sl, 42) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_smadslope_252d_slope_v037_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 252)
    base = _mean(sl, 84) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_smadslope_252d_slope_v038_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 252)
    base = _mean(sl, 84) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_smadslope_252d_slope_v039_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 252)
    base = _mean(sl, 84) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_smadslope_252d_slope_v040_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 252)
    base = _mean(sl, 84) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_zadslope_21d_slope_v041_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 21)
    base = _z(sl, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_zadslope_21d_slope_v042_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 21)
    base = _z(sl, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_zadslope_63d_slope_v043_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 63)
    base = _z(sl, 63) * closeadj
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_zadslope_63d_slope_v044_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 63)
    base = _z(sl, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_zadslope_126d_slope_v045_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 126)
    base = _z(sl, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_zadslope_126d_slope_v046_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 126)
    base = _z(sl, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_zadslope_252d_slope_v047_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 252)
    base = _z(sl, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_zadslope_252d_slope_v048_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 252)
    base = _z(sl, 252) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_zadslope_252d_slope_v049_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 252)
    base = _z(sl, 252) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_zadslope_252d_slope_v050_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 252)
    base = _z(sl, 252) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_stdadslope_21d_slope_v051_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 21)
    base = _std(sl, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_stdadslope_21d_slope_v052_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 21)
    base = _std(sl, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_stdadslope_63d_slope_v053_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 63)
    base = _std(sl, 63) * closeadj
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_stdadslope_63d_slope_v054_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 63)
    base = _std(sl, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_stdadslope_126d_slope_v055_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 126)
    base = _std(sl, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_stdadslope_126d_slope_v056_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 126)
    base = _std(sl, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_stdadslope_252d_slope_v057_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 252)
    base = _std(sl, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_stdadslope_252d_slope_v058_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 252)
    base = _std(sl, 252) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_stdadslope_252d_slope_v059_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 252)
    base = _std(sl, 252) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_stdadslope_252d_slope_v060_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 252)
    base = _std(sl, 252) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_smchaikin_21d_slope_v061_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 21)
    base = _mean(c, 7) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_smchaikin_21d_slope_v062_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 21)
    base = _mean(c, 7) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_smchaikin_63d_slope_v063_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 63)
    base = _mean(c, 21) * closeadj
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_smchaikin_63d_slope_v064_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 63)
    base = _mean(c, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_smchaikin_126d_slope_v065_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 126)
    base = _mean(c, 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_smchaikin_126d_slope_v066_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 126)
    base = _mean(c, 42) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_smchaikin_252d_slope_v067_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 252)
    base = _mean(c, 84) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_smchaikin_252d_slope_v068_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 252)
    base = _mean(c, 84) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_smchaikin_252d_slope_v069_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 252)
    base = _mean(c, 84) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_smchaikin_252d_slope_v070_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 252)
    base = _mean(c, 84) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_zchaikin_21d_slope_v071_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 21)
    base = _z(c, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_zchaikin_21d_slope_v072_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 21)
    base = _z(c, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_zchaikin_63d_slope_v073_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 63)
    base = _z(c, 63) * closeadj
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_zchaikin_63d_slope_v074_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 63)
    base = _z(c, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_zchaikin_126d_slope_v075_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 126)
    base = _z(c, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_zchaikin_126d_slope_v076_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 126)
    base = _z(c, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_zchaikin_252d_slope_v077_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 252)
    base = _z(c, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_zchaikin_252d_slope_v078_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 252)
    base = _z(c, 252) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_zchaikin_252d_slope_v079_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 252)
    base = _z(c, 252) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_zchaikin_252d_slope_v080_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 252)
    base = _z(c, 252) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adlineband_21d_slope_v081_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    m = _mean(ad, 21)
    base = (ad - m) / ad.abs().rolling(21, min_periods=5).mean().replace(0, np.nan) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adlineband_21d_slope_v082_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    m = _mean(ad, 21)
    base = (ad - m) / ad.abs().rolling(21, min_periods=5).mean().replace(0, np.nan) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adlineband_63d_slope_v083_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    m = _mean(ad, 63)
    base = (ad - m) / ad.abs().rolling(63, min_periods=15).mean().replace(0, np.nan) * closeadj
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adlineband_63d_slope_v084_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    m = _mean(ad, 63)
    base = (ad - m) / ad.abs().rolling(63, min_periods=15).mean().replace(0, np.nan) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adlineband_126d_slope_v085_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    m = _mean(ad, 126)
    base = (ad - m) / ad.abs().rolling(126, min_periods=31).mean().replace(0, np.nan) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adlineband_126d_slope_v086_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    m = _mean(ad, 126)
    base = (ad - m) / ad.abs().rolling(126, min_periods=31).mean().replace(0, np.nan) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adlineband_252d_slope_v087_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    m = _mean(ad, 252)
    base = (ad - m) / ad.abs().rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adlineband_252d_slope_v088_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    m = _mean(ad, 252)
    base = (ad - m) / ad.abs().rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adlineband_252d_slope_v089_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    m = _mean(ad, 252)
    base = (ad - m) / ad.abs().rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adlineband_252d_slope_v090_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    m = _mean(ad, 252)
    base = (ad - m) / ad.abs().rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_sqadslope_21d_slope_v091_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 21)
    base = (sl * sl) * np.sign(sl) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_sqadslope_21d_slope_v092_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 21)
    base = (sl * sl) * np.sign(sl) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_sqadslope_63d_slope_v093_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 63)
    base = (sl * sl) * np.sign(sl) * closeadj
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_sqadslope_63d_slope_v094_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 63)
    base = (sl * sl) * np.sign(sl) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_sqadslope_126d_slope_v095_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 126)
    base = (sl * sl) * np.sign(sl) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_sqadslope_126d_slope_v096_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 126)
    base = (sl * sl) * np.sign(sl) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_sqadslope_252d_slope_v097_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 252)
    base = (sl * sl) * np.sign(sl) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_sqadslope_252d_slope_v098_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 252)
    base = (sl * sl) * np.sign(sl) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_sqadslope_252d_slope_v099_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 252)
    base = (sl * sl) * np.sign(sl) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_sqadslope_252d_slope_v100_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 252)
    base = (sl * sl) * np.sign(sl) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adslopexsign_21d_slope_v101_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 21)
    ret = closeadj.pct_change(5)
    base = sl * np.sign(ret).fillna(0.0) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adslopexsign_21d_slope_v102_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 21)
    ret = closeadj.pct_change(5)
    base = sl * np.sign(ret).fillna(0.0) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adslopexsign_63d_slope_v103_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 63)
    ret = closeadj.pct_change(15)
    base = sl * np.sign(ret).fillna(0.0) * closeadj
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adslopexsign_63d_slope_v104_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 63)
    ret = closeadj.pct_change(15)
    base = sl * np.sign(ret).fillna(0.0) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adslopexsign_126d_slope_v105_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 126)
    ret = closeadj.pct_change(31)
    base = sl * np.sign(ret).fillna(0.0) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adslopexsign_126d_slope_v106_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 126)
    ret = closeadj.pct_change(31)
    base = sl * np.sign(ret).fillna(0.0) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adslopexsign_252d_slope_v107_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 252)
    ret = closeadj.pct_change(63)
    base = sl * np.sign(ret).fillna(0.0) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adslopexsign_252d_slope_v108_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 252)
    ret = closeadj.pct_change(63)
    base = sl * np.sign(ret).fillna(0.0) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adslopexsign_252d_slope_v109_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 252)
    ret = closeadj.pct_change(63)
    base = sl * np.sign(ret).fillna(0.0) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adslopexsign_252d_slope_v110_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 252)
    ret = closeadj.pct_change(63)
    base = sl * np.sign(ret).fillna(0.0) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_emaadline_21d_slope_v111_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    e = ad.ewm(span=21, adjust=False).mean()
    base = (ad - e) / ad.abs().rolling(63, min_periods=5).mean().replace(0, np.nan) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_emaadline_21d_slope_v112_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    e = ad.ewm(span=21, adjust=False).mean()
    base = (ad - e) / ad.abs().rolling(63, min_periods=5).mean().replace(0, np.nan) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_emaadline_63d_slope_v113_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    e = ad.ewm(span=63, adjust=False).mean()
    base = (ad - e) / ad.abs().rolling(63, min_periods=15).mean().replace(0, np.nan) * closeadj
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_emaadline_63d_slope_v114_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    e = ad.ewm(span=63, adjust=False).mean()
    base = (ad - e) / ad.abs().rolling(63, min_periods=15).mean().replace(0, np.nan) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_emaadline_126d_slope_v115_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    e = ad.ewm(span=126, adjust=False).mean()
    base = (ad - e) / ad.abs().rolling(126, min_periods=31).mean().replace(0, np.nan) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_emaadline_126d_slope_v116_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    e = ad.ewm(span=126, adjust=False).mean()
    base = (ad - e) / ad.abs().rolling(126, min_periods=31).mean().replace(0, np.nan) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_emaadline_252d_slope_v117_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    e = ad.ewm(span=252, adjust=False).mean()
    base = (ad - e) / ad.abs().rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_emaadline_252d_slope_v118_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    e = ad.ewm(span=252, adjust=False).mean()
    base = (ad - e) / ad.abs().rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_emaadline_252d_slope_v119_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    e = ad.ewm(span=252, adjust=False).mean()
    base = (ad - e) / ad.abs().rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_emaadline_252d_slope_v120_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    e = ad.ewm(span=252, adjust=False).mean()
    base = (ad - e) / ad.abs().rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_absadslope_21d_slope_v121_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 21)
    base = sl.abs().rolling(21, min_periods=5).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_absadslope_21d_slope_v122_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 21)
    base = sl.abs().rolling(21, min_periods=5).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_absadslope_63d_slope_v123_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 63)
    base = sl.abs().rolling(63, min_periods=15).mean() * closeadj
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_absadslope_63d_slope_v124_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 63)
    base = sl.abs().rolling(63, min_periods=15).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_absadslope_126d_slope_v125_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 126)
    base = sl.abs().rolling(126, min_periods=31).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_absadslope_126d_slope_v126_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 126)
    base = sl.abs().rolling(126, min_periods=31).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_absadslope_252d_slope_v127_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 252)
    base = sl.abs().rolling(252, min_periods=63).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_absadslope_252d_slope_v128_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 252)
    base = sl.abs().rolling(252, min_periods=63).mean() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_absadslope_252d_slope_v129_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 252)
    base = sl.abs().rolling(252, min_periods=63).mean() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_absadslope_252d_slope_v130_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 252)
    base = sl.abs().rolling(252, min_periods=63).mean() * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adgap_21d_slope_v131_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 21)
    c = _f035_chaikin_trend(high, low, closeadj, volume, 21)
    base = (sl - c) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adgap_21d_slope_v132_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 21)
    c = _f035_chaikin_trend(high, low, closeadj, volume, 21)
    base = (sl - c) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adgap_63d_slope_v133_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 63)
    c = _f035_chaikin_trend(high, low, closeadj, volume, 63)
    base = (sl - c) * closeadj
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adgap_63d_slope_v134_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 63)
    c = _f035_chaikin_trend(high, low, closeadj, volume, 63)
    base = (sl - c) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adgap_126d_slope_v135_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 126)
    c = _f035_chaikin_trend(high, low, closeadj, volume, 126)
    base = (sl - c) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adgap_126d_slope_v136_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 126)
    c = _f035_chaikin_trend(high, low, closeadj, volume, 126)
    base = (sl - c) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adgap_252d_slope_v137_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 252)
    c = _f035_chaikin_trend(high, low, closeadj, volume, 252)
    base = (sl - c) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adgap_252d_slope_v138_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 252)
    c = _f035_chaikin_trend(high, low, closeadj, volume, 252)
    base = (sl - c) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adgap_252d_slope_v139_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 252)
    c = _f035_chaikin_trend(high, low, closeadj, volume, 252)
    base = (sl - c) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adgap_252d_slope_v140_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 252)
    c = _f035_chaikin_trend(high, low, closeadj, volume, 252)
    base = (sl - c) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_emachaikin_21d_slope_v141_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 21)
    base = c.ewm(span=10, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_emachaikin_21d_slope_v142_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 21)
    base = c.ewm(span=10, adjust=False).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_emachaikin_63d_slope_v143_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 63)
    base = c.ewm(span=31, adjust=False).mean() * closeadj
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_emachaikin_63d_slope_v144_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 63)
    base = c.ewm(span=31, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_emachaikin_126d_slope_v145_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 126)
    base = c.ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_emachaikin_126d_slope_v146_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 126)
    base = c.ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_emachaikin_252d_slope_v147_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 252)
    base = c.ewm(span=126, adjust=False).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_emachaikin_252d_slope_v148_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 252)
    base = c.ewm(span=126, adjust=False).mean() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_emachaikin_252d_slope_v149_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 252)
    base = c.ewm(span=126, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_emachaikin_252d_slope_v150_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 252)
    base = c.ewm(span=126, adjust=False).mean() * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f035ads_f035_ad_line_slope_adslope_21d_slope_v001_signal,
    f035ads_f035_ad_line_slope_adslope_21d_slope_v002_signal,
    f035ads_f035_ad_line_slope_adslope_63d_slope_v003_signal,
    f035ads_f035_ad_line_slope_adslope_63d_slope_v004_signal,
    f035ads_f035_ad_line_slope_adslope_126d_slope_v005_signal,
    f035ads_f035_ad_line_slope_adslope_126d_slope_v006_signal,
    f035ads_f035_ad_line_slope_adslope_252d_slope_v007_signal,
    f035ads_f035_ad_line_slope_adslope_252d_slope_v008_signal,
    f035ads_f035_ad_line_slope_adslope_252d_slope_v009_signal,
    f035ads_f035_ad_line_slope_adslope_252d_slope_v010_signal,
    f035ads_f035_ad_line_slope_chaikin_21d_slope_v011_signal,
    f035ads_f035_ad_line_slope_chaikin_21d_slope_v012_signal,
    f035ads_f035_ad_line_slope_chaikin_63d_slope_v013_signal,
    f035ads_f035_ad_line_slope_chaikin_63d_slope_v014_signal,
    f035ads_f035_ad_line_slope_chaikin_126d_slope_v015_signal,
    f035ads_f035_ad_line_slope_chaikin_126d_slope_v016_signal,
    f035ads_f035_ad_line_slope_chaikin_252d_slope_v017_signal,
    f035ads_f035_ad_line_slope_chaikin_252d_slope_v018_signal,
    f035ads_f035_ad_line_slope_chaikin_252d_slope_v019_signal,
    f035ads_f035_ad_line_slope_chaikin_252d_slope_v020_signal,
    f035ads_f035_ad_line_slope_adlinez_21d_slope_v021_signal,
    f035ads_f035_ad_line_slope_adlinez_21d_slope_v022_signal,
    f035ads_f035_ad_line_slope_adlinez_63d_slope_v023_signal,
    f035ads_f035_ad_line_slope_adlinez_63d_slope_v024_signal,
    f035ads_f035_ad_line_slope_adlinez_126d_slope_v025_signal,
    f035ads_f035_ad_line_slope_adlinez_126d_slope_v026_signal,
    f035ads_f035_ad_line_slope_adlinez_252d_slope_v027_signal,
    f035ads_f035_ad_line_slope_adlinez_252d_slope_v028_signal,
    f035ads_f035_ad_line_slope_adlinez_252d_slope_v029_signal,
    f035ads_f035_ad_line_slope_adlinez_252d_slope_v030_signal,
    f035ads_f035_ad_line_slope_smadslope_21d_slope_v031_signal,
    f035ads_f035_ad_line_slope_smadslope_21d_slope_v032_signal,
    f035ads_f035_ad_line_slope_smadslope_63d_slope_v033_signal,
    f035ads_f035_ad_line_slope_smadslope_63d_slope_v034_signal,
    f035ads_f035_ad_line_slope_smadslope_126d_slope_v035_signal,
    f035ads_f035_ad_line_slope_smadslope_126d_slope_v036_signal,
    f035ads_f035_ad_line_slope_smadslope_252d_slope_v037_signal,
    f035ads_f035_ad_line_slope_smadslope_252d_slope_v038_signal,
    f035ads_f035_ad_line_slope_smadslope_252d_slope_v039_signal,
    f035ads_f035_ad_line_slope_smadslope_252d_slope_v040_signal,
    f035ads_f035_ad_line_slope_zadslope_21d_slope_v041_signal,
    f035ads_f035_ad_line_slope_zadslope_21d_slope_v042_signal,
    f035ads_f035_ad_line_slope_zadslope_63d_slope_v043_signal,
    f035ads_f035_ad_line_slope_zadslope_63d_slope_v044_signal,
    f035ads_f035_ad_line_slope_zadslope_126d_slope_v045_signal,
    f035ads_f035_ad_line_slope_zadslope_126d_slope_v046_signal,
    f035ads_f035_ad_line_slope_zadslope_252d_slope_v047_signal,
    f035ads_f035_ad_line_slope_zadslope_252d_slope_v048_signal,
    f035ads_f035_ad_line_slope_zadslope_252d_slope_v049_signal,
    f035ads_f035_ad_line_slope_zadslope_252d_slope_v050_signal,
    f035ads_f035_ad_line_slope_stdadslope_21d_slope_v051_signal,
    f035ads_f035_ad_line_slope_stdadslope_21d_slope_v052_signal,
    f035ads_f035_ad_line_slope_stdadslope_63d_slope_v053_signal,
    f035ads_f035_ad_line_slope_stdadslope_63d_slope_v054_signal,
    f035ads_f035_ad_line_slope_stdadslope_126d_slope_v055_signal,
    f035ads_f035_ad_line_slope_stdadslope_126d_slope_v056_signal,
    f035ads_f035_ad_line_slope_stdadslope_252d_slope_v057_signal,
    f035ads_f035_ad_line_slope_stdadslope_252d_slope_v058_signal,
    f035ads_f035_ad_line_slope_stdadslope_252d_slope_v059_signal,
    f035ads_f035_ad_line_slope_stdadslope_252d_slope_v060_signal,
    f035ads_f035_ad_line_slope_smchaikin_21d_slope_v061_signal,
    f035ads_f035_ad_line_slope_smchaikin_21d_slope_v062_signal,
    f035ads_f035_ad_line_slope_smchaikin_63d_slope_v063_signal,
    f035ads_f035_ad_line_slope_smchaikin_63d_slope_v064_signal,
    f035ads_f035_ad_line_slope_smchaikin_126d_slope_v065_signal,
    f035ads_f035_ad_line_slope_smchaikin_126d_slope_v066_signal,
    f035ads_f035_ad_line_slope_smchaikin_252d_slope_v067_signal,
    f035ads_f035_ad_line_slope_smchaikin_252d_slope_v068_signal,
    f035ads_f035_ad_line_slope_smchaikin_252d_slope_v069_signal,
    f035ads_f035_ad_line_slope_smchaikin_252d_slope_v070_signal,
    f035ads_f035_ad_line_slope_zchaikin_21d_slope_v071_signal,
    f035ads_f035_ad_line_slope_zchaikin_21d_slope_v072_signal,
    f035ads_f035_ad_line_slope_zchaikin_63d_slope_v073_signal,
    f035ads_f035_ad_line_slope_zchaikin_63d_slope_v074_signal,
    f035ads_f035_ad_line_slope_zchaikin_126d_slope_v075_signal,
    f035ads_f035_ad_line_slope_zchaikin_126d_slope_v076_signal,
    f035ads_f035_ad_line_slope_zchaikin_252d_slope_v077_signal,
    f035ads_f035_ad_line_slope_zchaikin_252d_slope_v078_signal,
    f035ads_f035_ad_line_slope_zchaikin_252d_slope_v079_signal,
    f035ads_f035_ad_line_slope_zchaikin_252d_slope_v080_signal,
    f035ads_f035_ad_line_slope_adlineband_21d_slope_v081_signal,
    f035ads_f035_ad_line_slope_adlineband_21d_slope_v082_signal,
    f035ads_f035_ad_line_slope_adlineband_63d_slope_v083_signal,
    f035ads_f035_ad_line_slope_adlineband_63d_slope_v084_signal,
    f035ads_f035_ad_line_slope_adlineband_126d_slope_v085_signal,
    f035ads_f035_ad_line_slope_adlineband_126d_slope_v086_signal,
    f035ads_f035_ad_line_slope_adlineband_252d_slope_v087_signal,
    f035ads_f035_ad_line_slope_adlineband_252d_slope_v088_signal,
    f035ads_f035_ad_line_slope_adlineband_252d_slope_v089_signal,
    f035ads_f035_ad_line_slope_adlineband_252d_slope_v090_signal,
    f035ads_f035_ad_line_slope_sqadslope_21d_slope_v091_signal,
    f035ads_f035_ad_line_slope_sqadslope_21d_slope_v092_signal,
    f035ads_f035_ad_line_slope_sqadslope_63d_slope_v093_signal,
    f035ads_f035_ad_line_slope_sqadslope_63d_slope_v094_signal,
    f035ads_f035_ad_line_slope_sqadslope_126d_slope_v095_signal,
    f035ads_f035_ad_line_slope_sqadslope_126d_slope_v096_signal,
    f035ads_f035_ad_line_slope_sqadslope_252d_slope_v097_signal,
    f035ads_f035_ad_line_slope_sqadslope_252d_slope_v098_signal,
    f035ads_f035_ad_line_slope_sqadslope_252d_slope_v099_signal,
    f035ads_f035_ad_line_slope_sqadslope_252d_slope_v100_signal,
    f035ads_f035_ad_line_slope_adslopexsign_21d_slope_v101_signal,
    f035ads_f035_ad_line_slope_adslopexsign_21d_slope_v102_signal,
    f035ads_f035_ad_line_slope_adslopexsign_63d_slope_v103_signal,
    f035ads_f035_ad_line_slope_adslopexsign_63d_slope_v104_signal,
    f035ads_f035_ad_line_slope_adslopexsign_126d_slope_v105_signal,
    f035ads_f035_ad_line_slope_adslopexsign_126d_slope_v106_signal,
    f035ads_f035_ad_line_slope_adslopexsign_252d_slope_v107_signal,
    f035ads_f035_ad_line_slope_adslopexsign_252d_slope_v108_signal,
    f035ads_f035_ad_line_slope_adslopexsign_252d_slope_v109_signal,
    f035ads_f035_ad_line_slope_adslopexsign_252d_slope_v110_signal,
    f035ads_f035_ad_line_slope_emaadline_21d_slope_v111_signal,
    f035ads_f035_ad_line_slope_emaadline_21d_slope_v112_signal,
    f035ads_f035_ad_line_slope_emaadline_63d_slope_v113_signal,
    f035ads_f035_ad_line_slope_emaadline_63d_slope_v114_signal,
    f035ads_f035_ad_line_slope_emaadline_126d_slope_v115_signal,
    f035ads_f035_ad_line_slope_emaadline_126d_slope_v116_signal,
    f035ads_f035_ad_line_slope_emaadline_252d_slope_v117_signal,
    f035ads_f035_ad_line_slope_emaadline_252d_slope_v118_signal,
    f035ads_f035_ad_line_slope_emaadline_252d_slope_v119_signal,
    f035ads_f035_ad_line_slope_emaadline_252d_slope_v120_signal,
    f035ads_f035_ad_line_slope_absadslope_21d_slope_v121_signal,
    f035ads_f035_ad_line_slope_absadslope_21d_slope_v122_signal,
    f035ads_f035_ad_line_slope_absadslope_63d_slope_v123_signal,
    f035ads_f035_ad_line_slope_absadslope_63d_slope_v124_signal,
    f035ads_f035_ad_line_slope_absadslope_126d_slope_v125_signal,
    f035ads_f035_ad_line_slope_absadslope_126d_slope_v126_signal,
    f035ads_f035_ad_line_slope_absadslope_252d_slope_v127_signal,
    f035ads_f035_ad_line_slope_absadslope_252d_slope_v128_signal,
    f035ads_f035_ad_line_slope_absadslope_252d_slope_v129_signal,
    f035ads_f035_ad_line_slope_absadslope_252d_slope_v130_signal,
    f035ads_f035_ad_line_slope_adgap_21d_slope_v131_signal,
    f035ads_f035_ad_line_slope_adgap_21d_slope_v132_signal,
    f035ads_f035_ad_line_slope_adgap_63d_slope_v133_signal,
    f035ads_f035_ad_line_slope_adgap_63d_slope_v134_signal,
    f035ads_f035_ad_line_slope_adgap_126d_slope_v135_signal,
    f035ads_f035_ad_line_slope_adgap_126d_slope_v136_signal,
    f035ads_f035_ad_line_slope_adgap_252d_slope_v137_signal,
    f035ads_f035_ad_line_slope_adgap_252d_slope_v138_signal,
    f035ads_f035_ad_line_slope_adgap_252d_slope_v139_signal,
    f035ads_f035_ad_line_slope_adgap_252d_slope_v140_signal,
    f035ads_f035_ad_line_slope_emachaikin_21d_slope_v141_signal,
    f035ads_f035_ad_line_slope_emachaikin_21d_slope_v142_signal,
    f035ads_f035_ad_line_slope_emachaikin_63d_slope_v143_signal,
    f035ads_f035_ad_line_slope_emachaikin_63d_slope_v144_signal,
    f035ads_f035_ad_line_slope_emachaikin_126d_slope_v145_signal,
    f035ads_f035_ad_line_slope_emachaikin_126d_slope_v146_signal,
    f035ads_f035_ad_line_slope_emachaikin_252d_slope_v147_signal,
    f035ads_f035_ad_line_slope_emachaikin_252d_slope_v148_signal,
    f035ads_f035_ad_line_slope_emachaikin_252d_slope_v149_signal,
    f035ads_f035_ad_line_slope_emachaikin_252d_slope_v150_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F035_AD_LINE_SLOPE_REGISTRY_SLOPE_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f035_ad_line_slope_2nd_derivatives_001_150_claude: {n_features} features pass")
