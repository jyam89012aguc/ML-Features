import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core00-09: mean 4q
def cg_f032_shares_diluted_core00_mean_4q_v001_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_mean(sharesdil, 4))
def cg_f032_shares_diluted_core01_mean_4q_v002_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_mean(_safe_div(sharesdil, assets), 4))
def cg_f032_shares_diluted_core02_mean_4q_v003_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_mean(_safe_div(sharesdil, revenue), 4))
def cg_f032_shares_diluted_core03_mean_4q_v004_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_mean(_safe_div(sharesdil, marketcap), 4))
def cg_f032_shares_diluted_core04_mean_4q_v005_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_mean(_safe_div(sharesdil, netinc.abs() + 1.0), 4))
def cg_f032_shares_diluted_core05_mean_4q_v006_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_mean(_safe_div(sharesdil, equity.abs() + 1.0), 4))
def cg_f032_shares_diluted_core06_mean_4q_v007_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_mean(_safe_div(sharesdil - sharesbas, sharesbas.abs() + 1.0), 4))
def cg_f032_shares_diluted_core07_mean_4q_v008_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_mean(_safe_div(sharesdil, opex.abs() + 1.0), 4))
def cg_f032_shares_diluted_core08_mean_4q_v009_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_mean(_pct_change(sharesdil, 4), 4))
def cg_f032_shares_diluted_core09_mean_4q_v010_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_mean(_log(sharesdil.clip(lower=1.0)), 4))

# core10-19: mean 8q
def cg_f032_shares_diluted_core10_mean_8q_v011_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_mean(sharesdil, 8))
def cg_f032_shares_diluted_core11_mean_8q_v012_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_mean(_safe_div(sharesdil, assets), 8))
def cg_f032_shares_diluted_core12_mean_8q_v013_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_mean(_safe_div(sharesdil, revenue), 8))
def cg_f032_shares_diluted_core13_mean_8q_v014_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_mean(_safe_div(sharesdil, marketcap), 8))
def cg_f032_shares_diluted_core14_mean_8q_v015_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_mean(_safe_div(sharesdil, netinc.abs() + 1.0), 8))
def cg_f032_shares_diluted_core15_mean_8q_v016_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_mean(_safe_div(sharesdil, equity.abs() + 1.0), 8))
def cg_f032_shares_diluted_core16_mean_8q_v017_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_mean(_safe_div(sharesdil - sharesbas, sharesbas.abs() + 1.0), 8))
def cg_f032_shares_diluted_core17_mean_8q_v018_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_mean(_safe_div(sharesdil, opex.abs() + 1.0), 8))
def cg_f032_shares_diluted_core18_mean_8q_v019_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_mean(_pct_change(sharesdil, 4), 8))
def cg_f032_shares_diluted_core19_mean_8q_v020_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_mean(_log(sharesdil.clip(lower=1.0)), 8))

# core20-29: z 8q
def cg_f032_shares_diluted_core20_z_8q_v021_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_z(sharesdil, 8))
def cg_f032_shares_diluted_core21_z_8q_v022_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_z(_safe_div(sharesdil, assets), 8))
def cg_f032_shares_diluted_core22_z_8q_v023_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_z(_safe_div(sharesdil, revenue), 8))
def cg_f032_shares_diluted_core23_z_8q_v024_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_z(_safe_div(sharesdil, marketcap), 8))
def cg_f032_shares_diluted_core24_z_8q_v025_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_z(_safe_div(sharesdil, netinc.abs() + 1.0), 8))
def cg_f032_shares_diluted_core25_z_8q_v026_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_z(_safe_div(sharesdil, equity.abs() + 1.0), 8))
def cg_f032_shares_diluted_core26_z_8q_v027_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_z(_safe_div(sharesdil - sharesbas, sharesbas.abs() + 1.0), 8))
def cg_f032_shares_diluted_core27_z_8q_v028_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_z(_safe_div(sharesdil, opex.abs() + 1.0), 8))
def cg_f032_shares_diluted_core28_z_8q_v029_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_z(_pct_change(sharesdil, 4), 8))
def cg_f032_shares_diluted_core29_z_8q_v030_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_z(_log(sharesdil.clip(lower=1.0)), 8))

# core30-39: z 20q
def cg_f032_shares_diluted_core30_z_20q_v031_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_z(sharesdil, 20))
def cg_f032_shares_diluted_core31_z_20q_v032_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_z(_safe_div(sharesdil, assets), 20))
def cg_f032_shares_diluted_core32_z_20q_v033_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_z(_safe_div(sharesdil, revenue), 20))
def cg_f032_shares_diluted_core33_z_20q_v034_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_z(_safe_div(sharesdil, marketcap), 20))
def cg_f032_shares_diluted_core34_z_20q_v035_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_z(_safe_div(sharesdil, netinc.abs() + 1.0), 20))
def cg_f032_shares_diluted_core35_z_20q_v036_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_z(_safe_div(sharesdil, equity.abs() + 1.0), 20))
def cg_f032_shares_diluted_core36_z_20q_v037_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_z(_safe_div(sharesdil - sharesbas, sharesbas.abs() + 1.0), 20))
def cg_f032_shares_diluted_core37_z_20q_v038_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_z(_safe_div(sharesdil, opex.abs() + 1.0), 20))
def cg_f032_shares_diluted_core38_z_20q_v039_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_z(_pct_change(sharesdil, 4), 20))
def cg_f032_shares_diluted_core39_z_20q_v040_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_z(_log(sharesdil.clip(lower=1.0)), 20))

# core40-49: rank 12q
def cg_f032_shares_diluted_core40_rank_12q_v041_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_rank(sharesdil, 12))
def cg_f032_shares_diluted_core41_rank_12q_v042_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_rank(_safe_div(sharesdil, assets), 12))
def cg_f032_shares_diluted_core42_rank_12q_v043_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_rank(_safe_div(sharesdil, revenue), 12))
def cg_f032_shares_diluted_core43_rank_12q_v044_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_rank(_safe_div(sharesdil, marketcap), 12))
def cg_f032_shares_diluted_core44_rank_12q_v045_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_rank(_safe_div(sharesdil, netinc.abs() + 1.0), 12))
def cg_f032_shares_diluted_core45_rank_12q_v046_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_rank(_safe_div(sharesdil, equity.abs() + 1.0), 12))
def cg_f032_shares_diluted_core46_rank_12q_v047_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_rank(_safe_div(sharesdil - sharesbas, sharesbas.abs() + 1.0), 12))
def cg_f032_shares_diluted_core47_rank_12q_v048_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_rank(_safe_div(sharesdil, opex.abs() + 1.0), 12))
def cg_f032_shares_diluted_core48_rank_12q_v049_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_rank(_pct_change(sharesdil, 4), 12))
def cg_f032_shares_diluted_core49_rank_12q_v050_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_rank(_log(sharesdil.clip(lower=1.0)), 12))

# core50-59: rank 20q
def cg_f032_shares_diluted_core50_rank_20q_v051_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_rank(sharesdil, 20))
def cg_f032_shares_diluted_core51_rank_20q_v052_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_rank(_safe_div(sharesdil, assets), 20))
def cg_f032_shares_diluted_core52_rank_20q_v053_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_rank(_safe_div(sharesdil, revenue), 20))
def cg_f032_shares_diluted_core53_rank_20q_v054_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_rank(_safe_div(sharesdil, marketcap), 20))
def cg_f032_shares_diluted_core54_rank_20q_v055_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_rank(_safe_div(sharesdil, netinc.abs() + 1.0), 20))
def cg_f032_shares_diluted_core55_rank_20q_v056_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_rank(_safe_div(sharesdil, equity.abs() + 1.0), 20))
def cg_f032_shares_diluted_core56_rank_20q_v057_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_rank(_safe_div(sharesdil - sharesbas, sharesbas.abs() + 1.0), 20))
def cg_f032_shares_diluted_core57_rank_20q_v058_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_rank(_safe_div(sharesdil, opex.abs() + 1.0), 20))
def cg_f032_shares_diluted_core58_rank_20q_v059_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_rank(_pct_change(sharesdil, 4), 20))
def cg_f032_shares_diluted_core59_rank_20q_v060_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_rank(_log(sharesdil.clip(lower=1.0)), 20))

# core60-69: pct 1q
def cg_f032_shares_diluted_core60_pct_1q_v061_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_pct_change(sharesdil, 1))
def cg_f032_shares_diluted_core61_pct_1q_v062_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_pct_change(_safe_div(sharesdil, assets), 1))
def cg_f032_shares_diluted_core62_pct_1q_v063_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_pct_change(_safe_div(sharesdil, revenue), 1))
def cg_f032_shares_diluted_core63_pct_1q_v064_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_pct_change(_safe_div(sharesdil, marketcap), 1))
def cg_f032_shares_diluted_core64_pct_1q_v065_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_pct_change(_safe_div(sharesdil, netinc.abs() + 1.0), 1))
def cg_f032_shares_diluted_core65_pct_1q_v066_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_pct_change(_safe_div(sharesdil, equity.abs() + 1.0), 1))
def cg_f032_shares_diluted_core66_pct_1q_v067_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_pct_change(_safe_div(sharesdil - sharesbas, sharesbas.abs() + 1.0), 1))
def cg_f032_shares_diluted_core67_pct_1q_v068_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_pct_change(_safe_div(sharesdil, opex.abs() + 1.0), 1))
def cg_f032_shares_diluted_core68_pct_1q_v069_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_pct_change(_pct_change(sharesdil, 4), 1))
def cg_f032_shares_diluted_core69_pct_1q_v070_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_pct_change(_log(sharesdil.clip(lower=1.0)), 1))

# core70-74: pct 4q
def cg_f032_shares_diluted_core70_pct_4q_v071_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_pct_change(sharesdil, 4))
def cg_f032_shares_diluted_core71_pct_4q_v072_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_pct_change(_safe_div(sharesdil, assets), 4))
def cg_f032_shares_diluted_core72_pct_4q_v073_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_pct_change(_safe_div(sharesdil, revenue), 4))
def cg_f032_shares_diluted_core73_pct_4q_v074_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_pct_change(_safe_div(sharesdil, marketcap), 4))
def cg_f032_shares_diluted_core74_pct_4q_v075_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_pct_change(_safe_div(sharesdil, netinc.abs() + 1.0), 4))
