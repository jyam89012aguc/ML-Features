import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f068_cash_conversion_cycle_core00_3rd_v001_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_diff(receivables, 4), 4))
def cg_f068_cash_conversion_cycle_core01_3rd_v002_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_diff(inventory, 4), 4))
def cg_f068_cash_conversion_cycle_core02_3rd_v003_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_diff(payables, 4), 4))
def cg_f068_cash_conversion_cycle_core03_3rd_v004_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_diff(revenue, 4), 4))
def cg_f068_cash_conversion_cycle_core04_3rd_v005_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_diff(cor, 4), 4))
def cg_f068_cash_conversion_cycle_core05_3rd_v006_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_diff(_safe_div(receivables, revenue) * 90.0, 4), 4))
def cg_f068_cash_conversion_cycle_core06_3rd_v007_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_diff(_safe_div(inventory, cor) * 90.0, 4), 4))
def cg_f068_cash_conversion_cycle_core07_3rd_v008_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_diff(_safe_div(payables, cor) * 90.0, 4), 4))
def cg_f068_cash_conversion_cycle_core08_3rd_v009_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_diff((_safe_div(receivables, revenue) + _safe_div(inventory, cor) - _safe_div(payables, cor)) * 90.0, 4), 4))
def cg_f068_cash_conversion_cycle_core09_3rd_v010_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_diff(_diff(receivables + inventory - payables, 4), 4), 4))
def cg_f068_cash_conversion_cycle_core10_3rd_v011_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_diff(receivables, 4), 8))
def cg_f068_cash_conversion_cycle_core11_3rd_v012_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_diff(inventory, 4), 8))
def cg_f068_cash_conversion_cycle_core12_3rd_v013_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_diff(payables, 4), 8))
def cg_f068_cash_conversion_cycle_core13_3rd_v014_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_diff(revenue, 4), 8))
def cg_f068_cash_conversion_cycle_core14_3rd_v015_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_diff(cor, 4), 8))
def cg_f068_cash_conversion_cycle_core15_3rd_v016_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_diff(_safe_div(receivables, revenue) * 90.0, 4), 8))
def cg_f068_cash_conversion_cycle_core16_3rd_v017_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_diff(_safe_div(inventory, cor) * 90.0, 4), 8))
def cg_f068_cash_conversion_cycle_core17_3rd_v018_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_diff(_safe_div(payables, cor) * 90.0, 4), 8))
def cg_f068_cash_conversion_cycle_core18_3rd_v019_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_diff((_safe_div(receivables, revenue) + _safe_div(inventory, cor) - _safe_div(payables, cor)) * 90.0, 4), 8))
def cg_f068_cash_conversion_cycle_core19_3rd_v020_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_diff(_diff(receivables + inventory - payables, 4), 4), 8))
def cg_f068_cash_conversion_cycle_core20_3rd_v021_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_slope(receivables, 4), 4))
def cg_f068_cash_conversion_cycle_core21_3rd_v022_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_slope(inventory, 4), 4))
def cg_f068_cash_conversion_cycle_core22_3rd_v023_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_slope(payables, 4), 4))
def cg_f068_cash_conversion_cycle_core23_3rd_v024_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_slope(revenue, 4), 4))
def cg_f068_cash_conversion_cycle_core24_3rd_v025_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_slope(cor, 4), 4))
def cg_f068_cash_conversion_cycle_core25_3rd_v026_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_slope(_safe_div(receivables, revenue) * 90.0, 4), 4))
def cg_f068_cash_conversion_cycle_core26_3rd_v027_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_slope(_safe_div(inventory, cor) * 90.0, 4), 4))
def cg_f068_cash_conversion_cycle_core27_3rd_v028_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_slope(_safe_div(payables, cor) * 90.0, 4), 4))
def cg_f068_cash_conversion_cycle_core28_3rd_v029_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_slope((_safe_div(receivables, revenue) + _safe_div(inventory, cor) - _safe_div(payables, cor)) * 90.0, 4), 4))
def cg_f068_cash_conversion_cycle_core29_3rd_v030_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_slope(_diff(receivables + inventory - payables, 4), 4), 4))
def cg_f068_cash_conversion_cycle_core30_3rd_v031_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_diff(_diff(receivables, 4), 4), 8))
def cg_f068_cash_conversion_cycle_core31_3rd_v032_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_diff(_diff(inventory, 4), 4), 8))
def cg_f068_cash_conversion_cycle_core32_3rd_v033_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_diff(_diff(payables, 4), 4), 8))
def cg_f068_cash_conversion_cycle_core33_3rd_v034_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_diff(_diff(revenue, 4), 4), 8))
def cg_f068_cash_conversion_cycle_core34_3rd_v035_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_diff(_diff(cor, 4), 4), 8))
def cg_f068_cash_conversion_cycle_core35_3rd_v036_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_diff(_diff(_safe_div(receivables, revenue) * 90.0, 4), 4), 8))
def cg_f068_cash_conversion_cycle_core36_3rd_v037_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_diff(_diff(_safe_div(inventory, cor) * 90.0, 4), 4), 8))
def cg_f068_cash_conversion_cycle_core37_3rd_v038_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_diff(_diff(_safe_div(payables, cor) * 90.0, 4), 4), 8))
def cg_f068_cash_conversion_cycle_core38_3rd_v039_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_diff(_diff((_safe_div(receivables, revenue) + _safe_div(inventory, cor) - _safe_div(payables, cor)) * 90.0, 4), 4), 8))
def cg_f068_cash_conversion_cycle_core39_3rd_v040_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_diff(_diff(_diff(receivables + inventory - payables, 4), 4), 4), 8))
def cg_f068_cash_conversion_cycle_core40_3rd_v041_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_slope(_diff(receivables, 4), 8), 12))
def cg_f068_cash_conversion_cycle_core41_3rd_v042_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_slope(_diff(inventory, 4), 8), 12))
def cg_f068_cash_conversion_cycle_core42_3rd_v043_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_slope(_diff(payables, 4), 8), 12))
def cg_f068_cash_conversion_cycle_core43_3rd_v044_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_slope(_diff(revenue, 4), 8), 12))
def cg_f068_cash_conversion_cycle_core44_3rd_v045_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_slope(_diff(cor, 4), 8), 12))
def cg_f068_cash_conversion_cycle_core45_3rd_v046_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_slope(_diff(_safe_div(receivables, revenue) * 90.0, 4), 8), 12))
def cg_f068_cash_conversion_cycle_core46_3rd_v047_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_slope(_diff(_safe_div(inventory, cor) * 90.0, 4), 8), 12))
def cg_f068_cash_conversion_cycle_core47_3rd_v048_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_slope(_diff(_safe_div(payables, cor) * 90.0, 4), 8), 12))
def cg_f068_cash_conversion_cycle_core48_3rd_v049_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_slope(_diff((_safe_div(receivables, revenue) + _safe_div(inventory, cor) - _safe_div(payables, cor)) * 90.0, 4), 8), 12))
def cg_f068_cash_conversion_cycle_core49_3rd_v050_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_slope(_diff(_diff(receivables + inventory - payables, 4), 4), 8), 12))
def cg_f068_cash_conversion_cycle_core50_3rd_v051_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_diff(_slope(receivables, 4), 4), 8))
def cg_f068_cash_conversion_cycle_core51_3rd_v052_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_diff(_slope(inventory, 4), 4), 8))
def cg_f068_cash_conversion_cycle_core52_3rd_v053_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_diff(_slope(payables, 4), 4), 8))
def cg_f068_cash_conversion_cycle_core53_3rd_v054_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_diff(_slope(revenue, 4), 4), 8))
def cg_f068_cash_conversion_cycle_core54_3rd_v055_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_diff(_slope(cor, 4), 4), 8))
def cg_f068_cash_conversion_cycle_core55_3rd_v056_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_diff(_slope(_safe_div(receivables, revenue) * 90.0, 4), 4), 8))
def cg_f068_cash_conversion_cycle_core56_3rd_v057_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_diff(_slope(_safe_div(inventory, cor) * 90.0, 4), 4), 8))
def cg_f068_cash_conversion_cycle_core57_3rd_v058_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_diff(_slope(_safe_div(payables, cor) * 90.0, 4), 4), 8))
def cg_f068_cash_conversion_cycle_core58_3rd_v059_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_diff(_slope((_safe_div(receivables, revenue) + _safe_div(inventory, cor) - _safe_div(payables, cor)) * 90.0, 4), 4), 8))
def cg_f068_cash_conversion_cycle_core59_3rd_v060_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_diff(_slope(_diff(receivables + inventory - payables, 4), 4), 4), 8))
def cg_f068_cash_conversion_cycle_core60_3rd_v061_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_diff(_diff(receivables, 4), 4), 12))
def cg_f068_cash_conversion_cycle_core61_3rd_v062_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_diff(_diff(inventory, 4), 4), 12))
def cg_f068_cash_conversion_cycle_core62_3rd_v063_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_diff(_diff(payables, 4), 4), 12))
def cg_f068_cash_conversion_cycle_core63_3rd_v064_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_diff(_diff(revenue, 4), 4), 12))
def cg_f068_cash_conversion_cycle_core64_3rd_v065_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_diff(_diff(cor, 4), 4), 12))
def cg_f068_cash_conversion_cycle_core65_3rd_v066_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_diff(_diff(_safe_div(receivables, revenue) * 90.0, 4), 4), 12))
def cg_f068_cash_conversion_cycle_core66_3rd_v067_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_diff(_diff(_safe_div(inventory, cor) * 90.0, 4), 4), 12))
def cg_f068_cash_conversion_cycle_core67_3rd_v068_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_diff(_diff(_safe_div(payables, cor) * 90.0, 4), 4), 12))
def cg_f068_cash_conversion_cycle_core68_3rd_v069_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_diff(_diff((_safe_div(receivables, revenue) + _safe_div(inventory, cor) - _safe_div(payables, cor)) * 90.0, 4), 4), 12))
def cg_f068_cash_conversion_cycle_core69_3rd_v070_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_diff(_diff(_diff(receivables + inventory - payables, 4), 4), 4), 12))
def cg_f068_cash_conversion_cycle_core70_3rd_v071_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_slope(_diff(receivables, 4), 8), 12))
def cg_f068_cash_conversion_cycle_core71_3rd_v072_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_slope(_diff(inventory, 4), 8), 12))
def cg_f068_cash_conversion_cycle_core72_3rd_v073_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_slope(_diff(payables, 4), 8), 12))
def cg_f068_cash_conversion_cycle_core73_3rd_v074_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_slope(_diff(revenue, 4), 8), 12))
def cg_f068_cash_conversion_cycle_core74_3rd_v075_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_slope(_diff(cor, 4), 8), 12))
def cg_f068_cash_conversion_cycle_core75_3rd_v076_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_slope(_diff(_safe_div(receivables, revenue) * 90.0, 4), 8), 12))
def cg_f068_cash_conversion_cycle_core76_3rd_v077_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_slope(_diff(_safe_div(inventory, cor) * 90.0, 4), 8), 12))
def cg_f068_cash_conversion_cycle_core77_3rd_v078_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_slope(_diff(_safe_div(payables, cor) * 90.0, 4), 8), 12))
def cg_f068_cash_conversion_cycle_core78_3rd_v079_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_slope(_diff((_safe_div(receivables, revenue) + _safe_div(inventory, cor) - _safe_div(payables, cor)) * 90.0, 4), 8), 12))
def cg_f068_cash_conversion_cycle_core79_3rd_v080_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_slope(_diff(_diff(receivables + inventory - payables, 4), 4), 8), 12))
def cg_f068_cash_conversion_cycle_core80_3rd_v081_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_diff(_slope(receivables, 4), 4), 12))
def cg_f068_cash_conversion_cycle_core81_3rd_v082_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_diff(_slope(inventory, 4), 4), 12))
def cg_f068_cash_conversion_cycle_core82_3rd_v083_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_diff(_slope(payables, 4), 4), 12))
def cg_f068_cash_conversion_cycle_core83_3rd_v084_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_diff(_slope(revenue, 4), 4), 12))
def cg_f068_cash_conversion_cycle_core84_3rd_v085_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_diff(_slope(cor, 4), 4), 12))
def cg_f068_cash_conversion_cycle_core85_3rd_v086_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_diff(_slope(_safe_div(receivables, revenue) * 90.0, 4), 4), 12))
def cg_f068_cash_conversion_cycle_core86_3rd_v087_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_diff(_slope(_safe_div(inventory, cor) * 90.0, 4), 4), 12))
def cg_f068_cash_conversion_cycle_core87_3rd_v088_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_diff(_slope(_safe_div(payables, cor) * 90.0, 4), 4), 12))
def cg_f068_cash_conversion_cycle_core88_3rd_v089_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_diff(_slope((_safe_div(receivables, revenue) + _safe_div(inventory, cor) - _safe_div(payables, cor)) * 90.0, 4), 4), 12))
def cg_f068_cash_conversion_cycle_core89_3rd_v090_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_rank(_diff(_slope(_diff(receivables + inventory - payables, 4), 4), 4), 12))
def cg_f068_cash_conversion_cycle_core90_3rd_v091_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_diff(_diff(receivables, 4), 4), 4))
def cg_f068_cash_conversion_cycle_core91_3rd_v092_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_diff(_diff(inventory, 4), 4), 4))
def cg_f068_cash_conversion_cycle_core92_3rd_v093_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_diff(_diff(payables, 4), 4), 4))
def cg_f068_cash_conversion_cycle_core93_3rd_v094_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_diff(_diff(revenue, 4), 4), 4))
def cg_f068_cash_conversion_cycle_core94_3rd_v095_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_diff(_diff(cor, 4), 4), 4))
def cg_f068_cash_conversion_cycle_core95_3rd_v096_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_diff(_diff(_safe_div(receivables, revenue) * 90.0, 4), 4), 4))
def cg_f068_cash_conversion_cycle_core96_3rd_v097_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_diff(_diff(_safe_div(inventory, cor) * 90.0, 4), 4), 4))
def cg_f068_cash_conversion_cycle_core97_3rd_v098_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_diff(_diff(_safe_div(payables, cor) * 90.0, 4), 4), 4))
def cg_f068_cash_conversion_cycle_core98_3rd_v099_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_diff(_diff((_safe_div(receivables, revenue) + _safe_div(inventory, cor) - _safe_div(payables, cor)) * 90.0, 4), 4), 4))
def cg_f068_cash_conversion_cycle_core99_3rd_v100_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_diff(_diff(_diff(receivables + inventory - payables, 4), 4), 4), 4))
def cg_f068_cash_conversion_cycle_core100_3rd_v101_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_slope(_diff(receivables, 4), 8), 4))
def cg_f068_cash_conversion_cycle_core101_3rd_v102_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_slope(_diff(inventory, 4), 8), 4))
def cg_f068_cash_conversion_cycle_core102_3rd_v103_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_slope(_diff(payables, 4), 8), 4))
def cg_f068_cash_conversion_cycle_core103_3rd_v104_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_slope(_diff(revenue, 4), 8), 4))
def cg_f068_cash_conversion_cycle_core104_3rd_v105_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_slope(_diff(cor, 4), 8), 4))
def cg_f068_cash_conversion_cycle_core105_3rd_v106_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_slope(_diff(_safe_div(receivables, revenue) * 90.0, 4), 8), 4))
def cg_f068_cash_conversion_cycle_core106_3rd_v107_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_slope(_diff(_safe_div(inventory, cor) * 90.0, 4), 8), 4))
def cg_f068_cash_conversion_cycle_core107_3rd_v108_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_slope(_diff(_safe_div(payables, cor) * 90.0, 4), 8), 4))
def cg_f068_cash_conversion_cycle_core108_3rd_v109_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_slope(_diff((_safe_div(receivables, revenue) + _safe_div(inventory, cor) - _safe_div(payables, cor)) * 90.0, 4), 8), 4))
def cg_f068_cash_conversion_cycle_core109_3rd_v110_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_slope(_diff(_diff(receivables + inventory - payables, 4), 4), 8), 4))
def cg_f068_cash_conversion_cycle_core110_3rd_v111_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_diff(_slope(receivables, 4), 4), 4))
def cg_f068_cash_conversion_cycle_core111_3rd_v112_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_diff(_slope(inventory, 4), 4), 4))
def cg_f068_cash_conversion_cycle_core112_3rd_v113_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_diff(_slope(payables, 4), 4), 4))
def cg_f068_cash_conversion_cycle_core113_3rd_v114_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_diff(_slope(revenue, 4), 4), 4))
def cg_f068_cash_conversion_cycle_core114_3rd_v115_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_diff(_slope(cor, 4), 4), 4))
def cg_f068_cash_conversion_cycle_core115_3rd_v116_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_diff(_slope(_safe_div(receivables, revenue) * 90.0, 4), 4), 4))
def cg_f068_cash_conversion_cycle_core116_3rd_v117_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_diff(_slope(_safe_div(inventory, cor) * 90.0, 4), 4), 4))
def cg_f068_cash_conversion_cycle_core117_3rd_v118_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_diff(_slope(_safe_div(payables, cor) * 90.0, 4), 4), 4))
def cg_f068_cash_conversion_cycle_core118_3rd_v119_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_diff(_slope((_safe_div(receivables, revenue) + _safe_div(inventory, cor) - _safe_div(payables, cor)) * 90.0, 4), 4), 4))
def cg_f068_cash_conversion_cycle_core119_3rd_v120_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_mean(_diff(_slope(_diff(receivables + inventory - payables, 4), 4), 4), 4))
def cg_f068_cash_conversion_cycle_core120_3rd_v121_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_diff(_diff(receivables, 4), 4), 4))
def cg_f068_cash_conversion_cycle_core121_3rd_v122_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_diff(_diff(inventory, 4), 4), 4))
def cg_f068_cash_conversion_cycle_core122_3rd_v123_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_diff(_diff(payables, 4), 4), 4))
def cg_f068_cash_conversion_cycle_core123_3rd_v124_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_diff(_diff(revenue, 4), 4), 4))
def cg_f068_cash_conversion_cycle_core124_3rd_v125_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_diff(_diff(cor, 4), 4), 4))
def cg_f068_cash_conversion_cycle_core125_3rd_v126_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_diff(_diff(_safe_div(receivables, revenue) * 90.0, 4), 4), 4))
def cg_f068_cash_conversion_cycle_core126_3rd_v127_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_diff(_diff(_safe_div(inventory, cor) * 90.0, 4), 4), 4))
def cg_f068_cash_conversion_cycle_core127_3rd_v128_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_diff(_diff(_safe_div(payables, cor) * 90.0, 4), 4), 4))
def cg_f068_cash_conversion_cycle_core128_3rd_v129_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_diff(_diff((_safe_div(receivables, revenue) + _safe_div(inventory, cor) - _safe_div(payables, cor)) * 90.0, 4), 4), 4))
def cg_f068_cash_conversion_cycle_core129_3rd_v130_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_diff(_diff(_diff(receivables + inventory - payables, 4), 4), 4), 4))
def cg_f068_cash_conversion_cycle_core130_3rd_v131_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_diff(_diff(receivables, 4), 4), 4))
def cg_f068_cash_conversion_cycle_core131_3rd_v132_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_diff(_diff(inventory, 4), 4), 4))
def cg_f068_cash_conversion_cycle_core132_3rd_v133_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_diff(_diff(payables, 4), 4), 4))
def cg_f068_cash_conversion_cycle_core133_3rd_v134_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_diff(_diff(revenue, 4), 4), 4))
def cg_f068_cash_conversion_cycle_core134_3rd_v135_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_diff(_diff(cor, 4), 4), 4))
def cg_f068_cash_conversion_cycle_core135_3rd_v136_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_diff(_diff(_safe_div(receivables, revenue) * 90.0, 4), 4), 4))
def cg_f068_cash_conversion_cycle_core136_3rd_v137_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_diff(_diff(_safe_div(inventory, cor) * 90.0, 4), 4), 4))
def cg_f068_cash_conversion_cycle_core137_3rd_v138_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_diff(_diff(_safe_div(payables, cor) * 90.0, 4), 4), 4))
def cg_f068_cash_conversion_cycle_core138_3rd_v139_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_diff(_diff((_safe_div(receivables, revenue) + _safe_div(inventory, cor) - _safe_div(payables, cor)) * 90.0, 4), 4), 4))
def cg_f068_cash_conversion_cycle_core139_3rd_v140_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_diff(_diff(_diff(receivables + inventory - payables, 4), 4), 4), 4))
def cg_f068_cash_conversion_cycle_core140_3rd_v141_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_slope(_diff(_diff(receivables, 4), 4), 4), 8))
def cg_f068_cash_conversion_cycle_core141_3rd_v142_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_slope(_diff(_diff(inventory, 4), 4), 4), 8))
def cg_f068_cash_conversion_cycle_core142_3rd_v143_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_slope(_diff(_diff(payables, 4), 4), 4), 8))
def cg_f068_cash_conversion_cycle_core143_3rd_v144_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_slope(_diff(_diff(revenue, 4), 4), 4), 8))
def cg_f068_cash_conversion_cycle_core144_3rd_v145_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_slope(_diff(_diff(cor, 4), 4), 4), 8))
def cg_f068_cash_conversion_cycle_core145_3rd_v146_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_slope(_diff(_diff(_safe_div(receivables, revenue) * 90.0, 4), 4), 4), 8))
def cg_f068_cash_conversion_cycle_core146_3rd_v147_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_slope(_diff(_diff(_safe_div(inventory, cor) * 90.0, 4), 4), 4), 8))
def cg_f068_cash_conversion_cycle_core147_3rd_v148_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_slope(_diff(_diff(_safe_div(payables, cor) * 90.0, 4), 4), 4), 8))
def cg_f068_cash_conversion_cycle_core148_3rd_v149_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_slope(_diff(_diff((_safe_div(receivables, revenue) + _safe_div(inventory, cor) - _safe_div(payables, cor)) * 90.0, 4), 4), 4), 8))
def cg_f068_cash_conversion_cycle_core149_3rd_v150_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_z(_slope(_diff(_diff(_diff(receivables + inventory - payables, 4), 4), 4), 4), 8))