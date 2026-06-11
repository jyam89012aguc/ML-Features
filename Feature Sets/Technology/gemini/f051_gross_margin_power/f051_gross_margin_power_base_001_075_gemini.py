import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core00-09: mean 4q
def cg_f051_gross_margin_power_core00_mean_4q_v001_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(grossmargin, 4))
def cg_f051_gross_margin_power_core01_mean_4q_v002_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_safe_div(gp, assets), 4))
def cg_f051_gross_margin_power_core02_mean_4q_v003_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_safe_div(gp, marketcap), 4))
def cg_f051_gross_margin_power_core03_mean_4q_v004_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_safe_div(gp, equity.abs() + 1.0), 4))
def cg_f051_gross_margin_power_core04_mean_4q_v005_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_safe_div(gp, opex.abs() + 1.0), 4))
def cg_f051_gross_margin_power_core05_mean_4q_v006_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    # GP to Net Income spread
    return _clean(_mean(_safe_div(gp - netinc, revenue), 4))
def cg_f051_gross_margin_power_core06_mean_4q_v007_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_diff(grossmargin, 4), 4))
def cg_f051_gross_margin_power_core07_mean_4q_v008_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_pct_change(gp, 4), 4))
def cg_f051_gross_margin_power_core08_mean_4q_v009_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_safe_div(grossmargin, _std(grossmargin, 4) + 1e-9), 4))
def cg_f051_gross_margin_power_core09_mean_4q_v010_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_log(grossmargin.clip(lower=0.001) + 1.0), 4))

# core10-19: mean 8q
def cg_f051_gross_margin_power_core10_mean_8q_v011_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(grossmargin, 8))
def cg_f051_gross_margin_power_core11_mean_8q_v012_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_safe_div(gp, assets), 8))
def cg_f051_gross_margin_power_core12_mean_8q_v013_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_safe_div(gp, marketcap), 8))
def cg_f051_gross_margin_power_core13_mean_8q_v014_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_safe_div(gp, equity.abs() + 1.0), 8))
def cg_f051_gross_margin_power_core14_mean_8q_v015_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_safe_div(gp, opex.abs() + 1.0), 8))
def cg_f051_gross_margin_power_core15_mean_8q_v016_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_safe_div(gp - netinc, revenue), 8))
def cg_f051_gross_margin_power_core16_mean_8q_v017_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_diff(grossmargin, 4), 8))
def cg_f051_gross_margin_power_core17_mean_8q_v018_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_pct_change(gp, 4), 8))
def cg_f051_gross_margin_power_core18_mean_8q_v019_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_safe_div(grossmargin, _std(grossmargin, 8) + 1e-9), 8))
def cg_f051_gross_margin_power_core19_mean_8q_v020_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_mean(_log(grossmargin.clip(lower=0.001) + 1.0), 8))

# core20-29: z 8q
def cg_f051_gross_margin_power_core20_z_8q_v021_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(grossmargin, 8))
def cg_f051_gross_margin_power_core21_z_8q_v022_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_safe_div(gp, assets), 8))
def cg_f051_gross_margin_power_core22_z_8q_v023_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_safe_div(gp, marketcap), 8))
def cg_f051_gross_margin_power_core23_z_8q_v024_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_safe_div(gp, equity.abs() + 1.0), 8))
def cg_f051_gross_margin_power_core24_z_8q_v025_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_safe_div(gp, opex.abs() + 1.0), 8))
def cg_f051_gross_margin_power_core25_z_8q_v026_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_safe_div(gp - netinc, revenue), 8))
def cg_f051_gross_margin_power_core26_z_8q_v027_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_diff(grossmargin, 4), 8))
def cg_f051_gross_margin_power_core27_z_8q_v028_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_pct_change(gp, 4), 8))
def cg_f051_gross_margin_power_core28_z_8q_v029_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_safe_div(grossmargin, _std(grossmargin, 4) + 1e-9), 8))
def cg_f051_gross_margin_power_core29_z_8q_v030_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_log(grossmargin.clip(lower=0.001) + 1.0), 8))

# core30-39: z 20q
def cg_f051_gross_margin_power_core30_z_20q_v031_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(grossmargin, 20))
def cg_f051_gross_margin_power_core31_z_20q_v032_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_safe_div(gp, assets), 20))
def cg_f051_gross_margin_power_core32_z_20q_v033_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_safe_div(gp, marketcap), 20))
def cg_f051_gross_margin_power_core33_z_20q_v034_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_safe_div(gp, equity.abs() + 1.0), 20))
def cg_f051_gross_margin_power_core34_z_20q_v035_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_safe_div(gp, opex.abs() + 1.0), 20))
def cg_f051_gross_margin_power_core35_z_20q_v036_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_safe_div(gp - netinc, revenue), 20))
def cg_f051_gross_margin_power_core36_z_20q_v037_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_diff(grossmargin, 4), 20))
def cg_f051_gross_margin_power_core37_z_20q_v038_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_pct_change(gp, 4), 20))
def cg_f051_gross_margin_power_core38_z_20q_v039_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_safe_div(grossmargin, _std(grossmargin, 8) + 1e-9), 20))
def cg_f051_gross_margin_power_core39_z_20q_v040_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_z(_log(grossmargin.clip(lower=0.001) + 1.0), 20))

# core40-49: rank 12q
def cg_f051_gross_margin_power_core40_rank_12q_v041_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(grossmargin, 12))
def cg_f051_gross_margin_power_core41_rank_12q_v042_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_safe_div(gp, assets), 12))
def cg_f051_gross_margin_power_core42_rank_12q_v043_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_safe_div(gp, marketcap), 12))
def cg_f051_gross_margin_power_core43_rank_12q_v044_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_safe_div(gp, equity.abs() + 1.0), 12))
def cg_f051_gross_margin_power_core44_rank_12q_v045_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_safe_div(gp, opex.abs() + 1.0), 12))
def cg_f051_gross_margin_power_core45_rank_12q_v046_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_safe_div(gp - netinc, revenue), 12))
def cg_f051_gross_margin_power_core46_rank_12q_v047_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_diff(grossmargin, 4), 12))
def cg_f051_gross_margin_power_core47_rank_12q_v048_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_pct_change(gp, 4), 12))
def cg_f051_gross_margin_power_core48_rank_12q_v049_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_safe_div(grossmargin, _std(grossmargin, 4) + 1e-9), 12))
def cg_f051_gross_margin_power_core49_rank_12q_v050_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_log(grossmargin.clip(lower=0.001) + 1.0), 12))

# core50-59: rank 20q
def cg_f051_gross_margin_power_core50_rank_20q_v051_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(grossmargin, 20))
def cg_f051_gross_margin_power_core51_rank_20q_v052_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_safe_div(gp, assets), 20))
def cg_f051_gross_margin_power_core52_rank_20q_v053_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_safe_div(gp, marketcap), 20))
def cg_f051_gross_margin_power_core53_rank_20q_v054_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_safe_div(gp, equity.abs() + 1.0), 20))
def cg_f051_gross_margin_power_core54_rank_20q_v055_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_safe_div(gp, opex.abs() + 1.0), 20))
def cg_f051_gross_margin_power_core55_rank_20q_v056_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_safe_div(gp - netinc, revenue), 20))
def cg_f051_gross_margin_power_core56_rank_20q_v057_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_diff(grossmargin, 4), 20))
def cg_f051_gross_margin_power_core57_rank_20q_v058_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_pct_change(gp, 4), 20))
def cg_f051_gross_margin_power_core58_rank_20q_v059_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_safe_div(grossmargin, _std(grossmargin, 8) + 1e-9), 20))
def cg_f051_gross_margin_power_core59_rank_20q_v060_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_rank(_log(grossmargin.clip(lower=0.001) + 1.0), 20))

# core60-69: pct 1q
def cg_f051_gross_margin_power_core60_pct_1q_v061_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(grossmargin, 1))
def cg_f051_gross_margin_power_core61_pct_1q_v062_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_safe_div(gp, assets), 1))
def cg_f051_gross_margin_power_core62_pct_1q_v063_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_safe_div(gp, marketcap), 1))
def cg_f051_gross_margin_power_core63_pct_1q_v064_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_safe_div(gp, equity.abs() + 1.0), 1))
def cg_f051_gross_margin_power_core64_pct_1q_v065_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_safe_div(gp, opex.abs() + 1.0), 1))
def cg_f051_gross_margin_power_core65_pct_1q_v066_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_safe_div(gp - netinc, revenue), 1))
def cg_f051_gross_margin_power_core66_pct_1q_v067_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_diff(grossmargin, 4), 1))
def cg_f051_gross_margin_power_core67_pct_1q_v068_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_pct_change(gp, 4), 1))
def cg_f051_gross_margin_power_core68_pct_1q_v069_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_safe_div(grossmargin, _std(grossmargin, 4) + 1e-9), 1))
def cg_f051_gross_margin_power_core69_pct_1q_v070_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_log(grossmargin.clip(lower=0.001) + 1.0), 1))

# core70-74: pct 4q
def cg_f051_gross_margin_power_core70_pct_4q_v071_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(grossmargin, 4))
def cg_f051_gross_margin_power_core71_pct_4q_v072_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_safe_div(gp, assets), 4))
def cg_f051_gross_margin_power_core72_pct_4q_v073_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_safe_div(gp, marketcap), 4))
def cg_f051_gross_margin_power_core73_pct_4q_v074_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_safe_div(gp, equity.abs() + 1.0), 4))
def cg_f051_gross_margin_power_core74_pct_4q_v075_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_safe_div(gp, opex.abs() + 1.0), 4))
