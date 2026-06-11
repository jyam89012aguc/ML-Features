import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f029_deferred_revenue_book_core00_2nd_v001_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(deferredrev, 4))
def cg_f029_deferred_revenue_book_core01_2nd_v002_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_safe_div(deferredrev, revenue.abs() + 1.0), 4))
def cg_f029_deferred_revenue_book_core02_2nd_v003_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_safe_div(deferredrev, liabilities.abs() + 1.0), 4))
def cg_f029_deferred_revenue_book_core03_2nd_v004_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_safe_div(revenue, liabilities.abs() + 1.0), 4))
def cg_f029_deferred_revenue_book_core04_2nd_v005_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(deferredrev / (revenue.abs() + 1.0), 4))
def cg_f029_deferred_revenue_book_core05_2nd_v006_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_diff(deferredrev, 4), 4))
def cg_f029_deferred_revenue_book_core06_2nd_v007_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_slope(deferredrev, 4), 4))
def cg_f029_deferred_revenue_book_core07_2nd_v008_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_z(deferredrev, 12), 4))
def cg_f029_deferred_revenue_book_core08_2nd_v009_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(deferredrev - revenue, 4))
def cg_f029_deferred_revenue_book_core09_2nd_v010_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_safe_div(deferredrev, revenue + liabilities + 1.0), 4))
def cg_f029_deferred_revenue_book_core10_2nd_v011_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(deferredrev, 8))
def cg_f029_deferred_revenue_book_core11_2nd_v012_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_safe_div(deferredrev, revenue.abs() + 1.0), 8))
def cg_f029_deferred_revenue_book_core12_2nd_v013_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_safe_div(deferredrev, liabilities.abs() + 1.0), 8))
def cg_f029_deferred_revenue_book_core13_2nd_v014_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_safe_div(revenue, liabilities.abs() + 1.0), 8))
def cg_f029_deferred_revenue_book_core14_2nd_v015_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(deferredrev / (revenue.abs() + 1.0), 8))
def cg_f029_deferred_revenue_book_core15_2nd_v016_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_diff(deferredrev, 4), 8))
def cg_f029_deferred_revenue_book_core16_2nd_v017_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_slope(deferredrev, 4), 8))
def cg_f029_deferred_revenue_book_core17_2nd_v018_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_z(deferredrev, 12), 8))
def cg_f029_deferred_revenue_book_core18_2nd_v019_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(deferredrev - revenue, 8))
def cg_f029_deferred_revenue_book_core19_2nd_v020_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_safe_div(deferredrev, revenue + liabilities + 1.0), 8))
def cg_f029_deferred_revenue_book_core20_2nd_v021_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(deferredrev, 4))
def cg_f029_deferred_revenue_book_core21_2nd_v022_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_safe_div(deferredrev, revenue.abs() + 1.0), 4))
def cg_f029_deferred_revenue_book_core22_2nd_v023_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_safe_div(deferredrev, liabilities.abs() + 1.0), 4))
def cg_f029_deferred_revenue_book_core23_2nd_v024_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_safe_div(revenue, liabilities.abs() + 1.0), 4))
def cg_f029_deferred_revenue_book_core24_2nd_v025_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(deferredrev / (revenue.abs() + 1.0), 4))
def cg_f029_deferred_revenue_book_core25_2nd_v026_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_diff(deferredrev, 4), 4))
def cg_f029_deferred_revenue_book_core26_2nd_v027_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_slope(deferredrev, 4), 4))
def cg_f029_deferred_revenue_book_core27_2nd_v028_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_z(deferredrev, 12), 4))
def cg_f029_deferred_revenue_book_core28_2nd_v029_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(deferredrev - revenue, 4))
def cg_f029_deferred_revenue_book_core29_2nd_v030_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_safe_div(deferredrev, revenue + liabilities + 1.0), 4))
def cg_f029_deferred_revenue_book_core30_2nd_v031_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_slope(deferredrev, 4), 8))
def cg_f029_deferred_revenue_book_core31_2nd_v032_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_slope(_safe_div(deferredrev, revenue.abs() + 1.0), 4), 8))
def cg_f029_deferred_revenue_book_core32_2nd_v033_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_slope(_safe_div(deferredrev, liabilities.abs() + 1.0), 4), 8))
def cg_f029_deferred_revenue_book_core33_2nd_v034_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_slope(_safe_div(revenue, liabilities.abs() + 1.0), 4), 8))
def cg_f029_deferred_revenue_book_core34_2nd_v035_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_slope(deferredrev / (revenue.abs() + 1.0), 4), 8))
def cg_f029_deferred_revenue_book_core35_2nd_v036_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_slope(_diff(deferredrev, 4), 4), 8))
def cg_f029_deferred_revenue_book_core36_2nd_v037_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_slope(_slope(deferredrev, 4), 4), 8))
def cg_f029_deferred_revenue_book_core37_2nd_v038_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_slope(_z(deferredrev, 12), 4), 8))
def cg_f029_deferred_revenue_book_core38_2nd_v039_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_slope(deferredrev - revenue, 4), 8))
def cg_f029_deferred_revenue_book_core39_2nd_v040_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_slope(_safe_div(deferredrev, revenue + liabilities + 1.0), 4), 8))
def cg_f029_deferred_revenue_book_core40_2nd_v041_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_slope(deferredrev, 8), 12))
def cg_f029_deferred_revenue_book_core41_2nd_v042_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_slope(_safe_div(deferredrev, revenue.abs() + 1.0), 8), 12))
def cg_f029_deferred_revenue_book_core42_2nd_v043_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_slope(_safe_div(deferredrev, liabilities.abs() + 1.0), 8), 12))
def cg_f029_deferred_revenue_book_core43_2nd_v044_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_slope(_safe_div(revenue, liabilities.abs() + 1.0), 8), 12))
def cg_f029_deferred_revenue_book_core44_2nd_v045_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_slope(deferredrev / (revenue.abs() + 1.0), 8), 12))
def cg_f029_deferred_revenue_book_core45_2nd_v046_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_slope(_diff(deferredrev, 4), 8), 12))
def cg_f029_deferred_revenue_book_core46_2nd_v047_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_slope(_slope(deferredrev, 4), 8), 12))
def cg_f029_deferred_revenue_book_core47_2nd_v048_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_slope(_z(deferredrev, 12), 8), 12))
def cg_f029_deferred_revenue_book_core48_2nd_v049_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_slope(deferredrev - revenue, 8), 12))
def cg_f029_deferred_revenue_book_core49_2nd_v050_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_slope(_safe_div(deferredrev, revenue + liabilities + 1.0), 8), 12))
def cg_f029_deferred_revenue_book_core50_2nd_v051_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_diff(deferredrev, 4), 8))
def cg_f029_deferred_revenue_book_core51_2nd_v052_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_diff(_safe_div(deferredrev, revenue.abs() + 1.0), 4), 8))
def cg_f029_deferred_revenue_book_core52_2nd_v053_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_diff(_safe_div(deferredrev, liabilities.abs() + 1.0), 4), 8))
def cg_f029_deferred_revenue_book_core53_2nd_v054_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_diff(_safe_div(revenue, liabilities.abs() + 1.0), 4), 8))
def cg_f029_deferred_revenue_book_core54_2nd_v055_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_diff(deferredrev / (revenue.abs() + 1.0), 4), 8))
def cg_f029_deferred_revenue_book_core55_2nd_v056_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_diff(_diff(deferredrev, 4), 4), 8))
def cg_f029_deferred_revenue_book_core56_2nd_v057_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_diff(_slope(deferredrev, 4), 4), 8))
def cg_f029_deferred_revenue_book_core57_2nd_v058_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_diff(_z(deferredrev, 12), 4), 8))
def cg_f029_deferred_revenue_book_core58_2nd_v059_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_diff(deferredrev - revenue, 4), 8))
def cg_f029_deferred_revenue_book_core59_2nd_v060_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_diff(_safe_div(deferredrev, revenue + liabilities + 1.0), 4), 8))
def cg_f029_deferred_revenue_book_core60_2nd_v061_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_slope(deferredrev, 4), 12))
def cg_f029_deferred_revenue_book_core61_2nd_v062_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_slope(_safe_div(deferredrev, revenue.abs() + 1.0), 4), 12))
def cg_f029_deferred_revenue_book_core62_2nd_v063_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_slope(_safe_div(deferredrev, liabilities.abs() + 1.0), 4), 12))
def cg_f029_deferred_revenue_book_core63_2nd_v064_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_slope(_safe_div(revenue, liabilities.abs() + 1.0), 4), 12))
def cg_f029_deferred_revenue_book_core64_2nd_v065_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_slope(deferredrev / (revenue.abs() + 1.0), 4), 12))
def cg_f029_deferred_revenue_book_core65_2nd_v066_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_slope(_diff(deferredrev, 4), 4), 12))
def cg_f029_deferred_revenue_book_core66_2nd_v067_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_slope(_slope(deferredrev, 4), 4), 12))
def cg_f029_deferred_revenue_book_core67_2nd_v068_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_slope(_z(deferredrev, 12), 4), 12))
def cg_f029_deferred_revenue_book_core68_2nd_v069_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_slope(deferredrev - revenue, 4), 12))
def cg_f029_deferred_revenue_book_core69_2nd_v070_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_slope(_safe_div(deferredrev, revenue + liabilities + 1.0), 4), 12))
def cg_f029_deferred_revenue_book_core70_2nd_v071_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_diff(deferredrev, 4), 12))
def cg_f029_deferred_revenue_book_core71_2nd_v072_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_diff(_safe_div(deferredrev, revenue.abs() + 1.0), 4), 12))
def cg_f029_deferred_revenue_book_core72_2nd_v073_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_diff(_safe_div(deferredrev, liabilities.abs() + 1.0), 4), 12))
def cg_f029_deferred_revenue_book_core73_2nd_v074_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_diff(_safe_div(revenue, liabilities.abs() + 1.0), 4), 12))
def cg_f029_deferred_revenue_book_core74_2nd_v075_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_diff(deferredrev / (revenue.abs() + 1.0), 4), 12))
def cg_f029_deferred_revenue_book_core75_2nd_v076_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_diff(_diff(deferredrev, 4), 4), 12))
def cg_f029_deferred_revenue_book_core76_2nd_v077_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_diff(_slope(deferredrev, 4), 4), 12))
def cg_f029_deferred_revenue_book_core77_2nd_v078_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_diff(_z(deferredrev, 12), 4), 12))
def cg_f029_deferred_revenue_book_core78_2nd_v079_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_diff(deferredrev - revenue, 4), 12))
def cg_f029_deferred_revenue_book_core79_2nd_v080_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_diff(_safe_div(deferredrev, revenue + liabilities + 1.0), 4), 12))
def cg_f029_deferred_revenue_book_core80_2nd_v081_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_slope(deferredrev, 4), 4))
def cg_f029_deferred_revenue_book_core81_2nd_v082_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_slope(_safe_div(deferredrev, revenue.abs() + 1.0), 4), 4))
def cg_f029_deferred_revenue_book_core82_2nd_v083_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_slope(_safe_div(deferredrev, liabilities.abs() + 1.0), 4), 4))
def cg_f029_deferred_revenue_book_core83_2nd_v084_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_slope(_safe_div(revenue, liabilities.abs() + 1.0), 4), 4))
def cg_f029_deferred_revenue_book_core84_2nd_v085_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_slope(deferredrev / (revenue.abs() + 1.0), 4), 4))
def cg_f029_deferred_revenue_book_core85_2nd_v086_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_slope(_diff(deferredrev, 4), 4), 4))
def cg_f029_deferred_revenue_book_core86_2nd_v087_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_slope(_slope(deferredrev, 4), 4), 4))
def cg_f029_deferred_revenue_book_core87_2nd_v088_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_slope(_z(deferredrev, 12), 4), 4))
def cg_f029_deferred_revenue_book_core88_2nd_v089_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_slope(deferredrev - revenue, 4), 4))
def cg_f029_deferred_revenue_book_core89_2nd_v090_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_slope(_safe_div(deferredrev, revenue + liabilities + 1.0), 4), 4))
def cg_f029_deferred_revenue_book_core90_2nd_v091_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_diff(deferredrev, 4), 4))
def cg_f029_deferred_revenue_book_core91_2nd_v092_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_diff(_safe_div(deferredrev, revenue.abs() + 1.0), 4), 4))
def cg_f029_deferred_revenue_book_core92_2nd_v093_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_diff(_safe_div(deferredrev, liabilities.abs() + 1.0), 4), 4))
def cg_f029_deferred_revenue_book_core93_2nd_v094_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_diff(_safe_div(revenue, liabilities.abs() + 1.0), 4), 4))
def cg_f029_deferred_revenue_book_core94_2nd_v095_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_diff(deferredrev / (revenue.abs() + 1.0), 4), 4))
def cg_f029_deferred_revenue_book_core95_2nd_v096_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_diff(_diff(deferredrev, 4), 4), 4))
def cg_f029_deferred_revenue_book_core96_2nd_v097_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_diff(_slope(deferredrev, 4), 4), 4))
def cg_f029_deferred_revenue_book_core97_2nd_v098_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_diff(_z(deferredrev, 12), 4), 4))
def cg_f029_deferred_revenue_book_core98_2nd_v099_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_diff(deferredrev - revenue, 4), 4))
def cg_f029_deferred_revenue_book_core99_2nd_v100_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_diff(_safe_div(deferredrev, revenue + liabilities + 1.0), 4), 4))
def cg_f029_deferred_revenue_book_core100_2nd_v101_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_mean(deferredrev, 4), 4))
def cg_f029_deferred_revenue_book_core101_2nd_v102_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_mean(_safe_div(deferredrev, revenue.abs() + 1.0), 4), 4))
def cg_f029_deferred_revenue_book_core102_2nd_v103_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_mean(_safe_div(deferredrev, liabilities.abs() + 1.0), 4), 4))
def cg_f029_deferred_revenue_book_core103_2nd_v104_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_mean(_safe_div(revenue, liabilities.abs() + 1.0), 4), 4))
def cg_f029_deferred_revenue_book_core104_2nd_v105_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_mean(deferredrev / (revenue.abs() + 1.0), 4), 4))
def cg_f029_deferred_revenue_book_core105_2nd_v106_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_mean(_diff(deferredrev, 4), 4), 4))
def cg_f029_deferred_revenue_book_core106_2nd_v107_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_mean(_slope(deferredrev, 4), 4), 4))
def cg_f029_deferred_revenue_book_core107_2nd_v108_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_mean(_z(deferredrev, 12), 4), 4))
def cg_f029_deferred_revenue_book_core108_2nd_v109_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_mean(deferredrev - revenue, 4), 4))
def cg_f029_deferred_revenue_book_core109_2nd_v110_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_mean(_safe_div(deferredrev, revenue + liabilities + 1.0), 4), 4))
def cg_f029_deferred_revenue_book_core110_2nd_v111_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_mean(deferredrev, 8), 8))
def cg_f029_deferred_revenue_book_core111_2nd_v112_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_mean(_safe_div(deferredrev, revenue.abs() + 1.0), 8), 8))
def cg_f029_deferred_revenue_book_core112_2nd_v113_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_mean(_safe_div(deferredrev, liabilities.abs() + 1.0), 8), 8))
def cg_f029_deferred_revenue_book_core113_2nd_v114_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_mean(_safe_div(revenue, liabilities.abs() + 1.0), 8), 8))
def cg_f029_deferred_revenue_book_core114_2nd_v115_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_mean(deferredrev / (revenue.abs() + 1.0), 8), 8))
def cg_f029_deferred_revenue_book_core115_2nd_v116_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_mean(_diff(deferredrev, 4), 8), 8))
def cg_f029_deferred_revenue_book_core116_2nd_v117_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_mean(_slope(deferredrev, 4), 8), 8))
def cg_f029_deferred_revenue_book_core117_2nd_v118_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_mean(_z(deferredrev, 12), 8), 8))
def cg_f029_deferred_revenue_book_core118_2nd_v119_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_mean(deferredrev - revenue, 8), 8))
def cg_f029_deferred_revenue_book_core119_2nd_v120_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_mean(_safe_div(deferredrev, revenue + liabilities + 1.0), 8), 8))
def cg_f029_deferred_revenue_book_core120_2nd_v121_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_mean(deferredrev, 4), 4))
def cg_f029_deferred_revenue_book_core121_2nd_v122_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_mean(_safe_div(deferredrev, revenue.abs() + 1.0), 4), 4))
def cg_f029_deferred_revenue_book_core122_2nd_v123_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_mean(_safe_div(deferredrev, liabilities.abs() + 1.0), 4), 4))
def cg_f029_deferred_revenue_book_core123_2nd_v124_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_mean(_safe_div(revenue, liabilities.abs() + 1.0), 4), 4))
def cg_f029_deferred_revenue_book_core124_2nd_v125_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_mean(deferredrev / (revenue.abs() + 1.0), 4), 4))
def cg_f029_deferred_revenue_book_core125_2nd_v126_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_mean(_diff(deferredrev, 4), 4), 4))
def cg_f029_deferred_revenue_book_core126_2nd_v127_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_mean(_slope(deferredrev, 4), 4), 4))
def cg_f029_deferred_revenue_book_core127_2nd_v128_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_mean(_z(deferredrev, 12), 4), 4))
def cg_f029_deferred_revenue_book_core128_2nd_v129_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_mean(deferredrev - revenue, 4), 4))
def cg_f029_deferred_revenue_book_core129_2nd_v130_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_mean(_safe_div(deferredrev, revenue + liabilities + 1.0), 4), 4))
def cg_f029_deferred_revenue_book_core130_2nd_v131_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_diff(_mean(deferredrev, 4), 4), 8))
def cg_f029_deferred_revenue_book_core131_2nd_v132_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_diff(_mean(_safe_div(deferredrev, revenue.abs() + 1.0), 4), 4), 8))
def cg_f029_deferred_revenue_book_core132_2nd_v133_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_diff(_mean(_safe_div(deferredrev, liabilities.abs() + 1.0), 4), 4), 8))
def cg_f029_deferred_revenue_book_core133_2nd_v134_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_diff(_mean(_safe_div(revenue, liabilities.abs() + 1.0), 4), 4), 8))
def cg_f029_deferred_revenue_book_core134_2nd_v135_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_diff(_mean(deferredrev / (revenue.abs() + 1.0), 4), 4), 8))
def cg_f029_deferred_revenue_book_core135_2nd_v136_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_diff(_mean(_diff(deferredrev, 4), 4), 4), 8))
def cg_f029_deferred_revenue_book_core136_2nd_v137_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_diff(_mean(_slope(deferredrev, 4), 4), 4), 8))
def cg_f029_deferred_revenue_book_core137_2nd_v138_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_diff(_mean(_z(deferredrev, 12), 4), 4), 8))
def cg_f029_deferred_revenue_book_core138_2nd_v139_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_diff(_mean(deferredrev - revenue, 4), 4), 8))
def cg_f029_deferred_revenue_book_core139_2nd_v140_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_diff(_mean(_safe_div(deferredrev, revenue + liabilities + 1.0), 4), 4), 8))
def cg_f029_deferred_revenue_book_core140_2nd_v141_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_slope(_mean(deferredrev, 4), 4), 12))
def cg_f029_deferred_revenue_book_core141_2nd_v142_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_slope(_mean(_safe_div(deferredrev, revenue.abs() + 1.0), 4), 4), 12))
def cg_f029_deferred_revenue_book_core142_2nd_v143_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_slope(_mean(_safe_div(deferredrev, liabilities.abs() + 1.0), 4), 4), 12))
def cg_f029_deferred_revenue_book_core143_2nd_v144_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_slope(_mean(_safe_div(revenue, liabilities.abs() + 1.0), 4), 4), 12))
def cg_f029_deferred_revenue_book_core144_2nd_v145_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_slope(_mean(deferredrev / (revenue.abs() + 1.0), 4), 4), 12))
def cg_f029_deferred_revenue_book_core145_2nd_v146_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_slope(_mean(_diff(deferredrev, 4), 4), 4), 12))
def cg_f029_deferred_revenue_book_core146_2nd_v147_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_slope(_mean(_slope(deferredrev, 4), 4), 4), 12))
def cg_f029_deferred_revenue_book_core147_2nd_v148_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_slope(_mean(_z(deferredrev, 12), 4), 4), 12))
def cg_f029_deferred_revenue_book_core148_2nd_v149_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_slope(_mean(deferredrev - revenue, 4), 4), 12))
def cg_f029_deferred_revenue_book_core149_2nd_v150_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_slope(_mean(_safe_div(deferredrev, revenue + liabilities + 1.0), 4), 4), 12))