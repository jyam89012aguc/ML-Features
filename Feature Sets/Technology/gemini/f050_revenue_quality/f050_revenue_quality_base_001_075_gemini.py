import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core00-09: mean 4q
def cg_f050_revenue_quality_core00_mean_4q_v001_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_mean(_safe_div(receivables, revenue), 4))
def cg_f050_revenue_quality_core01_mean_4q_v002_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_mean(_safe_div(deferredrev, revenue), 4))
def cg_f050_revenue_quality_core02_mean_4q_v003_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_mean(_pct_change(receivables, 4) - _pct_change(revenue, 4), 4))
def cg_f050_revenue_quality_core03_mean_4q_v004_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_mean(_pct_change(deferredrev, 4) - _pct_change(revenue, 4), 4))
def cg_f050_revenue_quality_core04_mean_4q_v005_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_mean(_safe_div(_diff(receivables, 4), revenue), 4))
def cg_f050_revenue_quality_core05_mean_4q_v006_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_mean(_safe_div(_diff(deferredrev, 4), revenue), 4))
def cg_f050_revenue_quality_core06_mean_4q_v007_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    # DSOs proxy
    return _clean(_mean(_safe_div(receivables, revenue) * 365, 4))
def cg_f050_revenue_quality_core07_mean_4q_v008_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    # Unearned revenue days proxy
    return _clean(_mean(_safe_div(deferredrev, revenue) * 365, 4))
def cg_f050_revenue_quality_core08_mean_4q_v009_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_mean(_pct_change(revenue, 4), 4))
def cg_f050_revenue_quality_core09_mean_4q_v010_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_mean(_log(revenue.clip(lower=1.0)), 4))

# core10-19: mean 8q
def cg_f050_revenue_quality_core10_mean_8q_v011_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_mean(_safe_div(receivables, revenue), 8))
def cg_f050_revenue_quality_core11_mean_8q_v012_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_mean(_safe_div(deferredrev, revenue), 8))
def cg_f050_revenue_quality_core12_mean_8q_v013_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_mean(_pct_change(receivables, 4) - _pct_change(revenue, 4), 8))
def cg_f050_revenue_quality_core13_mean_8q_v014_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_mean(_pct_change(deferredrev, 4) - _pct_change(revenue, 4), 8))
def cg_f050_revenue_quality_core14_mean_8q_v015_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_mean(_safe_div(_diff(receivables, 4), revenue), 8))
def cg_f050_revenue_quality_core15_mean_8q_v016_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_mean(_safe_div(_diff(deferredrev, 4), revenue), 8))
def cg_f050_revenue_quality_core16_mean_8q_v017_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_mean(_safe_div(receivables, revenue) * 365, 8))
def cg_f050_revenue_quality_core17_mean_8q_v018_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_mean(_safe_div(deferredrev, revenue) * 365, 8))
def cg_f050_revenue_quality_core18_mean_8q_v019_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_mean(_pct_change(revenue, 4), 8))
def cg_f050_revenue_quality_core19_mean_8q_v020_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_mean(_log(revenue.clip(lower=1.0)), 8))

# core20-29: z 8q
def cg_f050_revenue_quality_core20_z_8q_v021_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_z(_safe_div(receivables, revenue), 8))
def cg_f050_revenue_quality_core21_z_8q_v022_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_z(_safe_div(deferredrev, revenue), 8))
def cg_f050_revenue_quality_core22_z_8q_v023_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_z(_pct_change(receivables, 4) - _pct_change(revenue, 4), 8))
def cg_f050_revenue_quality_core23_z_8q_v024_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_z(_pct_change(deferredrev, 4) - _pct_change(revenue, 4), 8))
def cg_f050_revenue_quality_core24_z_8q_v025_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_z(_safe_div(_diff(receivables, 4), revenue), 8))
def cg_f050_revenue_quality_core25_z_8q_v026_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_z(_safe_div(_diff(deferredrev, 4), revenue), 8))
def cg_f050_revenue_quality_core26_z_8q_v027_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_z(_safe_div(receivables, revenue) * 365, 8))
def cg_f050_revenue_quality_core27_z_8q_v028_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_z(_safe_div(deferredrev, revenue) * 365, 8))
def cg_f050_revenue_quality_core28_z_8q_v029_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_z(_pct_change(revenue, 4), 8))
def cg_f050_revenue_quality_core29_z_8q_v030_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_z(_log(revenue.clip(lower=1.0)), 8))

# core30-39: z 20q
def cg_f050_revenue_quality_core30_z_20q_v031_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_z(_safe_div(receivables, revenue), 20))
def cg_f050_revenue_quality_core31_z_20q_v032_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_z(_safe_div(deferredrev, revenue), 20))
def cg_f050_revenue_quality_core32_z_20q_v033_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_z(_pct_change(receivables, 4) - _pct_change(revenue, 4), 20))
def cg_f050_revenue_quality_core33_z_20q_v034_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_z(_pct_change(deferredrev, 4) - _pct_change(revenue, 4), 20))
def cg_f050_revenue_quality_core34_z_20q_v035_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_z(_safe_div(_diff(receivables, 4), revenue), 20))
def cg_f050_revenue_quality_core35_z_20q_v036_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_z(_safe_div(_diff(deferredrev, 4), revenue), 20))
def cg_f050_revenue_quality_core36_z_20q_v037_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_z(_safe_div(receivables, revenue) * 365, 20))
def cg_f050_revenue_quality_core37_z_20q_v038_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_z(_safe_div(deferredrev, revenue) * 365, 20))
def cg_f050_revenue_quality_core38_z_20q_v039_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_z(_pct_change(revenue, 4), 20))
def cg_f050_revenue_quality_core39_z_20q_v040_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_z(_log(revenue.clip(lower=1.0)), 20))

# core40-49: rank 12q
def cg_f050_revenue_quality_core40_rank_12q_v041_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_rank(_safe_div(receivables, revenue), 12))
def cg_f050_revenue_quality_core41_rank_12q_v042_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_rank(_safe_div(deferredrev, revenue), 12))
def cg_f050_revenue_quality_core42_rank_12q_v043_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_rank(_pct_change(receivables, 4) - _pct_change(revenue, 4), 12))
def cg_f050_revenue_quality_core43_rank_12q_v044_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_rank(_pct_change(deferredrev, 4) - _pct_change(revenue, 4), 12))
def cg_f050_revenue_quality_core44_rank_12q_v045_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_rank(_safe_div(_diff(receivables, 4), revenue), 12))
def cg_f050_revenue_quality_core45_rank_12q_v046_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_rank(_safe_div(_diff(deferredrev, 4), revenue), 12))
def cg_f050_revenue_quality_core46_rank_12q_v047_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_rank(_safe_div(receivables, revenue) * 365, 12))
def cg_f050_revenue_quality_core47_rank_12q_v048_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_rank(_safe_div(deferredrev, revenue) * 365, 12))
def cg_f050_revenue_quality_core48_rank_12q_v049_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_rank(_pct_change(revenue, 4), 12))
def cg_f050_revenue_quality_core49_rank_12q_v050_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_rank(_log(revenue.clip(lower=1.0)), 12))

# core50-59: rank 20q
def cg_f050_revenue_quality_core50_rank_20q_v051_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_rank(_safe_div(receivables, revenue), 20))
def cg_f050_revenue_quality_core51_rank_20q_v052_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_rank(_safe_div(deferredrev, revenue), 20))
def cg_f050_revenue_quality_core52_rank_20q_v053_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_rank(_pct_change(receivables, 4) - _pct_change(revenue, 4), 20))
def cg_f050_revenue_quality_core53_rank_20q_v054_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_rank(_pct_change(deferredrev, 4) - _pct_change(revenue, 4), 20))
def cg_f050_revenue_quality_core54_rank_20q_v055_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_rank(_safe_div(_diff(receivables, 4), revenue), 20))
def cg_f050_revenue_quality_core55_rank_20q_v056_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_rank(_safe_div(_diff(deferredrev, 4), revenue), 20))
def cg_f050_revenue_quality_core56_rank_20q_v057_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_rank(_safe_div(receivables, revenue) * 365, 20))
def cg_f050_revenue_quality_core57_rank_20q_v058_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_rank(_safe_div(deferredrev, revenue) * 365, 20))
def cg_f050_revenue_quality_core58_rank_20q_v059_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_rank(_pct_change(revenue, 4), 20))
def cg_f050_revenue_quality_core59_rank_20q_v060_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_rank(_log(revenue.clip(lower=1.0)), 20))

# core60-69: pct 1q
def cg_f050_revenue_quality_core60_pct_1q_v061_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_pct_change(_safe_div(receivables, revenue), 1))
def cg_f050_revenue_quality_core61_pct_1q_v062_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_pct_change(_safe_div(deferredrev, revenue), 1))
def cg_f050_revenue_quality_core62_pct_1q_v063_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_pct_change(_pct_change(receivables, 4) - _pct_change(revenue, 4), 1))
def cg_f050_revenue_quality_core63_pct_1q_v064_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_pct_change(_pct_change(deferredrev, 4) - _pct_change(revenue, 4), 1))
def cg_f050_revenue_quality_core64_pct_1q_v065_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_pct_change(_safe_div(_diff(receivables, 4), revenue), 1))
def cg_f050_revenue_quality_core65_pct_1q_v066_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_pct_change(_safe_div(_diff(deferredrev, 4), revenue), 1))
def cg_f050_revenue_quality_core66_pct_1q_v067_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_pct_change(_safe_div(receivables, revenue) * 365, 1))
def cg_f050_revenue_quality_core67_pct_1q_v068_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_pct_change(_safe_div(deferredrev, revenue) * 365, 1))
def cg_f050_revenue_quality_core68_pct_1q_v069_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_pct_change(_pct_change(revenue, 4), 1))
def cg_f050_revenue_quality_core69_pct_1q_v070_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_pct_change(_log(revenue.clip(lower=1.0)), 1))

# core70-74: pct 4q
def cg_f050_revenue_quality_core70_pct_4q_v071_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_pct_change(_safe_div(receivables, revenue), 4))
def cg_f050_revenue_quality_core71_pct_4q_v072_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_pct_change(_safe_div(deferredrev, revenue), 4))
def cg_f050_revenue_quality_core72_pct_4q_v073_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_pct_change(_pct_change(receivables, 4) - _pct_change(revenue, 4), 4))
def cg_f050_revenue_quality_core73_pct_4q_v074_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_pct_change(_pct_change(deferredrev, 4) - _pct_change(revenue, 4), 4))
def cg_f050_revenue_quality_core74_pct_4q_v075_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_pct_change(_safe_div(_diff(receivables, 4), revenue), 4))
