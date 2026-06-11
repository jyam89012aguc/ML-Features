import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core00-09: mean 4q
def cg_f035_buyback_share_reduction_core00_mean_4q_v001_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    reduction = _pct_change(sharesbas, 1).clip(upper=0).abs()
    return _clean(_mean(reduction, 4))
def cg_f035_buyback_share_reduction_core01_mean_4q_v002_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_mean(_safe_div(ncff, marketcap), 4))
def cg_f035_buyback_share_reduction_core02_mean_4q_v003_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_mean(_safe_div(ncff, ncfo.abs() + 1.0), 4))
def cg_f035_buyback_share_reduction_core03_mean_4q_v004_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    reduction = _pct_change(sharesbas, 4).clip(upper=0).abs()
    return _clean(_mean(reduction, 4))
def cg_f035_buyback_share_reduction_core04_mean_4q_v005_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_mean(_safe_div(ncff, assets), 4))
def cg_f035_buyback_share_reduction_core05_mean_4q_v006_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_mean(_safe_div(ncff, revenue), 4))
def cg_f035_buyback_share_reduction_core06_mean_4q_v007_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    reduction_value = _pct_change(sharesbas, 1).clip(upper=0).abs() * marketcap
    return _clean(_mean(_safe_div(reduction_value, ncfo.abs() + 1.0), 4))
def cg_f035_buyback_share_reduction_core07_mean_4q_v008_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_mean(_safe_div(ncff, equity.abs() + 1.0), 4))
def cg_f035_buyback_share_reduction_core08_mean_4q_v009_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_mean(ncff, 4))
def cg_f035_buyback_share_reduction_core09_mean_4q_v010_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_mean(_log(sharesbas.clip(lower=1.0)), 4))

# core10-19: mean 8q
def cg_f035_buyback_share_reduction_core10_mean_8q_v011_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    reduction = _pct_change(sharesbas, 1).clip(upper=0).abs()
    return _clean(_mean(reduction, 8))
def cg_f035_buyback_share_reduction_core11_mean_8q_v012_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_mean(_safe_div(ncff, marketcap), 8))
def cg_f035_buyback_share_reduction_core12_mean_8q_v013_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_mean(_safe_div(ncff, ncfo.abs() + 1.0), 8))
def cg_f035_buyback_share_reduction_core13_mean_8q_v014_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    reduction = _pct_change(sharesbas, 4).clip(upper=0).abs()
    return _clean(_mean(reduction, 8))
def cg_f035_buyback_share_reduction_core14_mean_8q_v015_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_mean(_safe_div(ncff, assets), 8))
def cg_f035_buyback_share_reduction_core15_mean_8q_v016_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_mean(_safe_div(ncff, revenue), 8))
def cg_f035_buyback_share_reduction_core16_mean_8q_v017_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    reduction_value = _pct_change(sharesbas, 1).clip(upper=0).abs() * marketcap
    return _clean(_mean(_safe_div(reduction_value, ncfo.abs() + 1.0), 8))
def cg_f035_buyback_share_reduction_core17_mean_8q_v018_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_mean(_safe_div(ncff, equity.abs() + 1.0), 8))
def cg_f035_buyback_share_reduction_core18_mean_8q_v019_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_mean(ncff, 8))
def cg_f035_buyback_share_reduction_core19_mean_8q_v020_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_mean(_log(sharesbas.clip(lower=1.0)), 8))

# core20-29: z 8q
def cg_f035_buyback_share_reduction_core20_z_8q_v021_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    reduction = _pct_change(sharesbas, 1).clip(upper=0).abs()
    return _clean(_z(reduction, 8))
def cg_f035_buyback_share_reduction_core21_z_8q_v022_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_z(_safe_div(ncff, marketcap), 8))
def cg_f035_buyback_share_reduction_core22_z_8q_v023_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_z(_safe_div(ncff, ncfo.abs() + 1.0), 8))
def cg_f035_buyback_share_reduction_core23_z_8q_v024_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    reduction = _pct_change(sharesbas, 4).clip(upper=0).abs()
    return _clean(_z(reduction, 8))
def cg_f035_buyback_share_reduction_core24_z_8q_v025_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_z(_safe_div(ncff, assets), 8))
def cg_f035_buyback_share_reduction_core25_z_8q_v026_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_z(_safe_div(ncff, revenue), 8))
def cg_f035_buyback_share_reduction_core26_z_8q_v027_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    reduction_value = _pct_change(sharesbas, 1).clip(upper=0).abs() * marketcap
    return _clean(_z(_safe_div(reduction_value, ncfo.abs() + 1.0), 8))
def cg_f035_buyback_share_reduction_core27_z_8q_v028_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_z(_safe_div(ncff, equity.abs() + 1.0), 8))
def cg_f035_buyback_share_reduction_core28_z_8q_v029_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_z(ncff, 8))
def cg_f035_buyback_share_reduction_core29_z_8q_v030_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_z(_log(sharesbas.clip(lower=1.0)), 8))

# core30-39: z 20q
def cg_f035_buyback_share_reduction_core30_z_20q_v031_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    reduction = _pct_change(sharesbas, 1).clip(upper=0).abs()
    return _clean(_z(reduction, 20))
def cg_f035_buyback_share_reduction_core31_z_20q_v032_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_z(_safe_div(ncff, marketcap), 20))
def cg_f035_buyback_share_reduction_core32_z_20q_v033_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_z(_safe_div(ncff, ncfo.abs() + 1.0), 20))
def cg_f035_buyback_share_reduction_core33_z_20q_v034_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    reduction = _pct_change(sharesbas, 4).clip(upper=0).abs()
    return _clean(_z(reduction, 20))
def cg_f035_buyback_share_reduction_core34_z_20q_v035_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_z(_safe_div(ncff, assets), 20))
def cg_f035_buyback_share_reduction_core35_z_20q_v036_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_z(_safe_div(ncff, revenue), 20))
def cg_f035_buyback_share_reduction_core36_z_20q_v037_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    reduction_value = _pct_change(sharesbas, 1).clip(upper=0).abs() * marketcap
    return _clean(_z(_safe_div(reduction_value, ncfo.abs() + 1.0), 20))
def cg_f035_buyback_share_reduction_core37_z_20q_v038_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_z(_safe_div(ncff, equity.abs() + 1.0), 20))
def cg_f035_buyback_share_reduction_core38_z_20q_v039_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_z(ncff, 20))
def cg_f035_buyback_share_reduction_core39_z_20q_v040_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_z(_log(sharesbas.clip(lower=1.0)), 20))

# core40-49: rank 12q
def cg_f035_buyback_share_reduction_core40_rank_12q_v041_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    reduction = _pct_change(sharesbas, 1).clip(upper=0).abs()
    return _clean(_rank(reduction, 12))
def cg_f035_buyback_share_reduction_core41_rank_12q_v042_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_rank(_safe_div(ncff, marketcap), 12))
def cg_f035_buyback_share_reduction_core42_rank_12q_v043_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_rank(_safe_div(ncff, ncfo.abs() + 1.0), 12))
def cg_f035_buyback_share_reduction_core43_rank_12q_v044_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    reduction = _pct_change(sharesbas, 4).clip(upper=0).abs()
    return _clean(_rank(reduction, 12))
def cg_f035_buyback_share_reduction_core44_rank_12q_v045_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_rank(_safe_div(ncff, assets), 12))
def cg_f035_buyback_share_reduction_core45_rank_12q_v046_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_rank(_safe_div(ncff, revenue), 12))
def cg_f035_buyback_share_reduction_core46_rank_12q_v047_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    reduction_value = _pct_change(sharesbas, 1).clip(upper=0).abs() * marketcap
    return _clean(_rank(_safe_div(reduction_value, ncfo.abs() + 1.0), 12))
def cg_f035_buyback_share_reduction_core47_rank_12q_v048_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_rank(_safe_div(ncff, equity.abs() + 1.0), 12))
def cg_f035_buyback_share_reduction_core48_rank_12q_v049_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_rank(ncff, 12))
def cg_f035_buyback_share_reduction_core49_rank_12q_v050_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_rank(_log(sharesbas.clip(lower=1.0)), 12))

# core50-59: rank 20q
def cg_f035_buyback_share_reduction_core50_rank_20q_v051_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    reduction = _pct_change(sharesbas, 1).clip(upper=0).abs()
    return _clean(_rank(reduction, 20))
def cg_f035_buyback_share_reduction_core51_rank_20q_v052_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_rank(_safe_div(ncff, marketcap), 20))
def cg_f035_buyback_share_reduction_core52_rank_20q_v053_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_rank(_safe_div(ncff, ncfo.abs() + 1.0), 20))
def cg_f035_buyback_share_reduction_core53_rank_20q_v054_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    reduction = _pct_change(sharesbas, 4).clip(upper=0).abs()
    return _clean(_rank(reduction, 20))
def cg_f035_buyback_share_reduction_core54_rank_20q_v055_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_rank(_safe_div(ncff, assets), 20))
def cg_f035_buyback_share_reduction_core55_rank_20q_v056_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_rank(_safe_div(ncff, revenue), 20))
def cg_f035_buyback_share_reduction_core56_rank_20q_v057_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    reduction_value = _pct_change(sharesbas, 1).clip(upper=0).abs() * marketcap
    return _clean(_rank(_safe_div(reduction_value, ncfo.abs() + 1.0), 20))
def cg_f035_buyback_share_reduction_core57_rank_20q_v058_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_rank(_safe_div(ncff, equity.abs() + 1.0), 20))
def cg_f035_buyback_share_reduction_core58_rank_20q_v059_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_rank(ncff, 20))
def cg_f035_buyback_share_reduction_core59_rank_20q_v060_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_rank(_log(sharesbas.clip(lower=1.0)), 20))

# core60-69: pct 1q
def cg_f035_buyback_share_reduction_core60_pct_1q_v061_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    reduction = _pct_change(sharesbas, 1).clip(upper=0).abs()
    return _clean(_pct_change(reduction, 1))
def cg_f035_buyback_share_reduction_core61_pct_1q_v062_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_pct_change(_safe_div(ncff, marketcap), 1))
def cg_f035_buyback_share_reduction_core62_pct_1q_v063_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_pct_change(_safe_div(ncff, ncfo.abs() + 1.0), 1))
def cg_f035_buyback_share_reduction_core63_pct_1q_v064_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_pct_change(_safe_div(ncff, assets), 1))
def cg_f035_buyback_share_reduction_core64_pct_1q_v065_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_pct_change(_safe_div(ncff, revenue), 1))
def cg_f035_buyback_share_reduction_core65_pct_1q_v066_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    reduction_value = _pct_change(sharesbas, 1).clip(upper=0).abs() * marketcap
    return _clean(_pct_change(_safe_div(reduction_value, ncfo.abs() + 1.0), 1))
def cg_f035_buyback_share_reduction_core66_pct_1q_v067_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_pct_change(_diff(sharesbas, 4).clip(upper=0).abs(), 1))
def cg_f035_buyback_share_reduction_core67_pct_1q_v068_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_pct_change(_safe_div(ncff, equity.abs() + 1.0), 1))
def cg_f035_buyback_share_reduction_core68_pct_1q_v069_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_pct_change(ncff, 1))
def cg_f035_buyback_share_reduction_core69_pct_1q_v070_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_pct_change(_log(sharesbas.clip(lower=1.0)), 1))

# core70-74: pct 4q
def cg_f035_buyback_share_reduction_core70_pct_4q_v071_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    reduction = _pct_change(sharesbas, 1).clip(upper=0).abs()
    return _clean(_pct_change(reduction, 4))
def cg_f035_buyback_share_reduction_core71_pct_4q_v072_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_pct_change(_safe_div(ncff, marketcap), 4))
def cg_f035_buyback_share_reduction_core72_pct_4q_v073_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_pct_change(_safe_div(ncff, ncfo.abs() + 1.0), 4))
def cg_f035_buyback_share_reduction_core73_pct_4q_v074_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_pct_change(_safe_div(ncff, assets), 4))
def cg_f035_buyback_share_reduction_core74_pct_4q_v075_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_pct_change(_safe_div(ncff, revenue), 4))
