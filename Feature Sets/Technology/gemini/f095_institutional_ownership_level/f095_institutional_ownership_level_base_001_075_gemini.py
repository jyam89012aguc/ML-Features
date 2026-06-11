import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core00-09: event rates and flags
def cg_f095_institutional_ownership_level_core00_investor_flag_v001_signal(calendardate, investorname, securitytype, value, units, price):
    return _event_flag(investorname)
def cg_f095_institutional_ownership_level_core01_investor_count_252d_v002_signal(calendardate, investorname, securitytype, value, units, price):
    return _event_count(investorname, 252)
def cg_f095_institutional_ownership_level_core02_investor_rate_252d_v003_signal(calendardate, investorname, securitytype, value, units, price):
    return _event_rate(investorname, 252)
def cg_f095_institutional_ownership_level_core03_security_flag_v004_signal(calendardate, investorname, securitytype, value, units, price):
    return _event_flag(securitytype)
def cg_f095_institutional_ownership_level_core04_value_z_252d_v005_signal(calendardate, investorname, securitytype, value, units, price):
    return _z(_to_num(value), 252)
def cg_f095_institutional_ownership_level_core05_units_z_252d_v006_signal(calendardate, investorname, securitytype, value, units, price):
    return _z(_to_num(units), 252)
def cg_f095_institutional_ownership_level_core06_value_rank_252d_v007_signal(calendardate, investorname, securitytype, value, units, price):
    return _rank(_to_num(value), 252)
def cg_f095_institutional_ownership_level_core07_units_rank_252d_v008_signal(calendardate, investorname, securitytype, value, units, price):
    return _rank(_to_num(units), 252)
def cg_f095_institutional_ownership_level_core08_avg_price_v009_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_safe_div(_to_num(value), _to_num(units)))
def cg_f095_institutional_ownership_level_core09_price_z_252d_v010_signal(calendardate, investorname, securitytype, value, units, price):
    return _z(_to_num(price), 252)

# core10-19: mean 63d
def cg_f095_institutional_ownership_level_core10_mean_63d_v011_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_mean(_to_num(value), 63))
def cg_f095_institutional_ownership_level_core11_mean_63d_v012_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_mean(_to_num(units), 63))
def cg_f095_institutional_ownership_level_core12_mean_63d_v013_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_mean(_to_num(price), 63))
def cg_f095_institutional_ownership_level_core13_mean_63d_v014_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_mean(_event_flag(investorname), 63))
def cg_f095_institutional_ownership_level_core14_mean_63d_v015_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_mean(_pct_change(_to_num(value), 1), 63))
def cg_f095_institutional_ownership_level_core15_mean_63d_v016_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_mean(_z(_to_num(value), 252), 63))
def cg_f095_institutional_ownership_level_core16_mean_63d_v017_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_mean(_rank(_to_num(value), 252), 63))
def cg_f095_institutional_ownership_level_core17_mean_63d_v018_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_mean(_safe_div(_to_num(value), _to_num(units)), 63))
def cg_f095_institutional_ownership_level_core18_mean_63d_v019_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_mean(_event_count(investorname, 21), 63))
def cg_f095_institutional_ownership_level_core19_mean_63d_v020_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_mean(_event_rate(investorname, 21), 63))

# core20-29: z 126d
def cg_f095_institutional_ownership_level_core20_z_126d_v021_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_to_num(value), 126))
def cg_f095_institutional_ownership_level_core21_z_126d_v022_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_to_num(units), 126))
def cg_f095_institutional_ownership_level_core22_z_126d_v023_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_to_num(price), 126))
def cg_f095_institutional_ownership_level_core23_z_126d_v024_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_event_flag(investorname), 126))
def cg_f095_institutional_ownership_level_core24_z_126d_v025_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_pct_change(_to_num(value), 1), 126))
def cg_f095_institutional_ownership_level_core25_z_126d_v026_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_z(_to_num(value), 252), 126))
def cg_f095_institutional_ownership_level_core26_z_126d_v027_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_rank(_to_num(value), 252), 126))
def cg_f095_institutional_ownership_level_core27_z_126d_v028_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_safe_div(_to_num(value), _to_num(units)), 126))
def cg_f095_institutional_ownership_level_core28_z_126d_v029_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_event_count(investorname, 21), 126))
def cg_f095_institutional_ownership_level_core29_z_126d_v030_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_event_rate(investorname, 21), 126))

# core30-39: rank 252d
def cg_f095_institutional_ownership_level_core30_rank_252d_v031_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_rank(_to_num(value), 252))
def cg_f095_institutional_ownership_level_core31_rank_252d_v032_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_rank(_to_num(units), 252))
def cg_f095_institutional_ownership_level_core32_rank_252d_v033_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_rank(_to_num(price), 252))
def cg_f095_institutional_ownership_level_core33_rank_252d_v034_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_rank(_event_flag(investorname), 252))
def cg_f095_institutional_ownership_level_core34_rank_252d_v035_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_rank(_pct_change(_to_num(value), 1), 252))
def cg_f095_institutional_ownership_level_core35_rank_252d_v036_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_rank(_z(_to_num(value), 252), 252))
def cg_f095_institutional_ownership_level_core36_rank_252d_v037_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_rank(_rank(_to_num(value), 252), 252))
def cg_f095_institutional_ownership_level_core37_rank_252d_v038_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_rank(_safe_div(_to_num(value), _to_num(units)), 252))
def cg_f095_institutional_ownership_level_core38_rank_252d_v039_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_rank(_event_count(investorname, 21), 252))
def cg_f095_institutional_ownership_level_core39_rank_252d_v040_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_rank(_event_rate(investorname, 21), 252))

# core40-49: pct 21d
def cg_f095_institutional_ownership_level_core40_pct_21d_v041_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_pct_change(_to_num(value), 21))
def cg_f095_institutional_ownership_level_core41_pct_21d_v042_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_pct_change(_to_num(units), 21))
def cg_f095_institutional_ownership_level_core42_pct_21d_v043_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_pct_change(_to_num(price), 21))
def cg_f095_institutional_ownership_level_core43_pct_21d_v044_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_pct_change(_event_count(investorname, 21), 21))
def cg_f095_institutional_ownership_level_core44_pct_21d_v045_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_pct_change(_pct_change(_to_num(value), 1), 21))
def cg_f095_institutional_ownership_level_core45_pct_21d_v046_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_pct_change(_z(_to_num(value), 252), 21))
def cg_f095_institutional_ownership_level_core46_pct_21d_v047_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_pct_change(_rank(_to_num(value), 252), 21))
def cg_f095_institutional_ownership_level_core47_pct_21d_v048_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_pct_change(_safe_div(_to_num(value), _to_num(units)), 21))
def cg_f095_institutional_ownership_level_core48_pct_21d_v049_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_pct_change(_event_rate(investorname, 21), 21))
def cg_f095_institutional_ownership_level_core49_pct_21d_v050_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_pct_change(_to_num(value), 63))

# core50-59: std 63d
def cg_f095_institutional_ownership_level_core50_std_63d_v051_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_std(_to_num(value), 63))
def cg_f095_institutional_ownership_level_core51_std_63d_v052_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_std(_to_num(units), 63))
def cg_f095_institutional_ownership_level_core52_std_63d_v053_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_std(_to_num(price), 63))
def cg_f095_institutional_ownership_level_core53_std_63d_v054_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_std(_event_flag(investorname), 63))
def cg_f095_institutional_ownership_level_core54_std_63d_v055_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_std(_pct_change(_to_num(value), 1), 63))
def cg_f095_institutional_ownership_level_core55_std_63d_v056_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_std(_z(_to_num(value), 252), 63))
def cg_f095_institutional_ownership_level_core56_std_63d_v057_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_std(_rank(_to_num(value), 252), 63))
def cg_f095_institutional_ownership_level_core57_std_63d_v058_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_std(_safe_div(_to_num(value), _to_num(units)), 63))
def cg_f095_institutional_ownership_level_core58_std_63d_v059_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_std(_event_count(investorname, 21), 63))
def cg_f095_institutional_ownership_level_core59_std_63d_v060_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_std(_event_rate(investorname, 21), 63))

# core60-69: slope 63d
def cg_f095_institutional_ownership_level_core60_slope_63d_v061_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(_to_num(value), 63))
def cg_f095_institutional_ownership_level_core61_slope_63d_v062_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(_to_num(units), 63))
def cg_f095_institutional_ownership_level_core62_slope_63d_v063_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(_to_num(price), 63))
def cg_f095_institutional_ownership_level_core63_slope_63d_v064_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(_event_flag(investorname), 63))
def cg_f095_institutional_ownership_level_core64_slope_63d_v065_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(_pct_change(_to_num(value), 1), 63))
def cg_f095_institutional_ownership_level_core65_slope_63d_v066_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(_z(_to_num(value), 252), 63))
def cg_f095_institutional_ownership_level_core66_slope_63d_v067_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(_rank(_to_num(value), 252), 63))
def cg_f095_institutional_ownership_level_core67_slope_63d_v068_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(_safe_div(_to_num(value), _to_num(units)), 63))
def cg_f095_institutional_ownership_level_core68_slope_63d_v069_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(_event_count(investorname, 21), 63))
def cg_f095_institutional_ownership_level_core69_slope_63d_v070_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(_event_rate(investorname, 21), 63))

# core70-74: ewm 63d
def cg_f095_institutional_ownership_level_core70_ewm_63d_v071_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_ewm(_to_num(value), 63))
def cg_f095_institutional_ownership_level_core71_ewm_63d_v072_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_ewm(_to_num(units), 63))
def cg_f095_institutional_ownership_level_core72_ewm_63d_v073_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_ewm(_to_num(price), 63))
def cg_f095_institutional_ownership_level_core73_ewm_63d_v074_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_ewm(_event_flag(investorname), 63))
def cg_f095_institutional_ownership_level_core74_ewm_63d_v075_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_ewm(_pct_change(_to_num(value), 1), 63))
