import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f096_holder_concentration_core00_2nd_v001_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(value, 4))
def cg_f096_holder_concentration_core01_2nd_v002_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(units, 4))
def cg_f096_holder_concentration_core02_2nd_v003_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(shrholders, 4))
def cg_f096_holder_concentration_core03_2nd_v004_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(totalvalue, 4))
def cg_f096_holder_concentration_core04_2nd_v005_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(percentoftotal, 4))
def cg_f096_holder_concentration_core05_2nd_v006_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_safe_div(value, totalvalue), 4))
def cg_f096_holder_concentration_core06_2nd_v007_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_safe_div(units, shrholders), 4))
def cg_f096_holder_concentration_core07_2nd_v008_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_safe_div(totalvalue, shrholders), 4))
def cg_f096_holder_concentration_core08_2nd_v009_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_log(totalvalue + 1.0), 4))
def cg_f096_holder_concentration_core09_2nd_v010_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_log(shrholders + 1.0), 4))
def cg_f096_holder_concentration_core10_2nd_v011_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(value, 8))
def cg_f096_holder_concentration_core11_2nd_v012_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(units, 8))
def cg_f096_holder_concentration_core12_2nd_v013_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(shrholders, 8))
def cg_f096_holder_concentration_core13_2nd_v014_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(totalvalue, 8))
def cg_f096_holder_concentration_core14_2nd_v015_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(percentoftotal, 8))
def cg_f096_holder_concentration_core15_2nd_v016_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_safe_div(value, totalvalue), 8))
def cg_f096_holder_concentration_core16_2nd_v017_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_safe_div(units, shrholders), 8))
def cg_f096_holder_concentration_core17_2nd_v018_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_safe_div(totalvalue, shrholders), 8))
def cg_f096_holder_concentration_core18_2nd_v019_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_log(totalvalue + 1.0), 8))
def cg_f096_holder_concentration_core19_2nd_v020_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_log(shrholders + 1.0), 8))
def cg_f096_holder_concentration_core20_2nd_v021_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(value, 4))
def cg_f096_holder_concentration_core21_2nd_v022_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(units, 4))
def cg_f096_holder_concentration_core22_2nd_v023_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(shrholders, 4))
def cg_f096_holder_concentration_core23_2nd_v024_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(totalvalue, 4))
def cg_f096_holder_concentration_core24_2nd_v025_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(percentoftotal, 4))
def cg_f096_holder_concentration_core25_2nd_v026_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_safe_div(value, totalvalue), 4))
def cg_f096_holder_concentration_core26_2nd_v027_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_safe_div(units, shrholders), 4))
def cg_f096_holder_concentration_core27_2nd_v028_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_safe_div(totalvalue, shrholders), 4))
def cg_f096_holder_concentration_core28_2nd_v029_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_log(totalvalue + 1.0), 4))
def cg_f096_holder_concentration_core29_2nd_v030_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_log(shrholders + 1.0), 4))
def cg_f096_holder_concentration_core30_2nd_v031_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_slope(value, 4), 8))
def cg_f096_holder_concentration_core31_2nd_v032_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_slope(units, 4), 8))
def cg_f096_holder_concentration_core32_2nd_v033_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_slope(shrholders, 4), 8))
def cg_f096_holder_concentration_core33_2nd_v034_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_slope(totalvalue, 4), 8))
def cg_f096_holder_concentration_core34_2nd_v035_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_slope(percentoftotal, 4), 8))
def cg_f096_holder_concentration_core35_2nd_v036_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_slope(_safe_div(value, totalvalue), 4), 8))
def cg_f096_holder_concentration_core36_2nd_v037_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_slope(_safe_div(units, shrholders), 4), 8))
def cg_f096_holder_concentration_core37_2nd_v038_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_slope(_safe_div(totalvalue, shrholders), 4), 8))
def cg_f096_holder_concentration_core38_2nd_v039_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_slope(_log(totalvalue + 1.0), 4), 8))
def cg_f096_holder_concentration_core39_2nd_v040_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_slope(_log(shrholders + 1.0), 4), 8))
def cg_f096_holder_concentration_core40_2nd_v041_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_slope(value, 8), 12))
def cg_f096_holder_concentration_core41_2nd_v042_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_slope(units, 8), 12))
def cg_f096_holder_concentration_core42_2nd_v043_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_slope(shrholders, 8), 12))
def cg_f096_holder_concentration_core43_2nd_v044_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_slope(totalvalue, 8), 12))
def cg_f096_holder_concentration_core44_2nd_v045_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_slope(percentoftotal, 8), 12))
def cg_f096_holder_concentration_core45_2nd_v046_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_slope(_safe_div(value, totalvalue), 8), 12))
def cg_f096_holder_concentration_core46_2nd_v047_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_slope(_safe_div(units, shrholders), 8), 12))
def cg_f096_holder_concentration_core47_2nd_v048_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_slope(_safe_div(totalvalue, shrholders), 8), 12))
def cg_f096_holder_concentration_core48_2nd_v049_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_slope(_log(totalvalue + 1.0), 8), 12))
def cg_f096_holder_concentration_core49_2nd_v050_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_slope(_log(shrholders + 1.0), 8), 12))
def cg_f096_holder_concentration_core50_2nd_v051_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_diff(value, 4), 8))
def cg_f096_holder_concentration_core51_2nd_v052_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_diff(units, 4), 8))
def cg_f096_holder_concentration_core52_2nd_v053_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_diff(shrholders, 4), 8))
def cg_f096_holder_concentration_core53_2nd_v054_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_diff(totalvalue, 4), 8))
def cg_f096_holder_concentration_core54_2nd_v055_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_diff(percentoftotal, 4), 8))
def cg_f096_holder_concentration_core55_2nd_v056_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_diff(_safe_div(value, totalvalue), 4), 8))
def cg_f096_holder_concentration_core56_2nd_v057_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_diff(_safe_div(units, shrholders), 4), 8))
def cg_f096_holder_concentration_core57_2nd_v058_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_diff(_safe_div(totalvalue, shrholders), 4), 8))
def cg_f096_holder_concentration_core58_2nd_v059_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_diff(_log(totalvalue + 1.0), 4), 8))
def cg_f096_holder_concentration_core59_2nd_v060_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_diff(_log(shrholders + 1.0), 4), 8))
def cg_f096_holder_concentration_core60_2nd_v061_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_slope(value, 4), 12))
def cg_f096_holder_concentration_core61_2nd_v062_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_slope(units, 4), 12))
def cg_f096_holder_concentration_core62_2nd_v063_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_slope(shrholders, 4), 12))
def cg_f096_holder_concentration_core63_2nd_v064_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_slope(totalvalue, 4), 12))
def cg_f096_holder_concentration_core64_2nd_v065_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_slope(percentoftotal, 4), 12))
def cg_f096_holder_concentration_core65_2nd_v066_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_slope(_safe_div(value, totalvalue), 4), 12))
def cg_f096_holder_concentration_core66_2nd_v067_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_slope(_safe_div(units, shrholders), 4), 12))
def cg_f096_holder_concentration_core67_2nd_v068_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_slope(_safe_div(totalvalue, shrholders), 4), 12))
def cg_f096_holder_concentration_core68_2nd_v069_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_slope(_log(totalvalue + 1.0), 4), 12))
def cg_f096_holder_concentration_core69_2nd_v070_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_slope(_log(shrholders + 1.0), 4), 12))
def cg_f096_holder_concentration_core70_2nd_v071_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_diff(value, 4), 12))
def cg_f096_holder_concentration_core71_2nd_v072_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_diff(units, 4), 12))
def cg_f096_holder_concentration_core72_2nd_v073_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_diff(shrholders, 4), 12))
def cg_f096_holder_concentration_core73_2nd_v074_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_diff(totalvalue, 4), 12))
def cg_f096_holder_concentration_core74_2nd_v075_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_diff(percentoftotal, 4), 12))
def cg_f096_holder_concentration_core75_2nd_v076_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_diff(_safe_div(value, totalvalue), 4), 12))
def cg_f096_holder_concentration_core76_2nd_v077_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_diff(_safe_div(units, shrholders), 4), 12))
def cg_f096_holder_concentration_core77_2nd_v078_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_diff(_safe_div(totalvalue, shrholders), 4), 12))
def cg_f096_holder_concentration_core78_2nd_v079_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_diff(_log(totalvalue + 1.0), 4), 12))
def cg_f096_holder_concentration_core79_2nd_v080_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_diff(_log(shrholders + 1.0), 4), 12))
def cg_f096_holder_concentration_core80_2nd_v081_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_slope(value, 4), 4))
def cg_f096_holder_concentration_core81_2nd_v082_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_slope(units, 4), 4))
def cg_f096_holder_concentration_core82_2nd_v083_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_slope(shrholders, 4), 4))
def cg_f096_holder_concentration_core83_2nd_v084_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_slope(totalvalue, 4), 4))
def cg_f096_holder_concentration_core84_2nd_v085_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_slope(percentoftotal, 4), 4))
def cg_f096_holder_concentration_core85_2nd_v086_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_slope(_safe_div(value, totalvalue), 4), 4))
def cg_f096_holder_concentration_core86_2nd_v087_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_slope(_safe_div(units, shrholders), 4), 4))
def cg_f096_holder_concentration_core87_2nd_v088_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_slope(_safe_div(totalvalue, shrholders), 4), 4))
def cg_f096_holder_concentration_core88_2nd_v089_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_slope(_log(totalvalue + 1.0), 4), 4))
def cg_f096_holder_concentration_core89_2nd_v090_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_slope(_log(shrholders + 1.0), 4), 4))
def cg_f096_holder_concentration_core90_2nd_v091_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_diff(value, 4), 4))
def cg_f096_holder_concentration_core91_2nd_v092_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_diff(units, 4), 4))
def cg_f096_holder_concentration_core92_2nd_v093_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_diff(shrholders, 4), 4))
def cg_f096_holder_concentration_core93_2nd_v094_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_diff(totalvalue, 4), 4))
def cg_f096_holder_concentration_core94_2nd_v095_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_diff(percentoftotal, 4), 4))
def cg_f096_holder_concentration_core95_2nd_v096_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_diff(_safe_div(value, totalvalue), 4), 4))
def cg_f096_holder_concentration_core96_2nd_v097_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_diff(_safe_div(units, shrholders), 4), 4))
def cg_f096_holder_concentration_core97_2nd_v098_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_diff(_safe_div(totalvalue, shrholders), 4), 4))
def cg_f096_holder_concentration_core98_2nd_v099_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_diff(_log(totalvalue + 1.0), 4), 4))
def cg_f096_holder_concentration_core99_2nd_v100_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_diff(_log(shrholders + 1.0), 4), 4))
def cg_f096_holder_concentration_core100_2nd_v101_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_mean(value, 4), 4))
def cg_f096_holder_concentration_core101_2nd_v102_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_mean(units, 4), 4))
def cg_f096_holder_concentration_core102_2nd_v103_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_mean(shrholders, 4), 4))
def cg_f096_holder_concentration_core103_2nd_v104_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_mean(totalvalue, 4), 4))
def cg_f096_holder_concentration_core104_2nd_v105_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_mean(percentoftotal, 4), 4))
def cg_f096_holder_concentration_core105_2nd_v106_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_mean(_safe_div(value, totalvalue), 4), 4))
def cg_f096_holder_concentration_core106_2nd_v107_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_mean(_safe_div(units, shrholders), 4), 4))
def cg_f096_holder_concentration_core107_2nd_v108_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_mean(_safe_div(totalvalue, shrholders), 4), 4))
def cg_f096_holder_concentration_core108_2nd_v109_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_mean(_log(totalvalue + 1.0), 4), 4))
def cg_f096_holder_concentration_core109_2nd_v110_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_mean(_log(shrholders + 1.0), 4), 4))
def cg_f096_holder_concentration_core110_2nd_v111_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_mean(value, 8), 8))
def cg_f096_holder_concentration_core111_2nd_v112_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_mean(units, 8), 8))
def cg_f096_holder_concentration_core112_2nd_v113_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_mean(shrholders, 8), 8))
def cg_f096_holder_concentration_core113_2nd_v114_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_mean(totalvalue, 8), 8))
def cg_f096_holder_concentration_core114_2nd_v115_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_mean(percentoftotal, 8), 8))
def cg_f096_holder_concentration_core115_2nd_v116_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_mean(_safe_div(value, totalvalue), 8), 8))
def cg_f096_holder_concentration_core116_2nd_v117_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_mean(_safe_div(units, shrholders), 8), 8))
def cg_f096_holder_concentration_core117_2nd_v118_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_mean(_safe_div(totalvalue, shrholders), 8), 8))
def cg_f096_holder_concentration_core118_2nd_v119_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_mean(_log(totalvalue + 1.0), 8), 8))
def cg_f096_holder_concentration_core119_2nd_v120_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_mean(_log(shrholders + 1.0), 8), 8))
def cg_f096_holder_concentration_core120_2nd_v121_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_mean(value, 4), 4))
def cg_f096_holder_concentration_core121_2nd_v122_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_mean(units, 4), 4))
def cg_f096_holder_concentration_core122_2nd_v123_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_mean(shrholders, 4), 4))
def cg_f096_holder_concentration_core123_2nd_v124_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_mean(totalvalue, 4), 4))
def cg_f096_holder_concentration_core124_2nd_v125_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_mean(percentoftotal, 4), 4))
def cg_f096_holder_concentration_core125_2nd_v126_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_mean(_safe_div(value, totalvalue), 4), 4))
def cg_f096_holder_concentration_core126_2nd_v127_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_mean(_safe_div(units, shrholders), 4), 4))
def cg_f096_holder_concentration_core127_2nd_v128_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_mean(_safe_div(totalvalue, shrholders), 4), 4))
def cg_f096_holder_concentration_core128_2nd_v129_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_mean(_log(totalvalue + 1.0), 4), 4))
def cg_f096_holder_concentration_core129_2nd_v130_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_mean(_log(shrholders + 1.0), 4), 4))
def cg_f096_holder_concentration_core130_2nd_v131_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_diff(_mean(value, 4), 4), 8))
def cg_f096_holder_concentration_core131_2nd_v132_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_diff(_mean(units, 4), 4), 8))
def cg_f096_holder_concentration_core132_2nd_v133_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_diff(_mean(shrholders, 4), 4), 8))
def cg_f096_holder_concentration_core133_2nd_v134_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_diff(_mean(totalvalue, 4), 4), 8))
def cg_f096_holder_concentration_core134_2nd_v135_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_diff(_mean(percentoftotal, 4), 4), 8))
def cg_f096_holder_concentration_core135_2nd_v136_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_diff(_mean(_safe_div(value, totalvalue), 4), 4), 8))
def cg_f096_holder_concentration_core136_2nd_v137_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_diff(_mean(_safe_div(units, shrholders), 4), 4), 8))
def cg_f096_holder_concentration_core137_2nd_v138_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_diff(_mean(_safe_div(totalvalue, shrholders), 4), 4), 8))
def cg_f096_holder_concentration_core138_2nd_v139_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_diff(_mean(_log(totalvalue + 1.0), 4), 4), 8))
def cg_f096_holder_concentration_core139_2nd_v140_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_diff(_mean(_log(shrholders + 1.0), 4), 4), 8))
def cg_f096_holder_concentration_core140_2nd_v141_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_slope(_mean(value, 4), 4), 12))
def cg_f096_holder_concentration_core141_2nd_v142_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_slope(_mean(units, 4), 4), 12))
def cg_f096_holder_concentration_core142_2nd_v143_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_slope(_mean(shrholders, 4), 4), 12))
def cg_f096_holder_concentration_core143_2nd_v144_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_slope(_mean(totalvalue, 4), 4), 12))
def cg_f096_holder_concentration_core144_2nd_v145_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_slope(_mean(percentoftotal, 4), 4), 12))
def cg_f096_holder_concentration_core145_2nd_v146_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_slope(_mean(_safe_div(value, totalvalue), 4), 4), 12))
def cg_f096_holder_concentration_core146_2nd_v147_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_slope(_mean(_safe_div(units, shrholders), 4), 4), 12))
def cg_f096_holder_concentration_core147_2nd_v148_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_slope(_mean(_safe_div(totalvalue, shrholders), 4), 4), 12))
def cg_f096_holder_concentration_core148_2nd_v149_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_slope(_mean(_log(totalvalue + 1.0), 4), 4), 12))
def cg_f096_holder_concentration_core149_2nd_v150_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_slope(_mean(_log(shrholders + 1.0), 4), 4), 12))