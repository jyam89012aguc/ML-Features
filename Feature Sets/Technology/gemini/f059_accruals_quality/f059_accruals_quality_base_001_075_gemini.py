import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core00-09: mean 4q
def cg_f059_accruals_quality_core00_mean_4q_v001_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_mean(_safe_div(accruals, assets), 4))
def cg_f059_accruals_quality_core01_mean_4q_v002_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_mean(_safe_div(accruals, revenue), 4))
def cg_f059_accruals_quality_core02_mean_4q_v003_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_mean(_safe_div(accruals, marketcap), 4))
def cg_f059_accruals_quality_core03_mean_4q_v004_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_mean(_safe_div(accruals, equity), 4))
def cg_f059_accruals_quality_core04_mean_4q_v005_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_mean(_safe_div(accruals, ocf.abs() + 1.0), 4))
def cg_f059_accruals_quality_core05_mean_4q_v006_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_mean(_diff(_safe_div(accruals, assets), 4), 4))
def cg_f059_accruals_quality_core06_mean_4q_v007_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_mean(_diff(_safe_div(accruals, revenue), 4), 4))
def cg_f059_accruals_quality_core07_mean_4q_v008_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_mean(_z(_safe_div(accruals, assets), 12), 4))
def cg_f059_accruals_quality_core08_mean_4q_v009_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    return _clean(_mean(_pct_change(netinc, 4) - _pct_change(ocf, 4), 4))
def cg_f059_accruals_quality_core09_mean_4q_v010_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    return _clean(_mean(_safe_div(netinc, ocf.abs() + 1.0), 4))

# core10-19: mean 8q
def cg_f059_accruals_quality_core10_mean_8q_v011_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_mean(_safe_div(accruals, assets), 8))
def cg_f059_accruals_quality_core11_mean_8q_v012_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_mean(_safe_div(accruals, revenue), 8))
def cg_f059_accruals_quality_core12_mean_8q_v013_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_mean(_safe_div(accruals, marketcap), 8))
def cg_f059_accruals_quality_core13_mean_8q_v014_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_mean(_safe_div(accruals, equity), 8))
def cg_f059_accruals_quality_core14_mean_8q_v015_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_mean(_safe_div(accruals, ocf.abs() + 1.0), 8))
def cg_f059_accruals_quality_core15_mean_8q_v016_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_mean(_diff(_safe_div(accruals, assets), 4), 8))
def cg_f059_accruals_quality_core16_mean_8q_v017_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_mean(_diff(_safe_div(accruals, revenue), 4), 8))
def cg_f059_accruals_quality_core17_mean_8q_v018_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_mean(_z(_safe_div(accruals, assets), 12), 8))
def cg_f059_accruals_quality_core18_mean_8q_v019_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    return _clean(_mean(_pct_change(netinc, 4) - _pct_change(ocf, 4), 8))
def cg_f059_accruals_quality_core19_mean_8q_v020_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    return _clean(_mean(_safe_div(netinc, ocf.abs() + 1.0), 8))

# core20-29: z 8q
def cg_f059_accruals_quality_core20_z_8q_v021_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_z(_safe_div(accruals, assets), 8))
def cg_f059_accruals_quality_core21_z_8q_v022_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_z(_safe_div(accruals, revenue), 8))
def cg_f059_accruals_quality_core22_z_8q_v023_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_z(_safe_div(accruals, marketcap), 8))
def cg_f059_accruals_quality_core23_z_8q_v024_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_z(_safe_div(accruals, equity), 8))
def cg_f059_accruals_quality_core24_z_8q_v025_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_z(_safe_div(accruals, ocf.abs() + 1.0), 8))
def cg_f059_accruals_quality_core25_z_8q_v026_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_z(_diff(_safe_div(accruals, assets), 4), 8))
def cg_f059_accruals_quality_core26_z_8q_v027_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_z(_diff(_safe_div(accruals, revenue), 4), 8))
def cg_f059_accruals_quality_core27_z_8q_v028_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_z(_z(_safe_div(accruals, assets), 12), 8))
def cg_f059_accruals_quality_core28_z_8q_v029_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    return _clean(_z(_pct_change(netinc, 4) - _pct_change(ocf, 4), 8))
def cg_f059_accruals_quality_core29_z_8q_v030_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    return _clean(_z(_safe_div(netinc, ocf.abs() + 1.0), 8))

# core30-39: z 20q
def cg_f059_accruals_quality_core30_z_20q_v031_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_z(_safe_div(accruals, assets), 20))
def cg_f059_accruals_quality_core31_z_20q_v032_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_z(_safe_div(accruals, revenue), 20))
def cg_f059_accruals_quality_core32_z_20q_v033_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_z(_safe_div(accruals, marketcap), 20))
def cg_f059_accruals_quality_core33_z_20q_v034_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_z(_safe_div(accruals, equity), 20))
def cg_f059_accruals_quality_core34_z_20q_v035_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_z(_safe_div(accruals, ocf.abs() + 1.0), 20))
def cg_f059_accruals_quality_core35_z_20q_v036_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_z(_diff(_safe_div(accruals, assets), 4), 20))
def cg_f059_accruals_quality_core36_z_20q_v037_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_z(_diff(_safe_div(accruals, revenue), 4), 20))
def cg_f059_accruals_quality_core37_z_20q_v038_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_z(_z(_safe_div(accruals, assets), 12), 20))
def cg_f059_accruals_quality_core38_z_20q_v039_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    return _clean(_z(_pct_change(netinc, 4) - _pct_change(ocf, 4), 20))
def cg_f059_accruals_quality_core39_z_20q_v040_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    return _clean(_z(_safe_div(netinc, ocf.abs() + 1.0), 20))

# core40-49: rank 8q
def cg_f059_accruals_quality_core40_rank_8q_v041_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_rank(_safe_div(accruals, assets), 8))
def cg_f059_accruals_quality_core41_rank_8q_v042_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_rank(_safe_div(accruals, revenue), 8))
def cg_f059_accruals_quality_core42_rank_8q_v043_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_rank(_safe_div(accruals, marketcap), 8))
def cg_f059_accruals_quality_core43_rank_8q_v044_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_rank(_safe_div(accruals, equity), 8))
def cg_f059_accruals_quality_core44_rank_8q_v045_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_rank(_safe_div(accruals, ocf.abs() + 1.0), 8))
def cg_f059_accruals_quality_core45_rank_8q_v046_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_rank(_diff(_safe_div(accruals, assets), 4), 8))
def cg_f059_accruals_quality_core46_rank_8q_v047_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_rank(_diff(_safe_div(accruals, revenue), 4), 8))
def cg_f059_accruals_quality_core47_rank_8q_v048_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_rank(_z(_safe_div(accruals, assets), 12), 8))
def cg_f059_accruals_quality_core48_rank_8q_v049_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    return _clean(_rank(_pct_change(netinc, 4) - _pct_change(ocf, 4), 8))
def cg_f059_accruals_quality_core49_rank_8q_v050_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    return _clean(_rank(_safe_div(netinc, ocf.abs() + 1.0), 8))

# core50-59: rank 20q
def cg_f059_accruals_quality_core50_rank_20q_v051_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_rank(_safe_div(accruals, assets), 20))
def cg_f059_accruals_quality_core51_rank_20q_v052_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_rank(_safe_div(accruals, revenue), 20))
def cg_f059_accruals_quality_core52_rank_20q_v053_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_rank(_safe_div(accruals, marketcap), 20))
def cg_f059_accruals_quality_core53_rank_20q_v054_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_rank(_safe_div(accruals, equity), 20))
def cg_f059_accruals_quality_core54_rank_20q_v055_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_rank(_safe_div(accruals, ocf.abs() + 1.0), 20))
def cg_f059_accruals_quality_core55_rank_20q_v056_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_rank(_diff(_safe_div(accruals, assets), 4), 20))
def cg_f059_accruals_quality_core56_rank_20q_v057_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_rank(_diff(_safe_div(accruals, revenue), 4), 20))
def cg_f059_accruals_quality_core57_rank_20q_v058_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_rank(_z(_safe_div(accruals, assets), 12), 20))
def cg_f059_accruals_quality_core58_rank_20q_v059_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    return _clean(_rank(_pct_change(netinc, 4) - _pct_change(ocf, 4), 20))
def cg_f059_accruals_quality_core59_rank_20q_v060_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    return _clean(_rank(_safe_div(netinc, ocf.abs() + 1.0), 20))

# core60-69: pct 1q
def cg_f059_accruals_quality_core60_pct_1q_v061_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_pct_change(_safe_div(accruals, assets), 1))
def cg_f059_accruals_quality_core61_pct_1q_v062_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_pct_change(_safe_div(accruals, revenue), 1))
def cg_f059_accruals_quality_core62_pct_1q_v063_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_pct_change(_safe_div(accruals, marketcap), 1))
def cg_f059_accruals_quality_core63_pct_1q_v064_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_pct_change(_safe_div(accruals, equity), 1))
def cg_f059_accruals_quality_core64_pct_1q_v065_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_pct_change(_safe_div(accruals, ocf.abs() + 1.0), 1))
def cg_f059_accruals_quality_core65_pct_1q_v066_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    return _clean(_pct_change(_pct_change(netinc, 4) - _pct_change(ocf, 4), 1))
def cg_f059_accruals_quality_core66_pct_1q_v067_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    return _clean(_pct_change(_safe_div(netinc, ocf.abs() + 1.0), 1))
def cg_f059_accruals_quality_core67_pct_1q_v068_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_pct_change(_z(_safe_div(accruals, assets), 12), 1))
def cg_f059_accruals_quality_core68_pct_1q_v069_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_pct_change(_diff(_safe_div(accruals, assets), 4), 1))
def cg_f059_accruals_quality_core69_pct_1q_v070_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    return _clean(_pct_change(_safe_div(netinc - ocf - capex, assets), 1))

# core70-74: pct 4q
def cg_f059_accruals_quality_core70_pct_4q_v071_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_pct_change(_safe_div(accruals, assets), 4))
def cg_f059_accruals_quality_core71_pct_4q_v072_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_pct_change(_safe_div(accruals, revenue), 4))
def cg_f059_accruals_quality_core72_pct_4q_v073_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_pct_change(_safe_div(accruals, marketcap), 4))
def cg_f059_accruals_quality_core73_pct_4q_v074_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_pct_change(_safe_div(accruals, equity), 4))
def cg_f059_accruals_quality_core74_pct_4q_v075_signal(netinc, ocf, assets, revenue, marketcap, liabilities, equity, capex):
    accruals = netinc - ocf
    return _clean(_pct_change(_safe_div(accruals, ocf.abs() + 1.0), 4))
