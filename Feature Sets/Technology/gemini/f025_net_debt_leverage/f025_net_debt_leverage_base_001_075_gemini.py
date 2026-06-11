import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core00-09: mean 4q
def cg_f025_net_debt_leverage_core00_mean_4q_v001_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_mean(_safe_div(debtt - cashneq, ebitda.clip(lower=0) + 1.0), 4))
def cg_f025_net_debt_leverage_core01_mean_4q_v002_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_mean(_safe_div(debtt - cashneq, ncfo.abs() + 1.0), 4))
def cg_f025_net_debt_leverage_core02_mean_4q_v003_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_mean(_safe_div(debtt - cashneq, revenue), 4))
def cg_f025_net_debt_leverage_core03_mean_4q_v004_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_mean(_safe_div(debtt - cashneq, assets), 4))
def cg_f025_net_debt_leverage_core04_mean_4q_v005_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_mean(_safe_div(debtt - cashneq, marketcap), 4))
def cg_f025_net_debt_leverage_core05_mean_4q_v006_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_mean(debtt - cashneq, 4))
def cg_f025_net_debt_leverage_core06_mean_4q_v007_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_mean(_safe_div(debtt - cashneq, sharesbas), 4))
def cg_f025_net_debt_leverage_core07_mean_4q_v008_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_mean(_safe_div(debtt, cashneq.abs() + 1.0), 4))
def cg_f025_net_debt_leverage_core08_mean_4q_v009_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_mean(_safe_div(cashneq, debtt.abs() + 1.0), 4))
def cg_f025_net_debt_leverage_core09_mean_4q_v010_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_mean(_log((debtt - cashneq).clip(lower=1.0)), 4))

# core10-19: mean 8q
def cg_f025_net_debt_leverage_core10_mean_8q_v011_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_mean(_safe_div(debtt - cashneq, ebitda.clip(lower=0) + 1.0), 8))
def cg_f025_net_debt_leverage_core11_mean_8q_v012_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_mean(_safe_div(debtt - cashneq, ncfo.abs() + 1.0), 8))
def cg_f025_net_debt_leverage_core12_mean_8q_v013_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_mean(_safe_div(debtt - cashneq, revenue), 8))
def cg_f025_net_debt_leverage_core13_mean_8q_v014_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_mean(_safe_div(debtt - cashneq, assets), 8))
def cg_f025_net_debt_leverage_core14_mean_8q_v015_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_mean(_safe_div(debtt - cashneq, marketcap), 8))
def cg_f025_net_debt_leverage_core15_mean_8q_v016_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_mean(debtt - cashneq, 8))
def cg_f025_net_debt_leverage_core16_mean_8q_v017_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_mean(_safe_div(debtt - cashneq, sharesbas), 8))
def cg_f025_net_debt_leverage_core17_mean_8q_v018_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_mean(_safe_div(debtt, cashneq.abs() + 1.0), 8))
def cg_f025_net_debt_leverage_core18_mean_8q_v019_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_mean(_safe_div(cashneq, debtt.abs() + 1.0), 8))
def cg_f025_net_debt_leverage_core19_mean_8q_v020_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_mean(_log((debtt - cashneq).clip(lower=1.0)), 8))

# core20-29: z 8q
def cg_f025_net_debt_leverage_core20_z_8q_v021_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_z(_safe_div(debtt - cashneq, ebitda.clip(lower=0) + 1.0), 8))
def cg_f025_net_debt_leverage_core21_z_8q_v022_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_z(_safe_div(debtt - cashneq, ncfo.abs() + 1.0), 8))
def cg_f025_net_debt_leverage_core22_z_8q_v023_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_z(_safe_div(debtt - cashneq, revenue), 8))
def cg_f025_net_debt_leverage_core23_z_8q_v024_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_z(_safe_div(debtt - cashneq, assets), 8))
def cg_f025_net_debt_leverage_core24_z_8q_v025_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_z(_safe_div(debtt - cashneq, marketcap), 8))
def cg_f025_net_debt_leverage_core25_z_8q_v026_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_z(debtt - cashneq, 8))
def cg_f025_net_debt_leverage_core26_z_8q_v027_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_z(_safe_div(debtt - cashneq, sharesbas), 8))
def cg_f025_net_debt_leverage_core27_z_8q_v028_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_z(_safe_div(debtt, cashneq.abs() + 1.0), 8))
def cg_f025_net_debt_leverage_core28_z_8q_v029_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_z(_safe_div(cashneq, debtt.abs() + 1.0), 8))
def cg_f025_net_debt_leverage_core29_z_8q_v030_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_z(_log((debtt - cashneq).clip(lower=1.0)), 8))

# core30-39: z 20q
def cg_f025_net_debt_leverage_core30_z_20q_v031_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_z(_safe_div(debtt - cashneq, ebitda.clip(lower=0) + 1.0), 20))
def cg_f025_net_debt_leverage_core31_z_20q_v032_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_z(_safe_div(debtt - cashneq, ncfo.abs() + 1.0), 20))
def cg_f025_net_debt_leverage_core32_z_20q_v033_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_z(_safe_div(debtt - cashneq, revenue), 20))
def cg_f025_net_debt_leverage_core33_z_20q_v034_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_z(_safe_div(debtt - cashneq, assets), 20))
def cg_f025_net_debt_leverage_core34_z_20q_v035_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_z(_safe_div(debtt - cashneq, marketcap), 20))
def cg_f025_net_debt_leverage_core35_z_20q_v036_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_z(debtt - cashneq, 20))
def cg_f025_net_debt_leverage_core36_z_20q_v037_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_z(_safe_div(debtt - cashneq, sharesbas), 20))
def cg_f025_net_debt_leverage_core37_z_20q_v038_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_z(_safe_div(debtt, cashneq.abs() + 1.0), 20))
def cg_f025_net_debt_leverage_core38_z_20q_v039_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_z(_safe_div(cashneq, debtt.abs() + 1.0), 20))
def cg_f025_net_debt_leverage_core39_z_20q_v040_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_z(_log((debtt - cashneq).clip(lower=1.0)), 20))

# core40-49: rank 12q
def cg_f025_net_debt_leverage_core40_rank_12q_v041_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_rank(_safe_div(debtt - cashneq, ebitda.clip(lower=0) + 1.0), 12))
def cg_f025_net_debt_leverage_core41_rank_12q_v042_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_rank(_safe_div(debtt - cashneq, ncfo.abs() + 1.0), 12))
def cg_f025_net_debt_leverage_core42_rank_12q_v043_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_rank(_safe_div(debtt - cashneq, revenue), 12))
def cg_f025_net_debt_leverage_core43_rank_12q_v044_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_rank(_safe_div(debtt - cashneq, assets), 12))
def cg_f025_net_debt_leverage_core44_rank_12q_v045_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_rank(_safe_div(debtt - cashneq, marketcap), 12))
def cg_f025_net_debt_leverage_core45_rank_12q_v046_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_rank(debtt - cashneq, 12))
def cg_f025_net_debt_leverage_core46_rank_12q_v047_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_rank(_safe_div(debtt - cashneq, sharesbas), 12))
def cg_f025_net_debt_leverage_core47_rank_12q_v048_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_rank(_safe_div(debtt, cashneq.abs() + 1.0), 12))
def cg_f025_net_debt_leverage_core48_rank_12q_v049_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_rank(_safe_div(cashneq, debtt.abs() + 1.0), 12))
def cg_f025_net_debt_leverage_core49_rank_12q_v050_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_rank(_log((debtt - cashneq).clip(lower=1.0)), 12))

# core50-59: rank 20q
def cg_f025_net_debt_leverage_core50_rank_20q_v051_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_rank(_safe_div(debtt - cashneq, ebitda.clip(lower=0) + 1.0), 20))
def cg_f025_net_debt_leverage_core51_rank_20q_v052_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_rank(_safe_div(debtt - cashneq, ncfo.abs() + 1.0), 20))
def cg_f025_net_debt_leverage_core52_rank_20q_v053_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_rank(_safe_div(debtt - cashneq, revenue), 20))
def cg_f025_net_debt_leverage_core53_rank_20q_v054_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_rank(_safe_div(debtt - cashneq, assets), 20))
def cg_f025_net_debt_leverage_core54_rank_20q_v055_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_rank(_safe_div(debtt - cashneq, marketcap), 20))
def cg_f025_net_debt_leverage_core55_rank_20q_v056_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_rank(debtt - cashneq, 20))
def cg_f025_net_debt_leverage_core56_rank_20q_v057_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_rank(_safe_div(debtt - cashneq, sharesbas), 20))
def cg_f025_net_debt_leverage_core57_rank_20q_v058_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_rank(_safe_div(debtt, cashneq.abs() + 1.0), 20))
def cg_f025_net_debt_leverage_core58_rank_20q_v059_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_rank(_safe_div(cashneq, debtt.abs() + 1.0), 20))
def cg_f025_net_debt_leverage_core59_rank_20q_v060_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_rank(_log((debtt - cashneq).clip(lower=1.0)), 20))

# core60-69: pct 1q
def cg_f025_net_debt_leverage_core60_pct_1q_v061_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_pct_change(_safe_div(debtt - cashneq, ebitda.clip(lower=0) + 1.0), 1))
def cg_f025_net_debt_leverage_core61_pct_1q_v062_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_pct_change(_safe_div(debtt - cashneq, ncfo.abs() + 1.0), 1))
def cg_f025_net_debt_leverage_core62_pct_1q_v063_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_pct_change(_safe_div(debtt - cashneq, revenue), 1))
def cg_f025_net_debt_leverage_core63_pct_1q_v064_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_pct_change(_safe_div(debtt - cashneq, assets), 1))
def cg_f025_net_debt_leverage_core64_pct_1q_v065_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_pct_change(_safe_div(debtt - cashneq, marketcap), 1))
def cg_f025_net_debt_leverage_core65_pct_1q_v066_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_pct_change(debtt - cashneq, 1))
def cg_f025_net_debt_leverage_core66_pct_1q_v067_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_pct_change(_safe_div(debtt - cashneq, sharesbas), 1))
def cg_f025_net_debt_leverage_core67_pct_1q_v068_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_pct_change(_safe_div(debtt, cashneq.abs() + 1.0), 1))
def cg_f025_net_debt_leverage_core68_pct_1q_v069_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_pct_change(_safe_div(cashneq, debtt.abs() + 1.0), 1))
def cg_f025_net_debt_leverage_core69_pct_1q_v070_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_pct_change(_log((debtt - cashneq).clip(lower=1.0)), 1))

# core70-74: pct 4q
def cg_f025_net_debt_leverage_core70_pct_4q_v071_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_pct_change(_safe_div(debtt - cashneq, ebitda.clip(lower=0) + 1.0), 4))
def cg_f025_net_debt_leverage_core71_pct_4q_v072_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_pct_change(_safe_div(debtt - cashneq, ncfo.abs() + 1.0), 4))
def cg_f025_net_debt_leverage_core72_pct_4q_v073_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_pct_change(_safe_div(debtt - cashneq, revenue), 4))
def cg_f025_net_debt_leverage_core73_pct_4q_v074_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_pct_change(_safe_div(debtt - cashneq, assets), 4))
def cg_f025_net_debt_leverage_core74_pct_4q_v075_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_pct_change(_safe_div(debtt - cashneq, marketcap), 4))
