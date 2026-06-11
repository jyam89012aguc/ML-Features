import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f029_deferred_revenue_book_core00_3rd_v001_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_diff(deferredrev, 4), 4))
def cg_f029_deferred_revenue_book_core01_3rd_v002_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_diff(_safe_div(deferredrev, revenue.abs() + 1.0), 4), 4))
def cg_f029_deferred_revenue_book_core02_3rd_v003_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_diff(_safe_div(deferredrev, liabilities.abs() + 1.0), 4), 4))
def cg_f029_deferred_revenue_book_core03_3rd_v004_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_diff(_safe_div(revenue, liabilities.abs() + 1.0), 4), 4))
def cg_f029_deferred_revenue_book_core04_3rd_v005_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_diff(deferredrev / (revenue.abs() + 1.0), 4), 4))
def cg_f029_deferred_revenue_book_core05_3rd_v006_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_diff(_diff(deferredrev, 4), 4), 4))
def cg_f029_deferred_revenue_book_core06_3rd_v007_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_diff(_slope(deferredrev, 4), 4), 4))
def cg_f029_deferred_revenue_book_core07_3rd_v008_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_diff(_z(deferredrev, 12), 4), 4))
def cg_f029_deferred_revenue_book_core08_3rd_v009_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_diff(deferredrev - revenue, 4), 4))
def cg_f029_deferred_revenue_book_core09_3rd_v010_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_diff(_safe_div(deferredrev, revenue + liabilities + 1.0), 4), 4))
def cg_f029_deferred_revenue_book_core10_3rd_v011_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_diff(deferredrev, 4), 8))
def cg_f029_deferred_revenue_book_core11_3rd_v012_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_diff(_safe_div(deferredrev, revenue.abs() + 1.0), 4), 8))
def cg_f029_deferred_revenue_book_core12_3rd_v013_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_diff(_safe_div(deferredrev, liabilities.abs() + 1.0), 4), 8))
def cg_f029_deferred_revenue_book_core13_3rd_v014_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_diff(_safe_div(revenue, liabilities.abs() + 1.0), 4), 8))
def cg_f029_deferred_revenue_book_core14_3rd_v015_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_diff(deferredrev / (revenue.abs() + 1.0), 4), 8))
def cg_f029_deferred_revenue_book_core15_3rd_v016_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_diff(_diff(deferredrev, 4), 4), 8))
def cg_f029_deferred_revenue_book_core16_3rd_v017_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_diff(_slope(deferredrev, 4), 4), 8))
def cg_f029_deferred_revenue_book_core17_3rd_v018_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_diff(_z(deferredrev, 12), 4), 8))
def cg_f029_deferred_revenue_book_core18_3rd_v019_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_diff(deferredrev - revenue, 4), 8))
def cg_f029_deferred_revenue_book_core19_3rd_v020_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_diff(_safe_div(deferredrev, revenue + liabilities + 1.0), 4), 8))
def cg_f029_deferred_revenue_book_core20_3rd_v021_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_slope(deferredrev, 4), 4))
def cg_f029_deferred_revenue_book_core21_3rd_v022_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_slope(_safe_div(deferredrev, revenue.abs() + 1.0), 4), 4))
def cg_f029_deferred_revenue_book_core22_3rd_v023_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_slope(_safe_div(deferredrev, liabilities.abs() + 1.0), 4), 4))
def cg_f029_deferred_revenue_book_core23_3rd_v024_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_slope(_safe_div(revenue, liabilities.abs() + 1.0), 4), 4))
def cg_f029_deferred_revenue_book_core24_3rd_v025_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_slope(deferredrev / (revenue.abs() + 1.0), 4), 4))
def cg_f029_deferred_revenue_book_core25_3rd_v026_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_slope(_diff(deferredrev, 4), 4), 4))
def cg_f029_deferred_revenue_book_core26_3rd_v027_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_slope(_slope(deferredrev, 4), 4), 4))
def cg_f029_deferred_revenue_book_core27_3rd_v028_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_slope(_z(deferredrev, 12), 4), 4))
def cg_f029_deferred_revenue_book_core28_3rd_v029_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_slope(deferredrev - revenue, 4), 4))
def cg_f029_deferred_revenue_book_core29_3rd_v030_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_slope(_safe_div(deferredrev, revenue + liabilities + 1.0), 4), 4))
def cg_f029_deferred_revenue_book_core30_3rd_v031_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_diff(_diff(deferredrev, 4), 4), 8))
def cg_f029_deferred_revenue_book_core31_3rd_v032_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_diff(_diff(_safe_div(deferredrev, revenue.abs() + 1.0), 4), 4), 8))
def cg_f029_deferred_revenue_book_core32_3rd_v033_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_diff(_diff(_safe_div(deferredrev, liabilities.abs() + 1.0), 4), 4), 8))
def cg_f029_deferred_revenue_book_core33_3rd_v034_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_diff(_diff(_safe_div(revenue, liabilities.abs() + 1.0), 4), 4), 8))
def cg_f029_deferred_revenue_book_core34_3rd_v035_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_diff(_diff(deferredrev / (revenue.abs() + 1.0), 4), 4), 8))
def cg_f029_deferred_revenue_book_core35_3rd_v036_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_diff(_diff(_diff(deferredrev, 4), 4), 4), 8))
def cg_f029_deferred_revenue_book_core36_3rd_v037_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_diff(_diff(_slope(deferredrev, 4), 4), 4), 8))
def cg_f029_deferred_revenue_book_core37_3rd_v038_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_diff(_diff(_z(deferredrev, 12), 4), 4), 8))
def cg_f029_deferred_revenue_book_core38_3rd_v039_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_diff(_diff(deferredrev - revenue, 4), 4), 8))
def cg_f029_deferred_revenue_book_core39_3rd_v040_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_diff(_diff(_safe_div(deferredrev, revenue + liabilities + 1.0), 4), 4), 8))
def cg_f029_deferred_revenue_book_core40_3rd_v041_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_slope(_diff(deferredrev, 4), 8), 12))
def cg_f029_deferred_revenue_book_core41_3rd_v042_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_slope(_diff(_safe_div(deferredrev, revenue.abs() + 1.0), 4), 8), 12))
def cg_f029_deferred_revenue_book_core42_3rd_v043_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_slope(_diff(_safe_div(deferredrev, liabilities.abs() + 1.0), 4), 8), 12))
def cg_f029_deferred_revenue_book_core43_3rd_v044_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_slope(_diff(_safe_div(revenue, liabilities.abs() + 1.0), 4), 8), 12))
def cg_f029_deferred_revenue_book_core44_3rd_v045_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_slope(_diff(deferredrev / (revenue.abs() + 1.0), 4), 8), 12))
def cg_f029_deferred_revenue_book_core45_3rd_v046_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_slope(_diff(_diff(deferredrev, 4), 4), 8), 12))
def cg_f029_deferred_revenue_book_core46_3rd_v047_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_slope(_diff(_slope(deferredrev, 4), 4), 8), 12))
def cg_f029_deferred_revenue_book_core47_3rd_v048_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_slope(_diff(_z(deferredrev, 12), 4), 8), 12))
def cg_f029_deferred_revenue_book_core48_3rd_v049_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_slope(_diff(deferredrev - revenue, 4), 8), 12))
def cg_f029_deferred_revenue_book_core49_3rd_v050_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_slope(_diff(_safe_div(deferredrev, revenue + liabilities + 1.0), 4), 8), 12))
def cg_f029_deferred_revenue_book_core50_3rd_v051_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_diff(_slope(deferredrev, 4), 4), 8))
def cg_f029_deferred_revenue_book_core51_3rd_v052_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_diff(_slope(_safe_div(deferredrev, revenue.abs() + 1.0), 4), 4), 8))
def cg_f029_deferred_revenue_book_core52_3rd_v053_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_diff(_slope(_safe_div(deferredrev, liabilities.abs() + 1.0), 4), 4), 8))
def cg_f029_deferred_revenue_book_core53_3rd_v054_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_diff(_slope(_safe_div(revenue, liabilities.abs() + 1.0), 4), 4), 8))
def cg_f029_deferred_revenue_book_core54_3rd_v055_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_diff(_slope(deferredrev / (revenue.abs() + 1.0), 4), 4), 8))
def cg_f029_deferred_revenue_book_core55_3rd_v056_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_diff(_slope(_diff(deferredrev, 4), 4), 4), 8))
def cg_f029_deferred_revenue_book_core56_3rd_v057_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_diff(_slope(_slope(deferredrev, 4), 4), 4), 8))
def cg_f029_deferred_revenue_book_core57_3rd_v058_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_diff(_slope(_z(deferredrev, 12), 4), 4), 8))
def cg_f029_deferred_revenue_book_core58_3rd_v059_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_diff(_slope(deferredrev - revenue, 4), 4), 8))
def cg_f029_deferred_revenue_book_core59_3rd_v060_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_diff(_slope(_safe_div(deferredrev, revenue + liabilities + 1.0), 4), 4), 8))
def cg_f029_deferred_revenue_book_core60_3rd_v061_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_diff(_diff(deferredrev, 4), 4), 12))
def cg_f029_deferred_revenue_book_core61_3rd_v062_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_diff(_diff(_safe_div(deferredrev, revenue.abs() + 1.0), 4), 4), 12))
def cg_f029_deferred_revenue_book_core62_3rd_v063_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_diff(_diff(_safe_div(deferredrev, liabilities.abs() + 1.0), 4), 4), 12))
def cg_f029_deferred_revenue_book_core63_3rd_v064_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_diff(_diff(_safe_div(revenue, liabilities.abs() + 1.0), 4), 4), 12))
def cg_f029_deferred_revenue_book_core64_3rd_v065_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_diff(_diff(deferredrev / (revenue.abs() + 1.0), 4), 4), 12))
def cg_f029_deferred_revenue_book_core65_3rd_v066_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_diff(_diff(_diff(deferredrev, 4), 4), 4), 12))
def cg_f029_deferred_revenue_book_core66_3rd_v067_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_diff(_diff(_slope(deferredrev, 4), 4), 4), 12))
def cg_f029_deferred_revenue_book_core67_3rd_v068_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_diff(_diff(_z(deferredrev, 12), 4), 4), 12))
def cg_f029_deferred_revenue_book_core68_3rd_v069_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_diff(_diff(deferredrev - revenue, 4), 4), 12))
def cg_f029_deferred_revenue_book_core69_3rd_v070_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_diff(_diff(_safe_div(deferredrev, revenue + liabilities + 1.0), 4), 4), 12))
def cg_f029_deferred_revenue_book_core70_3rd_v071_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_slope(_diff(deferredrev, 4), 8), 12))
def cg_f029_deferred_revenue_book_core71_3rd_v072_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_slope(_diff(_safe_div(deferredrev, revenue.abs() + 1.0), 4), 8), 12))
def cg_f029_deferred_revenue_book_core72_3rd_v073_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_slope(_diff(_safe_div(deferredrev, liabilities.abs() + 1.0), 4), 8), 12))
def cg_f029_deferred_revenue_book_core73_3rd_v074_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_slope(_diff(_safe_div(revenue, liabilities.abs() + 1.0), 4), 8), 12))
def cg_f029_deferred_revenue_book_core74_3rd_v075_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_slope(_diff(deferredrev / (revenue.abs() + 1.0), 4), 8), 12))
def cg_f029_deferred_revenue_book_core75_3rd_v076_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_slope(_diff(_diff(deferredrev, 4), 4), 8), 12))
def cg_f029_deferred_revenue_book_core76_3rd_v077_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_slope(_diff(_slope(deferredrev, 4), 4), 8), 12))
def cg_f029_deferred_revenue_book_core77_3rd_v078_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_slope(_diff(_z(deferredrev, 12), 4), 8), 12))
def cg_f029_deferred_revenue_book_core78_3rd_v079_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_slope(_diff(deferredrev - revenue, 4), 8), 12))
def cg_f029_deferred_revenue_book_core79_3rd_v080_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_slope(_diff(_safe_div(deferredrev, revenue + liabilities + 1.0), 4), 8), 12))
def cg_f029_deferred_revenue_book_core80_3rd_v081_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_diff(_slope(deferredrev, 4), 4), 12))
def cg_f029_deferred_revenue_book_core81_3rd_v082_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_diff(_slope(_safe_div(deferredrev, revenue.abs() + 1.0), 4), 4), 12))
def cg_f029_deferred_revenue_book_core82_3rd_v083_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_diff(_slope(_safe_div(deferredrev, liabilities.abs() + 1.0), 4), 4), 12))
def cg_f029_deferred_revenue_book_core83_3rd_v084_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_diff(_slope(_safe_div(revenue, liabilities.abs() + 1.0), 4), 4), 12))
def cg_f029_deferred_revenue_book_core84_3rd_v085_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_diff(_slope(deferredrev / (revenue.abs() + 1.0), 4), 4), 12))
def cg_f029_deferred_revenue_book_core85_3rd_v086_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_diff(_slope(_diff(deferredrev, 4), 4), 4), 12))
def cg_f029_deferred_revenue_book_core86_3rd_v087_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_diff(_slope(_slope(deferredrev, 4), 4), 4), 12))
def cg_f029_deferred_revenue_book_core87_3rd_v088_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_diff(_slope(_z(deferredrev, 12), 4), 4), 12))
def cg_f029_deferred_revenue_book_core88_3rd_v089_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_diff(_slope(deferredrev - revenue, 4), 4), 12))
def cg_f029_deferred_revenue_book_core89_3rd_v090_signal(deferredrev, revenue, liabilities):
    return _clean(_rank(_diff(_slope(_safe_div(deferredrev, revenue + liabilities + 1.0), 4), 4), 12))
def cg_f029_deferred_revenue_book_core90_3rd_v091_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_diff(_diff(deferredrev, 4), 4), 4))
def cg_f029_deferred_revenue_book_core91_3rd_v092_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_diff(_diff(_safe_div(deferredrev, revenue.abs() + 1.0), 4), 4), 4))
def cg_f029_deferred_revenue_book_core92_3rd_v093_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_diff(_diff(_safe_div(deferredrev, liabilities.abs() + 1.0), 4), 4), 4))
def cg_f029_deferred_revenue_book_core93_3rd_v094_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_diff(_diff(_safe_div(revenue, liabilities.abs() + 1.0), 4), 4), 4))
def cg_f029_deferred_revenue_book_core94_3rd_v095_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_diff(_diff(deferredrev / (revenue.abs() + 1.0), 4), 4), 4))
def cg_f029_deferred_revenue_book_core95_3rd_v096_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_diff(_diff(_diff(deferredrev, 4), 4), 4), 4))
def cg_f029_deferred_revenue_book_core96_3rd_v097_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_diff(_diff(_slope(deferredrev, 4), 4), 4), 4))
def cg_f029_deferred_revenue_book_core97_3rd_v098_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_diff(_diff(_z(deferredrev, 12), 4), 4), 4))
def cg_f029_deferred_revenue_book_core98_3rd_v099_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_diff(_diff(deferredrev - revenue, 4), 4), 4))
def cg_f029_deferred_revenue_book_core99_3rd_v100_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_diff(_diff(_safe_div(deferredrev, revenue + liabilities + 1.0), 4), 4), 4))
def cg_f029_deferred_revenue_book_core100_3rd_v101_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_slope(_diff(deferredrev, 4), 8), 4))
def cg_f029_deferred_revenue_book_core101_3rd_v102_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_slope(_diff(_safe_div(deferredrev, revenue.abs() + 1.0), 4), 8), 4))
def cg_f029_deferred_revenue_book_core102_3rd_v103_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_slope(_diff(_safe_div(deferredrev, liabilities.abs() + 1.0), 4), 8), 4))
def cg_f029_deferred_revenue_book_core103_3rd_v104_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_slope(_diff(_safe_div(revenue, liabilities.abs() + 1.0), 4), 8), 4))
def cg_f029_deferred_revenue_book_core104_3rd_v105_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_slope(_diff(deferredrev / (revenue.abs() + 1.0), 4), 8), 4))
def cg_f029_deferred_revenue_book_core105_3rd_v106_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_slope(_diff(_diff(deferredrev, 4), 4), 8), 4))
def cg_f029_deferred_revenue_book_core106_3rd_v107_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_slope(_diff(_slope(deferredrev, 4), 4), 8), 4))
def cg_f029_deferred_revenue_book_core107_3rd_v108_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_slope(_diff(_z(deferredrev, 12), 4), 8), 4))
def cg_f029_deferred_revenue_book_core108_3rd_v109_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_slope(_diff(deferredrev - revenue, 4), 8), 4))
def cg_f029_deferred_revenue_book_core109_3rd_v110_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_slope(_diff(_safe_div(deferredrev, revenue + liabilities + 1.0), 4), 8), 4))
def cg_f029_deferred_revenue_book_core110_3rd_v111_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_diff(_slope(deferredrev, 4), 4), 4))
def cg_f029_deferred_revenue_book_core111_3rd_v112_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_diff(_slope(_safe_div(deferredrev, revenue.abs() + 1.0), 4), 4), 4))
def cg_f029_deferred_revenue_book_core112_3rd_v113_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_diff(_slope(_safe_div(deferredrev, liabilities.abs() + 1.0), 4), 4), 4))
def cg_f029_deferred_revenue_book_core113_3rd_v114_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_diff(_slope(_safe_div(revenue, liabilities.abs() + 1.0), 4), 4), 4))
def cg_f029_deferred_revenue_book_core114_3rd_v115_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_diff(_slope(deferredrev / (revenue.abs() + 1.0), 4), 4), 4))
def cg_f029_deferred_revenue_book_core115_3rd_v116_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_diff(_slope(_diff(deferredrev, 4), 4), 4), 4))
def cg_f029_deferred_revenue_book_core116_3rd_v117_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_diff(_slope(_slope(deferredrev, 4), 4), 4), 4))
def cg_f029_deferred_revenue_book_core117_3rd_v118_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_diff(_slope(_z(deferredrev, 12), 4), 4), 4))
def cg_f029_deferred_revenue_book_core118_3rd_v119_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_diff(_slope(deferredrev - revenue, 4), 4), 4))
def cg_f029_deferred_revenue_book_core119_3rd_v120_signal(deferredrev, revenue, liabilities):
    return _clean(_mean(_diff(_slope(_safe_div(deferredrev, revenue + liabilities + 1.0), 4), 4), 4))
def cg_f029_deferred_revenue_book_core120_3rd_v121_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_diff(_diff(deferredrev, 4), 4), 4))
def cg_f029_deferred_revenue_book_core121_3rd_v122_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_diff(_diff(_safe_div(deferredrev, revenue.abs() + 1.0), 4), 4), 4))
def cg_f029_deferred_revenue_book_core122_3rd_v123_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_diff(_diff(_safe_div(deferredrev, liabilities.abs() + 1.0), 4), 4), 4))
def cg_f029_deferred_revenue_book_core123_3rd_v124_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_diff(_diff(_safe_div(revenue, liabilities.abs() + 1.0), 4), 4), 4))
def cg_f029_deferred_revenue_book_core124_3rd_v125_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_diff(_diff(deferredrev / (revenue.abs() + 1.0), 4), 4), 4))
def cg_f029_deferred_revenue_book_core125_3rd_v126_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_diff(_diff(_diff(deferredrev, 4), 4), 4), 4))
def cg_f029_deferred_revenue_book_core126_3rd_v127_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_diff(_diff(_slope(deferredrev, 4), 4), 4), 4))
def cg_f029_deferred_revenue_book_core127_3rd_v128_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_diff(_diff(_z(deferredrev, 12), 4), 4), 4))
def cg_f029_deferred_revenue_book_core128_3rd_v129_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_diff(_diff(deferredrev - revenue, 4), 4), 4))
def cg_f029_deferred_revenue_book_core129_3rd_v130_signal(deferredrev, revenue, liabilities):
    return _clean(_slope(_diff(_diff(_safe_div(deferredrev, revenue + liabilities + 1.0), 4), 4), 4))
def cg_f029_deferred_revenue_book_core130_3rd_v131_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_diff(_diff(deferredrev, 4), 4), 4))
def cg_f029_deferred_revenue_book_core131_3rd_v132_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_diff(_diff(_safe_div(deferredrev, revenue.abs() + 1.0), 4), 4), 4))
def cg_f029_deferred_revenue_book_core132_3rd_v133_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_diff(_diff(_safe_div(deferredrev, liabilities.abs() + 1.0), 4), 4), 4))
def cg_f029_deferred_revenue_book_core133_3rd_v134_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_diff(_diff(_safe_div(revenue, liabilities.abs() + 1.0), 4), 4), 4))
def cg_f029_deferred_revenue_book_core134_3rd_v135_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_diff(_diff(deferredrev / (revenue.abs() + 1.0), 4), 4), 4))
def cg_f029_deferred_revenue_book_core135_3rd_v136_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_diff(_diff(_diff(deferredrev, 4), 4), 4), 4))
def cg_f029_deferred_revenue_book_core136_3rd_v137_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_diff(_diff(_slope(deferredrev, 4), 4), 4), 4))
def cg_f029_deferred_revenue_book_core137_3rd_v138_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_diff(_diff(_z(deferredrev, 12), 4), 4), 4))
def cg_f029_deferred_revenue_book_core138_3rd_v139_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_diff(_diff(deferredrev - revenue, 4), 4), 4))
def cg_f029_deferred_revenue_book_core139_3rd_v140_signal(deferredrev, revenue, liabilities):
    return _clean(_diff(_diff(_diff(_safe_div(deferredrev, revenue + liabilities + 1.0), 4), 4), 4))
def cg_f029_deferred_revenue_book_core140_3rd_v141_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_slope(_diff(_diff(deferredrev, 4), 4), 4), 8))
def cg_f029_deferred_revenue_book_core141_3rd_v142_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_slope(_diff(_diff(_safe_div(deferredrev, revenue.abs() + 1.0), 4), 4), 4), 8))
def cg_f029_deferred_revenue_book_core142_3rd_v143_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_slope(_diff(_diff(_safe_div(deferredrev, liabilities.abs() + 1.0), 4), 4), 4), 8))
def cg_f029_deferred_revenue_book_core143_3rd_v144_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_slope(_diff(_diff(_safe_div(revenue, liabilities.abs() + 1.0), 4), 4), 4), 8))
def cg_f029_deferred_revenue_book_core144_3rd_v145_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_slope(_diff(_diff(deferredrev / (revenue.abs() + 1.0), 4), 4), 4), 8))
def cg_f029_deferred_revenue_book_core145_3rd_v146_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_slope(_diff(_diff(_diff(deferredrev, 4), 4), 4), 4), 8))
def cg_f029_deferred_revenue_book_core146_3rd_v147_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_slope(_diff(_diff(_slope(deferredrev, 4), 4), 4), 4), 8))
def cg_f029_deferred_revenue_book_core147_3rd_v148_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_slope(_diff(_diff(_z(deferredrev, 12), 4), 4), 4), 8))
def cg_f029_deferred_revenue_book_core148_3rd_v149_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_slope(_diff(_diff(deferredrev - revenue, 4), 4), 4), 8))
def cg_f029_deferred_revenue_book_core149_3rd_v150_signal(deferredrev, revenue, liabilities):
    return _clean(_z(_slope(_diff(_diff(_safe_div(deferredrev, revenue + liabilities + 1.0), 4), 4), 4), 8))