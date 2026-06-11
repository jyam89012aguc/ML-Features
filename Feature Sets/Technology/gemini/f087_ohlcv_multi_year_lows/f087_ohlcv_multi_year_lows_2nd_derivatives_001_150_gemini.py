import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f087_ohlcv_multi_year_lows_core00_2nd_v001_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(open, 4))
def cg_f087_ohlcv_multi_year_lows_core01_2nd_v002_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(high, 4))
def cg_f087_ohlcv_multi_year_lows_core02_2nd_v003_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(low, 4))
def cg_f087_ohlcv_multi_year_lows_core03_2nd_v004_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(close, 4))
def cg_f087_ohlcv_multi_year_lows_core04_2nd_v005_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(volume, 4))
def cg_f087_ohlcv_multi_year_lows_core05_2nd_v006_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(closeadj, 4))
def cg_f087_ohlcv_multi_year_lows_core06_2nd_v007_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(closeunadj, 4))
def cg_f087_ohlcv_multi_year_lows_core07_2nd_v008_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(_safe_div(close, open), 4))
def cg_f087_ohlcv_multi_year_lows_core08_2nd_v009_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(_safe_div(high, low), 4))
def cg_f087_ohlcv_multi_year_lows_core09_2nd_v010_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(_safe_div(volume, close), 4))
def cg_f087_ohlcv_multi_year_lows_core10_2nd_v011_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(open, 8))
def cg_f087_ohlcv_multi_year_lows_core11_2nd_v012_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(high, 8))
def cg_f087_ohlcv_multi_year_lows_core12_2nd_v013_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(low, 8))
def cg_f087_ohlcv_multi_year_lows_core13_2nd_v014_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(close, 8))
def cg_f087_ohlcv_multi_year_lows_core14_2nd_v015_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(volume, 8))
def cg_f087_ohlcv_multi_year_lows_core15_2nd_v016_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(closeadj, 8))
def cg_f087_ohlcv_multi_year_lows_core16_2nd_v017_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(closeunadj, 8))
def cg_f087_ohlcv_multi_year_lows_core17_2nd_v018_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(_safe_div(close, open), 8))
def cg_f087_ohlcv_multi_year_lows_core18_2nd_v019_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(_safe_div(high, low), 8))
def cg_f087_ohlcv_multi_year_lows_core19_2nd_v020_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(_safe_div(volume, close), 8))
def cg_f087_ohlcv_multi_year_lows_core20_2nd_v021_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_diff(open, 4))
def cg_f087_ohlcv_multi_year_lows_core21_2nd_v022_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_diff(high, 4))
def cg_f087_ohlcv_multi_year_lows_core22_2nd_v023_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_diff(low, 4))
def cg_f087_ohlcv_multi_year_lows_core23_2nd_v024_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_diff(close, 4))
def cg_f087_ohlcv_multi_year_lows_core24_2nd_v025_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_diff(volume, 4))
def cg_f087_ohlcv_multi_year_lows_core25_2nd_v026_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_diff(closeadj, 4))
def cg_f087_ohlcv_multi_year_lows_core26_2nd_v027_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_diff(closeunadj, 4))
def cg_f087_ohlcv_multi_year_lows_core27_2nd_v028_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_diff(_safe_div(close, open), 4))
def cg_f087_ohlcv_multi_year_lows_core28_2nd_v029_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_diff(_safe_div(high, low), 4))
def cg_f087_ohlcv_multi_year_lows_core29_2nd_v030_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_diff(_safe_div(volume, close), 4))
def cg_f087_ohlcv_multi_year_lows_core30_2nd_v031_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_slope(open, 4), 8))
def cg_f087_ohlcv_multi_year_lows_core31_2nd_v032_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_slope(high, 4), 8))
def cg_f087_ohlcv_multi_year_lows_core32_2nd_v033_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_slope(low, 4), 8))
def cg_f087_ohlcv_multi_year_lows_core33_2nd_v034_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_slope(close, 4), 8))
def cg_f087_ohlcv_multi_year_lows_core34_2nd_v035_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_slope(volume, 4), 8))
def cg_f087_ohlcv_multi_year_lows_core35_2nd_v036_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_slope(closeadj, 4), 8))
def cg_f087_ohlcv_multi_year_lows_core36_2nd_v037_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_slope(closeunadj, 4), 8))
def cg_f087_ohlcv_multi_year_lows_core37_2nd_v038_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_slope(_safe_div(close, open), 4), 8))
def cg_f087_ohlcv_multi_year_lows_core38_2nd_v039_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_slope(_safe_div(high, low), 4), 8))
def cg_f087_ohlcv_multi_year_lows_core39_2nd_v040_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_slope(_safe_div(volume, close), 4), 8))
def cg_f087_ohlcv_multi_year_lows_core40_2nd_v041_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_slope(open, 8), 12))
def cg_f087_ohlcv_multi_year_lows_core41_2nd_v042_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_slope(high, 8), 12))
def cg_f087_ohlcv_multi_year_lows_core42_2nd_v043_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_slope(low, 8), 12))
def cg_f087_ohlcv_multi_year_lows_core43_2nd_v044_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_slope(close, 8), 12))
def cg_f087_ohlcv_multi_year_lows_core44_2nd_v045_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_slope(volume, 8), 12))
def cg_f087_ohlcv_multi_year_lows_core45_2nd_v046_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_slope(closeadj, 8), 12))
def cg_f087_ohlcv_multi_year_lows_core46_2nd_v047_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_slope(closeunadj, 8), 12))
def cg_f087_ohlcv_multi_year_lows_core47_2nd_v048_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_slope(_safe_div(close, open), 8), 12))
def cg_f087_ohlcv_multi_year_lows_core48_2nd_v049_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_slope(_safe_div(high, low), 8), 12))
def cg_f087_ohlcv_multi_year_lows_core49_2nd_v050_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_slope(_safe_div(volume, close), 8), 12))
def cg_f087_ohlcv_multi_year_lows_core50_2nd_v051_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_diff(open, 4), 8))
def cg_f087_ohlcv_multi_year_lows_core51_2nd_v052_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_diff(high, 4), 8))
def cg_f087_ohlcv_multi_year_lows_core52_2nd_v053_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_diff(low, 4), 8))
def cg_f087_ohlcv_multi_year_lows_core53_2nd_v054_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_diff(close, 4), 8))
def cg_f087_ohlcv_multi_year_lows_core54_2nd_v055_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_diff(volume, 4), 8))
def cg_f087_ohlcv_multi_year_lows_core55_2nd_v056_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_diff(closeadj, 4), 8))
def cg_f087_ohlcv_multi_year_lows_core56_2nd_v057_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_diff(closeunadj, 4), 8))
def cg_f087_ohlcv_multi_year_lows_core57_2nd_v058_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_diff(_safe_div(close, open), 4), 8))
def cg_f087_ohlcv_multi_year_lows_core58_2nd_v059_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_diff(_safe_div(high, low), 4), 8))
def cg_f087_ohlcv_multi_year_lows_core59_2nd_v060_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_diff(_safe_div(volume, close), 4), 8))
def cg_f087_ohlcv_multi_year_lows_core60_2nd_v061_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(_slope(open, 4), 12))
def cg_f087_ohlcv_multi_year_lows_core61_2nd_v062_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(_slope(high, 4), 12))
def cg_f087_ohlcv_multi_year_lows_core62_2nd_v063_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(_slope(low, 4), 12))
def cg_f087_ohlcv_multi_year_lows_core63_2nd_v064_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(_slope(close, 4), 12))
def cg_f087_ohlcv_multi_year_lows_core64_2nd_v065_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(_slope(volume, 4), 12))
def cg_f087_ohlcv_multi_year_lows_core65_2nd_v066_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(_slope(closeadj, 4), 12))
def cg_f087_ohlcv_multi_year_lows_core66_2nd_v067_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(_slope(closeunadj, 4), 12))
def cg_f087_ohlcv_multi_year_lows_core67_2nd_v068_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(_slope(_safe_div(close, open), 4), 12))
def cg_f087_ohlcv_multi_year_lows_core68_2nd_v069_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(_slope(_safe_div(high, low), 4), 12))
def cg_f087_ohlcv_multi_year_lows_core69_2nd_v070_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(_slope(_safe_div(volume, close), 4), 12))
def cg_f087_ohlcv_multi_year_lows_core70_2nd_v071_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(_diff(open, 4), 12))
def cg_f087_ohlcv_multi_year_lows_core71_2nd_v072_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(_diff(high, 4), 12))
def cg_f087_ohlcv_multi_year_lows_core72_2nd_v073_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(_diff(low, 4), 12))
def cg_f087_ohlcv_multi_year_lows_core73_2nd_v074_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(_diff(close, 4), 12))
def cg_f087_ohlcv_multi_year_lows_core74_2nd_v075_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(_diff(volume, 4), 12))
def cg_f087_ohlcv_multi_year_lows_core75_2nd_v076_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(_diff(closeadj, 4), 12))
def cg_f087_ohlcv_multi_year_lows_core76_2nd_v077_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(_diff(closeunadj, 4), 12))
def cg_f087_ohlcv_multi_year_lows_core77_2nd_v078_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(_diff(_safe_div(close, open), 4), 12))
def cg_f087_ohlcv_multi_year_lows_core78_2nd_v079_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(_diff(_safe_div(high, low), 4), 12))
def cg_f087_ohlcv_multi_year_lows_core79_2nd_v080_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(_diff(_safe_div(volume, close), 4), 12))
def cg_f087_ohlcv_multi_year_lows_core80_2nd_v081_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(_slope(open, 4), 4))
def cg_f087_ohlcv_multi_year_lows_core81_2nd_v082_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(_slope(high, 4), 4))
def cg_f087_ohlcv_multi_year_lows_core82_2nd_v083_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(_slope(low, 4), 4))
def cg_f087_ohlcv_multi_year_lows_core83_2nd_v084_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(_slope(close, 4), 4))
def cg_f087_ohlcv_multi_year_lows_core84_2nd_v085_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(_slope(volume, 4), 4))
def cg_f087_ohlcv_multi_year_lows_core85_2nd_v086_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(_slope(closeadj, 4), 4))
def cg_f087_ohlcv_multi_year_lows_core86_2nd_v087_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(_slope(closeunadj, 4), 4))
def cg_f087_ohlcv_multi_year_lows_core87_2nd_v088_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(_slope(_safe_div(close, open), 4), 4))
def cg_f087_ohlcv_multi_year_lows_core88_2nd_v089_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(_slope(_safe_div(high, low), 4), 4))
def cg_f087_ohlcv_multi_year_lows_core89_2nd_v090_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(_slope(_safe_div(volume, close), 4), 4))
def cg_f087_ohlcv_multi_year_lows_core90_2nd_v091_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(_diff(open, 4), 4))
def cg_f087_ohlcv_multi_year_lows_core91_2nd_v092_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(_diff(high, 4), 4))
def cg_f087_ohlcv_multi_year_lows_core92_2nd_v093_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(_diff(low, 4), 4))
def cg_f087_ohlcv_multi_year_lows_core93_2nd_v094_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(_diff(close, 4), 4))
def cg_f087_ohlcv_multi_year_lows_core94_2nd_v095_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(_diff(volume, 4), 4))
def cg_f087_ohlcv_multi_year_lows_core95_2nd_v096_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(_diff(closeadj, 4), 4))
def cg_f087_ohlcv_multi_year_lows_core96_2nd_v097_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(_diff(closeunadj, 4), 4))
def cg_f087_ohlcv_multi_year_lows_core97_2nd_v098_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(_diff(_safe_div(close, open), 4), 4))
def cg_f087_ohlcv_multi_year_lows_core98_2nd_v099_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(_diff(_safe_div(high, low), 4), 4))
def cg_f087_ohlcv_multi_year_lows_core99_2nd_v100_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(_diff(_safe_div(volume, close), 4), 4))
def cg_f087_ohlcv_multi_year_lows_core100_2nd_v101_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(_mean(open, 4), 4))
def cg_f087_ohlcv_multi_year_lows_core101_2nd_v102_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(_mean(high, 4), 4))
def cg_f087_ohlcv_multi_year_lows_core102_2nd_v103_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(_mean(low, 4), 4))
def cg_f087_ohlcv_multi_year_lows_core103_2nd_v104_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(_mean(close, 4), 4))
def cg_f087_ohlcv_multi_year_lows_core104_2nd_v105_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(_mean(volume, 4), 4))
def cg_f087_ohlcv_multi_year_lows_core105_2nd_v106_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(_mean(closeadj, 4), 4))
def cg_f087_ohlcv_multi_year_lows_core106_2nd_v107_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(_mean(closeunadj, 4), 4))
def cg_f087_ohlcv_multi_year_lows_core107_2nd_v108_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(_mean(_safe_div(close, open), 4), 4))
def cg_f087_ohlcv_multi_year_lows_core108_2nd_v109_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(_mean(_safe_div(high, low), 4), 4))
def cg_f087_ohlcv_multi_year_lows_core109_2nd_v110_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(_mean(_safe_div(volume, close), 4), 4))
def cg_f087_ohlcv_multi_year_lows_core110_2nd_v111_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(_mean(open, 8), 8))
def cg_f087_ohlcv_multi_year_lows_core111_2nd_v112_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(_mean(high, 8), 8))
def cg_f087_ohlcv_multi_year_lows_core112_2nd_v113_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(_mean(low, 8), 8))
def cg_f087_ohlcv_multi_year_lows_core113_2nd_v114_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(_mean(close, 8), 8))
def cg_f087_ohlcv_multi_year_lows_core114_2nd_v115_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(_mean(volume, 8), 8))
def cg_f087_ohlcv_multi_year_lows_core115_2nd_v116_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(_mean(closeadj, 8), 8))
def cg_f087_ohlcv_multi_year_lows_core116_2nd_v117_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(_mean(closeunadj, 8), 8))
def cg_f087_ohlcv_multi_year_lows_core117_2nd_v118_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(_mean(_safe_div(close, open), 8), 8))
def cg_f087_ohlcv_multi_year_lows_core118_2nd_v119_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(_mean(_safe_div(high, low), 8), 8))
def cg_f087_ohlcv_multi_year_lows_core119_2nd_v120_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(_mean(_safe_div(volume, close), 8), 8))
def cg_f087_ohlcv_multi_year_lows_core120_2nd_v121_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_diff(_mean(open, 4), 4))
def cg_f087_ohlcv_multi_year_lows_core121_2nd_v122_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_diff(_mean(high, 4), 4))
def cg_f087_ohlcv_multi_year_lows_core122_2nd_v123_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_diff(_mean(low, 4), 4))
def cg_f087_ohlcv_multi_year_lows_core123_2nd_v124_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_diff(_mean(close, 4), 4))
def cg_f087_ohlcv_multi_year_lows_core124_2nd_v125_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_diff(_mean(volume, 4), 4))
def cg_f087_ohlcv_multi_year_lows_core125_2nd_v126_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_diff(_mean(closeadj, 4), 4))
def cg_f087_ohlcv_multi_year_lows_core126_2nd_v127_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_diff(_mean(closeunadj, 4), 4))
def cg_f087_ohlcv_multi_year_lows_core127_2nd_v128_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_diff(_mean(_safe_div(close, open), 4), 4))
def cg_f087_ohlcv_multi_year_lows_core128_2nd_v129_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_diff(_mean(_safe_div(high, low), 4), 4))
def cg_f087_ohlcv_multi_year_lows_core129_2nd_v130_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_diff(_mean(_safe_div(volume, close), 4), 4))
def cg_f087_ohlcv_multi_year_lows_core130_2nd_v131_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_diff(_mean(open, 4), 4), 8))
def cg_f087_ohlcv_multi_year_lows_core131_2nd_v132_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_diff(_mean(high, 4), 4), 8))
def cg_f087_ohlcv_multi_year_lows_core132_2nd_v133_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_diff(_mean(low, 4), 4), 8))
def cg_f087_ohlcv_multi_year_lows_core133_2nd_v134_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_diff(_mean(close, 4), 4), 8))
def cg_f087_ohlcv_multi_year_lows_core134_2nd_v135_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_diff(_mean(volume, 4), 4), 8))
def cg_f087_ohlcv_multi_year_lows_core135_2nd_v136_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_diff(_mean(closeadj, 4), 4), 8))
def cg_f087_ohlcv_multi_year_lows_core136_2nd_v137_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_diff(_mean(closeunadj, 4), 4), 8))
def cg_f087_ohlcv_multi_year_lows_core137_2nd_v138_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_diff(_mean(_safe_div(close, open), 4), 4), 8))
def cg_f087_ohlcv_multi_year_lows_core138_2nd_v139_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_diff(_mean(_safe_div(high, low), 4), 4), 8))
def cg_f087_ohlcv_multi_year_lows_core139_2nd_v140_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_diff(_mean(_safe_div(volume, close), 4), 4), 8))
def cg_f087_ohlcv_multi_year_lows_core140_2nd_v141_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(_slope(_mean(open, 4), 4), 12))
def cg_f087_ohlcv_multi_year_lows_core141_2nd_v142_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(_slope(_mean(high, 4), 4), 12))
def cg_f087_ohlcv_multi_year_lows_core142_2nd_v143_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(_slope(_mean(low, 4), 4), 12))
def cg_f087_ohlcv_multi_year_lows_core143_2nd_v144_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(_slope(_mean(close, 4), 4), 12))
def cg_f087_ohlcv_multi_year_lows_core144_2nd_v145_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(_slope(_mean(volume, 4), 4), 12))
def cg_f087_ohlcv_multi_year_lows_core145_2nd_v146_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(_slope(_mean(closeadj, 4), 4), 12))
def cg_f087_ohlcv_multi_year_lows_core146_2nd_v147_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(_slope(_mean(closeunadj, 4), 4), 12))
def cg_f087_ohlcv_multi_year_lows_core147_2nd_v148_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(_slope(_mean(_safe_div(close, open), 4), 4), 12))
def cg_f087_ohlcv_multi_year_lows_core148_2nd_v149_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(_slope(_mean(_safe_div(high, low), 4), 4), 12))
def cg_f087_ohlcv_multi_year_lows_core149_2nd_v150_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(_slope(_mean(_safe_div(volume, close), 4), 4), 12))