import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f098_corporate_action_events_core00_2nd_v001_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(value, 4))
def cg_f098_corporate_action_events_core01_2nd_v002_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(value.abs(), 4))
def cg_f098_corporate_action_events_core02_2nd_v003_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(_log(value.abs() + 1.0), 4))
def cg_f098_corporate_action_events_core03_2nd_v004_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(_to_num(value), 4))
def cg_f098_corporate_action_events_core04_2nd_v005_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(value * 1.0, 4))
def cg_f098_corporate_action_events_core05_2nd_v006_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(value + 0.0, 4))
def cg_f098_corporate_action_events_core06_2nd_v007_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(value / 1.0, 4))
def cg_f098_corporate_action_events_core07_2nd_v008_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(_clean(value), 4))
def cg_f098_corporate_action_events_core08_2nd_v009_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(value * value, 4))
def cg_f098_corporate_action_events_core09_2nd_v010_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(_safe_div(1.0, value.abs() + 1.0), 4))
def cg_f098_corporate_action_events_core10_2nd_v011_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(value, 8))
def cg_f098_corporate_action_events_core11_2nd_v012_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(value.abs(), 8))
def cg_f098_corporate_action_events_core12_2nd_v013_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(_log(value.abs() + 1.0), 8))
def cg_f098_corporate_action_events_core13_2nd_v014_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(_to_num(value), 8))
def cg_f098_corporate_action_events_core14_2nd_v015_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(value * 1.0, 8))
def cg_f098_corporate_action_events_core15_2nd_v016_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(value + 0.0, 8))
def cg_f098_corporate_action_events_core16_2nd_v017_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(value / 1.0, 8))
def cg_f098_corporate_action_events_core17_2nd_v018_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(_clean(value), 8))
def cg_f098_corporate_action_events_core18_2nd_v019_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(value * value, 8))
def cg_f098_corporate_action_events_core19_2nd_v020_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(_safe_div(1.0, value.abs() + 1.0), 8))
def cg_f098_corporate_action_events_core20_2nd_v021_signal(date, action, value, name, contraticker, contraname):
    return _clean(_diff(value, 4))
def cg_f098_corporate_action_events_core21_2nd_v022_signal(date, action, value, name, contraticker, contraname):
    return _clean(_diff(value.abs(), 4))
def cg_f098_corporate_action_events_core22_2nd_v023_signal(date, action, value, name, contraticker, contraname):
    return _clean(_diff(_log(value.abs() + 1.0), 4))
def cg_f098_corporate_action_events_core23_2nd_v024_signal(date, action, value, name, contraticker, contraname):
    return _clean(_diff(_to_num(value), 4))
def cg_f098_corporate_action_events_core24_2nd_v025_signal(date, action, value, name, contraticker, contraname):
    return _clean(_diff(value * 1.0, 4))
def cg_f098_corporate_action_events_core25_2nd_v026_signal(date, action, value, name, contraticker, contraname):
    return _clean(_diff(value + 0.0, 4))
def cg_f098_corporate_action_events_core26_2nd_v027_signal(date, action, value, name, contraticker, contraname):
    return _clean(_diff(value / 1.0, 4))
def cg_f098_corporate_action_events_core27_2nd_v028_signal(date, action, value, name, contraticker, contraname):
    return _clean(_diff(_clean(value), 4))
def cg_f098_corporate_action_events_core28_2nd_v029_signal(date, action, value, name, contraticker, contraname):
    return _clean(_diff(value * value, 4))
def cg_f098_corporate_action_events_core29_2nd_v030_signal(date, action, value, name, contraticker, contraname):
    return _clean(_diff(_safe_div(1.0, value.abs() + 1.0), 4))
def cg_f098_corporate_action_events_core30_2nd_v031_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_slope(value, 4), 8))
def cg_f098_corporate_action_events_core31_2nd_v032_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_slope(value.abs(), 4), 8))
def cg_f098_corporate_action_events_core32_2nd_v033_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_slope(_log(value.abs() + 1.0), 4), 8))
def cg_f098_corporate_action_events_core33_2nd_v034_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_slope(_to_num(value), 4), 8))
def cg_f098_corporate_action_events_core34_2nd_v035_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_slope(value * 1.0, 4), 8))
def cg_f098_corporate_action_events_core35_2nd_v036_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_slope(value + 0.0, 4), 8))
def cg_f098_corporate_action_events_core36_2nd_v037_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_slope(value / 1.0, 4), 8))
def cg_f098_corporate_action_events_core37_2nd_v038_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_slope(_clean(value), 4), 8))
def cg_f098_corporate_action_events_core38_2nd_v039_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_slope(value * value, 4), 8))
def cg_f098_corporate_action_events_core39_2nd_v040_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_slope(_safe_div(1.0, value.abs() + 1.0), 4), 8))
def cg_f098_corporate_action_events_core40_2nd_v041_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_slope(value, 8), 12))
def cg_f098_corporate_action_events_core41_2nd_v042_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_slope(value.abs(), 8), 12))
def cg_f098_corporate_action_events_core42_2nd_v043_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_slope(_log(value.abs() + 1.0), 8), 12))
def cg_f098_corporate_action_events_core43_2nd_v044_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_slope(_to_num(value), 8), 12))
def cg_f098_corporate_action_events_core44_2nd_v045_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_slope(value * 1.0, 8), 12))
def cg_f098_corporate_action_events_core45_2nd_v046_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_slope(value + 0.0, 8), 12))
def cg_f098_corporate_action_events_core46_2nd_v047_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_slope(value / 1.0, 8), 12))
def cg_f098_corporate_action_events_core47_2nd_v048_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_slope(_clean(value), 8), 12))
def cg_f098_corporate_action_events_core48_2nd_v049_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_slope(value * value, 8), 12))
def cg_f098_corporate_action_events_core49_2nd_v050_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_slope(_safe_div(1.0, value.abs() + 1.0), 8), 12))
def cg_f098_corporate_action_events_core50_2nd_v051_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_diff(value, 4), 8))
def cg_f098_corporate_action_events_core51_2nd_v052_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_diff(value.abs(), 4), 8))
def cg_f098_corporate_action_events_core52_2nd_v053_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_diff(_log(value.abs() + 1.0), 4), 8))
def cg_f098_corporate_action_events_core53_2nd_v054_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_diff(_to_num(value), 4), 8))
def cg_f098_corporate_action_events_core54_2nd_v055_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_diff(value * 1.0, 4), 8))
def cg_f098_corporate_action_events_core55_2nd_v056_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_diff(value + 0.0, 4), 8))
def cg_f098_corporate_action_events_core56_2nd_v057_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_diff(value / 1.0, 4), 8))
def cg_f098_corporate_action_events_core57_2nd_v058_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_diff(_clean(value), 4), 8))
def cg_f098_corporate_action_events_core58_2nd_v059_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_diff(value * value, 4), 8))
def cg_f098_corporate_action_events_core59_2nd_v060_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_diff(_safe_div(1.0, value.abs() + 1.0), 4), 8))
def cg_f098_corporate_action_events_core60_2nd_v061_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_slope(value, 4), 12))
def cg_f098_corporate_action_events_core61_2nd_v062_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_slope(value.abs(), 4), 12))
def cg_f098_corporate_action_events_core62_2nd_v063_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_slope(_log(value.abs() + 1.0), 4), 12))
def cg_f098_corporate_action_events_core63_2nd_v064_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_slope(_to_num(value), 4), 12))
def cg_f098_corporate_action_events_core64_2nd_v065_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_slope(value * 1.0, 4), 12))
def cg_f098_corporate_action_events_core65_2nd_v066_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_slope(value + 0.0, 4), 12))
def cg_f098_corporate_action_events_core66_2nd_v067_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_slope(value / 1.0, 4), 12))
def cg_f098_corporate_action_events_core67_2nd_v068_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_slope(_clean(value), 4), 12))
def cg_f098_corporate_action_events_core68_2nd_v069_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_slope(value * value, 4), 12))
def cg_f098_corporate_action_events_core69_2nd_v070_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_slope(_safe_div(1.0, value.abs() + 1.0), 4), 12))
def cg_f098_corporate_action_events_core70_2nd_v071_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_diff(value, 4), 12))
def cg_f098_corporate_action_events_core71_2nd_v072_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_diff(value.abs(), 4), 12))
def cg_f098_corporate_action_events_core72_2nd_v073_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_diff(_log(value.abs() + 1.0), 4), 12))
def cg_f098_corporate_action_events_core73_2nd_v074_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_diff(_to_num(value), 4), 12))
def cg_f098_corporate_action_events_core74_2nd_v075_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_diff(value * 1.0, 4), 12))
def cg_f098_corporate_action_events_core75_2nd_v076_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_diff(value + 0.0, 4), 12))
def cg_f098_corporate_action_events_core76_2nd_v077_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_diff(value / 1.0, 4), 12))
def cg_f098_corporate_action_events_core77_2nd_v078_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_diff(_clean(value), 4), 12))
def cg_f098_corporate_action_events_core78_2nd_v079_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_diff(value * value, 4), 12))
def cg_f098_corporate_action_events_core79_2nd_v080_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_diff(_safe_div(1.0, value.abs() + 1.0), 4), 12))
def cg_f098_corporate_action_events_core80_2nd_v081_signal(date, action, value, name, contraticker, contraname):
    return _clean(_mean(_slope(value, 4), 4))
def cg_f098_corporate_action_events_core81_2nd_v082_signal(date, action, value, name, contraticker, contraname):
    return _clean(_mean(_slope(value.abs(), 4), 4))
def cg_f098_corporate_action_events_core82_2nd_v083_signal(date, action, value, name, contraticker, contraname):
    return _clean(_mean(_slope(_log(value.abs() + 1.0), 4), 4))
def cg_f098_corporate_action_events_core83_2nd_v084_signal(date, action, value, name, contraticker, contraname):
    return _clean(_mean(_slope(_to_num(value), 4), 4))
def cg_f098_corporate_action_events_core84_2nd_v085_signal(date, action, value, name, contraticker, contraname):
    return _clean(_mean(_slope(value * 1.0, 4), 4))
def cg_f098_corporate_action_events_core85_2nd_v086_signal(date, action, value, name, contraticker, contraname):
    return _clean(_mean(_slope(value + 0.0, 4), 4))
def cg_f098_corporate_action_events_core86_2nd_v087_signal(date, action, value, name, contraticker, contraname):
    return _clean(_mean(_slope(value / 1.0, 4), 4))
def cg_f098_corporate_action_events_core87_2nd_v088_signal(date, action, value, name, contraticker, contraname):
    return _clean(_mean(_slope(_clean(value), 4), 4))
def cg_f098_corporate_action_events_core88_2nd_v089_signal(date, action, value, name, contraticker, contraname):
    return _clean(_mean(_slope(value * value, 4), 4))
def cg_f098_corporate_action_events_core89_2nd_v090_signal(date, action, value, name, contraticker, contraname):
    return _clean(_mean(_slope(_safe_div(1.0, value.abs() + 1.0), 4), 4))
def cg_f098_corporate_action_events_core90_2nd_v091_signal(date, action, value, name, contraticker, contraname):
    return _clean(_mean(_diff(value, 4), 4))
def cg_f098_corporate_action_events_core91_2nd_v092_signal(date, action, value, name, contraticker, contraname):
    return _clean(_mean(_diff(value.abs(), 4), 4))
def cg_f098_corporate_action_events_core92_2nd_v093_signal(date, action, value, name, contraticker, contraname):
    return _clean(_mean(_diff(_log(value.abs() + 1.0), 4), 4))
def cg_f098_corporate_action_events_core93_2nd_v094_signal(date, action, value, name, contraticker, contraname):
    return _clean(_mean(_diff(_to_num(value), 4), 4))
def cg_f098_corporate_action_events_core94_2nd_v095_signal(date, action, value, name, contraticker, contraname):
    return _clean(_mean(_diff(value * 1.0, 4), 4))
def cg_f098_corporate_action_events_core95_2nd_v096_signal(date, action, value, name, contraticker, contraname):
    return _clean(_mean(_diff(value + 0.0, 4), 4))
def cg_f098_corporate_action_events_core96_2nd_v097_signal(date, action, value, name, contraticker, contraname):
    return _clean(_mean(_diff(value / 1.0, 4), 4))
def cg_f098_corporate_action_events_core97_2nd_v098_signal(date, action, value, name, contraticker, contraname):
    return _clean(_mean(_diff(_clean(value), 4), 4))
def cg_f098_corporate_action_events_core98_2nd_v099_signal(date, action, value, name, contraticker, contraname):
    return _clean(_mean(_diff(value * value, 4), 4))
def cg_f098_corporate_action_events_core99_2nd_v100_signal(date, action, value, name, contraticker, contraname):
    return _clean(_mean(_diff(_safe_div(1.0, value.abs() + 1.0), 4), 4))
def cg_f098_corporate_action_events_core100_2nd_v101_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(_mean(value, 4), 4))
def cg_f098_corporate_action_events_core101_2nd_v102_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(_mean(value.abs(), 4), 4))
def cg_f098_corporate_action_events_core102_2nd_v103_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(_mean(_log(value.abs() + 1.0), 4), 4))
def cg_f098_corporate_action_events_core103_2nd_v104_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(_mean(_to_num(value), 4), 4))
def cg_f098_corporate_action_events_core104_2nd_v105_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(_mean(value * 1.0, 4), 4))
def cg_f098_corporate_action_events_core105_2nd_v106_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(_mean(value + 0.0, 4), 4))
def cg_f098_corporate_action_events_core106_2nd_v107_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(_mean(value / 1.0, 4), 4))
def cg_f098_corporate_action_events_core107_2nd_v108_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(_mean(_clean(value), 4), 4))
def cg_f098_corporate_action_events_core108_2nd_v109_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(_mean(value * value, 4), 4))
def cg_f098_corporate_action_events_core109_2nd_v110_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(_mean(_safe_div(1.0, value.abs() + 1.0), 4), 4))
def cg_f098_corporate_action_events_core110_2nd_v111_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(_mean(value, 8), 8))
def cg_f098_corporate_action_events_core111_2nd_v112_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(_mean(value.abs(), 8), 8))
def cg_f098_corporate_action_events_core112_2nd_v113_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(_mean(_log(value.abs() + 1.0), 8), 8))
def cg_f098_corporate_action_events_core113_2nd_v114_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(_mean(_to_num(value), 8), 8))
def cg_f098_corporate_action_events_core114_2nd_v115_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(_mean(value * 1.0, 8), 8))
def cg_f098_corporate_action_events_core115_2nd_v116_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(_mean(value + 0.0, 8), 8))
def cg_f098_corporate_action_events_core116_2nd_v117_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(_mean(value / 1.0, 8), 8))
def cg_f098_corporate_action_events_core117_2nd_v118_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(_mean(_clean(value), 8), 8))
def cg_f098_corporate_action_events_core118_2nd_v119_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(_mean(value * value, 8), 8))
def cg_f098_corporate_action_events_core119_2nd_v120_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(_mean(_safe_div(1.0, value.abs() + 1.0), 8), 8))
def cg_f098_corporate_action_events_core120_2nd_v121_signal(date, action, value, name, contraticker, contraname):
    return _clean(_diff(_mean(value, 4), 4))
def cg_f098_corporate_action_events_core121_2nd_v122_signal(date, action, value, name, contraticker, contraname):
    return _clean(_diff(_mean(value.abs(), 4), 4))
def cg_f098_corporate_action_events_core122_2nd_v123_signal(date, action, value, name, contraticker, contraname):
    return _clean(_diff(_mean(_log(value.abs() + 1.0), 4), 4))
def cg_f098_corporate_action_events_core123_2nd_v124_signal(date, action, value, name, contraticker, contraname):
    return _clean(_diff(_mean(_to_num(value), 4), 4))
def cg_f098_corporate_action_events_core124_2nd_v125_signal(date, action, value, name, contraticker, contraname):
    return _clean(_diff(_mean(value * 1.0, 4), 4))
def cg_f098_corporate_action_events_core125_2nd_v126_signal(date, action, value, name, contraticker, contraname):
    return _clean(_diff(_mean(value + 0.0, 4), 4))
def cg_f098_corporate_action_events_core126_2nd_v127_signal(date, action, value, name, contraticker, contraname):
    return _clean(_diff(_mean(value / 1.0, 4), 4))
def cg_f098_corporate_action_events_core127_2nd_v128_signal(date, action, value, name, contraticker, contraname):
    return _clean(_diff(_mean(_clean(value), 4), 4))
def cg_f098_corporate_action_events_core128_2nd_v129_signal(date, action, value, name, contraticker, contraname):
    return _clean(_diff(_mean(value * value, 4), 4))
def cg_f098_corporate_action_events_core129_2nd_v130_signal(date, action, value, name, contraticker, contraname):
    return _clean(_diff(_mean(_safe_div(1.0, value.abs() + 1.0), 4), 4))
def cg_f098_corporate_action_events_core130_2nd_v131_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_diff(_mean(value, 4), 4), 8))
def cg_f098_corporate_action_events_core131_2nd_v132_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_diff(_mean(value.abs(), 4), 4), 8))
def cg_f098_corporate_action_events_core132_2nd_v133_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_diff(_mean(_log(value.abs() + 1.0), 4), 4), 8))
def cg_f098_corporate_action_events_core133_2nd_v134_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_diff(_mean(_to_num(value), 4), 4), 8))
def cg_f098_corporate_action_events_core134_2nd_v135_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_diff(_mean(value * 1.0, 4), 4), 8))
def cg_f098_corporate_action_events_core135_2nd_v136_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_diff(_mean(value + 0.0, 4), 4), 8))
def cg_f098_corporate_action_events_core136_2nd_v137_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_diff(_mean(value / 1.0, 4), 4), 8))
def cg_f098_corporate_action_events_core137_2nd_v138_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_diff(_mean(_clean(value), 4), 4), 8))
def cg_f098_corporate_action_events_core138_2nd_v139_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_diff(_mean(value * value, 4), 4), 8))
def cg_f098_corporate_action_events_core139_2nd_v140_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(_diff(_mean(_safe_div(1.0, value.abs() + 1.0), 4), 4), 8))
def cg_f098_corporate_action_events_core140_2nd_v141_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_slope(_mean(value, 4), 4), 12))
def cg_f098_corporate_action_events_core141_2nd_v142_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_slope(_mean(value.abs(), 4), 4), 12))
def cg_f098_corporate_action_events_core142_2nd_v143_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_slope(_mean(_log(value.abs() + 1.0), 4), 4), 12))
def cg_f098_corporate_action_events_core143_2nd_v144_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_slope(_mean(_to_num(value), 4), 4), 12))
def cg_f098_corporate_action_events_core144_2nd_v145_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_slope(_mean(value * 1.0, 4), 4), 12))
def cg_f098_corporate_action_events_core145_2nd_v146_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_slope(_mean(value + 0.0, 4), 4), 12))
def cg_f098_corporate_action_events_core146_2nd_v147_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_slope(_mean(value / 1.0, 4), 4), 12))
def cg_f098_corporate_action_events_core147_2nd_v148_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_slope(_mean(_clean(value), 4), 4), 12))
def cg_f098_corporate_action_events_core148_2nd_v149_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_slope(_mean(value * value, 4), 4), 12))
def cg_f098_corporate_action_events_core149_2nd_v150_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(_slope(_mean(_safe_div(1.0, value.abs() + 1.0), 4), 4), 12))