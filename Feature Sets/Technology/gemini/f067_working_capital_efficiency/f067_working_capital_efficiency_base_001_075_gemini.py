import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core00-09: mean 4q
def cg_f067_working_capital_efficiency_core00_mean_4q_v001_signal(workingcapital, revenue, assets):
    return _clean(_mean(workingcapital, 4))
def cg_f067_working_capital_efficiency_core01_mean_4q_v002_signal(workingcapital, revenue, assets):
    return _clean(_mean(_safe_div(workingcapital, revenue), 4))
def cg_f067_working_capital_efficiency_core02_mean_4q_v003_signal(workingcapital, revenue, assets):
    return _clean(_mean(_safe_div(workingcapital, assets), 4))
def cg_f067_working_capital_efficiency_core03_mean_4q_v004_signal(workingcapital, revenue, assets):
    return _clean(_mean(revenue, 4))
def cg_f067_working_capital_efficiency_core04_mean_4q_v005_signal(workingcapital, revenue, assets):
    return _clean(_mean(assets, 4))
def cg_f067_working_capital_efficiency_core05_mean_4q_v006_signal(workingcapital, revenue, assets):
    return _clean(_mean(_safe_div(revenue, assets), 4))
def cg_f067_working_capital_efficiency_core06_mean_4q_v007_signal(workingcapital, revenue, assets):
    return _clean(_mean(workingcapital - _mean(workingcapital, 4), 4))
def cg_f067_working_capital_efficiency_core07_mean_4q_v008_signal(workingcapital, revenue, assets):
    return _clean(_mean(_safe_div(workingcapital, revenue.abs() + 1.0), 4))
def cg_f067_working_capital_efficiency_core08_mean_4q_v009_signal(workingcapital, revenue, assets):
    return _clean(_mean(_safe_div(workingcapital, assets.abs() + 1.0), 4))
def cg_f067_working_capital_efficiency_core09_mean_4q_v010_signal(workingcapital, revenue, assets):
    return _clean(_mean(_safe_div(revenue - workingcapital, assets.abs() + 1.0), 4))

# core10-19: mean 8q
def cg_f067_working_capital_efficiency_core10_mean_8q_v011_signal(workingcapital, revenue, assets):
    return _clean(_mean(workingcapital, 8))
def cg_f067_working_capital_efficiency_core11_mean_8q_v012_signal(workingcapital, revenue, assets):
    return _clean(_mean(_safe_div(workingcapital, revenue), 8))
def cg_f067_working_capital_efficiency_core12_mean_8q_v013_signal(workingcapital, revenue, assets):
    return _clean(_mean(_safe_div(workingcapital, assets), 8))
def cg_f067_working_capital_efficiency_core13_mean_8q_v014_signal(workingcapital, revenue, assets):
    return _clean(_mean(revenue, 8))
def cg_f067_working_capital_efficiency_core14_mean_8q_v015_signal(workingcapital, revenue, assets):
    return _clean(_mean(assets, 8))
def cg_f067_working_capital_efficiency_core15_mean_8q_v016_signal(workingcapital, revenue, assets):
    return _clean(_mean(_safe_div(revenue, assets), 8))
def cg_f067_working_capital_efficiency_core16_mean_8q_v017_signal(workingcapital, revenue, assets):
    return _clean(_mean(workingcapital - _mean(workingcapital, 8), 8))
def cg_f067_working_capital_efficiency_core17_mean_8q_v018_signal(workingcapital, revenue, assets):
    return _clean(_mean(_safe_div(workingcapital, revenue.abs() + 1.0), 8))
def cg_f067_working_capital_efficiency_core18_mean_8q_v019_signal(workingcapital, revenue, assets):
    return _clean(_mean(_safe_div(workingcapital, assets.abs() + 1.0), 8))
def cg_f067_working_capital_efficiency_core19_mean_8q_v020_signal(workingcapital, revenue, assets):
    return _clean(_mean(_safe_div(revenue - workingcapital, assets.abs() + 1.0), 8))

# core20-29: z 8q
def cg_f067_working_capital_efficiency_core20_z_8q_v021_signal(workingcapital, revenue, assets):
    return _clean(_z(workingcapital, 8))
def cg_f067_working_capital_efficiency_core21_z_8q_v022_signal(workingcapital, revenue, assets):
    return _clean(_z(_safe_div(workingcapital, revenue), 8))
def cg_f067_working_capital_efficiency_core22_z_8q_v023_signal(workingcapital, revenue, assets):
    return _clean(_z(_safe_div(workingcapital, assets), 8))
def cg_f067_working_capital_efficiency_core23_z_8q_v024_signal(workingcapital, revenue, assets):
    return _clean(_z(revenue, 8))
def cg_f067_working_capital_efficiency_core24_z_8q_v025_signal(workingcapital, revenue, assets):
    return _clean(_z(assets, 8))
def cg_f067_working_capital_efficiency_core25_z_8q_v026_signal(workingcapital, revenue, assets):
    return _clean(_z(_safe_div(revenue, assets), 8))
def cg_f067_working_capital_efficiency_core26_z_8q_v027_signal(workingcapital, revenue, assets):
    return _clean(_z(workingcapital - _mean(workingcapital, 8), 8))
def cg_f067_working_capital_efficiency_core27_z_8q_v028_signal(workingcapital, revenue, assets):
    return _clean(_z(_safe_div(workingcapital, revenue.abs() + 1.0), 8))
def cg_f067_working_capital_efficiency_core28_z_8q_v029_signal(workingcapital, revenue, assets):
    return _clean(_z(_safe_div(workingcapital, assets.abs() + 1.0), 8))
def cg_f067_working_capital_efficiency_core29_z_8q_v030_signal(workingcapital, revenue, assets):
    return _clean(_z(_safe_div(revenue - workingcapital, assets.abs() + 1.0), 8))

# core30-39: z 20q
def cg_f067_working_capital_efficiency_core30_z_20q_v031_signal(workingcapital, revenue, assets):
    return _clean(_z(workingcapital, 20))
def cg_f067_working_capital_efficiency_core31_z_20q_v032_signal(workingcapital, revenue, assets):
    return _clean(_z(_safe_div(workingcapital, revenue), 20))
def cg_f067_working_capital_efficiency_core32_z_20q_v033_signal(workingcapital, revenue, assets):
    return _clean(_z(_safe_div(workingcapital, assets), 20))
def cg_f067_working_capital_efficiency_core33_z_20q_v034_signal(workingcapital, revenue, assets):
    return _clean(_z(revenue, 20))
def cg_f067_working_capital_efficiency_core34_z_20q_v035_signal(workingcapital, revenue, assets):
    return _clean(_z(assets, 20))
def cg_f067_working_capital_efficiency_core35_z_20q_v036_signal(workingcapital, revenue, assets):
    return _clean(_z(_safe_div(revenue, assets), 20))
def cg_f067_working_capital_efficiency_core36_z_20q_v037_signal(workingcapital, revenue, assets):
    return _clean(_z(workingcapital - _mean(workingcapital, 20), 20))
def cg_f067_working_capital_efficiency_core37_z_20q_v038_signal(workingcapital, revenue, assets):
    return _clean(_z(_safe_div(workingcapital, revenue.abs() + 1.0), 20))
def cg_f067_working_capital_efficiency_core38_z_20q_v039_signal(workingcapital, revenue, assets):
    return _clean(_z(_safe_div(workingcapital, assets.abs() + 1.0), 20))
def cg_f067_working_capital_efficiency_core39_z_20q_v040_signal(workingcapital, revenue, assets):
    return _clean(_z(_safe_div(revenue - workingcapital, assets.abs() + 1.0), 20))

# core40-49: rank 8q
def cg_f067_working_capital_efficiency_core40_rank_8q_v041_signal(workingcapital, revenue, assets):
    return _clean(_rank(workingcapital, 8))
def cg_f067_working_capital_efficiency_core41_rank_8q_v042_signal(workingcapital, revenue, assets):
    return _clean(_rank(_safe_div(workingcapital, revenue), 8))
def cg_f067_working_capital_efficiency_core42_rank_8q_v043_signal(workingcapital, revenue, assets):
    return _clean(_rank(_safe_div(workingcapital, assets), 8))
def cg_f067_working_capital_efficiency_core43_rank_8q_v044_signal(workingcapital, revenue, assets):
    return _clean(_rank(revenue, 8))
def cg_f067_working_capital_efficiency_core44_rank_8q_v045_signal(workingcapital, revenue, assets):
    return _clean(_rank(assets, 8))
def cg_f067_working_capital_efficiency_core45_rank_8q_v046_signal(workingcapital, revenue, assets):
    return _clean(_rank(_safe_div(revenue, assets), 8))
def cg_f067_working_capital_efficiency_core46_rank_8q_v047_signal(workingcapital, revenue, assets):
    return _clean(_rank(workingcapital - _mean(workingcapital, 8), 8))
def cg_f067_working_capital_efficiency_core47_rank_8q_v048_signal(workingcapital, revenue, assets):
    return _clean(_rank(_safe_div(workingcapital, revenue.abs() + 1.0), 8))
def cg_f067_working_capital_efficiency_core48_rank_8q_v049_signal(workingcapital, revenue, assets):
    return _clean(_rank(_safe_div(workingcapital, assets.abs() + 1.0), 8))
def cg_f067_working_capital_efficiency_core49_rank_8q_v050_signal(workingcapital, revenue, assets):
    return _clean(_rank(_safe_div(revenue - workingcapital, assets.abs() + 1.0), 8))

# core50-59: rank 20q
def cg_f067_working_capital_efficiency_core50_rank_20q_v051_signal(workingcapital, revenue, assets):
    return _clean(_rank(workingcapital, 20))
def cg_f067_working_capital_efficiency_core51_rank_20q_v052_signal(workingcapital, revenue, assets):
    return _clean(_rank(_safe_div(workingcapital, revenue), 20))
def cg_f067_working_capital_efficiency_core52_rank_20q_v053_signal(workingcapital, revenue, assets):
    return _clean(_rank(_safe_div(workingcapital, assets), 20))
def cg_f067_working_capital_efficiency_core53_rank_20q_v054_signal(workingcapital, revenue, assets):
    return _clean(_rank(revenue, 20))
def cg_f067_working_capital_efficiency_core54_rank_20q_v055_signal(workingcapital, revenue, assets):
    return _clean(_rank(assets, 20))
def cg_f067_working_capital_efficiency_core55_rank_20q_v056_signal(workingcapital, revenue, assets):
    return _clean(_rank(_safe_div(revenue, assets), 20))
def cg_f067_working_capital_efficiency_core56_rank_20q_v057_signal(workingcapital, revenue, assets):
    return _clean(_rank(workingcapital - _mean(workingcapital, 20), 20))
def cg_f067_working_capital_efficiency_core57_rank_20q_v058_signal(workingcapital, revenue, assets):
    return _clean(_rank(_safe_div(workingcapital, revenue.abs() + 1.0), 20))
def cg_f067_working_capital_efficiency_core58_rank_20q_v059_signal(workingcapital, revenue, assets):
    return _clean(_rank(_safe_div(workingcapital, assets.abs() + 1.0), 20))
def cg_f067_working_capital_efficiency_core59_rank_20q_v060_signal(workingcapital, revenue, assets):
    return _clean(_rank(_safe_div(revenue - workingcapital, assets.abs() + 1.0), 20))

# core60-69: pct 1q
def cg_f067_working_capital_efficiency_core60_pct_1q_v061_signal(workingcapital, revenue, assets):
    return _clean(_pct_change(workingcapital, 1))
def cg_f067_working_capital_efficiency_core61_pct_1q_v062_signal(workingcapital, revenue, assets):
    return _clean(_pct_change(_safe_div(workingcapital, revenue), 1))
def cg_f067_working_capital_efficiency_core62_pct_1q_v063_signal(workingcapital, revenue, assets):
    return _clean(_pct_change(_safe_div(workingcapital, assets), 1))
def cg_f067_working_capital_efficiency_core63_pct_1q_v064_signal(workingcapital, revenue, assets):
    return _clean(_pct_change(revenue, 1))
def cg_f067_working_capital_efficiency_core64_pct_1q_v065_signal(workingcapital, revenue, assets):
    return _clean(_pct_change(assets, 1))
def cg_f067_working_capital_efficiency_core65_pct_1q_v066_signal(workingcapital, revenue, assets):
    return _clean(_pct_change(_safe_div(revenue, assets), 1))
def cg_f067_working_capital_efficiency_core66_pct_1q_v067_signal(workingcapital, revenue, assets):
    return _clean(_pct_change(workingcapital - _mean(workingcapital, 4), 1))
def cg_f067_working_capital_efficiency_core67_pct_1q_v068_signal(workingcapital, revenue, assets):
    return _clean(_pct_change(_safe_div(workingcapital, revenue.abs() + 1.0), 1))
def cg_f067_working_capital_efficiency_core68_pct_1q_v069_signal(workingcapital, revenue, assets):
    return _clean(_pct_change(_safe_div(workingcapital, assets.abs() + 1.0), 1))
def cg_f067_working_capital_efficiency_core69_pct_1q_v070_signal(workingcapital, revenue, assets):
    return _clean(_pct_change(_safe_div(revenue - workingcapital, assets.abs() + 1.0), 1))

# core70-74: pct 4q
def cg_f067_working_capital_efficiency_core70_pct_4q_v071_signal(workingcapital, revenue, assets):
    return _clean(_pct_change(workingcapital, 4))
def cg_f067_working_capital_efficiency_core71_pct_4q_v072_signal(workingcapital, revenue, assets):
    return _clean(_pct_change(_safe_div(workingcapital, revenue), 4))
def cg_f067_working_capital_efficiency_core72_pct_4q_v073_signal(workingcapital, revenue, assets):
    return _clean(_pct_change(_safe_div(workingcapital, assets), 4))
def cg_f067_working_capital_efficiency_core73_pct_4q_v074_signal(workingcapital, revenue, assets):
    return _clean(_pct_change(revenue, 4))
def cg_f067_working_capital_efficiency_core74_pct_4q_v075_signal(workingcapital, revenue, assets):
    return _clean(_pct_change(assets, 4))
