import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core00-09: mean 4q
def cg_f033_equity_issuance_cash_core00_mean_4q_v001_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_mean(ncfbus, 4))
def cg_f033_equity_issuance_cash_core01_mean_4q_v002_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_mean(_safe_div(ncfbus, assets), 4))
def cg_f033_equity_issuance_cash_core02_mean_4q_v003_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_mean(_safe_div(ncfbus, revenue), 4))
def cg_f033_equity_issuance_cash_core03_mean_4q_v004_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_mean(_safe_div(ncfbus, marketcap), 4))
def cg_f033_equity_issuance_cash_core04_mean_4q_v005_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_mean(_safe_div(ncfbus, ncfo.abs() + 1.0), 4))
def cg_f033_equity_issuance_cash_core05_mean_4q_v006_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_mean(_safe_div(ncfbus, equity.abs() + 1.0), 4))
def cg_f033_equity_issuance_cash_core06_mean_4q_v007_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_mean(_safe_div(ncfbus, sharesbas), 4))
def cg_f033_equity_issuance_cash_core07_mean_4q_v008_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_mean(_safe_div(ncfbus, ncfbus.abs() + ncfo.abs() + 1.0), 4))
def cg_f033_equity_issuance_cash_core08_mean_4q_v009_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_mean(_pct_change(ncfbus, 4), 4))
def cg_f033_equity_issuance_cash_core09_mean_4q_v010_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_mean(_log(ncfbus.clip(lower=1.0)), 4))

# core10-19: mean 8q
def cg_f033_equity_issuance_cash_core10_mean_8q_v011_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_mean(ncfbus, 8))
def cg_f033_equity_issuance_cash_core11_mean_8q_v012_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_mean(_safe_div(ncfbus, assets), 8))
def cg_f033_equity_issuance_cash_core12_mean_8q_v013_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_mean(_safe_div(ncfbus, revenue), 8))
def cg_f033_equity_issuance_cash_core13_mean_8q_v014_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_mean(_safe_div(ncfbus, marketcap), 8))
def cg_f033_equity_issuance_cash_core14_mean_8q_v015_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_mean(_safe_div(ncfbus, ncfo.abs() + 1.0), 8))
def cg_f033_equity_issuance_cash_core15_mean_8q_v016_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_mean(_safe_div(ncfbus, equity.abs() + 1.0), 8))
def cg_f033_equity_issuance_cash_core16_mean_8q_v017_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_mean(_safe_div(ncfbus, sharesbas), 8))
def cg_f033_equity_issuance_cash_core17_mean_8q_v018_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_mean(_safe_div(ncfbus, ncfbus.abs() + ncfo.abs() + 1.0), 8))
def cg_f033_equity_issuance_cash_core18_mean_8q_v019_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_mean(_pct_change(ncfbus, 4), 8))
def cg_f033_equity_issuance_cash_core19_mean_8q_v020_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_mean(_log(ncfbus.clip(lower=1.0)), 8))

# core20-29: z 8q
def cg_f033_equity_issuance_cash_core20_z_8q_v021_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_z(ncfbus, 8))
def cg_f033_equity_issuance_cash_core21_z_8q_v022_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_z(_safe_div(ncfbus, assets), 8))
def cg_f033_equity_issuance_cash_core22_z_8q_v023_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_z(_safe_div(ncfbus, revenue), 8))
def cg_f033_equity_issuance_cash_core23_z_8q_v024_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_z(_safe_div(ncfbus, marketcap), 8))
def cg_f033_equity_issuance_cash_core24_z_8q_v025_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_z(_safe_div(ncfbus, ncfo.abs() + 1.0), 8))
def cg_f033_equity_issuance_cash_core25_z_8q_v026_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_z(_safe_div(ncfbus, equity.abs() + 1.0), 8))
def cg_f033_equity_issuance_cash_core26_z_8q_v027_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_z(_safe_div(ncfbus, sharesbas), 8))
def cg_f033_equity_issuance_cash_core27_z_8q_v028_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_z(_safe_div(ncfbus, ncfbus.abs() + ncfo.abs() + 1.0), 8))
def cg_f033_equity_issuance_cash_core28_z_8q_v029_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_z(_pct_change(ncfbus, 4), 8))
def cg_f033_equity_issuance_cash_core29_z_8q_v030_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_z(_log(ncfbus.clip(lower=1.0)), 8))

# core30-39: z 20q
def cg_f033_equity_issuance_cash_core30_z_20q_v031_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_z(ncfbus, 20))
def cg_f033_equity_issuance_cash_core31_z_20q_v032_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_z(_safe_div(ncfbus, assets), 20))
def cg_f033_equity_issuance_cash_core32_z_20q_v033_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_z(_safe_div(ncfbus, revenue), 20))
def cg_f033_equity_issuance_cash_core33_z_20q_v034_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_z(_safe_div(ncfbus, marketcap), 20))
def cg_f033_equity_issuance_cash_core34_z_20q_v035_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_z(_safe_div(ncfbus, ncfo.abs() + 1.0), 20))
def cg_f033_equity_issuance_cash_core35_z_20q_v036_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_z(_safe_div(ncfbus, equity.abs() + 1.0), 20))
def cg_f033_equity_issuance_cash_core36_z_20q_v037_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_z(_safe_div(ncfbus, sharesbas), 20))
def cg_f033_equity_issuance_cash_core37_z_20q_v038_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_z(_safe_div(ncfbus, ncfbus.abs() + ncfo.abs() + 1.0), 20))
def cg_f033_equity_issuance_cash_core38_z_20q_v039_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_z(_pct_change(ncfbus, 4), 20))
def cg_f033_equity_issuance_cash_core39_z_20q_v040_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_z(_log(ncfbus.clip(lower=1.0)), 20))

# core40-49: rank 12q
def cg_f033_equity_issuance_cash_core40_rank_12q_v041_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_rank(ncfbus, 12))
def cg_f033_equity_issuance_cash_core41_rank_12q_v042_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_rank(_safe_div(ncfbus, assets), 12))
def cg_f033_equity_issuance_cash_core42_rank_12q_v043_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_rank(_safe_div(ncfbus, revenue), 12))
def cg_f033_equity_issuance_cash_core43_rank_12q_v044_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_rank(_safe_div(ncfbus, marketcap), 12))
def cg_f033_equity_issuance_cash_core44_rank_12q_v045_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_rank(_safe_div(ncfbus, ncfo.abs() + 1.0), 12))
def cg_f033_equity_issuance_cash_core45_rank_12q_v046_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_rank(_safe_div(ncfbus, equity.abs() + 1.0), 12))
def cg_f033_equity_issuance_cash_core46_rank_12q_v047_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_rank(_safe_div(ncfbus, sharesbas), 12))
def cg_f033_equity_issuance_cash_core47_rank_12q_v048_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_rank(_safe_div(ncfbus, ncfbus.abs() + ncfo.abs() + 1.0), 12))
def cg_f033_equity_issuance_cash_core48_rank_12q_v049_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_rank(_pct_change(ncfbus, 4), 12))
def cg_f033_equity_issuance_cash_core49_rank_12q_v050_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_rank(_log(ncfbus.clip(lower=1.0)), 12))

# core50-59: rank 20q
def cg_f033_equity_issuance_cash_core50_rank_20q_v051_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_rank(ncfbus, 20))
def cg_f033_equity_issuance_cash_core51_rank_20q_v052_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_rank(_safe_div(ncfbus, assets), 20))
def cg_f033_equity_issuance_cash_core52_rank_20q_v053_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_rank(_safe_div(ncfbus, revenue), 20))
def cg_f033_equity_issuance_cash_core53_rank_20q_v054_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_rank(_safe_div(ncfbus, marketcap), 20))
def cg_f033_equity_issuance_cash_core54_rank_20q_v055_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_rank(_safe_div(ncfbus, ncfo.abs() + 1.0), 20))
def cg_f033_equity_issuance_cash_core55_rank_20q_v056_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_rank(_safe_div(ncfbus, equity.abs() + 1.0), 20))
def cg_f033_equity_issuance_cash_core56_rank_20q_v057_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_rank(_safe_div(ncfbus, sharesbas), 20))
def cg_f033_equity_issuance_cash_core57_rank_20q_v058_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_rank(_safe_div(ncfbus, ncfbus.abs() + ncfo.abs() + 1.0), 20))
def cg_f033_equity_issuance_cash_core58_rank_20q_v059_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_rank(_pct_change(ncfbus, 4), 20))
def cg_f033_equity_issuance_cash_core59_rank_20q_v060_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_rank(_log(ncfbus.clip(lower=1.0)), 20))

# core60-69: pct 1q
def cg_f033_equity_issuance_cash_core60_pct_1q_v061_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_pct_change(ncfbus, 1))
def cg_f033_equity_issuance_cash_core61_pct_1q_v062_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_pct_change(_safe_div(ncfbus, assets), 1))
def cg_f033_equity_issuance_cash_core62_pct_1q_v063_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_pct_change(_safe_div(ncfbus, revenue), 1))
def cg_f033_equity_issuance_cash_core63_pct_1q_v064_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_pct_change(_safe_div(ncfbus, marketcap), 1))
def cg_f033_equity_issuance_cash_core64_pct_1q_v065_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_pct_change(_safe_div(ncfbus, ncfo.abs() + 1.0), 1))
def cg_f033_equity_issuance_cash_core65_pct_1q_v066_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_pct_change(_safe_div(ncfbus, equity.abs() + 1.0), 1))
def cg_f033_equity_issuance_cash_core66_pct_1q_v067_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_pct_change(_safe_div(ncfbus, sharesbas), 1))
def cg_f033_equity_issuance_cash_core67_pct_1q_v068_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_pct_change(_safe_div(ncfbus, ncfbus.abs() + ncfo.abs() + 1.0), 1))
def cg_f033_equity_issuance_cash_core68_pct_1q_v069_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_pct_change(_pct_change(ncfbus, 4), 1))
def cg_f033_equity_issuance_cash_core69_pct_1q_v070_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_pct_change(_log(ncfbus.clip(lower=1.0)), 1))

# core70-74: pct 4q
def cg_f033_equity_issuance_cash_core70_pct_4q_v071_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_pct_change(ncfbus, 4))
def cg_f033_equity_issuance_cash_core71_pct_4q_v072_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_pct_change(_safe_div(ncfbus, assets), 4))
def cg_f033_equity_issuance_cash_core72_pct_4q_v073_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_pct_change(_safe_div(ncfbus, revenue), 4))
def cg_f033_equity_issuance_cash_core73_pct_4q_v074_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_pct_change(_safe_div(ncfbus, marketcap), 4))
def cg_f033_equity_issuance_cash_core74_pct_4q_v075_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_pct_change(_safe_div(ncfbus, ncfo.abs() + 1.0), 4))
