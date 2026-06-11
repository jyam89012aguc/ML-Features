import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core00-09: mean 4q
def cg_f068_cash_conversion_cycle_core00_mean_4q_v001_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_safe_div(receivables, revenue) * 90.0, 4))
def cg_f068_cash_conversion_cycle_core01_mean_4q_v002_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_safe_div(inventory, cor) * 90.0, 4))
def cg_f068_cash_conversion_cycle_core02_mean_4q_v003_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_safe_div(payables, cor) * 90.0, 4))
def cg_f068_cash_conversion_cycle_core03_mean_4q_v004_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_safe_div(receivables, revenue) * 90.0 + _safe_div(inventory, cor) * 90.0 - _safe_div(payables, cor) * 90.0, 4))
def cg_f068_cash_conversion_cycle_core04_mean_4q_v005_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(receivables, 4))
def cg_f068_cash_conversion_cycle_core05_mean_4q_v006_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(inventory, 4))
def cg_f068_cash_conversion_cycle_core06_mean_4q_v007_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(payables, 4))
def cg_f068_cash_conversion_cycle_core07_mean_4q_v008_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_safe_div(receivables, revenue), 4))
def cg_f068_cash_conversion_cycle_core08_mean_4q_v009_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_safe_div(inventory, cor), 4))
def cg_f068_cash_conversion_cycle_core09_mean_4q_v010_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_safe_div(payables, cor), 4))

# core10-19: mean 8q
def cg_f068_cash_conversion_cycle_core10_mean_8q_v011_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_safe_div(receivables, revenue) * 90.0, 8))
def cg_f068_cash_conversion_cycle_core11_mean_8q_v012_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_safe_div(inventory, cor) * 90.0, 8))
def cg_f068_cash_conversion_cycle_core12_mean_8q_v013_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_safe_div(payables, cor) * 90.0, 8))
def cg_f068_cash_conversion_cycle_core13_mean_8q_v014_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_safe_div(receivables, revenue) * 90.0 + _safe_div(inventory, cor) * 90.0 - _safe_div(payables, cor) * 90.0, 8))
def cg_f068_cash_conversion_cycle_core14_mean_8q_v015_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(receivables, 8))
def cg_f068_cash_conversion_cycle_core15_mean_8q_v016_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(inventory, 8))
def cg_f068_cash_conversion_cycle_core16_mean_8q_v017_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(payables, 8))
def cg_f068_cash_conversion_cycle_core17_mean_8q_v018_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_safe_div(receivables, revenue), 8))
def cg_f068_cash_conversion_cycle_core18_mean_8q_v019_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_safe_div(inventory, cor), 8))
def cg_f068_cash_conversion_cycle_core19_mean_8q_v020_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_safe_div(payables, cor), 8))

# core20-29: z 8q
def cg_f068_cash_conversion_cycle_core20_z_8q_v021_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_safe_div(receivables, revenue) * 90.0, 8))
def cg_f068_cash_conversion_cycle_core21_z_8q_v022_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_safe_div(inventory, cor) * 90.0, 8))
def cg_f068_cash_conversion_cycle_core22_z_8q_v023_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_safe_div(payables, cor) * 90.0, 8))
def cg_f068_cash_conversion_cycle_core23_z_8q_v024_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_safe_div(receivables, revenue) * 90.0 + _safe_div(inventory, cor) * 90.0 - _safe_div(payables, cor) * 90.0, 8))
def cg_f068_cash_conversion_cycle_core24_z_8q_v025_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(receivables, 8))
def cg_f068_cash_conversion_cycle_core25_z_8q_v026_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(inventory, 8))
def cg_f068_cash_conversion_cycle_core26_z_8q_v027_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(payables, 8))
def cg_f068_cash_conversion_cycle_core27_z_8q_v028_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_safe_div(receivables, revenue), 8))
def cg_f068_cash_conversion_cycle_core28_z_8q_v029_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_safe_div(inventory, cor), 8))
def cg_f068_cash_conversion_cycle_core29_z_8q_v030_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_safe_div(payables, cor), 8))

# core30-39: z 20q
def cg_f068_cash_conversion_cycle_core30_z_20q_v031_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_safe_div(receivables, revenue) * 90.0, 20))
def cg_f068_cash_conversion_cycle_core31_z_20q_v032_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_safe_div(inventory, cor) * 90.0, 20))
def cg_f068_cash_conversion_cycle_core32_z_20q_v033_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_safe_div(payables, cor) * 90.0, 20))
def cg_f068_cash_conversion_cycle_core33_z_20q_v034_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_safe_div(receivables, revenue) * 90.0 + _safe_div(inventory, cor) * 90.0 - _safe_div(payables, cor) * 90.0, 20))
def cg_f068_cash_conversion_cycle_core34_z_20q_v035_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(receivables, 20))
def cg_f068_cash_conversion_cycle_core35_z_20q_v036_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(inventory, 20))
def cg_f068_cash_conversion_cycle_core36_z_20q_v037_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(payables, 20))
def cg_f068_cash_conversion_cycle_core37_z_20q_v038_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_safe_div(receivables, revenue), 20))
def cg_f068_cash_conversion_cycle_core38_z_20q_v039_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_safe_div(inventory, cor), 20))
def cg_f068_cash_conversion_cycle_core39_z_20q_v040_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_safe_div(payables, cor), 20))

# core40-49: rank 8q
def cg_f068_cash_conversion_cycle_core40_rank_8q_v041_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_safe_div(receivables, revenue) * 90.0, 8))
def cg_f068_cash_conversion_cycle_core41_rank_8q_v042_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_safe_div(inventory, cor) * 90.0, 8))
def cg_f068_cash_conversion_cycle_core42_rank_8q_v043_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_safe_div(payables, cor) * 90.0, 8))
def cg_f068_cash_conversion_cycle_core43_rank_8q_v044_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_safe_div(receivables, revenue) * 90.0 + _safe_div(inventory, cor) * 90.0 - _safe_div(payables, cor) * 90.0, 8))
def cg_f068_cash_conversion_cycle_core44_rank_8q_v045_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(receivables, 8))
def cg_f068_cash_conversion_cycle_core45_rank_8q_v046_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(inventory, 8))
def cg_f068_cash_conversion_cycle_core46_rank_8q_v047_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(payables, 8))
def cg_f068_cash_conversion_cycle_core47_rank_8q_v048_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_safe_div(receivables, revenue), 8))
def cg_f068_cash_conversion_cycle_core48_rank_8q_v049_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_safe_div(inventory, cor), 8))
def cg_f068_cash_conversion_cycle_core49_rank_8q_v050_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_safe_div(payables, cor), 8))

# core50-59: rank 20q
def cg_f068_cash_conversion_cycle_core50_rank_20q_v051_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_safe_div(receivables, revenue) * 90.0, 20))
def cg_f068_cash_conversion_cycle_core51_rank_20q_v052_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_safe_div(inventory, cor) * 90.0, 20))
def cg_f068_cash_conversion_cycle_core52_rank_20q_v053_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_safe_div(payables, cor) * 90.0, 20))
def cg_f068_cash_conversion_cycle_core53_rank_20q_v054_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_safe_div(receivables, revenue) * 90.0 + _safe_div(inventory, cor) * 90.0 - _safe_div(payables, cor) * 90.0, 20))
def cg_f068_cash_conversion_cycle_core54_rank_20q_v055_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(receivables, 20))
def cg_f068_cash_conversion_cycle_core55_rank_20q_v056_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(inventory, 20))
def cg_f068_cash_conversion_cycle_core56_rank_20q_v057_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(payables, 20))
def cg_f068_cash_conversion_cycle_core57_rank_20q_v058_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_safe_div(receivables, revenue), 20))
def cg_f068_cash_conversion_cycle_core58_rank_20q_v059_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_safe_div(inventory, cor), 20))
def cg_f068_cash_conversion_cycle_core59_rank_20q_v060_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_safe_div(payables, cor), 20))

# core60-69: pct 1q
def cg_f068_cash_conversion_cycle_core60_pct_1q_v061_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_pct_change(_safe_div(receivables, revenue) * 90.0, 1))
def cg_f068_cash_conversion_cycle_core61_pct_1q_v062_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_pct_change(_safe_div(inventory, cor) * 90.0, 1))
def cg_f068_cash_conversion_cycle_core62_pct_1q_v063_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_pct_change(_safe_div(payables, cor) * 90.0, 1))
def cg_f068_cash_conversion_cycle_core63_pct_1q_v064_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_pct_change(_safe_div(receivables, revenue) * 90.0 + _safe_div(inventory, cor) * 90.0 - _safe_div(payables, cor) * 90.0, 1))
def cg_f068_cash_conversion_cycle_core64_pct_1q_v065_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_pct_change(receivables, 1))
def cg_f068_cash_conversion_cycle_core65_pct_1q_v066_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_pct_change(inventory, 1))
def cg_f068_cash_conversion_cycle_core66_pct_1q_v067_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_pct_change(payables, 1))
def cg_f068_cash_conversion_cycle_core67_pct_1q_v068_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_pct_change(_safe_div(receivables, revenue), 1))
def cg_f068_cash_conversion_cycle_core68_pct_1q_v069_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_pct_change(_safe_div(inventory, cor), 1))
def cg_f068_cash_conversion_cycle_core69_pct_1q_v070_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_pct_change(_safe_div(payables, cor), 1))

# core70-74: pct 4q
def cg_f068_cash_conversion_cycle_core70_pct_4q_v071_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_pct_change(_safe_div(receivables, revenue) * 90.0, 4))
def cg_f068_cash_conversion_cycle_core71_pct_4q_v072_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_pct_change(_safe_div(inventory, cor) * 90.0, 4))
def cg_f068_cash_conversion_cycle_core72_pct_4q_v073_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_pct_change(_safe_div(payables, cor) * 90.0, 4))
def cg_f068_cash_conversion_cycle_core73_pct_4q_v074_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_pct_change(_safe_div(receivables, revenue) * 90.0 + _safe_div(inventory, cor) * 90.0 - _safe_div(payables, cor) * 90.0, 4))
def cg_f068_cash_conversion_cycle_core74_pct_4q_v075_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_pct_change(receivables, 4))
