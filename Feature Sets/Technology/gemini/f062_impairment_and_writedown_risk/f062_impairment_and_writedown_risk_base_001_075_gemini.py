import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core00-09: mean 4q
def cg_f062_impairment_and_writedown_risk_core00_mean_4q_v001_signal(intangibles, depamor, assets, opex):
    return _clean(_mean(intangibles, 4))
def cg_f062_impairment_and_writedown_risk_core01_mean_4q_v002_signal(intangibles, depamor, assets, opex):
    return _clean(_mean(_safe_div(intangibles, assets), 4))
def cg_f062_impairment_and_writedown_risk_core02_mean_4q_v003_signal(intangibles, depamor, assets, opex):
    return _clean(_mean(depamor, 4))
def cg_f062_impairment_and_writedown_risk_core03_mean_4q_v004_signal(intangibles, depamor, assets, opex):
    return _clean(_mean(_safe_div(depamor, opex.abs() + 1.0), 4))
def cg_f062_impairment_and_writedown_risk_core04_mean_4q_v005_signal(intangibles, depamor, assets, opex):
    return _clean(_mean(_safe_div(depamor, assets), 4))
def cg_f062_impairment_and_writedown_risk_core05_mean_4q_v006_signal(intangibles, depamor, assets, opex):
    return _clean(_mean(opex, 4))
def cg_f062_impairment_and_writedown_risk_core06_mean_4q_v007_signal(intangibles, depamor, assets, opex):
    return _clean(_mean(_safe_div(opex, assets), 4))
def cg_f062_impairment_and_writedown_risk_core07_mean_4q_v008_signal(intangibles, depamor, assets, opex):
    return _clean(_mean(_safe_div(intangibles + depamor, assets), 4))
def cg_f062_impairment_and_writedown_risk_core08_mean_4q_v009_signal(intangibles, depamor, assets, opex):
    return _clean(_mean(_safe_div(intangibles, opex.abs() + 1.0), 4))
def cg_f062_impairment_and_writedown_risk_core09_mean_4q_v010_signal(intangibles, depamor, assets, opex):
    return _clean(_mean(_safe_div(depamor, intangibles.abs() + 1.0), 4))

# core10-19: mean 8q
def cg_f062_impairment_and_writedown_risk_core10_mean_8q_v011_signal(intangibles, depamor, assets, opex):
    return _clean(_mean(intangibles, 8))
def cg_f062_impairment_and_writedown_risk_core11_mean_8q_v012_signal(intangibles, depamor, assets, opex):
    return _clean(_mean(_safe_div(intangibles, assets), 8))
def cg_f062_impairment_and_writedown_risk_core12_mean_8q_v013_signal(intangibles, depamor, assets, opex):
    return _clean(_mean(depamor, 8))
def cg_f062_impairment_and_writedown_risk_core13_mean_8q_v014_signal(intangibles, depamor, assets, opex):
    return _clean(_mean(_safe_div(depamor, opex.abs() + 1.0), 8))
def cg_f062_impairment_and_writedown_risk_core14_mean_8q_v015_signal(intangibles, depamor, assets, opex):
    return _clean(_mean(_safe_div(depamor, assets), 8))
def cg_f062_impairment_and_writedown_risk_core15_mean_8q_v016_signal(intangibles, depamor, assets, opex):
    return _clean(_mean(opex, 8))
def cg_f062_impairment_and_writedown_risk_core16_mean_8q_v017_signal(intangibles, depamor, assets, opex):
    return _clean(_mean(_safe_div(opex, assets), 8))
def cg_f062_impairment_and_writedown_risk_core17_mean_8q_v018_signal(intangibles, depamor, assets, opex):
    return _clean(_mean(_safe_div(intangibles + depamor, assets), 8))
def cg_f062_impairment_and_writedown_risk_core18_mean_8q_v019_signal(intangibles, depamor, assets, opex):
    return _clean(_mean(_safe_div(intangibles, opex.abs() + 1.0), 8))
def cg_f062_impairment_and_writedown_risk_core19_mean_8q_v020_signal(intangibles, depamor, assets, opex):
    return _clean(_mean(_safe_div(depamor, intangibles.abs() + 1.0), 8))

# core20-29: z 8q
def cg_f062_impairment_and_writedown_risk_core20_z_8q_v021_signal(intangibles, depamor, assets, opex):
    return _clean(_z(intangibles, 8))
def cg_f062_impairment_and_writedown_risk_core21_z_8q_v022_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_safe_div(intangibles, assets), 8))
def cg_f062_impairment_and_writedown_risk_core22_z_8q_v023_signal(intangibles, depamor, assets, opex):
    return _clean(_z(depamor, 8))
def cg_f062_impairment_and_writedown_risk_core23_z_8q_v024_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_safe_div(depamor, opex.abs() + 1.0), 8))
def cg_f062_impairment_and_writedown_risk_core24_z_8q_v025_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_safe_div(depamor, assets), 8))
def cg_f062_impairment_and_writedown_risk_core25_z_8q_v026_signal(intangibles, depamor, assets, opex):
    return _clean(_z(opex, 8))
def cg_f062_impairment_and_writedown_risk_core26_z_8q_v027_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_safe_div(opex, assets), 8))
def cg_f062_impairment_and_writedown_risk_core27_z_8q_v028_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_safe_div(intangibles + depamor, assets), 8))
def cg_f062_impairment_and_writedown_risk_core28_z_8q_v029_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_safe_div(intangibles, opex.abs() + 1.0), 8))
def cg_f062_impairment_and_writedown_risk_core29_z_8q_v030_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_safe_div(depamor, intangibles.abs() + 1.0), 8))

# core30-39: z 20q
def cg_f062_impairment_and_writedown_risk_core30_z_20q_v031_signal(intangibles, depamor, assets, opex):
    return _clean(_z(intangibles, 20))
def cg_f062_impairment_and_writedown_risk_core31_z_20q_v032_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_safe_div(intangibles, assets), 20))
def cg_f062_impairment_and_writedown_risk_core32_z_20q_v033_signal(intangibles, depamor, assets, opex):
    return _clean(_z(depamor, 20))
def cg_f062_impairment_and_writedown_risk_core33_z_20q_v034_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_safe_div(depamor, opex.abs() + 1.0), 20))
def cg_f062_impairment_and_writedown_risk_core34_z_20q_v035_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_safe_div(depamor, assets), 20))
def cg_f062_impairment_and_writedown_risk_core35_z_20q_v036_signal(intangibles, depamor, assets, opex):
    return _clean(_z(opex, 20))
def cg_f062_impairment_and_writedown_risk_core36_z_20q_v037_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_safe_div(opex, assets), 20))
def cg_f062_impairment_and_writedown_risk_core37_z_20q_v038_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_safe_div(intangibles + depamor, assets), 20))
def cg_f062_impairment_and_writedown_risk_core38_z_20q_v039_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_safe_div(intangibles, opex.abs() + 1.0), 20))
def cg_f062_impairment_and_writedown_risk_core39_z_20q_v040_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_safe_div(depamor, intangibles.abs() + 1.0), 20))

# core40-49: rank 8q
def cg_f062_impairment_and_writedown_risk_core40_rank_8q_v041_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(intangibles, 8))
def cg_f062_impairment_and_writedown_risk_core41_rank_8q_v042_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(_safe_div(intangibles, assets), 8))
def cg_f062_impairment_and_writedown_risk_core42_rank_8q_v043_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(depamor, 8))
def cg_f062_impairment_and_writedown_risk_core43_rank_8q_v044_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(_safe_div(depamor, opex.abs() + 1.0), 8))
def cg_f062_impairment_and_writedown_risk_core44_rank_8q_v045_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(_safe_div(depamor, assets), 8))
def cg_f062_impairment_and_writedown_risk_core45_rank_8q_v046_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(opex, 8))
def cg_f062_impairment_and_writedown_risk_core46_rank_8q_v047_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(_safe_div(opex, assets), 8))
def cg_f062_impairment_and_writedown_risk_core47_rank_8q_v048_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(_safe_div(intangibles + depamor, assets), 8))
def cg_f062_impairment_and_writedown_risk_core48_rank_8q_v049_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(_safe_div(intangibles, opex.abs() + 1.0), 8))
def cg_f062_impairment_and_writedown_risk_core49_rank_8q_v050_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(_safe_div(depamor, intangibles.abs() + 1.0), 8))

# core50-59: rank 20q
def cg_f062_impairment_and_writedown_risk_core50_rank_20q_v051_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(intangibles, 20))
def cg_f062_impairment_and_writedown_risk_core51_rank_20q_v052_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(_safe_div(intangibles, assets), 20))
def cg_f062_impairment_and_writedown_risk_core52_rank_20q_v053_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(depamor, 20))
def cg_f062_impairment_and_writedown_risk_core53_rank_20q_v054_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(_safe_div(depamor, opex.abs() + 1.0), 20))
def cg_f062_impairment_and_writedown_risk_core54_rank_20q_v055_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(_safe_div(depamor, assets), 20))
def cg_f062_impairment_and_writedown_risk_core55_rank_20q_v056_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(opex, 20))
def cg_f062_impairment_and_writedown_risk_core56_rank_20q_v057_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(_safe_div(opex, assets), 20))
def cg_f062_impairment_and_writedown_risk_core57_rank_20q_v058_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(_safe_div(intangibles + depamor, assets), 20))
def cg_f062_impairment_and_writedown_risk_core58_rank_20q_v059_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(_safe_div(intangibles, opex.abs() + 1.0), 20))
def cg_f062_impairment_and_writedown_risk_core59_rank_20q_v060_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(_safe_div(depamor, intangibles.abs() + 1.0), 20))

# core60-69: pct 1q
def cg_f062_impairment_and_writedown_risk_core60_pct_1q_v061_signal(intangibles, depamor, assets, opex):
    return _clean(_pct_change(intangibles, 1))
def cg_f062_impairment_and_writedown_risk_core61_pct_1q_v062_signal(intangibles, depamor, assets, opex):
    return _clean(_pct_change(_safe_div(intangibles, assets), 1))
def cg_f062_impairment_and_writedown_risk_core62_pct_1q_v063_signal(intangibles, depamor, assets, opex):
    return _clean(_pct_change(depamor, 1))
def cg_f062_impairment_and_writedown_risk_core63_pct_1q_v064_signal(intangibles, depamor, assets, opex):
    return _clean(_pct_change(_safe_div(depamor, opex.abs() + 1.0), 1))
def cg_f062_impairment_and_writedown_risk_core64_pct_1q_v065_signal(intangibles, depamor, assets, opex):
    return _clean(_pct_change(_safe_div(depamor, assets), 1))
def cg_f062_impairment_and_writedown_risk_core65_pct_1q_v066_signal(intangibles, depamor, assets, opex):
    return _clean(_pct_change(opex, 1))
def cg_f062_impairment_and_writedown_risk_core66_pct_1q_v067_signal(intangibles, depamor, assets, opex):
    return _clean(_pct_change(_safe_div(opex, assets), 1))
def cg_f062_impairment_and_writedown_risk_core67_pct_1q_v068_signal(intangibles, depamor, assets, opex):
    return _clean(_pct_change(_safe_div(intangibles + depamor, assets), 1))
def cg_f062_impairment_and_writedown_risk_core68_pct_1q_v069_signal(intangibles, depamor, assets, opex):
    return _clean(_pct_change(_safe_div(intangibles, opex.abs() + 1.0), 1))
def cg_f062_impairment_and_writedown_risk_core69_pct_1q_v070_signal(intangibles, depamor, assets, opex):
    return _clean(_pct_change(_safe_div(depamor, intangibles.abs() + 1.0), 1))

# core70-74: pct 4q
def cg_f062_impairment_and_writedown_risk_core70_pct_4q_v071_signal(intangibles, depamor, assets, opex):
    return _clean(_pct_change(intangibles, 4))
def cg_f062_impairment_and_writedown_risk_core71_pct_4q_v072_signal(intangibles, depamor, assets, opex):
    return _clean(_pct_change(_safe_div(intangibles, assets), 4))
def cg_f062_impairment_and_writedown_risk_core72_pct_4q_v073_signal(intangibles, depamor, assets, opex):
    return _clean(_pct_change(depamor, 4))
def cg_f062_impairment_and_writedown_risk_core73_pct_4q_v074_signal(intangibles, depamor, assets, opex):
    return _clean(_pct_change(_safe_div(depamor, opex.abs() + 1.0), 4))
def cg_f062_impairment_and_writedown_risk_core74_pct_4q_v075_signal(intangibles, depamor, assets, opex):
    return _clean(_pct_change(_safe_div(depamor, assets), 4))
