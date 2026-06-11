import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core00-09: mean 4q
def cg_f043_ppne_footprint_core00_mean_4q_v001_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_mean(ppnenet, 4))
def cg_f043_ppne_footprint_core01_mean_4q_v002_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_mean(ppneg, 4))
def cg_f043_ppne_footprint_core02_mean_4q_v003_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_mean(_safe_div(ppnenet, assets), 4))
def cg_f043_ppne_footprint_core03_mean_4q_v004_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_mean(_safe_div(ppneg, assets), 4))
def cg_f043_ppne_footprint_core04_mean_4q_v005_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_mean(_safe_div(ppnenet, revenue), 4))
def cg_f043_ppne_footprint_core05_mean_4q_v006_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_mean(_safe_div(ppnenet, equity.abs() + 1.0), 4))
def cg_f043_ppne_footprint_core06_mean_4q_v007_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_mean(_safe_div(ppnenet, ppneg), 4))
def cg_f043_ppne_footprint_core07_mean_4q_v008_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_mean(_pct_change(ppnenet, 4), 4))
def cg_f043_ppne_footprint_core08_mean_4q_v009_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_mean(_safe_div(ppnenet, opex.abs() + 1.0), 4))
def cg_f043_ppne_footprint_core09_mean_4q_v010_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_mean(_log(ppnenet.clip(lower=1.0)), 4))

# core10-19: mean 8q
def cg_f043_ppne_footprint_core10_mean_8q_v011_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_mean(ppnenet, 8))
def cg_f043_ppne_footprint_core11_mean_8q_v012_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_mean(ppneg, 8))
def cg_f043_ppne_footprint_core12_mean_8q_v013_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_mean(_safe_div(ppnenet, assets), 8))
def cg_f043_ppne_footprint_core13_mean_8q_v014_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_mean(_safe_div(ppneg, assets), 8))
def cg_f043_ppne_footprint_core14_mean_8q_v015_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_mean(_safe_div(ppnenet, revenue), 8))
def cg_f043_ppne_footprint_core15_mean_8q_v016_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_mean(_safe_div(ppnenet, equity.abs() + 1.0), 8))
def cg_f043_ppne_footprint_core16_mean_8q_v017_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_mean(_safe_div(ppnenet, ppneg), 8))
def cg_f043_ppne_footprint_core17_mean_8q_v018_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_mean(_pct_change(ppnenet, 4), 8))
def cg_f043_ppne_footprint_core18_mean_8q_v019_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_mean(_safe_div(ppnenet, opex.abs() + 1.0), 8))
def cg_f043_ppne_footprint_core19_mean_8q_v020_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_mean(_log(ppnenet.clip(lower=1.0)), 8))

# core20-29: z 8q
def cg_f043_ppne_footprint_core20_z_8q_v021_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_z(ppnenet, 8))
def cg_f043_ppne_footprint_core21_z_8q_v022_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_z(ppneg, 8))
def cg_f043_ppne_footprint_core22_z_8q_v023_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_z(_safe_div(ppnenet, assets), 8))
def cg_f043_ppne_footprint_core23_z_8q_v024_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_z(_safe_div(ppneg, assets), 8))
def cg_f043_ppne_footprint_core24_z_8q_v025_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_z(_safe_div(ppnenet, revenue), 8))
def cg_f043_ppne_footprint_core25_z_8q_v026_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_z(_safe_div(ppnenet, equity.abs() + 1.0), 8))
def cg_f043_ppne_footprint_core26_z_8q_v027_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_z(_safe_div(ppnenet, ppneg), 8))
def cg_f043_ppne_footprint_core27_z_8q_v028_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_z(_pct_change(ppnenet, 4), 8))
def cg_f043_ppne_footprint_core28_z_8q_v029_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_z(_safe_div(ppnenet, opex.abs() + 1.0), 8))
def cg_f043_ppne_footprint_core29_z_8q_v030_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_z(_log(ppnenet.clip(lower=1.0)), 8))

# core30-39: z 20q
def cg_f043_ppne_footprint_core30_z_20q_v031_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_z(ppnenet, 20))
def cg_f043_ppne_footprint_core31_z_20q_v032_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_z(ppneg, 20))
def cg_f043_ppne_footprint_core32_z_20q_v033_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_z(_safe_div(ppnenet, assets), 20))
def cg_f043_ppne_footprint_core33_z_20q_v034_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_z(_safe_div(ppneg, assets), 20))
def cg_f043_ppne_footprint_core34_z_20q_v035_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_z(_safe_div(ppnenet, revenue), 20))
def cg_f043_ppne_footprint_core35_z_20q_v036_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_z(_safe_div(ppnenet, equity.abs() + 1.0), 20))
def cg_f043_ppne_footprint_core36_z_20q_v037_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_z(_safe_div(ppnenet, ppneg), 20))
def cg_f043_ppne_footprint_core37_z_20q_v038_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_z(_pct_change(ppnenet, 4), 20))
def cg_f043_ppne_footprint_core38_z_20q_v039_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_z(_safe_div(ppnenet, opex.abs() + 1.0), 20))
def cg_f043_ppne_footprint_core39_z_20q_v040_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_z(_log(ppnenet.clip(lower=1.0)), 20))

# core40-49: rank 12q
def cg_f043_ppne_footprint_core40_rank_12q_v041_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_rank(ppnenet, 12))
def cg_f043_ppne_footprint_core41_rank_12q_v042_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_rank(ppneg, 12))
def cg_f043_ppne_footprint_core42_rank_12q_v043_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_rank(_safe_div(ppnenet, assets), 12))
def cg_f043_ppne_footprint_core43_rank_12q_v044_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_rank(_safe_div(ppneg, assets), 12))
def cg_f043_ppne_footprint_core44_rank_12q_v045_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_rank(_safe_div(ppnenet, revenue), 12))
def cg_f043_ppne_footprint_core45_rank_12q_v046_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_rank(_safe_div(ppnenet, equity.abs() + 1.0), 12))
def cg_f043_ppne_footprint_core46_rank_12q_v047_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_rank(_safe_div(ppnenet, ppneg), 12))
def cg_f043_ppne_footprint_core47_rank_12q_v048_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_rank(_pct_change(ppnenet, 4), 12))
def cg_f043_ppne_footprint_core48_rank_12q_v049_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_rank(_safe_div(ppnenet, opex.abs() + 1.0), 12))
def cg_f043_ppne_footprint_core49_rank_12q_v050_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_rank(_log(ppnenet.clip(lower=1.0)), 12))

# core50-59: rank 20q
def cg_f043_ppne_footprint_core50_rank_20q_v051_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_rank(ppnenet, 20))
def cg_f043_ppne_footprint_core51_rank_20q_v052_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_rank(ppneg, 20))
def cg_f043_ppne_footprint_core52_rank_20q_v053_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_rank(_safe_div(ppnenet, assets), 20))
def cg_f043_ppne_footprint_core53_rank_20q_v054_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_rank(_safe_div(ppneg, assets), 20))
def cg_f043_ppne_footprint_core54_rank_20q_v055_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_rank(_safe_div(ppnenet, revenue), 20))
def cg_f043_ppne_footprint_core55_rank_20q_v056_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_rank(_safe_div(ppnenet, equity.abs() + 1.0), 20))
def cg_f043_ppne_footprint_core56_rank_20q_v057_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_rank(_safe_div(ppnenet, ppneg), 20))
def cg_f043_ppne_footprint_core57_rank_20q_v058_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_rank(_pct_change(ppnenet, 4), 20))
def cg_f043_ppne_footprint_core58_rank_20q_v059_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_rank(_safe_div(ppnenet, opex.abs() + 1.0), 20))
def cg_f043_ppne_footprint_core59_rank_20q_v060_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_rank(_log(ppnenet.clip(lower=1.0)), 20))

# core60-69: pct 1q
def cg_f043_ppne_footprint_core60_pct_1q_v061_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_pct_change(ppnenet, 1))
def cg_f043_ppne_footprint_core61_pct_1q_v062_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_pct_change(ppneg, 1))
def cg_f043_ppne_footprint_core62_pct_1q_v063_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_pct_change(_safe_div(ppnenet, assets), 1))
def cg_f043_ppne_footprint_core63_pct_1q_v064_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_pct_change(_safe_div(ppneg, assets), 1))
def cg_f043_ppne_footprint_core64_pct_1q_v065_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_pct_change(_safe_div(ppnenet, revenue), 1))
def cg_f043_ppne_footprint_core65_pct_1q_v066_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_pct_change(_safe_div(ppnenet, equity.abs() + 1.0), 1))
def cg_f043_ppne_footprint_core66_pct_1q_v067_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_pct_change(_safe_div(ppnenet, ppneg), 1))
def cg_f043_ppne_footprint_core67_pct_1q_v068_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_pct_change(_pct_change(ppnenet, 4), 1))
def cg_f043_ppne_footprint_core68_pct_1q_v069_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_pct_change(_safe_div(ppnenet, opex.abs() + 1.0), 1))
def cg_f043_ppne_footprint_core69_pct_1q_v070_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_pct_change(_log(ppnenet.clip(lower=1.0)), 1))

# core70-74: pct 4q
def cg_f043_ppne_footprint_core70_pct_4q_v071_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_pct_change(ppnenet, 4))
def cg_f043_ppne_footprint_core71_pct_4q_v072_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_pct_change(ppneg, 4))
def cg_f043_ppne_footprint_core72_pct_4q_v073_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_pct_change(_safe_div(ppnenet, assets), 4))
def cg_f043_ppne_footprint_core73_pct_4q_v074_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_pct_change(_safe_div(ppneg, assets), 4))
def cg_f043_ppne_footprint_core74_pct_4q_v075_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_pct_change(_safe_div(ppnenet, revenue), 4))
