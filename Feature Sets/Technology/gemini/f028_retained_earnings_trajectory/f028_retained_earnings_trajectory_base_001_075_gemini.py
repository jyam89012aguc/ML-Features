import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core00-09: mean 4q
def cg_f028_retained_earnings_trajectory_core00_mean_4q_v001_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_mean(_safe_div(retainedearnings, assets), 4))
def cg_f028_retained_earnings_trajectory_core01_mean_4q_v002_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_mean(_safe_div(retainedearnings, equity.abs() + 1.0), 4))
def cg_f028_retained_earnings_trajectory_core02_mean_4q_v003_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_mean(_safe_div(retainedearnings, marketcap), 4))
def cg_f028_retained_earnings_trajectory_core03_mean_4q_v004_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_mean(_safe_div(_diff(retainedearnings, 4), netinc.abs() + 1.0), 4))
def cg_f028_retained_earnings_trajectory_core04_mean_4q_v005_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_mean(_safe_div(retainedearnings, revenue), 4))
def cg_f028_retained_earnings_trajectory_core05_mean_4q_v006_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_mean(_safe_div(retainedearnings, debtt.abs() + 1.0), 4))
def cg_f028_retained_earnings_trajectory_core06_mean_4q_v007_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_mean(_safe_div(retainedearnings, sharesbas), 4))
def cg_f028_retained_earnings_trajectory_core07_mean_4q_v008_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_mean(_safe_div(retainedearnings, opex.abs() + 1.0), 4))
def cg_f028_retained_earnings_trajectory_core08_mean_4q_v009_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_mean(retainedearnings, 4))
def cg_f028_retained_earnings_trajectory_core09_mean_4q_v010_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_mean(_log(retainedearnings.clip(lower=1.0)), 4))

# core10-19: mean 8q
def cg_f028_retained_earnings_trajectory_core10_mean_8q_v011_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_mean(_safe_div(retainedearnings, assets), 8))
def cg_f028_retained_earnings_trajectory_core11_mean_8q_v012_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_mean(_safe_div(retainedearnings, equity.abs() + 1.0), 8))
def cg_f028_retained_earnings_trajectory_core12_mean_8q_v013_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_mean(_safe_div(retainedearnings, marketcap), 8))
def cg_f028_retained_earnings_trajectory_core13_mean_8q_v014_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_mean(_safe_div(_diff(retainedearnings, 4), netinc.abs() + 1.0), 8))
def cg_f028_retained_earnings_trajectory_core14_mean_8q_v015_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_mean(_safe_div(retainedearnings, revenue), 8))
def cg_f028_retained_earnings_trajectory_core15_mean_8q_v016_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_mean(_safe_div(retainedearnings, debtt.abs() + 1.0), 8))
def cg_f028_retained_earnings_trajectory_core16_mean_8q_v017_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_mean(_safe_div(retainedearnings, sharesbas), 8))
def cg_f028_retained_earnings_trajectory_core17_mean_8q_v018_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_mean(_safe_div(retainedearnings, opex.abs() + 1.0), 8))
def cg_f028_retained_earnings_trajectory_core18_mean_8q_v019_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_mean(retainedearnings, 8))
def cg_f028_retained_earnings_trajectory_core19_mean_8q_v020_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_mean(_log(retainedearnings.clip(lower=1.0)), 8))

# core20-29: z 8q
def cg_f028_retained_earnings_trajectory_core20_z_8q_v021_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_z(_safe_div(retainedearnings, assets), 8))
def cg_f028_retained_earnings_trajectory_core21_z_8q_v022_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_z(_safe_div(retainedearnings, equity.abs() + 1.0), 8))
def cg_f028_retained_earnings_trajectory_core22_z_8q_v023_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_z(_safe_div(retainedearnings, marketcap), 8))
def cg_f028_retained_earnings_trajectory_core23_z_8q_v024_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_z(_safe_div(_diff(retainedearnings, 4), netinc.abs() + 1.0), 8))
def cg_f028_retained_earnings_trajectory_core24_z_8q_v025_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_z(_safe_div(retainedearnings, revenue), 8))
def cg_f028_retained_earnings_trajectory_core25_z_8q_v026_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_z(_safe_div(retainedearnings, debtt.abs() + 1.0), 8))
def cg_f028_retained_earnings_trajectory_core26_z_8q_v027_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_z(_safe_div(retainedearnings, sharesbas), 8))
def cg_f028_retained_earnings_trajectory_core27_z_8q_v028_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_z(_safe_div(retainedearnings, opex.abs() + 1.0), 8))
def cg_f028_retained_earnings_trajectory_core28_z_8q_v029_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_z(retainedearnings, 8))
def cg_f028_retained_earnings_trajectory_core29_z_8q_v030_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_z(_log(retainedearnings.clip(lower=1.0)), 8))

# core30-39: z 20q
def cg_f028_retained_earnings_trajectory_core30_z_20q_v031_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_z(_safe_div(retainedearnings, assets), 20))
def cg_f028_retained_earnings_trajectory_core31_z_20q_v032_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_z(_safe_div(retainedearnings, equity.abs() + 1.0), 20))
def cg_f028_retained_earnings_trajectory_core32_z_20q_v033_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_z(_safe_div(retainedearnings, marketcap), 20))
def cg_f028_retained_earnings_trajectory_core33_z_20q_v034_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_z(_safe_div(_diff(retainedearnings, 4), netinc.abs() + 1.0), 20))
def cg_f028_retained_earnings_trajectory_core34_z_20q_v035_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_z(_safe_div(retainedearnings, revenue), 20))
def cg_f028_retained_earnings_trajectory_core35_z_20q_v036_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_z(_safe_div(retainedearnings, debtt.abs() + 1.0), 20))
def cg_f028_retained_earnings_trajectory_core36_z_20q_v037_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_z(_safe_div(retainedearnings, sharesbas), 20))
def cg_f028_retained_earnings_trajectory_core37_z_20q_v038_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_z(_safe_div(retainedearnings, opex.abs() + 1.0), 20))
def cg_f028_retained_earnings_trajectory_core38_z_20q_v039_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_z(retainedearnings, 20))
def cg_f028_retained_earnings_trajectory_core39_z_20q_v040_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_z(_log(retainedearnings.clip(lower=1.0)), 20))

# core40-49: rank 12q
def cg_f028_retained_earnings_trajectory_core40_rank_12q_v041_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_rank(_safe_div(retainedearnings, assets), 12))
def cg_f028_retained_earnings_trajectory_core41_rank_12q_v042_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_rank(_safe_div(retainedearnings, equity.abs() + 1.0), 12))
def cg_f028_retained_earnings_trajectory_core42_rank_12q_v043_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_rank(_safe_div(retainedearnings, marketcap), 12))
def cg_f028_retained_earnings_trajectory_core43_rank_12q_v044_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_rank(_safe_div(_diff(retainedearnings, 4), netinc.abs() + 1.0), 12))
def cg_f028_retained_earnings_trajectory_core44_rank_12q_v045_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_rank(_safe_div(retainedearnings, revenue), 12))
def cg_f028_retained_earnings_trajectory_core45_rank_12q_v046_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_rank(_safe_div(retainedearnings, debtt.abs() + 1.0), 12))
def cg_f028_retained_earnings_trajectory_core46_rank_12q_v047_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_rank(_safe_div(retainedearnings, sharesbas), 12))
def cg_f028_retained_earnings_trajectory_core47_rank_12q_v048_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_rank(_safe_div(retainedearnings, opex.abs() + 1.0), 12))
def cg_f028_retained_earnings_trajectory_core48_rank_12q_v049_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_rank(retainedearnings, 12))
def cg_f028_retained_earnings_trajectory_core49_rank_12q_v050_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_rank(_log(retainedearnings.clip(lower=1.0)), 12))

# core50-59: rank 20q
def cg_f028_retained_earnings_trajectory_core50_rank_20q_v051_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_rank(_safe_div(retainedearnings, assets), 20))
def cg_f028_retained_earnings_trajectory_core51_rank_20q_v052_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_rank(_safe_div(retainedearnings, equity.abs() + 1.0), 20))
def cg_f028_retained_earnings_trajectory_core52_rank_20q_v053_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_rank(_safe_div(retainedearnings, marketcap), 20))
def cg_f028_retained_earnings_trajectory_core53_rank_20q_v054_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_rank(_safe_div(_diff(retainedearnings, 4), netinc.abs() + 1.0), 20))
def cg_f028_retained_earnings_trajectory_core54_rank_20q_v055_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_rank(_safe_div(retainedearnings, revenue), 20))
def cg_f028_retained_earnings_trajectory_core55_rank_20q_v056_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_rank(_safe_div(retainedearnings, debtt.abs() + 1.0), 20))
def cg_f028_retained_earnings_trajectory_core56_rank_20q_v057_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_rank(_safe_div(retainedearnings, sharesbas), 20))
def cg_f028_retained_earnings_trajectory_core57_rank_20q_v058_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_rank(_safe_div(retainedearnings, opex.abs() + 1.0), 20))
def cg_f028_retained_earnings_trajectory_core58_rank_20q_v059_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_rank(retainedearnings, 20))
def cg_f028_retained_earnings_trajectory_core59_rank_20q_v060_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_rank(_log(retainedearnings.clip(lower=1.0)), 20))

# core60-69: pct 1q
def cg_f028_retained_earnings_trajectory_core60_pct_1q_v061_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_pct_change(retainedearnings, 1))
def cg_f028_retained_earnings_trajectory_core61_pct_1q_v062_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_pct_change(_safe_div(retainedearnings, assets), 1))
def cg_f028_retained_earnings_trajectory_core62_pct_1q_v063_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_pct_change(_safe_div(retainedearnings, equity.abs() + 1.0), 1))
def cg_f028_retained_earnings_trajectory_core63_pct_1q_v064_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_pct_change(_safe_div(retainedearnings, marketcap), 1))
def cg_f028_retained_earnings_trajectory_core64_pct_1q_v065_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_pct_change(_safe_div(retainedearnings, revenue), 1))
def cg_f028_retained_earnings_trajectory_core65_pct_1q_v066_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_pct_change(_safe_div(retainedearnings, debtt.abs() + 1.0), 1))
def cg_f028_retained_earnings_trajectory_core66_pct_1q_v067_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_pct_change(_safe_div(retainedearnings, sharesbas), 1))
def cg_f028_retained_earnings_trajectory_core67_pct_1q_v068_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_pct_change(_safe_div(retainedearnings, opex.abs() + 1.0), 1))
def cg_f028_retained_earnings_trajectory_core68_pct_1q_v069_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_pct_change(_log(retainedearnings.clip(lower=1.0)), 1))
def cg_f028_retained_earnings_trajectory_core69_pct_1q_v070_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_pct_change(_safe_div(_diff(retainedearnings, 4), netinc.abs() + 1.0), 1))

# core70-74: pct 4q
def cg_f028_retained_earnings_trajectory_core70_pct_4q_v071_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_pct_change(retainedearnings, 4))
def cg_f028_retained_earnings_trajectory_core71_pct_4q_v072_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_pct_change(_safe_div(retainedearnings, assets), 4))
def cg_f028_retained_earnings_trajectory_core72_pct_4q_v073_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_pct_change(_safe_div(retainedearnings, equity.abs() + 1.0), 4))
def cg_f028_retained_earnings_trajectory_core73_pct_4q_v074_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_pct_change(_safe_div(retainedearnings, marketcap), 4))
def cg_f028_retained_earnings_trajectory_core74_pct_4q_v075_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_pct_change(_safe_div(retainedearnings, revenue), 4))
