import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core00-09: mean 4q
def cg_f052_operating_margin_core00_mean_4q_v001_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(opmargin, 4))
def cg_f052_operating_margin_core01_mean_4q_v002_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_safe_div(opinc, assets), 4))
def cg_f052_operating_margin_core02_mean_4q_v003_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_safe_div(opinc, marketcap), 4))
def cg_f052_operating_margin_core03_mean_4q_v004_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_safe_div(opinc, equity.abs() + 1.0), 4))
def cg_f052_operating_margin_core04_mean_4q_v005_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_safe_div(opinc, opex.abs() + 1.0), 4))
def cg_f052_operating_margin_core05_mean_4q_v006_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_safe_div(opinc - netinc, revenue), 4))
def cg_f052_operating_margin_core06_mean_4q_v007_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_diff(opmargin, 4), 4))
def cg_f052_operating_margin_core07_mean_4q_v008_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_pct_change(opinc, 4), 4))
def cg_f052_operating_margin_core08_mean_4q_v009_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_safe_div(opmargin, _std(opmargin, 4) + 1e-9), 4))
def cg_f052_operating_margin_core09_mean_4q_v010_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_log(opmargin.clip(lower=0.001) + 1.0), 4))

# core10-19: mean 8q
def cg_f052_operating_margin_core10_mean_8q_v011_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(opmargin, 8))
def cg_f052_operating_margin_core11_mean_8q_v012_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_safe_div(opinc, assets), 8))
def cg_f052_operating_margin_core12_mean_8q_v013_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_safe_div(opinc, marketcap), 8))
def cg_f052_operating_margin_core13_mean_8q_v014_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_safe_div(opinc, equity.abs() + 1.0), 8))
def cg_f052_operating_margin_core14_mean_8q_v015_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_safe_div(opinc, opex.abs() + 1.0), 8))
def cg_f052_operating_margin_core15_mean_8q_v016_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_safe_div(opinc - netinc, revenue), 8))
def cg_f052_operating_margin_core16_mean_8q_v017_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_diff(opmargin, 4), 8))
def cg_f052_operating_margin_core17_mean_8q_v018_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_pct_change(opinc, 4), 8))
def cg_f052_operating_margin_core18_mean_8q_v019_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_safe_div(opmargin, _std(opmargin, 8) + 1e-9), 8))
def cg_f052_operating_margin_core19_mean_8q_v020_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_log(opmargin.clip(lower=0.001) + 1.0), 8))

# core20-29: z 8q
def cg_f052_operating_margin_core20_z_8q_v021_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(opmargin, 8))
def cg_f052_operating_margin_core21_z_8q_v022_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_safe_div(opinc, assets), 8))
def cg_f052_operating_margin_core22_z_8q_v023_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_safe_div(opinc, marketcap), 8))
def cg_f052_operating_margin_core23_z_8q_v024_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_safe_div(opinc, equity.abs() + 1.0), 8))
def cg_f052_operating_margin_core24_z_8q_v025_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_safe_div(opinc, opex.abs() + 1.0), 8))
def cg_f052_operating_margin_core25_z_8q_v026_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_safe_div(opinc - netinc, revenue), 8))
def cg_f052_operating_margin_core26_z_8q_v027_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_diff(opmargin, 4), 8))
def cg_f052_operating_margin_core27_z_8q_v028_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_pct_change(opinc, 4), 8))
def cg_f052_operating_margin_core28_z_8q_v029_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_safe_div(opmargin, _std(opmargin, 4) + 1e-9), 8))
def cg_f052_operating_margin_core29_z_8q_v030_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_log(opmargin.clip(lower=0.001) + 1.0), 8))

# core30-39: z 20q
def cg_f052_operating_margin_core30_z_20q_v031_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(opmargin, 20))
def cg_f052_operating_margin_core31_z_20q_v032_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_safe_div(opinc, assets), 20))
def cg_f052_operating_margin_core32_z_20q_v033_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_safe_div(opinc, marketcap), 20))
def cg_f052_operating_margin_core33_z_20q_v034_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_safe_div(opinc, equity.abs() + 1.0), 20))
def cg_f052_operating_margin_core34_z_20q_v035_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_safe_div(opinc, opex.abs() + 1.0), 20))
def cg_f052_operating_margin_core35_z_20q_v036_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_safe_div(opinc - netinc, revenue), 20))
def cg_f052_operating_margin_core36_z_20q_v037_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_diff(opmargin, 4), 20))
def cg_f052_operating_margin_core37_z_20q_v038_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_pct_change(opinc, 4), 20))
def cg_f052_operating_margin_core38_z_20q_v039_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_safe_div(opmargin, _std(opmargin, 8) + 1e-9), 20))
def cg_f052_operating_margin_core39_z_20q_v040_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_log(opmargin.clip(lower=0.001) + 1.0), 20))

# core40-49: rank 12q
def cg_f052_operating_margin_core40_rank_12q_v041_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(opmargin, 12))
def cg_f052_operating_margin_core41_rank_12q_v042_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_safe_div(opinc, assets), 12))
def cg_f052_operating_margin_core42_rank_12q_v043_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_safe_div(opinc, marketcap), 12))
def cg_f052_operating_margin_core43_rank_12q_v044_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_safe_div(opinc, equity.abs() + 1.0), 12))
def cg_f052_operating_margin_core44_rank_12q_v045_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_safe_div(opinc, opex.abs() + 1.0), 12))
def cg_f052_operating_margin_core45_rank_12q_v046_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_safe_div(opinc - netinc, revenue), 12))
def cg_f052_operating_margin_core46_rank_12q_v047_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_diff(opmargin, 4), 12))
def cg_f052_operating_margin_core47_rank_12q_v048_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_pct_change(opinc, 4), 12))
def cg_f052_operating_margin_core48_rank_12q_v049_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_safe_div(opmargin, _std(opmargin, 4) + 1e-9), 12))
def cg_f052_operating_margin_core49_rank_12q_v050_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_log(opmargin.clip(lower=0.001) + 1.0), 12))

# core50-59: rank 20q
def cg_f052_operating_margin_core50_rank_20q_v051_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(opmargin, 20))
def cg_f052_operating_margin_core51_rank_20q_v052_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_safe_div(opinc, assets), 20))
def cg_f052_operating_margin_core52_rank_20q_v053_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_safe_div(opinc, marketcap), 20))
def cg_f052_operating_margin_core53_rank_20q_v054_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_safe_div(opinc, equity.abs() + 1.0), 20))
def cg_f052_operating_margin_core54_rank_20q_v055_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_safe_div(opinc, opex.abs() + 1.0), 20))
def cg_f052_operating_margin_core55_rank_20q_v056_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_safe_div(opinc - netinc, revenue), 20))
def cg_f052_operating_margin_core56_rank_20q_v057_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_diff(opmargin, 4), 20))
def cg_f052_operating_margin_core57_rank_20q_v058_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_pct_change(opinc, 4), 20))
def cg_f052_operating_margin_core58_rank_20q_v059_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_safe_div(opmargin, _std(opmargin, 8) + 1e-9), 20))
def cg_f052_operating_margin_core59_rank_20q_v060_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_log(opmargin.clip(lower=0.001) + 1.0), 20))

# core60-69: pct 1q
def cg_f052_operating_margin_core60_pct_1q_v061_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(opmargin, 1))
def cg_f052_operating_margin_core61_pct_1q_v062_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_safe_div(opinc, assets), 1))
def cg_f052_operating_margin_core62_pct_1q_v063_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_safe_div(opinc, marketcap), 1))
def cg_f052_operating_margin_core63_pct_1q_v064_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_safe_div(opinc, equity.abs() + 1.0), 1))
def cg_f052_operating_margin_core64_pct_1q_v065_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_safe_div(opinc, opex.abs() + 1.0), 1))
def cg_f052_operating_margin_core65_pct_1q_v066_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_safe_div(opinc - netinc, revenue), 1))
def cg_f052_operating_margin_core66_pct_1q_v067_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_diff(opmargin, 4), 1))
def cg_f052_operating_margin_core67_pct_1q_v068_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_pct_change(opinc, 4), 1))
def cg_f052_operating_margin_core68_pct_1q_v069_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_safe_div(opmargin, _std(opmargin, 4) + 1e-9), 1))
def cg_f052_operating_margin_core69_pct_1q_v070_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_log(opmargin.clip(lower=0.001) + 1.0), 1))

# core70-74: pct 4q
def cg_f052_operating_margin_core70_pct_4q_v071_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(opmargin, 4))
def cg_f052_operating_margin_core71_pct_4q_v072_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_safe_div(opinc, assets), 4))
def cg_f052_operating_margin_core72_pct_4q_v073_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_safe_div(opinc, marketcap), 4))
def cg_f052_operating_margin_core73_pct_4q_v074_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_safe_div(opinc, equity.abs() + 1.0), 4))
def cg_f052_operating_margin_core74_pct_4q_v075_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_safe_div(opinc, opex.abs() + 1.0), 4))
