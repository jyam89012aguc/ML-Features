import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core00-09: mean 4q
def cg_f058_comprehensive_income_gap_core00_mean_4q_v001_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_mean(compinc - netinc, 4))
def cg_f058_comprehensive_income_gap_core01_mean_4q_v002_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_mean(_safe_div(compinc - netinc, assets), 4))
def cg_f058_comprehensive_income_gap_core02_mean_4q_v003_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_mean(_safe_div(compinc - netinc, equity.abs() + 1.0), 4))
def cg_f058_comprehensive_income_gap_core03_mean_4q_v004_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_mean(_safe_div(compinc - netinc, revenue), 4))
def cg_f058_comprehensive_income_gap_core04_mean_4q_v005_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_mean(_safe_div(compinc - netinc, marketcap), 4))
def cg_f058_comprehensive_income_gap_core05_mean_4q_v006_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_mean(_safe_div(compinc - netinc, netinc.abs() + 1e-9), 4))
def cg_f058_comprehensive_income_gap_core06_mean_4q_v007_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_mean(_safe_div(compinc, ncfo), 4))
def cg_f058_comprehensive_income_gap_core07_mean_4q_v008_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_mean(_safe_div(compinc, fcf), 4))
def cg_f058_comprehensive_income_gap_core08_mean_4q_v009_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_mean(_diff(compinc - netinc, 4), 4))
def cg_f058_comprehensive_income_gap_core09_mean_4q_v010_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    gap = compinc - netinc
    return _clean(_mean(_safe_div(gap, _std(gap, 4) + 1e-9), 4))

# core10-19: mean 8q
def cg_f058_comprehensive_income_gap_core10_mean_8q_v011_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_mean(compinc - netinc, 8))
def cg_f058_comprehensive_income_gap_core11_mean_8q_v012_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_mean(_safe_div(compinc - netinc, assets), 8))
def cg_f058_comprehensive_income_gap_core12_mean_8q_v013_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_mean(_safe_div(compinc - netinc, equity.abs() + 1.0), 8))
def cg_f058_comprehensive_income_gap_core13_mean_8q_v014_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_mean(_safe_div(compinc - netinc, revenue), 8))
def cg_f058_comprehensive_income_gap_core14_mean_8q_v015_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_mean(_safe_div(compinc - netinc, marketcap), 8))
def cg_f058_comprehensive_income_gap_core15_mean_8q_v016_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_mean(_safe_div(compinc - netinc, netinc.abs() + 1e-9), 8))
def cg_f058_comprehensive_income_gap_core16_mean_8q_v017_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_mean(_safe_div(compinc, ncfo), 8))
def cg_f058_comprehensive_income_gap_core17_mean_8q_v018_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_mean(_safe_div(compinc, fcf), 8))
def cg_f058_comprehensive_income_gap_core18_mean_8q_v019_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_mean(_diff(compinc - netinc, 4), 8))
def cg_f058_comprehensive_income_gap_core19_mean_8q_v020_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    gap = compinc - netinc
    return _clean(_mean(_safe_div(gap, _std(gap, 8) + 1e-9), 8))

# core20-29: z 8q
def cg_f058_comprehensive_income_gap_core20_z_8q_v021_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_z(compinc - netinc, 8))
def cg_f058_comprehensive_income_gap_core21_z_8q_v022_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_z(_safe_div(compinc - netinc, assets), 8))
def cg_f058_comprehensive_income_gap_core22_z_8q_v023_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_z(_safe_div(compinc - netinc, equity.abs() + 1.0), 8))
def cg_f058_comprehensive_income_gap_core23_z_8q_v024_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_z(_safe_div(compinc - netinc, revenue), 8))
def cg_f058_comprehensive_income_gap_core24_z_8q_v025_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_z(_safe_div(compinc - netinc, marketcap), 8))
def cg_f058_comprehensive_income_gap_core25_z_8q_v026_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_z(_safe_div(compinc - netinc, netinc.abs() + 1e-9), 8))
def cg_f058_comprehensive_income_gap_core26_z_8q_v027_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_z(_safe_div(compinc, ncfo), 8))
def cg_f058_comprehensive_income_gap_core27_z_8q_v028_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_z(_safe_div(compinc, fcf), 8))
def cg_f058_comprehensive_income_gap_core28_z_8q_v029_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_z(_diff(compinc - netinc, 4), 8))
def cg_f058_comprehensive_income_gap_core29_z_8q_v030_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    gap = compinc - netinc
    return _clean(_z(_safe_div(gap, _std(gap, 4) + 1e-9), 8))

# core30-39: z 20q
def cg_f058_comprehensive_income_gap_core30_z_20q_v031_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_z(compinc - netinc, 20))
def cg_f058_comprehensive_income_gap_core31_z_20q_v032_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_z(_safe_div(compinc - netinc, assets), 20))
def cg_f058_comprehensive_income_gap_core32_z_20q_v033_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_z(_safe_div(compinc - netinc, equity.abs() + 1.0), 20))
def cg_f058_comprehensive_income_gap_core33_z_20q_v034_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_z(_safe_div(compinc - netinc, revenue), 20))
def cg_f058_comprehensive_income_gap_core34_z_20q_v035_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_z(_safe_div(compinc - netinc, marketcap), 20))
def cg_f058_comprehensive_income_gap_core35_z_20q_v036_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_z(_safe_div(compinc - netinc, netinc.abs() + 1e-9), 20))
def cg_f058_comprehensive_income_gap_core36_z_20q_v037_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_z(_safe_div(compinc, ncfo), 20))
def cg_f058_comprehensive_income_gap_core37_z_20q_v038_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_z(_safe_div(compinc, fcf), 20))
def cg_f058_comprehensive_income_gap_core38_z_20q_v039_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_z(_diff(compinc - netinc, 4), 20))
def cg_f058_comprehensive_income_gap_core39_z_20q_v040_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    gap = compinc - netinc
    return _clean(_z(_safe_div(gap, _std(gap, 8) + 1e-9), 20))

# core40-49: rank 12q
def cg_f058_comprehensive_income_gap_core40_rank_12q_v041_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_rank(compinc - netinc, 12))
def cg_f058_comprehensive_income_gap_core41_rank_12q_v042_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_rank(_safe_div(compinc - netinc, assets), 12))
def cg_f058_comprehensive_income_gap_core42_rank_12q_v043_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_rank(_safe_div(compinc - netinc, equity.abs() + 1.0), 12))
def cg_f058_comprehensive_income_gap_core43_rank_12q_v044_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_rank(_safe_div(compinc - netinc, revenue), 12))
def cg_f058_comprehensive_income_gap_core44_rank_12q_v045_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_rank(_safe_div(compinc - netinc, marketcap), 12))
def cg_f058_comprehensive_income_gap_core45_rank_12q_v046_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_rank(_safe_div(compinc - netinc, netinc.abs() + 1e-9), 12))
def cg_f058_comprehensive_income_gap_core46_rank_12q_v047_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_rank(_safe_div(compinc, ncfo), 12))
def cg_f058_comprehensive_income_gap_core47_rank_12q_v048_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_rank(_safe_div(compinc, fcf), 12))
def cg_f058_comprehensive_income_gap_core48_rank_12q_v049_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_rank(_diff(compinc - netinc, 4), 12))
def cg_f058_comprehensive_income_gap_core49_rank_12q_v050_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    gap = compinc - netinc
    return _clean(_rank(_safe_div(gap, _std(gap, 4) + 1e-9), 12))

# core50-59: rank 20q
def cg_f058_comprehensive_income_gap_core50_rank_20q_v051_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_rank(compinc - netinc, 20))
def cg_f058_comprehensive_income_gap_core51_rank_20q_v052_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_rank(_safe_div(compinc - netinc, assets), 20))
def cg_f058_comprehensive_income_gap_core52_rank_20q_v053_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_rank(_safe_div(compinc - netinc, equity.abs() + 1.0), 20))
def cg_f058_comprehensive_income_gap_core53_rank_20q_v054_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_rank(_safe_div(compinc - netinc, revenue), 20))
def cg_f058_comprehensive_income_gap_core54_rank_20q_v055_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_rank(_safe_div(compinc - netinc, marketcap), 20))
def cg_f058_comprehensive_income_gap_core55_rank_20q_v056_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_rank(_safe_div(compinc - netinc, netinc.abs() + 1e-9), 20))
def cg_f058_comprehensive_income_gap_core56_rank_20q_v057_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_rank(_safe_div(compinc, ncfo), 20))
def cg_f058_comprehensive_income_gap_core57_rank_20q_v058_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_rank(_safe_div(compinc, fcf), 20))
def cg_f058_comprehensive_income_gap_core58_rank_20q_v059_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_rank(_diff(compinc - netinc, 4), 20))
def cg_f058_comprehensive_income_gap_core59_rank_20q_v060_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    gap = compinc - netinc
    return _clean(_rank(_safe_div(gap, _std(gap, 8) + 1e-9), 20))

# core60-69: pct 1q
def cg_f058_comprehensive_income_gap_core60_pct_1q_v061_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_pct_change(compinc - netinc, 1))
def cg_f058_comprehensive_income_gap_core61_pct_1q_v062_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_pct_change(_safe_div(compinc - netinc, assets), 1))
def cg_f058_comprehensive_income_gap_core62_pct_1q_v063_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_pct_change(_safe_div(compinc - netinc, equity.abs() + 1.0), 1))
def cg_f058_comprehensive_income_gap_core63_pct_1q_v064_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_pct_change(_safe_div(compinc - netinc, revenue), 1))
def cg_f058_comprehensive_income_gap_core64_pct_1q_v065_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_pct_change(_safe_div(compinc - netinc, marketcap), 1))
def cg_f058_comprehensive_income_gap_core65_pct_1q_v066_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_pct_change(_safe_div(compinc - netinc, netinc.abs() + 1e-9), 1))
def cg_f058_comprehensive_income_gap_core66_pct_1q_v067_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_pct_change(_safe_div(compinc, ncfo), 1))
def cg_f058_comprehensive_income_gap_core67_pct_1q_v068_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_pct_change(_safe_div(compinc, fcf), 1))
def cg_f058_comprehensive_income_gap_core68_pct_1q_v069_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_pct_change(_diff(compinc - netinc, 4), 1))
def cg_f058_comprehensive_income_gap_core69_pct_1q_v070_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    gap = compinc - netinc
    return _clean(_pct_change(_safe_div(gap, _std(gap, 4) + 1e-9), 1))

# core70-74: pct 4q
def cg_f058_comprehensive_income_gap_core70_pct_4q_v071_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_pct_change(compinc - netinc, 4))
def cg_f058_comprehensive_income_gap_core71_pct_4q_v072_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_pct_change(_safe_div(compinc - netinc, assets), 4))
def cg_f058_comprehensive_income_gap_core72_pct_4q_v073_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_pct_change(_safe_div(compinc - netinc, equity.abs() + 1.0), 4))
def cg_f058_comprehensive_income_gap_core73_pct_4q_v074_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_pct_change(_safe_div(compinc - netinc, revenue), 4))
def cg_f058_comprehensive_income_gap_core74_pct_4q_v075_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_pct_change(_safe_div(compinc - netinc, marketcap), 4))
