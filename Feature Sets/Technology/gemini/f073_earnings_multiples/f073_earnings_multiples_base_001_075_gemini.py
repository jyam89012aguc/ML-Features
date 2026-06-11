import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core00-09: mean 4q
def cg_f073_earnings_multiples_core00_mean_4q_v001_signal(pe, evebitda, ebit, ebitda):
    return _clean(_mean(pe, 4))
def cg_f073_earnings_multiples_core01_mean_4q_v002_signal(pe, evebitda, ebit, ebitda):
    return _clean(_mean(evebitda, 4))
def cg_f073_earnings_multiples_core02_mean_4q_v003_signal(pe, evebitda, ebit, ebitda):
    return _clean(_mean(ebit, 4))
def cg_f073_earnings_multiples_core03_mean_4q_v004_signal(pe, evebitda, ebit, ebitda):
    return _clean(_mean(ebitda, 4))
def cg_f073_earnings_multiples_core04_mean_4q_v005_signal(pe, evebitda, ebit, ebitda):
    return _clean(_mean(_safe_div(ebit, ebitda), 4))
def cg_f073_earnings_multiples_core05_mean_4q_v006_signal(pe, evebitda, ebit, ebitda):
    return _clean(_mean(_safe_div(pe, evebitda.abs() + 1.0), 4))
def cg_f073_earnings_multiples_core06_mean_4q_v007_signal(pe, evebitda, ebit, ebitda):
    return _clean(_mean(pe - evebitda, 4))
def cg_f073_earnings_multiples_core07_mean_4q_v008_signal(pe, evebitda, ebit, ebitda):
    return _clean(_mean(ebitda - ebit, 4))
def cg_f073_earnings_multiples_core08_mean_4q_v009_signal(pe, evebitda, ebit, ebitda):
    return _clean(_mean(_safe_div(pe, ebit.abs() + 1.0), 4))
def cg_f073_earnings_multiples_core09_mean_4q_v010_signal(pe, evebitda, ebit, ebitda):
    return _clean(_mean(_safe_div(evebitda, ebitda.abs() + 1.0), 4))

# core10-19: mean 8q
def cg_f073_earnings_multiples_core10_mean_8q_v011_signal(pe, evebitda, ebit, ebitda):
    return _clean(_mean(pe, 8))
def cg_f073_earnings_multiples_core11_mean_8q_v012_signal(pe, evebitda, ebit, ebitda):
    return _clean(_mean(evebitda, 8))
def cg_f073_earnings_multiples_core12_mean_8q_v013_signal(pe, evebitda, ebit, ebitda):
    return _clean(_mean(ebit, 8))
def cg_f073_earnings_multiples_core13_mean_8q_v014_signal(pe, evebitda, ebit, ebitda):
    return _clean(_mean(ebitda, 8))
def cg_f073_earnings_multiples_core14_mean_8q_v015_signal(pe, evebitda, ebit, ebitda):
    return _clean(_mean(_safe_div(ebit, ebitda), 8))
def cg_f073_earnings_multiples_core15_mean_8q_v016_signal(pe, evebitda, ebit, ebitda):
    return _clean(_mean(_safe_div(pe, evebitda.abs() + 1.0), 8))
def cg_f073_earnings_multiples_core16_mean_8q_v017_signal(pe, evebitda, ebit, ebitda):
    return _clean(_mean(pe - evebitda, 8))
def cg_f073_earnings_multiples_core17_mean_8q_v018_signal(pe, evebitda, ebit, ebitda):
    return _clean(_mean(ebitda - ebit, 8))
def cg_f073_earnings_multiples_core18_mean_8q_v019_signal(pe, evebitda, ebit, ebitda):
    return _clean(_mean(_safe_div(pe, ebit.abs() + 1.0), 8))
def cg_f073_earnings_multiples_core19_mean_8q_v020_signal(pe, evebitda, ebit, ebitda):
    return _clean(_mean(_safe_div(evebitda, ebitda.abs() + 1.0), 8))

# core20-29: z 8q
def cg_f073_earnings_multiples_core20_z_8q_v021_signal(pe, evebitda, ebit, ebitda):
    return _clean(_z(pe, 8))
def cg_f073_earnings_multiples_core21_z_8q_v022_signal(pe, evebitda, ebit, ebitda):
    return _clean(_z(evebitda, 8))
def cg_f073_earnings_multiples_core22_z_8q_v023_signal(pe, evebitda, ebit, ebitda):
    return _clean(_z(ebit, 8))
def cg_f073_earnings_multiples_core23_z_8q_v024_signal(pe, evebitda, ebit, ebitda):
    return _clean(_z(ebitda, 8))
def cg_f073_earnings_multiples_core24_z_8q_v025_signal(pe, evebitda, ebit, ebitda):
    return _clean(_z(_safe_div(ebit, ebitda), 8))
def cg_f073_earnings_multiples_core25_z_8q_v026_signal(pe, evebitda, ebit, ebitda):
    return _clean(_z(_safe_div(pe, evebitda.abs() + 1.0), 8))
def cg_f073_earnings_multiples_core26_z_8q_v027_signal(pe, evebitda, ebit, ebitda):
    return _clean(_z(pe - evebitda, 8))
def cg_f073_earnings_multiples_core27_z_8q_v028_signal(pe, evebitda, ebit, ebitda):
    return _clean(_z(ebitda - ebit, 8))
def cg_f073_earnings_multiples_core28_z_8q_v029_signal(pe, evebitda, ebit, ebitda):
    return _clean(_z(_safe_div(pe, ebit.abs() + 1.0), 8))
def cg_f073_earnings_multiples_core29_z_8q_v030_signal(pe, evebitda, ebit, ebitda):
    return _clean(_z(_safe_div(evebitda, ebitda.abs() + 1.0), 8))

# core30-39: z 20q
def cg_f073_earnings_multiples_core30_z_20q_v031_signal(pe, evebitda, ebit, ebitda):
    return _clean(_z(pe, 20))
def cg_f073_earnings_multiples_core31_z_20q_v032_signal(pe, evebitda, ebit, ebitda):
    return _clean(_z(evebitda, 20))
def cg_f073_earnings_multiples_core32_z_20q_v033_signal(pe, evebitda, ebit, ebitda):
    return _clean(_z(ebit, 20))
def cg_f073_earnings_multiples_core33_z_20q_v034_signal(pe, evebitda, ebit, ebitda):
    return _clean(_z(ebitda, 20))
def cg_f073_earnings_multiples_core34_z_20q_v035_signal(pe, evebitda, ebit, ebitda):
    return _clean(_z(_safe_div(ebit, ebitda), 20))
def cg_f073_earnings_multiples_core35_z_20q_v036_signal(pe, evebitda, ebit, ebitda):
    return _clean(_z(_safe_div(pe, evebitda.abs() + 1.0), 20))
def cg_f073_earnings_multiples_core36_z_20q_v037_signal(pe, evebitda, ebit, ebitda):
    return _clean(_z(pe - evebitda, 20))
def cg_f073_earnings_multiples_core37_z_20q_v038_signal(pe, evebitda, ebit, ebitda):
    return _clean(_z(ebitda - ebit, 20))
def cg_f073_earnings_multiples_core38_z_20q_v039_signal(pe, evebitda, ebit, ebitda):
    return _clean(_z(_safe_div(pe, ebit.abs() + 1.0), 20))
def cg_f073_earnings_multiples_core39_z_20q_v040_signal(pe, evebitda, ebit, ebitda):
    return _clean(_z(_safe_div(evebitda, ebitda.abs() + 1.0), 20))

# core40-49: rank 12q
def cg_f073_earnings_multiples_core40_rank_12q_v041_signal(pe, evebitda, ebit, ebitda):
    return _clean(_rank(pe, 12))
def cg_f073_earnings_multiples_core41_rank_12q_v042_signal(pe, evebitda, ebit, ebitda):
    return _clean(_rank(evebitda, 12))
def cg_f073_earnings_multiples_core42_rank_12q_v043_signal(pe, evebitda, ebit, ebitda):
    return _clean(_rank(ebit, 12))
def cg_f073_earnings_multiples_core43_rank_12q_v044_signal(pe, evebitda, ebit, ebitda):
    return _clean(_rank(ebitda, 12))
def cg_f073_earnings_multiples_core44_rank_12q_v045_signal(pe, evebitda, ebit, ebitda):
    return _clean(_rank(_safe_div(ebit, ebitda), 12))
def cg_f073_earnings_multiples_core45_rank_12q_v046_signal(pe, evebitda, ebit, ebitda):
    return _clean(_rank(_safe_div(pe, evebitda.abs() + 1.0), 12))
def cg_f073_earnings_multiples_core46_rank_12q_v047_signal(pe, evebitda, ebit, ebitda):
    return _clean(_rank(pe - evebitda, 12))
def cg_f073_earnings_multiples_core47_rank_12q_v048_signal(pe, evebitda, ebit, ebitda):
    return _clean(_rank(ebitda - ebit, 12))
def cg_f073_earnings_multiples_core48_rank_12q_v049_signal(pe, evebitda, ebit, ebitda):
    return _clean(_rank(_safe_div(pe, ebit.abs() + 1.0), 12))
def cg_f073_earnings_multiples_core49_rank_12q_v050_signal(pe, evebitda, ebit, ebitda):
    return _clean(_rank(_safe_div(evebitda, ebitda.abs() + 1.0), 12))

# core50-59: rank 20q
def cg_f073_earnings_multiples_core50_rank_20q_v051_signal(pe, evebitda, ebit, ebitda):
    return _clean(_rank(pe, 20))
def cg_f073_earnings_multiples_core51_rank_20q_v052_signal(pe, evebitda, ebit, ebitda):
    return _clean(_rank(evebitda, 20))
def cg_f073_earnings_multiples_core52_rank_20q_v053_signal(pe, evebitda, ebit, ebitda):
    return _clean(_rank(ebit, 20))
def cg_f073_earnings_multiples_core53_rank_20q_v054_signal(pe, evebitda, ebit, ebitda):
    return _clean(_rank(ebitda, 20))
def cg_f073_earnings_multiples_core54_rank_20q_v055_signal(pe, evebitda, ebit, ebitda):
    return _clean(_rank(_safe_div(ebit, ebitda), 20))
def cg_f073_earnings_multiples_core55_rank_20q_v056_signal(pe, evebitda, ebit, ebitda):
    return _clean(_rank(_safe_div(pe, evebitda.abs() + 1.0), 20))
def cg_f073_earnings_multiples_core56_rank_20q_v057_signal(pe, evebitda, ebit, ebitda):
    return _clean(_rank(pe - evebitda, 20))
def cg_f073_earnings_multiples_core57_rank_20q_v058_signal(pe, evebitda, ebit, ebitda):
    return _clean(_rank(ebitda - ebit, 20))
def cg_f073_earnings_multiples_core58_rank_20q_v059_signal(pe, evebitda, ebit, ebitda):
    return _clean(_rank(_safe_div(pe, ebit.abs() + 1.0), 20))
def cg_f073_earnings_multiples_core59_rank_20q_v060_signal(pe, evebitda, ebit, ebitda):
    return _clean(_rank(_safe_div(evebitda, ebitda.abs() + 1.0), 20))

# core60-69: pct 1q
def cg_f073_earnings_multiples_core60_pct_1q_v061_signal(pe, evebitda, ebit, ebitda):
    return _clean(_pct_change(pe, 1))
def cg_f073_earnings_multiples_core61_pct_1q_v062_signal(pe, evebitda, ebit, ebitda):
    return _clean(_pct_change(evebitda, 1))
def cg_f073_earnings_multiples_core62_pct_1q_v063_signal(pe, evebitda, ebit, ebitda):
    return _clean(_pct_change(ebit, 1))
def cg_f073_earnings_multiples_core63_pct_1q_v064_signal(pe, evebitda, ebit, ebitda):
    return _clean(_pct_change(ebitda, 1))
def cg_f073_earnings_multiples_core64_pct_1q_v065_signal(pe, evebitda, ebit, ebitda):
    return _clean(_pct_change(_safe_div(ebit, ebitda), 1))
def cg_f073_earnings_multiples_core65_pct_1q_v066_signal(pe, evebitda, ebit, ebitda):
    return _clean(_pct_change(_safe_div(pe, evebitda.abs() + 1.0), 1))
def cg_f073_earnings_multiples_core66_pct_1q_v067_signal(pe, evebitda, ebit, ebitda):
    return _clean(_pct_change(pe - evebitda, 1))
def cg_f073_earnings_multiples_core67_pct_1q_v068_signal(pe, evebitda, ebit, ebitda):
    return _clean(_pct_change(ebitda - ebit, 1))
def cg_f073_earnings_multiples_core68_pct_1q_v069_signal(pe, evebitda, ebit, ebitda):
    return _clean(_pct_change(_safe_div(pe, ebit.abs() + 1.0), 1))
def cg_f073_earnings_multiples_core69_pct_1q_v070_signal(pe, evebitda, ebit, ebitda):
    return _clean(_pct_change(_safe_div(evebitda, ebitda.abs() + 1.0), 1))

# core70-74: pct 4q
def cg_f073_earnings_multiples_core70_pct_4q_v071_signal(pe, evebitda, ebit, ebitda):
    return _clean(_pct_change(pe, 4))
def cg_f073_earnings_multiples_core71_pct_4q_v072_signal(pe, evebitda, ebit, ebitda):
    return _clean(_pct_change(evebitda, 4))
def cg_f073_earnings_multiples_core72_pct_4q_v073_signal(pe, evebitda, ebit, ebitda):
    return _clean(_pct_change(ebit, 4))
def cg_f073_earnings_multiples_core73_pct_4q_v074_signal(pe, evebitda, ebit, ebitda):
    return _clean(_pct_change(ebitda, 4))
def cg_f073_earnings_multiples_core74_pct_4q_v075_signal(pe, evebitda, ebit, ebitda):
    return _clean(_pct_change(_safe_div(ebit, ebitda), 4))
