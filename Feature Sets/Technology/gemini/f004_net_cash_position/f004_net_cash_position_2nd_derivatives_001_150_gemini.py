import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f004_net_cash_position_core00_2nd_v001_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(cashneq, 4))
def cg_f004_net_cash_position_core01_2nd_v002_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(investments, 4))
def cg_f004_net_cash_position_core02_2nd_v003_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(debt, 4))
def cg_f004_net_cash_position_core03_2nd_v004_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(debtc, 4))
def cg_f004_net_cash_position_core04_2nd_v005_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(debtnc, 4))
def cg_f004_net_cash_position_core05_2nd_v006_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(cashneq + investments, 4))
def cg_f004_net_cash_position_core06_2nd_v007_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope((cashneq + investments) - debt, 4))
def cg_f004_net_cash_position_core07_2nd_v008_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_safe_div(cashneq + investments, debt + 1.0), 4))
def cg_f004_net_cash_position_core08_2nd_v009_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_safe_div(debtc, debt + 1.0), 4))
def cg_f004_net_cash_position_core09_2nd_v010_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_safe_div(cashneq, debtc + 1.0), 4))

def cg_f004_net_cash_position_core10_2nd_v011_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(cashneq, 8))
def cg_f004_net_cash_position_core11_2nd_v012_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(investments, 8))
def cg_f004_net_cash_position_core12_2nd_v013_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(debt, 8))
def cg_f004_net_cash_position_core13_2nd_v014_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(debtc, 8))
def cg_f004_net_cash_position_core14_2nd_v015_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(debtnc, 8))
def cg_f004_net_cash_position_core15_2nd_v016_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(cashneq + investments, 8))
def cg_f004_net_cash_position_core16_2nd_v017_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope((cashneq + investments) - debt, 8))
def cg_f004_net_cash_position_core17_2nd_v018_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_safe_div(cashneq + investments, debt + 1.0), 8))
def cg_f004_net_cash_position_core18_2nd_v019_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_safe_div(debtc, debt + 1.0), 8))
def cg_f004_net_cash_position_core19_2nd_v020_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_safe_div(cashneq, debtc + 1.0), 8))

def cg_f004_net_cash_position_core20_2nd_v021_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(cashneq, 4))
def cg_f004_net_cash_position_core21_2nd_v022_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(investments, 4))
def cg_f004_net_cash_position_core22_2nd_v023_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(debt, 4))
def cg_f004_net_cash_position_core23_2nd_v024_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(debtc, 4))
def cg_f004_net_cash_position_core24_2nd_v025_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(debtnc, 4))
def cg_f004_net_cash_position_core25_2nd_v026_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(cashneq + investments, 4))
def cg_f004_net_cash_position_core26_2nd_v027_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff((cashneq + investments) - debt, 4))
def cg_f004_net_cash_position_core27_2nd_v028_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(_safe_div(cashneq + investments, debt + 1.0), 4))
def cg_f004_net_cash_position_core28_2nd_v029_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(_safe_div(debtc, debt + 1.0), 4))
def cg_f004_net_cash_position_core29_2nd_v030_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(_safe_div(cashneq, debtc + 1.0), 4))

def cg_f004_net_cash_position_core30_2nd_v031_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_slope(cashneq, 4), 8))
def cg_f004_net_cash_position_core31_2nd_v032_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_slope(investments, 4), 8))
def cg_f004_net_cash_position_core32_2nd_v033_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_slope(debt, 4), 8))
def cg_f004_net_cash_position_core33_2nd_v034_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_slope(debtc, 4), 8))
def cg_f004_net_cash_position_core34_2nd_v035_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_slope(debtnc, 4), 8))
def cg_f004_net_cash_position_core35_2nd_v036_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_slope(cashneq + investments, 4), 8))
def cg_f004_net_cash_position_core36_2nd_v037_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_slope((cashneq + investments) - debt, 4), 8))
def cg_f004_net_cash_position_core37_2nd_v038_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_slope(_safe_div(cashneq + investments, debt + 1.0), 4), 8))
def cg_f004_net_cash_position_core38_2nd_v039_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_slope(_safe_div(debtc, debt + 1.0), 4), 8))
def cg_f004_net_cash_position_core39_2nd_v040_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_slope(_safe_div(cashneq, debtc + 1.0), 4), 8))

def cg_f004_net_cash_position_core40_2nd_v041_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_slope(cashneq, 8), 12))
def cg_f004_net_cash_position_core41_2nd_v042_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_slope(investments, 8), 12))
def cg_f004_net_cash_position_core42_2nd_v043_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_slope(debt, 8), 12))
def cg_f004_net_cash_position_core43_2nd_v044_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_slope(debtc, 8), 12))
def cg_f004_net_cash_position_core44_2nd_v045_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_slope(debtnc, 8), 12))
def cg_f004_net_cash_position_core45_2nd_v046_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_slope(cashneq + investments, 8), 12))
def cg_f004_net_cash_position_core46_2nd_v047_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_slope((cashneq + investments) - debt, 8), 12))
def cg_f004_net_cash_position_core47_2nd_v048_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_slope(_safe_div(cashneq + investments, debt + 1.0), 8), 12))
def cg_f004_net_cash_position_core48_2nd_v049_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_slope(_safe_div(debtc, debt + 1.0), 8), 12))
def cg_f004_net_cash_position_core49_2nd_v050_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_slope(_safe_div(cashneq, debtc + 1.0), 8), 12))

def cg_f004_net_cash_position_core50_2nd_v051_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_diff(cashneq, 4), 8))
def cg_f004_net_cash_position_core51_2nd_v052_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_diff(investments, 4), 8))
def cg_f004_net_cash_position_core52_2nd_v053_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_diff(debt, 4), 8))
def cg_f004_net_cash_position_core53_2nd_v054_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_diff(debtc, 4), 8))
def cg_f004_net_cash_position_core54_2nd_v055_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_diff(debtnc, 4), 8))
def cg_f004_net_cash_position_core55_2nd_v056_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_diff(cashneq + investments, 4), 8))
def cg_f004_net_cash_position_core56_2nd_v057_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_diff((cashneq + investments) - debt, 4), 8))
def cg_f004_net_cash_position_core57_2nd_v058_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_diff(_safe_div(cashneq + investments, debt + 1.0), 4), 8))
def cg_f004_net_cash_position_core58_2nd_v059_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_diff(_safe_div(debtc, debt + 1.0), 4), 8))
def cg_f004_net_cash_position_core59_2nd_v060_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_diff(_safe_div(cashneq, debtc + 1.0), 4), 8))

def cg_f004_net_cash_position_core60_2nd_v061_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_slope(cashneq, 4), 12))
def cg_f004_net_cash_position_core61_2nd_v062_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_slope(investments, 4), 12))
def cg_f004_net_cash_position_core62_2nd_v063_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_slope(debt, 4), 12))
def cg_f004_net_cash_position_core63_2nd_v064_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_slope(debtc, 4), 12))
def cg_f004_net_cash_position_core64_2nd_v065_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_slope(debtnc, 4), 12))
def cg_f004_net_cash_position_core65_2nd_v066_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_slope(cashneq + investments, 4), 12))
def cg_f004_net_cash_position_core66_2nd_v067_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_slope((cashneq + investments) - debt, 4), 12))
def cg_f004_net_cash_position_core67_2nd_v068_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_slope(_safe_div(cashneq + investments, debt + 1.0), 4), 12))
def cg_f004_net_cash_position_core68_2nd_v069_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_slope(_safe_div(debtc, debt + 1.0), 4), 12))
def cg_f004_net_cash_position_core69_2nd_v070_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_slope(_safe_div(cashneq, debtc + 1.0), 4), 12))

def cg_f004_net_cash_position_core70_2nd_v071_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_diff(cashneq, 4), 12))
def cg_f004_net_cash_position_core71_2nd_v072_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_diff(investments, 4), 12))
def cg_f004_net_cash_position_core72_2nd_v073_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_diff(debt, 4), 12))
def cg_f004_net_cash_position_core73_2nd_v074_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_diff(debtc, 4), 12))
def cg_f004_net_cash_position_core74_2nd_v075_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_diff(debtnc, 4), 12))
def cg_f004_net_cash_position_core75_2nd_v076_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_diff(cashneq + investments, 4), 12))
def cg_f004_net_cash_position_core76_2nd_v077_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_diff((cashneq + investments) - debt, 4), 12))
def cg_f004_net_cash_position_core77_2nd_v078_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_diff(_safe_div(cashneq + investments, debt + 1.0), 4), 12))
def cg_f004_net_cash_position_core78_2nd_v079_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_diff(_safe_div(debtc, debt + 1.0), 4), 12))
def cg_f004_net_cash_position_core79_2nd_v080_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_diff(_safe_div(cashneq, debtc + 1.0), 4), 12))

def cg_f004_net_cash_position_core80_2nd_v081_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_slope(cashneq, 4), 4))
def cg_f004_net_cash_position_core81_2nd_v082_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_slope(investments, 4), 4))
def cg_f004_net_cash_position_core82_2nd_v083_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_slope(debt, 4), 4))
def cg_f004_net_cash_position_core83_2nd_v084_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_slope(debtc, 4), 4))
def cg_f004_net_cash_position_core84_2nd_v085_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_slope(debtnc, 4), 4))
def cg_f004_net_cash_position_core85_2nd_v086_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_slope(cashneq + investments, 4), 4))
def cg_f004_net_cash_position_core86_2nd_v087_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_slope((cashneq + investments) - debt, 4), 4))
def cg_f004_net_cash_position_core87_2nd_v088_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_slope(_safe_div(cashneq + investments, debt + 1.0), 4), 4))
def cg_f004_net_cash_position_core88_2nd_v089_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_slope(_safe_div(debtc, debt + 1.0), 4), 4))
def cg_f004_net_cash_position_core89_2nd_v090_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_slope(_safe_div(cashneq, debtc + 1.0), 4), 4))

def cg_f004_net_cash_position_core90_2nd_v091_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_diff(cashneq, 4), 4))
def cg_f004_net_cash_position_core91_2nd_v092_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_diff(investments, 4), 4))
def cg_f004_net_cash_position_core92_2nd_v093_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_diff(debt, 4), 4))
def cg_f004_net_cash_position_core93_2nd_v094_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_diff(debtc, 4), 4))
def cg_f004_net_cash_position_core94_2nd_v095_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_diff(debtnc, 4), 4))
def cg_f004_net_cash_position_core95_2nd_v096_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_diff(cashneq + investments, 4), 4))
def cg_f004_net_cash_position_core96_2nd_v097_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_diff((cashneq + investments) - debt, 4), 4))
def cg_f004_net_cash_position_core97_2nd_v098_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_diff(_safe_div(cashneq + investments, debt + 1.0), 4), 4))
def cg_f004_net_cash_position_core98_2nd_v099_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_diff(_safe_div(debtc, debt + 1.0), 4), 4))
def cg_f004_net_cash_position_core99_2nd_v100_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_mean(_diff(_safe_div(cashneq, debtc + 1.0), 4), 4))

def cg_f004_net_cash_position_core100_2nd_v101_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_mean(cashneq, 4), 4))
def cg_f004_net_cash_position_core101_2nd_v102_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_mean(investments, 4), 4))
def cg_f004_net_cash_position_core102_2nd_v103_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_mean(debt, 4), 4))
def cg_f004_net_cash_position_core103_2nd_v104_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_mean(debtc, 4), 4))
def cg_f004_net_cash_position_core104_2nd_v105_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_mean(debtnc, 4), 4))
def cg_f004_net_cash_position_core105_2nd_v106_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_mean(cashneq + investments, 4), 4))
def cg_f004_net_cash_position_core106_2nd_v107_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_mean((cashneq + investments) - debt, 4), 4))
def cg_f004_net_cash_position_core107_2nd_v108_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_mean(_safe_div(cashneq + investments, debt + 1.0), 4), 4))
def cg_f004_net_cash_position_core108_2nd_v109_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_mean(_safe_div(debtc, debt + 1.0), 4), 4))
def cg_f004_net_cash_position_core109_2nd_v110_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_mean(_safe_div(cashneq, debtc + 1.0), 4), 4))

def cg_f004_net_cash_position_core110_2nd_v111_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_mean(cashneq, 8), 8))
def cg_f004_net_cash_position_core111_2nd_v112_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_mean(investments, 8), 8))
def cg_f004_net_cash_position_core112_2nd_v113_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_mean(debt, 8), 8))
def cg_f004_net_cash_position_core113_2nd_v114_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_mean(debtc, 8), 8))
def cg_f004_net_cash_position_core114_2nd_v115_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_mean(debtnc, 8), 8))
def cg_f004_net_cash_position_core115_2nd_v116_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_mean(cashneq + investments, 8), 8))
def cg_f004_net_cash_position_core116_2nd_v117_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_mean((cashneq + investments) - debt, 8), 8))
def cg_f004_net_cash_position_core117_2nd_v118_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_mean(_safe_div(cashneq + investments, debt + 1.0), 8), 8))
def cg_f004_net_cash_position_core118_2nd_v119_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_mean(_safe_div(debtc, debt + 1.0), 8), 8))
def cg_f004_net_cash_position_core119_2nd_v120_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_slope(_mean(_safe_div(cashneq, debtc + 1.0), 8), 8))

def cg_f004_net_cash_position_core120_2nd_v121_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(_mean(cashneq, 4), 4))
def cg_f004_net_cash_position_core121_2nd_v122_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(_mean(investments, 4), 4))
def cg_f004_net_cash_position_core122_2nd_v123_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(_mean(debt, 4), 4))
def cg_f004_net_cash_position_core123_2nd_v124_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(_mean(debtc, 4), 4))
def cg_f004_net_cash_position_core124_2nd_v125_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(_mean(debtnc, 4), 4))
def cg_f004_net_cash_position_core125_2nd_v126_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(_mean(cashneq + investments, 4), 4))
def cg_f004_net_cash_position_core126_2nd_v127_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(_mean((cashneq + investments) - debt, 4), 4))
def cg_f004_net_cash_position_core127_2nd_v128_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(_mean(_safe_div(cashneq + investments, debt + 1.0), 4), 4))
def cg_f004_net_cash_position_core128_2nd_v129_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(_mean(_safe_div(debtc, debt + 1.0), 4), 4))
def cg_f004_net_cash_position_core129_2nd_v130_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_diff(_mean(_safe_div(cashneq, debtc + 1.0), 4), 4))

def cg_f004_net_cash_position_core130_2nd_v131_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_diff(_mean(cashneq, 4), 4), 8))
def cg_f004_net_cash_position_core131_2nd_v132_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_diff(_mean(investments, 4), 4), 8))
def cg_f004_net_cash_position_core132_2nd_v133_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_diff(_mean(debt, 4), 4), 8))
def cg_f004_net_cash_position_core133_2nd_v134_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_diff(_mean(debtc, 4), 4), 8))
def cg_f004_net_cash_position_core134_2nd_v135_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_diff(_mean(debtnc, 4), 4), 8))
def cg_f004_net_cash_position_core135_2nd_v136_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_diff(_mean(cashneq + investments, 4), 4), 8))
def cg_f004_net_cash_position_core136_2nd_v137_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_diff(_mean((cashneq + investments) - debt, 4), 4), 8))
def cg_f004_net_cash_position_core137_2nd_v138_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_diff(_mean(_safe_div(cashneq + investments, debt + 1.0), 4), 4), 8))
def cg_f004_net_cash_position_core138_2nd_v139_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_diff(_mean(_safe_div(debtc, debt + 1.0), 4), 4), 8))
def cg_f004_net_cash_position_core139_2nd_v140_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_z(_diff(_mean(_safe_div(cashneq, debtc + 1.0), 4), 4), 8))

def cg_f004_net_cash_position_core140_2nd_v141_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_slope(_mean(cashneq, 4), 4), 12))
def cg_f004_net_cash_position_core141_2nd_v142_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_slope(_mean(investments, 4), 4), 12))
def cg_f004_net_cash_position_core142_2nd_v143_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_slope(_mean(debt, 4), 4), 12))
def cg_f004_net_cash_position_core143_2nd_v144_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_slope(_mean(debtc, 4), 4), 12))
def cg_f004_net_cash_position_core144_2nd_v145_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_slope(_mean(debtnc, 4), 4), 12))
def cg_f004_net_cash_position_core145_2nd_v146_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_slope(_mean(cashneq + investments, 4), 4), 12))
def cg_f004_net_cash_position_core146_2nd_v147_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_slope(_mean((cashneq + investments) - debt, 4), 4), 12))
def cg_f004_net_cash_position_core147_2nd_v148_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_slope(_mean(_safe_div(cashneq + investments, debt + 1.0), 4), 4), 12))
def cg_f004_net_cash_position_core148_2nd_v149_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_slope(_mean(_safe_div(debtc, debt + 1.0), 4), 4), 12))
def cg_f004_net_cash_position_core149_2nd_v150_signal(cashneq, investments, debt, debtc, debtnc):
    return _clean(_rank(_slope(_mean(_safe_div(cashneq, debtc + 1.0), 4), 4), 12))
