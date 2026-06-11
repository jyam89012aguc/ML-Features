import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f080_restatement_revision_proxy_core00_event_flag_v001_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_flag(datekey))
def cg_f080_restatement_revision_proxy_core01_event_flag_v002_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_flag(lastupdated))
def cg_f080_restatement_revision_proxy_core02_event_flag_v003_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_flag(reportperiod))
def cg_f080_restatement_revision_proxy_core03_event_flag_v004_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_flag(dimension))
def cg_f080_restatement_revision_proxy_core04_event_count_4q_v005_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_count(datekey, 4))
def cg_f080_restatement_revision_proxy_core05_event_count_4q_v006_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_count(lastupdated, 4))
def cg_f080_restatement_revision_proxy_core06_event_count_4q_v007_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_count(reportperiod, 4))
def cg_f080_restatement_revision_proxy_core07_event_count_4q_v008_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_count(dimension, 4))
def cg_f080_restatement_revision_proxy_core08_event_count_8q_v009_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_count(datekey, 8))
def cg_f080_restatement_revision_proxy_core09_event_count_8q_v010_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_count(lastupdated, 8))
def cg_f080_restatement_revision_proxy_core10_event_count_8q_v011_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_count(reportperiod, 8))
def cg_f080_restatement_revision_proxy_core11_event_count_8q_v012_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_count(dimension, 8))
def cg_f080_restatement_revision_proxy_core12_event_rate_4q_v013_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_rate(datekey, 4))
def cg_f080_restatement_revision_proxy_core13_event_rate_4q_v014_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_rate(lastupdated, 4))
def cg_f080_restatement_revision_proxy_core14_event_rate_4q_v015_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_rate(reportperiod, 4))
def cg_f080_restatement_revision_proxy_core15_event_rate_4q_v016_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_rate(dimension, 4))
def cg_f080_restatement_revision_proxy_core16_event_rate_8q_v017_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_rate(datekey, 8))
def cg_f080_restatement_revision_proxy_core17_event_rate_8q_v018_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_rate(lastupdated, 8))
def cg_f080_restatement_revision_proxy_core18_event_rate_8q_v019_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_rate(reportperiod, 8))
def cg_f080_restatement_revision_proxy_core19_event_rate_8q_v020_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_rate(dimension, 8))
def cg_f080_restatement_revision_proxy_core20_autocorr_4q_v021_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_autocorr(datekey, 4))
def cg_f080_restatement_revision_proxy_core21_autocorr_4q_v022_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_autocorr(lastupdated, 4))
def cg_f080_restatement_revision_proxy_core22_autocorr_4q_v023_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_autocorr(reportperiod, 4))
def cg_f080_restatement_revision_proxy_core23_autocorr_4q_v024_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_autocorr(dimension, 4))
def cg_f080_restatement_revision_proxy_core24_autocorr_8q_v025_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_autocorr(datekey, 8))
def cg_f080_restatement_revision_proxy_core25_autocorr_8q_v026_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_autocorr(lastupdated, 8))
def cg_f080_restatement_revision_proxy_core26_autocorr_8q_v027_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_autocorr(reportperiod, 8))
def cg_f080_restatement_revision_proxy_core27_autocorr_8q_v028_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_autocorr(dimension, 8))
def cg_f080_restatement_revision_proxy_core28_rank_event_count_4q_12q_v029_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_event_count(datekey, 4), 12))
def cg_f080_restatement_revision_proxy_core29_rank_event_count_4q_12q_v030_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_event_count(lastupdated, 4), 12))
def cg_f080_restatement_revision_proxy_core30_rank_event_count_4q_12q_v031_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_event_count(reportperiod, 4), 12))
def cg_f080_restatement_revision_proxy_core31_rank_event_count_4q_12q_v032_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_event_count(dimension, 4), 12))
def cg_f080_restatement_revision_proxy_core32_rank_event_rate_4q_12q_v033_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_event_rate(datekey, 4), 12))
def cg_f080_restatement_revision_proxy_core33_rank_event_rate_4q_12q_v034_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_event_rate(lastupdated, 4), 12))
def cg_f080_restatement_revision_proxy_core34_rank_event_rate_4q_12q_v035_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_event_rate(reportperiod, 4), 12))
def cg_f080_restatement_revision_proxy_core35_rank_event_rate_4q_12q_v036_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_event_rate(dimension, 4), 12))
def cg_f080_restatement_revision_proxy_core36_diff_1q_v037_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_to_num(datekey), 1))
def cg_f080_restatement_revision_proxy_core37_diff_1q_v038_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_to_num(lastupdated), 1))
def cg_f080_restatement_revision_proxy_core38_diff_1q_v039_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_to_num(reportperiod), 1))
def cg_f080_restatement_revision_proxy_core39_event_diff_1q_v040_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_flag(dimension).diff(1))
def cg_f080_restatement_revision_proxy_core40_event_count_12q_v041_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_count(datekey, 12))
def cg_f080_restatement_revision_proxy_core41_event_count_12q_v042_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_count(lastupdated, 12))
def cg_f080_restatement_revision_proxy_core42_event_count_12q_v043_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_count(reportperiod, 12))
def cg_f080_restatement_revision_proxy_core43_event_count_12q_v044_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_count(dimension, 12))
def cg_f080_restatement_revision_proxy_core44_event_rate_12q_v045_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_rate(datekey, 12))
def cg_f080_restatement_revision_proxy_core45_event_rate_12q_v046_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_rate(lastupdated, 12))
def cg_f080_restatement_revision_proxy_core46_event_rate_12q_v047_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_rate(reportperiod, 12))
def cg_f080_restatement_revision_proxy_core47_event_rate_12q_v048_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_rate(dimension, 12))
def cg_f080_restatement_revision_proxy_core48_autocorr_12q_v049_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_autocorr(datekey, 12))
def cg_f080_restatement_revision_proxy_core49_autocorr_12q_v050_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_autocorr(lastupdated, 12))
def cg_f080_restatement_revision_proxy_core50_autocorr_12q_v051_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_autocorr(reportperiod, 12))
def cg_f080_restatement_revision_proxy_core51_autocorr_12q_v052_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_autocorr(dimension, 12))
def cg_f080_restatement_revision_proxy_core52_rank_event_count_8q_20q_v053_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_event_count(datekey, 8), 20))
def cg_f080_restatement_revision_proxy_core53_rank_event_count_8q_20q_v054_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_event_count(lastupdated, 8), 20))
def cg_f080_restatement_revision_proxy_core54_rank_event_count_8q_20q_v055_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_event_count(reportperiod, 8), 20))
def cg_f080_restatement_revision_proxy_core55_rank_event_count_8q_20q_v056_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_event_count(dimension, 8), 20))
def cg_f080_restatement_revision_proxy_core56_event_flag_alt_v057_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_flag(datekey))
def cg_f080_restatement_revision_proxy_core57_event_flag_alt_v058_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_flag(lastupdated))
def cg_f080_restatement_revision_proxy_core58_event_flag_alt_v059_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_flag(reportperiod))
def cg_f080_restatement_revision_proxy_core59_event_flag_alt_v060_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_flag(dimension))
def cg_f080_restatement_revision_proxy_core60_event_flag_v061_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_flag(datekey))
def cg_f080_restatement_revision_proxy_core61_event_flag_v062_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_flag(lastupdated))
def cg_f080_restatement_revision_proxy_core62_event_flag_v063_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_flag(reportperiod))
def cg_f080_restatement_revision_proxy_core63_event_flag_v064_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_flag(dimension))
def cg_f080_restatement_revision_proxy_core64_event_count_4q_v065_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_count(datekey, 4))
def cg_f080_restatement_revision_proxy_core65_event_count_4q_v066_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_count(lastupdated, 4))
def cg_f080_restatement_revision_proxy_core66_event_count_4q_v067_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_count(reportperiod, 4))
def cg_f080_restatement_revision_proxy_core67_event_count_4q_v068_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_count(dimension, 4))
def cg_f080_restatement_revision_proxy_core68_event_count_8q_v069_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_count(datekey, 8))
def cg_f080_restatement_revision_proxy_core69_event_count_8q_v070_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_count(lastupdated, 8))
def cg_f080_restatement_revision_proxy_core70_event_count_8q_v071_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_count(reportperiod, 8))
def cg_f080_restatement_revision_proxy_core71_event_count_8q_v072_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_count(dimension, 8))
def cg_f080_restatement_revision_proxy_core72_event_rate_4q_v073_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_rate(datekey, 4))
def cg_f080_restatement_revision_proxy_core73_event_rate_4q_v074_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_rate(lastupdated, 4))
def cg_f080_restatement_revision_proxy_core74_event_rate_4q_v075_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_rate(reportperiod, 4))