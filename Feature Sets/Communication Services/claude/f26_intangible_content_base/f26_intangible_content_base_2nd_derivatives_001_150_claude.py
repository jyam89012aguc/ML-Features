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


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _roc(s, w):
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _logroc(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 3)).rank(pct=True) - 0.5


# ===== folder domain primitives (intangible / content base & amortization) =====
def _f26_intang_share(intangibles, assets):
    return intangibles / assets.replace(0, np.nan)


def _f26_tang_share(tangibles, assets):
    return tangibles / assets.replace(0, np.nan)


def _f26_amort_pace(depamor, intangibles):
    return depamor / intangibles.replace(0, np.nan)


def _f26_amort_ppne(depamor, ppnenet):
    return depamor / ppnenet.replace(0, np.nan)


def _f26_intang_to_tang(intangibles, tangibles):
    return intangibles / tangibles.replace(0, np.nan)


def _f26_content_base(intangibles, ppnenet):
    return intangibles + ppnenet


def _f26_amort_aging(depamor, intangibles, ppnenet):
    return depamor / (intangibles + ppnenet).replace(0, np.nan)



# slope (roc=10d) of base intangshare_63d
def f26ic_f26_intangible_content_base_intangshare_10d_slope_v001_signal(intangibles, assets):
    b = _f26_intang_share(intangibles, assets)
    _d = (b - b.shift(10)) / 10.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=21d) of base intangshare_126d
def f26ic_f26_intangible_content_base_intangshare_21d_slope_v002_signal(intangibles, assets):
    b = _f26_intang_share(intangibles, assets)
    _d = (b - b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=42d) of base intangshare_252d
def f26ic_f26_intangible_content_base_intangshare_42d_slope_v003_signal(intangibles, assets):
    b = _f26_intang_share(intangibles, assets)
    _d = (b - b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base intangshare_504d
def f26ic_f26_intangible_content_base_intangshare_63d_slope_v004_signal(intangibles, assets):
    b = _f26_intang_share(intangibles, assets)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base intangshare_1260d
def f26ic_f26_intangible_content_base_intangshare_126d_slope_v005_signal(intangibles, assets):
    b = _f26_intang_share(intangibles, assets)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=10d) of tangible-to-content-base ratio tangibles/(intang+ppne)
def f26ic_f26_intangible_content_base_tangshare_10d_slope_v006_signal(tangibles, intangibles, ppnenet):
    b = tangibles / _f26_content_base(intangibles, ppnenet).replace(0, np.nan)
    _d = (b - b.shift(10)) / 10.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=21d) of tangible-to-content-base ratio
def f26ic_f26_intangible_content_base_tangshare_21d_slope_v007_signal(tangibles, intangibles, ppnenet):
    b = tangibles / _f26_content_base(intangibles, ppnenet).replace(0, np.nan)
    _d = (b - b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=42d) of tangible-to-content-base ratio
def f26ic_f26_intangible_content_base_tangshare_42d_slope_v008_signal(tangibles, intangibles, ppnenet):
    b = tangibles / _f26_content_base(intangibles, ppnenet).replace(0, np.nan)
    _d = (b - b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of tangible-to-content-base ratio
def f26ic_f26_intangible_content_base_tangshare_63d_slope_v009_signal(tangibles, intangibles, ppnenet):
    b = tangibles / _f26_content_base(intangibles, ppnenet).replace(0, np.nan)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of tangible-to-content-base ratio
def f26ic_f26_intangible_content_base_tangshare_126d_slope_v010_signal(tangibles, intangibles, ppnenet):
    b = tangibles / _f26_content_base(intangibles, ppnenet).replace(0, np.nan)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=10d) of base amortpace_63d
def f26ic_f26_intangible_content_base_amortpace_10d_slope_v011_signal(depamor, intangibles):
    b = _f26_amort_pace(depamor, intangibles)
    _d = (b - b.shift(10)) / 10.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=21d) of base amortpace_126d
def f26ic_f26_intangible_content_base_amortpace_21d_slope_v012_signal(depamor, intangibles):
    b = _f26_amort_pace(depamor, intangibles)
    _d = (b - b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=42d) of base amortpace_252d
def f26ic_f26_intangible_content_base_amortpace_42d_slope_v013_signal(depamor, intangibles):
    b = _f26_amort_pace(depamor, intangibles)
    _d = (b - b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base amortpace_504d
def f26ic_f26_intangible_content_base_amortpace_63d_slope_v014_signal(depamor, intangibles):
    b = _f26_amort_pace(depamor, intangibles)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base amortpace_1260d
def f26ic_f26_intangible_content_base_amortpace_126d_slope_v015_signal(depamor, intangibles):
    b = _f26_amort_pace(depamor, intangibles)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=15d) of base amortppne_63d
def f26ic_f26_intangible_content_base_amortppne_15d_slope_v016_signal(depamor, ppnenet):
    b = _f26_amort_ppne(depamor, ppnenet)
    _d = (b - b.shift(15)) / 15.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=31d) of base amortppne_126d
def f26ic_f26_intangible_content_base_amortppne_31d_slope_v017_signal(depamor, ppnenet):
    b = _f26_amort_ppne(depamor, ppnenet)
    _d = (b - b.shift(31)) / 31.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=52d) of base amortppne_252d
def f26ic_f26_intangible_content_base_amortppne_52d_slope_v018_signal(depamor, ppnenet):
    b = _f26_amort_ppne(depamor, ppnenet)
    _d = (b - b.shift(52)) / 52.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=84d) of base amortppne_504d
def f26ic_f26_intangible_content_base_amortppne_84d_slope_v019_signal(depamor, ppnenet):
    b = _f26_amort_ppne(depamor, ppnenet)
    _d = (b - b.shift(84)) / 84.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=168d) of base amortppne_1260d
def f26ic_f26_intangible_content_base_amortppne_168d_slope_v020_signal(depamor, ppnenet):
    b = _f26_amort_ppne(depamor, ppnenet)
    _d = (b - b.shift(168)) / 168.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=10d) of base intang2tang_63d
def f26ic_f26_intangible_content_base_intang2tang_10d_slope_v021_signal(intangibles, tangibles):
    b = np.log(_f26_intang_to_tang(intangibles, tangibles).replace(0, np.nan))
    _d = (b - b.shift(10)) / 10.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=21d) of base intang2tang_126d
def f26ic_f26_intangible_content_base_intang2tang_21d_slope_v022_signal(intangibles, tangibles):
    b = np.log(_f26_intang_to_tang(intangibles, tangibles).replace(0, np.nan))
    _d = (b - b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=42d) of base intang2tang_252d
def f26ic_f26_intangible_content_base_intang2tang_42d_slope_v023_signal(intangibles, tangibles):
    b = np.log(_f26_intang_to_tang(intangibles, tangibles).replace(0, np.nan))
    _d = (b - b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base intang2tang_504d
def f26ic_f26_intangible_content_base_intang2tang_63d_slope_v024_signal(intangibles, tangibles):
    b = np.log(_f26_intang_to_tang(intangibles, tangibles).replace(0, np.nan))
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base intang2tang_1260d
def f26ic_f26_intangible_content_base_intang2tang_126d_slope_v025_signal(intangibles, tangibles):
    b = np.log(_f26_intang_to_tang(intangibles, tangibles).replace(0, np.nan))
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=10d) of base intang2ppne_63d
def f26ic_f26_intangible_content_base_intang2ppne_10d_slope_v026_signal(intangibles, ppnenet):
    b = np.log((intangibles / ppnenet.replace(0, np.nan)).replace(0, np.nan))
    _d = (b - b.shift(10)) / 10.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=21d) of base intang2ppne_126d
def f26ic_f26_intangible_content_base_intang2ppne_21d_slope_v027_signal(intangibles, ppnenet):
    b = np.log((intangibles / ppnenet.replace(0, np.nan)).replace(0, np.nan))
    _d = (b - b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=42d) of base intang2ppne_252d
def f26ic_f26_intangible_content_base_intang2ppne_42d_slope_v028_signal(intangibles, ppnenet):
    b = np.log((intangibles / ppnenet.replace(0, np.nan)).replace(0, np.nan))
    _d = (b - b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base intang2ppne_504d
def f26ic_f26_intangible_content_base_intang2ppne_63d_slope_v029_signal(intangibles, ppnenet):
    b = np.log((intangibles / ppnenet.replace(0, np.nan)).replace(0, np.nan))
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base intang2ppne_1260d
def f26ic_f26_intangible_content_base_intang2ppne_126d_slope_v030_signal(intangibles, ppnenet):
    b = np.log((intangibles / ppnenet.replace(0, np.nan)).replace(0, np.nan))
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=10d) of base amortburden_63d
def f26ic_f26_intangible_content_base_amortburden_10d_slope_v031_signal(depamor, assets):
    b = depamor / assets.replace(0, np.nan)
    _d = (b - b.shift(10)) / 10.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=21d) of base amortburden_126d
def f26ic_f26_intangible_content_base_amortburden_21d_slope_v032_signal(depamor, assets):
    b = depamor / assets.replace(0, np.nan)
    _d = (b - b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=42d) of base amortburden_252d
def f26ic_f26_intangible_content_base_amortburden_42d_slope_v033_signal(depamor, assets):
    b = depamor / assets.replace(0, np.nan)
    _d = (b - b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base amortburden_504d
def f26ic_f26_intangible_content_base_amortburden_63d_slope_v034_signal(depamor, assets):
    b = depamor / assets.replace(0, np.nan)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base amortburden_1260d
def f26ic_f26_intangible_content_base_amortburden_126d_slope_v035_signal(depamor, assets):
    b = depamor / assets.replace(0, np.nan)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=13d) of base aging_63d
def f26ic_f26_intangible_content_base_aging_13d_slope_v036_signal(depamor, intangibles, ppnenet):
    b = _f26_amort_aging(depamor, intangibles, ppnenet)
    _d = (b - b.shift(13)) / 13.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=27d) of base aging_126d
def f26ic_f26_intangible_content_base_aging_27d_slope_v037_signal(depamor, intangibles, ppnenet):
    b = _f26_amort_aging(depamor, intangibles, ppnenet)
    _d = (b - b.shift(27)) / 27.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=47d) of base aging_252d
def f26ic_f26_intangible_content_base_aging_47d_slope_v038_signal(depamor, intangibles, ppnenet):
    b = _f26_amort_aging(depamor, intangibles, ppnenet)
    _d = (b - b.shift(47)) / 47.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=73d) of base aging_504d
def f26ic_f26_intangible_content_base_aging_73d_slope_v039_signal(depamor, intangibles, ppnenet):
    b = _f26_amort_aging(depamor, intangibles, ppnenet)
    _d = (b - b.shift(73)) / 73.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=147d) of base aging_1260d
def f26ic_f26_intangible_content_base_aging_147d_slope_v040_signal(depamor, intangibles, ppnenet):
    b = _f26_amort_aging(depamor, intangibles, ppnenet)
    _d = (b - b.shift(147)) / 147.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=10d) of base intensity_63d
def f26ic_f26_intangible_content_base_intensity_10d_slope_v041_signal(intangibles, ppnenet, assets):
    b = _f26_content_base(intangibles, ppnenet) / assets.replace(0, np.nan)
    _d = (b - b.shift(10)) / 10.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=21d) of base intensity_126d
def f26ic_f26_intangible_content_base_intensity_21d_slope_v042_signal(intangibles, ppnenet, assets):
    b = _f26_content_base(intangibles, ppnenet) / assets.replace(0, np.nan)
    _d = (b - b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=42d) of base intensity_252d
def f26ic_f26_intangible_content_base_intensity_42d_slope_v043_signal(intangibles, ppnenet, assets):
    b = _f26_content_base(intangibles, ppnenet) / assets.replace(0, np.nan)
    _d = (b - b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base intensity_504d
def f26ic_f26_intangible_content_base_intensity_63d_slope_v044_signal(intangibles, ppnenet, assets):
    b = _f26_content_base(intangibles, ppnenet) / assets.replace(0, np.nan)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base intensity_1260d
def f26ic_f26_intangible_content_base_intensity_126d_slope_v045_signal(intangibles, ppnenet, assets):
    b = _f26_content_base(intangibles, ppnenet) / assets.replace(0, np.nan)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=16d) of base contentlife_63d
def f26ic_f26_intangible_content_base_contentlife_16d_slope_v046_signal(intangibles, depamor):
    b = np.log((intangibles / depamor.replace(0, np.nan)).replace(0, np.nan))
    _d = (b - b.shift(16)) / 16.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=33d) of base contentlife_126d
def f26ic_f26_intangible_content_base_contentlife_33d_slope_v047_signal(intangibles, depamor):
    b = np.log((intangibles / depamor.replace(0, np.nan)).replace(0, np.nan))
    _d = (b - b.shift(33)) / 33.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=55d) of base contentlife_252d
def f26ic_f26_intangible_content_base_contentlife_55d_slope_v048_signal(intangibles, depamor):
    b = np.log((intangibles / depamor.replace(0, np.nan)).replace(0, np.nan))
    _d = (b - b.shift(55)) / 55.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=88d) of base contentlife_504d
def f26ic_f26_intangible_content_base_contentlife_88d_slope_v049_signal(intangibles, depamor):
    b = np.log((intangibles / depamor.replace(0, np.nan)).replace(0, np.nan))
    _d = (b - b.shift(88)) / 88.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=130d) of base contentlife_1260d
def f26ic_f26_intangible_content_base_contentlife_130d_slope_v050_signal(intangibles, depamor):
    b = np.log((intangibles / depamor.replace(0, np.nan)).replace(0, np.nan))
    _d = (b - b.shift(130)) / 130.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=14d) of base platformlife_63d
def f26ic_f26_intangible_content_base_platformlife_14d_slope_v051_signal(ppnenet, depamor):
    b = np.log((ppnenet / depamor.replace(0, np.nan)).replace(0, np.nan))
    _d = (b - b.shift(14)) / 14.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=29d) of base platformlife_126d
def f26ic_f26_intangible_content_base_platformlife_29d_slope_v052_signal(ppnenet, depamor):
    b = np.log((ppnenet / depamor.replace(0, np.nan)).replace(0, np.nan))
    _d = (b - b.shift(29)) / 29.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=50d) of base platformlife_252d
def f26ic_f26_intangible_content_base_platformlife_50d_slope_v053_signal(ppnenet, depamor):
    b = np.log((ppnenet / depamor.replace(0, np.nan)).replace(0, np.nan))
    _d = (b - b.shift(50)) / 50.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=70d) of base platformlife_504d
def f26ic_f26_intangible_content_base_platformlife_70d_slope_v054_signal(ppnenet, depamor):
    b = np.log((ppnenet / depamor.replace(0, np.nan)).replace(0, np.nan))
    _d = (b - b.shift(70)) / 70.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=115d) of base platformlife_1260d
def f26ic_f26_intangible_content_base_platformlife_115d_slope_v055_signal(ppnenet, depamor):
    b = np.log((ppnenet / depamor.replace(0, np.nan)).replace(0, np.nan))
    _d = (b - b.shift(115)) / 115.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=18d) of base amorttang_63d
def f26ic_f26_intangible_content_base_amorttang_18d_slope_v056_signal(depamor, tangibles):
    b = depamor / tangibles.replace(0, np.nan)
    _d = (b - b.shift(18)) / 18.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=36d) of base amorttang_126d
def f26ic_f26_intangible_content_base_amorttang_36d_slope_v057_signal(depamor, tangibles):
    b = depamor / tangibles.replace(0, np.nan)
    _d = (b - b.shift(36)) / 36.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=58d) of base amorttang_252d
def f26ic_f26_intangible_content_base_amorttang_58d_slope_v058_signal(depamor, tangibles):
    b = depamor / tangibles.replace(0, np.nan)
    _d = (b - b.shift(58)) / 58.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=95d) of base amorttang_504d
def f26ic_f26_intangible_content_base_amorttang_95d_slope_v059_signal(depamor, tangibles):
    b = depamor / tangibles.replace(0, np.nan)
    _d = (b - b.shift(95)) / 95.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=110d) of base amorttang_1260d
def f26ic_f26_intangible_content_base_amorttang_110d_slope_v060_signal(depamor, tangibles):
    b = depamor / tangibles.replace(0, np.nan)
    _d = (b - b.shift(110)) / 110.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=10d) of base tang2ppne_63d
def f26ic_f26_intangible_content_base_tang2ppne_10d_slope_v061_signal(tangibles, ppnenet):
    b = np.log((tangibles / ppnenet.replace(0, np.nan)).replace(0, np.nan))
    _d = (b - b.shift(10)) / 10.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=21d) of base tang2ppne_126d
def f26ic_f26_intangible_content_base_tang2ppne_21d_slope_v062_signal(tangibles, ppnenet):
    b = np.log((tangibles / ppnenet.replace(0, np.nan)).replace(0, np.nan))
    _d = (b - b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=42d) of base tang2ppne_252d
def f26ic_f26_intangible_content_base_tang2ppne_42d_slope_v063_signal(tangibles, ppnenet):
    b = np.log((tangibles / ppnenet.replace(0, np.nan)).replace(0, np.nan))
    _d = (b - b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base tang2ppne_504d
def f26ic_f26_intangible_content_base_tang2ppne_63d_slope_v064_signal(tangibles, ppnenet):
    b = np.log((tangibles / ppnenet.replace(0, np.nan)).replace(0, np.nan))
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base tang2ppne_1260d
def f26ic_f26_intangible_content_base_tang2ppne_126d_slope_v065_signal(tangibles, ppnenet):
    b = np.log((tangibles / ppnenet.replace(0, np.nan)).replace(0, np.nan))
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=12d) of base pacegap_63d
def f26ic_f26_intangible_content_base_pacegap_12d_slope_v066_signal(depamor, intangibles, ppnenet):
    b = _f26_amort_pace(depamor, intangibles) - _f26_amort_ppne(depamor, ppnenet)
    _d = (b - b.shift(12)) / 12.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=24d) of base pacegap_126d
def f26ic_f26_intangible_content_base_pacegap_24d_slope_v067_signal(depamor, intangibles, ppnenet):
    b = _f26_amort_pace(depamor, intangibles) - _f26_amort_ppne(depamor, ppnenet)
    _d = (b - b.shift(24)) / 24.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=48d) of base pacegap_252d
def f26ic_f26_intangible_content_base_pacegap_48d_slope_v068_signal(depamor, intangibles, ppnenet):
    b = _f26_amort_pace(depamor, intangibles) - _f26_amort_ppne(depamor, ppnenet)
    _d = (b - b.shift(48)) / 48.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=78d) of base pacegap_504d
def f26ic_f26_intangible_content_base_pacegap_78d_slope_v069_signal(depamor, intangibles, ppnenet):
    b = _f26_amort_pace(depamor, intangibles) - _f26_amort_ppne(depamor, ppnenet)
    _d = (b - b.shift(78)) / 78.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=100d) of base pacegap_1260d
def f26ic_f26_intangible_content_base_pacegap_100d_slope_v070_signal(depamor, intangibles, ppnenet):
    b = _f26_amort_pace(depamor, intangibles) - _f26_amort_ppne(depamor, ppnenet)
    _d = (b - b.shift(100)) / 100.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=10d) of amortization-concentration gap depamor/assets - depamor/(intang+ppne)
def f26ic_f26_intangible_content_base_tangminusbase_10d_slope_v071_signal(depamor, intangibles, ppnenet, assets):
    b = depamor / assets.replace(0, np.nan) - _f26_amort_aging(depamor, intangibles, ppnenet)
    _d = (b - b.shift(10)) / 10.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=21d) of amortization-concentration gap
def f26ic_f26_intangible_content_base_tangminusbase_21d_slope_v072_signal(depamor, intangibles, ppnenet, assets):
    b = depamor / assets.replace(0, np.nan) - _f26_amort_aging(depamor, intangibles, ppnenet)
    _d = (b - b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=42d) of amortization-concentration gap
def f26ic_f26_intangible_content_base_tangminusbase_42d_slope_v073_signal(depamor, intangibles, ppnenet, assets):
    b = depamor / assets.replace(0, np.nan) - _f26_amort_aging(depamor, intangibles, ppnenet)
    _d = (b - b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of amortization-concentration gap
def f26ic_f26_intangible_content_base_tangminusbase_63d_slope_v074_signal(depamor, intangibles, ppnenet, assets):
    b = depamor / assets.replace(0, np.nan) - _f26_amort_aging(depamor, intangibles, ppnenet)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of amortization-concentration gap
def f26ic_f26_intangible_content_base_tangminusbase_126d_slope_v075_signal(depamor, intangibles, ppnenet, assets):
    b = depamor / assets.replace(0, np.nan) - _f26_amort_aging(depamor, intangibles, ppnenet)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=10d) of base intanggrow_21d
def f26ic_f26_intangible_content_base_intanggrow_21d_slope_v076_signal(intangibles):
    b = _logroc(intangibles, 21)
    _d = (b - b.shift(10)) / 10.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=31d) of base intanggrow_63d
def f26ic_f26_intangible_content_base_intanggrow_63d_slope_v077_signal(intangibles):
    b = _logroc(intangibles, 63)
    _d = (b - b.shift(31)) / 31.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base intanggrow_126d
def f26ic_f26_intangible_content_base_intanggrow_126d_slope_v078_signal(intangibles):
    b = _logroc(intangibles, 126)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base intanggrow_252d
def f26ic_f26_intangible_content_base_intanggrow_252d_slope_v079_signal(intangibles):
    b = _logroc(intangibles, 252)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base intanggrow_504d
def f26ic_f26_intangible_content_base_intanggrow_504d_slope_v080_signal(intangibles):
    b = _logroc(intangibles, 504)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=10d) of base ppnegrow_21d
def f26ic_f26_intangible_content_base_ppnegrow_21d_slope_v081_signal(ppnenet):
    b = _logroc(ppnenet, 21)
    _d = (b - b.shift(10)) / 10.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=31d) of base ppnegrow_63d
def f26ic_f26_intangible_content_base_ppnegrow_63d_slope_v082_signal(ppnenet):
    b = _logroc(ppnenet, 63)
    _d = (b - b.shift(31)) / 31.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base ppnegrow_126d
def f26ic_f26_intangible_content_base_ppnegrow_126d_slope_v083_signal(ppnenet):
    b = _logroc(ppnenet, 126)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base ppnegrow_252d
def f26ic_f26_intangible_content_base_ppnegrow_252d_slope_v084_signal(ppnenet):
    b = _logroc(ppnenet, 252)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base ppnegrow_504d
def f26ic_f26_intangible_content_base_ppnegrow_504d_slope_v085_signal(ppnenet):
    b = _logroc(ppnenet, 504)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=10d) of base amortgrow_21d
def f26ic_f26_intangible_content_base_amortgrow_21d_slope_v086_signal(depamor):
    b = _logroc(depamor, 21)
    _d = (b - b.shift(10)) / 10.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=31d) of base amortgrow_63d
def f26ic_f26_intangible_content_base_amortgrow_63d_slope_v087_signal(depamor):
    b = _logroc(depamor, 63)
    _d = (b - b.shift(31)) / 31.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base amortgrow_126d
def f26ic_f26_intangible_content_base_amortgrow_126d_slope_v088_signal(depamor):
    b = _logroc(depamor, 126)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base amortgrow_252d
def f26ic_f26_intangible_content_base_amortgrow_252d_slope_v089_signal(depamor):
    b = _logroc(depamor, 252)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base amortgrow_504d
def f26ic_f26_intangible_content_base_amortgrow_504d_slope_v090_signal(depamor):
    b = _logroc(depamor, 504)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=10d) of base tanggrow_21d
def f26ic_f26_intangible_content_base_tanggrow_21d_slope_v091_signal(tangibles):
    b = _logroc(tangibles, 21)
    _d = (b - b.shift(10)) / 10.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=31d) of base tanggrow_63d
def f26ic_f26_intangible_content_base_tanggrow_63d_slope_v092_signal(tangibles):
    b = _logroc(tangibles, 63)
    _d = (b - b.shift(31)) / 31.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base tanggrow_126d
def f26ic_f26_intangible_content_base_tanggrow_126d_slope_v093_signal(tangibles):
    b = _logroc(tangibles, 126)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base tanggrow_252d
def f26ic_f26_intangible_content_base_tanggrow_252d_slope_v094_signal(tangibles):
    b = _logroc(tangibles, 252)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base tanggrow_504d
def f26ic_f26_intangible_content_base_tanggrow_504d_slope_v095_signal(tangibles):
    b = _logroc(tangibles, 504)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=10d) of base assetgrow_21d
def f26ic_f26_intangible_content_base_assetgrow_21d_slope_v096_signal(assets):
    b = _logroc(assets, 21)
    _d = (b - b.shift(10)) / 10.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=31d) of base assetgrow_63d
def f26ic_f26_intangible_content_base_assetgrow_63d_slope_v097_signal(assets):
    b = _logroc(assets, 63)
    _d = (b - b.shift(31)) / 31.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base assetgrow_126d
def f26ic_f26_intangible_content_base_assetgrow_126d_slope_v098_signal(assets):
    b = _logroc(assets, 126)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base assetgrow_252d
def f26ic_f26_intangible_content_base_assetgrow_252d_slope_v099_signal(assets):
    b = _logroc(assets, 252)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base assetgrow_504d
def f26ic_f26_intangible_content_base_assetgrow_504d_slope_v100_signal(assets):
    b = _logroc(assets, 504)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=10d) of base basegrow_21d
def f26ic_f26_intangible_content_base_basegrow_21d_slope_v101_signal(intangibles, ppnenet):
    b = _logroc(_f26_content_base(intangibles, ppnenet), 21)
    _d = (b - b.shift(10)) / 10.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=31d) of base basegrow_63d
def f26ic_f26_intangible_content_base_basegrow_63d_slope_v102_signal(intangibles, ppnenet):
    b = _logroc(_f26_content_base(intangibles, ppnenet), 63)
    _d = (b - b.shift(31)) / 31.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base basegrow_126d
def f26ic_f26_intangible_content_base_basegrow_126d_slope_v103_signal(intangibles, ppnenet):
    b = _logroc(_f26_content_base(intangibles, ppnenet), 126)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base basegrow_252d
def f26ic_f26_intangible_content_base_basegrow_252d_slope_v104_signal(intangibles, ppnenet):
    b = _logroc(_f26_content_base(intangibles, ppnenet), 252)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base basegrow_504d
def f26ic_f26_intangible_content_base_basegrow_504d_slope_v105_signal(intangibles, ppnenet):
    b = _logroc(_f26_content_base(intangibles, ppnenet), 504)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=10d) of base intangvsasset_21d
def f26ic_f26_intangible_content_base_intangvsasset_21d_slope_v106_signal(intangibles, assets):
    b = _logroc(intangibles, 21) - _logroc(assets, 21)
    _d = (b - b.shift(10)) / 10.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=31d) of base intangvsasset_63d
def f26ic_f26_intangible_content_base_intangvsasset_63d_slope_v107_signal(intangibles, assets):
    b = _logroc(intangibles, 63) - _logroc(assets, 63)
    _d = (b - b.shift(31)) / 31.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base intangvsasset_126d
def f26ic_f26_intangible_content_base_intangvsasset_126d_slope_v108_signal(intangibles, assets):
    b = _logroc(intangibles, 126) - _logroc(assets, 126)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base intangvsasset_252d
def f26ic_f26_intangible_content_base_intangvsasset_252d_slope_v109_signal(intangibles, assets):
    b = _logroc(intangibles, 252) - _logroc(assets, 252)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base intangvsasset_504d
def f26ic_f26_intangible_content_base_intangvsasset_504d_slope_v110_signal(intangibles, assets):
    b = _logroc(intangibles, 504) - _logroc(assets, 504)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=10d) of intangibles vs geometric-mean physical base (log tilt level)
def f26ic_f26_intangible_content_base_intangvstang_21d_slope_v111_signal(intangibles, tangibles, ppnenet):
    b = np.log(intangibles.replace(0, np.nan)) - 0.5 * np.log(tangibles.replace(0, np.nan)) - 0.5 * np.log(ppnenet.replace(0, np.nan))
    _d = (b - b.shift(10)) / 10.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=31d) of intangibles vs geometric-mean physical base
def f26ic_f26_intangible_content_base_intangvstang_63d_slope_v112_signal(intangibles, tangibles, ppnenet):
    b = np.log(intangibles.replace(0, np.nan)) - 0.5 * np.log(tangibles.replace(0, np.nan)) - 0.5 * np.log(ppnenet.replace(0, np.nan))
    _d = (b - b.shift(31)) / 31.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of intangibles vs geometric-mean physical base
def f26ic_f26_intangible_content_base_intangvstang_126d_slope_v113_signal(intangibles, tangibles, ppnenet):
    b = np.log(intangibles.replace(0, np.nan)) - 0.5 * np.log(tangibles.replace(0, np.nan)) - 0.5 * np.log(ppnenet.replace(0, np.nan))
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of intangibles vs geometric-mean physical base
def f26ic_f26_intangible_content_base_intangvstang_252d_slope_v114_signal(intangibles, tangibles, ppnenet):
    b = np.log(intangibles.replace(0, np.nan)) - 0.5 * np.log(tangibles.replace(0, np.nan)) - 0.5 * np.log(ppnenet.replace(0, np.nan))
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of intangibles vs geometric-mean physical base (long horizon)
def f26ic_f26_intangible_content_base_intangvstang_504d_slope_v115_signal(intangibles, tangibles, ppnenet):
    b = np.log(intangibles.replace(0, np.nan)) - 0.5 * np.log(tangibles.replace(0, np.nan)) - 0.5 * np.log(ppnenet.replace(0, np.nan))
    _d = (b - b.shift(252)) / 252.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=10d) of base ppnevstang_21d
def f26ic_f26_intangible_content_base_ppnevstang_21d_slope_v116_signal(tangibles, ppnenet):
    b = _logroc(ppnenet, 21) - _logroc(tangibles, 21)
    _d = (b - b.shift(10)) / 10.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=31d) of base ppnevstang_63d
def f26ic_f26_intangible_content_base_ppnevstang_63d_slope_v117_signal(tangibles, ppnenet):
    b = _logroc(ppnenet, 63) - _logroc(tangibles, 63)
    _d = (b - b.shift(31)) / 31.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base ppnevstang_126d
def f26ic_f26_intangible_content_base_ppnevstang_126d_slope_v118_signal(tangibles, ppnenet):
    b = _logroc(ppnenet, 126) - _logroc(tangibles, 126)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base ppnevstang_252d
def f26ic_f26_intangible_content_base_ppnevstang_252d_slope_v119_signal(tangibles, ppnenet):
    b = _logroc(ppnenet, 252) - _logroc(tangibles, 252)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base ppnevstang_504d
def f26ic_f26_intangible_content_base_ppnevstang_504d_slope_v120_signal(tangibles, ppnenet):
    b = _logroc(ppnenet, 504) - _logroc(tangibles, 504)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=10d) of base amortvsintang_21d
def f26ic_f26_intangible_content_base_amortvsintang_21d_slope_v121_signal(depamor, intangibles):
    b = _logroc(depamor, 21) - _logroc(intangibles, 21)
    _d = (b - b.shift(10)) / 10.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=31d) of base amortvsintang_63d
def f26ic_f26_intangible_content_base_amortvsintang_63d_slope_v122_signal(depamor, intangibles):
    b = _logroc(depamor, 63) - _logroc(intangibles, 63)
    _d = (b - b.shift(31)) / 31.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base amortvsintang_126d
def f26ic_f26_intangible_content_base_amortvsintang_126d_slope_v123_signal(depamor, intangibles):
    b = _logroc(depamor, 126) - _logroc(intangibles, 126)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base amortvsintang_252d
def f26ic_f26_intangible_content_base_amortvsintang_252d_slope_v124_signal(depamor, intangibles):
    b = _logroc(depamor, 252) - _logroc(intangibles, 252)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base amortvsintang_504d
def f26ic_f26_intangible_content_base_amortvsintang_504d_slope_v125_signal(depamor, intangibles):
    b = _logroc(depamor, 504) - _logroc(intangibles, 504)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=10d) of base amortvstang_21d
def f26ic_f26_intangible_content_base_amortvstang_21d_slope_v126_signal(depamor, tangibles):
    b = _logroc(depamor, 21) - _logroc(tangibles, 21)
    _d = (b - b.shift(10)) / 10.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=31d) of base amortvstang_63d
def f26ic_f26_intangible_content_base_amortvstang_63d_slope_v127_signal(depamor, tangibles):
    b = _logroc(depamor, 63) - _logroc(tangibles, 63)
    _d = (b - b.shift(31)) / 31.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base amortvstang_126d
def f26ic_f26_intangible_content_base_amortvstang_126d_slope_v128_signal(depamor, tangibles):
    b = _logroc(depamor, 126) - _logroc(tangibles, 126)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base amortvstang_252d
def f26ic_f26_intangible_content_base_amortvstang_252d_slope_v129_signal(depamor, tangibles):
    b = _logroc(depamor, 252) - _logroc(tangibles, 252)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base amortvstang_504d
def f26ic_f26_intangible_content_base_amortvstang_504d_slope_v130_signal(depamor, tangibles):
    b = _logroc(depamor, 504) - _logroc(tangibles, 504)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=10d) of base basevstang_21d
def f26ic_f26_intangible_content_base_basevstang_21d_slope_v131_signal(intangibles, ppnenet, tangibles):
    b = _logroc(_f26_content_base(intangibles, ppnenet), 21) - _logroc(tangibles, 21)
    _d = (b - b.shift(10)) / 10.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=31d) of base basevstang_63d
def f26ic_f26_intangible_content_base_basevstang_63d_slope_v132_signal(intangibles, ppnenet, tangibles):
    b = _logroc(_f26_content_base(intangibles, ppnenet), 63) - _logroc(tangibles, 63)
    _d = (b - b.shift(31)) / 31.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base basevstang_126d
def f26ic_f26_intangible_content_base_basevstang_126d_slope_v133_signal(intangibles, ppnenet, tangibles):
    b = _logroc(_f26_content_base(intangibles, ppnenet), 126) - _logroc(tangibles, 126)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base basevstang_252d
def f26ic_f26_intangible_content_base_basevstang_252d_slope_v134_signal(intangibles, ppnenet, tangibles):
    b = _logroc(_f26_content_base(intangibles, ppnenet), 252) - _logroc(tangibles, 252)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base basevstang_504d
def f26ic_f26_intangible_content_base_basevstang_504d_slope_v135_signal(intangibles, ppnenet, tangibles):
    b = _logroc(_f26_content_base(intangibles, ppnenet), 504) - _logroc(tangibles, 504)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=10d) of base assetvsppne_21d
def f26ic_f26_intangible_content_base_assetvsppne_21d_slope_v136_signal(intangibles, ppnenet, assets):
    b = _logroc(assets, 21) - _logroc(ppnenet, 21)
    _d = (b - b.shift(10)) / 10.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=31d) of base assetvsppne_63d
def f26ic_f26_intangible_content_base_assetvsppne_63d_slope_v137_signal(intangibles, ppnenet, assets):
    b = _logroc(assets, 63) - _logroc(ppnenet, 63)
    _d = (b - b.shift(31)) / 31.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base assetvsppne_126d
def f26ic_f26_intangible_content_base_assetvsppne_126d_slope_v138_signal(intangibles, ppnenet, assets):
    b = _logroc(assets, 126) - _logroc(ppnenet, 126)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base assetvsppne_252d
def f26ic_f26_intangible_content_base_assetvsppne_252d_slope_v139_signal(intangibles, ppnenet, assets):
    b = _logroc(assets, 252) - _logroc(ppnenet, 252)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base assetvsppne_504d
def f26ic_f26_intangible_content_base_assetvsppne_504d_slope_v140_signal(intangibles, ppnenet, assets):
    b = _logroc(assets, 504) - _logroc(ppnenet, 504)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=10d) of base intangvsppne_21d
def f26ic_f26_intangible_content_base_intangvsppne_21d_slope_v141_signal(intangibles, ppnenet):
    b = _logroc(intangibles, 21) - _logroc(ppnenet, 21)
    _d = (b - b.shift(10)) / 10.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=31d) of base intangvsppne_63d
def f26ic_f26_intangible_content_base_intangvsppne_63d_slope_v142_signal(intangibles, ppnenet):
    b = _logroc(intangibles, 63) - _logroc(ppnenet, 63)
    _d = (b - b.shift(31)) / 31.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base intangvsppne_126d
def f26ic_f26_intangible_content_base_intangvsppne_126d_slope_v143_signal(intangibles, ppnenet):
    b = _logroc(intangibles, 126) - _logroc(ppnenet, 126)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base intangvsppne_252d
def f26ic_f26_intangible_content_base_intangvsppne_252d_slope_v144_signal(intangibles, ppnenet):
    b = _logroc(intangibles, 252) - _logroc(ppnenet, 252)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base intangvsppne_504d
def f26ic_f26_intangible_content_base_intangvsppne_504d_slope_v145_signal(intangibles, ppnenet):
    b = _logroc(intangibles, 504) - _logroc(ppnenet, 504)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=10d) of base tangvsasset_21d
def f26ic_f26_intangible_content_base_tangvsasset_21d_slope_v146_signal(tangibles, assets):
    b = _logroc(tangibles, 21) - _logroc(assets, 21)
    _d = (b - b.shift(10)) / 10.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=31d) of base tangvsasset_63d
def f26ic_f26_intangible_content_base_tangvsasset_63d_slope_v147_signal(tangibles, assets):
    b = _logroc(tangibles, 63) - _logroc(assets, 63)
    _d = (b - b.shift(31)) / 31.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base tangvsasset_126d
def f26ic_f26_intangible_content_base_tangvsasset_126d_slope_v148_signal(tangibles, assets):
    b = _logroc(tangibles, 126) - _logroc(assets, 126)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base tangvsasset_252d
def f26ic_f26_intangible_content_base_tangvsasset_252d_slope_v149_signal(tangibles, assets):
    b = _logroc(tangibles, 252) - _logroc(assets, 252)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base tangvsasset_504d
def f26ic_f26_intangible_content_base_tangvsasset_504d_slope_v150_signal(tangibles, assets):
    b = _logroc(tangibles, 504) - _logroc(assets, 504)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f26ic_f26_intangible_content_base_intangshare_10d_slope_v001_signal,
    f26ic_f26_intangible_content_base_intangshare_21d_slope_v002_signal,
    f26ic_f26_intangible_content_base_intangshare_42d_slope_v003_signal,
    f26ic_f26_intangible_content_base_intangshare_63d_slope_v004_signal,
    f26ic_f26_intangible_content_base_intangshare_126d_slope_v005_signal,
    f26ic_f26_intangible_content_base_tangshare_10d_slope_v006_signal,
    f26ic_f26_intangible_content_base_tangshare_21d_slope_v007_signal,
    f26ic_f26_intangible_content_base_tangshare_42d_slope_v008_signal,
    f26ic_f26_intangible_content_base_tangshare_63d_slope_v009_signal,
    f26ic_f26_intangible_content_base_tangshare_126d_slope_v010_signal,
    f26ic_f26_intangible_content_base_amortpace_10d_slope_v011_signal,
    f26ic_f26_intangible_content_base_amortpace_21d_slope_v012_signal,
    f26ic_f26_intangible_content_base_amortpace_42d_slope_v013_signal,
    f26ic_f26_intangible_content_base_amortpace_63d_slope_v014_signal,
    f26ic_f26_intangible_content_base_amortpace_126d_slope_v015_signal,
    f26ic_f26_intangible_content_base_amortppne_15d_slope_v016_signal,
    f26ic_f26_intangible_content_base_amortppne_31d_slope_v017_signal,
    f26ic_f26_intangible_content_base_amortppne_52d_slope_v018_signal,
    f26ic_f26_intangible_content_base_amortppne_84d_slope_v019_signal,
    f26ic_f26_intangible_content_base_amortppne_168d_slope_v020_signal,
    f26ic_f26_intangible_content_base_intang2tang_10d_slope_v021_signal,
    f26ic_f26_intangible_content_base_intang2tang_21d_slope_v022_signal,
    f26ic_f26_intangible_content_base_intang2tang_42d_slope_v023_signal,
    f26ic_f26_intangible_content_base_intang2tang_63d_slope_v024_signal,
    f26ic_f26_intangible_content_base_intang2tang_126d_slope_v025_signal,
    f26ic_f26_intangible_content_base_intang2ppne_10d_slope_v026_signal,
    f26ic_f26_intangible_content_base_intang2ppne_21d_slope_v027_signal,
    f26ic_f26_intangible_content_base_intang2ppne_42d_slope_v028_signal,
    f26ic_f26_intangible_content_base_intang2ppne_63d_slope_v029_signal,
    f26ic_f26_intangible_content_base_intang2ppne_126d_slope_v030_signal,
    f26ic_f26_intangible_content_base_amortburden_10d_slope_v031_signal,
    f26ic_f26_intangible_content_base_amortburden_21d_slope_v032_signal,
    f26ic_f26_intangible_content_base_amortburden_42d_slope_v033_signal,
    f26ic_f26_intangible_content_base_amortburden_63d_slope_v034_signal,
    f26ic_f26_intangible_content_base_amortburden_126d_slope_v035_signal,
    f26ic_f26_intangible_content_base_aging_13d_slope_v036_signal,
    f26ic_f26_intangible_content_base_aging_27d_slope_v037_signal,
    f26ic_f26_intangible_content_base_aging_47d_slope_v038_signal,
    f26ic_f26_intangible_content_base_aging_73d_slope_v039_signal,
    f26ic_f26_intangible_content_base_aging_147d_slope_v040_signal,
    f26ic_f26_intangible_content_base_intensity_10d_slope_v041_signal,
    f26ic_f26_intangible_content_base_intensity_21d_slope_v042_signal,
    f26ic_f26_intangible_content_base_intensity_42d_slope_v043_signal,
    f26ic_f26_intangible_content_base_intensity_63d_slope_v044_signal,
    f26ic_f26_intangible_content_base_intensity_126d_slope_v045_signal,
    f26ic_f26_intangible_content_base_contentlife_16d_slope_v046_signal,
    f26ic_f26_intangible_content_base_contentlife_33d_slope_v047_signal,
    f26ic_f26_intangible_content_base_contentlife_55d_slope_v048_signal,
    f26ic_f26_intangible_content_base_contentlife_88d_slope_v049_signal,
    f26ic_f26_intangible_content_base_contentlife_130d_slope_v050_signal,
    f26ic_f26_intangible_content_base_platformlife_14d_slope_v051_signal,
    f26ic_f26_intangible_content_base_platformlife_29d_slope_v052_signal,
    f26ic_f26_intangible_content_base_platformlife_50d_slope_v053_signal,
    f26ic_f26_intangible_content_base_platformlife_70d_slope_v054_signal,
    f26ic_f26_intangible_content_base_platformlife_115d_slope_v055_signal,
    f26ic_f26_intangible_content_base_amorttang_18d_slope_v056_signal,
    f26ic_f26_intangible_content_base_amorttang_36d_slope_v057_signal,
    f26ic_f26_intangible_content_base_amorttang_58d_slope_v058_signal,
    f26ic_f26_intangible_content_base_amorttang_95d_slope_v059_signal,
    f26ic_f26_intangible_content_base_amorttang_110d_slope_v060_signal,
    f26ic_f26_intangible_content_base_tang2ppne_10d_slope_v061_signal,
    f26ic_f26_intangible_content_base_tang2ppne_21d_slope_v062_signal,
    f26ic_f26_intangible_content_base_tang2ppne_42d_slope_v063_signal,
    f26ic_f26_intangible_content_base_tang2ppne_63d_slope_v064_signal,
    f26ic_f26_intangible_content_base_tang2ppne_126d_slope_v065_signal,
    f26ic_f26_intangible_content_base_pacegap_12d_slope_v066_signal,
    f26ic_f26_intangible_content_base_pacegap_24d_slope_v067_signal,
    f26ic_f26_intangible_content_base_pacegap_48d_slope_v068_signal,
    f26ic_f26_intangible_content_base_pacegap_78d_slope_v069_signal,
    f26ic_f26_intangible_content_base_pacegap_100d_slope_v070_signal,
    f26ic_f26_intangible_content_base_tangminusbase_10d_slope_v071_signal,
    f26ic_f26_intangible_content_base_tangminusbase_21d_slope_v072_signal,
    f26ic_f26_intangible_content_base_tangminusbase_42d_slope_v073_signal,
    f26ic_f26_intangible_content_base_tangminusbase_63d_slope_v074_signal,
    f26ic_f26_intangible_content_base_tangminusbase_126d_slope_v075_signal,
    f26ic_f26_intangible_content_base_intanggrow_21d_slope_v076_signal,
    f26ic_f26_intangible_content_base_intanggrow_63d_slope_v077_signal,
    f26ic_f26_intangible_content_base_intanggrow_126d_slope_v078_signal,
    f26ic_f26_intangible_content_base_intanggrow_252d_slope_v079_signal,
    f26ic_f26_intangible_content_base_intanggrow_504d_slope_v080_signal,
    f26ic_f26_intangible_content_base_ppnegrow_21d_slope_v081_signal,
    f26ic_f26_intangible_content_base_ppnegrow_63d_slope_v082_signal,
    f26ic_f26_intangible_content_base_ppnegrow_126d_slope_v083_signal,
    f26ic_f26_intangible_content_base_ppnegrow_252d_slope_v084_signal,
    f26ic_f26_intangible_content_base_ppnegrow_504d_slope_v085_signal,
    f26ic_f26_intangible_content_base_amortgrow_21d_slope_v086_signal,
    f26ic_f26_intangible_content_base_amortgrow_63d_slope_v087_signal,
    f26ic_f26_intangible_content_base_amortgrow_126d_slope_v088_signal,
    f26ic_f26_intangible_content_base_amortgrow_252d_slope_v089_signal,
    f26ic_f26_intangible_content_base_amortgrow_504d_slope_v090_signal,
    f26ic_f26_intangible_content_base_tanggrow_21d_slope_v091_signal,
    f26ic_f26_intangible_content_base_tanggrow_63d_slope_v092_signal,
    f26ic_f26_intangible_content_base_tanggrow_126d_slope_v093_signal,
    f26ic_f26_intangible_content_base_tanggrow_252d_slope_v094_signal,
    f26ic_f26_intangible_content_base_tanggrow_504d_slope_v095_signal,
    f26ic_f26_intangible_content_base_assetgrow_21d_slope_v096_signal,
    f26ic_f26_intangible_content_base_assetgrow_63d_slope_v097_signal,
    f26ic_f26_intangible_content_base_assetgrow_126d_slope_v098_signal,
    f26ic_f26_intangible_content_base_assetgrow_252d_slope_v099_signal,
    f26ic_f26_intangible_content_base_assetgrow_504d_slope_v100_signal,
    f26ic_f26_intangible_content_base_basegrow_21d_slope_v101_signal,
    f26ic_f26_intangible_content_base_basegrow_63d_slope_v102_signal,
    f26ic_f26_intangible_content_base_basegrow_126d_slope_v103_signal,
    f26ic_f26_intangible_content_base_basegrow_252d_slope_v104_signal,
    f26ic_f26_intangible_content_base_basegrow_504d_slope_v105_signal,
    f26ic_f26_intangible_content_base_intangvsasset_21d_slope_v106_signal,
    f26ic_f26_intangible_content_base_intangvsasset_63d_slope_v107_signal,
    f26ic_f26_intangible_content_base_intangvsasset_126d_slope_v108_signal,
    f26ic_f26_intangible_content_base_intangvsasset_252d_slope_v109_signal,
    f26ic_f26_intangible_content_base_intangvsasset_504d_slope_v110_signal,
    f26ic_f26_intangible_content_base_intangvstang_21d_slope_v111_signal,
    f26ic_f26_intangible_content_base_intangvstang_63d_slope_v112_signal,
    f26ic_f26_intangible_content_base_intangvstang_126d_slope_v113_signal,
    f26ic_f26_intangible_content_base_intangvstang_252d_slope_v114_signal,
    f26ic_f26_intangible_content_base_intangvstang_504d_slope_v115_signal,
    f26ic_f26_intangible_content_base_ppnevstang_21d_slope_v116_signal,
    f26ic_f26_intangible_content_base_ppnevstang_63d_slope_v117_signal,
    f26ic_f26_intangible_content_base_ppnevstang_126d_slope_v118_signal,
    f26ic_f26_intangible_content_base_ppnevstang_252d_slope_v119_signal,
    f26ic_f26_intangible_content_base_ppnevstang_504d_slope_v120_signal,
    f26ic_f26_intangible_content_base_amortvsintang_21d_slope_v121_signal,
    f26ic_f26_intangible_content_base_amortvsintang_63d_slope_v122_signal,
    f26ic_f26_intangible_content_base_amortvsintang_126d_slope_v123_signal,
    f26ic_f26_intangible_content_base_amortvsintang_252d_slope_v124_signal,
    f26ic_f26_intangible_content_base_amortvsintang_504d_slope_v125_signal,
    f26ic_f26_intangible_content_base_amortvstang_21d_slope_v126_signal,
    f26ic_f26_intangible_content_base_amortvstang_63d_slope_v127_signal,
    f26ic_f26_intangible_content_base_amortvstang_126d_slope_v128_signal,
    f26ic_f26_intangible_content_base_amortvstang_252d_slope_v129_signal,
    f26ic_f26_intangible_content_base_amortvstang_504d_slope_v130_signal,
    f26ic_f26_intangible_content_base_basevstang_21d_slope_v131_signal,
    f26ic_f26_intangible_content_base_basevstang_63d_slope_v132_signal,
    f26ic_f26_intangible_content_base_basevstang_126d_slope_v133_signal,
    f26ic_f26_intangible_content_base_basevstang_252d_slope_v134_signal,
    f26ic_f26_intangible_content_base_basevstang_504d_slope_v135_signal,
    f26ic_f26_intangible_content_base_assetvsppne_21d_slope_v136_signal,
    f26ic_f26_intangible_content_base_assetvsppne_63d_slope_v137_signal,
    f26ic_f26_intangible_content_base_assetvsppne_126d_slope_v138_signal,
    f26ic_f26_intangible_content_base_assetvsppne_252d_slope_v139_signal,
    f26ic_f26_intangible_content_base_assetvsppne_504d_slope_v140_signal,
    f26ic_f26_intangible_content_base_intangvsppne_21d_slope_v141_signal,
    f26ic_f26_intangible_content_base_intangvsppne_63d_slope_v142_signal,
    f26ic_f26_intangible_content_base_intangvsppne_126d_slope_v143_signal,
    f26ic_f26_intangible_content_base_intangvsppne_252d_slope_v144_signal,
    f26ic_f26_intangible_content_base_intangvsppne_504d_slope_v145_signal,
    f26ic_f26_intangible_content_base_tangvsasset_21d_slope_v146_signal,
    f26ic_f26_intangible_content_base_tangvsasset_63d_slope_v147_signal,
    f26ic_f26_intangible_content_base_tangvsasset_126d_slope_v148_signal,
    f26ic_f26_intangible_content_base_tangvsasset_252d_slope_v149_signal,
    f26ic_f26_intangible_content_base_tangvsasset_504d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F26_INTANGIBLE_CONTENT_BASE_REGISTRY_2ND_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    ALLOW = {
        "open", "high", "low", "close", "closeadj", "volume",
        "revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc",
        "opex", "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin",
        "netinc", "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps",
        "ncfo", "ncff", "ncfi", "ncfcommon", "ncfdebt", "ncfbus", "capex",
        "depamor", "sharesbas", "shareswa", "shareswadil", "assets", "assetsc",
        "tangibles", "intangibles", "ppnenet", "investments", "inventory",
        "receivables", "payables", "equity", "retearn", "workingcapital", "debt",
        "debtc", "debtnc", "liabilities", "liabilitiesc", "cashneq", "currentratio",
        "roic", "roe", "roa", "ros", "assetturnover", "invcap", "intexp", "taxexp",
        "ebt", "sps", "bvps", "de", "ncfdiv", "dps", "divyield", "payoutratio",
        "prefdivis", "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
        "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal",
        "fndholders", "undholders", "prfholders", "dbtholders", "putholders",
        "putvalue", "cllholders", "cllvalue", "wntholders", "wntvalue", "dbtvalue",
    }

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    def _wig(seed, amp):
        g = np.random.default_rng(seed)
        w = np.cumsum(g.normal(0.0, amp, n))
        w = w - pd.Series(w).rolling(126, min_periods=1).mean().values
        return np.exp(w)

    assets = _fund(2601, base=1.0e9, drift=0.030, vol=0.06).rename("assets")
    assets = (assets * _wig(3601, 0.022)).rename("assets")
    ishare = _fund(2602, base=0.30, drift=0.010, vol=0.05)
    ishare = (0.16 + 0.20 * (ishare / ishare.iloc[0]).clip(0.6, 1.4) / 1.4) * _wig(3602, 0.030)
    intangibles = (assets * ishare).rename("intangibles")
    tshare = _fund(2603, base=0.28, drift=0.008, vol=0.045)
    tshare = (0.18 + 0.16 * (tshare / tshare.iloc[0]).clip(0.6, 1.4) / 1.4) * _wig(3603, 0.026)
    tangibles = (assets * tshare).rename("tangibles")
    ppshare = _fund(2604, base=0.16, drift=0.012, vol=0.06)
    ppshare = (0.09 + 0.11 * (ppshare / ppshare.iloc[0]).clip(0.6, 1.4) / 1.4) * _wig(3604, 0.034)
    ppnenet = (assets * ppshare).rename("ppnenet")
    dpace = _fund(2605, base=0.08, drift=0.006, vol=0.10)
    dpace = (0.05 + 0.09 * (dpace / dpace.iloc[0]).clip(0.5, 1.6) / 1.6) * _wig(3605, 0.050)
    depamor = ((intangibles + ppnenet) * dpace).rename("depamor")

    assert (intangibles > 0).all() and (tangibles > 0).all()
    assert (ppnenet > 0).all() and (depamor > 0).all() and (assets > 0).all()
    assert (intangibles < assets).all() and (tangibles < assets).all()
    assert ((intangibles + tangibles) <= assets).all()

    cols = {
        "intangibles": intangibles, "assets": assets, "depamor": depamor,
        "ppnenet": ppnenet, "tangibles": tangibles,
    }

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

    print("OK f26_intangible_content_base_2nd_derivatives_001_150_claude: %d features pass" % n_features)
