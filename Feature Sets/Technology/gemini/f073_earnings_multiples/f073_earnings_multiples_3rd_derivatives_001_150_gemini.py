import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f073_earnings_multiples_core00_3rd_v001_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(_diff(pe, 4), 4))
def cg_f073_earnings_multiples_core01_3rd_v002_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(_diff(pe1, 4), 4))
def cg_f073_earnings_multiples_core02_3rd_v003_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(_diff(evebit, 4), 4))
def cg_f073_earnings_multiples_core03_3rd_v004_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(_diff(evebitda, 4), 4))
def cg_f073_earnings_multiples_core04_3rd_v005_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(_diff(ebit, 4), 4))
def cg_f073_earnings_multiples_core05_3rd_v006_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(_diff(ebitda, 4), 4))
def cg_f073_earnings_multiples_core06_3rd_v007_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(_diff(_safe_div(ebitda, ebit), 4), 4))
def cg_f073_earnings_multiples_core07_3rd_v008_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(_diff(_safe_div(1.0, pe), 4), 4))
def cg_f073_earnings_multiples_core08_3rd_v009_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(_diff(_safe_div(1.0, evebitda), 4), 4))
def cg_f073_earnings_multiples_core09_3rd_v010_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(_diff(_safe_div(ebitda, ebit.abs() + 1.0), 4), 4))
def cg_f073_earnings_multiples_core10_3rd_v011_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_diff(pe, 4), 8))
def cg_f073_earnings_multiples_core11_3rd_v012_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_diff(pe1, 4), 8))
def cg_f073_earnings_multiples_core12_3rd_v013_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_diff(evebit, 4), 8))
def cg_f073_earnings_multiples_core13_3rd_v014_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_diff(evebitda, 4), 8))
def cg_f073_earnings_multiples_core14_3rd_v015_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_diff(ebit, 4), 8))
def cg_f073_earnings_multiples_core15_3rd_v016_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_diff(ebitda, 4), 8))
def cg_f073_earnings_multiples_core16_3rd_v017_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_diff(_safe_div(ebitda, ebit), 4), 8))
def cg_f073_earnings_multiples_core17_3rd_v018_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_diff(_safe_div(1.0, pe), 4), 8))
def cg_f073_earnings_multiples_core18_3rd_v019_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_diff(_safe_div(1.0, evebitda), 4), 8))
def cg_f073_earnings_multiples_core19_3rd_v020_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_diff(_safe_div(ebitda, ebit.abs() + 1.0), 4), 8))
def cg_f073_earnings_multiples_core20_3rd_v021_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(_slope(pe, 4), 4))
def cg_f073_earnings_multiples_core21_3rd_v022_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(_slope(pe1, 4), 4))
def cg_f073_earnings_multiples_core22_3rd_v023_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(_slope(evebit, 4), 4))
def cg_f073_earnings_multiples_core23_3rd_v024_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(_slope(evebitda, 4), 4))
def cg_f073_earnings_multiples_core24_3rd_v025_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(_slope(ebit, 4), 4))
def cg_f073_earnings_multiples_core25_3rd_v026_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(_slope(ebitda, 4), 4))
def cg_f073_earnings_multiples_core26_3rd_v027_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(_slope(_safe_div(ebitda, ebit), 4), 4))
def cg_f073_earnings_multiples_core27_3rd_v028_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(_slope(_safe_div(1.0, pe), 4), 4))
def cg_f073_earnings_multiples_core28_3rd_v029_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(_slope(_safe_div(1.0, evebitda), 4), 4))
def cg_f073_earnings_multiples_core29_3rd_v030_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(_slope(_safe_div(ebitda, ebit.abs() + 1.0), 4), 4))
def cg_f073_earnings_multiples_core30_3rd_v031_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_diff(_diff(pe, 4), 4), 8))
def cg_f073_earnings_multiples_core31_3rd_v032_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_diff(_diff(pe1, 4), 4), 8))
def cg_f073_earnings_multiples_core32_3rd_v033_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_diff(_diff(evebit, 4), 4), 8))
def cg_f073_earnings_multiples_core33_3rd_v034_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_diff(_diff(evebitda, 4), 4), 8))
def cg_f073_earnings_multiples_core34_3rd_v035_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_diff(_diff(ebit, 4), 4), 8))
def cg_f073_earnings_multiples_core35_3rd_v036_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_diff(_diff(ebitda, 4), 4), 8))
def cg_f073_earnings_multiples_core36_3rd_v037_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_diff(_diff(_safe_div(ebitda, ebit), 4), 4), 8))
def cg_f073_earnings_multiples_core37_3rd_v038_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_diff(_diff(_safe_div(1.0, pe), 4), 4), 8))
def cg_f073_earnings_multiples_core38_3rd_v039_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_diff(_diff(_safe_div(1.0, evebitda), 4), 4), 8))
def cg_f073_earnings_multiples_core39_3rd_v040_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_diff(_diff(_safe_div(ebitda, ebit.abs() + 1.0), 4), 4), 8))
def cg_f073_earnings_multiples_core40_3rd_v041_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_slope(_diff(pe, 4), 8), 12))
def cg_f073_earnings_multiples_core41_3rd_v042_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_slope(_diff(pe1, 4), 8), 12))
def cg_f073_earnings_multiples_core42_3rd_v043_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_slope(_diff(evebit, 4), 8), 12))
def cg_f073_earnings_multiples_core43_3rd_v044_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_slope(_diff(evebitda, 4), 8), 12))
def cg_f073_earnings_multiples_core44_3rd_v045_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_slope(_diff(ebit, 4), 8), 12))
def cg_f073_earnings_multiples_core45_3rd_v046_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_slope(_diff(ebitda, 4), 8), 12))
def cg_f073_earnings_multiples_core46_3rd_v047_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_slope(_diff(_safe_div(ebitda, ebit), 4), 8), 12))
def cg_f073_earnings_multiples_core47_3rd_v048_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_slope(_diff(_safe_div(1.0, pe), 4), 8), 12))
def cg_f073_earnings_multiples_core48_3rd_v049_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_slope(_diff(_safe_div(1.0, evebitda), 4), 8), 12))
def cg_f073_earnings_multiples_core49_3rd_v050_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_slope(_diff(_safe_div(ebitda, ebit.abs() + 1.0), 4), 8), 12))
def cg_f073_earnings_multiples_core50_3rd_v051_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_diff(_slope(pe, 4), 4), 8))
def cg_f073_earnings_multiples_core51_3rd_v052_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_diff(_slope(pe1, 4), 4), 8))
def cg_f073_earnings_multiples_core52_3rd_v053_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_diff(_slope(evebit, 4), 4), 8))
def cg_f073_earnings_multiples_core53_3rd_v054_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_diff(_slope(evebitda, 4), 4), 8))
def cg_f073_earnings_multiples_core54_3rd_v055_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_diff(_slope(ebit, 4), 4), 8))
def cg_f073_earnings_multiples_core55_3rd_v056_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_diff(_slope(ebitda, 4), 4), 8))
def cg_f073_earnings_multiples_core56_3rd_v057_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_diff(_slope(_safe_div(ebitda, ebit), 4), 4), 8))
def cg_f073_earnings_multiples_core57_3rd_v058_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_diff(_slope(_safe_div(1.0, pe), 4), 4), 8))
def cg_f073_earnings_multiples_core58_3rd_v059_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_diff(_slope(_safe_div(1.0, evebitda), 4), 4), 8))
def cg_f073_earnings_multiples_core59_3rd_v060_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_diff(_slope(_safe_div(ebitda, ebit.abs() + 1.0), 4), 4), 8))
def cg_f073_earnings_multiples_core60_3rd_v061_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_diff(_diff(pe, 4), 4), 12))
def cg_f073_earnings_multiples_core61_3rd_v062_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_diff(_diff(pe1, 4), 4), 12))
def cg_f073_earnings_multiples_core62_3rd_v063_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_diff(_diff(evebit, 4), 4), 12))
def cg_f073_earnings_multiples_core63_3rd_v064_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_diff(_diff(evebitda, 4), 4), 12))
def cg_f073_earnings_multiples_core64_3rd_v065_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_diff(_diff(ebit, 4), 4), 12))
def cg_f073_earnings_multiples_core65_3rd_v066_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_diff(_diff(ebitda, 4), 4), 12))
def cg_f073_earnings_multiples_core66_3rd_v067_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_diff(_diff(_safe_div(ebitda, ebit), 4), 4), 12))
def cg_f073_earnings_multiples_core67_3rd_v068_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_diff(_diff(_safe_div(1.0, pe), 4), 4), 12))
def cg_f073_earnings_multiples_core68_3rd_v069_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_diff(_diff(_safe_div(1.0, evebitda), 4), 4), 12))
def cg_f073_earnings_multiples_core69_3rd_v070_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_diff(_diff(_safe_div(ebitda, ebit.abs() + 1.0), 4), 4), 12))
def cg_f073_earnings_multiples_core70_3rd_v071_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_slope(_diff(pe, 4), 8), 12))
def cg_f073_earnings_multiples_core71_3rd_v072_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_slope(_diff(pe1, 4), 8), 12))
def cg_f073_earnings_multiples_core72_3rd_v073_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_slope(_diff(evebit, 4), 8), 12))
def cg_f073_earnings_multiples_core73_3rd_v074_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_slope(_diff(evebitda, 4), 8), 12))
def cg_f073_earnings_multiples_core74_3rd_v075_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_slope(_diff(ebit, 4), 8), 12))
def cg_f073_earnings_multiples_core75_3rd_v076_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_slope(_diff(ebitda, 4), 8), 12))
def cg_f073_earnings_multiples_core76_3rd_v077_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_slope(_diff(_safe_div(ebitda, ebit), 4), 8), 12))
def cg_f073_earnings_multiples_core77_3rd_v078_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_slope(_diff(_safe_div(1.0, pe), 4), 8), 12))
def cg_f073_earnings_multiples_core78_3rd_v079_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_slope(_diff(_safe_div(1.0, evebitda), 4), 8), 12))
def cg_f073_earnings_multiples_core79_3rd_v080_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_slope(_diff(_safe_div(ebitda, ebit.abs() + 1.0), 4), 8), 12))
def cg_f073_earnings_multiples_core80_3rd_v081_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_diff(_slope(pe, 4), 4), 12))
def cg_f073_earnings_multiples_core81_3rd_v082_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_diff(_slope(pe1, 4), 4), 12))
def cg_f073_earnings_multiples_core82_3rd_v083_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_diff(_slope(evebit, 4), 4), 12))
def cg_f073_earnings_multiples_core83_3rd_v084_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_diff(_slope(evebitda, 4), 4), 12))
def cg_f073_earnings_multiples_core84_3rd_v085_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_diff(_slope(ebit, 4), 4), 12))
def cg_f073_earnings_multiples_core85_3rd_v086_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_diff(_slope(ebitda, 4), 4), 12))
def cg_f073_earnings_multiples_core86_3rd_v087_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_diff(_slope(_safe_div(ebitda, ebit), 4), 4), 12))
def cg_f073_earnings_multiples_core87_3rd_v088_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_diff(_slope(_safe_div(1.0, pe), 4), 4), 12))
def cg_f073_earnings_multiples_core88_3rd_v089_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_diff(_slope(_safe_div(1.0, evebitda), 4), 4), 12))
def cg_f073_earnings_multiples_core89_3rd_v090_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_rank(_diff(_slope(_safe_div(ebitda, ebit.abs() + 1.0), 4), 4), 12))
def cg_f073_earnings_multiples_core90_3rd_v091_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_diff(_diff(pe, 4), 4), 4))
def cg_f073_earnings_multiples_core91_3rd_v092_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_diff(_diff(pe1, 4), 4), 4))
def cg_f073_earnings_multiples_core92_3rd_v093_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_diff(_diff(evebit, 4), 4), 4))
def cg_f073_earnings_multiples_core93_3rd_v094_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_diff(_diff(evebitda, 4), 4), 4))
def cg_f073_earnings_multiples_core94_3rd_v095_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_diff(_diff(ebit, 4), 4), 4))
def cg_f073_earnings_multiples_core95_3rd_v096_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_diff(_diff(ebitda, 4), 4), 4))
def cg_f073_earnings_multiples_core96_3rd_v097_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_diff(_diff(_safe_div(ebitda, ebit), 4), 4), 4))
def cg_f073_earnings_multiples_core97_3rd_v098_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_diff(_diff(_safe_div(1.0, pe), 4), 4), 4))
def cg_f073_earnings_multiples_core98_3rd_v099_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_diff(_diff(_safe_div(1.0, evebitda), 4), 4), 4))
def cg_f073_earnings_multiples_core99_3rd_v100_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_diff(_diff(_safe_div(ebitda, ebit.abs() + 1.0), 4), 4), 4))
def cg_f073_earnings_multiples_core100_3rd_v101_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_slope(_diff(pe, 4), 8), 4))
def cg_f073_earnings_multiples_core101_3rd_v102_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_slope(_diff(pe1, 4), 8), 4))
def cg_f073_earnings_multiples_core102_3rd_v103_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_slope(_diff(evebit, 4), 8), 4))
def cg_f073_earnings_multiples_core103_3rd_v104_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_slope(_diff(evebitda, 4), 8), 4))
def cg_f073_earnings_multiples_core104_3rd_v105_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_slope(_diff(ebit, 4), 8), 4))
def cg_f073_earnings_multiples_core105_3rd_v106_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_slope(_diff(ebitda, 4), 8), 4))
def cg_f073_earnings_multiples_core106_3rd_v107_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_slope(_diff(_safe_div(ebitda, ebit), 4), 8), 4))
def cg_f073_earnings_multiples_core107_3rd_v108_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_slope(_diff(_safe_div(1.0, pe), 4), 8), 4))
def cg_f073_earnings_multiples_core108_3rd_v109_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_slope(_diff(_safe_div(1.0, evebitda), 4), 8), 4))
def cg_f073_earnings_multiples_core109_3rd_v110_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_slope(_diff(_safe_div(ebitda, ebit.abs() + 1.0), 4), 8), 4))
def cg_f073_earnings_multiples_core110_3rd_v111_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_diff(_slope(pe, 4), 4), 4))
def cg_f073_earnings_multiples_core111_3rd_v112_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_diff(_slope(pe1, 4), 4), 4))
def cg_f073_earnings_multiples_core112_3rd_v113_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_diff(_slope(evebit, 4), 4), 4))
def cg_f073_earnings_multiples_core113_3rd_v114_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_diff(_slope(evebitda, 4), 4), 4))
def cg_f073_earnings_multiples_core114_3rd_v115_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_diff(_slope(ebit, 4), 4), 4))
def cg_f073_earnings_multiples_core115_3rd_v116_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_diff(_slope(ebitda, 4), 4), 4))
def cg_f073_earnings_multiples_core116_3rd_v117_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_diff(_slope(_safe_div(ebitda, ebit), 4), 4), 4))
def cg_f073_earnings_multiples_core117_3rd_v118_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_diff(_slope(_safe_div(1.0, pe), 4), 4), 4))
def cg_f073_earnings_multiples_core118_3rd_v119_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_diff(_slope(_safe_div(1.0, evebitda), 4), 4), 4))
def cg_f073_earnings_multiples_core119_3rd_v120_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_mean(_diff(_slope(_safe_div(ebitda, ebit.abs() + 1.0), 4), 4), 4))
def cg_f073_earnings_multiples_core120_3rd_v121_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_diff(_diff(pe, 4), 4), 4))
def cg_f073_earnings_multiples_core121_3rd_v122_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_diff(_diff(pe1, 4), 4), 4))
def cg_f073_earnings_multiples_core122_3rd_v123_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_diff(_diff(evebit, 4), 4), 4))
def cg_f073_earnings_multiples_core123_3rd_v124_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_diff(_diff(evebitda, 4), 4), 4))
def cg_f073_earnings_multiples_core124_3rd_v125_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_diff(_diff(ebit, 4), 4), 4))
def cg_f073_earnings_multiples_core125_3rd_v126_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_diff(_diff(ebitda, 4), 4), 4))
def cg_f073_earnings_multiples_core126_3rd_v127_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_diff(_diff(_safe_div(ebitda, ebit), 4), 4), 4))
def cg_f073_earnings_multiples_core127_3rd_v128_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_diff(_diff(_safe_div(1.0, pe), 4), 4), 4))
def cg_f073_earnings_multiples_core128_3rd_v129_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_diff(_diff(_safe_div(1.0, evebitda), 4), 4), 4))
def cg_f073_earnings_multiples_core129_3rd_v130_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_slope(_diff(_diff(_safe_div(ebitda, ebit.abs() + 1.0), 4), 4), 4))
def cg_f073_earnings_multiples_core130_3rd_v131_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(_diff(_diff(pe, 4), 4), 4))
def cg_f073_earnings_multiples_core131_3rd_v132_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(_diff(_diff(pe1, 4), 4), 4))
def cg_f073_earnings_multiples_core132_3rd_v133_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(_diff(_diff(evebit, 4), 4), 4))
def cg_f073_earnings_multiples_core133_3rd_v134_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(_diff(_diff(evebitda, 4), 4), 4))
def cg_f073_earnings_multiples_core134_3rd_v135_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(_diff(_diff(ebit, 4), 4), 4))
def cg_f073_earnings_multiples_core135_3rd_v136_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(_diff(_diff(ebitda, 4), 4), 4))
def cg_f073_earnings_multiples_core136_3rd_v137_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(_diff(_diff(_safe_div(ebitda, ebit), 4), 4), 4))
def cg_f073_earnings_multiples_core137_3rd_v138_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(_diff(_diff(_safe_div(1.0, pe), 4), 4), 4))
def cg_f073_earnings_multiples_core138_3rd_v139_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(_diff(_diff(_safe_div(1.0, evebitda), 4), 4), 4))
def cg_f073_earnings_multiples_core139_3rd_v140_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_diff(_diff(_diff(_safe_div(ebitda, ebit.abs() + 1.0), 4), 4), 4))
def cg_f073_earnings_multiples_core140_3rd_v141_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_slope(_diff(_diff(pe, 4), 4), 4), 8))
def cg_f073_earnings_multiples_core141_3rd_v142_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_slope(_diff(_diff(pe1, 4), 4), 4), 8))
def cg_f073_earnings_multiples_core142_3rd_v143_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_slope(_diff(_diff(evebit, 4), 4), 4), 8))
def cg_f073_earnings_multiples_core143_3rd_v144_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_slope(_diff(_diff(evebitda, 4), 4), 4), 8))
def cg_f073_earnings_multiples_core144_3rd_v145_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_slope(_diff(_diff(ebit, 4), 4), 4), 8))
def cg_f073_earnings_multiples_core145_3rd_v146_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_slope(_diff(_diff(ebitda, 4), 4), 4), 8))
def cg_f073_earnings_multiples_core146_3rd_v147_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_slope(_diff(_diff(_safe_div(ebitda, ebit), 4), 4), 4), 8))
def cg_f073_earnings_multiples_core147_3rd_v148_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_slope(_diff(_diff(_safe_div(1.0, pe), 4), 4), 4), 8))
def cg_f073_earnings_multiples_core148_3rd_v149_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_slope(_diff(_diff(_safe_div(1.0, evebitda), 4), 4), 4), 8))
def cg_f073_earnings_multiples_core149_3rd_v150_signal(pe, pe1, evebit, evebitda, ebit, ebitda):
    return _clean(_z(_slope(_diff(_diff(_safe_div(ebitda, ebit.abs() + 1.0), 4), 4), 4), 8))