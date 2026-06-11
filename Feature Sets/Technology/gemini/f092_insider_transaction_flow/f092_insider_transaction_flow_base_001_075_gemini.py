import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core00-09: event rates and flags (252d)
def cg_f092_insider_transaction_flow_core00_event_flag_v001_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _event_flag(transactioncode)
def cg_f092_insider_transaction_flow_core01_event_count_252d_v002_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _event_count(transactioncode, 252)
def cg_f092_insider_transaction_flow_core02_event_rate_252d_v003_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _event_rate(transactioncode, 252)
def cg_f092_insider_transaction_flow_core03_buy_flag_v004_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return (transactioncode == 'P').astype(float)
def cg_f092_insider_transaction_flow_core04_sell_flag_v005_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return (transactioncode == 'S').astype(float)
def cg_f092_insider_transaction_flow_core05_buy_count_252d_v006_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _event_count((transactioncode == 'P').astype(float), 252)
def cg_f092_insider_transaction_flow_core06_sell_count_252d_v007_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _event_count((transactioncode == 'S').astype(float), 252)
def cg_f092_insider_transaction_flow_core07_net_count_252d_v008_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _event_count((transactioncode == 'P').astype(float), 252) - _event_count((transactioncode == 'S').astype(float), 252)
def cg_f092_insider_transaction_flow_core08_value_z_252d_v009_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _z(_to_num(transactionvalue), 252)
def cg_f092_insider_transaction_flow_core09_shares_z_252d_v010_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _z(_to_num(transactionshares), 252)

# core10-19: mean 63d
def cg_f092_insider_transaction_flow_core10_mean_63d_v011_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_mean(_to_num(transactionvalue), 63))
def cg_f092_insider_transaction_flow_core11_mean_63d_v012_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_mean(_to_num(transactionshares), 63))
def cg_f092_insider_transaction_flow_core12_mean_63d_v013_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_mean(_to_num(transactionpricepershare), 63))
def cg_f092_insider_transaction_flow_core13_mean_63d_v014_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_mean(_event_flag(transactioncode), 63))
def cg_f092_insider_transaction_flow_core14_mean_63d_v015_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_mean(_pct_change(_to_num(transactionvalue), 1), 63))
def cg_f092_insider_transaction_flow_core15_mean_63d_v016_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_mean(_z(_to_num(transactionvalue), 252), 63))
def cg_f092_insider_transaction_flow_core16_mean_63d_v017_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_mean(_rank(_to_num(transactionvalue), 252), 63))
def cg_f092_insider_transaction_flow_core17_mean_63d_v018_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_mean(_safe_div(_to_num(transactionvalue), _to_num(transactionshares)), 63))
def cg_f092_insider_transaction_flow_core18_mean_63d_v019_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_mean(_event_count(transactioncode, 21), 63))
def cg_f092_insider_transaction_flow_core19_mean_63d_v020_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_mean(_event_rate(transactioncode, 21), 63))

# core20-29: z 126d
def cg_f092_insider_transaction_flow_core20_z_126d_v021_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_to_num(transactionvalue), 126))
def cg_f092_insider_transaction_flow_core21_z_126d_v022_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_to_num(transactionshares), 126))
def cg_f092_insider_transaction_flow_core22_z_126d_v023_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_to_num(transactionpricepershare), 126))
def cg_f092_insider_transaction_flow_core23_z_126d_v024_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_event_flag(transactioncode), 126))
def cg_f092_insider_transaction_flow_core24_z_126d_v025_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_pct_change(_to_num(transactionvalue), 1), 126))
def cg_f092_insider_transaction_flow_core25_z_126d_v026_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_z(_to_num(transactionvalue), 252), 126))
def cg_f092_insider_transaction_flow_core26_z_126d_v027_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_rank(_to_num(transactionvalue), 252), 126))
def cg_f092_insider_transaction_flow_core27_z_126d_v028_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_safe_div(_to_num(transactionvalue), _to_num(transactionshares)), 126))
def cg_f092_insider_transaction_flow_core28_z_126d_v029_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_event_count(transactioncode, 21), 126))
def cg_f092_insider_transaction_flow_core29_z_126d_v030_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_event_rate(transactioncode, 21), 126))

# core30-39: rank 252d
def cg_f092_insider_transaction_flow_core30_rank_252d_v031_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_rank(_to_num(transactionvalue), 252))
def cg_f092_insider_transaction_flow_core31_rank_252d_v032_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_rank(_to_num(transactionshares), 252))
def cg_f092_insider_transaction_flow_core32_rank_252d_v033_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_rank(_to_num(transactionpricepershare), 252))
def cg_f092_insider_transaction_flow_core33_rank_252d_v034_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_rank(_event_flag(transactioncode), 252))
def cg_f092_insider_transaction_flow_core34_rank_252d_v035_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_rank(_pct_change(_to_num(transactionvalue), 1), 252))
def cg_f092_insider_transaction_flow_core35_rank_252d_v036_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_rank(_z(_to_num(transactionvalue), 252), 252))
def cg_f092_insider_transaction_flow_core36_rank_252d_v037_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_rank(_rank(_to_num(transactionvalue), 252), 252))
def cg_f092_insider_transaction_flow_core37_rank_252d_v038_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_rank(_safe_div(_to_num(transactionvalue), _to_num(transactionshares)), 252))
def cg_f092_insider_transaction_flow_core38_rank_252d_v039_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_rank(_event_count(transactioncode, 21), 252))
def cg_f092_insider_transaction_flow_core39_rank_252d_v040_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_rank(_event_rate(transactioncode, 21), 252))

# core40-49: pct 21d
def cg_f092_insider_transaction_flow_core40_pct_21d_v041_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_pct_change(_to_num(transactionvalue), 21))
def cg_f092_insider_transaction_flow_core41_pct_21d_v042_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_pct_change(_to_num(transactionshares), 21))
def cg_f092_insider_transaction_flow_core42_pct_21d_v043_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_pct_change(_to_num(transactionpricepershare), 21))
def cg_f092_insider_transaction_flow_core43_pct_21d_v044_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_pct_change(_event_count(transactioncode, 21), 21))
def cg_f092_insider_transaction_flow_core44_pct_21d_v045_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_pct_change(_pct_change(_to_num(transactionvalue), 1), 21))
def cg_f092_insider_transaction_flow_core45_pct_21d_v046_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_pct_change(_z(_to_num(transactionvalue), 252), 21))
def cg_f092_insider_transaction_flow_core46_pct_21d_v047_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_pct_change(_rank(_to_num(transactionvalue), 252), 21))
def cg_f092_insider_transaction_flow_core47_pct_21d_v048_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_pct_change(_safe_div(_to_num(transactionvalue), _to_num(transactionshares)), 21))
def cg_f092_insider_transaction_flow_core48_pct_21d_v049_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_pct_change(_event_rate(transactioncode, 21), 21))
def cg_f092_insider_transaction_flow_core49_pct_21d_v050_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_pct_change(_to_num(transactionvalue), 63))

# core50-59: std 63d
def cg_f092_insider_transaction_flow_core50_std_63d_v051_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_std(_to_num(transactionvalue), 63))
def cg_f092_insider_transaction_flow_core51_std_63d_v052_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_std(_to_num(transactionshares), 63))
def cg_f092_insider_transaction_flow_core52_std_63d_v053_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_std(_to_num(transactionpricepershare), 63))
def cg_f092_insider_transaction_flow_core53_std_63d_v054_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_std(_event_flag(transactioncode), 63))
def cg_f092_insider_transaction_flow_core54_std_63d_v055_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_std(_pct_change(_to_num(transactionvalue), 1), 63))
def cg_f092_insider_transaction_flow_core55_std_63d_v056_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_std(_z(_to_num(transactionvalue), 252), 63))
def cg_f092_insider_transaction_flow_core56_std_63d_v057_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_std(_rank(_to_num(transactionvalue), 252), 63))
def cg_f092_insider_transaction_flow_core57_std_63d_v058_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_std(_safe_div(_to_num(transactionvalue), _to_num(transactionshares)), 63))
def cg_f092_insider_transaction_flow_core58_std_63d_v059_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_std(_event_count(transactioncode, 21), 63))
def cg_f092_insider_transaction_flow_core59_std_63d_v060_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_std(_event_rate(transactioncode, 21), 63))

# core60-69: slope 63d
def cg_f092_insider_transaction_flow_core60_slope_63d_v061_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(_to_num(transactionvalue), 63))
def cg_f092_insider_transaction_flow_core61_slope_63d_v062_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(_to_num(transactionshares), 63))
def cg_f092_insider_transaction_flow_core62_slope_63d_v063_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(_to_num(transactionpricepershare), 63))
def cg_f092_insider_transaction_flow_core63_slope_63d_v064_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(_event_flag(transactioncode), 63))
def cg_f092_insider_transaction_flow_core64_slope_63d_v065_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(_pct_change(_to_num(transactionvalue), 1), 63))
def cg_f092_insider_transaction_flow_core65_slope_63d_v066_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(_z(_to_num(transactionvalue), 252), 63))
def cg_f092_insider_transaction_flow_core66_slope_63d_v067_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(_rank(_to_num(transactionvalue), 252), 63))
def cg_f092_insider_transaction_flow_core67_slope_63d_v068_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(_safe_div(_to_num(transactionvalue), _to_num(transactionshares)), 63))
def cg_f092_insider_transaction_flow_core68_slope_63d_v069_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(_event_count(transactioncode, 21), 63))
def cg_f092_insider_transaction_flow_core69_slope_63d_v070_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(_event_rate(transactioncode, 21), 63))

# core70-74: ewm 63d
def cg_f092_insider_transaction_flow_core70_ewm_63d_v071_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_ewm(_to_num(transactionvalue), 63))
def cg_f092_insider_transaction_flow_core71_ewm_63d_v072_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_ewm(_to_num(transactionshares), 63))
def cg_f092_insider_transaction_flow_core72_ewm_63d_v073_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_ewm(_to_num(transactionpricepershare), 63))
def cg_f092_insider_transaction_flow_core73_ewm_63d_v074_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_ewm(_event_flag(transactioncode), 63))
def cg_f092_insider_transaction_flow_core74_ewm_63d_v075_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_ewm(_pct_change(_to_num(transactionvalue), 1), 63))
