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
def _f14_goodwill_ratio(intangibles, assets):
    return intangibles / assets.replace(0, np.nan)


def _f14_goodwill_cycle(intangibles, assets, w):
    r = intangibles / assets.replace(0, np.nan)
    return r - r.rolling(w, min_periods=max(1, w // 2)).mean()


def _f14_goodwill_burden(intangibles, equity, w):
    r = intangibles / equity.replace(0, np.nan)
    return r - r.rolling(w, min_periods=max(1, w // 2)).mean()



def f14gic_f14_goodwill_intensity_cycle_gwratio_5d_base_v001_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_ratio(intangibles, assets)
    result = base * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwratio_10d_base_v002_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_ratio(intangibles, assets)
    result = base * _mean(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwratio_21d_base_v003_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_ratio(intangibles, assets)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwratio_42d_base_v004_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_ratio(intangibles, assets)
    result = base * _mean(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwratio_63d_base_v005_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_ratio(intangibles, assets)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwratio_126d_base_v006_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_ratio(intangibles, assets)
    result = base * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwratio_189d_base_v007_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_ratio(intangibles, assets)
    result = base * _mean(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwratio_252d_base_v008_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_ratio(intangibles, assets)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwratio_378d_base_v009_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_ratio(intangibles, assets)
    result = base * _mean(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwratio_504d_base_v010_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_ratio(intangibles, assets)
    result = base * _mean(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwratiosd_5d_base_v011_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_ratio(intangibles, assets)
    result = base * _std(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwratiosd_10d_base_v012_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_ratio(intangibles, assets)
    result = base * _std(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwratiosd_21d_base_v013_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_ratio(intangibles, assets)
    result = base * _std(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwratiosd_42d_base_v014_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_ratio(intangibles, assets)
    result = base * _std(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwratiosd_63d_base_v015_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_ratio(intangibles, assets)
    result = base * _std(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwratiosd_126d_base_v016_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_ratio(intangibles, assets)
    result = base * _std(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwratiosd_189d_base_v017_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_ratio(intangibles, assets)
    result = base * _std(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwratiosd_252d_base_v018_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_ratio(intangibles, assets)
    result = base * _std(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwratiosd_378d_base_v019_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_ratio(intangibles, assets)
    result = base * _std(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwratiosd_504d_base_v020_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_ratio(intangibles, assets)
    result = base * _std(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwratiosh_5d_base_v021_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_ratio(intangibles, assets)
    result = base.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwratiosh_10d_base_v022_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_ratio(intangibles, assets)
    result = base.shift(10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwratiosh_21d_base_v023_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_ratio(intangibles, assets)
    result = base.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwratiosh_42d_base_v024_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_ratio(intangibles, assets)
    result = base.shift(42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwratiosh_63d_base_v025_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_ratio(intangibles, assets)
    result = base.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwratiosh_126d_base_v026_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_ratio(intangibles, assets)
    result = base.shift(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwratiosh_189d_base_v027_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_ratio(intangibles, assets)
    result = base.shift(189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwratiosh_252d_base_v028_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_ratio(intangibles, assets)
    result = base.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwratiosh_378d_base_v029_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_ratio(intangibles, assets)
    result = base.shift(378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwratiosh_504d_base_v030_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_ratio(intangibles, assets)
    result = base.shift(504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwcycle_21d_base_v031_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_cycle(intangibles, assets, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwcycle_42d_base_v032_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_cycle(intangibles, assets, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwcycle_63d_base_v033_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_cycle(intangibles, assets, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwcycle_126d_base_v034_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_cycle(intangibles, assets, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwcycle_189d_base_v035_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_cycle(intangibles, assets, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwcycle_252d_base_v036_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_cycle(intangibles, assets, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwcycle_378d_base_v037_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_cycle(intangibles, assets, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwcycle_504d_base_v038_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_cycle(intangibles, assets, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwcyclelog_21d_base_v039_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_cycle(intangibles, assets, 21)
    result = base * np.log(closeadj.clip(lower=1e-9))
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwcyclelog_42d_base_v040_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_cycle(intangibles, assets, 42)
    result = base * np.log(closeadj.clip(lower=1e-9))
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwcyclelog_63d_base_v041_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_cycle(intangibles, assets, 63)
    result = base * np.log(closeadj.clip(lower=1e-9))
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwcyclelog_126d_base_v042_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_cycle(intangibles, assets, 126)
    result = base * np.log(closeadj.clip(lower=1e-9))
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwcyclelog_189d_base_v043_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_cycle(intangibles, assets, 189)
    result = base * np.log(closeadj.clip(lower=1e-9))
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwcyclelog_252d_base_v044_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_cycle(intangibles, assets, 252)
    result = base * np.log(closeadj.clip(lower=1e-9))
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwcyclelog_378d_base_v045_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_cycle(intangibles, assets, 378)
    result = base * np.log(closeadj.clip(lower=1e-9))
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwcyclelog_504d_base_v046_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_cycle(intangibles, assets, 504)
    result = base * np.log(closeadj.clip(lower=1e-9))
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwcyclesq_21d_base_v047_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_cycle(intangibles, assets, 21)
    result = (base * base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwcyclesq_42d_base_v048_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_cycle(intangibles, assets, 42)
    result = (base * base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwcyclesq_63d_base_v049_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_cycle(intangibles, assets, 63)
    result = (base * base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwcyclesq_126d_base_v050_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_cycle(intangibles, assets, 126)
    result = (base * base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwcyclesq_189d_base_v051_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_cycle(intangibles, assets, 189)
    result = (base * base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwcyclesq_252d_base_v052_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_cycle(intangibles, assets, 252)
    result = (base * base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwcyclesq_378d_base_v053_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_cycle(intangibles, assets, 378)
    result = (base * base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwcyclesq_504d_base_v054_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_cycle(intangibles, assets, 504)
    result = (base * base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwburden_21d_base_v055_signal(intangibles, equity, closeadj):
    base = _f14_goodwill_burden(intangibles, equity, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwburden_42d_base_v056_signal(intangibles, equity, closeadj):
    base = _f14_goodwill_burden(intangibles, equity, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwburden_63d_base_v057_signal(intangibles, equity, closeadj):
    base = _f14_goodwill_burden(intangibles, equity, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwburden_126d_base_v058_signal(intangibles, equity, closeadj):
    base = _f14_goodwill_burden(intangibles, equity, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwburden_189d_base_v059_signal(intangibles, equity, closeadj):
    base = _f14_goodwill_burden(intangibles, equity, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwburden_252d_base_v060_signal(intangibles, equity, closeadj):
    base = _f14_goodwill_burden(intangibles, equity, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwburden_378d_base_v061_signal(intangibles, equity, closeadj):
    base = _f14_goodwill_burden(intangibles, equity, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwburden_504d_base_v062_signal(intangibles, equity, closeadj):
    base = _f14_goodwill_burden(intangibles, equity, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwburdenlog_21d_base_v063_signal(intangibles, equity, closeadj):
    base = _f14_goodwill_burden(intangibles, equity, 21)
    result = base * np.log(closeadj.clip(lower=1e-9))
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwburdenlog_42d_base_v064_signal(intangibles, equity, closeadj):
    base = _f14_goodwill_burden(intangibles, equity, 42)
    result = base * np.log(closeadj.clip(lower=1e-9))
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwburdenlog_63d_base_v065_signal(intangibles, equity, closeadj):
    base = _f14_goodwill_burden(intangibles, equity, 63)
    result = base * np.log(closeadj.clip(lower=1e-9))
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwburdenlog_126d_base_v066_signal(intangibles, equity, closeadj):
    base = _f14_goodwill_burden(intangibles, equity, 126)
    result = base * np.log(closeadj.clip(lower=1e-9))
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwburdenlog_189d_base_v067_signal(intangibles, equity, closeadj):
    base = _f14_goodwill_burden(intangibles, equity, 189)
    result = base * np.log(closeadj.clip(lower=1e-9))
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwburdenlog_252d_base_v068_signal(intangibles, equity, closeadj):
    base = _f14_goodwill_burden(intangibles, equity, 252)
    result = base * np.log(closeadj.clip(lower=1e-9))
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwburdenlog_378d_base_v069_signal(intangibles, equity, closeadj):
    base = _f14_goodwill_burden(intangibles, equity, 378)
    result = base * np.log(closeadj.clip(lower=1e-9))
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwburdenlog_504d_base_v070_signal(intangibles, equity, closeadj):
    base = _f14_goodwill_burden(intangibles, equity, 504)
    result = base * np.log(closeadj.clip(lower=1e-9))
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwcyclem_21d_21_base_v071_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_cycle(intangibles, assets, 21)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwcyclem_21d_63_base_v072_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_cycle(intangibles, assets, 21)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwcyclem_21d_126_base_v073_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_cycle(intangibles, assets, 21)
    result = base * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwcyclem_21d_252_base_v074_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_cycle(intangibles, assets, 21)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f14gic_f14_goodwill_intensity_cycle_gwcyclem_63d_21_base_v075_signal(intangibles, assets, closeadj):
    base = _f14_goodwill_cycle(intangibles, assets, 63)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f14gic_f14_goodwill_intensity_cycle_gwratio_5d_base_v001_signal,
    f14gic_f14_goodwill_intensity_cycle_gwratio_10d_base_v002_signal,
    f14gic_f14_goodwill_intensity_cycle_gwratio_21d_base_v003_signal,
    f14gic_f14_goodwill_intensity_cycle_gwratio_42d_base_v004_signal,
    f14gic_f14_goodwill_intensity_cycle_gwratio_63d_base_v005_signal,
    f14gic_f14_goodwill_intensity_cycle_gwratio_126d_base_v006_signal,
    f14gic_f14_goodwill_intensity_cycle_gwratio_189d_base_v007_signal,
    f14gic_f14_goodwill_intensity_cycle_gwratio_252d_base_v008_signal,
    f14gic_f14_goodwill_intensity_cycle_gwratio_378d_base_v009_signal,
    f14gic_f14_goodwill_intensity_cycle_gwratio_504d_base_v010_signal,
    f14gic_f14_goodwill_intensity_cycle_gwratiosd_5d_base_v011_signal,
    f14gic_f14_goodwill_intensity_cycle_gwratiosd_10d_base_v012_signal,
    f14gic_f14_goodwill_intensity_cycle_gwratiosd_21d_base_v013_signal,
    f14gic_f14_goodwill_intensity_cycle_gwratiosd_42d_base_v014_signal,
    f14gic_f14_goodwill_intensity_cycle_gwratiosd_63d_base_v015_signal,
    f14gic_f14_goodwill_intensity_cycle_gwratiosd_126d_base_v016_signal,
    f14gic_f14_goodwill_intensity_cycle_gwratiosd_189d_base_v017_signal,
    f14gic_f14_goodwill_intensity_cycle_gwratiosd_252d_base_v018_signal,
    f14gic_f14_goodwill_intensity_cycle_gwratiosd_378d_base_v019_signal,
    f14gic_f14_goodwill_intensity_cycle_gwratiosd_504d_base_v020_signal,
    f14gic_f14_goodwill_intensity_cycle_gwratiosh_5d_base_v021_signal,
    f14gic_f14_goodwill_intensity_cycle_gwratiosh_10d_base_v022_signal,
    f14gic_f14_goodwill_intensity_cycle_gwratiosh_21d_base_v023_signal,
    f14gic_f14_goodwill_intensity_cycle_gwratiosh_42d_base_v024_signal,
    f14gic_f14_goodwill_intensity_cycle_gwratiosh_63d_base_v025_signal,
    f14gic_f14_goodwill_intensity_cycle_gwratiosh_126d_base_v026_signal,
    f14gic_f14_goodwill_intensity_cycle_gwratiosh_189d_base_v027_signal,
    f14gic_f14_goodwill_intensity_cycle_gwratiosh_252d_base_v028_signal,
    f14gic_f14_goodwill_intensity_cycle_gwratiosh_378d_base_v029_signal,
    f14gic_f14_goodwill_intensity_cycle_gwratiosh_504d_base_v030_signal,
    f14gic_f14_goodwill_intensity_cycle_gwcycle_21d_base_v031_signal,
    f14gic_f14_goodwill_intensity_cycle_gwcycle_42d_base_v032_signal,
    f14gic_f14_goodwill_intensity_cycle_gwcycle_63d_base_v033_signal,
    f14gic_f14_goodwill_intensity_cycle_gwcycle_126d_base_v034_signal,
    f14gic_f14_goodwill_intensity_cycle_gwcycle_189d_base_v035_signal,
    f14gic_f14_goodwill_intensity_cycle_gwcycle_252d_base_v036_signal,
    f14gic_f14_goodwill_intensity_cycle_gwcycle_378d_base_v037_signal,
    f14gic_f14_goodwill_intensity_cycle_gwcycle_504d_base_v038_signal,
    f14gic_f14_goodwill_intensity_cycle_gwcyclelog_21d_base_v039_signal,
    f14gic_f14_goodwill_intensity_cycle_gwcyclelog_42d_base_v040_signal,
    f14gic_f14_goodwill_intensity_cycle_gwcyclelog_63d_base_v041_signal,
    f14gic_f14_goodwill_intensity_cycle_gwcyclelog_126d_base_v042_signal,
    f14gic_f14_goodwill_intensity_cycle_gwcyclelog_189d_base_v043_signal,
    f14gic_f14_goodwill_intensity_cycle_gwcyclelog_252d_base_v044_signal,
    f14gic_f14_goodwill_intensity_cycle_gwcyclelog_378d_base_v045_signal,
    f14gic_f14_goodwill_intensity_cycle_gwcyclelog_504d_base_v046_signal,
    f14gic_f14_goodwill_intensity_cycle_gwcyclesq_21d_base_v047_signal,
    f14gic_f14_goodwill_intensity_cycle_gwcyclesq_42d_base_v048_signal,
    f14gic_f14_goodwill_intensity_cycle_gwcyclesq_63d_base_v049_signal,
    f14gic_f14_goodwill_intensity_cycle_gwcyclesq_126d_base_v050_signal,
    f14gic_f14_goodwill_intensity_cycle_gwcyclesq_189d_base_v051_signal,
    f14gic_f14_goodwill_intensity_cycle_gwcyclesq_252d_base_v052_signal,
    f14gic_f14_goodwill_intensity_cycle_gwcyclesq_378d_base_v053_signal,
    f14gic_f14_goodwill_intensity_cycle_gwcyclesq_504d_base_v054_signal,
    f14gic_f14_goodwill_intensity_cycle_gwburden_21d_base_v055_signal,
    f14gic_f14_goodwill_intensity_cycle_gwburden_42d_base_v056_signal,
    f14gic_f14_goodwill_intensity_cycle_gwburden_63d_base_v057_signal,
    f14gic_f14_goodwill_intensity_cycle_gwburden_126d_base_v058_signal,
    f14gic_f14_goodwill_intensity_cycle_gwburden_189d_base_v059_signal,
    f14gic_f14_goodwill_intensity_cycle_gwburden_252d_base_v060_signal,
    f14gic_f14_goodwill_intensity_cycle_gwburden_378d_base_v061_signal,
    f14gic_f14_goodwill_intensity_cycle_gwburden_504d_base_v062_signal,
    f14gic_f14_goodwill_intensity_cycle_gwburdenlog_21d_base_v063_signal,
    f14gic_f14_goodwill_intensity_cycle_gwburdenlog_42d_base_v064_signal,
    f14gic_f14_goodwill_intensity_cycle_gwburdenlog_63d_base_v065_signal,
    f14gic_f14_goodwill_intensity_cycle_gwburdenlog_126d_base_v066_signal,
    f14gic_f14_goodwill_intensity_cycle_gwburdenlog_189d_base_v067_signal,
    f14gic_f14_goodwill_intensity_cycle_gwburdenlog_252d_base_v068_signal,
    f14gic_f14_goodwill_intensity_cycle_gwburdenlog_378d_base_v069_signal,
    f14gic_f14_goodwill_intensity_cycle_gwburdenlog_504d_base_v070_signal,
    f14gic_f14_goodwill_intensity_cycle_gwcyclem_21d_21_base_v071_signal,
    f14gic_f14_goodwill_intensity_cycle_gwcyclem_21d_63_base_v072_signal,
    f14gic_f14_goodwill_intensity_cycle_gwcyclem_21d_126_base_v073_signal,
    f14gic_f14_goodwill_intensity_cycle_gwcyclem_21d_252_base_v074_signal,
    f14gic_f14_goodwill_intensity_cycle_gwcyclem_63d_21_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F14_GOODWILL_INTENSITY_CYCLE_REGISTRY_001_075 = REGISTRY


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

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    rnd     = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    assetsc      = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsc")
    assetsnc     = pd.Series(1.2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsnc")
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    liabilitiesc = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesc")
    liabilitiesnc= pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesnc")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    equityusd    = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equityusd")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    debtc        = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtc")
    debtnc       = pd.Series(4.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtnc")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    intangibles  = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    tangibles    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="tangibles")
    invcap       = pd.Series(1.4e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="invcap")
    retearn      = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="retearn")
    sbcomp       = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="sbcomp")
    sharesbas    = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa     = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    shareswadil  = pd.Series(1.02e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswadil")
    eps          = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    epsdil       = pd.Series(0.98 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="epsdil")
    bvps         = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="bvps")
    fcfps        = pd.Series(0.8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcfps")
    sps          = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="sps")
    dps          = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    marketcap    = pd.Series(closeadj * 1e8, name="marketcap")
    ev           = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    pe           = pd.Series(closeadj / eps.replace(0, np.nan).abs(), name="pe")
    pb           = pd.Series(closeadj / bvps.replace(0, np.nan).abs(), name="pb")
    ps           = pd.Series(closeadj / sps.replace(0, np.nan).abs(), name="ps")
    evebit       = pd.Series(ev / ebit.replace(0, np.nan).abs(), name="evebit")
    evebitda     = pd.Series(ev / ebitda.replace(0, np.nan).abs(), name="evebitda")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")
    roa          = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe          = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ros          = pd.Series(0.08 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ros")
    currentratio = pd.Series(1.5 + 0.3*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="currentratio")
    de           = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")
    payoutratio  = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    divyield     = pd.Series(0.02 + 0.005*np.sin(np.arange(n)/250.0) + 0.001*np.random.randn(n), name="divyield")
    assetturnover= pd.Series(0.7 + 0.15*np.sin(np.arange(n)/250.0) + 0.02*np.random.randn(n), name="assetturnover")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "assets": assets, "assetsc": assetsc, "assetsnc": assetsnc,
        "liabilities": liabilities, "liabilitiesc": liabilitiesc, "liabilitiesnc": liabilitiesnc,
        "equity": equity, "equityusd": equityusd,
        "debt": debt, "debtc": debtc, "debtnc": debtnc, "cashneq": cashneq,
        "inventory": inventory, "receivables": receivables, "payables": payables,
        "deferredrev": deferredrev, "workingcapital": workingcapital,
        "ppnenet": ppnenet, "intangibles": intangibles, "tangibles": tangibles,
        "invcap": invcap, "retearn": retearn, "sbcomp": sbcomp,
        "sharesbas": sharesbas, "shareswa": shareswa, "shareswadil": shareswadil,
        "eps": eps, "epsdil": epsdil, "bvps": bvps, "fcfps": fcfps, "sps": sps, "dps": dps,
        "marketcap": marketcap, "ev": ev,
        "pe": pe, "pb": pb, "ps": ps, "evebit": evebit, "evebitda": evebitda,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
        "roa": roa, "roe": roe, "roic": roic, "ros": ros,
        "currentratio": currentratio, "de": de,
        "payoutratio": payoutratio, "divyield": divyield, "assetturnover": assetturnover,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f14_goodwill_ratio", "_f14_goodwill_cycle", "_f14_goodwill_burden")
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
    print(f"OK goodwill_intensity_cycle_base_001_075_claude: {n_features} features pass")
