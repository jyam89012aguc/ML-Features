import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f068_cash_conversion_cycle_core00_2nd_v001_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(receivables, 4))
def cg_f068_cash_conversion_cycle_core01_2nd_v002_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(inventory, 4))
def cg_f068_cash_conversion_cycle_core02_2nd_v003_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(payables, 4))
def cg_f068_cash_conversion_cycle_core03_2nd_v004_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(revenue, 4))
def cg_f068_cash_conversion_cycle_core04_2nd_v005_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(cor, 4))
def cg_f068_cash_conversion_cycle_core05_2nd_v006_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_safe_div(receivables, revenue) * 90.0, 4))
def cg_f068_cash_conversion_cycle_core06_2nd_v007_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_safe_div(inventory, cor) * 90.0, 4))
def cg_f068_cash_conversion_cycle_core07_2nd_v008_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_safe_div(payables, cor) * 90.0, 4))
def cg_f068_cash_conversion_cycle_core08_2nd_v009_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope((_safe_div(receivables, revenue) + _safe_div(inventory, cor) - _safe_div(payables, cor)) * 90.0, 4))
def cg_f068_cash_conversion_cycle_core09_2nd_v010_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_diff(receivables + inventory - payables, 4), 4))
def cg_f068_cash_conversion_cycle_core10_2nd_v011_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(receivables, 8))
def cg_f068_cash_conversion_cycle_core11_2nd_v012_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(inventory, 8))
def cg_f068_cash_conversion_cycle_core12_2nd_v013_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(payables, 8))
def cg_f068_cash_conversion_cycle_core13_2nd_v014_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(revenue, 8))
def cg_f068_cash_conversion_cycle_core14_2nd_v015_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(cor, 8))
def cg_f068_cash_conversion_cycle_core15_2nd_v016_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_safe_div(receivables, revenue) * 90.0, 8))
def cg_f068_cash_conversion_cycle_core16_2nd_v017_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_safe_div(inventory, cor) * 90.0, 8))
def cg_f068_cash_conversion_cycle_core17_2nd_v018_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_safe_div(payables, cor) * 90.0, 8))
def cg_f068_cash_conversion_cycle_core18_2nd_v019_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope((_safe_div(receivables, revenue) + _safe_div(inventory, cor) - _safe_div(payables, cor)) * 90.0, 8))
def cg_f068_cash_conversion_cycle_core19_2nd_v020_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_diff(receivables + inventory - payables, 4), 8))
def cg_f068_cash_conversion_cycle_core20_2nd_v021_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(receivables, 4))
def cg_f068_cash_conversion_cycle_core21_2nd_v022_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(inventory, 4))
def cg_f068_cash_conversion_cycle_core22_2nd_v023_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(payables, 4))
def cg_f068_cash_conversion_cycle_core23_2nd_v024_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(revenue, 4))
def cg_f068_cash_conversion_cycle_core24_2nd_v025_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(cor, 4))
def cg_f068_cash_conversion_cycle_core25_2nd_v026_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_safe_div(receivables, revenue) * 90.0, 4))
def cg_f068_cash_conversion_cycle_core26_2nd_v027_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_safe_div(inventory, cor) * 90.0, 4))
def cg_f068_cash_conversion_cycle_core27_2nd_v028_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_safe_div(payables, cor) * 90.0, 4))
def cg_f068_cash_conversion_cycle_core28_2nd_v029_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff((_safe_div(receivables, revenue) + _safe_div(inventory, cor) - _safe_div(payables, cor)) * 90.0, 4))
def cg_f068_cash_conversion_cycle_core29_2nd_v030_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_diff(receivables + inventory - payables, 4), 4))
def cg_f068_cash_conversion_cycle_core30_2nd_v031_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_slope(receivables, 4), 8))
def cg_f068_cash_conversion_cycle_core31_2nd_v032_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_slope(inventory, 4), 8))
def cg_f068_cash_conversion_cycle_core32_2nd_v033_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_slope(payables, 4), 8))
def cg_f068_cash_conversion_cycle_core33_2nd_v034_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_slope(revenue, 4), 8))
def cg_f068_cash_conversion_cycle_core34_2nd_v035_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_slope(cor, 4), 8))
def cg_f068_cash_conversion_cycle_core35_2nd_v036_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_slope(_safe_div(receivables, revenue) * 90.0, 4), 8))
def cg_f068_cash_conversion_cycle_core36_2nd_v037_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_slope(_safe_div(inventory, cor) * 90.0, 4), 8))
def cg_f068_cash_conversion_cycle_core37_2nd_v038_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_slope(_safe_div(payables, cor) * 90.0, 4), 8))
def cg_f068_cash_conversion_cycle_core38_2nd_v039_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_slope((_safe_div(receivables, revenue) + _safe_div(inventory, cor) - _safe_div(payables, cor)) * 90.0, 4), 8))
def cg_f068_cash_conversion_cycle_core39_2nd_v040_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_slope(_diff(receivables + inventory - payables, 4), 4), 8))
def cg_f068_cash_conversion_cycle_core40_2nd_v041_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_slope(receivables, 8), 12))
def cg_f068_cash_conversion_cycle_core41_2nd_v042_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_slope(inventory, 8), 12))
def cg_f068_cash_conversion_cycle_core42_2nd_v043_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_slope(payables, 8), 12))
def cg_f068_cash_conversion_cycle_core43_2nd_v044_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_slope(revenue, 8), 12))
def cg_f068_cash_conversion_cycle_core44_2nd_v045_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_slope(cor, 8), 12))
def cg_f068_cash_conversion_cycle_core45_2nd_v046_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_slope(_safe_div(receivables, revenue) * 90.0, 8), 12))
def cg_f068_cash_conversion_cycle_core46_2nd_v047_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_slope(_safe_div(inventory, cor) * 90.0, 8), 12))
def cg_f068_cash_conversion_cycle_core47_2nd_v048_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_slope(_safe_div(payables, cor) * 90.0, 8), 12))
def cg_f068_cash_conversion_cycle_core48_2nd_v049_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_slope((_safe_div(receivables, revenue) + _safe_div(inventory, cor) - _safe_div(payables, cor)) * 90.0, 8), 12))
def cg_f068_cash_conversion_cycle_core49_2nd_v050_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_slope(_diff(receivables + inventory - payables, 4), 8), 12))
def cg_f068_cash_conversion_cycle_core50_2nd_v051_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_diff(receivables, 4), 8))
def cg_f068_cash_conversion_cycle_core51_2nd_v052_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_diff(inventory, 4), 8))
def cg_f068_cash_conversion_cycle_core52_2nd_v053_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_diff(payables, 4), 8))
def cg_f068_cash_conversion_cycle_core53_2nd_v054_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_diff(revenue, 4), 8))
def cg_f068_cash_conversion_cycle_core54_2nd_v055_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_diff(cor, 4), 8))
def cg_f068_cash_conversion_cycle_core55_2nd_v056_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_diff(_safe_div(receivables, revenue) * 90.0, 4), 8))
def cg_f068_cash_conversion_cycle_core56_2nd_v057_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_diff(_safe_div(inventory, cor) * 90.0, 4), 8))
def cg_f068_cash_conversion_cycle_core57_2nd_v058_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_diff(_safe_div(payables, cor) * 90.0, 4), 8))
def cg_f068_cash_conversion_cycle_core58_2nd_v059_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_diff((_safe_div(receivables, revenue) + _safe_div(inventory, cor) - _safe_div(payables, cor)) * 90.0, 4), 8))
def cg_f068_cash_conversion_cycle_core59_2nd_v060_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_diff(_diff(receivables + inventory - payables, 4), 4), 8))
def cg_f068_cash_conversion_cycle_core60_2nd_v061_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_slope(receivables, 4), 12))
def cg_f068_cash_conversion_cycle_core61_2nd_v062_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_slope(inventory, 4), 12))
def cg_f068_cash_conversion_cycle_core62_2nd_v063_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_slope(payables, 4), 12))
def cg_f068_cash_conversion_cycle_core63_2nd_v064_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_slope(revenue, 4), 12))
def cg_f068_cash_conversion_cycle_core64_2nd_v065_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_slope(cor, 4), 12))
def cg_f068_cash_conversion_cycle_core65_2nd_v066_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_slope(_safe_div(receivables, revenue) * 90.0, 4), 12))
def cg_f068_cash_conversion_cycle_core66_2nd_v067_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_slope(_safe_div(inventory, cor) * 90.0, 4), 12))
def cg_f068_cash_conversion_cycle_core67_2nd_v068_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_slope(_safe_div(payables, cor) * 90.0, 4), 12))
def cg_f068_cash_conversion_cycle_core68_2nd_v069_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_slope((_safe_div(receivables, revenue) + _safe_div(inventory, cor) - _safe_div(payables, cor)) * 90.0, 4), 12))
def cg_f068_cash_conversion_cycle_core69_2nd_v070_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_slope(_diff(receivables + inventory - payables, 4), 4), 12))
def cg_f068_cash_conversion_cycle_core70_2nd_v071_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_diff(receivables, 4), 12))
def cg_f068_cash_conversion_cycle_core71_2nd_v072_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_diff(inventory, 4), 12))
def cg_f068_cash_conversion_cycle_core72_2nd_v073_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_diff(payables, 4), 12))
def cg_f068_cash_conversion_cycle_core73_2nd_v074_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_diff(revenue, 4), 12))
def cg_f068_cash_conversion_cycle_core74_2nd_v075_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_diff(cor, 4), 12))
def cg_f068_cash_conversion_cycle_core75_2nd_v076_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_diff(_safe_div(receivables, revenue) * 90.0, 4), 12))
def cg_f068_cash_conversion_cycle_core76_2nd_v077_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_diff(_safe_div(inventory, cor) * 90.0, 4), 12))
def cg_f068_cash_conversion_cycle_core77_2nd_v078_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_diff(_safe_div(payables, cor) * 90.0, 4), 12))
def cg_f068_cash_conversion_cycle_core78_2nd_v079_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_diff((_safe_div(receivables, revenue) + _safe_div(inventory, cor) - _safe_div(payables, cor)) * 90.0, 4), 12))
def cg_f068_cash_conversion_cycle_core79_2nd_v080_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_diff(_diff(receivables + inventory - payables, 4), 4), 12))
def cg_f068_cash_conversion_cycle_core80_2nd_v081_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_slope(receivables, 4), 4))
def cg_f068_cash_conversion_cycle_core81_2nd_v082_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_slope(inventory, 4), 4))
def cg_f068_cash_conversion_cycle_core82_2nd_v083_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_slope(payables, 4), 4))
def cg_f068_cash_conversion_cycle_core83_2nd_v084_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_slope(revenue, 4), 4))
def cg_f068_cash_conversion_cycle_core84_2nd_v085_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_slope(cor, 4), 4))
def cg_f068_cash_conversion_cycle_core85_2nd_v086_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_slope(_safe_div(receivables, revenue) * 90.0, 4), 4))
def cg_f068_cash_conversion_cycle_core86_2nd_v087_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_slope(_safe_div(inventory, cor) * 90.0, 4), 4))
def cg_f068_cash_conversion_cycle_core87_2nd_v088_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_slope(_safe_div(payables, cor) * 90.0, 4), 4))
def cg_f068_cash_conversion_cycle_core88_2nd_v089_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_slope((_safe_div(receivables, revenue) + _safe_div(inventory, cor) - _safe_div(payables, cor)) * 90.0, 4), 4))
def cg_f068_cash_conversion_cycle_core89_2nd_v090_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_slope(_diff(receivables + inventory - payables, 4), 4), 4))
def cg_f068_cash_conversion_cycle_core90_2nd_v091_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_diff(receivables, 4), 4))
def cg_f068_cash_conversion_cycle_core91_2nd_v092_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_diff(inventory, 4), 4))
def cg_f068_cash_conversion_cycle_core92_2nd_v093_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_diff(payables, 4), 4))
def cg_f068_cash_conversion_cycle_core93_2nd_v094_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_diff(revenue, 4), 4))
def cg_f068_cash_conversion_cycle_core94_2nd_v095_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_diff(cor, 4), 4))
def cg_f068_cash_conversion_cycle_core95_2nd_v096_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_diff(_safe_div(receivables, revenue) * 90.0, 4), 4))
def cg_f068_cash_conversion_cycle_core96_2nd_v097_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_diff(_safe_div(inventory, cor) * 90.0, 4), 4))
def cg_f068_cash_conversion_cycle_core97_2nd_v098_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_diff(_safe_div(payables, cor) * 90.0, 4), 4))
def cg_f068_cash_conversion_cycle_core98_2nd_v099_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_diff((_safe_div(receivables, revenue) + _safe_div(inventory, cor) - _safe_div(payables, cor)) * 90.0, 4), 4))
def cg_f068_cash_conversion_cycle_core99_2nd_v100_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_diff(_diff(receivables + inventory - payables, 4), 4), 4))
def cg_f068_cash_conversion_cycle_core100_2nd_v101_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_mean(receivables, 4), 4))
def cg_f068_cash_conversion_cycle_core101_2nd_v102_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_mean(inventory, 4), 4))
def cg_f068_cash_conversion_cycle_core102_2nd_v103_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_mean(payables, 4), 4))
def cg_f068_cash_conversion_cycle_core103_2nd_v104_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_mean(revenue, 4), 4))
def cg_f068_cash_conversion_cycle_core104_2nd_v105_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_mean(cor, 4), 4))
def cg_f068_cash_conversion_cycle_core105_2nd_v106_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_mean(_safe_div(receivables, revenue) * 90.0, 4), 4))
def cg_f068_cash_conversion_cycle_core106_2nd_v107_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_mean(_safe_div(inventory, cor) * 90.0, 4), 4))
def cg_f068_cash_conversion_cycle_core107_2nd_v108_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_mean(_safe_div(payables, cor) * 90.0, 4), 4))
def cg_f068_cash_conversion_cycle_core108_2nd_v109_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_mean((_safe_div(receivables, revenue) + _safe_div(inventory, cor) - _safe_div(payables, cor)) * 90.0, 4), 4))
def cg_f068_cash_conversion_cycle_core109_2nd_v110_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_mean(_diff(receivables + inventory - payables, 4), 4), 4))
def cg_f068_cash_conversion_cycle_core110_2nd_v111_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_mean(receivables, 8), 8))
def cg_f068_cash_conversion_cycle_core111_2nd_v112_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_mean(inventory, 8), 8))
def cg_f068_cash_conversion_cycle_core112_2nd_v113_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_mean(payables, 8), 8))
def cg_f068_cash_conversion_cycle_core113_2nd_v114_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_mean(revenue, 8), 8))
def cg_f068_cash_conversion_cycle_core114_2nd_v115_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_mean(cor, 8), 8))
def cg_f068_cash_conversion_cycle_core115_2nd_v116_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_mean(_safe_div(receivables, revenue) * 90.0, 8), 8))
def cg_f068_cash_conversion_cycle_core116_2nd_v117_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_mean(_safe_div(inventory, cor) * 90.0, 8), 8))
def cg_f068_cash_conversion_cycle_core117_2nd_v118_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_mean(_safe_div(payables, cor) * 90.0, 8), 8))
def cg_f068_cash_conversion_cycle_core118_2nd_v119_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_mean((_safe_div(receivables, revenue) + _safe_div(inventory, cor) - _safe_div(payables, cor)) * 90.0, 8), 8))
def cg_f068_cash_conversion_cycle_core119_2nd_v120_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_mean(_diff(receivables + inventory - payables, 4), 8), 8))
def cg_f068_cash_conversion_cycle_core120_2nd_v121_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_mean(receivables, 4), 4))
def cg_f068_cash_conversion_cycle_core121_2nd_v122_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_mean(inventory, 4), 4))
def cg_f068_cash_conversion_cycle_core122_2nd_v123_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_mean(payables, 4), 4))
def cg_f068_cash_conversion_cycle_core123_2nd_v124_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_mean(revenue, 4), 4))
def cg_f068_cash_conversion_cycle_core124_2nd_v125_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_mean(cor, 4), 4))
def cg_f068_cash_conversion_cycle_core125_2nd_v126_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_mean(_safe_div(receivables, revenue) * 90.0, 4), 4))
def cg_f068_cash_conversion_cycle_core126_2nd_v127_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_mean(_safe_div(inventory, cor) * 90.0, 4), 4))
def cg_f068_cash_conversion_cycle_core127_2nd_v128_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_mean(_safe_div(payables, cor) * 90.0, 4), 4))
def cg_f068_cash_conversion_cycle_core128_2nd_v129_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_mean((_safe_div(receivables, revenue) + _safe_div(inventory, cor) - _safe_div(payables, cor)) * 90.0, 4), 4))
def cg_f068_cash_conversion_cycle_core129_2nd_v130_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_mean(_diff(receivables + inventory - payables, 4), 4), 4))
def cg_f068_cash_conversion_cycle_core130_2nd_v131_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_diff(_mean(receivables, 4), 4), 8))
def cg_f068_cash_conversion_cycle_core131_2nd_v132_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_diff(_mean(inventory, 4), 4), 8))
def cg_f068_cash_conversion_cycle_core132_2nd_v133_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_diff(_mean(payables, 4), 4), 8))
def cg_f068_cash_conversion_cycle_core133_2nd_v134_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_diff(_mean(revenue, 4), 4), 8))
def cg_f068_cash_conversion_cycle_core134_2nd_v135_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_diff(_mean(cor, 4), 4), 8))
def cg_f068_cash_conversion_cycle_core135_2nd_v136_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_diff(_mean(_safe_div(receivables, revenue) * 90.0, 4), 4), 8))
def cg_f068_cash_conversion_cycle_core136_2nd_v137_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_diff(_mean(_safe_div(inventory, cor) * 90.0, 4), 4), 8))
def cg_f068_cash_conversion_cycle_core137_2nd_v138_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_diff(_mean(_safe_div(payables, cor) * 90.0, 4), 4), 8))
def cg_f068_cash_conversion_cycle_core138_2nd_v139_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_diff(_mean((_safe_div(receivables, revenue) + _safe_div(inventory, cor) - _safe_div(payables, cor)) * 90.0, 4), 4), 8))
def cg_f068_cash_conversion_cycle_core139_2nd_v140_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_diff(_mean(_diff(receivables + inventory - payables, 4), 4), 4), 8))
def cg_f068_cash_conversion_cycle_core140_2nd_v141_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_slope(_mean(receivables, 4), 4), 12))
def cg_f068_cash_conversion_cycle_core141_2nd_v142_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_slope(_mean(inventory, 4), 4), 12))
def cg_f068_cash_conversion_cycle_core142_2nd_v143_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_slope(_mean(payables, 4), 4), 12))
def cg_f068_cash_conversion_cycle_core143_2nd_v144_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_slope(_mean(revenue, 4), 4), 12))
def cg_f068_cash_conversion_cycle_core144_2nd_v145_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_slope(_mean(cor, 4), 4), 12))
def cg_f068_cash_conversion_cycle_core145_2nd_v146_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_slope(_mean(_safe_div(receivables, revenue) * 90.0, 4), 4), 12))
def cg_f068_cash_conversion_cycle_core146_2nd_v147_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_slope(_mean(_safe_div(inventory, cor) * 90.0, 4), 4), 12))
def cg_f068_cash_conversion_cycle_core147_2nd_v148_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_slope(_mean(_safe_div(payables, cor) * 90.0, 4), 4), 12))
def cg_f068_cash_conversion_cycle_core148_2nd_v149_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_slope(_mean((_safe_div(receivables, revenue) + _safe_div(inventory, cor) - _safe_div(payables, cor)) * 90.0, 4), 4), 12))
def cg_f068_cash_conversion_cycle_core149_2nd_v150_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_slope(_mean(_diff(receivables + inventory - payables, 4), 4), 4), 12))