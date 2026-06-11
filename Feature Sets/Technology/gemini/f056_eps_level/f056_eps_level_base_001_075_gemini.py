import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core00-09: mean 4q
def cg_f056_eps_level_core00_mean_4q_v001_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_mean(eps, 4))
def cg_f056_eps_level_core01_mean_4q_v002_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_mean(epsdil, 4))
def cg_f056_eps_level_core02_mean_4q_v003_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_mean(_safe_div(eps, revenue), 4))
def cg_f056_eps_level_core03_mean_4q_v004_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_mean(_safe_div(eps, assets), 4))
def cg_f056_eps_level_core04_mean_4q_v005_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_mean(_safe_div(eps, marketcap), 4))
def cg_f056_eps_level_core05_mean_4q_v006_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_mean(_safe_div(eps, equity.abs() + 1.0), 4))
def cg_f056_eps_level_core06_mean_4q_v007_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_mean(_safe_div(eps - epsdil, eps.abs() + 1e-9), 4))
def cg_f056_eps_level_core07_mean_4q_v008_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_mean(_diff(eps, 4), 4))
def cg_f056_eps_level_core08_mean_4q_v009_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_mean(_diff(epsdil, 4), 4))
def cg_f056_eps_level_core09_mean_4q_v010_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_mean(_safe_div(eps, sharesbas), 4))

# core10-19: mean 8q
def cg_f056_eps_level_core10_mean_8q_v011_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_mean(eps, 8))
def cg_f056_eps_level_core11_mean_8q_v012_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_mean(epsdil, 8))
def cg_f056_eps_level_core12_mean_8q_v013_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_mean(_safe_div(eps, revenue), 8))
def cg_f056_eps_level_core13_mean_8q_v014_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_mean(_safe_div(eps, assets), 8))
def cg_f056_eps_level_core14_mean_8q_v015_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_mean(_safe_div(eps, marketcap), 8))
def cg_f056_eps_level_core15_mean_8q_v016_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_mean(_safe_div(eps, equity.abs() + 1.0), 8))
def cg_f056_eps_level_core16_mean_8q_v017_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_mean(_safe_div(eps - epsdil, eps.abs() + 1e-9), 8))
def cg_f056_eps_level_core17_mean_8q_v018_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_mean(_diff(eps, 4), 8))
def cg_f056_eps_level_core18_mean_8q_v019_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_mean(_diff(epsdil, 4), 8))
def cg_f056_eps_level_core19_mean_8q_v020_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_mean(_safe_div(eps, sharesbas), 8))

# core20-29: z 8q
def cg_f056_eps_level_core20_z_8q_v021_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_z(eps, 8))
def cg_f056_eps_level_core21_z_8q_v022_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_z(epsdil, 8))
def cg_f056_eps_level_core22_z_8q_v023_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_z(_safe_div(eps, revenue), 8))
def cg_f056_eps_level_core23_z_8q_v024_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_z(_safe_div(eps, assets), 8))
def cg_f056_eps_level_core24_z_8q_v025_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_z(_safe_div(eps, marketcap), 8))
def cg_f056_eps_level_core25_z_8q_v026_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_z(_safe_div(eps, equity.abs() + 1.0), 8))
def cg_f056_eps_level_core26_z_8q_v027_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_z(_safe_div(eps - epsdil, eps.abs() + 1e-9), 8))
def cg_f056_eps_level_core27_z_8q_v028_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_z(_diff(eps, 4), 8))
def cg_f056_eps_level_core28_z_8q_v029_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_z(_diff(epsdil, 4), 8))
def cg_f056_eps_level_core29_z_8q_v030_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_z(_safe_div(eps, sharesbas), 8))

# core30-39: z 20q
def cg_f056_eps_level_core30_z_20q_v031_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_z(eps, 20))
def cg_f056_eps_level_core31_z_20q_v032_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_z(epsdil, 20))
def cg_f056_eps_level_core32_z_20q_v033_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_z(_safe_div(eps, revenue), 20))
def cg_f056_eps_level_core33_z_20q_v034_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_z(_safe_div(eps, assets), 20))
def cg_f056_eps_level_core34_z_20q_v035_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_z(_safe_div(eps, marketcap), 20))
def cg_f056_eps_level_core35_z_20q_v036_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_z(_safe_div(eps, equity.abs() + 1.0), 20))
def cg_f056_eps_level_core36_z_20q_v037_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_z(_safe_div(eps - epsdil, eps.abs() + 1e-9), 20))
def cg_f056_eps_level_core37_z_20q_v038_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_z(_diff(eps, 4), 20))
def cg_f056_eps_level_core38_z_20q_v039_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_z(_diff(epsdil, 4), 20))
def cg_f056_eps_level_core39_z_20q_v040_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_z(_safe_div(eps, sharesbas), 20))

# core40-49: rank 12q
def cg_f056_eps_level_core40_rank_12q_v041_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_rank(eps, 12))
def cg_f056_eps_level_core41_rank_12q_v042_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_rank(epsdil, 12))
def cg_f056_eps_level_core42_rank_12q_v043_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_rank(_safe_div(eps, revenue), 12))
def cg_f056_eps_level_core43_rank_12q_v044_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_rank(_safe_div(eps, assets), 12))
def cg_f056_eps_level_core44_rank_12q_v045_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_rank(_safe_div(eps, marketcap), 12))
def cg_f056_eps_level_core45_rank_12q_v046_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_rank(_safe_div(eps, equity.abs() + 1.0), 12))
def cg_f056_eps_level_core46_rank_12q_v047_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_rank(_safe_div(eps - epsdil, eps.abs() + 1e-9), 12))
def cg_f056_eps_level_core47_rank_12q_v048_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_rank(_diff(eps, 4), 12))
def cg_f056_eps_level_core48_rank_12q_v049_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_rank(_diff(epsdil, 4), 12))
def cg_f056_eps_level_core49_rank_12q_v050_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_rank(_safe_div(eps, sharesbas), 12))

# core50-59: rank 20q
def cg_f056_eps_level_core50_rank_20q_v051_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_rank(eps, 20))
def cg_f056_eps_level_core51_rank_20q_v052_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_rank(epsdil, 20))
def cg_f056_eps_level_core52_rank_20q_v053_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_rank(_safe_div(eps, revenue), 20))
def cg_f056_eps_level_core53_rank_20q_v054_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_rank(_safe_div(eps, assets), 20))
def cg_f056_eps_level_core54_rank_20q_v055_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_rank(_safe_div(eps, marketcap), 20))
def cg_f056_eps_level_core55_rank_20q_v056_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_rank(_safe_div(eps, equity.abs() + 1.0), 20))
def cg_f056_eps_level_core56_rank_20q_v057_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_rank(_safe_div(eps - epsdil, eps.abs() + 1e-9), 20))
def cg_f056_eps_level_core57_rank_20q_v058_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_rank(_diff(eps, 4), 20))
def cg_f056_eps_level_core58_rank_20q_v059_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_rank(_diff(epsdil, 4), 20))
def cg_f056_eps_level_core59_rank_20q_v060_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_rank(_safe_div(eps, sharesbas), 20))

# core60-69: pct 1q
def cg_f056_eps_level_core60_pct_1q_v061_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_pct_change(eps, 1))
def cg_f056_eps_level_core61_pct_1q_v062_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_pct_change(epsdil, 1))
def cg_f056_eps_level_core62_pct_1q_v063_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_pct_change(_safe_div(eps, revenue), 1))
def cg_f056_eps_level_core63_pct_1q_v064_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_pct_change(_safe_div(eps, assets), 1))
def cg_f056_eps_level_core64_pct_1q_v065_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_pct_change(_safe_div(eps, marketcap), 1))
def cg_f056_eps_level_core65_pct_1q_v066_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_pct_change(_safe_div(eps, equity.abs() + 1.0), 1))
def cg_f056_eps_level_core66_pct_1q_v067_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_pct_change(_safe_div(eps - epsdil, eps.abs() + 1e-9), 1))
def cg_f056_eps_level_core67_pct_1q_v068_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_pct_change(_diff(eps, 4), 1))
def cg_f056_eps_level_core68_pct_1q_v069_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_pct_change(_diff(epsdil, 4), 1))
def cg_f056_eps_level_core69_pct_1q_v070_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_pct_change(_safe_div(eps, sharesbas), 1))

# core70-74: pct 4q
def cg_f056_eps_level_core70_pct_4q_v071_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_pct_change(eps, 4))
def cg_f056_eps_level_core71_pct_4q_v072_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_pct_change(epsdil, 4))
def cg_f056_eps_level_core72_pct_4q_v073_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_pct_change(_safe_div(eps, revenue), 4))
def cg_f056_eps_level_core73_pct_4q_v074_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_pct_change(_safe_div(eps, assets), 4))
def cg_f056_eps_level_core74_pct_4q_v075_signal(eps, epsdil, revenue, assets, marketcap, equity, sharesbas, sharesdil):
    return _clean(_pct_change(_safe_div(eps, marketcap), 4))
