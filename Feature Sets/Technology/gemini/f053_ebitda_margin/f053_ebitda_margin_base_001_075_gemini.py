import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core00-09: mean 4q
def cg_f053_ebitda_margin_core00_mean_4q_v001_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(ebitdamargin, 4))
def cg_f053_ebitda_margin_core01_mean_4q_v002_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_safe_div(ebitda, assets), 4))
def cg_f053_ebitda_margin_core02_mean_4q_v003_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_safe_div(ebitda, marketcap), 4))
def cg_f053_ebitda_margin_core03_mean_4q_v004_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_safe_div(ebitda, equity.abs() + 1.0), 4))
def cg_f053_ebitda_margin_core04_mean_4q_v005_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_safe_div(ebitda, opex.abs() + 1.0), 4))
def cg_f053_ebitda_margin_core05_mean_4q_v006_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_safe_div(ebitda - netinc, revenue), 4))
def cg_f053_ebitda_margin_core06_mean_4q_v007_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_diff(ebitdamargin, 4), 4))
def cg_f053_ebitda_margin_core07_mean_4q_v008_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_pct_change(ebitda, 4), 4))
def cg_f053_ebitda_margin_core08_mean_4q_v009_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_safe_div(ebitdamargin, _std(ebitdamargin, 4) + 1e-9), 4))
def cg_f053_ebitda_margin_core09_mean_4q_v010_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_log(ebitdamargin.clip(lower=0.001) + 1.0), 4))

# core10-19: mean 8q
def cg_f053_ebitda_margin_core10_mean_8q_v011_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(ebitdamargin, 8))
def cg_f053_ebitda_margin_core11_mean_8q_v012_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_safe_div(ebitda, assets), 8))
def cg_f053_ebitda_margin_core12_mean_8q_v013_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_safe_div(ebitda, marketcap), 8))
def cg_f053_ebitda_margin_core13_mean_8q_v014_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_safe_div(ebitda, equity.abs() + 1.0), 8))
def cg_f053_ebitda_margin_core14_mean_8q_v015_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_safe_div(ebitda, opex.abs() + 1.0), 8))
def cg_f053_ebitda_margin_core15_mean_8q_v016_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_safe_div(ebitda - netinc, revenue), 8))
def cg_f053_ebitda_margin_core16_mean_8q_v017_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_diff(ebitdamargin, 4), 8))
def cg_f053_ebitda_margin_core17_mean_8q_v018_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_pct_change(ebitda, 4), 8))
def cg_f053_ebitda_margin_core18_mean_8q_v019_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_safe_div(ebitdamargin, _std(ebitdamargin, 8) + 1e-9), 8))
def cg_f053_ebitda_margin_core19_mean_8q_v020_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_log(ebitdamargin.clip(lower=0.001) + 1.0), 8))

# core20-29: z 8q
def cg_f053_ebitda_margin_core20_z_8q_v021_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(ebitdamargin, 8))
def cg_f053_ebitda_margin_core21_z_8q_v022_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_safe_div(ebitda, assets), 8))
def cg_f053_ebitda_margin_core22_z_8q_v023_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_safe_div(ebitda, marketcap), 8))
def cg_f053_ebitda_margin_core23_z_8q_v024_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_safe_div(ebitda, equity.abs() + 1.0), 8))
def cg_f053_ebitda_margin_core24_z_8q_v025_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_safe_div(ebitda, opex.abs() + 1.0), 8))
def cg_f053_ebitda_margin_core25_z_8q_v026_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_safe_div(ebitda - netinc, revenue), 8))
def cg_f053_ebitda_margin_core26_z_8q_v027_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_diff(ebitdamargin, 4), 8))
def cg_f053_ebitda_margin_core27_z_8q_v028_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_pct_change(ebitda, 4), 8))
def cg_f053_ebitda_margin_core28_z_8q_v029_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_safe_div(ebitdamargin, _std(ebitdamargin, 4) + 1e-9), 8))
def cg_f053_ebitda_margin_core29_z_8q_v030_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_log(ebitdamargin.clip(lower=0.001) + 1.0), 8))

# core30-39: z 20q
def cg_f053_ebitda_margin_core30_z_20q_v031_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(ebitdamargin, 20))
def cg_f053_ebitda_margin_core31_z_20q_v032_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_safe_div(ebitda, assets), 20))
def cg_f053_ebitda_margin_core32_z_20q_v033_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_safe_div(ebitda, marketcap), 20))
def cg_f053_ebitda_margin_core33_z_20q_v034_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_safe_div(ebitda, equity.abs() + 1.0), 20))
def cg_f053_ebitda_margin_core34_z_20q_v035_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_safe_div(ebitda, opex.abs() + 1.0), 20))
def cg_f053_ebitda_margin_core35_z_20q_v036_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_safe_div(ebitda - netinc, revenue), 20))
def cg_f053_ebitda_margin_core36_z_20q_v037_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_diff(ebitdamargin, 4), 20))
def cg_f053_ebitda_margin_core37_z_20q_v038_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_pct_change(ebitda, 4), 20))
def cg_f053_ebitda_margin_core38_z_20q_v039_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_safe_div(ebitdamargin, _std(ebitdamargin, 8) + 1e-9), 20))
def cg_f053_ebitda_margin_core39_z_20q_v040_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_log(ebitdamargin.clip(lower=0.001) + 1.0), 20))

# core40-49: rank 12q
def cg_f053_ebitda_margin_core40_rank_12q_v041_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(ebitdamargin, 12))
def cg_f053_ebitda_margin_core41_rank_12q_v042_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_safe_div(ebitda, assets), 12))
def cg_f053_ebitda_margin_core42_rank_12q_v043_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_safe_div(ebitda, marketcap), 12))
def cg_f053_ebitda_margin_core43_rank_12q_v044_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_safe_div(ebitda, equity.abs() + 1.0), 12))
def cg_f053_ebitda_margin_core44_rank_12q_v045_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_safe_div(ebitda, opex.abs() + 1.0), 12))
def cg_f053_ebitda_margin_core45_rank_12q_v046_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_safe_div(ebitda - netinc, revenue), 12))
def cg_f053_ebitda_margin_core46_rank_12q_v047_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_diff(ebitdamargin, 4), 12))
def cg_f053_ebitda_margin_core47_rank_12q_v048_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_pct_change(ebitda, 4), 12))
def cg_f053_ebitda_margin_core48_rank_12q_v049_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_safe_div(ebitdamargin, _std(ebitdamargin, 4) + 1e-9), 12))
def cg_f053_ebitda_margin_core49_rank_12q_v050_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_log(ebitdamargin.clip(lower=0.001) + 1.0), 12))

# core50-59: rank 20q
def cg_f053_ebitda_margin_core50_rank_20q_v051_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(ebitdamargin, 20))
def cg_f053_ebitda_margin_core51_rank_20q_v052_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_safe_div(ebitda, assets), 20))
def cg_f053_ebitda_margin_core52_rank_20q_v053_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_safe_div(ebitda, marketcap), 20))
def cg_f053_ebitda_margin_core53_rank_20q_v054_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_safe_div(ebitda, equity.abs() + 1.0), 20))
def cg_f053_ebitda_margin_core54_rank_20q_v055_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_safe_div(ebitda, opex.abs() + 1.0), 20))
def cg_f053_ebitda_margin_core55_rank_20q_v056_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_safe_div(ebitda - netinc, revenue), 20))
def cg_f053_ebitda_margin_core56_rank_20q_v057_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_diff(ebitdamargin, 4), 20))
def cg_f053_ebitda_margin_core57_rank_20q_v058_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_pct_change(ebitda, 4), 20))
def cg_f053_ebitda_margin_core58_rank_20q_v059_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_safe_div(ebitdamargin, _std(ebitdamargin, 8) + 1e-9), 20))
def cg_f053_ebitda_margin_core59_rank_20q_v060_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_log(ebitdamargin.clip(lower=0.001) + 1.0), 20))

# core60-69: pct 1q
def cg_f053_ebitda_margin_core60_pct_1q_v061_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(ebitdamargin, 1))
def cg_f053_ebitda_margin_core61_pct_1q_v062_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_safe_div(ebitda, assets), 1))
def cg_f053_ebitda_margin_core62_pct_1q_v063_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_safe_div(ebitda, marketcap), 1))
def cg_f053_ebitda_margin_core63_pct_1q_v064_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_safe_div(ebitda, equity.abs() + 1.0), 1))
def cg_f053_ebitda_margin_core64_pct_1q_v065_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_safe_div(ebitda, opex.abs() + 1.0), 1))
def cg_f053_ebitda_margin_core65_pct_1q_v066_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_safe_div(ebitda - netinc, revenue), 1))
def cg_f053_ebitda_margin_core66_pct_1q_v067_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_diff(ebitdamargin, 4), 1))
def cg_f053_ebitda_margin_core67_pct_1q_v068_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_pct_change(ebitda, 4), 1))
def cg_f053_ebitda_margin_core68_pct_1q_v069_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_safe_div(ebitdamargin, _std(ebitdamargin, 4) + 1e-9), 1))
def cg_f053_ebitda_margin_core69_pct_1q_v070_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_log(ebitdamargin.clip(lower=0.001) + 1.0), 1))

# core70-74: pct 4q
def cg_f053_ebitda_margin_core70_pct_4q_v071_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(ebitdamargin, 4))
def cg_f053_ebitda_margin_core71_pct_4q_v072_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_safe_div(ebitda, assets), 4))
def cg_f053_ebitda_margin_core72_pct_4q_v073_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_safe_div(ebitda, marketcap), 4))
def cg_f053_ebitda_margin_core73_pct_4q_v074_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_safe_div(ebitda, equity.abs() + 1.0), 4))
def cg_f053_ebitda_margin_core74_pct_4q_v075_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_safe_div(ebitda, opex.abs() + 1.0), 4))
