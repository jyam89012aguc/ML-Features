import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f006_quick_liquidity_core00_2nd_v001_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_slope(assetsc, 4))
def cg_f006_quick_liquidity_core01_2nd_v002_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_slope(inventory, 4))
def cg_f006_quick_liquidity_core02_2nd_v003_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_slope(liabilitiesc, 4))
def cg_f006_quick_liquidity_core03_2nd_v004_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_slope(cashneq, 4))
def cg_f006_quick_liquidity_core04_2nd_v005_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_slope(assetsc - inventory, 4))
def cg_f006_quick_liquidity_core05_2nd_v006_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_slope(_safe_div(assetsc - inventory, liabilitiesc + 1.0), 4))
def cg_f006_quick_liquidity_core06_2nd_v007_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_slope(_safe_div(cashneq, liabilitiesc + 1.0), 4))
def cg_f006_quick_liquidity_core07_2nd_v008_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_slope(_safe_div(inventory, assetsc + 1.0), 4))
def cg_f006_quick_liquidity_core08_2nd_v009_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_slope(_safe_div(cashneq, assetsc - inventory + 1.0), 4))
def cg_f006_quick_liquidity_core09_2nd_v010_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_slope(_safe_div(assetsc - inventory, assetsc + 1.0), 4))

def cg_f006_quick_liquidity_core10_2nd_v011_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_slope(assetsc, 8))
def cg_f006_quick_liquidity_core11_2nd_v012_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_slope(inventory, 8))
def cg_f006_quick_liquidity_core12_2nd_v013_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_slope(liabilitiesc, 8))
def cg_f006_quick_liquidity_core13_2nd_v014_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_slope(cashneq, 8))
def cg_f006_quick_liquidity_core14_2nd_v015_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_slope(assetsc - inventory, 8))
def cg_f006_quick_liquidity_core15_2nd_v016_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_slope(_safe_div(assetsc - inventory, liabilitiesc + 1.0), 8))
def cg_f006_quick_liquidity_core16_2nd_v017_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_slope(_safe_div(cashneq, liabilitiesc + 1.0), 8))
def cg_f006_quick_liquidity_core17_2nd_v018_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_slope(_safe_div(inventory, assetsc + 1.0), 8))
def cg_f006_quick_liquidity_core18_2nd_v019_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_slope(_safe_div(cashneq, assetsc - inventory + 1.0), 8))
def cg_f006_quick_liquidity_core19_2nd_v020_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_slope(_safe_div(assetsc - inventory, assetsc + 1.0), 8))

def cg_f006_quick_liquidity_core20_2nd_v021_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_diff(assetsc, 4))
def cg_f006_quick_liquidity_core21_2nd_v022_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_diff(inventory, 4))
def cg_f006_quick_liquidity_core22_2nd_v023_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_diff(liabilitiesc, 4))
def cg_f006_quick_liquidity_core23_2nd_v024_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_diff(cashneq, 4))
def cg_f006_quick_liquidity_core24_2nd_v025_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_diff(assetsc - inventory, 4))
def cg_f006_quick_liquidity_core25_2nd_v026_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_diff(_safe_div(assetsc - inventory, liabilitiesc + 1.0), 4))
def cg_f006_quick_liquidity_core26_2nd_v027_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_diff(_safe_div(cashneq, liabilitiesc + 1.0), 4))
def cg_f006_quick_liquidity_core27_2nd_v028_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_diff(_safe_div(inventory, assetsc + 1.0), 4))
def cg_f006_quick_liquidity_core28_2nd_v029_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_diff(_safe_div(cashneq, assetsc - inventory + 1.0), 4))
def cg_f006_quick_liquidity_core29_2nd_v030_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_diff(_safe_div(assetsc - inventory, assetsc + 1.0), 4))

def cg_f006_quick_liquidity_core30_2nd_v031_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_z(_slope(assetsc, 4), 8))
def cg_f006_quick_liquidity_core31_2nd_v032_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_z(_slope(inventory, 4), 8))
def cg_f006_quick_liquidity_core32_2nd_v033_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_z(_slope(liabilitiesc, 4), 8))
def cg_f006_quick_liquidity_core33_2nd_v034_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_z(_slope(cashneq, 4), 8))
def cg_f006_quick_liquidity_core34_2nd_v035_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_z(_slope(assetsc - inventory, 4), 8))
def cg_f006_quick_liquidity_core35_2nd_v036_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_z(_slope(_safe_div(assetsc - inventory, liabilitiesc + 1.0), 4), 8))
def cg_f006_quick_liquidity_core36_2nd_v037_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_z(_slope(_safe_div(cashneq, liabilitiesc + 1.0), 4), 8))
def cg_f006_quick_liquidity_core37_2nd_v038_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_z(_slope(_safe_div(inventory, assetsc + 1.0), 4), 8))
def cg_f006_quick_liquidity_core38_2nd_v039_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_z(_slope(_safe_div(cashneq, assetsc - inventory + 1.0), 4), 8))
def cg_f006_quick_liquidity_core39_2nd_v040_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_z(_slope(_safe_div(assetsc - inventory, assetsc + 1.0), 4), 8))

def cg_f006_quick_liquidity_core40_2nd_v041_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_z(_slope(assetsc, 8), 12))
def cg_f006_quick_liquidity_core41_2nd_v042_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_z(_slope(inventory, 8), 12))
def cg_f006_quick_liquidity_core42_2nd_v043_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_z(_slope(liabilitiesc, 8), 12))
def cg_f006_quick_liquidity_core43_2nd_v044_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_z(_slope(cashneq, 8), 12))
def cg_f006_quick_liquidity_core44_2nd_v045_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_z(_slope(assetsc - inventory, 8), 12))
def cg_f006_quick_liquidity_core45_2nd_v046_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_z(_slope(_safe_div(assetsc - inventory, liabilitiesc + 1.0), 8), 12))
def cg_f006_quick_liquidity_core46_2nd_v047_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_z(_slope(_safe_div(cashneq, liabilitiesc + 1.0), 8), 12))
def cg_f006_quick_liquidity_core47_2nd_v048_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_z(_slope(_safe_div(inventory, assetsc + 1.0), 8), 12))
def cg_f006_quick_liquidity_core48_2nd_v049_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_z(_slope(_safe_div(cashneq, assetsc - inventory + 1.0), 8), 12))
def cg_f006_quick_liquidity_core49_2nd_v050_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_z(_slope(_safe_div(assetsc - inventory, assetsc + 1.0), 8), 12))

def cg_f006_quick_liquidity_core50_2nd_v051_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_z(_diff(assetsc, 4), 8))
def cg_f006_quick_liquidity_core51_2nd_v052_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_z(_diff(inventory, 4), 8))
def cg_f006_quick_liquidity_core52_2nd_v053_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_z(_diff(liabilitiesc, 4), 8))
def cg_f006_quick_liquidity_core53_2nd_v054_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_z(_diff(cashneq, 4), 8))
def cg_f006_quick_liquidity_core54_2nd_v055_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_z(_diff(assetsc - inventory, 4), 8))
def cg_f006_quick_liquidity_core55_2nd_v056_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_z(_diff(_safe_div(assetsc - inventory, liabilitiesc + 1.0), 4), 8))
def cg_f006_quick_liquidity_core56_2nd_v057_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_z(_diff(_safe_div(cashneq, liabilitiesc + 1.0), 4), 8))
def cg_f006_quick_liquidity_core57_2nd_v058_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_z(_diff(_safe_div(inventory, assetsc + 1.0), 4), 8))
def cg_f006_quick_liquidity_core58_2nd_v059_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_z(_diff(_safe_div(cashneq, assetsc - inventory + 1.0), 4), 8))
def cg_f006_quick_liquidity_core59_2nd_v060_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_z(_diff(_safe_div(assetsc - inventory, assetsc + 1.0), 4), 8))

def cg_f006_quick_liquidity_core60_2nd_v061_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_rank(_slope(assetsc, 4), 12))
def cg_f006_quick_liquidity_core61_2nd_v062_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_rank(_slope(inventory, 4), 12))
def cg_f006_quick_liquidity_core62_2nd_v063_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_rank(_slope(liabilitiesc, 4), 12))
def cg_f006_quick_liquidity_core63_2nd_v064_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_rank(_slope(cashneq, 4), 12))
def cg_f006_quick_liquidity_core64_2nd_v065_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_rank(_slope(assetsc - inventory, 4), 12))
def cg_f006_quick_liquidity_core65_2nd_v066_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_rank(_slope(_safe_div(assetsc - inventory, liabilitiesc + 1.0), 4), 12))
def cg_f006_quick_liquidity_core66_2nd_v067_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_rank(_slope(_safe_div(cashneq, liabilitiesc + 1.0), 4), 12))
def cg_f006_quick_liquidity_core67_2nd_v068_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_rank(_slope(_safe_div(inventory, assetsc + 1.0), 4), 12))
def cg_f006_quick_liquidity_core68_2nd_v069_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_rank(_slope(_safe_div(cashneq, assetsc - inventory + 1.0), 4), 12))
def cg_f006_quick_liquidity_core69_2nd_v070_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_rank(_slope(_safe_div(assetsc - inventory, assetsc + 1.0), 4), 12))

def cg_f006_quick_liquidity_core70_2nd_v071_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_rank(_diff(assetsc, 4), 12))
def cg_f006_quick_liquidity_core71_2nd_v072_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_rank(_diff(inventory, 4), 12))
def cg_f006_quick_liquidity_core72_2nd_v073_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_rank(_diff(liabilitiesc, 4), 12))
def cg_f006_quick_liquidity_core73_2nd_v074_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_rank(_diff(cashneq, 4), 12))
def cg_f006_quick_liquidity_core74_2nd_v075_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_rank(_diff(assetsc - inventory, 4), 12))
def cg_f006_quick_liquidity_core75_2nd_v076_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_rank(_diff(_safe_div(assetsc - inventory, liabilitiesc + 1.0), 4), 12))
def cg_f006_quick_liquidity_core76_2nd_v077_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_rank(_diff(_safe_div(cashneq, liabilitiesc + 1.0), 4), 12))
def cg_f006_quick_liquidity_core77_2nd_v078_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_rank(_diff(_safe_div(inventory, assetsc + 1.0), 4), 12))
def cg_f006_quick_liquidity_core78_2nd_v079_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_rank(_diff(_safe_div(cashneq, assetsc - inventory + 1.0), 4), 12))
def cg_f006_quick_liquidity_core79_2nd_v080_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_rank(_diff(_safe_div(assetsc - inventory, assetsc + 1.0), 4), 12))

def cg_f006_quick_liquidity_core80_2nd_v081_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_mean(_slope(assetsc, 4), 4))
def cg_f006_quick_liquidity_core81_2nd_v082_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_mean(_slope(inventory, 4), 4))
def cg_f006_quick_liquidity_core82_2nd_v083_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_mean(_slope(liabilitiesc, 4), 4))
def cg_f006_quick_liquidity_core83_2nd_v084_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_mean(_slope(cashneq, 4), 4))
def cg_f006_quick_liquidity_core84_2nd_v085_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_mean(_slope(assetsc - inventory, 4), 4))
def cg_f006_quick_liquidity_core85_2nd_v086_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_mean(_slope(_safe_div(assetsc - inventory, liabilitiesc + 1.0), 4), 4))
def cg_f006_quick_liquidity_core86_2nd_v087_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_mean(_slope(_safe_div(cashneq, liabilitiesc + 1.0), 4), 4))
def cg_f006_quick_liquidity_core87_2nd_v088_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_mean(_slope(_safe_div(inventory, assetsc + 1.0), 4), 4))
def cg_f006_quick_liquidity_core88_2nd_v089_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_mean(_slope(_safe_div(cashneq, assetsc - inventory + 1.0), 4), 4))
def cg_f006_quick_liquidity_core89_2nd_v090_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_mean(_slope(_safe_div(assetsc - inventory, assetsc + 1.0), 4), 4))

def cg_f006_quick_liquidity_core90_2nd_v091_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_mean(_diff(assetsc, 4), 4))
def cg_f006_quick_liquidity_core91_2nd_v092_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_mean(_diff(inventory, 4), 4))
def cg_f006_quick_liquidity_core92_2nd_v093_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_mean(_diff(liabilitiesc, 4), 4))
def cg_f006_quick_liquidity_core93_2nd_v094_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_mean(_diff(cashneq, 4), 4))
def cg_f006_quick_liquidity_core94_2nd_v095_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_mean(_diff(assetsc - inventory, 4), 4))
def cg_f006_quick_liquidity_core95_2nd_v096_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_mean(_diff(_safe_div(assetsc - inventory, liabilitiesc + 1.0), 4), 4))
def cg_f006_quick_liquidity_core96_2nd_v097_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_mean(_diff(_safe_div(cashneq, liabilitiesc + 1.0), 4), 4))
def cg_f006_quick_liquidity_core97_2nd_v098_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_mean(_diff(_safe_div(inventory, assetsc + 1.0), 4), 4))
def cg_f006_quick_liquidity_core98_2nd_v099_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_mean(_diff(_safe_div(cashneq, assetsc - inventory + 1.0), 4), 4))
def cg_f006_quick_liquidity_core99_2nd_v100_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_mean(_diff(_safe_div(assetsc - inventory, assetsc + 1.0), 4), 4))

def cg_f006_quick_liquidity_core100_2nd_v101_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_slope(_mean(assetsc, 4), 4))
def cg_f006_quick_liquidity_core101_2nd_v102_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_slope(_mean(inventory, 4), 4))
def cg_f006_quick_liquidity_core102_2nd_v103_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_slope(_mean(liabilitiesc, 4), 4))
def cg_f006_quick_liquidity_core103_2nd_v104_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_slope(_mean(cashneq, 4), 4))
def cg_f006_quick_liquidity_core104_2nd_v105_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_slope(_mean(assetsc - inventory, 4), 4))
def cg_f006_quick_liquidity_core105_2nd_v106_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_slope(_mean(_safe_div(assetsc - inventory, liabilitiesc + 1.0), 4), 4))
def cg_f006_quick_liquidity_core106_2nd_v107_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_slope(_mean(_safe_div(cashneq, liabilitiesc + 1.0), 4), 4))
def cg_f006_quick_liquidity_core107_2nd_v108_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_slope(_mean(_safe_div(inventory, assetsc + 1.0), 4), 4))
def cg_f006_quick_liquidity_core108_2nd_v109_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_slope(_mean(_safe_div(cashneq, assetsc - inventory + 1.0), 4), 4))
def cg_f006_quick_liquidity_core109_2nd_v110_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_slope(_mean(_safe_div(assetsc - inventory, assetsc + 1.0), 4), 4))

def cg_f006_quick_liquidity_core110_2nd_v111_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_slope(_mean(assetsc, 8), 8))
def cg_f006_quick_liquidity_core111_2nd_v112_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_slope(_mean(inventory, 8), 8))
def cg_f006_quick_liquidity_core112_2nd_v113_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_slope(_mean(liabilitiesc, 8), 8))
def cg_f006_quick_liquidity_core113_2nd_v114_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_slope(_mean(cashneq, 8), 8))
def cg_f006_quick_liquidity_core114_2nd_v115_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_slope(_mean(assetsc - inventory, 8), 8))
def cg_f006_quick_liquidity_core115_2nd_v116_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_slope(_mean(_safe_div(assetsc - inventory, liabilitiesc + 1.0), 8), 8))
def cg_f006_quick_liquidity_core116_2nd_v117_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_slope(_mean(_safe_div(cashneq, liabilitiesc + 1.0), 8), 8))
def cg_f006_quick_liquidity_core117_2nd_v118_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_slope(_mean(_safe_div(inventory, assetsc + 1.0), 8), 8))
def cg_f006_quick_liquidity_core118_2nd_v119_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_slope(_mean(_safe_div(cashneq, assetsc - inventory + 1.0), 8), 8))
def cg_f006_quick_liquidity_core119_2nd_v120_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_slope(_mean(_safe_div(assetsc - inventory, assetsc + 1.0), 8), 8))

def cg_f006_quick_liquidity_core120_2nd_v121_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_diff(_mean(assetsc, 4), 4))
def cg_f006_quick_liquidity_core121_2nd_v122_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_diff(_mean(inventory, 4), 4))
def cg_f006_quick_liquidity_core122_2nd_v123_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_diff(_mean(liabilitiesc, 4), 4))
def cg_f006_quick_liquidity_core123_2nd_v124_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_diff(_mean(cashneq, 4), 4))
def cg_f006_quick_liquidity_core124_2nd_v125_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_diff(_mean(assetsc - inventory, 4), 4))
def cg_f006_quick_liquidity_core125_2nd_v126_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_diff(_mean(_safe_div(assetsc - inventory, liabilitiesc + 1.0), 4), 4))
def cg_f006_quick_liquidity_core126_2nd_v127_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_diff(_mean(_safe_div(cashneq, liabilitiesc + 1.0), 4), 4))
def cg_f006_quick_liquidity_core127_2nd_v128_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_diff(_mean(_safe_div(inventory, assetsc + 1.0), 4), 4))
def cg_f006_quick_liquidity_core128_2nd_v129_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_diff(_mean(_safe_div(cashneq, assetsc - inventory + 1.0), 4), 4))
def cg_f006_quick_liquidity_core129_2nd_v130_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_diff(_mean(_safe_div(assetsc - inventory, assetsc + 1.0), 4), 4))

def cg_f006_quick_liquidity_core130_2nd_v131_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_z(_diff(_mean(assetsc, 4), 4), 8))
def cg_f006_quick_liquidity_core131_2nd_v132_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_z(_diff(_mean(inventory, 4), 4), 8))
def cg_f006_quick_liquidity_core132_2nd_v133_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_z(_diff(_mean(liabilitiesc, 4), 4), 8))
def cg_f006_quick_liquidity_core133_2nd_v134_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_z(_diff(_mean(cashneq, 4), 4), 8))
def cg_f006_quick_liquidity_core134_2nd_v135_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_z(_diff(_mean(assetsc - inventory, 4), 4), 8))
def cg_f006_quick_liquidity_core135_2nd_v136_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_z(_diff(_mean(_safe_div(assetsc - inventory, liabilitiesc + 1.0), 4), 4), 8))
def cg_f006_quick_liquidity_core136_2nd_v137_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_z(_diff(_mean(_safe_div(cashneq, liabilitiesc + 1.0), 4), 4), 8))
def cg_f006_quick_liquidity_core137_2nd_v138_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_z(_diff(_mean(_safe_div(inventory, assetsc + 1.0), 4), 4), 8))
def cg_f006_quick_liquidity_core138_2nd_v139_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_z(_diff(_mean(_safe_div(cashneq, assetsc - inventory + 1.0), 4), 4), 8))
def cg_f006_quick_liquidity_core139_2nd_v140_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_z(_diff(_mean(_safe_div(assetsc - inventory, assetsc + 1.0), 4), 4), 8))

def cg_f006_quick_liquidity_core140_2nd_v141_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_rank(_slope(_mean(assetsc, 4), 4), 12))
def cg_f006_quick_liquidity_core141_2nd_v142_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_rank(_slope(_mean(inventory, 4), 4), 12))
def cg_f006_quick_liquidity_core142_2nd_v143_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_rank(_slope(_mean(liabilitiesc, 4), 4), 12))
def cg_f006_quick_liquidity_core143_2nd_v144_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_rank(_slope(_mean(cashneq, 4), 4), 12))
def cg_f006_quick_liquidity_core144_2nd_v145_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_rank(_slope(_mean(assetsc - inventory, 4), 4), 12))
def cg_f006_quick_liquidity_core145_2nd_v146_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_rank(_slope(_mean(_safe_div(assetsc - inventory, liabilitiesc + 1.0), 4), 4), 12))
def cg_f006_quick_liquidity_core146_2nd_v147_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_rank(_slope(_mean(_safe_div(cashneq, liabilitiesc + 1.0), 4), 4), 12))
def cg_f006_quick_liquidity_core147_2nd_v148_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_rank(_slope(_mean(_safe_div(inventory, assetsc + 1.0), 4), 4), 12))
def cg_f006_quick_liquidity_core148_2nd_v149_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_rank(_slope(_mean(_safe_div(cashneq, assetsc - inventory + 1.0), 4), 4), 12))
def cg_f006_quick_liquidity_core149_2nd_v150_signal(assetsc, inventory, liabilitiesc, cashneq):
    return _clean(_rank(_slope(_mean(_safe_div(assetsc - inventory, assetsc + 1.0), 4), 4), 12))
