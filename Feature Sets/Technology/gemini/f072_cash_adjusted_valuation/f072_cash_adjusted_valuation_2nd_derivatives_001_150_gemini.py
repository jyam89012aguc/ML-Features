import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f072_cash_adjusted_valuation_core00_2nd_v001_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_slope(marketcap, 4))
def cg_f072_cash_adjusted_valuation_core01_2nd_v002_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_slope(ev, 4))
def cg_f072_cash_adjusted_valuation_core02_2nd_v003_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_slope(cashneq, 4))
def cg_f072_cash_adjusted_valuation_core03_2nd_v004_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_slope(investments, 4))
def cg_f072_cash_adjusted_valuation_core04_2nd_v005_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_slope(debt, 4))
def cg_f072_cash_adjusted_valuation_core05_2nd_v006_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_slope(_safe_div(cashneq + investments, marketcap), 4))
def cg_f072_cash_adjusted_valuation_core06_2nd_v007_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_slope(_safe_div(debt, marketcap), 4))
def cg_f072_cash_adjusted_valuation_core07_2nd_v008_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_slope(ev - marketcap, 4))
def cg_f072_cash_adjusted_valuation_core08_2nd_v009_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_slope(_safe_div(cashneq, ev.abs() + 1.0), 4))
def cg_f072_cash_adjusted_valuation_core09_2nd_v010_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_slope(_safe_div(investments, ev.abs() + 1.0), 4))
def cg_f072_cash_adjusted_valuation_core10_2nd_v011_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_slope(marketcap, 8))
def cg_f072_cash_adjusted_valuation_core11_2nd_v012_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_slope(ev, 8))
def cg_f072_cash_adjusted_valuation_core12_2nd_v013_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_slope(cashneq, 8))
def cg_f072_cash_adjusted_valuation_core13_2nd_v014_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_slope(investments, 8))
def cg_f072_cash_adjusted_valuation_core14_2nd_v015_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_slope(debt, 8))
def cg_f072_cash_adjusted_valuation_core15_2nd_v016_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_slope(_safe_div(cashneq + investments, marketcap), 8))
def cg_f072_cash_adjusted_valuation_core16_2nd_v017_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_slope(_safe_div(debt, marketcap), 8))
def cg_f072_cash_adjusted_valuation_core17_2nd_v018_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_slope(ev - marketcap, 8))
def cg_f072_cash_adjusted_valuation_core18_2nd_v019_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_slope(_safe_div(cashneq, ev.abs() + 1.0), 8))
def cg_f072_cash_adjusted_valuation_core19_2nd_v020_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_slope(_safe_div(investments, ev.abs() + 1.0), 8))
def cg_f072_cash_adjusted_valuation_core20_2nd_v021_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_diff(marketcap, 4))
def cg_f072_cash_adjusted_valuation_core21_2nd_v022_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_diff(ev, 4))
def cg_f072_cash_adjusted_valuation_core22_2nd_v023_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_diff(cashneq, 4))
def cg_f072_cash_adjusted_valuation_core23_2nd_v024_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_diff(investments, 4))
def cg_f072_cash_adjusted_valuation_core24_2nd_v025_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_diff(debt, 4))
def cg_f072_cash_adjusted_valuation_core25_2nd_v026_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_diff(_safe_div(cashneq + investments, marketcap), 4))
def cg_f072_cash_adjusted_valuation_core26_2nd_v027_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_diff(_safe_div(debt, marketcap), 4))
def cg_f072_cash_adjusted_valuation_core27_2nd_v028_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_diff(ev - marketcap, 4))
def cg_f072_cash_adjusted_valuation_core28_2nd_v029_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_diff(_safe_div(cashneq, ev.abs() + 1.0), 4))
def cg_f072_cash_adjusted_valuation_core29_2nd_v030_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_diff(_safe_div(investments, ev.abs() + 1.0), 4))
def cg_f072_cash_adjusted_valuation_core30_2nd_v031_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_z(_slope(marketcap, 4), 8))
def cg_f072_cash_adjusted_valuation_core31_2nd_v032_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_z(_slope(ev, 4), 8))
def cg_f072_cash_adjusted_valuation_core32_2nd_v033_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_z(_slope(cashneq, 4), 8))
def cg_f072_cash_adjusted_valuation_core33_2nd_v034_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_z(_slope(investments, 4), 8))
def cg_f072_cash_adjusted_valuation_core34_2nd_v035_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_z(_slope(debt, 4), 8))
def cg_f072_cash_adjusted_valuation_core35_2nd_v036_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_z(_slope(_safe_div(cashneq + investments, marketcap), 4), 8))
def cg_f072_cash_adjusted_valuation_core36_2nd_v037_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_z(_slope(_safe_div(debt, marketcap), 4), 8))
def cg_f072_cash_adjusted_valuation_core37_2nd_v038_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_z(_slope(ev - marketcap, 4), 8))
def cg_f072_cash_adjusted_valuation_core38_2nd_v039_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_z(_slope(_safe_div(cashneq, ev.abs() + 1.0), 4), 8))
def cg_f072_cash_adjusted_valuation_core39_2nd_v040_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_z(_slope(_safe_div(investments, ev.abs() + 1.0), 4), 8))
def cg_f072_cash_adjusted_valuation_core40_2nd_v041_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_z(_slope(marketcap, 8), 12))
def cg_f072_cash_adjusted_valuation_core41_2nd_v042_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_z(_slope(ev, 8), 12))
def cg_f072_cash_adjusted_valuation_core42_2nd_v043_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_z(_slope(cashneq, 8), 12))
def cg_f072_cash_adjusted_valuation_core43_2nd_v044_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_z(_slope(investments, 8), 12))
def cg_f072_cash_adjusted_valuation_core44_2nd_v045_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_z(_slope(debt, 8), 12))
def cg_f072_cash_adjusted_valuation_core45_2nd_v046_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_z(_slope(_safe_div(cashneq + investments, marketcap), 8), 12))
def cg_f072_cash_adjusted_valuation_core46_2nd_v047_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_z(_slope(_safe_div(debt, marketcap), 8), 12))
def cg_f072_cash_adjusted_valuation_core47_2nd_v048_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_z(_slope(ev - marketcap, 8), 12))
def cg_f072_cash_adjusted_valuation_core48_2nd_v049_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_z(_slope(_safe_div(cashneq, ev.abs() + 1.0), 8), 12))
def cg_f072_cash_adjusted_valuation_core49_2nd_v050_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_z(_slope(_safe_div(investments, ev.abs() + 1.0), 8), 12))
def cg_f072_cash_adjusted_valuation_core50_2nd_v051_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_z(_diff(marketcap, 4), 8))
def cg_f072_cash_adjusted_valuation_core51_2nd_v052_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_z(_diff(ev, 4), 8))
def cg_f072_cash_adjusted_valuation_core52_2nd_v053_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_z(_diff(cashneq, 4), 8))
def cg_f072_cash_adjusted_valuation_core53_2nd_v054_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_z(_diff(investments, 4), 8))
def cg_f072_cash_adjusted_valuation_core54_2nd_v055_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_z(_diff(debt, 4), 8))
def cg_f072_cash_adjusted_valuation_core55_2nd_v056_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_z(_diff(_safe_div(cashneq + investments, marketcap), 4), 8))
def cg_f072_cash_adjusted_valuation_core56_2nd_v057_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_z(_diff(_safe_div(debt, marketcap), 4), 8))
def cg_f072_cash_adjusted_valuation_core57_2nd_v058_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_z(_diff(ev - marketcap, 4), 8))
def cg_f072_cash_adjusted_valuation_core58_2nd_v059_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_z(_diff(_safe_div(cashneq, ev.abs() + 1.0), 4), 8))
def cg_f072_cash_adjusted_valuation_core59_2nd_v060_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_z(_diff(_safe_div(investments, ev.abs() + 1.0), 4), 8))
def cg_f072_cash_adjusted_valuation_core60_2nd_v061_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_rank(_slope(marketcap, 4), 12))
def cg_f072_cash_adjusted_valuation_core61_2nd_v062_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_rank(_slope(ev, 4), 12))
def cg_f072_cash_adjusted_valuation_core62_2nd_v063_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_rank(_slope(cashneq, 4), 12))
def cg_f072_cash_adjusted_valuation_core63_2nd_v064_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_rank(_slope(investments, 4), 12))
def cg_f072_cash_adjusted_valuation_core64_2nd_v065_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_rank(_slope(debt, 4), 12))
def cg_f072_cash_adjusted_valuation_core65_2nd_v066_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_rank(_slope(_safe_div(cashneq + investments, marketcap), 4), 12))
def cg_f072_cash_adjusted_valuation_core66_2nd_v067_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_rank(_slope(_safe_div(debt, marketcap), 4), 12))
def cg_f072_cash_adjusted_valuation_core67_2nd_v068_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_rank(_slope(ev - marketcap, 4), 12))
def cg_f072_cash_adjusted_valuation_core68_2nd_v069_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_rank(_slope(_safe_div(cashneq, ev.abs() + 1.0), 4), 12))
def cg_f072_cash_adjusted_valuation_core69_2nd_v070_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_rank(_slope(_safe_div(investments, ev.abs() + 1.0), 4), 12))
def cg_f072_cash_adjusted_valuation_core70_2nd_v071_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_rank(_diff(marketcap, 4), 12))
def cg_f072_cash_adjusted_valuation_core71_2nd_v072_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_rank(_diff(ev, 4), 12))
def cg_f072_cash_adjusted_valuation_core72_2nd_v073_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_rank(_diff(cashneq, 4), 12))
def cg_f072_cash_adjusted_valuation_core73_2nd_v074_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_rank(_diff(investments, 4), 12))
def cg_f072_cash_adjusted_valuation_core74_2nd_v075_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_rank(_diff(debt, 4), 12))
def cg_f072_cash_adjusted_valuation_core75_2nd_v076_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_rank(_diff(_safe_div(cashneq + investments, marketcap), 4), 12))
def cg_f072_cash_adjusted_valuation_core76_2nd_v077_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_rank(_diff(_safe_div(debt, marketcap), 4), 12))
def cg_f072_cash_adjusted_valuation_core77_2nd_v078_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_rank(_diff(ev - marketcap, 4), 12))
def cg_f072_cash_adjusted_valuation_core78_2nd_v079_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_rank(_diff(_safe_div(cashneq, ev.abs() + 1.0), 4), 12))
def cg_f072_cash_adjusted_valuation_core79_2nd_v080_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_rank(_diff(_safe_div(investments, ev.abs() + 1.0), 4), 12))
def cg_f072_cash_adjusted_valuation_core80_2nd_v081_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_mean(_slope(marketcap, 4), 4))
def cg_f072_cash_adjusted_valuation_core81_2nd_v082_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_mean(_slope(ev, 4), 4))
def cg_f072_cash_adjusted_valuation_core82_2nd_v083_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_mean(_slope(cashneq, 4), 4))
def cg_f072_cash_adjusted_valuation_core83_2nd_v084_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_mean(_slope(investments, 4), 4))
def cg_f072_cash_adjusted_valuation_core84_2nd_v085_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_mean(_slope(debt, 4), 4))
def cg_f072_cash_adjusted_valuation_core85_2nd_v086_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_mean(_slope(_safe_div(cashneq + investments, marketcap), 4), 4))
def cg_f072_cash_adjusted_valuation_core86_2nd_v087_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_mean(_slope(_safe_div(debt, marketcap), 4), 4))
def cg_f072_cash_adjusted_valuation_core87_2nd_v088_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_mean(_slope(ev - marketcap, 4), 4))
def cg_f072_cash_adjusted_valuation_core88_2nd_v089_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_mean(_slope(_safe_div(cashneq, ev.abs() + 1.0), 4), 4))
def cg_f072_cash_adjusted_valuation_core89_2nd_v090_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_mean(_slope(_safe_div(investments, ev.abs() + 1.0), 4), 4))
def cg_f072_cash_adjusted_valuation_core90_2nd_v091_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_mean(_diff(marketcap, 4), 4))
def cg_f072_cash_adjusted_valuation_core91_2nd_v092_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_mean(_diff(ev, 4), 4))
def cg_f072_cash_adjusted_valuation_core92_2nd_v093_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_mean(_diff(cashneq, 4), 4))
def cg_f072_cash_adjusted_valuation_core93_2nd_v094_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_mean(_diff(investments, 4), 4))
def cg_f072_cash_adjusted_valuation_core94_2nd_v095_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_mean(_diff(debt, 4), 4))
def cg_f072_cash_adjusted_valuation_core95_2nd_v096_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_mean(_diff(_safe_div(cashneq + investments, marketcap), 4), 4))
def cg_f072_cash_adjusted_valuation_core96_2nd_v097_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_mean(_diff(_safe_div(debt, marketcap), 4), 4))
def cg_f072_cash_adjusted_valuation_core97_2nd_v098_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_mean(_diff(ev - marketcap, 4), 4))
def cg_f072_cash_adjusted_valuation_core98_2nd_v099_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_mean(_diff(_safe_div(cashneq, ev.abs() + 1.0), 4), 4))
def cg_f072_cash_adjusted_valuation_core99_2nd_v100_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_mean(_diff(_safe_div(investments, ev.abs() + 1.0), 4), 4))
def cg_f072_cash_adjusted_valuation_core100_2nd_v101_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_slope(_mean(marketcap, 4), 4))
def cg_f072_cash_adjusted_valuation_core101_2nd_v102_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_slope(_mean(ev, 4), 4))
def cg_f072_cash_adjusted_valuation_core102_2nd_v103_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_slope(_mean(cashneq, 4), 4))
def cg_f072_cash_adjusted_valuation_core103_2nd_v104_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_slope(_mean(investments, 4), 4))
def cg_f072_cash_adjusted_valuation_core104_2nd_v105_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_slope(_mean(debt, 4), 4))
def cg_f072_cash_adjusted_valuation_core105_2nd_v106_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_slope(_mean(_safe_div(cashneq + investments, marketcap), 4), 4))
def cg_f072_cash_adjusted_valuation_core106_2nd_v107_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_slope(_mean(_safe_div(debt, marketcap), 4), 4))
def cg_f072_cash_adjusted_valuation_core107_2nd_v108_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_slope(_mean(ev - marketcap, 4), 4))
def cg_f072_cash_adjusted_valuation_core108_2nd_v109_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_slope(_mean(_safe_div(cashneq, ev.abs() + 1.0), 4), 4))
def cg_f072_cash_adjusted_valuation_core109_2nd_v110_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_slope(_mean(_safe_div(investments, ev.abs() + 1.0), 4), 4))
def cg_f072_cash_adjusted_valuation_core110_2nd_v111_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_slope(_mean(marketcap, 8), 8))
def cg_f072_cash_adjusted_valuation_core111_2nd_v112_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_slope(_mean(ev, 8), 8))
def cg_f072_cash_adjusted_valuation_core112_2nd_v113_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_slope(_mean(cashneq, 8), 8))
def cg_f072_cash_adjusted_valuation_core113_2nd_v114_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_slope(_mean(investments, 8), 8))
def cg_f072_cash_adjusted_valuation_core114_2nd_v115_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_slope(_mean(debt, 8), 8))
def cg_f072_cash_adjusted_valuation_core115_2nd_v116_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_slope(_mean(_safe_div(cashneq + investments, marketcap), 8), 8))
def cg_f072_cash_adjusted_valuation_core116_2nd_v117_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_slope(_mean(_safe_div(debt, marketcap), 8), 8))
def cg_f072_cash_adjusted_valuation_core117_2nd_v118_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_slope(_mean(ev - marketcap, 8), 8))
def cg_f072_cash_adjusted_valuation_core118_2nd_v119_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_slope(_mean(_safe_div(cashneq, ev.abs() + 1.0), 8), 8))
def cg_f072_cash_adjusted_valuation_core119_2nd_v120_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_slope(_mean(_safe_div(investments, ev.abs() + 1.0), 8), 8))
def cg_f072_cash_adjusted_valuation_core120_2nd_v121_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_diff(_mean(marketcap, 4), 4))
def cg_f072_cash_adjusted_valuation_core121_2nd_v122_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_diff(_mean(ev, 4), 4))
def cg_f072_cash_adjusted_valuation_core122_2nd_v123_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_diff(_mean(cashneq, 4), 4))
def cg_f072_cash_adjusted_valuation_core123_2nd_v124_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_diff(_mean(investments, 4), 4))
def cg_f072_cash_adjusted_valuation_core124_2nd_v125_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_diff(_mean(debt, 4), 4))
def cg_f072_cash_adjusted_valuation_core125_2nd_v126_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_diff(_mean(_safe_div(cashneq + investments, marketcap), 4), 4))
def cg_f072_cash_adjusted_valuation_core126_2nd_v127_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_diff(_mean(_safe_div(debt, marketcap), 4), 4))
def cg_f072_cash_adjusted_valuation_core127_2nd_v128_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_diff(_mean(ev - marketcap, 4), 4))
def cg_f072_cash_adjusted_valuation_core128_2nd_v129_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_diff(_mean(_safe_div(cashneq, ev.abs() + 1.0), 4), 4))
def cg_f072_cash_adjusted_valuation_core129_2nd_v130_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_diff(_mean(_safe_div(investments, ev.abs() + 1.0), 4), 4))
def cg_f072_cash_adjusted_valuation_core130_2nd_v131_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_z(_diff(_mean(marketcap, 4), 4), 8))
def cg_f072_cash_adjusted_valuation_core131_2nd_v132_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_z(_diff(_mean(ev, 4), 4), 8))
def cg_f072_cash_adjusted_valuation_core132_2nd_v133_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_z(_diff(_mean(cashneq, 4), 4), 8))
def cg_f072_cash_adjusted_valuation_core133_2nd_v134_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_z(_diff(_mean(investments, 4), 4), 8))
def cg_f072_cash_adjusted_valuation_core134_2nd_v135_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_z(_diff(_mean(debt, 4), 4), 8))
def cg_f072_cash_adjusted_valuation_core135_2nd_v136_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_z(_diff(_mean(_safe_div(cashneq + investments, marketcap), 4), 4), 8))
def cg_f072_cash_adjusted_valuation_core136_2nd_v137_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_z(_diff(_mean(_safe_div(debt, marketcap), 4), 4), 8))
def cg_f072_cash_adjusted_valuation_core137_2nd_v138_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_z(_diff(_mean(ev - marketcap, 4), 4), 8))
def cg_f072_cash_adjusted_valuation_core138_2nd_v139_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_z(_diff(_mean(_safe_div(cashneq, ev.abs() + 1.0), 4), 4), 8))
def cg_f072_cash_adjusted_valuation_core139_2nd_v140_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_z(_diff(_mean(_safe_div(investments, ev.abs() + 1.0), 4), 4), 8))
def cg_f072_cash_adjusted_valuation_core140_2nd_v141_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_rank(_slope(_mean(marketcap, 4), 4), 12))
def cg_f072_cash_adjusted_valuation_core141_2nd_v142_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_rank(_slope(_mean(ev, 4), 4), 12))
def cg_f072_cash_adjusted_valuation_core142_2nd_v143_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_rank(_slope(_mean(cashneq, 4), 4), 12))
def cg_f072_cash_adjusted_valuation_core143_2nd_v144_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_rank(_slope(_mean(investments, 4), 4), 12))
def cg_f072_cash_adjusted_valuation_core144_2nd_v145_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_rank(_slope(_mean(debt, 4), 4), 12))
def cg_f072_cash_adjusted_valuation_core145_2nd_v146_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_rank(_slope(_mean(_safe_div(cashneq + investments, marketcap), 4), 4), 12))
def cg_f072_cash_adjusted_valuation_core146_2nd_v147_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_rank(_slope(_mean(_safe_div(debt, marketcap), 4), 4), 12))
def cg_f072_cash_adjusted_valuation_core147_2nd_v148_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_rank(_slope(_mean(ev - marketcap, 4), 4), 12))
def cg_f072_cash_adjusted_valuation_core148_2nd_v149_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_rank(_slope(_mean(_safe_div(cashneq, ev.abs() + 1.0), 4), 4), 12))
def cg_f072_cash_adjusted_valuation_core149_2nd_v150_signal(marketcap, ev, cashneq, investments, debt):
    return _clean(_rank(_slope(_mean(_safe_div(investments, ev.abs() + 1.0), 4), 4), 12))