import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core00-09: mean 4q
def cg_f064_return_on_equity_core00_mean_4q_v001_signal(netinc, equity):
    return _clean(_mean(netinc, 4))
def cg_f064_return_on_equity_core01_mean_4q_v002_signal(netinc, equity):
    return _clean(_mean(_safe_div(netinc, equity), 4))
def cg_f064_return_on_equity_core02_mean_4q_v003_signal(netinc, equity):
    return _clean(_mean(equity, 4))
def cg_f064_return_on_equity_core03_mean_4q_v004_signal(netinc, equity):
    return _clean(_mean(_safe_div(netinc, equity.abs() + 1.0), 4))
def cg_f064_return_on_equity_core04_mean_4q_v005_signal(netinc, equity):
    return _clean(_mean(netinc - _mean(netinc, 4), 4))
def cg_f064_return_on_equity_core05_mean_4q_v006_signal(netinc, equity):
    return _clean(_mean(equity - _mean(equity, 4), 4))
def cg_f064_return_on_equity_core06_mean_4q_v007_signal(netinc, equity):
    return _clean(_mean(_safe_div(netinc - _mean(netinc, 4), equity.abs() + 1.0), 4))
def cg_f064_return_on_equity_core07_mean_4q_v008_signal(netinc, equity):
    return _clean(_mean(_safe_div(netinc, (equity - _mean(equity, 4)).abs() + 1.0), 4))
def cg_f064_return_on_equity_core08_mean_4q_v009_signal(netinc, equity):
    return _clean(_mean(_safe_div(netinc, equity).abs(), 4))
def cg_f064_return_on_equity_core09_mean_4q_v010_signal(netinc, equity):
    return _clean(_mean(_safe_div(netinc, equity * 0.5 + 1.0), 4))

# core10-19: mean 8q
def cg_f064_return_on_equity_core10_mean_8q_v011_signal(netinc, equity):
    return _clean(_mean(netinc, 8))
def cg_f064_return_on_equity_core11_mean_8q_v012_signal(netinc, equity):
    return _clean(_mean(_safe_div(netinc, equity), 8))
def cg_f064_return_on_equity_core12_mean_8q_v013_signal(netinc, equity):
    return _clean(_mean(equity, 8))
def cg_f064_return_on_equity_core13_mean_8q_v014_signal(netinc, equity):
    return _clean(_mean(_safe_div(netinc, equity.abs() + 1.0), 8))
def cg_f064_return_on_equity_core14_mean_8q_v015_signal(netinc, equity):
    return _clean(_mean(netinc - _mean(netinc, 8), 8))
def cg_f064_return_on_equity_core15_mean_8q_v016_signal(netinc, equity):
    return _clean(_mean(equity - _mean(equity, 8), 8))
def cg_f064_return_on_equity_core16_mean_8q_v017_signal(netinc, equity):
    return _clean(_mean(_safe_div(netinc - _mean(netinc, 8), equity.abs() + 1.0), 8))
def cg_f064_return_on_equity_core17_mean_8q_v018_signal(netinc, equity):
    return _clean(_mean(_safe_div(netinc, (equity - _mean(equity, 8)).abs() + 1.0), 8))
def cg_f064_return_on_equity_core18_mean_8q_v019_signal(netinc, equity):
    return _clean(_mean(_safe_div(netinc, equity).abs(), 8))
def cg_f064_return_on_equity_core19_mean_8q_v020_signal(netinc, equity):
    return _clean(_mean(_safe_div(netinc, equity * 0.5 + 1.0), 8))

# core20-29: z 8q
def cg_f064_return_on_equity_core20_z_8q_v021_signal(netinc, equity):
    return _clean(_z(netinc, 8))
def cg_f064_return_on_equity_core21_z_8q_v022_signal(netinc, equity):
    return _clean(_z(_safe_div(netinc, equity), 8))
def cg_f064_return_on_equity_core22_z_8q_v023_signal(netinc, equity):
    return _clean(_z(equity, 8))
def cg_f064_return_on_equity_core23_z_8q_v024_signal(netinc, equity):
    return _clean(_z(_safe_div(netinc, equity.abs() + 1.0), 8))
def cg_f064_return_on_equity_core24_z_8q_v025_signal(netinc, equity):
    return _clean(_z(netinc - _mean(netinc, 8), 8))
def cg_f064_return_on_equity_core25_z_8q_v026_signal(netinc, equity):
    return _clean(_z(equity - _mean(equity, 8), 8))
def cg_f064_return_on_equity_core26_z_8q_v027_signal(netinc, equity):
    return _clean(_z(_safe_div(netinc - _mean(netinc, 8), equity.abs() + 1.0), 8))
def cg_f064_return_on_equity_core27_z_8q_v028_signal(netinc, equity):
    return _clean(_z(_safe_div(netinc, (equity - _mean(equity, 8)).abs() + 1.0), 8))
def cg_f064_return_on_equity_core28_z_8q_v029_signal(netinc, equity):
    return _clean(_z(_safe_div(netinc, equity).abs(), 8))
def cg_f064_return_on_equity_core29_z_8q_v030_signal(netinc, equity):
    return _clean(_z(_safe_div(netinc, equity * 0.5 + 1.0), 8))

# core30-39: z 20q
def cg_f064_return_on_equity_core30_z_20q_v031_signal(netinc, equity):
    return _clean(_z(netinc, 20))
def cg_f064_return_on_equity_core31_z_20q_v032_signal(netinc, equity):
    return _clean(_z(_safe_div(netinc, equity), 20))
def cg_f064_return_on_equity_core32_z_20q_v033_signal(netinc, equity):
    return _clean(_z(equity, 20))
def cg_f064_return_on_equity_core33_z_20q_v034_signal(netinc, equity):
    return _clean(_z(_safe_div(netinc, equity.abs() + 1.0), 20))
def cg_f064_return_on_equity_core34_z_20q_v035_signal(netinc, equity):
    return _clean(_z(netinc - _mean(netinc, 20), 20))
def cg_f064_return_on_equity_core35_z_20q_v036_signal(netinc, equity):
    return _clean(_z(equity - _mean(equity, 20), 20))
def cg_f064_return_on_equity_core36_z_20q_v037_signal(netinc, equity):
    return _clean(_z(_safe_div(netinc - _mean(netinc, 20), equity.abs() + 1.0), 20))
def cg_f064_return_on_equity_core37_z_20q_v038_signal(netinc, equity):
    return _clean(_z(_safe_div(netinc, (equity - _mean(equity, 20)).abs() + 1.0), 20))
def cg_f064_return_on_equity_core38_z_20q_v039_signal(netinc, equity):
    return _clean(_z(_safe_div(netinc, equity).abs(), 20))
def cg_f064_return_on_equity_core39_z_20q_v040_signal(netinc, equity):
    return _clean(_z(_safe_div(netinc, equity * 0.5 + 1.0), 20))

# core40-49: rank 8q
def cg_f064_return_on_equity_core40_rank_8q_v041_signal(netinc, equity):
    return _clean(_rank(netinc, 8))
def cg_f064_return_on_equity_core41_rank_8q_v042_signal(netinc, equity):
    return _clean(_rank(_safe_div(netinc, equity), 8))
def cg_f064_return_on_equity_core42_rank_8q_v043_signal(netinc, equity):
    return _clean(_rank(equity, 8))
def cg_f064_return_on_equity_core43_rank_8q_v044_signal(netinc, equity):
    return _clean(_rank(_safe_div(netinc, equity.abs() + 1.0), 8))
def cg_f064_return_on_equity_core44_rank_8q_v045_signal(netinc, equity):
    return _clean(_rank(netinc - _mean(netinc, 8), 8))
def cg_f064_return_on_equity_core45_rank_8q_v046_signal(netinc, equity):
    return _clean(_rank(equity - _mean(equity, 8), 8))
def cg_f064_return_on_equity_core46_rank_8q_v047_signal(netinc, equity):
    return _clean(_rank(_safe_div(netinc - _mean(netinc, 8), equity.abs() + 1.0), 8))
def cg_f064_return_on_equity_core47_rank_8q_v048_signal(netinc, equity):
    return _clean(_rank(_safe_div(netinc, (equity - _mean(equity, 8)).abs() + 1.0), 8))
def cg_f064_return_on_equity_core48_rank_8q_v049_signal(netinc, equity):
    return _clean(_rank(_safe_div(netinc, equity).abs(), 8))
def cg_f064_return_on_equity_core49_rank_8q_v050_signal(netinc, equity):
    return _clean(_rank(_safe_div(netinc, equity * 0.5 + 1.0), 8))

# core50-59: rank 20q
def cg_f064_return_on_equity_core50_rank_20q_v051_signal(netinc, equity):
    return _clean(_rank(netinc, 20))
def cg_f064_return_on_equity_core51_rank_20q_v052_signal(netinc, equity):
    return _clean(_rank(_safe_div(netinc, equity), 20))
def cg_f064_return_on_equity_core52_rank_20q_v053_signal(netinc, equity):
    return _clean(_rank(equity, 20))
def cg_f064_return_on_equity_core53_rank_20q_v054_signal(netinc, equity):
    return _clean(_rank(_safe_div(netinc, equity.abs() + 1.0), 20))
def cg_f064_return_on_equity_core54_rank_20q_v055_signal(netinc, equity):
    return _clean(_rank(netinc - _mean(netinc, 20), 20))
def cg_f064_return_on_equity_core55_rank_20q_v056_signal(netinc, equity):
    return _clean(_rank(equity - _mean(equity, 20), 20))
def cg_f064_return_on_equity_core56_rank_20q_v057_signal(netinc, equity):
    return _clean(_rank(_safe_div(netinc - _mean(netinc, 20), equity.abs() + 1.0), 20))
def cg_f064_return_on_equity_core57_rank_20q_v058_signal(netinc, equity):
    return _clean(_rank(_safe_div(netinc, (equity - _mean(equity, 20)).abs() + 1.0), 20))
def cg_f064_return_on_equity_core58_rank_20q_v059_signal(netinc, equity):
    return _clean(_rank(_safe_div(netinc, equity).abs(), 20))
def cg_f064_return_on_equity_core59_rank_20q_v060_signal(netinc, equity):
    return _clean(_rank(_safe_div(netinc, equity * 0.5 + 1.0), 20))

# core60-69: pct 1q
def cg_f064_return_on_equity_core60_pct_1q_v061_signal(netinc, equity):
    return _clean(_pct_change(netinc, 1))
def cg_f064_return_on_equity_core61_pct_1q_v062_signal(netinc, equity):
    return _clean(_pct_change(_safe_div(netinc, equity), 1))
def cg_f064_return_on_equity_core62_pct_1q_v063_signal(netinc, equity):
    return _clean(_pct_change(equity, 1))
def cg_f064_return_on_equity_core63_pct_1q_v064_signal(netinc, equity):
    return _clean(_pct_change(_safe_div(netinc, equity.abs() + 1.0), 1))
def cg_f064_return_on_equity_core64_pct_1q_v065_signal(netinc, equity):
    return _clean(_pct_change(netinc - _mean(netinc, 4), 1))
def cg_f064_return_on_equity_core65_pct_1q_v066_signal(netinc, equity):
    return _clean(_pct_change(equity - _mean(equity, 4), 1))
def cg_f064_return_on_equity_core66_pct_1q_v067_signal(netinc, equity):
    return _clean(_pct_change(_safe_div(netinc - _mean(netinc, 4), equity.abs() + 1.0), 1))
def cg_f064_return_on_equity_core67_pct_1q_v068_signal(netinc, equity):
    return _clean(_pct_change(_safe_div(netinc, (equity - _mean(equity, 4)).abs() + 1.0), 1))
def cg_f064_return_on_equity_core68_pct_1q_v069_signal(netinc, equity):
    return _clean(_pct_change(_safe_div(netinc, equity).abs(), 1))
def cg_f064_return_on_equity_core69_pct_1q_v070_signal(netinc, equity):
    return _clean(_pct_change(_safe_div(netinc, equity * 0.5 + 1.0), 1))

# core70-74: pct 4q
def cg_f064_return_on_equity_core70_pct_4q_v071_signal(netinc, equity):
    return _clean(_pct_change(netinc, 4))
def cg_f064_return_on_equity_core71_pct_4q_v072_signal(netinc, equity):
    return _clean(_pct_change(_safe_div(netinc, equity), 4))
def cg_f064_return_on_equity_core72_pct_4q_v073_signal(netinc, equity):
    return _clean(_pct_change(equity, 4))
def cg_f064_return_on_equity_core73_pct_4q_v074_signal(netinc, equity):
    return _clean(_pct_change(_safe_div(netinc, equity.abs() + 1.0), 4))
def cg_f064_return_on_equity_core74_pct_4q_v075_signal(netinc, equity):
    return _clean(_pct_change(netinc - _mean(netinc, 4), 4))
