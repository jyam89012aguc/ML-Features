import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core0-9: mean_4q
def cg_f099_sec_8k_event_density_core00_mean_4q_v001_signal(ticker, date, eventcodes):
    return _clean(_mean(_event_count(eventcodes, 4), 4))
def cg_f099_sec_8k_event_density_core01_mean_4q_v002_signal(ticker, date, eventcodes):
    return _clean(_mean(_event_count(eventcodes, 12), 4))
def cg_f099_sec_8k_event_density_core02_mean_4q_v003_signal(ticker, date, eventcodes):
    return _clean(_mean(_event_count(eventcodes, 20), 4))
def cg_f099_sec_8k_event_density_core03_mean_4q_v004_signal(ticker, date, eventcodes):
    return _clean(_mean(_event_rate(eventcodes, 4), 4))
def cg_f099_sec_8k_event_density_core04_mean_4q_v005_signal(ticker, date, eventcodes):
    return _clean(_mean(_event_rate(eventcodes, 12), 4))
def cg_f099_sec_8k_event_density_core05_mean_4q_v006_signal(ticker, date, eventcodes):
    return _clean(_mean(_event_rate(eventcodes, 20), 4))
def cg_f099_sec_8k_event_density_core06_mean_4q_v007_signal(ticker, date, eventcodes):
    return _clean(_mean(_z(_event_count(eventcodes, 12), 20), 4))
def cg_f099_sec_8k_event_density_core07_mean_4q_v008_signal(ticker, date, eventcodes):
    return _clean(_mean(_rank(_event_count(eventcodes, 12), 20), 4))
def cg_f099_sec_8k_event_density_core08_mean_4q_v009_signal(ticker, date, eventcodes):
    return _clean(_mean(_diff(_event_count(eventcodes, 4), 1), 4))
def cg_f099_sec_8k_event_density_core09_mean_4q_v010_signal(ticker, date, eventcodes):
    return _clean(_mean(_pct_change(_event_count(eventcodes, 12) + 1, 4), 4))
# core10-19: mean_8q
def cg_f099_sec_8k_event_density_core10_mean_8q_v011_signal(ticker, date, eventcodes):
    return _clean(_mean(_event_count(eventcodes, 4), 8))
def cg_f099_sec_8k_event_density_core11_mean_8q_v012_signal(ticker, date, eventcodes):
    return _clean(_mean(_event_count(eventcodes, 12), 8))
def cg_f099_sec_8k_event_density_core12_mean_8q_v013_signal(ticker, date, eventcodes):
    return _clean(_mean(_event_count(eventcodes, 20), 8))
def cg_f099_sec_8k_event_density_core13_mean_8q_v014_signal(ticker, date, eventcodes):
    return _clean(_mean(_event_rate(eventcodes, 4), 8))
def cg_f099_sec_8k_event_density_core14_mean_8q_v015_signal(ticker, date, eventcodes):
    return _clean(_mean(_event_rate(eventcodes, 12), 8))
def cg_f099_sec_8k_event_density_core15_mean_8q_v016_signal(ticker, date, eventcodes):
    return _clean(_mean(_event_rate(eventcodes, 20), 8))
def cg_f099_sec_8k_event_density_core16_mean_8q_v017_signal(ticker, date, eventcodes):
    return _clean(_mean(_z(_event_count(eventcodes, 12), 20), 8))
def cg_f099_sec_8k_event_density_core17_mean_8q_v018_signal(ticker, date, eventcodes):
    return _clean(_mean(_rank(_event_count(eventcodes, 12), 20), 8))
def cg_f099_sec_8k_event_density_core18_mean_8q_v019_signal(ticker, date, eventcodes):
    return _clean(_mean(_diff(_event_count(eventcodes, 4), 1), 8))
def cg_f099_sec_8k_event_density_core19_mean_8q_v020_signal(ticker, date, eventcodes):
    return _clean(_mean(_pct_change(_event_count(eventcodes, 12) + 1, 4), 8))
# core20-29: z_8q
def cg_f099_sec_8k_event_density_core20_z_8q_v021_signal(ticker, date, eventcodes):
    return _clean(_z(_event_count(eventcodes, 4), 8))
def cg_f099_sec_8k_event_density_core21_z_8q_v022_signal(ticker, date, eventcodes):
    return _clean(_z(_event_count(eventcodes, 12), 8))
def cg_f099_sec_8k_event_density_core22_z_8q_v023_signal(ticker, date, eventcodes):
    return _clean(_z(_event_count(eventcodes, 20), 8))
def cg_f099_sec_8k_event_density_core23_z_8q_v024_signal(ticker, date, eventcodes):
    return _clean(_z(_event_rate(eventcodes, 4), 8))
def cg_f099_sec_8k_event_density_core24_z_8q_v025_signal(ticker, date, eventcodes):
    return _clean(_z(_event_rate(eventcodes, 12), 8))
def cg_f099_sec_8k_event_density_core25_z_8q_v026_signal(ticker, date, eventcodes):
    return _clean(_z(_event_rate(eventcodes, 20), 8))
def cg_f099_sec_8k_event_density_core26_z_8q_v027_signal(ticker, date, eventcodes):
    return _clean(_z(_z(_event_count(eventcodes, 12), 20), 8))
def cg_f099_sec_8k_event_density_core27_z_8q_v028_signal(ticker, date, eventcodes):
    return _clean(_z(_rank(_event_count(eventcodes, 12), 20), 8))
def cg_f099_sec_8k_event_density_core28_z_8q_v029_signal(ticker, date, eventcodes):
    return _clean(_z(_diff(_event_count(eventcodes, 4), 1), 8))
def cg_f099_sec_8k_event_density_core29_z_8q_v030_signal(ticker, date, eventcodes):
    return _clean(_z(_pct_change(_event_count(eventcodes, 12) + 1, 4), 8))
# core30-39: z_20q
def cg_f099_sec_8k_event_density_core30_z_20q_v031_signal(ticker, date, eventcodes):
    return _clean(_z(_event_count(eventcodes, 4), 20))
def cg_f099_sec_8k_event_density_core31_z_20q_v032_signal(ticker, date, eventcodes):
    return _clean(_z(_event_count(eventcodes, 12), 20))
def cg_f099_sec_8k_event_density_core32_z_20q_v033_signal(ticker, date, eventcodes):
    return _clean(_z(_event_count(eventcodes, 20), 20))
def cg_f099_sec_8k_event_density_core33_z_20q_v034_signal(ticker, date, eventcodes):
    return _clean(_z(_event_rate(eventcodes, 4), 20))
def cg_f099_sec_8k_event_density_core34_z_20q_v035_signal(ticker, date, eventcodes):
    return _clean(_z(_event_rate(eventcodes, 12), 20))
def cg_f099_sec_8k_event_density_core35_z_20q_v036_signal(ticker, date, eventcodes):
    return _clean(_z(_event_rate(eventcodes, 20), 20))
def cg_f099_sec_8k_event_density_core36_z_20q_v037_signal(ticker, date, eventcodes):
    return _clean(_z(_z(_event_count(eventcodes, 12), 20), 20))
def cg_f099_sec_8k_event_density_core37_z_20q_v038_signal(ticker, date, eventcodes):
    return _clean(_z(_rank(_event_count(eventcodes, 12), 20), 20))
def cg_f099_sec_8k_event_density_core38_z_20q_v039_signal(ticker, date, eventcodes):
    return _clean(_z(_diff(_event_count(eventcodes, 4), 1), 20))
def cg_f099_sec_8k_event_density_core39_z_20q_v040_signal(ticker, date, eventcodes):
    return _clean(_z(_pct_change(_event_count(eventcodes, 12) + 1, 4), 20))
# core40-49: rank_12q
def cg_f099_sec_8k_event_density_core40_rank_12q_v041_signal(ticker, date, eventcodes):
    return _clean(_rank(_event_count(eventcodes, 4), 12))
def cg_f099_sec_8k_event_density_core41_rank_12q_v042_signal(ticker, date, eventcodes):
    return _clean(_rank(_event_count(eventcodes, 12), 12))
def cg_f099_sec_8k_event_density_core42_rank_12q_v043_signal(ticker, date, eventcodes):
    return _clean(_rank(_event_count(eventcodes, 20), 12))
def cg_f099_sec_8k_event_density_core43_rank_12q_v044_signal(ticker, date, eventcodes):
    return _clean(_rank(_event_rate(eventcodes, 4), 12))
def cg_f099_sec_8k_event_density_core44_rank_12q_v045_signal(ticker, date, eventcodes):
    return _clean(_rank(_event_rate(eventcodes, 12), 12))
def cg_f099_sec_8k_event_density_core45_rank_12q_v046_signal(ticker, date, eventcodes):
    return _clean(_rank(_event_rate(eventcodes, 20), 12))
def cg_f099_sec_8k_event_density_core46_rank_12q_v047_signal(ticker, date, eventcodes):
    return _clean(_rank(_z(_event_count(eventcodes, 12), 20), 12))
def cg_f099_sec_8k_event_density_core47_rank_12q_v048_signal(ticker, date, eventcodes):
    return _clean(_rank(_rank(_event_count(eventcodes, 12), 20), 12))
def cg_f099_sec_8k_event_density_core48_rank_12q_v049_signal(ticker, date, eventcodes):
    return _clean(_rank(_diff(_event_count(eventcodes, 4), 1), 12))
def cg_f099_sec_8k_event_density_core49_rank_12q_v050_signal(ticker, date, eventcodes):
    return _clean(_rank(_pct_change(_event_count(eventcodes, 12) + 1, 4), 12))
# core50-59: rank_20q
def cg_f099_sec_8k_event_density_core50_rank_20q_v051_signal(ticker, date, eventcodes):
    return _clean(_rank(_event_count(eventcodes, 4), 20))
def cg_f099_sec_8k_event_density_core51_rank_20q_v052_signal(ticker, date, eventcodes):
    return _clean(_rank(_event_count(eventcodes, 12), 20))
def cg_f099_sec_8k_event_density_core52_rank_20q_v053_signal(ticker, date, eventcodes):
    return _clean(_rank(_event_count(eventcodes, 20), 20))
def cg_f099_sec_8k_event_density_core53_rank_20q_v054_signal(ticker, date, eventcodes):
    return _clean(_rank(_event_rate(eventcodes, 4), 20))
def cg_f099_sec_8k_event_density_core54_rank_20q_v055_signal(ticker, date, eventcodes):
    return _clean(_rank(_event_rate(eventcodes, 12), 20))
def cg_f099_sec_8k_event_density_core55_rank_20q_v056_signal(ticker, date, eventcodes):
    return _clean(_rank(_event_rate(eventcodes, 20), 20))
def cg_f099_sec_8k_event_density_core56_rank_20q_v057_signal(ticker, date, eventcodes):
    return _clean(_rank(_z(_event_count(eventcodes, 12), 20), 20))
def cg_f099_sec_8k_event_density_core57_rank_20q_v058_signal(ticker, date, eventcodes):
    return _clean(_rank(_rank(_event_count(eventcodes, 12), 20), 20))
def cg_f099_sec_8k_event_density_core58_rank_20q_v059_signal(ticker, date, eventcodes):
    return _clean(_rank(_diff(_event_count(eventcodes, 4), 1), 20))
def cg_f099_sec_8k_event_density_core59_rank_20q_v060_signal(ticker, date, eventcodes):
    return _clean(_rank(_pct_change(_event_count(eventcodes, 12) + 1, 4), 20))
# core60-69: pct_1q
def cg_f099_sec_8k_event_density_core60_pct_1q_v061_signal(ticker, date, eventcodes):
    return _clean(_pct_change(_event_count(eventcodes, 4), 1))
def cg_f099_sec_8k_event_density_core61_pct_1q_v062_signal(ticker, date, eventcodes):
    return _clean(_pct_change(_event_count(eventcodes, 12), 1))
def cg_f099_sec_8k_event_density_core62_pct_1q_v063_signal(ticker, date, eventcodes):
    return _clean(_pct_change(_event_count(eventcodes, 20), 1))
def cg_f099_sec_8k_event_density_core63_pct_1q_v064_signal(ticker, date, eventcodes):
    return _clean(_pct_change(_event_rate(eventcodes, 4), 1))
def cg_f099_sec_8k_event_density_core64_pct_1q_v065_signal(ticker, date, eventcodes):
    return _clean(_pct_change(_event_rate(eventcodes, 12), 1))
def cg_f099_sec_8k_event_density_core65_pct_1q_v066_signal(ticker, date, eventcodes):
    return _clean(_pct_change(_event_rate(eventcodes, 20), 1))
def cg_f099_sec_8k_event_density_core66_pct_1q_v067_signal(ticker, date, eventcodes):
    return _clean(_pct_change(_z(_event_count(eventcodes, 12), 20), 1))
def cg_f099_sec_8k_event_density_core67_pct_1q_v068_signal(ticker, date, eventcodes):
    return _clean(_pct_change(_rank(_event_count(eventcodes, 12), 20), 1))
def cg_f099_sec_8k_event_density_core68_pct_1q_v069_signal(ticker, date, eventcodes):
    return _clean(_pct_change(_diff(_event_count(eventcodes, 4), 1), 1))
def cg_f099_sec_8k_event_density_core69_pct_1q_v070_signal(ticker, date, eventcodes):
    return _clean(_pct_change(_pct_change(_event_count(eventcodes, 12) + 1, 4), 1))
# core70-79: pct_4q
def cg_f099_sec_8k_event_density_core70_pct_4q_v071_signal(ticker, date, eventcodes):
    return _clean(_pct_change(_event_count(eventcodes, 4), 4))
def cg_f099_sec_8k_event_density_core71_pct_4q_v072_signal(ticker, date, eventcodes):
    return _clean(_pct_change(_event_count(eventcodes, 12), 4))
def cg_f099_sec_8k_event_density_core72_pct_4q_v073_signal(ticker, date, eventcodes):
    return _clean(_pct_change(_event_count(eventcodes, 20), 4))
def cg_f099_sec_8k_event_density_core73_pct_4q_v074_signal(ticker, date, eventcodes):
    return _clean(_pct_change(_event_rate(eventcodes, 4), 4))
def cg_f099_sec_8k_event_density_core74_pct_4q_v075_signal(ticker, date, eventcodes):
    return _clean(_pct_change(_event_rate(eventcodes, 12), 4))
