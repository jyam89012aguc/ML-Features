import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core00-09: mean 4q
def cg_f011_financing_cash_flow_core00_mean_4q_v001_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_mean(ncff, 4))
def cg_f011_financing_cash_flow_core01_mean_4q_v002_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_mean(ncfinv, 4))
def cg_f011_financing_cash_flow_core02_mean_4q_v003_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_mean(ncfbus, 4))
def cg_f011_financing_cash_flow_core03_mean_4q_v004_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_mean(debt, 4))
def cg_f011_financing_cash_flow_core04_mean_4q_v005_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_mean(dps, 4))
def cg_f011_financing_cash_flow_core05_mean_4q_v006_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_mean(_safe_div(ncff, ncfo.abs() + 1.0), 4))
def cg_f011_financing_cash_flow_core06_mean_4q_v007_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_mean(_safe_div(ncff, assets), 4))
def cg_f011_financing_cash_flow_core07_mean_4q_v008_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_mean(_safe_div(ncfinv, assets), 4))
def cg_f011_financing_cash_flow_core08_mean_4q_v009_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_mean(_safe_div(ncfbus, assets), 4))
def cg_f011_financing_cash_flow_core09_mean_4q_v010_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_mean(_safe_div(ncff, marketcap), 4))

# core10-19: mean 8q
def cg_f011_financing_cash_flow_core10_mean_8q_v011_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_mean(ncff, 8))
def cg_f011_financing_cash_flow_core11_mean_8q_v012_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_mean(ncfinv, 8))
def cg_f011_financing_cash_flow_core12_mean_8q_v013_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_mean(ncfbus, 8))
def cg_f011_financing_cash_flow_core13_mean_8q_v014_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_mean(debt, 8))
def cg_f011_financing_cash_flow_core14_mean_8q_v015_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_mean(dps, 8))
def cg_f011_financing_cash_flow_core15_mean_8q_v016_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_mean(_safe_div(ncff, ncfo.abs() + 1.0), 8))
def cg_f011_financing_cash_flow_core16_mean_8q_v017_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_mean(_safe_div(ncff, assets), 8))
def cg_f011_financing_cash_flow_core17_mean_8q_v018_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_mean(_safe_div(ncfinv, assets), 8))
def cg_f011_financing_cash_flow_core18_mean_8q_v019_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_mean(_safe_div(ncfbus, assets), 8))
def cg_f011_financing_cash_flow_core19_mean_8q_v020_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_mean(_safe_div(ncff, marketcap), 8))

# core20-29: z 8q
def cg_f011_financing_cash_flow_core20_z_8q_v021_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_z(ncff, 8))
def cg_f011_financing_cash_flow_core21_z_8q_v022_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_z(ncfinv, 8))
def cg_f011_financing_cash_flow_core22_z_8q_v023_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_z(ncfbus, 8))
def cg_f011_financing_cash_flow_core23_z_8q_v024_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_z(debt, 8))
def cg_f011_financing_cash_flow_core24_z_8q_v025_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_z(dps, 8))
def cg_f011_financing_cash_flow_core25_z_8q_v026_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_z(_safe_div(ncff, ncfo.abs() + 1.0), 8))
def cg_f011_financing_cash_flow_core26_z_8q_v027_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_z(_safe_div(ncff, assets), 8))
def cg_f011_financing_cash_flow_core27_z_8q_v028_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_z(_safe_div(ncfinv, assets), 8))
def cg_f011_financing_cash_flow_core28_z_8q_v029_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_z(_safe_div(ncfbus, assets), 8))
def cg_f011_financing_cash_flow_core29_z_8q_v030_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_z(_safe_div(ncff, marketcap), 8))

# core30-39: z 20q
def cg_f011_financing_cash_flow_core30_z_20q_v031_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_z(ncff, 20))
def cg_f011_financing_cash_flow_core31_z_20q_v032_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_z(ncfinv, 20))
def cg_f011_financing_cash_flow_core32_z_20q_v033_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_z(ncfbus, 20))
def cg_f011_financing_cash_flow_core33_z_20q_v034_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_z(debt, 20))
def cg_f011_financing_cash_flow_core34_z_20q_v035_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_z(dps, 20))
def cg_f011_financing_cash_flow_core35_z_20q_v036_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_z(_safe_div(ncff, ncfo.abs() + 1.0), 20))
def cg_f011_financing_cash_flow_core36_z_20q_v037_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_z(_safe_div(ncff, assets), 20))
def cg_f011_financing_cash_flow_core37_z_20q_v038_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_z(_safe_div(ncfinv, assets), 20))
def cg_f011_financing_cash_flow_core38_z_20q_v039_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_z(_safe_div(ncfbus, assets), 20))
def cg_f011_financing_cash_flow_core39_z_20q_v040_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_z(_safe_div(ncff, marketcap), 20))

# core40-49: rank 12q
def cg_f011_financing_cash_flow_core40_rank_12q_v041_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_rank(ncff, 12))
def cg_f011_financing_cash_flow_core41_rank_12q_v042_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_rank(ncfinv, 12))
def cg_f011_financing_cash_flow_core42_rank_12q_v043_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_rank(ncfbus, 12))
def cg_f011_financing_cash_flow_core43_rank_12q_v044_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_rank(debt, 12))
def cg_f011_financing_cash_flow_core44_rank_12q_v045_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_rank(dps, 12))
def cg_f011_financing_cash_flow_core45_rank_12q_v046_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_rank(_safe_div(ncff, ncfo.abs() + 1.0), 12))
def cg_f011_financing_cash_flow_core46_rank_12q_v047_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_rank(_safe_div(ncff, assets), 12))
def cg_f011_financing_cash_flow_core47_rank_12q_v048_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_rank(_safe_div(ncfinv, assets), 12))
def cg_f011_financing_cash_flow_core48_rank_12q_v049_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_rank(_safe_div(ncfbus, assets), 12))
def cg_f011_financing_cash_flow_core49_rank_12q_v050_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_rank(_safe_div(ncff, marketcap), 12))

# core50-59: rank 20q
def cg_f011_financing_cash_flow_core50_rank_20q_v051_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_rank(ncff, 20))
def cg_f011_financing_cash_flow_core51_rank_20q_v052_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_rank(ncfinv, 20))
def cg_f011_financing_cash_flow_core52_rank_20q_v053_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_rank(ncfbus, 20))
def cg_f011_financing_cash_flow_core53_rank_20q_v054_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_rank(debt, 20))
def cg_f011_financing_cash_flow_core54_rank_20q_v055_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_rank(dps, 20))
def cg_f011_financing_cash_flow_core55_rank_20q_v056_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_rank(_safe_div(ncff, ncfo.abs() + 1.0), 20))
def cg_f011_financing_cash_flow_core56_rank_20q_v057_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_rank(_safe_div(ncff, assets), 20))
def cg_f011_financing_cash_flow_core57_rank_20q_v058_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_rank(_safe_div(ncfinv, assets), 20))
def cg_f011_financing_cash_flow_core58_rank_20q_v059_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_rank(_safe_div(ncfbus, assets), 20))
def cg_f011_financing_cash_flow_core59_rank_20q_v060_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_rank(_safe_div(ncff, marketcap), 20))

# core60-69: pct 1q
def cg_f011_financing_cash_flow_core60_pct_1q_v061_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_pct_change(ncff, 1))
def cg_f011_financing_cash_flow_core61_pct_1q_v062_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_pct_change(ncfinv, 1))
def cg_f011_financing_cash_flow_core62_pct_1q_v063_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_pct_change(ncfbus, 1))
def cg_f011_financing_cash_flow_core63_pct_1q_v064_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_pct_change(debt, 1))
def cg_f011_financing_cash_flow_core64_pct_1q_v065_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_pct_change(dps, 1))
def cg_f011_financing_cash_flow_core65_pct_1q_v066_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_pct_change(_safe_div(ncff, ncfo.abs() + 1.0), 1))
def cg_f011_financing_cash_flow_core66_pct_1q_v067_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_pct_change(_safe_div(ncff, assets), 1))
def cg_f011_financing_cash_flow_core67_pct_1q_v068_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_pct_change(_safe_div(ncfinv, assets), 1))
def cg_f011_financing_cash_flow_core68_pct_1q_v069_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_pct_change(_safe_div(ncfbus, assets), 1))
def cg_f011_financing_cash_flow_core69_pct_1q_v070_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_pct_change(_safe_div(ncff, marketcap), 1))

# core70-74: pct 4q
def cg_f011_financing_cash_flow_core70_pct_4q_v071_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_pct_change(ncff, 4))
def cg_f011_financing_cash_flow_core71_pct_4q_v072_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_pct_change(ncfinv, 4))
def cg_f011_financing_cash_flow_core72_pct_4q_v073_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_pct_change(ncfbus, 4))
def cg_f011_financing_cash_flow_core73_pct_4q_v074_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_pct_change(debt, 4))
def cg_f011_financing_cash_flow_core74_pct_4q_v075_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_pct_change(dps, 4))
