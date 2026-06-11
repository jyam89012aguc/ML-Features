import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f037_float_and_tradeable_scale_core00_2nd_v001_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(sharesbas, 4))
def cg_f037_float_and_tradeable_scale_core01_2nd_v002_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(volume, 4))
def cg_f037_float_and_tradeable_scale_core02_2nd_v003_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_safe_div(volume, sharesbas.abs() + 1.0), 4))
def cg_f037_float_and_tradeable_scale_core03_2nd_v004_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(close, 4))
def cg_f037_float_and_tradeable_scale_core04_2nd_v005_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(closeadj, 4))
def cg_f037_float_and_tradeable_scale_core05_2nd_v006_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_safe_div(close, closeadj.abs() + 0.001), 4))
def cg_f037_float_and_tradeable_scale_core06_2nd_v007_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(volume * close, 4))
def cg_f037_float_and_tradeable_scale_core07_2nd_v008_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_log(volume + 1.0), 4))
def cg_f037_float_and_tradeable_scale_core08_2nd_v009_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_z(volume, 20), 4))
def cg_f037_float_and_tradeable_scale_core09_2nd_v010_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_slope(volume, 10), 4))
def cg_f037_float_and_tradeable_scale_core10_2nd_v011_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(sharesbas, 8))
def cg_f037_float_and_tradeable_scale_core11_2nd_v012_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(volume, 8))
def cg_f037_float_and_tradeable_scale_core12_2nd_v013_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_safe_div(volume, sharesbas.abs() + 1.0), 8))
def cg_f037_float_and_tradeable_scale_core13_2nd_v014_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(close, 8))
def cg_f037_float_and_tradeable_scale_core14_2nd_v015_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(closeadj, 8))
def cg_f037_float_and_tradeable_scale_core15_2nd_v016_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_safe_div(close, closeadj.abs() + 0.001), 8))
def cg_f037_float_and_tradeable_scale_core16_2nd_v017_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(volume * close, 8))
def cg_f037_float_and_tradeable_scale_core17_2nd_v018_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_log(volume + 1.0), 8))
def cg_f037_float_and_tradeable_scale_core18_2nd_v019_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_z(volume, 20), 8))
def cg_f037_float_and_tradeable_scale_core19_2nd_v020_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_slope(volume, 10), 8))
def cg_f037_float_and_tradeable_scale_core20_2nd_v021_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(sharesbas, 4))
def cg_f037_float_and_tradeable_scale_core21_2nd_v022_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(volume, 4))
def cg_f037_float_and_tradeable_scale_core22_2nd_v023_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(_safe_div(volume, sharesbas.abs() + 1.0), 4))
def cg_f037_float_and_tradeable_scale_core23_2nd_v024_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(close, 4))
def cg_f037_float_and_tradeable_scale_core24_2nd_v025_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(closeadj, 4))
def cg_f037_float_and_tradeable_scale_core25_2nd_v026_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(_safe_div(close, closeadj.abs() + 0.001), 4))
def cg_f037_float_and_tradeable_scale_core26_2nd_v027_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(volume * close, 4))
def cg_f037_float_and_tradeable_scale_core27_2nd_v028_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(_log(volume + 1.0), 4))
def cg_f037_float_and_tradeable_scale_core28_2nd_v029_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(_z(volume, 20), 4))
def cg_f037_float_and_tradeable_scale_core29_2nd_v030_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(_slope(volume, 10), 4))
def cg_f037_float_and_tradeable_scale_core30_2nd_v031_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_slope(sharesbas, 4), 8))
def cg_f037_float_and_tradeable_scale_core31_2nd_v032_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_slope(volume, 4), 8))
def cg_f037_float_and_tradeable_scale_core32_2nd_v033_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_slope(_safe_div(volume, sharesbas.abs() + 1.0), 4), 8))
def cg_f037_float_and_tradeable_scale_core33_2nd_v034_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_slope(close, 4), 8))
def cg_f037_float_and_tradeable_scale_core34_2nd_v035_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_slope(closeadj, 4), 8))
def cg_f037_float_and_tradeable_scale_core35_2nd_v036_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_slope(_safe_div(close, closeadj.abs() + 0.001), 4), 8))
def cg_f037_float_and_tradeable_scale_core36_2nd_v037_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_slope(volume * close, 4), 8))
def cg_f037_float_and_tradeable_scale_core37_2nd_v038_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_slope(_log(volume + 1.0), 4), 8))
def cg_f037_float_and_tradeable_scale_core38_2nd_v039_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_slope(_z(volume, 20), 4), 8))
def cg_f037_float_and_tradeable_scale_core39_2nd_v040_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_slope(_slope(volume, 10), 4), 8))
def cg_f037_float_and_tradeable_scale_core40_2nd_v041_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_slope(sharesbas, 8), 12))
def cg_f037_float_and_tradeable_scale_core41_2nd_v042_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_slope(volume, 8), 12))
def cg_f037_float_and_tradeable_scale_core42_2nd_v043_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_slope(_safe_div(volume, sharesbas.abs() + 1.0), 8), 12))
def cg_f037_float_and_tradeable_scale_core43_2nd_v044_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_slope(close, 8), 12))
def cg_f037_float_and_tradeable_scale_core44_2nd_v045_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_slope(closeadj, 8), 12))
def cg_f037_float_and_tradeable_scale_core45_2nd_v046_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_slope(_safe_div(close, closeadj.abs() + 0.001), 8), 12))
def cg_f037_float_and_tradeable_scale_core46_2nd_v047_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_slope(volume * close, 8), 12))
def cg_f037_float_and_tradeable_scale_core47_2nd_v048_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_slope(_log(volume + 1.0), 8), 12))
def cg_f037_float_and_tradeable_scale_core48_2nd_v049_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_slope(_z(volume, 20), 8), 12))
def cg_f037_float_and_tradeable_scale_core49_2nd_v050_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_slope(_slope(volume, 10), 8), 12))
def cg_f037_float_and_tradeable_scale_core50_2nd_v051_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_diff(sharesbas, 4), 8))
def cg_f037_float_and_tradeable_scale_core51_2nd_v052_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_diff(volume, 4), 8))
def cg_f037_float_and_tradeable_scale_core52_2nd_v053_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_diff(_safe_div(volume, sharesbas.abs() + 1.0), 4), 8))
def cg_f037_float_and_tradeable_scale_core53_2nd_v054_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_diff(close, 4), 8))
def cg_f037_float_and_tradeable_scale_core54_2nd_v055_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_diff(closeadj, 4), 8))
def cg_f037_float_and_tradeable_scale_core55_2nd_v056_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_diff(_safe_div(close, closeadj.abs() + 0.001), 4), 8))
def cg_f037_float_and_tradeable_scale_core56_2nd_v057_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_diff(volume * close, 4), 8))
def cg_f037_float_and_tradeable_scale_core57_2nd_v058_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_diff(_log(volume + 1.0), 4), 8))
def cg_f037_float_and_tradeable_scale_core58_2nd_v059_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_diff(_z(volume, 20), 4), 8))
def cg_f037_float_and_tradeable_scale_core59_2nd_v060_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_diff(_slope(volume, 10), 4), 8))
def cg_f037_float_and_tradeable_scale_core60_2nd_v061_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_slope(sharesbas, 4), 12))
def cg_f037_float_and_tradeable_scale_core61_2nd_v062_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_slope(volume, 4), 12))
def cg_f037_float_and_tradeable_scale_core62_2nd_v063_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_slope(_safe_div(volume, sharesbas.abs() + 1.0), 4), 12))
def cg_f037_float_and_tradeable_scale_core63_2nd_v064_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_slope(close, 4), 12))
def cg_f037_float_and_tradeable_scale_core64_2nd_v065_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_slope(closeadj, 4), 12))
def cg_f037_float_and_tradeable_scale_core65_2nd_v066_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_slope(_safe_div(close, closeadj.abs() + 0.001), 4), 12))
def cg_f037_float_and_tradeable_scale_core66_2nd_v067_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_slope(volume * close, 4), 12))
def cg_f037_float_and_tradeable_scale_core67_2nd_v068_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_slope(_log(volume + 1.0), 4), 12))
def cg_f037_float_and_tradeable_scale_core68_2nd_v069_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_slope(_z(volume, 20), 4), 12))
def cg_f037_float_and_tradeable_scale_core69_2nd_v070_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_slope(_slope(volume, 10), 4), 12))
def cg_f037_float_and_tradeable_scale_core70_2nd_v071_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_diff(sharesbas, 4), 12))
def cg_f037_float_and_tradeable_scale_core71_2nd_v072_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_diff(volume, 4), 12))
def cg_f037_float_and_tradeable_scale_core72_2nd_v073_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_diff(_safe_div(volume, sharesbas.abs() + 1.0), 4), 12))
def cg_f037_float_and_tradeable_scale_core73_2nd_v074_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_diff(close, 4), 12))
def cg_f037_float_and_tradeable_scale_core74_2nd_v075_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_diff(closeadj, 4), 12))
def cg_f037_float_and_tradeable_scale_core75_2nd_v076_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_diff(_safe_div(close, closeadj.abs() + 0.001), 4), 12))
def cg_f037_float_and_tradeable_scale_core76_2nd_v077_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_diff(volume * close, 4), 12))
def cg_f037_float_and_tradeable_scale_core77_2nd_v078_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_diff(_log(volume + 1.0), 4), 12))
def cg_f037_float_and_tradeable_scale_core78_2nd_v079_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_diff(_z(volume, 20), 4), 12))
def cg_f037_float_and_tradeable_scale_core79_2nd_v080_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_diff(_slope(volume, 10), 4), 12))
def cg_f037_float_and_tradeable_scale_core80_2nd_v081_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_slope(sharesbas, 4), 4))
def cg_f037_float_and_tradeable_scale_core81_2nd_v082_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_slope(volume, 4), 4))
def cg_f037_float_and_tradeable_scale_core82_2nd_v083_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_slope(_safe_div(volume, sharesbas.abs() + 1.0), 4), 4))
def cg_f037_float_and_tradeable_scale_core83_2nd_v084_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_slope(close, 4), 4))
def cg_f037_float_and_tradeable_scale_core84_2nd_v085_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_slope(closeadj, 4), 4))
def cg_f037_float_and_tradeable_scale_core85_2nd_v086_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_slope(_safe_div(close, closeadj.abs() + 0.001), 4), 4))
def cg_f037_float_and_tradeable_scale_core86_2nd_v087_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_slope(volume * close, 4), 4))
def cg_f037_float_and_tradeable_scale_core87_2nd_v088_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_slope(_log(volume + 1.0), 4), 4))
def cg_f037_float_and_tradeable_scale_core88_2nd_v089_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_slope(_z(volume, 20), 4), 4))
def cg_f037_float_and_tradeable_scale_core89_2nd_v090_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_slope(_slope(volume, 10), 4), 4))
def cg_f037_float_and_tradeable_scale_core90_2nd_v091_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_diff(sharesbas, 4), 4))
def cg_f037_float_and_tradeable_scale_core91_2nd_v092_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_diff(volume, 4), 4))
def cg_f037_float_and_tradeable_scale_core92_2nd_v093_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_diff(_safe_div(volume, sharesbas.abs() + 1.0), 4), 4))
def cg_f037_float_and_tradeable_scale_core93_2nd_v094_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_diff(close, 4), 4))
def cg_f037_float_and_tradeable_scale_core94_2nd_v095_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_diff(closeadj, 4), 4))
def cg_f037_float_and_tradeable_scale_core95_2nd_v096_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_diff(_safe_div(close, closeadj.abs() + 0.001), 4), 4))
def cg_f037_float_and_tradeable_scale_core96_2nd_v097_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_diff(volume * close, 4), 4))
def cg_f037_float_and_tradeable_scale_core97_2nd_v098_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_diff(_log(volume + 1.0), 4), 4))
def cg_f037_float_and_tradeable_scale_core98_2nd_v099_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_diff(_z(volume, 20), 4), 4))
def cg_f037_float_and_tradeable_scale_core99_2nd_v100_signal(sharesbas, volume, close, closeadj):
    return _clean(_mean(_diff(_slope(volume, 10), 4), 4))
def cg_f037_float_and_tradeable_scale_core100_2nd_v101_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_mean(sharesbas, 4), 4))
def cg_f037_float_and_tradeable_scale_core101_2nd_v102_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_mean(volume, 4), 4))
def cg_f037_float_and_tradeable_scale_core102_2nd_v103_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_mean(_safe_div(volume, sharesbas.abs() + 1.0), 4), 4))
def cg_f037_float_and_tradeable_scale_core103_2nd_v104_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_mean(close, 4), 4))
def cg_f037_float_and_tradeable_scale_core104_2nd_v105_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_mean(closeadj, 4), 4))
def cg_f037_float_and_tradeable_scale_core105_2nd_v106_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_mean(_safe_div(close, closeadj.abs() + 0.001), 4), 4))
def cg_f037_float_and_tradeable_scale_core106_2nd_v107_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_mean(volume * close, 4), 4))
def cg_f037_float_and_tradeable_scale_core107_2nd_v108_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_mean(_log(volume + 1.0), 4), 4))
def cg_f037_float_and_tradeable_scale_core108_2nd_v109_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_mean(_z(volume, 20), 4), 4))
def cg_f037_float_and_tradeable_scale_core109_2nd_v110_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_mean(_slope(volume, 10), 4), 4))
def cg_f037_float_and_tradeable_scale_core110_2nd_v111_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_mean(sharesbas, 8), 8))
def cg_f037_float_and_tradeable_scale_core111_2nd_v112_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_mean(volume, 8), 8))
def cg_f037_float_and_tradeable_scale_core112_2nd_v113_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_mean(_safe_div(volume, sharesbas.abs() + 1.0), 8), 8))
def cg_f037_float_and_tradeable_scale_core113_2nd_v114_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_mean(close, 8), 8))
def cg_f037_float_and_tradeable_scale_core114_2nd_v115_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_mean(closeadj, 8), 8))
def cg_f037_float_and_tradeable_scale_core115_2nd_v116_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_mean(_safe_div(close, closeadj.abs() + 0.001), 8), 8))
def cg_f037_float_and_tradeable_scale_core116_2nd_v117_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_mean(volume * close, 8), 8))
def cg_f037_float_and_tradeable_scale_core117_2nd_v118_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_mean(_log(volume + 1.0), 8), 8))
def cg_f037_float_and_tradeable_scale_core118_2nd_v119_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_mean(_z(volume, 20), 8), 8))
def cg_f037_float_and_tradeable_scale_core119_2nd_v120_signal(sharesbas, volume, close, closeadj):
    return _clean(_slope(_mean(_slope(volume, 10), 8), 8))
def cg_f037_float_and_tradeable_scale_core120_2nd_v121_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(_mean(sharesbas, 4), 4))
def cg_f037_float_and_tradeable_scale_core121_2nd_v122_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(_mean(volume, 4), 4))
def cg_f037_float_and_tradeable_scale_core122_2nd_v123_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(_mean(_safe_div(volume, sharesbas.abs() + 1.0), 4), 4))
def cg_f037_float_and_tradeable_scale_core123_2nd_v124_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(_mean(close, 4), 4))
def cg_f037_float_and_tradeable_scale_core124_2nd_v125_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(_mean(closeadj, 4), 4))
def cg_f037_float_and_tradeable_scale_core125_2nd_v126_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(_mean(_safe_div(close, closeadj.abs() + 0.001), 4), 4))
def cg_f037_float_and_tradeable_scale_core126_2nd_v127_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(_mean(volume * close, 4), 4))
def cg_f037_float_and_tradeable_scale_core127_2nd_v128_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(_mean(_log(volume + 1.0), 4), 4))
def cg_f037_float_and_tradeable_scale_core128_2nd_v129_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(_mean(_z(volume, 20), 4), 4))
def cg_f037_float_and_tradeable_scale_core129_2nd_v130_signal(sharesbas, volume, close, closeadj):
    return _clean(_diff(_mean(_slope(volume, 10), 4), 4))
def cg_f037_float_and_tradeable_scale_core130_2nd_v131_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_diff(_mean(sharesbas, 4), 4), 8))
def cg_f037_float_and_tradeable_scale_core131_2nd_v132_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_diff(_mean(volume, 4), 4), 8))
def cg_f037_float_and_tradeable_scale_core132_2nd_v133_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_diff(_mean(_safe_div(volume, sharesbas.abs() + 1.0), 4), 4), 8))
def cg_f037_float_and_tradeable_scale_core133_2nd_v134_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_diff(_mean(close, 4), 4), 8))
def cg_f037_float_and_tradeable_scale_core134_2nd_v135_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_diff(_mean(closeadj, 4), 4), 8))
def cg_f037_float_and_tradeable_scale_core135_2nd_v136_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_diff(_mean(_safe_div(close, closeadj.abs() + 0.001), 4), 4), 8))
def cg_f037_float_and_tradeable_scale_core136_2nd_v137_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_diff(_mean(volume * close, 4), 4), 8))
def cg_f037_float_and_tradeable_scale_core137_2nd_v138_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_diff(_mean(_log(volume + 1.0), 4), 4), 8))
def cg_f037_float_and_tradeable_scale_core138_2nd_v139_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_diff(_mean(_z(volume, 20), 4), 4), 8))
def cg_f037_float_and_tradeable_scale_core139_2nd_v140_signal(sharesbas, volume, close, closeadj):
    return _clean(_z(_diff(_mean(_slope(volume, 10), 4), 4), 8))
def cg_f037_float_and_tradeable_scale_core140_2nd_v141_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_slope(_mean(sharesbas, 4), 4), 12))
def cg_f037_float_and_tradeable_scale_core141_2nd_v142_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_slope(_mean(volume, 4), 4), 12))
def cg_f037_float_and_tradeable_scale_core142_2nd_v143_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_slope(_mean(_safe_div(volume, sharesbas.abs() + 1.0), 4), 4), 12))
def cg_f037_float_and_tradeable_scale_core143_2nd_v144_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_slope(_mean(close, 4), 4), 12))
def cg_f037_float_and_tradeable_scale_core144_2nd_v145_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_slope(_mean(closeadj, 4), 4), 12))
def cg_f037_float_and_tradeable_scale_core145_2nd_v146_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_slope(_mean(_safe_div(close, closeadj.abs() + 0.001), 4), 4), 12))
def cg_f037_float_and_tradeable_scale_core146_2nd_v147_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_slope(_mean(volume * close, 4), 4), 12))
def cg_f037_float_and_tradeable_scale_core147_2nd_v148_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_slope(_mean(_log(volume + 1.0), 4), 4), 12))
def cg_f037_float_and_tradeable_scale_core148_2nd_v149_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_slope(_mean(_z(volume, 20), 4), 4), 12))
def cg_f037_float_and_tradeable_scale_core149_2nd_v150_signal(sharesbas, volume, close, closeadj):
    return _clean(_rank(_slope(_mean(_slope(volume, 10), 4), 4), 12))