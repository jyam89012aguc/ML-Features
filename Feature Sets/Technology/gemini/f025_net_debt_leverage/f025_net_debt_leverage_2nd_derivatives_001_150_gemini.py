import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f025_net_debt_leverage_core00_2nd_v001_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(debt, 4))
def cg_f025_net_debt_leverage_core01_2nd_v002_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(cashneq, 4))
def cg_f025_net_debt_leverage_core02_2nd_v003_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(investments, 4))
def cg_f025_net_debt_leverage_core03_2nd_v004_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(ebitda, 4))
def cg_f025_net_debt_leverage_core04_2nd_v005_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(debt - cashneq - investments, 4))
def cg_f025_net_debt_leverage_core05_2nd_v006_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_safe_div(debt - cashneq - investments, ebitda.abs() + 1.0), 4))
def cg_f025_net_debt_leverage_core06_2nd_v007_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_safe_div(debt, assets), 4))
def cg_f025_net_debt_leverage_core07_2nd_v008_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_safe_div(cashneq + investments, assets), 4))
def cg_f025_net_debt_leverage_core08_2nd_v009_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_safe_div(ebitda, assets), 4))
def cg_f025_net_debt_leverage_core09_2nd_v010_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_log((debt - cashneq).abs() + 1.0), 4))
def cg_f025_net_debt_leverage_core10_2nd_v011_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(debt, 8))
def cg_f025_net_debt_leverage_core11_2nd_v012_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(cashneq, 8))
def cg_f025_net_debt_leverage_core12_2nd_v013_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(investments, 8))
def cg_f025_net_debt_leverage_core13_2nd_v014_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(ebitda, 8))
def cg_f025_net_debt_leverage_core14_2nd_v015_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(debt - cashneq - investments, 8))
def cg_f025_net_debt_leverage_core15_2nd_v016_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_safe_div(debt - cashneq - investments, ebitda.abs() + 1.0), 8))
def cg_f025_net_debt_leverage_core16_2nd_v017_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_safe_div(debt, assets), 8))
def cg_f025_net_debt_leverage_core17_2nd_v018_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_safe_div(cashneq + investments, assets), 8))
def cg_f025_net_debt_leverage_core18_2nd_v019_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_safe_div(ebitda, assets), 8))
def cg_f025_net_debt_leverage_core19_2nd_v020_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_log((debt - cashneq).abs() + 1.0), 8))
def cg_f025_net_debt_leverage_core20_2nd_v021_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(debt, 4))
def cg_f025_net_debt_leverage_core21_2nd_v022_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(cashneq, 4))
def cg_f025_net_debt_leverage_core22_2nd_v023_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(investments, 4))
def cg_f025_net_debt_leverage_core23_2nd_v024_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(ebitda, 4))
def cg_f025_net_debt_leverage_core24_2nd_v025_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(debt - cashneq - investments, 4))
def cg_f025_net_debt_leverage_core25_2nd_v026_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(_safe_div(debt - cashneq - investments, ebitda.abs() + 1.0), 4))
def cg_f025_net_debt_leverage_core26_2nd_v027_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(_safe_div(debt, assets), 4))
def cg_f025_net_debt_leverage_core27_2nd_v028_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(_safe_div(cashneq + investments, assets), 4))
def cg_f025_net_debt_leverage_core28_2nd_v029_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(_safe_div(ebitda, assets), 4))
def cg_f025_net_debt_leverage_core29_2nd_v030_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(_log((debt - cashneq).abs() + 1.0), 4))
def cg_f025_net_debt_leverage_core30_2nd_v031_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_slope(debt, 4), 8))
def cg_f025_net_debt_leverage_core31_2nd_v032_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_slope(cashneq, 4), 8))
def cg_f025_net_debt_leverage_core32_2nd_v033_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_slope(investments, 4), 8))
def cg_f025_net_debt_leverage_core33_2nd_v034_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_slope(ebitda, 4), 8))
def cg_f025_net_debt_leverage_core34_2nd_v035_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_slope(debt - cashneq - investments, 4), 8))
def cg_f025_net_debt_leverage_core35_2nd_v036_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_slope(_safe_div(debt - cashneq - investments, ebitda.abs() + 1.0), 4), 8))
def cg_f025_net_debt_leverage_core36_2nd_v037_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_slope(_safe_div(debt, assets), 4), 8))
def cg_f025_net_debt_leverage_core37_2nd_v038_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_slope(_safe_div(cashneq + investments, assets), 4), 8))
def cg_f025_net_debt_leverage_core38_2nd_v039_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_slope(_safe_div(ebitda, assets), 4), 8))
def cg_f025_net_debt_leverage_core39_2nd_v040_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_slope(_log((debt - cashneq).abs() + 1.0), 4), 8))
def cg_f025_net_debt_leverage_core40_2nd_v041_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_slope(debt, 8), 12))
def cg_f025_net_debt_leverage_core41_2nd_v042_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_slope(cashneq, 8), 12))
def cg_f025_net_debt_leverage_core42_2nd_v043_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_slope(investments, 8), 12))
def cg_f025_net_debt_leverage_core43_2nd_v044_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_slope(ebitda, 8), 12))
def cg_f025_net_debt_leverage_core44_2nd_v045_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_slope(debt - cashneq - investments, 8), 12))
def cg_f025_net_debt_leverage_core45_2nd_v046_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_slope(_safe_div(debt - cashneq - investments, ebitda.abs() + 1.0), 8), 12))
def cg_f025_net_debt_leverage_core46_2nd_v047_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_slope(_safe_div(debt, assets), 8), 12))
def cg_f025_net_debt_leverage_core47_2nd_v048_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_slope(_safe_div(cashneq + investments, assets), 8), 12))
def cg_f025_net_debt_leverage_core48_2nd_v049_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_slope(_safe_div(ebitda, assets), 8), 12))
def cg_f025_net_debt_leverage_core49_2nd_v050_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_slope(_log((debt - cashneq).abs() + 1.0), 8), 12))
def cg_f025_net_debt_leverage_core50_2nd_v051_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_diff(debt, 4), 8))
def cg_f025_net_debt_leverage_core51_2nd_v052_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_diff(cashneq, 4), 8))
def cg_f025_net_debt_leverage_core52_2nd_v053_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_diff(investments, 4), 8))
def cg_f025_net_debt_leverage_core53_2nd_v054_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_diff(ebitda, 4), 8))
def cg_f025_net_debt_leverage_core54_2nd_v055_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_diff(debt - cashneq - investments, 4), 8))
def cg_f025_net_debt_leverage_core55_2nd_v056_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_diff(_safe_div(debt - cashneq - investments, ebitda.abs() + 1.0), 4), 8))
def cg_f025_net_debt_leverage_core56_2nd_v057_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_diff(_safe_div(debt, assets), 4), 8))
def cg_f025_net_debt_leverage_core57_2nd_v058_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_diff(_safe_div(cashneq + investments, assets), 4), 8))
def cg_f025_net_debt_leverage_core58_2nd_v059_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_diff(_safe_div(ebitda, assets), 4), 8))
def cg_f025_net_debt_leverage_core59_2nd_v060_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_diff(_log((debt - cashneq).abs() + 1.0), 4), 8))
def cg_f025_net_debt_leverage_core60_2nd_v061_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_slope(debt, 4), 12))
def cg_f025_net_debt_leverage_core61_2nd_v062_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_slope(cashneq, 4), 12))
def cg_f025_net_debt_leverage_core62_2nd_v063_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_slope(investments, 4), 12))
def cg_f025_net_debt_leverage_core63_2nd_v064_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_slope(ebitda, 4), 12))
def cg_f025_net_debt_leverage_core64_2nd_v065_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_slope(debt - cashneq - investments, 4), 12))
def cg_f025_net_debt_leverage_core65_2nd_v066_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_slope(_safe_div(debt - cashneq - investments, ebitda.abs() + 1.0), 4), 12))
def cg_f025_net_debt_leverage_core66_2nd_v067_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_slope(_safe_div(debt, assets), 4), 12))
def cg_f025_net_debt_leverage_core67_2nd_v068_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_slope(_safe_div(cashneq + investments, assets), 4), 12))
def cg_f025_net_debt_leverage_core68_2nd_v069_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_slope(_safe_div(ebitda, assets), 4), 12))
def cg_f025_net_debt_leverage_core69_2nd_v070_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_slope(_log((debt - cashneq).abs() + 1.0), 4), 12))
def cg_f025_net_debt_leverage_core70_2nd_v071_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_diff(debt, 4), 12))
def cg_f025_net_debt_leverage_core71_2nd_v072_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_diff(cashneq, 4), 12))
def cg_f025_net_debt_leverage_core72_2nd_v073_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_diff(investments, 4), 12))
def cg_f025_net_debt_leverage_core73_2nd_v074_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_diff(ebitda, 4), 12))
def cg_f025_net_debt_leverage_core74_2nd_v075_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_diff(debt - cashneq - investments, 4), 12))
def cg_f025_net_debt_leverage_core75_2nd_v076_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_diff(_safe_div(debt - cashneq - investments, ebitda.abs() + 1.0), 4), 12))
def cg_f025_net_debt_leverage_core76_2nd_v077_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_diff(_safe_div(debt, assets), 4), 12))
def cg_f025_net_debt_leverage_core77_2nd_v078_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_diff(_safe_div(cashneq + investments, assets), 4), 12))
def cg_f025_net_debt_leverage_core78_2nd_v079_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_diff(_safe_div(ebitda, assets), 4), 12))
def cg_f025_net_debt_leverage_core79_2nd_v080_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_diff(_log((debt - cashneq).abs() + 1.0), 4), 12))
def cg_f025_net_debt_leverage_core80_2nd_v081_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_slope(debt, 4), 4))
def cg_f025_net_debt_leverage_core81_2nd_v082_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_slope(cashneq, 4), 4))
def cg_f025_net_debt_leverage_core82_2nd_v083_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_slope(investments, 4), 4))
def cg_f025_net_debt_leverage_core83_2nd_v084_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_slope(ebitda, 4), 4))
def cg_f025_net_debt_leverage_core84_2nd_v085_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_slope(debt - cashneq - investments, 4), 4))
def cg_f025_net_debt_leverage_core85_2nd_v086_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_slope(_safe_div(debt - cashneq - investments, ebitda.abs() + 1.0), 4), 4))
def cg_f025_net_debt_leverage_core86_2nd_v087_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_slope(_safe_div(debt, assets), 4), 4))
def cg_f025_net_debt_leverage_core87_2nd_v088_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_slope(_safe_div(cashneq + investments, assets), 4), 4))
def cg_f025_net_debt_leverage_core88_2nd_v089_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_slope(_safe_div(ebitda, assets), 4), 4))
def cg_f025_net_debt_leverage_core89_2nd_v090_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_slope(_log((debt - cashneq).abs() + 1.0), 4), 4))
def cg_f025_net_debt_leverage_core90_2nd_v091_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_diff(debt, 4), 4))
def cg_f025_net_debt_leverage_core91_2nd_v092_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_diff(cashneq, 4), 4))
def cg_f025_net_debt_leverage_core92_2nd_v093_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_diff(investments, 4), 4))
def cg_f025_net_debt_leverage_core93_2nd_v094_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_diff(ebitda, 4), 4))
def cg_f025_net_debt_leverage_core94_2nd_v095_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_diff(debt - cashneq - investments, 4), 4))
def cg_f025_net_debt_leverage_core95_2nd_v096_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_diff(_safe_div(debt - cashneq - investments, ebitda.abs() + 1.0), 4), 4))
def cg_f025_net_debt_leverage_core96_2nd_v097_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_diff(_safe_div(debt, assets), 4), 4))
def cg_f025_net_debt_leverage_core97_2nd_v098_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_diff(_safe_div(cashneq + investments, assets), 4), 4))
def cg_f025_net_debt_leverage_core98_2nd_v099_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_diff(_safe_div(ebitda, assets), 4), 4))
def cg_f025_net_debt_leverage_core99_2nd_v100_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_mean(_diff(_log((debt - cashneq).abs() + 1.0), 4), 4))
def cg_f025_net_debt_leverage_core100_2nd_v101_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_mean(debt, 4), 4))
def cg_f025_net_debt_leverage_core101_2nd_v102_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_mean(cashneq, 4), 4))
def cg_f025_net_debt_leverage_core102_2nd_v103_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_mean(investments, 4), 4))
def cg_f025_net_debt_leverage_core103_2nd_v104_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_mean(ebitda, 4), 4))
def cg_f025_net_debt_leverage_core104_2nd_v105_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_mean(debt - cashneq - investments, 4), 4))
def cg_f025_net_debt_leverage_core105_2nd_v106_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_mean(_safe_div(debt - cashneq - investments, ebitda.abs() + 1.0), 4), 4))
def cg_f025_net_debt_leverage_core106_2nd_v107_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_mean(_safe_div(debt, assets), 4), 4))
def cg_f025_net_debt_leverage_core107_2nd_v108_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_mean(_safe_div(cashneq + investments, assets), 4), 4))
def cg_f025_net_debt_leverage_core108_2nd_v109_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_mean(_safe_div(ebitda, assets), 4), 4))
def cg_f025_net_debt_leverage_core109_2nd_v110_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_mean(_log((debt - cashneq).abs() + 1.0), 4), 4))
def cg_f025_net_debt_leverage_core110_2nd_v111_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_mean(debt, 8), 8))
def cg_f025_net_debt_leverage_core111_2nd_v112_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_mean(cashneq, 8), 8))
def cg_f025_net_debt_leverage_core112_2nd_v113_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_mean(investments, 8), 8))
def cg_f025_net_debt_leverage_core113_2nd_v114_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_mean(ebitda, 8), 8))
def cg_f025_net_debt_leverage_core114_2nd_v115_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_mean(debt - cashneq - investments, 8), 8))
def cg_f025_net_debt_leverage_core115_2nd_v116_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_mean(_safe_div(debt - cashneq - investments, ebitda.abs() + 1.0), 8), 8))
def cg_f025_net_debt_leverage_core116_2nd_v117_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_mean(_safe_div(debt, assets), 8), 8))
def cg_f025_net_debt_leverage_core117_2nd_v118_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_mean(_safe_div(cashneq + investments, assets), 8), 8))
def cg_f025_net_debt_leverage_core118_2nd_v119_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_mean(_safe_div(ebitda, assets), 8), 8))
def cg_f025_net_debt_leverage_core119_2nd_v120_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_slope(_mean(_log((debt - cashneq).abs() + 1.0), 8), 8))
def cg_f025_net_debt_leverage_core120_2nd_v121_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(_mean(debt, 4), 4))
def cg_f025_net_debt_leverage_core121_2nd_v122_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(_mean(cashneq, 4), 4))
def cg_f025_net_debt_leverage_core122_2nd_v123_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(_mean(investments, 4), 4))
def cg_f025_net_debt_leverage_core123_2nd_v124_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(_mean(ebitda, 4), 4))
def cg_f025_net_debt_leverage_core124_2nd_v125_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(_mean(debt - cashneq - investments, 4), 4))
def cg_f025_net_debt_leverage_core125_2nd_v126_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(_mean(_safe_div(debt - cashneq - investments, ebitda.abs() + 1.0), 4), 4))
def cg_f025_net_debt_leverage_core126_2nd_v127_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(_mean(_safe_div(debt, assets), 4), 4))
def cg_f025_net_debt_leverage_core127_2nd_v128_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(_mean(_safe_div(cashneq + investments, assets), 4), 4))
def cg_f025_net_debt_leverage_core128_2nd_v129_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(_mean(_safe_div(ebitda, assets), 4), 4))
def cg_f025_net_debt_leverage_core129_2nd_v130_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_diff(_mean(_log((debt - cashneq).abs() + 1.0), 4), 4))
def cg_f025_net_debt_leverage_core130_2nd_v131_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_diff(_mean(debt, 4), 4), 8))
def cg_f025_net_debt_leverage_core131_2nd_v132_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_diff(_mean(cashneq, 4), 4), 8))
def cg_f025_net_debt_leverage_core132_2nd_v133_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_diff(_mean(investments, 4), 4), 8))
def cg_f025_net_debt_leverage_core133_2nd_v134_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_diff(_mean(ebitda, 4), 4), 8))
def cg_f025_net_debt_leverage_core134_2nd_v135_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_diff(_mean(debt - cashneq - investments, 4), 4), 8))
def cg_f025_net_debt_leverage_core135_2nd_v136_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_diff(_mean(_safe_div(debt - cashneq - investments, ebitda.abs() + 1.0), 4), 4), 8))
def cg_f025_net_debt_leverage_core136_2nd_v137_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_diff(_mean(_safe_div(debt, assets), 4), 4), 8))
def cg_f025_net_debt_leverage_core137_2nd_v138_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_diff(_mean(_safe_div(cashneq + investments, assets), 4), 4), 8))
def cg_f025_net_debt_leverage_core138_2nd_v139_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_diff(_mean(_safe_div(ebitda, assets), 4), 4), 8))
def cg_f025_net_debt_leverage_core139_2nd_v140_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_z(_diff(_mean(_log((debt - cashneq).abs() + 1.0), 4), 4), 8))
def cg_f025_net_debt_leverage_core140_2nd_v141_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_slope(_mean(debt, 4), 4), 12))
def cg_f025_net_debt_leverage_core141_2nd_v142_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_slope(_mean(cashneq, 4), 4), 12))
def cg_f025_net_debt_leverage_core142_2nd_v143_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_slope(_mean(investments, 4), 4), 12))
def cg_f025_net_debt_leverage_core143_2nd_v144_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_slope(_mean(ebitda, 4), 4), 12))
def cg_f025_net_debt_leverage_core144_2nd_v145_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_slope(_mean(debt - cashneq - investments, 4), 4), 12))
def cg_f025_net_debt_leverage_core145_2nd_v146_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_slope(_mean(_safe_div(debt - cashneq - investments, ebitda.abs() + 1.0), 4), 4), 12))
def cg_f025_net_debt_leverage_core146_2nd_v147_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_slope(_mean(_safe_div(debt, assets), 4), 4), 12))
def cg_f025_net_debt_leverage_core147_2nd_v148_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_slope(_mean(_safe_div(cashneq + investments, assets), 4), 4), 12))
def cg_f025_net_debt_leverage_core148_2nd_v149_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_slope(_mean(_safe_div(ebitda, assets), 4), 4), 12))
def cg_f025_net_debt_leverage_core149_2nd_v150_signal(debt, cashneq, investments, ebitda, assets):
    return _clean(_rank(_slope(_mean(_log((debt - cashneq).abs() + 1.0), 4), 4), 12))