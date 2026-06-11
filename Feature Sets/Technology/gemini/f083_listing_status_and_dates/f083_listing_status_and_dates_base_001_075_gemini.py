import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f083_listing_status_and_dates_core00_event_flag_v001_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_flag(isdelisted))
def cg_f083_listing_status_and_dates_core01_event_flag_v002_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_flag(firstpricedate))
def cg_f083_listing_status_and_dates_core02_event_flag_v003_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_flag(lastpricedate))
def cg_f083_listing_status_and_dates_core03_event_flag_v004_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_flag(firstquarter))
def cg_f083_listing_status_and_dates_core04_event_flag_v005_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_flag(lastquarter))
def cg_f083_listing_status_and_dates_core05_event_count_4q_v006_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_count(isdelisted, 4))
def cg_f083_listing_status_and_dates_core06_event_count_4q_v007_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_count(firstpricedate, 4))
def cg_f083_listing_status_and_dates_core07_event_count_4q_v008_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_count(lastpricedate, 4))
def cg_f083_listing_status_and_dates_core08_event_count_4q_v009_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_count(firstquarter, 4))
def cg_f083_listing_status_and_dates_core09_event_count_4q_v010_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_count(lastquarter, 4))
def cg_f083_listing_status_and_dates_core10_event_count_8q_v011_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_count(isdelisted, 8))
def cg_f083_listing_status_and_dates_core11_event_count_8q_v012_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_count(firstpricedate, 8))
def cg_f083_listing_status_and_dates_core12_event_count_8q_v013_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_count(lastpricedate, 8))
def cg_f083_listing_status_and_dates_core13_event_count_8q_v014_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_count(firstquarter, 8))
def cg_f083_listing_status_and_dates_core14_event_count_8q_v015_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_count(lastquarter, 8))
def cg_f083_listing_status_and_dates_core15_event_rate_4q_v016_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_rate(isdelisted, 4))
def cg_f083_listing_status_and_dates_core16_event_rate_4q_v017_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_rate(firstpricedate, 4))
def cg_f083_listing_status_and_dates_core17_event_rate_4q_v018_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_rate(lastpricedate, 4))
def cg_f083_listing_status_and_dates_core18_event_rate_4q_v019_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_rate(firstquarter, 4))
def cg_f083_listing_status_and_dates_core19_event_rate_4q_v020_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_rate(lastquarter, 4))
def cg_f083_listing_status_and_dates_core20_event_rate_8q_v021_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_rate(isdelisted, 8))
def cg_f083_listing_status_and_dates_core21_event_rate_8q_v022_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_rate(firstpricedate, 8))
def cg_f083_listing_status_and_dates_core22_event_rate_8q_v023_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_rate(lastpricedate, 8))
def cg_f083_listing_status_and_dates_core23_event_rate_8q_v024_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_rate(firstquarter, 8))
def cg_f083_listing_status_and_dates_core24_event_rate_8q_v025_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_rate(lastquarter, 8))
def cg_f083_listing_status_and_dates_core25_autocorr_4q_v026_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_autocorr(isdelisted, 4))
def cg_f083_listing_status_and_dates_core26_autocorr_4q_v027_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_autocorr(firstpricedate, 4))
def cg_f083_listing_status_and_dates_core27_autocorr_4q_v028_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_autocorr(lastpricedate, 4))
def cg_f083_listing_status_and_dates_core28_autocorr_4q_v029_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_autocorr(firstquarter, 4))
def cg_f083_listing_status_and_dates_core29_autocorr_4q_v030_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_autocorr(lastquarter, 4))
def cg_f083_listing_status_and_dates_core30_autocorr_8q_v031_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_autocorr(isdelisted, 8))
def cg_f083_listing_status_and_dates_core31_autocorr_8q_v032_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_autocorr(firstpricedate, 8))
def cg_f083_listing_status_and_dates_core32_autocorr_8q_v033_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_autocorr(lastpricedate, 8))
def cg_f083_listing_status_and_dates_core33_autocorr_8q_v034_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_autocorr(firstquarter, 8))
def cg_f083_listing_status_and_dates_core34_autocorr_8q_v035_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_autocorr(lastquarter, 8))
def cg_f083_listing_status_and_dates_core35_rank_event_count_4q_12q_v036_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_event_count(isdelisted, 4), 12))
def cg_f083_listing_status_and_dates_core36_rank_event_count_4q_12q_v037_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_event_count(firstpricedate, 4), 12))
def cg_f083_listing_status_and_dates_core37_rank_event_count_4q_12q_v038_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_event_count(lastpricedate, 4), 12))
def cg_f083_listing_status_and_dates_core38_rank_event_count_4q_12q_v039_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_event_count(firstquarter, 4), 12))
def cg_f083_listing_status_and_dates_core39_rank_event_count_4q_12q_v040_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_event_count(lastquarter, 4), 12))
def cg_f083_listing_status_and_dates_core40_rank_event_rate_4q_12q_v041_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_event_rate(isdelisted, 4), 12))
def cg_f083_listing_status_and_dates_core41_rank_event_rate_4q_12q_v042_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_event_rate(firstpricedate, 4), 12))
def cg_f083_listing_status_and_dates_core42_rank_event_rate_4q_12q_v043_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_event_rate(lastpricedate, 4), 12))
def cg_f083_listing_status_and_dates_core43_rank_event_rate_4q_12q_v044_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_event_rate(firstquarter, 4), 12))
def cg_f083_listing_status_and_dates_core44_rank_event_rate_4q_12q_v045_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_event_rate(lastquarter, 4), 12))
def cg_f083_listing_status_and_dates_core45_event_diff_1q_v046_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_flag(isdelisted).diff(1))
def cg_f083_listing_status_and_dates_core46_diff_1q_v047_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_to_num(firstpricedate), 1))
def cg_f083_listing_status_and_dates_core47_diff_1q_v048_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_to_num(lastpricedate), 1))
def cg_f083_listing_status_and_dates_core48_event_diff_1q_v049_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_flag(firstquarter).diff(1))
def cg_f083_listing_status_and_dates_core49_event_diff_1q_v050_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_flag(lastquarter).diff(1))
def cg_f083_listing_status_and_dates_core50_event_count_12q_v051_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_count(isdelisted, 12))
def cg_f083_listing_status_and_dates_core51_event_count_12q_v052_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_count(firstpricedate, 12))
def cg_f083_listing_status_and_dates_core52_event_count_12q_v053_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_count(lastpricedate, 12))
def cg_f083_listing_status_and_dates_core53_event_count_12q_v054_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_count(firstquarter, 12))
def cg_f083_listing_status_and_dates_core54_event_count_12q_v055_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_count(lastquarter, 12))
def cg_f083_listing_status_and_dates_core55_event_rate_12q_v056_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_rate(isdelisted, 12))
def cg_f083_listing_status_and_dates_core56_event_rate_12q_v057_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_rate(firstpricedate, 12))
def cg_f083_listing_status_and_dates_core57_event_rate_12q_v058_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_rate(lastpricedate, 12))
def cg_f083_listing_status_and_dates_core58_event_rate_12q_v059_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_rate(firstquarter, 12))
def cg_f083_listing_status_and_dates_core59_event_rate_12q_v060_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_rate(lastquarter, 12))
def cg_f083_listing_status_and_dates_core60_autocorr_12q_v061_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_autocorr(isdelisted, 12))
def cg_f083_listing_status_and_dates_core61_autocorr_12q_v062_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_autocorr(firstpricedate, 12))
def cg_f083_listing_status_and_dates_core62_autocorr_12q_v063_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_autocorr(lastpricedate, 12))
def cg_f083_listing_status_and_dates_core63_autocorr_12q_v064_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_autocorr(firstquarter, 12))
def cg_f083_listing_status_and_dates_core64_autocorr_12q_v065_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_autocorr(lastquarter, 12))
def cg_f083_listing_status_and_dates_core65_rank_event_count_8q_20q_v066_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_event_count(isdelisted, 8), 20))
def cg_f083_listing_status_and_dates_core66_rank_event_count_8q_20q_v067_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_event_count(firstpricedate, 8), 20))
def cg_f083_listing_status_and_dates_core67_rank_event_count_8q_20q_v068_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_event_count(lastpricedate, 8), 20))
def cg_f083_listing_status_and_dates_core68_rank_event_count_8q_20q_v069_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_event_count(firstquarter, 8), 20))
def cg_f083_listing_status_and_dates_core69_rank_event_count_8q_20q_v070_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_event_count(lastquarter, 8), 20))
def cg_f083_listing_status_and_dates_core70_event_flag_alt_v071_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_flag(isdelisted))
def cg_f083_listing_status_and_dates_core71_event_flag_alt_v072_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_flag(firstpricedate))
def cg_f083_listing_status_and_dates_core72_event_flag_alt_v073_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_flag(lastpricedate))
def cg_f083_listing_status_and_dates_core73_event_flag_alt_v074_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_flag(firstquarter))
def cg_f083_listing_status_and_dates_core74_event_flag_alt_v075_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_flag(lastquarter))