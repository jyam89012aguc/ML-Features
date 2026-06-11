import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f094_insider_ownership_after_trade_core00_2nd_v001_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(sharesownedfollowingtransaction, 4))
def cg_f094_insider_ownership_after_trade_core01_2nd_v002_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(transactionshares, 4))
def cg_f094_insider_ownership_after_trade_core02_2nd_v003_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(sharesownedbeforetransaction, 4))
def cg_f094_insider_ownership_after_trade_core03_2nd_v004_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(sharesownedfollowingtransaction - sharesownedbeforetransaction, 4))
def cg_f094_insider_ownership_after_trade_core04_2nd_v005_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(_safe_div(transactionshares, sharesownedbeforetransaction.abs() + 1.0), 4))
def cg_f094_insider_ownership_after_trade_core05_2nd_v006_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(_safe_div(sharesownedfollowingtransaction, sharesownedbeforetransaction.abs() + 1.0), 4))
def cg_f094_insider_ownership_after_trade_core06_2nd_v007_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(_log(sharesownedfollowingtransaction.abs() + 1.0), 4))
def cg_f094_insider_ownership_after_trade_core07_2nd_v008_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(_log(transactionshares.abs() + 1.0), 4))
def cg_f094_insider_ownership_after_trade_core08_2nd_v009_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(_log(sharesownedbeforetransaction.abs() + 1.0), 4))
def cg_f094_insider_ownership_after_trade_core09_2nd_v010_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(transactionshares.abs(), 4))
def cg_f094_insider_ownership_after_trade_core10_2nd_v011_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(sharesownedfollowingtransaction, 8))
def cg_f094_insider_ownership_after_trade_core11_2nd_v012_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(transactionshares, 8))
def cg_f094_insider_ownership_after_trade_core12_2nd_v013_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(sharesownedbeforetransaction, 8))
def cg_f094_insider_ownership_after_trade_core13_2nd_v014_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(sharesownedfollowingtransaction - sharesownedbeforetransaction, 8))
def cg_f094_insider_ownership_after_trade_core14_2nd_v015_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(_safe_div(transactionshares, sharesownedbeforetransaction.abs() + 1.0), 8))
def cg_f094_insider_ownership_after_trade_core15_2nd_v016_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(_safe_div(sharesownedfollowingtransaction, sharesownedbeforetransaction.abs() + 1.0), 8))
def cg_f094_insider_ownership_after_trade_core16_2nd_v017_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(_log(sharesownedfollowingtransaction.abs() + 1.0), 8))
def cg_f094_insider_ownership_after_trade_core17_2nd_v018_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(_log(transactionshares.abs() + 1.0), 8))
def cg_f094_insider_ownership_after_trade_core18_2nd_v019_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(_log(sharesownedbeforetransaction.abs() + 1.0), 8))
def cg_f094_insider_ownership_after_trade_core19_2nd_v020_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(transactionshares.abs(), 8))
def cg_f094_insider_ownership_after_trade_core20_2nd_v021_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_diff(sharesownedfollowingtransaction, 4))
def cg_f094_insider_ownership_after_trade_core21_2nd_v022_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_diff(transactionshares, 4))
def cg_f094_insider_ownership_after_trade_core22_2nd_v023_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_diff(sharesownedbeforetransaction, 4))
def cg_f094_insider_ownership_after_trade_core23_2nd_v024_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_diff(sharesownedfollowingtransaction - sharesownedbeforetransaction, 4))
def cg_f094_insider_ownership_after_trade_core24_2nd_v025_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_diff(_safe_div(transactionshares, sharesownedbeforetransaction.abs() + 1.0), 4))
def cg_f094_insider_ownership_after_trade_core25_2nd_v026_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_diff(_safe_div(sharesownedfollowingtransaction, sharesownedbeforetransaction.abs() + 1.0), 4))
def cg_f094_insider_ownership_after_trade_core26_2nd_v027_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_diff(_log(sharesownedfollowingtransaction.abs() + 1.0), 4))
def cg_f094_insider_ownership_after_trade_core27_2nd_v028_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_diff(_log(transactionshares.abs() + 1.0), 4))
def cg_f094_insider_ownership_after_trade_core28_2nd_v029_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_diff(_log(sharesownedbeforetransaction.abs() + 1.0), 4))
def cg_f094_insider_ownership_after_trade_core29_2nd_v030_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_diff(transactionshares.abs(), 4))
def cg_f094_insider_ownership_after_trade_core30_2nd_v031_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_slope(sharesownedfollowingtransaction, 4), 8))
def cg_f094_insider_ownership_after_trade_core31_2nd_v032_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_slope(transactionshares, 4), 8))
def cg_f094_insider_ownership_after_trade_core32_2nd_v033_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_slope(sharesownedbeforetransaction, 4), 8))
def cg_f094_insider_ownership_after_trade_core33_2nd_v034_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_slope(sharesownedfollowingtransaction - sharesownedbeforetransaction, 4), 8))
def cg_f094_insider_ownership_after_trade_core34_2nd_v035_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_slope(_safe_div(transactionshares, sharesownedbeforetransaction.abs() + 1.0), 4), 8))
def cg_f094_insider_ownership_after_trade_core35_2nd_v036_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_slope(_safe_div(sharesownedfollowingtransaction, sharesownedbeforetransaction.abs() + 1.0), 4), 8))
def cg_f094_insider_ownership_after_trade_core36_2nd_v037_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_slope(_log(sharesownedfollowingtransaction.abs() + 1.0), 4), 8))
def cg_f094_insider_ownership_after_trade_core37_2nd_v038_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_slope(_log(transactionshares.abs() + 1.0), 4), 8))
def cg_f094_insider_ownership_after_trade_core38_2nd_v039_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_slope(_log(sharesownedbeforetransaction.abs() + 1.0), 4), 8))
def cg_f094_insider_ownership_after_trade_core39_2nd_v040_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_slope(transactionshares.abs(), 4), 8))
def cg_f094_insider_ownership_after_trade_core40_2nd_v041_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_slope(sharesownedfollowingtransaction, 8), 12))
def cg_f094_insider_ownership_after_trade_core41_2nd_v042_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_slope(transactionshares, 8), 12))
def cg_f094_insider_ownership_after_trade_core42_2nd_v043_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_slope(sharesownedbeforetransaction, 8), 12))
def cg_f094_insider_ownership_after_trade_core43_2nd_v044_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_slope(sharesownedfollowingtransaction - sharesownedbeforetransaction, 8), 12))
def cg_f094_insider_ownership_after_trade_core44_2nd_v045_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_slope(_safe_div(transactionshares, sharesownedbeforetransaction.abs() + 1.0), 8), 12))
def cg_f094_insider_ownership_after_trade_core45_2nd_v046_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_slope(_safe_div(sharesownedfollowingtransaction, sharesownedbeforetransaction.abs() + 1.0), 8), 12))
def cg_f094_insider_ownership_after_trade_core46_2nd_v047_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_slope(_log(sharesownedfollowingtransaction.abs() + 1.0), 8), 12))
def cg_f094_insider_ownership_after_trade_core47_2nd_v048_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_slope(_log(transactionshares.abs() + 1.0), 8), 12))
def cg_f094_insider_ownership_after_trade_core48_2nd_v049_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_slope(_log(sharesownedbeforetransaction.abs() + 1.0), 8), 12))
def cg_f094_insider_ownership_after_trade_core49_2nd_v050_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_slope(transactionshares.abs(), 8), 12))
def cg_f094_insider_ownership_after_trade_core50_2nd_v051_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_diff(sharesownedfollowingtransaction, 4), 8))
def cg_f094_insider_ownership_after_trade_core51_2nd_v052_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_diff(transactionshares, 4), 8))
def cg_f094_insider_ownership_after_trade_core52_2nd_v053_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_diff(sharesownedbeforetransaction, 4), 8))
def cg_f094_insider_ownership_after_trade_core53_2nd_v054_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_diff(sharesownedfollowingtransaction - sharesownedbeforetransaction, 4), 8))
def cg_f094_insider_ownership_after_trade_core54_2nd_v055_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_diff(_safe_div(transactionshares, sharesownedbeforetransaction.abs() + 1.0), 4), 8))
def cg_f094_insider_ownership_after_trade_core55_2nd_v056_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_diff(_safe_div(sharesownedfollowingtransaction, sharesownedbeforetransaction.abs() + 1.0), 4), 8))
def cg_f094_insider_ownership_after_trade_core56_2nd_v057_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_diff(_log(sharesownedfollowingtransaction.abs() + 1.0), 4), 8))
def cg_f094_insider_ownership_after_trade_core57_2nd_v058_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_diff(_log(transactionshares.abs() + 1.0), 4), 8))
def cg_f094_insider_ownership_after_trade_core58_2nd_v059_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_diff(_log(sharesownedbeforetransaction.abs() + 1.0), 4), 8))
def cg_f094_insider_ownership_after_trade_core59_2nd_v060_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_diff(transactionshares.abs(), 4), 8))
def cg_f094_insider_ownership_after_trade_core60_2nd_v061_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_rank(_slope(sharesownedfollowingtransaction, 4), 12))
def cg_f094_insider_ownership_after_trade_core61_2nd_v062_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_rank(_slope(transactionshares, 4), 12))
def cg_f094_insider_ownership_after_trade_core62_2nd_v063_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_rank(_slope(sharesownedbeforetransaction, 4), 12))
def cg_f094_insider_ownership_after_trade_core63_2nd_v064_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_rank(_slope(sharesownedfollowingtransaction - sharesownedbeforetransaction, 4), 12))
def cg_f094_insider_ownership_after_trade_core64_2nd_v065_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_rank(_slope(_safe_div(transactionshares, sharesownedbeforetransaction.abs() + 1.0), 4), 12))
def cg_f094_insider_ownership_after_trade_core65_2nd_v066_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_rank(_slope(_safe_div(sharesownedfollowingtransaction, sharesownedbeforetransaction.abs() + 1.0), 4), 12))
def cg_f094_insider_ownership_after_trade_core66_2nd_v067_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_rank(_slope(_log(sharesownedfollowingtransaction.abs() + 1.0), 4), 12))
def cg_f094_insider_ownership_after_trade_core67_2nd_v068_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_rank(_slope(_log(transactionshares.abs() + 1.0), 4), 12))
def cg_f094_insider_ownership_after_trade_core68_2nd_v069_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_rank(_slope(_log(sharesownedbeforetransaction.abs() + 1.0), 4), 12))
def cg_f094_insider_ownership_after_trade_core69_2nd_v070_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_rank(_slope(transactionshares.abs(), 4), 12))
def cg_f094_insider_ownership_after_trade_core70_2nd_v071_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_rank(_diff(sharesownedfollowingtransaction, 4), 12))
def cg_f094_insider_ownership_after_trade_core71_2nd_v072_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_rank(_diff(transactionshares, 4), 12))
def cg_f094_insider_ownership_after_trade_core72_2nd_v073_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_rank(_diff(sharesownedbeforetransaction, 4), 12))
def cg_f094_insider_ownership_after_trade_core73_2nd_v074_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_rank(_diff(sharesownedfollowingtransaction - sharesownedbeforetransaction, 4), 12))
def cg_f094_insider_ownership_after_trade_core74_2nd_v075_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_rank(_diff(_safe_div(transactionshares, sharesownedbeforetransaction.abs() + 1.0), 4), 12))
def cg_f094_insider_ownership_after_trade_core75_2nd_v076_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_rank(_diff(_safe_div(sharesownedfollowingtransaction, sharesownedbeforetransaction.abs() + 1.0), 4), 12))
def cg_f094_insider_ownership_after_trade_core76_2nd_v077_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_rank(_diff(_log(sharesownedfollowingtransaction.abs() + 1.0), 4), 12))
def cg_f094_insider_ownership_after_trade_core77_2nd_v078_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_rank(_diff(_log(transactionshares.abs() + 1.0), 4), 12))
def cg_f094_insider_ownership_after_trade_core78_2nd_v079_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_rank(_diff(_log(sharesownedbeforetransaction.abs() + 1.0), 4), 12))
def cg_f094_insider_ownership_after_trade_core79_2nd_v080_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_rank(_diff(transactionshares.abs(), 4), 12))
def cg_f094_insider_ownership_after_trade_core80_2nd_v081_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_mean(_slope(sharesownedfollowingtransaction, 4), 4))
def cg_f094_insider_ownership_after_trade_core81_2nd_v082_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_mean(_slope(transactionshares, 4), 4))
def cg_f094_insider_ownership_after_trade_core82_2nd_v083_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_mean(_slope(sharesownedbeforetransaction, 4), 4))
def cg_f094_insider_ownership_after_trade_core83_2nd_v084_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_mean(_slope(sharesownedfollowingtransaction - sharesownedbeforetransaction, 4), 4))
def cg_f094_insider_ownership_after_trade_core84_2nd_v085_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_mean(_slope(_safe_div(transactionshares, sharesownedbeforetransaction.abs() + 1.0), 4), 4))
def cg_f094_insider_ownership_after_trade_core85_2nd_v086_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_mean(_slope(_safe_div(sharesownedfollowingtransaction, sharesownedbeforetransaction.abs() + 1.0), 4), 4))
def cg_f094_insider_ownership_after_trade_core86_2nd_v087_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_mean(_slope(_log(sharesownedfollowingtransaction.abs() + 1.0), 4), 4))
def cg_f094_insider_ownership_after_trade_core87_2nd_v088_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_mean(_slope(_log(transactionshares.abs() + 1.0), 4), 4))
def cg_f094_insider_ownership_after_trade_core88_2nd_v089_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_mean(_slope(_log(sharesownedbeforetransaction.abs() + 1.0), 4), 4))
def cg_f094_insider_ownership_after_trade_core89_2nd_v090_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_mean(_slope(transactionshares.abs(), 4), 4))
def cg_f094_insider_ownership_after_trade_core90_2nd_v091_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_mean(_diff(sharesownedfollowingtransaction, 4), 4))
def cg_f094_insider_ownership_after_trade_core91_2nd_v092_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_mean(_diff(transactionshares, 4), 4))
def cg_f094_insider_ownership_after_trade_core92_2nd_v093_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_mean(_diff(sharesownedbeforetransaction, 4), 4))
def cg_f094_insider_ownership_after_trade_core93_2nd_v094_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_mean(_diff(sharesownedfollowingtransaction - sharesownedbeforetransaction, 4), 4))
def cg_f094_insider_ownership_after_trade_core94_2nd_v095_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_mean(_diff(_safe_div(transactionshares, sharesownedbeforetransaction.abs() + 1.0), 4), 4))
def cg_f094_insider_ownership_after_trade_core95_2nd_v096_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_mean(_diff(_safe_div(sharesownedfollowingtransaction, sharesownedbeforetransaction.abs() + 1.0), 4), 4))
def cg_f094_insider_ownership_after_trade_core96_2nd_v097_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_mean(_diff(_log(sharesownedfollowingtransaction.abs() + 1.0), 4), 4))
def cg_f094_insider_ownership_after_trade_core97_2nd_v098_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_mean(_diff(_log(transactionshares.abs() + 1.0), 4), 4))
def cg_f094_insider_ownership_after_trade_core98_2nd_v099_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_mean(_diff(_log(sharesownedbeforetransaction.abs() + 1.0), 4), 4))
def cg_f094_insider_ownership_after_trade_core99_2nd_v100_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_mean(_diff(transactionshares.abs(), 4), 4))
def cg_f094_insider_ownership_after_trade_core100_2nd_v101_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(_mean(sharesownedfollowingtransaction, 4), 4))
def cg_f094_insider_ownership_after_trade_core101_2nd_v102_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(_mean(transactionshares, 4), 4))
def cg_f094_insider_ownership_after_trade_core102_2nd_v103_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(_mean(sharesownedbeforetransaction, 4), 4))
def cg_f094_insider_ownership_after_trade_core103_2nd_v104_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(_mean(sharesownedfollowingtransaction - sharesownedbeforetransaction, 4), 4))
def cg_f094_insider_ownership_after_trade_core104_2nd_v105_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(_mean(_safe_div(transactionshares, sharesownedbeforetransaction.abs() + 1.0), 4), 4))
def cg_f094_insider_ownership_after_trade_core105_2nd_v106_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(_mean(_safe_div(sharesownedfollowingtransaction, sharesownedbeforetransaction.abs() + 1.0), 4), 4))
def cg_f094_insider_ownership_after_trade_core106_2nd_v107_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(_mean(_log(sharesownedfollowingtransaction.abs() + 1.0), 4), 4))
def cg_f094_insider_ownership_after_trade_core107_2nd_v108_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(_mean(_log(transactionshares.abs() + 1.0), 4), 4))
def cg_f094_insider_ownership_after_trade_core108_2nd_v109_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(_mean(_log(sharesownedbeforetransaction.abs() + 1.0), 4), 4))
def cg_f094_insider_ownership_after_trade_core109_2nd_v110_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(_mean(transactionshares.abs(), 4), 4))
def cg_f094_insider_ownership_after_trade_core110_2nd_v111_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(_mean(sharesownedfollowingtransaction, 8), 8))
def cg_f094_insider_ownership_after_trade_core111_2nd_v112_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(_mean(transactionshares, 8), 8))
def cg_f094_insider_ownership_after_trade_core112_2nd_v113_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(_mean(sharesownedbeforetransaction, 8), 8))
def cg_f094_insider_ownership_after_trade_core113_2nd_v114_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(_mean(sharesownedfollowingtransaction - sharesownedbeforetransaction, 8), 8))
def cg_f094_insider_ownership_after_trade_core114_2nd_v115_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(_mean(_safe_div(transactionshares, sharesownedbeforetransaction.abs() + 1.0), 8), 8))
def cg_f094_insider_ownership_after_trade_core115_2nd_v116_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(_mean(_safe_div(sharesownedfollowingtransaction, sharesownedbeforetransaction.abs() + 1.0), 8), 8))
def cg_f094_insider_ownership_after_trade_core116_2nd_v117_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(_mean(_log(sharesownedfollowingtransaction.abs() + 1.0), 8), 8))
def cg_f094_insider_ownership_after_trade_core117_2nd_v118_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(_mean(_log(transactionshares.abs() + 1.0), 8), 8))
def cg_f094_insider_ownership_after_trade_core118_2nd_v119_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(_mean(_log(sharesownedbeforetransaction.abs() + 1.0), 8), 8))
def cg_f094_insider_ownership_after_trade_core119_2nd_v120_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_slope(_mean(transactionshares.abs(), 8), 8))
def cg_f094_insider_ownership_after_trade_core120_2nd_v121_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_diff(_mean(sharesownedfollowingtransaction, 4), 4))
def cg_f094_insider_ownership_after_trade_core121_2nd_v122_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_diff(_mean(transactionshares, 4), 4))
def cg_f094_insider_ownership_after_trade_core122_2nd_v123_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_diff(_mean(sharesownedbeforetransaction, 4), 4))
def cg_f094_insider_ownership_after_trade_core123_2nd_v124_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_diff(_mean(sharesownedfollowingtransaction - sharesownedbeforetransaction, 4), 4))
def cg_f094_insider_ownership_after_trade_core124_2nd_v125_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_diff(_mean(_safe_div(transactionshares, sharesownedbeforetransaction.abs() + 1.0), 4), 4))
def cg_f094_insider_ownership_after_trade_core125_2nd_v126_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_diff(_mean(_safe_div(sharesownedfollowingtransaction, sharesownedbeforetransaction.abs() + 1.0), 4), 4))
def cg_f094_insider_ownership_after_trade_core126_2nd_v127_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_diff(_mean(_log(sharesownedfollowingtransaction.abs() + 1.0), 4), 4))
def cg_f094_insider_ownership_after_trade_core127_2nd_v128_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_diff(_mean(_log(transactionshares.abs() + 1.0), 4), 4))
def cg_f094_insider_ownership_after_trade_core128_2nd_v129_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_diff(_mean(_log(sharesownedbeforetransaction.abs() + 1.0), 4), 4))
def cg_f094_insider_ownership_after_trade_core129_2nd_v130_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_diff(_mean(transactionshares.abs(), 4), 4))
def cg_f094_insider_ownership_after_trade_core130_2nd_v131_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_diff(_mean(sharesownedfollowingtransaction, 4), 4), 8))
def cg_f094_insider_ownership_after_trade_core131_2nd_v132_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_diff(_mean(transactionshares, 4), 4), 8))
def cg_f094_insider_ownership_after_trade_core132_2nd_v133_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_diff(_mean(sharesownedbeforetransaction, 4), 4), 8))
def cg_f094_insider_ownership_after_trade_core133_2nd_v134_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_diff(_mean(sharesownedfollowingtransaction - sharesownedbeforetransaction, 4), 4), 8))
def cg_f094_insider_ownership_after_trade_core134_2nd_v135_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_diff(_mean(_safe_div(transactionshares, sharesownedbeforetransaction.abs() + 1.0), 4), 4), 8))
def cg_f094_insider_ownership_after_trade_core135_2nd_v136_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_diff(_mean(_safe_div(sharesownedfollowingtransaction, sharesownedbeforetransaction.abs() + 1.0), 4), 4), 8))
def cg_f094_insider_ownership_after_trade_core136_2nd_v137_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_diff(_mean(_log(sharesownedfollowingtransaction.abs() + 1.0), 4), 4), 8))
def cg_f094_insider_ownership_after_trade_core137_2nd_v138_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_diff(_mean(_log(transactionshares.abs() + 1.0), 4), 4), 8))
def cg_f094_insider_ownership_after_trade_core138_2nd_v139_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_diff(_mean(_log(sharesownedbeforetransaction.abs() + 1.0), 4), 4), 8))
def cg_f094_insider_ownership_after_trade_core139_2nd_v140_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_z(_diff(_mean(transactionshares.abs(), 4), 4), 8))
def cg_f094_insider_ownership_after_trade_core140_2nd_v141_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_rank(_slope(_mean(sharesownedfollowingtransaction, 4), 4), 12))
def cg_f094_insider_ownership_after_trade_core141_2nd_v142_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_rank(_slope(_mean(transactionshares, 4), 4), 12))
def cg_f094_insider_ownership_after_trade_core142_2nd_v143_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_rank(_slope(_mean(sharesownedbeforetransaction, 4), 4), 12))
def cg_f094_insider_ownership_after_trade_core143_2nd_v144_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_rank(_slope(_mean(sharesownedfollowingtransaction - sharesownedbeforetransaction, 4), 4), 12))
def cg_f094_insider_ownership_after_trade_core144_2nd_v145_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_rank(_slope(_mean(_safe_div(transactionshares, sharesownedbeforetransaction.abs() + 1.0), 4), 4), 12))
def cg_f094_insider_ownership_after_trade_core145_2nd_v146_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_rank(_slope(_mean(_safe_div(sharesownedfollowingtransaction, sharesownedbeforetransaction.abs() + 1.0), 4), 4), 12))
def cg_f094_insider_ownership_after_trade_core146_2nd_v147_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_rank(_slope(_mean(_log(sharesownedfollowingtransaction.abs() + 1.0), 4), 4), 12))
def cg_f094_insider_ownership_after_trade_core147_2nd_v148_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_rank(_slope(_mean(_log(transactionshares.abs() + 1.0), 4), 4), 12))
def cg_f094_insider_ownership_after_trade_core148_2nd_v149_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_rank(_slope(_mean(_log(sharesownedbeforetransaction.abs() + 1.0), 4), 4), 12))
def cg_f094_insider_ownership_after_trade_core149_2nd_v150_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_rank(_slope(_mean(transactionshares.abs(), 4), 4), 12))