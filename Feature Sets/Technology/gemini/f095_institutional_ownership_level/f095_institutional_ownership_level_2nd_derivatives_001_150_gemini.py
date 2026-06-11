import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f095_institutional_ownership_level_core00_2nd_v001_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(value, 4))
def cg_f095_institutional_ownership_level_core01_2nd_v002_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(units, 4))
def cg_f095_institutional_ownership_level_core02_2nd_v003_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(price, 4))
def cg_f095_institutional_ownership_level_core03_2nd_v004_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(_safe_div(value, units), 4))
def cg_f095_institutional_ownership_level_core04_2nd_v005_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(units * price, 4))
def cg_f095_institutional_ownership_level_core05_2nd_v006_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(_log(value + 1.0), 4))
def cg_f095_institutional_ownership_level_core06_2nd_v007_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(_log(units + 1.0), 4))
def cg_f095_institutional_ownership_level_core07_2nd_v008_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(_log(price + 1.0), 4))
def cg_f095_institutional_ownership_level_core08_2nd_v009_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(value - (units * price), 4))
def cg_f095_institutional_ownership_level_core09_2nd_v010_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(_safe_div(units, value), 4))
def cg_f095_institutional_ownership_level_core10_2nd_v011_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(value, 8))
def cg_f095_institutional_ownership_level_core11_2nd_v012_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(units, 8))
def cg_f095_institutional_ownership_level_core12_2nd_v013_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(price, 8))
def cg_f095_institutional_ownership_level_core13_2nd_v014_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(_safe_div(value, units), 8))
def cg_f095_institutional_ownership_level_core14_2nd_v015_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(units * price, 8))
def cg_f095_institutional_ownership_level_core15_2nd_v016_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(_log(value + 1.0), 8))
def cg_f095_institutional_ownership_level_core16_2nd_v017_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(_log(units + 1.0), 8))
def cg_f095_institutional_ownership_level_core17_2nd_v018_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(_log(price + 1.0), 8))
def cg_f095_institutional_ownership_level_core18_2nd_v019_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(value - (units * price), 8))
def cg_f095_institutional_ownership_level_core19_2nd_v020_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(_safe_div(units, value), 8))
def cg_f095_institutional_ownership_level_core20_2nd_v021_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_diff(value, 4))
def cg_f095_institutional_ownership_level_core21_2nd_v022_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_diff(units, 4))
def cg_f095_institutional_ownership_level_core22_2nd_v023_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_diff(price, 4))
def cg_f095_institutional_ownership_level_core23_2nd_v024_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_diff(_safe_div(value, units), 4))
def cg_f095_institutional_ownership_level_core24_2nd_v025_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_diff(units * price, 4))
def cg_f095_institutional_ownership_level_core25_2nd_v026_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_diff(_log(value + 1.0), 4))
def cg_f095_institutional_ownership_level_core26_2nd_v027_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_diff(_log(units + 1.0), 4))
def cg_f095_institutional_ownership_level_core27_2nd_v028_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_diff(_log(price + 1.0), 4))
def cg_f095_institutional_ownership_level_core28_2nd_v029_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_diff(value - (units * price), 4))
def cg_f095_institutional_ownership_level_core29_2nd_v030_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_diff(_safe_div(units, value), 4))
def cg_f095_institutional_ownership_level_core30_2nd_v031_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_slope(value, 4), 8))
def cg_f095_institutional_ownership_level_core31_2nd_v032_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_slope(units, 4), 8))
def cg_f095_institutional_ownership_level_core32_2nd_v033_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_slope(price, 4), 8))
def cg_f095_institutional_ownership_level_core33_2nd_v034_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_slope(_safe_div(value, units), 4), 8))
def cg_f095_institutional_ownership_level_core34_2nd_v035_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_slope(units * price, 4), 8))
def cg_f095_institutional_ownership_level_core35_2nd_v036_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_slope(_log(value + 1.0), 4), 8))
def cg_f095_institutional_ownership_level_core36_2nd_v037_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_slope(_log(units + 1.0), 4), 8))
def cg_f095_institutional_ownership_level_core37_2nd_v038_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_slope(_log(price + 1.0), 4), 8))
def cg_f095_institutional_ownership_level_core38_2nd_v039_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_slope(value - (units * price), 4), 8))
def cg_f095_institutional_ownership_level_core39_2nd_v040_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_slope(_safe_div(units, value), 4), 8))
def cg_f095_institutional_ownership_level_core40_2nd_v041_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_slope(value, 8), 12))
def cg_f095_institutional_ownership_level_core41_2nd_v042_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_slope(units, 8), 12))
def cg_f095_institutional_ownership_level_core42_2nd_v043_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_slope(price, 8), 12))
def cg_f095_institutional_ownership_level_core43_2nd_v044_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_slope(_safe_div(value, units), 8), 12))
def cg_f095_institutional_ownership_level_core44_2nd_v045_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_slope(units * price, 8), 12))
def cg_f095_institutional_ownership_level_core45_2nd_v046_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_slope(_log(value + 1.0), 8), 12))
def cg_f095_institutional_ownership_level_core46_2nd_v047_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_slope(_log(units + 1.0), 8), 12))
def cg_f095_institutional_ownership_level_core47_2nd_v048_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_slope(_log(price + 1.0), 8), 12))
def cg_f095_institutional_ownership_level_core48_2nd_v049_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_slope(value - (units * price), 8), 12))
def cg_f095_institutional_ownership_level_core49_2nd_v050_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_slope(_safe_div(units, value), 8), 12))
def cg_f095_institutional_ownership_level_core50_2nd_v051_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_diff(value, 4), 8))
def cg_f095_institutional_ownership_level_core51_2nd_v052_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_diff(units, 4), 8))
def cg_f095_institutional_ownership_level_core52_2nd_v053_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_diff(price, 4), 8))
def cg_f095_institutional_ownership_level_core53_2nd_v054_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_diff(_safe_div(value, units), 4), 8))
def cg_f095_institutional_ownership_level_core54_2nd_v055_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_diff(units * price, 4), 8))
def cg_f095_institutional_ownership_level_core55_2nd_v056_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_diff(_log(value + 1.0), 4), 8))
def cg_f095_institutional_ownership_level_core56_2nd_v057_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_diff(_log(units + 1.0), 4), 8))
def cg_f095_institutional_ownership_level_core57_2nd_v058_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_diff(_log(price + 1.0), 4), 8))
def cg_f095_institutional_ownership_level_core58_2nd_v059_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_diff(value - (units * price), 4), 8))
def cg_f095_institutional_ownership_level_core59_2nd_v060_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_diff(_safe_div(units, value), 4), 8))
def cg_f095_institutional_ownership_level_core60_2nd_v061_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_rank(_slope(value, 4), 12))
def cg_f095_institutional_ownership_level_core61_2nd_v062_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_rank(_slope(units, 4), 12))
def cg_f095_institutional_ownership_level_core62_2nd_v063_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_rank(_slope(price, 4), 12))
def cg_f095_institutional_ownership_level_core63_2nd_v064_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_rank(_slope(_safe_div(value, units), 4), 12))
def cg_f095_institutional_ownership_level_core64_2nd_v065_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_rank(_slope(units * price, 4), 12))
def cg_f095_institutional_ownership_level_core65_2nd_v066_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_rank(_slope(_log(value + 1.0), 4), 12))
def cg_f095_institutional_ownership_level_core66_2nd_v067_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_rank(_slope(_log(units + 1.0), 4), 12))
def cg_f095_institutional_ownership_level_core67_2nd_v068_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_rank(_slope(_log(price + 1.0), 4), 12))
def cg_f095_institutional_ownership_level_core68_2nd_v069_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_rank(_slope(value - (units * price), 4), 12))
def cg_f095_institutional_ownership_level_core69_2nd_v070_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_rank(_slope(_safe_div(units, value), 4), 12))
def cg_f095_institutional_ownership_level_core70_2nd_v071_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_rank(_diff(value, 4), 12))
def cg_f095_institutional_ownership_level_core71_2nd_v072_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_rank(_diff(units, 4), 12))
def cg_f095_institutional_ownership_level_core72_2nd_v073_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_rank(_diff(price, 4), 12))
def cg_f095_institutional_ownership_level_core73_2nd_v074_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_rank(_diff(_safe_div(value, units), 4), 12))
def cg_f095_institutional_ownership_level_core74_2nd_v075_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_rank(_diff(units * price, 4), 12))
def cg_f095_institutional_ownership_level_core75_2nd_v076_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_rank(_diff(_log(value + 1.0), 4), 12))
def cg_f095_institutional_ownership_level_core76_2nd_v077_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_rank(_diff(_log(units + 1.0), 4), 12))
def cg_f095_institutional_ownership_level_core77_2nd_v078_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_rank(_diff(_log(price + 1.0), 4), 12))
def cg_f095_institutional_ownership_level_core78_2nd_v079_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_rank(_diff(value - (units * price), 4), 12))
def cg_f095_institutional_ownership_level_core79_2nd_v080_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_rank(_diff(_safe_div(units, value), 4), 12))
def cg_f095_institutional_ownership_level_core80_2nd_v081_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_mean(_slope(value, 4), 4))
def cg_f095_institutional_ownership_level_core81_2nd_v082_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_mean(_slope(units, 4), 4))
def cg_f095_institutional_ownership_level_core82_2nd_v083_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_mean(_slope(price, 4), 4))
def cg_f095_institutional_ownership_level_core83_2nd_v084_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_mean(_slope(_safe_div(value, units), 4), 4))
def cg_f095_institutional_ownership_level_core84_2nd_v085_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_mean(_slope(units * price, 4), 4))
def cg_f095_institutional_ownership_level_core85_2nd_v086_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_mean(_slope(_log(value + 1.0), 4), 4))
def cg_f095_institutional_ownership_level_core86_2nd_v087_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_mean(_slope(_log(units + 1.0), 4), 4))
def cg_f095_institutional_ownership_level_core87_2nd_v088_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_mean(_slope(_log(price + 1.0), 4), 4))
def cg_f095_institutional_ownership_level_core88_2nd_v089_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_mean(_slope(value - (units * price), 4), 4))
def cg_f095_institutional_ownership_level_core89_2nd_v090_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_mean(_slope(_safe_div(units, value), 4), 4))
def cg_f095_institutional_ownership_level_core90_2nd_v091_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_mean(_diff(value, 4), 4))
def cg_f095_institutional_ownership_level_core91_2nd_v092_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_mean(_diff(units, 4), 4))
def cg_f095_institutional_ownership_level_core92_2nd_v093_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_mean(_diff(price, 4), 4))
def cg_f095_institutional_ownership_level_core93_2nd_v094_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_mean(_diff(_safe_div(value, units), 4), 4))
def cg_f095_institutional_ownership_level_core94_2nd_v095_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_mean(_diff(units * price, 4), 4))
def cg_f095_institutional_ownership_level_core95_2nd_v096_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_mean(_diff(_log(value + 1.0), 4), 4))
def cg_f095_institutional_ownership_level_core96_2nd_v097_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_mean(_diff(_log(units + 1.0), 4), 4))
def cg_f095_institutional_ownership_level_core97_2nd_v098_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_mean(_diff(_log(price + 1.0), 4), 4))
def cg_f095_institutional_ownership_level_core98_2nd_v099_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_mean(_diff(value - (units * price), 4), 4))
def cg_f095_institutional_ownership_level_core99_2nd_v100_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_mean(_diff(_safe_div(units, value), 4), 4))
def cg_f095_institutional_ownership_level_core100_2nd_v101_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(_mean(value, 4), 4))
def cg_f095_institutional_ownership_level_core101_2nd_v102_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(_mean(units, 4), 4))
def cg_f095_institutional_ownership_level_core102_2nd_v103_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(_mean(price, 4), 4))
def cg_f095_institutional_ownership_level_core103_2nd_v104_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(_mean(_safe_div(value, units), 4), 4))
def cg_f095_institutional_ownership_level_core104_2nd_v105_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(_mean(units * price, 4), 4))
def cg_f095_institutional_ownership_level_core105_2nd_v106_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(_mean(_log(value + 1.0), 4), 4))
def cg_f095_institutional_ownership_level_core106_2nd_v107_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(_mean(_log(units + 1.0), 4), 4))
def cg_f095_institutional_ownership_level_core107_2nd_v108_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(_mean(_log(price + 1.0), 4), 4))
def cg_f095_institutional_ownership_level_core108_2nd_v109_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(_mean(value - (units * price), 4), 4))
def cg_f095_institutional_ownership_level_core109_2nd_v110_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(_mean(_safe_div(units, value), 4), 4))
def cg_f095_institutional_ownership_level_core110_2nd_v111_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(_mean(value, 8), 8))
def cg_f095_institutional_ownership_level_core111_2nd_v112_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(_mean(units, 8), 8))
def cg_f095_institutional_ownership_level_core112_2nd_v113_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(_mean(price, 8), 8))
def cg_f095_institutional_ownership_level_core113_2nd_v114_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(_mean(_safe_div(value, units), 8), 8))
def cg_f095_institutional_ownership_level_core114_2nd_v115_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(_mean(units * price, 8), 8))
def cg_f095_institutional_ownership_level_core115_2nd_v116_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(_mean(_log(value + 1.0), 8), 8))
def cg_f095_institutional_ownership_level_core116_2nd_v117_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(_mean(_log(units + 1.0), 8), 8))
def cg_f095_institutional_ownership_level_core117_2nd_v118_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(_mean(_log(price + 1.0), 8), 8))
def cg_f095_institutional_ownership_level_core118_2nd_v119_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(_mean(value - (units * price), 8), 8))
def cg_f095_institutional_ownership_level_core119_2nd_v120_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_slope(_mean(_safe_div(units, value), 8), 8))
def cg_f095_institutional_ownership_level_core120_2nd_v121_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_diff(_mean(value, 4), 4))
def cg_f095_institutional_ownership_level_core121_2nd_v122_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_diff(_mean(units, 4), 4))
def cg_f095_institutional_ownership_level_core122_2nd_v123_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_diff(_mean(price, 4), 4))
def cg_f095_institutional_ownership_level_core123_2nd_v124_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_diff(_mean(_safe_div(value, units), 4), 4))
def cg_f095_institutional_ownership_level_core124_2nd_v125_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_diff(_mean(units * price, 4), 4))
def cg_f095_institutional_ownership_level_core125_2nd_v126_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_diff(_mean(_log(value + 1.0), 4), 4))
def cg_f095_institutional_ownership_level_core126_2nd_v127_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_diff(_mean(_log(units + 1.0), 4), 4))
def cg_f095_institutional_ownership_level_core127_2nd_v128_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_diff(_mean(_log(price + 1.0), 4), 4))
def cg_f095_institutional_ownership_level_core128_2nd_v129_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_diff(_mean(value - (units * price), 4), 4))
def cg_f095_institutional_ownership_level_core129_2nd_v130_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_diff(_mean(_safe_div(units, value), 4), 4))
def cg_f095_institutional_ownership_level_core130_2nd_v131_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_diff(_mean(value, 4), 4), 8))
def cg_f095_institutional_ownership_level_core131_2nd_v132_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_diff(_mean(units, 4), 4), 8))
def cg_f095_institutional_ownership_level_core132_2nd_v133_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_diff(_mean(price, 4), 4), 8))
def cg_f095_institutional_ownership_level_core133_2nd_v134_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_diff(_mean(_safe_div(value, units), 4), 4), 8))
def cg_f095_institutional_ownership_level_core134_2nd_v135_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_diff(_mean(units * price, 4), 4), 8))
def cg_f095_institutional_ownership_level_core135_2nd_v136_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_diff(_mean(_log(value + 1.0), 4), 4), 8))
def cg_f095_institutional_ownership_level_core136_2nd_v137_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_diff(_mean(_log(units + 1.0), 4), 4), 8))
def cg_f095_institutional_ownership_level_core137_2nd_v138_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_diff(_mean(_log(price + 1.0), 4), 4), 8))
def cg_f095_institutional_ownership_level_core138_2nd_v139_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_diff(_mean(value - (units * price), 4), 4), 8))
def cg_f095_institutional_ownership_level_core139_2nd_v140_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_z(_diff(_mean(_safe_div(units, value), 4), 4), 8))
def cg_f095_institutional_ownership_level_core140_2nd_v141_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_rank(_slope(_mean(value, 4), 4), 12))
def cg_f095_institutional_ownership_level_core141_2nd_v142_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_rank(_slope(_mean(units, 4), 4), 12))
def cg_f095_institutional_ownership_level_core142_2nd_v143_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_rank(_slope(_mean(price, 4), 4), 12))
def cg_f095_institutional_ownership_level_core143_2nd_v144_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_rank(_slope(_mean(_safe_div(value, units), 4), 4), 12))
def cg_f095_institutional_ownership_level_core144_2nd_v145_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_rank(_slope(_mean(units * price, 4), 4), 12))
def cg_f095_institutional_ownership_level_core145_2nd_v146_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_rank(_slope(_mean(_log(value + 1.0), 4), 4), 12))
def cg_f095_institutional_ownership_level_core146_2nd_v147_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_rank(_slope(_mean(_log(units + 1.0), 4), 4), 12))
def cg_f095_institutional_ownership_level_core147_2nd_v148_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_rank(_slope(_mean(_log(price + 1.0), 4), 4), 12))
def cg_f095_institutional_ownership_level_core148_2nd_v149_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_rank(_slope(_mean(value - (units * price), 4), 4), 12))
def cg_f095_institutional_ownership_level_core149_2nd_v150_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_rank(_slope(_mean(_safe_div(units, value), 4), 4), 12))