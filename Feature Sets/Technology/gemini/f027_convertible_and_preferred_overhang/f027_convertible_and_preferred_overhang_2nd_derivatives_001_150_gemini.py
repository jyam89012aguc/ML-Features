import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f027_convertible_and_preferred_overhang_core00_2nd_v001_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(prefdivis, 4))
def cg_f027_convertible_and_preferred_overhang_core01_2nd_v002_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(prefdiv, 4))
def cg_f027_convertible_and_preferred_overhang_core02_2nd_v003_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(debt, 4))
def cg_f027_convertible_and_preferred_overhang_core03_2nd_v004_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_safe_div(prefdivis, equity.abs() + 1.0), 4))
def cg_f027_convertible_and_preferred_overhang_core04_2nd_v005_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_safe_div(prefdiv, equity.abs() + 1.0), 4))
def cg_f027_convertible_and_preferred_overhang_core05_2nd_v006_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_safe_div(debt, equity.abs() + 1.0), 4))
def cg_f027_convertible_and_preferred_overhang_core06_2nd_v007_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_safe_div(prefdivis, debt.abs() + 1.0), 4))
def cg_f027_convertible_and_preferred_overhang_core07_2nd_v008_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_safe_div(prefdiv, debt.abs() + 1.0), 4))
def cg_f027_convertible_and_preferred_overhang_core08_2nd_v009_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(prefdivis + prefdiv, 4))
def cg_f027_convertible_and_preferred_overhang_core09_2nd_v010_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_safe_div(prefdivis + prefdiv, equity.abs() + 1.0), 4))
def cg_f027_convertible_and_preferred_overhang_core10_2nd_v011_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(prefdivis, 8))
def cg_f027_convertible_and_preferred_overhang_core11_2nd_v012_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(prefdiv, 8))
def cg_f027_convertible_and_preferred_overhang_core12_2nd_v013_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(debt, 8))
def cg_f027_convertible_and_preferred_overhang_core13_2nd_v014_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_safe_div(prefdivis, equity.abs() + 1.0), 8))
def cg_f027_convertible_and_preferred_overhang_core14_2nd_v015_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_safe_div(prefdiv, equity.abs() + 1.0), 8))
def cg_f027_convertible_and_preferred_overhang_core15_2nd_v016_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_safe_div(debt, equity.abs() + 1.0), 8))
def cg_f027_convertible_and_preferred_overhang_core16_2nd_v017_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_safe_div(prefdivis, debt.abs() + 1.0), 8))
def cg_f027_convertible_and_preferred_overhang_core17_2nd_v018_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_safe_div(prefdiv, debt.abs() + 1.0), 8))
def cg_f027_convertible_and_preferred_overhang_core18_2nd_v019_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(prefdivis + prefdiv, 8))
def cg_f027_convertible_and_preferred_overhang_core19_2nd_v020_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_safe_div(prefdivis + prefdiv, equity.abs() + 1.0), 8))
def cg_f027_convertible_and_preferred_overhang_core20_2nd_v021_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(prefdivis, 4))
def cg_f027_convertible_and_preferred_overhang_core21_2nd_v022_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(prefdiv, 4))
def cg_f027_convertible_and_preferred_overhang_core22_2nd_v023_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(debt, 4))
def cg_f027_convertible_and_preferred_overhang_core23_2nd_v024_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_safe_div(prefdivis, equity.abs() + 1.0), 4))
def cg_f027_convertible_and_preferred_overhang_core24_2nd_v025_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_safe_div(prefdiv, equity.abs() + 1.0), 4))
def cg_f027_convertible_and_preferred_overhang_core25_2nd_v026_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_safe_div(debt, equity.abs() + 1.0), 4))
def cg_f027_convertible_and_preferred_overhang_core26_2nd_v027_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_safe_div(prefdivis, debt.abs() + 1.0), 4))
def cg_f027_convertible_and_preferred_overhang_core27_2nd_v028_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_safe_div(prefdiv, debt.abs() + 1.0), 4))
def cg_f027_convertible_and_preferred_overhang_core28_2nd_v029_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(prefdivis + prefdiv, 4))
def cg_f027_convertible_and_preferred_overhang_core29_2nd_v030_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_safe_div(prefdivis + prefdiv, equity.abs() + 1.0), 4))
def cg_f027_convertible_and_preferred_overhang_core30_2nd_v031_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_slope(prefdivis, 4), 8))
def cg_f027_convertible_and_preferred_overhang_core31_2nd_v032_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_slope(prefdiv, 4), 8))
def cg_f027_convertible_and_preferred_overhang_core32_2nd_v033_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_slope(debt, 4), 8))
def cg_f027_convertible_and_preferred_overhang_core33_2nd_v034_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_slope(_safe_div(prefdivis, equity.abs() + 1.0), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core34_2nd_v035_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_slope(_safe_div(prefdiv, equity.abs() + 1.0), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core35_2nd_v036_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_slope(_safe_div(debt, equity.abs() + 1.0), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core36_2nd_v037_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_slope(_safe_div(prefdivis, debt.abs() + 1.0), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core37_2nd_v038_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_slope(_safe_div(prefdiv, debt.abs() + 1.0), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core38_2nd_v039_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_slope(prefdivis + prefdiv, 4), 8))
def cg_f027_convertible_and_preferred_overhang_core39_2nd_v040_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_slope(_safe_div(prefdivis + prefdiv, equity.abs() + 1.0), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core40_2nd_v041_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_slope(prefdivis, 8), 12))
def cg_f027_convertible_and_preferred_overhang_core41_2nd_v042_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_slope(prefdiv, 8), 12))
def cg_f027_convertible_and_preferred_overhang_core42_2nd_v043_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_slope(debt, 8), 12))
def cg_f027_convertible_and_preferred_overhang_core43_2nd_v044_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_slope(_safe_div(prefdivis, equity.abs() + 1.0), 8), 12))
def cg_f027_convertible_and_preferred_overhang_core44_2nd_v045_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_slope(_safe_div(prefdiv, equity.abs() + 1.0), 8), 12))
def cg_f027_convertible_and_preferred_overhang_core45_2nd_v046_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_slope(_safe_div(debt, equity.abs() + 1.0), 8), 12))
def cg_f027_convertible_and_preferred_overhang_core46_2nd_v047_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_slope(_safe_div(prefdivis, debt.abs() + 1.0), 8), 12))
def cg_f027_convertible_and_preferred_overhang_core47_2nd_v048_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_slope(_safe_div(prefdiv, debt.abs() + 1.0), 8), 12))
def cg_f027_convertible_and_preferred_overhang_core48_2nd_v049_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_slope(prefdivis + prefdiv, 8), 12))
def cg_f027_convertible_and_preferred_overhang_core49_2nd_v050_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_slope(_safe_div(prefdivis + prefdiv, equity.abs() + 1.0), 8), 12))
def cg_f027_convertible_and_preferred_overhang_core50_2nd_v051_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_diff(prefdivis, 4), 8))
def cg_f027_convertible_and_preferred_overhang_core51_2nd_v052_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_diff(prefdiv, 4), 8))
def cg_f027_convertible_and_preferred_overhang_core52_2nd_v053_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_diff(debt, 4), 8))
def cg_f027_convertible_and_preferred_overhang_core53_2nd_v054_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_diff(_safe_div(prefdivis, equity.abs() + 1.0), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core54_2nd_v055_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_diff(_safe_div(prefdiv, equity.abs() + 1.0), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core55_2nd_v056_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_diff(_safe_div(debt, equity.abs() + 1.0), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core56_2nd_v057_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_diff(_safe_div(prefdivis, debt.abs() + 1.0), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core57_2nd_v058_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_diff(_safe_div(prefdiv, debt.abs() + 1.0), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core58_2nd_v059_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_diff(prefdivis + prefdiv, 4), 8))
def cg_f027_convertible_and_preferred_overhang_core59_2nd_v060_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_diff(_safe_div(prefdivis + prefdiv, equity.abs() + 1.0), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core60_2nd_v061_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_slope(prefdivis, 4), 12))
def cg_f027_convertible_and_preferred_overhang_core61_2nd_v062_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_slope(prefdiv, 4), 12))
def cg_f027_convertible_and_preferred_overhang_core62_2nd_v063_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_slope(debt, 4), 12))
def cg_f027_convertible_and_preferred_overhang_core63_2nd_v064_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_slope(_safe_div(prefdivis, equity.abs() + 1.0), 4), 12))
def cg_f027_convertible_and_preferred_overhang_core64_2nd_v065_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_slope(_safe_div(prefdiv, equity.abs() + 1.0), 4), 12))
def cg_f027_convertible_and_preferred_overhang_core65_2nd_v066_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_slope(_safe_div(debt, equity.abs() + 1.0), 4), 12))
def cg_f027_convertible_and_preferred_overhang_core66_2nd_v067_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_slope(_safe_div(prefdivis, debt.abs() + 1.0), 4), 12))
def cg_f027_convertible_and_preferred_overhang_core67_2nd_v068_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_slope(_safe_div(prefdiv, debt.abs() + 1.0), 4), 12))
def cg_f027_convertible_and_preferred_overhang_core68_2nd_v069_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_slope(prefdivis + prefdiv, 4), 12))
def cg_f027_convertible_and_preferred_overhang_core69_2nd_v070_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_slope(_safe_div(prefdivis + prefdiv, equity.abs() + 1.0), 4), 12))
def cg_f027_convertible_and_preferred_overhang_core70_2nd_v071_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_diff(prefdivis, 4), 12))
def cg_f027_convertible_and_preferred_overhang_core71_2nd_v072_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_diff(prefdiv, 4), 12))
def cg_f027_convertible_and_preferred_overhang_core72_2nd_v073_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_diff(debt, 4), 12))
def cg_f027_convertible_and_preferred_overhang_core73_2nd_v074_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_diff(_safe_div(prefdivis, equity.abs() + 1.0), 4), 12))
def cg_f027_convertible_and_preferred_overhang_core74_2nd_v075_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_diff(_safe_div(prefdiv, equity.abs() + 1.0), 4), 12))
def cg_f027_convertible_and_preferred_overhang_core75_2nd_v076_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_diff(_safe_div(debt, equity.abs() + 1.0), 4), 12))
def cg_f027_convertible_and_preferred_overhang_core76_2nd_v077_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_diff(_safe_div(prefdivis, debt.abs() + 1.0), 4), 12))
def cg_f027_convertible_and_preferred_overhang_core77_2nd_v078_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_diff(_safe_div(prefdiv, debt.abs() + 1.0), 4), 12))
def cg_f027_convertible_and_preferred_overhang_core78_2nd_v079_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_diff(prefdivis + prefdiv, 4), 12))
def cg_f027_convertible_and_preferred_overhang_core79_2nd_v080_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_diff(_safe_div(prefdivis + prefdiv, equity.abs() + 1.0), 4), 12))
def cg_f027_convertible_and_preferred_overhang_core80_2nd_v081_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_slope(prefdivis, 4), 4))
def cg_f027_convertible_and_preferred_overhang_core81_2nd_v082_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_slope(prefdiv, 4), 4))
def cg_f027_convertible_and_preferred_overhang_core82_2nd_v083_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_slope(debt, 4), 4))
def cg_f027_convertible_and_preferred_overhang_core83_2nd_v084_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_slope(_safe_div(prefdivis, equity.abs() + 1.0), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core84_2nd_v085_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_slope(_safe_div(prefdiv, equity.abs() + 1.0), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core85_2nd_v086_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_slope(_safe_div(debt, equity.abs() + 1.0), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core86_2nd_v087_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_slope(_safe_div(prefdivis, debt.abs() + 1.0), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core87_2nd_v088_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_slope(_safe_div(prefdiv, debt.abs() + 1.0), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core88_2nd_v089_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_slope(prefdivis + prefdiv, 4), 4))
def cg_f027_convertible_and_preferred_overhang_core89_2nd_v090_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_slope(_safe_div(prefdivis + prefdiv, equity.abs() + 1.0), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core90_2nd_v091_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_diff(prefdivis, 4), 4))
def cg_f027_convertible_and_preferred_overhang_core91_2nd_v092_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_diff(prefdiv, 4), 4))
def cg_f027_convertible_and_preferred_overhang_core92_2nd_v093_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_diff(debt, 4), 4))
def cg_f027_convertible_and_preferred_overhang_core93_2nd_v094_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_diff(_safe_div(prefdivis, equity.abs() + 1.0), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core94_2nd_v095_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_diff(_safe_div(prefdiv, equity.abs() + 1.0), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core95_2nd_v096_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_diff(_safe_div(debt, equity.abs() + 1.0), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core96_2nd_v097_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_diff(_safe_div(prefdivis, debt.abs() + 1.0), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core97_2nd_v098_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_diff(_safe_div(prefdiv, debt.abs() + 1.0), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core98_2nd_v099_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_diff(prefdivis + prefdiv, 4), 4))
def cg_f027_convertible_and_preferred_overhang_core99_2nd_v100_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_diff(_safe_div(prefdivis + prefdiv, equity.abs() + 1.0), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core100_2nd_v101_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_mean(prefdivis, 4), 4))
def cg_f027_convertible_and_preferred_overhang_core101_2nd_v102_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_mean(prefdiv, 4), 4))
def cg_f027_convertible_and_preferred_overhang_core102_2nd_v103_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_mean(debt, 4), 4))
def cg_f027_convertible_and_preferred_overhang_core103_2nd_v104_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_mean(_safe_div(prefdivis, equity.abs() + 1.0), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core104_2nd_v105_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_mean(_safe_div(prefdiv, equity.abs() + 1.0), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core105_2nd_v106_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_mean(_safe_div(debt, equity.abs() + 1.0), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core106_2nd_v107_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_mean(_safe_div(prefdivis, debt.abs() + 1.0), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core107_2nd_v108_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_mean(_safe_div(prefdiv, debt.abs() + 1.0), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core108_2nd_v109_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_mean(prefdivis + prefdiv, 4), 4))
def cg_f027_convertible_and_preferred_overhang_core109_2nd_v110_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_mean(_safe_div(prefdivis + prefdiv, equity.abs() + 1.0), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core110_2nd_v111_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_mean(prefdivis, 8), 8))
def cg_f027_convertible_and_preferred_overhang_core111_2nd_v112_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_mean(prefdiv, 8), 8))
def cg_f027_convertible_and_preferred_overhang_core112_2nd_v113_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_mean(debt, 8), 8))
def cg_f027_convertible_and_preferred_overhang_core113_2nd_v114_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_mean(_safe_div(prefdivis, equity.abs() + 1.0), 8), 8))
def cg_f027_convertible_and_preferred_overhang_core114_2nd_v115_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_mean(_safe_div(prefdiv, equity.abs() + 1.0), 8), 8))
def cg_f027_convertible_and_preferred_overhang_core115_2nd_v116_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_mean(_safe_div(debt, equity.abs() + 1.0), 8), 8))
def cg_f027_convertible_and_preferred_overhang_core116_2nd_v117_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_mean(_safe_div(prefdivis, debt.abs() + 1.0), 8), 8))
def cg_f027_convertible_and_preferred_overhang_core117_2nd_v118_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_mean(_safe_div(prefdiv, debt.abs() + 1.0), 8), 8))
def cg_f027_convertible_and_preferred_overhang_core118_2nd_v119_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_mean(prefdivis + prefdiv, 8), 8))
def cg_f027_convertible_and_preferred_overhang_core119_2nd_v120_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_mean(_safe_div(prefdivis + prefdiv, equity.abs() + 1.0), 8), 8))
def cg_f027_convertible_and_preferred_overhang_core120_2nd_v121_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_mean(prefdivis, 4), 4))
def cg_f027_convertible_and_preferred_overhang_core121_2nd_v122_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_mean(prefdiv, 4), 4))
def cg_f027_convertible_and_preferred_overhang_core122_2nd_v123_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_mean(debt, 4), 4))
def cg_f027_convertible_and_preferred_overhang_core123_2nd_v124_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_mean(_safe_div(prefdivis, equity.abs() + 1.0), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core124_2nd_v125_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_mean(_safe_div(prefdiv, equity.abs() + 1.0), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core125_2nd_v126_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_mean(_safe_div(debt, equity.abs() + 1.0), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core126_2nd_v127_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_mean(_safe_div(prefdivis, debt.abs() + 1.0), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core127_2nd_v128_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_mean(_safe_div(prefdiv, debt.abs() + 1.0), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core128_2nd_v129_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_mean(prefdivis + prefdiv, 4), 4))
def cg_f027_convertible_and_preferred_overhang_core129_2nd_v130_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_mean(_safe_div(prefdivis + prefdiv, equity.abs() + 1.0), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core130_2nd_v131_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_diff(_mean(prefdivis, 4), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core131_2nd_v132_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_diff(_mean(prefdiv, 4), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core132_2nd_v133_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_diff(_mean(debt, 4), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core133_2nd_v134_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_diff(_mean(_safe_div(prefdivis, equity.abs() + 1.0), 4), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core134_2nd_v135_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_diff(_mean(_safe_div(prefdiv, equity.abs() + 1.0), 4), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core135_2nd_v136_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_diff(_mean(_safe_div(debt, equity.abs() + 1.0), 4), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core136_2nd_v137_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_diff(_mean(_safe_div(prefdivis, debt.abs() + 1.0), 4), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core137_2nd_v138_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_diff(_mean(_safe_div(prefdiv, debt.abs() + 1.0), 4), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core138_2nd_v139_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_diff(_mean(prefdivis + prefdiv, 4), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core139_2nd_v140_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_diff(_mean(_safe_div(prefdivis + prefdiv, equity.abs() + 1.0), 4), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core140_2nd_v141_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_slope(_mean(prefdivis, 4), 4), 12))
def cg_f027_convertible_and_preferred_overhang_core141_2nd_v142_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_slope(_mean(prefdiv, 4), 4), 12))
def cg_f027_convertible_and_preferred_overhang_core142_2nd_v143_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_slope(_mean(debt, 4), 4), 12))
def cg_f027_convertible_and_preferred_overhang_core143_2nd_v144_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_slope(_mean(_safe_div(prefdivis, equity.abs() + 1.0), 4), 4), 12))
def cg_f027_convertible_and_preferred_overhang_core144_2nd_v145_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_slope(_mean(_safe_div(prefdiv, equity.abs() + 1.0), 4), 4), 12))
def cg_f027_convertible_and_preferred_overhang_core145_2nd_v146_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_slope(_mean(_safe_div(debt, equity.abs() + 1.0), 4), 4), 12))
def cg_f027_convertible_and_preferred_overhang_core146_2nd_v147_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_slope(_mean(_safe_div(prefdivis, debt.abs() + 1.0), 4), 4), 12))
def cg_f027_convertible_and_preferred_overhang_core147_2nd_v148_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_slope(_mean(_safe_div(prefdiv, debt.abs() + 1.0), 4), 4), 12))
def cg_f027_convertible_and_preferred_overhang_core148_2nd_v149_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_slope(_mean(prefdivis + prefdiv, 4), 4), 12))
def cg_f027_convertible_and_preferred_overhang_core149_2nd_v150_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_slope(_mean(_safe_div(prefdivis + prefdiv, equity.abs() + 1.0), 4), 4), 12))