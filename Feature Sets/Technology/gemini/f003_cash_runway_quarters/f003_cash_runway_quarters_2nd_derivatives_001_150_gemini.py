import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f003_cash_runway_quarters_core00_2nd_v001_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_slope(cashneq, 4))
def cg_f003_cash_runway_quarters_core01_2nd_v002_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_slope(investmentsc, 4))
def cg_f003_cash_runway_quarters_core02_2nd_v003_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_slope(ncfo, 4))
def cg_f003_cash_runway_quarters_core03_2nd_v004_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_slope(fcf, 4))
def cg_f003_cash_runway_quarters_core04_2nd_v005_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_slope(cashneq + investmentsc, 4))
def cg_f003_cash_runway_quarters_core05_2nd_v006_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_slope(_safe_div(cashneq + investmentsc, ncfo.abs() + 1.0), 4))
def cg_f003_cash_runway_quarters_core06_2nd_v007_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_slope(_safe_div(cashneq + investmentsc, fcf.abs() + 1.0), 4))
def cg_f003_cash_runway_quarters_core07_2nd_v008_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_slope(_safe_div(ncfo, fcf.abs() + 1.0), 4))
def cg_f003_cash_runway_quarters_core08_2nd_v009_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_slope(_safe_div(cashneq, investmentsc + 1.0), 4))
def cg_f003_cash_runway_quarters_core09_2nd_v010_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_slope(_safe_div(fcf, ncfo.abs() + 1.0), 4))

def cg_f003_cash_runway_quarters_core10_2nd_v011_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_slope(cashneq, 8))
def cg_f003_cash_runway_quarters_core11_2nd_v012_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_slope(investmentsc, 8))
def cg_f003_cash_runway_quarters_core12_2nd_v013_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_slope(ncfo, 8))
def cg_f003_cash_runway_quarters_core13_2nd_v014_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_slope(fcf, 8))
def cg_f003_cash_runway_quarters_core14_2nd_v015_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_slope(cashneq + investmentsc, 8))
def cg_f003_cash_runway_quarters_core15_2nd_v016_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_slope(_safe_div(cashneq + investmentsc, ncfo.abs() + 1.0), 8))
def cg_f003_cash_runway_quarters_core16_2nd_v017_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_slope(_safe_div(cashneq + investmentsc, fcf.abs() + 1.0), 8))
def cg_f003_cash_runway_quarters_core17_2nd_v018_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_slope(_safe_div(ncfo, fcf.abs() + 1.0), 8))
def cg_f003_cash_runway_quarters_core18_2nd_v019_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_slope(_safe_div(cashneq, investmentsc + 1.0), 8))
def cg_f003_cash_runway_quarters_core19_2nd_v020_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_slope(_safe_div(fcf, ncfo.abs() + 1.0), 8))

def cg_f003_cash_runway_quarters_core20_2nd_v021_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_diff(cashneq, 4))
def cg_f003_cash_runway_quarters_core21_2nd_v022_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_diff(investmentsc, 4))
def cg_f003_cash_runway_quarters_core22_2nd_v023_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_diff(ncfo, 4))
def cg_f003_cash_runway_quarters_core23_2nd_v024_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_diff(fcf, 4))
def cg_f003_cash_runway_quarters_core24_2nd_v025_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_diff(cashneq + investmentsc, 4))
def cg_f003_cash_runway_quarters_core25_2nd_v026_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_diff(_safe_div(cashneq + investmentsc, ncfo.abs() + 1.0), 4))
def cg_f003_cash_runway_quarters_core26_2nd_v027_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_diff(_safe_div(cashneq + investmentsc, fcf.abs() + 1.0), 4))
def cg_f003_cash_runway_quarters_core27_2nd_v028_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_diff(_safe_div(ncfo, fcf.abs() + 1.0), 4))
def cg_f003_cash_runway_quarters_core28_2nd_v029_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_diff(_safe_div(cashneq, investmentsc + 1.0), 4))
def cg_f003_cash_runway_quarters_core29_2nd_v030_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_diff(_safe_div(fcf, ncfo.abs() + 1.0), 4))

def cg_f003_cash_runway_quarters_core30_2nd_v031_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_z(_slope(cashneq, 4), 8))
def cg_f003_cash_runway_quarters_core31_2nd_v032_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_z(_slope(investmentsc, 4), 8))
def cg_f003_cash_runway_quarters_core32_2nd_v033_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_z(_slope(ncfo, 4), 8))
def cg_f003_cash_runway_quarters_core33_2nd_v034_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_z(_slope(fcf, 4), 8))
def cg_f003_cash_runway_quarters_core34_2nd_v035_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_z(_slope(cashneq + investmentsc, 4), 8))
def cg_f003_cash_runway_quarters_core35_2nd_v036_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_z(_slope(_safe_div(cashneq + investmentsc, ncfo.abs() + 1.0), 4), 8))
def cg_f003_cash_runway_quarters_core36_2nd_v037_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_z(_slope(_safe_div(cashneq + investmentsc, fcf.abs() + 1.0), 4), 8))
def cg_f003_cash_runway_quarters_core37_2nd_v038_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_z(_slope(_safe_div(ncfo, fcf.abs() + 1.0), 4), 8))
def cg_f003_cash_runway_quarters_core38_2nd_v039_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_z(_slope(_safe_div(cashneq, investmentsc + 1.0), 4), 8))
def cg_f003_cash_runway_quarters_core39_2nd_v040_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_z(_slope(_safe_div(fcf, ncfo.abs() + 1.0), 4), 8))

def cg_f003_cash_runway_quarters_core40_2nd_v041_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_z(_slope(cashneq, 8), 12))
def cg_f003_cash_runway_quarters_core41_2nd_v042_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_z(_slope(investmentsc, 8), 12))
def cg_f003_cash_runway_quarters_core42_2nd_v043_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_z(_slope(ncfo, 8), 12))
def cg_f003_cash_runway_quarters_core43_2nd_v044_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_z(_slope(fcf, 8), 12))
def cg_f003_cash_runway_quarters_core44_2nd_v045_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_z(_slope(cashneq + investmentsc, 8), 12))
def cg_f003_cash_runway_quarters_core45_2nd_v046_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_z(_slope(_safe_div(cashneq + investmentsc, ncfo.abs() + 1.0), 8), 12))
def cg_f003_cash_runway_quarters_core46_2nd_v047_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_z(_slope(_safe_div(cashneq + investmentsc, fcf.abs() + 1.0), 8), 12))
def cg_f003_cash_runway_quarters_core47_2nd_v048_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_z(_slope(_safe_div(ncfo, fcf.abs() + 1.0), 8), 12))
def cg_f003_cash_runway_quarters_core48_2nd_v049_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_z(_slope(_safe_div(cashneq, investmentsc + 1.0), 8), 12))
def cg_f003_cash_runway_quarters_core49_2nd_v050_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_z(_slope(_safe_div(fcf, ncfo.abs() + 1.0), 8), 12))

def cg_f003_cash_runway_quarters_core50_2nd_v051_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_z(_diff(cashneq, 4), 8))
def cg_f003_cash_runway_quarters_core51_2nd_v052_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_z(_diff(investmentsc, 4), 8))
def cg_f003_cash_runway_quarters_core52_2nd_v053_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_z(_diff(ncfo, 4), 8))
def cg_f003_cash_runway_quarters_core53_2nd_v054_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_z(_diff(fcf, 4), 8))
def cg_f003_cash_runway_quarters_core54_2nd_v055_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_z(_diff(cashneq + investmentsc, 4), 8))
def cg_f003_cash_runway_quarters_core55_2nd_v056_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_z(_diff(_safe_div(cashneq + investmentsc, ncfo.abs() + 1.0), 4), 8))
def cg_f003_cash_runway_quarters_core56_2nd_v057_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_z(_diff(_safe_div(cashneq + investmentsc, fcf.abs() + 1.0), 4), 8))
def cg_f003_cash_runway_quarters_core57_2nd_v058_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_z(_diff(_safe_div(ncfo, fcf.abs() + 1.0), 4), 8))
def cg_f003_cash_runway_quarters_core58_2nd_v059_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_z(_diff(_safe_div(cashneq, investmentsc + 1.0), 4), 8))
def cg_f003_cash_runway_quarters_core59_2nd_v060_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_z(_diff(_safe_div(fcf, ncfo.abs() + 1.0), 4), 8))

def cg_f003_cash_runway_quarters_core60_2nd_v061_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_rank(_slope(cashneq, 4), 12))
def cg_f003_cash_runway_quarters_core61_2nd_v062_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_rank(_slope(investmentsc, 4), 12))
def cg_f003_cash_runway_quarters_core62_2nd_v063_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_rank(_slope(ncfo, 4), 12))
def cg_f003_cash_runway_quarters_core63_2nd_v064_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_rank(_slope(fcf, 4), 12))
def cg_f003_cash_runway_quarters_core64_2nd_v065_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_rank(_slope(cashneq + investmentsc, 4), 12))
def cg_f003_cash_runway_quarters_core65_2nd_v066_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_rank(_slope(_safe_div(cashneq + investmentsc, ncfo.abs() + 1.0), 4), 12))
def cg_f003_cash_runway_quarters_core66_2nd_v067_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_rank(_slope(_safe_div(cashneq + investmentsc, fcf.abs() + 1.0), 4), 12))
def cg_f003_cash_runway_quarters_core67_2nd_v068_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_rank(_slope(_safe_div(ncfo, fcf.abs() + 1.0), 4), 12))
def cg_f003_cash_runway_quarters_core68_2nd_v069_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_rank(_slope(_safe_div(cashneq, investmentsc + 1.0), 4), 12))
def cg_f003_cash_runway_quarters_core69_2nd_v070_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_rank(_slope(_safe_div(fcf, ncfo.abs() + 1.0), 4), 12))

def cg_f003_cash_runway_quarters_core70_2nd_v071_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_rank(_diff(cashneq, 4), 12))
def cg_f003_cash_runway_quarters_core71_2nd_v072_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_rank(_diff(investmentsc, 4), 12))
def cg_f003_cash_runway_quarters_core72_2nd_v073_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_rank(_diff(ncfo, 4), 12))
def cg_f003_cash_runway_quarters_core73_2nd_v074_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_rank(_diff(fcf, 4), 12))
def cg_f003_cash_runway_quarters_core74_2nd_v075_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_rank(_diff(cashneq + investmentsc, 4), 12))
def cg_f003_cash_runway_quarters_core75_2nd_v076_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_rank(_diff(_safe_div(cashneq + investmentsc, ncfo.abs() + 1.0), 4), 12))
def cg_f003_cash_runway_quarters_core76_2nd_v077_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_rank(_diff(_safe_div(cashneq + investmentsc, fcf.abs() + 1.0), 4), 12))
def cg_f003_cash_runway_quarters_core77_2nd_v078_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_rank(_diff(_safe_div(ncfo, fcf.abs() + 1.0), 4), 12))
def cg_f003_cash_runway_quarters_core78_2nd_v079_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_rank(_diff(_safe_div(cashneq, investmentsc + 1.0), 4), 12))
def cg_f003_cash_runway_quarters_core79_2nd_v080_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_rank(_diff(_safe_div(fcf, ncfo.abs() + 1.0), 4), 12))

def cg_f003_cash_runway_quarters_core80_2nd_v081_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_mean(_slope(cashneq, 4), 4))
def cg_f003_cash_runway_quarters_core81_2nd_v082_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_mean(_slope(investmentsc, 4), 4))
def cg_f003_cash_runway_quarters_core82_2nd_v083_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_mean(_slope(ncfo, 4), 4))
def cg_f003_cash_runway_quarters_core83_2nd_v084_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_mean(_slope(fcf, 4), 4))
def cg_f003_cash_runway_quarters_core84_2nd_v085_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_mean(_slope(cashneq + investmentsc, 4), 4))
def cg_f003_cash_runway_quarters_core85_2nd_v086_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_mean(_slope(_safe_div(cashneq + investmentsc, ncfo.abs() + 1.0), 4), 4))
def cg_f003_cash_runway_quarters_core86_2nd_v087_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_mean(_slope(_safe_div(cashneq + investmentsc, fcf.abs() + 1.0), 4), 4))
def cg_f003_cash_runway_quarters_core87_2nd_v088_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_mean(_slope(_safe_div(ncfo, fcf.abs() + 1.0), 4), 4))
def cg_f003_cash_runway_quarters_core88_2nd_v089_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_mean(_slope(_safe_div(cashneq, investmentsc + 1.0), 4), 4))
def cg_f003_cash_runway_quarters_core89_2nd_v090_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_mean(_slope(_safe_div(fcf, ncfo.abs() + 1.0), 4), 4))

def cg_f003_cash_runway_quarters_core90_2nd_v091_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_mean(_diff(cashneq, 4), 4))
def cg_f003_cash_runway_quarters_core91_2nd_v092_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_mean(_diff(investmentsc, 4), 4))
def cg_f003_cash_runway_quarters_core92_2nd_v093_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_mean(_diff(ncfo, 4), 4))
def cg_f003_cash_runway_quarters_core93_2nd_v094_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_mean(_diff(fcf, 4), 4))
def cg_f003_cash_runway_quarters_core94_2nd_v095_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_mean(_diff(cashneq + investmentsc, 4), 4))
def cg_f003_cash_runway_quarters_core95_2nd_v096_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_mean(_diff(_safe_div(cashneq + investmentsc, ncfo.abs() + 1.0), 4), 4))
def cg_f003_cash_runway_quarters_core96_2nd_v097_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_mean(_diff(_safe_div(cashneq + investmentsc, fcf.abs() + 1.0), 4), 4))
def cg_f003_cash_runway_quarters_core97_2nd_v098_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_mean(_diff(_safe_div(ncfo, fcf.abs() + 1.0), 4), 4))
def cg_f003_cash_runway_quarters_core98_2nd_v099_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_mean(_diff(_safe_div(cashneq, investmentsc + 1.0), 4), 4))
def cg_f003_cash_runway_quarters_core99_2nd_v100_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_mean(_diff(_safe_div(fcf, ncfo.abs() + 1.0), 4), 4))

def cg_f003_cash_runway_quarters_core100_2nd_v101_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_slope(_mean(cashneq, 4), 4))
def cg_f003_cash_runway_quarters_core101_2nd_v102_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_slope(_mean(investmentsc, 4), 4))
def cg_f003_cash_runway_quarters_core102_2nd_v103_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_slope(_mean(ncfo, 4), 4))
def cg_f003_cash_runway_quarters_core103_2nd_v104_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_slope(_mean(fcf, 4), 4))
def cg_f003_cash_runway_quarters_core104_2nd_v105_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_slope(_mean(cashneq + investmentsc, 4), 4))
def cg_f003_cash_runway_quarters_core105_2nd_v106_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_slope(_mean(_safe_div(cashneq + investmentsc, ncfo.abs() + 1.0), 4), 4))
def cg_f003_cash_runway_quarters_core106_2nd_v107_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_slope(_mean(_safe_div(cashneq + investmentsc, fcf.abs() + 1.0), 4), 4))
def cg_f003_cash_runway_quarters_core107_2nd_v108_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_slope(_mean(_safe_div(ncfo, fcf.abs() + 1.0), 4), 4))
def cg_f003_cash_runway_quarters_core108_2nd_v109_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_slope(_mean(_safe_div(cashneq, investmentsc + 1.0), 4), 4))
def cg_f003_cash_runway_quarters_core109_2nd_v110_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_slope(_mean(_safe_div(fcf, ncfo.abs() + 1.0), 4), 4))

def cg_f003_cash_runway_quarters_core110_2nd_v111_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_slope(_mean(cashneq, 8), 8))
def cg_f003_cash_runway_quarters_core111_2nd_v112_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_slope(_mean(investmentsc, 8), 8))
def cg_f003_cash_runway_quarters_core112_2nd_v113_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_slope(_mean(ncfo, 8), 8))
def cg_f003_cash_runway_quarters_core113_2nd_v114_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_slope(_mean(fcf, 8), 8))
def cg_f003_cash_runway_quarters_core114_2nd_v115_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_slope(_mean(cashneq + investmentsc, 8), 8))
def cg_f003_cash_runway_quarters_core115_2nd_v116_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_slope(_mean(_safe_div(cashneq + investmentsc, ncfo.abs() + 1.0), 8), 8))
def cg_f003_cash_runway_quarters_core116_2nd_v117_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_slope(_mean(_safe_div(cashneq + investmentsc, fcf.abs() + 1.0), 8), 8))
def cg_f003_cash_runway_quarters_core117_2nd_v118_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_slope(_mean(_safe_div(ncfo, fcf.abs() + 1.0), 8), 8))
def cg_f003_cash_runway_quarters_core118_2nd_v119_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_slope(_mean(_safe_div(cashneq, investmentsc + 1.0), 8), 8))
def cg_f003_cash_runway_quarters_core119_2nd_v120_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_slope(_mean(_safe_div(fcf, ncfo.abs() + 1.0), 8), 8))

def cg_f003_cash_runway_quarters_core120_2nd_v121_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_diff(_mean(cashneq, 4), 4))
def cg_f003_cash_runway_quarters_core121_2nd_v122_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_diff(_mean(investmentsc, 4), 4))
def cg_f003_cash_runway_quarters_core122_2nd_v123_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_diff(_mean(ncfo, 4), 4))
def cg_f003_cash_runway_quarters_core123_2nd_v124_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_diff(_mean(fcf, 4), 4))
def cg_f003_cash_runway_quarters_core124_2nd_v125_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_diff(_mean(cashneq + investmentsc, 4), 4))
def cg_f003_cash_runway_quarters_core125_2nd_v126_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_diff(_mean(_safe_div(cashneq + investmentsc, ncfo.abs() + 1.0), 4), 4))
def cg_f003_cash_runway_quarters_core126_2nd_v127_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_diff(_mean(_safe_div(cashneq + investmentsc, fcf.abs() + 1.0), 4), 4))
def cg_f003_cash_runway_quarters_core127_2nd_v128_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_diff(_mean(_safe_div(ncfo, fcf.abs() + 1.0), 4), 4))
def cg_f003_cash_runway_quarters_core128_2nd_v129_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_diff(_mean(_safe_div(cashneq, investmentsc + 1.0), 4), 4))
def cg_f003_cash_runway_quarters_core129_2nd_v130_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_diff(_mean(_safe_div(fcf, ncfo.abs() + 1.0), 4), 4))

def cg_f003_cash_runway_quarters_core130_2nd_v131_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_z(_diff(_mean(cashneq, 4), 4), 8))
def cg_f003_cash_runway_quarters_core131_2nd_v132_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_z(_diff(_mean(investmentsc, 4), 4), 8))
def cg_f003_cash_runway_quarters_core132_2nd_v133_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_z(_diff(_mean(ncfo, 4), 4), 8))
def cg_f003_cash_runway_quarters_core133_2nd_v134_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_z(_diff(_mean(fcf, 4), 4), 8))
def cg_f003_cash_runway_quarters_core134_2nd_v135_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_z(_diff(_mean(cashneq + investmentsc, 4), 4), 8))
def cg_f003_cash_runway_quarters_core135_2nd_v136_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_z(_diff(_mean(_safe_div(cashneq + investmentsc, ncfo.abs() + 1.0), 4), 4), 8))
def cg_f003_cash_runway_quarters_core136_2nd_v137_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_z(_diff(_mean(_safe_div(cashneq + investmentsc, fcf.abs() + 1.0), 4), 4), 8))
def cg_f003_cash_runway_quarters_core137_2nd_v138_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_z(_diff(_mean(_safe_div(ncfo, fcf.abs() + 1.0), 4), 4), 8))
def cg_f003_cash_runway_quarters_core138_2nd_v139_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_z(_diff(_mean(_safe_div(cashneq, investmentsc + 1.0), 4), 4), 8))
def cg_f003_cash_runway_quarters_core139_2nd_v140_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_z(_diff(_mean(_safe_div(fcf, ncfo.abs() + 1.0), 4), 4), 8))

def cg_f003_cash_runway_quarters_core140_2nd_v141_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_rank(_slope(_mean(cashneq, 4), 4), 12))
def cg_f003_cash_runway_quarters_core141_2nd_v142_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_rank(_slope(_mean(investmentsc, 4), 4), 12))
def cg_f003_cash_runway_quarters_core142_2nd_v143_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_rank(_slope(_mean(ncfo, 4), 4), 12))
def cg_f003_cash_runway_quarters_core143_2nd_v144_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_rank(_slope(_mean(fcf, 4), 4), 12))
def cg_f003_cash_runway_quarters_core144_2nd_v145_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_rank(_slope(_mean(cashneq + investmentsc, 4), 4), 12))
def cg_f003_cash_runway_quarters_core145_2nd_v146_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_rank(_slope(_mean(_safe_div(cashneq + investmentsc, ncfo.abs() + 1.0), 4), 4), 12))
def cg_f003_cash_runway_quarters_core146_2nd_v147_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_rank(_slope(_mean(_safe_div(cashneq + investmentsc, fcf.abs() + 1.0), 4), 4), 12))
def cg_f003_cash_runway_quarters_core147_2nd_v148_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_rank(_slope(_mean(_safe_div(ncfo, fcf.abs() + 1.0), 4), 4), 12))
def cg_f003_cash_runway_quarters_core148_2nd_v149_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_rank(_slope(_mean(_safe_div(cashneq, investmentsc + 1.0), 4), 4), 12))
def cg_f003_cash_runway_quarters_core149_2nd_v150_signal(cashneq, investmentsc, ncfo, fcf):
    return _clean(_rank(_slope(_mean(_safe_div(fcf, ncfo.abs() + 1.0), 4), 4), 12))
