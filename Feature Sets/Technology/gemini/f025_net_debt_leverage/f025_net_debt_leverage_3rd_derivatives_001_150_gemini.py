import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f025_net_debt_leverage_core00_3rd_v001_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(_diff(debt, 4), 4))
def cg_f025_net_debt_leverage_core01_3rd_v002_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(_diff(cashneq, 4), 4))
def cg_f025_net_debt_leverage_core02_3rd_v003_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(_diff(investments, 4), 4))
def cg_f025_net_debt_leverage_core03_3rd_v004_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(_diff(ebitda, 4), 4))
def cg_f025_net_debt_leverage_core04_3rd_v005_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(_diff(debt - cashneq - investments, 4), 4))
def cg_f025_net_debt_leverage_core05_3rd_v006_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(_diff(_safe_div(debt - cashneq - investments, ebitda.abs() + 1.0), 4), 4))
def cg_f025_net_debt_leverage_core06_3rd_v007_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(_diff(_safe_div(debt, assets), 4), 4))
def cg_f025_net_debt_leverage_core07_3rd_v008_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(_diff(_safe_div(cashneq + investments, assets), 4), 4))
def cg_f025_net_debt_leverage_core08_3rd_v009_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(_diff(_safe_div(ebitda, assets), 4), 4))
def cg_f025_net_debt_leverage_core09_3rd_v010_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(_diff(_log((debt - cashneq).abs() + 1.0), 4), 4))
def cg_f025_net_debt_leverage_core10_3rd_v011_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_diff(debt, 4), 8))
def cg_f025_net_debt_leverage_core11_3rd_v012_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_diff(cashneq, 4), 8))
def cg_f025_net_debt_leverage_core12_3rd_v013_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_diff(investments, 4), 8))
def cg_f025_net_debt_leverage_core13_3rd_v014_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_diff(ebitda, 4), 8))
def cg_f025_net_debt_leverage_core14_3rd_v015_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_diff(debt - cashneq - investments, 4), 8))
def cg_f025_net_debt_leverage_core15_3rd_v016_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_diff(_safe_div(debt - cashneq - investments, ebitda.abs() + 1.0), 4), 8))
def cg_f025_net_debt_leverage_core16_3rd_v017_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_diff(_safe_div(debt, assets), 4), 8))
def cg_f025_net_debt_leverage_core17_3rd_v018_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_diff(_safe_div(cashneq + investments, assets), 4), 8))
def cg_f025_net_debt_leverage_core18_3rd_v019_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_diff(_safe_div(ebitda, assets), 4), 8))
def cg_f025_net_debt_leverage_core19_3rd_v020_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_diff(_log((debt - cashneq).abs() + 1.0), 4), 8))
def cg_f025_net_debt_leverage_core20_3rd_v021_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(_slope(debt, 4), 4))
def cg_f025_net_debt_leverage_core21_3rd_v022_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(_slope(cashneq, 4), 4))
def cg_f025_net_debt_leverage_core22_3rd_v023_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(_slope(investments, 4), 4))
def cg_f025_net_debt_leverage_core23_3rd_v024_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(_slope(ebitda, 4), 4))
def cg_f025_net_debt_leverage_core24_3rd_v025_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(_slope(debt - cashneq - investments, 4), 4))
def cg_f025_net_debt_leverage_core25_3rd_v026_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(_slope(_safe_div(debt - cashneq - investments, ebitda.abs() + 1.0), 4), 4))
def cg_f025_net_debt_leverage_core26_3rd_v027_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(_slope(_safe_div(debt, assets), 4), 4))
def cg_f025_net_debt_leverage_core27_3rd_v028_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(_slope(_safe_div(cashneq + investments, assets), 4), 4))
def cg_f025_net_debt_leverage_core28_3rd_v029_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(_slope(_safe_div(ebitda, assets), 4), 4))
def cg_f025_net_debt_leverage_core29_3rd_v030_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(_slope(_log((debt - cashneq).abs() + 1.0), 4), 4))
def cg_f025_net_debt_leverage_core30_3rd_v031_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_diff(_diff(debt, 4), 4), 8))
def cg_f025_net_debt_leverage_core31_3rd_v032_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_diff(_diff(cashneq, 4), 4), 8))
def cg_f025_net_debt_leverage_core32_3rd_v033_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_diff(_diff(investments, 4), 4), 8))
def cg_f025_net_debt_leverage_core33_3rd_v034_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_diff(_diff(ebitda, 4), 4), 8))
def cg_f025_net_debt_leverage_core34_3rd_v035_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_diff(_diff(debt - cashneq - investments, 4), 4), 8))
def cg_f025_net_debt_leverage_core35_3rd_v036_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_diff(_diff(_safe_div(debt - cashneq - investments, ebitda.abs() + 1.0), 4), 4), 8))
def cg_f025_net_debt_leverage_core36_3rd_v037_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_diff(_diff(_safe_div(debt, assets), 4), 4), 8))
def cg_f025_net_debt_leverage_core37_3rd_v038_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_diff(_diff(_safe_div(cashneq + investments, assets), 4), 4), 8))
def cg_f025_net_debt_leverage_core38_3rd_v039_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_diff(_diff(_safe_div(ebitda, assets), 4), 4), 8))
def cg_f025_net_debt_leverage_core39_3rd_v040_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_diff(_diff(_log((debt - cashneq).abs() + 1.0), 4), 4), 8))
def cg_f025_net_debt_leverage_core40_3rd_v041_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_slope(_diff(debt, 4), 8), 12))
def cg_f025_net_debt_leverage_core41_3rd_v042_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_slope(_diff(cashneq, 4), 8), 12))
def cg_f025_net_debt_leverage_core42_3rd_v043_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_slope(_diff(investments, 4), 8), 12))
def cg_f025_net_debt_leverage_core43_3rd_v044_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_slope(_diff(ebitda, 4), 8), 12))
def cg_f025_net_debt_leverage_core44_3rd_v045_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_slope(_diff(debt - cashneq - investments, 4), 8), 12))
def cg_f025_net_debt_leverage_core45_3rd_v046_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_slope(_diff(_safe_div(debt - cashneq - investments, ebitda.abs() + 1.0), 4), 8), 12))
def cg_f025_net_debt_leverage_core46_3rd_v047_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_slope(_diff(_safe_div(debt, assets), 4), 8), 12))
def cg_f025_net_debt_leverage_core47_3rd_v048_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_slope(_diff(_safe_div(cashneq + investments, assets), 4), 8), 12))
def cg_f025_net_debt_leverage_core48_3rd_v049_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_slope(_diff(_safe_div(ebitda, assets), 4), 8), 12))
def cg_f025_net_debt_leverage_core49_3rd_v050_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_slope(_diff(_log((debt - cashneq).abs() + 1.0), 4), 8), 12))
def cg_f025_net_debt_leverage_core50_3rd_v051_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_diff(_slope(debt, 4), 4), 8))
def cg_f025_net_debt_leverage_core51_3rd_v052_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_diff(_slope(cashneq, 4), 4), 8))
def cg_f025_net_debt_leverage_core52_3rd_v053_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_diff(_slope(investments, 4), 4), 8))
def cg_f025_net_debt_leverage_core53_3rd_v054_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_diff(_slope(ebitda, 4), 4), 8))
def cg_f025_net_debt_leverage_core54_3rd_v055_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_diff(_slope(debt - cashneq - investments, 4), 4), 8))
def cg_f025_net_debt_leverage_core55_3rd_v056_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_diff(_slope(_safe_div(debt - cashneq - investments, ebitda.abs() + 1.0), 4), 4), 8))
def cg_f025_net_debt_leverage_core56_3rd_v057_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_diff(_slope(_safe_div(debt, assets), 4), 4), 8))
def cg_f025_net_debt_leverage_core57_3rd_v058_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_diff(_slope(_safe_div(cashneq + investments, assets), 4), 4), 8))
def cg_f025_net_debt_leverage_core58_3rd_v059_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_diff(_slope(_safe_div(ebitda, assets), 4), 4), 8))
def cg_f025_net_debt_leverage_core59_3rd_v060_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_diff(_slope(_log((debt - cashneq).abs() + 1.0), 4), 4), 8))
def cg_f025_net_debt_leverage_core60_3rd_v061_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_diff(_diff(debt, 4), 4), 12))
def cg_f025_net_debt_leverage_core61_3rd_v062_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_diff(_diff(cashneq, 4), 4), 12))
def cg_f025_net_debt_leverage_core62_3rd_v063_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_diff(_diff(investments, 4), 4), 12))
def cg_f025_net_debt_leverage_core63_3rd_v064_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_diff(_diff(ebitda, 4), 4), 12))
def cg_f025_net_debt_leverage_core64_3rd_v065_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_diff(_diff(debt - cashneq - investments, 4), 4), 12))
def cg_f025_net_debt_leverage_core65_3rd_v066_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_diff(_diff(_safe_div(debt - cashneq - investments, ebitda.abs() + 1.0), 4), 4), 12))
def cg_f025_net_debt_leverage_core66_3rd_v067_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_diff(_diff(_safe_div(debt, assets), 4), 4), 12))
def cg_f025_net_debt_leverage_core67_3rd_v068_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_diff(_diff(_safe_div(cashneq + investments, assets), 4), 4), 12))
def cg_f025_net_debt_leverage_core68_3rd_v069_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_diff(_diff(_safe_div(ebitda, assets), 4), 4), 12))
def cg_f025_net_debt_leverage_core69_3rd_v070_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_diff(_diff(_log((debt - cashneq).abs() + 1.0), 4), 4), 12))
def cg_f025_net_debt_leverage_core70_3rd_v071_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_slope(_diff(debt, 4), 8), 12))
def cg_f025_net_debt_leverage_core71_3rd_v072_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_slope(_diff(cashneq, 4), 8), 12))
def cg_f025_net_debt_leverage_core72_3rd_v073_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_slope(_diff(investments, 4), 8), 12))
def cg_f025_net_debt_leverage_core73_3rd_v074_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_slope(_diff(ebitda, 4), 8), 12))
def cg_f025_net_debt_leverage_core74_3rd_v075_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_slope(_diff(debt - cashneq - investments, 4), 8), 12))
def cg_f025_net_debt_leverage_core75_3rd_v076_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_slope(_diff(_safe_div(debt - cashneq - investments, ebitda.abs() + 1.0), 4), 8), 12))
def cg_f025_net_debt_leverage_core76_3rd_v077_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_slope(_diff(_safe_div(debt, assets), 4), 8), 12))
def cg_f025_net_debt_leverage_core77_3rd_v078_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_slope(_diff(_safe_div(cashneq + investments, assets), 4), 8), 12))
def cg_f025_net_debt_leverage_core78_3rd_v079_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_slope(_diff(_safe_div(ebitda, assets), 4), 8), 12))
def cg_f025_net_debt_leverage_core79_3rd_v080_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_slope(_diff(_log((debt - cashneq).abs() + 1.0), 4), 8), 12))
def cg_f025_net_debt_leverage_core80_3rd_v081_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_diff(_slope(debt, 4), 4), 12))
def cg_f025_net_debt_leverage_core81_3rd_v082_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_diff(_slope(cashneq, 4), 4), 12))
def cg_f025_net_debt_leverage_core82_3rd_v083_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_diff(_slope(investments, 4), 4), 12))
def cg_f025_net_debt_leverage_core83_3rd_v084_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_diff(_slope(ebitda, 4), 4), 12))
def cg_f025_net_debt_leverage_core84_3rd_v085_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_diff(_slope(debt - cashneq - investments, 4), 4), 12))
def cg_f025_net_debt_leverage_core85_3rd_v086_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_diff(_slope(_safe_div(debt - cashneq - investments, ebitda.abs() + 1.0), 4), 4), 12))
def cg_f025_net_debt_leverage_core86_3rd_v087_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_diff(_slope(_safe_div(debt, assets), 4), 4), 12))
def cg_f025_net_debt_leverage_core87_3rd_v088_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_diff(_slope(_safe_div(cashneq + investments, assets), 4), 4), 12))
def cg_f025_net_debt_leverage_core88_3rd_v089_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_diff(_slope(_safe_div(ebitda, assets), 4), 4), 12))
def cg_f025_net_debt_leverage_core89_3rd_v090_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_diff(_slope(_log((debt - cashneq).abs() + 1.0), 4), 4), 12))
def cg_f025_net_debt_leverage_core90_3rd_v091_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_diff(_diff(debt, 4), 4), 4))
def cg_f025_net_debt_leverage_core91_3rd_v092_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_diff(_diff(cashneq, 4), 4), 4))
def cg_f025_net_debt_leverage_core92_3rd_v093_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_diff(_diff(investments, 4), 4), 4))
def cg_f025_net_debt_leverage_core93_3rd_v094_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_diff(_diff(ebitda, 4), 4), 4))
def cg_f025_net_debt_leverage_core94_3rd_v095_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_diff(_diff(debt - cashneq - investments, 4), 4), 4))
def cg_f025_net_debt_leverage_core95_3rd_v096_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_diff(_diff(_safe_div(debt - cashneq - investments, ebitda.abs() + 1.0), 4), 4), 4))
def cg_f025_net_debt_leverage_core96_3rd_v097_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_diff(_diff(_safe_div(debt, assets), 4), 4), 4))
def cg_f025_net_debt_leverage_core97_3rd_v098_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_diff(_diff(_safe_div(cashneq + investments, assets), 4), 4), 4))
def cg_f025_net_debt_leverage_core98_3rd_v099_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_diff(_diff(_safe_div(ebitda, assets), 4), 4), 4))
def cg_f025_net_debt_leverage_core99_3rd_v100_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_diff(_diff(_log((debt - cashneq).abs() + 1.0), 4), 4), 4))
def cg_f025_net_debt_leverage_core100_3rd_v101_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_slope(_diff(debt, 4), 8), 4))
def cg_f025_net_debt_leverage_core101_3rd_v102_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_slope(_diff(cashneq, 4), 8), 4))
def cg_f025_net_debt_leverage_core102_3rd_v103_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_slope(_diff(investments, 4), 8), 4))
def cg_f025_net_debt_leverage_core103_3rd_v104_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_slope(_diff(ebitda, 4), 8), 4))
def cg_f025_net_debt_leverage_core104_3rd_v105_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_slope(_diff(debt - cashneq - investments, 4), 8), 4))
def cg_f025_net_debt_leverage_core105_3rd_v106_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_slope(_diff(_safe_div(debt - cashneq - investments, ebitda.abs() + 1.0), 4), 8), 4))
def cg_f025_net_debt_leverage_core106_3rd_v107_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_slope(_diff(_safe_div(debt, assets), 4), 8), 4))
def cg_f025_net_debt_leverage_core107_3rd_v108_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_slope(_diff(_safe_div(cashneq + investments, assets), 4), 8), 4))
def cg_f025_net_debt_leverage_core108_3rd_v109_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_slope(_diff(_safe_div(ebitda, assets), 4), 8), 4))
def cg_f025_net_debt_leverage_core109_3rd_v110_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_slope(_diff(_log((debt - cashneq).abs() + 1.0), 4), 8), 4))
def cg_f025_net_debt_leverage_core110_3rd_v111_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_diff(_slope(debt, 4), 4), 4))
def cg_f025_net_debt_leverage_core111_3rd_v112_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_diff(_slope(cashneq, 4), 4), 4))
def cg_f025_net_debt_leverage_core112_3rd_v113_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_diff(_slope(investments, 4), 4), 4))
def cg_f025_net_debt_leverage_core113_3rd_v114_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_diff(_slope(ebitda, 4), 4), 4))
def cg_f025_net_debt_leverage_core114_3rd_v115_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_diff(_slope(debt - cashneq - investments, 4), 4), 4))
def cg_f025_net_debt_leverage_core115_3rd_v116_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_diff(_slope(_safe_div(debt - cashneq - investments, ebitda.abs() + 1.0), 4), 4), 4))
def cg_f025_net_debt_leverage_core116_3rd_v117_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_diff(_slope(_safe_div(debt, assets), 4), 4), 4))
def cg_f025_net_debt_leverage_core117_3rd_v118_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_diff(_slope(_safe_div(cashneq + investments, assets), 4), 4), 4))
def cg_f025_net_debt_leverage_core118_3rd_v119_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_diff(_slope(_safe_div(ebitda, assets), 4), 4), 4))
def cg_f025_net_debt_leverage_core119_3rd_v120_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_diff(_slope(_log((debt - cashneq).abs() + 1.0), 4), 4), 4))
def cg_f025_net_debt_leverage_core120_3rd_v121_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_diff(_diff(debt, 4), 4), 4))
def cg_f025_net_debt_leverage_core121_3rd_v122_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_diff(_diff(cashneq, 4), 4), 4))
def cg_f025_net_debt_leverage_core122_3rd_v123_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_diff(_diff(investments, 4), 4), 4))
def cg_f025_net_debt_leverage_core123_3rd_v124_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_diff(_diff(ebitda, 4), 4), 4))
def cg_f025_net_debt_leverage_core124_3rd_v125_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_diff(_diff(debt - cashneq - investments, 4), 4), 4))
def cg_f025_net_debt_leverage_core125_3rd_v126_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_diff(_diff(_safe_div(debt - cashneq - investments, ebitda.abs() + 1.0), 4), 4), 4))
def cg_f025_net_debt_leverage_core126_3rd_v127_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_diff(_diff(_safe_div(debt, assets), 4), 4), 4))
def cg_f025_net_debt_leverage_core127_3rd_v128_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_diff(_diff(_safe_div(cashneq + investments, assets), 4), 4), 4))
def cg_f025_net_debt_leverage_core128_3rd_v129_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_diff(_diff(_safe_div(ebitda, assets), 4), 4), 4))
def cg_f025_net_debt_leverage_core129_3rd_v130_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_diff(_diff(_log((debt - cashneq).abs() + 1.0), 4), 4), 4))
def cg_f025_net_debt_leverage_core130_3rd_v131_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(_diff(_diff(debt, 4), 4), 4))
def cg_f025_net_debt_leverage_core131_3rd_v132_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(_diff(_diff(cashneq, 4), 4), 4))
def cg_f025_net_debt_leverage_core132_3rd_v133_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(_diff(_diff(investments, 4), 4), 4))
def cg_f025_net_debt_leverage_core133_3rd_v134_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(_diff(_diff(ebitda, 4), 4), 4))
def cg_f025_net_debt_leverage_core134_3rd_v135_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(_diff(_diff(debt - cashneq - investments, 4), 4), 4))
def cg_f025_net_debt_leverage_core135_3rd_v136_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(_diff(_diff(_safe_div(debt - cashneq - investments, ebitda.abs() + 1.0), 4), 4), 4))
def cg_f025_net_debt_leverage_core136_3rd_v137_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(_diff(_diff(_safe_div(debt, assets), 4), 4), 4))
def cg_f025_net_debt_leverage_core137_3rd_v138_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(_diff(_diff(_safe_div(cashneq + investments, assets), 4), 4), 4))
def cg_f025_net_debt_leverage_core138_3rd_v139_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(_diff(_diff(_safe_div(ebitda, assets), 4), 4), 4))
def cg_f025_net_debt_leverage_core139_3rd_v140_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(_diff(_diff(_log((debt - cashneq).abs() + 1.0), 4), 4), 4))
def cg_f025_net_debt_leverage_core140_3rd_v141_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_slope(_diff(_diff(debt, 4), 4), 4), 8))
def cg_f025_net_debt_leverage_core141_3rd_v142_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_slope(_diff(_diff(cashneq, 4), 4), 4), 8))
def cg_f025_net_debt_leverage_core142_3rd_v143_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_slope(_diff(_diff(investments, 4), 4), 4), 8))
def cg_f025_net_debt_leverage_core143_3rd_v144_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_slope(_diff(_diff(ebitda, 4), 4), 4), 8))
def cg_f025_net_debt_leverage_core144_3rd_v145_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_slope(_diff(_diff(debt - cashneq - investments, 4), 4), 4), 8))
def cg_f025_net_debt_leverage_core145_3rd_v146_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_slope(_diff(_diff(_safe_div(debt - cashneq - investments, ebitda.abs() + 1.0), 4), 4), 4), 8))
def cg_f025_net_debt_leverage_core146_3rd_v147_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_slope(_diff(_diff(_safe_div(debt, assets), 4), 4), 4), 8))
def cg_f025_net_debt_leverage_core147_3rd_v148_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_slope(_diff(_diff(_safe_div(cashneq + investments, assets), 4), 4), 4), 8))
def cg_f025_net_debt_leverage_core148_3rd_v149_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_slope(_diff(_diff(_safe_div(ebitda, assets), 4), 4), 4), 8))
def cg_f025_net_debt_leverage_core149_3rd_v150_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_slope(_diff(_diff(_log((debt - cashneq).abs() + 1.0), 4), 4), 4), 8))