import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f045_receivables_payables_core00_3rd_v001_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_diff(receivables, 4), 4))
def cg_f045_receivables_payables_core01_3rd_v002_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_diff(payables, 4), 4))
def cg_f045_receivables_payables_core02_3rd_v003_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_diff(_safe_div(receivables, revenue), 4), 4))
def cg_f045_receivables_payables_core03_3rd_v004_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_diff(_safe_div(payables, revenue), 4), 4))
def cg_f045_receivables_payables_core04_3rd_v005_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_diff(_safe_div(receivables, payables.abs() + 1.0), 4), 4))
def cg_f045_receivables_payables_core05_3rd_v006_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_diff(_safe_div(receivables, liabilitiesc), 4), 4))
def cg_f045_receivables_payables_core06_3rd_v007_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_diff(_safe_div(payables, opex), 4), 4))
def cg_f045_receivables_payables_core07_3rd_v008_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_diff(_diff(receivables, 4), 4), 4))
def cg_f045_receivables_payables_core08_3rd_v009_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_diff(_diff(payables, 4), 4), 4))
def cg_f045_receivables_payables_core09_3rd_v010_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_diff(_pct_change(receivables, 4), 4), 4))
def cg_f045_receivables_payables_core10_3rd_v011_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_diff(receivables, 4), 8))
def cg_f045_receivables_payables_core11_3rd_v012_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_diff(payables, 4), 8))
def cg_f045_receivables_payables_core12_3rd_v013_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_diff(_safe_div(receivables, revenue), 4), 8))
def cg_f045_receivables_payables_core13_3rd_v014_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_diff(_safe_div(payables, revenue), 4), 8))
def cg_f045_receivables_payables_core14_3rd_v015_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_diff(_safe_div(receivables, payables.abs() + 1.0), 4), 8))
def cg_f045_receivables_payables_core15_3rd_v016_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_diff(_safe_div(receivables, liabilitiesc), 4), 8))
def cg_f045_receivables_payables_core16_3rd_v017_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_diff(_safe_div(payables, opex), 4), 8))
def cg_f045_receivables_payables_core17_3rd_v018_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_diff(_diff(receivables, 4), 4), 8))
def cg_f045_receivables_payables_core18_3rd_v019_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_diff(_diff(payables, 4), 4), 8))
def cg_f045_receivables_payables_core19_3rd_v020_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_diff(_pct_change(receivables, 4), 4), 8))
def cg_f045_receivables_payables_core20_3rd_v021_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_slope(receivables, 4), 4))
def cg_f045_receivables_payables_core21_3rd_v022_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_slope(payables, 4), 4))
def cg_f045_receivables_payables_core22_3rd_v023_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_slope(_safe_div(receivables, revenue), 4), 4))
def cg_f045_receivables_payables_core23_3rd_v024_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_slope(_safe_div(payables, revenue), 4), 4))
def cg_f045_receivables_payables_core24_3rd_v025_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_slope(_safe_div(receivables, payables.abs() + 1.0), 4), 4))
def cg_f045_receivables_payables_core25_3rd_v026_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_slope(_safe_div(receivables, liabilitiesc), 4), 4))
def cg_f045_receivables_payables_core26_3rd_v027_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_slope(_safe_div(payables, opex), 4), 4))
def cg_f045_receivables_payables_core27_3rd_v028_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_slope(_diff(receivables, 4), 4), 4))
def cg_f045_receivables_payables_core28_3rd_v029_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_slope(_diff(payables, 4), 4), 4))
def cg_f045_receivables_payables_core29_3rd_v030_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_slope(_pct_change(receivables, 4), 4), 4))
def cg_f045_receivables_payables_core30_3rd_v031_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_diff(_diff(receivables, 4), 4), 8))
def cg_f045_receivables_payables_core31_3rd_v032_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_diff(_diff(payables, 4), 4), 8))
def cg_f045_receivables_payables_core32_3rd_v033_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_diff(_diff(_safe_div(receivables, revenue), 4), 4), 8))
def cg_f045_receivables_payables_core33_3rd_v034_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_diff(_diff(_safe_div(payables, revenue), 4), 4), 8))
def cg_f045_receivables_payables_core34_3rd_v035_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_diff(_diff(_safe_div(receivables, payables.abs() + 1.0), 4), 4), 8))
def cg_f045_receivables_payables_core35_3rd_v036_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_diff(_diff(_safe_div(receivables, liabilitiesc), 4), 4), 8))
def cg_f045_receivables_payables_core36_3rd_v037_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_diff(_diff(_safe_div(payables, opex), 4), 4), 8))
def cg_f045_receivables_payables_core37_3rd_v038_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_diff(_diff(_diff(receivables, 4), 4), 4), 8))
def cg_f045_receivables_payables_core38_3rd_v039_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_diff(_diff(_diff(payables, 4), 4), 4), 8))
def cg_f045_receivables_payables_core39_3rd_v040_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_diff(_diff(_pct_change(receivables, 4), 4), 4), 8))
def cg_f045_receivables_payables_core40_3rd_v041_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_slope(_diff(receivables, 4), 8), 12))
def cg_f045_receivables_payables_core41_3rd_v042_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_slope(_diff(payables, 4), 8), 12))
def cg_f045_receivables_payables_core42_3rd_v043_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_slope(_diff(_safe_div(receivables, revenue), 4), 8), 12))
def cg_f045_receivables_payables_core43_3rd_v044_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_slope(_diff(_safe_div(payables, revenue), 4), 8), 12))
def cg_f045_receivables_payables_core44_3rd_v045_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_slope(_diff(_safe_div(receivables, payables.abs() + 1.0), 4), 8), 12))
def cg_f045_receivables_payables_core45_3rd_v046_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_slope(_diff(_safe_div(receivables, liabilitiesc), 4), 8), 12))
def cg_f045_receivables_payables_core46_3rd_v047_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_slope(_diff(_safe_div(payables, opex), 4), 8), 12))
def cg_f045_receivables_payables_core47_3rd_v048_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_slope(_diff(_diff(receivables, 4), 4), 8), 12))
def cg_f045_receivables_payables_core48_3rd_v049_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_slope(_diff(_diff(payables, 4), 4), 8), 12))
def cg_f045_receivables_payables_core49_3rd_v050_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_slope(_diff(_pct_change(receivables, 4), 4), 8), 12))
def cg_f045_receivables_payables_core50_3rd_v051_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_diff(_slope(receivables, 4), 4), 8))
def cg_f045_receivables_payables_core51_3rd_v052_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_diff(_slope(payables, 4), 4), 8))
def cg_f045_receivables_payables_core52_3rd_v053_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_diff(_slope(_safe_div(receivables, revenue), 4), 4), 8))
def cg_f045_receivables_payables_core53_3rd_v054_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_diff(_slope(_safe_div(payables, revenue), 4), 4), 8))
def cg_f045_receivables_payables_core54_3rd_v055_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_diff(_slope(_safe_div(receivables, payables.abs() + 1.0), 4), 4), 8))
def cg_f045_receivables_payables_core55_3rd_v056_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_diff(_slope(_safe_div(receivables, liabilitiesc), 4), 4), 8))
def cg_f045_receivables_payables_core56_3rd_v057_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_diff(_slope(_safe_div(payables, opex), 4), 4), 8))
def cg_f045_receivables_payables_core57_3rd_v058_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_diff(_slope(_diff(receivables, 4), 4), 4), 8))
def cg_f045_receivables_payables_core58_3rd_v059_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_diff(_slope(_diff(payables, 4), 4), 4), 8))
def cg_f045_receivables_payables_core59_3rd_v060_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_diff(_slope(_pct_change(receivables, 4), 4), 4), 8))
def cg_f045_receivables_payables_core60_3rd_v061_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_diff(_diff(receivables, 4), 4), 12))
def cg_f045_receivables_payables_core61_3rd_v062_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_diff(_diff(payables, 4), 4), 12))
def cg_f045_receivables_payables_core62_3rd_v063_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_diff(_diff(_safe_div(receivables, revenue), 4), 4), 12))
def cg_f045_receivables_payables_core63_3rd_v064_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_diff(_diff(_safe_div(payables, revenue), 4), 4), 12))
def cg_f045_receivables_payables_core64_3rd_v065_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_diff(_diff(_safe_div(receivables, payables.abs() + 1.0), 4), 4), 12))
def cg_f045_receivables_payables_core65_3rd_v066_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_diff(_diff(_safe_div(receivables, liabilitiesc), 4), 4), 12))
def cg_f045_receivables_payables_core66_3rd_v067_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_diff(_diff(_safe_div(payables, opex), 4), 4), 12))
def cg_f045_receivables_payables_core67_3rd_v068_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_diff(_diff(_diff(receivables, 4), 4), 4), 12))
def cg_f045_receivables_payables_core68_3rd_v069_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_diff(_diff(_diff(payables, 4), 4), 4), 12))
def cg_f045_receivables_payables_core69_3rd_v070_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_diff(_diff(_pct_change(receivables, 4), 4), 4), 12))
def cg_f045_receivables_payables_core70_3rd_v071_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_slope(_diff(receivables, 4), 8), 12))
def cg_f045_receivables_payables_core71_3rd_v072_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_slope(_diff(payables, 4), 8), 12))
def cg_f045_receivables_payables_core72_3rd_v073_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_slope(_diff(_safe_div(receivables, revenue), 4), 8), 12))
def cg_f045_receivables_payables_core73_3rd_v074_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_slope(_diff(_safe_div(payables, revenue), 4), 8), 12))
def cg_f045_receivables_payables_core74_3rd_v075_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_slope(_diff(_safe_div(receivables, payables.abs() + 1.0), 4), 8), 12))
def cg_f045_receivables_payables_core75_3rd_v076_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_slope(_diff(_safe_div(receivables, liabilitiesc), 4), 8), 12))
def cg_f045_receivables_payables_core76_3rd_v077_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_slope(_diff(_safe_div(payables, opex), 4), 8), 12))
def cg_f045_receivables_payables_core77_3rd_v078_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_slope(_diff(_diff(receivables, 4), 4), 8), 12))
def cg_f045_receivables_payables_core78_3rd_v079_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_slope(_diff(_diff(payables, 4), 4), 8), 12))
def cg_f045_receivables_payables_core79_3rd_v080_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_slope(_diff(_pct_change(receivables, 4), 4), 8), 12))
def cg_f045_receivables_payables_core80_3rd_v081_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_diff(_slope(receivables, 4), 4), 12))
def cg_f045_receivables_payables_core81_3rd_v082_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_diff(_slope(payables, 4), 4), 12))
def cg_f045_receivables_payables_core82_3rd_v083_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_diff(_slope(_safe_div(receivables, revenue), 4), 4), 12))
def cg_f045_receivables_payables_core83_3rd_v084_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_diff(_slope(_safe_div(payables, revenue), 4), 4), 12))
def cg_f045_receivables_payables_core84_3rd_v085_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_diff(_slope(_safe_div(receivables, payables.abs() + 1.0), 4), 4), 12))
def cg_f045_receivables_payables_core85_3rd_v086_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_diff(_slope(_safe_div(receivables, liabilitiesc), 4), 4), 12))
def cg_f045_receivables_payables_core86_3rd_v087_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_diff(_slope(_safe_div(payables, opex), 4), 4), 12))
def cg_f045_receivables_payables_core87_3rd_v088_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_diff(_slope(_diff(receivables, 4), 4), 4), 12))
def cg_f045_receivables_payables_core88_3rd_v089_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_diff(_slope(_diff(payables, 4), 4), 4), 12))
def cg_f045_receivables_payables_core89_3rd_v090_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_rank(_diff(_slope(_pct_change(receivables, 4), 4), 4), 12))
def cg_f045_receivables_payables_core90_3rd_v091_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_diff(_diff(receivables, 4), 4), 4))
def cg_f045_receivables_payables_core91_3rd_v092_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_diff(_diff(payables, 4), 4), 4))
def cg_f045_receivables_payables_core92_3rd_v093_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_diff(_diff(_safe_div(receivables, revenue), 4), 4), 4))
def cg_f045_receivables_payables_core93_3rd_v094_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_diff(_diff(_safe_div(payables, revenue), 4), 4), 4))
def cg_f045_receivables_payables_core94_3rd_v095_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_diff(_diff(_safe_div(receivables, payables.abs() + 1.0), 4), 4), 4))
def cg_f045_receivables_payables_core95_3rd_v096_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_diff(_diff(_safe_div(receivables, liabilitiesc), 4), 4), 4))
def cg_f045_receivables_payables_core96_3rd_v097_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_diff(_diff(_safe_div(payables, opex), 4), 4), 4))
def cg_f045_receivables_payables_core97_3rd_v098_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_diff(_diff(_diff(receivables, 4), 4), 4), 4))
def cg_f045_receivables_payables_core98_3rd_v099_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_diff(_diff(_diff(payables, 4), 4), 4), 4))
def cg_f045_receivables_payables_core99_3rd_v100_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_diff(_diff(_pct_change(receivables, 4), 4), 4), 4))
def cg_f045_receivables_payables_core100_3rd_v101_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_slope(_diff(receivables, 4), 8), 4))
def cg_f045_receivables_payables_core101_3rd_v102_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_slope(_diff(payables, 4), 8), 4))
def cg_f045_receivables_payables_core102_3rd_v103_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_slope(_diff(_safe_div(receivables, revenue), 4), 8), 4))
def cg_f045_receivables_payables_core103_3rd_v104_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_slope(_diff(_safe_div(payables, revenue), 4), 8), 4))
def cg_f045_receivables_payables_core104_3rd_v105_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_slope(_diff(_safe_div(receivables, payables.abs() + 1.0), 4), 8), 4))
def cg_f045_receivables_payables_core105_3rd_v106_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_slope(_diff(_safe_div(receivables, liabilitiesc), 4), 8), 4))
def cg_f045_receivables_payables_core106_3rd_v107_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_slope(_diff(_safe_div(payables, opex), 4), 8), 4))
def cg_f045_receivables_payables_core107_3rd_v108_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_slope(_diff(_diff(receivables, 4), 4), 8), 4))
def cg_f045_receivables_payables_core108_3rd_v109_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_slope(_diff(_diff(payables, 4), 4), 8), 4))
def cg_f045_receivables_payables_core109_3rd_v110_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_slope(_diff(_pct_change(receivables, 4), 4), 8), 4))
def cg_f045_receivables_payables_core110_3rd_v111_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_diff(_slope(receivables, 4), 4), 4))
def cg_f045_receivables_payables_core111_3rd_v112_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_diff(_slope(payables, 4), 4), 4))
def cg_f045_receivables_payables_core112_3rd_v113_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_diff(_slope(_safe_div(receivables, revenue), 4), 4), 4))
def cg_f045_receivables_payables_core113_3rd_v114_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_diff(_slope(_safe_div(payables, revenue), 4), 4), 4))
def cg_f045_receivables_payables_core114_3rd_v115_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_diff(_slope(_safe_div(receivables, payables.abs() + 1.0), 4), 4), 4))
def cg_f045_receivables_payables_core115_3rd_v116_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_diff(_slope(_safe_div(receivables, liabilitiesc), 4), 4), 4))
def cg_f045_receivables_payables_core116_3rd_v117_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_diff(_slope(_safe_div(payables, opex), 4), 4), 4))
def cg_f045_receivables_payables_core117_3rd_v118_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_diff(_slope(_diff(receivables, 4), 4), 4), 4))
def cg_f045_receivables_payables_core118_3rd_v119_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_diff(_slope(_diff(payables, 4), 4), 4), 4))
def cg_f045_receivables_payables_core119_3rd_v120_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_mean(_diff(_slope(_pct_change(receivables, 4), 4), 4), 4))
def cg_f045_receivables_payables_core120_3rd_v121_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_diff(_diff(receivables, 4), 4), 4))
def cg_f045_receivables_payables_core121_3rd_v122_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_diff(_diff(payables, 4), 4), 4))
def cg_f045_receivables_payables_core122_3rd_v123_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_diff(_diff(_safe_div(receivables, revenue), 4), 4), 4))
def cg_f045_receivables_payables_core123_3rd_v124_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_diff(_diff(_safe_div(payables, revenue), 4), 4), 4))
def cg_f045_receivables_payables_core124_3rd_v125_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_diff(_diff(_safe_div(receivables, payables.abs() + 1.0), 4), 4), 4))
def cg_f045_receivables_payables_core125_3rd_v126_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_diff(_diff(_safe_div(receivables, liabilitiesc), 4), 4), 4))
def cg_f045_receivables_payables_core126_3rd_v127_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_diff(_diff(_safe_div(payables, opex), 4), 4), 4))
def cg_f045_receivables_payables_core127_3rd_v128_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_diff(_diff(_diff(receivables, 4), 4), 4), 4))
def cg_f045_receivables_payables_core128_3rd_v129_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_diff(_diff(_diff(payables, 4), 4), 4), 4))
def cg_f045_receivables_payables_core129_3rd_v130_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_slope(_diff(_diff(_pct_change(receivables, 4), 4), 4), 4))
def cg_f045_receivables_payables_core130_3rd_v131_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_diff(_diff(receivables, 4), 4), 4))
def cg_f045_receivables_payables_core131_3rd_v132_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_diff(_diff(payables, 4), 4), 4))
def cg_f045_receivables_payables_core132_3rd_v133_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_diff(_diff(_safe_div(receivables, revenue), 4), 4), 4))
def cg_f045_receivables_payables_core133_3rd_v134_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_diff(_diff(_safe_div(payables, revenue), 4), 4), 4))
def cg_f045_receivables_payables_core134_3rd_v135_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_diff(_diff(_safe_div(receivables, payables.abs() + 1.0), 4), 4), 4))
def cg_f045_receivables_payables_core135_3rd_v136_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_diff(_diff(_safe_div(receivables, liabilitiesc), 4), 4), 4))
def cg_f045_receivables_payables_core136_3rd_v137_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_diff(_diff(_safe_div(payables, opex), 4), 4), 4))
def cg_f045_receivables_payables_core137_3rd_v138_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_diff(_diff(_diff(receivables, 4), 4), 4), 4))
def cg_f045_receivables_payables_core138_3rd_v139_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_diff(_diff(_diff(payables, 4), 4), 4), 4))
def cg_f045_receivables_payables_core139_3rd_v140_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_diff(_diff(_diff(_pct_change(receivables, 4), 4), 4), 4))
def cg_f045_receivables_payables_core140_3rd_v141_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_slope(_diff(_diff(receivables, 4), 4), 4), 8))
def cg_f045_receivables_payables_core141_3rd_v142_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_slope(_diff(_diff(payables, 4), 4), 4), 8))
def cg_f045_receivables_payables_core142_3rd_v143_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_slope(_diff(_diff(_safe_div(receivables, revenue), 4), 4), 4), 8))
def cg_f045_receivables_payables_core143_3rd_v144_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_slope(_diff(_diff(_safe_div(payables, revenue), 4), 4), 4), 8))
def cg_f045_receivables_payables_core144_3rd_v145_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_slope(_diff(_diff(_safe_div(receivables, payables.abs() + 1.0), 4), 4), 4), 8))
def cg_f045_receivables_payables_core145_3rd_v146_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_slope(_diff(_diff(_safe_div(receivables, liabilitiesc), 4), 4), 4), 8))
def cg_f045_receivables_payables_core146_3rd_v147_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_slope(_diff(_diff(_safe_div(payables, opex), 4), 4), 4), 8))
def cg_f045_receivables_payables_core147_3rd_v148_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_slope(_diff(_diff(_diff(receivables, 4), 4), 4), 4), 8))
def cg_f045_receivables_payables_core148_3rd_v149_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_slope(_diff(_diff(_diff(payables, 4), 4), 4), 4), 8))
def cg_f045_receivables_payables_core149_3rd_v150_signal(receivables, payables, revenue, opex, liabilitiesc):
    return _clean(_z(_slope(_diff(_diff(_pct_change(receivables, 4), 4), 4), 4), 8))