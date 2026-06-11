import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f005_current_liquidity_core00_2nd_v001_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(currentratio, 4))
def cg_f005_current_liquidity_core01_2nd_v002_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(assetsc, 4))
def cg_f005_current_liquidity_core02_2nd_v003_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(liabilitiesc, 4))
def cg_f005_current_liquidity_core03_2nd_v004_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(cashneq, 4))
def cg_f005_current_liquidity_core04_2nd_v005_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_safe_div(cashneq, liabilitiesc + 1.0), 4))
def cg_f005_current_liquidity_core05_2nd_v006_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_safe_div(cashneq, assetsc + 1.0), 4))
def cg_f005_current_liquidity_core06_2nd_v007_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(assetsc - liabilitiesc, 4))
def cg_f005_current_liquidity_core07_2nd_v008_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_safe_div(assetsc - liabilitiesc, assetsc + 1.0), 4))
def cg_f005_current_liquidity_core08_2nd_v009_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_safe_div(liabilitiesc, assetsc + 1.0), 4))
def cg_f005_current_liquidity_core09_2nd_v010_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_safe_div(cashneq, assetsc - liabilitiesc + 1.0), 4))

def cg_f005_current_liquidity_core10_2nd_v011_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(currentratio, 8))
def cg_f005_current_liquidity_core11_2nd_v012_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(assetsc, 8))
def cg_f005_current_liquidity_core12_2nd_v013_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(liabilitiesc, 8))
def cg_f005_current_liquidity_core13_2nd_v014_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(cashneq, 8))
def cg_f005_current_liquidity_core14_2nd_v015_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_safe_div(cashneq, liabilitiesc + 1.0), 8))
def cg_f005_current_liquidity_core15_2nd_v016_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_safe_div(cashneq, assetsc + 1.0), 8))
def cg_f005_current_liquidity_core16_2nd_v017_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(assetsc - liabilitiesc, 8))
def cg_f005_current_liquidity_core17_2nd_v018_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_safe_div(assetsc - liabilitiesc, assetsc + 1.0), 8))
def cg_f005_current_liquidity_core18_2nd_v019_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_safe_div(liabilitiesc, assetsc + 1.0), 8))
def cg_f005_current_liquidity_core19_2nd_v020_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_safe_div(cashneq, assetsc - liabilitiesc + 1.0), 8))

def cg_f005_current_liquidity_core20_2nd_v021_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(currentratio, 4))
def cg_f005_current_liquidity_core21_2nd_v022_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(assetsc, 4))
def cg_f005_current_liquidity_core22_2nd_v023_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(liabilitiesc, 4))
def cg_f005_current_liquidity_core23_2nd_v024_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(cashneq, 4))
def cg_f005_current_liquidity_core24_2nd_v025_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(_safe_div(cashneq, liabilitiesc + 1.0), 4))
def cg_f005_current_liquidity_core25_2nd_v026_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(_safe_div(cashneq, assetsc + 1.0), 4))
def cg_f005_current_liquidity_core26_2nd_v027_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(assetsc - liabilitiesc, 4))
def cg_f005_current_liquidity_core27_2nd_v028_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(_safe_div(assetsc - liabilitiesc, assetsc + 1.0), 4))
def cg_f005_current_liquidity_core28_2nd_v029_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(_safe_div(liabilitiesc, assetsc + 1.0), 4))
def cg_f005_current_liquidity_core29_2nd_v030_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(_safe_div(cashneq, assetsc - liabilitiesc + 1.0), 4))

def cg_f005_current_liquidity_core30_2nd_v031_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_slope(currentratio, 4), 8))
def cg_f005_current_liquidity_core31_2nd_v032_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_slope(assetsc, 4), 8))
def cg_f005_current_liquidity_core32_2nd_v033_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_slope(liabilitiesc, 4), 8))
def cg_f005_current_liquidity_core33_2nd_v034_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_slope(cashneq, 4), 8))
def cg_f005_current_liquidity_core34_2nd_v035_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_slope(_safe_div(cashneq, liabilitiesc + 1.0), 4), 8))
def cg_f005_current_liquidity_core35_2nd_v036_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_slope(_safe_div(cashneq, assetsc + 1.0), 4), 8))
def cg_f005_current_liquidity_core36_2nd_v037_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_slope(assetsc - liabilitiesc, 4), 8))
def cg_f005_current_liquidity_core37_2nd_v038_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_slope(_safe_div(assetsc - liabilitiesc, assetsc + 1.0), 4), 8))
def cg_f005_current_liquidity_core38_2nd_v039_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_slope(_safe_div(liabilitiesc, assetsc + 1.0), 4), 8))
def cg_f005_current_liquidity_core39_2nd_v040_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_slope(_safe_div(cashneq, assetsc - liabilitiesc + 1.0), 4), 8))

def cg_f005_current_liquidity_core40_2nd_v041_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_slope(currentratio, 8), 12))
def cg_f005_current_liquidity_core41_2nd_v042_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_slope(assetsc, 8), 12))
def cg_f005_current_liquidity_core42_2nd_v043_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_slope(liabilitiesc, 8), 12))
def cg_f005_current_liquidity_core43_2nd_v044_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_slope(cashneq, 8), 12))
def cg_f005_current_liquidity_core44_2nd_v045_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_slope(_safe_div(cashneq, liabilitiesc + 1.0), 8), 12))
def cg_f005_current_liquidity_core45_2nd_v046_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_slope(_safe_div(cashneq, assetsc + 1.0), 8), 12))
def cg_f005_current_liquidity_core46_2nd_v047_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_slope(assetsc - liabilitiesc, 8), 12))
def cg_f005_current_liquidity_core47_2nd_v048_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_slope(_safe_div(assetsc - liabilitiesc, assetsc + 1.0), 8), 12))
def cg_f005_current_liquidity_core48_2nd_v049_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_slope(_safe_div(liabilitiesc, assetsc + 1.0), 8), 12))
def cg_f005_current_liquidity_core49_2nd_v050_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_slope(_safe_div(cashneq, assetsc - liabilitiesc + 1.0), 8), 12))

def cg_f005_current_liquidity_core50_2nd_v051_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_diff(currentratio, 4), 8))
def cg_f005_current_liquidity_core51_2nd_v052_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_diff(assetsc, 4), 8))
def cg_f005_current_liquidity_core52_2nd_v053_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_diff(liabilitiesc, 4), 8))
def cg_f005_current_liquidity_core53_2nd_v054_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_diff(cashneq, 4), 8))
def cg_f005_current_liquidity_core54_2nd_v055_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_diff(_safe_div(cashneq, liabilitiesc + 1.0), 4), 8))
def cg_f005_current_liquidity_core55_2nd_v056_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_diff(_safe_div(cashneq, assetsc + 1.0), 4), 8))
def cg_f005_current_liquidity_core56_2nd_v057_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_diff(assetsc - liabilitiesc, 4), 8))
def cg_f005_current_liquidity_core57_2nd_v058_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_diff(_safe_div(assetsc - liabilitiesc, assetsc + 1.0), 4), 8))
def cg_f005_current_liquidity_core58_2nd_v059_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_diff(_safe_div(liabilitiesc, assetsc + 1.0), 4), 8))
def cg_f005_current_liquidity_core59_2nd_v060_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_diff(_safe_div(cashneq, assetsc - liabilitiesc + 1.0), 4), 8))

def cg_f005_current_liquidity_core60_2nd_v061_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_slope(currentratio, 4), 12))
def cg_f005_current_liquidity_core61_2nd_v062_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_slope(assetsc, 4), 12))
def cg_f005_current_liquidity_core62_2nd_v063_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_slope(liabilitiesc, 4), 12))
def cg_f005_current_liquidity_core63_2nd_v064_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_slope(cashneq, 4), 12))
def cg_f005_current_liquidity_core64_2nd_v065_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_slope(_safe_div(cashneq, liabilitiesc + 1.0), 4), 12))
def cg_f005_current_liquidity_core65_2nd_v066_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_slope(_safe_div(cashneq, assetsc + 1.0), 4), 12))
def cg_f005_current_liquidity_core66_2nd_v067_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_slope(assetsc - liabilitiesc, 4), 12))
def cg_f005_current_liquidity_core67_2nd_v068_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_slope(_safe_div(assetsc - liabilitiesc, assetsc + 1.0), 4), 12))
def cg_f005_current_liquidity_core68_2nd_v069_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_slope(_safe_div(liabilitiesc, assetsc + 1.0), 4), 12))
def cg_f005_current_liquidity_core69_2nd_v070_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_slope(_safe_div(cashneq, assetsc - liabilitiesc + 1.0), 4), 12))

def cg_f005_current_liquidity_core70_2nd_v071_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_diff(currentratio, 4), 12))
def cg_f005_current_liquidity_core71_2nd_v072_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_diff(assetsc, 4), 12))
def cg_f005_current_liquidity_core72_2nd_v073_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_diff(liabilitiesc, 4), 12))
def cg_f005_current_liquidity_core73_2nd_v074_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_diff(cashneq, 4), 12))
def cg_f005_current_liquidity_core74_2nd_v075_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_diff(_safe_div(cashneq, liabilitiesc + 1.0), 4), 12))
def cg_f005_current_liquidity_core75_2nd_v076_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_diff(_safe_div(cashneq, assetsc + 1.0), 4), 12))
def cg_f005_current_liquidity_core76_2nd_v077_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_diff(assetsc - liabilitiesc, 4), 12))
def cg_f005_current_liquidity_core77_2nd_v078_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_diff(_safe_div(assetsc - liabilitiesc, assetsc + 1.0), 4), 12))
def cg_f005_current_liquidity_core78_2nd_v079_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_diff(_safe_div(liabilitiesc, assetsc + 1.0), 4), 12))
def cg_f005_current_liquidity_core79_2nd_v080_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_diff(_safe_div(cashneq, assetsc - liabilitiesc + 1.0), 4), 12))

def cg_f005_current_liquidity_core80_2nd_v081_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_slope(currentratio, 4), 4))
def cg_f005_current_liquidity_core81_2nd_v082_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_slope(assetsc, 4), 4))
def cg_f005_current_liquidity_core82_2nd_v083_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_slope(liabilitiesc, 4), 4))
def cg_f005_current_liquidity_core83_2nd_v084_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_slope(cashneq, 4), 4))
def cg_f005_current_liquidity_core84_2nd_v085_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_slope(_safe_div(cashneq, liabilitiesc + 1.0), 4), 4))
def cg_f005_current_liquidity_core85_2nd_v086_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_slope(_safe_div(cashneq, assetsc + 1.0), 4), 4))
def cg_f005_current_liquidity_core86_2nd_v087_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_slope(assetsc - liabilitiesc, 4), 4))
def cg_f005_current_liquidity_core87_2nd_v088_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_slope(_safe_div(assetsc - liabilitiesc, assetsc + 1.0), 4), 4))
def cg_f005_current_liquidity_core88_2nd_v089_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_slope(_safe_div(liabilitiesc, assetsc + 1.0), 4), 4))
def cg_f005_current_liquidity_core89_2nd_v090_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_slope(_safe_div(cashneq, assetsc - liabilitiesc + 1.0), 4), 4))

def cg_f005_current_liquidity_core90_2nd_v091_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_diff(currentratio, 4), 4))
def cg_f005_current_liquidity_core91_2nd_v092_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_diff(assetsc, 4), 4))
def cg_f005_current_liquidity_core92_2nd_v093_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_diff(liabilitiesc, 4), 4))
def cg_f005_current_liquidity_core93_2nd_v094_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_diff(cashneq, 4), 4))
def cg_f005_current_liquidity_core94_2nd_v095_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_diff(_safe_div(cashneq, liabilitiesc + 1.0), 4), 4))
def cg_f005_current_liquidity_core95_2nd_v096_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_diff(_safe_div(cashneq, assetsc + 1.0), 4), 4))
def cg_f005_current_liquidity_core96_2nd_v097_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_diff(assetsc - liabilitiesc, 4), 4))
def cg_f005_current_liquidity_core97_2nd_v098_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_diff(_safe_div(assetsc - liabilitiesc, assetsc + 1.0), 4), 4))
def cg_f005_current_liquidity_core98_2nd_v099_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_diff(_safe_div(liabilitiesc, assetsc + 1.0), 4), 4))
def cg_f005_current_liquidity_core99_2nd_v100_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_diff(_safe_div(cashneq, assetsc - liabilitiesc + 1.0), 4), 4))

def cg_f005_current_liquidity_core100_2nd_v101_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_mean(currentratio, 4), 4))
def cg_f005_current_liquidity_core101_2nd_v102_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_mean(assetsc, 4), 4))
def cg_f005_current_liquidity_core102_2nd_v103_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_mean(liabilitiesc, 4), 4))
def cg_f005_current_liquidity_core103_2nd_v104_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_mean(cashneq, 4), 4))
def cg_f005_current_liquidity_core104_2nd_v105_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_mean(_safe_div(cashneq, liabilitiesc + 1.0), 4), 4))
def cg_f005_current_liquidity_core105_2nd_v106_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_mean(_safe_div(cashneq, assetsc + 1.0), 4), 4))
def cg_f005_current_liquidity_core106_2nd_v107_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_mean(assetsc - liabilitiesc, 4), 4))
def cg_f005_current_liquidity_core107_2nd_v108_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_mean(_safe_div(assetsc - liabilitiesc, assetsc + 1.0), 4), 4))
def cg_f005_current_liquidity_core108_2nd_v109_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_mean(_safe_div(liabilitiesc, assetsc + 1.0), 4), 4))
def cg_f005_current_liquidity_core109_2nd_v110_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_mean(_safe_div(cashneq, assetsc - liabilitiesc + 1.0), 4), 4))

def cg_f005_current_liquidity_core110_2nd_v111_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_mean(currentratio, 8), 8))
def cg_f005_current_liquidity_core111_2nd_v112_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_mean(assetsc, 8), 8))
def cg_f005_current_liquidity_core112_2nd_v113_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_mean(liabilitiesc, 8), 8))
def cg_f005_current_liquidity_core113_2nd_v114_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_mean(cashneq, 8), 8))
def cg_f005_current_liquidity_core114_2nd_v115_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_mean(_safe_div(cashneq, liabilitiesc + 1.0), 8), 8))
def cg_f005_current_liquidity_core115_2nd_v116_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_mean(_safe_div(cashneq, assetsc + 1.0), 8), 8))
def cg_f005_current_liquidity_core116_2nd_v117_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_mean(assetsc - liabilitiesc, 8), 8))
def cg_f005_current_liquidity_core117_2nd_v118_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_mean(_safe_div(assetsc - liabilitiesc, assetsc + 1.0), 8), 8))
def cg_f005_current_liquidity_core118_2nd_v119_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_mean(_safe_div(liabilitiesc, assetsc + 1.0), 8), 8))
def cg_f005_current_liquidity_core119_2nd_v120_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_mean(_safe_div(cashneq, assetsc - liabilitiesc + 1.0), 8), 8))

def cg_f005_current_liquidity_core120_2nd_v121_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(_mean(currentratio, 4), 4))
def cg_f005_current_liquidity_core121_2nd_v122_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(_mean(assetsc, 4), 4))
def cg_f005_current_liquidity_core122_2nd_v123_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(_mean(liabilitiesc, 4), 4))
def cg_f005_current_liquidity_core123_2nd_v124_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(_mean(cashneq, 4), 4))
def cg_f005_current_liquidity_core124_2nd_v125_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(_mean(_safe_div(cashneq, liabilitiesc + 1.0), 4), 4))
def cg_f005_current_liquidity_core125_2nd_v126_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(_mean(_safe_div(cashneq, assetsc + 1.0), 4), 4))
def cg_f005_current_liquidity_core126_2nd_v127_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(_mean(assetsc - liabilitiesc, 4), 4))
def cg_f005_current_liquidity_core127_2nd_v128_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(_mean(_safe_div(assetsc - liabilitiesc, assetsc + 1.0), 4), 4))
def cg_f005_current_liquidity_core128_2nd_v129_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(_mean(_safe_div(liabilitiesc, assetsc + 1.0), 4), 4))
def cg_f005_current_liquidity_core129_2nd_v130_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(_mean(_safe_div(cashneq, assetsc - liabilitiesc + 1.0), 4), 4))

def cg_f005_current_liquidity_core130_2nd_v131_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_diff(_mean(currentratio, 4), 4), 8))
def cg_f005_current_liquidity_core131_2nd_v132_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_diff(_mean(assetsc, 4), 4), 8))
def cg_f005_current_liquidity_core132_2nd_v133_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_diff(_mean(liabilitiesc, 4), 4), 8))
def cg_f005_current_liquidity_core133_2nd_v134_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_diff(_mean(cashneq, 4), 4), 8))
def cg_f005_current_liquidity_core134_2nd_v135_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_diff(_mean(_safe_div(cashneq, liabilitiesc + 1.0), 4), 4), 8))
def cg_f005_current_liquidity_core135_2nd_v136_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_diff(_mean(_safe_div(cashneq, assetsc + 1.0), 4), 4), 8))
def cg_f005_current_liquidity_core136_2nd_v137_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_diff(_mean(assetsc - liabilitiesc, 4), 4), 8))
def cg_f005_current_liquidity_core137_2nd_v138_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_diff(_mean(_safe_div(assetsc - liabilitiesc, assetsc + 1.0), 4), 4), 8))
def cg_f005_current_liquidity_core138_2nd_v139_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_diff(_mean(_safe_div(liabilitiesc, assetsc + 1.0), 4), 4), 8))
def cg_f005_current_liquidity_core139_2nd_v140_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_diff(_mean(_safe_div(cashneq, assetsc - liabilitiesc + 1.0), 4), 4), 8))

def cg_f005_current_liquidity_core140_2nd_v141_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_slope(_mean(currentratio, 4), 4), 12))
def cg_f005_current_liquidity_core141_2nd_v142_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_slope(_mean(assetsc, 4), 4), 12))
def cg_f005_current_liquidity_core142_2nd_v143_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_slope(_mean(liabilitiesc, 4), 4), 12))
def cg_f005_current_liquidity_core143_2nd_v144_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_slope(_mean(cashneq, 4), 4), 12))
def cg_f005_current_liquidity_core144_2nd_v145_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_slope(_mean(_safe_div(cashneq, liabilitiesc + 1.0), 4), 4), 12))
def cg_f005_current_liquidity_core145_2nd_v146_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_slope(_mean(_safe_div(cashneq, assetsc + 1.0), 4), 4), 12))
def cg_f005_current_liquidity_core146_2nd_v147_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_slope(_mean(assetsc - liabilitiesc, 4), 4), 12))
def cg_f005_current_liquidity_core147_2nd_v148_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_slope(_mean(_safe_div(assetsc - liabilitiesc, assetsc + 1.0), 4), 4), 12))
def cg_f005_current_liquidity_core148_2nd_v149_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_slope(_mean(_safe_div(liabilitiesc, assetsc + 1.0), 4), 4), 12))
def cg_f005_current_liquidity_core149_2nd_v150_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_slope(_mean(_safe_div(cashneq, assetsc - liabilitiesc + 1.0), 4), 4), 12))
