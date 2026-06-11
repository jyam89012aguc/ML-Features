import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f050_revenue_quality_core00_2nd_v001_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_slope(revenue, 4))
def cg_f050_revenue_quality_core01_2nd_v002_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_slope(ncfo, 4))
def cg_f050_revenue_quality_core02_2nd_v003_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_slope(receivables, 4))
def cg_f050_revenue_quality_core03_2nd_v004_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_slope(deferredrev, 4))
def cg_f050_revenue_quality_core04_2nd_v005_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_slope(_safe_div(ncfo, revenue), 4))
def cg_f050_revenue_quality_core05_2nd_v006_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_slope(_safe_div(receivables, revenue), 4))
def cg_f050_revenue_quality_core06_2nd_v007_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_slope(_safe_div(deferredrev, revenue), 4))
def cg_f050_revenue_quality_core07_2nd_v008_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_slope(ncfo - revenue, 4))
def cg_f050_revenue_quality_core08_2nd_v009_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_slope(_diff(revenue, 4), 4))
def cg_f050_revenue_quality_core09_2nd_v010_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_slope(_pct_change(revenue, 4), 4))
def cg_f050_revenue_quality_core10_2nd_v011_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_slope(revenue, 8))
def cg_f050_revenue_quality_core11_2nd_v012_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_slope(ncfo, 8))
def cg_f050_revenue_quality_core12_2nd_v013_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_slope(receivables, 8))
def cg_f050_revenue_quality_core13_2nd_v014_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_slope(deferredrev, 8))
def cg_f050_revenue_quality_core14_2nd_v015_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_slope(_safe_div(ncfo, revenue), 8))
def cg_f050_revenue_quality_core15_2nd_v016_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_slope(_safe_div(receivables, revenue), 8))
def cg_f050_revenue_quality_core16_2nd_v017_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_slope(_safe_div(deferredrev, revenue), 8))
def cg_f050_revenue_quality_core17_2nd_v018_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_slope(ncfo - revenue, 8))
def cg_f050_revenue_quality_core18_2nd_v019_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_slope(_diff(revenue, 4), 8))
def cg_f050_revenue_quality_core19_2nd_v020_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_slope(_pct_change(revenue, 4), 8))
def cg_f050_revenue_quality_core20_2nd_v021_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_diff(revenue, 4))
def cg_f050_revenue_quality_core21_2nd_v022_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_diff(ncfo, 4))
def cg_f050_revenue_quality_core22_2nd_v023_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_diff(receivables, 4))
def cg_f050_revenue_quality_core23_2nd_v024_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_diff(deferredrev, 4))
def cg_f050_revenue_quality_core24_2nd_v025_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_diff(_safe_div(ncfo, revenue), 4))
def cg_f050_revenue_quality_core25_2nd_v026_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_diff(_safe_div(receivables, revenue), 4))
def cg_f050_revenue_quality_core26_2nd_v027_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_diff(_safe_div(deferredrev, revenue), 4))
def cg_f050_revenue_quality_core27_2nd_v028_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_diff(ncfo - revenue, 4))
def cg_f050_revenue_quality_core28_2nd_v029_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_diff(_diff(revenue, 4), 4))
def cg_f050_revenue_quality_core29_2nd_v030_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_diff(_pct_change(revenue, 4), 4))
def cg_f050_revenue_quality_core30_2nd_v031_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_z(_slope(revenue, 4), 8))
def cg_f050_revenue_quality_core31_2nd_v032_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_z(_slope(ncfo, 4), 8))
def cg_f050_revenue_quality_core32_2nd_v033_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_z(_slope(receivables, 4), 8))
def cg_f050_revenue_quality_core33_2nd_v034_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_z(_slope(deferredrev, 4), 8))
def cg_f050_revenue_quality_core34_2nd_v035_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_z(_slope(_safe_div(ncfo, revenue), 4), 8))
def cg_f050_revenue_quality_core35_2nd_v036_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_z(_slope(_safe_div(receivables, revenue), 4), 8))
def cg_f050_revenue_quality_core36_2nd_v037_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_z(_slope(_safe_div(deferredrev, revenue), 4), 8))
def cg_f050_revenue_quality_core37_2nd_v038_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_z(_slope(ncfo - revenue, 4), 8))
def cg_f050_revenue_quality_core38_2nd_v039_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_z(_slope(_diff(revenue, 4), 4), 8))
def cg_f050_revenue_quality_core39_2nd_v040_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_z(_slope(_pct_change(revenue, 4), 4), 8))
def cg_f050_revenue_quality_core40_2nd_v041_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_z(_slope(revenue, 8), 12))
def cg_f050_revenue_quality_core41_2nd_v042_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_z(_slope(ncfo, 8), 12))
def cg_f050_revenue_quality_core42_2nd_v043_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_z(_slope(receivables, 8), 12))
def cg_f050_revenue_quality_core43_2nd_v044_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_z(_slope(deferredrev, 8), 12))
def cg_f050_revenue_quality_core44_2nd_v045_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_z(_slope(_safe_div(ncfo, revenue), 8), 12))
def cg_f050_revenue_quality_core45_2nd_v046_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_z(_slope(_safe_div(receivables, revenue), 8), 12))
def cg_f050_revenue_quality_core46_2nd_v047_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_z(_slope(_safe_div(deferredrev, revenue), 8), 12))
def cg_f050_revenue_quality_core47_2nd_v048_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_z(_slope(ncfo - revenue, 8), 12))
def cg_f050_revenue_quality_core48_2nd_v049_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_z(_slope(_diff(revenue, 4), 8), 12))
def cg_f050_revenue_quality_core49_2nd_v050_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_z(_slope(_pct_change(revenue, 4), 8), 12))
def cg_f050_revenue_quality_core50_2nd_v051_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_z(_diff(revenue, 4), 8))
def cg_f050_revenue_quality_core51_2nd_v052_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_z(_diff(ncfo, 4), 8))
def cg_f050_revenue_quality_core52_2nd_v053_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_z(_diff(receivables, 4), 8))
def cg_f050_revenue_quality_core53_2nd_v054_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_z(_diff(deferredrev, 4), 8))
def cg_f050_revenue_quality_core54_2nd_v055_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_z(_diff(_safe_div(ncfo, revenue), 4), 8))
def cg_f050_revenue_quality_core55_2nd_v056_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_z(_diff(_safe_div(receivables, revenue), 4), 8))
def cg_f050_revenue_quality_core56_2nd_v057_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_z(_diff(_safe_div(deferredrev, revenue), 4), 8))
def cg_f050_revenue_quality_core57_2nd_v058_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_z(_diff(ncfo - revenue, 4), 8))
def cg_f050_revenue_quality_core58_2nd_v059_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_z(_diff(_diff(revenue, 4), 4), 8))
def cg_f050_revenue_quality_core59_2nd_v060_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_z(_diff(_pct_change(revenue, 4), 4), 8))
def cg_f050_revenue_quality_core60_2nd_v061_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_rank(_slope(revenue, 4), 12))
def cg_f050_revenue_quality_core61_2nd_v062_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_rank(_slope(ncfo, 4), 12))
def cg_f050_revenue_quality_core62_2nd_v063_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_rank(_slope(receivables, 4), 12))
def cg_f050_revenue_quality_core63_2nd_v064_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_rank(_slope(deferredrev, 4), 12))
def cg_f050_revenue_quality_core64_2nd_v065_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_rank(_slope(_safe_div(ncfo, revenue), 4), 12))
def cg_f050_revenue_quality_core65_2nd_v066_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_rank(_slope(_safe_div(receivables, revenue), 4), 12))
def cg_f050_revenue_quality_core66_2nd_v067_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_rank(_slope(_safe_div(deferredrev, revenue), 4), 12))
def cg_f050_revenue_quality_core67_2nd_v068_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_rank(_slope(ncfo - revenue, 4), 12))
def cg_f050_revenue_quality_core68_2nd_v069_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_rank(_slope(_diff(revenue, 4), 4), 12))
def cg_f050_revenue_quality_core69_2nd_v070_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_rank(_slope(_pct_change(revenue, 4), 4), 12))
def cg_f050_revenue_quality_core70_2nd_v071_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_rank(_diff(revenue, 4), 12))
def cg_f050_revenue_quality_core71_2nd_v072_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_rank(_diff(ncfo, 4), 12))
def cg_f050_revenue_quality_core72_2nd_v073_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_rank(_diff(receivables, 4), 12))
def cg_f050_revenue_quality_core73_2nd_v074_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_rank(_diff(deferredrev, 4), 12))
def cg_f050_revenue_quality_core74_2nd_v075_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_rank(_diff(_safe_div(ncfo, revenue), 4), 12))
def cg_f050_revenue_quality_core75_2nd_v076_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_rank(_diff(_safe_div(receivables, revenue), 4), 12))
def cg_f050_revenue_quality_core76_2nd_v077_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_rank(_diff(_safe_div(deferredrev, revenue), 4), 12))
def cg_f050_revenue_quality_core77_2nd_v078_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_rank(_diff(ncfo - revenue, 4), 12))
def cg_f050_revenue_quality_core78_2nd_v079_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_rank(_diff(_diff(revenue, 4), 4), 12))
def cg_f050_revenue_quality_core79_2nd_v080_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_rank(_diff(_pct_change(revenue, 4), 4), 12))
def cg_f050_revenue_quality_core80_2nd_v081_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_mean(_slope(revenue, 4), 4))
def cg_f050_revenue_quality_core81_2nd_v082_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_mean(_slope(ncfo, 4), 4))
def cg_f050_revenue_quality_core82_2nd_v083_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_mean(_slope(receivables, 4), 4))
def cg_f050_revenue_quality_core83_2nd_v084_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_mean(_slope(deferredrev, 4), 4))
def cg_f050_revenue_quality_core84_2nd_v085_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_mean(_slope(_safe_div(ncfo, revenue), 4), 4))
def cg_f050_revenue_quality_core85_2nd_v086_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_mean(_slope(_safe_div(receivables, revenue), 4), 4))
def cg_f050_revenue_quality_core86_2nd_v087_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_mean(_slope(_safe_div(deferredrev, revenue), 4), 4))
def cg_f050_revenue_quality_core87_2nd_v088_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_mean(_slope(ncfo - revenue, 4), 4))
def cg_f050_revenue_quality_core88_2nd_v089_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_mean(_slope(_diff(revenue, 4), 4), 4))
def cg_f050_revenue_quality_core89_2nd_v090_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_mean(_slope(_pct_change(revenue, 4), 4), 4))
def cg_f050_revenue_quality_core90_2nd_v091_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_mean(_diff(revenue, 4), 4))
def cg_f050_revenue_quality_core91_2nd_v092_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_mean(_diff(ncfo, 4), 4))
def cg_f050_revenue_quality_core92_2nd_v093_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_mean(_diff(receivables, 4), 4))
def cg_f050_revenue_quality_core93_2nd_v094_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_mean(_diff(deferredrev, 4), 4))
def cg_f050_revenue_quality_core94_2nd_v095_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_mean(_diff(_safe_div(ncfo, revenue), 4), 4))
def cg_f050_revenue_quality_core95_2nd_v096_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_mean(_diff(_safe_div(receivables, revenue), 4), 4))
def cg_f050_revenue_quality_core96_2nd_v097_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_mean(_diff(_safe_div(deferredrev, revenue), 4), 4))
def cg_f050_revenue_quality_core97_2nd_v098_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_mean(_diff(ncfo - revenue, 4), 4))
def cg_f050_revenue_quality_core98_2nd_v099_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_mean(_diff(_diff(revenue, 4), 4), 4))
def cg_f050_revenue_quality_core99_2nd_v100_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_mean(_diff(_pct_change(revenue, 4), 4), 4))
def cg_f050_revenue_quality_core100_2nd_v101_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_slope(_mean(revenue, 4), 4))
def cg_f050_revenue_quality_core101_2nd_v102_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_slope(_mean(ncfo, 4), 4))
def cg_f050_revenue_quality_core102_2nd_v103_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_slope(_mean(receivables, 4), 4))
def cg_f050_revenue_quality_core103_2nd_v104_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_slope(_mean(deferredrev, 4), 4))
def cg_f050_revenue_quality_core104_2nd_v105_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_slope(_mean(_safe_div(ncfo, revenue), 4), 4))
def cg_f050_revenue_quality_core105_2nd_v106_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_slope(_mean(_safe_div(receivables, revenue), 4), 4))
def cg_f050_revenue_quality_core106_2nd_v107_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_slope(_mean(_safe_div(deferredrev, revenue), 4), 4))
def cg_f050_revenue_quality_core107_2nd_v108_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_slope(_mean(ncfo - revenue, 4), 4))
def cg_f050_revenue_quality_core108_2nd_v109_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_slope(_mean(_diff(revenue, 4), 4), 4))
def cg_f050_revenue_quality_core109_2nd_v110_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_slope(_mean(_pct_change(revenue, 4), 4), 4))
def cg_f050_revenue_quality_core110_2nd_v111_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_slope(_mean(revenue, 8), 8))
def cg_f050_revenue_quality_core111_2nd_v112_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_slope(_mean(ncfo, 8), 8))
def cg_f050_revenue_quality_core112_2nd_v113_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_slope(_mean(receivables, 8), 8))
def cg_f050_revenue_quality_core113_2nd_v114_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_slope(_mean(deferredrev, 8), 8))
def cg_f050_revenue_quality_core114_2nd_v115_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_slope(_mean(_safe_div(ncfo, revenue), 8), 8))
def cg_f050_revenue_quality_core115_2nd_v116_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_slope(_mean(_safe_div(receivables, revenue), 8), 8))
def cg_f050_revenue_quality_core116_2nd_v117_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_slope(_mean(_safe_div(deferredrev, revenue), 8), 8))
def cg_f050_revenue_quality_core117_2nd_v118_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_slope(_mean(ncfo - revenue, 8), 8))
def cg_f050_revenue_quality_core118_2nd_v119_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_slope(_mean(_diff(revenue, 4), 8), 8))
def cg_f050_revenue_quality_core119_2nd_v120_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_slope(_mean(_pct_change(revenue, 4), 8), 8))
def cg_f050_revenue_quality_core120_2nd_v121_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_diff(_mean(revenue, 4), 4))
def cg_f050_revenue_quality_core121_2nd_v122_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_diff(_mean(ncfo, 4), 4))
def cg_f050_revenue_quality_core122_2nd_v123_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_diff(_mean(receivables, 4), 4))
def cg_f050_revenue_quality_core123_2nd_v124_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_diff(_mean(deferredrev, 4), 4))
def cg_f050_revenue_quality_core124_2nd_v125_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_diff(_mean(_safe_div(ncfo, revenue), 4), 4))
def cg_f050_revenue_quality_core125_2nd_v126_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_diff(_mean(_safe_div(receivables, revenue), 4), 4))
def cg_f050_revenue_quality_core126_2nd_v127_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_diff(_mean(_safe_div(deferredrev, revenue), 4), 4))
def cg_f050_revenue_quality_core127_2nd_v128_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_diff(_mean(ncfo - revenue, 4), 4))
def cg_f050_revenue_quality_core128_2nd_v129_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_diff(_mean(_diff(revenue, 4), 4), 4))
def cg_f050_revenue_quality_core129_2nd_v130_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_diff(_mean(_pct_change(revenue, 4), 4), 4))
def cg_f050_revenue_quality_core130_2nd_v131_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_z(_diff(_mean(revenue, 4), 4), 8))
def cg_f050_revenue_quality_core131_2nd_v132_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_z(_diff(_mean(ncfo, 4), 4), 8))
def cg_f050_revenue_quality_core132_2nd_v133_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_z(_diff(_mean(receivables, 4), 4), 8))
def cg_f050_revenue_quality_core133_2nd_v134_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_z(_diff(_mean(deferredrev, 4), 4), 8))
def cg_f050_revenue_quality_core134_2nd_v135_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_z(_diff(_mean(_safe_div(ncfo, revenue), 4), 4), 8))
def cg_f050_revenue_quality_core135_2nd_v136_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_z(_diff(_mean(_safe_div(receivables, revenue), 4), 4), 8))
def cg_f050_revenue_quality_core136_2nd_v137_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_z(_diff(_mean(_safe_div(deferredrev, revenue), 4), 4), 8))
def cg_f050_revenue_quality_core137_2nd_v138_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_z(_diff(_mean(ncfo - revenue, 4), 4), 8))
def cg_f050_revenue_quality_core138_2nd_v139_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_z(_diff(_mean(_diff(revenue, 4), 4), 4), 8))
def cg_f050_revenue_quality_core139_2nd_v140_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_z(_diff(_mean(_pct_change(revenue, 4), 4), 4), 8))
def cg_f050_revenue_quality_core140_2nd_v141_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_rank(_slope(_mean(revenue, 4), 4), 12))
def cg_f050_revenue_quality_core141_2nd_v142_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_rank(_slope(_mean(ncfo, 4), 4), 12))
def cg_f050_revenue_quality_core142_2nd_v143_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_rank(_slope(_mean(receivables, 4), 4), 12))
def cg_f050_revenue_quality_core143_2nd_v144_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_rank(_slope(_mean(deferredrev, 4), 4), 12))
def cg_f050_revenue_quality_core144_2nd_v145_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_rank(_slope(_mean(_safe_div(ncfo, revenue), 4), 4), 12))
def cg_f050_revenue_quality_core145_2nd_v146_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_rank(_slope(_mean(_safe_div(receivables, revenue), 4), 4), 12))
def cg_f050_revenue_quality_core146_2nd_v147_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_rank(_slope(_mean(_safe_div(deferredrev, revenue), 4), 4), 12))
def cg_f050_revenue_quality_core147_2nd_v148_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_rank(_slope(_mean(ncfo - revenue, 4), 4), 12))
def cg_f050_revenue_quality_core148_2nd_v149_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_rank(_slope(_mean(_diff(revenue, 4), 4), 4), 12))
def cg_f050_revenue_quality_core149_2nd_v150_signal(revenue, ncfo, receivables, deferredrev):
    return _clean(_rank(_slope(_mean(_pct_change(revenue, 4), 4), 4), 12))