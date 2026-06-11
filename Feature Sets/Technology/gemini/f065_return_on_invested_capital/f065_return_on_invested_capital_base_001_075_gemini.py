import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core00-09: mean 4q
def cg_f065_return_on_invested_capital_core00_mean_4q_v001_signal(roic, invcap, invcapavg):
    return _clean(_mean(roic, 4))
def cg_f065_return_on_invested_capital_core01_mean_4q_v002_signal(roic, invcap, invcapavg):
    return _clean(_mean(invcap, 4))
def cg_f065_return_on_invested_capital_core02_mean_4q_v003_signal(roic, invcap, invcapavg):
    return _clean(_mean(invcapavg, 4))
def cg_f065_return_on_invested_capital_core03_mean_4q_v004_signal(roic, invcap, invcapavg):
    return _clean(_mean(_safe_div(roic * invcap, invcapavg), 4))
def cg_f065_return_on_invested_capital_core04_mean_4q_v005_signal(roic, invcap, invcapavg):
    return _clean(_mean(roic - _mean(roic, 4), 4))
def cg_f065_return_on_invested_capital_core05_mean_4q_v006_signal(roic, invcap, invcapavg):
    return _clean(_mean(_safe_div(invcap, invcapavg), 4))
def cg_f065_return_on_invested_capital_core06_mean_4q_v007_signal(roic, invcap, invcapavg):
    return _clean(_mean(_diff(roic, 1), 4))
def cg_f065_return_on_invested_capital_core07_mean_4q_v008_signal(roic, invcap, invcapavg):
    return _clean(_mean(_pct_change(invcap, 1), 4))
def cg_f065_return_on_invested_capital_core08_mean_4q_v009_signal(roic, invcap, invcapavg):
    return _clean(_mean(_safe_div(roic, invcapavg.abs() + 1.0), 4))
def cg_f065_return_on_invested_capital_core09_mean_4q_v010_signal(roic, invcap, invcapavg):
    return _clean(_mean(_safe_div(invcap - invcapavg, invcapavg.abs() + 1.0), 4))

# core10-19: mean 8q
def cg_f065_return_on_invested_capital_core10_mean_8q_v011_signal(roic, invcap, invcapavg):
    return _clean(_mean(roic, 8))
def cg_f065_return_on_invested_capital_core11_mean_8q_v012_signal(roic, invcap, invcapavg):
    return _clean(_mean(invcap, 8))
def cg_f065_return_on_invested_capital_core12_mean_8q_v013_signal(roic, invcap, invcapavg):
    return _clean(_mean(invcapavg, 8))
def cg_f065_return_on_invested_capital_core13_mean_8q_v014_signal(roic, invcap, invcapavg):
    return _clean(_mean(_safe_div(roic * invcap, invcapavg), 8))
def cg_f065_return_on_invested_capital_core14_mean_8q_v015_signal(roic, invcap, invcapavg):
    return _clean(_mean(roic - _mean(roic, 8), 8))
def cg_f065_return_on_invested_capital_core15_mean_8q_v016_signal(roic, invcap, invcapavg):
    return _clean(_mean(_safe_div(invcap, invcapavg), 8))
def cg_f065_return_on_invested_capital_core16_mean_8q_v017_signal(roic, invcap, invcapavg):
    return _clean(_mean(_diff(roic, 1), 8))
def cg_f065_return_on_invested_capital_core17_mean_8q_v018_signal(roic, invcap, invcapavg):
    return _clean(_mean(_pct_change(invcap, 1), 8))
def cg_f065_return_on_invested_capital_core18_mean_8q_v019_signal(roic, invcap, invcapavg):
    return _clean(_mean(_safe_div(roic, invcapavg.abs() + 1.0), 8))
def cg_f065_return_on_invested_capital_core19_mean_8q_v020_signal(roic, invcap, invcapavg):
    return _clean(_mean(_safe_div(invcap - invcapavg, invcapavg.abs() + 1.0), 8))

# core20-29: z 8q
def cg_f065_return_on_invested_capital_core20_z_8q_v021_signal(roic, invcap, invcapavg):
    return _clean(_z(roic, 8))
def cg_f065_return_on_invested_capital_core21_z_8q_v022_signal(roic, invcap, invcapavg):
    return _clean(_z(invcap, 8))
def cg_f065_return_on_invested_capital_core22_z_8q_v023_signal(roic, invcap, invcapavg):
    return _clean(_z(invcapavg, 8))
def cg_f065_return_on_invested_capital_core23_z_8q_v024_signal(roic, invcap, invcapavg):
    return _clean(_z(_safe_div(roic * invcap, invcapavg), 8))
def cg_f065_return_on_invested_capital_core24_z_8q_v025_signal(roic, invcap, invcapavg):
    return _clean(_z(roic - _mean(roic, 8), 8))
def cg_f065_return_on_invested_capital_core25_z_8q_v026_signal(roic, invcap, invcapavg):
    return _clean(_z(_safe_div(invcap, invcapavg), 8))
def cg_f065_return_on_invested_capital_core26_z_8q_v027_signal(roic, invcap, invcapavg):
    return _clean(_z(_diff(roic, 1), 8))
def cg_f065_return_on_invested_capital_core27_z_8q_v028_signal(roic, invcap, invcapavg):
    return _clean(_z(_pct_change(invcap, 1), 8))
def cg_f065_return_on_invested_capital_core28_z_8q_v029_signal(roic, invcap, invcapavg):
    return _clean(_z(_safe_div(roic, invcapavg.abs() + 1.0), 8))
def cg_f065_return_on_invested_capital_core29_z_8q_v030_signal(roic, invcap, invcapavg):
    return _clean(_z(_safe_div(invcap - invcapavg, invcapavg.abs() + 1.0), 8))

# core30-39: z 20q
def cg_f065_return_on_invested_capital_core30_z_20q_v031_signal(roic, invcap, invcapavg):
    return _clean(_z(roic, 20))
def cg_f065_return_on_invested_capital_core31_z_20q_v032_signal(roic, invcap, invcapavg):
    return _clean(_z(invcap, 20))
def cg_f065_return_on_invested_capital_core32_z_20q_v033_signal(roic, invcap, invcapavg):
    return _clean(_z(invcapavg, 20))
def cg_f065_return_on_invested_capital_core33_z_20q_v034_signal(roic, invcap, invcapavg):
    return _clean(_z(_safe_div(roic * invcap, invcapavg), 20))
def cg_f065_return_on_invested_capital_core34_z_20q_v035_signal(roic, invcap, invcapavg):
    return _clean(_z(roic - _mean(roic, 20), 20))
def cg_f065_return_on_invested_capital_core35_z_20q_v036_signal(roic, invcap, invcapavg):
    return _clean(_z(_safe_div(invcap, invcapavg), 20))
def cg_f065_return_on_invested_capital_core36_z_20q_v037_signal(roic, invcap, invcapavg):
    return _clean(_z(_diff(roic, 1), 20))
def cg_f065_return_on_invested_capital_core37_z_20q_v038_signal(roic, invcap, invcapavg):
    return _clean(_z(_pct_change(invcap, 1), 20))
def cg_f065_return_on_invested_capital_core38_z_20q_v039_signal(roic, invcap, invcapavg):
    return _clean(_z(_safe_div(roic, invcapavg.abs() + 1.0), 20))
def cg_f065_return_on_invested_capital_core39_z_20q_v040_signal(roic, invcap, invcapavg):
    return _clean(_z(_safe_div(invcap - invcapavg, invcapavg.abs() + 1.0), 20))

# core40-49: rank 8q
def cg_f065_return_on_invested_capital_core40_rank_8q_v041_signal(roic, invcap, invcapavg):
    return _clean(_rank(roic, 8))
def cg_f065_return_on_invested_capital_core41_rank_8q_v042_signal(roic, invcap, invcapavg):
    return _clean(_rank(invcap, 8))
def cg_f065_return_on_invested_capital_core42_rank_8q_v043_signal(roic, invcap, invcapavg):
    return _clean(_rank(invcapavg, 8))
def cg_f065_return_on_invested_capital_core43_rank_8q_v044_signal(roic, invcap, invcapavg):
    return _clean(_rank(_safe_div(roic * invcap, invcapavg), 8))
def cg_f065_return_on_invested_capital_core44_rank_8q_v045_signal(roic, invcap, invcapavg):
    return _clean(_rank(roic - _mean(roic, 8), 8))
def cg_f065_return_on_invested_capital_core45_rank_8q_v046_signal(roic, invcap, invcapavg):
    return _clean(_rank(_safe_div(invcap, invcapavg), 8))
def cg_f065_return_on_invested_capital_core46_rank_8q_v047_signal(roic, invcap, invcapavg):
    return _clean(_rank(_diff(roic, 1), 8))
def cg_f065_return_on_invested_capital_core47_rank_8q_v048_signal(roic, invcap, invcapavg):
    return _clean(_rank(_pct_change(invcap, 1), 8))
def cg_f065_return_on_invested_capital_core48_rank_8q_v049_signal(roic, invcap, invcapavg):
    return _clean(_rank(_safe_div(roic, invcapavg.abs() + 1.0), 8))
def cg_f065_return_on_invested_capital_core49_rank_8q_v050_signal(roic, invcap, invcapavg):
    return _clean(_rank(_safe_div(invcap - invcapavg, invcapavg.abs() + 1.0), 8))

# core50-59: rank 20q
def cg_f065_return_on_invested_capital_core50_rank_20q_v051_signal(roic, invcap, invcapavg):
    return _clean(_rank(roic, 20))
def cg_f065_return_on_invested_capital_core51_rank_20q_v052_signal(roic, invcap, invcapavg):
    return _clean(_rank(invcap, 20))
def cg_f065_return_on_invested_capital_core52_rank_20q_v053_signal(roic, invcap, invcapavg):
    return _clean(_rank(invcapavg, 20))
def cg_f065_return_on_invested_capital_core53_rank_20q_v054_signal(roic, invcap, invcapavg):
    return _clean(_rank(_safe_div(roic * invcap, invcapavg), 20))
def cg_f065_return_on_invested_capital_core54_rank_20q_v055_signal(roic, invcap, invcapavg):
    return _clean(_rank(roic - _mean(roic, 20), 20))
def cg_f065_return_on_invested_capital_core55_rank_20q_v056_signal(roic, invcap, invcapavg):
    return _clean(_rank(_safe_div(invcap, invcapavg), 20))
def cg_f065_return_on_invested_capital_core56_rank_20q_v057_signal(roic, invcap, invcapavg):
    return _clean(_rank(_diff(roic, 1), 20))
def cg_f065_return_on_invested_capital_core57_rank_20q_v058_signal(roic, invcap, invcapavg):
    return _clean(_rank(_pct_change(invcap, 1), 20))
def cg_f065_return_on_invested_capital_core58_rank_20q_v059_signal(roic, invcap, invcapavg):
    return _clean(_rank(_safe_div(roic, invcapavg.abs() + 1.0), 20))
def cg_f065_return_on_invested_capital_core59_rank_20q_v060_signal(roic, invcap, invcapavg):
    return _clean(_rank(_safe_div(invcap - invcapavg, invcapavg.abs() + 1.0), 20))

# core60-69: pct 1q
def cg_f065_return_on_invested_capital_core60_pct_1q_v061_signal(roic, invcap, invcapavg):
    return _clean(_pct_change(roic, 1))
def cg_f065_return_on_invested_capital_core61_pct_1q_v062_signal(roic, invcap, invcapavg):
    return _clean(_pct_change(invcap, 1))
def cg_f065_return_on_invested_capital_core62_pct_1q_v063_signal(roic, invcap, invcapavg):
    return _clean(_pct_change(invcapavg, 1))
def cg_f065_return_on_invested_capital_core63_pct_1q_v064_signal(roic, invcap, invcapavg):
    return _clean(_pct_change(_safe_div(roic * invcap, invcapavg), 1))
def cg_f065_return_on_invested_capital_core64_pct_1q_v065_signal(roic, invcap, invcapavg):
    return _clean(_pct_change(roic - _mean(roic, 4), 1))
def cg_f065_return_on_invested_capital_core65_pct_1q_v066_signal(roic, invcap, invcapavg):
    return _clean(_pct_change(_safe_div(invcap, invcapavg), 1))
def cg_f065_return_on_invested_capital_core66_pct_1q_v067_signal(roic, invcap, invcapavg):
    return _clean(_pct_change(_diff(roic, 1), 1))
def cg_f065_return_on_invested_capital_core67_pct_1q_v068_signal(roic, invcap, invcapavg):
    return _clean(_pct_change(_pct_change(invcap, 1), 1))
def cg_f065_return_on_invested_capital_core68_pct_1q_v069_signal(roic, invcap, invcapavg):
    return _clean(_pct_change(_safe_div(roic, invcapavg.abs() + 1.0), 1))
def cg_f065_return_on_invested_capital_core69_pct_1q_v070_signal(roic, invcap, invcapavg):
    return _clean(_pct_change(_safe_div(invcap - invcapavg, invcapavg.abs() + 1.0), 1))

# core70-74: pct 4q
def cg_f065_return_on_invested_capital_core70_pct_4q_v071_signal(roic, invcap, invcapavg):
    return _clean(_pct_change(roic, 4))
def cg_f065_return_on_invested_capital_core71_pct_4q_v072_signal(roic, invcap, invcapavg):
    return _clean(_pct_change(invcap, 4))
def cg_f065_return_on_invested_capital_core72_pct_4q_v073_signal(roic, invcap, invcapavg):
    return _clean(_pct_change(invcapavg, 4))
def cg_f065_return_on_invested_capital_core73_pct_4q_v074_signal(roic, invcap, invcapavg):
    return _clean(_pct_change(_safe_div(roic * invcap, invcapavg), 4))
def cg_f065_return_on_invested_capital_core74_pct_4q_v075_signal(roic, invcap, invcapavg):
    return _clean(_pct_change(roic - _mean(roic, 4), 4))
