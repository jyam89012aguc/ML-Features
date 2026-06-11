import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f034_share_factor_splits_core00_2nd_v001_signal(sharefactor, action, value, date):
    return _clean(_slope(sharefactor, 4))
def cg_f034_share_factor_splits_core01_2nd_v002_signal(sharefactor, action, value, date):
    return _clean(_slope(value, 4))
def cg_f034_share_factor_splits_core02_2nd_v003_signal(sharefactor, action, value, date):
    return _clean(_slope(_diff(sharefactor, 1), 4))
def cg_f034_share_factor_splits_core03_2nd_v004_signal(sharefactor, action, value, date):
    return _clean(_slope(_pct_change(sharefactor, 1), 4))
def cg_f034_share_factor_splits_core04_2nd_v005_signal(sharefactor, action, value, date):
    return _clean(_slope(_slope(sharefactor, 4), 4))
def cg_f034_share_factor_splits_core05_2nd_v006_signal(sharefactor, action, value, date):
    return _clean(_slope(_z(sharefactor, 8), 4))
def cg_f034_share_factor_splits_core06_2nd_v007_signal(sharefactor, action, value, date):
    return _clean(_slope(sharefactor * value, 4))
def cg_f034_share_factor_splits_core07_2nd_v008_signal(sharefactor, action, value, date):
    return _clean(_slope(_safe_div(sharefactor, value.abs() + 1.0), 4))
def cg_f034_share_factor_splits_core08_2nd_v009_signal(sharefactor, action, value, date):
    return _clean(_slope(_diff(value, 4), 4))
def cg_f034_share_factor_splits_core09_2nd_v010_signal(sharefactor, action, value, date):
    return _clean(_slope(_mean(sharefactor, 4), 4))
def cg_f034_share_factor_splits_core10_2nd_v011_signal(sharefactor, action, value, date):
    return _clean(_slope(sharefactor, 8))
def cg_f034_share_factor_splits_core11_2nd_v012_signal(sharefactor, action, value, date):
    return _clean(_slope(value, 8))
def cg_f034_share_factor_splits_core12_2nd_v013_signal(sharefactor, action, value, date):
    return _clean(_slope(_diff(sharefactor, 1), 8))
def cg_f034_share_factor_splits_core13_2nd_v014_signal(sharefactor, action, value, date):
    return _clean(_slope(_pct_change(sharefactor, 1), 8))
def cg_f034_share_factor_splits_core14_2nd_v015_signal(sharefactor, action, value, date):
    return _clean(_slope(_slope(sharefactor, 4), 8))
def cg_f034_share_factor_splits_core15_2nd_v016_signal(sharefactor, action, value, date):
    return _clean(_slope(_z(sharefactor, 8), 8))
def cg_f034_share_factor_splits_core16_2nd_v017_signal(sharefactor, action, value, date):
    return _clean(_slope(sharefactor * value, 8))
def cg_f034_share_factor_splits_core17_2nd_v018_signal(sharefactor, action, value, date):
    return _clean(_slope(_safe_div(sharefactor, value.abs() + 1.0), 8))
def cg_f034_share_factor_splits_core18_2nd_v019_signal(sharefactor, action, value, date):
    return _clean(_slope(_diff(value, 4), 8))
def cg_f034_share_factor_splits_core19_2nd_v020_signal(sharefactor, action, value, date):
    return _clean(_slope(_mean(sharefactor, 4), 8))
def cg_f034_share_factor_splits_core20_2nd_v021_signal(sharefactor, action, value, date):
    return _clean(_diff(sharefactor, 4))
def cg_f034_share_factor_splits_core21_2nd_v022_signal(sharefactor, action, value, date):
    return _clean(_diff(value, 4))
def cg_f034_share_factor_splits_core22_2nd_v023_signal(sharefactor, action, value, date):
    return _clean(_diff(_diff(sharefactor, 1), 4))
def cg_f034_share_factor_splits_core23_2nd_v024_signal(sharefactor, action, value, date):
    return _clean(_diff(_pct_change(sharefactor, 1), 4))
def cg_f034_share_factor_splits_core24_2nd_v025_signal(sharefactor, action, value, date):
    return _clean(_diff(_slope(sharefactor, 4), 4))
def cg_f034_share_factor_splits_core25_2nd_v026_signal(sharefactor, action, value, date):
    return _clean(_diff(_z(sharefactor, 8), 4))
def cg_f034_share_factor_splits_core26_2nd_v027_signal(sharefactor, action, value, date):
    return _clean(_diff(sharefactor * value, 4))
def cg_f034_share_factor_splits_core27_2nd_v028_signal(sharefactor, action, value, date):
    return _clean(_diff(_safe_div(sharefactor, value.abs() + 1.0), 4))
def cg_f034_share_factor_splits_core28_2nd_v029_signal(sharefactor, action, value, date):
    return _clean(_diff(_diff(value, 4), 4))
def cg_f034_share_factor_splits_core29_2nd_v030_signal(sharefactor, action, value, date):
    return _clean(_diff(_mean(sharefactor, 4), 4))
def cg_f034_share_factor_splits_core30_2nd_v031_signal(sharefactor, action, value, date):
    return _clean(_z(_slope(sharefactor, 4), 8))
def cg_f034_share_factor_splits_core31_2nd_v032_signal(sharefactor, action, value, date):
    return _clean(_z(_slope(value, 4), 8))
def cg_f034_share_factor_splits_core32_2nd_v033_signal(sharefactor, action, value, date):
    return _clean(_z(_slope(_diff(sharefactor, 1), 4), 8))
def cg_f034_share_factor_splits_core33_2nd_v034_signal(sharefactor, action, value, date):
    return _clean(_z(_slope(_pct_change(sharefactor, 1), 4), 8))
def cg_f034_share_factor_splits_core34_2nd_v035_signal(sharefactor, action, value, date):
    return _clean(_z(_slope(_slope(sharefactor, 4), 4), 8))
def cg_f034_share_factor_splits_core35_2nd_v036_signal(sharefactor, action, value, date):
    return _clean(_z(_slope(_z(sharefactor, 8), 4), 8))
def cg_f034_share_factor_splits_core36_2nd_v037_signal(sharefactor, action, value, date):
    return _clean(_z(_slope(sharefactor * value, 4), 8))
def cg_f034_share_factor_splits_core37_2nd_v038_signal(sharefactor, action, value, date):
    return _clean(_z(_slope(_safe_div(sharefactor, value.abs() + 1.0), 4), 8))
def cg_f034_share_factor_splits_core38_2nd_v039_signal(sharefactor, action, value, date):
    return _clean(_z(_slope(_diff(value, 4), 4), 8))
def cg_f034_share_factor_splits_core39_2nd_v040_signal(sharefactor, action, value, date):
    return _clean(_z(_slope(_mean(sharefactor, 4), 4), 8))
def cg_f034_share_factor_splits_core40_2nd_v041_signal(sharefactor, action, value, date):
    return _clean(_z(_slope(sharefactor, 8), 12))
def cg_f034_share_factor_splits_core41_2nd_v042_signal(sharefactor, action, value, date):
    return _clean(_z(_slope(value, 8), 12))
def cg_f034_share_factor_splits_core42_2nd_v043_signal(sharefactor, action, value, date):
    return _clean(_z(_slope(_diff(sharefactor, 1), 8), 12))
def cg_f034_share_factor_splits_core43_2nd_v044_signal(sharefactor, action, value, date):
    return _clean(_z(_slope(_pct_change(sharefactor, 1), 8), 12))
def cg_f034_share_factor_splits_core44_2nd_v045_signal(sharefactor, action, value, date):
    return _clean(_z(_slope(_slope(sharefactor, 4), 8), 12))
def cg_f034_share_factor_splits_core45_2nd_v046_signal(sharefactor, action, value, date):
    return _clean(_z(_slope(_z(sharefactor, 8), 8), 12))
def cg_f034_share_factor_splits_core46_2nd_v047_signal(sharefactor, action, value, date):
    return _clean(_z(_slope(sharefactor * value, 8), 12))
def cg_f034_share_factor_splits_core47_2nd_v048_signal(sharefactor, action, value, date):
    return _clean(_z(_slope(_safe_div(sharefactor, value.abs() + 1.0), 8), 12))
def cg_f034_share_factor_splits_core48_2nd_v049_signal(sharefactor, action, value, date):
    return _clean(_z(_slope(_diff(value, 4), 8), 12))
def cg_f034_share_factor_splits_core49_2nd_v050_signal(sharefactor, action, value, date):
    return _clean(_z(_slope(_mean(sharefactor, 4), 8), 12))
def cg_f034_share_factor_splits_core50_2nd_v051_signal(sharefactor, action, value, date):
    return _clean(_z(_diff(sharefactor, 4), 8))
def cg_f034_share_factor_splits_core51_2nd_v052_signal(sharefactor, action, value, date):
    return _clean(_z(_diff(value, 4), 8))
def cg_f034_share_factor_splits_core52_2nd_v053_signal(sharefactor, action, value, date):
    return _clean(_z(_diff(_diff(sharefactor, 1), 4), 8))
def cg_f034_share_factor_splits_core53_2nd_v054_signal(sharefactor, action, value, date):
    return _clean(_z(_diff(_pct_change(sharefactor, 1), 4), 8))
def cg_f034_share_factor_splits_core54_2nd_v055_signal(sharefactor, action, value, date):
    return _clean(_z(_diff(_slope(sharefactor, 4), 4), 8))
def cg_f034_share_factor_splits_core55_2nd_v056_signal(sharefactor, action, value, date):
    return _clean(_z(_diff(_z(sharefactor, 8), 4), 8))
def cg_f034_share_factor_splits_core56_2nd_v057_signal(sharefactor, action, value, date):
    return _clean(_z(_diff(sharefactor * value, 4), 8))
def cg_f034_share_factor_splits_core57_2nd_v058_signal(sharefactor, action, value, date):
    return _clean(_z(_diff(_safe_div(sharefactor, value.abs() + 1.0), 4), 8))
def cg_f034_share_factor_splits_core58_2nd_v059_signal(sharefactor, action, value, date):
    return _clean(_z(_diff(_diff(value, 4), 4), 8))
def cg_f034_share_factor_splits_core59_2nd_v060_signal(sharefactor, action, value, date):
    return _clean(_z(_diff(_mean(sharefactor, 4), 4), 8))
def cg_f034_share_factor_splits_core60_2nd_v061_signal(sharefactor, action, value, date):
    return _clean(_rank(_slope(sharefactor, 4), 12))
def cg_f034_share_factor_splits_core61_2nd_v062_signal(sharefactor, action, value, date):
    return _clean(_rank(_slope(value, 4), 12))
def cg_f034_share_factor_splits_core62_2nd_v063_signal(sharefactor, action, value, date):
    return _clean(_rank(_slope(_diff(sharefactor, 1), 4), 12))
def cg_f034_share_factor_splits_core63_2nd_v064_signal(sharefactor, action, value, date):
    return _clean(_rank(_slope(_pct_change(sharefactor, 1), 4), 12))
def cg_f034_share_factor_splits_core64_2nd_v065_signal(sharefactor, action, value, date):
    return _clean(_rank(_slope(_slope(sharefactor, 4), 4), 12))
def cg_f034_share_factor_splits_core65_2nd_v066_signal(sharefactor, action, value, date):
    return _clean(_rank(_slope(_z(sharefactor, 8), 4), 12))
def cg_f034_share_factor_splits_core66_2nd_v067_signal(sharefactor, action, value, date):
    return _clean(_rank(_slope(sharefactor * value, 4), 12))
def cg_f034_share_factor_splits_core67_2nd_v068_signal(sharefactor, action, value, date):
    return _clean(_rank(_slope(_safe_div(sharefactor, value.abs() + 1.0), 4), 12))
def cg_f034_share_factor_splits_core68_2nd_v069_signal(sharefactor, action, value, date):
    return _clean(_rank(_slope(_diff(value, 4), 4), 12))
def cg_f034_share_factor_splits_core69_2nd_v070_signal(sharefactor, action, value, date):
    return _clean(_rank(_slope(_mean(sharefactor, 4), 4), 12))
def cg_f034_share_factor_splits_core70_2nd_v071_signal(sharefactor, action, value, date):
    return _clean(_rank(_diff(sharefactor, 4), 12))
def cg_f034_share_factor_splits_core71_2nd_v072_signal(sharefactor, action, value, date):
    return _clean(_rank(_diff(value, 4), 12))
def cg_f034_share_factor_splits_core72_2nd_v073_signal(sharefactor, action, value, date):
    return _clean(_rank(_diff(_diff(sharefactor, 1), 4), 12))
def cg_f034_share_factor_splits_core73_2nd_v074_signal(sharefactor, action, value, date):
    return _clean(_rank(_diff(_pct_change(sharefactor, 1), 4), 12))
def cg_f034_share_factor_splits_core74_2nd_v075_signal(sharefactor, action, value, date):
    return _clean(_rank(_diff(_slope(sharefactor, 4), 4), 12))
def cg_f034_share_factor_splits_core75_2nd_v076_signal(sharefactor, action, value, date):
    return _clean(_rank(_diff(_z(sharefactor, 8), 4), 12))
def cg_f034_share_factor_splits_core76_2nd_v077_signal(sharefactor, action, value, date):
    return _clean(_rank(_diff(sharefactor * value, 4), 12))
def cg_f034_share_factor_splits_core77_2nd_v078_signal(sharefactor, action, value, date):
    return _clean(_rank(_diff(_safe_div(sharefactor, value.abs() + 1.0), 4), 12))
def cg_f034_share_factor_splits_core78_2nd_v079_signal(sharefactor, action, value, date):
    return _clean(_rank(_diff(_diff(value, 4), 4), 12))
def cg_f034_share_factor_splits_core79_2nd_v080_signal(sharefactor, action, value, date):
    return _clean(_rank(_diff(_mean(sharefactor, 4), 4), 12))
def cg_f034_share_factor_splits_core80_2nd_v081_signal(sharefactor, action, value, date):
    return _clean(_mean(_slope(sharefactor, 4), 4))
def cg_f034_share_factor_splits_core81_2nd_v082_signal(sharefactor, action, value, date):
    return _clean(_mean(_slope(value, 4), 4))
def cg_f034_share_factor_splits_core82_2nd_v083_signal(sharefactor, action, value, date):
    return _clean(_mean(_slope(_diff(sharefactor, 1), 4), 4))
def cg_f034_share_factor_splits_core83_2nd_v084_signal(sharefactor, action, value, date):
    return _clean(_mean(_slope(_pct_change(sharefactor, 1), 4), 4))
def cg_f034_share_factor_splits_core84_2nd_v085_signal(sharefactor, action, value, date):
    return _clean(_mean(_slope(_slope(sharefactor, 4), 4), 4))
def cg_f034_share_factor_splits_core85_2nd_v086_signal(sharefactor, action, value, date):
    return _clean(_mean(_slope(_z(sharefactor, 8), 4), 4))
def cg_f034_share_factor_splits_core86_2nd_v087_signal(sharefactor, action, value, date):
    return _clean(_mean(_slope(sharefactor * value, 4), 4))
def cg_f034_share_factor_splits_core87_2nd_v088_signal(sharefactor, action, value, date):
    return _clean(_mean(_slope(_safe_div(sharefactor, value.abs() + 1.0), 4), 4))
def cg_f034_share_factor_splits_core88_2nd_v089_signal(sharefactor, action, value, date):
    return _clean(_mean(_slope(_diff(value, 4), 4), 4))
def cg_f034_share_factor_splits_core89_2nd_v090_signal(sharefactor, action, value, date):
    return _clean(_mean(_slope(_mean(sharefactor, 4), 4), 4))
def cg_f034_share_factor_splits_core90_2nd_v091_signal(sharefactor, action, value, date):
    return _clean(_mean(_diff(sharefactor, 4), 4))
def cg_f034_share_factor_splits_core91_2nd_v092_signal(sharefactor, action, value, date):
    return _clean(_mean(_diff(value, 4), 4))
def cg_f034_share_factor_splits_core92_2nd_v093_signal(sharefactor, action, value, date):
    return _clean(_mean(_diff(_diff(sharefactor, 1), 4), 4))
def cg_f034_share_factor_splits_core93_2nd_v094_signal(sharefactor, action, value, date):
    return _clean(_mean(_diff(_pct_change(sharefactor, 1), 4), 4))
def cg_f034_share_factor_splits_core94_2nd_v095_signal(sharefactor, action, value, date):
    return _clean(_mean(_diff(_slope(sharefactor, 4), 4), 4))
def cg_f034_share_factor_splits_core95_2nd_v096_signal(sharefactor, action, value, date):
    return _clean(_mean(_diff(_z(sharefactor, 8), 4), 4))
def cg_f034_share_factor_splits_core96_2nd_v097_signal(sharefactor, action, value, date):
    return _clean(_mean(_diff(sharefactor * value, 4), 4))
def cg_f034_share_factor_splits_core97_2nd_v098_signal(sharefactor, action, value, date):
    return _clean(_mean(_diff(_safe_div(sharefactor, value.abs() + 1.0), 4), 4))
def cg_f034_share_factor_splits_core98_2nd_v099_signal(sharefactor, action, value, date):
    return _clean(_mean(_diff(_diff(value, 4), 4), 4))
def cg_f034_share_factor_splits_core99_2nd_v100_signal(sharefactor, action, value, date):
    return _clean(_mean(_diff(_mean(sharefactor, 4), 4), 4))
def cg_f034_share_factor_splits_core100_2nd_v101_signal(sharefactor, action, value, date):
    return _clean(_slope(_mean(sharefactor, 4), 4))
def cg_f034_share_factor_splits_core101_2nd_v102_signal(sharefactor, action, value, date):
    return _clean(_slope(_mean(value, 4), 4))
def cg_f034_share_factor_splits_core102_2nd_v103_signal(sharefactor, action, value, date):
    return _clean(_slope(_mean(_diff(sharefactor, 1), 4), 4))
def cg_f034_share_factor_splits_core103_2nd_v104_signal(sharefactor, action, value, date):
    return _clean(_slope(_mean(_pct_change(sharefactor, 1), 4), 4))
def cg_f034_share_factor_splits_core104_2nd_v105_signal(sharefactor, action, value, date):
    return _clean(_slope(_mean(_slope(sharefactor, 4), 4), 4))
def cg_f034_share_factor_splits_core105_2nd_v106_signal(sharefactor, action, value, date):
    return _clean(_slope(_mean(_z(sharefactor, 8), 4), 4))
def cg_f034_share_factor_splits_core106_2nd_v107_signal(sharefactor, action, value, date):
    return _clean(_slope(_mean(sharefactor * value, 4), 4))
def cg_f034_share_factor_splits_core107_2nd_v108_signal(sharefactor, action, value, date):
    return _clean(_slope(_mean(_safe_div(sharefactor, value.abs() + 1.0), 4), 4))
def cg_f034_share_factor_splits_core108_2nd_v109_signal(sharefactor, action, value, date):
    return _clean(_slope(_mean(_diff(value, 4), 4), 4))
def cg_f034_share_factor_splits_core109_2nd_v110_signal(sharefactor, action, value, date):
    return _clean(_slope(_mean(_mean(sharefactor, 4), 4), 4))
def cg_f034_share_factor_splits_core110_2nd_v111_signal(sharefactor, action, value, date):
    return _clean(_slope(_mean(sharefactor, 8), 8))
def cg_f034_share_factor_splits_core111_2nd_v112_signal(sharefactor, action, value, date):
    return _clean(_slope(_mean(value, 8), 8))
def cg_f034_share_factor_splits_core112_2nd_v113_signal(sharefactor, action, value, date):
    return _clean(_slope(_mean(_diff(sharefactor, 1), 8), 8))
def cg_f034_share_factor_splits_core113_2nd_v114_signal(sharefactor, action, value, date):
    return _clean(_slope(_mean(_pct_change(sharefactor, 1), 8), 8))
def cg_f034_share_factor_splits_core114_2nd_v115_signal(sharefactor, action, value, date):
    return _clean(_slope(_mean(_slope(sharefactor, 4), 8), 8))
def cg_f034_share_factor_splits_core115_2nd_v116_signal(sharefactor, action, value, date):
    return _clean(_slope(_mean(_z(sharefactor, 8), 8), 8))
def cg_f034_share_factor_splits_core116_2nd_v117_signal(sharefactor, action, value, date):
    return _clean(_slope(_mean(sharefactor * value, 8), 8))
def cg_f034_share_factor_splits_core117_2nd_v118_signal(sharefactor, action, value, date):
    return _clean(_slope(_mean(_safe_div(sharefactor, value.abs() + 1.0), 8), 8))
def cg_f034_share_factor_splits_core118_2nd_v119_signal(sharefactor, action, value, date):
    return _clean(_slope(_mean(_diff(value, 4), 8), 8))
def cg_f034_share_factor_splits_core119_2nd_v120_signal(sharefactor, action, value, date):
    return _clean(_slope(_mean(_mean(sharefactor, 4), 8), 8))
def cg_f034_share_factor_splits_core120_2nd_v121_signal(sharefactor, action, value, date):
    return _clean(_diff(_mean(sharefactor, 4), 4))
def cg_f034_share_factor_splits_core121_2nd_v122_signal(sharefactor, action, value, date):
    return _clean(_diff(_mean(value, 4), 4))
def cg_f034_share_factor_splits_core122_2nd_v123_signal(sharefactor, action, value, date):
    return _clean(_diff(_mean(_diff(sharefactor, 1), 4), 4))
def cg_f034_share_factor_splits_core123_2nd_v124_signal(sharefactor, action, value, date):
    return _clean(_diff(_mean(_pct_change(sharefactor, 1), 4), 4))
def cg_f034_share_factor_splits_core124_2nd_v125_signal(sharefactor, action, value, date):
    return _clean(_diff(_mean(_slope(sharefactor, 4), 4), 4))
def cg_f034_share_factor_splits_core125_2nd_v126_signal(sharefactor, action, value, date):
    return _clean(_diff(_mean(_z(sharefactor, 8), 4), 4))
def cg_f034_share_factor_splits_core126_2nd_v127_signal(sharefactor, action, value, date):
    return _clean(_diff(_mean(sharefactor * value, 4), 4))
def cg_f034_share_factor_splits_core127_2nd_v128_signal(sharefactor, action, value, date):
    return _clean(_diff(_mean(_safe_div(sharefactor, value.abs() + 1.0), 4), 4))
def cg_f034_share_factor_splits_core128_2nd_v129_signal(sharefactor, action, value, date):
    return _clean(_diff(_mean(_diff(value, 4), 4), 4))
def cg_f034_share_factor_splits_core129_2nd_v130_signal(sharefactor, action, value, date):
    return _clean(_diff(_mean(_mean(sharefactor, 4), 4), 4))
def cg_f034_share_factor_splits_core130_2nd_v131_signal(sharefactor, action, value, date):
    return _clean(_z(_diff(_mean(sharefactor, 4), 4), 8))
def cg_f034_share_factor_splits_core131_2nd_v132_signal(sharefactor, action, value, date):
    return _clean(_z(_diff(_mean(value, 4), 4), 8))
def cg_f034_share_factor_splits_core132_2nd_v133_signal(sharefactor, action, value, date):
    return _clean(_z(_diff(_mean(_diff(sharefactor, 1), 4), 4), 8))
def cg_f034_share_factor_splits_core133_2nd_v134_signal(sharefactor, action, value, date):
    return _clean(_z(_diff(_mean(_pct_change(sharefactor, 1), 4), 4), 8))
def cg_f034_share_factor_splits_core134_2nd_v135_signal(sharefactor, action, value, date):
    return _clean(_z(_diff(_mean(_slope(sharefactor, 4), 4), 4), 8))
def cg_f034_share_factor_splits_core135_2nd_v136_signal(sharefactor, action, value, date):
    return _clean(_z(_diff(_mean(_z(sharefactor, 8), 4), 4), 8))
def cg_f034_share_factor_splits_core136_2nd_v137_signal(sharefactor, action, value, date):
    return _clean(_z(_diff(_mean(sharefactor * value, 4), 4), 8))
def cg_f034_share_factor_splits_core137_2nd_v138_signal(sharefactor, action, value, date):
    return _clean(_z(_diff(_mean(_safe_div(sharefactor, value.abs() + 1.0), 4), 4), 8))
def cg_f034_share_factor_splits_core138_2nd_v139_signal(sharefactor, action, value, date):
    return _clean(_z(_diff(_mean(_diff(value, 4), 4), 4), 8))
def cg_f034_share_factor_splits_core139_2nd_v140_signal(sharefactor, action, value, date):
    return _clean(_z(_diff(_mean(_mean(sharefactor, 4), 4), 4), 8))
def cg_f034_share_factor_splits_core140_2nd_v141_signal(sharefactor, action, value, date):
    return _clean(_rank(_slope(_mean(sharefactor, 4), 4), 12))
def cg_f034_share_factor_splits_core141_2nd_v142_signal(sharefactor, action, value, date):
    return _clean(_rank(_slope(_mean(value, 4), 4), 12))
def cg_f034_share_factor_splits_core142_2nd_v143_signal(sharefactor, action, value, date):
    return _clean(_rank(_slope(_mean(_diff(sharefactor, 1), 4), 4), 12))
def cg_f034_share_factor_splits_core143_2nd_v144_signal(sharefactor, action, value, date):
    return _clean(_rank(_slope(_mean(_pct_change(sharefactor, 1), 4), 4), 12))
def cg_f034_share_factor_splits_core144_2nd_v145_signal(sharefactor, action, value, date):
    return _clean(_rank(_slope(_mean(_slope(sharefactor, 4), 4), 4), 12))
def cg_f034_share_factor_splits_core145_2nd_v146_signal(sharefactor, action, value, date):
    return _clean(_rank(_slope(_mean(_z(sharefactor, 8), 4), 4), 12))
def cg_f034_share_factor_splits_core146_2nd_v147_signal(sharefactor, action, value, date):
    return _clean(_rank(_slope(_mean(sharefactor * value, 4), 4), 12))
def cg_f034_share_factor_splits_core147_2nd_v148_signal(sharefactor, action, value, date):
    return _clean(_rank(_slope(_mean(_safe_div(sharefactor, value.abs() + 1.0), 4), 4), 12))
def cg_f034_share_factor_splits_core148_2nd_v149_signal(sharefactor, action, value, date):
    return _clean(_rank(_slope(_mean(_diff(value, 4), 4), 4), 12))
def cg_f034_share_factor_splits_core149_2nd_v150_signal(sharefactor, action, value, date):
    return _clean(_rank(_slope(_mean(_mean(sharefactor, 4), 4), 4), 12))