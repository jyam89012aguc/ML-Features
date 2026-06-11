import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f073_earnings_multiples_core00_2nd_v001_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(pe, 4))
def cg_f073_earnings_multiples_core01_2nd_v002_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(pe1, 4))
def cg_f073_earnings_multiples_core02_2nd_v003_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(evebit, 4))
def cg_f073_earnings_multiples_core03_2nd_v004_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(evebitda, 4))
def cg_f073_earnings_multiples_core04_2nd_v005_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(ebit, 4))
def cg_f073_earnings_multiples_core05_2nd_v006_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(ebitda, 4))
def cg_f073_earnings_multiples_core06_2nd_v007_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_safe_div(ebitda, ebit), 4))
def cg_f073_earnings_multiples_core07_2nd_v008_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_safe_div(1.0, pe), 4))
def cg_f073_earnings_multiples_core08_2nd_v009_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_safe_div(1.0, evebitda), 4))
def cg_f073_earnings_multiples_core09_2nd_v010_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_safe_div(ebitda, ebit.abs() + 1.0), 4))
def cg_f073_earnings_multiples_core10_2nd_v011_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(pe, 8))
def cg_f073_earnings_multiples_core11_2nd_v012_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(pe1, 8))
def cg_f073_earnings_multiples_core12_2nd_v013_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(evebit, 8))
def cg_f073_earnings_multiples_core13_2nd_v014_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(evebitda, 8))
def cg_f073_earnings_multiples_core14_2nd_v015_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(ebit, 8))
def cg_f073_earnings_multiples_core15_2nd_v016_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(ebitda, 8))
def cg_f073_earnings_multiples_core16_2nd_v017_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_safe_div(ebitda, ebit), 8))
def cg_f073_earnings_multiples_core17_2nd_v018_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_safe_div(1.0, pe), 8))
def cg_f073_earnings_multiples_core18_2nd_v019_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_safe_div(1.0, evebitda), 8))
def cg_f073_earnings_multiples_core19_2nd_v020_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_safe_div(ebitda, ebit.abs() + 1.0), 8))
def cg_f073_earnings_multiples_core20_2nd_v021_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(pe, 4))
def cg_f073_earnings_multiples_core21_2nd_v022_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(pe1, 4))
def cg_f073_earnings_multiples_core22_2nd_v023_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(evebit, 4))
def cg_f073_earnings_multiples_core23_2nd_v024_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(evebitda, 4))
def cg_f073_earnings_multiples_core24_2nd_v025_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(ebit, 4))
def cg_f073_earnings_multiples_core25_2nd_v026_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(ebitda, 4))
def cg_f073_earnings_multiples_core26_2nd_v027_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(_safe_div(ebitda, ebit), 4))
def cg_f073_earnings_multiples_core27_2nd_v028_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(_safe_div(1.0, pe), 4))
def cg_f073_earnings_multiples_core28_2nd_v029_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(_safe_div(1.0, evebitda), 4))
def cg_f073_earnings_multiples_core29_2nd_v030_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(_safe_div(ebitda, ebit.abs() + 1.0), 4))
def cg_f073_earnings_multiples_core30_2nd_v031_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_slope(pe, 4), 8))
def cg_f073_earnings_multiples_core31_2nd_v032_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_slope(pe1, 4), 8))
def cg_f073_earnings_multiples_core32_2nd_v033_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_slope(evebit, 4), 8))
def cg_f073_earnings_multiples_core33_2nd_v034_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_slope(evebitda, 4), 8))
def cg_f073_earnings_multiples_core34_2nd_v035_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_slope(ebit, 4), 8))
def cg_f073_earnings_multiples_core35_2nd_v036_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_slope(ebitda, 4), 8))
def cg_f073_earnings_multiples_core36_2nd_v037_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_slope(_safe_div(ebitda, ebit), 4), 8))
def cg_f073_earnings_multiples_core37_2nd_v038_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_slope(_safe_div(1.0, pe), 4), 8))
def cg_f073_earnings_multiples_core38_2nd_v039_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_slope(_safe_div(1.0, evebitda), 4), 8))
def cg_f073_earnings_multiples_core39_2nd_v040_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_slope(_safe_div(ebitda, ebit.abs() + 1.0), 4), 8))
def cg_f073_earnings_multiples_core40_2nd_v041_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_slope(pe, 8), 12))
def cg_f073_earnings_multiples_core41_2nd_v042_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_slope(pe1, 8), 12))
def cg_f073_earnings_multiples_core42_2nd_v043_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_slope(evebit, 8), 12))
def cg_f073_earnings_multiples_core43_2nd_v044_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_slope(evebitda, 8), 12))
def cg_f073_earnings_multiples_core44_2nd_v045_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_slope(ebit, 8), 12))
def cg_f073_earnings_multiples_core45_2nd_v046_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_slope(ebitda, 8), 12))
def cg_f073_earnings_multiples_core46_2nd_v047_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_slope(_safe_div(ebitda, ebit), 8), 12))
def cg_f073_earnings_multiples_core47_2nd_v048_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_slope(_safe_div(1.0, pe), 8), 12))
def cg_f073_earnings_multiples_core48_2nd_v049_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_slope(_safe_div(1.0, evebitda), 8), 12))
def cg_f073_earnings_multiples_core49_2nd_v050_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_slope(_safe_div(ebitda, ebit.abs() + 1.0), 8), 12))
def cg_f073_earnings_multiples_core50_2nd_v051_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_diff(pe, 4), 8))
def cg_f073_earnings_multiples_core51_2nd_v052_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_diff(pe1, 4), 8))
def cg_f073_earnings_multiples_core52_2nd_v053_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_diff(evebit, 4), 8))
def cg_f073_earnings_multiples_core53_2nd_v054_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_diff(evebitda, 4), 8))
def cg_f073_earnings_multiples_core54_2nd_v055_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_diff(ebit, 4), 8))
def cg_f073_earnings_multiples_core55_2nd_v056_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_diff(ebitda, 4), 8))
def cg_f073_earnings_multiples_core56_2nd_v057_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_diff(_safe_div(ebitda, ebit), 4), 8))
def cg_f073_earnings_multiples_core57_2nd_v058_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_diff(_safe_div(1.0, pe), 4), 8))
def cg_f073_earnings_multiples_core58_2nd_v059_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_diff(_safe_div(1.0, evebitda), 4), 8))
def cg_f073_earnings_multiples_core59_2nd_v060_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_diff(_safe_div(ebitda, ebit.abs() + 1.0), 4), 8))
def cg_f073_earnings_multiples_core60_2nd_v061_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_slope(pe, 4), 12))
def cg_f073_earnings_multiples_core61_2nd_v062_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_slope(pe1, 4), 12))
def cg_f073_earnings_multiples_core62_2nd_v063_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_slope(evebit, 4), 12))
def cg_f073_earnings_multiples_core63_2nd_v064_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_slope(evebitda, 4), 12))
def cg_f073_earnings_multiples_core64_2nd_v065_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_slope(ebit, 4), 12))
def cg_f073_earnings_multiples_core65_2nd_v066_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_slope(ebitda, 4), 12))
def cg_f073_earnings_multiples_core66_2nd_v067_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_slope(_safe_div(ebitda, ebit), 4), 12))
def cg_f073_earnings_multiples_core67_2nd_v068_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_slope(_safe_div(1.0, pe), 4), 12))
def cg_f073_earnings_multiples_core68_2nd_v069_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_slope(_safe_div(1.0, evebitda), 4), 12))
def cg_f073_earnings_multiples_core69_2nd_v070_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_slope(_safe_div(ebitda, ebit.abs() + 1.0), 4), 12))
def cg_f073_earnings_multiples_core70_2nd_v071_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_diff(pe, 4), 12))
def cg_f073_earnings_multiples_core71_2nd_v072_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_diff(pe1, 4), 12))
def cg_f073_earnings_multiples_core72_2nd_v073_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_diff(evebit, 4), 12))
def cg_f073_earnings_multiples_core73_2nd_v074_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_diff(evebitda, 4), 12))
def cg_f073_earnings_multiples_core74_2nd_v075_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_diff(ebit, 4), 12))
def cg_f073_earnings_multiples_core75_2nd_v076_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_diff(ebitda, 4), 12))
def cg_f073_earnings_multiples_core76_2nd_v077_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_diff(_safe_div(ebitda, ebit), 4), 12))
def cg_f073_earnings_multiples_core77_2nd_v078_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_diff(_safe_div(1.0, pe), 4), 12))
def cg_f073_earnings_multiples_core78_2nd_v079_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_diff(_safe_div(1.0, evebitda), 4), 12))
def cg_f073_earnings_multiples_core79_2nd_v080_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_diff(_safe_div(ebitda, ebit.abs() + 1.0), 4), 12))
def cg_f073_earnings_multiples_core80_2nd_v081_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_slope(pe, 4), 4))
def cg_f073_earnings_multiples_core81_2nd_v082_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_slope(pe1, 4), 4))
def cg_f073_earnings_multiples_core82_2nd_v083_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_slope(evebit, 4), 4))
def cg_f073_earnings_multiples_core83_2nd_v084_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_slope(evebitda, 4), 4))
def cg_f073_earnings_multiples_core84_2nd_v085_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_slope(ebit, 4), 4))
def cg_f073_earnings_multiples_core85_2nd_v086_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_slope(ebitda, 4), 4))
def cg_f073_earnings_multiples_core86_2nd_v087_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_slope(_safe_div(ebitda, ebit), 4), 4))
def cg_f073_earnings_multiples_core87_2nd_v088_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_slope(_safe_div(1.0, pe), 4), 4))
def cg_f073_earnings_multiples_core88_2nd_v089_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_slope(_safe_div(1.0, evebitda), 4), 4))
def cg_f073_earnings_multiples_core89_2nd_v090_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_slope(_safe_div(ebitda, ebit.abs() + 1.0), 4), 4))
def cg_f073_earnings_multiples_core90_2nd_v091_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_diff(pe, 4), 4))
def cg_f073_earnings_multiples_core91_2nd_v092_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_diff(pe1, 4), 4))
def cg_f073_earnings_multiples_core92_2nd_v093_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_diff(evebit, 4), 4))
def cg_f073_earnings_multiples_core93_2nd_v094_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_diff(evebitda, 4), 4))
def cg_f073_earnings_multiples_core94_2nd_v095_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_diff(ebit, 4), 4))
def cg_f073_earnings_multiples_core95_2nd_v096_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_diff(ebitda, 4), 4))
def cg_f073_earnings_multiples_core96_2nd_v097_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_diff(_safe_div(ebitda, ebit), 4), 4))
def cg_f073_earnings_multiples_core97_2nd_v098_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_diff(_safe_div(1.0, pe), 4), 4))
def cg_f073_earnings_multiples_core98_2nd_v099_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_diff(_safe_div(1.0, evebitda), 4), 4))
def cg_f073_earnings_multiples_core99_2nd_v100_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_diff(_safe_div(ebitda, ebit.abs() + 1.0), 4), 4))
def cg_f073_earnings_multiples_core100_2nd_v101_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_mean(pe, 4), 4))
def cg_f073_earnings_multiples_core101_2nd_v102_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_mean(pe1, 4), 4))
def cg_f073_earnings_multiples_core102_2nd_v103_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_mean(evebit, 4), 4))
def cg_f073_earnings_multiples_core103_2nd_v104_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_mean(evebitda, 4), 4))
def cg_f073_earnings_multiples_core104_2nd_v105_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_mean(ebit, 4), 4))
def cg_f073_earnings_multiples_core105_2nd_v106_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_mean(ebitda, 4), 4))
def cg_f073_earnings_multiples_core106_2nd_v107_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_mean(_safe_div(ebitda, ebit), 4), 4))
def cg_f073_earnings_multiples_core107_2nd_v108_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_mean(_safe_div(1.0, pe), 4), 4))
def cg_f073_earnings_multiples_core108_2nd_v109_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_mean(_safe_div(1.0, evebitda), 4), 4))
def cg_f073_earnings_multiples_core109_2nd_v110_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_mean(_safe_div(ebitda, ebit.abs() + 1.0), 4), 4))
def cg_f073_earnings_multiples_core110_2nd_v111_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_mean(pe, 8), 8))
def cg_f073_earnings_multiples_core111_2nd_v112_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_mean(pe1, 8), 8))
def cg_f073_earnings_multiples_core112_2nd_v113_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_mean(evebit, 8), 8))
def cg_f073_earnings_multiples_core113_2nd_v114_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_mean(evebitda, 8), 8))
def cg_f073_earnings_multiples_core114_2nd_v115_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_mean(ebit, 8), 8))
def cg_f073_earnings_multiples_core115_2nd_v116_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_mean(ebitda, 8), 8))
def cg_f073_earnings_multiples_core116_2nd_v117_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_mean(_safe_div(ebitda, ebit), 8), 8))
def cg_f073_earnings_multiples_core117_2nd_v118_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_mean(_safe_div(1.0, pe), 8), 8))
def cg_f073_earnings_multiples_core118_2nd_v119_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_mean(_safe_div(1.0, evebitda), 8), 8))
def cg_f073_earnings_multiples_core119_2nd_v120_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_mean(_safe_div(ebitda, ebit.abs() + 1.0), 8), 8))
def cg_f073_earnings_multiples_core120_2nd_v121_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(_mean(pe, 4), 4))
def cg_f073_earnings_multiples_core121_2nd_v122_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(_mean(pe1, 4), 4))
def cg_f073_earnings_multiples_core122_2nd_v123_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(_mean(evebit, 4), 4))
def cg_f073_earnings_multiples_core123_2nd_v124_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(_mean(evebitda, 4), 4))
def cg_f073_earnings_multiples_core124_2nd_v125_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(_mean(ebit, 4), 4))
def cg_f073_earnings_multiples_core125_2nd_v126_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(_mean(ebitda, 4), 4))
def cg_f073_earnings_multiples_core126_2nd_v127_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(_mean(_safe_div(ebitda, ebit), 4), 4))
def cg_f073_earnings_multiples_core127_2nd_v128_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(_mean(_safe_div(1.0, pe), 4), 4))
def cg_f073_earnings_multiples_core128_2nd_v129_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(_mean(_safe_div(1.0, evebitda), 4), 4))
def cg_f073_earnings_multiples_core129_2nd_v130_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(_mean(_safe_div(ebitda, ebit.abs() + 1.0), 4), 4))
def cg_f073_earnings_multiples_core130_2nd_v131_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_diff(_mean(pe, 4), 4), 8))
def cg_f073_earnings_multiples_core131_2nd_v132_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_diff(_mean(pe1, 4), 4), 8))
def cg_f073_earnings_multiples_core132_2nd_v133_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_diff(_mean(evebit, 4), 4), 8))
def cg_f073_earnings_multiples_core133_2nd_v134_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_diff(_mean(evebitda, 4), 4), 8))
def cg_f073_earnings_multiples_core134_2nd_v135_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_diff(_mean(ebit, 4), 4), 8))
def cg_f073_earnings_multiples_core135_2nd_v136_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_diff(_mean(ebitda, 4), 4), 8))
def cg_f073_earnings_multiples_core136_2nd_v137_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_diff(_mean(_safe_div(ebitda, ebit), 4), 4), 8))
def cg_f073_earnings_multiples_core137_2nd_v138_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_diff(_mean(_safe_div(1.0, pe), 4), 4), 8))
def cg_f073_earnings_multiples_core138_2nd_v139_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_diff(_mean(_safe_div(1.0, evebitda), 4), 4), 8))
def cg_f073_earnings_multiples_core139_2nd_v140_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_diff(_mean(_safe_div(ebitda, ebit.abs() + 1.0), 4), 4), 8))
def cg_f073_earnings_multiples_core140_2nd_v141_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_slope(_mean(pe, 4), 4), 12))
def cg_f073_earnings_multiples_core141_2nd_v142_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_slope(_mean(pe1, 4), 4), 12))
def cg_f073_earnings_multiples_core142_2nd_v143_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_slope(_mean(evebit, 4), 4), 12))
def cg_f073_earnings_multiples_core143_2nd_v144_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_slope(_mean(evebitda, 4), 4), 12))
def cg_f073_earnings_multiples_core144_2nd_v145_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_slope(_mean(ebit, 4), 4), 12))
def cg_f073_earnings_multiples_core145_2nd_v146_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_slope(_mean(ebitda, 4), 4), 12))
def cg_f073_earnings_multiples_core146_2nd_v147_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_slope(_mean(_safe_div(ebitda, ebit), 4), 4), 12))
def cg_f073_earnings_multiples_core147_2nd_v148_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_slope(_mean(_safe_div(1.0, pe), 4), 4), 12))
def cg_f073_earnings_multiples_core148_2nd_v149_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_slope(_mean(_safe_div(1.0, evebitda), 4), 4), 12))
def cg_f073_earnings_multiples_core149_2nd_v150_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_slope(_mean(_safe_div(ebitda, ebit.abs() + 1.0), 4), 4), 12))