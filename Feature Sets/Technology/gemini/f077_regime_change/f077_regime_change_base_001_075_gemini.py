import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f077_regime_change_core00_mean_4q_v001_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_mean(revenue, 4))
def cg_f077_regime_change_core01_mean_4q_v002_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_mean(rnd, 4))
def cg_f077_regime_change_core02_mean_4q_v003_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_mean(ncfo, 4))
def cg_f077_regime_change_core03_mean_4q_v004_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_mean(opex, 4))
def cg_f077_regime_change_core04_mean_4q_v005_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_mean(cashneq, 4))
def cg_f077_regime_change_core05_mean_4q_v006_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_mean(fcf, 4))
def cg_f077_regime_change_core06_mean_8q_v007_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_mean(revenue, 8))
def cg_f077_regime_change_core07_mean_8q_v008_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_mean(rnd, 8))
def cg_f077_regime_change_core08_mean_8q_v009_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_mean(ncfo, 8))
def cg_f077_regime_change_core09_mean_8q_v010_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_mean(opex, 8))
def cg_f077_regime_change_core10_mean_8q_v011_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_mean(cashneq, 8))
def cg_f077_regime_change_core11_mean_8q_v012_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_mean(fcf, 8))
def cg_f077_regime_change_core12_z_8q_v013_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(revenue, 8))
def cg_f077_regime_change_core13_z_8q_v014_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(rnd, 8))
def cg_f077_regime_change_core14_z_8q_v015_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(ncfo, 8))
def cg_f077_regime_change_core15_z_8q_v016_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(opex, 8))
def cg_f077_regime_change_core16_z_8q_v017_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(cashneq, 8))
def cg_f077_regime_change_core17_z_8q_v018_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(fcf, 8))
def cg_f077_regime_change_core18_z_20q_v019_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(revenue, 20))
def cg_f077_regime_change_core19_z_20q_v020_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(rnd, 20))
def cg_f077_regime_change_core20_z_20q_v021_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(ncfo, 20))
def cg_f077_regime_change_core21_z_20q_v022_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(opex, 20))
def cg_f077_regime_change_core22_z_20q_v023_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(cashneq, 20))
def cg_f077_regime_change_core23_z_20q_v024_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(fcf, 20))
def cg_f077_regime_change_core24_rank_12q_v025_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(revenue, 12))
def cg_f077_regime_change_core25_rank_12q_v026_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(rnd, 12))
def cg_f077_regime_change_core26_rank_12q_v027_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(ncfo, 12))
def cg_f077_regime_change_core27_rank_12q_v028_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(opex, 12))
def cg_f077_regime_change_core28_rank_12q_v029_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(cashneq, 12))
def cg_f077_regime_change_core29_rank_12q_v030_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(fcf, 12))
def cg_f077_regime_change_core30_rank_20q_v031_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(revenue, 20))
def cg_f077_regime_change_core31_rank_20q_v032_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(rnd, 20))
def cg_f077_regime_change_core32_rank_20q_v033_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(ncfo, 20))
def cg_f077_regime_change_core33_rank_20q_v034_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(opex, 20))
def cg_f077_regime_change_core34_rank_20q_v035_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(cashneq, 20))
def cg_f077_regime_change_core35_rank_20q_v036_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(fcf, 20))
def cg_f077_regime_change_core36_pct_1q_v037_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_pct_change(revenue, 1))
def cg_f077_regime_change_core37_pct_1q_v038_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_pct_change(rnd, 1))
def cg_f077_regime_change_core38_pct_1q_v039_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_pct_change(ncfo, 1))
def cg_f077_regime_change_core39_pct_1q_v040_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_pct_change(opex, 1))
def cg_f077_regime_change_core40_pct_1q_v041_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_pct_change(cashneq, 1))
def cg_f077_regime_change_core41_pct_1q_v042_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_pct_change(fcf, 1))
def cg_f077_regime_change_core42_pct_4q_v043_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_pct_change(revenue, 4))
def cg_f077_regime_change_core43_pct_4q_v044_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_pct_change(rnd, 4))
def cg_f077_regime_change_core44_pct_4q_v045_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_pct_change(ncfo, 4))
def cg_f077_regime_change_core45_pct_4q_v046_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_pct_change(opex, 4))
def cg_f077_regime_change_core46_pct_4q_v047_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_pct_change(cashneq, 4))
def cg_f077_regime_change_core47_pct_4q_v048_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_pct_change(fcf, 4))
def cg_f077_regime_change_core48_slope_4q_v049_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(revenue, 4))
def cg_f077_regime_change_core49_slope_4q_v050_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(rnd, 4))
def cg_f077_regime_change_core50_slope_4q_v051_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(ncfo, 4))
def cg_f077_regime_change_core51_slope_4q_v052_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(opex, 4))
def cg_f077_regime_change_core52_slope_4q_v053_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(cashneq, 4))
def cg_f077_regime_change_core53_slope_4q_v054_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(fcf, 4))
def cg_f077_regime_change_core54_slope_8q_v055_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(revenue, 8))
def cg_f077_regime_change_core55_slope_8q_v056_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(rnd, 8))
def cg_f077_regime_change_core56_slope_8q_v057_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(ncfo, 8))
def cg_f077_regime_change_core57_slope_8q_v058_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(opex, 8))
def cg_f077_regime_change_core58_slope_8q_v059_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(cashneq, 8))
def cg_f077_regime_change_core59_slope_8q_v060_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(fcf, 8))
def cg_f077_regime_change_core60_autocorr_8q_v061_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_autocorr(revenue, 8))
def cg_f077_regime_change_core61_autocorr_8q_v062_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_autocorr(rnd, 8))
def cg_f077_regime_change_core62_autocorr_8q_v063_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_autocorr(ncfo, 8))
def cg_f077_regime_change_core63_autocorr_8q_v064_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_autocorr(opex, 8))
def cg_f077_regime_change_core64_autocorr_8q_v065_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_autocorr(cashneq, 8))
def cg_f077_regime_change_core65_autocorr_8q_v066_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_autocorr(fcf, 8))
def cg_f077_regime_change_core66_ewm_4q_v067_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_ewm(revenue, 4))
def cg_f077_regime_change_core67_ewm_4q_v068_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_ewm(rnd, 4))
def cg_f077_regime_change_core68_ewm_4q_v069_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_ewm(ncfo, 4))
def cg_f077_regime_change_core69_ewm_4q_v070_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_ewm(opex, 4))
def cg_f077_regime_change_core70_ewm_4q_v071_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_ewm(cashneq, 4))
def cg_f077_regime_change_core71_ewm_4q_v072_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_ewm(fcf, 4))
def cg_f077_regime_change_core72_ewm_8q_v073_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_ewm(revenue, 8))
def cg_f077_regime_change_core73_ewm_8q_v074_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_ewm(rnd, 8))
def cg_f077_regime_change_core74_ewm_8q_v075_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_ewm(ncfo, 8))