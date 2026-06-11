import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f045_receivables_payables_core00_2nd_v001_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(receivables, 4))
def cg_f045_receivables_payables_core01_2nd_v002_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(payables, 4))
def cg_f045_receivables_payables_core02_2nd_v003_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_safe_div(receivables, revenue), 4))
def cg_f045_receivables_payables_core03_2nd_v004_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_safe_div(payables, revenue), 4))
def cg_f045_receivables_payables_core04_2nd_v005_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_safe_div(receivables, payables.abs() + 1.0), 4))
def cg_f045_receivables_payables_core05_2nd_v006_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_safe_div(receivables, liabilitiesc), 4))
def cg_f045_receivables_payables_core06_2nd_v007_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_safe_div(payables, opex), 4))
def cg_f045_receivables_payables_core07_2nd_v008_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_diff(receivables, 4), 4))
def cg_f045_receivables_payables_core08_2nd_v009_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_diff(payables, 4), 4))
def cg_f045_receivables_payables_core09_2nd_v010_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_pct_change(receivables, 4), 4))
def cg_f045_receivables_payables_core10_2nd_v011_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(receivables, 8))
def cg_f045_receivables_payables_core11_2nd_v012_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(payables, 8))
def cg_f045_receivables_payables_core12_2nd_v013_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_safe_div(receivables, revenue), 8))
def cg_f045_receivables_payables_core13_2nd_v014_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_safe_div(payables, revenue), 8))
def cg_f045_receivables_payables_core14_2nd_v015_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_safe_div(receivables, payables.abs() + 1.0), 8))
def cg_f045_receivables_payables_core15_2nd_v016_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_safe_div(receivables, liabilitiesc), 8))
def cg_f045_receivables_payables_core16_2nd_v017_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_safe_div(payables, opex), 8))
def cg_f045_receivables_payables_core17_2nd_v018_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_diff(receivables, 4), 8))
def cg_f045_receivables_payables_core18_2nd_v019_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_diff(payables, 4), 8))
def cg_f045_receivables_payables_core19_2nd_v020_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_pct_change(receivables, 4), 8))
def cg_f045_receivables_payables_core20_2nd_v021_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(receivables, 4))
def cg_f045_receivables_payables_core21_2nd_v022_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(payables, 4))
def cg_f045_receivables_payables_core22_2nd_v023_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_safe_div(receivables, revenue), 4))
def cg_f045_receivables_payables_core23_2nd_v024_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_safe_div(payables, revenue), 4))
def cg_f045_receivables_payables_core24_2nd_v025_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_safe_div(receivables, payables.abs() + 1.0), 4))
def cg_f045_receivables_payables_core25_2nd_v026_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_safe_div(receivables, liabilitiesc), 4))
def cg_f045_receivables_payables_core26_2nd_v027_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_safe_div(payables, opex), 4))
def cg_f045_receivables_payables_core27_2nd_v028_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_diff(receivables, 4), 4))
def cg_f045_receivables_payables_core28_2nd_v029_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_diff(payables, 4), 4))
def cg_f045_receivables_payables_core29_2nd_v030_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_pct_change(receivables, 4), 4))
def cg_f045_receivables_payables_core30_2nd_v031_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_slope(receivables, 4), 8))
def cg_f045_receivables_payables_core31_2nd_v032_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_slope(payables, 4), 8))
def cg_f045_receivables_payables_core32_2nd_v033_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_slope(_safe_div(receivables, revenue), 4), 8))
def cg_f045_receivables_payables_core33_2nd_v034_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_slope(_safe_div(payables, revenue), 4), 8))
def cg_f045_receivables_payables_core34_2nd_v035_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_slope(_safe_div(receivables, payables.abs() + 1.0), 4), 8))
def cg_f045_receivables_payables_core35_2nd_v036_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_slope(_safe_div(receivables, liabilitiesc), 4), 8))
def cg_f045_receivables_payables_core36_2nd_v037_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_slope(_safe_div(payables, opex), 4), 8))
def cg_f045_receivables_payables_core37_2nd_v038_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_slope(_diff(receivables, 4), 4), 8))
def cg_f045_receivables_payables_core38_2nd_v039_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_slope(_diff(payables, 4), 4), 8))
def cg_f045_receivables_payables_core39_2nd_v040_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_slope(_pct_change(receivables, 4), 4), 8))
def cg_f045_receivables_payables_core40_2nd_v041_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_slope(receivables, 8), 12))
def cg_f045_receivables_payables_core41_2nd_v042_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_slope(payables, 8), 12))
def cg_f045_receivables_payables_core42_2nd_v043_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_slope(_safe_div(receivables, revenue), 8), 12))
def cg_f045_receivables_payables_core43_2nd_v044_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_slope(_safe_div(payables, revenue), 8), 12))
def cg_f045_receivables_payables_core44_2nd_v045_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_slope(_safe_div(receivables, payables.abs() + 1.0), 8), 12))
def cg_f045_receivables_payables_core45_2nd_v046_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_slope(_safe_div(receivables, liabilitiesc), 8), 12))
def cg_f045_receivables_payables_core46_2nd_v047_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_slope(_safe_div(payables, opex), 8), 12))
def cg_f045_receivables_payables_core47_2nd_v048_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_slope(_diff(receivables, 4), 8), 12))
def cg_f045_receivables_payables_core48_2nd_v049_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_slope(_diff(payables, 4), 8), 12))
def cg_f045_receivables_payables_core49_2nd_v050_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_slope(_pct_change(receivables, 4), 8), 12))
def cg_f045_receivables_payables_core50_2nd_v051_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_diff(receivables, 4), 8))
def cg_f045_receivables_payables_core51_2nd_v052_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_diff(payables, 4), 8))
def cg_f045_receivables_payables_core52_2nd_v053_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_diff(_safe_div(receivables, revenue), 4), 8))
def cg_f045_receivables_payables_core53_2nd_v054_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_diff(_safe_div(payables, revenue), 4), 8))
def cg_f045_receivables_payables_core54_2nd_v055_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_diff(_safe_div(receivables, payables.abs() + 1.0), 4), 8))
def cg_f045_receivables_payables_core55_2nd_v056_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_diff(_safe_div(receivables, liabilitiesc), 4), 8))
def cg_f045_receivables_payables_core56_2nd_v057_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_diff(_safe_div(payables, opex), 4), 8))
def cg_f045_receivables_payables_core57_2nd_v058_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_diff(_diff(receivables, 4), 4), 8))
def cg_f045_receivables_payables_core58_2nd_v059_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_diff(_diff(payables, 4), 4), 8))
def cg_f045_receivables_payables_core59_2nd_v060_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_diff(_pct_change(receivables, 4), 4), 8))
def cg_f045_receivables_payables_core60_2nd_v061_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_slope(receivables, 4), 12))
def cg_f045_receivables_payables_core61_2nd_v062_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_slope(payables, 4), 12))
def cg_f045_receivables_payables_core62_2nd_v063_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_slope(_safe_div(receivables, revenue), 4), 12))
def cg_f045_receivables_payables_core63_2nd_v064_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_slope(_safe_div(payables, revenue), 4), 12))
def cg_f045_receivables_payables_core64_2nd_v065_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_slope(_safe_div(receivables, payables.abs() + 1.0), 4), 12))
def cg_f045_receivables_payables_core65_2nd_v066_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_slope(_safe_div(receivables, liabilitiesc), 4), 12))
def cg_f045_receivables_payables_core66_2nd_v067_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_slope(_safe_div(payables, opex), 4), 12))
def cg_f045_receivables_payables_core67_2nd_v068_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_slope(_diff(receivables, 4), 4), 12))
def cg_f045_receivables_payables_core68_2nd_v069_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_slope(_diff(payables, 4), 4), 12))
def cg_f045_receivables_payables_core69_2nd_v070_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_slope(_pct_change(receivables, 4), 4), 12))
def cg_f045_receivables_payables_core70_2nd_v071_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_diff(receivables, 4), 12))
def cg_f045_receivables_payables_core71_2nd_v072_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_diff(payables, 4), 12))
def cg_f045_receivables_payables_core72_2nd_v073_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_diff(_safe_div(receivables, revenue), 4), 12))
def cg_f045_receivables_payables_core73_2nd_v074_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_diff(_safe_div(payables, revenue), 4), 12))
def cg_f045_receivables_payables_core74_2nd_v075_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_diff(_safe_div(receivables, payables.abs() + 1.0), 4), 12))
def cg_f045_receivables_payables_core75_2nd_v076_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_diff(_safe_div(receivables, liabilitiesc), 4), 12))
def cg_f045_receivables_payables_core76_2nd_v077_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_diff(_safe_div(payables, opex), 4), 12))
def cg_f045_receivables_payables_core77_2nd_v078_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_diff(_diff(receivables, 4), 4), 12))
def cg_f045_receivables_payables_core78_2nd_v079_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_diff(_diff(payables, 4), 4), 12))
def cg_f045_receivables_payables_core79_2nd_v080_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_diff(_pct_change(receivables, 4), 4), 12))
def cg_f045_receivables_payables_core80_2nd_v081_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_slope(receivables, 4), 4))
def cg_f045_receivables_payables_core81_2nd_v082_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_slope(payables, 4), 4))
def cg_f045_receivables_payables_core82_2nd_v083_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_slope(_safe_div(receivables, revenue), 4), 4))
def cg_f045_receivables_payables_core83_2nd_v084_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_slope(_safe_div(payables, revenue), 4), 4))
def cg_f045_receivables_payables_core84_2nd_v085_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_slope(_safe_div(receivables, payables.abs() + 1.0), 4), 4))
def cg_f045_receivables_payables_core85_2nd_v086_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_slope(_safe_div(receivables, liabilitiesc), 4), 4))
def cg_f045_receivables_payables_core86_2nd_v087_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_slope(_safe_div(payables, opex), 4), 4))
def cg_f045_receivables_payables_core87_2nd_v088_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_slope(_diff(receivables, 4), 4), 4))
def cg_f045_receivables_payables_core88_2nd_v089_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_slope(_diff(payables, 4), 4), 4))
def cg_f045_receivables_payables_core89_2nd_v090_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_slope(_pct_change(receivables, 4), 4), 4))
def cg_f045_receivables_payables_core90_2nd_v091_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_diff(receivables, 4), 4))
def cg_f045_receivables_payables_core91_2nd_v092_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_diff(payables, 4), 4))
def cg_f045_receivables_payables_core92_2nd_v093_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_diff(_safe_div(receivables, revenue), 4), 4))
def cg_f045_receivables_payables_core93_2nd_v094_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_diff(_safe_div(payables, revenue), 4), 4))
def cg_f045_receivables_payables_core94_2nd_v095_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_diff(_safe_div(receivables, payables.abs() + 1.0), 4), 4))
def cg_f045_receivables_payables_core95_2nd_v096_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_diff(_safe_div(receivables, liabilitiesc), 4), 4))
def cg_f045_receivables_payables_core96_2nd_v097_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_diff(_safe_div(payables, opex), 4), 4))
def cg_f045_receivables_payables_core97_2nd_v098_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_diff(_diff(receivables, 4), 4), 4))
def cg_f045_receivables_payables_core98_2nd_v099_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_diff(_diff(payables, 4), 4), 4))
def cg_f045_receivables_payables_core99_2nd_v100_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_diff(_pct_change(receivables, 4), 4), 4))
def cg_f045_receivables_payables_core100_2nd_v101_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_mean(receivables, 4), 4))
def cg_f045_receivables_payables_core101_2nd_v102_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_mean(payables, 4), 4))
def cg_f045_receivables_payables_core102_2nd_v103_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_mean(_safe_div(receivables, revenue), 4), 4))
def cg_f045_receivables_payables_core103_2nd_v104_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_mean(_safe_div(payables, revenue), 4), 4))
def cg_f045_receivables_payables_core104_2nd_v105_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_mean(_safe_div(receivables, payables.abs() + 1.0), 4), 4))
def cg_f045_receivables_payables_core105_2nd_v106_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_mean(_safe_div(receivables, liabilitiesc), 4), 4))
def cg_f045_receivables_payables_core106_2nd_v107_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_mean(_safe_div(payables, opex), 4), 4))
def cg_f045_receivables_payables_core107_2nd_v108_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_mean(_diff(receivables, 4), 4), 4))
def cg_f045_receivables_payables_core108_2nd_v109_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_mean(_diff(payables, 4), 4), 4))
def cg_f045_receivables_payables_core109_2nd_v110_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_mean(_pct_change(receivables, 4), 4), 4))
def cg_f045_receivables_payables_core110_2nd_v111_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_mean(receivables, 8), 8))
def cg_f045_receivables_payables_core111_2nd_v112_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_mean(payables, 8), 8))
def cg_f045_receivables_payables_core112_2nd_v113_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_mean(_safe_div(receivables, revenue), 8), 8))
def cg_f045_receivables_payables_core113_2nd_v114_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_mean(_safe_div(payables, revenue), 8), 8))
def cg_f045_receivables_payables_core114_2nd_v115_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_mean(_safe_div(receivables, payables.abs() + 1.0), 8), 8))
def cg_f045_receivables_payables_core115_2nd_v116_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_mean(_safe_div(receivables, liabilitiesc), 8), 8))
def cg_f045_receivables_payables_core116_2nd_v117_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_mean(_safe_div(payables, opex), 8), 8))
def cg_f045_receivables_payables_core117_2nd_v118_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_mean(_diff(receivables, 4), 8), 8))
def cg_f045_receivables_payables_core118_2nd_v119_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_mean(_diff(payables, 4), 8), 8))
def cg_f045_receivables_payables_core119_2nd_v120_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_mean(_pct_change(receivables, 4), 8), 8))
def cg_f045_receivables_payables_core120_2nd_v121_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_mean(receivables, 4), 4))
def cg_f045_receivables_payables_core121_2nd_v122_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_mean(payables, 4), 4))
def cg_f045_receivables_payables_core122_2nd_v123_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_mean(_safe_div(receivables, revenue), 4), 4))
def cg_f045_receivables_payables_core123_2nd_v124_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_mean(_safe_div(payables, revenue), 4), 4))
def cg_f045_receivables_payables_core124_2nd_v125_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_mean(_safe_div(receivables, payables.abs() + 1.0), 4), 4))
def cg_f045_receivables_payables_core125_2nd_v126_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_mean(_safe_div(receivables, liabilitiesc), 4), 4))
def cg_f045_receivables_payables_core126_2nd_v127_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_mean(_safe_div(payables, opex), 4), 4))
def cg_f045_receivables_payables_core127_2nd_v128_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_mean(_diff(receivables, 4), 4), 4))
def cg_f045_receivables_payables_core128_2nd_v129_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_mean(_diff(payables, 4), 4), 4))
def cg_f045_receivables_payables_core129_2nd_v130_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_mean(_pct_change(receivables, 4), 4), 4))
def cg_f045_receivables_payables_core130_2nd_v131_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_diff(_mean(receivables, 4), 4), 8))
def cg_f045_receivables_payables_core131_2nd_v132_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_diff(_mean(payables, 4), 4), 8))
def cg_f045_receivables_payables_core132_2nd_v133_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_diff(_mean(_safe_div(receivables, revenue), 4), 4), 8))
def cg_f045_receivables_payables_core133_2nd_v134_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_diff(_mean(_safe_div(payables, revenue), 4), 4), 8))
def cg_f045_receivables_payables_core134_2nd_v135_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_diff(_mean(_safe_div(receivables, payables.abs() + 1.0), 4), 4), 8))
def cg_f045_receivables_payables_core135_2nd_v136_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_diff(_mean(_safe_div(receivables, liabilitiesc), 4), 4), 8))
def cg_f045_receivables_payables_core136_2nd_v137_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_diff(_mean(_safe_div(payables, opex), 4), 4), 8))
def cg_f045_receivables_payables_core137_2nd_v138_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_diff(_mean(_diff(receivables, 4), 4), 4), 8))
def cg_f045_receivables_payables_core138_2nd_v139_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_diff(_mean(_diff(payables, 4), 4), 4), 8))
def cg_f045_receivables_payables_core139_2nd_v140_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_diff(_mean(_pct_change(receivables, 4), 4), 4), 8))
def cg_f045_receivables_payables_core140_2nd_v141_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_slope(_mean(receivables, 4), 4), 12))
def cg_f045_receivables_payables_core141_2nd_v142_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_slope(_mean(payables, 4), 4), 12))
def cg_f045_receivables_payables_core142_2nd_v143_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_slope(_mean(_safe_div(receivables, revenue), 4), 4), 12))
def cg_f045_receivables_payables_core143_2nd_v144_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_slope(_mean(_safe_div(payables, revenue), 4), 4), 12))
def cg_f045_receivables_payables_core144_2nd_v145_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_slope(_mean(_safe_div(receivables, payables.abs() + 1.0), 4), 4), 12))
def cg_f045_receivables_payables_core145_2nd_v146_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_slope(_mean(_safe_div(receivables, liabilitiesc), 4), 4), 12))
def cg_f045_receivables_payables_core146_2nd_v147_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_slope(_mean(_safe_div(payables, opex), 4), 4), 12))
def cg_f045_receivables_payables_core147_2nd_v148_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_slope(_mean(_diff(receivables, 4), 4), 4), 12))
def cg_f045_receivables_payables_core148_2nd_v149_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_slope(_mean(_diff(payables, 4), 4), 4), 12))
def cg_f045_receivables_payables_core149_2nd_v150_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_slope(_mean(_pct_change(receivables, 4), 4), 4), 12))