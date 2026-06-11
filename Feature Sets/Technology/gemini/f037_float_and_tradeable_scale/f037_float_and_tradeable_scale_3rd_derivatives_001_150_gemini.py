import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f037_float_and_tradeable_scale_core00_3rd_v001_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(_diff(sharesbas, 4), 4))
def cg_f037_float_and_tradeable_scale_core01_3rd_v002_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(_diff(volume, 4), 4))
def cg_f037_float_and_tradeable_scale_core02_3rd_v003_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(_diff(_safe_div(volume, sharesbas.abs() + 1.0), 4), 4))
def cg_f037_float_and_tradeable_scale_core03_3rd_v004_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(_diff(close, 4), 4))
def cg_f037_float_and_tradeable_scale_core04_3rd_v005_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(_diff(closeadj, 4), 4))
def cg_f037_float_and_tradeable_scale_core05_3rd_v006_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(_diff(_safe_div(close, closeadj.abs() + 0.001), 4), 4))
def cg_f037_float_and_tradeable_scale_core06_3rd_v007_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(_diff(volume * close, 4), 4))
def cg_f037_float_and_tradeable_scale_core07_3rd_v008_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(_diff(_log(volume + 1.0), 4), 4))
def cg_f037_float_and_tradeable_scale_core08_3rd_v009_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(_diff(_z(volume, 20), 4), 4))
def cg_f037_float_and_tradeable_scale_core09_3rd_v010_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(_diff(_slope(volume, 10), 4), 4))
def cg_f037_float_and_tradeable_scale_core10_3rd_v011_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_diff(sharesbas, 4), 8))
def cg_f037_float_and_tradeable_scale_core11_3rd_v012_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_diff(volume, 4), 8))
def cg_f037_float_and_tradeable_scale_core12_3rd_v013_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_diff(_safe_div(volume, sharesbas.abs() + 1.0), 4), 8))
def cg_f037_float_and_tradeable_scale_core13_3rd_v014_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_diff(close, 4), 8))
def cg_f037_float_and_tradeable_scale_core14_3rd_v015_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_diff(closeadj, 4), 8))
def cg_f037_float_and_tradeable_scale_core15_3rd_v016_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_diff(_safe_div(close, closeadj.abs() + 0.001), 4), 8))
def cg_f037_float_and_tradeable_scale_core16_3rd_v017_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_diff(volume * close, 4), 8))
def cg_f037_float_and_tradeable_scale_core17_3rd_v018_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_diff(_log(volume + 1.0), 4), 8))
def cg_f037_float_and_tradeable_scale_core18_3rd_v019_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_diff(_z(volume, 20), 4), 8))
def cg_f037_float_and_tradeable_scale_core19_3rd_v020_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_diff(_slope(volume, 10), 4), 8))
def cg_f037_float_and_tradeable_scale_core20_3rd_v021_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(_slope(sharesbas, 4), 4))
def cg_f037_float_and_tradeable_scale_core21_3rd_v022_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(_slope(volume, 4), 4))
def cg_f037_float_and_tradeable_scale_core22_3rd_v023_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(_slope(_safe_div(volume, sharesbas.abs() + 1.0), 4), 4))
def cg_f037_float_and_tradeable_scale_core23_3rd_v024_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(_slope(close, 4), 4))
def cg_f037_float_and_tradeable_scale_core24_3rd_v025_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(_slope(closeadj, 4), 4))
def cg_f037_float_and_tradeable_scale_core25_3rd_v026_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(_slope(_safe_div(close, closeadj.abs() + 0.001), 4), 4))
def cg_f037_float_and_tradeable_scale_core26_3rd_v027_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(_slope(volume * close, 4), 4))
def cg_f037_float_and_tradeable_scale_core27_3rd_v028_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(_slope(_log(volume + 1.0), 4), 4))
def cg_f037_float_and_tradeable_scale_core28_3rd_v029_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(_slope(_z(volume, 20), 4), 4))
def cg_f037_float_and_tradeable_scale_core29_3rd_v030_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(_slope(_slope(volume, 10), 4), 4))
def cg_f037_float_and_tradeable_scale_core30_3rd_v031_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_diff(_diff(sharesbas, 4), 4), 8))
def cg_f037_float_and_tradeable_scale_core31_3rd_v032_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_diff(_diff(volume, 4), 4), 8))
def cg_f037_float_and_tradeable_scale_core32_3rd_v033_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_diff(_diff(_safe_div(volume, sharesbas.abs() + 1.0), 4), 4), 8))
def cg_f037_float_and_tradeable_scale_core33_3rd_v034_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_diff(_diff(close, 4), 4), 8))
def cg_f037_float_and_tradeable_scale_core34_3rd_v035_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_diff(_diff(closeadj, 4), 4), 8))
def cg_f037_float_and_tradeable_scale_core35_3rd_v036_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_diff(_diff(_safe_div(close, closeadj.abs() + 0.001), 4), 4), 8))
def cg_f037_float_and_tradeable_scale_core36_3rd_v037_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_diff(_diff(volume * close, 4), 4), 8))
def cg_f037_float_and_tradeable_scale_core37_3rd_v038_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_diff(_diff(_log(volume + 1.0), 4), 4), 8))
def cg_f037_float_and_tradeable_scale_core38_3rd_v039_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_diff(_diff(_z(volume, 20), 4), 4), 8))
def cg_f037_float_and_tradeable_scale_core39_3rd_v040_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_diff(_diff(_slope(volume, 10), 4), 4), 8))
def cg_f037_float_and_tradeable_scale_core40_3rd_v041_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_slope(_diff(sharesbas, 4), 8), 12))
def cg_f037_float_and_tradeable_scale_core41_3rd_v042_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_slope(_diff(volume, 4), 8), 12))
def cg_f037_float_and_tradeable_scale_core42_3rd_v043_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_slope(_diff(_safe_div(volume, sharesbas.abs() + 1.0), 4), 8), 12))
def cg_f037_float_and_tradeable_scale_core43_3rd_v044_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_slope(_diff(close, 4), 8), 12))
def cg_f037_float_and_tradeable_scale_core44_3rd_v045_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_slope(_diff(closeadj, 4), 8), 12))
def cg_f037_float_and_tradeable_scale_core45_3rd_v046_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_slope(_diff(_safe_div(close, closeadj.abs() + 0.001), 4), 8), 12))
def cg_f037_float_and_tradeable_scale_core46_3rd_v047_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_slope(_diff(volume * close, 4), 8), 12))
def cg_f037_float_and_tradeable_scale_core47_3rd_v048_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_slope(_diff(_log(volume + 1.0), 4), 8), 12))
def cg_f037_float_and_tradeable_scale_core48_3rd_v049_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_slope(_diff(_z(volume, 20), 4), 8), 12))
def cg_f037_float_and_tradeable_scale_core49_3rd_v050_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_slope(_diff(_slope(volume, 10), 4), 8), 12))
def cg_f037_float_and_tradeable_scale_core50_3rd_v051_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_diff(_slope(sharesbas, 4), 4), 8))
def cg_f037_float_and_tradeable_scale_core51_3rd_v052_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_diff(_slope(volume, 4), 4), 8))
def cg_f037_float_and_tradeable_scale_core52_3rd_v053_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_diff(_slope(_safe_div(volume, sharesbas.abs() + 1.0), 4), 4), 8))
def cg_f037_float_and_tradeable_scale_core53_3rd_v054_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_diff(_slope(close, 4), 4), 8))
def cg_f037_float_and_tradeable_scale_core54_3rd_v055_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_diff(_slope(closeadj, 4), 4), 8))
def cg_f037_float_and_tradeable_scale_core55_3rd_v056_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_diff(_slope(_safe_div(close, closeadj.abs() + 0.001), 4), 4), 8))
def cg_f037_float_and_tradeable_scale_core56_3rd_v057_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_diff(_slope(volume * close, 4), 4), 8))
def cg_f037_float_and_tradeable_scale_core57_3rd_v058_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_diff(_slope(_log(volume + 1.0), 4), 4), 8))
def cg_f037_float_and_tradeable_scale_core58_3rd_v059_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_diff(_slope(_z(volume, 20), 4), 4), 8))
def cg_f037_float_and_tradeable_scale_core59_3rd_v060_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_diff(_slope(_slope(volume, 10), 4), 4), 8))
def cg_f037_float_and_tradeable_scale_core60_3rd_v061_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_diff(_diff(sharesbas, 4), 4), 12))
def cg_f037_float_and_tradeable_scale_core61_3rd_v062_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_diff(_diff(volume, 4), 4), 12))
def cg_f037_float_and_tradeable_scale_core62_3rd_v063_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_diff(_diff(_safe_div(volume, sharesbas.abs() + 1.0), 4), 4), 12))
def cg_f037_float_and_tradeable_scale_core63_3rd_v064_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_diff(_diff(close, 4), 4), 12))
def cg_f037_float_and_tradeable_scale_core64_3rd_v065_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_diff(_diff(closeadj, 4), 4), 12))
def cg_f037_float_and_tradeable_scale_core65_3rd_v066_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_diff(_diff(_safe_div(close, closeadj.abs() + 0.001), 4), 4), 12))
def cg_f037_float_and_tradeable_scale_core66_3rd_v067_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_diff(_diff(volume * close, 4), 4), 12))
def cg_f037_float_and_tradeable_scale_core67_3rd_v068_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_diff(_diff(_log(volume + 1.0), 4), 4), 12))
def cg_f037_float_and_tradeable_scale_core68_3rd_v069_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_diff(_diff(_z(volume, 20), 4), 4), 12))
def cg_f037_float_and_tradeable_scale_core69_3rd_v070_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_diff(_diff(_slope(volume, 10), 4), 4), 12))
def cg_f037_float_and_tradeable_scale_core70_3rd_v071_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_slope(_diff(sharesbas, 4), 8), 12))
def cg_f037_float_and_tradeable_scale_core71_3rd_v072_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_slope(_diff(volume, 4), 8), 12))
def cg_f037_float_and_tradeable_scale_core72_3rd_v073_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_slope(_diff(_safe_div(volume, sharesbas.abs() + 1.0), 4), 8), 12))
def cg_f037_float_and_tradeable_scale_core73_3rd_v074_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_slope(_diff(close, 4), 8), 12))
def cg_f037_float_and_tradeable_scale_core74_3rd_v075_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_slope(_diff(closeadj, 4), 8), 12))
def cg_f037_float_and_tradeable_scale_core75_3rd_v076_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_slope(_diff(_safe_div(close, closeadj.abs() + 0.001), 4), 8), 12))
def cg_f037_float_and_tradeable_scale_core76_3rd_v077_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_slope(_diff(volume * close, 4), 8), 12))
def cg_f037_float_and_tradeable_scale_core77_3rd_v078_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_slope(_diff(_log(volume + 1.0), 4), 8), 12))
def cg_f037_float_and_tradeable_scale_core78_3rd_v079_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_slope(_diff(_z(volume, 20), 4), 8), 12))
def cg_f037_float_and_tradeable_scale_core79_3rd_v080_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_slope(_diff(_slope(volume, 10), 4), 8), 12))
def cg_f037_float_and_tradeable_scale_core80_3rd_v081_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_diff(_slope(sharesbas, 4), 4), 12))
def cg_f037_float_and_tradeable_scale_core81_3rd_v082_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_diff(_slope(volume, 4), 4), 12))
def cg_f037_float_and_tradeable_scale_core82_3rd_v083_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_diff(_slope(_safe_div(volume, sharesbas.abs() + 1.0), 4), 4), 12))
def cg_f037_float_and_tradeable_scale_core83_3rd_v084_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_diff(_slope(close, 4), 4), 12))
def cg_f037_float_and_tradeable_scale_core84_3rd_v085_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_diff(_slope(closeadj, 4), 4), 12))
def cg_f037_float_and_tradeable_scale_core85_3rd_v086_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_diff(_slope(_safe_div(close, closeadj.abs() + 0.001), 4), 4), 12))
def cg_f037_float_and_tradeable_scale_core86_3rd_v087_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_diff(_slope(volume * close, 4), 4), 12))
def cg_f037_float_and_tradeable_scale_core87_3rd_v088_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_diff(_slope(_log(volume + 1.0), 4), 4), 12))
def cg_f037_float_and_tradeable_scale_core88_3rd_v089_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_diff(_slope(_z(volume, 20), 4), 4), 12))
def cg_f037_float_and_tradeable_scale_core89_3rd_v090_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_diff(_slope(_slope(volume, 10), 4), 4), 12))
def cg_f037_float_and_tradeable_scale_core90_3rd_v091_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_diff(_diff(sharesbas, 4), 4), 4))
def cg_f037_float_and_tradeable_scale_core91_3rd_v092_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_diff(_diff(volume, 4), 4), 4))
def cg_f037_float_and_tradeable_scale_core92_3rd_v093_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_diff(_diff(_safe_div(volume, sharesbas.abs() + 1.0), 4), 4), 4))
def cg_f037_float_and_tradeable_scale_core93_3rd_v094_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_diff(_diff(close, 4), 4), 4))
def cg_f037_float_and_tradeable_scale_core94_3rd_v095_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_diff(_diff(closeadj, 4), 4), 4))
def cg_f037_float_and_tradeable_scale_core95_3rd_v096_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_diff(_diff(_safe_div(close, closeadj.abs() + 0.001), 4), 4), 4))
def cg_f037_float_and_tradeable_scale_core96_3rd_v097_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_diff(_diff(volume * close, 4), 4), 4))
def cg_f037_float_and_tradeable_scale_core97_3rd_v098_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_diff(_diff(_log(volume + 1.0), 4), 4), 4))
def cg_f037_float_and_tradeable_scale_core98_3rd_v099_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_diff(_diff(_z(volume, 20), 4), 4), 4))
def cg_f037_float_and_tradeable_scale_core99_3rd_v100_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_diff(_diff(_slope(volume, 10), 4), 4), 4))
def cg_f037_float_and_tradeable_scale_core100_3rd_v101_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_slope(_diff(sharesbas, 4), 8), 4))
def cg_f037_float_and_tradeable_scale_core101_3rd_v102_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_slope(_diff(volume, 4), 8), 4))
def cg_f037_float_and_tradeable_scale_core102_3rd_v103_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_slope(_diff(_safe_div(volume, sharesbas.abs() + 1.0), 4), 8), 4))
def cg_f037_float_and_tradeable_scale_core103_3rd_v104_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_slope(_diff(close, 4), 8), 4))
def cg_f037_float_and_tradeable_scale_core104_3rd_v105_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_slope(_diff(closeadj, 4), 8), 4))
def cg_f037_float_and_tradeable_scale_core105_3rd_v106_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_slope(_diff(_safe_div(close, closeadj.abs() + 0.001), 4), 8), 4))
def cg_f037_float_and_tradeable_scale_core106_3rd_v107_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_slope(_diff(volume * close, 4), 8), 4))
def cg_f037_float_and_tradeable_scale_core107_3rd_v108_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_slope(_diff(_log(volume + 1.0), 4), 8), 4))
def cg_f037_float_and_tradeable_scale_core108_3rd_v109_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_slope(_diff(_z(volume, 20), 4), 8), 4))
def cg_f037_float_and_tradeable_scale_core109_3rd_v110_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_slope(_diff(_slope(volume, 10), 4), 8), 4))
def cg_f037_float_and_tradeable_scale_core110_3rd_v111_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_diff(_slope(sharesbas, 4), 4), 4))
def cg_f037_float_and_tradeable_scale_core111_3rd_v112_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_diff(_slope(volume, 4), 4), 4))
def cg_f037_float_and_tradeable_scale_core112_3rd_v113_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_diff(_slope(_safe_div(volume, sharesbas.abs() + 1.0), 4), 4), 4))
def cg_f037_float_and_tradeable_scale_core113_3rd_v114_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_diff(_slope(close, 4), 4), 4))
def cg_f037_float_and_tradeable_scale_core114_3rd_v115_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_diff(_slope(closeadj, 4), 4), 4))
def cg_f037_float_and_tradeable_scale_core115_3rd_v116_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_diff(_slope(_safe_div(close, closeadj.abs() + 0.001), 4), 4), 4))
def cg_f037_float_and_tradeable_scale_core116_3rd_v117_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_diff(_slope(volume * close, 4), 4), 4))
def cg_f037_float_and_tradeable_scale_core117_3rd_v118_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_diff(_slope(_log(volume + 1.0), 4), 4), 4))
def cg_f037_float_and_tradeable_scale_core118_3rd_v119_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_diff(_slope(_z(volume, 20), 4), 4), 4))
def cg_f037_float_and_tradeable_scale_core119_3rd_v120_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_diff(_slope(_slope(volume, 10), 4), 4), 4))
def cg_f037_float_and_tradeable_scale_core120_3rd_v121_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_diff(_diff(sharesbas, 4), 4), 4))
def cg_f037_float_and_tradeable_scale_core121_3rd_v122_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_diff(_diff(volume, 4), 4), 4))
def cg_f037_float_and_tradeable_scale_core122_3rd_v123_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_diff(_diff(_safe_div(volume, sharesbas.abs() + 1.0), 4), 4), 4))
def cg_f037_float_and_tradeable_scale_core123_3rd_v124_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_diff(_diff(close, 4), 4), 4))
def cg_f037_float_and_tradeable_scale_core124_3rd_v125_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_diff(_diff(closeadj, 4), 4), 4))
def cg_f037_float_and_tradeable_scale_core125_3rd_v126_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_diff(_diff(_safe_div(close, closeadj.abs() + 0.001), 4), 4), 4))
def cg_f037_float_and_tradeable_scale_core126_3rd_v127_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_diff(_diff(volume * close, 4), 4), 4))
def cg_f037_float_and_tradeable_scale_core127_3rd_v128_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_diff(_diff(_log(volume + 1.0), 4), 4), 4))
def cg_f037_float_and_tradeable_scale_core128_3rd_v129_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_diff(_diff(_z(volume, 20), 4), 4), 4))
def cg_f037_float_and_tradeable_scale_core129_3rd_v130_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_diff(_diff(_slope(volume, 10), 4), 4), 4))
def cg_f037_float_and_tradeable_scale_core130_3rd_v131_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(_diff(_diff(sharesbas, 4), 4), 4))
def cg_f037_float_and_tradeable_scale_core131_3rd_v132_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(_diff(_diff(volume, 4), 4), 4))
def cg_f037_float_and_tradeable_scale_core132_3rd_v133_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(_diff(_diff(_safe_div(volume, sharesbas.abs() + 1.0), 4), 4), 4))
def cg_f037_float_and_tradeable_scale_core133_3rd_v134_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(_diff(_diff(close, 4), 4), 4))
def cg_f037_float_and_tradeable_scale_core134_3rd_v135_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(_diff(_diff(closeadj, 4), 4), 4))
def cg_f037_float_and_tradeable_scale_core135_3rd_v136_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(_diff(_diff(_safe_div(close, closeadj.abs() + 0.001), 4), 4), 4))
def cg_f037_float_and_tradeable_scale_core136_3rd_v137_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(_diff(_diff(volume * close, 4), 4), 4))
def cg_f037_float_and_tradeable_scale_core137_3rd_v138_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(_diff(_diff(_log(volume + 1.0), 4), 4), 4))
def cg_f037_float_and_tradeable_scale_core138_3rd_v139_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(_diff(_diff(_z(volume, 20), 4), 4), 4))
def cg_f037_float_and_tradeable_scale_core139_3rd_v140_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(_diff(_diff(_slope(volume, 10), 4), 4), 4))
def cg_f037_float_and_tradeable_scale_core140_3rd_v141_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_slope(_diff(_diff(sharesbas, 4), 4), 4), 8))
def cg_f037_float_and_tradeable_scale_core141_3rd_v142_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_slope(_diff(_diff(volume, 4), 4), 4), 8))
def cg_f037_float_and_tradeable_scale_core142_3rd_v143_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_slope(_diff(_diff(_safe_div(volume, sharesbas.abs() + 1.0), 4), 4), 4), 8))
def cg_f037_float_and_tradeable_scale_core143_3rd_v144_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_slope(_diff(_diff(close, 4), 4), 4), 8))
def cg_f037_float_and_tradeable_scale_core144_3rd_v145_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_slope(_diff(_diff(closeadj, 4), 4), 4), 8))
def cg_f037_float_and_tradeable_scale_core145_3rd_v146_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_slope(_diff(_diff(_safe_div(close, closeadj.abs() + 0.001), 4), 4), 4), 8))
def cg_f037_float_and_tradeable_scale_core146_3rd_v147_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_slope(_diff(_diff(volume * close, 4), 4), 4), 8))
def cg_f037_float_and_tradeable_scale_core147_3rd_v148_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_slope(_diff(_diff(_log(volume + 1.0), 4), 4), 4), 8))
def cg_f037_float_and_tradeable_scale_core148_3rd_v149_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_slope(_diff(_diff(_z(volume, 20), 4), 4), 4), 8))
def cg_f037_float_and_tradeable_scale_core149_3rd_v150_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_slope(_diff(_diff(_slope(volume, 10), 4), 4), 4), 8))