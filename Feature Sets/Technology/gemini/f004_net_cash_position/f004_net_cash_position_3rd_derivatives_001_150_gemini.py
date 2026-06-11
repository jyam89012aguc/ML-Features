import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f004_net_cash_position_core00_3rd_v001_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(_diff(cashneq, 4), 4))
def cg_f004_net_cash_position_core01_3rd_v002_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(_diff(investments, 4), 4))
def cg_f004_net_cash_position_core02_3rd_v003_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(_diff(debt, 4), 4))
def cg_f004_net_cash_position_core03_3rd_v004_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(_diff(debtc, 4), 4))
def cg_f004_net_cash_position_core04_3rd_v005_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(_diff(debtnc, 4), 4))
def cg_f004_net_cash_position_core05_3rd_v006_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(_diff(cashneq + investments, 4), 4))
def cg_f004_net_cash_position_core06_3rd_v007_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(_diff((cashneq + investments) - debt, 4), 4))
def cg_f004_net_cash_position_core07_3rd_v008_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(_diff(_safe_div(cashneq + investments, debt + 1.0), 4), 4))
def cg_f004_net_cash_position_core08_3rd_v009_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(_diff(_safe_div(debtc, debt + 1.0), 4), 4))
def cg_f004_net_cash_position_core09_3rd_v010_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(_diff(_safe_div(cashneq, debtc + 1.0), 4), 4))

def cg_f004_net_cash_position_core10_3rd_v011_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_diff(cashneq, 4), 8))
def cg_f004_net_cash_position_core11_3rd_v012_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_diff(investments, 4), 8))
def cg_f004_net_cash_position_core12_3rd_v013_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_diff(debt, 4), 8))
def cg_f004_net_cash_position_core13_3rd_v014_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_diff(debtc, 4), 8))
def cg_f004_net_cash_position_core14_3rd_v015_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_diff(debtnc, 4), 8))
def cg_f004_net_cash_position_core15_3rd_v016_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_diff(cashneq + investments, 4), 8))
def cg_f004_net_cash_position_core16_3rd_v017_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_diff((cashneq + investments) - debt, 4), 8))
def cg_f004_net_cash_position_core17_3rd_v018_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_diff(_safe_div(cashneq + investments, debt + 1.0), 4), 8))
def cg_f004_net_cash_position_core18_3rd_v019_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_diff(_safe_div(debtc, debt + 1.0), 4), 8))
def cg_f004_net_cash_position_core19_3rd_v020_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_diff(_safe_div(cashneq, debtc + 1.0), 4), 8))

def cg_f004_net_cash_position_core20_3rd_v021_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(_slope(cashneq, 4), 4))
def cg_f004_net_cash_position_core21_3rd_v022_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(_slope(investments, 4), 4))
def cg_f004_net_cash_position_core22_3rd_v023_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(_slope(debt, 4), 4))
def cg_f004_net_cash_position_core23_3rd_v024_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(_slope(debtc, 4), 4))
def cg_f004_net_cash_position_core24_3rd_v025_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(_slope(debtnc, 4), 4))
def cg_f004_net_cash_position_core25_3rd_v026_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(_slope(cashneq + investments, 4), 4))
def cg_f004_net_cash_position_core26_3rd_v027_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(_slope((cashneq + investments) - debt, 4), 4))
def cg_f004_net_cash_position_core27_3rd_v028_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(_slope(_safe_div(cashneq + investments, debt + 1.0), 4), 4))
def cg_f004_net_cash_position_core28_3rd_v029_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(_slope(_safe_div(debtc, debt + 1.0), 4), 4))
def cg_f004_net_cash_position_core29_3rd_v030_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(_slope(_safe_div(cashneq, debtc + 1.0), 4), 4))

def cg_f004_net_cash_position_core30_3rd_v031_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_diff(_diff(cashneq, 4), 4), 8))
def cg_f004_net_cash_position_core31_3rd_v032_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_diff(_diff(investments, 4), 4), 8))
def cg_f004_net_cash_position_core32_3rd_v033_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_diff(_diff(debt, 4), 4), 8))
def cg_f004_net_cash_position_core33_3rd_v034_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_diff(_diff(debtc, 4), 4), 8))
def cg_f004_net_cash_position_core34_3rd_v035_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_diff(_diff(debtnc, 4), 4), 8))
def cg_f004_net_cash_position_core35_3rd_v036_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_diff(_diff(cashneq + investments, 4), 4), 8))
def cg_f004_net_cash_position_core36_3rd_v037_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_diff(_diff((cashneq + investments) - debt, 4), 4), 8))
def cg_f004_net_cash_position_core37_3rd_v038_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_diff(_diff(_safe_div(cashneq + investments, debt + 1.0), 4), 4), 8))
def cg_f004_net_cash_position_core38_3rd_v039_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_diff(_diff(_safe_div(debtc, debt + 1.0), 4), 4), 8))
def cg_f004_net_cash_position_core39_3rd_v040_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_diff(_diff(_safe_div(cashneq, debtc + 1.0), 4), 4), 8))

def cg_f004_net_cash_position_core40_3rd_v041_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_slope(_diff(cashneq, 4), 8), 12))
def cg_f004_net_cash_position_core41_3rd_v042_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_slope(_diff(investments, 4), 8), 12))
def cg_f004_net_cash_position_core42_3rd_v043_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_slope(_diff(debt, 4), 8), 12))
def cg_f004_net_cash_position_core43_3rd_v044_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_slope(_diff(debtc, 4), 8), 12))
def cg_f004_net_cash_position_core44_3rd_v045_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_slope(_diff(debtnc, 4), 8), 12))
def cg_f004_net_cash_position_core45_3rd_v046_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_slope(_diff(cashneq + investments, 4), 8), 12))
def cg_f004_net_cash_position_core46_3rd_v047_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_slope(_diff((cashneq + investments) - debt, 4), 8), 12))
def cg_f004_net_cash_position_core47_3rd_v048_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_slope(_diff(_safe_div(cashneq + investments, debt + 1.0), 4), 8), 12))
def cg_f004_net_cash_position_core48_3rd_v049_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_slope(_diff(_safe_div(debtc, debt + 1.0), 4), 8), 12))
def cg_f004_net_cash_position_core49_3rd_v050_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_slope(_diff(_safe_div(cashneq, debtc + 1.0), 4), 8), 12))

def cg_f004_net_cash_position_core50_3rd_v051_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_diff(_slope(cashneq, 4), 4), 8))
def cg_f004_net_cash_position_core51_3rd_v052_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_diff(_slope(investments, 4), 4), 8))
def cg_f004_net_cash_position_core52_3rd_v053_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_diff(_slope(debt, 4), 4), 8))
def cg_f004_net_cash_position_core53_3rd_v054_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_diff(_slope(debtc, 4), 4), 8))
def cg_f004_net_cash_position_core54_3rd_v055_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_diff(_slope(debtnc, 4), 4), 8))
def cg_f004_net_cash_position_core55_3rd_v056_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_diff(_slope(cashneq + investments, 4), 4), 8))
def cg_f004_net_cash_position_core56_3rd_v057_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_diff(_slope((cashneq + investments) - debt, 4), 4), 8))
def cg_f004_net_cash_position_core57_3rd_v058_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_diff(_slope(_safe_div(cashneq + investments, debt + 1.0), 4), 4), 8))
def cg_f004_net_cash_position_core58_3rd_v059_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_diff(_slope(_safe_div(debtc, debt + 1.0), 4), 4), 8))
def cg_f004_net_cash_position_core59_3rd_v060_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_diff(_slope(_safe_div(cashneq, debtc + 1.0), 4), 4), 8))

def cg_f004_net_cash_position_core60_3rd_v061_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_diff(_diff(cashneq, 4), 4), 12))
def cg_f004_net_cash_position_core61_3rd_v062_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_diff(_diff(investments, 4), 4), 12))
def cg_f004_net_cash_position_core62_3rd_v063_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_diff(_diff(debt, 4), 4), 12))
def cg_f004_net_cash_position_core63_3rd_v064_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_diff(_diff(debtc, 4), 4), 12))
def cg_f004_net_cash_position_core64_3rd_v065_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_diff(_diff(debtnc, 4), 4), 12))
def cg_f004_net_cash_position_core65_3rd_v066_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_diff(_diff(cashneq + investments, 4), 4), 12))
def cg_f004_net_cash_position_core66_3rd_v067_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_diff(_diff((cashneq + investments) - debt, 4), 4), 12))
def cg_f004_net_cash_position_core67_3rd_v068_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_diff(_diff(_safe_div(cashneq + investments, debt + 1.0), 4), 4), 12))
def cg_f004_net_cash_position_core68_3rd_v069_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_diff(_diff(_safe_div(debtc, debt + 1.0), 4), 4), 12))
def cg_f004_net_cash_position_core69_3rd_v070_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_diff(_diff(_safe_div(cashneq, debtc + 1.0), 4), 4), 12))

def cg_f004_net_cash_position_core70_3rd_v071_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_slope(_diff(cashneq, 4), 8), 12))
def cg_f004_net_cash_position_core71_3rd_v072_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_slope(_diff(investments, 4), 8), 12))
def cg_f004_net_cash_position_core72_3rd_v073_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_slope(_diff(debt, 4), 8), 12))
def cg_f004_net_cash_position_core73_3rd_v074_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_slope(_diff(debtc, 4), 8), 12))
def cg_f004_net_cash_position_core74_3rd_v075_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_slope(_diff(debtnc, 4), 8), 12))
def cg_f004_net_cash_position_core75_3rd_v076_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_slope(_diff(cashneq + investments, 4), 8), 12))
def cg_f004_net_cash_position_core76_3rd_v077_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_slope(_diff((cashneq + investments) - debt, 4), 8), 12))
def cg_f004_net_cash_position_core77_3rd_v078_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_slope(_diff(_safe_div(cashneq + investments, debt + 1.0), 4), 8), 12))
def cg_f004_net_cash_position_core78_3rd_v079_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_slope(_diff(_safe_div(debtc, debt + 1.0), 4), 8), 12))
def cg_f004_net_cash_position_core79_3rd_v080_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_slope(_diff(_safe_div(cashneq, debtc + 1.0), 4), 8), 12))

def cg_f004_net_cash_position_core80_3rd_v081_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_diff(_slope(cashneq, 4), 4), 12))
def cg_f004_net_cash_position_core81_3rd_v082_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_diff(_slope(investments, 4), 4), 12))
def cg_f004_net_cash_position_core82_3rd_v083_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_diff(_slope(debt, 4), 4), 12))
def cg_f004_net_cash_position_core83_3rd_v084_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_diff(_slope(debtc, 4), 4), 12))
def cg_f004_net_cash_position_core84_3rd_v085_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_diff(_slope(debtnc, 4), 4), 12))
def cg_f004_net_cash_position_core85_3rd_v086_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_diff(_slope(cashneq + investments, 4), 4), 12))
def cg_f004_net_cash_position_core86_3rd_v087_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_diff(_slope((cashneq + investments) - debt, 4), 4), 12))
def cg_f004_net_cash_position_core87_3rd_v088_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_diff(_slope(_safe_div(cashneq + investments, debt + 1.0), 4), 4), 12))
def cg_f004_net_cash_position_core88_3rd_v089_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_diff(_slope(_safe_div(debtc, debt + 1.0), 4), 4), 12))
def cg_f004_net_cash_position_core89_3rd_v090_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_diff(_slope(_safe_div(cashneq, debtc + 1.0), 4), 4), 12))

def cg_f004_net_cash_position_core90_3rd_v091_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_diff(_diff(cashneq, 4), 4), 4))
def cg_f004_net_cash_position_core91_3rd_v092_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_diff(_diff(investments, 4), 4), 4))
def cg_f004_net_cash_position_core92_3rd_v093_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_diff(_diff(debt, 4), 4), 4))
def cg_f004_net_cash_position_core93_3rd_v094_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_diff(_diff(debtc, 4), 4), 4))
def cg_f004_net_cash_position_core94_3rd_v095_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_diff(_diff(debtnc, 4), 4), 4))
def cg_f004_net_cash_position_core95_3rd_v096_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_diff(_diff(cashneq + investments, 4), 4), 4))
def cg_f004_net_cash_position_core96_3rd_v097_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_diff(_diff((cashneq + investments) - debt, 4), 4), 4))
def cg_f004_net_cash_position_core97_3rd_v098_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_diff(_diff(_safe_div(cashneq + investments, debt + 1.0), 4), 4), 4))
def cg_f004_net_cash_position_core98_3rd_v099_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_diff(_diff(_safe_div(debtc, debt + 1.0), 4), 4), 4))
def cg_f004_net_cash_position_core99_3rd_v100_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_diff(_diff(_safe_div(cashneq, debtc + 1.0), 4), 4), 4))

def cg_f004_net_cash_position_core100_3rd_v101_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_slope(_diff(cashneq, 4), 8), 4))
def cg_f004_net_cash_position_core101_3rd_v102_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_slope(_diff(investments, 4), 8), 4))
def cg_f004_net_cash_position_core102_3rd_v103_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_slope(_diff(debt, 4), 8), 4))
def cg_f004_net_cash_position_core103_3rd_v104_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_slope(_diff(debtc, 4), 8), 4))
def cg_f004_net_cash_position_core104_3rd_v105_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_slope(_diff(debtnc, 4), 8), 4))
def cg_f004_net_cash_position_core105_3rd_v106_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_slope(_diff(cashneq + investments, 4), 8), 4))
def cg_f004_net_cash_position_core106_3rd_v107_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_slope(_diff((cashneq + investments) - debt, 4), 8), 4))
def cg_f004_net_cash_position_core107_3rd_v108_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_slope(_diff(_safe_div(cashneq + investments, debt + 1.0), 4), 8), 4))
def cg_f004_net_cash_position_core108_3rd_v109_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_slope(_diff(_safe_div(debtc, debt + 1.0), 4), 8), 4))
def cg_f004_net_cash_position_core109_3rd_v110_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_slope(_diff(_safe_div(cashneq, debtc + 1.0), 4), 8), 4))

def cg_f004_net_cash_position_core110_3rd_v111_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_diff(_slope(cashneq, 4), 4), 4))
def cg_f004_net_cash_position_core111_3rd_v112_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_diff(_slope(investments, 4), 4), 4))
def cg_f004_net_cash_position_core112_3rd_v113_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_diff(_slope(debt, 4), 4), 4))
def cg_f004_net_cash_position_core113_3rd_v114_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_diff(_slope(debtc, 4), 4), 4))
def cg_f004_net_cash_position_core114_3rd_v115_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_diff(_slope(debtnc, 4), 4), 4))
def cg_f004_net_cash_position_core115_3rd_v116_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_diff(_slope(cashneq + investments, 4), 4), 4))
def cg_f004_net_cash_position_core116_3rd_v117_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_diff(_slope((cashneq + investments) - debt, 4), 4), 4))
def cg_f004_net_cash_position_core117_3rd_v118_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_diff(_slope(_safe_div(cashneq + investments, debt + 1.0), 4), 4), 4))
def cg_f004_net_cash_position_core118_3rd_v119_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_diff(_slope(_safe_div(debtc, debt + 1.0), 4), 4), 4))
def cg_f004_net_cash_position_core119_3rd_v120_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_diff(_slope(_safe_div(cashneq, debtc + 1.0), 4), 4), 4))

def cg_f004_net_cash_position_core120_3rd_v121_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_diff(_diff(cashneq, 4), 4), 4))
def cg_f004_net_cash_position_core121_3rd_v122_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_diff(_diff(investments, 4), 4), 4))
def cg_f004_net_cash_position_core122_3rd_v123_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_diff(_diff(debt, 4), 4), 4))
def cg_f004_net_cash_position_core123_3rd_v124_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_diff(_diff(debtc, 4), 4), 4))
def cg_f004_net_cash_position_core124_3rd_v125_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_diff(_diff(debtnc, 4), 4), 4))
def cg_f004_net_cash_position_core125_3rd_v126_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_diff(_diff(cashneq + investments, 4), 4), 4))
def cg_f004_net_cash_position_core126_3rd_v127_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_diff(_diff((cashneq + investments) - debt, 4), 4), 4))
def cg_f004_net_cash_position_core127_3rd_v128_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_diff(_diff(_safe_div(cashneq + investments, debt + 1.0), 4), 4), 4))
def cg_f004_net_cash_position_core128_3rd_v129_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_diff(_diff(_safe_div(debtc, debt + 1.0), 4), 4), 4))
def cg_f004_net_cash_position_core129_3rd_v130_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_diff(_diff(_safe_div(cashneq, debtc + 1.0), 4), 4), 4))

def cg_f004_net_cash_position_core130_3rd_v131_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(_diff(_diff(cashneq, 4), 4), 4))
def cg_f004_net_cash_position_core131_3rd_v132_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(_diff(_diff(investments, 4), 4), 4))
def cg_f004_net_cash_position_core132_3rd_v133_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(_diff(_diff(debt, 4), 4), 4))
def cg_f004_net_cash_position_core133_3rd_v134_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(_diff(_diff(debtc, 4), 4), 4))
def cg_f004_net_cash_position_core134_3rd_v135_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(_diff(_diff(debtnc, 4), 4), 4))
def cg_f004_net_cash_position_core135_3rd_v136_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(_diff(_diff(cashneq + investments, 4), 4), 4))
def cg_f004_net_cash_position_core136_3rd_v137_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(_diff(_diff((cashneq + investments) - debt, 4), 4), 4))
def cg_f004_net_cash_position_core137_3rd_v138_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(_diff(_diff(_safe_div(cashneq + investments, debt + 1.0), 4), 4), 4))
def cg_f004_net_cash_position_core138_3rd_v139_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(_diff(_diff(_safe_div(debtc, debt + 1.0), 4), 4), 4))
def cg_f004_net_cash_position_core139_3rd_v140_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(_diff(_diff(_safe_div(cashneq, debtc + 1.0), 4), 4), 4))

def cg_f004_net_cash_position_core140_3rd_v141_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_slope(_diff(_diff(cashneq, 4), 4), 4), 8))
def cg_f004_net_cash_position_core141_3rd_v142_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_slope(_diff(_diff(investments, 4), 4), 4), 8))
def cg_f004_net_cash_position_core142_3rd_v143_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_slope(_diff(_diff(debt, 4), 4), 4), 8))
def cg_f004_net_cash_position_core143_3rd_v144_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_slope(_diff(_diff(debtc, 4), 4), 4), 8))
def cg_f004_net_cash_position_core144_3rd_v145_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_slope(_diff(_diff(debtnc, 4), 4), 4), 8))
def cg_f004_net_cash_position_core145_3rd_v146_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_slope(_diff(_diff(cashneq + investments, 4), 4), 4), 8))
def cg_f004_net_cash_position_core146_3rd_v147_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_slope(_diff(_diff((cashneq + investments) - debt, 4), 4), 4), 8))
def cg_f004_net_cash_position_core147_3rd_v148_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_slope(_diff(_diff(_safe_div(cashneq + investments, debt + 1.0), 4), 4), 4), 8))
def cg_f004_net_cash_position_core148_3rd_v149_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_slope(_diff(_diff(_safe_div(debtc, debt + 1.0), 4), 4), 4), 8))
def cg_f004_net_cash_position_core149_3rd_v150_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_slope(_diff(_diff(_safe_div(cashneq, debtc + 1.0), 4), 4), 4), 8))
