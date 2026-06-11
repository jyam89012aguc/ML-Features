import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f083_listing_status_and_dates_core00_2nd_v001_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_to_num(isdelisted), 4))
def cg_f083_listing_status_and_dates_core01_2nd_v002_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_to_num(firstpricedate), 4))
def cg_f083_listing_status_and_dates_core02_2nd_v003_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_to_num(lastpricedate), 4))
def cg_f083_listing_status_and_dates_core03_2nd_v004_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_to_num(firstquarter), 4))
def cg_f083_listing_status_and_dates_core04_2nd_v005_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_to_num(lastquarter), 4))
def cg_f083_listing_status_and_dates_core05_2nd_v006_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_event_flag(isdelisted), 4))
def cg_f083_listing_status_and_dates_core06_2nd_v007_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_event_count(lastpricedate, 4), 4))
def cg_f083_listing_status_and_dates_core07_2nd_v008_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_event_rate(lastquarter, 8), 4))
def cg_f083_listing_status_and_dates_core08_2nd_v009_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_to_num(lastpricedate) - _to_num(firstpricedate), 4))
def cg_f083_listing_status_and_dates_core09_2nd_v010_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_to_num(lastquarter) - _to_num(firstquarter), 4))
def cg_f083_listing_status_and_dates_core10_2nd_v011_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_to_num(isdelisted), 8))
def cg_f083_listing_status_and_dates_core11_2nd_v012_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_to_num(firstpricedate), 8))
def cg_f083_listing_status_and_dates_core12_2nd_v013_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_to_num(lastpricedate), 8))
def cg_f083_listing_status_and_dates_core13_2nd_v014_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_to_num(firstquarter), 8))
def cg_f083_listing_status_and_dates_core14_2nd_v015_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_to_num(lastquarter), 8))
def cg_f083_listing_status_and_dates_core15_2nd_v016_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_event_flag(isdelisted), 8))
def cg_f083_listing_status_and_dates_core16_2nd_v017_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_event_count(lastpricedate, 4), 8))
def cg_f083_listing_status_and_dates_core17_2nd_v018_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_event_rate(lastquarter, 8), 8))
def cg_f083_listing_status_and_dates_core18_2nd_v019_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_to_num(lastpricedate) - _to_num(firstpricedate), 8))
def cg_f083_listing_status_and_dates_core19_2nd_v020_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_to_num(lastquarter) - _to_num(firstquarter), 8))
def cg_f083_listing_status_and_dates_core20_2nd_v021_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_to_num(isdelisted), 4))
def cg_f083_listing_status_and_dates_core21_2nd_v022_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_to_num(firstpricedate), 4))
def cg_f083_listing_status_and_dates_core22_2nd_v023_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_to_num(lastpricedate), 4))
def cg_f083_listing_status_and_dates_core23_2nd_v024_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_to_num(firstquarter), 4))
def cg_f083_listing_status_and_dates_core24_2nd_v025_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_to_num(lastquarter), 4))
def cg_f083_listing_status_and_dates_core25_2nd_v026_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_event_flag(isdelisted), 4))
def cg_f083_listing_status_and_dates_core26_2nd_v027_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_event_count(lastpricedate, 4), 4))
def cg_f083_listing_status_and_dates_core27_2nd_v028_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_event_rate(lastquarter, 8), 4))
def cg_f083_listing_status_and_dates_core28_2nd_v029_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_to_num(lastpricedate) - _to_num(firstpricedate), 4))
def cg_f083_listing_status_and_dates_core29_2nd_v030_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_to_num(lastquarter) - _to_num(firstquarter), 4))
def cg_f083_listing_status_and_dates_core30_2nd_v031_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_slope(_to_num(isdelisted), 4), 8))
def cg_f083_listing_status_and_dates_core31_2nd_v032_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_slope(_to_num(firstpricedate), 4), 8))
def cg_f083_listing_status_and_dates_core32_2nd_v033_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_slope(_to_num(lastpricedate), 4), 8))
def cg_f083_listing_status_and_dates_core33_2nd_v034_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_slope(_to_num(firstquarter), 4), 8))
def cg_f083_listing_status_and_dates_core34_2nd_v035_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_slope(_to_num(lastquarter), 4), 8))
def cg_f083_listing_status_and_dates_core35_2nd_v036_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_slope(_event_flag(isdelisted), 4), 8))
def cg_f083_listing_status_and_dates_core36_2nd_v037_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_slope(_event_count(lastpricedate, 4), 4), 8))
def cg_f083_listing_status_and_dates_core37_2nd_v038_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_slope(_event_rate(lastquarter, 8), 4), 8))
def cg_f083_listing_status_and_dates_core38_2nd_v039_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_slope(_to_num(lastpricedate) - _to_num(firstpricedate), 4), 8))
def cg_f083_listing_status_and_dates_core39_2nd_v040_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_slope(_to_num(lastquarter) - _to_num(firstquarter), 4), 8))
def cg_f083_listing_status_and_dates_core40_2nd_v041_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_slope(_to_num(isdelisted), 8), 12))
def cg_f083_listing_status_and_dates_core41_2nd_v042_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_slope(_to_num(firstpricedate), 8), 12))
def cg_f083_listing_status_and_dates_core42_2nd_v043_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_slope(_to_num(lastpricedate), 8), 12))
def cg_f083_listing_status_and_dates_core43_2nd_v044_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_slope(_to_num(firstquarter), 8), 12))
def cg_f083_listing_status_and_dates_core44_2nd_v045_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_slope(_to_num(lastquarter), 8), 12))
def cg_f083_listing_status_and_dates_core45_2nd_v046_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_slope(_event_flag(isdelisted), 8), 12))
def cg_f083_listing_status_and_dates_core46_2nd_v047_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_slope(_event_count(lastpricedate, 4), 8), 12))
def cg_f083_listing_status_and_dates_core47_2nd_v048_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_slope(_event_rate(lastquarter, 8), 8), 12))
def cg_f083_listing_status_and_dates_core48_2nd_v049_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_slope(_to_num(lastpricedate) - _to_num(firstpricedate), 8), 12))
def cg_f083_listing_status_and_dates_core49_2nd_v050_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_slope(_to_num(lastquarter) - _to_num(firstquarter), 8), 12))
def cg_f083_listing_status_and_dates_core50_2nd_v051_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_diff(_to_num(isdelisted), 4), 8))
def cg_f083_listing_status_and_dates_core51_2nd_v052_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_diff(_to_num(firstpricedate), 4), 8))
def cg_f083_listing_status_and_dates_core52_2nd_v053_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_diff(_to_num(lastpricedate), 4), 8))
def cg_f083_listing_status_and_dates_core53_2nd_v054_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_diff(_to_num(firstquarter), 4), 8))
def cg_f083_listing_status_and_dates_core54_2nd_v055_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_diff(_to_num(lastquarter), 4), 8))
def cg_f083_listing_status_and_dates_core55_2nd_v056_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_diff(_event_flag(isdelisted), 4), 8))
def cg_f083_listing_status_and_dates_core56_2nd_v057_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_diff(_event_count(lastpricedate, 4), 4), 8))
def cg_f083_listing_status_and_dates_core57_2nd_v058_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_diff(_event_rate(lastquarter, 8), 4), 8))
def cg_f083_listing_status_and_dates_core58_2nd_v059_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_diff(_to_num(lastpricedate) - _to_num(firstpricedate), 4), 8))
def cg_f083_listing_status_and_dates_core59_2nd_v060_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_diff(_to_num(lastquarter) - _to_num(firstquarter), 4), 8))
def cg_f083_listing_status_and_dates_core60_2nd_v061_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_slope(_to_num(isdelisted), 4), 12))
def cg_f083_listing_status_and_dates_core61_2nd_v062_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_slope(_to_num(firstpricedate), 4), 12))
def cg_f083_listing_status_and_dates_core62_2nd_v063_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_slope(_to_num(lastpricedate), 4), 12))
def cg_f083_listing_status_and_dates_core63_2nd_v064_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_slope(_to_num(firstquarter), 4), 12))
def cg_f083_listing_status_and_dates_core64_2nd_v065_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_slope(_to_num(lastquarter), 4), 12))
def cg_f083_listing_status_and_dates_core65_2nd_v066_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_slope(_event_flag(isdelisted), 4), 12))
def cg_f083_listing_status_and_dates_core66_2nd_v067_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_slope(_event_count(lastpricedate, 4), 4), 12))
def cg_f083_listing_status_and_dates_core67_2nd_v068_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_slope(_event_rate(lastquarter, 8), 4), 12))
def cg_f083_listing_status_and_dates_core68_2nd_v069_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_slope(_to_num(lastpricedate) - _to_num(firstpricedate), 4), 12))
def cg_f083_listing_status_and_dates_core69_2nd_v070_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_slope(_to_num(lastquarter) - _to_num(firstquarter), 4), 12))
def cg_f083_listing_status_and_dates_core70_2nd_v071_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_diff(_to_num(isdelisted), 4), 12))
def cg_f083_listing_status_and_dates_core71_2nd_v072_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_diff(_to_num(firstpricedate), 4), 12))
def cg_f083_listing_status_and_dates_core72_2nd_v073_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_diff(_to_num(lastpricedate), 4), 12))
def cg_f083_listing_status_and_dates_core73_2nd_v074_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_diff(_to_num(firstquarter), 4), 12))
def cg_f083_listing_status_and_dates_core74_2nd_v075_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_diff(_to_num(lastquarter), 4), 12))
def cg_f083_listing_status_and_dates_core75_2nd_v076_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_diff(_event_flag(isdelisted), 4), 12))
def cg_f083_listing_status_and_dates_core76_2nd_v077_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_diff(_event_count(lastpricedate, 4), 4), 12))
def cg_f083_listing_status_and_dates_core77_2nd_v078_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_diff(_event_rate(lastquarter, 8), 4), 12))
def cg_f083_listing_status_and_dates_core78_2nd_v079_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_diff(_to_num(lastpricedate) - _to_num(firstpricedate), 4), 12))
def cg_f083_listing_status_and_dates_core79_2nd_v080_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_diff(_to_num(lastquarter) - _to_num(firstquarter), 4), 12))
def cg_f083_listing_status_and_dates_core80_2nd_v081_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_slope(_to_num(isdelisted), 4), 4))
def cg_f083_listing_status_and_dates_core81_2nd_v082_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_slope(_to_num(firstpricedate), 4), 4))
def cg_f083_listing_status_and_dates_core82_2nd_v083_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_slope(_to_num(lastpricedate), 4), 4))
def cg_f083_listing_status_and_dates_core83_2nd_v084_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_slope(_to_num(firstquarter), 4), 4))
def cg_f083_listing_status_and_dates_core84_2nd_v085_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_slope(_to_num(lastquarter), 4), 4))
def cg_f083_listing_status_and_dates_core85_2nd_v086_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_slope(_event_flag(isdelisted), 4), 4))
def cg_f083_listing_status_and_dates_core86_2nd_v087_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_slope(_event_count(lastpricedate, 4), 4), 4))
def cg_f083_listing_status_and_dates_core87_2nd_v088_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_slope(_event_rate(lastquarter, 8), 4), 4))
def cg_f083_listing_status_and_dates_core88_2nd_v089_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_slope(_to_num(lastpricedate) - _to_num(firstpricedate), 4), 4))
def cg_f083_listing_status_and_dates_core89_2nd_v090_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_slope(_to_num(lastquarter) - _to_num(firstquarter), 4), 4))
def cg_f083_listing_status_and_dates_core90_2nd_v091_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_diff(_to_num(isdelisted), 4), 4))
def cg_f083_listing_status_and_dates_core91_2nd_v092_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_diff(_to_num(firstpricedate), 4), 4))
def cg_f083_listing_status_and_dates_core92_2nd_v093_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_diff(_to_num(lastpricedate), 4), 4))
def cg_f083_listing_status_and_dates_core93_2nd_v094_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_diff(_to_num(firstquarter), 4), 4))
def cg_f083_listing_status_and_dates_core94_2nd_v095_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_diff(_to_num(lastquarter), 4), 4))
def cg_f083_listing_status_and_dates_core95_2nd_v096_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_diff(_event_flag(isdelisted), 4), 4))
def cg_f083_listing_status_and_dates_core96_2nd_v097_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_diff(_event_count(lastpricedate, 4), 4), 4))
def cg_f083_listing_status_and_dates_core97_2nd_v098_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_diff(_event_rate(lastquarter, 8), 4), 4))
def cg_f083_listing_status_and_dates_core98_2nd_v099_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_diff(_to_num(lastpricedate) - _to_num(firstpricedate), 4), 4))
def cg_f083_listing_status_and_dates_core99_2nd_v100_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_diff(_to_num(lastquarter) - _to_num(firstquarter), 4), 4))
def cg_f083_listing_status_and_dates_core100_2nd_v101_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_mean(_to_num(isdelisted), 4), 4))
def cg_f083_listing_status_and_dates_core101_2nd_v102_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_mean(_to_num(firstpricedate), 4), 4))
def cg_f083_listing_status_and_dates_core102_2nd_v103_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_mean(_to_num(lastpricedate), 4), 4))
def cg_f083_listing_status_and_dates_core103_2nd_v104_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_mean(_to_num(firstquarter), 4), 4))
def cg_f083_listing_status_and_dates_core104_2nd_v105_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_mean(_to_num(lastquarter), 4), 4))
def cg_f083_listing_status_and_dates_core105_2nd_v106_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_mean(_event_flag(isdelisted), 4), 4))
def cg_f083_listing_status_and_dates_core106_2nd_v107_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_mean(_event_count(lastpricedate, 4), 4), 4))
def cg_f083_listing_status_and_dates_core107_2nd_v108_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_mean(_event_rate(lastquarter, 8), 4), 4))
def cg_f083_listing_status_and_dates_core108_2nd_v109_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_mean(_to_num(lastpricedate) - _to_num(firstpricedate), 4), 4))
def cg_f083_listing_status_and_dates_core109_2nd_v110_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_mean(_to_num(lastquarter) - _to_num(firstquarter), 4), 4))
def cg_f083_listing_status_and_dates_core110_2nd_v111_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_mean(_to_num(isdelisted), 8), 8))
def cg_f083_listing_status_and_dates_core111_2nd_v112_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_mean(_to_num(firstpricedate), 8), 8))
def cg_f083_listing_status_and_dates_core112_2nd_v113_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_mean(_to_num(lastpricedate), 8), 8))
def cg_f083_listing_status_and_dates_core113_2nd_v114_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_mean(_to_num(firstquarter), 8), 8))
def cg_f083_listing_status_and_dates_core114_2nd_v115_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_mean(_to_num(lastquarter), 8), 8))
def cg_f083_listing_status_and_dates_core115_2nd_v116_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_mean(_event_flag(isdelisted), 8), 8))
def cg_f083_listing_status_and_dates_core116_2nd_v117_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_mean(_event_count(lastpricedate, 4), 8), 8))
def cg_f083_listing_status_and_dates_core117_2nd_v118_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_mean(_event_rate(lastquarter, 8), 8), 8))
def cg_f083_listing_status_and_dates_core118_2nd_v119_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_mean(_to_num(lastpricedate) - _to_num(firstpricedate), 8), 8))
def cg_f083_listing_status_and_dates_core119_2nd_v120_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_mean(_to_num(lastquarter) - _to_num(firstquarter), 8), 8))
def cg_f083_listing_status_and_dates_core120_2nd_v121_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_mean(_to_num(isdelisted), 4), 4))
def cg_f083_listing_status_and_dates_core121_2nd_v122_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_mean(_to_num(firstpricedate), 4), 4))
def cg_f083_listing_status_and_dates_core122_2nd_v123_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_mean(_to_num(lastpricedate), 4), 4))
def cg_f083_listing_status_and_dates_core123_2nd_v124_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_mean(_to_num(firstquarter), 4), 4))
def cg_f083_listing_status_and_dates_core124_2nd_v125_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_mean(_to_num(lastquarter), 4), 4))
def cg_f083_listing_status_and_dates_core125_2nd_v126_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_mean(_event_flag(isdelisted), 4), 4))
def cg_f083_listing_status_and_dates_core126_2nd_v127_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_mean(_event_count(lastpricedate, 4), 4), 4))
def cg_f083_listing_status_and_dates_core127_2nd_v128_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_mean(_event_rate(lastquarter, 8), 4), 4))
def cg_f083_listing_status_and_dates_core128_2nd_v129_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_mean(_to_num(lastpricedate) - _to_num(firstpricedate), 4), 4))
def cg_f083_listing_status_and_dates_core129_2nd_v130_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_mean(_to_num(lastquarter) - _to_num(firstquarter), 4), 4))
def cg_f083_listing_status_and_dates_core130_2nd_v131_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_diff(_mean(_to_num(isdelisted), 4), 4), 8))
def cg_f083_listing_status_and_dates_core131_2nd_v132_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_diff(_mean(_to_num(firstpricedate), 4), 4), 8))
def cg_f083_listing_status_and_dates_core132_2nd_v133_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_diff(_mean(_to_num(lastpricedate), 4), 4), 8))
def cg_f083_listing_status_and_dates_core133_2nd_v134_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_diff(_mean(_to_num(firstquarter), 4), 4), 8))
def cg_f083_listing_status_and_dates_core134_2nd_v135_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_diff(_mean(_to_num(lastquarter), 4), 4), 8))
def cg_f083_listing_status_and_dates_core135_2nd_v136_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_diff(_mean(_event_flag(isdelisted), 4), 4), 8))
def cg_f083_listing_status_and_dates_core136_2nd_v137_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_diff(_mean(_event_count(lastpricedate, 4), 4), 4), 8))
def cg_f083_listing_status_and_dates_core137_2nd_v138_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_diff(_mean(_event_rate(lastquarter, 8), 4), 4), 8))
def cg_f083_listing_status_and_dates_core138_2nd_v139_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_diff(_mean(_to_num(lastpricedate) - _to_num(firstpricedate), 4), 4), 8))
def cg_f083_listing_status_and_dates_core139_2nd_v140_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_diff(_mean(_to_num(lastquarter) - _to_num(firstquarter), 4), 4), 8))
def cg_f083_listing_status_and_dates_core140_2nd_v141_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_slope(_mean(_to_num(isdelisted), 4), 4), 12))
def cg_f083_listing_status_and_dates_core141_2nd_v142_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_slope(_mean(_to_num(firstpricedate), 4), 4), 12))
def cg_f083_listing_status_and_dates_core142_2nd_v143_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_slope(_mean(_to_num(lastpricedate), 4), 4), 12))
def cg_f083_listing_status_and_dates_core143_2nd_v144_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_slope(_mean(_to_num(firstquarter), 4), 4), 12))
def cg_f083_listing_status_and_dates_core144_2nd_v145_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_slope(_mean(_to_num(lastquarter), 4), 4), 12))
def cg_f083_listing_status_and_dates_core145_2nd_v146_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_slope(_mean(_event_flag(isdelisted), 4), 4), 12))
def cg_f083_listing_status_and_dates_core146_2nd_v147_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_slope(_mean(_event_count(lastpricedate, 4), 4), 4), 12))
def cg_f083_listing_status_and_dates_core147_2nd_v148_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_slope(_mean(_event_rate(lastquarter, 8), 4), 4), 12))
def cg_f083_listing_status_and_dates_core148_2nd_v149_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_slope(_mean(_to_num(lastpricedate) - _to_num(firstpricedate), 4), 4), 12))
def cg_f083_listing_status_and_dates_core149_2nd_v150_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_slope(_mean(_to_num(lastquarter) - _to_num(firstquarter), 4), 4), 12))