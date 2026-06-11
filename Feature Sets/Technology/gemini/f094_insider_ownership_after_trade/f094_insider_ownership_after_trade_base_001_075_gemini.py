import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core00-09: ownership ratios
def cg_f094_insider_ownership_after_trade_core00_pct_bought_v001_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_safe_div(_to_num(transactionshares), _to_num(sharesownedbeforetransaction)))
def cg_f094_insider_ownership_after_trade_core01_pct_owned_v002_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_safe_div(_to_num(sharesownedfollowingtransaction), _to_num(sharesownedbeforetransaction)))
def cg_f094_insider_ownership_after_trade_core02_trade_size_v003_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_safe_div(_to_num(transactionshares), _to_num(sharesownedfollowingtransaction)))
def cg_f094_insider_ownership_after_trade_core03_ownership_diff_v004_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_to_num(sharesownedfollowingtransaction) - _to_num(sharesownedbeforetransaction))
def cg_f094_insider_ownership_after_trade_core04_ownership_pct_v005_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_pct_change(_to_num(sharesownedfollowingtransaction), 1))
def cg_f094_insider_ownership_after_trade_core05_ownership_z_252d_v006_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_to_num(sharesownedfollowingtransaction), 252))
def cg_f094_insider_ownership_after_trade_core06_ownership_rank_252d_v007_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_rank(_to_num(sharesownedfollowingtransaction), 252))
def cg_f094_insider_ownership_after_trade_core07_trade_z_252d_v008_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_to_num(transactionshares), 252))
def cg_f094_insider_ownership_after_trade_core08_trade_rank_252d_v009_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_rank(_to_num(transactionshares), 252))
def cg_f094_insider_ownership_after_trade_core09_ratio_mean_63d_v010_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_mean(_safe_div(_to_num(transactionshares), _to_num(sharesownedbeforetransaction)), 63))

# core10-19: mean 63d
def cg_f094_insider_ownership_after_trade_core10_mean_63d_v011_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_mean(_to_num(sharesownedfollowingtransaction), 63))
def cg_f094_insider_ownership_after_trade_core11_mean_63d_v012_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_mean(_to_num(transactionshares), 63))
def cg_f094_insider_ownership_after_trade_core12_mean_63d_v013_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_mean(_to_num(sharesownedbeforetransaction), 63))
def cg_f094_insider_ownership_after_trade_core13_mean_63d_v014_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_mean(_safe_div(_to_num(transactionshares), _to_num(sharesownedbeforetransaction)), 63))
def cg_f094_insider_ownership_after_trade_core14_mean_63d_v015_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_mean(_pct_change(_to_num(sharesownedfollowingtransaction), 1), 63))
def cg_f094_insider_ownership_after_trade_core15_mean_63d_v016_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_mean(_z(_to_num(sharesownedfollowingtransaction), 252), 63))
def cg_f094_insider_ownership_after_trade_core16_mean_63d_v017_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_mean(_rank(_to_num(sharesownedfollowingtransaction), 252), 63))
def cg_f094_insider_ownership_after_trade_core17_mean_63d_v018_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_mean(_safe_div(_to_num(transactionshares), _to_num(sharesownedfollowingtransaction)), 63))
def cg_f094_insider_ownership_after_trade_core18_mean_63d_v019_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_mean(_diff(_to_num(sharesownedfollowingtransaction), 21), 63))
def cg_f094_insider_ownership_after_trade_core19_mean_63d_v020_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_mean(_z(_to_num(transactionshares), 252), 63))

# core20-29: z 126d
def cg_f094_insider_ownership_after_trade_core20_z_126d_v021_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_to_num(sharesownedfollowingtransaction), 126))
def cg_f094_insider_ownership_after_trade_core21_z_126d_v022_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_to_num(transactionshares), 126))
def cg_f094_insider_ownership_after_trade_core22_z_126d_v023_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_to_num(sharesownedbeforetransaction), 126))
def cg_f094_insider_ownership_after_trade_core23_z_126d_v024_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_safe_div(_to_num(transactionshares), _to_num(sharesownedbeforetransaction)), 126))
def cg_f094_insider_ownership_after_trade_core24_z_126d_v025_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_pct_change(_to_num(sharesownedfollowingtransaction), 1), 126))
def cg_f094_insider_ownership_after_trade_core25_z_126d_v026_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_z(_to_num(sharesownedfollowingtransaction), 252), 126))
def cg_f094_insider_ownership_after_trade_core26_z_126d_v027_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_rank(_to_num(sharesownedfollowingtransaction), 252), 126))
def cg_f094_insider_ownership_after_trade_core27_z_126d_v028_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_safe_div(_to_num(transactionshares), _to_num(sharesownedfollowingtransaction)), 126))
def cg_f094_insider_ownership_after_trade_core28_z_126d_v029_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_diff(_to_num(sharesownedfollowingtransaction), 21), 126))
def cg_f094_insider_ownership_after_trade_core29_z_126d_v030_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_z(_to_num(transactionshares), 252), 126))

# core30-39: rank 252d
def cg_f094_insider_ownership_after_trade_core30_rank_252d_v031_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_rank(_to_num(sharesownedfollowingtransaction), 252))
def cg_f094_insider_ownership_after_trade_core31_rank_252d_v032_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_rank(_to_num(transactionshares), 252))
def cg_f094_insider_ownership_after_trade_core32_rank_252d_v033_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_rank(_to_num(sharesownedbeforetransaction), 252))
def cg_f094_insider_ownership_after_trade_core33_rank_252d_v034_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_rank(_safe_div(_to_num(transactionshares), _to_num(sharesownedbeforetransaction)), 252))
def cg_f094_insider_ownership_after_trade_core34_rank_252d_v035_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_rank(_pct_change(_to_num(sharesownedfollowingtransaction), 1), 252))
def cg_f094_insider_ownership_after_trade_core35_rank_252d_v036_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_rank(_z(_to_num(sharesownedfollowingtransaction), 252), 252))
def cg_f094_insider_ownership_after_trade_core36_rank_252d_v037_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_rank(_rank(_to_num(sharesownedfollowingtransaction), 252), 252))
def cg_f094_insider_ownership_after_trade_core37_rank_252d_v038_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_rank(_safe_div(_to_num(transactionshares), _to_num(sharesownedfollowingtransaction)), 252))
def cg_f094_insider_ownership_after_trade_core38_rank_252d_v039_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_rank(_diff(_to_num(sharesownedfollowingtransaction), 21), 252))
def cg_f094_insider_ownership_after_trade_core39_rank_252d_v040_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_rank(_z(_to_num(transactionshares), 252), 252))

# core40-49: pct 21d
def cg_f094_insider_ownership_after_trade_core40_pct_21d_v041_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_pct_change(_to_num(sharesownedfollowingtransaction), 21))
def cg_f094_insider_ownership_after_trade_core41_pct_21d_v042_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_pct_change(_to_num(transactionshares), 21))
def cg_f094_insider_ownership_after_trade_core42_pct_21d_v043_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_pct_change(_to_num(sharesownedbeforetransaction), 21))
def cg_f094_insider_ownership_after_trade_core43_pct_21d_v044_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_pct_change(_safe_div(_to_num(transactionshares), _to_num(sharesownedbeforetransaction)), 21))
def cg_f094_insider_ownership_after_trade_core44_pct_21d_v045_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_pct_change(_pct_change(_to_num(sharesownedfollowingtransaction), 1), 21))
def cg_f094_insider_ownership_after_trade_core45_pct_21d_v046_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_pct_change(_z(_to_num(sharesownedfollowingtransaction), 252), 21))
def cg_f094_insider_ownership_after_trade_core46_pct_21d_v047_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_pct_change(_rank(_to_num(sharesownedfollowingtransaction), 252), 21))
def cg_f094_insider_ownership_after_trade_core47_pct_21d_v048_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_pct_change(_safe_div(_to_num(transactionshares), _to_num(sharesownedfollowingtransaction)), 21))
def cg_f094_insider_ownership_after_trade_core48_pct_21d_v049_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_pct_change(_diff(_to_num(sharesownedfollowingtransaction), 21), 21))
def cg_f094_insider_ownership_after_trade_core49_pct_21d_v050_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_pct_change(_to_num(sharesownedfollowingtransaction), 63))

# core50-59: std 63d
def cg_f094_insider_ownership_after_trade_core50_std_63d_v051_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_std(_to_num(sharesownedfollowingtransaction), 63))
def cg_f094_insider_ownership_after_trade_core51_std_63d_v052_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_std(_to_num(transactionshares), 63))
def cg_f094_insider_ownership_after_trade_core52_std_63d_v053_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_std(_to_num(sharesownedbeforetransaction), 63))
def cg_f094_insider_ownership_after_trade_core53_std_63d_v054_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_std(_safe_div(_to_num(transactionshares), _to_num(sharesownedbeforetransaction)), 63))
def cg_f094_insider_ownership_after_trade_core54_std_63d_v055_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_std(_pct_change(_to_num(sharesownedfollowingtransaction), 1), 63))
def cg_f094_insider_ownership_after_trade_core55_std_63d_v056_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_std(_z(_to_num(sharesownedfollowingtransaction), 252), 63))
def cg_f094_insider_ownership_after_trade_core56_std_63d_v057_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_std(_rank(_to_num(sharesownedfollowingtransaction), 252), 63))
def cg_f094_insider_ownership_after_trade_core57_std_63d_v058_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_std(_safe_div(_to_num(transactionshares), _to_num(sharesownedfollowingtransaction)), 63))
def cg_f094_insider_ownership_after_trade_core58_std_63d_v059_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_std(_diff(_to_num(sharesownedfollowingtransaction), 21), 63))
def cg_f094_insider_ownership_after_trade_core59_std_63d_v060_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_std(_z(_to_num(transactionshares), 252), 63))

# core60-69: slope 63d
def cg_f094_insider_ownership_after_trade_core60_slope_63d_v061_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(_to_num(sharesownedfollowingtransaction), 63))
def cg_f094_insider_ownership_after_trade_core61_slope_63d_v062_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(_to_num(transactionshares), 63))
def cg_f094_insider_ownership_after_trade_core62_slope_63d_v063_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(_to_num(sharesownedbeforetransaction), 63))
def cg_f094_insider_ownership_after_trade_core63_slope_63d_v064_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(_safe_div(_to_num(transactionshares), _to_num(sharesownedbeforetransaction)), 63))
def cg_f094_insider_ownership_after_trade_core64_slope_63d_v065_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(_pct_change(_to_num(sharesownedfollowingtransaction), 1), 63))
def cg_f094_insider_ownership_after_trade_core65_slope_63d_v066_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(_z(_to_num(sharesownedfollowingtransaction), 252), 63))
def cg_f094_insider_ownership_after_trade_core66_slope_63d_v067_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(_rank(_to_num(sharesownedfollowingtransaction), 252), 63))
def cg_f094_insider_ownership_after_trade_core67_slope_63d_v068_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(_safe_div(_to_num(transactionshares), _to_num(sharesownedfollowingtransaction)), 63))
def cg_f094_insider_ownership_after_trade_core68_slope_63d_v069_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(_diff(_to_num(sharesownedfollowingtransaction), 21), 63))
def cg_f094_insider_ownership_after_trade_core69_slope_63d_v070_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(_z(_to_num(transactionshares), 252), 63))

# core70-74: ewm 63d
def cg_f094_insider_ownership_after_trade_core70_ewm_63d_v071_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_ewm(_to_num(sharesownedfollowingtransaction), 63))
def cg_f094_insider_ownership_after_trade_core71_ewm_63d_v072_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_ewm(_to_num(transactionshares), 63))
def cg_f094_insider_ownership_after_trade_core72_ewm_63d_v073_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_ewm(_to_num(sharesownedbeforetransaction), 63))
def cg_f094_insider_ownership_after_trade_core73_ewm_63d_v074_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_ewm(_safe_div(_to_num(transactionshares), _to_num(sharesownedbeforetransaction)), 63))
def cg_f094_insider_ownership_after_trade_core74_ewm_63d_v075_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_ewm(_pct_change(_to_num(sharesownedfollowingtransaction), 1), 63))
