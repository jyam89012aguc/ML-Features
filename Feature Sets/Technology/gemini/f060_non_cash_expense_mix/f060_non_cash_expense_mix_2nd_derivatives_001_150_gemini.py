import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f060_non_cash_expense_mix_core00_2nd_v001_signal(depamor, sbcomp, netinc, opex):
    return _clean(_slope(depamor, 4))
def cg_f060_non_cash_expense_mix_core01_2nd_v002_signal(depamor, sbcomp, netinc, opex):
    return _clean(_slope(sbcomp, 4))
def cg_f060_non_cash_expense_mix_core02_2nd_v003_signal(depamor, sbcomp, netinc, opex):
    return _clean(_slope(netinc, 4))
def cg_f060_non_cash_expense_mix_core03_2nd_v004_signal(depamor, sbcomp, netinc, opex):
    return _clean(_slope(opex, 4))
def cg_f060_non_cash_expense_mix_core04_2nd_v005_signal(depamor, sbcomp, netinc, opex):
    return _clean(_slope(depamor + sbcomp, 4))
def cg_f060_non_cash_expense_mix_core05_2nd_v006_signal(depamor, sbcomp, netinc, opex):
    return _clean(_slope(_safe_div(depamor, opex), 4))
def cg_f060_non_cash_expense_mix_core06_2nd_v007_signal(depamor, sbcomp, netinc, opex):
    return _clean(_slope(_safe_div(sbcomp, opex), 4))
def cg_f060_non_cash_expense_mix_core07_2nd_v008_signal(depamor, sbcomp, netinc, opex):
    return _clean(_slope(_safe_div(depamor + sbcomp, opex), 4))
def cg_f060_non_cash_expense_mix_core08_2nd_v009_signal(depamor, sbcomp, netinc, opex):
    return _clean(_slope(_safe_div(sbcomp, netinc.abs() + 1.0), 4))
def cg_f060_non_cash_expense_mix_core09_2nd_v010_signal(depamor, sbcomp, netinc, opex):
    return _clean(_slope(_safe_div(depamor, netinc.abs() + 1.0), 4))
def cg_f060_non_cash_expense_mix_core10_2nd_v011_signal(depamor, sbcomp, netinc, opex):
    return _clean(_slope(depamor, 8))
def cg_f060_non_cash_expense_mix_core11_2nd_v012_signal(depamor, sbcomp, netinc, opex):
    return _clean(_slope(sbcomp, 8))
def cg_f060_non_cash_expense_mix_core12_2nd_v013_signal(depamor, sbcomp, netinc, opex):
    return _clean(_slope(netinc, 8))
def cg_f060_non_cash_expense_mix_core13_2nd_v014_signal(depamor, sbcomp, netinc, opex):
    return _clean(_slope(opex, 8))
def cg_f060_non_cash_expense_mix_core14_2nd_v015_signal(depamor, sbcomp, netinc, opex):
    return _clean(_slope(depamor + sbcomp, 8))
def cg_f060_non_cash_expense_mix_core15_2nd_v016_signal(depamor, sbcomp, netinc, opex):
    return _clean(_slope(_safe_div(depamor, opex), 8))
def cg_f060_non_cash_expense_mix_core16_2nd_v017_signal(depamor, sbcomp, netinc, opex):
    return _clean(_slope(_safe_div(sbcomp, opex), 8))
def cg_f060_non_cash_expense_mix_core17_2nd_v018_signal(depamor, sbcomp, netinc, opex):
    return _clean(_slope(_safe_div(depamor + sbcomp, opex), 8))
def cg_f060_non_cash_expense_mix_core18_2nd_v019_signal(depamor, sbcomp, netinc, opex):
    return _clean(_slope(_safe_div(sbcomp, netinc.abs() + 1.0), 8))
def cg_f060_non_cash_expense_mix_core19_2nd_v020_signal(depamor, sbcomp, netinc, opex):
    return _clean(_slope(_safe_div(depamor, netinc.abs() + 1.0), 8))
def cg_f060_non_cash_expense_mix_core20_2nd_v021_signal(depamor, sbcomp, netinc, opex):
    return _clean(_diff(depamor, 4))
def cg_f060_non_cash_expense_mix_core21_2nd_v022_signal(depamor, sbcomp, netinc, opex):
    return _clean(_diff(sbcomp, 4))
def cg_f060_non_cash_expense_mix_core22_2nd_v023_signal(depamor, sbcomp, netinc, opex):
    return _clean(_diff(netinc, 4))
def cg_f060_non_cash_expense_mix_core23_2nd_v024_signal(depamor, sbcomp, netinc, opex):
    return _clean(_diff(opex, 4))
def cg_f060_non_cash_expense_mix_core24_2nd_v025_signal(depamor, sbcomp, netinc, opex):
    return _clean(_diff(depamor + sbcomp, 4))
def cg_f060_non_cash_expense_mix_core25_2nd_v026_signal(depamor, sbcomp, netinc, opex):
    return _clean(_diff(_safe_div(depamor, opex), 4))
def cg_f060_non_cash_expense_mix_core26_2nd_v027_signal(depamor, sbcomp, netinc, opex):
    return _clean(_diff(_safe_div(sbcomp, opex), 4))
def cg_f060_non_cash_expense_mix_core27_2nd_v028_signal(depamor, sbcomp, netinc, opex):
    return _clean(_diff(_safe_div(depamor + sbcomp, opex), 4))
def cg_f060_non_cash_expense_mix_core28_2nd_v029_signal(depamor, sbcomp, netinc, opex):
    return _clean(_diff(_safe_div(sbcomp, netinc.abs() + 1.0), 4))
def cg_f060_non_cash_expense_mix_core29_2nd_v030_signal(depamor, sbcomp, netinc, opex):
    return _clean(_diff(_safe_div(depamor, netinc.abs() + 1.0), 4))
def cg_f060_non_cash_expense_mix_core30_2nd_v031_signal(depamor, sbcomp, netinc, opex):
    return _clean(_z(_slope(depamor, 4), 8))
def cg_f060_non_cash_expense_mix_core31_2nd_v032_signal(depamor, sbcomp, netinc, opex):
    return _clean(_z(_slope(sbcomp, 4), 8))
def cg_f060_non_cash_expense_mix_core32_2nd_v033_signal(depamor, sbcomp, netinc, opex):
    return _clean(_z(_slope(netinc, 4), 8))
def cg_f060_non_cash_expense_mix_core33_2nd_v034_signal(depamor, sbcomp, netinc, opex):
    return _clean(_z(_slope(opex, 4), 8))
def cg_f060_non_cash_expense_mix_core34_2nd_v035_signal(depamor, sbcomp, netinc, opex):
    return _clean(_z(_slope(depamor + sbcomp, 4), 8))
def cg_f060_non_cash_expense_mix_core35_2nd_v036_signal(depamor, sbcomp, netinc, opex):
    return _clean(_z(_slope(_safe_div(depamor, opex), 4), 8))
def cg_f060_non_cash_expense_mix_core36_2nd_v037_signal(depamor, sbcomp, netinc, opex):
    return _clean(_z(_slope(_safe_div(sbcomp, opex), 4), 8))
def cg_f060_non_cash_expense_mix_core37_2nd_v038_signal(depamor, sbcomp, netinc, opex):
    return _clean(_z(_slope(_safe_div(depamor + sbcomp, opex), 4), 8))
def cg_f060_non_cash_expense_mix_core38_2nd_v039_signal(depamor, sbcomp, netinc, opex):
    return _clean(_z(_slope(_safe_div(sbcomp, netinc.abs() + 1.0), 4), 8))
def cg_f060_non_cash_expense_mix_core39_2nd_v040_signal(depamor, sbcomp, netinc, opex):
    return _clean(_z(_slope(_safe_div(depamor, netinc.abs() + 1.0), 4), 8))
def cg_f060_non_cash_expense_mix_core40_2nd_v041_signal(depamor, sbcomp, netinc, opex):
    return _clean(_z(_slope(depamor, 8), 12))
def cg_f060_non_cash_expense_mix_core41_2nd_v042_signal(depamor, sbcomp, netinc, opex):
    return _clean(_z(_slope(sbcomp, 8), 12))
def cg_f060_non_cash_expense_mix_core42_2nd_v043_signal(depamor, sbcomp, netinc, opex):
    return _clean(_z(_slope(netinc, 8), 12))
def cg_f060_non_cash_expense_mix_core43_2nd_v044_signal(depamor, sbcomp, netinc, opex):
    return _clean(_z(_slope(opex, 8), 12))
def cg_f060_non_cash_expense_mix_core44_2nd_v045_signal(depamor, sbcomp, netinc, opex):
    return _clean(_z(_slope(depamor + sbcomp, 8), 12))
def cg_f060_non_cash_expense_mix_core45_2nd_v046_signal(depamor, sbcomp, netinc, opex):
    return _clean(_z(_slope(_safe_div(depamor, opex), 8), 12))
def cg_f060_non_cash_expense_mix_core46_2nd_v047_signal(depamor, sbcomp, netinc, opex):
    return _clean(_z(_slope(_safe_div(sbcomp, opex), 8), 12))
def cg_f060_non_cash_expense_mix_core47_2nd_v048_signal(depamor, sbcomp, netinc, opex):
    return _clean(_z(_slope(_safe_div(depamor + sbcomp, opex), 8), 12))
def cg_f060_non_cash_expense_mix_core48_2nd_v049_signal(depamor, sbcomp, netinc, opex):
    return _clean(_z(_slope(_safe_div(sbcomp, netinc.abs() + 1.0), 8), 12))
def cg_f060_non_cash_expense_mix_core49_2nd_v050_signal(depamor, sbcomp, netinc, opex):
    return _clean(_z(_slope(_safe_div(depamor, netinc.abs() + 1.0), 8), 12))
def cg_f060_non_cash_expense_mix_core50_2nd_v051_signal(depamor, sbcomp, netinc, opex):
    return _clean(_z(_diff(depamor, 4), 8))
def cg_f060_non_cash_expense_mix_core51_2nd_v052_signal(depamor, sbcomp, netinc, opex):
    return _clean(_z(_diff(sbcomp, 4), 8))
def cg_f060_non_cash_expense_mix_core52_2nd_v053_signal(depamor, sbcomp, netinc, opex):
    return _clean(_z(_diff(netinc, 4), 8))
def cg_f060_non_cash_expense_mix_core53_2nd_v054_signal(depamor, sbcomp, netinc, opex):
    return _clean(_z(_diff(opex, 4), 8))
def cg_f060_non_cash_expense_mix_core54_2nd_v055_signal(depamor, sbcomp, netinc, opex):
    return _clean(_z(_diff(depamor + sbcomp, 4), 8))
def cg_f060_non_cash_expense_mix_core55_2nd_v056_signal(depamor, sbcomp, netinc, opex):
    return _clean(_z(_diff(_safe_div(depamor, opex), 4), 8))
def cg_f060_non_cash_expense_mix_core56_2nd_v057_signal(depamor, sbcomp, netinc, opex):
    return _clean(_z(_diff(_safe_div(sbcomp, opex), 4), 8))
def cg_f060_non_cash_expense_mix_core57_2nd_v058_signal(depamor, sbcomp, netinc, opex):
    return _clean(_z(_diff(_safe_div(depamor + sbcomp, opex), 4), 8))
def cg_f060_non_cash_expense_mix_core58_2nd_v059_signal(depamor, sbcomp, netinc, opex):
    return _clean(_z(_diff(_safe_div(sbcomp, netinc.abs() + 1.0), 4), 8))
def cg_f060_non_cash_expense_mix_core59_2nd_v060_signal(depamor, sbcomp, netinc, opex):
    return _clean(_z(_diff(_safe_div(depamor, netinc.abs() + 1.0), 4), 8))
def cg_f060_non_cash_expense_mix_core60_2nd_v061_signal(depamor, sbcomp, netinc, opex):
    return _clean(_rank(_slope(depamor, 4), 12))
def cg_f060_non_cash_expense_mix_core61_2nd_v062_signal(depamor, sbcomp, netinc, opex):
    return _clean(_rank(_slope(sbcomp, 4), 12))
def cg_f060_non_cash_expense_mix_core62_2nd_v063_signal(depamor, sbcomp, netinc, opex):
    return _clean(_rank(_slope(netinc, 4), 12))
def cg_f060_non_cash_expense_mix_core63_2nd_v064_signal(depamor, sbcomp, netinc, opex):
    return _clean(_rank(_slope(opex, 4), 12))
def cg_f060_non_cash_expense_mix_core64_2nd_v065_signal(depamor, sbcomp, netinc, opex):
    return _clean(_rank(_slope(depamor + sbcomp, 4), 12))
def cg_f060_non_cash_expense_mix_core65_2nd_v066_signal(depamor, sbcomp, netinc, opex):
    return _clean(_rank(_slope(_safe_div(depamor, opex), 4), 12))
def cg_f060_non_cash_expense_mix_core66_2nd_v067_signal(depamor, sbcomp, netinc, opex):
    return _clean(_rank(_slope(_safe_div(sbcomp, opex), 4), 12))
def cg_f060_non_cash_expense_mix_core67_2nd_v068_signal(depamor, sbcomp, netinc, opex):
    return _clean(_rank(_slope(_safe_div(depamor + sbcomp, opex), 4), 12))
def cg_f060_non_cash_expense_mix_core68_2nd_v069_signal(depamor, sbcomp, netinc, opex):
    return _clean(_rank(_slope(_safe_div(sbcomp, netinc.abs() + 1.0), 4), 12))
def cg_f060_non_cash_expense_mix_core69_2nd_v070_signal(depamor, sbcomp, netinc, opex):
    return _clean(_rank(_slope(_safe_div(depamor, netinc.abs() + 1.0), 4), 12))
def cg_f060_non_cash_expense_mix_core70_2nd_v071_signal(depamor, sbcomp, netinc, opex):
    return _clean(_rank(_diff(depamor, 4), 12))
def cg_f060_non_cash_expense_mix_core71_2nd_v072_signal(depamor, sbcomp, netinc, opex):
    return _clean(_rank(_diff(sbcomp, 4), 12))
def cg_f060_non_cash_expense_mix_core72_2nd_v073_signal(depamor, sbcomp, netinc, opex):
    return _clean(_rank(_diff(netinc, 4), 12))
def cg_f060_non_cash_expense_mix_core73_2nd_v074_signal(depamor, sbcomp, netinc, opex):
    return _clean(_rank(_diff(opex, 4), 12))
def cg_f060_non_cash_expense_mix_core74_2nd_v075_signal(depamor, sbcomp, netinc, opex):
    return _clean(_rank(_diff(depamor + sbcomp, 4), 12))
def cg_f060_non_cash_expense_mix_core75_2nd_v076_signal(depamor, sbcomp, netinc, opex):
    return _clean(_rank(_diff(_safe_div(depamor, opex), 4), 12))
def cg_f060_non_cash_expense_mix_core76_2nd_v077_signal(depamor, sbcomp, netinc, opex):
    return _clean(_rank(_diff(_safe_div(sbcomp, opex), 4), 12))
def cg_f060_non_cash_expense_mix_core77_2nd_v078_signal(depamor, sbcomp, netinc, opex):
    return _clean(_rank(_diff(_safe_div(depamor + sbcomp, opex), 4), 12))
def cg_f060_non_cash_expense_mix_core78_2nd_v079_signal(depamor, sbcomp, netinc, opex):
    return _clean(_rank(_diff(_safe_div(sbcomp, netinc.abs() + 1.0), 4), 12))
def cg_f060_non_cash_expense_mix_core79_2nd_v080_signal(depamor, sbcomp, netinc, opex):
    return _clean(_rank(_diff(_safe_div(depamor, netinc.abs() + 1.0), 4), 12))
def cg_f060_non_cash_expense_mix_core80_2nd_v081_signal(depamor, sbcomp, netinc, opex):
    return _clean(_mean(_slope(depamor, 4), 4))
def cg_f060_non_cash_expense_mix_core81_2nd_v082_signal(depamor, sbcomp, netinc, opex):
    return _clean(_mean(_slope(sbcomp, 4), 4))
def cg_f060_non_cash_expense_mix_core82_2nd_v083_signal(depamor, sbcomp, netinc, opex):
    return _clean(_mean(_slope(netinc, 4), 4))
def cg_f060_non_cash_expense_mix_core83_2nd_v084_signal(depamor, sbcomp, netinc, opex):
    return _clean(_mean(_slope(opex, 4), 4))
def cg_f060_non_cash_expense_mix_core84_2nd_v085_signal(depamor, sbcomp, netinc, opex):
    return _clean(_mean(_slope(depamor + sbcomp, 4), 4))
def cg_f060_non_cash_expense_mix_core85_2nd_v086_signal(depamor, sbcomp, netinc, opex):
    return _clean(_mean(_slope(_safe_div(depamor, opex), 4), 4))
def cg_f060_non_cash_expense_mix_core86_2nd_v087_signal(depamor, sbcomp, netinc, opex):
    return _clean(_mean(_slope(_safe_div(sbcomp, opex), 4), 4))
def cg_f060_non_cash_expense_mix_core87_2nd_v088_signal(depamor, sbcomp, netinc, opex):
    return _clean(_mean(_slope(_safe_div(depamor + sbcomp, opex), 4), 4))
def cg_f060_non_cash_expense_mix_core88_2nd_v089_signal(depamor, sbcomp, netinc, opex):
    return _clean(_mean(_slope(_safe_div(sbcomp, netinc.abs() + 1.0), 4), 4))
def cg_f060_non_cash_expense_mix_core89_2nd_v090_signal(depamor, sbcomp, netinc, opex):
    return _clean(_mean(_slope(_safe_div(depamor, netinc.abs() + 1.0), 4), 4))
def cg_f060_non_cash_expense_mix_core90_2nd_v091_signal(depamor, sbcomp, netinc, opex):
    return _clean(_mean(_diff(depamor, 4), 4))
def cg_f060_non_cash_expense_mix_core91_2nd_v092_signal(depamor, sbcomp, netinc, opex):
    return _clean(_mean(_diff(sbcomp, 4), 4))
def cg_f060_non_cash_expense_mix_core92_2nd_v093_signal(depamor, sbcomp, netinc, opex):
    return _clean(_mean(_diff(netinc, 4), 4))
def cg_f060_non_cash_expense_mix_core93_2nd_v094_signal(depamor, sbcomp, netinc, opex):
    return _clean(_mean(_diff(opex, 4), 4))
def cg_f060_non_cash_expense_mix_core94_2nd_v095_signal(depamor, sbcomp, netinc, opex):
    return _clean(_mean(_diff(depamor + sbcomp, 4), 4))
def cg_f060_non_cash_expense_mix_core95_2nd_v096_signal(depamor, sbcomp, netinc, opex):
    return _clean(_mean(_diff(_safe_div(depamor, opex), 4), 4))
def cg_f060_non_cash_expense_mix_core96_2nd_v097_signal(depamor, sbcomp, netinc, opex):
    return _clean(_mean(_diff(_safe_div(sbcomp, opex), 4), 4))
def cg_f060_non_cash_expense_mix_core97_2nd_v098_signal(depamor, sbcomp, netinc, opex):
    return _clean(_mean(_diff(_safe_div(depamor + sbcomp, opex), 4), 4))
def cg_f060_non_cash_expense_mix_core98_2nd_v099_signal(depamor, sbcomp, netinc, opex):
    return _clean(_mean(_diff(_safe_div(sbcomp, netinc.abs() + 1.0), 4), 4))
def cg_f060_non_cash_expense_mix_core99_2nd_v100_signal(depamor, sbcomp, netinc, opex):
    return _clean(_mean(_diff(_safe_div(depamor, netinc.abs() + 1.0), 4), 4))
def cg_f060_non_cash_expense_mix_core100_2nd_v101_signal(depamor, sbcomp, netinc, opex):
    return _clean(_slope(_mean(depamor, 4), 4))
def cg_f060_non_cash_expense_mix_core101_2nd_v102_signal(depamor, sbcomp, netinc, opex):
    return _clean(_slope(_mean(sbcomp, 4), 4))
def cg_f060_non_cash_expense_mix_core102_2nd_v103_signal(depamor, sbcomp, netinc, opex):
    return _clean(_slope(_mean(netinc, 4), 4))
def cg_f060_non_cash_expense_mix_core103_2nd_v104_signal(depamor, sbcomp, netinc, opex):
    return _clean(_slope(_mean(opex, 4), 4))
def cg_f060_non_cash_expense_mix_core104_2nd_v105_signal(depamor, sbcomp, netinc, opex):
    return _clean(_slope(_mean(depamor + sbcomp, 4), 4))
def cg_f060_non_cash_expense_mix_core105_2nd_v106_signal(depamor, sbcomp, netinc, opex):
    return _clean(_slope(_mean(_safe_div(depamor, opex), 4), 4))
def cg_f060_non_cash_expense_mix_core106_2nd_v107_signal(depamor, sbcomp, netinc, opex):
    return _clean(_slope(_mean(_safe_div(sbcomp, opex), 4), 4))
def cg_f060_non_cash_expense_mix_core107_2nd_v108_signal(depamor, sbcomp, netinc, opex):
    return _clean(_slope(_mean(_safe_div(depamor + sbcomp, opex), 4), 4))
def cg_f060_non_cash_expense_mix_core108_2nd_v109_signal(depamor, sbcomp, netinc, opex):
    return _clean(_slope(_mean(_safe_div(sbcomp, netinc.abs() + 1.0), 4), 4))
def cg_f060_non_cash_expense_mix_core109_2nd_v110_signal(depamor, sbcomp, netinc, opex):
    return _clean(_slope(_mean(_safe_div(depamor, netinc.abs() + 1.0), 4), 4))
def cg_f060_non_cash_expense_mix_core110_2nd_v111_signal(depamor, sbcomp, netinc, opex):
    return _clean(_slope(_mean(depamor, 8), 8))
def cg_f060_non_cash_expense_mix_core111_2nd_v112_signal(depamor, sbcomp, netinc, opex):
    return _clean(_slope(_mean(sbcomp, 8), 8))
def cg_f060_non_cash_expense_mix_core112_2nd_v113_signal(depamor, sbcomp, netinc, opex):
    return _clean(_slope(_mean(netinc, 8), 8))
def cg_f060_non_cash_expense_mix_core113_2nd_v114_signal(depamor, sbcomp, netinc, opex):
    return _clean(_slope(_mean(opex, 8), 8))
def cg_f060_non_cash_expense_mix_core114_2nd_v115_signal(depamor, sbcomp, netinc, opex):
    return _clean(_slope(_mean(depamor + sbcomp, 8), 8))
def cg_f060_non_cash_expense_mix_core115_2nd_v116_signal(depamor, sbcomp, netinc, opex):
    return _clean(_slope(_mean(_safe_div(depamor, opex), 8), 8))
def cg_f060_non_cash_expense_mix_core116_2nd_v117_signal(depamor, sbcomp, netinc, opex):
    return _clean(_slope(_mean(_safe_div(sbcomp, opex), 8), 8))
def cg_f060_non_cash_expense_mix_core117_2nd_v118_signal(depamor, sbcomp, netinc, opex):
    return _clean(_slope(_mean(_safe_div(depamor + sbcomp, opex), 8), 8))
def cg_f060_non_cash_expense_mix_core118_2nd_v119_signal(depamor, sbcomp, netinc, opex):
    return _clean(_slope(_mean(_safe_div(sbcomp, netinc.abs() + 1.0), 8), 8))
def cg_f060_non_cash_expense_mix_core119_2nd_v120_signal(depamor, sbcomp, netinc, opex):
    return _clean(_slope(_mean(_safe_div(depamor, netinc.abs() + 1.0), 8), 8))
def cg_f060_non_cash_expense_mix_core120_2nd_v121_signal(depamor, sbcomp, netinc, opex):
    return _clean(_diff(_mean(depamor, 4), 4))
def cg_f060_non_cash_expense_mix_core121_2nd_v122_signal(depamor, sbcomp, netinc, opex):
    return _clean(_diff(_mean(sbcomp, 4), 4))
def cg_f060_non_cash_expense_mix_core122_2nd_v123_signal(depamor, sbcomp, netinc, opex):
    return _clean(_diff(_mean(netinc, 4), 4))
def cg_f060_non_cash_expense_mix_core123_2nd_v124_signal(depamor, sbcomp, netinc, opex):
    return _clean(_diff(_mean(opex, 4), 4))
def cg_f060_non_cash_expense_mix_core124_2nd_v125_signal(depamor, sbcomp, netinc, opex):
    return _clean(_diff(_mean(depamor + sbcomp, 4), 4))
def cg_f060_non_cash_expense_mix_core125_2nd_v126_signal(depamor, sbcomp, netinc, opex):
    return _clean(_diff(_mean(_safe_div(depamor, opex), 4), 4))
def cg_f060_non_cash_expense_mix_core126_2nd_v127_signal(depamor, sbcomp, netinc, opex):
    return _clean(_diff(_mean(_safe_div(sbcomp, opex), 4), 4))
def cg_f060_non_cash_expense_mix_core127_2nd_v128_signal(depamor, sbcomp, netinc, opex):
    return _clean(_diff(_mean(_safe_div(depamor + sbcomp, opex), 4), 4))
def cg_f060_non_cash_expense_mix_core128_2nd_v129_signal(depamor, sbcomp, netinc, opex):
    return _clean(_diff(_mean(_safe_div(sbcomp, netinc.abs() + 1.0), 4), 4))
def cg_f060_non_cash_expense_mix_core129_2nd_v130_signal(depamor, sbcomp, netinc, opex):
    return _clean(_diff(_mean(_safe_div(depamor, netinc.abs() + 1.0), 4), 4))
def cg_f060_non_cash_expense_mix_core130_2nd_v131_signal(depamor, sbcomp, netinc, opex):
    return _clean(_z(_diff(_mean(depamor, 4), 4), 8))
def cg_f060_non_cash_expense_mix_core131_2nd_v132_signal(depamor, sbcomp, netinc, opex):
    return _clean(_z(_diff(_mean(sbcomp, 4), 4), 8))
def cg_f060_non_cash_expense_mix_core132_2nd_v133_signal(depamor, sbcomp, netinc, opex):
    return _clean(_z(_diff(_mean(netinc, 4), 4), 8))
def cg_f060_non_cash_expense_mix_core133_2nd_v134_signal(depamor, sbcomp, netinc, opex):
    return _clean(_z(_diff(_mean(opex, 4), 4), 8))
def cg_f060_non_cash_expense_mix_core134_2nd_v135_signal(depamor, sbcomp, netinc, opex):
    return _clean(_z(_diff(_mean(depamor + sbcomp, 4), 4), 8))
def cg_f060_non_cash_expense_mix_core135_2nd_v136_signal(depamor, sbcomp, netinc, opex):
    return _clean(_z(_diff(_mean(_safe_div(depamor, opex), 4), 4), 8))
def cg_f060_non_cash_expense_mix_core136_2nd_v137_signal(depamor, sbcomp, netinc, opex):
    return _clean(_z(_diff(_mean(_safe_div(sbcomp, opex), 4), 4), 8))
def cg_f060_non_cash_expense_mix_core137_2nd_v138_signal(depamor, sbcomp, netinc, opex):
    return _clean(_z(_diff(_mean(_safe_div(depamor + sbcomp, opex), 4), 4), 8))
def cg_f060_non_cash_expense_mix_core138_2nd_v139_signal(depamor, sbcomp, netinc, opex):
    return _clean(_z(_diff(_mean(_safe_div(sbcomp, netinc.abs() + 1.0), 4), 4), 8))
def cg_f060_non_cash_expense_mix_core139_2nd_v140_signal(depamor, sbcomp, netinc, opex):
    return _clean(_z(_diff(_mean(_safe_div(depamor, netinc.abs() + 1.0), 4), 4), 8))
def cg_f060_non_cash_expense_mix_core140_2nd_v141_signal(depamor, sbcomp, netinc, opex):
    return _clean(_rank(_slope(_mean(depamor, 4), 4), 12))
def cg_f060_non_cash_expense_mix_core141_2nd_v142_signal(depamor, sbcomp, netinc, opex):
    return _clean(_rank(_slope(_mean(sbcomp, 4), 4), 12))
def cg_f060_non_cash_expense_mix_core142_2nd_v143_signal(depamor, sbcomp, netinc, opex):
    return _clean(_rank(_slope(_mean(netinc, 4), 4), 12))
def cg_f060_non_cash_expense_mix_core143_2nd_v144_signal(depamor, sbcomp, netinc, opex):
    return _clean(_rank(_slope(_mean(opex, 4), 4), 12))
def cg_f060_non_cash_expense_mix_core144_2nd_v145_signal(depamor, sbcomp, netinc, opex):
    return _clean(_rank(_slope(_mean(depamor + sbcomp, 4), 4), 12))
def cg_f060_non_cash_expense_mix_core145_2nd_v146_signal(depamor, sbcomp, netinc, opex):
    return _clean(_rank(_slope(_mean(_safe_div(depamor, opex), 4), 4), 12))
def cg_f060_non_cash_expense_mix_core146_2nd_v147_signal(depamor, sbcomp, netinc, opex):
    return _clean(_rank(_slope(_mean(_safe_div(sbcomp, opex), 4), 4), 12))
def cg_f060_non_cash_expense_mix_core147_2nd_v148_signal(depamor, sbcomp, netinc, opex):
    return _clean(_rank(_slope(_mean(_safe_div(depamor + sbcomp, opex), 4), 4), 12))
def cg_f060_non_cash_expense_mix_core148_2nd_v149_signal(depamor, sbcomp, netinc, opex):
    return _clean(_rank(_slope(_mean(_safe_div(sbcomp, netinc.abs() + 1.0), 4), 4), 12))
def cg_f060_non_cash_expense_mix_core149_2nd_v150_signal(depamor, sbcomp, netinc, opex):
    return _clean(_rank(_slope(_mean(_safe_div(depamor, netinc.abs() + 1.0), 4), 4), 12))