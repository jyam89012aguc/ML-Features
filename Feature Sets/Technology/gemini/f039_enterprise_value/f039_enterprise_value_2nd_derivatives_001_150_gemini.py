import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f039_enterprise_value_core00_2nd_v001_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(ev, 4))
def cg_f039_enterprise_value_core01_2nd_v002_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(marketcap + debt - cashneq - investments, 4))
def cg_f039_enterprise_value_core02_2nd_v003_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_safe_div(ev, marketcap.abs() + 1.0), 4))
def cg_f039_enterprise_value_core03_2nd_v004_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_safe_div(debt, ev.abs() + 1.0), 4))
def cg_f039_enterprise_value_core04_2nd_v005_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_safe_div(cashneq + investments, ev.abs() + 1.0), 4))
def cg_f039_enterprise_value_core05_2nd_v006_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_diff(ev, 4), 4))
def cg_f039_enterprise_value_core06_2nd_v007_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_slope(ev, 8), 4))
def cg_f039_enterprise_value_core07_2nd_v008_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_z(ev, 12), 4))
def cg_f039_enterprise_value_core08_2nd_v009_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(ev - marketcap, 4))
def cg_f039_enterprise_value_core09_2nd_v010_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(debt - cashneq, 4))
def cg_f039_enterprise_value_core10_2nd_v011_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(ev, 8))
def cg_f039_enterprise_value_core11_2nd_v012_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(marketcap + debt - cashneq - investments, 8))
def cg_f039_enterprise_value_core12_2nd_v013_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_safe_div(ev, marketcap.abs() + 1.0), 8))
def cg_f039_enterprise_value_core13_2nd_v014_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_safe_div(debt, ev.abs() + 1.0), 8))
def cg_f039_enterprise_value_core14_2nd_v015_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_safe_div(cashneq + investments, ev.abs() + 1.0), 8))
def cg_f039_enterprise_value_core15_2nd_v016_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_diff(ev, 4), 8))
def cg_f039_enterprise_value_core16_2nd_v017_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_slope(ev, 8), 8))
def cg_f039_enterprise_value_core17_2nd_v018_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_z(ev, 12), 8))
def cg_f039_enterprise_value_core18_2nd_v019_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(ev - marketcap, 8))
def cg_f039_enterprise_value_core19_2nd_v020_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(debt - cashneq, 8))
def cg_f039_enterprise_value_core20_2nd_v021_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(ev, 4))
def cg_f039_enterprise_value_core21_2nd_v022_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(marketcap + debt - cashneq - investments, 4))
def cg_f039_enterprise_value_core22_2nd_v023_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_safe_div(ev, marketcap.abs() + 1.0), 4))
def cg_f039_enterprise_value_core23_2nd_v024_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_safe_div(debt, ev.abs() + 1.0), 4))
def cg_f039_enterprise_value_core24_2nd_v025_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_safe_div(cashneq + investments, ev.abs() + 1.0), 4))
def cg_f039_enterprise_value_core25_2nd_v026_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_diff(ev, 4), 4))
def cg_f039_enterprise_value_core26_2nd_v027_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_slope(ev, 8), 4))
def cg_f039_enterprise_value_core27_2nd_v028_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_z(ev, 12), 4))
def cg_f039_enterprise_value_core28_2nd_v029_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(ev - marketcap, 4))
def cg_f039_enterprise_value_core29_2nd_v030_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(debt - cashneq, 4))
def cg_f039_enterprise_value_core30_2nd_v031_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_slope(ev, 4), 8))
def cg_f039_enterprise_value_core31_2nd_v032_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_slope(marketcap + debt - cashneq - investments, 4), 8))
def cg_f039_enterprise_value_core32_2nd_v033_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_slope(_safe_div(ev, marketcap.abs() + 1.0), 4), 8))
def cg_f039_enterprise_value_core33_2nd_v034_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_slope(_safe_div(debt, ev.abs() + 1.0), 4), 8))
def cg_f039_enterprise_value_core34_2nd_v035_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_slope(_safe_div(cashneq + investments, ev.abs() + 1.0), 4), 8))
def cg_f039_enterprise_value_core35_2nd_v036_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_slope(_diff(ev, 4), 4), 8))
def cg_f039_enterprise_value_core36_2nd_v037_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_slope(_slope(ev, 8), 4), 8))
def cg_f039_enterprise_value_core37_2nd_v038_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_slope(_z(ev, 12), 4), 8))
def cg_f039_enterprise_value_core38_2nd_v039_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_slope(ev - marketcap, 4), 8))
def cg_f039_enterprise_value_core39_2nd_v040_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_slope(debt - cashneq, 4), 8))
def cg_f039_enterprise_value_core40_2nd_v041_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_slope(ev, 8), 12))
def cg_f039_enterprise_value_core41_2nd_v042_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_slope(marketcap + debt - cashneq - investments, 8), 12))
def cg_f039_enterprise_value_core42_2nd_v043_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_slope(_safe_div(ev, marketcap.abs() + 1.0), 8), 12))
def cg_f039_enterprise_value_core43_2nd_v044_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_slope(_safe_div(debt, ev.abs() + 1.0), 8), 12))
def cg_f039_enterprise_value_core44_2nd_v045_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_slope(_safe_div(cashneq + investments, ev.abs() + 1.0), 8), 12))
def cg_f039_enterprise_value_core45_2nd_v046_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_slope(_diff(ev, 4), 8), 12))
def cg_f039_enterprise_value_core46_2nd_v047_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_slope(_slope(ev, 8), 8), 12))
def cg_f039_enterprise_value_core47_2nd_v048_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_slope(_z(ev, 12), 8), 12))
def cg_f039_enterprise_value_core48_2nd_v049_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_slope(ev - marketcap, 8), 12))
def cg_f039_enterprise_value_core49_2nd_v050_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_slope(debt - cashneq, 8), 12))
def cg_f039_enterprise_value_core50_2nd_v051_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_diff(ev, 4), 8))
def cg_f039_enterprise_value_core51_2nd_v052_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_diff(marketcap + debt - cashneq - investments, 4), 8))
def cg_f039_enterprise_value_core52_2nd_v053_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_diff(_safe_div(ev, marketcap.abs() + 1.0), 4), 8))
def cg_f039_enterprise_value_core53_2nd_v054_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_diff(_safe_div(debt, ev.abs() + 1.0), 4), 8))
def cg_f039_enterprise_value_core54_2nd_v055_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_diff(_safe_div(cashneq + investments, ev.abs() + 1.0), 4), 8))
def cg_f039_enterprise_value_core55_2nd_v056_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_diff(_diff(ev, 4), 4), 8))
def cg_f039_enterprise_value_core56_2nd_v057_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_diff(_slope(ev, 8), 4), 8))
def cg_f039_enterprise_value_core57_2nd_v058_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_diff(_z(ev, 12), 4), 8))
def cg_f039_enterprise_value_core58_2nd_v059_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_diff(ev - marketcap, 4), 8))
def cg_f039_enterprise_value_core59_2nd_v060_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_diff(debt - cashneq, 4), 8))
def cg_f039_enterprise_value_core60_2nd_v061_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_slope(ev, 4), 12))
def cg_f039_enterprise_value_core61_2nd_v062_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_slope(marketcap + debt - cashneq - investments, 4), 12))
def cg_f039_enterprise_value_core62_2nd_v063_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_slope(_safe_div(ev, marketcap.abs() + 1.0), 4), 12))
def cg_f039_enterprise_value_core63_2nd_v064_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_slope(_safe_div(debt, ev.abs() + 1.0), 4), 12))
def cg_f039_enterprise_value_core64_2nd_v065_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_slope(_safe_div(cashneq + investments, ev.abs() + 1.0), 4), 12))
def cg_f039_enterprise_value_core65_2nd_v066_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_slope(_diff(ev, 4), 4), 12))
def cg_f039_enterprise_value_core66_2nd_v067_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_slope(_slope(ev, 8), 4), 12))
def cg_f039_enterprise_value_core67_2nd_v068_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_slope(_z(ev, 12), 4), 12))
def cg_f039_enterprise_value_core68_2nd_v069_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_slope(ev - marketcap, 4), 12))
def cg_f039_enterprise_value_core69_2nd_v070_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_slope(debt - cashneq, 4), 12))
def cg_f039_enterprise_value_core70_2nd_v071_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_diff(ev, 4), 12))
def cg_f039_enterprise_value_core71_2nd_v072_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_diff(marketcap + debt - cashneq - investments, 4), 12))
def cg_f039_enterprise_value_core72_2nd_v073_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_diff(_safe_div(ev, marketcap.abs() + 1.0), 4), 12))
def cg_f039_enterprise_value_core73_2nd_v074_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_diff(_safe_div(debt, ev.abs() + 1.0), 4), 12))
def cg_f039_enterprise_value_core74_2nd_v075_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_diff(_safe_div(cashneq + investments, ev.abs() + 1.0), 4), 12))
def cg_f039_enterprise_value_core75_2nd_v076_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_diff(_diff(ev, 4), 4), 12))
def cg_f039_enterprise_value_core76_2nd_v077_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_diff(_slope(ev, 8), 4), 12))
def cg_f039_enterprise_value_core77_2nd_v078_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_diff(_z(ev, 12), 4), 12))
def cg_f039_enterprise_value_core78_2nd_v079_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_diff(ev - marketcap, 4), 12))
def cg_f039_enterprise_value_core79_2nd_v080_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_diff(debt - cashneq, 4), 12))
def cg_f039_enterprise_value_core80_2nd_v081_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_slope(ev, 4), 4))
def cg_f039_enterprise_value_core81_2nd_v082_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_slope(marketcap + debt - cashneq - investments, 4), 4))
def cg_f039_enterprise_value_core82_2nd_v083_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_slope(_safe_div(ev, marketcap.abs() + 1.0), 4), 4))
def cg_f039_enterprise_value_core83_2nd_v084_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_slope(_safe_div(debt, ev.abs() + 1.0), 4), 4))
def cg_f039_enterprise_value_core84_2nd_v085_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_slope(_safe_div(cashneq + investments, ev.abs() + 1.0), 4), 4))
def cg_f039_enterprise_value_core85_2nd_v086_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_slope(_diff(ev, 4), 4), 4))
def cg_f039_enterprise_value_core86_2nd_v087_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_slope(_slope(ev, 8), 4), 4))
def cg_f039_enterprise_value_core87_2nd_v088_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_slope(_z(ev, 12), 4), 4))
def cg_f039_enterprise_value_core88_2nd_v089_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_slope(ev - marketcap, 4), 4))
def cg_f039_enterprise_value_core89_2nd_v090_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_slope(debt - cashneq, 4), 4))
def cg_f039_enterprise_value_core90_2nd_v091_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_diff(ev, 4), 4))
def cg_f039_enterprise_value_core91_2nd_v092_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_diff(marketcap + debt - cashneq - investments, 4), 4))
def cg_f039_enterprise_value_core92_2nd_v093_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_diff(_safe_div(ev, marketcap.abs() + 1.0), 4), 4))
def cg_f039_enterprise_value_core93_2nd_v094_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_diff(_safe_div(debt, ev.abs() + 1.0), 4), 4))
def cg_f039_enterprise_value_core94_2nd_v095_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_diff(_safe_div(cashneq + investments, ev.abs() + 1.0), 4), 4))
def cg_f039_enterprise_value_core95_2nd_v096_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_diff(_diff(ev, 4), 4), 4))
def cg_f039_enterprise_value_core96_2nd_v097_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_diff(_slope(ev, 8), 4), 4))
def cg_f039_enterprise_value_core97_2nd_v098_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_diff(_z(ev, 12), 4), 4))
def cg_f039_enterprise_value_core98_2nd_v099_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_diff(ev - marketcap, 4), 4))
def cg_f039_enterprise_value_core99_2nd_v100_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_diff(debt - cashneq, 4), 4))
def cg_f039_enterprise_value_core100_2nd_v101_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_mean(ev, 4), 4))
def cg_f039_enterprise_value_core101_2nd_v102_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_mean(marketcap + debt - cashneq - investments, 4), 4))
def cg_f039_enterprise_value_core102_2nd_v103_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_mean(_safe_div(ev, marketcap.abs() + 1.0), 4), 4))
def cg_f039_enterprise_value_core103_2nd_v104_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_mean(_safe_div(debt, ev.abs() + 1.0), 4), 4))
def cg_f039_enterprise_value_core104_2nd_v105_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_mean(_safe_div(cashneq + investments, ev.abs() + 1.0), 4), 4))
def cg_f039_enterprise_value_core105_2nd_v106_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_mean(_diff(ev, 4), 4), 4))
def cg_f039_enterprise_value_core106_2nd_v107_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_mean(_slope(ev, 8), 4), 4))
def cg_f039_enterprise_value_core107_2nd_v108_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_mean(_z(ev, 12), 4), 4))
def cg_f039_enterprise_value_core108_2nd_v109_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_mean(ev - marketcap, 4), 4))
def cg_f039_enterprise_value_core109_2nd_v110_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_mean(debt - cashneq, 4), 4))
def cg_f039_enterprise_value_core110_2nd_v111_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_mean(ev, 8), 8))
def cg_f039_enterprise_value_core111_2nd_v112_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_mean(marketcap + debt - cashneq - investments, 8), 8))
def cg_f039_enterprise_value_core112_2nd_v113_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_mean(_safe_div(ev, marketcap.abs() + 1.0), 8), 8))
def cg_f039_enterprise_value_core113_2nd_v114_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_mean(_safe_div(debt, ev.abs() + 1.0), 8), 8))
def cg_f039_enterprise_value_core114_2nd_v115_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_mean(_safe_div(cashneq + investments, ev.abs() + 1.0), 8), 8))
def cg_f039_enterprise_value_core115_2nd_v116_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_mean(_diff(ev, 4), 8), 8))
def cg_f039_enterprise_value_core116_2nd_v117_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_mean(_slope(ev, 8), 8), 8))
def cg_f039_enterprise_value_core117_2nd_v118_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_mean(_z(ev, 12), 8), 8))
def cg_f039_enterprise_value_core118_2nd_v119_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_mean(ev - marketcap, 8), 8))
def cg_f039_enterprise_value_core119_2nd_v120_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_mean(debt - cashneq, 8), 8))
def cg_f039_enterprise_value_core120_2nd_v121_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_mean(ev, 4), 4))
def cg_f039_enterprise_value_core121_2nd_v122_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_mean(marketcap + debt - cashneq - investments, 4), 4))
def cg_f039_enterprise_value_core122_2nd_v123_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_mean(_safe_div(ev, marketcap.abs() + 1.0), 4), 4))
def cg_f039_enterprise_value_core123_2nd_v124_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_mean(_safe_div(debt, ev.abs() + 1.0), 4), 4))
def cg_f039_enterprise_value_core124_2nd_v125_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_mean(_safe_div(cashneq + investments, ev.abs() + 1.0), 4), 4))
def cg_f039_enterprise_value_core125_2nd_v126_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_mean(_diff(ev, 4), 4), 4))
def cg_f039_enterprise_value_core126_2nd_v127_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_mean(_slope(ev, 8), 4), 4))
def cg_f039_enterprise_value_core127_2nd_v128_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_mean(_z(ev, 12), 4), 4))
def cg_f039_enterprise_value_core128_2nd_v129_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_mean(ev - marketcap, 4), 4))
def cg_f039_enterprise_value_core129_2nd_v130_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_mean(debt - cashneq, 4), 4))
def cg_f039_enterprise_value_core130_2nd_v131_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_diff(_mean(ev, 4), 4), 8))
def cg_f039_enterprise_value_core131_2nd_v132_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_diff(_mean(marketcap + debt - cashneq - investments, 4), 4), 8))
def cg_f039_enterprise_value_core132_2nd_v133_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_diff(_mean(_safe_div(ev, marketcap.abs() + 1.0), 4), 4), 8))
def cg_f039_enterprise_value_core133_2nd_v134_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_diff(_mean(_safe_div(debt, ev.abs() + 1.0), 4), 4), 8))
def cg_f039_enterprise_value_core134_2nd_v135_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_diff(_mean(_safe_div(cashneq + investments, ev.abs() + 1.0), 4), 4), 8))
def cg_f039_enterprise_value_core135_2nd_v136_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_diff(_mean(_diff(ev, 4), 4), 4), 8))
def cg_f039_enterprise_value_core136_2nd_v137_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_diff(_mean(_slope(ev, 8), 4), 4), 8))
def cg_f039_enterprise_value_core137_2nd_v138_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_diff(_mean(_z(ev, 12), 4), 4), 8))
def cg_f039_enterprise_value_core138_2nd_v139_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_diff(_mean(ev - marketcap, 4), 4), 8))
def cg_f039_enterprise_value_core139_2nd_v140_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_diff(_mean(debt - cashneq, 4), 4), 8))
def cg_f039_enterprise_value_core140_2nd_v141_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_slope(_mean(ev, 4), 4), 12))
def cg_f039_enterprise_value_core141_2nd_v142_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_slope(_mean(marketcap + debt - cashneq - investments, 4), 4), 12))
def cg_f039_enterprise_value_core142_2nd_v143_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_slope(_mean(_safe_div(ev, marketcap.abs() + 1.0), 4), 4), 12))
def cg_f039_enterprise_value_core143_2nd_v144_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_slope(_mean(_safe_div(debt, ev.abs() + 1.0), 4), 4), 12))
def cg_f039_enterprise_value_core144_2nd_v145_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_slope(_mean(_safe_div(cashneq + investments, ev.abs() + 1.0), 4), 4), 12))
def cg_f039_enterprise_value_core145_2nd_v146_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_slope(_mean(_diff(ev, 4), 4), 4), 12))
def cg_f039_enterprise_value_core146_2nd_v147_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_slope(_mean(_slope(ev, 8), 4), 4), 12))
def cg_f039_enterprise_value_core147_2nd_v148_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_slope(_mean(_z(ev, 12), 4), 4), 12))
def cg_f039_enterprise_value_core148_2nd_v149_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_slope(_mean(ev - marketcap, 4), 4), 12))
def cg_f039_enterprise_value_core149_2nd_v150_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_slope(_mean(debt - cashneq, 4), 4), 12))