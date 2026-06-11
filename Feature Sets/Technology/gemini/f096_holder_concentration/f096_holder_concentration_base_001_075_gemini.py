import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core0-9: mean_4q
def cg_f096_holder_concentration_core00_mean_4q_v001_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(value, 4))
def cg_f096_holder_concentration_core01_mean_4q_v002_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(shrholders, 4))
def cg_f096_holder_concentration_core02_mean_4q_v003_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(totalvalue, 4))
def cg_f096_holder_concentration_core03_mean_4q_v004_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(percentoftotal, 4))
def cg_f096_holder_concentration_core04_mean_4q_v005_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_safe_div(value, totalvalue), 4))
def cg_f096_holder_concentration_core05_mean_4q_v006_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_safe_div(value, shrholders), 4))
def cg_f096_holder_concentration_core06_mean_4q_v007_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_safe_div(totalvalue, shrholders), 4))
def cg_f096_holder_concentration_core07_mean_4q_v008_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_safe_div(value, percentoftotal + 1e-9), 4))
def cg_f096_holder_concentration_core08_mean_4q_v009_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_safe_div(totalvalue, percentoftotal + 1e-9), 4))
def cg_f096_holder_concentration_core09_mean_4q_v010_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_safe_div(shrholders, percentoftotal + 1e-9), 4))
# core10-19: mean_8q
def cg_f096_holder_concentration_core10_mean_8q_v011_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(value, 8))
def cg_f096_holder_concentration_core11_mean_8q_v012_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(shrholders, 8))
def cg_f096_holder_concentration_core12_mean_8q_v013_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(totalvalue, 8))
def cg_f096_holder_concentration_core13_mean_8q_v014_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(percentoftotal, 8))
def cg_f096_holder_concentration_core14_mean_8q_v015_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_safe_div(value, totalvalue), 8))
def cg_f096_holder_concentration_core15_mean_8q_v016_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_safe_div(value, shrholders), 8))
def cg_f096_holder_concentration_core16_mean_8q_v017_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_safe_div(totalvalue, shrholders), 8))
def cg_f096_holder_concentration_core17_mean_8q_v018_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_safe_div(value, percentoftotal + 1e-9), 8))
def cg_f096_holder_concentration_core18_mean_8q_v019_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_safe_div(totalvalue, percentoftotal + 1e-9), 8))
def cg_f096_holder_concentration_core19_mean_8q_v020_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_safe_div(shrholders, percentoftotal + 1e-9), 8))
# core20-29: z_8q
def cg_f096_holder_concentration_core20_z_8q_v021_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(value, 8))
def cg_f096_holder_concentration_core21_z_8q_v022_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(shrholders, 8))
def cg_f096_holder_concentration_core22_z_8q_v023_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(totalvalue, 8))
def cg_f096_holder_concentration_core23_z_8q_v024_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(percentoftotal, 8))
def cg_f096_holder_concentration_core24_z_8q_v025_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_safe_div(value, totalvalue), 8))
def cg_f096_holder_concentration_core25_z_8q_v026_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_safe_div(value, shrholders), 8))
def cg_f096_holder_concentration_core26_z_8q_v027_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_safe_div(totalvalue, shrholders), 8))
def cg_f096_holder_concentration_core27_z_8q_v028_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_safe_div(value, percentoftotal + 1e-9), 8))
def cg_f096_holder_concentration_core28_z_8q_v029_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_safe_div(totalvalue, percentoftotal + 1e-9), 8))
def cg_f096_holder_concentration_core29_z_8q_v030_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_safe_div(shrholders, percentoftotal + 1e-9), 8))
# core30-39: z_20q
def cg_f096_holder_concentration_core30_z_20q_v031_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(value, 20))
def cg_f096_holder_concentration_core31_z_20q_v032_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(shrholders, 20))
def cg_f096_holder_concentration_core32_z_20q_v033_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(totalvalue, 20))
def cg_f096_holder_concentration_core33_z_20q_v034_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(percentoftotal, 20))
def cg_f096_holder_concentration_core34_z_20q_v035_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_safe_div(value, totalvalue), 20))
def cg_f096_holder_concentration_core35_z_20q_v036_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_safe_div(value, shrholders), 20))
def cg_f096_holder_concentration_core36_z_20q_v037_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_safe_div(totalvalue, shrholders), 20))
def cg_f096_holder_concentration_core37_z_20q_v038_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_safe_div(value, percentoftotal + 1e-9), 20))
def cg_f096_holder_concentration_core38_z_20q_v039_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_safe_div(totalvalue, percentoftotal + 1e-9), 20))
def cg_f096_holder_concentration_core39_z_20q_v040_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_safe_div(shrholders, percentoftotal + 1e-9), 20))
# core40-49: rank_12q
def cg_f096_holder_concentration_core40_rank_12q_v041_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(value, 12))
def cg_f096_holder_concentration_core41_rank_12q_v042_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(shrholders, 12))
def cg_f096_holder_concentration_core42_rank_12q_v043_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(totalvalue, 12))
def cg_f096_holder_concentration_core43_rank_12q_v044_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(percentoftotal, 12))
def cg_f096_holder_concentration_core44_rank_12q_v045_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_safe_div(value, totalvalue), 12))
def cg_f096_holder_concentration_core45_rank_12q_v046_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_safe_div(value, shrholders), 12))
def cg_f096_holder_concentration_core46_rank_12q_v047_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_safe_div(totalvalue, shrholders), 12))
def cg_f096_holder_concentration_core47_rank_12q_v048_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_safe_div(value, percentoftotal + 1e-9), 12))
def cg_f096_holder_concentration_core48_rank_12q_v049_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_safe_div(totalvalue, percentoftotal + 1e-9), 12))
def cg_f096_holder_concentration_core49_rank_12q_v050_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_safe_div(shrholders, percentoftotal + 1e-9), 12))
# core50-59: rank_20q
def cg_f096_holder_concentration_core50_rank_20q_v051_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(value, 20))
def cg_f096_holder_concentration_core51_rank_20q_v052_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(shrholders, 20))
def cg_f096_holder_concentration_core52_rank_20q_v053_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(totalvalue, 20))
def cg_f096_holder_concentration_core53_rank_20q_v054_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(percentoftotal, 20))
def cg_f096_holder_concentration_core54_rank_20q_v055_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_safe_div(value, totalvalue), 20))
def cg_f096_holder_concentration_core55_rank_20q_v056_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_safe_div(value, shrholders), 20))
def cg_f096_holder_concentration_core56_rank_20q_v057_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_safe_div(totalvalue, shrholders), 20))
def cg_f096_holder_concentration_core57_rank_20q_v058_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_safe_div(value, percentoftotal + 1e-9), 20))
def cg_f096_holder_concentration_core58_rank_20q_v059_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_safe_div(totalvalue, percentoftotal + 1e-9), 20))
def cg_f096_holder_concentration_core59_rank_20q_v060_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_safe_div(shrholders, percentoftotal + 1e-9), 20))
# core60-69: pct_1q
def cg_f096_holder_concentration_core60_pct_1q_v061_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_pct_change(value, 1))
def cg_f096_holder_concentration_core61_pct_1q_v062_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_pct_change(shrholders, 1))
def cg_f096_holder_concentration_core62_pct_1q_v063_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_pct_change(totalvalue, 1))
def cg_f096_holder_concentration_core63_pct_1q_v064_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_pct_change(percentoftotal, 1))
def cg_f096_holder_concentration_core64_pct_1q_v065_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_pct_change(_safe_div(value, totalvalue), 1))
def cg_f096_holder_concentration_core65_pct_1q_v066_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_pct_change(_safe_div(value, shrholders), 1))
def cg_f096_holder_concentration_core66_pct_1q_v067_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_pct_change(_safe_div(totalvalue, shrholders), 1))
def cg_f096_holder_concentration_core67_pct_1q_v068_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_pct_change(_safe_div(value, percentoftotal + 1e-9), 1))
def cg_f096_holder_concentration_core68_pct_1q_v069_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_pct_change(_safe_div(totalvalue, percentoftotal + 1e-9), 1))
def cg_f096_holder_concentration_core69_pct_1q_v070_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_pct_change(_safe_div(shrholders, percentoftotal + 1e-9), 1))
# core70-79: pct_4q
def cg_f096_holder_concentration_core70_pct_4q_v071_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_pct_change(value, 4))
def cg_f096_holder_concentration_core71_pct_4q_v072_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_pct_change(shrholders, 4))
def cg_f096_holder_concentration_core72_pct_4q_v073_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_pct_change(totalvalue, 4))
def cg_f096_holder_concentration_core73_pct_4q_v074_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_pct_change(percentoftotal, 4))
def cg_f096_holder_concentration_core74_pct_4q_v075_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_pct_change(_safe_div(value, totalvalue), 4))
