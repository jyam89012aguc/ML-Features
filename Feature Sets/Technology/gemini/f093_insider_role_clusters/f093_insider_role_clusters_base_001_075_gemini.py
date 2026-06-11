import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core00-09: role flags and rates
def cg_f093_insider_role_clusters_core00_director_flag_v001_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _event_flag(isdirector)
def cg_f093_insider_role_clusters_core01_officer_flag_v002_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _event_flag(isofficer)
def cg_f093_insider_role_clusters_core02_ten_pct_flag_v003_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _event_flag(istenpercentowner)
def cg_f093_insider_role_clusters_core03_director_rate_252d_v004_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _event_rate(isdirector, 252)
def cg_f093_insider_role_clusters_core04_officer_rate_252d_v005_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _event_rate(isofficer, 252)
def cg_f093_insider_role_clusters_core05_ten_pct_rate_252d_v006_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _event_rate(istenpercentowner, 252)
def cg_f093_insider_role_clusters_core06_owner_count_252d_v007_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _event_count(ownername, 252)
def cg_f093_insider_role_clusters_core07_title_count_252d_v008_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _event_count(officertitle, 252)
def cg_f093_insider_role_clusters_core08_director_officer_v009_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return (_event_flag(isdirector) * _event_flag(isofficer)).astype(float)
def cg_f093_insider_role_clusters_core09_multi_role_v010_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return (_event_flag(isdirector) + _event_flag(isofficer) + _event_flag(istenpercentowner)).astype(float)

# core10-19: mean 63d
def cg_f093_insider_role_clusters_core10_mean_63d_v011_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_event_flag(isdirector), 63))
def cg_f093_insider_role_clusters_core11_mean_63d_v012_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_event_flag(isofficer), 63))
def cg_f093_insider_role_clusters_core12_mean_63d_v013_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_event_flag(istenpercentowner), 63))
def cg_f093_insider_role_clusters_core13_mean_63d_v014_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_event_rate(ownername, 21), 63))
def cg_f093_insider_role_clusters_core14_mean_63d_v015_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_event_rate(officertitle, 21), 63))
def cg_f093_insider_role_clusters_core15_mean_63d_v016_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_event_count(ownername, 63), 63))
def cg_f093_insider_role_clusters_core16_mean_63d_v017_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_event_count(officertitle, 63), 63))
def cg_f093_insider_role_clusters_core17_mean_63d_v018_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_event_flag(ownername), 63))
def cg_f093_insider_role_clusters_core18_mean_63d_v019_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_event_flag(officertitle), 63))
def cg_f093_insider_role_clusters_core19_mean_63d_v020_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_z(_event_count(ownername, 252), 252), 63))

# core20-29: z 126d
def cg_f093_insider_role_clusters_core20_z_126d_v021_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_event_flag(isdirector), 126))
def cg_f093_insider_role_clusters_core21_z_126d_v022_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_event_flag(isofficer), 126))
def cg_f093_insider_role_clusters_core22_z_126d_v023_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_event_flag(istenpercentowner), 126))
def cg_f093_insider_role_clusters_core23_z_126d_v024_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_event_rate(ownername, 21), 126))
def cg_f093_insider_role_clusters_core24_z_126d_v025_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_event_rate(officertitle, 21), 126))
def cg_f093_insider_role_clusters_core25_z_126d_v026_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_event_count(ownername, 63), 126))
def cg_f093_insider_role_clusters_core26_z_126d_v027_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_event_count(officertitle, 63), 126))
def cg_f093_insider_role_clusters_core27_z_126d_v028_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_event_flag(ownername), 126))
def cg_f093_insider_role_clusters_core28_z_126d_v029_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_event_flag(officertitle), 126))
def cg_f093_insider_role_clusters_core29_z_126d_v030_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_z(_event_count(ownername, 252), 252), 126))

# core30-39: rank 252d
def cg_f093_insider_role_clusters_core30_rank_252d_v031_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_event_flag(isdirector), 252))
def cg_f093_insider_role_clusters_core31_rank_252d_v032_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_event_flag(isofficer), 252))
def cg_f093_insider_role_clusters_core32_rank_252d_v033_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_event_flag(istenpercentowner), 252))
def cg_f093_insider_role_clusters_core33_rank_252d_v034_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_event_rate(ownername, 21), 252))
def cg_f093_insider_role_clusters_core34_rank_252d_v035_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_event_rate(officertitle, 21), 252))
def cg_f093_insider_role_clusters_core35_rank_252d_v036_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_event_count(ownername, 63), 252))
def cg_f093_insider_role_clusters_core36_rank_252d_v037_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_event_count(officertitle, 63), 252))
def cg_f093_insider_role_clusters_core37_rank_252d_v038_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_event_flag(ownername), 252))
def cg_f093_insider_role_clusters_core38_rank_252d_v039_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_event_flag(officertitle), 252))
def cg_f093_insider_role_clusters_core39_rank_252d_v040_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_z(_event_count(ownername, 252), 252), 252))

# core40-49: pct 21d
def cg_f093_insider_role_clusters_core40_pct_21d_v041_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_pct_change(_event_rate(ownername, 252), 21))
def cg_f093_insider_role_clusters_core41_pct_21d_v042_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_pct_change(_event_rate(officertitle, 252), 21))
def cg_f093_insider_role_clusters_core42_pct_21d_v043_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_pct_change(_event_count(ownername, 63), 21))
def cg_f093_insider_role_clusters_core43_pct_21d_v044_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_pct_change(_event_count(officertitle, 63), 21))
def cg_f093_insider_role_clusters_core44_pct_21d_v045_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_pct_change(_mean(_event_flag(isdirector), 63), 21))
def cg_f093_insider_role_clusters_core45_pct_21d_v046_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_pct_change(_mean(_event_flag(isofficer), 63), 21))
def cg_f093_insider_role_clusters_core46_pct_21d_v047_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_pct_change(_mean(_event_flag(istenpercentowner), 63), 21))
def cg_f093_insider_role_clusters_core47_pct_21d_v048_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_pct_change(_z(_event_count(ownername, 252), 252), 21))
def cg_f093_insider_role_clusters_core48_pct_21d_v049_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_pct_change(_rank(_event_count(ownername, 252), 252), 21))
def cg_f093_insider_role_clusters_core49_pct_21d_v050_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_pct_change(_event_rate(ownername, 63), 21))

# core50-59: std 63d
def cg_f093_insider_role_clusters_core50_std_63d_v051_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_std(_event_flag(isdirector), 63))
def cg_f093_insider_role_clusters_core51_std_63d_v052_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_std(_event_flag(isofficer), 63))
def cg_f093_insider_role_clusters_core52_std_63d_v053_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_std(_event_flag(istenpercentowner), 63))
def cg_f093_insider_role_clusters_core53_std_63d_v054_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_std(_event_rate(ownername, 21), 63))
def cg_f093_insider_role_clusters_core54_std_63d_v055_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_std(_event_rate(officertitle, 21), 63))
def cg_f093_insider_role_clusters_core55_std_63d_v056_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_std(_event_count(ownername, 63), 63))
def cg_f093_insider_role_clusters_core56_std_63d_v057_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_std(_event_count(officertitle, 63), 63))
def cg_f093_insider_role_clusters_core57_std_63d_v058_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_std(_event_flag(ownername), 63))
def cg_f093_insider_role_clusters_core58_std_63d_v059_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_std(_event_flag(officertitle), 63))
def cg_f093_insider_role_clusters_core59_std_63d_v060_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_std(_z(_event_count(ownername, 252), 252), 63))

# core60-69: slope 63d
def cg_f093_insider_role_clusters_core60_slope_63d_v061_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_event_flag(isdirector), 63))
def cg_f093_insider_role_clusters_core61_slope_63d_v062_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_event_flag(isofficer), 63))
def cg_f093_insider_role_clusters_core62_slope_63d_v063_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_event_flag(istenpercentowner), 63))
def cg_f093_insider_role_clusters_core63_slope_63d_v064_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_event_rate(ownername, 21), 63))
def cg_f093_insider_role_clusters_core64_slope_63d_v065_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_event_rate(officertitle, 21), 63))
def cg_f093_insider_role_clusters_core65_slope_63d_v066_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_event_count(ownername, 63), 63))
def cg_f093_insider_role_clusters_core66_slope_63d_v067_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_event_count(officertitle, 63), 63))
def cg_f093_insider_role_clusters_core67_slope_63d_v068_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_event_flag(ownername), 63))
def cg_f093_insider_role_clusters_core68_slope_63d_v069_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_event_flag(officertitle), 63))
def cg_f093_insider_role_clusters_core69_slope_63d_v070_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_z(_event_count(ownername, 252), 252), 63))

# core70-74: ewm 63d
def cg_f093_insider_role_clusters_core70_ewm_63d_v071_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_ewm(_event_flag(isdirector), 63))
def cg_f093_insider_role_clusters_core71_ewm_63d_v072_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_ewm(_event_flag(isofficer), 63))
def cg_f093_insider_role_clusters_core72_ewm_63d_v073_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_ewm(_event_flag(istenpercentowner), 63))
def cg_f093_insider_role_clusters_core73_ewm_63d_v074_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_ewm(_event_rate(ownername, 21), 63))
def cg_f093_insider_role_clusters_core74_ewm_63d_v075_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_ewm(_event_rate(officertitle, 21), 63))
