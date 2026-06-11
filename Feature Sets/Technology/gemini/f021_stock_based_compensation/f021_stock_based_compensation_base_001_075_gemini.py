import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core00-09: mean 4q
def cg_f021_stock_based_compensation_core00_mean_4q_v001_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_mean(sbc, 4))
def cg_f021_stock_based_compensation_core01_mean_4q_v002_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_mean(_safe_div(sbc, revenue), 4))
def cg_f021_stock_based_compensation_core02_mean_4q_v003_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_mean(_safe_div(sbc, netinc.abs() + 1.0), 4))
def cg_f021_stock_based_compensation_core03_mean_4q_v004_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_mean(_safe_div(sbc, opex.abs() + 1.0), 4))
def cg_f021_stock_based_compensation_core04_mean_4q_v005_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_mean(_safe_div(sbc, marketcap), 4))
def cg_f021_stock_based_compensation_core05_mean_4q_v006_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_mean(_safe_div(sbc, sharesbas), 4))
def cg_f021_stock_based_compensation_core06_mean_4q_v007_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_mean(_safe_div(sbc, fcf.abs() + 1.0), 4))
def cg_f021_stock_based_compensation_core07_mean_4q_v008_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_mean(_safe_div(sbc, rnd.abs() + 1.0), 4))
def cg_f021_stock_based_compensation_core08_mean_4q_v009_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_mean(_safe_div(sbc, assets), 4))
def cg_f021_stock_based_compensation_core09_mean_4q_v010_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_mean(_log(sbc.clip(lower=1.0)), 4))

# core10-19: mean 8q
def cg_f021_stock_based_compensation_core10_mean_8q_v011_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_mean(sbc, 8))
def cg_f021_stock_based_compensation_core11_mean_8q_v012_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_mean(_safe_div(sbc, revenue), 8))
def cg_f021_stock_based_compensation_core12_mean_8q_v013_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_mean(_safe_div(sbc, netinc.abs() + 1.0), 8))
def cg_f021_stock_based_compensation_core13_mean_8q_v014_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_mean(_safe_div(sbc, opex.abs() + 1.0), 8))
def cg_f021_stock_based_compensation_core14_mean_8q_v015_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_mean(_safe_div(sbc, marketcap), 8))
def cg_f021_stock_based_compensation_core15_mean_8q_v016_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_mean(_safe_div(sbc, sharesbas), 8))
def cg_f021_stock_based_compensation_core16_mean_8q_v017_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_mean(_safe_div(sbc, fcf.abs() + 1.0), 8))
def cg_f021_stock_based_compensation_core17_mean_8q_v018_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_mean(_safe_div(sbc, rnd.abs() + 1.0), 8))
def cg_f021_stock_based_compensation_core18_mean_8q_v019_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_mean(_safe_div(sbc, assets), 8))
def cg_f021_stock_based_compensation_core19_mean_8q_v020_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_mean(_log(sbc.clip(lower=1.0)), 8))

# core20-29: z 8q
def cg_f021_stock_based_compensation_core20_z_8q_v021_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_z(sbc, 8))
def cg_f021_stock_based_compensation_core21_z_8q_v022_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_z(_safe_div(sbc, revenue), 8))
def cg_f021_stock_based_compensation_core22_z_8q_v023_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_z(_safe_div(sbc, netinc.abs() + 1.0), 8))
def cg_f021_stock_based_compensation_core23_z_8q_v024_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_z(_safe_div(sbc, opex.abs() + 1.0), 8))
def cg_f021_stock_based_compensation_core24_z_8q_v025_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_z(_safe_div(sbc, marketcap), 8))
def cg_f021_stock_based_compensation_core25_z_8q_v026_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_z(_safe_div(sbc, sharesbas), 8))
def cg_f021_stock_based_compensation_core26_z_8q_v027_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_z(_safe_div(sbc, fcf.abs() + 1.0), 8))
def cg_f021_stock_based_compensation_core27_z_8q_v028_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_z(_safe_div(sbc, rnd.abs() + 1.0), 8))
def cg_f021_stock_based_compensation_core28_z_8q_v029_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_z(_safe_div(sbc, assets), 8))
def cg_f021_stock_based_compensation_core29_z_8q_v030_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_z(_log(sbc.clip(lower=1.0)), 8))

# core30-39: z 20q
def cg_f021_stock_based_compensation_core30_z_20q_v031_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_z(sbc, 20))
def cg_f021_stock_based_compensation_core31_z_20q_v032_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_z(_safe_div(sbc, revenue), 20))
def cg_f021_stock_based_compensation_core32_z_20q_v033_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_z(_safe_div(sbc, netinc.abs() + 1.0), 20))
def cg_f021_stock_based_compensation_core33_z_20q_v034_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_z(_safe_div(sbc, opex.abs() + 1.0), 20))
def cg_f021_stock_based_compensation_core34_z_20q_v035_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_z(_safe_div(sbc, marketcap), 20))
def cg_f021_stock_based_compensation_core35_z_20q_v036_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_z(_safe_div(sbc, sharesbas), 20))
def cg_f021_stock_based_compensation_core36_z_20q_v037_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_z(_safe_div(sbc, fcf.abs() + 1.0), 20))
def cg_f021_stock_based_compensation_core37_z_20q_v038_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_z(_safe_div(sbc, rnd.abs() + 1.0), 20))
def cg_f021_stock_based_compensation_core38_z_20q_v039_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_z(_safe_div(sbc, assets), 20))
def cg_f021_stock_based_compensation_core39_z_20q_v040_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_z(_log(sbc.clip(lower=1.0)), 20))

# core40-49: rank 12q
def cg_f021_stock_based_compensation_core40_rank_12q_v041_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_rank(sbc, 12))
def cg_f021_stock_based_compensation_core41_rank_12q_v042_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_rank(_safe_div(sbc, revenue), 12))
def cg_f021_stock_based_compensation_core42_rank_12q_v043_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_rank(_safe_div(sbc, netinc.abs() + 1.0), 12))
def cg_f021_stock_based_compensation_core43_rank_12q_v044_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_rank(_safe_div(sbc, opex.abs() + 1.0), 12))
def cg_f021_stock_based_compensation_core44_rank_12q_v045_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_rank(_safe_div(sbc, marketcap), 12))
def cg_f021_stock_based_compensation_core45_rank_12q_v046_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_rank(_safe_div(sbc, sharesbas), 12))
def cg_f021_stock_based_compensation_core46_rank_12q_v047_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_rank(_safe_div(sbc, fcf.abs() + 1.0), 12))
def cg_f021_stock_based_compensation_core47_rank_12q_v048_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_rank(_safe_div(sbc, rnd.abs() + 1.0), 12))
def cg_f021_stock_based_compensation_core48_rank_12q_v049_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_rank(_safe_div(sbc, assets), 12))
def cg_f021_stock_based_compensation_core49_rank_12q_v050_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_rank(_log(sbc.clip(lower=1.0)), 12))

# core50-59: rank 20q
def cg_f021_stock_based_compensation_core50_rank_20q_v051_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_rank(sbc, 20))
def cg_f021_stock_based_compensation_core51_rank_20q_v052_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_rank(_safe_div(sbc, revenue), 20))
def cg_f021_stock_based_compensation_core52_rank_20q_v053_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_rank(_safe_div(sbc, netinc.abs() + 1.0), 20))
def cg_f021_stock_based_compensation_core53_rank_20q_v054_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_rank(_safe_div(sbc, opex.abs() + 1.0), 20))
def cg_f021_stock_based_compensation_core54_rank_20q_v055_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_rank(_safe_div(sbc, marketcap), 20))
def cg_f021_stock_based_compensation_core55_rank_20q_v056_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_rank(_safe_div(sbc, sharesbas), 20))
def cg_f021_stock_based_compensation_core56_rank_20q_v057_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_rank(_safe_div(sbc, fcf.abs() + 1.0), 20))
def cg_f021_stock_based_compensation_core57_rank_20q_v058_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_rank(_safe_div(sbc, rnd.abs() + 1.0), 20))
def cg_f021_stock_based_compensation_core58_rank_20q_v059_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_rank(_safe_div(sbc, assets), 20))
def cg_f021_stock_based_compensation_core59_rank_20q_v060_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_rank(_log(sbc.clip(lower=1.0)), 20))

# core60-69: pct 1q
def cg_f021_stock_based_compensation_core60_pct_1q_v061_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_pct_change(sbc, 1))
def cg_f021_stock_based_compensation_core61_pct_1q_v062_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_pct_change(_safe_div(sbc, revenue), 1))
def cg_f021_stock_based_compensation_core62_pct_1q_v063_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_pct_change(_safe_div(sbc, netinc.abs() + 1.0), 1))
def cg_f021_stock_based_compensation_core63_pct_1q_v064_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_pct_change(_safe_div(sbc, opex.abs() + 1.0), 1))
def cg_f021_stock_based_compensation_core64_pct_1q_v065_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_pct_change(_safe_div(sbc, marketcap), 1))
def cg_f021_stock_based_compensation_core65_pct_1q_v066_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_pct_change(_safe_div(sbc, sharesbas), 1))
def cg_f021_stock_based_compensation_core66_pct_1q_v067_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_pct_change(_safe_div(sbc, fcf.abs() + 1.0), 1))
def cg_f021_stock_based_compensation_core67_pct_1q_v068_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_pct_change(_safe_div(sbc, rnd.abs() + 1.0), 1))
def cg_f021_stock_based_compensation_core68_pct_1q_v069_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_pct_change(_safe_div(sbc, assets), 1))
def cg_f021_stock_based_compensation_core69_pct_1q_v070_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_pct_change(_log(sbc.clip(lower=1.0)), 1))

# core70-74: pct 4q
def cg_f021_stock_based_compensation_core70_pct_4q_v071_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_pct_change(sbc, 4))
def cg_f021_stock_based_compensation_core71_pct_4q_v072_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_pct_change(_safe_div(sbc, revenue), 4))
def cg_f021_stock_based_compensation_core72_pct_4q_v073_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_pct_change(_safe_div(sbc, netinc.abs() + 1.0), 4))
def cg_f021_stock_based_compensation_core73_pct_4q_v074_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_pct_change(_safe_div(sbc, opex.abs() + 1.0), 4))
def cg_f021_stock_based_compensation_core74_pct_4q_v075_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_pct_change(_safe_div(sbc, marketcap), 4))
