import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core00-09: mean 4q
def cg_f048_revenue_acceleration_core00_mean_4q_v001_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_mean(_diff(_pct_change(revenue, 4), 1), 4))
def cg_f048_revenue_acceleration_core01_mean_4q_v002_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_mean(_diff(_pct_change(revenue, 4), 4), 4))
def cg_f048_revenue_acceleration_core02_mean_4q_v003_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_mean(_diff(_pct_change(revenue, 1), 1), 4))
def cg_f048_revenue_acceleration_core03_mean_4q_v004_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_mean(_diff(_pct_change(_safe_div(revenue, assets), 4), 1), 4))
def cg_f048_revenue_acceleration_core04_mean_4q_v005_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_mean(_diff(_pct_change(_safe_div(revenue, opex.abs() + 1.0), 4), 1), 4))
def cg_f048_revenue_acceleration_core05_mean_4q_v006_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    accel = _diff(_pct_change(revenue, 4), 1)
    accel_assets = _diff(_pct_change(assets, 4), 1)
    return _clean(_mean(accel - accel_assets, 4))
def cg_f048_revenue_acceleration_core06_mean_4q_v007_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    accel = _diff(_pct_change(revenue, 4), 1)
    accel_opex = _diff(_pct_change(opex, 4), 1)
    return _clean(_mean(accel - accel_opex, 4))
def cg_f048_revenue_acceleration_core07_mean_4q_v008_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_mean(_diff(_diff(_pct_change(revenue, 4), 1), 1), 4))
def cg_f048_revenue_acceleration_core08_mean_4q_v009_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_mean(_diff(_diff(_pct_change(revenue, 4), 4), 4), 4))
def cg_f048_revenue_acceleration_core09_mean_4q_v010_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_mean(_z(_diff(_pct_change(revenue, 4), 1), 12), 4))

# core10-19: mean 8q
def cg_f048_revenue_acceleration_core10_mean_8q_v011_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_mean(_diff(_pct_change(revenue, 4), 1), 8))
def cg_f048_revenue_acceleration_core11_mean_8q_v012_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_mean(_diff(_pct_change(revenue, 4), 4), 8))
def cg_f048_revenue_acceleration_core12_mean_8q_v013_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_mean(_diff(_pct_change(revenue, 1), 1), 8))
def cg_f048_revenue_acceleration_core13_mean_8q_v014_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_mean(_diff(_pct_change(_safe_div(revenue, assets), 4), 1), 8))
def cg_f048_revenue_acceleration_core14_mean_8q_v015_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_mean(_diff(_pct_change(_safe_div(revenue, opex.abs() + 1.0), 4), 1), 8))
def cg_f048_revenue_acceleration_core15_mean_8q_v016_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    accel = _diff(_pct_change(revenue, 4), 1)
    accel_assets = _diff(_pct_change(assets, 4), 1)
    return _clean(_mean(accel - accel_assets, 8))
def cg_f048_revenue_acceleration_core16_mean_8q_v017_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    accel = _diff(_pct_change(revenue, 4), 1)
    accel_opex = _diff(_pct_change(opex, 4), 1)
    return _clean(_mean(accel - accel_opex, 8))
def cg_f048_revenue_acceleration_core17_mean_8q_v018_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_mean(_diff(_diff(_pct_change(revenue, 4), 1), 1), 8))
def cg_f048_revenue_acceleration_core18_mean_8q_v019_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_mean(_diff(_diff(_pct_change(revenue, 4), 4), 4), 8))
def cg_f048_revenue_acceleration_core19_mean_8q_v020_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_mean(_z(_diff(_pct_change(revenue, 4), 1), 12), 8))

# core20-29: z 8q
def cg_f048_revenue_acceleration_core20_z_8q_v021_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_z(_diff(_pct_change(revenue, 4), 1), 8))
def cg_f048_revenue_acceleration_core21_z_8q_v022_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_z(_diff(_pct_change(revenue, 4), 4), 8))
def cg_f048_revenue_acceleration_core22_z_8q_v023_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_z(_diff(_pct_change(revenue, 1), 1), 8))
def cg_f048_revenue_acceleration_core23_z_8q_v024_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_z(_diff(_pct_change(_safe_div(revenue, assets), 4), 1), 8))
def cg_f048_revenue_acceleration_core24_z_8q_v025_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_z(_diff(_pct_change(_safe_div(revenue, opex.abs() + 1.0), 4), 1), 8))
def cg_f048_revenue_acceleration_core25_z_8q_v026_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    accel = _diff(_pct_change(revenue, 4), 1)
    accel_assets = _diff(_pct_change(assets, 4), 1)
    return _clean(_z(accel - accel_assets, 8))
def cg_f048_revenue_acceleration_core26_z_8q_v027_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    accel = _diff(_pct_change(revenue, 4), 1)
    accel_opex = _diff(_pct_change(opex, 4), 1)
    return _clean(_z(accel - accel_opex, 8))
def cg_f048_revenue_acceleration_core27_z_8q_v028_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_z(_diff(_diff(_pct_change(revenue, 4), 1), 1), 8))
def cg_f048_revenue_acceleration_core28_z_8q_v029_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_z(_diff(_diff(_pct_change(revenue, 4), 4), 4), 8))
def cg_f048_revenue_acceleration_core29_z_8q_v030_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_z(_z(_diff(_pct_change(revenue, 4), 1), 12), 8))

# core30-39: z 20q
def cg_f048_revenue_acceleration_core30_z_20q_v031_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_z(_diff(_pct_change(revenue, 4), 1), 20))
def cg_f048_revenue_acceleration_core31_z_20q_v032_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_z(_diff(_pct_change(revenue, 4), 4), 20))
def cg_f048_revenue_acceleration_core32_z_20q_v033_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_z(_diff(_pct_change(revenue, 1), 1), 20))
def cg_f048_revenue_acceleration_core33_z_20q_v034_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_z(_diff(_pct_change(_safe_div(revenue, assets), 4), 1), 20))
def cg_f048_revenue_acceleration_core34_z_20q_v035_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_z(_diff(_pct_change(_safe_div(revenue, opex.abs() + 1.0), 4), 1), 20))
def cg_f048_revenue_acceleration_core35_z_20q_v036_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    accel = _diff(_pct_change(revenue, 4), 1)
    accel_assets = _diff(_pct_change(assets, 4), 1)
    return _clean(_z(accel - accel_assets, 20))
def cg_f048_revenue_acceleration_core36_z_20q_v037_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    accel = _diff(_pct_change(revenue, 4), 1)
    accel_opex = _diff(_pct_change(opex, 4), 1)
    return _clean(_z(accel - accel_opex, 20))
def cg_f048_revenue_acceleration_core37_z_20q_v038_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_z(_diff(_diff(_pct_change(revenue, 4), 1), 1), 20))
def cg_f048_revenue_acceleration_core38_z_20q_v039_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_z(_diff(_diff(_pct_change(revenue, 4), 4), 4), 20))
def cg_f048_revenue_acceleration_core39_z_20q_v040_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_z(_z(_diff(_pct_change(revenue, 4), 1), 12), 20))

# core40-49: rank 12q
def cg_f048_revenue_acceleration_core40_rank_12q_v041_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_rank(_diff(_pct_change(revenue, 4), 1), 12))
def cg_f048_revenue_acceleration_core41_rank_12q_v042_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_rank(_diff(_pct_change(revenue, 4), 4), 12))
def cg_f048_revenue_acceleration_core42_rank_12q_v043_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_rank(_diff(_pct_change(revenue, 1), 1), 12))
def cg_f048_revenue_acceleration_core43_rank_12q_v044_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_rank(_diff(_pct_change(_safe_div(revenue, assets), 4), 1), 12))
def cg_f048_revenue_acceleration_core44_rank_12q_v045_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_rank(_diff(_pct_change(_safe_div(revenue, opex.abs() + 1.0), 4), 1), 12))
def cg_f048_revenue_acceleration_core45_rank_12q_v046_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    accel = _diff(_pct_change(revenue, 4), 1)
    accel_assets = _diff(_pct_change(assets, 4), 1)
    return _clean(_rank(accel - accel_assets, 12))
def cg_f048_revenue_acceleration_core46_rank_12q_v047_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    accel = _diff(_pct_change(revenue, 4), 1)
    accel_opex = _diff(_pct_change(opex, 4), 1)
    return _clean(_rank(accel - accel_opex, 12))
def cg_f048_revenue_acceleration_core47_rank_12q_v048_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_rank(_diff(_diff(_pct_change(revenue, 4), 1), 1), 12))
def cg_f048_revenue_acceleration_core48_rank_12q_v049_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_rank(_diff(_diff(_pct_change(revenue, 4), 4), 4), 12))
def cg_f048_revenue_acceleration_core49_rank_12q_v050_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_rank(_z(_diff(_pct_change(revenue, 4), 1), 12), 12))

# core50-59: rank 20q
def cg_f048_revenue_acceleration_core50_rank_20q_v051_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_rank(_diff(_pct_change(revenue, 4), 1), 20))
def cg_f048_revenue_acceleration_core51_rank_20q_v052_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_rank(_diff(_pct_change(revenue, 4), 4), 20))
def cg_f048_revenue_acceleration_core52_rank_20q_v053_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_rank(_diff(_pct_change(revenue, 1), 1), 20))
def cg_f048_revenue_acceleration_core53_rank_20q_v054_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_rank(_diff(_pct_change(_safe_div(revenue, assets), 4), 1), 20))
def cg_f048_revenue_acceleration_core54_rank_20q_v055_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_rank(_diff(_pct_change(_safe_div(revenue, opex.abs() + 1.0), 4), 1), 20))
def cg_f048_revenue_acceleration_core55_rank_20q_v056_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    accel = _diff(_pct_change(revenue, 4), 1)
    accel_assets = _diff(_pct_change(assets, 4), 1)
    return _clean(_rank(accel - accel_assets, 20))
def cg_f048_revenue_acceleration_core56_rank_20q_v057_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    accel = _diff(_pct_change(revenue, 4), 1)
    accel_opex = _diff(_pct_change(opex, 4), 1)
    return _clean(_rank(accel - accel_opex, 20))
def cg_f048_revenue_acceleration_core57_rank_20q_v058_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_rank(_diff(_diff(_pct_change(revenue, 4), 1), 1), 20))
def cg_f048_revenue_acceleration_core58_rank_20q_v059_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_rank(_diff(_diff(_pct_change(revenue, 4), 4), 4), 20))
def cg_f048_revenue_acceleration_core59_rank_20q_v060_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_rank(_z(_diff(_pct_change(revenue, 4), 1), 12), 20))

# core60-69: pct 1q
def cg_f048_revenue_acceleration_core60_pct_1q_v061_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_pct_change(_diff(_pct_change(revenue, 4), 1), 1))
def cg_f048_revenue_acceleration_core61_pct_1q_v062_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_pct_change(_diff(_pct_change(revenue, 4), 4), 1))
def cg_f048_revenue_acceleration_core62_pct_1q_v063_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_pct_change(_diff(_pct_change(revenue, 1), 1), 1))
def cg_f048_revenue_acceleration_core63_pct_1q_v064_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_pct_change(_diff(_pct_change(_safe_div(revenue, assets), 4), 1), 1))
def cg_f048_revenue_acceleration_core64_pct_1q_v065_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_pct_change(_diff(_pct_change(_safe_div(revenue, opex.abs() + 1.0), 4), 1), 1))
def cg_f048_revenue_acceleration_core65_pct_1q_v066_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    accel = _diff(_pct_change(revenue, 4), 1)
    accel_assets = _diff(_pct_change(assets, 4), 1)
    return _clean(_pct_change(accel - accel_assets, 1))
def cg_f048_revenue_acceleration_core66_pct_1q_v067_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    accel = _diff(_pct_change(revenue, 4), 1)
    accel_opex = _diff(_pct_change(opex, 4), 1)
    return _clean(_pct_change(accel - accel_opex, 1))
def cg_f048_revenue_acceleration_core67_pct_1q_v068_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_pct_change(_diff(_diff(_pct_change(revenue, 4), 1), 1), 1))
def cg_f048_revenue_acceleration_core68_pct_1q_v069_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_pct_change(_diff(_diff(_pct_change(revenue, 4), 4), 4), 1))
def cg_f048_revenue_acceleration_core69_pct_1q_v070_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_pct_change(_z(_diff(_pct_change(revenue, 4), 1), 12), 1))

# core70-74: pct 4q
def cg_f048_revenue_acceleration_core70_pct_4q_v071_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_pct_change(_diff(_pct_change(revenue, 4), 1), 4))
def cg_f048_revenue_acceleration_core71_pct_4q_v072_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_pct_change(_diff(_pct_change(revenue, 4), 4), 4))
def cg_f048_revenue_acceleration_core72_pct_4q_v073_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_pct_change(_diff(_pct_change(revenue, 1), 1), 4))
def cg_f048_revenue_acceleration_core73_pct_4q_v074_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_pct_change(_diff(_pct_change(_safe_div(revenue, assets), 4), 1), 4))
def cg_f048_revenue_acceleration_core74_pct_4q_v075_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_pct_change(_diff(_pct_change(_safe_div(revenue, opex.abs() + 1.0), 4), 1), 4))
