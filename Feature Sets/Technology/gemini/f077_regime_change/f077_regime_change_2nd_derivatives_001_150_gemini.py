import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f077_regime_change_core00_2nd_v001_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(revenue, 4))
def cg_f077_regime_change_core01_2nd_v002_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(rnd, 4))
def cg_f077_regime_change_core02_2nd_v003_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(ncfo, 4))
def cg_f077_regime_change_core03_2nd_v004_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(opex, 4))
def cg_f077_regime_change_core04_2nd_v005_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(cashneq, 4))
def cg_f077_regime_change_core05_2nd_v006_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(fcf, 4))
def cg_f077_regime_change_core06_2nd_v007_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(_safe_div(revenue, opex), 4))
def cg_f077_regime_change_core07_2nd_v008_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(_safe_div(ncfo, cashneq.abs() + 1.0), 4))
def cg_f077_regime_change_core08_2nd_v009_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(_safe_div(fcf, revenue), 4))
def cg_f077_regime_change_core09_2nd_v010_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(_safe_div(rnd, opex), 4))
def cg_f077_regime_change_core10_2nd_v011_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(revenue, 8))
def cg_f077_regime_change_core11_2nd_v012_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(rnd, 8))
def cg_f077_regime_change_core12_2nd_v013_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(ncfo, 8))
def cg_f077_regime_change_core13_2nd_v014_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(opex, 8))
def cg_f077_regime_change_core14_2nd_v015_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(cashneq, 8))
def cg_f077_regime_change_core15_2nd_v016_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(fcf, 8))
def cg_f077_regime_change_core16_2nd_v017_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(_safe_div(revenue, opex), 8))
def cg_f077_regime_change_core17_2nd_v018_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(_safe_div(ncfo, cashneq.abs() + 1.0), 8))
def cg_f077_regime_change_core18_2nd_v019_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(_safe_div(fcf, revenue), 8))
def cg_f077_regime_change_core19_2nd_v020_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(_safe_div(rnd, opex), 8))
def cg_f077_regime_change_core20_2nd_v021_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_diff(revenue, 4))
def cg_f077_regime_change_core21_2nd_v022_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_diff(rnd, 4))
def cg_f077_regime_change_core22_2nd_v023_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_diff(ncfo, 4))
def cg_f077_regime_change_core23_2nd_v024_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_diff(opex, 4))
def cg_f077_regime_change_core24_2nd_v025_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_diff(cashneq, 4))
def cg_f077_regime_change_core25_2nd_v026_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_diff(fcf, 4))
def cg_f077_regime_change_core26_2nd_v027_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_diff(_safe_div(revenue, opex), 4))
def cg_f077_regime_change_core27_2nd_v028_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_diff(_safe_div(ncfo, cashneq.abs() + 1.0), 4))
def cg_f077_regime_change_core28_2nd_v029_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_diff(_safe_div(fcf, revenue), 4))
def cg_f077_regime_change_core29_2nd_v030_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_diff(_safe_div(rnd, opex), 4))
def cg_f077_regime_change_core30_2nd_v031_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(_slope(revenue, 4), 8))
def cg_f077_regime_change_core31_2nd_v032_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(_slope(rnd, 4), 8))
def cg_f077_regime_change_core32_2nd_v033_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(_slope(ncfo, 4), 8))
def cg_f077_regime_change_core33_2nd_v034_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(_slope(opex, 4), 8))
def cg_f077_regime_change_core34_2nd_v035_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(_slope(cashneq, 4), 8))
def cg_f077_regime_change_core35_2nd_v036_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(_slope(fcf, 4), 8))
def cg_f077_regime_change_core36_2nd_v037_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(_slope(_safe_div(revenue, opex), 4), 8))
def cg_f077_regime_change_core37_2nd_v038_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(_slope(_safe_div(ncfo, cashneq.abs() + 1.0), 4), 8))
def cg_f077_regime_change_core38_2nd_v039_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(_slope(_safe_div(fcf, revenue), 4), 8))
def cg_f077_regime_change_core39_2nd_v040_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(_slope(_safe_div(rnd, opex), 4), 8))
def cg_f077_regime_change_core40_2nd_v041_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(_slope(revenue, 8), 12))
def cg_f077_regime_change_core41_2nd_v042_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(_slope(rnd, 8), 12))
def cg_f077_regime_change_core42_2nd_v043_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(_slope(ncfo, 8), 12))
def cg_f077_regime_change_core43_2nd_v044_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(_slope(opex, 8), 12))
def cg_f077_regime_change_core44_2nd_v045_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(_slope(cashneq, 8), 12))
def cg_f077_regime_change_core45_2nd_v046_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(_slope(fcf, 8), 12))
def cg_f077_regime_change_core46_2nd_v047_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(_slope(_safe_div(revenue, opex), 8), 12))
def cg_f077_regime_change_core47_2nd_v048_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(_slope(_safe_div(ncfo, cashneq.abs() + 1.0), 8), 12))
def cg_f077_regime_change_core48_2nd_v049_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(_slope(_safe_div(fcf, revenue), 8), 12))
def cg_f077_regime_change_core49_2nd_v050_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(_slope(_safe_div(rnd, opex), 8), 12))
def cg_f077_regime_change_core50_2nd_v051_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(_diff(revenue, 4), 8))
def cg_f077_regime_change_core51_2nd_v052_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(_diff(rnd, 4), 8))
def cg_f077_regime_change_core52_2nd_v053_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(_diff(ncfo, 4), 8))
def cg_f077_regime_change_core53_2nd_v054_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(_diff(opex, 4), 8))
def cg_f077_regime_change_core54_2nd_v055_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(_diff(cashneq, 4), 8))
def cg_f077_regime_change_core55_2nd_v056_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(_diff(fcf, 4), 8))
def cg_f077_regime_change_core56_2nd_v057_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(_diff(_safe_div(revenue, opex), 4), 8))
def cg_f077_regime_change_core57_2nd_v058_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(_diff(_safe_div(ncfo, cashneq.abs() + 1.0), 4), 8))
def cg_f077_regime_change_core58_2nd_v059_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(_diff(_safe_div(fcf, revenue), 4), 8))
def cg_f077_regime_change_core59_2nd_v060_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(_diff(_safe_div(rnd, opex), 4), 8))
def cg_f077_regime_change_core60_2nd_v061_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(_slope(revenue, 4), 12))
def cg_f077_regime_change_core61_2nd_v062_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(_slope(rnd, 4), 12))
def cg_f077_regime_change_core62_2nd_v063_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(_slope(ncfo, 4), 12))
def cg_f077_regime_change_core63_2nd_v064_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(_slope(opex, 4), 12))
def cg_f077_regime_change_core64_2nd_v065_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(_slope(cashneq, 4), 12))
def cg_f077_regime_change_core65_2nd_v066_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(_slope(fcf, 4), 12))
def cg_f077_regime_change_core66_2nd_v067_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(_slope(_safe_div(revenue, opex), 4), 12))
def cg_f077_regime_change_core67_2nd_v068_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(_slope(_safe_div(ncfo, cashneq.abs() + 1.0), 4), 12))
def cg_f077_regime_change_core68_2nd_v069_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(_slope(_safe_div(fcf, revenue), 4), 12))
def cg_f077_regime_change_core69_2nd_v070_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(_slope(_safe_div(rnd, opex), 4), 12))
def cg_f077_regime_change_core70_2nd_v071_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(_diff(revenue, 4), 12))
def cg_f077_regime_change_core71_2nd_v072_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(_diff(rnd, 4), 12))
def cg_f077_regime_change_core72_2nd_v073_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(_diff(ncfo, 4), 12))
def cg_f077_regime_change_core73_2nd_v074_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(_diff(opex, 4), 12))
def cg_f077_regime_change_core74_2nd_v075_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(_diff(cashneq, 4), 12))
def cg_f077_regime_change_core75_2nd_v076_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(_diff(fcf, 4), 12))
def cg_f077_regime_change_core76_2nd_v077_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(_diff(_safe_div(revenue, opex), 4), 12))
def cg_f077_regime_change_core77_2nd_v078_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(_diff(_safe_div(ncfo, cashneq.abs() + 1.0), 4), 12))
def cg_f077_regime_change_core78_2nd_v079_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(_diff(_safe_div(fcf, revenue), 4), 12))
def cg_f077_regime_change_core79_2nd_v080_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(_diff(_safe_div(rnd, opex), 4), 12))
def cg_f077_regime_change_core80_2nd_v081_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_mean(_slope(revenue, 4), 4))
def cg_f077_regime_change_core81_2nd_v082_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_mean(_slope(rnd, 4), 4))
def cg_f077_regime_change_core82_2nd_v083_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_mean(_slope(ncfo, 4), 4))
def cg_f077_regime_change_core83_2nd_v084_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_mean(_slope(opex, 4), 4))
def cg_f077_regime_change_core84_2nd_v085_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_mean(_slope(cashneq, 4), 4))
def cg_f077_regime_change_core85_2nd_v086_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_mean(_slope(fcf, 4), 4))
def cg_f077_regime_change_core86_2nd_v087_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_mean(_slope(_safe_div(revenue, opex), 4), 4))
def cg_f077_regime_change_core87_2nd_v088_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_mean(_slope(_safe_div(ncfo, cashneq.abs() + 1.0), 4), 4))
def cg_f077_regime_change_core88_2nd_v089_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_mean(_slope(_safe_div(fcf, revenue), 4), 4))
def cg_f077_regime_change_core89_2nd_v090_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_mean(_slope(_safe_div(rnd, opex), 4), 4))
def cg_f077_regime_change_core90_2nd_v091_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_mean(_diff(revenue, 4), 4))
def cg_f077_regime_change_core91_2nd_v092_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_mean(_diff(rnd, 4), 4))
def cg_f077_regime_change_core92_2nd_v093_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_mean(_diff(ncfo, 4), 4))
def cg_f077_regime_change_core93_2nd_v094_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_mean(_diff(opex, 4), 4))
def cg_f077_regime_change_core94_2nd_v095_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_mean(_diff(cashneq, 4), 4))
def cg_f077_regime_change_core95_2nd_v096_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_mean(_diff(fcf, 4), 4))
def cg_f077_regime_change_core96_2nd_v097_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_mean(_diff(_safe_div(revenue, opex), 4), 4))
def cg_f077_regime_change_core97_2nd_v098_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_mean(_diff(_safe_div(ncfo, cashneq.abs() + 1.0), 4), 4))
def cg_f077_regime_change_core98_2nd_v099_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_mean(_diff(_safe_div(fcf, revenue), 4), 4))
def cg_f077_regime_change_core99_2nd_v100_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_mean(_diff(_safe_div(rnd, opex), 4), 4))
def cg_f077_regime_change_core100_2nd_v101_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(_mean(revenue, 4), 4))
def cg_f077_regime_change_core101_2nd_v102_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(_mean(rnd, 4), 4))
def cg_f077_regime_change_core102_2nd_v103_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(_mean(ncfo, 4), 4))
def cg_f077_regime_change_core103_2nd_v104_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(_mean(opex, 4), 4))
def cg_f077_regime_change_core104_2nd_v105_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(_mean(cashneq, 4), 4))
def cg_f077_regime_change_core105_2nd_v106_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(_mean(fcf, 4), 4))
def cg_f077_regime_change_core106_2nd_v107_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(_mean(_safe_div(revenue, opex), 4), 4))
def cg_f077_regime_change_core107_2nd_v108_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(_mean(_safe_div(ncfo, cashneq.abs() + 1.0), 4), 4))
def cg_f077_regime_change_core108_2nd_v109_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(_mean(_safe_div(fcf, revenue), 4), 4))
def cg_f077_regime_change_core109_2nd_v110_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(_mean(_safe_div(rnd, opex), 4), 4))
def cg_f077_regime_change_core110_2nd_v111_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(_mean(revenue, 8), 8))
def cg_f077_regime_change_core111_2nd_v112_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(_mean(rnd, 8), 8))
def cg_f077_regime_change_core112_2nd_v113_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(_mean(ncfo, 8), 8))
def cg_f077_regime_change_core113_2nd_v114_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(_mean(opex, 8), 8))
def cg_f077_regime_change_core114_2nd_v115_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(_mean(cashneq, 8), 8))
def cg_f077_regime_change_core115_2nd_v116_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(_mean(fcf, 8), 8))
def cg_f077_regime_change_core116_2nd_v117_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(_mean(_safe_div(revenue, opex), 8), 8))
def cg_f077_regime_change_core117_2nd_v118_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(_mean(_safe_div(ncfo, cashneq.abs() + 1.0), 8), 8))
def cg_f077_regime_change_core118_2nd_v119_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(_mean(_safe_div(fcf, revenue), 8), 8))
def cg_f077_regime_change_core119_2nd_v120_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(_mean(_safe_div(rnd, opex), 8), 8))
def cg_f077_regime_change_core120_2nd_v121_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_diff(_mean(revenue, 4), 4))
def cg_f077_regime_change_core121_2nd_v122_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_diff(_mean(rnd, 4), 4))
def cg_f077_regime_change_core122_2nd_v123_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_diff(_mean(ncfo, 4), 4))
def cg_f077_regime_change_core123_2nd_v124_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_diff(_mean(opex, 4), 4))
def cg_f077_regime_change_core124_2nd_v125_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_diff(_mean(cashneq, 4), 4))
def cg_f077_regime_change_core125_2nd_v126_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_diff(_mean(fcf, 4), 4))
def cg_f077_regime_change_core126_2nd_v127_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_diff(_mean(_safe_div(revenue, opex), 4), 4))
def cg_f077_regime_change_core127_2nd_v128_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_diff(_mean(_safe_div(ncfo, cashneq.abs() + 1.0), 4), 4))
def cg_f077_regime_change_core128_2nd_v129_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_diff(_mean(_safe_div(fcf, revenue), 4), 4))
def cg_f077_regime_change_core129_2nd_v130_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_diff(_mean(_safe_div(rnd, opex), 4), 4))
def cg_f077_regime_change_core130_2nd_v131_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(_diff(_mean(revenue, 4), 4), 8))
def cg_f077_regime_change_core131_2nd_v132_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(_diff(_mean(rnd, 4), 4), 8))
def cg_f077_regime_change_core132_2nd_v133_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(_diff(_mean(ncfo, 4), 4), 8))
def cg_f077_regime_change_core133_2nd_v134_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(_diff(_mean(opex, 4), 4), 8))
def cg_f077_regime_change_core134_2nd_v135_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(_diff(_mean(cashneq, 4), 4), 8))
def cg_f077_regime_change_core135_2nd_v136_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(_diff(_mean(fcf, 4), 4), 8))
def cg_f077_regime_change_core136_2nd_v137_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(_diff(_mean(_safe_div(revenue, opex), 4), 4), 8))
def cg_f077_regime_change_core137_2nd_v138_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(_diff(_mean(_safe_div(ncfo, cashneq.abs() + 1.0), 4), 4), 8))
def cg_f077_regime_change_core138_2nd_v139_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(_diff(_mean(_safe_div(fcf, revenue), 4), 4), 8))
def cg_f077_regime_change_core139_2nd_v140_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(_diff(_mean(_safe_div(rnd, opex), 4), 4), 8))
def cg_f077_regime_change_core140_2nd_v141_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(_slope(_mean(revenue, 4), 4), 12))
def cg_f077_regime_change_core141_2nd_v142_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(_slope(_mean(rnd, 4), 4), 12))
def cg_f077_regime_change_core142_2nd_v143_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(_slope(_mean(ncfo, 4), 4), 12))
def cg_f077_regime_change_core143_2nd_v144_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(_slope(_mean(opex, 4), 4), 12))
def cg_f077_regime_change_core144_2nd_v145_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(_slope(_mean(cashneq, 4), 4), 12))
def cg_f077_regime_change_core145_2nd_v146_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(_slope(_mean(fcf, 4), 4), 12))
def cg_f077_regime_change_core146_2nd_v147_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(_slope(_mean(_safe_div(revenue, opex), 4), 4), 12))
def cg_f077_regime_change_core147_2nd_v148_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(_slope(_mean(_safe_div(ncfo, cashneq.abs() + 1.0), 4), 4), 12))
def cg_f077_regime_change_core148_2nd_v149_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(_slope(_mean(_safe_div(fcf, revenue), 4), 4), 12))
def cg_f077_regime_change_core149_2nd_v150_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(_slope(_mean(_safe_div(rnd, opex), 4), 4), 12))