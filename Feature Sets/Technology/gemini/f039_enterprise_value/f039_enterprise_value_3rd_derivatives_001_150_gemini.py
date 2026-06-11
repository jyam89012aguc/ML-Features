import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f039_enterprise_value_core00_3rd_v001_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_diff(ev, 4), 4))
def cg_f039_enterprise_value_core01_3rd_v002_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_diff(marketcap + debt - cashneq - investments, 4), 4))
def cg_f039_enterprise_value_core02_3rd_v003_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_diff(_safe_div(ev, marketcap.abs() + 1.0), 4), 4))
def cg_f039_enterprise_value_core03_3rd_v004_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_diff(_safe_div(debt, ev.abs() + 1.0), 4), 4))
def cg_f039_enterprise_value_core04_3rd_v005_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_diff(_safe_div(cashneq + investments, ev.abs() + 1.0), 4), 4))
def cg_f039_enterprise_value_core05_3rd_v006_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_diff(_diff(ev, 4), 4), 4))
def cg_f039_enterprise_value_core06_3rd_v007_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_diff(_slope(ev, 8), 4), 4))
def cg_f039_enterprise_value_core07_3rd_v008_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_diff(_z(ev, 12), 4), 4))
def cg_f039_enterprise_value_core08_3rd_v009_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_diff(ev - marketcap, 4), 4))
def cg_f039_enterprise_value_core09_3rd_v010_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_diff(debt - cashneq, 4), 4))
def cg_f039_enterprise_value_core10_3rd_v011_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_diff(ev, 4), 8))
def cg_f039_enterprise_value_core11_3rd_v012_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_diff(marketcap + debt - cashneq - investments, 4), 8))
def cg_f039_enterprise_value_core12_3rd_v013_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_diff(_safe_div(ev, marketcap.abs() + 1.0), 4), 8))
def cg_f039_enterprise_value_core13_3rd_v014_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_diff(_safe_div(debt, ev.abs() + 1.0), 4), 8))
def cg_f039_enterprise_value_core14_3rd_v015_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_diff(_safe_div(cashneq + investments, ev.abs() + 1.0), 4), 8))
def cg_f039_enterprise_value_core15_3rd_v016_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_diff(_diff(ev, 4), 4), 8))
def cg_f039_enterprise_value_core16_3rd_v017_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_diff(_slope(ev, 8), 4), 8))
def cg_f039_enterprise_value_core17_3rd_v018_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_diff(_z(ev, 12), 4), 8))
def cg_f039_enterprise_value_core18_3rd_v019_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_diff(ev - marketcap, 4), 8))
def cg_f039_enterprise_value_core19_3rd_v020_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_diff(debt - cashneq, 4), 8))
def cg_f039_enterprise_value_core20_3rd_v021_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_slope(ev, 4), 4))
def cg_f039_enterprise_value_core21_3rd_v022_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_slope(marketcap + debt - cashneq - investments, 4), 4))
def cg_f039_enterprise_value_core22_3rd_v023_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_slope(_safe_div(ev, marketcap.abs() + 1.0), 4), 4))
def cg_f039_enterprise_value_core23_3rd_v024_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_slope(_safe_div(debt, ev.abs() + 1.0), 4), 4))
def cg_f039_enterprise_value_core24_3rd_v025_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_slope(_safe_div(cashneq + investments, ev.abs() + 1.0), 4), 4))
def cg_f039_enterprise_value_core25_3rd_v026_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_slope(_diff(ev, 4), 4), 4))
def cg_f039_enterprise_value_core26_3rd_v027_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_slope(_slope(ev, 8), 4), 4))
def cg_f039_enterprise_value_core27_3rd_v028_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_slope(_z(ev, 12), 4), 4))
def cg_f039_enterprise_value_core28_3rd_v029_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_slope(ev - marketcap, 4), 4))
def cg_f039_enterprise_value_core29_3rd_v030_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_slope(debt - cashneq, 4), 4))
def cg_f039_enterprise_value_core30_3rd_v031_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_diff(_diff(ev, 4), 4), 8))
def cg_f039_enterprise_value_core31_3rd_v032_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_diff(_diff(marketcap + debt - cashneq - investments, 4), 4), 8))
def cg_f039_enterprise_value_core32_3rd_v033_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_diff(_diff(_safe_div(ev, marketcap.abs() + 1.0), 4), 4), 8))
def cg_f039_enterprise_value_core33_3rd_v034_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_diff(_diff(_safe_div(debt, ev.abs() + 1.0), 4), 4), 8))
def cg_f039_enterprise_value_core34_3rd_v035_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_diff(_diff(_safe_div(cashneq + investments, ev.abs() + 1.0), 4), 4), 8))
def cg_f039_enterprise_value_core35_3rd_v036_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_diff(_diff(_diff(ev, 4), 4), 4), 8))
def cg_f039_enterprise_value_core36_3rd_v037_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_diff(_diff(_slope(ev, 8), 4), 4), 8))
def cg_f039_enterprise_value_core37_3rd_v038_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_diff(_diff(_z(ev, 12), 4), 4), 8))
def cg_f039_enterprise_value_core38_3rd_v039_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_diff(_diff(ev - marketcap, 4), 4), 8))
def cg_f039_enterprise_value_core39_3rd_v040_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_diff(_diff(debt - cashneq, 4), 4), 8))
def cg_f039_enterprise_value_core40_3rd_v041_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_slope(_diff(ev, 4), 8), 12))
def cg_f039_enterprise_value_core41_3rd_v042_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_slope(_diff(marketcap + debt - cashneq - investments, 4), 8), 12))
def cg_f039_enterprise_value_core42_3rd_v043_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_slope(_diff(_safe_div(ev, marketcap.abs() + 1.0), 4), 8), 12))
def cg_f039_enterprise_value_core43_3rd_v044_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_slope(_diff(_safe_div(debt, ev.abs() + 1.0), 4), 8), 12))
def cg_f039_enterprise_value_core44_3rd_v045_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_slope(_diff(_safe_div(cashneq + investments, ev.abs() + 1.0), 4), 8), 12))
def cg_f039_enterprise_value_core45_3rd_v046_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_slope(_diff(_diff(ev, 4), 4), 8), 12))
def cg_f039_enterprise_value_core46_3rd_v047_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_slope(_diff(_slope(ev, 8), 4), 8), 12))
def cg_f039_enterprise_value_core47_3rd_v048_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_slope(_diff(_z(ev, 12), 4), 8), 12))
def cg_f039_enterprise_value_core48_3rd_v049_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_slope(_diff(ev - marketcap, 4), 8), 12))
def cg_f039_enterprise_value_core49_3rd_v050_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_slope(_diff(debt - cashneq, 4), 8), 12))
def cg_f039_enterprise_value_core50_3rd_v051_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_diff(_slope(ev, 4), 4), 8))
def cg_f039_enterprise_value_core51_3rd_v052_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_diff(_slope(marketcap + debt - cashneq - investments, 4), 4), 8))
def cg_f039_enterprise_value_core52_3rd_v053_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_diff(_slope(_safe_div(ev, marketcap.abs() + 1.0), 4), 4), 8))
def cg_f039_enterprise_value_core53_3rd_v054_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_diff(_slope(_safe_div(debt, ev.abs() + 1.0), 4), 4), 8))
def cg_f039_enterprise_value_core54_3rd_v055_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_diff(_slope(_safe_div(cashneq + investments, ev.abs() + 1.0), 4), 4), 8))
def cg_f039_enterprise_value_core55_3rd_v056_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_diff(_slope(_diff(ev, 4), 4), 4), 8))
def cg_f039_enterprise_value_core56_3rd_v057_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_diff(_slope(_slope(ev, 8), 4), 4), 8))
def cg_f039_enterprise_value_core57_3rd_v058_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_diff(_slope(_z(ev, 12), 4), 4), 8))
def cg_f039_enterprise_value_core58_3rd_v059_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_diff(_slope(ev - marketcap, 4), 4), 8))
def cg_f039_enterprise_value_core59_3rd_v060_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_diff(_slope(debt - cashneq, 4), 4), 8))
def cg_f039_enterprise_value_core60_3rd_v061_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_diff(_diff(ev, 4), 4), 12))
def cg_f039_enterprise_value_core61_3rd_v062_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_diff(_diff(marketcap + debt - cashneq - investments, 4), 4), 12))
def cg_f039_enterprise_value_core62_3rd_v063_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_diff(_diff(_safe_div(ev, marketcap.abs() + 1.0), 4), 4), 12))
def cg_f039_enterprise_value_core63_3rd_v064_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_diff(_diff(_safe_div(debt, ev.abs() + 1.0), 4), 4), 12))
def cg_f039_enterprise_value_core64_3rd_v065_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_diff(_diff(_safe_div(cashneq + investments, ev.abs() + 1.0), 4), 4), 12))
def cg_f039_enterprise_value_core65_3rd_v066_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_diff(_diff(_diff(ev, 4), 4), 4), 12))
def cg_f039_enterprise_value_core66_3rd_v067_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_diff(_diff(_slope(ev, 8), 4), 4), 12))
def cg_f039_enterprise_value_core67_3rd_v068_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_diff(_diff(_z(ev, 12), 4), 4), 12))
def cg_f039_enterprise_value_core68_3rd_v069_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_diff(_diff(ev - marketcap, 4), 4), 12))
def cg_f039_enterprise_value_core69_3rd_v070_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_diff(_diff(debt - cashneq, 4), 4), 12))
def cg_f039_enterprise_value_core70_3rd_v071_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_slope(_diff(ev, 4), 8), 12))
def cg_f039_enterprise_value_core71_3rd_v072_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_slope(_diff(marketcap + debt - cashneq - investments, 4), 8), 12))
def cg_f039_enterprise_value_core72_3rd_v073_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_slope(_diff(_safe_div(ev, marketcap.abs() + 1.0), 4), 8), 12))
def cg_f039_enterprise_value_core73_3rd_v074_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_slope(_diff(_safe_div(debt, ev.abs() + 1.0), 4), 8), 12))
def cg_f039_enterprise_value_core74_3rd_v075_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_slope(_diff(_safe_div(cashneq + investments, ev.abs() + 1.0), 4), 8), 12))
def cg_f039_enterprise_value_core75_3rd_v076_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_slope(_diff(_diff(ev, 4), 4), 8), 12))
def cg_f039_enterprise_value_core76_3rd_v077_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_slope(_diff(_slope(ev, 8), 4), 8), 12))
def cg_f039_enterprise_value_core77_3rd_v078_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_slope(_diff(_z(ev, 12), 4), 8), 12))
def cg_f039_enterprise_value_core78_3rd_v079_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_slope(_diff(ev - marketcap, 4), 8), 12))
def cg_f039_enterprise_value_core79_3rd_v080_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_slope(_diff(debt - cashneq, 4), 8), 12))
def cg_f039_enterprise_value_core80_3rd_v081_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_diff(_slope(ev, 4), 4), 12))
def cg_f039_enterprise_value_core81_3rd_v082_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_diff(_slope(marketcap + debt - cashneq - investments, 4), 4), 12))
def cg_f039_enterprise_value_core82_3rd_v083_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_diff(_slope(_safe_div(ev, marketcap.abs() + 1.0), 4), 4), 12))
def cg_f039_enterprise_value_core83_3rd_v084_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_diff(_slope(_safe_div(debt, ev.abs() + 1.0), 4), 4), 12))
def cg_f039_enterprise_value_core84_3rd_v085_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_diff(_slope(_safe_div(cashneq + investments, ev.abs() + 1.0), 4), 4), 12))
def cg_f039_enterprise_value_core85_3rd_v086_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_diff(_slope(_diff(ev, 4), 4), 4), 12))
def cg_f039_enterprise_value_core86_3rd_v087_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_diff(_slope(_slope(ev, 8), 4), 4), 12))
def cg_f039_enterprise_value_core87_3rd_v088_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_diff(_slope(_z(ev, 12), 4), 4), 12))
def cg_f039_enterprise_value_core88_3rd_v089_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_diff(_slope(ev - marketcap, 4), 4), 12))
def cg_f039_enterprise_value_core89_3rd_v090_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_rank(_diff(_slope(debt - cashneq, 4), 4), 12))
def cg_f039_enterprise_value_core90_3rd_v091_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_diff(_diff(ev, 4), 4), 4))
def cg_f039_enterprise_value_core91_3rd_v092_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_diff(_diff(marketcap + debt - cashneq - investments, 4), 4), 4))
def cg_f039_enterprise_value_core92_3rd_v093_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_diff(_diff(_safe_div(ev, marketcap.abs() + 1.0), 4), 4), 4))
def cg_f039_enterprise_value_core93_3rd_v094_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_diff(_diff(_safe_div(debt, ev.abs() + 1.0), 4), 4), 4))
def cg_f039_enterprise_value_core94_3rd_v095_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_diff(_diff(_safe_div(cashneq + investments, ev.abs() + 1.0), 4), 4), 4))
def cg_f039_enterprise_value_core95_3rd_v096_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_diff(_diff(_diff(ev, 4), 4), 4), 4))
def cg_f039_enterprise_value_core96_3rd_v097_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_diff(_diff(_slope(ev, 8), 4), 4), 4))
def cg_f039_enterprise_value_core97_3rd_v098_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_diff(_diff(_z(ev, 12), 4), 4), 4))
def cg_f039_enterprise_value_core98_3rd_v099_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_diff(_diff(ev - marketcap, 4), 4), 4))
def cg_f039_enterprise_value_core99_3rd_v100_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_diff(_diff(debt - cashneq, 4), 4), 4))
def cg_f039_enterprise_value_core100_3rd_v101_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_slope(_diff(ev, 4), 8), 4))
def cg_f039_enterprise_value_core101_3rd_v102_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_slope(_diff(marketcap + debt - cashneq - investments, 4), 8), 4))
def cg_f039_enterprise_value_core102_3rd_v103_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_slope(_diff(_safe_div(ev, marketcap.abs() + 1.0), 4), 8), 4))
def cg_f039_enterprise_value_core103_3rd_v104_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_slope(_diff(_safe_div(debt, ev.abs() + 1.0), 4), 8), 4))
def cg_f039_enterprise_value_core104_3rd_v105_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_slope(_diff(_safe_div(cashneq + investments, ev.abs() + 1.0), 4), 8), 4))
def cg_f039_enterprise_value_core105_3rd_v106_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_slope(_diff(_diff(ev, 4), 4), 8), 4))
def cg_f039_enterprise_value_core106_3rd_v107_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_slope(_diff(_slope(ev, 8), 4), 8), 4))
def cg_f039_enterprise_value_core107_3rd_v108_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_slope(_diff(_z(ev, 12), 4), 8), 4))
def cg_f039_enterprise_value_core108_3rd_v109_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_slope(_diff(ev - marketcap, 4), 8), 4))
def cg_f039_enterprise_value_core109_3rd_v110_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_slope(_diff(debt - cashneq, 4), 8), 4))
def cg_f039_enterprise_value_core110_3rd_v111_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_diff(_slope(ev, 4), 4), 4))
def cg_f039_enterprise_value_core111_3rd_v112_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_diff(_slope(marketcap + debt - cashneq - investments, 4), 4), 4))
def cg_f039_enterprise_value_core112_3rd_v113_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_diff(_slope(_safe_div(ev, marketcap.abs() + 1.0), 4), 4), 4))
def cg_f039_enterprise_value_core113_3rd_v114_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_diff(_slope(_safe_div(debt, ev.abs() + 1.0), 4), 4), 4))
def cg_f039_enterprise_value_core114_3rd_v115_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_diff(_slope(_safe_div(cashneq + investments, ev.abs() + 1.0), 4), 4), 4))
def cg_f039_enterprise_value_core115_3rd_v116_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_diff(_slope(_diff(ev, 4), 4), 4), 4))
def cg_f039_enterprise_value_core116_3rd_v117_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_diff(_slope(_slope(ev, 8), 4), 4), 4))
def cg_f039_enterprise_value_core117_3rd_v118_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_diff(_slope(_z(ev, 12), 4), 4), 4))
def cg_f039_enterprise_value_core118_3rd_v119_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_diff(_slope(ev - marketcap, 4), 4), 4))
def cg_f039_enterprise_value_core119_3rd_v120_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_mean(_diff(_slope(debt - cashneq, 4), 4), 4))
def cg_f039_enterprise_value_core120_3rd_v121_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_diff(_diff(ev, 4), 4), 4))
def cg_f039_enterprise_value_core121_3rd_v122_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_diff(_diff(marketcap + debt - cashneq - investments, 4), 4), 4))
def cg_f039_enterprise_value_core122_3rd_v123_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_diff(_diff(_safe_div(ev, marketcap.abs() + 1.0), 4), 4), 4))
def cg_f039_enterprise_value_core123_3rd_v124_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_diff(_diff(_safe_div(debt, ev.abs() + 1.0), 4), 4), 4))
def cg_f039_enterprise_value_core124_3rd_v125_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_diff(_diff(_safe_div(cashneq + investments, ev.abs() + 1.0), 4), 4), 4))
def cg_f039_enterprise_value_core125_3rd_v126_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_diff(_diff(_diff(ev, 4), 4), 4), 4))
def cg_f039_enterprise_value_core126_3rd_v127_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_diff(_diff(_slope(ev, 8), 4), 4), 4))
def cg_f039_enterprise_value_core127_3rd_v128_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_diff(_diff(_z(ev, 12), 4), 4), 4))
def cg_f039_enterprise_value_core128_3rd_v129_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_diff(_diff(ev - marketcap, 4), 4), 4))
def cg_f039_enterprise_value_core129_3rd_v130_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_slope(_diff(_diff(debt - cashneq, 4), 4), 4))
def cg_f039_enterprise_value_core130_3rd_v131_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_diff(_diff(ev, 4), 4), 4))
def cg_f039_enterprise_value_core131_3rd_v132_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_diff(_diff(marketcap + debt - cashneq - investments, 4), 4), 4))
def cg_f039_enterprise_value_core132_3rd_v133_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_diff(_diff(_safe_div(ev, marketcap.abs() + 1.0), 4), 4), 4))
def cg_f039_enterprise_value_core133_3rd_v134_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_diff(_diff(_safe_div(debt, ev.abs() + 1.0), 4), 4), 4))
def cg_f039_enterprise_value_core134_3rd_v135_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_diff(_diff(_safe_div(cashneq + investments, ev.abs() + 1.0), 4), 4), 4))
def cg_f039_enterprise_value_core135_3rd_v136_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_diff(_diff(_diff(ev, 4), 4), 4), 4))
def cg_f039_enterprise_value_core136_3rd_v137_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_diff(_diff(_slope(ev, 8), 4), 4), 4))
def cg_f039_enterprise_value_core137_3rd_v138_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_diff(_diff(_z(ev, 12), 4), 4), 4))
def cg_f039_enterprise_value_core138_3rd_v139_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_diff(_diff(ev - marketcap, 4), 4), 4))
def cg_f039_enterprise_value_core139_3rd_v140_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_diff(_diff(_diff(debt - cashneq, 4), 4), 4))
def cg_f039_enterprise_value_core140_3rd_v141_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_slope(_diff(_diff(ev, 4), 4), 4), 8))
def cg_f039_enterprise_value_core141_3rd_v142_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_slope(_diff(_diff(marketcap + debt - cashneq - investments, 4), 4), 4), 8))
def cg_f039_enterprise_value_core142_3rd_v143_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_slope(_diff(_diff(_safe_div(ev, marketcap.abs() + 1.0), 4), 4), 4), 8))
def cg_f039_enterprise_value_core143_3rd_v144_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_slope(_diff(_diff(_safe_div(debt, ev.abs() + 1.0), 4), 4), 4), 8))
def cg_f039_enterprise_value_core144_3rd_v145_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_slope(_diff(_diff(_safe_div(cashneq + investments, ev.abs() + 1.0), 4), 4), 4), 8))
def cg_f039_enterprise_value_core145_3rd_v146_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_slope(_diff(_diff(_diff(ev, 4), 4), 4), 4), 8))
def cg_f039_enterprise_value_core146_3rd_v147_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_slope(_diff(_diff(_slope(ev, 8), 4), 4), 4), 8))
def cg_f039_enterprise_value_core147_3rd_v148_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_slope(_diff(_diff(_z(ev, 12), 4), 4), 4), 8))
def cg_f039_enterprise_value_core148_3rd_v149_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_slope(_diff(_diff(ev - marketcap, 4), 4), 4), 8))
def cg_f039_enterprise_value_core149_3rd_v150_signal(ev, marketcap, cashneq, investments, debt):
    return _clean(_z(_slope(_diff(_diff(debt - cashneq, 4), 4), 4), 8))