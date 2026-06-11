import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core00-09: mean 4q
def cg_f023_debt_level_core00_mean_4q_v001_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_mean(debt, 4))
def cg_f023_debt_level_core01_mean_4q_v002_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_mean(_safe_div(debt, assets), 4))
def cg_f023_debt_level_core02_mean_4q_v003_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_mean(_safe_div(debt, marketcap), 4))
def cg_f023_debt_level_core03_mean_4q_v004_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_mean(_safe_div(debt, equity.abs() + 1.0), 4))
def cg_f023_debt_level_core04_mean_4q_v005_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_mean(_safe_div(debt, ncfo.abs() + 1.0), 4))
def cg_f023_debt_level_core05_mean_4q_v006_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_mean(_safe_div(debt, ebitda.clip(lower=0) + 1.0), 4))
def cg_f023_debt_level_core06_mean_4q_v007_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_mean(_safe_div(debt, capital.abs() + 1.0), 4))
def cg_f023_debt_level_core07_mean_4q_v008_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_mean(_safe_div(debt, sharesbas), 4))
def cg_f023_debt_level_core08_mean_4q_v009_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_mean(_safe_div(debtt - debt, debtt.abs() + 1.0), 4))
def cg_f023_debt_level_core09_mean_4q_v010_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_mean(_log(debt.clip(lower=1.0)), 4))

# core10-19: mean 8q
def cg_f023_debt_level_core10_mean_8q_v011_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_mean(debt, 8))
def cg_f023_debt_level_core11_mean_8q_v012_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_mean(_safe_div(debt, assets), 8))
def cg_f023_debt_level_core12_mean_8q_v013_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_mean(_safe_div(debt, marketcap), 8))
def cg_f023_debt_level_core13_mean_8q_v014_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_mean(_safe_div(debt, equity.abs() + 1.0), 8))
def cg_f023_debt_level_core14_mean_8q_v015_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_mean(_safe_div(debt, ncfo.abs() + 1.0), 8))
def cg_f023_debt_level_core15_mean_8q_v016_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_mean(_safe_div(debt, ebitda.clip(lower=0) + 1.0), 8))
def cg_f023_debt_level_core16_mean_8q_v017_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_mean(_safe_div(debt, capital.abs() + 1.0), 8))
def cg_f023_debt_level_core17_mean_8q_v018_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_mean(_safe_div(debt, sharesbas), 8))
def cg_f023_debt_level_core18_mean_8q_v019_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_mean(_safe_div(debtt - debt, debtt.abs() + 1.0), 8))
def cg_f023_debt_level_core19_mean_8q_v020_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_mean(_log(debt.clip(lower=1.0)), 8))

# core20-29: z 8q
def cg_f023_debt_level_core20_z_8q_v021_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_z(debt, 8))
def cg_f023_debt_level_core21_z_8q_v022_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_z(_safe_div(debt, assets), 8))
def cg_f023_debt_level_core22_z_8q_v023_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_z(_safe_div(debt, marketcap), 8))
def cg_f023_debt_level_core23_z_8q_v024_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_z(_safe_div(debt, equity.abs() + 1.0), 8))
def cg_f023_debt_level_core24_z_8q_v025_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_z(_safe_div(debt, ncfo.abs() + 1.0), 8))
def cg_f023_debt_level_core25_z_8q_v026_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_z(_safe_div(debt, ebitda.clip(lower=0) + 1.0), 8))
def cg_f023_debt_level_core26_z_8q_v027_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_z(_safe_div(debt, capital.abs() + 1.0), 8))
def cg_f023_debt_level_core27_z_8q_v028_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_z(_safe_div(debt, sharesbas), 8))
def cg_f023_debt_level_core28_z_8q_v029_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_z(_safe_div(debtt - debt, debtt.abs() + 1.0), 8))
def cg_f023_debt_level_core29_z_8q_v030_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_z(_log(debt.clip(lower=1.0)), 8))

# core30-39: z 20q
def cg_f023_debt_level_core30_z_20q_v031_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_z(debt, 20))
def cg_f023_debt_level_core31_z_20q_v032_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_z(_safe_div(debt, assets), 20))
def cg_f023_debt_level_core32_z_20q_v033_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_z(_safe_div(debt, marketcap), 20))
def cg_f023_debt_level_core33_z_20q_v034_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_z(_safe_div(debt, equity.abs() + 1.0), 20))
def cg_f023_debt_level_core34_z_20q_v035_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_z(_safe_div(debt, ncfo.abs() + 1.0), 20))
def cg_f023_debt_level_core35_z_20q_v036_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_z(_safe_div(debt, ebitda.clip(lower=0) + 1.0), 20))
def cg_f023_debt_level_core36_z_20q_v037_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_z(_safe_div(debt, capital.abs() + 1.0), 20))
def cg_f023_debt_level_core37_z_20q_v038_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_z(_safe_div(debt, sharesbas), 20))
def cg_f023_debt_level_core38_z_20q_v039_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_z(_safe_div(debtt - debt, debtt.abs() + 1.0), 20))
def cg_f023_debt_level_core39_z_20q_v040_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_z(_log(debt.clip(lower=1.0)), 20))

# core40-49: rank 12q
def cg_f023_debt_level_core40_rank_12q_v041_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_rank(debt, 12))
def cg_f023_debt_level_core41_rank_12q_v042_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_rank(_safe_div(debt, assets), 12))
def cg_f023_debt_level_core42_rank_12q_v043_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_rank(_safe_div(debt, marketcap), 12))
def cg_f023_debt_level_core43_rank_12q_v044_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_rank(_safe_div(debt, equity.abs() + 1.0), 12))
def cg_f023_debt_level_core44_rank_12q_v045_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_rank(_safe_div(debt, ncfo.abs() + 1.0), 12))
def cg_f023_debt_level_core45_rank_12q_v046_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_rank(_safe_div(debt, ebitda.clip(lower=0) + 1.0), 12))
def cg_f023_debt_level_core46_rank_12q_v047_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_rank(_safe_div(debt, capital.abs() + 1.0), 12))
def cg_f023_debt_level_core47_rank_12q_v048_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_rank(_safe_div(debt, sharesbas), 12))
def cg_f023_debt_level_core48_rank_12q_v049_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_rank(_safe_div(debtt - debt, debtt.abs() + 1.0), 12))
def cg_f023_debt_level_core49_rank_12q_v050_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_rank(_log(debt.clip(lower=1.0)), 12))

# core50-59: rank 20q
def cg_f023_debt_level_core50_rank_20q_v051_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_rank(debt, 20))
def cg_f023_debt_level_core51_rank_20q_v052_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_rank(_safe_div(debt, assets), 20))
def cg_f023_debt_level_core52_rank_20q_v053_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_rank(_safe_div(debt, marketcap), 20))
def cg_f023_debt_level_core53_rank_20q_v054_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_rank(_safe_div(debt, equity.abs() + 1.0), 20))
def cg_f023_debt_level_core54_rank_20q_v055_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_rank(_safe_div(debt, ncfo.abs() + 1.0), 20))
def cg_f023_debt_level_core55_rank_20q_v056_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_rank(_safe_div(debt, ebitda.clip(lower=0) + 1.0), 20))
def cg_f023_debt_level_core56_rank_20q_v057_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_rank(_safe_div(debt, capital.abs() + 1.0), 20))
def cg_f023_debt_level_core57_rank_20q_v058_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_rank(_safe_div(debt, sharesbas), 20))
def cg_f023_debt_level_core58_rank_20q_v059_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_rank(_safe_div(debtt - debt, debtt.abs() + 1.0), 20))
def cg_f023_debt_level_core59_rank_20q_v060_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_rank(_log(debt.clip(lower=1.0)), 20))

# core60-69: pct 1q
def cg_f023_debt_level_core60_pct_1q_v061_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_pct_change(debt, 1))
def cg_f023_debt_level_core61_pct_1q_v062_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_pct_change(_safe_div(debt, assets), 1))
def cg_f023_debt_level_core62_pct_1q_v063_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_pct_change(_safe_div(debt, marketcap), 1))
def cg_f023_debt_level_core63_pct_1q_v064_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_pct_change(_safe_div(debt, equity.abs() + 1.0), 1))
def cg_f023_debt_level_core64_pct_1q_v065_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_pct_change(_safe_div(debt, ncfo.abs() + 1.0), 1))
def cg_f023_debt_level_core65_pct_1q_v066_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_pct_change(_safe_div(debt, ebitda.clip(lower=0) + 1.0), 1))
def cg_f023_debt_level_core66_pct_1q_v067_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_pct_change(_safe_div(debt, capital.abs() + 1.0), 1))
def cg_f023_debt_level_core67_pct_1q_v068_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_pct_change(_safe_div(debt, sharesbas), 1))
def cg_f023_debt_level_core68_pct_1q_v069_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_pct_change(_safe_div(debtt - debt, debtt.abs() + 1.0), 1))
def cg_f023_debt_level_core69_pct_1q_v070_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_pct_change(_log(debt.clip(lower=1.0)), 1))

# core70-74: pct 4q
def cg_f023_debt_level_core70_pct_4q_v071_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_pct_change(debt, 4))
def cg_f023_debt_level_core71_pct_4q_v072_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_pct_change(_safe_div(debt, assets), 4))
def cg_f023_debt_level_core72_pct_4q_v073_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_pct_change(_safe_div(debt, marketcap), 4))
def cg_f023_debt_level_core73_pct_4q_v074_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_pct_change(_safe_div(debt, equity.abs() + 1.0), 4))
def cg_f023_debt_level_core74_pct_4q_v075_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_pct_change(_safe_div(debt, ncfo.abs() + 1.0), 4))
