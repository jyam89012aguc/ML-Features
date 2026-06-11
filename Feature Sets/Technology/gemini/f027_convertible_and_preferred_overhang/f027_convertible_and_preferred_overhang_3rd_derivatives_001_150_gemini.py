import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f027_convertible_and_preferred_overhang_core00_3rd_v001_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_diff(prefdivis, 4), 4))
def cg_f027_convertible_and_preferred_overhang_core01_3rd_v002_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_diff(prefdiv, 4), 4))
def cg_f027_convertible_and_preferred_overhang_core02_3rd_v003_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_diff(debt, 4), 4))
def cg_f027_convertible_and_preferred_overhang_core03_3rd_v004_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_diff(_safe_div(prefdivis, equity.abs() + 1.0), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core04_3rd_v005_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_diff(_safe_div(prefdiv, equity.abs() + 1.0), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core05_3rd_v006_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_diff(_safe_div(debt, equity.abs() + 1.0), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core06_3rd_v007_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_diff(_safe_div(prefdivis, debt.abs() + 1.0), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core07_3rd_v008_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_diff(_safe_div(prefdiv, debt.abs() + 1.0), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core08_3rd_v009_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_diff(prefdivis + prefdiv, 4), 4))
def cg_f027_convertible_and_preferred_overhang_core09_3rd_v010_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_diff(_safe_div(prefdivis + prefdiv, equity.abs() + 1.0), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core10_3rd_v011_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_diff(prefdivis, 4), 8))
def cg_f027_convertible_and_preferred_overhang_core11_3rd_v012_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_diff(prefdiv, 4), 8))
def cg_f027_convertible_and_preferred_overhang_core12_3rd_v013_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_diff(debt, 4), 8))
def cg_f027_convertible_and_preferred_overhang_core13_3rd_v014_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_diff(_safe_div(prefdivis, equity.abs() + 1.0), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core14_3rd_v015_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_diff(_safe_div(prefdiv, equity.abs() + 1.0), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core15_3rd_v016_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_diff(_safe_div(debt, equity.abs() + 1.0), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core16_3rd_v017_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_diff(_safe_div(prefdivis, debt.abs() + 1.0), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core17_3rd_v018_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_diff(_safe_div(prefdiv, debt.abs() + 1.0), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core18_3rd_v019_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_diff(prefdivis + prefdiv, 4), 8))
def cg_f027_convertible_and_preferred_overhang_core19_3rd_v020_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_diff(_safe_div(prefdivis + prefdiv, equity.abs() + 1.0), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core20_3rd_v021_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_slope(prefdivis, 4), 4))
def cg_f027_convertible_and_preferred_overhang_core21_3rd_v022_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_slope(prefdiv, 4), 4))
def cg_f027_convertible_and_preferred_overhang_core22_3rd_v023_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_slope(debt, 4), 4))
def cg_f027_convertible_and_preferred_overhang_core23_3rd_v024_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_slope(_safe_div(prefdivis, equity.abs() + 1.0), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core24_3rd_v025_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_slope(_safe_div(prefdiv, equity.abs() + 1.0), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core25_3rd_v026_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_slope(_safe_div(debt, equity.abs() + 1.0), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core26_3rd_v027_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_slope(_safe_div(prefdivis, debt.abs() + 1.0), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core27_3rd_v028_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_slope(_safe_div(prefdiv, debt.abs() + 1.0), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core28_3rd_v029_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_slope(prefdivis + prefdiv, 4), 4))
def cg_f027_convertible_and_preferred_overhang_core29_3rd_v030_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_slope(_safe_div(prefdivis + prefdiv, equity.abs() + 1.0), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core30_3rd_v031_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_diff(_diff(prefdivis, 4), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core31_3rd_v032_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_diff(_diff(prefdiv, 4), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core32_3rd_v033_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_diff(_diff(debt, 4), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core33_3rd_v034_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_diff(_diff(_safe_div(prefdivis, equity.abs() + 1.0), 4), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core34_3rd_v035_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_diff(_diff(_safe_div(prefdiv, equity.abs() + 1.0), 4), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core35_3rd_v036_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_diff(_diff(_safe_div(debt, equity.abs() + 1.0), 4), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core36_3rd_v037_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_diff(_diff(_safe_div(prefdivis, debt.abs() + 1.0), 4), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core37_3rd_v038_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_diff(_diff(_safe_div(prefdiv, debt.abs() + 1.0), 4), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core38_3rd_v039_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_diff(_diff(prefdivis + prefdiv, 4), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core39_3rd_v040_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_diff(_diff(_safe_div(prefdivis + prefdiv, equity.abs() + 1.0), 4), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core40_3rd_v041_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_slope(_diff(prefdivis, 4), 8), 12))
def cg_f027_convertible_and_preferred_overhang_core41_3rd_v042_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_slope(_diff(prefdiv, 4), 8), 12))
def cg_f027_convertible_and_preferred_overhang_core42_3rd_v043_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_slope(_diff(debt, 4), 8), 12))
def cg_f027_convertible_and_preferred_overhang_core43_3rd_v044_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_slope(_diff(_safe_div(prefdivis, equity.abs() + 1.0), 4), 8), 12))
def cg_f027_convertible_and_preferred_overhang_core44_3rd_v045_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_slope(_diff(_safe_div(prefdiv, equity.abs() + 1.0), 4), 8), 12))
def cg_f027_convertible_and_preferred_overhang_core45_3rd_v046_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_slope(_diff(_safe_div(debt, equity.abs() + 1.0), 4), 8), 12))
def cg_f027_convertible_and_preferred_overhang_core46_3rd_v047_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_slope(_diff(_safe_div(prefdivis, debt.abs() + 1.0), 4), 8), 12))
def cg_f027_convertible_and_preferred_overhang_core47_3rd_v048_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_slope(_diff(_safe_div(prefdiv, debt.abs() + 1.0), 4), 8), 12))
def cg_f027_convertible_and_preferred_overhang_core48_3rd_v049_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_slope(_diff(prefdivis + prefdiv, 4), 8), 12))
def cg_f027_convertible_and_preferred_overhang_core49_3rd_v050_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_slope(_diff(_safe_div(prefdivis + prefdiv, equity.abs() + 1.0), 4), 8), 12))
def cg_f027_convertible_and_preferred_overhang_core50_3rd_v051_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_diff(_slope(prefdivis, 4), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core51_3rd_v052_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_diff(_slope(prefdiv, 4), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core52_3rd_v053_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_diff(_slope(debt, 4), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core53_3rd_v054_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_diff(_slope(_safe_div(prefdivis, equity.abs() + 1.0), 4), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core54_3rd_v055_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_diff(_slope(_safe_div(prefdiv, equity.abs() + 1.0), 4), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core55_3rd_v056_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_diff(_slope(_safe_div(debt, equity.abs() + 1.0), 4), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core56_3rd_v057_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_diff(_slope(_safe_div(prefdivis, debt.abs() + 1.0), 4), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core57_3rd_v058_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_diff(_slope(_safe_div(prefdiv, debt.abs() + 1.0), 4), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core58_3rd_v059_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_diff(_slope(prefdivis + prefdiv, 4), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core59_3rd_v060_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_diff(_slope(_safe_div(prefdivis + prefdiv, equity.abs() + 1.0), 4), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core60_3rd_v061_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_diff(_diff(prefdivis, 4), 4), 12))
def cg_f027_convertible_and_preferred_overhang_core61_3rd_v062_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_diff(_diff(prefdiv, 4), 4), 12))
def cg_f027_convertible_and_preferred_overhang_core62_3rd_v063_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_diff(_diff(debt, 4), 4), 12))
def cg_f027_convertible_and_preferred_overhang_core63_3rd_v064_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_diff(_diff(_safe_div(prefdivis, equity.abs() + 1.0), 4), 4), 12))
def cg_f027_convertible_and_preferred_overhang_core64_3rd_v065_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_diff(_diff(_safe_div(prefdiv, equity.abs() + 1.0), 4), 4), 12))
def cg_f027_convertible_and_preferred_overhang_core65_3rd_v066_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_diff(_diff(_safe_div(debt, equity.abs() + 1.0), 4), 4), 12))
def cg_f027_convertible_and_preferred_overhang_core66_3rd_v067_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_diff(_diff(_safe_div(prefdivis, debt.abs() + 1.0), 4), 4), 12))
def cg_f027_convertible_and_preferred_overhang_core67_3rd_v068_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_diff(_diff(_safe_div(prefdiv, debt.abs() + 1.0), 4), 4), 12))
def cg_f027_convertible_and_preferred_overhang_core68_3rd_v069_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_diff(_diff(prefdivis + prefdiv, 4), 4), 12))
def cg_f027_convertible_and_preferred_overhang_core69_3rd_v070_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_diff(_diff(_safe_div(prefdivis + prefdiv, equity.abs() + 1.0), 4), 4), 12))
def cg_f027_convertible_and_preferred_overhang_core70_3rd_v071_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_slope(_diff(prefdivis, 4), 8), 12))
def cg_f027_convertible_and_preferred_overhang_core71_3rd_v072_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_slope(_diff(prefdiv, 4), 8), 12))
def cg_f027_convertible_and_preferred_overhang_core72_3rd_v073_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_slope(_diff(debt, 4), 8), 12))
def cg_f027_convertible_and_preferred_overhang_core73_3rd_v074_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_slope(_diff(_safe_div(prefdivis, equity.abs() + 1.0), 4), 8), 12))
def cg_f027_convertible_and_preferred_overhang_core74_3rd_v075_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_slope(_diff(_safe_div(prefdiv, equity.abs() + 1.0), 4), 8), 12))
def cg_f027_convertible_and_preferred_overhang_core75_3rd_v076_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_slope(_diff(_safe_div(debt, equity.abs() + 1.0), 4), 8), 12))
def cg_f027_convertible_and_preferred_overhang_core76_3rd_v077_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_slope(_diff(_safe_div(prefdivis, debt.abs() + 1.0), 4), 8), 12))
def cg_f027_convertible_and_preferred_overhang_core77_3rd_v078_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_slope(_diff(_safe_div(prefdiv, debt.abs() + 1.0), 4), 8), 12))
def cg_f027_convertible_and_preferred_overhang_core78_3rd_v079_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_slope(_diff(prefdivis + prefdiv, 4), 8), 12))
def cg_f027_convertible_and_preferred_overhang_core79_3rd_v080_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_slope(_diff(_safe_div(prefdivis + prefdiv, equity.abs() + 1.0), 4), 8), 12))
def cg_f027_convertible_and_preferred_overhang_core80_3rd_v081_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_diff(_slope(prefdivis, 4), 4), 12))
def cg_f027_convertible_and_preferred_overhang_core81_3rd_v082_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_diff(_slope(prefdiv, 4), 4), 12))
def cg_f027_convertible_and_preferred_overhang_core82_3rd_v083_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_diff(_slope(debt, 4), 4), 12))
def cg_f027_convertible_and_preferred_overhang_core83_3rd_v084_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_diff(_slope(_safe_div(prefdivis, equity.abs() + 1.0), 4), 4), 12))
def cg_f027_convertible_and_preferred_overhang_core84_3rd_v085_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_diff(_slope(_safe_div(prefdiv, equity.abs() + 1.0), 4), 4), 12))
def cg_f027_convertible_and_preferred_overhang_core85_3rd_v086_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_diff(_slope(_safe_div(debt, equity.abs() + 1.0), 4), 4), 12))
def cg_f027_convertible_and_preferred_overhang_core86_3rd_v087_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_diff(_slope(_safe_div(prefdivis, debt.abs() + 1.0), 4), 4), 12))
def cg_f027_convertible_and_preferred_overhang_core87_3rd_v088_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_diff(_slope(_safe_div(prefdiv, debt.abs() + 1.0), 4), 4), 12))
def cg_f027_convertible_and_preferred_overhang_core88_3rd_v089_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_diff(_slope(prefdivis + prefdiv, 4), 4), 12))
def cg_f027_convertible_and_preferred_overhang_core89_3rd_v090_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_rank(_diff(_slope(_safe_div(prefdivis + prefdiv, equity.abs() + 1.0), 4), 4), 12))
def cg_f027_convertible_and_preferred_overhang_core90_3rd_v091_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_diff(_diff(prefdivis, 4), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core91_3rd_v092_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_diff(_diff(prefdiv, 4), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core92_3rd_v093_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_diff(_diff(debt, 4), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core93_3rd_v094_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_diff(_diff(_safe_div(prefdivis, equity.abs() + 1.0), 4), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core94_3rd_v095_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_diff(_diff(_safe_div(prefdiv, equity.abs() + 1.0), 4), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core95_3rd_v096_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_diff(_diff(_safe_div(debt, equity.abs() + 1.0), 4), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core96_3rd_v097_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_diff(_diff(_safe_div(prefdivis, debt.abs() + 1.0), 4), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core97_3rd_v098_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_diff(_diff(_safe_div(prefdiv, debt.abs() + 1.0), 4), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core98_3rd_v099_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_diff(_diff(prefdivis + prefdiv, 4), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core99_3rd_v100_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_diff(_diff(_safe_div(prefdivis + prefdiv, equity.abs() + 1.0), 4), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core100_3rd_v101_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_slope(_diff(prefdivis, 4), 8), 4))
def cg_f027_convertible_and_preferred_overhang_core101_3rd_v102_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_slope(_diff(prefdiv, 4), 8), 4))
def cg_f027_convertible_and_preferred_overhang_core102_3rd_v103_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_slope(_diff(debt, 4), 8), 4))
def cg_f027_convertible_and_preferred_overhang_core103_3rd_v104_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_slope(_diff(_safe_div(prefdivis, equity.abs() + 1.0), 4), 8), 4))
def cg_f027_convertible_and_preferred_overhang_core104_3rd_v105_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_slope(_diff(_safe_div(prefdiv, equity.abs() + 1.0), 4), 8), 4))
def cg_f027_convertible_and_preferred_overhang_core105_3rd_v106_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_slope(_diff(_safe_div(debt, equity.abs() + 1.0), 4), 8), 4))
def cg_f027_convertible_and_preferred_overhang_core106_3rd_v107_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_slope(_diff(_safe_div(prefdivis, debt.abs() + 1.0), 4), 8), 4))
def cg_f027_convertible_and_preferred_overhang_core107_3rd_v108_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_slope(_diff(_safe_div(prefdiv, debt.abs() + 1.0), 4), 8), 4))
def cg_f027_convertible_and_preferred_overhang_core108_3rd_v109_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_slope(_diff(prefdivis + prefdiv, 4), 8), 4))
def cg_f027_convertible_and_preferred_overhang_core109_3rd_v110_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_slope(_diff(_safe_div(prefdivis + prefdiv, equity.abs() + 1.0), 4), 8), 4))
def cg_f027_convertible_and_preferred_overhang_core110_3rd_v111_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_diff(_slope(prefdivis, 4), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core111_3rd_v112_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_diff(_slope(prefdiv, 4), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core112_3rd_v113_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_diff(_slope(debt, 4), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core113_3rd_v114_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_diff(_slope(_safe_div(prefdivis, equity.abs() + 1.0), 4), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core114_3rd_v115_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_diff(_slope(_safe_div(prefdiv, equity.abs() + 1.0), 4), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core115_3rd_v116_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_diff(_slope(_safe_div(debt, equity.abs() + 1.0), 4), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core116_3rd_v117_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_diff(_slope(_safe_div(prefdivis, debt.abs() + 1.0), 4), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core117_3rd_v118_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_diff(_slope(_safe_div(prefdiv, debt.abs() + 1.0), 4), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core118_3rd_v119_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_diff(_slope(prefdivis + prefdiv, 4), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core119_3rd_v120_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_mean(_diff(_slope(_safe_div(prefdivis + prefdiv, equity.abs() + 1.0), 4), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core120_3rd_v121_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_diff(_diff(prefdivis, 4), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core121_3rd_v122_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_diff(_diff(prefdiv, 4), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core122_3rd_v123_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_diff(_diff(debt, 4), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core123_3rd_v124_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_diff(_diff(_safe_div(prefdivis, equity.abs() + 1.0), 4), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core124_3rd_v125_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_diff(_diff(_safe_div(prefdiv, equity.abs() + 1.0), 4), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core125_3rd_v126_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_diff(_diff(_safe_div(debt, equity.abs() + 1.0), 4), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core126_3rd_v127_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_diff(_diff(_safe_div(prefdivis, debt.abs() + 1.0), 4), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core127_3rd_v128_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_diff(_diff(_safe_div(prefdiv, debt.abs() + 1.0), 4), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core128_3rd_v129_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_diff(_diff(prefdivis + prefdiv, 4), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core129_3rd_v130_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_slope(_diff(_diff(_safe_div(prefdivis + prefdiv, equity.abs() + 1.0), 4), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core130_3rd_v131_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_diff(_diff(prefdivis, 4), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core131_3rd_v132_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_diff(_diff(prefdiv, 4), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core132_3rd_v133_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_diff(_diff(debt, 4), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core133_3rd_v134_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_diff(_diff(_safe_div(prefdivis, equity.abs() + 1.0), 4), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core134_3rd_v135_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_diff(_diff(_safe_div(prefdiv, equity.abs() + 1.0), 4), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core135_3rd_v136_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_diff(_diff(_safe_div(debt, equity.abs() + 1.0), 4), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core136_3rd_v137_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_diff(_diff(_safe_div(prefdivis, debt.abs() + 1.0), 4), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core137_3rd_v138_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_diff(_diff(_safe_div(prefdiv, debt.abs() + 1.0), 4), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core138_3rd_v139_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_diff(_diff(prefdivis + prefdiv, 4), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core139_3rd_v140_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_diff(_diff(_diff(_safe_div(prefdivis + prefdiv, equity.abs() + 1.0), 4), 4), 4))
def cg_f027_convertible_and_preferred_overhang_core140_3rd_v141_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_slope(_diff(_diff(prefdivis, 4), 4), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core141_3rd_v142_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_slope(_diff(_diff(prefdiv, 4), 4), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core142_3rd_v143_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_slope(_diff(_diff(debt, 4), 4), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core143_3rd_v144_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_slope(_diff(_diff(_safe_div(prefdivis, equity.abs() + 1.0), 4), 4), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core144_3rd_v145_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_slope(_diff(_diff(_safe_div(prefdiv, equity.abs() + 1.0), 4), 4), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core145_3rd_v146_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_slope(_diff(_diff(_safe_div(debt, equity.abs() + 1.0), 4), 4), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core146_3rd_v147_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_slope(_diff(_diff(_safe_div(prefdivis, debt.abs() + 1.0), 4), 4), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core147_3rd_v148_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_slope(_diff(_diff(_safe_div(prefdiv, debt.abs() + 1.0), 4), 4), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core148_3rd_v149_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_slope(_diff(_diff(prefdivis + prefdiv, 4), 4), 4), 8))
def cg_f027_convertible_and_preferred_overhang_core149_3rd_v150_signal(prefdivis, prefdiv, debt, equity):
    return _clean(_z(_slope(_diff(_diff(_safe_div(prefdivis + prefdiv, equity.abs() + 1.0), 4), 4), 4), 8))