import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core00-09: mean 4q
def cg_f066_asset_turnover_core00_mean_4q_v001_signal(revenue, assetsavg):
    return _clean(_mean(revenue, 4))
def cg_f066_asset_turnover_core01_mean_4q_v002_signal(revenue, assetsavg):
    return _clean(_mean(_safe_div(revenue, assetsavg), 4))
def cg_f066_asset_turnover_core02_mean_4q_v003_signal(revenue, assetsavg):
    return _clean(_mean(assetsavg, 4))
def cg_f066_asset_turnover_core03_mean_4q_v004_signal(revenue, assetsavg):
    return _clean(_mean(_safe_div(revenue, assetsavg.abs() + 1.0), 4))
def cg_f066_asset_turnover_core04_mean_4q_v005_signal(revenue, assetsavg):
    return _clean(_mean(revenue - _mean(revenue, 4), 4))
def cg_f066_asset_turnover_core05_mean_4q_v006_signal(revenue, assetsavg):
    return _clean(_mean(assetsavg - _mean(assetsavg, 4), 4))
def cg_f066_asset_turnover_core06_mean_4q_v007_signal(revenue, assetsavg):
    return _clean(_mean(_safe_div(revenue - _mean(revenue, 4), assetsavg.abs() + 1.0), 4))
def cg_f066_asset_turnover_core07_mean_4q_v008_signal(revenue, assetsavg):
    return _clean(_mean(_safe_div(revenue, (assetsavg - _mean(assetsavg, 4)).abs() + 1.0), 4))
def cg_f066_asset_turnover_core08_mean_4q_v009_signal(revenue, assetsavg):
    return _clean(_mean(_safe_div(revenue, assetsavg).abs(), 4))
def cg_f066_asset_turnover_core09_mean_4q_v010_signal(revenue, assetsavg):
    return _clean(_mean(_safe_div(revenue, assetsavg * 0.5 + 1.0), 4))

# core10-19: mean 8q
def cg_f066_asset_turnover_core10_mean_8q_v011_signal(revenue, assetsavg):
    return _clean(_mean(revenue, 8))
def cg_f066_asset_turnover_core11_mean_8q_v012_signal(revenue, assetsavg):
    return _clean(_mean(_safe_div(revenue, assetsavg), 8))
def cg_f066_asset_turnover_core12_mean_8q_v013_signal(revenue, assetsavg):
    return _clean(_mean(assetsavg, 8))
def cg_f066_asset_turnover_core13_mean_8q_v014_signal(revenue, assetsavg):
    return _clean(_mean(_safe_div(revenue, assetsavg.abs() + 1.0), 8))
def cg_f066_asset_turnover_core14_mean_8q_v015_signal(revenue, assetsavg):
    return _clean(_mean(revenue - _mean(revenue, 8), 8))
def cg_f066_asset_turnover_core15_mean_8q_v016_signal(revenue, assetsavg):
    return _clean(_mean(assetsavg - _mean(assetsavg, 8), 8))
def cg_f066_asset_turnover_core16_mean_8q_v017_signal(revenue, assetsavg):
    return _clean(_mean(_safe_div(revenue - _mean(revenue, 8), assetsavg.abs() + 1.0), 8))
def cg_f066_asset_turnover_core17_mean_8q_v018_signal(revenue, assetsavg):
    return _clean(_mean(_safe_div(revenue, (assetsavg - _mean(assetsavg, 8)).abs() + 1.0), 8))
def cg_f066_asset_turnover_core18_mean_8q_v019_signal(revenue, assetsavg):
    return _clean(_mean(_safe_div(revenue, assetsavg).abs(), 8))
def cg_f066_asset_turnover_core19_mean_8q_v020_signal(revenue, assetsavg):
    return _clean(_mean(_safe_div(revenue, assetsavg * 0.5 + 1.0), 8))

# core20-29: z 8q
def cg_f066_asset_turnover_core20_z_8q_v021_signal(revenue, assetsavg):
    return _clean(_z(revenue, 8))
def cg_f066_asset_turnover_core21_z_8q_v022_signal(revenue, assetsavg):
    return _clean(_z(_safe_div(revenue, assetsavg), 8))
def cg_f066_asset_turnover_core22_z_8q_v023_signal(revenue, assetsavg):
    return _clean(_z(assetsavg, 8))
def cg_f066_asset_turnover_core23_z_8q_v024_signal(revenue, assetsavg):
    return _clean(_z(_safe_div(revenue, assetsavg.abs() + 1.0), 8))
def cg_f066_asset_turnover_core24_z_8q_v025_signal(revenue, assetsavg):
    return _clean(_z(revenue - _mean(revenue, 8), 8))
def cg_f066_asset_turnover_core25_z_8q_v026_signal(revenue, assetsavg):
    return _clean(_z(assetsavg - _mean(assetsavg, 8), 8))
def cg_f066_asset_turnover_core26_z_8q_v027_signal(revenue, assetsavg):
    return _clean(_z(_safe_div(revenue - _mean(revenue, 8), assetsavg.abs() + 1.0), 8))
def cg_f066_asset_turnover_core27_z_8q_v028_signal(revenue, assetsavg):
    return _clean(_z(_safe_div(revenue, (assetsavg - _mean(assetsavg, 8)).abs() + 1.0), 8))
def cg_f066_asset_turnover_core28_z_8q_v029_signal(revenue, assetsavg):
    return _clean(_z(_safe_div(revenue, assetsavg).abs(), 8))
def cg_f066_asset_turnover_core29_z_8q_v030_signal(revenue, assetsavg):
    return _clean(_z(_safe_div(revenue, assetsavg * 0.5 + 1.0), 8))

# core30-39: z 20q
def cg_f066_asset_turnover_core30_z_20q_v031_signal(revenue, assetsavg):
    return _clean(_z(revenue, 20))
def cg_f066_asset_turnover_core31_z_20q_v032_signal(revenue, assetsavg):
    return _clean(_z(_safe_div(revenue, assetsavg), 20))
def cg_f066_asset_turnover_core32_z_20q_v033_signal(revenue, assetsavg):
    return _clean(_z(assetsavg, 20))
def cg_f066_asset_turnover_core33_z_20q_v034_signal(revenue, assetsavg):
    return _clean(_z(_safe_div(revenue, assetsavg.abs() + 1.0), 20))
def cg_f066_asset_turnover_core34_z_20q_v035_signal(revenue, assetsavg):
    return _clean(_z(revenue - _mean(revenue, 20), 20))
def cg_f066_asset_turnover_core35_z_20q_v036_signal(revenue, assetsavg):
    return _clean(_z(assetsavg - _mean(assetsavg, 20), 20))
def cg_f066_asset_turnover_core36_z_20q_v037_signal(revenue, assetsavg):
    return _clean(_z(_safe_div(revenue - _mean(revenue, 20), assetsavg.abs() + 1.0), 20))
def cg_f066_asset_turnover_core37_z_20q_v038_signal(revenue, assetsavg):
    return _clean(_z(_safe_div(revenue, (assetsavg - _mean(assetsavg, 20)).abs() + 1.0), 20))
def cg_f066_asset_turnover_core38_z_20q_v039_signal(revenue, assetsavg):
    return _clean(_z(_safe_div(revenue, assetsavg).abs(), 20))
def cg_f066_asset_turnover_core39_z_20q_v040_signal(revenue, assetsavg):
    return _clean(_z(_safe_div(revenue, assetsavg * 0.5 + 1.0), 20))

# core40-49: rank 8q
def cg_f066_asset_turnover_core40_rank_8q_v041_signal(revenue, assetsavg):
    return _clean(_rank(revenue, 8))
def cg_f066_asset_turnover_core41_rank_8q_v042_signal(revenue, assetsavg):
    return _clean(_rank(_safe_div(revenue, assetsavg), 8))
def cg_f066_asset_turnover_core42_rank_8q_v043_signal(revenue, assetsavg):
    return _clean(_rank(assetsavg, 8))
def cg_f066_asset_turnover_core43_rank_8q_v044_signal(revenue, assetsavg):
    return _clean(_rank(_safe_div(revenue, assetsavg.abs() + 1.0), 8))
def cg_f066_asset_turnover_core44_rank_8q_v045_signal(revenue, assetsavg):
    return _clean(_rank(revenue - _mean(revenue, 8), 8))
def cg_f066_asset_turnover_core45_rank_8q_v046_signal(revenue, assetsavg):
    return _clean(_rank(assetsavg - _mean(assetsavg, 8), 8))
def cg_f066_asset_turnover_core46_rank_8q_v047_signal(revenue, assetsavg):
    return _clean(_rank(_safe_div(revenue - _mean(revenue, 8), assetsavg.abs() + 1.0), 8))
def cg_f066_asset_turnover_core47_rank_8q_v048_signal(revenue, assetsavg):
    return _clean(_rank(_safe_div(revenue, (assetsavg - _mean(assetsavg, 8)).abs() + 1.0), 8))
def cg_f066_asset_turnover_core48_rank_8q_v049_signal(revenue, assetsavg):
    return _clean(_rank(_safe_div(revenue, assetsavg).abs(), 8))
def cg_f066_asset_turnover_core49_rank_8q_v050_signal(revenue, assetsavg):
    return _clean(_rank(_safe_div(revenue, assetsavg * 0.5 + 1.0), 8))

# core50-59: rank 20q
def cg_f066_asset_turnover_core50_rank_20q_v051_signal(revenue, assetsavg):
    return _clean(_rank(revenue, 20))
def cg_f066_asset_turnover_core51_rank_20q_v052_signal(revenue, assetsavg):
    return _clean(_rank(_safe_div(revenue, assetsavg), 20))
def cg_f066_asset_turnover_core52_rank_20q_v053_signal(revenue, assetsavg):
    return _clean(_rank(assetsavg, 20))
def cg_f066_asset_turnover_core53_rank_20q_v054_signal(revenue, assetsavg):
    return _clean(_rank(_safe_div(revenue, assetsavg.abs() + 1.0), 20))
def cg_f066_asset_turnover_core54_rank_20q_v055_signal(revenue, assetsavg):
    return _clean(_rank(revenue - _mean(revenue, 20), 20))
def cg_f066_asset_turnover_core55_rank_20q_v056_signal(revenue, assetsavg):
    return _clean(_rank(assetsavg - _mean(assetsavg, 20), 20))
def cg_f066_asset_turnover_core56_rank_20q_v057_signal(revenue, assetsavg):
    return _clean(_rank(_safe_div(revenue - _mean(revenue, 20), assetsavg.abs() + 1.0), 20))
def cg_f066_asset_turnover_core57_rank_20q_v058_signal(revenue, assetsavg):
    return _clean(_rank(_safe_div(revenue, (assetsavg - _mean(assetsavg, 20)).abs() + 1.0), 20))
def cg_f066_asset_turnover_core58_rank_20q_v059_signal(revenue, assetsavg):
    return _clean(_rank(_safe_div(revenue, assetsavg).abs(), 20))
def cg_f066_asset_turnover_core59_rank_20q_v060_signal(revenue, assetsavg):
    return _clean(_rank(_safe_div(revenue, assetsavg * 0.5 + 1.0), 20))

# core60-69: pct 1q
def cg_f066_asset_turnover_core60_pct_1q_v061_signal(revenue, assetsavg):
    return _clean(_pct_change(revenue, 1))
def cg_f066_asset_turnover_core61_pct_1q_v062_signal(revenue, assetsavg):
    return _clean(_pct_change(_safe_div(revenue, assetsavg), 1))
def cg_f066_asset_turnover_core62_pct_1q_v063_signal(revenue, assetsavg):
    return _clean(_pct_change(assetsavg, 1))
def cg_f066_asset_turnover_core63_pct_1q_v064_signal(revenue, assetsavg):
    return _clean(_pct_change(_safe_div(revenue, assetsavg.abs() + 1.0), 1))
def cg_f066_asset_turnover_core64_pct_1q_v065_signal(revenue, assetsavg):
    return _clean(_pct_change(revenue - _mean(revenue, 4), 1))
def cg_f066_asset_turnover_core65_pct_1q_v066_signal(revenue, assetsavg):
    return _clean(_pct_change(assetsavg - _mean(assetsavg, 4), 1))
def cg_f066_asset_turnover_core66_pct_1q_v067_signal(revenue, assetsavg):
    return _clean(_pct_change(_safe_div(revenue - _mean(revenue, 4), assetsavg.abs() + 1.0), 1))
def cg_f066_asset_turnover_core67_pct_1q_v068_signal(revenue, assetsavg):
    return _clean(_pct_change(_safe_div(revenue, (assetsavg - _mean(assetsavg, 4)).abs() + 1.0), 1))
def cg_f066_asset_turnover_core68_pct_1q_v069_signal(revenue, assetsavg):
    return _clean(_pct_change(_safe_div(revenue, assetsavg).abs(), 1))
def cg_f066_asset_turnover_core69_pct_1q_v070_signal(revenue, assetsavg):
    return _clean(_pct_change(_safe_div(revenue, assetsavg * 0.5 + 1.0), 1))

# core70-74: pct 4q
def cg_f066_asset_turnover_core70_pct_4q_v071_signal(revenue, assetsavg):
    return _clean(_pct_change(revenue, 4))
def cg_f066_asset_turnover_core71_pct_4q_v072_signal(revenue, assetsavg):
    return _clean(_pct_change(_safe_div(revenue, assetsavg), 4))
def cg_f066_asset_turnover_core72_pct_4q_v073_signal(revenue, assetsavg):
    return _clean(_pct_change(assetsavg, 4))
def cg_f066_asset_turnover_core73_pct_4q_v074_signal(revenue, assetsavg):
    return _clean(_pct_change(_safe_div(revenue, assetsavg.abs() + 1.0), 4))
def cg_f066_asset_turnover_core74_pct_4q_v075_signal(revenue, assetsavg):
    return _clean(_pct_change(revenue - _mean(revenue, 4), 4))
