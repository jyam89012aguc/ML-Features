import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f034_share_factor_splits_core00_3rd_v001_signal(sharefactor, action, value, date):
    return _clean(_diff(_diff(sharefactor, 4), 4))
def cg_f034_share_factor_splits_core01_3rd_v002_signal(sharefactor, action, value, date):
    return _clean(_diff(_diff(value, 4), 4))
def cg_f034_share_factor_splits_core02_3rd_v003_signal(sharefactor, action, value, date):
    return _clean(_diff(_diff(_diff(sharefactor, 1), 4), 4))
def cg_f034_share_factor_splits_core03_3rd_v004_signal(sharefactor, action, value, date):
    return _clean(_diff(_diff(_pct_change(sharefactor, 1), 4), 4))
def cg_f034_share_factor_splits_core04_3rd_v005_signal(sharefactor, action, value, date):
    return _clean(_diff(_diff(_slope(sharefactor, 4), 4), 4))
def cg_f034_share_factor_splits_core05_3rd_v006_signal(sharefactor, action, value, date):
    return _clean(_diff(_diff(_z(sharefactor, 8), 4), 4))
def cg_f034_share_factor_splits_core06_3rd_v007_signal(sharefactor, action, value, date):
    return _clean(_diff(_diff(sharefactor * value, 4), 4))
def cg_f034_share_factor_splits_core07_3rd_v008_signal(sharefactor, action, value, date):
    return _clean(_diff(_diff(_safe_div(sharefactor, value.abs() + 1.0), 4), 4))
def cg_f034_share_factor_splits_core08_3rd_v009_signal(sharefactor, action, value, date):
    return _clean(_diff(_diff(_diff(value, 4), 4), 4))
def cg_f034_share_factor_splits_core09_3rd_v010_signal(sharefactor, action, value, date):
    return _clean(_diff(_diff(_mean(sharefactor, 4), 4), 4))
def cg_f034_share_factor_splits_core10_3rd_v011_signal(sharefactor, action, value, date):
    return _clean(_slope(_diff(sharefactor, 4), 8))
def cg_f034_share_factor_splits_core11_3rd_v012_signal(sharefactor, action, value, date):
    return _clean(_slope(_diff(value, 4), 8))
def cg_f034_share_factor_splits_core12_3rd_v013_signal(sharefactor, action, value, date):
    return _clean(_slope(_diff(_diff(sharefactor, 1), 4), 8))
def cg_f034_share_factor_splits_core13_3rd_v014_signal(sharefactor, action, value, date):
    return _clean(_slope(_diff(_pct_change(sharefactor, 1), 4), 8))
def cg_f034_share_factor_splits_core14_3rd_v015_signal(sharefactor, action, value, date):
    return _clean(_slope(_diff(_slope(sharefactor, 4), 4), 8))
def cg_f034_share_factor_splits_core15_3rd_v016_signal(sharefactor, action, value, date):
    return _clean(_slope(_diff(_z(sharefactor, 8), 4), 8))
def cg_f034_share_factor_splits_core16_3rd_v017_signal(sharefactor, action, value, date):
    return _clean(_slope(_diff(sharefactor * value, 4), 8))
def cg_f034_share_factor_splits_core17_3rd_v018_signal(sharefactor, action, value, date):
    return _clean(_slope(_diff(_safe_div(sharefactor, value.abs() + 1.0), 4), 8))
def cg_f034_share_factor_splits_core18_3rd_v019_signal(sharefactor, action, value, date):
    return _clean(_slope(_diff(_diff(value, 4), 4), 8))
def cg_f034_share_factor_splits_core19_3rd_v020_signal(sharefactor, action, value, date):
    return _clean(_slope(_diff(_mean(sharefactor, 4), 4), 8))
def cg_f034_share_factor_splits_core20_3rd_v021_signal(sharefactor, action, value, date):
    return _clean(_diff(_slope(sharefactor, 4), 4))
def cg_f034_share_factor_splits_core21_3rd_v022_signal(sharefactor, action, value, date):
    return _clean(_diff(_slope(value, 4), 4))
def cg_f034_share_factor_splits_core22_3rd_v023_signal(sharefactor, action, value, date):
    return _clean(_diff(_slope(_diff(sharefactor, 1), 4), 4))
def cg_f034_share_factor_splits_core23_3rd_v024_signal(sharefactor, action, value, date):
    return _clean(_diff(_slope(_pct_change(sharefactor, 1), 4), 4))
def cg_f034_share_factor_splits_core24_3rd_v025_signal(sharefactor, action, value, date):
    return _clean(_diff(_slope(_slope(sharefactor, 4), 4), 4))
def cg_f034_share_factor_splits_core25_3rd_v026_signal(sharefactor, action, value, date):
    return _clean(_diff(_slope(_z(sharefactor, 8), 4), 4))
def cg_f034_share_factor_splits_core26_3rd_v027_signal(sharefactor, action, value, date):
    return _clean(_diff(_slope(sharefactor * value, 4), 4))
def cg_f034_share_factor_splits_core27_3rd_v028_signal(sharefactor, action, value, date):
    return _clean(_diff(_slope(_safe_div(sharefactor, value.abs() + 1.0), 4), 4))
def cg_f034_share_factor_splits_core28_3rd_v029_signal(sharefactor, action, value, date):
    return _clean(_diff(_slope(_diff(value, 4), 4), 4))
def cg_f034_share_factor_splits_core29_3rd_v030_signal(sharefactor, action, value, date):
    return _clean(_diff(_slope(_mean(sharefactor, 4), 4), 4))
def cg_f034_share_factor_splits_core30_3rd_v031_signal(sharefactor, action, value, date):
    return _clean(_z(_diff(_diff(sharefactor, 4), 4), 8))
def cg_f034_share_factor_splits_core31_3rd_v032_signal(sharefactor, action, value, date):
    return _clean(_z(_diff(_diff(value, 4), 4), 8))
def cg_f034_share_factor_splits_core32_3rd_v033_signal(sharefactor, action, value, date):
    return _clean(_z(_diff(_diff(_diff(sharefactor, 1), 4), 4), 8))
def cg_f034_share_factor_splits_core33_3rd_v034_signal(sharefactor, action, value, date):
    return _clean(_z(_diff(_diff(_pct_change(sharefactor, 1), 4), 4), 8))
def cg_f034_share_factor_splits_core34_3rd_v035_signal(sharefactor, action, value, date):
    return _clean(_z(_diff(_diff(_slope(sharefactor, 4), 4), 4), 8))
def cg_f034_share_factor_splits_core35_3rd_v036_signal(sharefactor, action, value, date):
    return _clean(_z(_diff(_diff(_z(sharefactor, 8), 4), 4), 8))
def cg_f034_share_factor_splits_core36_3rd_v037_signal(sharefactor, action, value, date):
    return _clean(_z(_diff(_diff(sharefactor * value, 4), 4), 8))
def cg_f034_share_factor_splits_core37_3rd_v038_signal(sharefactor, action, value, date):
    return _clean(_z(_diff(_diff(_safe_div(sharefactor, value.abs() + 1.0), 4), 4), 8))
def cg_f034_share_factor_splits_core38_3rd_v039_signal(sharefactor, action, value, date):
    return _clean(_z(_diff(_diff(_diff(value, 4), 4), 4), 8))
def cg_f034_share_factor_splits_core39_3rd_v040_signal(sharefactor, action, value, date):
    return _clean(_z(_diff(_diff(_mean(sharefactor, 4), 4), 4), 8))
def cg_f034_share_factor_splits_core40_3rd_v041_signal(sharefactor, action, value, date):
    return _clean(_z(_slope(_diff(sharefactor, 4), 8), 12))
def cg_f034_share_factor_splits_core41_3rd_v042_signal(sharefactor, action, value, date):
    return _clean(_z(_slope(_diff(value, 4), 8), 12))
def cg_f034_share_factor_splits_core42_3rd_v043_signal(sharefactor, action, value, date):
    return _clean(_z(_slope(_diff(_diff(sharefactor, 1), 4), 8), 12))
def cg_f034_share_factor_splits_core43_3rd_v044_signal(sharefactor, action, value, date):
    return _clean(_z(_slope(_diff(_pct_change(sharefactor, 1), 4), 8), 12))
def cg_f034_share_factor_splits_core44_3rd_v045_signal(sharefactor, action, value, date):
    return _clean(_z(_slope(_diff(_slope(sharefactor, 4), 4), 8), 12))
def cg_f034_share_factor_splits_core45_3rd_v046_signal(sharefactor, action, value, date):
    return _clean(_z(_slope(_diff(_z(sharefactor, 8), 4), 8), 12))
def cg_f034_share_factor_splits_core46_3rd_v047_signal(sharefactor, action, value, date):
    return _clean(_z(_slope(_diff(sharefactor * value, 4), 8), 12))
def cg_f034_share_factor_splits_core47_3rd_v048_signal(sharefactor, action, value, date):
    return _clean(_z(_slope(_diff(_safe_div(sharefactor, value.abs() + 1.0), 4), 8), 12))
def cg_f034_share_factor_splits_core48_3rd_v049_signal(sharefactor, action, value, date):
    return _clean(_z(_slope(_diff(_diff(value, 4), 4), 8), 12))
def cg_f034_share_factor_splits_core49_3rd_v050_signal(sharefactor, action, value, date):
    return _clean(_z(_slope(_diff(_mean(sharefactor, 4), 4), 8), 12))
def cg_f034_share_factor_splits_core50_3rd_v051_signal(sharefactor, action, value, date):
    return _clean(_z(_diff(_slope(sharefactor, 4), 4), 8))
def cg_f034_share_factor_splits_core51_3rd_v052_signal(sharefactor, action, value, date):
    return _clean(_z(_diff(_slope(value, 4), 4), 8))
def cg_f034_share_factor_splits_core52_3rd_v053_signal(sharefactor, action, value, date):
    return _clean(_z(_diff(_slope(_diff(sharefactor, 1), 4), 4), 8))
def cg_f034_share_factor_splits_core53_3rd_v054_signal(sharefactor, action, value, date):
    return _clean(_z(_diff(_slope(_pct_change(sharefactor, 1), 4), 4), 8))
def cg_f034_share_factor_splits_core54_3rd_v055_signal(sharefactor, action, value, date):
    return _clean(_z(_diff(_slope(_slope(sharefactor, 4), 4), 4), 8))
def cg_f034_share_factor_splits_core55_3rd_v056_signal(sharefactor, action, value, date):
    return _clean(_z(_diff(_slope(_z(sharefactor, 8), 4), 4), 8))
def cg_f034_share_factor_splits_core56_3rd_v057_signal(sharefactor, action, value, date):
    return _clean(_z(_diff(_slope(sharefactor * value, 4), 4), 8))
def cg_f034_share_factor_splits_core57_3rd_v058_signal(sharefactor, action, value, date):
    return _clean(_z(_diff(_slope(_safe_div(sharefactor, value.abs() + 1.0), 4), 4), 8))
def cg_f034_share_factor_splits_core58_3rd_v059_signal(sharefactor, action, value, date):
    return _clean(_z(_diff(_slope(_diff(value, 4), 4), 4), 8))
def cg_f034_share_factor_splits_core59_3rd_v060_signal(sharefactor, action, value, date):
    return _clean(_z(_diff(_slope(_mean(sharefactor, 4), 4), 4), 8))
def cg_f034_share_factor_splits_core60_3rd_v061_signal(sharefactor, action, value, date):
    return _clean(_rank(_diff(_diff(sharefactor, 4), 4), 12))
def cg_f034_share_factor_splits_core61_3rd_v062_signal(sharefactor, action, value, date):
    return _clean(_rank(_diff(_diff(value, 4), 4), 12))
def cg_f034_share_factor_splits_core62_3rd_v063_signal(sharefactor, action, value, date):
    return _clean(_rank(_diff(_diff(_diff(sharefactor, 1), 4), 4), 12))
def cg_f034_share_factor_splits_core63_3rd_v064_signal(sharefactor, action, value, date):
    return _clean(_rank(_diff(_diff(_pct_change(sharefactor, 1), 4), 4), 12))
def cg_f034_share_factor_splits_core64_3rd_v065_signal(sharefactor, action, value, date):
    return _clean(_rank(_diff(_diff(_slope(sharefactor, 4), 4), 4), 12))
def cg_f034_share_factor_splits_core65_3rd_v066_signal(sharefactor, action, value, date):
    return _clean(_rank(_diff(_diff(_z(sharefactor, 8), 4), 4), 12))
def cg_f034_share_factor_splits_core66_3rd_v067_signal(sharefactor, action, value, date):
    return _clean(_rank(_diff(_diff(sharefactor * value, 4), 4), 12))
def cg_f034_share_factor_splits_core67_3rd_v068_signal(sharefactor, action, value, date):
    return _clean(_rank(_diff(_diff(_safe_div(sharefactor, value.abs() + 1.0), 4), 4), 12))
def cg_f034_share_factor_splits_core68_3rd_v069_signal(sharefactor, action, value, date):
    return _clean(_rank(_diff(_diff(_diff(value, 4), 4), 4), 12))
def cg_f034_share_factor_splits_core69_3rd_v070_signal(sharefactor, action, value, date):
    return _clean(_rank(_diff(_diff(_mean(sharefactor, 4), 4), 4), 12))
def cg_f034_share_factor_splits_core70_3rd_v071_signal(sharefactor, action, value, date):
    return _clean(_rank(_slope(_diff(sharefactor, 4), 8), 12))
def cg_f034_share_factor_splits_core71_3rd_v072_signal(sharefactor, action, value, date):
    return _clean(_rank(_slope(_diff(value, 4), 8), 12))
def cg_f034_share_factor_splits_core72_3rd_v073_signal(sharefactor, action, value, date):
    return _clean(_rank(_slope(_diff(_diff(sharefactor, 1), 4), 8), 12))
def cg_f034_share_factor_splits_core73_3rd_v074_signal(sharefactor, action, value, date):
    return _clean(_rank(_slope(_diff(_pct_change(sharefactor, 1), 4), 8), 12))
def cg_f034_share_factor_splits_core74_3rd_v075_signal(sharefactor, action, value, date):
    return _clean(_rank(_slope(_diff(_slope(sharefactor, 4), 4), 8), 12))
def cg_f034_share_factor_splits_core75_3rd_v076_signal(sharefactor, action, value, date):
    return _clean(_rank(_slope(_diff(_z(sharefactor, 8), 4), 8), 12))
def cg_f034_share_factor_splits_core76_3rd_v077_signal(sharefactor, action, value, date):
    return _clean(_rank(_slope(_diff(sharefactor * value, 4), 8), 12))
def cg_f034_share_factor_splits_core77_3rd_v078_signal(sharefactor, action, value, date):
    return _clean(_rank(_slope(_diff(_safe_div(sharefactor, value.abs() + 1.0), 4), 8), 12))
def cg_f034_share_factor_splits_core78_3rd_v079_signal(sharefactor, action, value, date):
    return _clean(_rank(_slope(_diff(_diff(value, 4), 4), 8), 12))
def cg_f034_share_factor_splits_core79_3rd_v080_signal(sharefactor, action, value, date):
    return _clean(_rank(_slope(_diff(_mean(sharefactor, 4), 4), 8), 12))
def cg_f034_share_factor_splits_core80_3rd_v081_signal(sharefactor, action, value, date):
    return _clean(_rank(_diff(_slope(sharefactor, 4), 4), 12))
def cg_f034_share_factor_splits_core81_3rd_v082_signal(sharefactor, action, value, date):
    return _clean(_rank(_diff(_slope(value, 4), 4), 12))
def cg_f034_share_factor_splits_core82_3rd_v083_signal(sharefactor, action, value, date):
    return _clean(_rank(_diff(_slope(_diff(sharefactor, 1), 4), 4), 12))
def cg_f034_share_factor_splits_core83_3rd_v084_signal(sharefactor, action, value, date):
    return _clean(_rank(_diff(_slope(_pct_change(sharefactor, 1), 4), 4), 12))
def cg_f034_share_factor_splits_core84_3rd_v085_signal(sharefactor, action, value, date):
    return _clean(_rank(_diff(_slope(_slope(sharefactor, 4), 4), 4), 12))
def cg_f034_share_factor_splits_core85_3rd_v086_signal(sharefactor, action, value, date):
    return _clean(_rank(_diff(_slope(_z(sharefactor, 8), 4), 4), 12))
def cg_f034_share_factor_splits_core86_3rd_v087_signal(sharefactor, action, value, date):
    return _clean(_rank(_diff(_slope(sharefactor * value, 4), 4), 12))
def cg_f034_share_factor_splits_core87_3rd_v088_signal(sharefactor, action, value, date):
    return _clean(_rank(_diff(_slope(_safe_div(sharefactor, value.abs() + 1.0), 4), 4), 12))
def cg_f034_share_factor_splits_core88_3rd_v089_signal(sharefactor, action, value, date):
    return _clean(_rank(_diff(_slope(_diff(value, 4), 4), 4), 12))
def cg_f034_share_factor_splits_core89_3rd_v090_signal(sharefactor, action, value, date):
    return _clean(_rank(_diff(_slope(_mean(sharefactor, 4), 4), 4), 12))
def cg_f034_share_factor_splits_core90_3rd_v091_signal(sharefactor, action, value, date):
    return _clean(_mean(_diff(_diff(sharefactor, 4), 4), 4))
def cg_f034_share_factor_splits_core91_3rd_v092_signal(sharefactor, action, value, date):
    return _clean(_mean(_diff(_diff(value, 4), 4), 4))
def cg_f034_share_factor_splits_core92_3rd_v093_signal(sharefactor, action, value, date):
    return _clean(_mean(_diff(_diff(_diff(sharefactor, 1), 4), 4), 4))
def cg_f034_share_factor_splits_core93_3rd_v094_signal(sharefactor, action, value, date):
    return _clean(_mean(_diff(_diff(_pct_change(sharefactor, 1), 4), 4), 4))
def cg_f034_share_factor_splits_core94_3rd_v095_signal(sharefactor, action, value, date):
    return _clean(_mean(_diff(_diff(_slope(sharefactor, 4), 4), 4), 4))
def cg_f034_share_factor_splits_core95_3rd_v096_signal(sharefactor, action, value, date):
    return _clean(_mean(_diff(_diff(_z(sharefactor, 8), 4), 4), 4))
def cg_f034_share_factor_splits_core96_3rd_v097_signal(sharefactor, action, value, date):
    return _clean(_mean(_diff(_diff(sharefactor * value, 4), 4), 4))
def cg_f034_share_factor_splits_core97_3rd_v098_signal(sharefactor, action, value, date):
    return _clean(_mean(_diff(_diff(_safe_div(sharefactor, value.abs() + 1.0), 4), 4), 4))
def cg_f034_share_factor_splits_core98_3rd_v099_signal(sharefactor, action, value, date):
    return _clean(_mean(_diff(_diff(_diff(value, 4), 4), 4), 4))
def cg_f034_share_factor_splits_core99_3rd_v100_signal(sharefactor, action, value, date):
    return _clean(_mean(_diff(_diff(_mean(sharefactor, 4), 4), 4), 4))
def cg_f034_share_factor_splits_core100_3rd_v101_signal(sharefactor, action, value, date):
    return _clean(_mean(_slope(_diff(sharefactor, 4), 8), 4))
def cg_f034_share_factor_splits_core101_3rd_v102_signal(sharefactor, action, value, date):
    return _clean(_mean(_slope(_diff(value, 4), 8), 4))
def cg_f034_share_factor_splits_core102_3rd_v103_signal(sharefactor, action, value, date):
    return _clean(_mean(_slope(_diff(_diff(sharefactor, 1), 4), 8), 4))
def cg_f034_share_factor_splits_core103_3rd_v104_signal(sharefactor, action, value, date):
    return _clean(_mean(_slope(_diff(_pct_change(sharefactor, 1), 4), 8), 4))
def cg_f034_share_factor_splits_core104_3rd_v105_signal(sharefactor, action, value, date):
    return _clean(_mean(_slope(_diff(_slope(sharefactor, 4), 4), 8), 4))
def cg_f034_share_factor_splits_core105_3rd_v106_signal(sharefactor, action, value, date):
    return _clean(_mean(_slope(_diff(_z(sharefactor, 8), 4), 8), 4))
def cg_f034_share_factor_splits_core106_3rd_v107_signal(sharefactor, action, value, date):
    return _clean(_mean(_slope(_diff(sharefactor * value, 4), 8), 4))
def cg_f034_share_factor_splits_core107_3rd_v108_signal(sharefactor, action, value, date):
    return _clean(_mean(_slope(_diff(_safe_div(sharefactor, value.abs() + 1.0), 4), 8), 4))
def cg_f034_share_factor_splits_core108_3rd_v109_signal(sharefactor, action, value, date):
    return _clean(_mean(_slope(_diff(_diff(value, 4), 4), 8), 4))
def cg_f034_share_factor_splits_core109_3rd_v110_signal(sharefactor, action, value, date):
    return _clean(_mean(_slope(_diff(_mean(sharefactor, 4), 4), 8), 4))
def cg_f034_share_factor_splits_core110_3rd_v111_signal(sharefactor, action, value, date):
    return _clean(_mean(_diff(_slope(sharefactor, 4), 4), 4))
def cg_f034_share_factor_splits_core111_3rd_v112_signal(sharefactor, action, value, date):
    return _clean(_mean(_diff(_slope(value, 4), 4), 4))
def cg_f034_share_factor_splits_core112_3rd_v113_signal(sharefactor, action, value, date):
    return _clean(_mean(_diff(_slope(_diff(sharefactor, 1), 4), 4), 4))
def cg_f034_share_factor_splits_core113_3rd_v114_signal(sharefactor, action, value, date):
    return _clean(_mean(_diff(_slope(_pct_change(sharefactor, 1), 4), 4), 4))
def cg_f034_share_factor_splits_core114_3rd_v115_signal(sharefactor, action, value, date):
    return _clean(_mean(_diff(_slope(_slope(sharefactor, 4), 4), 4), 4))
def cg_f034_share_factor_splits_core115_3rd_v116_signal(sharefactor, action, value, date):
    return _clean(_mean(_diff(_slope(_z(sharefactor, 8), 4), 4), 4))
def cg_f034_share_factor_splits_core116_3rd_v117_signal(sharefactor, action, value, date):
    return _clean(_mean(_diff(_slope(sharefactor * value, 4), 4), 4))
def cg_f034_share_factor_splits_core117_3rd_v118_signal(sharefactor, action, value, date):
    return _clean(_mean(_diff(_slope(_safe_div(sharefactor, value.abs() + 1.0), 4), 4), 4))
def cg_f034_share_factor_splits_core118_3rd_v119_signal(sharefactor, action, value, date):
    return _clean(_mean(_diff(_slope(_diff(value, 4), 4), 4), 4))
def cg_f034_share_factor_splits_core119_3rd_v120_signal(sharefactor, action, value, date):
    return _clean(_mean(_diff(_slope(_mean(sharefactor, 4), 4), 4), 4))
def cg_f034_share_factor_splits_core120_3rd_v121_signal(sharefactor, action, value, date):
    return _clean(_slope(_diff(_diff(sharefactor, 4), 4), 4))
def cg_f034_share_factor_splits_core121_3rd_v122_signal(sharefactor, action, value, date):
    return _clean(_slope(_diff(_diff(value, 4), 4), 4))
def cg_f034_share_factor_splits_core122_3rd_v123_signal(sharefactor, action, value, date):
    return _clean(_slope(_diff(_diff(_diff(sharefactor, 1), 4), 4), 4))
def cg_f034_share_factor_splits_core123_3rd_v124_signal(sharefactor, action, value, date):
    return _clean(_slope(_diff(_diff(_pct_change(sharefactor, 1), 4), 4), 4))
def cg_f034_share_factor_splits_core124_3rd_v125_signal(sharefactor, action, value, date):
    return _clean(_slope(_diff(_diff(_slope(sharefactor, 4), 4), 4), 4))
def cg_f034_share_factor_splits_core125_3rd_v126_signal(sharefactor, action, value, date):
    return _clean(_slope(_diff(_diff(_z(sharefactor, 8), 4), 4), 4))
def cg_f034_share_factor_splits_core126_3rd_v127_signal(sharefactor, action, value, date):
    return _clean(_slope(_diff(_diff(sharefactor * value, 4), 4), 4))
def cg_f034_share_factor_splits_core127_3rd_v128_signal(sharefactor, action, value, date):
    return _clean(_slope(_diff(_diff(_safe_div(sharefactor, value.abs() + 1.0), 4), 4), 4))
def cg_f034_share_factor_splits_core128_3rd_v129_signal(sharefactor, action, value, date):
    return _clean(_slope(_diff(_diff(_diff(value, 4), 4), 4), 4))
def cg_f034_share_factor_splits_core129_3rd_v130_signal(sharefactor, action, value, date):
    return _clean(_slope(_diff(_diff(_mean(sharefactor, 4), 4), 4), 4))
def cg_f034_share_factor_splits_core130_3rd_v131_signal(sharefactor, action, value, date):
    return _clean(_diff(_diff(_diff(sharefactor, 4), 4), 4))
def cg_f034_share_factor_splits_core131_3rd_v132_signal(sharefactor, action, value, date):
    return _clean(_diff(_diff(_diff(value, 4), 4), 4))
def cg_f034_share_factor_splits_core132_3rd_v133_signal(sharefactor, action, value, date):
    return _clean(_diff(_diff(_diff(_diff(sharefactor, 1), 4), 4), 4))
def cg_f034_share_factor_splits_core133_3rd_v134_signal(sharefactor, action, value, date):
    return _clean(_diff(_diff(_diff(_pct_change(sharefactor, 1), 4), 4), 4))
def cg_f034_share_factor_splits_core134_3rd_v135_signal(sharefactor, action, value, date):
    return _clean(_diff(_diff(_diff(_slope(sharefactor, 4), 4), 4), 4))
def cg_f034_share_factor_splits_core135_3rd_v136_signal(sharefactor, action, value, date):
    return _clean(_diff(_diff(_diff(_z(sharefactor, 8), 4), 4), 4))
def cg_f034_share_factor_splits_core136_3rd_v137_signal(sharefactor, action, value, date):
    return _clean(_diff(_diff(_diff(sharefactor * value, 4), 4), 4))
def cg_f034_share_factor_splits_core137_3rd_v138_signal(sharefactor, action, value, date):
    return _clean(_diff(_diff(_diff(_safe_div(sharefactor, value.abs() + 1.0), 4), 4), 4))
def cg_f034_share_factor_splits_core138_3rd_v139_signal(sharefactor, action, value, date):
    return _clean(_diff(_diff(_diff(_diff(value, 4), 4), 4), 4))
def cg_f034_share_factor_splits_core139_3rd_v140_signal(sharefactor, action, value, date):
    return _clean(_diff(_diff(_diff(_mean(sharefactor, 4), 4), 4), 4))
def cg_f034_share_factor_splits_core140_3rd_v141_signal(sharefactor, action, value, date):
    return _clean(_z(_slope(_diff(_diff(sharefactor, 4), 4), 4), 8))
def cg_f034_share_factor_splits_core141_3rd_v142_signal(sharefactor, action, value, date):
    return _clean(_z(_slope(_diff(_diff(value, 4), 4), 4), 8))
def cg_f034_share_factor_splits_core142_3rd_v143_signal(sharefactor, action, value, date):
    return _clean(_z(_slope(_diff(_diff(_diff(sharefactor, 1), 4), 4), 4), 8))
def cg_f034_share_factor_splits_core143_3rd_v144_signal(sharefactor, action, value, date):
    return _clean(_z(_slope(_diff(_diff(_pct_change(sharefactor, 1), 4), 4), 4), 8))
def cg_f034_share_factor_splits_core144_3rd_v145_signal(sharefactor, action, value, date):
    return _clean(_z(_slope(_diff(_diff(_slope(sharefactor, 4), 4), 4), 4), 8))
def cg_f034_share_factor_splits_core145_3rd_v146_signal(sharefactor, action, value, date):
    return _clean(_z(_slope(_diff(_diff(_z(sharefactor, 8), 4), 4), 4), 8))
def cg_f034_share_factor_splits_core146_3rd_v147_signal(sharefactor, action, value, date):
    return _clean(_z(_slope(_diff(_diff(sharefactor * value, 4), 4), 4), 8))
def cg_f034_share_factor_splits_core147_3rd_v148_signal(sharefactor, action, value, date):
    return _clean(_z(_slope(_diff(_diff(_safe_div(sharefactor, value.abs() + 1.0), 4), 4), 4), 8))
def cg_f034_share_factor_splits_core148_3rd_v149_signal(sharefactor, action, value, date):
    return _clean(_z(_slope(_diff(_diff(_diff(value, 4), 4), 4), 4), 8))
def cg_f034_share_factor_splits_core149_3rd_v150_signal(sharefactor, action, value, date):
    return _clean(_z(_slope(_diff(_diff(_mean(sharefactor, 4), 4), 4), 4), 8))