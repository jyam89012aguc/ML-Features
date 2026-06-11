import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core00-09: mean 4q
def cg_f001_cash_and_equivalents_core00_mean_4q_v001_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(cashneq, 4))
def cg_f001_cash_and_equivalents_core01_mean_4q_v002_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_safe_div(cashneq, assets), 4))
def cg_f001_cash_and_equivalents_core02_mean_4q_v003_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_safe_div(cashneq, marketcap), 4))
def cg_f001_cash_and_equivalents_core03_mean_4q_v004_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_safe_div(cashneq, revenue), 4))
def cg_f001_cash_and_equivalents_core04_mean_4q_v005_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_safe_div(cashneq, liabilities), 4))
def cg_f001_cash_and_equivalents_core05_mean_4q_v006_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_safe_div(cashneq, debt), 4))
def cg_f001_cash_and_equivalents_core06_mean_4q_v007_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_safe_div(cashneq, sharesbas), 4))
def cg_f001_cash_and_equivalents_core07_mean_4q_v008_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_safe_div(cashneq, capex.abs() + 1.0), 4))
def cg_f001_cash_and_equivalents_core08_mean_4q_v009_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_safe_div(cashneq, rnd.abs() + 1.0), 4))
def cg_f001_cash_and_equivalents_core09_mean_4q_v010_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_safe_div(cashneq, opex.abs() + 1.0), 4))

# core10-19: mean 8q
def cg_f001_cash_and_equivalents_core10_mean_8q_v011_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(cashneq, 8))
def cg_f001_cash_and_equivalents_core11_mean_8q_v012_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_safe_div(cashneq, assets), 8))
def cg_f001_cash_and_equivalents_core12_mean_8q_v013_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_safe_div(cashneq, marketcap), 8))
def cg_f001_cash_and_equivalents_core13_mean_8q_v014_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_safe_div(cashneq, revenue), 8))
def cg_f001_cash_and_equivalents_core14_mean_8q_v015_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_safe_div(cashneq, liabilities), 8))
def cg_f001_cash_and_equivalents_core15_mean_8q_v016_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_safe_div(cashneq, debt), 8))
def cg_f001_cash_and_equivalents_core16_mean_8q_v017_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_safe_div(cashneq, sharesbas), 8))
def cg_f001_cash_and_equivalents_core17_mean_8q_v018_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_safe_div(cashneq, capex.abs() + 1.0), 8))
def cg_f001_cash_and_equivalents_core18_mean_8q_v019_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_safe_div(cashneq, rnd.abs() + 1.0), 8))
def cg_f001_cash_and_equivalents_core19_mean_8q_v020_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_safe_div(cashneq, opex.abs() + 1.0), 8))

# core20-29: z 8q
def cg_f001_cash_and_equivalents_core20_z_8q_v021_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(cashneq, 8))
def cg_f001_cash_and_equivalents_core21_z_8q_v022_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_safe_div(cashneq, assets), 8))
def cg_f001_cash_and_equivalents_core22_z_8q_v023_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_safe_div(cashneq, marketcap), 8))
def cg_f001_cash_and_equivalents_core23_z_8q_v024_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_safe_div(cashneq, revenue), 8))
def cg_f001_cash_and_equivalents_core24_z_8q_v025_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_safe_div(cashneq, liabilities), 8))
def cg_f001_cash_and_equivalents_core25_z_8q_v026_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_safe_div(cashneq, debt), 8))
def cg_f001_cash_and_equivalents_core26_z_8q_v027_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_safe_div(cashneq, sharesbas), 8))
def cg_f001_cash_and_equivalents_core27_z_8q_v028_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_safe_div(cashneq, capex.abs() + 1.0), 8))
def cg_f001_cash_and_equivalents_core28_z_8q_v029_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_safe_div(cashneq, rnd.abs() + 1.0), 8))
def cg_f001_cash_and_equivalents_core29_z_8q_v030_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_safe_div(cashneq, opex.abs() + 1.0), 8))

# core30-39: z 20q
def cg_f001_cash_and_equivalents_core30_z_20q_v031_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(cashneq, 20))
def cg_f001_cash_and_equivalents_core31_z_20q_v032_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_safe_div(cashneq, assets), 20))
def cg_f001_cash_and_equivalents_core32_z_20q_v033_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_safe_div(cashneq, marketcap), 20))
def cg_f001_cash_and_equivalents_core33_z_20q_v034_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_safe_div(cashneq, revenue), 20))
def cg_f001_cash_and_equivalents_core34_z_20q_v035_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_safe_div(cashneq, liabilities), 20))
def cg_f001_cash_and_equivalents_core35_z_20q_v036_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_safe_div(cashneq, debt), 20))
def cg_f001_cash_and_equivalents_core36_z_20q_v037_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_safe_div(cashneq, sharesbas), 20))
def cg_f001_cash_and_equivalents_core37_z_20q_v038_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_safe_div(cashneq, capex.abs() + 1.0), 20))
def cg_f001_cash_and_equivalents_core38_z_20q_v039_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_safe_div(cashneq, rnd.abs() + 1.0), 20))
def cg_f001_cash_and_equivalents_core39_z_20q_v040_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_safe_div(cashneq, opex.abs() + 1.0), 20))

# core40-49: rank 12q
def cg_f001_cash_and_equivalents_core40_rank_12q_v041_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(cashneq, 12))
def cg_f001_cash_and_equivalents_core41_rank_12q_v042_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_safe_div(cashneq, assets), 12))
def cg_f001_cash_and_equivalents_core42_rank_12q_v043_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_safe_div(cashneq, marketcap), 12))
def cg_f001_cash_and_equivalents_core43_rank_12q_v044_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_safe_div(cashneq, revenue), 12))
def cg_f001_cash_and_equivalents_core44_rank_12q_v045_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_safe_div(cashneq, liabilities), 12))
def cg_f001_cash_and_equivalents_core45_rank_12q_v046_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_safe_div(cashneq, debt), 12))
def cg_f001_cash_and_equivalents_core46_rank_12q_v047_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_safe_div(cashneq, sharesbas), 12))
def cg_f001_cash_and_equivalents_core47_rank_12q_v048_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_safe_div(cashneq, capex.abs() + 1.0), 12))
def cg_f001_cash_and_equivalents_core48_rank_12q_v049_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_safe_div(cashneq, rnd.abs() + 1.0), 12))
def cg_f001_cash_and_equivalents_core49_rank_12q_v050_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_safe_div(cashneq, opex.abs() + 1.0), 12))

# core50-59: rank 20q
def cg_f001_cash_and_equivalents_core50_rank_20q_v051_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(cashneq, 20))
def cg_f001_cash_and_equivalents_core51_rank_20q_v052_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_safe_div(cashneq, assets), 20))
def cg_f001_cash_and_equivalents_core52_rank_20q_v053_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_safe_div(cashneq, marketcap), 20))
def cg_f001_cash_and_equivalents_core53_rank_20q_v054_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_safe_div(cashneq, revenue), 20))
def cg_f001_cash_and_equivalents_core54_rank_20q_v055_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_safe_div(cashneq, liabilities), 20))
def cg_f001_cash_and_equivalents_core55_rank_20q_v056_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_safe_div(cashneq, debt), 20))
def cg_f001_cash_and_equivalents_core56_rank_20q_v057_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_safe_div(cashneq, sharesbas), 20))
def cg_f001_cash_and_equivalents_core57_rank_20q_v058_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_safe_div(cashneq, capex.abs() + 1.0), 20))
def cg_f001_cash_and_equivalents_core58_rank_20q_v059_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_safe_div(cashneq, rnd.abs() + 1.0), 20))
def cg_f001_cash_and_equivalents_core59_rank_20q_v060_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_safe_div(cashneq, opex.abs() + 1.0), 20))

# core60-69: pct 1q
def cg_f001_cash_and_equivalents_core60_pct_1q_v061_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_pct_change(cashneq, 1))
def cg_f001_cash_and_equivalents_core61_pct_1q_v062_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_pct_change(_safe_div(cashneq, assets), 1))
def cg_f001_cash_and_equivalents_core62_pct_1q_v063_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_pct_change(_safe_div(cashneq, marketcap), 1))
def cg_f001_cash_and_equivalents_core63_pct_1q_v064_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_pct_change(_safe_div(cashneq, revenue), 1))
def cg_f001_cash_and_equivalents_core64_pct_1q_v065_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_pct_change(_safe_div(cashneq, liabilities), 1))
def cg_f001_cash_and_equivalents_core65_pct_1q_v066_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_pct_change(_safe_div(cashneq, debt), 1))
def cg_f001_cash_and_equivalents_core66_pct_1q_v067_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_pct_change(_safe_div(cashneq, sharesbas), 1))
def cg_f001_cash_and_equivalents_core67_pct_1q_v068_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_pct_change(_safe_div(cashneq, capex.abs() + 1.0), 1))
def cg_f001_cash_and_equivalents_core68_pct_1q_v069_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_pct_change(_safe_div(cashneq, rnd.abs() + 1.0), 1))
def cg_f001_cash_and_equivalents_core69_pct_1q_v070_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_pct_change(_safe_div(cashneq, opex.abs() + 1.0), 1))

# core70-74: pct 4q
def cg_f001_cash_and_equivalents_core70_pct_4q_v071_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_pct_change(cashneq, 4))
def cg_f001_cash_and_equivalents_core71_pct_4q_v072_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_pct_change(_safe_div(cashneq, assets), 4))
def cg_f001_cash_and_equivalents_core72_pct_4q_v073_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_pct_change(_safe_div(cashneq, marketcap), 4))
def cg_f001_cash_and_equivalents_core73_pct_4q_v074_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_pct_change(_safe_div(cashneq, revenue), 4))
def cg_f001_cash_and_equivalents_core74_pct_4q_v075_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_pct_change(_safe_div(cashneq, liabilities), 4))
