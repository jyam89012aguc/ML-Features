import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f087_ohlcv_multi_year_lows_core00_mean_4q_v001_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(date, 4))
def cg_f087_ohlcv_multi_year_lows_core01_mean_4q_v002_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(open, 4))
def cg_f087_ohlcv_multi_year_lows_core02_mean_4q_v003_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(high, 4))
def cg_f087_ohlcv_multi_year_lows_core03_mean_4q_v004_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(low, 4))
def cg_f087_ohlcv_multi_year_lows_core04_mean_4q_v005_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(close, 4))
def cg_f087_ohlcv_multi_year_lows_core05_mean_4q_v006_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(volume, 4))
def cg_f087_ohlcv_multi_year_lows_core06_mean_4q_v007_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(closeadj, 4))
def cg_f087_ohlcv_multi_year_lows_core07_mean_4q_v008_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(closeunadj, 4))
def cg_f087_ohlcv_multi_year_lows_core08_mean_8q_v009_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(date, 8))
def cg_f087_ohlcv_multi_year_lows_core09_mean_8q_v010_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(open, 8))
def cg_f087_ohlcv_multi_year_lows_core10_mean_8q_v011_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(high, 8))
def cg_f087_ohlcv_multi_year_lows_core11_mean_8q_v012_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(low, 8))
def cg_f087_ohlcv_multi_year_lows_core12_mean_8q_v013_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(close, 8))
def cg_f087_ohlcv_multi_year_lows_core13_mean_8q_v014_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(volume, 8))
def cg_f087_ohlcv_multi_year_lows_core14_mean_8q_v015_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(closeadj, 8))
def cg_f087_ohlcv_multi_year_lows_core15_mean_8q_v016_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(closeunadj, 8))
def cg_f087_ohlcv_multi_year_lows_core16_z_8q_v017_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(date, 8))
def cg_f087_ohlcv_multi_year_lows_core17_z_8q_v018_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(open, 8))
def cg_f087_ohlcv_multi_year_lows_core18_z_8q_v019_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(high, 8))
def cg_f087_ohlcv_multi_year_lows_core19_z_8q_v020_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(low, 8))
def cg_f087_ohlcv_multi_year_lows_core20_z_8q_v021_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(close, 8))
def cg_f087_ohlcv_multi_year_lows_core21_z_8q_v022_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(volume, 8))
def cg_f087_ohlcv_multi_year_lows_core22_z_8q_v023_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(closeadj, 8))
def cg_f087_ohlcv_multi_year_lows_core23_z_8q_v024_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(closeunadj, 8))
def cg_f087_ohlcv_multi_year_lows_core24_z_20q_v025_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(date, 20))
def cg_f087_ohlcv_multi_year_lows_core25_z_20q_v026_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(open, 20))
def cg_f087_ohlcv_multi_year_lows_core26_z_20q_v027_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(high, 20))
def cg_f087_ohlcv_multi_year_lows_core27_z_20q_v028_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(low, 20))
def cg_f087_ohlcv_multi_year_lows_core28_z_20q_v029_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(close, 20))
def cg_f087_ohlcv_multi_year_lows_core29_z_20q_v030_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(volume, 20))
def cg_f087_ohlcv_multi_year_lows_core30_z_20q_v031_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(closeadj, 20))
def cg_f087_ohlcv_multi_year_lows_core31_z_20q_v032_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(closeunadj, 20))
def cg_f087_ohlcv_multi_year_lows_core32_rank_12q_v033_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(date, 12))
def cg_f087_ohlcv_multi_year_lows_core33_rank_12q_v034_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(open, 12))
def cg_f087_ohlcv_multi_year_lows_core34_rank_12q_v035_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(high, 12))
def cg_f087_ohlcv_multi_year_lows_core35_rank_12q_v036_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(low, 12))
def cg_f087_ohlcv_multi_year_lows_core36_rank_12q_v037_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(close, 12))
def cg_f087_ohlcv_multi_year_lows_core37_rank_12q_v038_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(volume, 12))
def cg_f087_ohlcv_multi_year_lows_core38_rank_12q_v039_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(closeadj, 12))
def cg_f087_ohlcv_multi_year_lows_core39_rank_12q_v040_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(closeunadj, 12))
def cg_f087_ohlcv_multi_year_lows_core40_rank_20q_v041_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(date, 20))
def cg_f087_ohlcv_multi_year_lows_core41_rank_20q_v042_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(open, 20))
def cg_f087_ohlcv_multi_year_lows_core42_rank_20q_v043_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(high, 20))
def cg_f087_ohlcv_multi_year_lows_core43_rank_20q_v044_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(low, 20))
def cg_f087_ohlcv_multi_year_lows_core44_rank_20q_v045_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(close, 20))
def cg_f087_ohlcv_multi_year_lows_core45_rank_20q_v046_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(volume, 20))
def cg_f087_ohlcv_multi_year_lows_core46_rank_20q_v047_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(closeadj, 20))
def cg_f087_ohlcv_multi_year_lows_core47_rank_20q_v048_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(closeunadj, 20))
def cg_f087_ohlcv_multi_year_lows_core48_pct_1q_v049_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_pct_change(date, 1))
def cg_f087_ohlcv_multi_year_lows_core49_pct_1q_v050_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_pct_change(open, 1))
def cg_f087_ohlcv_multi_year_lows_core50_pct_1q_v051_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_pct_change(high, 1))
def cg_f087_ohlcv_multi_year_lows_core51_pct_1q_v052_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_pct_change(low, 1))
def cg_f087_ohlcv_multi_year_lows_core52_pct_1q_v053_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_pct_change(close, 1))
def cg_f087_ohlcv_multi_year_lows_core53_pct_1q_v054_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_pct_change(volume, 1))
def cg_f087_ohlcv_multi_year_lows_core54_pct_1q_v055_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_pct_change(closeadj, 1))
def cg_f087_ohlcv_multi_year_lows_core55_pct_1q_v056_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_pct_change(closeunadj, 1))
def cg_f087_ohlcv_multi_year_lows_core56_pct_4q_v057_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_pct_change(date, 4))
def cg_f087_ohlcv_multi_year_lows_core57_pct_4q_v058_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_pct_change(open, 4))
def cg_f087_ohlcv_multi_year_lows_core58_pct_4q_v059_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_pct_change(high, 4))
def cg_f087_ohlcv_multi_year_lows_core59_pct_4q_v060_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_pct_change(low, 4))
def cg_f087_ohlcv_multi_year_lows_core60_pct_4q_v061_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_pct_change(close, 4))
def cg_f087_ohlcv_multi_year_lows_core61_pct_4q_v062_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_pct_change(volume, 4))
def cg_f087_ohlcv_multi_year_lows_core62_pct_4q_v063_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_pct_change(closeadj, 4))
def cg_f087_ohlcv_multi_year_lows_core63_pct_4q_v064_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_pct_change(closeunadj, 4))
def cg_f087_ohlcv_multi_year_lows_core64_slope_4q_v065_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(date, 4))
def cg_f087_ohlcv_multi_year_lows_core65_slope_4q_v066_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(open, 4))
def cg_f087_ohlcv_multi_year_lows_core66_slope_4q_v067_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(high, 4))
def cg_f087_ohlcv_multi_year_lows_core67_slope_4q_v068_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(low, 4))
def cg_f087_ohlcv_multi_year_lows_core68_slope_4q_v069_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(close, 4))
def cg_f087_ohlcv_multi_year_lows_core69_slope_4q_v070_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(volume, 4))
def cg_f087_ohlcv_multi_year_lows_core70_slope_4q_v071_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(closeadj, 4))
def cg_f087_ohlcv_multi_year_lows_core71_slope_4q_v072_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(closeunadj, 4))
def cg_f087_ohlcv_multi_year_lows_core72_slope_8q_v073_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(date, 8))
def cg_f087_ohlcv_multi_year_lows_core73_slope_8q_v074_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(open, 8))
def cg_f087_ohlcv_multi_year_lows_core74_slope_8q_v075_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(high, 8))