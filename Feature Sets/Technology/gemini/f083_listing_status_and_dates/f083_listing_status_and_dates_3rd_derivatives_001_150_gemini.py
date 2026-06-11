import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f083_listing_status_and_dates_core00_3rd_v001_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_diff(_to_num(isdelisted), 4), 4))
def cg_f083_listing_status_and_dates_core01_3rd_v002_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_diff(_to_num(firstpricedate), 4), 4))
def cg_f083_listing_status_and_dates_core02_3rd_v003_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_diff(_to_num(lastpricedate), 4), 4))
def cg_f083_listing_status_and_dates_core03_3rd_v004_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_diff(_to_num(firstquarter), 4), 4))
def cg_f083_listing_status_and_dates_core04_3rd_v005_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_diff(_to_num(lastquarter), 4), 4))
def cg_f083_listing_status_and_dates_core05_3rd_v006_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_diff(_event_flag(isdelisted), 4), 4))
def cg_f083_listing_status_and_dates_core06_3rd_v007_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_diff(_event_count(lastpricedate, 4), 4), 4))
def cg_f083_listing_status_and_dates_core07_3rd_v008_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_diff(_event_rate(lastquarter, 8), 4), 4))
def cg_f083_listing_status_and_dates_core08_3rd_v009_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_diff(_to_num(lastpricedate) - _to_num(firstpricedate), 4), 4))
def cg_f083_listing_status_and_dates_core09_3rd_v010_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_diff(_to_num(lastquarter) - _to_num(firstquarter), 4), 4))
def cg_f083_listing_status_and_dates_core10_3rd_v011_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_diff(_to_num(isdelisted), 4), 8))
def cg_f083_listing_status_and_dates_core11_3rd_v012_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_diff(_to_num(firstpricedate), 4), 8))
def cg_f083_listing_status_and_dates_core12_3rd_v013_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_diff(_to_num(lastpricedate), 4), 8))
def cg_f083_listing_status_and_dates_core13_3rd_v014_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_diff(_to_num(firstquarter), 4), 8))
def cg_f083_listing_status_and_dates_core14_3rd_v015_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_diff(_to_num(lastquarter), 4), 8))
def cg_f083_listing_status_and_dates_core15_3rd_v016_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_diff(_event_flag(isdelisted), 4), 8))
def cg_f083_listing_status_and_dates_core16_3rd_v017_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_diff(_event_count(lastpricedate, 4), 4), 8))
def cg_f083_listing_status_and_dates_core17_3rd_v018_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_diff(_event_rate(lastquarter, 8), 4), 8))
def cg_f083_listing_status_and_dates_core18_3rd_v019_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_diff(_to_num(lastpricedate) - _to_num(firstpricedate), 4), 8))
def cg_f083_listing_status_and_dates_core19_3rd_v020_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_diff(_to_num(lastquarter) - _to_num(firstquarter), 4), 8))
def cg_f083_listing_status_and_dates_core20_3rd_v021_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_slope(_to_num(isdelisted), 4), 4))
def cg_f083_listing_status_and_dates_core21_3rd_v022_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_slope(_to_num(firstpricedate), 4), 4))
def cg_f083_listing_status_and_dates_core22_3rd_v023_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_slope(_to_num(lastpricedate), 4), 4))
def cg_f083_listing_status_and_dates_core23_3rd_v024_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_slope(_to_num(firstquarter), 4), 4))
def cg_f083_listing_status_and_dates_core24_3rd_v025_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_slope(_to_num(lastquarter), 4), 4))
def cg_f083_listing_status_and_dates_core25_3rd_v026_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_slope(_event_flag(isdelisted), 4), 4))
def cg_f083_listing_status_and_dates_core26_3rd_v027_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_slope(_event_count(lastpricedate, 4), 4), 4))
def cg_f083_listing_status_and_dates_core27_3rd_v028_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_slope(_event_rate(lastquarter, 8), 4), 4))
def cg_f083_listing_status_and_dates_core28_3rd_v029_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_slope(_to_num(lastpricedate) - _to_num(firstpricedate), 4), 4))
def cg_f083_listing_status_and_dates_core29_3rd_v030_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_slope(_to_num(lastquarter) - _to_num(firstquarter), 4), 4))
def cg_f083_listing_status_and_dates_core30_3rd_v031_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_diff(_diff(_to_num(isdelisted), 4), 4), 8))
def cg_f083_listing_status_and_dates_core31_3rd_v032_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_diff(_diff(_to_num(firstpricedate), 4), 4), 8))
def cg_f083_listing_status_and_dates_core32_3rd_v033_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_diff(_diff(_to_num(lastpricedate), 4), 4), 8))
def cg_f083_listing_status_and_dates_core33_3rd_v034_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_diff(_diff(_to_num(firstquarter), 4), 4), 8))
def cg_f083_listing_status_and_dates_core34_3rd_v035_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_diff(_diff(_to_num(lastquarter), 4), 4), 8))
def cg_f083_listing_status_and_dates_core35_3rd_v036_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_diff(_diff(_event_flag(isdelisted), 4), 4), 8))
def cg_f083_listing_status_and_dates_core36_3rd_v037_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_diff(_diff(_event_count(lastpricedate, 4), 4), 4), 8))
def cg_f083_listing_status_and_dates_core37_3rd_v038_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_diff(_diff(_event_rate(lastquarter, 8), 4), 4), 8))
def cg_f083_listing_status_and_dates_core38_3rd_v039_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_diff(_diff(_to_num(lastpricedate) - _to_num(firstpricedate), 4), 4), 8))
def cg_f083_listing_status_and_dates_core39_3rd_v040_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_diff(_diff(_to_num(lastquarter) - _to_num(firstquarter), 4), 4), 8))
def cg_f083_listing_status_and_dates_core40_3rd_v041_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_slope(_diff(_to_num(isdelisted), 4), 8), 12))
def cg_f083_listing_status_and_dates_core41_3rd_v042_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_slope(_diff(_to_num(firstpricedate), 4), 8), 12))
def cg_f083_listing_status_and_dates_core42_3rd_v043_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_slope(_diff(_to_num(lastpricedate), 4), 8), 12))
def cg_f083_listing_status_and_dates_core43_3rd_v044_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_slope(_diff(_to_num(firstquarter), 4), 8), 12))
def cg_f083_listing_status_and_dates_core44_3rd_v045_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_slope(_diff(_to_num(lastquarter), 4), 8), 12))
def cg_f083_listing_status_and_dates_core45_3rd_v046_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_slope(_diff(_event_flag(isdelisted), 4), 8), 12))
def cg_f083_listing_status_and_dates_core46_3rd_v047_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_slope(_diff(_event_count(lastpricedate, 4), 4), 8), 12))
def cg_f083_listing_status_and_dates_core47_3rd_v048_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_slope(_diff(_event_rate(lastquarter, 8), 4), 8), 12))
def cg_f083_listing_status_and_dates_core48_3rd_v049_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_slope(_diff(_to_num(lastpricedate) - _to_num(firstpricedate), 4), 8), 12))
def cg_f083_listing_status_and_dates_core49_3rd_v050_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_slope(_diff(_to_num(lastquarter) - _to_num(firstquarter), 4), 8), 12))
def cg_f083_listing_status_and_dates_core50_3rd_v051_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_diff(_slope(_to_num(isdelisted), 4), 4), 8))
def cg_f083_listing_status_and_dates_core51_3rd_v052_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_diff(_slope(_to_num(firstpricedate), 4), 4), 8))
def cg_f083_listing_status_and_dates_core52_3rd_v053_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_diff(_slope(_to_num(lastpricedate), 4), 4), 8))
def cg_f083_listing_status_and_dates_core53_3rd_v054_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_diff(_slope(_to_num(firstquarter), 4), 4), 8))
def cg_f083_listing_status_and_dates_core54_3rd_v055_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_diff(_slope(_to_num(lastquarter), 4), 4), 8))
def cg_f083_listing_status_and_dates_core55_3rd_v056_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_diff(_slope(_event_flag(isdelisted), 4), 4), 8))
def cg_f083_listing_status_and_dates_core56_3rd_v057_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_diff(_slope(_event_count(lastpricedate, 4), 4), 4), 8))
def cg_f083_listing_status_and_dates_core57_3rd_v058_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_diff(_slope(_event_rate(lastquarter, 8), 4), 4), 8))
def cg_f083_listing_status_and_dates_core58_3rd_v059_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_diff(_slope(_to_num(lastpricedate) - _to_num(firstpricedate), 4), 4), 8))
def cg_f083_listing_status_and_dates_core59_3rd_v060_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_diff(_slope(_to_num(lastquarter) - _to_num(firstquarter), 4), 4), 8))
def cg_f083_listing_status_and_dates_core60_3rd_v061_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_diff(_diff(_to_num(isdelisted), 4), 4), 12))
def cg_f083_listing_status_and_dates_core61_3rd_v062_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_diff(_diff(_to_num(firstpricedate), 4), 4), 12))
def cg_f083_listing_status_and_dates_core62_3rd_v063_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_diff(_diff(_to_num(lastpricedate), 4), 4), 12))
def cg_f083_listing_status_and_dates_core63_3rd_v064_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_diff(_diff(_to_num(firstquarter), 4), 4), 12))
def cg_f083_listing_status_and_dates_core64_3rd_v065_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_diff(_diff(_to_num(lastquarter), 4), 4), 12))
def cg_f083_listing_status_and_dates_core65_3rd_v066_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_diff(_diff(_event_flag(isdelisted), 4), 4), 12))
def cg_f083_listing_status_and_dates_core66_3rd_v067_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_diff(_diff(_event_count(lastpricedate, 4), 4), 4), 12))
def cg_f083_listing_status_and_dates_core67_3rd_v068_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_diff(_diff(_event_rate(lastquarter, 8), 4), 4), 12))
def cg_f083_listing_status_and_dates_core68_3rd_v069_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_diff(_diff(_to_num(lastpricedate) - _to_num(firstpricedate), 4), 4), 12))
def cg_f083_listing_status_and_dates_core69_3rd_v070_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_diff(_diff(_to_num(lastquarter) - _to_num(firstquarter), 4), 4), 12))
def cg_f083_listing_status_and_dates_core70_3rd_v071_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_slope(_diff(_to_num(isdelisted), 4), 8), 12))
def cg_f083_listing_status_and_dates_core71_3rd_v072_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_slope(_diff(_to_num(firstpricedate), 4), 8), 12))
def cg_f083_listing_status_and_dates_core72_3rd_v073_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_slope(_diff(_to_num(lastpricedate), 4), 8), 12))
def cg_f083_listing_status_and_dates_core73_3rd_v074_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_slope(_diff(_to_num(firstquarter), 4), 8), 12))
def cg_f083_listing_status_and_dates_core74_3rd_v075_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_slope(_diff(_to_num(lastquarter), 4), 8), 12))
def cg_f083_listing_status_and_dates_core75_3rd_v076_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_slope(_diff(_event_flag(isdelisted), 4), 8), 12))
def cg_f083_listing_status_and_dates_core76_3rd_v077_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_slope(_diff(_event_count(lastpricedate, 4), 4), 8), 12))
def cg_f083_listing_status_and_dates_core77_3rd_v078_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_slope(_diff(_event_rate(lastquarter, 8), 4), 8), 12))
def cg_f083_listing_status_and_dates_core78_3rd_v079_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_slope(_diff(_to_num(lastpricedate) - _to_num(firstpricedate), 4), 8), 12))
def cg_f083_listing_status_and_dates_core79_3rd_v080_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_slope(_diff(_to_num(lastquarter) - _to_num(firstquarter), 4), 8), 12))
def cg_f083_listing_status_and_dates_core80_3rd_v081_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_diff(_slope(_to_num(isdelisted), 4), 4), 12))
def cg_f083_listing_status_and_dates_core81_3rd_v082_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_diff(_slope(_to_num(firstpricedate), 4), 4), 12))
def cg_f083_listing_status_and_dates_core82_3rd_v083_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_diff(_slope(_to_num(lastpricedate), 4), 4), 12))
def cg_f083_listing_status_and_dates_core83_3rd_v084_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_diff(_slope(_to_num(firstquarter), 4), 4), 12))
def cg_f083_listing_status_and_dates_core84_3rd_v085_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_diff(_slope(_to_num(lastquarter), 4), 4), 12))
def cg_f083_listing_status_and_dates_core85_3rd_v086_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_diff(_slope(_event_flag(isdelisted), 4), 4), 12))
def cg_f083_listing_status_and_dates_core86_3rd_v087_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_diff(_slope(_event_count(lastpricedate, 4), 4), 4), 12))
def cg_f083_listing_status_and_dates_core87_3rd_v088_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_diff(_slope(_event_rate(lastquarter, 8), 4), 4), 12))
def cg_f083_listing_status_and_dates_core88_3rd_v089_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_diff(_slope(_to_num(lastpricedate) - _to_num(firstpricedate), 4), 4), 12))
def cg_f083_listing_status_and_dates_core89_3rd_v090_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_diff(_slope(_to_num(lastquarter) - _to_num(firstquarter), 4), 4), 12))
def cg_f083_listing_status_and_dates_core90_3rd_v091_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_diff(_diff(_to_num(isdelisted), 4), 4), 4))
def cg_f083_listing_status_and_dates_core91_3rd_v092_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_diff(_diff(_to_num(firstpricedate), 4), 4), 4))
def cg_f083_listing_status_and_dates_core92_3rd_v093_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_diff(_diff(_to_num(lastpricedate), 4), 4), 4))
def cg_f083_listing_status_and_dates_core93_3rd_v094_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_diff(_diff(_to_num(firstquarter), 4), 4), 4))
def cg_f083_listing_status_and_dates_core94_3rd_v095_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_diff(_diff(_to_num(lastquarter), 4), 4), 4))
def cg_f083_listing_status_and_dates_core95_3rd_v096_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_diff(_diff(_event_flag(isdelisted), 4), 4), 4))
def cg_f083_listing_status_and_dates_core96_3rd_v097_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_diff(_diff(_event_count(lastpricedate, 4), 4), 4), 4))
def cg_f083_listing_status_and_dates_core97_3rd_v098_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_diff(_diff(_event_rate(lastquarter, 8), 4), 4), 4))
def cg_f083_listing_status_and_dates_core98_3rd_v099_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_diff(_diff(_to_num(lastpricedate) - _to_num(firstpricedate), 4), 4), 4))
def cg_f083_listing_status_and_dates_core99_3rd_v100_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_diff(_diff(_to_num(lastquarter) - _to_num(firstquarter), 4), 4), 4))
def cg_f083_listing_status_and_dates_core100_3rd_v101_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_slope(_diff(_to_num(isdelisted), 4), 8), 4))
def cg_f083_listing_status_and_dates_core101_3rd_v102_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_slope(_diff(_to_num(firstpricedate), 4), 8), 4))
def cg_f083_listing_status_and_dates_core102_3rd_v103_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_slope(_diff(_to_num(lastpricedate), 4), 8), 4))
def cg_f083_listing_status_and_dates_core103_3rd_v104_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_slope(_diff(_to_num(firstquarter), 4), 8), 4))
def cg_f083_listing_status_and_dates_core104_3rd_v105_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_slope(_diff(_to_num(lastquarter), 4), 8), 4))
def cg_f083_listing_status_and_dates_core105_3rd_v106_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_slope(_diff(_event_flag(isdelisted), 4), 8), 4))
def cg_f083_listing_status_and_dates_core106_3rd_v107_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_slope(_diff(_event_count(lastpricedate, 4), 4), 8), 4))
def cg_f083_listing_status_and_dates_core107_3rd_v108_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_slope(_diff(_event_rate(lastquarter, 8), 4), 8), 4))
def cg_f083_listing_status_and_dates_core108_3rd_v109_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_slope(_diff(_to_num(lastpricedate) - _to_num(firstpricedate), 4), 8), 4))
def cg_f083_listing_status_and_dates_core109_3rd_v110_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_slope(_diff(_to_num(lastquarter) - _to_num(firstquarter), 4), 8), 4))
def cg_f083_listing_status_and_dates_core110_3rd_v111_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_diff(_slope(_to_num(isdelisted), 4), 4), 4))
def cg_f083_listing_status_and_dates_core111_3rd_v112_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_diff(_slope(_to_num(firstpricedate), 4), 4), 4))
def cg_f083_listing_status_and_dates_core112_3rd_v113_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_diff(_slope(_to_num(lastpricedate), 4), 4), 4))
def cg_f083_listing_status_and_dates_core113_3rd_v114_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_diff(_slope(_to_num(firstquarter), 4), 4), 4))
def cg_f083_listing_status_and_dates_core114_3rd_v115_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_diff(_slope(_to_num(lastquarter), 4), 4), 4))
def cg_f083_listing_status_and_dates_core115_3rd_v116_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_diff(_slope(_event_flag(isdelisted), 4), 4), 4))
def cg_f083_listing_status_and_dates_core116_3rd_v117_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_diff(_slope(_event_count(lastpricedate, 4), 4), 4), 4))
def cg_f083_listing_status_and_dates_core117_3rd_v118_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_diff(_slope(_event_rate(lastquarter, 8), 4), 4), 4))
def cg_f083_listing_status_and_dates_core118_3rd_v119_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_diff(_slope(_to_num(lastpricedate) - _to_num(firstpricedate), 4), 4), 4))
def cg_f083_listing_status_and_dates_core119_3rd_v120_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_mean(_diff(_slope(_to_num(lastquarter) - _to_num(firstquarter), 4), 4), 4))
def cg_f083_listing_status_and_dates_core120_3rd_v121_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_diff(_diff(_to_num(isdelisted), 4), 4), 4))
def cg_f083_listing_status_and_dates_core121_3rd_v122_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_diff(_diff(_to_num(firstpricedate), 4), 4), 4))
def cg_f083_listing_status_and_dates_core122_3rd_v123_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_diff(_diff(_to_num(lastpricedate), 4), 4), 4))
def cg_f083_listing_status_and_dates_core123_3rd_v124_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_diff(_diff(_to_num(firstquarter), 4), 4), 4))
def cg_f083_listing_status_and_dates_core124_3rd_v125_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_diff(_diff(_to_num(lastquarter), 4), 4), 4))
def cg_f083_listing_status_and_dates_core125_3rd_v126_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_diff(_diff(_event_flag(isdelisted), 4), 4), 4))
def cg_f083_listing_status_and_dates_core126_3rd_v127_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_diff(_diff(_event_count(lastpricedate, 4), 4), 4), 4))
def cg_f083_listing_status_and_dates_core127_3rd_v128_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_diff(_diff(_event_rate(lastquarter, 8), 4), 4), 4))
def cg_f083_listing_status_and_dates_core128_3rd_v129_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_diff(_diff(_to_num(lastpricedate) - _to_num(firstpricedate), 4), 4), 4))
def cg_f083_listing_status_and_dates_core129_3rd_v130_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_slope(_diff(_diff(_to_num(lastquarter) - _to_num(firstquarter), 4), 4), 4))
def cg_f083_listing_status_and_dates_core130_3rd_v131_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_diff(_diff(_to_num(isdelisted), 4), 4), 4))
def cg_f083_listing_status_and_dates_core131_3rd_v132_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_diff(_diff(_to_num(firstpricedate), 4), 4), 4))
def cg_f083_listing_status_and_dates_core132_3rd_v133_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_diff(_diff(_to_num(lastpricedate), 4), 4), 4))
def cg_f083_listing_status_and_dates_core133_3rd_v134_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_diff(_diff(_to_num(firstquarter), 4), 4), 4))
def cg_f083_listing_status_and_dates_core134_3rd_v135_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_diff(_diff(_to_num(lastquarter), 4), 4), 4))
def cg_f083_listing_status_and_dates_core135_3rd_v136_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_diff(_diff(_event_flag(isdelisted), 4), 4), 4))
def cg_f083_listing_status_and_dates_core136_3rd_v137_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_diff(_diff(_event_count(lastpricedate, 4), 4), 4), 4))
def cg_f083_listing_status_and_dates_core137_3rd_v138_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_diff(_diff(_event_rate(lastquarter, 8), 4), 4), 4))
def cg_f083_listing_status_and_dates_core138_3rd_v139_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_diff(_diff(_to_num(lastpricedate) - _to_num(firstpricedate), 4), 4), 4))
def cg_f083_listing_status_and_dates_core139_3rd_v140_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_diff(_diff(_to_num(lastquarter) - _to_num(firstquarter), 4), 4), 4))
def cg_f083_listing_status_and_dates_core140_3rd_v141_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_slope(_diff(_diff(_to_num(isdelisted), 4), 4), 4), 8))
def cg_f083_listing_status_and_dates_core141_3rd_v142_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_slope(_diff(_diff(_to_num(firstpricedate), 4), 4), 4), 8))
def cg_f083_listing_status_and_dates_core142_3rd_v143_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_slope(_diff(_diff(_to_num(lastpricedate), 4), 4), 4), 8))
def cg_f083_listing_status_and_dates_core143_3rd_v144_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_slope(_diff(_diff(_to_num(firstquarter), 4), 4), 4), 8))
def cg_f083_listing_status_and_dates_core144_3rd_v145_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_slope(_diff(_diff(_to_num(lastquarter), 4), 4), 4), 8))
def cg_f083_listing_status_and_dates_core145_3rd_v146_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_slope(_diff(_diff(_event_flag(isdelisted), 4), 4), 4), 8))
def cg_f083_listing_status_and_dates_core146_3rd_v147_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_slope(_diff(_diff(_event_count(lastpricedate, 4), 4), 4), 4), 8))
def cg_f083_listing_status_and_dates_core147_3rd_v148_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_slope(_diff(_diff(_event_rate(lastquarter, 8), 4), 4), 4), 8))
def cg_f083_listing_status_and_dates_core148_3rd_v149_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_slope(_diff(_diff(_to_num(lastpricedate) - _to_num(firstpricedate), 4), 4), 4), 8))
def cg_f083_listing_status_and_dates_core149_3rd_v150_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_z(_slope(_diff(_diff(_to_num(lastquarter) - _to_num(firstquarter), 4), 4), 4), 8))