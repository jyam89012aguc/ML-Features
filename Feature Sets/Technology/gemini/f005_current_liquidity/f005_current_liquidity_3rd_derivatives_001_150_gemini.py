import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f005_current_liquidity_core00_3rd_v001_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(_diff(currentratio, 4), 4))
def cg_f005_current_liquidity_core01_3rd_v002_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(_diff(assetsc, 4), 4))
def cg_f005_current_liquidity_core02_3rd_v003_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(_diff(liabilitiesc, 4), 4))
def cg_f005_current_liquidity_core03_3rd_v004_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(_diff(cashneq, 4), 4))
def cg_f005_current_liquidity_core04_3rd_v005_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(_diff(_safe_div(cashneq, liabilitiesc + 1.0), 4), 4))
def cg_f005_current_liquidity_core05_3rd_v006_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(_diff(_safe_div(cashneq, assetsc + 1.0), 4), 4))
def cg_f005_current_liquidity_core06_3rd_v007_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(_diff(assetsc - liabilitiesc, 4), 4))
def cg_f005_current_liquidity_core07_3rd_v008_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(_diff(_safe_div(assetsc - liabilitiesc, assetsc + 1.0), 4), 4))
def cg_f005_current_liquidity_core08_3rd_v009_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(_diff(_safe_div(liabilitiesc, assetsc + 1.0), 4), 4))
def cg_f005_current_liquidity_core09_3rd_v010_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(_diff(_safe_div(cashneq, assetsc - liabilitiesc + 1.0), 4), 4))

def cg_f005_current_liquidity_core10_3rd_v011_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_diff(currentratio, 4), 8))
def cg_f005_current_liquidity_core11_3rd_v012_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_diff(assetsc, 4), 8))
def cg_f005_current_liquidity_core12_3rd_v013_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_diff(liabilitiesc, 4), 8))
def cg_f005_current_liquidity_core13_3rd_v014_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_diff(cashneq, 4), 8))
def cg_f005_current_liquidity_core14_3rd_v015_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_diff(_safe_div(cashneq, liabilitiesc + 1.0), 4), 8))
def cg_f005_current_liquidity_core15_3rd_v016_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_diff(_safe_div(cashneq, assetsc + 1.0), 4), 8))
def cg_f005_current_liquidity_core16_3rd_v017_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_diff(assetsc - liabilitiesc, 4), 8))
def cg_f005_current_liquidity_core17_3rd_v018_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_diff(_safe_div(assetsc - liabilitiesc, assetsc + 1.0), 4), 8))
def cg_f005_current_liquidity_core18_3rd_v019_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_diff(_safe_div(liabilitiesc, assetsc + 1.0), 4), 8))
def cg_f005_current_liquidity_core19_3rd_v020_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_diff(_safe_div(cashneq, assetsc - liabilitiesc + 1.0), 4), 8))

def cg_f005_current_liquidity_core20_3rd_v021_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(_slope(currentratio, 4), 4))
def cg_f005_current_liquidity_core21_3rd_v022_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(_slope(assetsc, 4), 4))
def cg_f005_current_liquidity_core22_3rd_v023_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(_slope(liabilitiesc, 4), 4))
def cg_f005_current_liquidity_core23_3rd_v024_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(_slope(cashneq, 4), 4))
def cg_f005_current_liquidity_core24_3rd_v025_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(_slope(_safe_div(cashneq, liabilitiesc + 1.0), 4), 4))
def cg_f005_current_liquidity_core25_3rd_v026_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(_slope(_safe_div(cashneq, assetsc + 1.0), 4), 4))
def cg_f005_current_liquidity_core26_3rd_v027_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(_slope(assetsc - liabilitiesc, 4), 4))
def cg_f005_current_liquidity_core27_3rd_v028_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(_slope(_safe_div(assetsc - liabilitiesc, assetsc + 1.0), 4), 4))
def cg_f005_current_liquidity_core28_3rd_v029_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(_slope(_safe_div(liabilitiesc, assetsc + 1.0), 4), 4))
def cg_f005_current_liquidity_core29_3rd_v030_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(_slope(_safe_div(cashneq, assetsc - liabilitiesc + 1.0), 4), 4))

def cg_f005_current_liquidity_core30_3rd_v031_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_diff(_diff(currentratio, 4), 4), 8))
def cg_f005_current_liquidity_core31_3rd_v032_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_diff(_diff(assetsc, 4), 4), 8))
def cg_f005_current_liquidity_core32_3rd_v033_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_diff(_diff(liabilitiesc, 4), 4), 8))
def cg_f005_current_liquidity_core33_3rd_v034_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_diff(_diff(cashneq, 4), 4), 8))
def cg_f005_current_liquidity_core34_3rd_v035_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_diff(_diff(_safe_div(cashneq, liabilitiesc + 1.0), 4), 4), 8))
def cg_f005_current_liquidity_core35_3rd_v036_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_diff(_diff(_safe_div(cashneq, assetsc + 1.0), 4), 4), 8))
def cg_f005_current_liquidity_core36_3rd_v037_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_diff(_diff(assetsc - liabilitiesc, 4), 4), 8))
def cg_f005_current_liquidity_core37_3rd_v038_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_diff(_diff(_safe_div(assetsc - liabilitiesc, assetsc + 1.0), 4), 4), 8))
def cg_f005_current_liquidity_core38_3rd_v039_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_diff(_diff(_safe_div(liabilitiesc, assetsc + 1.0), 4), 4), 8))
def cg_f005_current_liquidity_core39_3rd_v040_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_diff(_diff(_safe_div(cashneq, assetsc - liabilitiesc + 1.0), 4), 4), 8))

def cg_f005_current_liquidity_core40_3rd_v041_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_slope(_diff(currentratio, 4), 8), 12))
def cg_f005_current_liquidity_core41_3rd_v042_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_slope(_diff(assetsc, 4), 8), 12))
def cg_f005_current_liquidity_core42_3rd_v043_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_slope(_diff(liabilitiesc, 4), 8), 12))
def cg_f005_current_liquidity_core43_3rd_v044_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_slope(_diff(cashneq, 4), 8), 12))
def cg_f005_current_liquidity_core44_3rd_v045_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_slope(_diff(_safe_div(cashneq, liabilitiesc + 1.0), 4), 8), 12))
def cg_f005_current_liquidity_core45_3rd_v046_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_slope(_diff(_safe_div(cashneq, assetsc + 1.0), 4), 8), 12))
def cg_f005_current_liquidity_core46_3rd_v047_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_slope(_diff(assetsc - liabilitiesc, 4), 8), 12))
def cg_f005_current_liquidity_core47_3rd_v048_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_slope(_diff(_safe_div(assetsc - liabilitiesc, assetsc + 1.0), 4), 8), 12))
def cg_f005_current_liquidity_core48_3rd_v049_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_slope(_diff(_safe_div(liabilitiesc, assetsc + 1.0), 4), 8), 12))
def cg_f005_current_liquidity_core49_3rd_v050_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_slope(_diff(_safe_div(cashneq, assetsc - liabilitiesc + 1.0), 4), 8), 12))

def cg_f005_current_liquidity_core50_3rd_v051_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_diff(_slope(currentratio, 4), 4), 8))
def cg_f005_current_liquidity_core51_3rd_v052_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_diff(_slope(assetsc, 4), 4), 8))
def cg_f005_current_liquidity_core52_3rd_v053_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_diff(_slope(liabilitiesc, 4), 4), 8))
def cg_f005_current_liquidity_core53_3rd_v054_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_diff(_slope(cashneq, 4), 4), 8))
def cg_f005_current_liquidity_core54_3rd_v055_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_diff(_slope(_safe_div(cashneq, liabilitiesc + 1.0), 4), 4), 8))
def cg_f005_current_liquidity_core55_3rd_v056_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_diff(_slope(_safe_div(cashneq, assetsc + 1.0), 4), 4), 8))
def cg_f005_current_liquidity_core56_3rd_v057_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_diff(_slope(assetsc - liabilitiesc, 4), 4), 8))
def cg_f005_current_liquidity_core57_3rd_v058_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_diff(_slope(_safe_div(assetsc - liabilitiesc, assetsc + 1.0), 4), 4), 8))
def cg_f005_current_liquidity_core58_3rd_v059_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_diff(_slope(_safe_div(liabilitiesc, assetsc + 1.0), 4), 4), 8))
def cg_f005_current_liquidity_core59_3rd_v060_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_diff(_slope(_safe_div(cashneq, assetsc - liabilitiesc + 1.0), 4), 4), 8))

def cg_f005_current_liquidity_core60_3rd_v061_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_diff(_diff(currentratio, 4), 4), 12))
def cg_f005_current_liquidity_core61_3rd_v062_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_diff(_diff(assetsc, 4), 4), 12))
def cg_f005_current_liquidity_core62_3rd_v063_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_diff(_diff(liabilitiesc, 4), 4), 12))
def cg_f005_current_liquidity_core63_3rd_v064_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_diff(_diff(cashneq, 4), 4), 12))
def cg_f005_current_liquidity_core64_3rd_v065_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_diff(_diff(_safe_div(cashneq, liabilitiesc + 1.0), 4), 4), 12))
def cg_f005_current_liquidity_core65_3rd_v066_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_diff(_diff(_safe_div(cashneq, assetsc + 1.0), 4), 4), 12))
def cg_f005_current_liquidity_core66_3rd_v067_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_diff(_diff(assetsc - liabilitiesc, 4), 4), 12))
def cg_f005_current_liquidity_core67_3rd_v068_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_diff(_diff(_safe_div(assetsc - liabilitiesc, assetsc + 1.0), 4), 4), 12))
def cg_f005_current_liquidity_core68_3rd_v069_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_diff(_diff(_safe_div(liabilitiesc, assetsc + 1.0), 4), 4), 12))
def cg_f005_current_liquidity_core69_3rd_v070_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_diff(_diff(_safe_div(cashneq, assetsc - liabilitiesc + 1.0), 4), 4), 12))

def cg_f005_current_liquidity_core70_3rd_v071_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_slope(_diff(currentratio, 4), 8), 12))
def cg_f005_current_liquidity_core71_3rd_v072_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_slope(_diff(assetsc, 4), 8), 12))
def cg_f005_current_liquidity_core72_3rd_v073_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_slope(_diff(liabilitiesc, 4), 8), 12))
def cg_f005_current_liquidity_core73_3rd_v074_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_slope(_diff(cashneq, 4), 8), 12))
def cg_f005_current_liquidity_core74_3rd_v075_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_slope(_diff(_safe_div(cashneq, liabilitiesc + 1.0), 4), 8), 12))
def cg_f005_current_liquidity_core75_3rd_v076_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_slope(_diff(_safe_div(cashneq, assetsc + 1.0), 4), 8), 12))
def cg_f005_current_liquidity_core76_3rd_v077_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_slope(_diff(assetsc - liabilitiesc, 4), 8), 12))
def cg_f005_current_liquidity_core77_3rd_v078_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_slope(_diff(_safe_div(assetsc - liabilitiesc, assetsc + 1.0), 4), 8), 12))
def cg_f005_current_liquidity_core78_3rd_v079_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_slope(_diff(_safe_div(liabilitiesc, assetsc + 1.0), 4), 8), 12))
def cg_f005_current_liquidity_core79_3rd_v080_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_slope(_diff(_safe_div(cashneq, assetsc - liabilitiesc + 1.0), 4), 8), 12))

def cg_f005_current_liquidity_core80_3rd_v081_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_diff(_slope(currentratio, 4), 4), 12))
def cg_f005_current_liquidity_core81_3rd_v082_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_diff(_slope(assetsc, 4), 4), 12))
def cg_f005_current_liquidity_core82_3rd_v083_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_diff(_slope(liabilitiesc, 4), 4), 12))
def cg_f005_current_liquidity_core83_3rd_v084_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_diff(_slope(cashneq, 4), 4), 12))
def cg_f005_current_liquidity_core84_3rd_v085_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_diff(_slope(_safe_div(cashneq, liabilitiesc + 1.0), 4), 4), 12))
def cg_f005_current_liquidity_core85_3rd_v086_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_diff(_slope(_safe_div(cashneq, assetsc + 1.0), 4), 4), 12))
def cg_f005_current_liquidity_core86_3rd_v087_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_diff(_slope(assetsc - liabilitiesc, 4), 4), 12))
def cg_f005_current_liquidity_core87_3rd_v088_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_diff(_slope(_safe_div(assetsc - liabilitiesc, assetsc + 1.0), 4), 4), 12))
def cg_f005_current_liquidity_core88_3rd_v089_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_diff(_slope(_safe_div(liabilitiesc, assetsc + 1.0), 4), 4), 12))
def cg_f005_current_liquidity_core89_3rd_v090_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_rank(_diff(_slope(_safe_div(cashneq, assetsc - liabilitiesc + 1.0), 4), 4), 12))

def cg_f005_current_liquidity_core90_3rd_v091_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_diff(_diff(currentratio, 4), 4), 4))
def cg_f005_current_liquidity_core91_3rd_v092_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_diff(_diff(assetsc, 4), 4), 4))
def cg_f005_current_liquidity_core92_3rd_v093_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_diff(_diff(liabilitiesc, 4), 4), 4))
def cg_f005_current_liquidity_core93_3rd_v094_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_diff(_diff(cashneq, 4), 4), 4))
def cg_f005_current_liquidity_core94_3rd_v095_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_diff(_diff(_safe_div(cashneq, liabilitiesc + 1.0), 4), 4), 4))
def cg_f005_current_liquidity_core95_3rd_v096_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_diff(_diff(_safe_div(cashneq, assetsc + 1.0), 4), 4), 4))
def cg_f005_current_liquidity_core96_3rd_v097_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_diff(_diff(assetsc - liabilitiesc, 4), 4), 4))
def cg_f005_current_liquidity_core97_3rd_v098_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_diff(_diff(_safe_div(assetsc - liabilitiesc, assetsc + 1.0), 4), 4), 4))
def cg_f005_current_liquidity_core98_3rd_v099_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_diff(_diff(_safe_div(liabilitiesc, assetsc + 1.0), 4), 4), 4))
def cg_f005_current_liquidity_core99_3rd_v100_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_diff(_diff(_safe_div(cashneq, assetsc - liabilitiesc + 1.0), 4), 4), 4))

def cg_f005_current_liquidity_core100_3rd_v101_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_slope(_diff(currentratio, 4), 8), 4))
def cg_f005_current_liquidity_core101_3rd_v102_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_slope(_diff(assetsc, 4), 8), 4))
def cg_f005_current_liquidity_core102_3rd_v103_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_slope(_diff(liabilitiesc, 4), 8), 4))
def cg_f005_current_liquidity_core103_3rd_v104_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_slope(_diff(cashneq, 4), 8), 4))
def cg_f005_current_liquidity_core104_3rd_v105_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_slope(_diff(_safe_div(cashneq, liabilitiesc + 1.0), 4), 8), 4))
def cg_f005_current_liquidity_core105_3rd_v106_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_slope(_diff(_safe_div(cashneq, assetsc + 1.0), 4), 8), 4))
def cg_f005_current_liquidity_core106_3rd_v107_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_slope(_diff(assetsc - liabilitiesc, 4), 8), 4))
def cg_f005_current_liquidity_core107_3rd_v108_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_slope(_diff(_safe_div(assetsc - liabilitiesc, assetsc + 1.0), 4), 8), 4))
def cg_f005_current_liquidity_core108_3rd_v109_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_slope(_diff(_safe_div(liabilitiesc, assetsc + 1.0), 4), 8), 4))
def cg_f005_current_liquidity_core109_3rd_v110_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_slope(_diff(_safe_div(cashneq, assetsc - liabilitiesc + 1.0), 4), 8), 4))

def cg_f005_current_liquidity_core110_3rd_v111_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_diff(_slope(currentratio, 4), 4), 4))
def cg_f005_current_liquidity_core111_3rd_v112_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_diff(_slope(assetsc, 4), 4), 4))
def cg_f005_current_liquidity_core112_3rd_v113_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_diff(_slope(liabilitiesc, 4), 4), 4))
def cg_f005_current_liquidity_core113_3rd_v114_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_diff(_slope(cashneq, 4), 4), 4))
def cg_f005_current_liquidity_core114_3rd_v115_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_diff(_slope(_safe_div(cashneq, liabilitiesc + 1.0), 4), 4), 4))
def cg_f005_current_liquidity_core115_3rd_v116_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_diff(_slope(_safe_div(cashneq, assetsc + 1.0), 4), 4), 4))
def cg_f005_current_liquidity_core116_3rd_v117_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_diff(_slope(assetsc - liabilitiesc, 4), 4), 4))
def cg_f005_current_liquidity_core117_3rd_v118_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_diff(_slope(_safe_div(assetsc - liabilitiesc, assetsc + 1.0), 4), 4), 4))
def cg_f005_current_liquidity_core118_3rd_v119_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_diff(_slope(_safe_div(liabilitiesc, assetsc + 1.0), 4), 4), 4))
def cg_f005_current_liquidity_core119_3rd_v120_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_mean(_diff(_slope(_safe_div(cashneq, assetsc - liabilitiesc + 1.0), 4), 4), 4))

def cg_f005_current_liquidity_core120_3rd_v121_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_diff(_diff(currentratio, 4), 4), 4))
def cg_f005_current_liquidity_core121_3rd_v122_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_diff(_diff(assetsc, 4), 4), 4))
def cg_f005_current_liquidity_core122_3rd_v123_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_diff(_diff(liabilitiesc, 4), 4), 4))
def cg_f005_current_liquidity_core123_3rd_v124_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_diff(_diff(cashneq, 4), 4), 4))
def cg_f005_current_liquidity_core124_3rd_v125_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_diff(_diff(_safe_div(cashneq, liabilitiesc + 1.0), 4), 4), 4))
def cg_f005_current_liquidity_core125_3rd_v126_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_diff(_diff(_safe_div(cashneq, assetsc + 1.0), 4), 4), 4))
def cg_f005_current_liquidity_core126_3rd_v127_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_diff(_diff(assetsc - liabilitiesc, 4), 4), 4))
def cg_f005_current_liquidity_core127_3rd_v128_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_diff(_diff(_safe_div(assetsc - liabilitiesc, assetsc + 1.0), 4), 4), 4))
def cg_f005_current_liquidity_core128_3rd_v129_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_diff(_diff(_safe_div(liabilitiesc, assetsc + 1.0), 4), 4), 4))
def cg_f005_current_liquidity_core129_3rd_v130_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_slope(_diff(_diff(_safe_div(cashneq, assetsc - liabilitiesc + 1.0), 4), 4), 4))

def cg_f005_current_liquidity_core130_3rd_v131_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(_diff(_diff(currentratio, 4), 4), 4))
def cg_f005_current_liquidity_core131_3rd_v132_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(_diff(_diff(assetsc, 4), 4), 4))
def cg_f005_current_liquidity_core132_3rd_v133_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(_diff(_diff(liabilitiesc, 4), 4), 4))
def cg_f005_current_liquidity_core133_3rd_v134_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(_diff(_diff(cashneq, 4), 4), 4))
def cg_f005_current_liquidity_core134_3rd_v135_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(_diff(_diff(_safe_div(cashneq, liabilitiesc + 1.0), 4), 4), 4))
def cg_f005_current_liquidity_core135_3rd_v136_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(_diff(_diff(_safe_div(cashneq, assetsc + 1.0), 4), 4), 4))
def cg_f005_current_liquidity_core136_3rd_v137_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(_diff(_diff(assetsc - liabilitiesc, 4), 4), 4))
def cg_f005_current_liquidity_core137_3rd_v138_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(_diff(_diff(_safe_div(assetsc - liabilitiesc, assetsc + 1.0), 4), 4), 4))
def cg_f005_current_liquidity_core138_3rd_v139_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(_diff(_diff(_safe_div(liabilitiesc, assetsc + 1.0), 4), 4), 4))
def cg_f005_current_liquidity_core139_3rd_v140_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_diff(_diff(_diff(_safe_div(cashneq, assetsc - liabilitiesc + 1.0), 4), 4), 4))

def cg_f005_current_liquidity_core140_3rd_v141_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_slope(_diff(_diff(currentratio, 4), 4), 4), 8))
def cg_f005_current_liquidity_core141_3rd_v142_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_slope(_diff(_diff(assetsc, 4), 4), 4), 8))
def cg_f005_current_liquidity_core142_3rd_v143_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_slope(_diff(_diff(liabilitiesc, 4), 4), 4), 8))
def cg_f005_current_liquidity_core143_3rd_v144_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_slope(_diff(_diff(cashneq, 4), 4), 4), 8))
def cg_f005_current_liquidity_core144_3rd_v145_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_slope(_diff(_diff(_safe_div(cashneq, liabilitiesc + 1.0), 4), 4), 4), 8))
def cg_f005_current_liquidity_core145_3rd_v146_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_slope(_diff(_diff(_safe_div(cashneq, assetsc + 1.0), 4), 4), 4), 8))
def cg_f005_current_liquidity_core146_3rd_v147_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_slope(_diff(_diff(assetsc - liabilitiesc, 4), 4), 4), 8))
def cg_f005_current_liquidity_core147_3rd_v148_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_slope(_diff(_diff(_safe_div(assetsc - liabilitiesc, assetsc + 1.0), 4), 4), 4), 8))
def cg_f005_current_liquidity_core148_3rd_v149_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_slope(_diff(_diff(_safe_div(liabilitiesc, assetsc + 1.0), 4), 4), 4), 8))
def cg_f005_current_liquidity_core149_3rd_v150_signal(currentratio, assetsc, liabilitiesc, cashneq):
    return _clean(_z(_slope(_diff(_diff(_safe_div(cashneq, assetsc - liabilitiesc + 1.0), 4), 4), 4), 8))
