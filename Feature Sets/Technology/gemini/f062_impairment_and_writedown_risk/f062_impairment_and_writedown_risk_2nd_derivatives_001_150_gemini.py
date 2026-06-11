import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f062_impairment_and_writedown_risk_core00_2nd_v001_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(intangibles, 4))
def cg_f062_impairment_and_writedown_risk_core01_2nd_v002_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(depamor, 4))
def cg_f062_impairment_and_writedown_risk_core02_2nd_v003_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(assets, 4))
def cg_f062_impairment_and_writedown_risk_core03_2nd_v004_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(opex, 4))
def cg_f062_impairment_and_writedown_risk_core04_2nd_v005_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(_safe_div(intangibles, assets), 4))
def cg_f062_impairment_and_writedown_risk_core05_2nd_v006_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(_safe_div(depamor, opex), 4))
def cg_f062_impairment_and_writedown_risk_core06_2nd_v007_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(_safe_div(depamor, intangibles.abs() + 1.0), 4))
def cg_f062_impairment_and_writedown_risk_core07_2nd_v008_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(_safe_div(intangibles + depamor, assets), 4))
def cg_f062_impairment_and_writedown_risk_core08_2nd_v009_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(_diff(intangibles, 4), 4))
def cg_f062_impairment_and_writedown_risk_core09_2nd_v010_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(_z(_safe_div(intangibles, assets), 8), 4))
def cg_f062_impairment_and_writedown_risk_core10_2nd_v011_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(intangibles, 8))
def cg_f062_impairment_and_writedown_risk_core11_2nd_v012_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(depamor, 8))
def cg_f062_impairment_and_writedown_risk_core12_2nd_v013_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(assets, 8))
def cg_f062_impairment_and_writedown_risk_core13_2nd_v014_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(opex, 8))
def cg_f062_impairment_and_writedown_risk_core14_2nd_v015_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(_safe_div(intangibles, assets), 8))
def cg_f062_impairment_and_writedown_risk_core15_2nd_v016_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(_safe_div(depamor, opex), 8))
def cg_f062_impairment_and_writedown_risk_core16_2nd_v017_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(_safe_div(depamor, intangibles.abs() + 1.0), 8))
def cg_f062_impairment_and_writedown_risk_core17_2nd_v018_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(_safe_div(intangibles + depamor, assets), 8))
def cg_f062_impairment_and_writedown_risk_core18_2nd_v019_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(_diff(intangibles, 4), 8))
def cg_f062_impairment_and_writedown_risk_core19_2nd_v020_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(_z(_safe_div(intangibles, assets), 8), 8))
def cg_f062_impairment_and_writedown_risk_core20_2nd_v021_signal(intangibles, depamor, assets, opex):
    return _clean(_diff(intangibles, 4))
def cg_f062_impairment_and_writedown_risk_core21_2nd_v022_signal(intangibles, depamor, assets, opex):
    return _clean(_diff(depamor, 4))
def cg_f062_impairment_and_writedown_risk_core22_2nd_v023_signal(intangibles, depamor, assets, opex):
    return _clean(_diff(assets, 4))
def cg_f062_impairment_and_writedown_risk_core23_2nd_v024_signal(intangibles, depamor, assets, opex):
    return _clean(_diff(opex, 4))
def cg_f062_impairment_and_writedown_risk_core24_2nd_v025_signal(intangibles, depamor, assets, opex):
    return _clean(_diff(_safe_div(intangibles, assets), 4))
def cg_f062_impairment_and_writedown_risk_core25_2nd_v026_signal(intangibles, depamor, assets, opex):
    return _clean(_diff(_safe_div(depamor, opex), 4))
def cg_f062_impairment_and_writedown_risk_core26_2nd_v027_signal(intangibles, depamor, assets, opex):
    return _clean(_diff(_safe_div(depamor, intangibles.abs() + 1.0), 4))
def cg_f062_impairment_and_writedown_risk_core27_2nd_v028_signal(intangibles, depamor, assets, opex):
    return _clean(_diff(_safe_div(intangibles + depamor, assets), 4))
def cg_f062_impairment_and_writedown_risk_core28_2nd_v029_signal(intangibles, depamor, assets, opex):
    return _clean(_diff(_diff(intangibles, 4), 4))
def cg_f062_impairment_and_writedown_risk_core29_2nd_v030_signal(intangibles, depamor, assets, opex):
    return _clean(_diff(_z(_safe_div(intangibles, assets), 8), 4))
def cg_f062_impairment_and_writedown_risk_core30_2nd_v031_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_slope(intangibles, 4), 8))
def cg_f062_impairment_and_writedown_risk_core31_2nd_v032_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_slope(depamor, 4), 8))
def cg_f062_impairment_and_writedown_risk_core32_2nd_v033_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_slope(assets, 4), 8))
def cg_f062_impairment_and_writedown_risk_core33_2nd_v034_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_slope(opex, 4), 8))
def cg_f062_impairment_and_writedown_risk_core34_2nd_v035_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_slope(_safe_div(intangibles, assets), 4), 8))
def cg_f062_impairment_and_writedown_risk_core35_2nd_v036_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_slope(_safe_div(depamor, opex), 4), 8))
def cg_f062_impairment_and_writedown_risk_core36_2nd_v037_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_slope(_safe_div(depamor, intangibles.abs() + 1.0), 4), 8))
def cg_f062_impairment_and_writedown_risk_core37_2nd_v038_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_slope(_safe_div(intangibles + depamor, assets), 4), 8))
def cg_f062_impairment_and_writedown_risk_core38_2nd_v039_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_slope(_diff(intangibles, 4), 4), 8))
def cg_f062_impairment_and_writedown_risk_core39_2nd_v040_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_slope(_z(_safe_div(intangibles, assets), 8), 4), 8))
def cg_f062_impairment_and_writedown_risk_core40_2nd_v041_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_slope(intangibles, 8), 12))
def cg_f062_impairment_and_writedown_risk_core41_2nd_v042_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_slope(depamor, 8), 12))
def cg_f062_impairment_and_writedown_risk_core42_2nd_v043_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_slope(assets, 8), 12))
def cg_f062_impairment_and_writedown_risk_core43_2nd_v044_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_slope(opex, 8), 12))
def cg_f062_impairment_and_writedown_risk_core44_2nd_v045_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_slope(_safe_div(intangibles, assets), 8), 12))
def cg_f062_impairment_and_writedown_risk_core45_2nd_v046_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_slope(_safe_div(depamor, opex), 8), 12))
def cg_f062_impairment_and_writedown_risk_core46_2nd_v047_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_slope(_safe_div(depamor, intangibles.abs() + 1.0), 8), 12))
def cg_f062_impairment_and_writedown_risk_core47_2nd_v048_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_slope(_safe_div(intangibles + depamor, assets), 8), 12))
def cg_f062_impairment_and_writedown_risk_core48_2nd_v049_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_slope(_diff(intangibles, 4), 8), 12))
def cg_f062_impairment_and_writedown_risk_core49_2nd_v050_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_slope(_z(_safe_div(intangibles, assets), 8), 8), 12))
def cg_f062_impairment_and_writedown_risk_core50_2nd_v051_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_diff(intangibles, 4), 8))
def cg_f062_impairment_and_writedown_risk_core51_2nd_v052_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_diff(depamor, 4), 8))
def cg_f062_impairment_and_writedown_risk_core52_2nd_v053_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_diff(assets, 4), 8))
def cg_f062_impairment_and_writedown_risk_core53_2nd_v054_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_diff(opex, 4), 8))
def cg_f062_impairment_and_writedown_risk_core54_2nd_v055_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_diff(_safe_div(intangibles, assets), 4), 8))
def cg_f062_impairment_and_writedown_risk_core55_2nd_v056_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_diff(_safe_div(depamor, opex), 4), 8))
def cg_f062_impairment_and_writedown_risk_core56_2nd_v057_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_diff(_safe_div(depamor, intangibles.abs() + 1.0), 4), 8))
def cg_f062_impairment_and_writedown_risk_core57_2nd_v058_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_diff(_safe_div(intangibles + depamor, assets), 4), 8))
def cg_f062_impairment_and_writedown_risk_core58_2nd_v059_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_diff(_diff(intangibles, 4), 4), 8))
def cg_f062_impairment_and_writedown_risk_core59_2nd_v060_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_diff(_z(_safe_div(intangibles, assets), 8), 4), 8))
def cg_f062_impairment_and_writedown_risk_core60_2nd_v061_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(_slope(intangibles, 4), 12))
def cg_f062_impairment_and_writedown_risk_core61_2nd_v062_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(_slope(depamor, 4), 12))
def cg_f062_impairment_and_writedown_risk_core62_2nd_v063_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(_slope(assets, 4), 12))
def cg_f062_impairment_and_writedown_risk_core63_2nd_v064_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(_slope(opex, 4), 12))
def cg_f062_impairment_and_writedown_risk_core64_2nd_v065_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(_slope(_safe_div(intangibles, assets), 4), 12))
def cg_f062_impairment_and_writedown_risk_core65_2nd_v066_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(_slope(_safe_div(depamor, opex), 4), 12))
def cg_f062_impairment_and_writedown_risk_core66_2nd_v067_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(_slope(_safe_div(depamor, intangibles.abs() + 1.0), 4), 12))
def cg_f062_impairment_and_writedown_risk_core67_2nd_v068_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(_slope(_safe_div(intangibles + depamor, assets), 4), 12))
def cg_f062_impairment_and_writedown_risk_core68_2nd_v069_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(_slope(_diff(intangibles, 4), 4), 12))
def cg_f062_impairment_and_writedown_risk_core69_2nd_v070_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(_slope(_z(_safe_div(intangibles, assets), 8), 4), 12))
def cg_f062_impairment_and_writedown_risk_core70_2nd_v071_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(_diff(intangibles, 4), 12))
def cg_f062_impairment_and_writedown_risk_core71_2nd_v072_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(_diff(depamor, 4), 12))
def cg_f062_impairment_and_writedown_risk_core72_2nd_v073_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(_diff(assets, 4), 12))
def cg_f062_impairment_and_writedown_risk_core73_2nd_v074_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(_diff(opex, 4), 12))
def cg_f062_impairment_and_writedown_risk_core74_2nd_v075_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(_diff(_safe_div(intangibles, assets), 4), 12))
def cg_f062_impairment_and_writedown_risk_core75_2nd_v076_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(_diff(_safe_div(depamor, opex), 4), 12))
def cg_f062_impairment_and_writedown_risk_core76_2nd_v077_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(_diff(_safe_div(depamor, intangibles.abs() + 1.0), 4), 12))
def cg_f062_impairment_and_writedown_risk_core77_2nd_v078_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(_diff(_safe_div(intangibles + depamor, assets), 4), 12))
def cg_f062_impairment_and_writedown_risk_core78_2nd_v079_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(_diff(_diff(intangibles, 4), 4), 12))
def cg_f062_impairment_and_writedown_risk_core79_2nd_v080_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(_diff(_z(_safe_div(intangibles, assets), 8), 4), 12))
def cg_f062_impairment_and_writedown_risk_core80_2nd_v081_signal(intangibles, depamor, assets, opex):
    return _clean(_mean(_slope(intangibles, 4), 4))
def cg_f062_impairment_and_writedown_risk_core81_2nd_v082_signal(intangibles, depamor, assets, opex):
    return _clean(_mean(_slope(depamor, 4), 4))
def cg_f062_impairment_and_writedown_risk_core82_2nd_v083_signal(intangibles, depamor, assets, opex):
    return _clean(_mean(_slope(assets, 4), 4))
def cg_f062_impairment_and_writedown_risk_core83_2nd_v084_signal(intangibles, depamor, assets, opex):
    return _clean(_mean(_slope(opex, 4), 4))
def cg_f062_impairment_and_writedown_risk_core84_2nd_v085_signal(intangibles, depamor, assets, opex):
    return _clean(_mean(_slope(_safe_div(intangibles, assets), 4), 4))
def cg_f062_impairment_and_writedown_risk_core85_2nd_v086_signal(intangibles, depamor, assets, opex):
    return _clean(_mean(_slope(_safe_div(depamor, opex), 4), 4))
def cg_f062_impairment_and_writedown_risk_core86_2nd_v087_signal(intangibles, depamor, assets, opex):
    return _clean(_mean(_slope(_safe_div(depamor, intangibles.abs() + 1.0), 4), 4))
def cg_f062_impairment_and_writedown_risk_core87_2nd_v088_signal(intangibles, depamor, assets, opex):
    return _clean(_mean(_slope(_safe_div(intangibles + depamor, assets), 4), 4))
def cg_f062_impairment_and_writedown_risk_core88_2nd_v089_signal(intangibles, depamor, assets, opex):
    return _clean(_mean(_slope(_diff(intangibles, 4), 4), 4))
def cg_f062_impairment_and_writedown_risk_core89_2nd_v090_signal(intangibles, depamor, assets, opex):
    return _clean(_mean(_slope(_z(_safe_div(intangibles, assets), 8), 4), 4))
def cg_f062_impairment_and_writedown_risk_core90_2nd_v091_signal(intangibles, depamor, assets, opex):
    return _clean(_mean(_diff(intangibles, 4), 4))
def cg_f062_impairment_and_writedown_risk_core91_2nd_v092_signal(intangibles, depamor, assets, opex):
    return _clean(_mean(_diff(depamor, 4), 4))
def cg_f062_impairment_and_writedown_risk_core92_2nd_v093_signal(intangibles, depamor, assets, opex):
    return _clean(_mean(_diff(assets, 4), 4))
def cg_f062_impairment_and_writedown_risk_core93_2nd_v094_signal(intangibles, depamor, assets, opex):
    return _clean(_mean(_diff(opex, 4), 4))
def cg_f062_impairment_and_writedown_risk_core94_2nd_v095_signal(intangibles, depamor, assets, opex):
    return _clean(_mean(_diff(_safe_div(intangibles, assets), 4), 4))
def cg_f062_impairment_and_writedown_risk_core95_2nd_v096_signal(intangibles, depamor, assets, opex):
    return _clean(_mean(_diff(_safe_div(depamor, opex), 4), 4))
def cg_f062_impairment_and_writedown_risk_core96_2nd_v097_signal(intangibles, depamor, assets, opex):
    return _clean(_mean(_diff(_safe_div(depamor, intangibles.abs() + 1.0), 4), 4))
def cg_f062_impairment_and_writedown_risk_core97_2nd_v098_signal(intangibles, depamor, assets, opex):
    return _clean(_mean(_diff(_safe_div(intangibles + depamor, assets), 4), 4))
def cg_f062_impairment_and_writedown_risk_core98_2nd_v099_signal(intangibles, depamor, assets, opex):
    return _clean(_mean(_diff(_diff(intangibles, 4), 4), 4))
def cg_f062_impairment_and_writedown_risk_core99_2nd_v100_signal(intangibles, depamor, assets, opex):
    return _clean(_mean(_diff(_z(_safe_div(intangibles, assets), 8), 4), 4))
def cg_f062_impairment_and_writedown_risk_core100_2nd_v101_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(_mean(intangibles, 4), 4))
def cg_f062_impairment_and_writedown_risk_core101_2nd_v102_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(_mean(depamor, 4), 4))
def cg_f062_impairment_and_writedown_risk_core102_2nd_v103_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(_mean(assets, 4), 4))
def cg_f062_impairment_and_writedown_risk_core103_2nd_v104_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(_mean(opex, 4), 4))
def cg_f062_impairment_and_writedown_risk_core104_2nd_v105_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(_mean(_safe_div(intangibles, assets), 4), 4))
def cg_f062_impairment_and_writedown_risk_core105_2nd_v106_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(_mean(_safe_div(depamor, opex), 4), 4))
def cg_f062_impairment_and_writedown_risk_core106_2nd_v107_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(_mean(_safe_div(depamor, intangibles.abs() + 1.0), 4), 4))
def cg_f062_impairment_and_writedown_risk_core107_2nd_v108_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(_mean(_safe_div(intangibles + depamor, assets), 4), 4))
def cg_f062_impairment_and_writedown_risk_core108_2nd_v109_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(_mean(_diff(intangibles, 4), 4), 4))
def cg_f062_impairment_and_writedown_risk_core109_2nd_v110_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(_mean(_z(_safe_div(intangibles, assets), 8), 4), 4))
def cg_f062_impairment_and_writedown_risk_core110_2nd_v111_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(_mean(intangibles, 8), 8))
def cg_f062_impairment_and_writedown_risk_core111_2nd_v112_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(_mean(depamor, 8), 8))
def cg_f062_impairment_and_writedown_risk_core112_2nd_v113_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(_mean(assets, 8), 8))
def cg_f062_impairment_and_writedown_risk_core113_2nd_v114_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(_mean(opex, 8), 8))
def cg_f062_impairment_and_writedown_risk_core114_2nd_v115_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(_mean(_safe_div(intangibles, assets), 8), 8))
def cg_f062_impairment_and_writedown_risk_core115_2nd_v116_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(_mean(_safe_div(depamor, opex), 8), 8))
def cg_f062_impairment_and_writedown_risk_core116_2nd_v117_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(_mean(_safe_div(depamor, intangibles.abs() + 1.0), 8), 8))
def cg_f062_impairment_and_writedown_risk_core117_2nd_v118_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(_mean(_safe_div(intangibles + depamor, assets), 8), 8))
def cg_f062_impairment_and_writedown_risk_core118_2nd_v119_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(_mean(_diff(intangibles, 4), 8), 8))
def cg_f062_impairment_and_writedown_risk_core119_2nd_v120_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(_mean(_z(_safe_div(intangibles, assets), 8), 8), 8))
def cg_f062_impairment_and_writedown_risk_core120_2nd_v121_signal(intangibles, depamor, assets, opex):
    return _clean(_diff(_mean(intangibles, 4), 4))
def cg_f062_impairment_and_writedown_risk_core121_2nd_v122_signal(intangibles, depamor, assets, opex):
    return _clean(_diff(_mean(depamor, 4), 4))
def cg_f062_impairment_and_writedown_risk_core122_2nd_v123_signal(intangibles, depamor, assets, opex):
    return _clean(_diff(_mean(assets, 4), 4))
def cg_f062_impairment_and_writedown_risk_core123_2nd_v124_signal(intangibles, depamor, assets, opex):
    return _clean(_diff(_mean(opex, 4), 4))
def cg_f062_impairment_and_writedown_risk_core124_2nd_v125_signal(intangibles, depamor, assets, opex):
    return _clean(_diff(_mean(_safe_div(intangibles, assets), 4), 4))
def cg_f062_impairment_and_writedown_risk_core125_2nd_v126_signal(intangibles, depamor, assets, opex):
    return _clean(_diff(_mean(_safe_div(depamor, opex), 4), 4))
def cg_f062_impairment_and_writedown_risk_core126_2nd_v127_signal(intangibles, depamor, assets, opex):
    return _clean(_diff(_mean(_safe_div(depamor, intangibles.abs() + 1.0), 4), 4))
def cg_f062_impairment_and_writedown_risk_core127_2nd_v128_signal(intangibles, depamor, assets, opex):
    return _clean(_diff(_mean(_safe_div(intangibles + depamor, assets), 4), 4))
def cg_f062_impairment_and_writedown_risk_core128_2nd_v129_signal(intangibles, depamor, assets, opex):
    return _clean(_diff(_mean(_diff(intangibles, 4), 4), 4))
def cg_f062_impairment_and_writedown_risk_core129_2nd_v130_signal(intangibles, depamor, assets, opex):
    return _clean(_diff(_mean(_z(_safe_div(intangibles, assets), 8), 4), 4))
def cg_f062_impairment_and_writedown_risk_core130_2nd_v131_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_diff(_mean(intangibles, 4), 4), 8))
def cg_f062_impairment_and_writedown_risk_core131_2nd_v132_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_diff(_mean(depamor, 4), 4), 8))
def cg_f062_impairment_and_writedown_risk_core132_2nd_v133_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_diff(_mean(assets, 4), 4), 8))
def cg_f062_impairment_and_writedown_risk_core133_2nd_v134_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_diff(_mean(opex, 4), 4), 8))
def cg_f062_impairment_and_writedown_risk_core134_2nd_v135_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_diff(_mean(_safe_div(intangibles, assets), 4), 4), 8))
def cg_f062_impairment_and_writedown_risk_core135_2nd_v136_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_diff(_mean(_safe_div(depamor, opex), 4), 4), 8))
def cg_f062_impairment_and_writedown_risk_core136_2nd_v137_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_diff(_mean(_safe_div(depamor, intangibles.abs() + 1.0), 4), 4), 8))
def cg_f062_impairment_and_writedown_risk_core137_2nd_v138_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_diff(_mean(_safe_div(intangibles + depamor, assets), 4), 4), 8))
def cg_f062_impairment_and_writedown_risk_core138_2nd_v139_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_diff(_mean(_diff(intangibles, 4), 4), 4), 8))
def cg_f062_impairment_and_writedown_risk_core139_2nd_v140_signal(intangibles, depamor, assets, opex):
    return _clean(_z(_diff(_mean(_z(_safe_div(intangibles, assets), 8), 4), 4), 8))
def cg_f062_impairment_and_writedown_risk_core140_2nd_v141_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(_slope(_mean(intangibles, 4), 4), 12))
def cg_f062_impairment_and_writedown_risk_core141_2nd_v142_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(_slope(_mean(depamor, 4), 4), 12))
def cg_f062_impairment_and_writedown_risk_core142_2nd_v143_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(_slope(_mean(assets, 4), 4), 12))
def cg_f062_impairment_and_writedown_risk_core143_2nd_v144_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(_slope(_mean(opex, 4), 4), 12))
def cg_f062_impairment_and_writedown_risk_core144_2nd_v145_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(_slope(_mean(_safe_div(intangibles, assets), 4), 4), 12))
def cg_f062_impairment_and_writedown_risk_core145_2nd_v146_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(_slope(_mean(_safe_div(depamor, opex), 4), 4), 12))
def cg_f062_impairment_and_writedown_risk_core146_2nd_v147_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(_slope(_mean(_safe_div(depamor, intangibles.abs() + 1.0), 4), 4), 12))
def cg_f062_impairment_and_writedown_risk_core147_2nd_v148_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(_slope(_mean(_safe_div(intangibles + depamor, assets), 4), 4), 12))
def cg_f062_impairment_and_writedown_risk_core148_2nd_v149_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(_slope(_mean(_diff(intangibles, 4), 4), 4), 12))
def cg_f062_impairment_and_writedown_risk_core149_2nd_v150_signal(intangibles, depamor, assets, opex):
    return _clean(_rank(_slope(_mean(_z(_safe_div(intangibles, assets), 8), 4), 4), 12))