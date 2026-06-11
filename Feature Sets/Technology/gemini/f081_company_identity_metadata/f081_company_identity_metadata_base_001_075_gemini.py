import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f081_company_identity_metadata_core00_event_flag_v001_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_flag(ticker))
def cg_f081_company_identity_metadata_core01_event_flag_v002_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_flag(name))
def cg_f081_company_identity_metadata_core02_event_flag_v003_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_flag(exchange))
def cg_f081_company_identity_metadata_core03_event_flag_v004_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_flag(category))
def cg_f081_company_identity_metadata_core04_event_flag_v005_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_flag(siccode))
def cg_f081_company_identity_metadata_core05_event_flag_v006_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_flag(scalemarketcap))
def cg_f081_company_identity_metadata_core06_event_count_4q_v007_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_count(ticker, 4))
def cg_f081_company_identity_metadata_core07_event_count_4q_v008_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_count(name, 4))
def cg_f081_company_identity_metadata_core08_event_count_4q_v009_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_count(exchange, 4))
def cg_f081_company_identity_metadata_core09_event_count_4q_v010_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_count(category, 4))
def cg_f081_company_identity_metadata_core10_event_count_4q_v011_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_count(siccode, 4))
def cg_f081_company_identity_metadata_core11_event_count_4q_v012_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_count(scalemarketcap, 4))
def cg_f081_company_identity_metadata_core12_event_count_8q_v013_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_count(ticker, 8))
def cg_f081_company_identity_metadata_core13_event_count_8q_v014_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_count(name, 8))
def cg_f081_company_identity_metadata_core14_event_count_8q_v015_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_count(exchange, 8))
def cg_f081_company_identity_metadata_core15_event_count_8q_v016_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_count(category, 8))
def cg_f081_company_identity_metadata_core16_event_count_8q_v017_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_count(siccode, 8))
def cg_f081_company_identity_metadata_core17_event_count_8q_v018_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_count(scalemarketcap, 8))
def cg_f081_company_identity_metadata_core18_event_rate_4q_v019_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_rate(ticker, 4))
def cg_f081_company_identity_metadata_core19_event_rate_4q_v020_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_rate(name, 4))
def cg_f081_company_identity_metadata_core20_event_rate_4q_v021_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_rate(exchange, 4))
def cg_f081_company_identity_metadata_core21_event_rate_4q_v022_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_rate(category, 4))
def cg_f081_company_identity_metadata_core22_event_rate_4q_v023_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_rate(siccode, 4))
def cg_f081_company_identity_metadata_core23_event_rate_4q_v024_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_rate(scalemarketcap, 4))
def cg_f081_company_identity_metadata_core24_event_rate_8q_v025_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_rate(ticker, 8))
def cg_f081_company_identity_metadata_core25_event_rate_8q_v026_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_rate(name, 8))
def cg_f081_company_identity_metadata_core26_event_rate_8q_v027_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_rate(exchange, 8))
def cg_f081_company_identity_metadata_core27_event_rate_8q_v028_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_rate(category, 8))
def cg_f081_company_identity_metadata_core28_event_rate_8q_v029_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_rate(siccode, 8))
def cg_f081_company_identity_metadata_core29_event_rate_8q_v030_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_rate(scalemarketcap, 8))
def cg_f081_company_identity_metadata_core30_autocorr_4q_v031_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_autocorr(ticker, 4))
def cg_f081_company_identity_metadata_core31_autocorr_4q_v032_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_autocorr(name, 4))
def cg_f081_company_identity_metadata_core32_autocorr_4q_v033_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_autocorr(exchange, 4))
def cg_f081_company_identity_metadata_core33_autocorr_4q_v034_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_autocorr(category, 4))
def cg_f081_company_identity_metadata_core34_autocorr_4q_v035_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_autocorr(siccode, 4))
def cg_f081_company_identity_metadata_core35_autocorr_4q_v036_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_autocorr(scalemarketcap, 4))
def cg_f081_company_identity_metadata_core36_autocorr_8q_v037_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_autocorr(ticker, 8))
def cg_f081_company_identity_metadata_core37_autocorr_8q_v038_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_autocorr(name, 8))
def cg_f081_company_identity_metadata_core38_autocorr_8q_v039_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_autocorr(exchange, 8))
def cg_f081_company_identity_metadata_core39_autocorr_8q_v040_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_autocorr(category, 8))
def cg_f081_company_identity_metadata_core40_autocorr_8q_v041_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_autocorr(siccode, 8))
def cg_f081_company_identity_metadata_core41_autocorr_8q_v042_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_autocorr(scalemarketcap, 8))
def cg_f081_company_identity_metadata_core42_rank_event_count_4q_12q_v043_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_event_count(ticker, 4), 12))
def cg_f081_company_identity_metadata_core43_rank_event_count_4q_12q_v044_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_event_count(name, 4), 12))
def cg_f081_company_identity_metadata_core44_rank_event_count_4q_12q_v045_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_event_count(exchange, 4), 12))
def cg_f081_company_identity_metadata_core45_rank_event_count_4q_12q_v046_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_event_count(category, 4), 12))
def cg_f081_company_identity_metadata_core46_rank_event_count_4q_12q_v047_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_event_count(siccode, 4), 12))
def cg_f081_company_identity_metadata_core47_rank_event_count_4q_12q_v048_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_event_count(scalemarketcap, 4), 12))
def cg_f081_company_identity_metadata_core48_rank_event_rate_4q_12q_v049_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_event_rate(ticker, 4), 12))
def cg_f081_company_identity_metadata_core49_rank_event_rate_4q_12q_v050_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_event_rate(name, 4), 12))
def cg_f081_company_identity_metadata_core50_rank_event_rate_4q_12q_v051_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_event_rate(exchange, 4), 12))
def cg_f081_company_identity_metadata_core51_rank_event_rate_4q_12q_v052_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_event_rate(category, 4), 12))
def cg_f081_company_identity_metadata_core52_rank_event_rate_4q_12q_v053_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_event_rate(siccode, 4), 12))
def cg_f081_company_identity_metadata_core53_rank_event_rate_4q_12q_v054_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_event_rate(scalemarketcap, 4), 12))
def cg_f081_company_identity_metadata_core54_event_diff_1q_v055_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_flag(ticker).diff(1))
def cg_f081_company_identity_metadata_core55_event_diff_1q_v056_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_flag(name).diff(1))
def cg_f081_company_identity_metadata_core56_event_diff_1q_v057_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_flag(exchange).diff(1))
def cg_f081_company_identity_metadata_core57_event_diff_1q_v058_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_flag(category).diff(1))
def cg_f081_company_identity_metadata_core58_event_diff_1q_v059_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_flag(siccode).diff(1))
def cg_f081_company_identity_metadata_core59_event_diff_1q_v060_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_flag(scalemarketcap).diff(1))
def cg_f081_company_identity_metadata_core60_event_count_12q_v061_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_count(ticker, 12))
def cg_f081_company_identity_metadata_core61_event_count_12q_v062_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_count(name, 12))
def cg_f081_company_identity_metadata_core62_event_count_12q_v063_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_count(exchange, 12))
def cg_f081_company_identity_metadata_core63_event_count_12q_v064_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_count(category, 12))
def cg_f081_company_identity_metadata_core64_event_count_12q_v065_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_count(siccode, 12))
def cg_f081_company_identity_metadata_core65_event_count_12q_v066_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_count(scalemarketcap, 12))
def cg_f081_company_identity_metadata_core66_event_rate_12q_v067_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_rate(ticker, 12))
def cg_f081_company_identity_metadata_core67_event_rate_12q_v068_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_rate(name, 12))
def cg_f081_company_identity_metadata_core68_event_rate_12q_v069_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_rate(exchange, 12))
def cg_f081_company_identity_metadata_core69_event_rate_12q_v070_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_rate(category, 12))
def cg_f081_company_identity_metadata_core70_event_rate_12q_v071_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_rate(siccode, 12))
def cg_f081_company_identity_metadata_core71_event_rate_12q_v072_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_rate(scalemarketcap, 12))
def cg_f081_company_identity_metadata_core72_autocorr_12q_v073_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_autocorr(ticker, 12))
def cg_f081_company_identity_metadata_core73_autocorr_12q_v074_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_autocorr(name, 12))
def cg_f081_company_identity_metadata_core74_autocorr_12q_v075_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_autocorr(exchange, 12))