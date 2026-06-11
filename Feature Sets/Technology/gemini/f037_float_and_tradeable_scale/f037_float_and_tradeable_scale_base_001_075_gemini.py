import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core00-09: mean 4q
def cg_f037_float_and_tradeable_scale_core00_mean_4q_v001_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_mean(marketcap, 4))
def cg_f037_float_and_tradeable_scale_core01_mean_4q_v002_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_mean(_safe_div(marketcap, assets), 4))
def cg_f037_float_and_tradeable_scale_core02_mean_4q_v003_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_mean(_safe_div(marketcap, revenue), 4))
def cg_f037_float_and_tradeable_scale_core03_mean_4q_v004_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    # turnover proxy: (volume * price / marketcap) is constant if price is same. 
    # but we only have marketcap and volume. (marketcap / sharesbas) = price.
    # turnover = (volume * (marketcap / sharesbas)) / marketcap = volume / sharesbas.
    return _clean(_mean(_safe_div(volume, sharesbas), 4))
def cg_f037_float_and_tradeable_scale_core04_mean_4q_v005_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_mean(_safe_div(marketcap, ncfo.abs() + 1.0), 4))
def cg_f037_float_and_tradeable_scale_core05_mean_4q_v006_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_mean(_safe_div(marketcap, equity.abs() + 1.0), 4))
def cg_f037_float_and_tradeable_scale_core06_mean_4q_v007_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_mean(_safe_div(marketcap, opex.abs() + 1.0), 4))
def cg_f037_float_and_tradeable_scale_core07_mean_4q_v008_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_mean(_pct_change(marketcap, 4), 4))
def cg_f037_float_and_tradeable_scale_core08_mean_4q_v009_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_mean(_safe_div(volume, sharesbas * 100.0), 4))
def cg_f037_float_and_tradeable_scale_core09_mean_4q_v010_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_mean(_log(marketcap.clip(lower=1.0)), 4))

# core10-19: mean 8q
def cg_f037_float_and_tradeable_scale_core10_mean_8q_v011_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_mean(marketcap, 8))
def cg_f037_float_and_tradeable_scale_core11_mean_8q_v012_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_mean(_safe_div(marketcap, assets), 8))
def cg_f037_float_and_tradeable_scale_core12_mean_8q_v013_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_mean(_safe_div(marketcap, revenue), 8))
def cg_f037_float_and_tradeable_scale_core13_mean_8q_v014_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_mean(_safe_div(volume, sharesbas), 8))
def cg_f037_float_and_tradeable_scale_core14_mean_8q_v015_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_mean(_safe_div(marketcap, ncfo.abs() + 1.0), 8))
def cg_f037_float_and_tradeable_scale_core15_mean_8q_v016_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_mean(_safe_div(marketcap, equity.abs() + 1.0), 8))
def cg_f037_float_and_tradeable_scale_core16_mean_8q_v017_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_mean(_safe_div(marketcap, opex.abs() + 1.0), 8))
def cg_f037_float_and_tradeable_scale_core17_mean_8q_v018_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_mean(_pct_change(marketcap, 4), 8))
def cg_f037_float_and_tradeable_scale_core18_mean_8q_v019_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_mean(_safe_div(volume, sharesbas * 100.0), 8))
def cg_f037_float_and_tradeable_scale_core19_mean_8q_v020_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_mean(_log(marketcap.clip(lower=1.0)), 8))

# core20-29: z 8q
def cg_f037_float_and_tradeable_scale_core20_z_8q_v021_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_z(marketcap, 8))
def cg_f037_float_and_tradeable_scale_core21_z_8q_v022_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_z(_safe_div(marketcap, assets), 8))
def cg_f037_float_and_tradeable_scale_core22_z_8q_v023_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_z(_safe_div(marketcap, revenue), 8))
def cg_f037_float_and_tradeable_scale_core23_z_8q_v024_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_z(_safe_div(volume, sharesbas), 8))
def cg_f037_float_and_tradeable_scale_core24_z_8q_v025_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_z(_safe_div(marketcap, ncfo.abs() + 1.0), 8))
def cg_f037_float_and_tradeable_scale_core25_z_8q_v026_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_z(_safe_div(marketcap, equity.abs() + 1.0), 8))
def cg_f037_float_and_tradeable_scale_core26_z_8q_v027_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_z(_safe_div(marketcap, opex.abs() + 1.0), 8))
def cg_f037_float_and_tradeable_scale_core27_z_8q_v028_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_z(_pct_change(marketcap, 4), 8))
def cg_f037_float_and_tradeable_scale_core28_z_8q_v029_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_z(_safe_div(volume, sharesbas * 100.0), 8))
def cg_f037_float_and_tradeable_scale_core29_z_8q_v030_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_z(_log(marketcap.clip(lower=1.0)), 8))

# core30-39: z 20q
def cg_f037_float_and_tradeable_scale_core30_z_20q_v031_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_z(marketcap, 20))
def cg_f037_float_and_tradeable_scale_core31_z_20q_v032_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_z(_safe_div(marketcap, assets), 20))
def cg_f037_float_and_tradeable_scale_core32_z_20q_v033_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_z(_safe_div(marketcap, revenue), 20))
def cg_f037_float_and_tradeable_scale_core33_z_20q_v034_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_z(_safe_div(volume, sharesbas), 20))
def cg_f037_float_and_tradeable_scale_core34_z_20q_v035_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_z(_safe_div(marketcap, ncfo.abs() + 1.0), 20))
def cg_f037_float_and_tradeable_scale_core35_z_20q_v036_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_z(_safe_div(marketcap, equity.abs() + 1.0), 20))
def cg_f037_float_and_tradeable_scale_core36_z_20q_v037_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_z(_safe_div(marketcap, opex.abs() + 1.0), 20))
def cg_f037_float_and_tradeable_scale_core37_z_20q_v038_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_z(_pct_change(marketcap, 4), 20))
def cg_f037_float_and_tradeable_scale_core38_z_20q_v039_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_z(_safe_div(volume, sharesbas * 100.0), 20))
def cg_f037_float_and_tradeable_scale_core39_z_20q_v040_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_z(_log(marketcap.clip(lower=1.0)), 20))

# core40-49: rank 12q
def cg_f037_float_and_tradeable_scale_core40_rank_12q_v041_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_rank(marketcap, 12))
def cg_f037_float_and_tradeable_scale_core41_rank_12q_v042_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_rank(_safe_div(marketcap, assets), 12))
def cg_f037_float_and_tradeable_scale_core42_rank_12q_v043_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_rank(_safe_div(marketcap, revenue), 12))
def cg_f037_float_and_tradeable_scale_core43_rank_12q_v044_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_rank(_safe_div(volume, sharesbas), 12))
def cg_f037_float_and_tradeable_scale_core44_rank_12q_v045_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_rank(_safe_div(marketcap, ncfo.abs() + 1.0), 12))
def cg_f037_float_and_tradeable_scale_core45_rank_12q_v046_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_rank(_safe_div(marketcap, equity.abs() + 1.0), 12))
def cg_f037_float_and_tradeable_scale_core46_rank_12q_v047_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_rank(_safe_div(marketcap, opex.abs() + 1.0), 12))
def cg_f037_float_and_tradeable_scale_core47_rank_12q_v048_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_rank(_pct_change(marketcap, 4), 12))
def cg_f037_float_and_tradeable_scale_core48_rank_12q_v049_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_rank(_safe_div(volume, sharesbas * 100.0), 12))
def cg_f037_float_and_tradeable_scale_core49_rank_12q_v050_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_rank(_log(marketcap.clip(lower=1.0)), 12))

# core50-59: rank 20q
def cg_f037_float_and_tradeable_scale_core50_rank_20q_v051_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_rank(marketcap, 20))
def cg_f037_float_and_tradeable_scale_core51_rank_20q_v052_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_rank(_safe_div(marketcap, assets), 20))
def cg_f037_float_and_tradeable_scale_core52_rank_20q_v053_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_rank(_safe_div(marketcap, revenue), 20))
def cg_f037_float_and_tradeable_scale_core53_rank_20q_v054_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_rank(_safe_div(volume, sharesbas), 20))
def cg_f037_float_and_tradeable_scale_core54_rank_20q_v055_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_rank(_safe_div(marketcap, ncfo.abs() + 1.0), 20))
def cg_f037_float_and_tradeable_scale_core55_rank_20q_v056_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_rank(_safe_div(marketcap, equity.abs() + 1.0), 20))
def cg_f037_float_and_tradeable_scale_core56_rank_20q_v057_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_rank(_safe_div(marketcap, opex.abs() + 1.0), 20))
def cg_f037_float_and_tradeable_scale_core57_rank_20q_v058_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_rank(_pct_change(marketcap, 4), 20))
def cg_f037_float_and_tradeable_scale_core58_rank_20q_v059_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_rank(_safe_div(volume, sharesbas * 100.0), 20))
def cg_f037_float_and_tradeable_scale_core59_rank_20q_v060_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_rank(_log(marketcap.clip(lower=1.0)), 20))

# core60-69: pct 1q
def cg_f037_float_and_tradeable_scale_core60_pct_1q_v061_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_pct_change(marketcap, 1))
def cg_f037_float_and_tradeable_scale_core61_pct_1q_v062_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_pct_change(_safe_div(marketcap, assets), 1))
def cg_f037_float_and_tradeable_scale_core62_pct_1q_v063_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_pct_change(_safe_div(marketcap, revenue), 1))
def cg_f037_float_and_tradeable_scale_core63_pct_1q_v064_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_pct_change(_safe_div(volume, sharesbas), 1))
def cg_f037_float_and_tradeable_scale_core64_pct_1q_v065_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_pct_change(_safe_div(marketcap, ncfo.abs() + 1.0), 1))
def cg_f037_float_and_tradeable_scale_core65_pct_1q_v066_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_pct_change(_safe_div(marketcap, equity.abs() + 1.0), 1))
def cg_f037_float_and_tradeable_scale_core66_pct_1q_v067_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_pct_change(_safe_div(marketcap, opex.abs() + 1.0), 1))
def cg_f037_float_and_tradeable_scale_core67_pct_1q_v068_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_pct_change(_pct_change(marketcap, 4), 1))
def cg_f037_float_and_tradeable_scale_core68_pct_1q_v069_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_pct_change(_safe_div(volume, sharesbas * 100.0), 1))
def cg_f037_float_and_tradeable_scale_core69_pct_1q_v070_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_pct_change(_log(marketcap.clip(lower=1.0)), 1))

# core70-74: pct 4q
def cg_f037_float_and_tradeable_scale_core70_pct_4q_v071_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_pct_change(marketcap, 4))
def cg_f037_float_and_tradeable_scale_core71_pct_4q_v072_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_pct_change(_safe_div(marketcap, assets), 4))
def cg_f037_float_and_tradeable_scale_core72_pct_4q_v073_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_pct_change(_safe_div(marketcap, revenue), 4))
def cg_f037_float_and_tradeable_scale_core73_pct_4q_v074_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_pct_change(_safe_div(volume, sharesbas), 4))
def cg_f037_float_and_tradeable_scale_core74_pct_4q_v075_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_pct_change(_safe_div(marketcap, ncfo.abs() + 1.0), 4))
