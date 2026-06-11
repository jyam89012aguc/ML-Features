import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f096_holder_concentration_core00_3rd_v001_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_diff(value, 4), 4))
def cg_f096_holder_concentration_core01_3rd_v002_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_diff(units, 4), 4))
def cg_f096_holder_concentration_core02_3rd_v003_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_diff(shrholders, 4), 4))
def cg_f096_holder_concentration_core03_3rd_v004_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_diff(totalvalue, 4), 4))
def cg_f096_holder_concentration_core04_3rd_v005_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_diff(percentoftotal, 4), 4))
def cg_f096_holder_concentration_core05_3rd_v006_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_diff(_safe_div(value, totalvalue), 4), 4))
def cg_f096_holder_concentration_core06_3rd_v007_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_diff(_safe_div(units, shrholders), 4), 4))
def cg_f096_holder_concentration_core07_3rd_v008_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_diff(_safe_div(totalvalue, shrholders), 4), 4))
def cg_f096_holder_concentration_core08_3rd_v009_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_diff(_log(totalvalue + 1.0), 4), 4))
def cg_f096_holder_concentration_core09_3rd_v010_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_diff(_log(shrholders + 1.0), 4), 4))
def cg_f096_holder_concentration_core10_3rd_v011_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_diff(value, 4), 8))
def cg_f096_holder_concentration_core11_3rd_v012_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_diff(units, 4), 8))
def cg_f096_holder_concentration_core12_3rd_v013_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_diff(shrholders, 4), 8))
def cg_f096_holder_concentration_core13_3rd_v014_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_diff(totalvalue, 4), 8))
def cg_f096_holder_concentration_core14_3rd_v015_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_diff(percentoftotal, 4), 8))
def cg_f096_holder_concentration_core15_3rd_v016_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_diff(_safe_div(value, totalvalue), 4), 8))
def cg_f096_holder_concentration_core16_3rd_v017_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_diff(_safe_div(units, shrholders), 4), 8))
def cg_f096_holder_concentration_core17_3rd_v018_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_diff(_safe_div(totalvalue, shrholders), 4), 8))
def cg_f096_holder_concentration_core18_3rd_v019_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_diff(_log(totalvalue + 1.0), 4), 8))
def cg_f096_holder_concentration_core19_3rd_v020_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_diff(_log(shrholders + 1.0), 4), 8))
def cg_f096_holder_concentration_core20_3rd_v021_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_slope(value, 4), 4))
def cg_f096_holder_concentration_core21_3rd_v022_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_slope(units, 4), 4))
def cg_f096_holder_concentration_core22_3rd_v023_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_slope(shrholders, 4), 4))
def cg_f096_holder_concentration_core23_3rd_v024_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_slope(totalvalue, 4), 4))
def cg_f096_holder_concentration_core24_3rd_v025_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_slope(percentoftotal, 4), 4))
def cg_f096_holder_concentration_core25_3rd_v026_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_slope(_safe_div(value, totalvalue), 4), 4))
def cg_f096_holder_concentration_core26_3rd_v027_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_slope(_safe_div(units, shrholders), 4), 4))
def cg_f096_holder_concentration_core27_3rd_v028_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_slope(_safe_div(totalvalue, shrholders), 4), 4))
def cg_f096_holder_concentration_core28_3rd_v029_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_slope(_log(totalvalue + 1.0), 4), 4))
def cg_f096_holder_concentration_core29_3rd_v030_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_slope(_log(shrholders + 1.0), 4), 4))
def cg_f096_holder_concentration_core30_3rd_v031_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_diff(_diff(value, 4), 4), 8))
def cg_f096_holder_concentration_core31_3rd_v032_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_diff(_diff(units, 4), 4), 8))
def cg_f096_holder_concentration_core32_3rd_v033_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_diff(_diff(shrholders, 4), 4), 8))
def cg_f096_holder_concentration_core33_3rd_v034_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_diff(_diff(totalvalue, 4), 4), 8))
def cg_f096_holder_concentration_core34_3rd_v035_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_diff(_diff(percentoftotal, 4), 4), 8))
def cg_f096_holder_concentration_core35_3rd_v036_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_diff(_diff(_safe_div(value, totalvalue), 4), 4), 8))
def cg_f096_holder_concentration_core36_3rd_v037_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_diff(_diff(_safe_div(units, shrholders), 4), 4), 8))
def cg_f096_holder_concentration_core37_3rd_v038_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_diff(_diff(_safe_div(totalvalue, shrholders), 4), 4), 8))
def cg_f096_holder_concentration_core38_3rd_v039_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_diff(_diff(_log(totalvalue + 1.0), 4), 4), 8))
def cg_f096_holder_concentration_core39_3rd_v040_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_diff(_diff(_log(shrholders + 1.0), 4), 4), 8))
def cg_f096_holder_concentration_core40_3rd_v041_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_slope(_diff(value, 4), 8), 12))
def cg_f096_holder_concentration_core41_3rd_v042_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_slope(_diff(units, 4), 8), 12))
def cg_f096_holder_concentration_core42_3rd_v043_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_slope(_diff(shrholders, 4), 8), 12))
def cg_f096_holder_concentration_core43_3rd_v044_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_slope(_diff(totalvalue, 4), 8), 12))
def cg_f096_holder_concentration_core44_3rd_v045_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_slope(_diff(percentoftotal, 4), 8), 12))
def cg_f096_holder_concentration_core45_3rd_v046_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_slope(_diff(_safe_div(value, totalvalue), 4), 8), 12))
def cg_f096_holder_concentration_core46_3rd_v047_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_slope(_diff(_safe_div(units, shrholders), 4), 8), 12))
def cg_f096_holder_concentration_core47_3rd_v048_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_slope(_diff(_safe_div(totalvalue, shrholders), 4), 8), 12))
def cg_f096_holder_concentration_core48_3rd_v049_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_slope(_diff(_log(totalvalue + 1.0), 4), 8), 12))
def cg_f096_holder_concentration_core49_3rd_v050_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_slope(_diff(_log(shrholders + 1.0), 4), 8), 12))
def cg_f096_holder_concentration_core50_3rd_v051_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_diff(_slope(value, 4), 4), 8))
def cg_f096_holder_concentration_core51_3rd_v052_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_diff(_slope(units, 4), 4), 8))
def cg_f096_holder_concentration_core52_3rd_v053_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_diff(_slope(shrholders, 4), 4), 8))
def cg_f096_holder_concentration_core53_3rd_v054_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_diff(_slope(totalvalue, 4), 4), 8))
def cg_f096_holder_concentration_core54_3rd_v055_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_diff(_slope(percentoftotal, 4), 4), 8))
def cg_f096_holder_concentration_core55_3rd_v056_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_diff(_slope(_safe_div(value, totalvalue), 4), 4), 8))
def cg_f096_holder_concentration_core56_3rd_v057_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_diff(_slope(_safe_div(units, shrholders), 4), 4), 8))
def cg_f096_holder_concentration_core57_3rd_v058_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_diff(_slope(_safe_div(totalvalue, shrholders), 4), 4), 8))
def cg_f096_holder_concentration_core58_3rd_v059_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_diff(_slope(_log(totalvalue + 1.0), 4), 4), 8))
def cg_f096_holder_concentration_core59_3rd_v060_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_diff(_slope(_log(shrholders + 1.0), 4), 4), 8))
def cg_f096_holder_concentration_core60_3rd_v061_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_diff(_diff(value, 4), 4), 12))
def cg_f096_holder_concentration_core61_3rd_v062_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_diff(_diff(units, 4), 4), 12))
def cg_f096_holder_concentration_core62_3rd_v063_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_diff(_diff(shrholders, 4), 4), 12))
def cg_f096_holder_concentration_core63_3rd_v064_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_diff(_diff(totalvalue, 4), 4), 12))
def cg_f096_holder_concentration_core64_3rd_v065_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_diff(_diff(percentoftotal, 4), 4), 12))
def cg_f096_holder_concentration_core65_3rd_v066_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_diff(_diff(_safe_div(value, totalvalue), 4), 4), 12))
def cg_f096_holder_concentration_core66_3rd_v067_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_diff(_diff(_safe_div(units, shrholders), 4), 4), 12))
def cg_f096_holder_concentration_core67_3rd_v068_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_diff(_diff(_safe_div(totalvalue, shrholders), 4), 4), 12))
def cg_f096_holder_concentration_core68_3rd_v069_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_diff(_diff(_log(totalvalue + 1.0), 4), 4), 12))
def cg_f096_holder_concentration_core69_3rd_v070_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_diff(_diff(_log(shrholders + 1.0), 4), 4), 12))
def cg_f096_holder_concentration_core70_3rd_v071_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_slope(_diff(value, 4), 8), 12))
def cg_f096_holder_concentration_core71_3rd_v072_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_slope(_diff(units, 4), 8), 12))
def cg_f096_holder_concentration_core72_3rd_v073_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_slope(_diff(shrholders, 4), 8), 12))
def cg_f096_holder_concentration_core73_3rd_v074_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_slope(_diff(totalvalue, 4), 8), 12))
def cg_f096_holder_concentration_core74_3rd_v075_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_slope(_diff(percentoftotal, 4), 8), 12))
def cg_f096_holder_concentration_core75_3rd_v076_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_slope(_diff(_safe_div(value, totalvalue), 4), 8), 12))
def cg_f096_holder_concentration_core76_3rd_v077_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_slope(_diff(_safe_div(units, shrholders), 4), 8), 12))
def cg_f096_holder_concentration_core77_3rd_v078_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_slope(_diff(_safe_div(totalvalue, shrholders), 4), 8), 12))
def cg_f096_holder_concentration_core78_3rd_v079_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_slope(_diff(_log(totalvalue + 1.0), 4), 8), 12))
def cg_f096_holder_concentration_core79_3rd_v080_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_slope(_diff(_log(shrholders + 1.0), 4), 8), 12))
def cg_f096_holder_concentration_core80_3rd_v081_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_diff(_slope(value, 4), 4), 12))
def cg_f096_holder_concentration_core81_3rd_v082_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_diff(_slope(units, 4), 4), 12))
def cg_f096_holder_concentration_core82_3rd_v083_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_diff(_slope(shrholders, 4), 4), 12))
def cg_f096_holder_concentration_core83_3rd_v084_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_diff(_slope(totalvalue, 4), 4), 12))
def cg_f096_holder_concentration_core84_3rd_v085_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_diff(_slope(percentoftotal, 4), 4), 12))
def cg_f096_holder_concentration_core85_3rd_v086_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_diff(_slope(_safe_div(value, totalvalue), 4), 4), 12))
def cg_f096_holder_concentration_core86_3rd_v087_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_diff(_slope(_safe_div(units, shrholders), 4), 4), 12))
def cg_f096_holder_concentration_core87_3rd_v088_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_diff(_slope(_safe_div(totalvalue, shrholders), 4), 4), 12))
def cg_f096_holder_concentration_core88_3rd_v089_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_diff(_slope(_log(totalvalue + 1.0), 4), 4), 12))
def cg_f096_holder_concentration_core89_3rd_v090_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_rank(_diff(_slope(_log(shrholders + 1.0), 4), 4), 12))
def cg_f096_holder_concentration_core90_3rd_v091_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_diff(_diff(value, 4), 4), 4))
def cg_f096_holder_concentration_core91_3rd_v092_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_diff(_diff(units, 4), 4), 4))
def cg_f096_holder_concentration_core92_3rd_v093_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_diff(_diff(shrholders, 4), 4), 4))
def cg_f096_holder_concentration_core93_3rd_v094_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_diff(_diff(totalvalue, 4), 4), 4))
def cg_f096_holder_concentration_core94_3rd_v095_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_diff(_diff(percentoftotal, 4), 4), 4))
def cg_f096_holder_concentration_core95_3rd_v096_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_diff(_diff(_safe_div(value, totalvalue), 4), 4), 4))
def cg_f096_holder_concentration_core96_3rd_v097_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_diff(_diff(_safe_div(units, shrholders), 4), 4), 4))
def cg_f096_holder_concentration_core97_3rd_v098_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_diff(_diff(_safe_div(totalvalue, shrholders), 4), 4), 4))
def cg_f096_holder_concentration_core98_3rd_v099_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_diff(_diff(_log(totalvalue + 1.0), 4), 4), 4))
def cg_f096_holder_concentration_core99_3rd_v100_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_diff(_diff(_log(shrholders + 1.0), 4), 4), 4))
def cg_f096_holder_concentration_core100_3rd_v101_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_slope(_diff(value, 4), 8), 4))
def cg_f096_holder_concentration_core101_3rd_v102_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_slope(_diff(units, 4), 8), 4))
def cg_f096_holder_concentration_core102_3rd_v103_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_slope(_diff(shrholders, 4), 8), 4))
def cg_f096_holder_concentration_core103_3rd_v104_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_slope(_diff(totalvalue, 4), 8), 4))
def cg_f096_holder_concentration_core104_3rd_v105_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_slope(_diff(percentoftotal, 4), 8), 4))
def cg_f096_holder_concentration_core105_3rd_v106_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_slope(_diff(_safe_div(value, totalvalue), 4), 8), 4))
def cg_f096_holder_concentration_core106_3rd_v107_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_slope(_diff(_safe_div(units, shrholders), 4), 8), 4))
def cg_f096_holder_concentration_core107_3rd_v108_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_slope(_diff(_safe_div(totalvalue, shrholders), 4), 8), 4))
def cg_f096_holder_concentration_core108_3rd_v109_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_slope(_diff(_log(totalvalue + 1.0), 4), 8), 4))
def cg_f096_holder_concentration_core109_3rd_v110_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_slope(_diff(_log(shrholders + 1.0), 4), 8), 4))
def cg_f096_holder_concentration_core110_3rd_v111_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_diff(_slope(value, 4), 4), 4))
def cg_f096_holder_concentration_core111_3rd_v112_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_diff(_slope(units, 4), 4), 4))
def cg_f096_holder_concentration_core112_3rd_v113_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_diff(_slope(shrholders, 4), 4), 4))
def cg_f096_holder_concentration_core113_3rd_v114_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_diff(_slope(totalvalue, 4), 4), 4))
def cg_f096_holder_concentration_core114_3rd_v115_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_diff(_slope(percentoftotal, 4), 4), 4))
def cg_f096_holder_concentration_core115_3rd_v116_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_diff(_slope(_safe_div(value, totalvalue), 4), 4), 4))
def cg_f096_holder_concentration_core116_3rd_v117_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_diff(_slope(_safe_div(units, shrholders), 4), 4), 4))
def cg_f096_holder_concentration_core117_3rd_v118_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_diff(_slope(_safe_div(totalvalue, shrholders), 4), 4), 4))
def cg_f096_holder_concentration_core118_3rd_v119_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_diff(_slope(_log(totalvalue + 1.0), 4), 4), 4))
def cg_f096_holder_concentration_core119_3rd_v120_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_mean(_diff(_slope(_log(shrholders + 1.0), 4), 4), 4))
def cg_f096_holder_concentration_core120_3rd_v121_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_diff(_diff(value, 4), 4), 4))
def cg_f096_holder_concentration_core121_3rd_v122_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_diff(_diff(units, 4), 4), 4))
def cg_f096_holder_concentration_core122_3rd_v123_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_diff(_diff(shrholders, 4), 4), 4))
def cg_f096_holder_concentration_core123_3rd_v124_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_diff(_diff(totalvalue, 4), 4), 4))
def cg_f096_holder_concentration_core124_3rd_v125_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_diff(_diff(percentoftotal, 4), 4), 4))
def cg_f096_holder_concentration_core125_3rd_v126_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_diff(_diff(_safe_div(value, totalvalue), 4), 4), 4))
def cg_f096_holder_concentration_core126_3rd_v127_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_diff(_diff(_safe_div(units, shrholders), 4), 4), 4))
def cg_f096_holder_concentration_core127_3rd_v128_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_diff(_diff(_safe_div(totalvalue, shrholders), 4), 4), 4))
def cg_f096_holder_concentration_core128_3rd_v129_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_diff(_diff(_log(totalvalue + 1.0), 4), 4), 4))
def cg_f096_holder_concentration_core129_3rd_v130_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_diff(_diff(_log(shrholders + 1.0), 4), 4), 4))
def cg_f096_holder_concentration_core130_3rd_v131_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_diff(_diff(value, 4), 4), 4))
def cg_f096_holder_concentration_core131_3rd_v132_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_diff(_diff(units, 4), 4), 4))
def cg_f096_holder_concentration_core132_3rd_v133_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_diff(_diff(shrholders, 4), 4), 4))
def cg_f096_holder_concentration_core133_3rd_v134_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_diff(_diff(totalvalue, 4), 4), 4))
def cg_f096_holder_concentration_core134_3rd_v135_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_diff(_diff(percentoftotal, 4), 4), 4))
def cg_f096_holder_concentration_core135_3rd_v136_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_diff(_diff(_safe_div(value, totalvalue), 4), 4), 4))
def cg_f096_holder_concentration_core136_3rd_v137_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_diff(_diff(_safe_div(units, shrholders), 4), 4), 4))
def cg_f096_holder_concentration_core137_3rd_v138_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_diff(_diff(_safe_div(totalvalue, shrholders), 4), 4), 4))
def cg_f096_holder_concentration_core138_3rd_v139_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_diff(_diff(_log(totalvalue + 1.0), 4), 4), 4))
def cg_f096_holder_concentration_core139_3rd_v140_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_diff(_diff(_log(shrholders + 1.0), 4), 4), 4))
def cg_f096_holder_concentration_core140_3rd_v141_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_slope(_diff(_diff(value, 4), 4), 4), 8))
def cg_f096_holder_concentration_core141_3rd_v142_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_slope(_diff(_diff(units, 4), 4), 4), 8))
def cg_f096_holder_concentration_core142_3rd_v143_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_slope(_diff(_diff(shrholders, 4), 4), 4), 8))
def cg_f096_holder_concentration_core143_3rd_v144_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_slope(_diff(_diff(totalvalue, 4), 4), 4), 8))
def cg_f096_holder_concentration_core144_3rd_v145_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_slope(_diff(_diff(percentoftotal, 4), 4), 4), 8))
def cg_f096_holder_concentration_core145_3rd_v146_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_slope(_diff(_diff(_safe_div(value, totalvalue), 4), 4), 4), 8))
def cg_f096_holder_concentration_core146_3rd_v147_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_slope(_diff(_diff(_safe_div(units, shrholders), 4), 4), 4), 8))
def cg_f096_holder_concentration_core147_3rd_v148_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_slope(_diff(_diff(_safe_div(totalvalue, shrholders), 4), 4), 4), 8))
def cg_f096_holder_concentration_core148_3rd_v149_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_slope(_diff(_diff(_log(totalvalue + 1.0), 4), 4), 4), 8))
def cg_f096_holder_concentration_core149_3rd_v150_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_z(_slope(_diff(_diff(_log(shrholders + 1.0), 4), 4), 4), 8))