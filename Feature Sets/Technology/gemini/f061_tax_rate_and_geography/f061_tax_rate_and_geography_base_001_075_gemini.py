import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core00-09: mean 4q
def cg_f061_tax_rate_and_geography_core00_mean_4q_v001_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(taxexp, 4))
def cg_f061_tax_rate_and_geography_core01_mean_4q_v002_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_safe_div(taxexp, ebt), 4))
def cg_f061_tax_rate_and_geography_core02_mean_4q_v003_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_safe_div(taxexp, taxassets.abs() + 1.0), 4))
def cg_f061_tax_rate_and_geography_core03_mean_4q_v004_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_safe_div(taxexp, taxliabilities.abs() + 1.0), 4))
def cg_f061_tax_rate_and_geography_core04_mean_4q_v005_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(taxassets, 4))
def cg_f061_tax_rate_and_geography_core05_mean_4q_v006_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_safe_div(taxassets, taxliabilities.abs() + 1.0), 4))
def cg_f061_tax_rate_and_geography_core06_mean_4q_v007_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_safe_div(taxassets, ebt.abs() + 1.0), 4))
def cg_f061_tax_rate_and_geography_core07_mean_4q_v008_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(taxliabilities, 4))
def cg_f061_tax_rate_and_geography_core08_mean_4q_v009_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_safe_div(taxliabilities, ebt.abs() + 1.0), 4))
def cg_f061_tax_rate_and_geography_core09_mean_4q_v010_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_safe_div(taxexp, (taxassets + taxliabilities).abs() + 1.0), 4))

# core10-19: mean 8q
def cg_f061_tax_rate_and_geography_core10_mean_8q_v011_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(taxexp, 8))
def cg_f061_tax_rate_and_geography_core11_mean_8q_v012_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_safe_div(taxexp, ebt), 8))
def cg_f061_tax_rate_and_geography_core12_mean_8q_v013_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_safe_div(taxexp, taxassets.abs() + 1.0), 8))
def cg_f061_tax_rate_and_geography_core13_mean_8q_v014_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_safe_div(taxexp, taxliabilities.abs() + 1.0), 8))
def cg_f061_tax_rate_and_geography_core14_mean_8q_v015_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(taxassets, 8))
def cg_f061_tax_rate_and_geography_core15_mean_8q_v016_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_safe_div(taxassets, taxliabilities.abs() + 1.0), 8))
def cg_f061_tax_rate_and_geography_core16_mean_8q_v017_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_safe_div(taxassets, ebt.abs() + 1.0), 8))
def cg_f061_tax_rate_and_geography_core17_mean_8q_v018_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(taxliabilities, 8))
def cg_f061_tax_rate_and_geography_core18_mean_8q_v019_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_safe_div(taxliabilities, ebt.abs() + 1.0), 8))
def cg_f061_tax_rate_and_geography_core19_mean_8q_v020_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_safe_div(taxexp, (taxassets + taxliabilities).abs() + 1.0), 8))

# core20-29: z 8q
def cg_f061_tax_rate_and_geography_core20_z_8q_v021_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(taxexp, 8))
def cg_f061_tax_rate_and_geography_core21_z_8q_v022_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_safe_div(taxexp, ebt), 8))
def cg_f061_tax_rate_and_geography_core22_z_8q_v023_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_safe_div(taxexp, taxassets.abs() + 1.0), 8))
def cg_f061_tax_rate_and_geography_core23_z_8q_v024_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_safe_div(taxexp, taxliabilities.abs() + 1.0), 8))
def cg_f061_tax_rate_and_geography_core24_z_8q_v025_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(taxassets, 8))
def cg_f061_tax_rate_and_geography_core25_z_8q_v026_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_safe_div(taxassets, taxliabilities.abs() + 1.0), 8))
def cg_f061_tax_rate_and_geography_core26_z_8q_v027_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_safe_div(taxassets, ebt.abs() + 1.0), 8))
def cg_f061_tax_rate_and_geography_core27_z_8q_v028_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(taxliabilities, 8))
def cg_f061_tax_rate_and_geography_core28_z_8q_v029_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_safe_div(taxliabilities, ebt.abs() + 1.0), 8))
def cg_f061_tax_rate_and_geography_core29_z_8q_v030_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_safe_div(taxexp, (taxassets + taxliabilities).abs() + 1.0), 8))

# core30-39: z 20q
def cg_f061_tax_rate_and_geography_core30_z_20q_v031_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(taxexp, 20))
def cg_f061_tax_rate_and_geography_core31_z_20q_v032_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_safe_div(taxexp, ebt), 20))
def cg_f061_tax_rate_and_geography_core32_z_20q_v033_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_safe_div(taxexp, taxassets.abs() + 1.0), 20))
def cg_f061_tax_rate_and_geography_core33_z_20q_v034_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_safe_div(taxexp, taxliabilities.abs() + 1.0), 20))
def cg_f061_tax_rate_and_geography_core34_z_20q_v035_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(taxassets, 20))
def cg_f061_tax_rate_and_geography_core35_z_20q_v036_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_safe_div(taxassets, taxliabilities.abs() + 1.0), 20))
def cg_f061_tax_rate_and_geography_core36_z_20q_v037_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_safe_div(taxassets, ebt.abs() + 1.0), 20))
def cg_f061_tax_rate_and_geography_core37_z_20q_v038_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(taxliabilities, 20))
def cg_f061_tax_rate_and_geography_core38_z_20q_v039_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_safe_div(taxliabilities, ebt.abs() + 1.0), 20))
def cg_f061_tax_rate_and_geography_core39_z_20q_v040_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_safe_div(taxexp, (taxassets + taxliabilities).abs() + 1.0), 20))

# core40-49: rank 8q
def cg_f061_tax_rate_and_geography_core40_rank_8q_v041_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(taxexp, 8))
def cg_f061_tax_rate_and_geography_core41_rank_8q_v042_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_safe_div(taxexp, ebt), 8))
def cg_f061_tax_rate_and_geography_core42_rank_8q_v043_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_safe_div(taxexp, taxassets.abs() + 1.0), 8))
def cg_f061_tax_rate_and_geography_core43_rank_8q_v044_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_safe_div(taxexp, taxliabilities.abs() + 1.0), 8))
def cg_f061_tax_rate_and_geography_core44_rank_8q_v045_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(taxassets, 8))
def cg_f061_tax_rate_and_geography_core45_rank_8q_v046_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_safe_div(taxassets, taxliabilities.abs() + 1.0), 8))
def cg_f061_tax_rate_and_geography_core46_rank_8q_v047_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_safe_div(taxassets, ebt.abs() + 1.0), 8))
def cg_f061_tax_rate_and_geography_core47_rank_8q_v048_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(taxliabilities, 8))
def cg_f061_tax_rate_and_geography_core48_rank_8q_v049_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_safe_div(taxliabilities, ebt.abs() + 1.0), 8))
def cg_f061_tax_rate_and_geography_core49_rank_8q_v050_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_safe_div(taxexp, (taxassets + taxliabilities).abs() + 1.0), 8))

# core50-59: rank 20q
def cg_f061_tax_rate_and_geography_core50_rank_20q_v051_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(taxexp, 20))
def cg_f061_tax_rate_and_geography_core51_rank_20q_v052_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_safe_div(taxexp, ebt), 20))
def cg_f061_tax_rate_and_geography_core52_rank_20q_v053_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_safe_div(taxexp, taxassets.abs() + 1.0), 20))
def cg_f061_tax_rate_and_geography_core53_rank_20q_v054_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_safe_div(taxexp, taxliabilities.abs() + 1.0), 20))
def cg_f061_tax_rate_and_geography_core54_rank_20q_v055_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(taxassets, 20))
def cg_f061_tax_rate_and_geography_core55_rank_20q_v056_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_safe_div(taxassets, taxliabilities.abs() + 1.0), 20))
def cg_f061_tax_rate_and_geography_core56_rank_20q_v057_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_safe_div(taxassets, ebt.abs() + 1.0), 20))
def cg_f061_tax_rate_and_geography_core57_rank_20q_v058_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(taxliabilities, 20))
def cg_f061_tax_rate_and_geography_core58_rank_20q_v059_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_safe_div(taxliabilities, ebt.abs() + 1.0), 20))
def cg_f061_tax_rate_and_geography_core59_rank_20q_v060_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_safe_div(taxexp, (taxassets + taxliabilities).abs() + 1.0), 20))

# core60-69: pct 1q
def cg_f061_tax_rate_and_geography_core60_pct_1q_v061_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_pct_change(taxexp, 1))
def cg_f061_tax_rate_and_geography_core61_pct_1q_v062_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_pct_change(_safe_div(taxexp, ebt), 1))
def cg_f061_tax_rate_and_geography_core62_pct_1q_v063_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_pct_change(_safe_div(taxexp, taxassets.abs() + 1.0), 1))
def cg_f061_tax_rate_and_geography_core63_pct_1q_v064_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_pct_change(_safe_div(taxexp, taxliabilities.abs() + 1.0), 1))
def cg_f061_tax_rate_and_geography_core64_pct_1q_v065_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_pct_change(taxassets, 1))
def cg_f061_tax_rate_and_geography_core65_pct_1q_v066_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_pct_change(_safe_div(taxassets, taxliabilities.abs() + 1.0), 1))
def cg_f061_tax_rate_and_geography_core66_pct_1q_v067_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_pct_change(_safe_div(taxassets, ebt.abs() + 1.0), 1))
def cg_f061_tax_rate_and_geography_core67_pct_1q_v068_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_pct_change(taxliabilities, 1))
def cg_f061_tax_rate_and_geography_core68_pct_1q_v069_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_pct_change(_safe_div(taxliabilities, ebt.abs() + 1.0), 1))
def cg_f061_tax_rate_and_geography_core69_pct_1q_v070_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_pct_change(_safe_div(taxexp, (taxassets + taxliabilities).abs() + 1.0), 1))

# core70-74: pct 4q
def cg_f061_tax_rate_and_geography_core70_pct_4q_v071_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_pct_change(taxexp, 4))
def cg_f061_tax_rate_and_geography_core71_pct_4q_v072_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_pct_change(_safe_div(taxexp, ebt), 4))
def cg_f061_tax_rate_and_geography_core72_pct_4q_v073_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_pct_change(_safe_div(taxexp, taxassets.abs() + 1.0), 4))
def cg_f061_tax_rate_and_geography_core73_pct_4q_v074_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_pct_change(_safe_div(taxexp, taxliabilities.abs() + 1.0), 4))
def cg_f061_tax_rate_and_geography_core74_pct_4q_v075_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_pct_change(taxassets, 4))
