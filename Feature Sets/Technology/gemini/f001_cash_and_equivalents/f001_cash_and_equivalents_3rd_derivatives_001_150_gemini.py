import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f001_cash_and_equivalents_core00_3rd_v001_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_diff(cashneq, 4), 4))
def cg_f001_cash_and_equivalents_core01_3rd_v002_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_diff(_safe_div(cashneq, assets), 4), 4))
def cg_f001_cash_and_equivalents_core02_3rd_v003_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_diff(_safe_div(cashneq, marketcap), 4), 4))
def cg_f001_cash_and_equivalents_core03_3rd_v004_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_diff(_safe_div(cashneq, revenue), 4), 4))
def cg_f001_cash_and_equivalents_core04_3rd_v005_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_diff(_safe_div(cashneq, liabilities), 4), 4))
def cg_f001_cash_and_equivalents_core05_3rd_v006_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_diff(_safe_div(cashneq, debt), 4), 4))
def cg_f001_cash_and_equivalents_core06_3rd_v007_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_diff(_safe_div(cashneq, sharesbas), 4), 4))
def cg_f001_cash_and_equivalents_core07_3rd_v008_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_diff(_safe_div(cashneq, capex.abs() + 1.0), 4), 4))
def cg_f001_cash_and_equivalents_core08_3rd_v009_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_diff(_safe_div(cashneq, rnd.abs() + 1.0), 4), 4))
def cg_f001_cash_and_equivalents_core09_3rd_v010_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_diff(_safe_div(cashneq, opex.abs() + 1.0), 4), 4))

def cg_f001_cash_and_equivalents_core10_3rd_v011_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_diff(cashneq, 4), 8))
def cg_f001_cash_and_equivalents_core11_3rd_v012_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_diff(_safe_div(cashneq, assets), 4), 8))
def cg_f001_cash_and_equivalents_core12_3rd_v013_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_diff(_safe_div(cashneq, marketcap), 4), 8))
def cg_f001_cash_and_equivalents_core13_3rd_v014_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_diff(_safe_div(cashneq, revenue), 4), 8))
def cg_f001_cash_and_equivalents_core14_3rd_v015_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_diff(_safe_div(cashneq, liabilities), 4), 8))
def cg_f001_cash_and_equivalents_core15_3rd_v016_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_diff(_safe_div(cashneq, debt), 4), 8))
def cg_f001_cash_and_equivalents_core16_3rd_v017_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_diff(_safe_div(cashneq, sharesbas), 4), 8))
def cg_f001_cash_and_equivalents_core17_3rd_v018_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_diff(_safe_div(cashneq, capex.abs() + 1.0), 4), 8))
def cg_f001_cash_and_equivalents_core18_3rd_v019_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_diff(_safe_div(cashneq, rnd.abs() + 1.0), 4), 8))
def cg_f001_cash_and_equivalents_core19_3rd_v020_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_diff(_safe_div(cashneq, opex.abs() + 1.0), 4), 8))

def cg_f001_cash_and_equivalents_core20_3rd_v021_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_slope(cashneq, 4), 4))
def cg_f001_cash_and_equivalents_core21_3rd_v022_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_slope(_safe_div(cashneq, assets), 4), 4))
def cg_f001_cash_and_equivalents_core22_3rd_v023_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_slope(_safe_div(cashneq, marketcap), 4), 4))
def cg_f001_cash_and_equivalents_core23_3rd_v024_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_slope(_safe_div(cashneq, revenue), 4), 4))
def cg_f001_cash_and_equivalents_core24_3rd_v025_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_slope(_safe_div(cashneq, liabilities), 4), 4))
def cg_f001_cash_and_equivalents_core25_3rd_v026_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_slope(_safe_div(cashneq, debt), 4), 4))
def cg_f001_cash_and_equivalents_core26_3rd_v027_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_slope(_safe_div(cashneq, sharesbas), 4), 4))
def cg_f001_cash_and_equivalents_core27_3rd_v028_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_slope(_safe_div(cashneq, capex.abs() + 1.0), 4), 4))
def cg_f001_cash_and_equivalents_core28_3rd_v029_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_slope(_safe_div(cashneq, rnd.abs() + 1.0), 4), 4))
def cg_f001_cash_and_equivalents_core29_3rd_v030_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_slope(_safe_div(cashneq, opex.abs() + 1.0), 4), 4))

def cg_f001_cash_and_equivalents_core30_3rd_v031_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_diff(_diff(cashneq, 4), 4), 8))
def cg_f001_cash_and_equivalents_core31_3rd_v032_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_diff(_diff(_safe_div(cashneq, assets), 4), 4), 8))
def cg_f001_cash_and_equivalents_core32_3rd_v033_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_diff(_diff(_safe_div(cashneq, marketcap), 4), 4), 8))
def cg_f001_cash_and_equivalents_core33_3rd_v034_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_diff(_diff(_safe_div(cashneq, revenue), 4), 4), 8))
def cg_f001_cash_and_equivalents_core34_3rd_v035_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_diff(_diff(_safe_div(cashneq, liabilities), 4), 4), 8))
def cg_f001_cash_and_equivalents_core35_3rd_v036_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_diff(_diff(_safe_div(cashneq, debt), 4), 4), 8))
def cg_f001_cash_and_equivalents_core36_3rd_v037_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_diff(_diff(_safe_div(cashneq, sharesbas), 4), 4), 8))
def cg_f001_cash_and_equivalents_core37_3rd_v038_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_diff(_diff(_safe_div(cashneq, capex.abs() + 1.0), 4), 4), 8))
def cg_f001_cash_and_equivalents_core38_3rd_v039_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_diff(_diff(_safe_div(cashneq, rnd.abs() + 1.0), 4), 4), 8))
def cg_f001_cash_and_equivalents_core39_3rd_v040_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_diff(_diff(_safe_div(cashneq, opex.abs() + 1.0), 4), 4), 8))

def cg_f001_cash_and_equivalents_core40_3rd_v041_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_slope(_diff(cashneq, 4), 8), 12))
def cg_f001_cash_and_equivalents_core41_3rd_v042_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_slope(_diff(_safe_div(cashneq, assets), 4), 8), 12))
def cg_f001_cash_and_equivalents_core42_3rd_v043_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_slope(_diff(_safe_div(cashneq, marketcap), 4), 8), 12))
def cg_f001_cash_and_equivalents_core43_3rd_v044_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_slope(_diff(_safe_div(cashneq, revenue), 4), 8), 12))
def cg_f001_cash_and_equivalents_core44_3rd_v045_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_slope(_diff(_safe_div(cashneq, liabilities), 4), 8), 12))
def cg_f001_cash_and_equivalents_core45_3rd_v046_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_slope(_diff(_safe_div(cashneq, debt), 4), 8), 12))
def cg_f001_cash_and_equivalents_core46_3rd_v047_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_slope(_diff(_safe_div(cashneq, sharesbas), 4), 8), 12))
def cg_f001_cash_and_equivalents_core47_3rd_v048_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_slope(_diff(_safe_div(cashneq, capex.abs() + 1.0), 4), 8), 12))
def cg_f001_cash_and_equivalents_core48_3rd_v049_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_slope(_diff(_safe_div(cashneq, rnd.abs() + 1.0), 4), 8), 12))
def cg_f001_cash_and_equivalents_core49_3rd_v050_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_slope(_diff(_safe_div(cashneq, opex.abs() + 1.0), 4), 8), 12))

def cg_f001_cash_and_equivalents_core50_3rd_v051_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_diff(_slope(cashneq, 4), 4), 8))
def cg_f001_cash_and_equivalents_core51_3rd_v052_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_diff(_slope(_safe_div(cashneq, assets), 4), 4), 8))
def cg_f001_cash_and_equivalents_core52_3rd_v053_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_diff(_slope(_safe_div(cashneq, marketcap), 4), 4), 8))
def cg_f001_cash_and_equivalents_core53_3rd_v054_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_diff(_slope(_safe_div(cashneq, revenue), 4), 4), 8))
def cg_f001_cash_and_equivalents_core54_3rd_v055_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_diff(_slope(_safe_div(cashneq, liabilities), 4), 4), 8))
def cg_f001_cash_and_equivalents_core55_3rd_v056_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_diff(_slope(_safe_div(cashneq, debt), 4), 4), 8))
def cg_f001_cash_and_equivalents_core56_3rd_v057_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_diff(_slope(_safe_div(cashneq, sharesbas), 4), 4), 8))
def cg_f001_cash_and_equivalents_core57_3rd_v058_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_diff(_slope(_safe_div(cashneq, capex.abs() + 1.0), 4), 4), 8))
def cg_f001_cash_and_equivalents_core58_3rd_v059_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_diff(_slope(_safe_div(cashneq, rnd.abs() + 1.0), 4), 4), 8))
def cg_f001_cash_and_equivalents_core59_3rd_v060_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_diff(_slope(_safe_div(cashneq, opex.abs() + 1.0), 4), 4), 8))

def cg_f001_cash_and_equivalents_core60_3rd_v061_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_diff(_diff(cashneq, 4), 4), 12))
def cg_f001_cash_and_equivalents_core61_3rd_v062_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_diff(_diff(_safe_div(cashneq, assets), 4), 4), 12))
def cg_f001_cash_and_equivalents_core62_3rd_v063_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_diff(_diff(_safe_div(cashneq, marketcap), 4), 4), 12))
def cg_f001_cash_and_equivalents_core63_3rd_v064_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_diff(_diff(_safe_div(cashneq, revenue), 4), 4), 12))
def cg_f001_cash_and_equivalents_core64_3rd_v065_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_diff(_diff(_safe_div(cashneq, liabilities), 4), 4), 12))
def cg_f001_cash_and_equivalents_core65_3rd_v066_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_diff(_diff(_safe_div(cashneq, debt), 4), 4), 12))
def cg_f001_cash_and_equivalents_core66_3rd_v067_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_diff(_diff(_safe_div(cashneq, sharesbas), 4), 4), 12))
def cg_f001_cash_and_equivalents_core67_3rd_v068_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_diff(_diff(_safe_div(cashneq, capex.abs() + 1.0), 4), 4), 12))
def cg_f001_cash_and_equivalents_core68_3rd_v069_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_diff(_diff(_safe_div(cashneq, rnd.abs() + 1.0), 4), 4), 12))
def cg_f001_cash_and_equivalents_core69_3rd_v070_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_diff(_diff(_safe_div(cashneq, opex.abs() + 1.0), 4), 4), 12))

def cg_f001_cash_and_equivalents_core70_3rd_v071_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_slope(_diff(cashneq, 4), 8), 12))
def cg_f001_cash_and_equivalents_core71_3rd_v072_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_slope(_diff(_safe_div(cashneq, assets), 4), 8), 12))
def cg_f001_cash_and_equivalents_core72_3rd_v073_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_slope(_diff(_safe_div(cashneq, marketcap), 4), 8), 12))
def cg_f001_cash_and_equivalents_core73_3rd_v074_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_slope(_diff(_safe_div(cashneq, revenue), 4), 8), 12))
def cg_f001_cash_and_equivalents_core74_3rd_v075_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_slope(_diff(_safe_div(cashneq, liabilities), 4), 8), 12))
def cg_f001_cash_and_equivalents_core75_3rd_v076_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_slope(_diff(_safe_div(cashneq, debt), 4), 8), 12))
def cg_f001_cash_and_equivalents_core76_3rd_v077_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_slope(_diff(_safe_div(cashneq, sharesbas), 4), 8), 12))
def cg_f001_cash_and_equivalents_core77_3rd_v078_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_slope(_diff(_safe_div(cashneq, capex.abs() + 1.0), 4), 8), 12))
def cg_f001_cash_and_equivalents_core78_3rd_v079_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_slope(_diff(_safe_div(cashneq, rnd.abs() + 1.0), 4), 8), 12))
def cg_f001_cash_and_equivalents_core79_3rd_v080_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_slope(_diff(_safe_div(cashneq, opex.abs() + 1.0), 4), 8), 12))

def cg_f001_cash_and_equivalents_core80_3rd_v081_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_diff(_slope(cashneq, 4), 4), 12))
def cg_f001_cash_and_equivalents_core81_3rd_v082_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_diff(_slope(_safe_div(cashneq, assets), 4), 4), 12))
def cg_f001_cash_and_equivalents_core82_3rd_v083_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_diff(_slope(_safe_div(cashneq, marketcap), 4), 4), 12))
def cg_f001_cash_and_equivalents_core83_3rd_v084_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_diff(_slope(_safe_div(cashneq, revenue), 4), 4), 12))
def cg_f001_cash_and_equivalents_core84_3rd_v085_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_diff(_slope(_safe_div(cashneq, liabilities), 4), 4), 12))
def cg_f001_cash_and_equivalents_core85_3rd_v086_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_diff(_slope(_safe_div(cashneq, debt), 4), 4), 12))
def cg_f001_cash_and_equivalents_core86_3rd_v087_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_diff(_slope(_safe_div(cashneq, sharesbas), 4), 4), 12))
def cg_f001_cash_and_equivalents_core87_3rd_v088_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_diff(_slope(_safe_div(cashneq, capex.abs() + 1.0), 4), 4), 12))
def cg_f001_cash_and_equivalents_core88_3rd_v089_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_diff(_slope(_safe_div(cashneq, rnd.abs() + 1.0), 4), 4), 12))
def cg_f001_cash_and_equivalents_core89_3rd_v090_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_rank(_diff(_slope(_safe_div(cashneq, opex.abs() + 1.0), 4), 4), 12))

def cg_f001_cash_and_equivalents_core90_3rd_v091_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_diff(_diff(cashneq, 4), 4), 4))
def cg_f001_cash_and_equivalents_core91_3rd_v092_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_diff(_diff(_safe_div(cashneq, assets), 4), 4), 4))
def cg_f001_cash_and_equivalents_core92_3rd_v093_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_diff(_diff(_safe_div(cashneq, marketcap), 4), 4), 4))
def cg_f001_cash_and_equivalents_core93_3rd_v094_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_diff(_diff(_safe_div(cashneq, revenue), 4), 4), 4))
def cg_f001_cash_and_equivalents_core94_3rd_v095_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_diff(_diff(_safe_div(cashneq, liabilities), 4), 4), 4))
def cg_f001_cash_and_equivalents_core95_3rd_v096_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_diff(_diff(_safe_div(cashneq, debt), 4), 4), 4))
def cg_f001_cash_and_equivalents_core96_3rd_v097_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_diff(_diff(_safe_div(cashneq, sharesbas), 4), 4), 4))
def cg_f001_cash_and_equivalents_core97_3rd_v098_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_diff(_diff(_safe_div(cashneq, capex.abs() + 1.0), 4), 4), 4))
def cg_f001_cash_and_equivalents_core98_3rd_v099_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_diff(_diff(_safe_div(cashneq, rnd.abs() + 1.0), 4), 4), 4))
def cg_f001_cash_and_equivalents_core99_3rd_v100_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_diff(_diff(_safe_div(cashneq, opex.abs() + 1.0), 4), 4), 4))

def cg_f001_cash_and_equivalents_core100_3rd_v101_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_slope(_diff(cashneq, 4), 8), 4))
def cg_f001_cash_and_equivalents_core101_3rd_v102_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_slope(_diff(_safe_div(cashneq, assets), 4), 8), 4))
def cg_f001_cash_and_equivalents_core102_3rd_v103_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_slope(_diff(_safe_div(cashneq, marketcap), 4), 8), 4))
def cg_f001_cash_and_equivalents_core103_3rd_v104_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_slope(_diff(_safe_div(cashneq, revenue), 4), 8), 4))
def cg_f001_cash_and_equivalents_core104_3rd_v105_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_slope(_diff(_safe_div(cashneq, liabilities), 4), 8), 4))
def cg_f001_cash_and_equivalents_core105_3rd_v106_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_slope(_diff(_safe_div(cashneq, debt), 4), 8), 4))
def cg_f001_cash_and_equivalents_core106_3rd_v107_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_slope(_diff(_safe_div(cashneq, sharesbas), 4), 8), 4))
def cg_f001_cash_and_equivalents_core107_3rd_v108_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_slope(_diff(_safe_div(cashneq, capex.abs() + 1.0), 4), 8), 4))
def cg_f001_cash_and_equivalents_core108_3rd_v109_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_slope(_diff(_safe_div(cashneq, rnd.abs() + 1.0), 4), 8), 4))
def cg_f001_cash_and_equivalents_core109_3rd_v110_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_slope(_diff(_safe_div(cashneq, opex.abs() + 1.0), 4), 8), 4))

def cg_f001_cash_and_equivalents_core110_3rd_v111_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_diff(_slope(cashneq, 4), 4), 4))
def cg_f001_cash_and_equivalents_core111_3rd_v112_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_diff(_slope(_safe_div(cashneq, assets), 4), 4), 4))
def cg_f001_cash_and_equivalents_core112_3rd_v113_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_diff(_slope(_safe_div(cashneq, marketcap), 4), 4), 4))
def cg_f001_cash_and_equivalents_core113_3rd_v114_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_diff(_slope(_safe_div(cashneq, revenue), 4), 4), 4))
def cg_f001_cash_and_equivalents_core114_3rd_v115_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_diff(_slope(_safe_div(cashneq, liabilities), 4), 4), 4))
def cg_f001_cash_and_equivalents_core115_3rd_v116_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_diff(_slope(_safe_div(cashneq, debt), 4), 4), 4))
def cg_f001_cash_and_equivalents_core116_3rd_v117_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_diff(_slope(_safe_div(cashneq, sharesbas), 4), 4), 4))
def cg_f001_cash_and_equivalents_core117_3rd_v118_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_diff(_slope(_safe_div(cashneq, capex.abs() + 1.0), 4), 4), 4))
def cg_f001_cash_and_equivalents_core118_3rd_v119_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_diff(_slope(_safe_div(cashneq, rnd.abs() + 1.0), 4), 4), 4))
def cg_f001_cash_and_equivalents_core119_3rd_v120_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_mean(_diff(_slope(_safe_div(cashneq, opex.abs() + 1.0), 4), 4), 4))

def cg_f001_cash_and_equivalents_core120_3rd_v121_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_diff(_diff(cashneq, 4), 4), 4))
def cg_f001_cash_and_equivalents_core121_3rd_v122_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_diff(_diff(_safe_div(cashneq, assets), 4), 4), 4))
def cg_f001_cash_and_equivalents_core122_3rd_v123_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_diff(_diff(_safe_div(cashneq, marketcap), 4), 4), 4))
def cg_f001_cash_and_equivalents_core123_3rd_v124_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_diff(_diff(_safe_div(cashneq, revenue), 4), 4), 4))
def cg_f001_cash_and_equivalents_core124_3rd_v125_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_diff(_diff(_safe_div(cashneq, liabilities), 4), 4), 4))
def cg_f001_cash_and_equivalents_core125_3rd_v126_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_diff(_diff(_safe_div(cashneq, debt), 4), 4), 4))
def cg_f001_cash_and_equivalents_core126_3rd_v127_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_diff(_diff(_safe_div(cashneq, sharesbas), 4), 4), 4))
def cg_f001_cash_and_equivalents_core127_3rd_v128_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_diff(_diff(_safe_div(cashneq, capex.abs() + 1.0), 4), 4), 4))
def cg_f001_cash_and_equivalents_core128_3rd_v129_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_diff(_diff(_safe_div(cashneq, rnd.abs() + 1.0), 4), 4), 4))
def cg_f001_cash_and_equivalents_core129_3rd_v130_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_diff(_diff(_safe_div(cashneq, opex.abs() + 1.0), 4), 4), 4))

def cg_f001_cash_and_equivalents_core130_3rd_v131_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_diff(_diff(cashneq, 4), 4), 4))
def cg_f001_cash_and_equivalents_core131_3rd_v132_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_diff(_diff(_safe_div(cashneq, assets), 4), 4), 4))
def cg_f001_cash_and_equivalents_core132_3rd_v133_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_diff(_diff(_safe_div(cashneq, marketcap), 4), 4), 4))
def cg_f001_cash_and_equivalents_core133_3rd_v134_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_diff(_diff(_safe_div(cashneq, revenue), 4), 4), 4))
def cg_f001_cash_and_equivalents_core134_3rd_v135_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_diff(_diff(_safe_div(cashneq, liabilities), 4), 4), 4))
def cg_f001_cash_and_equivalents_core135_3rd_v136_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_diff(_diff(_safe_div(cashneq, debt), 4), 4), 4))
def cg_f001_cash_and_equivalents_core136_3rd_v137_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_diff(_diff(_safe_div(cashneq, sharesbas), 4), 4), 4))
def cg_f001_cash_and_equivalents_core137_3rd_v138_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_diff(_diff(_safe_div(cashneq, capex.abs() + 1.0), 4), 4), 4))
def cg_f001_cash_and_equivalents_core138_3rd_v139_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_diff(_diff(_safe_div(cashneq, rnd.abs() + 1.0), 4), 4), 4))
def cg_f001_cash_and_equivalents_core139_3rd_v140_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_diff(_diff(_safe_div(cashneq, opex.abs() + 1.0), 4), 4), 4))

def cg_f001_cash_and_equivalents_core140_3rd_v141_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_slope(_diff(_diff(cashneq, 4), 4), 4), 8))
def cg_f001_cash_and_equivalents_core141_3rd_v142_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_slope(_diff(_diff(_safe_div(cashneq, assets), 4), 4), 4), 8))
def cg_f001_cash_and_equivalents_core142_3rd_v143_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_slope(_diff(_diff(_safe_div(cashneq, marketcap), 4), 4), 4), 8))
def cg_f001_cash_and_equivalents_core143_3rd_v144_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_slope(_diff(_diff(_safe_div(cashneq, revenue), 4), 4), 4), 8))
def cg_f001_cash_and_equivalents_core144_3rd_v145_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_slope(_diff(_diff(_safe_div(cashneq, liabilities), 4), 4), 4), 8))
def cg_f001_cash_and_equivalents_core145_3rd_v146_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_slope(_diff(_diff(_safe_div(cashneq, debt), 4), 4), 4), 8))
def cg_f001_cash_and_equivalents_core146_3rd_v147_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_slope(_diff(_diff(_safe_div(cashneq, sharesbas), 4), 4), 4), 8))
def cg_f001_cash_and_equivalents_core147_3rd_v148_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_slope(_diff(_diff(_safe_div(cashneq, capex.abs() + 1.0), 4), 4), 4), 8))
def cg_f001_cash_and_equivalents_core148_3rd_v149_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_slope(_diff(_diff(_safe_div(cashneq, rnd.abs() + 1.0), 4), 4), 4), 8))
def cg_f001_cash_and_equivalents_core149_3rd_v150_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_z(_slope(_diff(_diff(_safe_div(cashneq, opex.abs() + 1.0), 4), 4), 4), 8))
