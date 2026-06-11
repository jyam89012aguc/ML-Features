import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f001_cash_and_equivalents_core00_2nd_v001_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(cashneq, 4))
def cg_f001_cash_and_equivalents_core01_2nd_v002_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_safe_div(cashneq, assets), 4))
def cg_f001_cash_and_equivalents_core02_2nd_v003_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_safe_div(cashneq, marketcap), 4))
def cg_f001_cash_and_equivalents_core03_2nd_v004_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_safe_div(cashneq, revenue), 4))
def cg_f001_cash_and_equivalents_core04_2nd_v005_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_safe_div(cashneq, liabilities), 4))
def cg_f001_cash_and_equivalents_core05_2nd_v006_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_safe_div(cashneq, debt), 4))
def cg_f001_cash_and_equivalents_core06_2nd_v007_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_safe_div(cashneq, sharesbas), 4))
def cg_f001_cash_and_equivalents_core07_2nd_v008_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_safe_div(cashneq, capex.abs() + 1.0), 4))
def cg_f001_cash_and_equivalents_core08_2nd_v009_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_safe_div(cashneq, rnd.abs() + 1.0), 4))
def cg_f001_cash_and_equivalents_core09_2nd_v010_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_safe_div(cashneq, opex.abs() + 1.0), 4))

def cg_f001_cash_and_equivalents_core10_2nd_v011_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(cashneq, 8))
def cg_f001_cash_and_equivalents_core11_2nd_v012_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_safe_div(cashneq, assets), 8))
def cg_f001_cash_and_equivalents_core12_2nd_v013_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_safe_div(cashneq, marketcap), 8))
def cg_f001_cash_and_equivalents_core13_2nd_v014_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_safe_div(cashneq, revenue), 8))
def cg_f001_cash_and_equivalents_core14_2nd_v015_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_safe_div(cashneq, liabilities), 8))
def cg_f001_cash_and_equivalents_core15_2nd_v016_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_safe_div(cashneq, debt), 8))
def cg_f001_cash_and_equivalents_core16_2nd_v017_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_safe_div(cashneq, sharesbas), 8))
def cg_f001_cash_and_equivalents_core17_2nd_v018_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_safe_div(cashneq, capex.abs() + 1.0), 8))
def cg_f001_cash_and_equivalents_core18_2nd_v019_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_safe_div(cashneq, rnd.abs() + 1.0), 8))
def cg_f001_cash_and_equivalents_core19_2nd_v020_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_safe_div(cashneq, opex.abs() + 1.0), 8))

def cg_f001_cash_and_equivalents_core20_2nd_v021_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(cashneq, 4))
def cg_f001_cash_and_equivalents_core21_2nd_v022_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_safe_div(cashneq, assets), 4))
def cg_f001_cash_and_equivalents_core22_2nd_v023_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_safe_div(cashneq, marketcap), 4))
def cg_f001_cash_and_equivalents_core23_2nd_v024_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_safe_div(cashneq, revenue), 4))
def cg_f001_cash_and_equivalents_core24_2nd_v025_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_safe_div(cashneq, liabilities), 4))
def cg_f001_cash_and_equivalents_core25_2nd_v026_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_safe_div(cashneq, debt), 4))
def cg_f001_cash_and_equivalents_core26_2nd_v027_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_safe_div(cashneq, sharesbas), 4))
def cg_f001_cash_and_equivalents_core27_2nd_v028_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_safe_div(cashneq, capex.abs() + 1.0), 4))
def cg_f001_cash_and_equivalents_core28_2nd_v029_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_safe_div(cashneq, rnd.abs() + 1.0), 4))
def cg_f001_cash_and_equivalents_core29_2nd_v030_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_safe_div(cashneq, opex.abs() + 1.0), 4))

def cg_f001_cash_and_equivalents_core30_2nd_v031_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_slope(cashneq, 4), 8))
def cg_f001_cash_and_equivalents_core31_2nd_v032_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_slope(_safe_div(cashneq, assets), 4), 8))
def cg_f001_cash_and_equivalents_core32_2nd_v033_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_slope(_safe_div(cashneq, marketcap), 4), 8))
def cg_f001_cash_and_equivalents_core33_2nd_v034_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_slope(_safe_div(cashneq, revenue), 4), 8))
def cg_f001_cash_and_equivalents_core34_2nd_v035_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_slope(_safe_div(cashneq, liabilities), 4), 8))
def cg_f001_cash_and_equivalents_core35_2nd_v036_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_slope(_safe_div(cashneq, debt), 4), 8))
def cg_f001_cash_and_equivalents_core36_2nd_v037_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_slope(_safe_div(cashneq, sharesbas), 4), 8))
def cg_f001_cash_and_equivalents_core37_2nd_v038_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_slope(_safe_div(cashneq, capex.abs() + 1.0), 4), 8))
def cg_f001_cash_and_equivalents_core38_2nd_v039_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_slope(_safe_div(cashneq, rnd.abs() + 1.0), 4), 8))
def cg_f001_cash_and_equivalents_core39_2nd_v040_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_slope(_safe_div(cashneq, opex.abs() + 1.0), 4), 8))

def cg_f001_cash_and_equivalents_core40_2nd_v041_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_slope(cashneq, 8), 12))
def cg_f001_cash_and_equivalents_core41_2nd_v042_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_slope(_safe_div(cashneq, assets), 8), 12))
def cg_f001_cash_and_equivalents_core42_2nd_v043_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_slope(_safe_div(cashneq, marketcap), 8), 12))
def cg_f001_cash_and_equivalents_core43_2nd_v044_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_slope(_safe_div(cashneq, revenue), 8), 12))
def cg_f001_cash_and_equivalents_core44_2nd_v045_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_slope(_safe_div(cashneq, liabilities), 8), 12))
def cg_f001_cash_and_equivalents_core45_2nd_v046_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_slope(_safe_div(cashneq, debt), 8), 12))
def cg_f001_cash_and_equivalents_core46_2nd_v047_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_slope(_safe_div(cashneq, sharesbas), 8), 12))
def cg_f001_cash_and_equivalents_core47_2nd_v048_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_slope(_safe_div(cashneq, capex.abs() + 1.0), 8), 12))
def cg_f001_cash_and_equivalents_core48_2nd_v049_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_slope(_safe_div(cashneq, rnd.abs() + 1.0), 8), 12))
def cg_f001_cash_and_equivalents_core49_2nd_v050_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_slope(_safe_div(cashneq, opex.abs() + 1.0), 8), 12))

def cg_f001_cash_and_equivalents_core50_2nd_v051_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_diff(cashneq, 4), 8))
def cg_f001_cash_and_equivalents_core51_2nd_v052_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_diff(_safe_div(cashneq, assets), 4), 8))
def cg_f001_cash_and_equivalents_core52_2nd_v053_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_diff(_safe_div(cashneq, marketcap), 4), 8))
def cg_f001_cash_and_equivalents_core53_2nd_v054_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_diff(_safe_div(cashneq, revenue), 4), 8))
def cg_f001_cash_and_equivalents_core54_2nd_v055_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_diff(_safe_div(cashneq, liabilities), 4), 8))
def cg_f001_cash_and_equivalents_core55_2nd_v056_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_diff(_safe_div(cashneq, debt), 4), 8))
def cg_f001_cash_and_equivalents_core56_2nd_v057_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_diff(_safe_div(cashneq, sharesbas), 4), 8))
def cg_f001_cash_and_equivalents_core57_2nd_v058_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_diff(_safe_div(cashneq, capex.abs() + 1.0), 4), 8))
def cg_f001_cash_and_equivalents_core58_2nd_v059_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_diff(_safe_div(cashneq, rnd.abs() + 1.0), 4), 8))
def cg_f001_cash_and_equivalents_core59_2nd_v060_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_diff(_safe_div(cashneq, opex.abs() + 1.0), 4), 8))

def cg_f001_cash_and_equivalents_core60_2nd_v061_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_slope(cashneq, 4), 12))
def cg_f001_cash_and_equivalents_core61_2nd_v062_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_slope(_safe_div(cashneq, assets), 4), 12))
def cg_f001_cash_and_equivalents_core62_2nd_v063_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_slope(_safe_div(cashneq, marketcap), 4), 12))
def cg_f001_cash_and_equivalents_core63_2nd_v064_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_slope(_safe_div(cashneq, revenue), 4), 12))
def cg_f001_cash_and_equivalents_core64_2nd_v065_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_slope(_safe_div(cashneq, liabilities), 4), 12))
def cg_f001_cash_and_equivalents_core65_2nd_v066_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_slope(_safe_div(cashneq, debt), 4), 12))
def cg_f001_cash_and_equivalents_core66_2nd_v067_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_slope(_safe_div(cashneq, sharesbas), 4), 12))
def cg_f001_cash_and_equivalents_core67_2nd_v068_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_slope(_safe_div(cashneq, capex.abs() + 1.0), 4), 12))
def cg_f001_cash_and_equivalents_core68_2nd_v069_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_slope(_safe_div(cashneq, rnd.abs() + 1.0), 4), 12))
def cg_f001_cash_and_equivalents_core69_2nd_v070_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_slope(_safe_div(cashneq, opex.abs() + 1.0), 4), 12))

def cg_f001_cash_and_equivalents_core70_2nd_v071_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_diff(cashneq, 4), 12))
def cg_f001_cash_and_equivalents_core71_2nd_v072_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_diff(_safe_div(cashneq, assets), 4), 12))
def cg_f001_cash_and_equivalents_core72_2nd_v073_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_diff(_safe_div(cashneq, marketcap), 4), 12))
def cg_f001_cash_and_equivalents_core73_2nd_v074_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_diff(_safe_div(cashneq, revenue), 4), 12))
def cg_f001_cash_and_equivalents_core74_2nd_v075_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_diff(_safe_div(cashneq, liabilities), 4), 12))
def cg_f001_cash_and_equivalents_core75_2nd_v076_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_diff(_safe_div(cashneq, debt), 4), 12))
def cg_f001_cash_and_equivalents_core76_2nd_v077_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_diff(_safe_div(cashneq, sharesbas), 4), 12))
def cg_f001_cash_and_equivalents_core77_2nd_v078_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_diff(_safe_div(cashneq, capex.abs() + 1.0), 4), 12))
def cg_f001_cash_and_equivalents_core78_2nd_v079_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_diff(_safe_div(cashneq, rnd.abs() + 1.0), 4), 12))
def cg_f001_cash_and_equivalents_core79_2nd_v080_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_diff(_safe_div(cashneq, opex.abs() + 1.0), 4), 12))

def cg_f001_cash_and_equivalents_core80_2nd_v081_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_slope(cashneq, 4), 4))
def cg_f001_cash_and_equivalents_core81_2nd_v082_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_slope(_safe_div(cashneq, assets), 4), 4))
def cg_f001_cash_and_equivalents_core82_2nd_v083_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_slope(_safe_div(cashneq, marketcap), 4), 4))
def cg_f001_cash_and_equivalents_core83_2nd_v084_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_slope(_safe_div(cashneq, revenue), 4), 4))
def cg_f001_cash_and_equivalents_core84_2nd_v085_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_slope(_safe_div(cashneq, liabilities), 4), 4))
def cg_f001_cash_and_equivalents_core85_2nd_v086_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_slope(_safe_div(cashneq, debt), 4), 4))
def cg_f001_cash_and_equivalents_core86_2nd_v087_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_slope(_safe_div(cashneq, sharesbas), 4), 4))
def cg_f001_cash_and_equivalents_core87_2nd_v088_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_slope(_safe_div(cashneq, capex.abs() + 1.0), 4), 4))
def cg_f001_cash_and_equivalents_core88_2nd_v089_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_slope(_safe_div(cashneq, rnd.abs() + 1.0), 4), 4))
def cg_f001_cash_and_equivalents_core89_2nd_v090_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_slope(_safe_div(cashneq, opex.abs() + 1.0), 4), 4))

def cg_f001_cash_and_equivalents_core90_2nd_v091_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_diff(cashneq, 4), 4))
def cg_f001_cash_and_equivalents_core91_2nd_v092_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_diff(_safe_div(cashneq, assets), 4), 4))
def cg_f001_cash_and_equivalents_core92_2nd_v093_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_diff(_safe_div(cashneq, marketcap), 4), 4))
def cg_f001_cash_and_equivalents_core93_2nd_v094_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_diff(_safe_div(cashneq, revenue), 4), 4))
def cg_f001_cash_and_equivalents_core94_2nd_v095_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_diff(_safe_div(cashneq, liabilities), 4), 4))
def cg_f001_cash_and_equivalents_core95_2nd_v096_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_diff(_safe_div(cashneq, debt), 4), 4))
def cg_f001_cash_and_equivalents_core96_2nd_v097_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_diff(_safe_div(cashneq, sharesbas), 4), 4))
def cg_f001_cash_and_equivalents_core97_2nd_v098_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_diff(_safe_div(cashneq, capex.abs() + 1.0), 4), 4))
def cg_f001_cash_and_equivalents_core98_2nd_v099_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_diff(_safe_div(cashneq, rnd.abs() + 1.0), 4), 4))
def cg_f001_cash_and_equivalents_core99_2nd_v100_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_diff(_safe_div(cashneq, opex.abs() + 1.0), 4), 4))

def cg_f001_cash_and_equivalents_core100_2nd_v101_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_mean(cashneq, 4), 4))
def cg_f001_cash_and_equivalents_core101_2nd_v102_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_mean(_safe_div(cashneq, assets), 4), 4))
def cg_f001_cash_and_equivalents_core102_2nd_v103_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_mean(_safe_div(cashneq, marketcap), 4), 4))
def cg_f001_cash_and_equivalents_core103_2nd_v104_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_mean(_safe_div(cashneq, revenue), 4), 4))
def cg_f001_cash_and_equivalents_core104_2nd_v105_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_mean(_safe_div(cashneq, liabilities), 4), 4))
def cg_f001_cash_and_equivalents_core105_2nd_v106_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_mean(_safe_div(cashneq, debt), 4), 4))
def cg_f001_cash_and_equivalents_core106_2nd_v107_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_mean(_safe_div(cashneq, sharesbas), 4), 4))
def cg_f001_cash_and_equivalents_core107_2nd_v108_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_mean(_safe_div(cashneq, capex.abs() + 1.0), 4), 4))
def cg_f001_cash_and_equivalents_core108_2nd_v109_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_mean(_safe_div(cashneq, rnd.abs() + 1.0), 4), 4))
def cg_f001_cash_and_equivalents_core109_2nd_v110_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_mean(_safe_div(cashneq, opex.abs() + 1.0), 4), 4))

def cg_f001_cash_and_equivalents_core110_2nd_v111_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_mean(cashneq, 8), 8))
def cg_f001_cash_and_equivalents_core111_2nd_v112_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_mean(_safe_div(cashneq, assets), 8), 8))
def cg_f001_cash_and_equivalents_core112_2nd_v113_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_mean(_safe_div(cashneq, marketcap), 8), 8))
def cg_f001_cash_and_equivalents_core113_2nd_v114_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_mean(_safe_div(cashneq, revenue), 8), 8))
def cg_f001_cash_and_equivalents_core114_2nd_v115_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_mean(_safe_div(cashneq, liabilities), 8), 8))
def cg_f001_cash_and_equivalents_core115_2nd_v116_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_mean(_safe_div(cashneq, debt), 8), 8))
def cg_f001_cash_and_equivalents_core116_2nd_v117_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_mean(_safe_div(cashneq, sharesbas), 8), 8))
def cg_f001_cash_and_equivalents_core117_2nd_v118_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_mean(_safe_div(cashneq, capex.abs() + 1.0), 8), 8))
def cg_f001_cash_and_equivalents_core118_2nd_v119_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_mean(_safe_div(cashneq, rnd.abs() + 1.0), 8), 8))
def cg_f001_cash_and_equivalents_core119_2nd_v120_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_mean(_safe_div(cashneq, opex.abs() + 1.0), 8), 8))

def cg_f001_cash_and_equivalents_core120_2nd_v121_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_mean(cashneq, 4), 4))
def cg_f001_cash_and_equivalents_core121_2nd_v122_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_mean(_safe_div(cashneq, assets), 4), 4))
def cg_f001_cash_and_equivalents_core122_2nd_v123_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_mean(_safe_div(cashneq, marketcap), 4), 4))
def cg_f001_cash_and_equivalents_core123_2nd_v124_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_mean(_safe_div(cashneq, revenue), 4), 4))
def cg_f001_cash_and_equivalents_core124_2nd_v125_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_mean(_safe_div(cashneq, liabilities), 4), 4))
def cg_f001_cash_and_equivalents_core125_2nd_v126_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_mean(_safe_div(cashneq, debt), 4), 4))
def cg_f001_cash_and_equivalents_core126_2nd_v127_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_mean(_safe_div(cashneq, sharesbas), 4), 4))
def cg_f001_cash_and_equivalents_core127_2nd_v128_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_mean(_safe_div(cashneq, capex.abs() + 1.0), 4), 4))
def cg_f001_cash_and_equivalents_core128_2nd_v129_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_mean(_safe_div(cashneq, rnd.abs() + 1.0), 4), 4))
def cg_f001_cash_and_equivalents_core129_2nd_v130_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_mean(_safe_div(cashneq, opex.abs() + 1.0), 4), 4))

def cg_f001_cash_and_equivalents_core130_2nd_v131_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_diff(_mean(cashneq, 4), 4), 8))
def cg_f001_cash_and_equivalents_core131_2nd_v132_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_diff(_mean(_safe_div(cashneq, assets), 4), 4), 8))
def cg_f001_cash_and_equivalents_core132_2nd_v133_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_diff(_mean(_safe_div(cashneq, marketcap), 4), 4), 8))
def cg_f001_cash_and_equivalents_core133_2nd_v134_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_diff(_mean(_safe_div(cashneq, revenue), 4), 4), 8))
def cg_f001_cash_and_equivalents_core134_2nd_v135_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_diff(_mean(_safe_div(cashneq, liabilities), 4), 4), 8))
def cg_f001_cash_and_equivalents_core135_2nd_v136_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_diff(_mean(_safe_div(cashneq, debt), 4), 4), 8))
def cg_f001_cash_and_equivalents_core136_2nd_v137_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_diff(_mean(_safe_div(cashneq, sharesbas), 4), 4), 8))
def cg_f001_cash_and_equivalents_core137_2nd_v138_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_diff(_mean(_safe_div(cashneq, capex.abs() + 1.0), 4), 4), 8))
def cg_f001_cash_and_equivalents_core138_2nd_v139_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_diff(_mean(_safe_div(cashneq, rnd.abs() + 1.0), 4), 4), 8))
def cg_f001_cash_and_equivalents_core139_2nd_v140_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_diff(_mean(_safe_div(cashneq, opex.abs() + 1.0), 4), 4), 8))

def cg_f001_cash_and_equivalents_core140_2nd_v141_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_slope(_mean(cashneq, 4), 4), 12))
def cg_f001_cash_and_equivalents_core141_2nd_v142_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_slope(_mean(_safe_div(cashneq, assets), 4), 4), 12))
def cg_f001_cash_and_equivalents_core142_2nd_v143_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_slope(_mean(_safe_div(cashneq, marketcap), 4), 4), 12))
def cg_f001_cash_and_equivalents_core143_2nd_v144_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_slope(_mean(_safe_div(cashneq, revenue), 4), 4), 12))
def cg_f001_cash_and_equivalents_core144_2nd_v145_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_slope(_mean(_safe_div(cashneq, liabilities), 4), 4), 12))
def cg_f001_cash_and_equivalents_core145_2nd_v146_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_slope(_mean(_safe_div(cashneq, debt), 4), 4), 12))
def cg_f001_cash_and_equivalents_core146_2nd_v147_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_slope(_mean(_safe_div(cashneq, sharesbas), 4), 4), 12))
def cg_f001_cash_and_equivalents_core147_2nd_v148_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_slope(_mean(_safe_div(cashneq, capex.abs() + 1.0), 4), 4), 12))
def cg_f001_cash_and_equivalents_core148_2nd_v149_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_slope(_mean(_safe_div(cashneq, rnd.abs() + 1.0), 4), 4), 12))
def cg_f001_cash_and_equivalents_core149_2nd_v150_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_slope(_mean(_safe_div(cashneq, opex.abs() + 1.0), 4), 4), 12))
