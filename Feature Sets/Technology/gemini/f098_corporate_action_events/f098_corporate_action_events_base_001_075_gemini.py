import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core0-9: mean_4q
def cg_f098_corporate_action_events_core00_mean_4q_v001_signal(date, action, value, name, contraticker, contraname):
    return _clean(_mean(value, 4))
def cg_f098_corporate_action_events_core01_mean_4q_v002_signal(date, action, value, name, contraticker, contraname):
    return _clean(_mean(_log(value.clip(lower=1.0) if hasattr(value, 'clip') else value), 4))
def cg_f098_corporate_action_events_core02_mean_4q_v003_signal(date, action, value, name, contraticker, contraname):
    return _clean(_mean(_safe_div(value, _mean(value, 20)), 4))
def cg_f098_corporate_action_events_core03_mean_4q_v004_signal(date, action, value, name, contraticker, contraname):
    return _clean(_mean(_z(value, 20), 4))
def cg_f098_corporate_action_events_core04_mean_4q_v005_signal(date, action, value, name, contraticker, contraname):
    return _clean(_mean(_rank(value, 20), 4))
def cg_f098_corporate_action_events_core05_mean_4q_v006_signal(date, action, value, name, contraticker, contraname):
    return _clean(_mean(_pct_change(value, 1), 4))
def cg_f098_corporate_action_events_core06_mean_4q_v007_signal(date, action, value, name, contraticker, contraname):
    return _clean(_mean(_pct_change(value, 4), 4))
def cg_f098_corporate_action_events_core07_mean_4q_v008_signal(date, action, value, name, contraticker, contraname):
    return _clean(_mean(_diff(value, 1), 4))
def cg_f098_corporate_action_events_core08_mean_4q_v009_signal(date, action, value, name, contraticker, contraname):
    return _clean(_mean(_ewm(value, 8), 4))
def cg_f098_corporate_action_events_core09_mean_4q_v010_signal(date, action, value, name, contraticker, contraname):
    return _clean(_mean(_event_count(value, 12), 4))
# core10-19: mean_8q
def cg_f098_corporate_action_events_core10_mean_8q_v011_signal(date, action, value, name, contraticker, contraname):
    return _clean(_mean(value, 8))
def cg_f098_corporate_action_events_core11_mean_8q_v012_signal(date, action, value, name, contraticker, contraname):
    return _clean(_mean(_log(value.clip(lower=1.0) if hasattr(value, 'clip') else value), 8))
def cg_f098_corporate_action_events_core12_mean_8q_v013_signal(date, action, value, name, contraticker, contraname):
    return _clean(_mean(_safe_div(value, _mean(value, 20)), 8))
def cg_f098_corporate_action_events_core13_mean_8q_v014_signal(date, action, value, name, contraticker, contraname):
    return _clean(_mean(_z(value, 20), 8))
def cg_f098_corporate_action_events_core14_mean_8q_v015_signal(date, action, value, name, contraticker, contraname):
    return _clean(_mean(_rank(value, 20), 8))
def cg_f098_corporate_action_events_core15_mean_8q_v016_signal(date, action, value, name, contraticker, contraname):
    return _clean(_mean(_pct_change(value, 1), 8))
def cg_f098_corporate_action_events_core16_mean_8q_v017_signal(date, action, value, name, contraticker, contraname):
    return _clean(_mean(_pct_change(value, 4), 8))
def cg_f098_corporate_action_events_core17_mean_8q_v018_signal(date, action, value, name, contraticker, contraname):
    return _clean(_mean(_diff(value, 1), 8))
def cg_f098_corporate_action_events_core18_mean_8q_v019_signal(date, action, value, name, contraticker, contraname):
    return _clean(_mean(_ewm(value, 8), 8))
def cg_f098_corporate_action_events_core19_mean_8q_v020_signal(date, action, value, name, contraticker, contraname):
    return _clean(_mean(_event_count(value, 12), 8))
# core20-29: z_8q
def cg_f098_corporate_action_events_core20_z_8q_v021_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(value, 8))
def cg_f098_corporate_action_events_core21_z_8q_v022_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_log(value.clip(lower=1.0) if hasattr(value, 'clip') else value), 8))
def cg_f098_corporate_action_events_core22_z_8q_v023_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_safe_div(value, _mean(value, 20)), 8))
def cg_f098_corporate_action_events_core23_z_8q_v024_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_z(value, 20), 8))
def cg_f098_corporate_action_events_core24_z_8q_v025_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_rank(value, 20), 8))
def cg_f098_corporate_action_events_core25_z_8q_v026_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_pct_change(value, 1), 8))
def cg_f098_corporate_action_events_core26_z_8q_v027_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_pct_change(value, 4), 8))
def cg_f098_corporate_action_events_core27_z_8q_v028_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_diff(value, 1), 8))
def cg_f098_corporate_action_events_core28_z_8q_v029_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_ewm(value, 8), 8))
def cg_f098_corporate_action_events_core29_z_8q_v030_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_event_count(value, 12), 8))
# core30-39: z_20q
def cg_f098_corporate_action_events_core30_z_20q_v031_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(value, 20))
def cg_f098_corporate_action_events_core31_z_20q_v032_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_log(value.clip(lower=1.0) if hasattr(value, 'clip') else value), 20))
def cg_f098_corporate_action_events_core32_z_20q_v033_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_safe_div(value, _mean(value, 20)), 20))
def cg_f098_corporate_action_events_core33_z_20q_v034_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_z(value, 20), 20))
def cg_f098_corporate_action_events_core34_z_20q_v035_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_rank(value, 20), 20))
def cg_f098_corporate_action_events_core35_z_20q_v036_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_pct_change(value, 1), 20))
def cg_f098_corporate_action_events_core36_z_20q_v037_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_pct_change(value, 4), 20))
def cg_f098_corporate_action_events_core37_z_20q_v038_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_diff(value, 1), 20))
def cg_f098_corporate_action_events_core38_z_20q_v039_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_ewm(value, 8), 20))
def cg_f098_corporate_action_events_core39_z_20q_v040_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_event_count(value, 12), 20))
# core40-49: rank_12q
def cg_f098_corporate_action_events_core40_rank_12q_v041_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(value, 12))
def cg_f098_corporate_action_events_core41_rank_12q_v042_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_log(value.clip(lower=1.0) if hasattr(value, 'clip') else value), 12))
def cg_f098_corporate_action_events_core42_rank_12q_v043_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_safe_div(value, _mean(value, 20)), 12))
def cg_f098_corporate_action_events_core43_rank_12q_v044_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_z(value, 20), 12))
def cg_f098_corporate_action_events_core44_rank_12q_v045_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_rank(value, 20), 12))
def cg_f098_corporate_action_events_core45_rank_12q_v046_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_pct_change(value, 1), 12))
def cg_f098_corporate_action_events_core46_rank_12q_v047_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_pct_change(value, 4), 12))
def cg_f098_corporate_action_events_core47_rank_12q_v048_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_diff(value, 1), 12))
def cg_f098_corporate_action_events_core48_rank_12q_v049_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_ewm(value, 8), 12))
def cg_f098_corporate_action_events_core49_rank_12q_v050_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_event_count(value, 12), 12))
# core50-59: rank_20q
def cg_f098_corporate_action_events_core50_rank_20q_v051_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(value, 20))
def cg_f098_corporate_action_events_core51_rank_20q_v052_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_log(value.clip(lower=1.0) if hasattr(value, 'clip') else value), 20))
def cg_f098_corporate_action_events_core52_rank_20q_v053_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_safe_div(value, _mean(value, 20)), 20))
def cg_f098_corporate_action_events_core53_rank_20q_v054_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_z(value, 20), 20))
def cg_f098_corporate_action_events_core54_rank_20q_v055_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_rank(value, 20), 20))
def cg_f098_corporate_action_events_core55_rank_20q_v056_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_pct_change(value, 1), 20))
def cg_f098_corporate_action_events_core56_rank_20q_v057_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_pct_change(value, 4), 20))
def cg_f098_corporate_action_events_core57_rank_20q_v058_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_diff(value, 1), 20))
def cg_f098_corporate_action_events_core58_rank_20q_v059_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_ewm(value, 8), 20))
def cg_f098_corporate_action_events_core59_rank_20q_v060_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_event_count(value, 12), 20))
# core60-69: pct_1q
def cg_f098_corporate_action_events_core60_pct_1q_v061_signal(date, action, value, name, contraticker, contraname):
    return _clean(_pct_change(value, 1))
def cg_f098_corporate_action_events_core61_pct_1q_v062_signal(date, action, value, name, contraticker, contraname):
    return _clean(_pct_change(_log(value.clip(lower=1.0) if hasattr(value, 'clip') else value), 1))
def cg_f098_corporate_action_events_core62_pct_1q_v063_signal(date, action, value, name, contraticker, contraname):
    return _clean(_pct_change(_safe_div(value, _mean(value, 20)), 1))
def cg_f098_corporate_action_events_core63_pct_1q_v064_signal(date, action, value, name, contraticker, contraname):
    return _clean(_pct_change(_z(value, 20), 1))
def cg_f098_corporate_action_events_core64_pct_1q_v065_signal(date, action, value, name, contraticker, contraname):
    return _clean(_pct_change(_rank(value, 20), 1))
def cg_f098_corporate_action_events_core65_pct_1q_v066_signal(date, action, value, name, contraticker, contraname):
    return _clean(_pct_change(_pct_change(value, 1), 1))
def cg_f098_corporate_action_events_core66_pct_1q_v067_signal(date, action, value, name, contraticker, contraname):
    return _clean(_pct_change(_pct_change(value, 4), 1))
def cg_f098_corporate_action_events_core67_pct_1q_v068_signal(date, action, value, name, contraticker, contraname):
    return _clean(_pct_change(_diff(value, 1), 1))
def cg_f098_corporate_action_events_core68_pct_1q_v069_signal(date, action, value, name, contraticker, contraname):
    return _clean(_pct_change(_ewm(value, 8), 1))
def cg_f098_corporate_action_events_core69_pct_1q_v070_signal(date, action, value, name, contraticker, contraname):
    return _clean(_pct_change(_event_count(value, 12), 1))
# core70-79: pct_4q
def cg_f098_corporate_action_events_core70_pct_4q_v071_signal(date, action, value, name, contraticker, contraname):
    return _clean(_pct_change(value, 4))
def cg_f098_corporate_action_events_core71_pct_4q_v072_signal(date, action, value, name, contraticker, contraname):
    return _clean(_pct_change(_log(value.clip(lower=1.0) if hasattr(value, 'clip') else value), 4))
def cg_f098_corporate_action_events_core72_pct_4q_v073_signal(date, action, value, name, contraticker, contraname):
    return _clean(_pct_change(_safe_div(value, _mean(value, 20)), 4))
def cg_f098_corporate_action_events_core73_pct_4q_v074_signal(date, action, value, name, contraticker, contraname):
    return _clean(_pct_change(_z(value, 20), 4))
def cg_f098_corporate_action_events_core74_pct_4q_v075_signal(date, action, value, name, contraticker, contraname):
    return _clean(_pct_change(_rank(value, 20), 4))
